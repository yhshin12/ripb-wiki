"""PSAR Chapter 11 (Conduct of Operations) hooks — run after the common PSAR steps, before assign_levels.

Spec: meta/references_cleanup/file_reviews/review_ch11.md (§1 findings, §4 heading list, §5 rules).
Every step is PDF-guarded: an expected anchor that is not found is recorded in doc.meta['ch11_warnings']
(reported by the tests) instead of silently changing text.
"""
import re

import fitz

from .. import normalize as N
from .. import structure as S
from .. import tables as T
from ..doc import El
from ..pdfaux import header_footer_band

TERMINAL = tuple('.,:;?!)”"')


def _warn(doc, msg):
    doc.meta.setdefault("ch11_warnings", []).append(msg)


def _anchor(doc, page):
    lab = doc.page_labels.get(page)
    return f"<!-- page {page}{' | ' + lab if lab else ''} -->"


def _x0(e):
    return e.bbox[0] if e.bbox else None


# ------------------------------------------------------------------ noise ----
NOISE = {"LIST OF TABLES", "LIST OF FIGURES"}


def drop_noise(doc, aux=None):
    """LoT/LoF titles left on p4-5 (their entries were dropped with the dot leaders) and the stray 7-pt '.'
    in the right margin of p67 (x=680 pt), which also cut Table 11.5-1 into two tables."""
    out = []
    for e in doc.els:
        t = e.text.strip()
        if e.kind in ("para", "heading", "caption", "hdr", "item"):
            if t in NOISE or (t and re.fullmatch(r"[.·•\s]+", t)):
                continue
        out.append(e)
    doc.els = out


# --------------------------------------------------------------- headings ----
# Numbered headings that the pre-2026-09-13 core whitelist missed: on p23/p35/p40 the modal line x0 is the list
# indent (90/108 pt), so the per-page body-margin test rejected these margin lines. The core now accepts the page
# OR the document margin and finds them, so this module only checks that each is emitted exactly once.
FORMERLY_MISSED = [("11.2.1.4", "Human Factors Engineering Program Technical Elements", 23),
                   ("11.2.2.2.4", "Recognized Industry Issues", 35),
                   ("11.2.2.2.5", "Issues identified by Plant Personnel", 35),
                   ("11.2.2.3", "Results", 35),
                   ("11.2.6.2.1", "Objectives and Scope", 40)]


def check_expected_headings(doc, aux):
    for num, title, page in FORMERLY_MISSED:
        full = f"{num} {title}"
        n = sum(1 for e in doc.els if e.kind == "heading" and e.meta.get("num") == num
                and " ".join(e.text.split()) == full)
        if n != 1:
            _warn(doc, f"heading '{full}' (PDF p{page}) emitted {n} times, expected 1")


BOLD_SUBHEADS = [("Design Changes", 28)]   # bold run-in-free line under 11.2.1.9 (review §1 #6: H5)


def bold_subheads(doc, aux):
    lines = aux.meta.get("lines_by_page", {})
    for text, page in BOLD_SUBHEADS:
        bold = any(ln.text.strip() == text and all("Bold" in f for f in ln.fonts) for ln in lines.get(page, []))
        hit = [e for e in doc.els if e.page == page and e.kind == "para" and e.text.strip() == text]
        if not bold or len(hit) != 1:
            _warn(doc, f"bold subheading not found: {text} (p{page})")
            continue
        e = hit[0]
        e.kind, e.level = "heading", 0
        e.meta.update({"sub": True, "heading_done": True})


REF_ENTRY = re.compile(r"^\d+(?:\.\d+)+-\d+\s")


def split_glued_references(doc, aux=None):
    """'…support testing. References' (p66) / '…security operations. References' (p77): the section's
    References heading glued to the end of the last paragraph; the entries follow as paragraphs."""
    out = []
    els = doc.els
    for i, e in enumerate(els):
        m = re.search(r"\s+References$", e.text) if e.kind in ("para", "item") else None
        nxt = next((x for x in els[i + 1:i + 3] if x.kind not in ("hdr",)), None)
        if m and nxt is not None and REF_ENTRY.match(nxt.text.strip()) and e.text[:m.start()].rstrip().endswith("."):
            e.text = e.text[:m.start()].rstrip()
            out.append(e)
            out.append(El("heading", "References", e.page, e.bbox, id=e.id, meta={"keep_heading": True}))
            continue
        out.append(e)
    doc.els = out
    S.references_as_items(doc, aux)


# --------------------------------------------------------------- withheld ----
WITHHELD = "This information is withheld"


def withheld_section(doc, aux):
    """Section 11.4 is withheld; the PDF prints the marker on every page of the section (p60-64, and the core's
    running-title dedupe keeps an arbitrary subset). Keep one callout under the section heading and record the
    section with its page range in the frontmatter (doc.meta['withheld'], review §1 #23)."""
    pages = sorted(p for p, lines in aux.meta.get("lines_by_page", {}).items()
                   if any(WITHHELD in ln.text for ln in lines))
    if not pages:
        return
    out, kept, owner = [], False, ""
    for e in doc.els:
        if e.kind == "heading" and e.meta.get("numbered") and e.page == pages[0]:
            owner = " ".join(e.text.split())
        if e.kind == "raw_md" and e.meta.get("withheld") and e.page in pages:
            if kept:
                continue
            kept = True
        out.append(e)
    doc.els = out
    if not kept or not owner:
        _warn(doc, f"withheld section: heading={owner!r} callout={kept} on PDF p{pages[0]}-{pages[-1]}")
        return
    rng = f"p{pages[0]}" if len(pages) == 1 else f"p{pages[0]}-{pages[-1]}"
    doc.meta.setdefault("withheld", []).append(f"{owner} (PDF {rng}, SRI)")


# ------------------------------------------------------------- paragraphs ----
def _pdf_para_starts(doc, aux):
    """{page: [first-line text of every PDF body paragraph]} (block start or a >6 pt gap between lines)."""
    pdf = fitz.open(doc.pdf_path)
    res = {}
    for pno, lines in aux.meta.get("lines_by_page", {}).items():
        top, bot = header_footer_band(pdf[pno - 1])
        body = sorted((ln for ln in lines if top <= (ln.y0 + ln.y1) / 2 <= bot and ln.size >= 10),
                      key=lambda ln: (ln.y0, ln.x0))
        prev = None
        for ln in body:
            if prev is None or ln.block != prev.block or ln.y0 - prev.y1 > 6:
                res.setdefault(pno, []).append(" ".join(ln.text.split()))
            prev = ln
    pdf.close()
    return res


def split_merged_paragraphs(doc, aux):
    """Split paragraphs that the converter merged, at PDF paragraph starts: the full first line of a PDF
    paragraph (>= 4 words) found inside a body paragraph right after sentence-final punctuation.
    ch11: §11.3 intro (4 PDF paragraphs), 11.3.1, 11.3.5.2, 11.6.2 Meteorology (3) and Hydrology (2)."""
    starts = _pdf_para_starts(doc, aux)
    out = []
    n = 0
    for e in doc.els:
        if e.kind != "para":
            out.append(e)
            continue
        pieces = [(e.page, e.text)]
        for pno in (e.page, e.page + 1):
            for first in starts.get(pno, []):
                words = first.split()
                if first.endswith("-"):
                    words = words[:-1]
                if len(words) < 4:
                    continue
                pat = re.compile(r"(?<=[.:;?!”\")])\s+(" + r"\s+".join(map(re.escape, words)) + r")(?![\w])")
                new = []
                for pg, txt in pieces:
                    m = pat.search(txt)
                    if m and m.start() > 0:
                        new += [(pg, txt[:m.start()].rstrip()), (pno, txt[m.start(1):])]
                        n += 1
                    else:
                        new.append((pg, txt))
                pieces = new
        if len(pieces) == 1:
            out.append(e)
            continue
        for k, (pg, txt) in enumerate(pieces):
            meta = dict(e.meta) if k == 0 else {"split_from": e.id, "pdf_para": True}
            out.append(El("para", txt, pg if k else e.page, e.bbox, e.font, e.size, id=e.id, meta=meta))
    doc.els = out
    doc.meta["ch11_para_splits"] = n


# ------------------------------------------------------------------ lists ----
def list_markers(doc, aux=None):
    """PDF '-' sub-bullets (11.3.1, p52) keep a literal '- ' in the item text ('- - Emergency …'), and the single
    '●' bullet on p55 (11.3.5.1) was read as a paragraph."""
    for e in doc.els:
        if e.kind == "item" and re.match(r"^-\s+\S", e.text):
            e.text = re.sub(r"^-\s+", "", e.text)
        elif e.kind == "para" and re.match(r"^[●•▪]\s+\S", e.text):
            e.kind, e.level, e.list_style = "item", 0, "unordered"
            e.text = N.strip_bullet(e.text)


NUM_ITEM = re.compile(r"^(\d{1,2})\.\s+(\S.*)$", re.S)


def numbered_list(doc, aux=None):
    """11.2.1.4 technical elements 1-12 (p23-25): ODL emitted '- 1. …' double markers, flattened the bullets under
    item 7 and item 10's six paragraphs + two bullet lists, and read item 12 as a paragraph. Rebuilt as one
    Markdown ordered list, nesting by PDF x0 (numbers 90 pt, continuation paragraphs 108 pt, bullets 126 pt);
    page anchors inside the list are indented so the list is not broken. The rest of the last page's body
    paragraphs is included in the block so that no page anchor is emitted twice."""
    els = doc.els
    start = next((i for i, e in enumerate(els) if e.kind == "item" and e.page == 23 and e.text.startswith("1. ")
                  and "Operating experience review" in e.text), None)
    if start is None:
        _warn(doc, "numbered list 11.2.1.4 not found")
        return
    x_num = _x0(els[start])
    expect, cur_ind = 1, ""
    lines = []
    page = els[start].page
    j = start
    while j < len(els):
        e = els[j]
        x = _x0(e)
        if e.kind not in ("item", "para") or x is None:
            break
        m = NUM_ITEM.match(e.text.strip())
        if m and int(m.group(1)) == expect and abs(x - x_num) < 3:
            body = m.group(2)
            if e.page != page:
                lines += [cur_ind + _anchor(doc, e.page), ""]
                page = e.page
            lines += [f"{expect}. {body}", ""]
            cur_ind = " " * (len(str(expect)) + 2)
            expect += 1
        elif x > x_num + 5 and expect > 1:
            if e.page != page:
                lines += [cur_ind + _anchor(doc, e.page), ""]
                page = e.page
            if e.kind == "item":
                lines.append(cur_ind + "- " + e.text.strip())
                nxt = els[j + 1] if j + 1 < len(els) else None
                if nxt is None or nxt.kind != "item" or (_x0(nxt) or 0) <= x_num + 5 or nxt.page != e.page:
                    lines.append("")
            else:
                lines += [cur_ind + e.text.strip(), ""]
        else:
            break
        j += 1
    if expect != 13:
        _warn(doc, f"numbered list 11.2.1.4: {expect - 1} items rebuilt (expected 12)")
        return
    # trailing body elements on the same page (avoid a duplicate anchor for that page)
    while j < len(els) and els[j].page == page and els[j].kind in ("para", "item"):
        e = els[j]
        lines += [("  " * e.level + "- " if e.kind == "item" else "") + e.text.strip(), ""]
        j += 1
    block = El("raw_md", "\n".join(lines).rstrip(), els[start].page, els[start].bbox,
               meta={"ordered_list": "11.2.1.4"})
    doc.els = els[:start] + [block] + els[j:]


# ----------------------------------------------------------------- tables ----
def _cell_paras(words, rect):
    """Paragraphs of one table cell from PyMuPDF words: visual lines = words with the same vertical centre,
    a new paragraph at a vertical gap > 3 pt or at a bullet. A line-final hyphen joins without space."""
    inside = sorted((w for w in words if rect.contains(fitz.Point((w[0] + w[2]) / 2, (w[1] + w[3]) / 2))),
                    key=lambda w: (w[1] + w[3]) / 2)
    clusters = []                                   # visual lines: words whose vertical centres agree
    for w in inside:
        yc = (w[1] + w[3]) / 2
        if clusters and abs(clusters[-1]["yc"] - yc) < 3:
            clusters[-1]["words"].append(w)
        else:
            clusters.append({"yc": yc, "words": [w]})
    rows = []
    for c in clusters:
        ws = sorted(c["words"], key=lambda w: w[0])
        rows.append({"text": " ".join(w[4] for w in ws), "top": min(w[1] for w in ws),
                     "bottom": max(w[3] for w in ws), "x0": ws[0][0]})
    paras, prev = [], None
    for ln in rows:
        t = ln["text"]
        # PyMuPDF line boxes in these tables: 1.7-1.8 pt between lines of a paragraph, >= 4.7 pt between paragraphs
        if prev is None or ln["top"] - prev["bottom"] > 3.0 or t.startswith("•"):
            paras.append({"text": t, "top": ln["top"]})
        else:
            p = paras[-1]
            p["text"] = p["text"] + t if p["text"].endswith("-") else p["text"] + " " + t
        prev = ln
    return paras


def pdf_table_rows(pdf_path, pages):
    """[{'page', 'cells'}] for the single ruled table on each page; cells = one entry per column: a list of
    paragraph dicts, or None for a position covered by a column span. PyMuPDF find_tables geometry
    (pdfplumber algorithm) + PyMuPDF words (pdfplumber itself merges '10 CFR' into '10CFR' on p67)."""
    import contextlib
    import io
    rows = []
    pdf = fitz.open(pdf_path)
    try:
        for pno in pages:
            page = pdf[pno - 1]
            with contextlib.redirect_stdout(io.StringIO()):    # silence PyMuPDF's layout-package hint
                tabs = page.find_tables().tables
            if len(tabs) != 1:
                raise ValueError(f"p{pno}: {len(tabs)} tables")
            words = page.get_text("words")
            for r in tabs[0].rows:
                rows.append({"page": pno, "cells": [None if cb is None else _cell_paras(words, fitz.Rect(cb))
                                                    for cb in r.cells]})
    finally:
        pdf.close()
    return rows


def cell_text(paras):
    """Join cell paragraphs on one line: '; ' before a bullet and after a paragraph without sentence-final
    punctuation (a stage label run, a title, the last bullet of a list), else a space."""
    out = ""
    for p in paras:
        t = p["text"] if isinstance(p, dict) else p
        if not out:
            out = t
        elif t.startswith("•") or not out.rstrip().endswith(TERMINAL):
            out += "; " + t
        else:
            out += " " + t
    return out


def _norm(t, aux):
    return N.text_pipeline(t, None, aux.hyphen_map if aux else None)


def _render(header, rows):
    esc = lambda s: s.replace("|", "\\|")
    lines = ["| " + " | ".join(header) + " |", "|" + "---|" * len(header)]
    lines += ["| " + " | ".join(esc(c) for c in r) + " |" for r in rows]
    return "\n".join(lines)


def _table_el(doc, cap_prefix, pages):
    """Replace every table element on `pages` by the first one; returns it (or None)."""
    first, out = None, []
    for e in doc.els:
        if e.kind == "table" and set(e.table.pages or [e.page]) <= set(pages):
            if first is None:
                first = e
                out.append(e)
            continue
        out.append(e)
    if first is None or not first.table.caption.startswith(cap_prefix):
        _warn(doc, f"{cap_prefix}: table element not found on p{pages[0]}-{pages[-1]}")
        return None
    doc.els = out
    return first


def _grid(rows_txt, header):
    grid = [[T.Cell(h, 0, j, bold=True) for j, h in enumerate(header)]]
    for i, r in enumerate(rows_txt, 1):
        grid.append([T.Cell(v, i, j) for j, v in enumerate(r)])
    return grid


def table_11_5_1(doc, aux):
    """Table 11.5-1 (7 sheets, p67-73) from pdfplumber cells. Fixes: row 5.0 (ODL cut the spanning cell at the
    column rules into 12 rows x 3 columns, 14 words split, 3 letters doubled); rows 1.0-5.0 are one cell spanning
    Section Name..Basis: the printed title line (1.0-3.0) goes to Section Name and the text once to
    Variable or Condition (no triple fill-right); bullet/paragraph boundaries kept ('• PSP leakage; The PHT …')."""
    pages = list(range(67, 74))
    e = _table_el(doc, "Table 11.5-1", pages)
    if e is None:
        return
    rows = pdf_table_rows(doc.pdf_path, pages)
    header = [cell_text(c) for c in rows[0]["cells"]]
    body = []
    for r in rows:
        cells = r["cells"]
        texts = [cell_text(c) if c is not None else None for c in cells]
        if texts == header:
            continue          # repeated sheet header
        if cells[2] is None and cells[3] is None:        # spanning section-introduction row
            paras = [p["text"] for p in cells[1]]
            title = ""
            if len(paras) > 1 and not paras[0].endswith(TERMINAL) and len(paras[0]) < 80:
                title, paras = paras[0], paras[1:]
            row = [texts[0], title, cell_text(paras), ""]
        else:
            row = [t or "" for t in texts]
        body.append([_norm(x, aux) for x in row])
    t = e.table
    header = [_norm(h, aux) for h in header]
    t.grid, t.header_rows, t.pages = _grid(body, header), 1, pages
    e.meta["rendered"] = _render(header, body)
    e.meta["ch11_rows"] = [r[0] for r in body]


def table_11_2_2(doc, aux):
    """Table 11.2-2 (4 sheets, p47-50) from pdfplumber cells: stage paragraphs kept apart ('…for analysis;
    HF in Preliminary Design: …'); the 11.2.5 / 11.2.1.10 double row (one cell pair, no rule between them)
    split into two rows sharing the NUREG-0711 cell (fill-down)."""
    pages = list(range(47, 51))
    e = _table_el(doc, "Table 11.2-2", pages)
    if e is None:
        return
    rows = pdf_table_rows(doc.pdf_path, pages)
    header = [cell_text(c) for c in rows[0]["cells"]]
    body = []
    for r in rows:
        cells = [c or [] for c in r["cells"]]
        texts = [cell_text(c) for c in cells]
        if texts == header:
            continue
        secs = [p["text"] for p in cells[0]]
        if len(secs) > 1 and all(re.fullmatch(r"\d+(?:\.\d+)+", s) for s in secs) and len(cells[1]) == len(secs):
            for k, s in enumerate(secs):
                sub = [s, cells[1][k]["text"]]
                for c in cells[2:]:
                    sub.append(cell_text(c) if len(c) != len(secs) else c[k]["text"])
                body.append(sub)
            continue
        body.append(texts)
    body = [[_norm(x, aux) for x in row] for row in body]
    t = e.table
    header = [_norm(h, aux) for h in header]
    t.grid, t.header_rows, t.pages = _grid(body, header), 1, pages
    e.meta["rendered"] = _render(header, body)
    e.meta["ch11_rows"] = [r[0] for r in body]


def table_11_5_2_notes(doc, aux):
    """Table 11.5-2: 7.7-pt note markers '(1)', '(2)' (NSS, IAC and the two notes) -> <sup>(n)</sup>."""
    sups = {s.sup for s in aux.sups.get(74, [])}
    for e in doc.els:
        if e.kind != "table" or not e.table.caption.startswith("Table 11.5-2"):
            continue
        for row in e.table.grid:
            for c in row:
                m = re.fullmatch(r"(.*\S)\s*(\(\d\))", c.text.strip())
                if m and m.group(2) in sups:
                    c.text = f"{m.group(1)}<sup>{m.group(2)}</sup>"
        e.table.notes = [re.sub(r"^(\(\d\))\s+", lambda m: f"<sup>{m.group(1)}</sup> " if m.group(1) in sups
                                else m.group(0), n) for n in e.table.notes]
        return
    _warn(doc, "Table 11.5-2 not found")


def section_number_cells(doc, aux=None):
    """A table cell whose lines are each a bare section number ('11.2.6.1' / '11.2.6.2' / '11.2.6.3' in
    Table 11.2-1 row 11) is an enumeration, not a wrapped sentence: join with '; ' (plan §3 "enumeration
    separators stay '; '"). Written into the cell text so the rendering does not depend on tables.ENUM."""
    n = 0
    for e in doc.els:
        if e.kind != "table" or e.table is None:
            continue
        for row in e.table.grid:
            for c in row:
                lines = [ln.strip() for ln in c.text.splitlines() if ln.strip()]
                if len(lines) > 1 and all(re.fullmatch(r"\d+(?:\.\d+)+", ln) for ln in lines):
                    c.text = "; ".join(lines)
                    n += 1
    doc.meta.setdefault("ch11_qa", {})["section_number_cells"] = n


def qa_metrics(doc, aux=None):
    qa = doc.meta.setdefault("ch11_qa", {})
    qa["paragraph_splits"] = doc.meta.get("ch11_para_splits", 0)
    qa["numbered_headings"] = sum(1 for e in doc.els if e.kind == "heading" and e.meta.get("numbered"))
    for e in doc.els:
        if e.kind == "table" and e.table is not None and e.table.caption.startswith(("Table 11.5-1", "Table 11.2-2")):
            qa[e.table.caption.split()[1] + "_rows"] = e.table.n_rows - e.table.header_rows
    qa["withheld"] = doc.meta.get("withheld", [])


STEPS = [
    drop_noise,
    check_expected_headings,
    bold_subheads,
    withheld_section,
    split_glued_references,
    split_merged_paragraphs,
    list_markers,
    numbered_list,
    table_11_2_2,
    table_11_5_1,
    table_11_5_2_notes,
    section_number_cells,
    qa_metrics,
]
