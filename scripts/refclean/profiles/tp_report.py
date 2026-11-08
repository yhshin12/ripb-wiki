"""TerraPower report profile (public versions of TP-LIC-RPT-0011 and the NAT-3049 white paper): the generic pipeline
with TerraPower page furniture, numbered headings and redaction brackets. Per-document differences are in CONFIG.

- NAT-3049: the PDF is the transmittal letter, the withholding affidavit and the enclosure cover (p.1-5) followed by
  the white paper (p.6-26, "Page N of 21"); its document control table on p.6 survives conversion. Bracket labels
  also read "(a)(4)(ECI)", and figure captions "Figure 5. Title".

- The document control table on p.2 is lost by the converter and is read from the PDF (control_table).
- Page 1 is the enclosure cover ("ENCLOSURE 5 … Public") and is dropped. Every later page carries a running header
  table ("TP-LIC-RPT-0011 Rev 0 | <title> | Page N of 93"), the lines "Not Confidential" and "Controlled Document -
  Verify Current Revision", and the DOE agreement / copyright footer; all are dropped. "Page N of 93" becomes the
  printed page label N.
- Numbered section headings ("4.1.2.4 Hot Channel Factors") are set in the body font and are found from the PDF
  lines for every chapter number (as in the SER profile).
- Proprietary text is withheld with "[[ … ]](a)(4),ECI" (the label is "(a)(4)" in a few places). The public version
  keeps the brackets and drops the text. Each closing bracket (one run of withheld text) becomes one "> [!withheld] (a)(4),ECI" callout;
  public text before or after a bracket stays. "10 CFR 50.34(a)(4)" in body text is not a bracket label.
  A table row whose cells hold nothing but brackets is dropped and a callout follows the table.
- Figure captions read "Figure 4-1: Title" (colon). A figure whose box holds a bracket label is withheld: its caption
  stays as a heading and a callout replaces the image.
"""
import re

import fitz

from .. import structure as S
from ..doc import El
from ..figures import figures_step
from ..levels import assign_levels
from ..pdfaux import LEADER, FigureRef, HeadingRef, figure_box
from . import generic, ser

META = {k: generic.META[k] for k in ("TP-LIC-RPT-0011", "NAT-3049")}
CONFIG = {
    "TP-LIC-RPT-0011": {"drop_pages": {1}, "control_table_page": 2},
    "NAT-3049": {"drop_pages": set(), "control_table_page": 6},
}

MAX_CHAPTER = 8
KEEP_HEADINGS = {"REVISION HISTORY", "ACRONYMS", "END OF DOCUMENT"}
HEADER_CELL = re.compile(r"^(?:TP-LIC-RPT-\d{4} Rev \d+|NAT-\d{4}(?: Rev \d+)?)$")
PAGE_LABEL = re.compile(r"^Page (\d+) of \d+$")
CONTROL_PAGE = re.compile(r"Page:\s*(\d+) of \d+")
FURNITURE = re.compile(r"^(?:Not Confidential\s*)?(?:Controlled Document - Verify Current Revision)?$|"
                       r"^SUBJECT TO DOE COOPERATIVE AGREEMENT|^Copyright © \d{4} TerraPower")
OPEN = r"\[\["
LABEL = r"\(a\)\(4\)?(?:,\s*ECI|\(ECI\))?"     # NAT-3049 p.12 prints "]](a)(4" (no closing parenthesis)
CLOSE = rf"\]\]\s*({LABEL})"
BARE = re.compile(rf"^\s*({LABEL})\s*$")
MARK = re.compile(rf"{OPEN}|{CLOSE}")
LEGEND = re.compile(r"redacted information is identified using")
EMPTY_PAIR = re.compile(r"\[\[\s*\]\]")
HEAD = re.compile(r"^(\d(?:\.\d+)*)\s+(\S.*?)\s*$")
FIG_CAP = re.compile(r"^Figure\s+(\d+(?:-\d+)?)[:.]\s+(\S.*)$")
FIG_TXT = re.compile(r"^Figure\s+(\d+(?:-\d+)?)[:.]\s*(.*)$")


def callout(label, page):
    label = re.sub(r",\s*", ",", label)
    return El("raw_md", f"> [!withheld] {label}", page, meta={"withheld": True})


def toc_continuation(doc, aux):
    """The list of figures runs on to p.6 with two dotted-leader lines, too few for pdfaux.is_toc_page."""
    lines = aux.meta.get("lines_by_page", {})
    for pno in sorted(lines):
        if pno - 1 in aux.toc_pages and any(LEADER.search(l.text) for l in lines[pno]):
            aux.toc_pages.add(pno)


def drop_cover(doc, aux=None):
    S.drop_pages(doc, CONFIG[doc.key]["drop_pages"])


def page_labels(doc, aux=None):
    pdf = fitz.open(doc.pdf_path)
    for page in pdf:
        top = page.rect.height * 0.08
        for b in page.get_text("blocks"):
            if b[1] < top:
                for line in b[4].splitlines():
                    m = PAGE_LABEL.match(line.strip())
                    if m:
                        doc.page_labels[page.number + 1] = m.group(1)
        if page.number + 1 not in doc.page_labels:    # a document control table: "Page: 1 of 21"
            m = CONTROL_PAGE.search(page.get_text())
            if m:
                doc.page_labels[page.number + 1] = m.group(1)
    pdf.close()


def control_table(doc, aux=None):
    """The document control table (number, title, dates, approvals; TP-LIC-RPT-0011 p.2, NAT-3049 p.6), which the
    converter drops: read with PyMuPDF and emitted as one line per table row, empty cells left out."""
    cpage = CONFIG[doc.key]["control_table_page"]
    if cpage is None:
        return
    pdf = fitz.open(doc.pdf_path)
    tabs = pdf[cpage - 1].find_tables().tables
    pdf.close()
    if not tabs:
        return
    rows = []
    for row in tabs[0].extract():
        cells = [" ".join(c.split()) for c in row if c]
        if cells:
            rows.append("- " + " | ".join(cells))
        m = CONTROL_PAGE.search(" ".join(cells))
        if m:
            doc.page_labels[cpage] = m.group(1)
    md = (f"<!-- source: PDF p.{cpage} document control table, read with PyMuPDF (one line per row) -->\n"
          + "\n".join(rows))
    i = next((k for k, e in enumerate(doc.els) if e.page > cpage), len(doc.els))
    doc.els.insert(i, El("raw_md", md, cpage))


def drop_furniture(doc, aux=None):
    out = []
    for e in doc.els:
        if e.kind == "table" and e.table.grid and (
                HEADER_CELL.match(e.table.grid[0][0].text.strip())
                or FURNITURE.match(" ".join(" ".join(c.text for row in e.table.grid for c in row).split()))):
            continue
        if e.kind == "heading" and not e.text.strip():
            continue
        if e.kind in ("para", "item", "heading", "caption", "hdr") and (
                FURNITURE.match(" ".join(e.text.split())) or HEADER_CELL.match(e.text.strip())
                or PAGE_LABEL.match(e.text.strip())):
            continue
        out.append(e)
    doc.els = out


def headings(doc, aux, max_chapter=MAX_CHAPTER):
    """Numbered headings of chapters 1-8 from the PDF lines: '1 INTRODUCTION' (chapter, capitals) and
    '4.1.2.4 Hot Channel Factors'. Each depth has its own indent (x 25, 47, 101, 119 pt) and the heading line shares
    a text block with the body below it, so pdfaux.numbered_headings (body margin, block-wrap rule) does not fit.
    A heading is one line, starts with a capital, is not a sentence, and lies outside the TOC pages."""
    refs = []
    for pno, lines in sorted(aux.meta.get("lines_by_page", {}).items()):
        if pno in aux.toc_pages:
            continue
        for ln in lines:
            m = HEAD.match(ln.text)
            if not m or LEADER.search(ln.text) or int(m.group(1).split(".")[0]) > max_chapter:
                continue
            num, title = m.group(1), m.group(2).split("[[")[0].strip()
            if "." not in num and not title.isupper():
                continue    # chapter titles are capitals; '1 a TerraPower …' is a footnote
            if not title and "." in num and m.group(2).startswith("[["):
                pass        # the title itself is withheld ('3.1.1 [[')
            elif not title[:1].isupper() or title.endswith(".") or len(title) > 100:
                continue
            refs.append(HeadingRef(num, " ".join(title.split()), pno, len(num.split("."))))
    aux.headings = refs


def _pieces(e):
    """Split a text element at bracket marks: [(text, None)] for public text, [(None, label)] for a closed run."""
    out, pos = [], 0
    for m in MARK.finditer(e.text):
        before = e.text[pos:m.start()].strip()
        if before:
            out.append((before, None))
        if m.group(1):
            out.append((None, m.group(1)))
        pos = m.end()
    rest = e.text[pos:].strip()
    if rest:
        out.append((rest, None))
    return out


def _cell_withheld(text):
    t = MARK.sub(" ", text)
    return not t.strip() or bool(BARE.match(t))


def withheld(doc, aux=None):
    out = []
    for e in doc.els:
        if e.kind in ("para", "item") and LEGEND.search(e.text):
            e.text = EMPTY_PAIR.sub("`[[ ]]`", e.text)    # the transmittal letter explains the marks: keep as text
            out.append(e)
            continue
        if e.kind == "table" and any("`[[" in c.text for r in e.table.grid for c in r):
            out.append(e)       # cells already rebuilt with the marks as code spans (tp_slides.slide_tables)
            continue
        if e.kind == "table":
            rows = e.table.grid
            keep = [r for r in rows if not all(_cell_withheld(c.text) for c in r)]
            if any(MARK.search(c.text) for r in rows for c in r):
                for r in keep:
                    for c in r:
                        c.text = MARK.sub(" ", c.text).strip()
                e.table.grid = keep
                if keep:            # an emptied table must not take the caption above it with it
                    out.append(e)
                out.append(callout("(a)(4)", e.page))
            else:
                out.append(e)
            continue
        if e.kind not in ("para", "item", "heading", "caption", "hdr"):
            out.append(e)
            continue
        m = BARE.match(e.text)
        if m:
            out.append(callout(m.group(1), e.page))
            continue
        if not MARK.search(e.text):
            out.append(e)
            continue
        first = True
        for text, label in _pieces(e):
            if label:
                out.append(callout(label, e.page))
            else:
                kind = e.kind if first else "para"
                out.append(El(kind, text, e.page, e.bbox, e.font, e.size, e.level if first else 0,
                              e.list_style if first else "", id=e.id, meta=dict(e.meta)))
                first = False
    doc.els = out


def figures(doc, aux, fig_cap=FIG_CAP, fig_txt=FIG_TXT, is_caption=lambda ln, page: True):
    """Figure refs for colon captions. A withheld figure is an empty frame with a bracket label ('(a)(4)' alone on a
    line) at its right edge, between the previous caption on the page and its own caption."""
    pdf = fitz.open(doc.pdf_path)
    refs = []
    for pno, lines in aux.meta.get("lines_by_page", {}).items():
        if pno in aux.toc_pages:
            continue
        above = 0.0
        for ln in sorted(lines, key=lambda l: l.y0):
            m = fig_cap.match(ln.text)
            if not m or not is_caption(ln, pdf[pno - 1]):
                continue    # body sentences cite figures without the colon ('Figure 2-1 provides …')
            cap = fitz.Rect(ln.x0, ln.y0, ln.x1, ln.y1)
            x0, y0, x1, y1 = figure_box(pdf[pno - 1], cap)
            box = (x0, max(y0, above), x1, min(y1, cap.y1 + 6))    # a figure ends at its caption
            labels = [BARE.match(l.text).group(1) for l in lines if BARE.match(l.text) and above <= l.y0 < ln.y0]
            title = " ".join(MARK.sub(" ", m.group(2)).split())
            refs.append(FigureRef(m.group(1), title, pno, box, withheld=bool(labels)))
            if labels:
                aux.meta.setdefault("figure_labels", {})[m.group(1)] = labels[-1]
            above = ln.y1
    pdf.close()
    aux.figures = refs
    _split_captions(doc, refs, fig_txt)
    figures_step(doc, aux, render=aux.meta.get("render_figures", True), fig_txt=fig_txt)


def _split_captions(doc, refs, fig_txt=FIG_TXT):
    """A caption the converter glued to the next body line ('Figure 1. Natrium Type 1 Assembly Sketch The fuel
    assemblies include') is cut after the caption text read from the PDF line."""
    out = []
    for e in doc.els:
        t = " ".join(e.text.split()) if e.kind in ("para", "caption") else ""
        m = fig_txt.match(t)
        ref = next((r for r in refs if m and r.page == e.page and r.num == m.group(1) and r.caption), None)
        cut = t.find(ref.caption) + len(ref.caption) if ref and ref.caption in t else -1
        if cut > 0 and t[cut:].strip():
            out.append(El(e.kind, t[:cut], e.page, e.bbox, e.font, e.size, e.level, e.list_style, id=e.id,
                          meta=dict(e.meta)))
            out.append(El("para", t[cut:].strip(), e.page, e.bbox, e.font, e.size, id=e.id, meta={"split_from": e.id}))
        else:
            out.append(e)
    doc.els = out


def figure_levels(doc, aux=None):
    """Figure numbers carry only the chapter ('4-1'), so a figure heading goes one level below the section heading
    above it instead of below the chapter."""
    cur = 1
    for e in doc.els:
        if e.kind == "heading" and e.meta.get("numbered"):
            cur = e.level
        elif e.kind == "heading" and e.meta.get("figure"):
            e.level = min(cur + 1, 6)


def withheld_figure_callouts(doc, aux=None):
    held = {r.num for r in aux.figures if r.withheld}
    out = []
    for e in doc.els:
        out.append(e)
        if e.kind == "heading" and e.meta.get("figure") in held:
            out.append(callout(aux.meta.get("figure_labels", {}).get(e.meta["figure"], "(a)(4)"), e.page))
    doc.els = out


def steps():
    return [
        toc_continuation,
        drop_cover,
        page_labels,
        drop_furniture,
        control_table,
        headings,
        ser.bracket_closers_are_body,
        S.drop_toc,
        withheld,
        figures,
        withheld_figure_callouts,
        S.promote_headings,
        S.insert_subheads,
        lambda d, a: S.demote_other_headings(d, a, keep=lambda e: e.text.strip() in KEEP_HEADINGS),
        S.fix_false_items,
        S.join_breaks,
        S.attach_captions_and_merge,
        S.attach_table_notes,
        S.normalise_text,
        S.references_as_items,
        S.normalise_item_levels,
        assign_levels,
        figure_levels,
    ]


def metadata(doc, aux):
    m = generic.metadata(doc, aux)
    m["headings_found"] = len(aux.headings)
    return m
