"""PSAR Chapter 7 (Descriptions for Safety-Significant SSCs) — chapter hooks.

Review evidence: meta/references_cleanup/file_reviews/review_ch7a.md, review_ch7b.md, review_ch7c.md.

Steps (run after the common PSAR steps, before assign_levels):
  retry_unmatched_subheads  underlined subheadings after a colon lead-in (2 real hits, p265/p365)
  dl_tables             27 borderless "Function ID | Function Description | <SYS> Functional Support" tables
                        rebuilt from PDF word positions; the prose remnants opendataloader produced are removed
  nested_nic_items      21 NIC sub-bullets ("-" under "●", PDF p251-252) nested under their parent item
  false_items           list items without a printed bullet/label in the PDF become paragraphs
  table_notes           '*' / '**' table-note markers as <sup>*</sup>; Table 7.2.3-1 group rows -> Subsystem column
  resplit_paragraphs    paragraphs that opendataloader merged are split again at PDF paragraph starts
"""
import collections
import re

import fitz

from .. import normalize as N
from .. import structure as S
from ..doc import El
from ..figures import odl_to_visible
from .. import tables as T
from ..tables import Cell, Table

# ------------------------------------------------------------------ PDF words ----
ID_TOKEN = re.compile(r"^DL\d-(?:[A-Z]{2,4}\d+[a-z]?)?,?$")
ID_PART = re.compile(r"^(?:DL\d-)?[A-Z]{2,4}\d+[a-z]?,?$")
BULLET = re.compile(r"^[•●▪■◦]$")
TERMINAL = tuple('.:;?!”")')


def page_words(page):
    """PyMuPDF words in visible coordinates: [(x0, y0, x1, y1, text)]."""
    m = page.rotation_matrix
    out = []
    for w in page.get_text("words"):
        r = fitz.Rect(w[:4]) * m
        r.normalize()
        out.append((r.x0, r.y0, r.x1, r.y1, w[4]))
    return out


def word_lines(words, tol=2.0):
    """Group words into visual lines (same bottom within tol), left to right, top to bottom."""
    lines = []
    for w in sorted(words, key=lambda w: (round(w[3], 1), w[0])):
        if lines and abs(lines[-1]["y1"] - w[3]) < tol:
            lines[-1]["w"].append(w)
            lines[-1]["y0"] = min(lines[-1]["y0"], w[1])
        else:
            lines.append({"y0": w[1], "y1": w[3], "w": [w]})
    for ln in lines:
        ln["w"].sort(key=lambda w: w[0])
        ln["x0"] = ln["w"][0][0]
        ln["x1"] = max(w[2] for w in ln["w"])
        ln["text"] = " ".join(w[4] for w in ln["w"])
    lines.sort(key=lambda ln: ln["y0"])
    return lines


# --------------------------------------------------------- DL function tables ----
def _header_at(lines, i):
    """Column starts (c1, c2, c3) if line i is a 'Function ID  Function Description  <X>' header line."""
    ws = lines[i]["w"]
    for k in range(len(ws) - 3):
        if ws[k][4] == "Function" and ws[k + 1][4] == "ID" and ws[k + 2][4] == "Function" \
                and ws[k + 3][4] == "Description":
            c1, c2 = ws[k][0], ws[k + 2][0]
            third = [w for w in ws[k + 4:] if w[0] > c2 + 60]
            if third:
                return c1, c2, third[0][0]
    return None


def _col(x0, c2, c3):
    return 0 if x0 < c2 - 4 else (1 if x0 < c3 - 4 else 2)


def _id_line(ln, c2):
    toks = [w[4] for w in ln["w"] if w[0] < c2 - 4]
    return bool(toks) and bool(ID_TOKEN.match(toks[0]))


def _cell_text(parts):
    """Join the lines of one cell: hyphen at a line end joins directly; bullet lines become '; item'."""
    out = ""
    for ln in parts:
        t = ln.strip()
        if not t:
            continue
        bullet = False
        if t[:1] in "•●▪■◦" and t[1:2] == " ":
            t, bullet = t[2:].strip(), True
        if not out:
            out = t
        elif bullet:
            out = out + (" " if out.endswith(":") else "; ") + t
        elif out.endswith("-") and not out.endswith(" -") and t[:1].isalnum():
            out += t
        else:
            out += " " + t
    return out


def _segment(lines, start, c2, c3, header, page_no):
    """Rows of one table segment starting at body line index `start`. Returns (seg dict, next index)."""
    rows, lead = [], []
    last_y1 = None
    i = start
    while i < len(lines):
        ln = lines[i]
        if ln["y0"] > 715:                       # footer band
            break
        if last_y1 is not None and ln["y0"] - last_y1 > 30:
            break
        c0 = [w for w in ln["w"] if _col(w[0], c2, c3) == 0]
        if c0:
            t0 = " ".join(w[4] for w in c0)
            if ID_TOKEN.match(c0[0][4]):
                if rows and rows[-1]["id"].endswith(","):
                    rows[-1]["id"] += " " + t0          # 'DL3-RC1,' / 'DL3-RC2' (one cell)
                else:
                    rows.append({"id": t0, "y0": ln["y0"], "desc": [], "sup": [], "y1": ln["y1"]})
            elif rows and rows[-1]["id"].endswith(("-", ",")) and ID_PART.match(c0[0][4]):
                rows[-1]["id"] += " " + t0
            else:
                break                                 # body text at the margin: table ended
        tgt = rows[-1] if rows else None
        for col in (1, 2):
            ws = [w for w in ln["w"] if _col(w[0], c2, c3) == col]
            if not ws:
                continue
            txt = " ".join(w[4] for w in ws)
            if tgt is None:
                lead.append((col, txt, ln["y0"]))
            else:
                tgt["desc" if col == 1 else "sup"].append((txt, ln["y0"]))
        if tgt is not None:
            tgt["y1"] = ln["y1"]
        last_y1 = ln["y1"]
        i += 1
    seg = {"page": page_no, "header": header, "c2": c2, "c3": c3, "rows": rows, "lead": lead,
           "y1": last_y1}
    return seg, i


def extract_dl_segments(pdf_path):
    """All table segments (one per page part) in document order."""
    pdf = fitz.open(pdf_path)
    segs = []
    for page in pdf:
        pno = page.number + 1
        words = page_words(page)
        if not any(ID_TOKEN.match(w[4]) and w[0] < 90 for w in words):
            continue
        lines = word_lines(words)
        i = 0
        while i < len(lines):
            hc = _header_at(lines, i)
            if hc:
                c1, c2, c3 = hc
                top = lines[i]["y0"]
                head3 = [w[4] for w in lines[i]["w"] if w[0] >= c3 - 4]
                j = i + 1
                while j < len(lines) and not _id_line(lines[j], c2) and lines[j]["y0"] - lines[j - 1]["y1"] < 6 \
                        and all(w[0] >= c3 - 4 for w in lines[j]["w"]):
                    head3 += [w[4] for w in lines[j]["w"]]
                    j += 1
                seg, i = _segment(lines, j, c2, c3, " ".join(head3), pno)
                seg["y0"] = top
                segs.append(seg)
                continue
            ln = lines[i]
            # header-less table (RWG p219, NHV p229): an ID at the margin followed by two more text columns
            if abs(ln["x0"] - 72.5) < 3 and ID_TOKEN.match(ln["w"][0][4]) and len(ln["w"]) > 2:
                cols = _infer_columns(lines, i)
                if cols:
                    c2, c3 = cols
                    seg, i = _segment(lines, i, c2, c3, None, pno)
                    seg["y0"] = ln["y0"]
                    segs.append(seg)
                    continue
            i += 1
    pdf.close()
    return segs


def _infer_columns(lines, i):
    """(c2, c3) for a header-less table from its ID lines: gaps > 12 pt separate the three columns."""
    c2s, c3s = [], []
    for ln in lines[i:i + 40]:
        if ln["y0"] > 715:
            break
        ws = ln["w"]
        if not ID_TOKEN.match(ws[0][4]):
            continue
        gaps = [(ws[k + 1][0], ws[k + 1][0] - ws[k][2]) for k in range(len(ws) - 1)]
        big = [x for x, g in gaps if g > 12]
        if len(big) >= 2:
            c2s.append(round(big[0]))
            c3s.append(round(big[1]))
    if len(c2s) < 1:
        return None
    return (collections.Counter(c2s).most_common(1)[0][0], collections.Counter(c3s).most_common(1)[0][0])


def build_dl_tables(segs):
    """Merge page segments of one logical table; return [{'header', 'rows': [(id, desc, sup)], 'segs'}]."""
    tables = []
    for s in segs:
        prev = tables[-1] if tables else None
        cont = (prev is not None and s["header"] is not None and prev["header"] == s["header"]
                and s["page"] == prev["segs"][-1]["page"] + 1 and s["y0"] < 110
                and not any(x["page"] == s["page"] and x is not s and x["y0"] < s["y0"] for x in segs))
        if cont:
            if s["lead"] and prev["rows"]:                  # a row split over the page break
                r = prev["rows"][-1]
                for col, txt, y in s["lead"]:
                    r["desc" if col == 1 else "sup"].append((txt, y + 10000))
            prev["rows"].extend(s["rows"])
            prev["segs"].append(s)
        else:
            tables.append({"header": s["header"], "rows": list(s["rows"]), "segs": [s]})
    for t in tables:
        _fill_shared_support(t)
        t["cells"] = [(r["id"], _cell_text([x[0] for x in r["desc"]]), _cell_text([x[0] for x in r["sup"]]))
                      for r in t["rows"]]
    return tables


def _fill_shared_support(t):
    """A support cell spanning several rows (NDC/NUP, PDF p328): its lines are spread over the rows by y.

    Detected when a row's support text continues (no terminal punctuation) into the next row's support, which
    starts in lower case; the merged text then fills the spanned rows and the empty rows that follow."""
    rows = t["rows"]
    k = 0
    while k < len(rows) - 1:
        cur = " ".join(x[0] for x in rows[k]["sup"]).strip()
        nxt = " ".join(x[0] for x in rows[k + 1]["sup"]).strip()
        if cur and nxt and not cur.endswith(TERMINAL) and nxt[:1].islower():
            j = k + 1
            lines = list(rows[k]["sup"])
            while j < len(rows):
                s = " ".join(x[0] for x in rows[j]["sup"]).strip()
                if not s:
                    break
                lines += rows[j]["sup"]
                if s.endswith(TERMINAL):
                    j += 1
                    break
                j += 1
            end = j
            while end < len(rows) and not rows[end]["sup"]:
                end += 1
            for r in rows[k:end]:
                r["sup"] = list(lines)
                r["shared_support"] = True
            k = end
            continue
        k += 1


# ------------------------------------------------------------ doc surgery ----
def _vis(e, pdf):
    if not e.bbox or not (0 < e.page <= len(pdf)):
        return None
    return odl_to_visible(e.bbox, pdf[e.page - 1])


def _tokens(s):
    return [t.lower() for t in re.findall(r"[A-Za-z0-9]+", s)]


def dl_tables(doc, aux):
    """Replace the prose remnants of the borderless DL function tables by Markdown tables."""
    segs = get_dl_segments(doc, aux)
    tables = build_dl_tables(segs)
    pdf = fitz.open(doc.pdf_path)
    sups_of = lambda p: [s.sup for s in aux.sups.get(p, [])]  # noqa: E731
    vis = [_vis(e, pdf) for e in doc.els]
    remove = set()
    inserts = []           # (index to insert before, El)
    qa = []
    for t in tables:
        removed_idx = []
        for s in t["segs"]:
            y0, y1 = s["y0"] - 1.5, s["y1"] + 1.5
            for i, e in enumerate(doc.els):
                if e.page != s["page"] or i in remove or e.kind not in ("para", "item", "hdr", "caption"):
                    continue
                v = vis[i]
                if v is None:
                    continue
                cy = (v.y0 + v.y1) / 2
                if y0 <= cy <= y1:
                    removed_idx.append(i)
        remove.update(removed_idx)
        first = t["segs"][0]
        # insertion point: after the last element above the table on its first page (reading-order safe)
        above = [i for i, e in enumerate(doc.els) if e.page == first["page"] and i not in remove and vis[i] is not None
                 and (vis[i].y0 + vis[i].y1) / 2 < first["y0"]]
        if above:
            at = max(above) + 1
        else:
            on_page = [i for i, e in enumerate(doc.els) if e.page == first["page"]]
            at = min(on_page) if on_page else (min(removed_idx) if removed_idx else len(doc.els))
        sys_head = t["header"] or "Functional Support"
        grid = [[Cell("Function ID", 0, 0, bold=True), Cell("Function Description", 0, 1, bold=True),
                 Cell(sys_head, 0, 2, bold=True)]]
        for r, (fid, desc, sup) in enumerate(t["cells"], start=1):
            p = first["page"]
            grid.append([Cell(fid, r, 0), Cell(N.text_pipeline(desc, sups_of(p), aux.hyphen_map), r, 1),
                         Cell(N.text_pipeline(sup, sups_of(p), aux.hyphen_map), r, 2)])
        pages = sorted({s["page"] for s in t["segs"]})
        tab = Table(grid=grid, header_rows=1, page=first["page"], pages=pages)
        tab.meta["dl_table"] = True
        el = El("table", "", first["page"], table=tab, meta={"dl_table": True})
        if t["header"] is None:
            # RWG (p219) and NHV (p229) print the same three columns without a header row
            el.meta["header_supplied"] = True
            note = f"<!-- header row supplied: the PDF prints this table without one (p.{first['page']}) -->"
            el.meta["rendered"] = note + "\n\n" + T.render_md(tab)
        inserts.append((at, el))
        # QA: removed text must be table text, and the table text must come from removed elements
        rem_tok = collections.Counter()
        for i in removed_idx:
            rem_tok.update(_tokens(doc.els[i].text))
        tab_tok = collections.Counter()
        for fid, desc, sup in t["cells"]:
            tab_tok.update(_tokens(fid + " " + desc + " " + sup))
        head_tok = collections.Counter(_tokens("Function ID Function Description " + (t["header"] or "")))
        tab_tok_h = tab_tok + collections.Counter({k: v * len(t["segs"]) for k, v in head_tok.items()})
        extra_removed = rem_tok - tab_tok_h
        shared = any(r.get("shared_support") for r in t["rows"])
        not_removed = collections.Counter() if shared else (tab_tok - rem_tok)
        qa.append({"page": first["page"], "pages": pages, "header": t["header"], "ids": [c[0] for c in t["cells"]],
                   "removed_elements": len(removed_idx),
                   "removed_not_in_table": sum(extra_removed.values()),
                   "table_not_in_removed": sum(not_removed.values()),
                   "removed_not_in_table_tokens": list(extra_removed)[:12],
                   "table_not_in_removed_tokens": list(not_removed)[:12]})
    pdf.close()
    out = []
    ins = collections.defaultdict(list)
    for at, el in inserts:
        ins[at].append(el)
    for i, e in enumerate(doc.els):
        for el in ins.get(i, []):
            out.append(el)
        if i not in remove:
            out.append(e)
    for el in ins.get(len(doc.els), []):
        out.append(el)
    doc.els = out
    doc.meta["dl_tables"] = qa
    # the two-way token coverage of the rebuilt tables, in the report (and asserted by tests/test_psar_ch07.py):
    # every token removed with the prose remnants must be in the table, and every table token must come from them
    doc.meta["ch07_dl_qa"] = {
        "tables": len(qa),
        "rows": sum(len(x["ids"]) for x in qa),
        "removed_elements": sum(x["removed_elements"] for x in qa),
        "removed_not_in_table": sum(x["removed_not_in_table"] for x in qa),
        "table_not_in_removed": sum(x["table_not_in_removed"] for x in qa),
    }
    for x in qa:
        if x["removed_not_in_table"] or x["table_not_in_removed"]:
            doc.meta.setdefault("ch07_warnings", []).append(
                f"DL table p{x['page']}: {x['removed_not_in_table']} removed tokens not in the table "
                f"{x['removed_not_in_table_tokens']}, {x['table_not_in_removed']} table tokens not removed "
                f"{x['table_not_in_removed_tokens']}")
    # the second header line of the NDC/NUP table ('Functional Support', p328) is underlined and was reported as an
    # unmatched subheading; it is a table header, not a subheading
    heads = {(s["page"], t["header"]) for t in tables for s in t["segs"] if t["header"]}
    keep, dropped = [], []
    for u in doc.meta.get("unmatched_subheads", []):
        m = re.match(r"^(.*) \(p(\d+)\)$", u)
        if m and any(int(m.group(2)) == p and m.group(1) in h for p, h in heads):
            dropped.append(u)
        else:
            keep.append(u)
    doc.meta["unmatched_subheads"] = keep
    doc.meta["ch07_table_header_subheads"] = doc.meta.get("ch07_table_header_subheads", []) + dropped


# ----------------------------------------------------------------- lists ----
def nested_nic_items(doc, aux):
    """NIC sub-systems list (PDF p251-252): the 21 sub-bullets printed with '-' under a '●' item keep the '-' in
    their text ('- - Gaseous …' in Markdown). Strip it and nest them one level below their parent item."""
    n = 0
    parent = None
    for e in doc.els:
        if e.kind != "item":
            if not (e.kind == "raw_md" and e.meta.get("anchor")):
                parent = None
            continue
        m = re.match(r"^-\s+(\S.*)$", e.text)
        if m and parent is not None and 250 <= e.page <= 253:
            e.text = m.group(1)
            e.level = parent.level + 1
            n += 1
        else:
            parent = e
    doc.meta["ch07_nested_items"] = n


def glyph_bullets(doc, aux):
    """Paragraph text that still starts with the bullet glyph ('● IEEE 603-2018 ● IEEE 379-2014 ● IEEE 384-2018',
    PDF p298; '● IEEE 379-2014,' p322) -> one list item per glyph."""
    out, n = [], 0
    for e in doc.els:
        if e.kind == "para" and e.text.lstrip().startswith("●"):
            for part in (p.strip() for p in e.text.split("●")):
                if part:
                    out.append(El("item", part, e.page, e.bbox, e.font, e.size, 0, "unordered", id=e.id,
                                  meta={"from_glyph": True}))
                    n += 1
            continue
        out.append(e)
    doc.els = out
    doc.meta["ch07_glyph_items"] = n


def numbered_items(doc, aux):
    """Numbered lists rendered as '- 1. …' (Table 7.1.2-1 Note 1 p42; RAB seismic parameters p361): a run of items
    '1. …', '2. …' becomes one ordered Markdown list."""
    out, i, runs = [], 0, 0
    els = doc.els
    while i < len(els):
        e = els[i]
        if e.kind == "item" and re.match(r"^1\.\s", e.text):
            j = i
            run = []
            while j < len(els) and els[j].kind == "item" and re.match(rf"^{len(run) + 1}\.\s", els[j].text):
                run.append(els[j])
                j += 1
            if len(run) >= 2:
                out.append(El("raw_md", "\n".join(r.text.strip() for r in run), e.page, e.bbox,
                              meta={"numbered_list": True}))
                runs += 1
                i = j
                continue
        out.append(e)
        i += 1
    doc.els = out
    doc.meta["ch07_numbered_lists"] = runs


# ----------------------------------------------------------------- tables ----
def table_notes(doc, aux):
    """Table-note markers '*' / '**' (Tables 7.1.2-4, 7.1.3-6, 7.2.3-1, 7.2.4-1) as <sup>*</sup> in the cells and
    at the start of the note, so that '* Classification …' is no longer parsed as a nested Markdown list."""
    n = 0
    for e in doc.els:
        if e.kind != "table" or not any(re.match(r"^\*{1,2}\s?\S", x) for x in e.table.notes):
            continue
        t = e.table
        for row in t.grid:
            for c in row:
                if re.search(r"\w\*{1,2}$", c.text.strip()):
                    c.text = re.sub(r"(\*{1,2})$", r"<sup>\1</sup>", c.text.strip())
                    n += 1
        t.notes = [re.sub(r"^(\*{1,2})\s?(?=\S)", r"<sup>\1</sup> ", x) for x in t.notes]
    doc.meta["ch07_note_markers"] = n


def group_rows(doc, aux):
    """Table 7.2.3-1 (p130): the group rows 'Primary SCG' / 'Intermediate SCG' span both columns; opendataloader made
    the first one a second header row ('Component: Primary SCG'). Rebuilt with a leading Subsystem column (the
    column name is supplied; review_ch7a §1 #18)."""
    for e in doc.els:
        if e.kind != "table" or not e.table.caption.startswith("Table 7.2.3-1"):
            continue
        t = e.table
        rows = [[c.text for c in r] for r in t.grid]
        head = [x for x in rows[0]]
        body = rows[1:]
        grid = [[Cell("Subsystem", 0, 0, bold=True)] + [Cell(h, 0, j + 1, bold=True) for j, h in enumerate(head)]]
        group = ""
        for vals in body:
            if vals and len(set(v.strip() for v in vals)) == 1 and vals[0].strip().endswith("SCG"):
                group = vals[0].strip()
                continue
            grid.append([Cell(group, len(grid), 0, filled=True)] +
                        [Cell(v, len(grid), j + 1) for j, v in enumerate(vals)])
        t.grid = grid
        t.header_rows = 1
        doc.meta["ch07_group_rows"] = len(grid) - 1


def subscripts(doc, aux):
    """k<sub>eff</sub> (PDF p187 prints 'eff' as a 7.7 pt subscript; the only symbol subscript in the chapter)."""
    for e in doc.els:
        if e.page == 187 and e.kind in ("para", "item") and "keff" in e.text:
            e.text = re.sub(r"\bkeff\b", "k<sub>eff</sub>", e.text)


def registered_space(doc, aux):
    """'GT STRUDL®Version 40' (p370): the superscript '® ' carries a space in the PDF that the conversion lost."""
    for e in doc.els:
        if e.kind in ("para", "item") and "®" in e.text:
            e.text = re.sub(r"®(?=[A-Za-z0-9])", "® ", e.text)


# ----------------------------------------------------------- paragraphs ----
def _norm(s):
    """Lower-case alphanumerics of s and their indices in s."""
    chars, idx = [], []
    for i, ch in enumerate(s):
        if ch.isalnum():
            chars.append(ch.lower())
            idx.append(i)
    return "".join(chars), idx


CONT_LAST = {"through", "and", "or", "of", "in", "to", "the", "a", "an", "with", "by", "for", "from", "as", "at", "on",
             "per", "see", "under", "within", "including", "between", "than", "that", "which", "is", "are", "be",
             "described", "listed", "provided", "identified", "shown", "discussed"}


def _body_lines(doc, aux, pdf):
    """{page: [line dicts]} of body text lines (header/footer band, figures and tables excluded), y-sorted, with
    'start' = the line begins a PDF paragraph (vertical gap > 6 pt above it, or a bullet glyph)."""
    from ..pdfaux import header_footer_band
    excl = {}
    for f in aux.figures:
        excl.setdefault(f.page, []).append(fitz.Rect(f.box))
    for e in doc.els:
        if e.kind == "table" and e.bbox and not e.meta.get("dl_table"):
            excl.setdefault(e.page, []).append(odl_to_visible(e.bbox, pdf[e.page - 1]))
    for s in get_dl_segments(doc, aux):
        excl.setdefault(s["page"], []).append(fitz.Rect(0, s["y0"] - 1, 1000, (s["y1"] or s["y0"]) + 1))
    out = {}
    for pno, lines in aux.meta.get("lines_by_page", {}).items():
        if pno in aux.toc_pages or pno == 1:
            continue
        top, bot = header_footer_band(pdf[pno - 1])
        keep = []
        for ln in lines:
            c = fitz.Point((ln.x0 + ln.x1) / 2, (ln.y0 + ln.y1) / 2)
            if not (top <= c.y <= bot) or any(r.contains(c) for r in excl.get(pno, [])):
                continue
            keep.append(ln)
        keep.sort(key=lambda ln: ln.y0)
        rows = []
        for k, ln in enumerate(keep):
            prev = keep[k - 1] if k else None
            bullet = ln.text[:1] in "●•▪■◦"
            rows.append({"text": ln.text, "norm": _norm(ln.text)[0], "x0": ln.x0, "y0": ln.y0, "y1": ln.y1,
                         "prev": prev.text if prev else None,
                         "start": prev is None or ln.y0 - prev.y1 > 6 or bullet, "first": prev is None,
                         "bullet": bullet})
        out[pno] = rows
    return out


def _first_line(e, body):
    """The PDF line that begins element e (its normalised text is a prefix of e's normalised text)."""
    tn = _norm(e.text)[0]
    if len(tn) < 12:
        return None
    for p in (e.page, e.page + 1):
        for ln in body.get(p, []):
            key = ln["norm"][:40]
            if len(key) >= 12 and tn.startswith(key):
                return p, ln
    return None


def pdf_paragraphs(doc, aux):
    """Re-align paragraph boundaries with the PDF (review ch7a #7-8, ch7b #4-5, ch7c #7-8).

    join:  a paragraph whose first PDF line is not a paragraph start (gap <= 6 pt above it) and whose predecessor
           ends with the PDF line just above it is the rest of that paragraph (e.g. '… discussed in Section 7.6.5.3.1
           through' + 'Section 7.6.5.3.4. The following …', p298); across a page break only when the predecessor
           ends in a continuation word ('through', 'in', …) or a comma.
    split: a paragraph that contains a PDF paragraph start (gap > 6 pt, or a bullet line) after its first character,
           where the text before it ends with the PDF line preceding that start, is split there (RG title +
           conformance paragraph, subheading-less run-ins, the p2 309 bullet + paragraph merge, and the > 2,000-char
           merges)."""
    pdf = fitz.open(doc.pdf_path)
    body = _body_lines(doc, aux, pdf)
    pdf.close()
    joins, splits = [], []
    # ---- join
    out = []
    for e in doc.els:
        prev = out[-1] if out else None
        if e.kind == "para" and prev is not None and prev.kind == "para" and not e.meta.get("in_item"):
            fl = _first_line(e, body)
            pn = _norm(prev.text)[0]
            ok = False
            if fl is not None:
                p, ln = fl
                if not ln["start"] and ln["prev"]:
                    tail = _norm(ln["prev"])[0][-20:]
                    ok = len(tail) >= 8 and pn.endswith(tail)
                elif ln["first"] and p == e.page:
                    last = re.findall(r"[A-Za-z]+,?$", prev.text.rstrip())
                    ok = (bool(last) and (last[0].endswith(",") or last[0].lower() in CONT_LAST)
                          and not prev.text.rstrip().endswith(TERMINAL))
            if ok:
                joins.append(f"p{e.page}: …{prev.text[-40:]} + {e.text[:40]}…")
                prev.text = prev.text.rstrip() + " " + e.text.lstrip()
                continue
        out.append(e)
    doc.els = out
    # ---- split
    out = []
    for e in doc.els:
        if e.kind not in ("para", "item") or len(e.text) < 30:
            out.append(e)
            continue
        text = e.text
        tn, ti = _norm(text)
        cuts = set()
        for p in (e.page, e.page + 1):
            for ln in body.get(p, []):
                if not ln["start"] or not ln["prev"]:
                    continue
                key = ln["norm"][:40]
                tail = _norm(ln["prev"])[0][-20:]
                if len(key) < 12 or len(tail) < 8:
                    continue
                pos = tn.find(key, 1)
                while pos > 0:
                    if tn[:pos].endswith(tail):
                        cut = ti[pos]
                        while cut > 0 and not text[cut - 1].isspace():
                            cut -= 1
                        if cut > 0:
                            cuts.add((cut, ln["bullet"]))
                        break
                    pos = tn.find(key, pos + 1)
        if not cuts:
            out.append(e)
            continue
        bounds = sorted(cuts)
        pieces, last = [], 0
        kinds = [e.kind]
        for cut, bullet in bounds:
            pieces.append(text[last:cut].strip())
            kinds.append("item" if (bullet and e.kind == "item") else "para")
            last = cut
        pieces.append(text[last:].strip())
        for k, piece in enumerate(pieces):
            if not piece:
                continue
            if k == 0:
                e.text = piece
                out.append(e)
            else:
                out.append(El(kinds[k], piece, e.page, e.bbox, e.font, e.size, e.level if kinds[k] == "item" else 0,
                              e.list_style, id=e.id, meta={"split_from": e.id, "pdf_para_split": True}))
                splits.append(f"p{e.page}: …{pieces[k - 1][-30:]} | {piece[:40]}…")
    doc.els = out
    doc.meta["ch07_para_joins"] = joins
    doc.meta["ch07_para_splits"] = splits


def _next_pdf_line(aux, page, y):
    lines = [ln for ln in aux.meta.get("lines_by_page", {}).get(page, []) if ln.y0 > y + 5 and ln.y0 < 715]
    return min(lines, key=lambda ln: ln.y0) if lines else None


def _match_end(text, start, needle):
    """End offset in `text` of the whitespace-insensitive match of `needle` that begins at `start` (the alnum
    index map stops at the last alphanumeric character, which would leave a trailing ')' behind)."""
    i, j = start, 0
    while j < len(needle) and i < len(text):
        if needle[j].isspace():
            j += 1
        elif text[i].isspace():
            i += 1
        elif text[i] == needle[j]:
            i += 1
            j += 1
        else:
            return None
    return i if j == len(needle) else None


def _pdf_line_at(aux, page, y, text):
    """The PDF line at (page, y) when the underlined text is the whole line (a standalone subheading line)."""
    for ln in aux.meta.get("lines_by_page", {}).get(page, []):
        if abs(ln.y0 - y) < 2 and _norm(ln.text)[0] == _norm(text)[0]:
            return ln
    return None


def _split_out_subhead(els, lo, hi, text, key_next, meta):
    """Split `text` out of one of els[lo:hi] as a heading, where it is followed by `key_next` (the normalised
    start of the PDF line printed below it). Returns True when the split was made."""
    hn = _norm(text)[0]
    for j in range(lo, hi):
        t = els[j]
        if t.kind not in ("para", "item"):
            continue
        tn, ti = _norm(t.text)
        pos = tn.find(hn + key_next)
        if pos < 0:
            nxt = next((x for x in els[j + 1:j + 3] if x.kind in ("para", "item")), None)
            if tn.endswith(hn) and nxt is not None and _norm(nxt.text)[0].startswith(key_next):
                pos = len(tn) - len(hn)
            else:
                continue
        start = ti[pos]
        end = _match_end(t.text, start, text) or ti[pos + len(hn) - 1] + 1
        before, after = t.text[:start].strip(), t.text[end:].strip()
        new = []
        if before:
            t.text = before
            new.append(t)
        new.append(El("heading", " ".join(text.split()), t.page, t.bbox, meta=dict(meta)))
        if after:
            new.append(El("para", after, t.page, t.bbox, id=t.id, meta={"split_from": t.id}))
        els[j:j + 1] = new
        return True
    return False


def retry_unmatched_subheads(doc, aux):
    """structure.insert_subheads only accepts a subheading whose preceding text ends in '.?!”")', so a subheading
    that follows a lead-in sentence ending in a colon stays inside the paragraph: 'The RPS conforms to RGs as
    follows: RG 1.22, Revision 0, …' (p265, the only RG title of the RPS Regulatory Guidance subsection that was
    left out — its ten siblings on p266-267 are headings) and '… which are designated as SR or NSRST: External
    Hazard Protection for SR SSCs (SR)' (p365, siblings on p340/p346/p347). Such a subheading is re-inserted when
    the PDF prints it as a line of its own and the element text continues with the line printed below it."""
    todo, left, done = doc.meta.get("unmatched_subheads", []), [], []
    dl_regions = {}
    for seg in get_dl_segments(doc, aux):
        dl_regions.setdefault(seg["page"], []).append((seg["y0"] - 2, (seg["y1"] or seg["y0"]) + 2))
    skipped = []
    for entry in todo:
        m = re.match(r"^(.*) \(p(\d+)\)$", entry)
        sub = None
        if m:
            page = int(m.group(2))
            sub = next((s for s in aux.subheads if s.text == m.group(1) and s.page == page), None)
        if sub is not None and any(a <= sub.y <= b for a, b in dl_regions.get(sub.page, [])):
            skipped.append(entry)          # the underlined second header line of a DL table, not a subheading
            continue
        line = _pdf_line_at(aux, sub.page, sub.y, sub.text) if sub else None
        nl = _next_pdf_line(aux, sub.page, sub.y) if sub else None
        if line is None or nl is None:
            left.append(entry)
            continue
        idx = [i for i, e in enumerate(doc.els) if sub.page - 1 <= e.page <= sub.page + 1]
        ok = idx and _split_out_subhead(doc.els, min(idx), max(idx) + 1, sub.text, _norm(nl.text)[0][:30],
                                        {"sub": True, "heading_done": True, "colon_lead_in": True})
        (done if ok else left).append(entry)
    doc.meta["unmatched_subheads"] = left
    doc.meta["ch07_retried_subheads"] = done
    doc.meta["ch07_table_header_subheads"] = skipped


# Standalone title lines that are not underlined in the PDF but are siblings of underlined subheadings
# (FHP p169: the same three titles are underlined in FHE p189; p231: the other three HVAC titles are underlined).
UNDERLINE_LESS_SUBHEADS = {
    169: ("Structural Support (SR) – Load Path for SR SSCs", "Temporary Load Path for SR SSCs (NSRST)",
          "External Hazard Protection"),
    231: ("NI Contol Building HVAC",),
}


def standalone_subheads(doc, aux):
    n = 0
    for e in doc.els:
        if e.kind == "para" and e.text.strip() in UNDERLINE_LESS_SUBHEADS.get(e.page, ()):
            e.kind, e.meta = "heading", {"sub": True, "heading_done": True, "underline_less": True}
            n += 1
    doc.meta["ch07_standalone_subheads"] = n


REF_ENTRY = re.compile(r"^\d+(?:\.\d+)+-\d+\s")


def references_headings(doc, aux):
    """'References' / 'Reference' headings glued to the end of the preceding paragraph or list item (p18 after the
    re-split, p129, p261, p318, p342, p362 …) or left as a paragraph become headings; their entries become items."""
    out, n = [], 0
    els = doc.els
    for k, e in enumerate(els):
        nxt = next((x for x in els[k + 1:k + 4] if x.kind not in ("raw_md", "image")), None)
        entry_next = nxt is not None and nxt.kind in ("para", "item") and bool(REF_ENTRY.match(nxt.text.strip()))
        if e.kind in ("para", "item") and entry_next:
            m = re.search(r"(?:^|\s)(References?)$", e.text.strip())
            if m:
                rest = e.text.strip()[:m.start()].strip()
                if rest:
                    e.text = rest
                    out.append(e)
                out.append(El("heading", m.group(1), e.page, e.bbox, meta={"keep_heading": True}))
                n += 1
                continue
        out.append(e)
    doc.els = out
    S.references_as_items(doc, aux)
    doc.meta["ch07_reference_headings"] = n


def get_dl_segments(doc, aux):
    if "ch07_dl_segments" not in aux.meta:
        aux.meta["ch07_dl_segments"] = extract_dl_segments(doc.pdf_path)
    return aux.meta["ch07_dl_segments"]


STEPS = [retry_unmatched_subheads, dl_tables, nested_nic_items, glyph_bullets,
         numbered_items, table_notes, group_rows, subscripts, registered_space, pdf_paragraphs,
         standalone_subheads, references_headings]
