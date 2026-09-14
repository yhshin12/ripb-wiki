"""PSAR Chapter 6 hook (Safety-Significant SSC Criteria and Capabilities).

Spec: meta/references_cleanup/file_reviews/review_ch6.md (§1 #1-#4, #8, #11, #12, #16, #21; §5 do-not-fix list).
The steps run after the common PSAR steps and before ``psar.assign_levels``.

Load-combination Tables 6.4-5/-6/-7/-8/-11/-12 are rebuilt from pdfplumber (the review's reference extraction,
522 non-empty load factors); each table is attributed by PDF page only, and the page caption is checked.
Source defects are never corrected; they get an HTML comment ``<!-- source: ... -->`` at most.
"""
import json
import re

from .. import normalize as N
from .. import structure as S
from .. import tables as T
from ..doc import El

# ------------------------------------------------------------ constants ----
# table id -> PDF pages of its sheets (attribution by page only: 6.4-7/6.4-11 and 6.4-8/6.4-12 look alike)
LOAD_TABLES = {
    "6.4-5": (61, 62),
    "6.4-6": (63, 64),
    "6.4-7": (65, 66),
    "6.4-8": (67, 68),
    "6.4-11": (71, 72),
    "6.4-12": (73, 74),
}
EXPECTED_FACTORS = {"6.4-5": 125, "6.4-6": 193, "6.4-7": 52, "6.4-8": 48, "6.4-11": 52, "6.4-12": 52}
EXPECTED_NOTES = {"6.4-5": 17, "6.4-6": 12, "6.4-7": 10, "6.4-8": 9, "6.4-11": 9, "6.4-12": 9, "6.4-9": 5}
SHEET_LABEL = re.compile(r"^\(?Sheet \d+ of \d+\)?$")
NOTE_LINE = re.compile(r"^\((\d{1,2})\)\s*(.*)$")
TRANSIENT = re.compile(r"^(?:Service Level [A-D] Transient \d{1,2}|Test \d) [–-] \S")
FOOTER_LINE = re.compile(r"^\S+ Revision \d+$")

SOURCE_NOTES = {
    "alpha": "<!-- source: the values of the dynamic amplification factor α for single and multiple supports are not "
             "printed (absent from the PDF text layer and the rendered page, p17); nothing is inserted. -->",
    "xref": "<!-- source: cross-reference printed as \"Table 6.4-11 and Table 6.4-12\"; the tables captioned for "
            "SR substructures are Table 6.4-5 (concrete) and Table 6.4-6 (structural steel). Reproduced as printed. -->",
    "mesh": "<!-- source: both mesh-size expressions (soft soil and backfill; hard rock) are printed without a "
            "left-hand side; the preceding sentence names the quantity \"maximum mesh sizes (L)\". Reproduced as "
            "printed. -->",
    "6.4-6": "<!-- source: Table 6.4-6 prints the pipe-break jet-impingement symbol as \"Yi (7)\"; the other "
             "load-combination tables and Section 6.4.2.2.4 use \"Yj\". Reproduced as printed. -->",
    "6.4-8": "<!-- source: in Table 6.4-8 (Sheet 2 of 2, p68) the \"Accident Thermal\" row is printed without a "
             "symbol and without load factors, and no \"Accident Pipe Break Missile Impact\" row is printed. "
             "Reproduced as printed. -->",
    "6.4-9": "<!-- source: in Table 6.4-9 the \"Minimum Factors of Safety\" values are printed one column to the "
             "left of the St- headers (the first value stands in the symbol column and the St-7 column is blank). "
             "Values are reproduced as printed and not re-assigned. -->",
    "6.4-16": "<!-- source: Table 6.4-16 prints event ID \"A. 9\" (with a space) and names B.3 \"Loss of One "
              "Intermediate Sodium Loop\", whereas Section 6.4.3.1.1 titles it \"Loss of One Intermediate Sodium "
              "Pump\". Reproduced as printed. -->",
}


def _ws(s):
    return " ".join((s or "").split())


def _norm(aux, page, s):
    """The common text normalisation (normalise_text has already run when the hook starts)."""
    sups = [x.sup for x in aux.sups.get(page, [])] if aux else None
    return N.text_pipeline(s, sups, aux.hyphen_map if aux else None)


def _find_table(doc, prefix):
    for i, e in enumerate(doc.els):
        if e.kind == "table" and e.table.caption.startswith(prefix):
            return i
    return None


def _insert_after(doc, i, el):
    doc.els.insert(i + 1, el)


def nested_dash_items(doc, aux=None):
    """'- sub item' texts (dash bullets under a '•' item) become nested items without the dash."""
    parent = None
    for e in doc.els:
        if e.kind != "item":
            if e.kind != "raw_md":
                parent = None
            continue
        m = re.match(r"^[-–]\s+(\S.*)$", e.text)
        if not m:
            parent = e
            continue
        e.text = m.group(1)
        if parent is not None and e.level <= parent.level:
            e.level = parent.level + 1


def drop_sheet_labels(doc, aux=None):
    """Stand-alone '(Sheet n of m)' paragraphs left by the header band."""
    doc.els = [e for e in doc.els if not (e.kind in ("para", "caption", "hdr", "heading")
                                          and SHEET_LABEL.match(_ws(e.text)))]


# ------------------------------------------------ load-combination tables ----
def _symbol(s):
    """pdfplumber symbol cell 'W (2)\\ntw' -> 'Wtw (2)'; 'L\\nr' -> 'Lr'; 'D(3)(4)' unchanged."""
    parts = [p.strip() for p in (s or "").split("\n") if p.strip()]
    if not parts:
        return ""
    if len(parts) == 1:
        return parts[0]
    m = re.match(r"^(.*?)(\s*(?:\(\d+\))+)?$", parts[0])
    return m.group(1) + "".join(parts[1:]) + (m.group(2) or "")


def parse_sheet(rows):
    """pdfplumber rows of one sheet -> (column names, body rows).

    Header rows are the leading rows whose symbol column is part of the label span (None). Group / load case /
    equation labels are filled right across their spans and flattened to 'Group: Case: Equation'.
    """
    rows = [list(r) for r in rows if any(_ws(c) for c in r if c is not None)]
    ncol = max(len(r) for r in rows)
    rows = [r + [None] * (ncol - len(r)) for r in rows]
    keep = [j for j in range(ncol) if any(_ws(r[j]) for r in rows)]
    rows = [[r[j] for j in keep] for r in rows]
    nh = 0
    while nh < len(rows) and rows[nh][1] is None:
        nh += 1
    head = []
    for r in rows[:nh]:
        filled, last = [], ""
        for c in r:
            last = last if c is None else _ws(c)
            filled.append(last)
        head.append(filled)
    names = []
    for j in range(len(keep)):
        parts = []
        for r in head:
            if r[j] and (not parts or parts[-1] != r[j]):
                parts.append(r[j])
        names.append(": ".join(parts))
    body = [[_ws(r[0]), _symbol(r[1])] + [_ws(c) for c in r[2:]] for r in rows[nh:]]
    return names, body


def _pdf_caption(aux, page):
    for ln in aux.meta["lines_by_page"].get(page, []):
        if ln.text.startswith("Table ") and all("Bold" in f for f in ln.fonts):
            return _ws(S.SHEET_RE.sub("", ln.text))
    return ""


def pdf_notes(lines):
    """Note block under a table from PyMuPDF lines: ('Notes' header as printed, ['(1) text', ...])."""
    header, notes = None, []
    for ln in sorted(lines, key=lambda l: (round(l.y0, 1), l.x0)):
        t = _ws(ln.text)
        if header is None:
            if re.fullmatch(r"Notes:?", t):
                header = t
            continue
        if ln.size < 9 or FOOTER_LINE.match(t):
            continue
        m = NOTE_LINE.match(t)
        if m:
            notes.append(f"({m.group(1)}) {m.group(2)}".rstrip())
        elif notes:
            notes[-1] += ("" if notes[-1].endswith("-") else " ") + t
    return header, notes


def _odl_values(els):
    """{(row label, case id): value} from the ODL table elements of one load-combination table (QA only)."""
    out = {}
    for e in els:
        g = [[_ws(c.text) for c in row] for row in e.table.grid]
        case_row = next((r for r in g if sum(bool(re.match(r"^[CS]-\d", x)) for x in r) >= 3), None)
        if case_row is None:
            continue
        for r in g:
            if not r[0] or r[0].startswith(("Design Load Cases", "Load Combination")) or r is case_row:
                continue
            if any(x in ("Normal and Severe", "Extreme and Abnormal") for x in r):
                continue
            for j, v in enumerate(r[2:], start=2):
                if j < len(case_row) and case_row[j] and v:
                    out[(r[0], case_row[j])] = v.replace(" ", "")
    return out


def build_load_table(pdf, aux, tid):
    """Rebuild one load-combination table (both sheets, notes) from the PDF. Returns (Table, header, qa)."""
    pages = LOAD_TABLES[tid]
    names, body = None, []
    for p in pages:
        tabs = pdf.pages[p - 1].extract_tables()
        rows = max(tabs, key=lambda t: len(t) * len(t[0]))
        n, b = parse_sheet(rows)
        if names is None:
            names = n
        elif n != names:
            raise ValueError(f"Table {tid}: sheet header on p{p} differs from sheet 1")
        body += b
    caption = _pdf_caption(aux, pages[0])
    if not caption.startswith(f"Table {tid} "):
        raise ValueError(f"Table {tid}: page {pages[0]} caption is {caption!r}")
    if _pdf_caption(aux, pages[1]) != caption:
        raise ValueError(f"Table {tid}: sheet-2 caption on p{pages[1]} differs")
    header, notes = pdf_notes(aux.meta["lines_by_page"][pages[-1]])
    grid = [[T.Cell(_norm(aux, pages[0], x), 0, j, bold=True) for j, x in enumerate(names)]]
    for i, r in enumerate(body, start=1):
        grid.append([T.Cell(_norm(aux, pages[0], x), i, j) for j, x in enumerate(r)])
    t = T.Table(grid=grid, header_rows=1, page=pages[0], pages=list(pages), caption=_norm(aux, pages[0], caption),
                notes=[_norm(aux, pages[-1], x) for x in notes])
    cases = [n.split(": ")[-2] if n.count(": ") >= 1 else n for n in names]
    pdf_vals = {(r[0], cases[j]): v.replace(" ", "") for r in body for j, v in enumerate(r[2:], start=2) if v}
    qa = {"factors": len(pdf_vals), "rows": len(body), "cols": len(names), "notes": len(notes),
          "note_numbers": [int(NOTE_LINE.match(x).group(1)) for x in notes], "pdf_vals": pdf_vals}
    return t, header, qa


def load_combination_tables(doc, aux):
    """Replace the ODL elements of Tables 6.4-5/-6/-7/-8/-11/-12 with tables rebuilt from pdfplumber."""
    import pdfplumber
    qa_all = {}
    with pdfplumber.open(doc.pdf_path) as pdf:
        for tid, pages in LOAD_TABLES.items():
            t, header, qa = build_load_table(pdf, aux, tid)
            idx = [i for i, e in enumerate(doc.els) if e.page in pages and (
                e.kind == "table"
                or (e.kind in ("para", "item", "caption") and e.page == pages[-1]
                    and (NOTE_LINE.match(_ws(e.text)) or re.fullmatch(r"Notes:?", _ws(e.text))))
                or (e.kind in ("caption", "heading") and _ws(e.text).startswith(f"Table {tid} ")))]
            tables_idx = [i for i in idx if doc.els[i].kind == "table"]
            if not tables_idx:
                raise ValueError(f"Table {tid}: no ODL table element on pages {pages}")
            odl = _odl_values([doc.els[i] for i in tables_idx])
            diff = sorted(f"{k[0]} / {k[1]}: odl={odl.get(k)!r} pdf={qa['pdf_vals'].get(k)!r}"
                          for k in set(odl) | set(qa["pdf_vals"]) if odl.get(k) != qa["pdf_vals"].get(k))
            qa["odl_diff"] = diff
            first = doc.els[tables_idx[0]]
            new = El("table", "", pages[0], first.bbox, table=t, id=first.id,
                     meta={"ch6_load_table": tid, "rendered": T.render_md(t) + (f"\n\n{header}" if header else "")})
            keep = [e for i, e in enumerate(doc.els) if i not in set(idx)]
            pos = sum(1 for i in range(tables_idx[0]) if i not in set(idx))
            keep.insert(pos, new)
            doc.els = keep
            if tid in SOURCE_NOTES:
                _insert_after(doc, pos, El("raw_md", SOURCE_NOTES[tid], pages[0], meta={"source_note": tid}))
            qa.pop("pdf_vals")
            qa_all[tid] = qa
    doc.meta["ch6_load_tables"] = qa_all


def stability_table_notes(doc, aux):
    """Table 6.4-9: notes (printed '(1)Refer ...') rebuilt from the PDF lines and kept with the table."""
    i = _find_table(doc, "Table 6.4-9 ")
    if i is None:
        return
    e = doc.els[i]
    header, notes = pdf_notes(aux.meta["lines_by_page"][e.page])
    e.table.notes = [_norm(aux, e.page, x) for x in notes]
    e.meta["rendered"] = T.render_md(e.table) + (f"\n\n{header}" if header else "")
    doc.els = [x for k, x in enumerate(doc.els) if not (
        k > i and x.page == e.page and x.kind in ("para", "item") and NOTE_LINE.match(_ws(x.text)))]
    _insert_after(doc, i, El("raw_md", SOURCE_NOTES["6.4-9"], e.page, meta={"source_note": "6.4-9"}))
    doc.meta.setdefault("ch6_notes", {})["6.4-9"] = len(notes)


def merge_regulatory_guide_sheets(doc, aux=None):
    """Table 6.4-4: the sheet-2 table (no caption, same header) follows sheet 1 once the sheet labels are gone."""
    i = _find_table(doc, "Table 6.4-4 ")
    if i is None or i + 1 >= len(doc.els):
        return
    a, b = doc.els[i], doc.els[i + 1]
    if b.kind == "table" and not b.table.caption and T.same_header(a.table, b.table):
        T.append_rows(a.table, b.table, drop_header=True)
        del doc.els[i + 1]


# ------------------------------------------------------ Table 6.4-1B cells ----
def _nested_text(cell):
    parts = []

    def walk(node):
        for kid in node.get("kids", []) or []:
            if kid.get("type") == "list":
                for it in kid.get("list items", []) or []:
                    t = (it.get("content") or "").strip()
                    if t:
                        parts.append(t)
                    walk(it)
            elif kid.get("type") in ("paragraph", "heading"):
                t = (kid.get("content") or "").strip()
                if t:
                    parts.append(t)

    walk(cell)
    return "\n".join(parts)


def _odl_node(doc, node_id):
    with open(doc.json_path, encoding="utf-8") as f:
        tree = json.load(f)
    return next((n for n in tree.get("kids", []) if n.get("type") == "table" and n.get("id") == node_id), None)


def seismic_classification_cells(doc, aux):
    """Table 6.4-1B: nested sub-bullets inside the cells (dropped by the core cell reader) restored from the ODL
    JSON; the footnote row '1 See Section 6.4.1.2.3' becomes the table note."""
    i = _find_table(doc, "Table 6.4-1B ")
    if i is None:
        return
    e = doc.els[i]
    node = _odl_node(doc, e.table.id or e.id)
    if node is None:
        return
    for row in node.get("rows", []):
        for cell in row.get("cells", []):
            r, c = int(cell.get("row number", 1)) - 1, int(cell.get("column number", 1)) - 1
            if r < e.table.n_rows and c < e.table.n_cols:
                txt = _nested_text(cell)
                if len(txt) > len(e.table.grid[r][c].text):
                    e.table.grid[r][c].text = "\n".join(_norm(aux, e.page, x) for x in txt.split("\n"))
    last = e.table.grid[-1]
    m = re.fullmatch(r"(\d)\s+(See Section .+)", _ws(last[0].text))
    if m and all(_ws(c.text) == _ws(last[0].text) for c in last):
        e.table.grid.pop()
        e.table.notes = [f"<sup>{m.group(1)}</sup> {m.group(2)}"] + e.table.notes


def glued_note_markers(doc, aux):
    """Table-note superscripts extracted glued to the word ('FHB2', 'Motion1') -> 'FHB<sup>2</sup>'.

    Only (word, digit) pairs attested as superscripts on the table's page are converted."""
    count = 0
    for e in doc.els:
        if e.kind != "table":
            continue
        pairs = {(s.base, s.sup) for p in e.table.pages or [e.page] for s in aux.sups.get(p, [])
                 if re.fullmatch(r"\d{1,2}", s.sup) and re.fullmatch(r"[A-Za-z]{2,}", s.base)}
        for base, sup in pairs:
            pat = re.compile(rf"(?<![\w<]){re.escape(base)}{re.escape(sup)}(?!\w)")
            for row in e.table.grid:
                for c in row:
                    c.text, n = pat.subn(f"{base}<sup>{sup}</sup>", c.text)
                    count += n
    doc.meta["ch6_sup_markers"] = count


# ------------------------------------------------------- formula blocks ----
IBC_SPLIT = re.compile(r"\s+(?=(?:1\.[24]|0\.9) (?:\(|D\b))")
LEGEND_SPLIT = re.compile(r"\s(?=(?:[A-Z][a-z]?|f[12]) [–=] )")
PRIME_SPLIT = re.compile(r"\s(?=(?:Ig|[A-Za-zγ][’']?) = )")


def _items(texts, page, style="unordered"):
    return [El("item", t, page, level=0, list_style=style, meta={"ch6_formula": True}) for t in texts]


def formula_blocks(doc, aux=None):
    """IBC-2021 load combinations one per line, the 12-entry symbol legend, the cracked-section property block."""
    els = doc.els
    out, i = [], 0
    qa = {}
    while i < len(els):
        e = els[i]
        t = _ws(e.text) if e.kind in ("para", "item") else ""
        if t.startswith("1.4 (D + F) 1.2 (D + F)"):
            combos = IBC_SPLIT.split(t)
            qa["ibc_combinations"] = len(combos)
            if len(combos) == 7:
                out += _items(combos, e.page)
                i += 1
                # legend: 'Where:' then entries up to the next body sentence
                if i < len(els) and _ws(els[i].text) == "Where:":
                    out.append(els[i])
                    i += 1
                    legend, j = [], i
                    while j < len(els) and els[j].kind in ("para", "item", "raw_md") and not _ws(
                            els[j].text).startswith("ACI 318-19"):
                        if els[j].kind != "raw_md":
                            legend += [(x, els[j].page) for x in LEGEND_SPLIT.split(_ws(els[j].text))]
                        j += 1
                    qa["legend_entries"] = len(legend)
                    if len(legend) == 12:
                        out += [El("item", x, p, level=0, list_style="unordered", meta={"ch6_formula": True})
                                for x, p in legend]
                        i = j
                continue
        if t.startswith("t' = 0.707 × t "):
            props = PRIME_SPLIT.split(t)
            qa["cracked_properties"] = len(props)
            if len(props) == 4:
                out += _items(props, e.page)
                i += 1
                nxt = els[i] if i < len(els) else None
                if nxt is not None and _ws(nxt.text).startswith("Where E’ = "):
                    defs = [(_ws(nxt.text)[len("Where "):], nxt.page)]
                    j = i + 1
                    if j < len(els) and _ws(els[j].text).startswith("E = Modulus"):
                        defs += [(x, els[j].page) for x in PRIME_SPLIT.split(_ws(els[j].text))]
                        j += 1
                    qa["definitions"] = len(defs)
                    if len(defs) == 10:
                        out.append(El("para", "Where", nxt.page, nxt.bbox))
                        out += [El("item", x, p, level=0, list_style="unordered", meta={"ch6_formula": True})
                                for x, p in defs]
                        i = j
                continue
        out.append(e)
        i += 1
    doc.els = out
    doc.meta["ch6_formulas"] = qa


# ------------------------------------------------------ transient titles ----
def transient_titles(doc, aux=None):
    """Design-transient titles (A.1-A.11, B.1-B.9, C.1-C.2, D.1-D.2, Test 1-6) are subheadings under the
    underlined 'Service Level X Conditions' / 'Test Conditions' subheading (H6 under 6.4.3.1.1, H5), i.e. H7:
    they become bold paragraphs."""
    num_level, sub_level, n = 1, None, 0
    for e in doc.els:
        if e.kind == "heading" and e.meta.get("numbered"):
            num_level, sub_level = len(e.meta["num"].split(".")), None
            continue
        if e.kind == "heading" and e.meta.get("sub"):
            sub_level = num_level + 1
            continue
        if e.kind in ("para", "item") and TRANSIENT.match(_ws(e.text)):
            level = (sub_level or num_level) + 1
            if level <= 6:
                e.kind, e.level, e.meta = "heading", level, dict(e.meta, transient=True)
            else:
                e.kind, e.text, e.level = "para", f"**{_ws(e.text)}**", 0
                e.meta = dict(e.meta, transient=True)
            n += 1
    doc.meta["ch6_transients"] = n


# ---------------------------------------------------------- source notes ----
def source_notes(doc, aux=None):
    """HTML comments at source defects in running text and Table 6.4-16 (no value is changed)."""
    for key, test in (
            ("alpha", lambda x: x.kind == "item" and _ws(x.text).startswith("for systems with multiple supports, with 1.0")),
            ("xref", lambda x: x.kind == "para" and "SR substructures, primarily based on" in x.text
             and _ws(x.text).endswith("are provided in Table 6.4-11 and Table 6.4-12.")),
            ("mesh", lambda x: x.kind == "para" and _ws(x.text).startswith("For hard rock: = [")),
            ("6.4-16", lambda x: x.kind == "table" and x.table.caption.startswith("Table 6.4-16 "))):
        i = next((k for k, x in enumerate(doc.els) if test(x)), None)
        if i is not None:
            _insert_after(doc, i, El("raw_md", SOURCE_NOTES[key], doc.els[i].page, meta={"source_note": key}))
    doc.meta["ch6_source_notes"] = [e.meta["source_note"] for e in doc.els
                                    if e.kind == "raw_md" and e.meta.get("source_note")]


STEPS = [
    nested_dash_items,
    drop_sheet_labels,
    load_combination_tables,
    stability_table_notes,
    merge_regulatory_guide_sheets,
    seismic_classification_cells,
    glued_note_markers,
    formula_blocks,
    transient_titles,
    source_notes,
]
