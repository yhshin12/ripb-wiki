"""Approved TerraPower topical reports (NAT-9390-A, NAT-9394-A, NAT-9395-A; public versions). One PDF holds three parts:

- p.1-6: transmittal letter, withholding affidavit, enclosure cover, -A cover.
- SE part: the NRC approval letter and final safety evaluation. Authority differs from the report, and its section
  numbers overlap the report's, so a heading "# NRC Safety Evaluation" opens the part and notes cite "[KEY SE §n p.N]".
  Pages carry "OFFICIAL USE ONLY – …" banners and "- N -" (printed page label N).
  Brackets are "[[ ]]" without a label and may run across a page. All text between them is dropped, including the
  words the public version left inside a pair (NAT-9394-A SE p.26): marked proprietary, so never public text here.
- Report part: as tp_report (running header "NAT-9390 Rev 2 | title | Page N of 98"), with labelled brackets.
  Figure captions read "Figure 1-1.", "Figure 2.2-1." or "Figure 5-17 Title" (no colon).
"""
import re

import fitz

from .. import structure as S
from ..doc import El
from ..levels import assign_levels
from . import generic, ser, tp_report as TP

CONFIG = {
    "NAT-9390-A": {"se": (7, 53), "control_table_page": 54, "drop_pages": set()},
    "NAT-9394-A": {"se": (7, 28), "control_table_page": 29, "drop_pages": set()},
    "NAT-9395-A": {"se": (7, 35), "control_table_page": 36, "drop_pages": set()},
}
TP.CONFIG.update(CONFIG)

MAX_CHAPTER = 9
BANNER = re.compile(r"^(?:OFFICIAL USE ONLY\s*[–-][^\n]*?(?:INFORMATION)\s*)+(?:Enclosure\s*)?$")
SE_PAGE = re.compile(r"^-\s*(\d+)\s*-$")
REPORT_RUNNING = re.compile(r"^NAT-\d{4} Rev \d+$|^Not Proprietary$|^Verify Current Revision$")
FIG_CAP = re.compile(r"^Figure\s+(\d+(?:\.\d+)?(?:-\d+)?)(?:[:.]\s+|\s+(?=[A-Z\[]))(\S.*)$")
FIG_TXT = re.compile(r"^Figure\s+(\d+(?:\.\d+)?(?:-\d+)?)(?:[:.]\s*|\s+(?=[A-Z\[]))(.*)$")
SE_MARK = re.compile(rf"\[\[|\]\]\s*({TP.LABEL})?")
UNLABELLED = "(no label)"


SE_HEADS = {"REGULATORY EVALUATION", "TECHNICAL EVALUATION", "LIMITATIONS AND CONDITIONS", "CONCLUSION", "REFERENCES"}
SE_SUBHEAD = re.compile(r"^(?:INTRODUCTION|EMDAP Element \d: .+|Relationship to Other TerraPower TRs)$")
FURNITURE_LINE = re.compile(r"^(?:Not (?:Proprietary|Confidential)\s*)?(?:Controlled Document - Verify Current Revision)?$|"
                            r"^Verify Current Revision$")
OPEN_S, CLOSE_S = "", ""     # legend marks in the letter, hidden from the withheld step
NOT_HEADING = {"NAT-9394-A": re.compile(r"^3\.(?:[2-9]|1\d)$")}     # report §3.1 is a numbered list of assumptions
TABLE_CAP = re.compile(r"^Table \d+-\d+\.?\s+\S")
TABLE_HEAD = re.compile(r"^(?:Parameter |Event Type |Geometric Parameters|Blockage Parameters|Fuel Properties)")
BARE_CLOSE = re.compile(r"\]\](?!\s*\(+a\))")
PAIR_WITH_TEXT = re.compile(r"\[\[((?:(?!\[\[|\]\]).)*)\]\]", re.S)


def se_range(doc):
    return CONFIG[doc.key]["se"]


def in_report(doc, page):
    return page > se_range(doc)[1]


def is_text(e):
    return e.kind in ("para", "item", "heading", "caption", "hdr")


def centred(ln, page):
    """Captions are centred; a body line that starts with 'Figure 5-6. It has …' is not."""
    return abs((ln.x0 + ln.x1) / 2 - page.rect.width / 2) < 30


def protect_legend(doc, aux=None):
    """The letter (p.1-2) explains the marks; they stay as code spans and must not reach the withheld steps."""
    for e in doc.els:
        if e.page <= 2 and is_text(e):
            e.text = TP.EMPTY_PAIR.sub(f"`{OPEN_S} {CLOSE_S}`", e.text)
            e.text = re.sub(r"(?<!`)\[\[", f"`{OPEN_S}`", e.text)
            e.text = re.sub(r"\]\](?!`)", f"`{CLOSE_S}`", e.text)


def restore_legend(doc, aux=None):
    for e in doc.els:
        if e.kind in ("para", "item", "heading", "caption", "hdr") and e.page <= 2:
            e.text = e.text.replace(OPEN_S, "[[").replace(CLOSE_S, "]]")


def report_brackets(doc, aux=None):
    """Report part, before tp_report.withheld: normalise the '((a)(4)' slip, drop text inside a same-element pair,
    and turn a close without a label into a callout."""
    dropped, out = [], []
    for e in doc.els:
        if not is_text(e) or e.page <= 2 or not in_report(doc, e.page):
            out.append(e)
            continue
        e.text = e.text.replace("]]((a)", "]](a)")

        def clean(m):
            dropped.append((e.page, " ".join(m.group(1).split())))
            return "[[ ]]"
        e.text = PAIR_WITH_TEXT.sub(lambda m: m.group(0) if not re.search(r"\w", m.group(1)) else clean(m), e.text)
        pos, first = 0, True
        for m in BARE_CLOSE.finditer(e.text):
            before = e.text[pos:m.start()].replace("[[", " ").strip()
            if before:
                out.append(El(e.kind if first else "para", before, e.page, e.bbox, e.font, e.size,
                              e.level if first else 0, e.list_style if first else "", id=e.id, meta=dict(e.meta)))
                first = False
            out.append(TP.callout(UNLABELLED, e.page))
            pos = m.end()
        if pos == 0:
            out.append(e)
            continue
        after = e.text[pos:].strip()
        if after:
            out.append(El(e.kind if first else "para", after, e.page, e.bbox, e.font, e.size,
                          e.level if first else 0, e.list_style if first else "", id=e.id, meta=dict(e.meta)))
    doc.els = out
    doc.meta["report_dropped"] = dropped


def report_page_labels(doc, aux=None):
    """Landscape sheets carry 'Page N of M' outside the top band that tp_report.page_labels reads."""
    pdf = fitz.open(doc.pdf_path)
    for page in pdf:
        pno = page.number + 1
        if in_report(doc, pno) and pno not in doc.page_labels:
            m = re.search(r"Page (\d+) of \d+", page.get_text())
            if m:
                doc.page_labels[pno] = m.group(1)
    pdf.close()


def withheld_table_captions(doc, aux=None):
    """A table withheld whole has no table element for its caption to attach to, and attach_captions_and_merge would
    hand the caption to a later table. Keep such a caption as a plain line above its callout."""
    els = doc.els
    for i, e in enumerate(els):
        if is_text(e) and TABLE_CAP.match(" ".join(e.text.split())):
            for nxt in els[i + 1:i + 4]:
                if nxt.kind == "table":
                    break
                if nxt.kind == "raw_md" and nxt.meta.get("withheld"):
                    e.kind, e.text = "raw_md", " ".join(e.text.split())
                    break


def se_structure(doc, aux=None):
    """Unnumbered SE headings, and report table header rows the converter tagged as headings. Runs last so that the
    page anchors stay above them."""
    lo, hi = se_range(doc)
    for e in doc.els:
        if e.kind == "heading" and in_report(doc, e.page) and TABLE_HEAD.search(e.text) and not e.meta.get("numbered"):
            e.kind, e.level = "para", 0
        if not lo <= e.page <= hi or not is_text(e):
            continue
        t = " ".join(e.text.split())
        if e.kind == "heading" and t.startswith("DISTRIBUTION"):
            e.kind, e.level = "para", 0
        elif t in SE_HEADS or SE_SUBHEAD.match(t):
            e.kind, e.text = "raw_md", f"{'##' if t in SE_HEADS else '###'} {t}"


def se_page_labels(doc, aux=None):
    lo, hi = se_range(doc)
    for pno, lines in aux.meta.get("lines_by_page", {}).items():
        if lo <= pno <= hi:
            for ln in lines:
                m = SE_PAGE.match(ln.text.strip())
                if m:
                    doc.page_labels[pno] = m.group(1)
                    break


def drop_furniture(doc, aux=None):
    TP.drop_furniture(doc, aux)
    lo, hi = se_range(doc)
    out = []
    for e in doc.els:
        t = " ".join(e.text.split()) if is_text(e) else ""
        if t and (BANNER.match(t) or REPORT_RUNNING.match(t) or FURNITURE_LINE.match(t)
                  or (lo <= e.page <= hi and (SE_PAGE.match(t) or t == "Enclosure"))):
            continue
        if e.kind == "table" and e.table.grid:
            cells = " ".join(" ".join(c.text for c in row) for row in e.table.grid)
            if BANNER.match(" ".join(cells.split())):
                continue
            e.table.grid = [r for r in e.table.grid if not any("SUBJECT TO DOE" in c.text for c in r)]
            if not e.table.grid:
                continue
        out.append(e)
    doc.els = out
    # the running lines sit inside the verify band on these reports: credit what was dropped on purpose
    credit = doc.meta.setdefault("sheet_credit", [])
    for pno, lines in aux.meta.get("lines_by_page", {}).items():
        if pno > hi:
            credit += [ln.text for ln in lines if ln.text.strip() and FURNITURE_LINE.match(ln.text.strip())]


def se_withheld(doc, aux=None):
    """SE part only: every run between '[[' and ']]' becomes one callout, across elements and pages if it must."""
    lo, hi = se_range(doc)
    out, inside, dropped = [], False, []
    for e in doc.els:
        if not lo <= e.page <= hi or e.kind not in ("para", "item", "heading", "caption", "hdr"):
            out.append(e)
            continue
        pieces, pos = [], 0
        for m in SE_MARK.finditer(e.text):
            seg = e.text[pos:m.start()].strip()
            if seg:
                dropped.append(seg) if inside else pieces.append((seg, None))
            if m.group(0) == "[[":
                inside = True
            else:
                inside = False
                pieces.append((None, m.group(1) or UNLABELLED))
            pos = m.end()
        seg = e.text[pos:].strip()
        if seg:
            dropped.append(seg) if inside else pieces.append((seg, None))
        first = True
        for text, label in pieces:
            if label:
                out.append(TP.callout(label, e.page))
                continue
            kind = e.kind if first else "para"
            out.append(El(kind, text, e.page, e.bbox, e.font, e.size, e.level if first else 0,
                          e.list_style if first else "", id=e.id, meta=dict(e.meta)))
            first = False
    doc.els = out
    doc.meta["se_dropped"] = dropped


def part_headings(doc, aux=None):
    """Open the SE and report parts with a level-1 heading, so that repeated section numbers stay under their part."""
    lo, hi = se_range(doc)
    marks = [(lo, "NRC Safety Evaluation"), (hi + 1, "Topical Report")]
    for page, title in marks:
        i = next((k for k, e in enumerate(doc.els) if e.page >= page), len(doc.els))
        doc.els.insert(i, El("raw_md", f"# {title}\n\n<!-- source: part heading supplied; PDF p.{page} starts this "
                                       "part -->", page))


def headings(doc, aux):
    TP.headings(doc, aux, max_chapter=MAX_CHAPTER)
    skip = NOT_HEADING.get(doc.key)
    if skip:
        aux.headings = [h for h in aux.headings if not (in_report(doc, h.page) and skip.match(h.num))]


def figures(doc, aux):
    TP.figures(doc, aux, fig_cap=FIG_CAP, fig_txt=FIG_TXT, is_caption=centred)


def steps():
    return [
        TP.toc_continuation,
        TP.page_labels,
        se_page_labels,
        report_page_labels,
        drop_furniture,
        TP.control_table,
        headings,
        ser.bracket_closers_are_body,
        S.drop_toc,
        protect_legend,
        se_withheld,
        report_brackets,
        TP.withheld,
        restore_legend,
        figures,
        TP.withheld_figure_callouts,
        S.promote_headings,
        S.insert_subheads,
        lambda d, a: S.demote_other_headings(d, a, keep=lambda e: e.text.strip() in TP.KEEP_HEADINGS),
        S.fix_false_items,
        S.join_breaks,
        withheld_table_captions,
        S.attach_captions_and_merge,
        S.attach_table_notes,
        S.normalise_text,
        S.references_as_items,
        S.normalise_item_levels,
        assign_levels,
        TP.figure_levels,
        se_structure,
        part_headings,
    ]


def metadata(doc, aux):
    m = generic.metadata(doc, aux)
    m["headings_found"] = len(aux.headings)
    m["bracket_text_dropped"] = len(doc.meta.get("se_dropped", [])) + len(doc.meta.get("report_dropped", []))
    return m
