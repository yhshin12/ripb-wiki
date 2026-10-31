"""RG 1.247 profile: the generic pipeline, plus Appendix A staff-position tables rendered as records.

Appendix A (Tables A-1 to A-22, PDF p.73-155) gives one row per requirement of ASME/ANS RA-S-1.4-2021 in four
columns (Index No. | Issue | Position | Resolution). The converter reports one table per page; merged into one Markdown
table, a single table would span up to 60 pages and a quotation could not be cited to its page. Each row therefore
becomes a record that stays on its own page:

    #### POS-A8
    - Issue: ...
    - Position: Qualification
    - Resolution: ...

- The table captions are only in the page-header band (converted with include_header_footer); the first occurrence of
  each caption becomes a `### Table A-n. ...` heading before that table's first record. Repeats on continuation pages
  and all other header lines are dropped. The column header row is not rendered (the field names carry it). Both
  dropped repeats are listed in doc.meta["sheet_credit"] so that verify does not count them as missing.
- A row with text only in the Index No. cell (e.g. "Section 4.3.1") is a group label: a record heading without
  fields. A row with an empty Index No. cell continues the previous record across a page break: its fields follow
  the page anchor without a new heading.
- The converter drops a hyphen at a line end inside a cell ("HR-" / "E4" -> "HRE4", "post-" / "initiator"); it is
  restored from the line breaks of the same PDF page (restore_hyphens).
- Cells holding only a dash rule ("-----") are layout placeholders in the source and are not rendered.
Appendix B tables (hazard lists, three columns) go through the generic table path.

Figure 1 has a bare number ("Figure 1. Title") that the shared caption pattern and figure search do not read, so
figures() takes the box from the converter's image element right before the caption.
"""
import re

import fitz

from .. import structure as S
from ..doc import El
from ..figures import figures_step, odl_to_visible
from ..levels import assign_levels
from ..pdfaux import FigureRef
from . import generic

META = {"RG_1.247": generic.META["RG_1.247"]}

CAPTION_RE = re.compile(r"^Table A-\d+\.\s")
FIG_TXT = re.compile(r"^Figure\s+(\d+)\.\s+(.*)$")
DASHES = re.compile(r"^-{3,}$")
HEADER = ["Index No.", "Issue", "Position", "Resolution"]


def _clean(text):
    return " ".join(text.split())


LINE_HYPHEN = re.compile(r"([A-Za-z0-9]+)-[ \t]*\n[ \t]*([A-Za-z0-9]+)")


def line_end_hyphens(pdf_path, pages):
    """{page: [(a, b)]} for every 'a-' at a line end followed by 'b' on the next line of the PDF page."""
    pdf = fitz.open(pdf_path)
    out = {p: [m.groups() for m in LINE_HYPHEN.finditer(pdf[p - 1].get_text())] for p in pages if 0 < p <= len(pdf)}
    pdf.close()
    return out


def restore_hyphens(text, pairs):
    """The converter joins a line-end hyphen in table cells ('HR-' + 'E4' -> 'HRE4'). Restore 'a-b' where the PDF
    page breaks the line after 'a-' and the cell holds the joined word. Returns (text, number restored)."""
    n = 0
    for a, b in pairs:
        text, k = re.subn(rf"(?<![A-Za-z0-9]){re.escape(a)}{re.escape(b)}(?![A-Za-z0-9])", f"{a}-{b}", text, count=1)
        n += k
    return text, n


def _is_appendix_a(e):
    if e.kind != "table" or e.table.n_cols != 4 or not e.table.n_rows:
        return False
    return [_clean(c.text) for c in e.table.grid[0]] == HEADER


def appendix_a_records(doc, aux=None):
    captions, consumed = {}, set()
    for i, e in enumerate(doc.els):
        if e.kind == "hdr" and CAPTION_RE.match(e.text) and e.page not in captions:
            cap = _clean(e.text)
            if cap.endswith(","):
                # the second caption line sometimes lands in the body as a heading or paragraph on the same page
                nxt = next((x for x in doc.els[i + 1:] if x.page == e.page and x.kind != "hdr"), None)
                if nxt is not None and nxt.kind in ("heading", "para") and nxt.text.startswith("Technical Requirements"):
                    cap = f"{cap} {_clean(nxt.text)}"
                    consumed.add(id(nxt))
            captions[e.page] = cap
    hyph = line_end_hyphens(doc.pdf_path, sorted({e.page for e in doc.els if _is_appendix_a(e)}))
    seen, out, n_records, n_hyph = set(), [], 0, 0
    for e in doc.els:
        if e.kind == "hdr" or id(e) in consumed:
            continue
        if not _is_appendix_a(e):
            out.append(e)
            continue
        cap = captions.get(e.page)
        if cap and cap not in seen:
            seen.add(cap)
            out.append(El("raw_md", f"### {cap}", e.page, meta={"rg1247_caption": True}))
        elif cap:
            doc.meta.setdefault("sheet_credit", []).append(cap)          # caption repeated on a continuation page
        doc.meta.setdefault("sheet_credit", []).append(" ".join(HEADER))  # column header row printed on every page
        for row in e.table.grid[e.table.header_rows:]:
            # a spanned cell is reported once, at its origin; covered positions repeat its text (filled=True)
            cells = ["" if c.filled else _clean(c.text) for c in row]
            for i, v in enumerate(cells):
                cells[i], k = restore_hyphens(v, hyph.get(e.page, []))
                n_hyph += k
            index, fields = cells[0], [(HEADER[i], v) for i, v in enumerate(cells) if i and v and not DASHES.match(v)]
            lines = [f"#### {index}"] if index else []
            lines += [f"- {name}: {v}" for name, v in fields]
            if lines:
                out.append(El("raw_md", "\n".join(lines), e.page, meta={"rg1247_record": True}))
                n_records += bool(index)
    doc.els = out
    doc.meta["appendix_a_records"] = n_records
    doc.meta["appendix_a_captions"] = len(seen)
    doc.meta["appendix_a_hyphens_restored"] = n_hyph


def figures(doc, aux):
    """Each 'Figure N. Title' caption takes its box from the image element directly before it."""
    pdf = fitz.open(doc.pdf_path)
    refs, last = [], None
    for e in doc.els:
        m = FIG_TXT.match(" ".join(e.text.split())) if e.kind in ("para", "heading", "caption") else None
        if m and last is not None and last.page == e.page:
            box = odl_to_visible(last.bbox, pdf[e.page - 1])
            refs.append(FigureRef(m.group(1), " ".join(m.group(2).split()), e.page, tuple(box)))
        last = e if e.kind == "image" else None
    pdf.close()
    aux.figures = refs
    figures_step(doc, aux, render=aux.meta.get("render_figures", True), fig_txt=FIG_TXT)


def figure_levels(doc, aux=None):
    """A bare figure number has no owner section, so its heading keeps the converter's level and does not split §B."""
    for e in doc.els:
        if e.kind == "heading" and e.meta.get("figure"):
            e.level = 5


def steps():
    return [
        S.drop_toc,
        S.withheld_callouts,
        figures,
        appendix_a_records,
        S.promote_headings,
        S.insert_subheads,
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
    m = dict(META[doc.key])
    tables = [e.table.caption for e in doc.els if e.kind == "table" and e.table.caption]
    m.update({
        "source_pdf": f"references/raw/{doc.stem}.pdf",
        "raw_json": f"references/raw/{doc.stem}.json",
        "pdf_pages": doc.n_pages,
        "tables": tables,
        "appendix_a_records": doc.meta.get("appendix_a_records", 0),
        "figures": doc.meta.get("figures", []),
        "withheld": doc.meta.get("withheld", []),
    })
    return m
