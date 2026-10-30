"""NEI 18-04 Rev. 1 (August 2019), "Risk-Informed Performance-Based Technology Inclusive Guidance for Non-Light
Water Reactor Licensing Basis Development" — document profile for scripts/clean_references.py.

Spec: meta/references_cleanup/file_reviews/review_nei.md (§1 F01–F40, §2 table log, §3 figures, §4 outline,
§5.2 ordered rules R0–R9, §5.3 do-not-fix list). Inputs: the main opendataloader JSON (reading order, prose) and the
use_struct_tree JSON (`<stem>.structtree.json`, correct table cells) in references/raw/.

Order of steps (see steps()):
  labels -> noise -> TOC -> figures -> tables -> headings -> footnotes -> page-break joins -> lists
  -> subscripts / sign-lost exponents / PDF hyphen supplement -> core text normalisation -> post fixes.
"""
import collections
import copy
import json
import os
import re

import fitz

from .. import structure as S
from .. import tables as T
from ..doc import El, elements_from_json
from ..figures import odl_to_visible, render_png
from ..pdfaux import HeadingRef

KEY = "NEI_18-04"
BODY_OFFSET = 8                       # printed body page = PDF page - 8 (PDF p9 = printed 1)
FRONT_LABELS = {2: "ii", 3: "iii", 4: "iv", 5: "v", 6: "vi", 7: "vii", 8: "viii"}
FOOTER_RE = re.compile(r"^©\s*NEI 2019\. All rights reserved\.\s*nei\.org(?:\s+(\S+))?$")
NOISE_TEXTS = {"August 2019", "THIS PAGE INTENTIONALLY BLANK", "SEE TABLES FOLLOWING PAGES"}
FRONT_HEADINGS = {"NOTICE", "ABSTRACT", "LIST OF ACRONYMS"}
TERMINAL = tuple('.:;?!”")')
BULLET_RE = re.compile(r"^\s*(?:[•●▪■◦]|o(?=\s+[A-Z“(]))\s*")
NUM_ITEM_RE = re.compile(r"^\d{1,2}\.\s")
CAPTION_TABLE_RE = re.compile(r"^Table (\d+-\d+)\.\s+\S")
CAPTION_FIG_RE = re.compile(r"^Figure (\d+-\d+)\.\s+\S")


def ws(s):
    return " ".join((s or "").split())


def _key(s):
    return re.sub(r"[^0-9a-z]", "", (s or "").lower())


def _lines(aux, page):
    return aux.meta["lines_by_page"].get(page, [])


# ------------------------------------------------------------------ labels ----
def set_page_labels(doc, aux):
    """Printed page labels from the PDF footer ('© NEI 2019. All rights reserved. nei.org 49'); the body offset
    (printed = PDF page - 8) is the fallback and is checked against every footer that carries a number."""
    labels = {}
    for p in range(2, doc.n_pages + 1):
        labels[p] = FRONT_LABELS.get(p) or str(p - BODY_OFFSET)
    found = {}
    for p, lines in aux.meta["lines_by_page"].items():
        for ln in lines:
            m = re.search(r"nei\.org\s+([ivx]+|\d+)\s*$", ln.text)
            if m:
                found[p] = m.group(1)
    mismatch = {p: (found[p], labels.get(p)) for p in found if labels.get(p) != found[p]}
    doc.meta["page_label_mismatch"] = mismatch
    labels.update(found)
    doc.page_labels = labels


# ------------------------------------------------------------------- noise ----
def drop_noise(doc, aux=None):
    """Cover (-> H1 + frontmatter), running footers of the front matter, the landscape-page header 'August 2019',
    'THIS PAGE INTENTIONALLY BLANK' (p41) and 'SEE TABLES FOLLOWING PAGES' (p89)."""
    cover = [e for e in doc.els if e.page == 1]
    title = next((ws(e.text) for e in cover if e.kind == "heading"), "")
    doc.meta["cover"] = {
        "number": next((ws(e.text) for e in cover if re.fullmatch(r"\d\d-\d\d", ws(e.text))), ""),
        "series": next((ws(e.text) for e in cover if ws(e.text).startswith("Modernization")), ""),
        "title": title,
        "revision": next((ws(e.text) for e in cover if "Revision" in e.text), ""),
        "date": next((ws(e.text) for e in cover if re.fullmatch(r"[A-Z][a-z]+ \d{4}", ws(e.text))), ""),
    }
    keep = [El("heading", title, 1, level=1, meta={"doc_title": True})]
    for e in doc.els:
        if e.page == 1:
            continue
        t = ws(e.text)
        if e.kind in ("para", "item", "heading", "caption") and (FOOTER_RE.match(t) or t in NOISE_TEXTS):
            continue
        if "CambriaMath" in (e.font or ""):
            e.meta["equation"] = True      # display equation (R_j, p73): own paragraph, transcribed by patch
        keep.append(e)
    doc.els = keep


# ----------------------------------------------------------------- figures ----
def _caption_line(aux, ref):
    for ln in _lines(aux, ref.page):
        if ws(ln.text).startswith(f"Figure {ref.num}."):
            return ln
    return None


def figure_box(aux, ref):
    """Core box, clamped to the caption bottom (the core box of Fig 5-2 spans the whole page) and extended upwards to
    the last body-text line above the figure (column titles such as 'Systems Engineering Inputs' sit above the
    drawings of Fig 3-3)."""
    x0, y0, x1, y1 = ref.box
    cap = _caption_line(aux, ref)
    if cap is not None:
        y1 = min(y1, cap.y1 + 4)
        above = [ln for ln in _lines(aux, ref.page)
                 if ln.size >= 10.5 and ln.x0 < 80 and len(ln.text) > 25 and ln.y1 < y0 + 8 and ln.y1 < cap.y0 - 40
                 and not any("Arial" in f for f in ln.fonts)]
        if above:
            y0 = min(y0, max(ln.y1 for ln in above) + 2)
        else:
            y0 = min(y0, 66.0)
    return (x0, y0, x1, y1)


def _spans_in(page, rect):
    """Text of the spans whose centre lies in rect, rows top-down, spans left-right; a row ending with a hyphen or
    dash joins the next row without a space (this Word PDF has no automatic hyphenation)."""
    r = fitz.Rect(rect)
    spans = []
    for b in page.get_text("dict")["blocks"]:
        for ln in b.get("lines", []):
            for s in ln["spans"]:
                if not s["text"].strip():
                    continue
                bb = fitz.Rect(s["bbox"])
                if r.contains(fitz.Point((bb.x0 + bb.x1) / 2, (bb.y0 + bb.y1) / 2)):
                    spans.append((bb, s["text"]))
    rows = []
    for bb, t in sorted(spans, key=lambda s: (round((s[0].y0 + s[0].y1) / 2), s[0].x0)):
        mid = (bb.y0 + bb.y1) / 2
        for row in rows:
            if abs(row["mid"] - mid) < 3:
                row["spans"].append((bb, t))
                break
        else:
            rows.append({"mid": mid, "spans": [(bb, t)]})
    out = []
    for row in rows:
        sps = sorted(row["spans"], key=lambda s: s[0].x0)
        text = ""
        for i, (bb, t) in enumerate(sps):
            if i and bb.x0 - sps[i - 1][0].x1 > 1.5 and not text.endswith(" ") and not t.startswith(" "):
                text += " "
            text += t
        out.append(ws(text))
    return out


def _join_rows(rows):
    out = ""
    for r in rows:
        if not out:
            out = r
        elif out.endswith(("-", "—")):
            out += r
        else:
            out += " " + r
    return out


def _bullets(rows, glyph="•"):
    items = []
    for r in rows:
        if r.startswith(glyph):
            items.append([r[len(glyph):].strip()])
        elif items:
            items[-1].append(r)
    return [_join_rows(i) for i in items]


# regions in visible PDF coordinates (x0, y0, x1, y1), read off the rendered pages 45, 57 and 58
FIG_REGIONS = {
    "4-3": {
        "root": (255, 72, 320, 112),
        "SR": (100, 150, 190, 182), "SR1": (125, 200, 245, 238), "SR2": (125, 243, 245, 290),
        "NSRST": (245, 150, 330, 186), "NSRST1": (275, 204, 368, 233), "NSRST2": (275, 247, 368, 286),
        "NST": (395, 150, 480, 186), "NST1": (405, 200, 512, 229),
        "leg1": (320, 362, 386, 392), "leg2": (408, 362, 472, 392),
        "note": (100, 340, 300, 392),
    },
    "5-1": {"box1": (370, 230, 480, 340), "box2": (205, 408, 480, 462)},
    "5-2": {
        "top": (215, 84, 345, 124), "top_list": (355, 70, 560, 160),
        "pra": (250, 158, 310, 180), "det": (245, 178, 315, 206),
        "left_note": (90, 168, 205, 196), "right_note": (350, 168, 480, 196),
        "left": (150, 222, 235, 250), "right": (320, 222, 410, 250),
        "left_list": (100, 258, 292, 352), "right_list": (292, 258, 522, 352),
    },
}


def _esc_star(s):
    return s.replace("*", "\\*")


def figure_callout(pdf, num):
    """`> [!figure]` block with the informative figure text that exists nowhere else in the document (review F17:
    Fig 4-3 categories and note, Fig 5-1 explanatory boxes, Fig 5-2 bullet lists)."""
    reg = FIG_REGIONS.get(num)
    if not reg:
        return None
    if num == "4-3":
        page = pdf[44]
        g = {k: _join_rows(_spans_in(page, r)) for k, r in reg.items()}
        lines = [
            f"> [!figure] Figure {num} text",
            f"> {g['root']}:",
            f"> - {g['SR']}: {_esc_star(g['SR1'])}; {g['SR2']}",
            f"> - {g['NSRST']}: {g['NSRST1']}; {g['NSRST2']}",
            f"> - {g['NST']}: {g['NST1']}",
            ">",
            f"> Legend: {g['leg1']} (green: the SR and NSRST boxes); {g['leg2']} (purple: the NST box)",
            ">",
            f"> {_esc_star(g['note'])}",
        ]
        return "\n".join(lines)
    if num == "5-1":
        page = pdf[56]
        return "\n".join([f"> [!figure] Figure {num} text",
                          f"> {_join_rows(_spans_in(page, reg['box1']))}",
                          ">",
                          f"> {_join_rows(_spans_in(page, reg['box2']))}"])
    if num == "5-2":
        page = pdf[57]
        g = {k: _spans_in(page, r) for k, r in reg.items()}
        out = [f"> [!figure] Figure {num} text", f"> {_join_rows(g['top'])}:"]
        out += [f"> - {b}" for b in _bullets(g["top_list"])]
        out += [">", f"> {_join_rows(g['left'])}:"]
        out += [f"> - {b}" for b in _bullets(g["left_list"])]
        out += [">", f"> {_join_rows(g['right'])}:"]
        out += [f"> - {b}" for b in _bullets(g["right_list"])]
        out += [">", "> Other labels: " + "; ".join(_join_rows(g[k]) for k in ("pra", "det", "left_note", "right_note"))]
        return "\n".join(out)
    return None


def figures(doc, aux):
    """Caption -> bold caption paragraph + PNG embed (+ figure-text callout); vector-figure debris dropped.

    Local replacement of refclean.figures.figures_step: the core caption match would take the body paragraph
    'Figure 5-1 illustrates …' (p57) as the caption of Figure 5-1, and the core box of Figure 5-2 covers the whole
    page (the body text under the caption would be dropped as debris)."""
    render = aux.meta.get("render_figures", True)
    fig_dir_rel = f"figures/{doc.key}"
    pdf = fitz.open(doc.pdf_path)
    refs = {r.num: r for r in aux.figures}
    boxes = {r.num: figure_box(aux, r) for r in aux.figures}
    by_page = collections.defaultdict(list)
    for r in aux.figures:
        by_page[r.page].append(r)
    done, out, captions = set(), [], {}
    for e in doc.els:
        refs_here = by_page.get(e.page, [])
        t = ws(e.text)
        m = CAPTION_FIG_RE.match(t) if e.kind in ("para", "item", "heading", "caption") else None
        ref = refs.get(m.group(1)) if m else None
        if ref is not None and ref.page == e.page and ref.num not in done:
            cap_line = _caption_line(aux, ref)
            cap = ws(cap_line.text) if cap_line is not None else f"Figure {ref.num}. {ref.caption}"
            if not _key(t).startswith(_key(cap)):
                ref = None
        else:
            ref = None
        if ref is not None:
            done.add(ref.num)
            captions[ref.num] = cap
            out.append(El("para", f"**{cap}**", e.page, e.bbox, meta={"figure_caption": ref.num}))
            fname = f"Fig_{ref.num}.png"
            if render:
                r2 = copy.copy(ref)
                r2.box = boxes[ref.num]
                render_png(pdf, r2, os.path.join(doc.out_dir, fig_dir_rel, fname))
            out.append(El("raw_md", f"![{cap}]({fig_dir_rel}/{fname})", e.page, meta={"figure_img": ref.num}))
            call = figure_callout(pdf, ref.num)
            if call:
                out.append(El("raw_md", call, e.page, meta={"figure_callout": ref.num}))
            # text glued after the caption (p43: '… SSCs The following key points …') stays as body text
            end = _prefix_end(e.text, _key(cap))
            rest = e.text[end:].strip() if end is not None else ""
            if rest:
                out.append(El("para", rest, e.page, e.bbox, e.font, e.size, meta={"split_from_caption": ref.num}))
            continue
        if e.kind == "image":
            continue
        if refs_here and e.kind in ("para", "item", "heading", "caption", "table") and e.bbox:
            vis = odl_to_visible(e.bbox, pdf[e.page - 1])
            c = fitz.Point((vis.x0 + vis.x1) / 2, (vis.y0 + vis.y1) / 2)
            if any(fitz.Rect(boxes[r.num]).contains(c) for r in refs_here):
                continue
        out.append(e)
    pdf.close()
    doc.els = out
    doc.meta["figures"] = [captions.get(r.num, f"Figure {r.num}. {r.caption}") for r in aux.figures]
    doc.meta.setdefault("figures_without_caption_element", []).extend(r.num for r in aux.figures if r.num not in done)


# ------------------------------------------------------------------ tables ----
def _st_tables(doc):
    path = os.path.join(doc.raw_dir, doc.stem + ".structtree.json")
    with open(path, encoding="utf-8") as f:
        tree = json.load(f)
    els, _ = elements_from_json(tree)
    return [e.table for e in els if e.kind == "table"]


def _pick(sts, page, first):
    for t in sts:
        if t.page == page and ws(t.grid[0][0].text).startswith(first):
            return t
    raise LookupError(f"struct-tree table on p{page} starting with {first!r} not found")


def _cell(text, r=0, c=0, bold=False):
    return T.Cell(text, r, c, bold=bold)


def _table(rows, header_rows, page, pages, join=" ", caption="", notes=None):
    grid = [[_cell(x, i, j) for j, x in enumerate(row)] for i, row in enumerate(rows)]
    t = T.Table(grid=grid, header_rows=header_rows, page=page, pages=list(pages), caption=caption,
                notes=list(notes or []))
    t.meta["join"] = join
    return t


def _texts(t, r):
    return [c.text for c in t.grid[r]]


def _is_repeat_header(t, r):
    return [ws(x) for x in _texts(t, r)] == [ws(x) for x in _texts(t, 0)]


def _group_rows(t, start):
    """Rows whose only non-empty cell is the first one (group labels such as 'Terms Associated with Functions')."""
    out = []
    for r in range(start, t.n_rows):
        v = _texts(t, r)
        out.append(bool(v[0].strip()) and not any(x.strip() for x in v[1:]))
    return out


def table_3_1(sts):
    t = _pick(sts, 14, "Event Type")
    rows = [_texts(t, r) for r in range(t.n_rows)]
    return _table(rows, 1, 14, [14])


def table_3_2(sts):
    t = _pick(sts, 36, "Measure")
    return _table([_texts(t, r) for r in range(t.n_rows)], 1, 36, [36])


SUP_NUM = re.compile(r"^(Applicability|Available Guidance|.*Process)(\d)$")


def table_4_1(sts):
    """Single header, 'Group' column, RISC-2 check mark moved from SR to NSRST (struct-tree shift, review F04),
    note markers as <sup>n</sup>, notes 1-5 under the table, repeated page headers dropped."""
    t = _pick(sts, 52, "Special Treatment Category")
    head = ["Group", "Special Treatment Category", "Applicability<sup>1</sup>", "Applicability<sup>1</sup>",
            "Applicability<sup>1</sup>", "Available Guidance<sup>4</sup>"]
    sub = ["Group", "Special Treatment Category", "SR SSC", "NSRST SSC", "NST SSC", "Available Guidance<sup>4</sup>"]
    rows, notes, group, prev = [head, sub], [], "", None
    for r in range(2, t.n_rows):
        v = [ws(x) if i else x for i, x in enumerate(_texts(t, r))]
        v[0] = ws(v[0])
        if v[0].startswith("Special Treatment Category") or v[0] == "SR SSC" or ws(v[0]) == "SR SSC":
            continue
        if re.match(r"^SR\s+SSC$", v[0]):
            continue
        if re.match(r"^\d\s+\S", v[0]) and not any(v[1:]):
            for line in _texts(t, r)[0].split("\n"):
                m = re.match(r"^(\d)\s+(.*)$", ws(line))
                if m:
                    notes.append(f"<sup>{m.group(1)}</sup> {m.group(2)}")
            continue
        if v[0] and not any(v[1:]):
            group = v[0]
            continue
        if not v[0] and prev is not None and not v[4] and v[3].startswith("Essentially"):
            # 'Document evaluation of adequacy …' spans the RISC-1 and RISC-2 sub-rows; the struct-tree reading
            # puts the RISC-2 check mark in the SR column and the guidance in the NST column
            v = [prev[0], "", v[1], "", v[3]]
        elif not v[0] and prev is not None:
            v[0] = prev[0]
        m = re.match(r"^(.*Process)(\d)$", v[0])
        if m:
            v[0] = f"{m.group(1)}<sup>{m.group(2)}</sup>"
        for i in (2, 3):
            if re.fullmatch(r"\d", v[i]):
                v[i] = f"<sup>{v[i]}</sup>"
        rows.append([group] + v)
        prev = v
    return _table(rows, 2, 52, [52, 53, 54], notes=notes)


def table_5_1(sts):
    t = _pick(sts, 67, "Elements of")
    return _table([_texts(t, r) for r in range(t.n_rows)], 1, 67, [67], join="; ")


def table_5_2(main_tab):
    """Main-JSON cells carry the correct spans (Layer 1 guideline spans both 'Layer Guideline' columns, Layers 4-5
    share one guideline pair, the two 'Overall Guidelines' cells span all five layers); the core fill-down makes each
    row self-contained. Notes row -> table notes; [a]-[d] markers -> <sup>."""
    t = main_tab
    rows = []
    notes = []
    for r in range(t.n_rows):
        v = _texts(t, r)
        if v[0].startswith("Notes:"):
            for line in v[0].split("\n"):
                if ws(line):
                    notes.append(ws(line))
            continue
        if r >= t.header_rows or True:
            rows.append([re.sub(r"\[([a-d])\]", r"<sup>[\1]</sup>", x) for x in v])
    return _table(rows, 2, 69, [69], notes=notes)


def _item_starts(pdf, page, bbox_odl, frac=0.33):
    """Left edges of list items in the right-hand column of a 2-column list table (hanging indents)."""
    pg = pdf[page - 1]
    vis = odl_to_visible(bbox_odl, pg)
    col_x = vis.x0 + frac * vis.width
    lines = []
    for b in pg.get_text("dict")["blocks"]:
        for ln in b.get("lines", []):
            txt = ws("".join(s["text"] for s in ln["spans"]))
            bb = fitz.Rect(ln["bbox"])
            if txt and vis.contains(fitz.Point(bb.x0 + 1, (bb.y0 + bb.y1) / 2)) and bb.x0 > col_x:
                lines.append((bb.x0, txt))
    if not lines:
        return []
    x_item = min(x for x, _ in lines)
    return [t for x, t in lines if abs(x - x_item) < 2]


def list_table(t, page, pages, starts=(), join=" "):
    """2-column list tables (5-3, 5-5, 5-7, 5-8): the struct-tree reading puts the 2nd..nth item of a row-spanned
    attribute into column 1 of the following rows (review R5b). Rebuild one row per item with the attribute
    filled down; items glued into one cell are split at item starts taken from the PDF lines."""
    rows = [[ws(x) for x in _texts(t, 0)]]
    attr = None
    for r in range(t.header_rows, t.n_rows):
        a, f = _texts(t, r)[:2]
        if a.strip() and f.strip():
            attr = ws(a)
            items = f.split("\n")
        elif a.strip() and attr is not None:
            items = a.split("\n")
        elif f.strip():
            items = f.split("\n")
        else:
            continue
        for it in items:
            for piece in _split_at_starts(ws(it), starts):
                rows.append([attr, piece])
    return _table(rows, 1, page, pages, join=join)


def _split_at_starts(text, starts):
    cuts = sorted({text.find(s) for s in (ws(x) for x in starts) if s and text.find(s) > 0})
    if not cuts:
        return [text]
    parts, prev = [], 0
    for c in cuts:
        parts.append(text[prev:c].strip())
        prev = c
    parts.append(text[prev:].strip())
    return [p for p in parts if p]


def table_5_4(sts):
    t = _pick(sts, 72, "Standard Elements")
    rows = [_texts(t, r) for r in range(t.n_rows) if r == 0 or not _is_repeat_header(t, r)]
    return _table(rows, 1, 72, [72, 73])


def group_table(t, group_name, page, pages, join=" "):
    """Group-label rows -> leading group column; repeated page headers dropped."""
    rows = [[group_name] + _texts(t, 0)]
    group = ""
    flags = _group_rows(t, 0)
    for r in range(t.header_rows, t.n_rows):
        if _is_repeat_header(t, r):
            continue
        if flags[r]:
            group = ws(_texts(t, r)[0])
            continue
        rows.append([group] + _texts(t, r))
    return _table(rows, 1, page, pages, join=join)


def table_5_9(sts):
    t = _pick(sts, 87, "LBE IE Series Name")          # first table on p87 = 5-9
    child = [ws(x) for x in _texts(t, 1)][:5]
    head = ["LBE IE Series Name", "Functional", "Functional", "Functional", "Physical", "Physical"]
    sub = ["LBE IE Series Name"] + child
    rows = [head, sub] + [_texts(t, r) for r in range(2, t.n_rows)]
    return _table(rows, 2, 87, [87])


def table_5_10(sts, main_tab):
    t = [x for x in sts if x.page == 87][1]            # second table on p87 = 5-10
    head = [ws(x) for x in _texts(main_tab, 0)]
    sub = [ws(x) for x in _texts(main_tab, 1)]
    rows = [head, sub] + [_texts(t, r) for r in range(1, t.n_rows)]
    return _table(rows, 2, 87, [87])


def acronyms(sts):
    rows = [["Acronym", "Definition"]]
    for t in [x for x in sts if x.page == 8]:
        for r in range(t.n_rows):
            a, d = _texts(t, r)[:2]
            aa, dd = a.split("\n"), d.split("\n")
            if len(aa) > 1 and len(aa) == len(dd):          # 'IDP\nIDPP' in one cell pair
                rows += [[x, y] for x, y in zip(aa, dd)]
            else:
                rows.append([a, d])
    return _table(rows, 1, 8, [8])


def where_items(sts):
    t = _pick(sts, 73, "Rj =")
    return [ws(_texts(t, r)[0]) for r in range(t.n_rows)]


def tables(doc, aux):
    """Replace the collapsed main-JSON tables with the struct-tree tables (review R5)."""
    sts = _st_tables(doc)
    pdf = fitz.open(doc.pdf_path)
    caps = {}
    for e in doc.els:
        m = CAPTION_TABLE_RE.match(ws(e.text)) if e.kind in ("heading", "caption", "item", "para") else None
        if m and len(ws(e.text)) < 200 and not ws(e.text).endswith("."):
            caps[m.group(1)] = (ws(e.text), id(e))
    main_tabs = {e.page: e.table for e in doc.els if e.kind == "table"}
    st = {t.page: t for t in sts}
    new = {
        "3-1": table_3_1(sts), "3-2": table_3_2(sts), "4-1": table_4_1(sts), "5-1": table_5_1(sts),
        "5-2": table_5_2(main_tabs[69]),
        "5-3": list_table(_pick(sts, 70, "Attribute"), 70, [70],
                          _item_starts(pdf, 70, _st_bbox(doc, 70))),
        "5-4": table_5_4(sts),
        "5-5": list_table(_pick(sts, 75, "Attribute"), 75, [75], _item_starts(pdf, 75, _st_bbox(doc, 75))),
        "5-6": group_table(_pick(sts, 77, "Evaluation Focus"), "Group", 77, [77, 78], join="; "),
        "5-7": list_table(_pick(sts, 81, "Programs"), 81, [81], _item_starts(pdf, 81, _st_bbox(doc, 81))),
        "5-8": list_table(_pick(sts, 83, "Attribute"), 83, [83], _item_starts(pdf, 83, _st_bbox(doc, 83))),
        "5-9": table_5_9(sts), "5-10": table_5_10(sts, main_tabs[87]),
    }
    pdf.close()
    for num, t in new.items():
        if num not in caps:
            raise LookupError(f"caption for Table {num} not found")
        t.caption = caps[num][0]
        t.meta["num"] = num
    gloss = group_table(_pick(sts, 90, "LMP Term"), "Category", 90, list(range(90, 96)))
    gloss.meta["num"] = "Glossary"
    acr = acronyms(sts)
    acr.meta["num"] = "Acronyms"
    where = where_items(sts)

    cap_ids = {v[1] for v in caps.values()}
    # replacement anchor: element id -> [new elements]; removed elements
    plan = {"3-1": {"tables": {14}}, "3-2": {"tables": {36}}, "4-1": {"clear": {52, 53, 54}},
            "5-1": {"tables": {67}}, "5-2": {"tables": {69}}, "5-3": {"tables": {70}}, "5-4": {"tables": {72, 73}},
            "5-5": {"tables": {75}}, "5-6": {"tables": {77}, "clear": {78}}, "5-7": {"tables": {81}},
            "5-8": {"tables": {83}}, "5-9": {"tables": {87}}, "5-10": {"tables": {87}}}
    table_pages = {p for v in plan.values() for p in v.get("tables", ())} | set(range(90, 96))
    clear_pages = {p for v in plan.values() for p in v.get("clear", ())}
    out, placed = [], set()

    def tel(t):
        return El("table", "", t.page, table=t, meta={"nei_table": t.meta["num"]})

    for e in doc.els:
        if id(e) in cap_ids:
            num = next(k for k, v in caps.items() if v[1] == id(e))
            if num in new and num not in placed:
                placed.add(num)
                out.append(tel(new[num]))
            continue
        if e.page in clear_pages or (e.kind == "table" and e.page in table_pages):
            if e.kind == "table" and e.page == 90 and "Glossary" not in placed:
                placed.add("Glossary")
                out.append(tel(gloss))
            continue
        if e.page == 8 and e.kind == "para" and not e.text.lstrip().startswith("*"):
            if "Acronyms" not in placed:
                placed.add("Acronyms")
                out.append(tel(acr))
            continue
        if e.page == 73 and e.kind == "para" and ws(e.text).startswith("where: Rj ="):
            out.append(El("para", "where:", e.page, e.bbox, e.font, e.size, meta={"where_head": True}))
            for w in where:
                out.append(El("item", w, e.page, (90.0,) + tuple(e.bbox[1:]), e.font, e.size, 0, "unordered",
                              meta={"where_item": True}))
            continue
        out.append(e)
    missing = [k for k in list(new) + ["Glossary", "Acronyms"] if k not in placed]
    if missing:
        raise LookupError(f"tables not placed: {missing}")
    doc.els = out


def _st_bbox(doc, page):
    """ODL bbox of the first struct-tree table on a page (for the PDF item-start scan)."""
    path = os.path.join(doc.raw_dir, doc.stem + ".structtree.json")
    cache = doc.meta.setdefault("_st_bbox", {})
    if not cache:
        with open(path, encoding="utf-8") as f:
            tree = json.load(f)
        for node in tree.get("kids", []):
            if node.get("type") == "table":
                cache.setdefault(node.get("page number"), tuple(node.get("bounding box", ())))
    return cache[page]


# ---------------------------------------------------------------- headings ----
def outline_refs(pdf_path):
    """Body outline entries (55): [(depth, page, title)]; front-matter bookmarks are skipped."""
    from pypdf import PdfReader
    r = PdfReader(pdf_path)
    out = []

    def walk(ol, d=0):
        for it in ol:
            if isinstance(it, list):
                walk(it, d + 1)
            else:
                out.append((d, r.get_destination_page_number(it) + 1, ws(it.title)))
    walk(r.outline)
    return [x for x in out if re.match(r"^\d+(?:\.\d+)*\s", x[2])]


def subhead_lines(aux):
    """Whole lines set in Calibri-BoldItalic 11 pt (68 unnumbered subheadings: Task … and topic subheads)."""
    subs = []
    for p in sorted(aux.meta["lines_by_page"]):
        if p in aux.toc_pages:
            continue
        for ln in aux.meta["lines_by_page"][p]:
            if ln.fonts and all("BoldItalic" in f for f in ln.fonts) and abs(ln.size - 11) < 0.3:
                subs.append((p, ln.y0, ws(ln.text)))
    return subs


def heading_refs(aux, pdf_path):
    refs = []
    for depth, page, title in outline_refs(pdf_path):
        y = None
        for ln in _lines(aux, page):
            k, kl = _key(title), _key(ln.text)
            if len(kl) >= 4 and (k.startswith(kl) or kl.startswith(k)) and ln.x0 < 80:
                y = ln.y0
                break
        num = title.split()[0]
        refs.append({"kind": "num", "num": num, "title": title, "page": page, "y": y if y is not None else 0.0,
                     "depth": depth})
    for page, y, text in subhead_lines(aux):
        refs.append({"kind": "sub", "title": text, "page": page, "y": y})
    refs.sort(key=lambda r: (r["page"], r["y"]))
    return refs


def _prefix_end(text, key):
    """Index in text just after the prefix whose alphanumeric characters spell `key`; None if no such prefix."""
    n = 0
    for i, c in enumerate(text):
        if n == len(key):
            return i
        if c.isalnum():
            if c.lower() != key[n]:
                return None
            n += 1
    return len(text) if n == len(key) else None


def _suffix_start(text, key):
    n = len(key)
    for i in range(len(text) - 1, -1, -1):
        if n == 0:
            return i + 1
        c = text[i]
        if c.isalnum():
            if c.lower() != key[n - 1]:
                return None
            n -= 1
    return 0 if n == 0 else None


def _match_heading(e, key):
    """('start', end) | ('end', start) | None."""
    text = BULLET_RE.sub("", e.text, count=1)
    off = len(e.text) - len(text)
    end = _prefix_end(text, key)
    if end is not None:
        while end < len(text) and text[end] in ")]}”\"'":
            end += 1                       # closing bracket of the heading itself ('… Functions (RSFs)')
        rest = text[end:]
        if not rest.strip() or (rest[:1].isspace() and re.match(r"\s+[A-Z“\"(0-9]", rest)):
            return ("start", off + end)
    start = _suffix_start(e.text, key)
    if start is not None and start > 0 and e.text[:start].rstrip().endswith(TERMINAL):
        return ("end", start)
    return None


def headings(doc, aux):
    """pypdf outline (55 sections, depth 0/1/2 -> H2/H3/H4 under the H1 title) + Calibri-BoldItalic 11 pt
    subheadings (parent + 1); glued headings are split; other ODL headings become paragraphs (captions were
    consumed by the figure/table steps)."""
    refs = heading_refs(aux, doc.pdf_path)
    aux.headings = [HeadingRef(r["num"], r["title"], r["page"], r["depth"] + 2) for r in refs if r["kind"] == "num"]
    els = doc.els
    cursor = 0
    unmatched = []
    for ref in refs:
        key = _key(ref["title"])
        found = None
        for i in range(cursor, len(els)):
            e = els[i]
            if e.page > ref["page"] + 1:
                break
            if e.kind not in ("heading", "para", "item", "caption") or e.meta.get("heading_done"):
                continue
            if e.meta.get("figure_caption") or e.page < ref["page"] - 1:
                continue
            mm = _match_heading(e, key)
            if mm:
                found = (i, mm)
                break
        if not found:
            unmatched.append(ref)
            continue
        i, (where, pos) = found
        e = els[i]
        if where == "start":
            head_txt, before, after = e.text[:pos], "", e.text[pos:]
        else:
            head_txt, before, after = e.text[pos:], e.text[:pos], ""
        head_txt = ws(BULLET_RE.sub("", head_txt, count=1))
        meta = {"heading_done": True}
        if ref["kind"] == "num":
            meta.update({"numbered": True, "num": ref["num"], "depth": ref["depth"]})
        else:
            meta["sub"] = True
        new = []
        if before.strip():
            new.append(El(e.kind, before.strip(), e.page, e.bbox, e.font, e.size, e.level, e.list_style,
                          id=e.id, meta=dict(e.meta)))
        new.append(El("heading", head_txt, e.page, e.bbox, e.font, e.size, 0, id=e.id, meta=meta))
        if after.strip():
            new.append(El("para", after.strip(), e.page, e.bbox, e.font, e.size, id=e.id,
                          meta={"split_from_heading": True}))
        els[i:i + 1] = new
        cursor = i + [k for k, n in enumerate(new) if n.kind == "heading"][0] + 1
    doc.els = els
    doc.meta.setdefault("unmatched_headings", []).extend(
        f"{r.get('num', '')} {r['title']} (p{r['page']})".strip() for r in unmatched if r["kind"] == "num")
    doc.meta.setdefault("unmatched_subheads", []).extend(
        f"{r['title']} (p{r['page']})" for r in unmatched if r["kind"] == "sub")
    # levels; front-matter headings H2; everything else that ODL called a heading becomes a paragraph
    cur = 1
    for e in doc.els:
        if e.kind != "heading":
            continue
        if e.meta.get("doc_title"):
            e.level, cur = 1, 1
        elif e.meta.get("numbered"):
            e.level = e.meta["depth"] + 2
            cur = e.level
        elif e.meta.get("sub"):
            e.level = min(cur + 1, 6)
        elif ws(e.text) in FRONT_HEADINGS:
            e.level, cur = 2, 2
            e.meta["front"] = True
        else:
            e.kind = "para"


# --------------------------------------------------------------- footnotes ----
FN_BODY_RE = re.compile(r"^[*†]")


def _is_fn_body(e):
    return (e.kind in ("para", "item") and e.size and e.size <= 9.5 and FN_BODY_RE.match(e.text.strip())
            and e.bbox and e.bbox[1] < 140 and e.page != 8)


def footnotes(doc, aux=None):
    """Page footnotes (15 '*' + 1 '†', review F13) -> [^pNN] references and definitions at the end of the enclosing
    section; the footnote bodies no longer split the running text."""
    bodies = []                                   # (page, symbol, text)
    keep = []
    for e in doc.els:
        if _is_fn_body(e):
            parts = re.split(r"\s+(?=†\s)", e.text.strip())
            for p in parts:
                bodies.append((e.page, p[0], ws(p[1:])))
            continue
        keep.append(e)
    doc.els = keep
    labels = {}
    count = collections.Counter()
    for page, sym, _ in bodies:
        count[page] += 1
        labels[(page, sym)] = f"p{page}" if count[page] == 1 else f"p{page}b"
    placed_after = {}                             # label -> index of the element holding the reference
    missing = []
    for (page, sym), label in labels.items():
        # a reference marker follows a word character; '**' of a bold caption is not a marker
        pat = re.compile(r"(?<=[^\s*])\*(?![*\w])") if sym == "*" else re.compile(r"(?<=\S)†")
        hit = None
        for i, e in enumerate(doc.els):
            if e.page != page or e.meta.get("figure_caption"):
                continue
            if e.kind in ("para", "item", "heading"):
                m = pat.search(e.text)
                if m:
                    e.text = e.text[:m.start()] + f"[^{label}]" + e.text[m.end():]
                    hit = i
                    break
            elif e.kind == "table":
                for row in e.table.grid:
                    for c in row:
                        m = pat.search(c.text) if c.text else None
                        if m and not c.filled:
                            c.text = c.text[:m.start()] + f"[^{label}]" + c.text[m.end():]
                            hit = i
                            break
                    if hit is not None:
                        break
                if hit is not None:
                    break
        if hit is None:
            missing.append(label)
        else:
            placed_after[label] = hit
    doc.meta["footnotes_unreferenced"] = missing
    # definition goes before the next heading or the next page after the reference, whichever comes first, so it stays
    # under its own page anchor; a paragraph running on across the page break is passed (join_breaks merges it back)
    inserts = collections.defaultdict(list)
    for page, sym, text in bodies:
        label = labels[(page, sym)]
        i = placed_after.get(label)
        if i is None:
            continue
        j = i + 1
        while j < len(doc.els) and doc.els[j].kind != "heading" and not (doc.els[j].page or 0) > page:
            j += 1
        while j < len(doc.els) and doc.els[j].kind != "heading" and _joins(doc.els[j - 1], doc.els[j]):
            j += 1
        inserts[j].append(El("para", f"[^{label}]: {text}", 0, meta={"footnote_def": label}))
    out = []
    for j, e in enumerate(doc.els):
        out.extend(inserts.get(j, []))
        out.append(e)
    out.extend(inserts.get(len(doc.els), []))
    doc.els = out
    doc.meta["footnotes"] = [labels[(p, s)] for p, s, _ in bodies]


# --------------------------------------------------------- joins and lists ----
def _bulleted(text):
    return bool(BULLET_RE.match(text)) or bool(NUM_ITEM_RE.match(text.strip()))


def _continues(prev, nxt):
    p = prev.rstrip()
    t = nxt.lstrip()
    if not p or not t or p.endswith(TERMINAL):
        return False
    if p.endswith(("-", "—")) and t[0].isalpha():
        return True
    return S._is_continuation(p, t, "para")


def join_breaks(doc, aux=None):
    """Merge paragraph/item fragments split by page breaks or by an interposed footnote; a line-end hyphen is a real
    hyphen in this Word PDF ('all non-' + 'safety-related' -> 'all non-safety-related')."""
    out = []
    for e in doc.els:
        if out and _joins(out[-1], e):
            prev = out[-1]
            sep = "" if prev.text.rstrip().endswith(("-", "—")) else " "
            prev.text = prev.text.rstrip() + sep + e.text.lstrip()
            continue
        out.append(e)
    doc.els = out


NOJOIN = ("footnote_def", "where_item", "where_head", "equation")


def _joins(prev, e):
    """True when join_breaks merges fragment e into the element before it."""
    return (e.kind in ("para", "item") and not any(e.meta.get(k) for k in NOJOIN)
            and prev.kind in ("para", "item") and not any(prev.meta.get(k) for k in NOJOIN)
            and not prev.meta.get("figure_caption") and not _bulleted(e.text) and _continues(prev.text, e.text))


INLINE_SUB = re.compile(r":\s+o\s+(?=[A-Z])")


def lists(doc, aux=None):
    """Nested list levels from the PDF x0 of the item (bullet 90 pt, 'o' 108 pt, Wingdings ▪ 126 pt), glyphs
    stripped, false items at the body margin (- As …, - At …) -> paragraphs, bullet paragraphs -> items,
    inline 'o' sub-item split (p38)."""
    out = []
    for e in doc.els:
        if e.kind == "para" and BULLET_RE.match(e.text) and e.bbox and 85 <= e.bbox[0] <= 130 \
                and not e.meta.get("footnote_def"):
            e.kind = "item"
        if e.kind != "item":
            out.append(e)
            continue
        x0 = e.bbox[0] if e.bbox else 90.0
        if x0 < 80 and not BULLET_RE.match(e.text) and not NUM_ITEM_RE.match(e.text.strip()):
            e.kind, e.level = "para", 0
            out.append(e)
            continue
        e.level = 0 if x0 < 100 else (1 if x0 < 117 else 2)
        e.text = BULLET_RE.sub("", e.text, count=1).strip()
        m = INLINE_SUB.search(e.text)
        if m:
            head, tail = e.text[:m.start() + 1], e.text[m.end():]
            e.text = head
            out.append(e)
            out.append(El("item", tail, e.page, e.bbox, e.font, e.size, e.level + 1, e.list_style,
                          meta={"inline_sub": True}))
            continue
        out.append(e)
    doc.els = out


def ordered_lists(doc, aux=None):
    """Runs of numbered items ('1. Mitigate DBEs …') -> one Markdown ordered list (no '- 1.' double marker)."""
    out = []
    for e in doc.els:
        if e.kind == "item" and NUM_ITEM_RE.match(e.text.strip()):
            if out and out[-1].kind == "raw_md" and out[-1].meta.get("ordered") and out[-1].page in (e.page, e.page - 1):
                out[-1].text += "\n" + e.text.strip()
                continue
            out.append(El("raw_md", e.text.strip(), e.page, meta={"ordered": True}))
            continue
        out.append(e)
    doc.els = out


# ------------------------------------------------------------ text fixes ----
def subscripts(doc, aux):
    """Subscripts lost in extraction (p35 x_i, p73 where-list symbols) -> <sub>, from PDF span evidence
    (span <= 0.75 x the size of the preceding span, same baseline, lower top)."""
    fixes = collections.defaultdict(list)
    for p, lines in aux.meta["lines_by_page"].items():
        for ln in lines:
            prev = None
            for sp in ln.spans:
                t, r, size, font = sp[0], sp[1], sp[2], sp[3]
                if (prev is not None and size <= 0.75 * prev[2] and abs(r.y1 - prev[1].y1) < 1.6
                        and r.y0 > prev[1].y0 + 1 and "CambriaMath" not in font):
                    base = prev[0].split()[-1] if prev[0].split() else ""
                    if base:
                        fixes[p].append((base, t.strip()))
                prev = sp
    n = 0
    for e in doc.els:
        if e.kind not in ("para", "item") or e.page not in fixes:
            continue
        for base, sub in fixes[e.page]:
            pat = re.compile(r"(?<![\w<])" + re.escape(base + sub) + r"(?![\w>])")
            new, k = pat.subn(f"{base}<sub>{sub}</sub>", e.text)
            if k:
                e.text, n = new, n + k
    doc.meta["subscripts_restored"] = n


def sign_lost_exponents(doc, aux):
    """Review F01 (H): superscript exponents broken across a line end ('1×10-⏎4/plant-year', '10-⏎2/plant-year')
    lose their minus sign in both conversions ('1×104/plant-year', '102/plant-year'). Restored only where the PDF
    shows the '10-' line end followed by the digit on the next line."""
    pdf = fitz.open(doc.pdf_path)
    evidence = collections.defaultdict(set)
    for page in pdf:
        words = page.get_text("words")
        by = collections.defaultdict(list)
        for w in words:
            by[(w[5], w[6])].append(w)
        keys = sorted(by)
        for k, k2 in zip(keys, keys[1:]):
            # consecutive lines in reading order; the break often falls on a PyMuPDF block boundary
            last = sorted(by[k], key=lambda w: w[7])[-1][4]
            first = sorted(by[k2], key=lambda w: w[7])[0][4]
            m1 = re.search(r"(?:(\d+)×)?10-$", last)
            m2 = re.match(r"^(\d)/plant", first)
            if m1 and m2:
                evidence[page.number + 1].add((m1.group(1) or "", m2.group(1)))
    pdf.close()
    doc.meta["sign_lost_evidence"] = {p: sorted(v) for p, v in evidence.items()}
    fixed = []

    # every bare '10-N' in this document is an exponent and stands before '/plant' (review R6 and §5.3); the core
    # rule needs superscript evidence on the element's own page, which is lost when a paragraph split across a page
    # break is rejoined (p22/p23)
    BARE = re.compile(r"(?<![\w.\-×xX])10-(\d{1,2})(?=/plant)")

    def fix(text, page):
        for mant, d in evidence.get(page, ()):
            if mant:
                pat = re.compile(rf"(?<![\w.]){re.escape(mant)}×10{d}(?=/plant)")
                rep = f"{mant}E-0{d}"
            else:
                pat = re.compile(rf"(?<![\w.×\-]){'10'}{d}(?=/plant)")
                rep = f"1E-0{d}"
            text, k = pat.subn(rep, text)
            if k:
                fixed.append((page, rep, k))
        text, k = BARE.subn(lambda m: f"1E-{int(m.group(1)):02d}", text)
        if k:
            fixed.append((page, "bare 10-N/plant", k))
        return text

    for e in doc.els:
        if e.kind in ("para", "item"):
            e.text = fix(e.text, e.page)
        elif e.kind == "table":
            for row in e.table.grid:
                for c in row:
                    if c.text:
                        c.text = fix(c.text, e.page)
    doc.meta["sign_lost_fixed"] = fixed


def hyphen_supplement(doc, aux):
    """Line-end hyphens inside table cells that the core line pairing misses (table rows merge several cells into
    one line): 'NEI-00-⏎04', 'Defense-in-⏎Depth'. Same acceptance rule as the core map (joined form never occurs
    inline in the PDF); word pairs are taken within one PDF text block."""
    pdf = fitz.open(doc.pdf_path)
    inline = collections.Counter()
    seq = []
    for page in pdf:
        by = collections.defaultdict(list)
        for w in page.get_text("words"):
            by[(w[5], w[6])].append(w)
        for k in sorted(by):
            wl = sorted(by[k], key=lambda w: w[7])
            seq.append((page.number + 1, k[0], wl))
            for w in wl:
                inline[w[4].strip(".,;:()“”\"*")] += 1
    pdf.close()
    add = {}
    for (p, b, wl), (p2, b2, wl2) in zip(seq, seq[1:]):
        if (p, b) != (p2, b2):
            continue
        last, first = wl[-1][4], wl2[0][4]
        m = re.search(r"([A-Za-z][\w/.-]*?)([-—])$", last.lstrip("(“\""))
        if not m or not re.match(r"[A-Za-z0-9]", first):
            continue
        left, dash, right = m.group(1), m.group(2), first.rstrip(".,;:)”\"*")
        if re.search(r"\d$", left) and re.match(r"\d/plant", right):
            continue                                   # sign-lost exponent, handled separately
        joined = left + right
        if inline.get(joined, 0) == 0 and joined not in aux.hyphen_map:
            add[joined] = left + dash + right
    aux.hyphen_map.update(add)
    doc.meta["hyphen_supplement"] = add


# -------------------------------------------------------------- post fixes ----
def _render_table(t):
    join = t.meta.get("join", " ")
    names = T.header_names(t)

    def cell(text):
        lines = [ws(x) for x in text.split("\n") if ws(x)]
        if join == " ":
            s = T.cell_md("\n".join(lines))
        else:
            s = "; ".join(lines).replace("|", "\\|")
        return s

    lines = ["| " + " | ".join(names) + " |", "|" + "---|" * t.n_cols]
    for r in range(t.header_rows, t.n_rows):
        vals = [cell(c.text) for c in t.grid[r]]
        if any(vals):
            lines.append("| " + " | ".join(vals) + " |")
    return "\n".join(lines)


def post_fixes(doc, aux=None):
    ordered_lists(doc, aux)
    for e in doc.els:
        if e.kind == "table":
            e.meta["rendered"] = _render_table(e.table)
        elif e.kind in ("para", "item") and e.text.lstrip().startswith("*") and not e.text.lstrip().startswith("**"):
            e.text = "\\" + e.text.lstrip()
    # drop empty elements
    doc.els = [e for e in doc.els if e.kind in ("table", "image") or e.text.strip()]


# ------------------------------------------------------------------ public ----
def steps():
    return [
        set_page_labels,
        drop_noise,
        S.drop_toc,
        figures,
        tables,
        headings,
        footnotes,
        join_breaks,
        lists,
        subscripts,
        sign_lost_exponents,
        hyphen_supplement,
        S.normalise_text,
        post_fixes,
    ]


def _pdf_meta(path):
    try:
        from pypdf import PdfReader
        return dict(PdfReader(path).metadata or {})
    except Exception:
        return {}


def metadata(doc, aux):
    cover = doc.meta.get("cover", {})
    pm = _pdf_meta(doc.pdf_path)
    tables_ = [e.table.caption for e in doc.els if e.kind == "table" and e.table.caption]
    return {
        "doc_id": "NEI 18-04",
        "title": cover.get("title") or "Risk-Informed Performance-Based Technology Inclusive Guidance for Non-Light "
                                      "Water Reactor Licensing Basis Development",
        "series_title": cover.get("series") or "Modernization of Technical Requirements for Licensing of Advanced "
                                               "Non-Light Water Reactors",
        "doc_type": "Industry guidance document (technical report)",
        "issuer": "Nuclear Energy Institute (NEI)",
        "revision": "1",
        "date": "2019-08",
        "adams": pm.get("/AccessionNumber", "ML19241A472"),
        "docket": pm.get("/DocketNumber", "PROJ0689"),
        "source_pdf": f"references/raw/{doc.stem}.pdf",
        "raw_json": f"references/raw/{doc.stem}.json",
        "raw_json_tables": f"references/raw/{doc.stem}.structtree.json",
        "pdf_pages": doc.n_pages,
        "page_label_offset": "body printed page = PDF page - 8 (PDF p9-95 = printed 1-87; front matter p2-8 = ii-viii)",
        "tables": tables_,
        "figures": doc.meta.get("figures", []),
        "tags": ["reference", "nei", "lmp", "licensing-modernization", "non-lwr", "risk-informed"],
        "aliases": ["NEI 18-04", "NEI 18-04 Rev. 1", "NEI 18-04 Revision 1", "LMP guidance document"],
    }
