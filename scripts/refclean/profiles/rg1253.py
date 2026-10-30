"""RG 1.253 profile: the generic pipeline, plus Appendix A Tables A-2 and A-3 rebuilt from the PDF.

Tables A-2 (4 sheets, PDF p.39-42) and A-3 (6 sheets, p.43-48) are printed newspaper-style: four columns per page, each
a running list of PRA element labels ('C.1.3.2 (IE)', bold), high-level requirement labels ('HLR-IE-A', underlined)
and supporting requirements with their entry ('IE-A1  Yes'). The list runs down column 1, then column 2, and on to the
next sheet. The converter makes one cell of each column, so the requirement-entry pairs run together in one line.

column_tables replaces each such table with one table per sheet (citations stay on their page) whose rows are
(PRA element | High-level requirement | Supporting requirement | Entry), read from the PDF spans in reading order; the
element and HLR of a row carry over from the labels above it, across columns and sheets. The PDF prints no header
row; the supplied one takes its words from the notes on p.38 and is marked with an editorial comment. The sheet
caption is taken from the bold lines above the columns verbatim. The first caption line of Table A-3 sheet 6 is printed
at the foot of p.47, below the columns: a bold line below the columns opens the next sheet's caption, with a comment.
"""
import re

import fitz

from .. import structure as S
from .. import tables as T
from ..doc import El
from ..figures import figures_step
from ..levels import assign_levels
from ..tables import Cell, Table
from . import generic

META = {"RG_1.253": generic.META["RG_1.253"]}

SHEET_RE = re.compile(r"Applicability of ASME/ANS Non-LWR PRA Standard .*\((\d+) of (\d+)\)\s*$")
ELEMENT_RE = re.compile(r"^C\.1\.3\.\d+ \([A-Z]+\)$")
HLR_RE = re.compile(r"^HLR-[A-Z]+-[A-Z]$")
SR_RE = re.compile(r"^([A-Z]+-[A-Z]\d+)(?:\s+(Yes|CC-II|CC-I))?$")
HEADER = ["PRA element", "High-level requirement", "Supporting requirement", "Entry"]
FOOTER_Y = 735


def _caption_of(table):
    first = " ".join(c.text for c in table.grid[0]) if table.grid else ""
    return SHEET_RE.search(first)


def _sheet(page):
    """(caption, [(column, y, text)], foot) of one sheet page; a line is the spans of one column at one baseline;
    foot is bold text below the columns (the next sheet's caption start)."""
    spans = []
    for b in page.get_text("dict")["blocks"]:
        for ln in b.get("lines", []):
            for s in ln["spans"]:
                if s["text"].strip() and s["bbox"][1] < FOOTER_Y:
                    spans.append((s["bbox"][1], s["bbox"][0], "Bold" in s["font"], s["text"].strip()))
    spans.sort()
    body_top = min(y for y, x, bold, t in spans if ELEMENT_RE.match(t) or HLR_RE.match(t) or SR_RE.match(t))
    caption = " ".join(t for y, x, bold, t in spans if y < body_top - 1 and bold)
    body_end = max(y for y, x, bold, t in spans if ELEMENT_RE.match(t) or HLR_RE.match(t) or SR_RE.match(t))
    foot = " ".join(t for y, x, bold, t in spans if y > body_end + 1 and bold)
    body = [s for s in spans if body_top - 1 <= s[0] <= body_end + 1]
    starts = sorted({round(x) for y, x, bold, t in body if ELEMENT_RE.match(t) or HLR_RE.match(t) or SR_RE.match(t)})
    cols = [x for i, x in enumerate(starts) if i == 0 or x - starts[i - 1] > 40]
    lines = {}
    for y, x, bold, t in body:
        c = max(i for i, cx in enumerate(cols) if x >= cx - 2)
        key = next((k for k in lines if k[0] == c and abs(k[1] - y) < 3), (c, y))
        lines.setdefault(key, []).append((x, t))
    return caption, [(c, y, " ".join(t for x, t in sorted(parts))) for (c, y), parts in sorted(lines.items())], foot


def column_tables(doc, aux):
    """Tables A-2 and A-3: one (element | HLR | SR | entry) table per sheet; see the module docstring."""
    if not any(e.kind == "table" and _caption_of(e.table) for e in doc.els):
        return
    pdf = fitz.open(doc.pdf_path)
    state = {}                                    # table number -> [element, hlr], carried across sheets
    unparsed, rebuilt = [], []
    out, carried = [], None                       # carried: (page, text) of a caption start below the columns
    for e in doc.els:
        m = _caption_of(e.table) if e.kind == "table" else None
        if not m:
            out.append(e)
            continue
        caption, lines, foot = _sheet(pdf[e.page - 1])
        source = ""
        if carried:
            caption = carried[1] + " " + caption
            source = f"<!-- source: the caption's first line is printed at the foot of p.{carried[0]} -->\n\n"
        carried = (e.page, foot) if foot else None
        tno = "A-2" if "Minimally Acceptable" in caption else "A-3"
        if m.group(1) == "1":
            state[tno] = [None, None]
        elem, hlr = state[tno]
        grid = [[Cell(h, 0, i, bold=True) for i, h in enumerate(HEADER)]]
        for c, y, text in sorted(lines, key=lambda x: (x[0], x[1])):
            if ELEMENT_RE.match(text):
                elem, hlr = text, None
            elif HLR_RE.match(text):
                hlr = text
            elif SR_RE.match(text):
                sr, entry = SR_RE.match(text).groups()
                r = len(grid)
                grid.append([Cell(elem or "", r, 0, filled=True), Cell(hlr or "", r, 1, filled=True),
                             Cell(sr, r, 2), Cell(entry or "", r, 3)])
            else:
                unparsed.append(f"p{e.page}: {text}")
        state[tno] = [elem, hlr]
        tab = Table(grid=grid, header_rows=1, page=e.page, pages=[e.page], caption=caption)
        note = (f"<!-- header row supplied: the PDF prints this table without one; words from the notes on p.38 "
                f"(p.{e.page}) -->")
        out.append(El("table", "", e.page, e.bbox, table=tab, id=e.id,
                      meta={"header_supplied": True, "rendered": source + note + "\n\n" + T.render_md(tab)}))
        rebuilt.append({"page": e.page, "table": tno, "rows": len(grid) - 1})
    pdf.close()
    doc.els = out
    doc.meta["column_tables"] = rebuilt
    doc.meta["column_tables_unparsed"] = unparsed


def steps():
    return [
        S.drop_toc,
        S.withheld_callouts,
        lambda d, a: figures_step(d, a, render=a.meta.get("render_figures", True)),
        S.promote_headings,
        S.insert_subheads,
        S.fix_false_items,
        S.join_breaks,
        S.attach_captions_and_merge,
        column_tables,
        S.attach_table_notes,
        S.normalise_text,
        S.references_as_items,
        S.normalise_item_levels,
        assign_levels,
    ]


def metadata(doc, aux):
    m = generic.metadata(doc, aux)
    m["column_tables"] = [f"Table {t['table']} p{t['page']}: {t['rows']} rows"
                          for t in doc.meta.get("column_tables", [])]
    return m
