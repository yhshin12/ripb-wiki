"""Kemmerer Unit 1 PSAR Chapter 1 (General Plant and Site Description) — chapter hooks.

Spec: meta/references_cleanup/file_reviews/review_ch1.md (§1 findings, §5 rules / do-not-fix list).
Runs after the common PSAR steps (text already normalised) and before `psar.assign_levels`.

Every fixed-list item below was checked against the PDF text layer / page render (page numbers = PDF pages).
QA anomalies are collected in `doc.meta['psar_ch01_qa']` (empty on a clean run; asserted by the tests).

Core coverage (2026-09-13 core patches), no longer done here: stray footer lines and their page labels
(`psar.drop_stray_footers`), the `(Sheet n of m)` paragraphs and the sheet merge of Table 1.4-1, the running-title
dedupe and the merge of the acronym list (`structure.hdr_to_captions` / `attach_captions_and_merge`), the
`Water-Cooled` line-end hyphen (`pdfaux.hyphen_map`) and the wrapped table-cell lines that were joined with `; `
(`tables.cell_md`). The steps below verify the result of those merges and record a QA entry if they regress.
"""
import re

from .. import tables as T
from ..doc import El

STATUS_TERMS = ("Full Conformance", "Partial Conformance", "Full Compliance", "Partial Compliance", "Not Applicable")
TERMINAL = tuple('.:;?!”")’')

ACRONYM_TITLE = "LIST OF ACRONYMS AND ABBREVIATIONS"
ACRONYM_HEADER = ["Term", "Description"]
T141_HEADER = ["Guide Number", "Title", "Revision", "Conformance Status"]
T141_STATUS = re.compile(r"^(Full Conformance|Partial Conformance)\b\s*(.*)$", re.S)

# §1.1: the PDF prints two paragraphs (p19); opendataloader delivered one.
PARA_SPLITS = [
    # (page, text ending the first paragraph, text starting the second)
    (19, "Production and Utilization Facilities.”", "This preliminary safety analysis report (PSAR)"),
]

# Page-break splits the common join rule leaves (next fragment starts with a capital): p26->p27 'the' | 'CRD.',
# p63->p64 'the' | 'IAC blower.' (review #16, L762 / L1518).
JOIN_WORDS = {"the", "a", "an", "of", "to", "and", "or", "in", "for", "with", "by", "from", "at", "on"}

# Line-end hyphens lost inside table cells (review #4), reduced to the two cases pdfaux.hyphen_map cannot see:
# the dash does not end the *visual* line (the table row continues in the next column), and the spaced form
# 'word -' is not a line-end hyphen at all. Water-Cooled, Tamper-Indicating, long-term, non-essential and
# in-plant are restored by the core hyphen map.
# The last three entries repair cell line breaks: a wrapped enumeration whose first line ends with a comma (which
# tables.ENUM reads as a new item), and two Section cells the converter delivered as one line although the PDF
# prints two (the spec renders a line-separated enumeration with '; ', as tables.cell_md now does elsewhere).
CELL_FIXES = [
    # (find, replace, pdf page, evidence)
    ("NATD-LIC-RPRT0002-A", "NATD-LIC-RPRT-0002-A", 95,
     "Table 1.4-2: line 'NATD-LIC-RPRT- ML24283A066 Principal Design Criteria for the' / '0002-A Natrium …'"),
    ("Information Containment", "Information - Containment", 105,
     "50.34(f)(3)(v): 'Preliminary Design Information -' / 'Containment Integrity. (II.B.8)'"),
    ("3.12,\n3.13", "3.12, 3.13", 96,
     "Table 1.4-3 TP-LIC-RPT-0011 Section(s): printed '3.12,' / '3.13' — one wrapped list, not two items"),
    ("7.1.3 11.2", "7.1.3; 11.2", 102,
     "Table 1.4-4 (2)(xviii) Section: printed '7.1.3' (y=456) / '11.2' (y=473) at x=488 in the Section column"),
    ("7.6.5 11.2", "7.6.5; 11.2", 102,
     "Table 1.4-4 (2)(xix) Section: printed '7.6.5' (y=514) / '11.2' (y=531); '5.3.2.10, 7.6.7' is one printed "
     "line and stays as printed"),
]

# Line-wrap artefacts in running text (review #19).
TEXT_FIXES = [
    ("NUREG/ CR-7046", "NUREG/CR-7046", 67, "Ref 1.4-2: line ends 'NUREG/', next line 'CR-7046, 2011.'"),
]

LEGEND_HEAD = "FACILITY NUMBER/DESCRIPTION:"
LEGEND_ENTRY = re.compile(r"^(\d{2}[A-Z]?)\s+(\S.*)$")
LEGEND_NUMBERS = ["11", "12", "21", "32A", "32B", "33", "34", "35", "36", "37", "38", "41", "42", "43", "44", "45",
                  "51", "52", "61", "62", "71", "72", "73", "75", "76", "78", "81A", "81B", "82", "84", "85"]
WITHHELD_FIGURES = [f"1.1-{n}" for n in range(5, 18)]


def _qa(doc, msg):
    doc.meta.setdefault("psar_ch01_qa", []).append(msg)


def _lines_by_page(aux):
    return (aux.meta.get("lines_by_page") or {}) if aux is not None and aux.meta else {}


def _lines(aux, page):
    return _lines_by_page(aux).get(page, [])


def _row(texts, bold=False):
    return [T.Cell(t, 0, j, bold=bold) for j, t in enumerate(texts)]


def _header(t):
    return [T.cell_md(c.text) for c in t.grid[0]] if t.grid else []


# -------------------------------------------------------------- paragraphs ----
def split_paragraphs(doc, aux=None, splits=None):
    """Split paragraphs that the PDF prints as two (fixed list, PARA_SPLITS)."""
    for page, end_a, start_b in (PARA_SPLITS if splits is None else splits):
        for i, e in enumerate(doc.els):
            if e.kind != "para" or e.page != page:
                continue
            k = e.text.find(end_a + " " + start_b)
            if k < 0:
                continue
            cut = k + len(end_a)
            second = El("para", e.text[cut:].strip(), e.page, e.bbox, e.font, e.size, id=e.id,
                        meta={"split_from": e.id})
            e.text = e.text[:cut].strip()
            doc.els.insert(i + 1, second)
            break
        else:
            _qa(doc, f"paragraph split not found: p{page} {end_a!r}")


def join_page_breaks(doc, aux=None):
    """Join a paragraph cut by a page break when it ends on a function word and the continuation (a paragraph at
    the top of the next page) starts with a capital, e.g. '… manipulation of the' | 'CRD. During shutdown …'."""
    out = []
    for e in doc.els:
        prev = out[-1] if out else None
        if prev is not None and e.kind == "para" and prev.kind == "para" and e.page == prev.page + 1:
            p = prev.text.rstrip()
            words = re.findall(r"[A-Za-z]+$", p)
            if (p and not p.endswith(TERMINAL) and words and words[0] in JOIN_WORDS
                    and e.text.lstrip()[:1].isupper()):
                prev.text = p + " " + e.text.lstrip()
                doc.meta.setdefault("psar_ch01_joined", []).append(
                    f"p{prev.page}->p{e.page}: …{p[-30:]} | {e.text[:30]}…")
                continue
        out.append(e)
    doc.els = out


def nest_dash_items(doc, aux=None):
    """Sub-bullets printed with a '-' glyph (p66, §1.4.1) arrive as '- text' items at the parent's depth."""
    parent = None
    for e in doc.els:
        if e.kind != "item":
            parent = None
            continue
        m = re.match(r"^[-–]\s+(\S.*)$", e.text)
        if m and parent is not None:
            e.text = m.group(1)
            e.level = parent.level + 1
            continue
        parent = e


def bold_status_terms(doc, aux=None):
    """D7: the status definitions of §1.4.1/§1.4.3 start with a bold term (PDF p66–67). Bold is applied only where
    a PDF line on the same page starts with that term in a bold font."""
    bold = {}
    for page, lines in _lines_by_page(aux).items():
        for ln in lines:
            if not ln.spans:
                continue
            t, _r, _s, font, flags, _c = ln.spans[0]
            if t.strip() in STATUS_TERMS and ("Bold" in font or "bold" in font or flags & 16):
                bold.setdefault(page, set()).add(t.strip())
    n = 0
    for e in doc.els:
        if e.kind != "para" or e.page not in bold:
            continue
        for term in bold[e.page]:
            if re.match(re.escape(term) + r" [–-] ", e.text):
                e.text = f"**{term}**" + e.text[len(term):]
                n += 1
                break
    if n != sum(len(v) for v in bold.values()):
        _qa(doc, f"bold status terms: {n} applied, {sum(len(v) for v in bold.values())} bold in PDF")


# ------------------------------------------------------------------ tables ----
def _merged(doc, header, what):
    """The single table with this header (the core merges the page fragments); None + a QA entry otherwise."""
    tabs = [e for e in doc.els if e.kind == "table" and _header(e.table) == header]
    if len(tabs) != 1:
        _qa(doc, f"{what}: {len(tabs)} tables with header {header} (core merge)")
        return None
    return tabs[0]


def subscripts(aux):
    """{page: [(base, sub)]}: small spans set below the baseline of the preceding full-size span (V + S30)."""
    res = {}
    body = aux.meta.get("body_size", 11.0) if aux is not None and aux.meta else 11.0
    for page, lines in _lines_by_page(aux).items():
        for ln in lines:
            prev = None
            for (t, r, s, _f, _fl, _c) in ln.spans:
                if prev is not None and s <= 0.8 * body < prev[2] and r.y1 > prev[1].y1 + 0.5 and prev[0].split():
                    res.setdefault(page, []).append((prev[0].split()[-1], t.strip()))
                prev = (t, r, s)
    return res


def acronym_list(doc, aux=None):
    """Front-matter acronym list: the running title becomes the H2 heading of the merged table; V<sub>S</sub>."""
    hdrs = [e for e in doc.els if e.kind in ("hdr", "para", "caption") and " ".join(e.text.split()) == ACRONYM_TITLE]
    if not hdrs:
        _qa(doc, "acronym title not found")
        return
    if len(hdrs) != 1:
        _qa(doc, f"acronym list: {len(hdrs)} running titles (core dedupe)")
    first = hdrs[0]
    first.kind, first.text, first.level = "heading", ACRONYM_TITLE, 2
    first.meta["acronym_list"] = True
    extra = {id(e) for e in hdrs[1:]}
    doc.els = [e for e in doc.els if id(e) not in extra]
    el = _merged(doc, ACRONYM_HEADER, "acronym list")
    if el is None:
        return
    t = el.table
    subs = subscripts(aux)
    for page in t.pages:
        for base, sub in subs.get(page, []):
            for row in t.grid[t.header_rows:]:
                if row[0].text.strip() == base + sub:
                    row[0].text = f"{base}<sub>{sub}</sub>"


def table_141(doc, aux=None):
    """Table 1.4-1 (sheets merged by the core): 'Conformance Status' split into status label + 'Comments'.

    The PDF prints the label ('Full Conformance' / 'Partial Conformance') and the comment as separate paragraphs of
    one cell; opendataloader glued them (26 of 183 rows). OL-stage rows keep their sentence as the status."""
    el = _merged(doc, T141_HEADER, "Table 1.4-1")
    if el is None:
        return
    t = el.table
    if not t.caption:
        t.caption = "Table 1.4-1 Conformance with Regulatory Guides"
    t.grid[0].append(T.Cell("Comments", 0, len(t.grid[0]), bold=True))
    for i in range(1, t.header_rows):
        t.grid[i].append(T.Cell("Comments", i, len(t.grid[i]), bold=True, filled=True))
    for r in range(t.header_rows, t.n_rows):
        row = t.grid[r]
        st = row[3]
        m = T141_STATUS.match(st.text.strip())
        comment = ""
        if m:
            st.text, comment = m.group(1), m.group(2).strip()
        row.append(T.Cell(comment, r, 4))
    el.meta["t141_rows"] = t.n_rows - t.header_rows


def table_cell_fixes(doc, aux=None, fixes=None):
    """Fixed, PDF-verified substitutions inside table cells; each must occur exactly once."""
    for find, repl, page, _ev in (CELL_FIXES if fixes is None else fixes):
        hits = [c for e in doc.els if e.kind == "table" for row in e.table.grid for c in row if find in c.text]
        if len(hits) != 1:
            _qa(doc, f"cell fix {find!r} (p{page}): {len(hits)} hits")
            continue
        hits[0].text = hits[0].text.replace(find, repl)


def text_fixes(doc, aux=None, fixes=None):
    for find, repl, page, _ev in (TEXT_FIXES if fixes is None else fixes):
        hits = [e for e in doc.els if e.kind in ("para", "item") and find in e.text]
        if len(hits) != 1:
            _qa(doc, f"text fix {find!r} (p{page}): {len(hits)} hits")
            continue
        hits[0].text = hits[0].text.replace(find, repl)


# ----------------------------------------------------------------- figures ----
def parse_legend(lines, head_text=LEGEND_HEAD):
    """Facility legend of Figure 1.2-1 from PDF visual lines: [(number, description)] in printed order.

    Entries are the lines of the column that starts under the legend header; a line without a leading facility
    number continues the previous entry ('84 STEAM GENERATOR BUILDING/TURBINE FACILITY' + 'BUILDING (STEAM) RACK')."""
    head = next((ln for ln in lines if ln.text.strip() == head_text), None)
    if head is None:
        return []
    col = sorted((ln for ln in lines if abs(ln.x0 - head.x0) <= 6 and ln.y0 >= head.y1 - 0.5 and ln is not head
                  and abs(ln.size - head.size) < 0.6), key=lambda ln: ln.y0)
    entries, prev_y1 = [], head.y1
    for ln in col:
        if ln.y0 - prev_y1 > 2.5 * max(ln.y1 - ln.y0, 1.0):
            break                        # gap: end of the legend column
        m = LEGEND_ENTRY.match(ln.text.strip())
        if m:
            entries.append([m.group(1), m.group(2).strip()])
        elif entries:
            entries[-1][1] += " " + ln.text.strip()
        else:
            break
        prev_y1 = ln.y1
    return [tuple(x) for x in entries]


def _figure_index(doc, num, kind="figure_img"):
    for i, e in enumerate(doc.els):
        if e.kind == "raw_md" and e.meta.get(kind) == num:
            return i
    for i, e in enumerate(doc.els):
        if e.kind == "heading" and e.meta.get("figure") == num:
            return i
    return None


def site_layout_legend(doc, aux=None):
    """Figure 1.2-1: facility legend (31 entries, PDF p59 text layer) as a two-column table after the image."""
    ref = next((f for f in (aux.figures if aux is not None else []) if f.num == "1.2-1"), None)
    page = ref.page if ref else 59
    lines = _lines(aux, page)
    if ref is not None:
        x0, y0, x1, y1 = ref.box
        lines = [ln for ln in lines if x0 <= (ln.x0 + ln.x1) / 2 <= x1 and y0 <= (ln.y0 + ln.y1) / 2 <= y1]
    entries = parse_legend(lines)
    if [n for n, _ in entries] != LEGEND_NUMBERS:
        _qa(doc, f"Figure 1.2-1 legend: got {[n for n, _ in entries]}")
        if not entries:
            return
    i = _figure_index(doc, "1.2-1")
    if i is None:
        _qa(doc, "Figure 1.2-1 not in the element stream")
        return
    t = T.Table(grid=[_row(["Facility number", "Facility"], bold=True)] + [_row([n, d]) for n, d in entries],
                header_rows=1, page=page, pages=[page])
    doc.els.insert(i + 1, El("table", "", page, table=t, meta={"figure_legend": "1.2-1"}))


def figure_notes(doc, aux=None, num="1.3-1"):
    """Figure 1.3-1: keep the printed '*' note (text layer, inside the figure box) as a paragraph after the image."""
    ref = next((f for f in (aux.figures if aux is not None else []) if f.num == num), None)
    if ref is None:
        _qa(doc, f"Figure {num}: no figure ref")
        return
    x0, y0, x1, y1 = ref.box
    lines = sorted((ln for ln in _lines(aux, ref.page)
                    if x0 <= ln.x0 <= x1 and y0 <= ln.y0 <= y1), key=lambda ln: ln.y0)
    note = None
    for ln in lines:
        if note is None:
            if ln.text.startswith("*") and len(ln.text) > 10:
                note = [ln]
            continue
        last = note[-1]
        if abs(ln.x0 - last.x0) <= 3 and 0 <= ln.y0 - last.y1 <= 0.8 * (last.y1 - last.y0) and ln.size == last.size:
            note.append(ln)
        else:
            break
    if not note:
        _qa(doc, f"Figure {num}: note not found")
        return
    text = " ".join(ln.text.strip() for ln in note)
    i = _figure_index(doc, num)
    if i is None:
        _qa(doc, f"Figure {num} not in the element stream")
        return
    doc.els.insert(i + 1, El("para", "\\" + text, ref.page, meta={"figure_note": num}))


def check_withheld(doc, aux=None):
    """Figures 1.1-5 … 1.1-17: heading followed by exactly one withheld callout; no '[[' / ']]' anywhere."""
    for num in WITHHELD_FIGURES:
        idx = [i for i, e in enumerate(doc.els) if e.kind == "heading" and e.meta.get("figure") == num]
        if len(idx) != 1:
            _qa(doc, f"Figure {num}: {len(idx)} headings")
            continue
        i = idx[0]
        j = i + 1
        callouts = []
        while j < len(doc.els) and doc.els[j].kind != "heading":
            if doc.els[j].kind == "raw_md" and doc.els[j].meta.get("withheld"):
                callouts.append(j)
            j += 1
        if not callouts or callouts[0] != i + 1:
            _qa(doc, f"Figure {num}: withheld callout does not follow the heading")
        for k in callouts[1:]:
            doc.els[k] = El("drop", "", doc.els[k].page)
    doc.els = [e for e in doc.els if e.kind != "drop"]
    for e in doc.els:
        txt = e.text if e.kind != "table" else " ".join(c.text for row in e.table.grid for c in row)
        if "[[" in txt or "]]" in txt:
            _qa(doc, f"wikilink brackets left on p{e.page}: {txt[:60]!r}")


STEPS = [
    split_paragraphs,
    join_page_breaks,
    nest_dash_items,
    bold_status_terms,
    acronym_list,
    table_141,
    table_cell_fixes,
    text_fixes,
    site_layout_legend,
    figure_notes,
    check_withheld,
]
