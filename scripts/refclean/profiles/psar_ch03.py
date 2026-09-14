"""PSAR Chapter 3 (Licensing Basis Events) hooks.

Run after the common PSAR steps (text already normalised), before `psar.assign_levels`.
Evidence for every rule: meta/references_cleanup/file_reviews/review_ch3.md and the PDF pages cited
in the docstrings (re-checked 2026-09-11 on
references/raw/TP_Natrium_PSAR2025_ch3_Licensing Basis Events.pdf).
"""
import collections
import re

from ..doc import El
from .. import tables as T

TERMINAL = tuple('.:;?!”")')
LBE_KINDS = ("freq", "dose", "dba")
LISTED = re.compile(r"are listed below\.")
SENT_BOUNDARY = re.compile(r"[.!?][”\")]?\s+")
ST_LABEL = "Cumulative Activity Release to Environment (Ci)"
RELEASE_LABELS = ("Plenum Release", "Non-Plenum Release")


def _warn(doc, msg):
    doc.meta.setdefault("ch03_warnings", []).append(msg)


def _heading_index(els, num, start=0):
    for i in range(start, len(els)):
        e = els[i]
        if e.kind == "heading" and e.meta.get("num") == num:
            return i
    return None


def _depth(num):
    return len(num.split("."))


def _section_end(els, i0):
    """Index of the next numbered heading at the same or a higher level than els[i0]."""
    d = _depth(els[i0].meta["num"])
    for j in range(i0 + 1, len(els)):
        e = els[j]
        if e.kind == "heading" and e.meta.get("numbered") and _depth(e.meta["num"]) <= d:
            return j
    return len(els)


def _clone(e, kind=None, text=None, **meta):
    m = dict(e.meta)
    m.update(meta)
    return El(kind or e.kind, e.text if text is None else text, e.page, e.bbox, e.font, e.size, e.level,
              e.list_style, id=e.id, meta=m)


def _new_table(rows, page, pages, caption="", notes=None):
    grid = [[T.Cell(txt, r, c, bold=(r == 0)) for c, txt in enumerate(row)] for r, row in enumerate(rows)]
    return T.Table(grid=grid, header_rows=1, page=page, pages=list(pages), caption=caption, notes=list(notes or []))


def _rows(t):
    return [[c.text.strip() for c in row] for row in t.grid]


# ------------------------------------------------------------------ noise ----
def drop_invisible_periods(doc, aux=None):
    """Lone '.' paragraphs are 2-pt Arial periods in the left margin (x = 18 pt) on PDF p97, p100, p103
    (2 each); they are invisible in print."""
    doc.els = [e for e in doc.els
               if not (e.kind == "para" and e.text.strip() == "." and (not e.bbox or e.bbox[0] < 40))]


# ----------------------------------------------------------- tables 3.1 ----
HAZ_LABEL = re.compile(r"^(Individual|Coexistent) Hazards -? ?(Qualitatively|Quantitatively) Screened Out(?: \(continued\))?$")


def _table_by_caption(doc, prefix):
    for e in doc.els:
        if e.kind == "table" and (e.table.caption or "").startswith(prefix):
            return e
    return None


def _fill_down(t, cols, key_col=0):
    """Rows whose key column is filled but whose `cols` are all empty inherit `cols` from the row above."""
    for r in range(t.header_rows + 1, t.n_rows):
        row, above = t.grid[r], t.grid[r - 1]
        if row[key_col].text.strip() and all(not row[c].text.strip() for c in cols):
            for c in cols:
                row[c] = T.Cell(above[c].text, r, c, filled=True)


def fix_hazard_tables(doc, aux=None):
    """Table 3.1-2: the group label is 'Individual Hazards - Qualitatively Screened Out' etc. (PDF p17-20: separate
    word '-' after 'Hazards'; dropped by the converter) and the sheet-repeat suffix '(continued)' is not part of
    the label. The row-spanned group column itself is filled down by `tables.from_odl` (asserted in the tests:
    90/10/10 rows per label), so only the label text is rewritten here."""
    e = _table_by_caption(doc, "Table 3.1-2")
    if e is None:
        _warn(doc, "Table 3.1-2 not found")
    else:
        t = e.table
        for r in range(t.header_rows, t.n_rows):
            m = HAZ_LABEL.match(t.grid[r][0].text.strip())
            if m:
                t.grid[r][0] = T.Cell(f"{m.group(1)} Hazards - {m.group(2)} Screened Out", r, 0,
                                      filled=t.grid[r][0].filled)


# ----------------------------------------------------------- table 3.5-4 ----
LPZ_HEADER = "DBA 30-day Low Population Zone Boundary TEDE (rem)"


def fix_dba_summary(doc, aux=None):
    """Table 3.5-4 (PDF p60-61): 5th column header present, DBE rows filled from the row-spanned DBA ID / title /
    doses, and 'Secondary-to-Primary' (line-end hyphen 'Secondary-to-' + 'Primary' on p60)."""
    e = _table_by_caption(doc, "Table 3.5-4")
    if e is None:
        _warn(doc, "Table 3.5-4 not found")
        return
    t = e.table
    if t.n_cols != 5 or T.header_names(t)[4] != LPZ_HEADER:
        _warn(doc, f"Table 3.5-4 header unexpected: {T.header_names(t)}")
    _fill_down(t, [1, 2, 3, 4])
    for row in t.grid:
        for c in row:
            c.text = c.text.replace("Secondary-toPrimary", "Secondary-to-Primary")


def fix_bdbe_note(doc, aux=None):
    """Table 3.5-3 note: the leading '*' is literal (marks RFH-FDEM-2*, RFH-LMCA-2*), escaped for Obsidian."""
    e = _table_by_caption(doc, "Table 3.5-3")
    if e is not None:
        e.table.notes = [re.sub(r"^\*(?=Denotes)", r"\\*", n) for n in e.table.notes]


# ------------------------------------------------- source-term tables 3.2 ----
def _is_source_term(t):
    return any(ST_LABEL in c.text for row in t.grid[:3] for c in row) or (t.grid and t.grid[0][0].text.strip() in RELEASE_LABELS)


def source_term_tables(doc, aux=None):
    """Tables 3.2-1 ... 3.2-18 (PDF p25-43): one header row `Isotope | 2hr | ...`; the group label 'Cumulative
    Activity Release to Environment (Ci)' becomes a subtitle line under the caption. Tables 3.2-4/-5/-6 stack a
    'Plenum Release' and a 'Non-Plenum Release' sub-table (the same isotope appears in both, e.g. Table 3.2-5
    I-131 2hr 1.22E+00 vs 4.71E+00): a leading `Release` column keeps every row unambiguous. The caption-less
    sheet 2 of Table 3.2-4 (p29) is merged."""
    out, els, i = [], doc.els, 0
    n_done = 0
    while i < len(els):
        e = els[i]
        if not (e.kind == "table" and re.match(r"^Table 3\.2-\d+\b", e.table.caption or "")):
            out.append(e)
            i += 1
            continue
        rows, pages = _rows(e.table), set(e.table.pages)
        j = i + 1
        while j < len(els) and els[j].kind == "table" and not els[j].table.caption and _is_source_term(els[j].table):
            rows += _rows(els[j].table)
            pages |= set(els[j].table.pages)
            j += 1
        release, times, data = None, None, []
        for r in rows:
            vals = [v for v in r if v]
            if not vals:
                continue
            if set(vals) <= set(RELEASE_LABELS):
                release = vals[0]
                continue
            if set(vals) == {ST_LABEL}:
                continue
            if r[0] == "Isotope":
                if times is None:
                    times = r[1:]
                elif times != r[1:]:
                    _warn(doc, f"{e.table.caption}: time columns differ between sub-tables")
                continue
            data.append((release, r))
        if times is None or not data:
            _warn(doc, f"{e.table.caption}: source-term structure not recognised")
            out.append(e)
            i += 1
            continue
        with_release = any(rel for rel, _ in data)
        header = (["Release"] if with_release else []) + ["Isotope"] + times
        body = [([rel or ""] if with_release else []) + r for rel, r in data]
        t = _new_table([header] + body, e.table.page, sorted(pages), e.table.caption, e.table.notes)
        e.table = t
        e.meta["rendered"] = ST_LABEL + "\n\n" + T.render_md(t)
        out.append(e)
        n_done += 1
        i = j
    doc.els = out
    doc.meta["ch03_source_term_tables"] = n_done


# --------------------------------------------------- 3.3.4.2 table order ----
def move_initial_conditions_table(doc, aux=None):
    """The Low/Full Power initial-conditions table follows '... used in the LBE analyses:' in 3.3.4.2 (PDF p50);
    reading order put it after the 3.3.4.3 heading."""
    els = doc.els
    ti = next((i for i, e in enumerate(els) if e.kind == "table" and not e.table.caption
               and e.table.grid and e.table.grid[0][0].text.strip() == "Plant Condition"), None)
    pi = next((i for i, e in enumerate(els) if e.kind == "para" and e.text.rstrip().endswith("used in the LBE analyses:")), None)
    if ti is None or pi is None:
        _warn(doc, "initial-conditions table or its lead-in sentence not found")
        return
    tab = els.pop(ti)
    if ti < pi:
        pi -= 1
    els.insert(pi + 1, tab)


# ---------------------------------------------- LBE sub-section order ----
LBE_REORDER = ("3.8.1.11", "3.8.2.6")   # PDF p87 (OTH-LMAC-4), p89 (IPI-IHEL-2)


def reorder_lbe_subsections(doc, aux=None):
    """OTH-LMAC-4 (3.8.1.11) and IPI-IHEL-2 (3.8.2.6): both sub-headings precede both paragraphs in the
    converter's reading order. PDF order: x.1 LBE Description + 'The postulated initiating event ...',
    x.2 Radiological Consequences + 'The fuel performance acceptance criteria ...'."""
    els = doc.els
    for num in LBE_REORDER:
        i0 = _heading_index(els, num)
        if i0 is None:
            _warn(doc, f"reorder: {num} not found")
            continue
        i1 = _section_end(els, i0)
        span = els[i0 + 1:i1]
        heads = {e.meta.get("num"): e for e in span if e.kind == "heading"}
        desc, rad = heads.get(num + ".1"), heads.get(num + ".2")
        paras = [e for e in span if e.kind != "heading"]
        d_par = [p for p in paras if p.text.startswith("The postulated initiating event")]
        r_par = [p for p in paras if p not in d_par]
        if not (desc and rad and len(heads) == 2 and d_par and r_par):
            _warn(doc, f"reorder: unexpected structure in {num}")
            continue
        els[i0 + 1:i1] = [desc] + d_par + [rad] + r_par


# ------------------------------------------------ LBE mini-table placement ----
def _table_kind(t):
    if t is None or t.n_rows < 2:
        return None
    h = " ".join(c.text for c in t.grid[0])
    if not re.match(r"^\s*(?:5th Percentile|Enveloping)", h):
        return None
    if "Enveloping" in h:
        return "dba"
    if "Frequency" in h:
        return "freq"
    if "TEDE" in h:
        return "dose"
    return None


def sentence_kind(sentence):
    s = sentence.lower()
    if "enveloping" in s:
        return "dba"
    if "frequency" in s:
        return "freq"
    if "tede" in s or "dose" in s:
        return "dose"
    return None


def announcements(text):
    """[(end_offset, kind)] for every '... are listed below.' sentence (kind judged on the whole sentence)."""
    res = []
    for m in LISTED.finditer(text):
        start = 0
        for b in SENT_BOUNDARY.finditer(text, 0, m.start()):
            start = b.end()
        k = sentence_kind(text[start:m.end()])
        if k:
            res.append((m.end(), k))
    return res


def _split_rows(e):
    """A multi-row LBE table is two adjacent PDF tables merged by the sheet merger; each PDF mini-table has one
    value row (e.g. RRS-CGR-CN + RRS-ISPL-CN on p112, RRS-SPLX-CN + RRS-SPLA-CN on p113)."""
    t = e.table
    if t.n_rows <= 2:
        return [e]
    res = []
    for r in range(1, t.n_rows):
        nt = _new_table([_rows(t)[0], _rows(t)[r]], t.page, t.pages)
        res.append(El("table", "", e.page, e.bbox, table=nt, id=e.id, meta=dict(e.meta)))
    return res


def relocate_lbe_tables(doc, aux=None):
    """Within 3.6-3.9 the i-th '... are listed below.' sentence of kind k (frequency / 30-day EAB TEDE / enveloping
    DBA dose) receives the i-th mini-table of kind k, placed right after the paragraph holding the sentence
    (PDF: every table follows its sentence on the same page; review_ch3 F1: 29 of 88 were displaced)."""
    els = doc.els
    s = _heading_index(els, "3.6")
    e_ = _heading_index(els, "3.10")
    if s is None or e_ is None:
        _warn(doc, "relocate: 3.6 or 3.10 heading missing")
        return
    region = els[s:e_]
    queues = {k: [] for k in LBE_KINDS}
    body = []
    for x in region:
        k = _table_kind(x.table) if x.kind == "table" else None
        if k:
            queues[k].extend(_split_rows(x))
        else:
            body.append(x)
    sents = collections.Counter()
    for x in body:
        if x.kind in ("para", "item", "caption"):
            for _, k in announcements(x.text):
                sents[k] += 1
    stats = {k: {"sentences": sents[k], "tables": len(queues[k])} for k in LBE_KINDS}
    doc.meta["ch03_lbe_tables"] = stats
    if any(sents[k] != len(queues[k]) for k in LBE_KINDS):
        _warn(doc, f"relocate: sentence/table counts differ {stats}; order left unchanged")
        return
    out, ptr = [], {k: 0 for k in LBE_KINDS}
    for x in body:
        ann = announcements(x.text) if x.kind in ("para", "item", "caption") else []
        if not ann:
            out.append(x)
            continue
        cut = 0
        for n, (end, k) in enumerate(ann):
            last = n == len(ann) - 1
            piece = x.text[cut:].strip() if last else x.text[cut:end].strip()
            cut = end
            el = _clone(x, kind="para" if x.kind == "caption" else x.kind, text=piece)
            out.append(el)
            out.append(queues[k][ptr[k]])
            ptr[k] += 1
    els[s:e_] = out


# ------------------------------------------------------------ headings ----
NUM_LINE = re.compile(r"^(3(?:\.\d+)+) (\S.*)$")


def promote_missed_headings(doc, aux):
    """Numbered headings the whitelist missed (their PDF block starts with list items): 3.12.3 Codes Used in System
    Evaluation (p124), 3.14.2.2 Ex-Vessel Storage Tank and 3.14.2.3 In-Vessel Storage (p130). Rule: an item/para
    whose whole text is 'N title', N a not-yet-emitted ch3 section number whose parent is emitted, and the PDF page
    has exactly that line at the body margin."""
    have = {e.meta.get("num") for e in doc.els if e.kind == "heading" and e.meta.get("numbered")}
    lines = aux.meta.get("lines_by_page", {}) if aux else {}
    for e in doc.els:
        if e.kind not in ("item", "para"):
            continue
        m = NUM_LINE.match(e.text.strip())
        if not m or m.group(1) in have or len(e.text) > 120:
            continue
        num = m.group(1)
        if num.rsplit(".", 1)[0] not in have:
            continue
        page_lines = lines.get(e.page, [])
        margin = min((ln.x0 for ln in page_lines if len(ln.text) > 20), default=None)
        if margin is None or not any(ln.text.strip() == e.text.strip() and abs(ln.x0 - margin) <= 3
                                     for ln in page_lines):
            continue
        e.kind, e.level = "heading", min(_depth(num), 6)
        e.meta.update({"num": num, "numbered": True, "heading_done": True, "promoted_by": "psar_ch03"})
        have.add(num)
        doc.meta.setdefault("ch03_promoted_headings", []).append(e.text.strip())


REF_ENTRY = re.compile(r"^\d+(?:\.\d+)+-\d+\s")


def split_glued_references(doc, aux=None):
    """'... stage. References' (3.11, p120) and '... TP-LIC-RPT-0011. References' (3.13, p126): the PDF has a
    standalone 'References' line; the following '3.x-n ...' paragraphs are reference entries."""
    out = []
    in_refs = False
    for e in doc.els:
        if e.kind == "para" and re.search(r"[.)”] References$", e.text.strip()):
            out.append(_clone(e, text=e.text.strip()[: -len("References")].rstrip()))
            out.append(El("heading", "References", e.page, e.bbox, id=e.id, meta={"keep_heading": True}))
            in_refs = True
            continue
        if in_refs and e.kind == "para" and REF_ENTRY.match(e.text.strip()):
            e.kind, e.level = "item", 0
            out.append(e)
            continue
        in_refs = False
        out.append(e)
    doc.els = out


# --------------------------------------------------------------- §3.14 ----
SUB = {"keff": "k<sub>eff</sub>", "σbias": "σ<sub>bias</sub>", "ΔSM": "Δ<sub>SM</sub>", "ΔAOA": "Δ<sub>AOA</sub>"}
EQ1 = "k<sub>eff</sub> + 2σ < USL (Equation 3.14-1)"
EQ2 = "USL = 1 + bias – σ<sub>bias</sub> – Δ<sub>SM</sub> – Δ<sub>AOA</sub> (Equation 3.14-2)"
WHERE_ITEMS = [
    "Bias is calculated as the difference between the calculated k<sub>eff</sub> and the critical experiment model. "
    "Because a positive bias can be non-conservative, the bias is set to zero when the calculated average "
    "k<sub>eff</sub> is greater than 1.0.",
    "σ<sub>bias</sub> is the uncertainty in the bias.",
    "Δ<sub>SM</sub> is an administrative margin, typically 0.05.",
    "Δ<sub>AOA</sub> is an additional subcritical margin to account for extensions in the area of applicability if "
    "the available benchmarks are not sufficiently similar to the fuel storage systems.",
]
ORPHAN_SYMBOLS = {"σ", "σbias ΔAOA", "ΔSM", "σbias ΔSM ΔAOA"}
INLINE_SYMBOL_FIXES = [   # (PDF p128, p129)
    ("(Reference 3.14-6). Bias, , and are computed", "(Reference 3.14-6). Bias, σ<sub>bias</sub>, and Δ<sub>AOA</sub> are computed"),
    ("to calculate the bias, , and for an input application", "to calculate the bias, σ<sub>bias</sub>, and Δ<sub>AOA</sub> for an input application"),
    ("much less than the standard value of 0.05", "much less than the standard Δ<sub>SM</sub> value of 0.05"),
]


def criticality_block(doc, aux=None):
    """3.14.2 equations and symbol list (PDF p127-129; review_ch3 §5-4 answer block, re-checked on the rendered
    pages): the converter dropped the symbols σ, σ_bias, Δ_SM, Δ_AOA from the sentences, left them as orphan
    lines, and put '(Equation 3.14-1/-2)' after the wrong lines. The block between the 3.14.2 heading and
    'The USLs are computed ...' is rebuilt; symbols inside later sentences are restored."""
    els = doc.els
    i0 = _heading_index(els, "3.14.2")
    if i0 is None:
        _warn(doc, "3.14.2 heading not found")
        return
    i1 = next((j for j in range(i0 + 1, len(els)) if els[j].text.startswith("The USLs are computed using either")), None)
    span = els[i0 + 1:i1] if i1 else []
    texts = [x.text.strip() for x in span]
    if not span or "Where," not in texts or "(Equation 3.14-2)" not in texts or not texts[0].startswith("The methodology used"):
        _warn(doc, "3.14.2 block structure not recognised; left unchanged")
        return
    first = span[0]
    cut = first.text.find(" The USLs are developed")
    p127a = first.text[:cut].strip() if cut > 0 else first.text.strip()
    p127b = first.text[cut:].strip() if cut > 0 else ""
    page2 = next((x.page for x in span[1:] if x.page != first.page), first.page + 1)

    def para(text, page):
        return El("para", text, page, meta={"ch03_block": "3.14.2"})

    new = [para(p127a, first.page)]
    if p127b:
        new.append(para(p127b, first.page))
    new += [
        para("The computed k<sub>eff</sub> for the system plus twice the Monte Carlo uncertainty (σ) must be less "
             "than the USL:", page2),
        para(EQ1, page2),
        para("This ensures that the USL is met at a 95 percent probability and 95 percent confidence level.", page2),
        para("The USL is defined as:", page2),
        para(EQ2, page2),
        para("Where,", page2),
    ]
    new += [El("item", t, page2, level=0, meta={"ch03_block": "3.14.2"}) for t in WHERE_ITEMS]
    els[i0 + 1:i1] = new
    # later sentences in 3.14.2 and orphan symbol lines
    j0 = _heading_index(els, "3.14.2")
    j1 = _section_end(els, j0)
    keep = []
    for k, x in enumerate(els):
        if j0 < k < j1 and x.kind == "para" and x.text.strip() in ORPHAN_SYMBOLS:
            continue
        if j0 < k < j1 and x.kind in ("para", "item"):
            for a, b in INLINE_SYMBOL_FIXES:
                x.text = x.text.replace(a, b)
        keep.append(x)
    doc.els = keep


def symbol_subscripts(doc, aux=None):
    """k_eff (9x, PDF p127-131: 'eff' 7.7-pt subscript), F_ΔH / F_Z / F_XY (p122, 7.7-pt subscripts)."""
    def fix(s):
        s = re.sub(r"(?<![\w<>])keff(?!\w)", "k<sub>eff</sub>", s)
        s = re.sub(r"(?<=factor, )F(ΔH|Z|XY)(?=,)", r"F<sub>\1</sub>", s)
        return s
    for e in doc.els:
        if e.kind in ("para", "item", "heading", "caption"):
            e.text = fix(e.text)
        elif e.kind == "table":
            for row in e.table.grid:
                for c in row:
                    c.text = fix(c.text)


# ------------------------------------------------------- paragraphs ----
def join_split_paragraphs(doc, aux=None):
    """Paragraph halves split by a page break ('... is assumed to occur' | '2.5 days after ...' p65-66;
    '... The leakage rate out of the' | 'HAA is assumed ...' p105-106) or a line ending in a quotation mark
    ('... Limits,”' | '(Reference 3.14-3).' p128; '... Revision 0' | '(Reference 3.11-1), which ...' p120)."""
    out = []
    for e in doc.els:
        prev = out[-1] if out else None
        if prev is not None and prev.kind == "para" and e.kind == "para" and not prev.meta.get("ch03_block"):
            p, t = prev.text.rstrip(), e.text.strip()
            ref_cont = bool(re.match(r"^\(Reference 3\.\d+-\d+\)", t)) and not p.endswith((".", ":", ";"))
            page_cont = e.page == prev.page + 1 and not p.endswith(TERMINAL) and t[:1].isalnum()
            if ref_cont or page_cont:
                prev.text = p + " " + t
                continue
        out.append(e)
    doc.els = out


# ------------------------------------------------------------- lists ----
def fix_list_markers(doc, aux=None):
    """'● Heat removal exceeds total heat produced ...' (p50) is a bullet item; nested POS items '- Peak Power',
    '- Minimum Power' (p9, dash glyph at x = 126 pt) carry their glyph in the text."""
    for e in doc.els:
        if e.kind == "para" and e.text.startswith("● "):
            e.kind, e.level, e.text = "item", 0, e.text[2:].strip()
        elif e.kind == "item" and e.level >= 1 and re.match(r"^- \S", e.text):
            e.text = e.text[2:]


STEPS = [
    drop_invisible_periods,
    fix_hazard_tables,
    fix_dba_summary,
    fix_bdbe_note,
    source_term_tables,
    move_initial_conditions_table,
    reorder_lbe_subsections,
    relocate_lbe_tables,
    promote_missed_headings,
    split_glued_references,
    criticality_block,
    join_split_paragraphs,
    symbol_subscripts,
    fix_list_markers,
]
