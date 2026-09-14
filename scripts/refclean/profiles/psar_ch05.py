"""Kemmerer Unit 1 PSAR Chapter 5 (Safety Functions, Design Criteria, and SSC Safety Classification) — chapter hooks.

Spec: meta/references_cleanup/file_reviews/review_ch45.md Part B (§1 findings, §2a per-PSF list, §5 rules and
do-not-fix list), spec decision D6 (PSF record format for Tables 5.2-1 … 5.2-4).
Runs after the common PSAR steps (text already normalised) and before `psar.assign_levels`.

Tables 5.2-1 … 5.2-4 are rebuilt from the PDF with pdfplumber (ruled cells, one text line per LBE / type / SSC)
and cross-checked cell by cell against the opendataloader JSON. The ODL grid cannot express the SSC line breaks,
the LBE/type line alignment or the DL3-RR2 row split, so it is used only as the independent check.

QA anomalies are collected in `doc.meta['psar_ch05_qa']` (empty on a clean run; asserted by the tests).
"""
import json
import re
from dataclasses import dataclass, field

from .. import normalize as N
from ..doc import El

TERMINAL = tuple('.:;?!”")’')
TABLE_PAGES = range(6, 21)
SR_TABLES = ("5.2-1", "5.2-2", "5.2-3")
CAPTION = re.compile(r"Table (5\.2-[1-4]) ([^\n]+?)\s*\n\s*\(Sheet (\d+) of (\d+)\)")
CONTINUED = re.compile(r"\s*\(continued\)\s*$", re.I)
SSC_END = re.compile(r"\([A-Z]{2,4}\)$")
RPCS = "Relevant PSAR Chapters and Sections"
RPCS_REF = re.compile(r"^(?:Section|Chapter)\s+\d+(?:\.\d+)*$")
REF_ENTRY = re.compile(r"\s+References\s+(?=\d+(?:\.\d+)*-\d+\s)")
ENUM_START = re.compile(r"^\(\d{1,2}\)\s")
ORDERED = re.compile(r"^\d{1,2}\.\s")

# Review ch45 §2a: the 62 PRA safety functions in table order (SR 25, NSRST 37).
EXPECTED_PSF = {
    "5.2-1": ["DL3-RC1", "DL3-RC2"],
    "5.2-2": [f"DL3-HR{n}" for n in range(1, 14)],
    "5.2-3": ["DL3-RR1", "DL3-RR2", "DL3-RR3", "DL3-RR4", "DL3-RR5", "DL3-RR5a", "DL3-RR6", "DL3-RR7", "DL3-RR8",
              "DL3-RR10"],
    "5.2-4": ["DL4-RC1", "DL4-RC3", "DL4-RC4", "DL4-RC6", "DL4-RC6a", "DL4-RC6b", "DL4-RC6c", "DL4-RC6d", "DL2-HR2",
              "DL4-HR1", "DL4-HR2", "DL4-HR3", "DL4-HR4", "DL4-HR6", "DL4-HR7", "DL2-RR2", "DL2-RR4", "DL2-RR7",
              "DL2-RR8", "DL2-RR10", "DL4-RR1", "DL4-RR1a", "DL4-RR1b", "DL4-RR1c", "DL4-RR3", "DL4-RR3a", "DL4-RR3b",
              "DL4-RR3c", "DL4-RR4", "DL4-RR4a", "DL4-RR4b", "DL4-RR4c", "DL4-RR5", "DL4-RR7", "DL4-RR8", "DL4-DID1",
              "DL5-PAM1"],
}


def _qa(doc, msg):
    doc.meta.setdefault("psar_ch05_qa", []).append(msg)


def ws(s):
    return " ".join((s or "").split())


# ---------------------------------------------------------------- paragraphs/lists ----
def join_enumeration_breaks(doc, aux=None, first_page=21):
    """PDC criteria wrapped before '(n)' or a lowercase word were split into two paragraphs by opendataloader
    (PDC 17, 31, 71, 77; review B19). A paragraph that ends with ':' (PDC 78 '(1) postulated leakage…') is a real
    new paragraph in the PDF (25 pt spacing) and stays."""
    out = []
    for e in doc.els:
        prev = out[-1] if out else None
        if (prev is not None and e.kind == "para" and prev.kind == "para" and e.page >= first_page
                and not prev.text.rstrip().endswith(TERMINAL)
                and (ENUM_START.match(e.text) or e.text[:1].islower())):
            prev.text = prev.text.rstrip() + " " + e.text.lstrip()
            doc.meta.setdefault("psar_ch05_joined", []).append((prev.page, e.text[:40]))
            continue
        out.append(e)
    doc.els = out


def pdf_paragraph_starts(pdf_path, pages):
    """{page: [first-line text]} of PDF body paragraphs: a line preceded on the same page by a vertical gap > 6 pt
    (normal line gap ≈ 1.5 pt, paragraph gap ≈ 12 pt) whose previous line ends a sentence."""
    import fitz
    from ..pdfaux import header_footer_band, page_lines
    out = {}
    with fitz.open(pdf_path) as pdf:
        for p in pages:
            if p > len(pdf):
                continue
            page = pdf[p - 1]
            top, bot = header_footer_band(page)
            prev = None
            for ln in page_lines(page):
                if not top <= (ln.y0 + ln.y1) / 2 <= bot:
                    continue
                if prev is not None and ln.y0 - prev.y1 > 6 and prev.text.rstrip().endswith(TERMINAL):
                    out.setdefault(p, []).append(ln.text)
                prev = ln
    return out


def split_merged_paragraphs(doc, aux=None, pages=range(4, 53), starts=None):
    """opendataloader merged some consecutive PDF paragraphs into one element (review B22, e.g. PDC 2
    '… described in Chapter 2.' | 'Design basis hazard levels …'). Split where a PDF paragraph start (up to 60
    characters of its first line, unique in the element) follows a sentence end inside a paragraph element on the
    same or next page."""
    starts = pdf_paragraph_starts(doc.pdf_path, pages) if starts is None else starts
    out = []
    for e in doc.els:
        if e.kind != "para" or e.meta.get("ordered_item") or e.page not in pages:
            out.append(e)
            continue
        cur = e
        for p in (e.page, e.page + 1):
            for s in starts.get(p, []):
                head = ws(s)[:60].strip()
                if len(head) < 20:
                    continue
                hits = [m for m in re.finditer(r"(?<=[.:;?!”\")])\s+" + re.escape(head), cur.text)]
                if len(hits) != 1:
                    continue
                cut = hits[0].start()
                before, after = cur.text[:cut].rstrip(), cur.text[cut:].lstrip()
                out.append(El(cur.kind, before, cur.page, cur.bbox, cur.font, cur.size, id=cur.id, meta=dict(cur.meta)))
                cur = El("para", after, p, (), cur.font, cur.size, id=cur.id, meta={"split_from": cur.id})
                doc.meta.setdefault("psar_ch05_para_splits", []).append((p, head))
        out.append(cur)
    doc.els = out


def rpcs_lists(doc, aux=None):
    """Content of each 'Relevant PSAR Chapters and Sections' subheading -> one list item per reference.
    Wrapped lines (PDC 15, 61, 73) are joined first; the §5.3 References heading and entry 5.3-1 glued to the
    PDC 82 list (review B7) are split off."""
    els, out, i = doc.els, [], 0
    n_lists = 0
    while i < len(els):
        e = els[i]
        out.append(e)
        i += 1
        if not (e.kind == "heading" and e.meta.get("sub") and ws(e.text) == RPCS):
            continue
        body = []
        while i < len(els) and els[i].kind in ("para", "item"):
            body.append(els[i])
            i += 1
        if not body:
            _qa(doc, f"empty {RPCS} list on p{e.page}")
            continue
        texts = [ws(b.text) for b in body]
        tail = []
        for k, t in enumerate(texts):
            m = REF_ENTRY.search(t)
            if m:
                ref = " ".join([t[m.end():]] + texts[k + 1:])
                tail = [El("heading", "References", body[k].page, meta={"keep_heading": True}),
                        El("item", ref, body[k].page, level=0, list_style="unordered")]
                texts = texts[:k] + [t[:m.start()]]
                break
        parts = [p.strip() for p in re.split(r",\s*", " ".join(texts)) if p.strip()]
        if not parts or not all(RPCS_REF.match(p) for p in parts):
            _qa(doc, f"{RPCS} list on p{e.page} not split: {' '.join(texts)[:80]}")
            out.extend(body)
            continue
        if len({b.page for b in body}) > 1:
            _qa(doc, f"{RPCS} list spans pages {sorted({b.page for b in body})}")
        out.extend(El("item", p, body[0].page, level=0, list_style="unordered", meta={"rpcs": True}) for p in parts)
        out.extend(tail)
        n_lists += 1
    doc.els = out
    doc.meta["psar_ch05_rpcs_lists"] = n_lists


def ordered_lists(doc, aux=None):
    """'1. Doppler …' items were emitted as '- 1. Doppler …' (bullet + number, review B21): Markdown ordered list."""
    n = 0
    for e in doc.els:
        if e.kind == "item" and ORDERED.match(e.text):
            e.kind, e.level = "para", 0
            e.meta["ordered_item"] = True
            n += 1
    doc.meta["psar_ch05_ordered_items"] = n


# --------------------------------------------------------------------- table notes ----
def table_notes(doc, aux=None):
    """Table 5.2-3 Note 1 is complete after re-conversion (checked); Table 5.2-4 'Note:' + superscript-1 note was cut
    at the page-20 line break ('application.' left as a paragraph) and its marker read as plain '1'."""
    els = doc.els
    for idx, e in enumerate(els):
        if e.kind != "table" or not e.table.caption.startswith("Table 5.2-"):
            continue
        notes = e.table.notes
        if e.table.caption.startswith("Table 5.2-3"):
            if not any("RFH-FDIV-CN" in n and n.rstrip().endswith("provided by DL3-RR10.") for n in notes):
                _qa(doc, f"Table 5.2-3 Note 1 incomplete: {notes}")
        if not e.table.caption.startswith("Table 5.2-4"):
            continue
        # continuation fragments of the last note (lowercase start, no heading in between)
        j = idx + 1
        while notes and j < len(els) and els[j].kind == "para" and els[j].text[:1].islower() \
                and not notes[-1].rstrip().endswith(TERMINAL):
            notes[-1] = notes[-1].rstrip() + " " + els[j].text.strip()
            els[j].kind = "drop"
            j += 1
        fixed = []
        for n in notes:
            m = re.match(r"^(Notes?:)\s+(\d)\s+(\S.*)$", n)
            if m and _superscript_marker(aux, e.table.pages[-1] if e.table.pages else e.page, m.group(2)):
                fixed += [m.group(1), f"<sup>{m.group(2)}</sup> {m.group(3)}"]
            else:
                fixed.append(n)
        e.table.notes = fixed
        if not (len(fixed) == 2 and fixed[0] == "Note:" and fixed[1].startswith("<sup>1</sup> DL4-RC6(a-d) ")
                and fixed[1].endswith("construction permit application.")):
            _qa(doc, f"Table 5.2-4 note unexpected: {fixed}")
    doc.els = [e for e in els if e.kind != "drop"]


def _superscript_marker(aux, page, mark):
    """True when the PDF line on `page` starts with a small raised `mark` span (table-note marker)."""
    body = (aux.meta.get("body_size") if aux else None) or 11.0
    for ln in ((aux.meta.get("lines_by_page") or {}).get(page, []) if aux else []):
        if ln.spans and ln.spans[0][0].strip() == mark and ln.spans[0][2] <= 0.8 * body:
            return True
    return False


# ----------------------------------------------------------------- PSF records ----
@dataclass
class PSF:
    table: str
    psf_id: str
    desc: str
    page: int
    lbes: list = field(default_factory=list)      # [(lbe, type)] in source order
    rows: list = field(default_factory=list)      # SR tables: [([ssc, …], srdc)]
    criteria: str = ""                            # Table 5.2-4
    sscs: list = field(default_factory=list)      # Table 5.2-4
    pages: list = field(default_factory=list)


def join_lines(text):
    """Cell text lines -> one string (a line ending in a letter + '-' continues without a space)."""
    out = ""
    for ln in (x.strip() for x in (text or "").split("\n")):
        if not ln:
            continue
        if out and re.search(r"[A-Za-z]-$", out) and ln[:1].isalpha():
            out += ln
        else:
            out = (out + " " + ln) if out else ln
    return out


def ssc_names(text):
    """SSC cell -> names, one per PDF line; a line not ending in '(ABC)' continues on the next line."""
    names, buf = [], ""
    for ln in (x.strip() for x in (text or "").split("\n")):
        if not ln:
            continue
        buf = f"{buf} {ln}".strip()
        if SSC_END.search(buf) or buf in ("See Note 1", "None"):
            names.append(buf)
            buf = ""
    if buf:
        names.append(buf)
    return names


def _cell_lines(page, bbox):
    """[(top, text)] of the visual lines inside a cell."""
    if bbox is None:
        return []
    crop = page.within_bbox(bbox)
    return [(ln["top"], ln["text"].strip()) for ln in crop.extract_text_lines(strip=True) if ln["text"].strip()]


def _pair_by_y(page, lbe_bbox, type_bbox, lbe_text, type_text, where, qa):
    """LBE/type pairs aligned by line position; the order-based pairing of the cell texts must agree."""
    by_order = list(zip([x for x in lbe_text.split("\n") if x.strip()], [x for x in type_text.split("\n") if x.strip()]))
    a, b = _cell_lines(page, lbe_bbox), _cell_lines(page, type_bbox)
    pairs, used = [], set()
    for top, lbe in a:
        k = min((k for k in range(len(b)) if k not in used), key=lambda k: abs(b[k][0] - top), default=None)
        if k is None or abs(b[k][0] - top) > 3:
            qa(f"{where}: LBE {lbe} has no type on its line")
            continue
        used.add(k)
        pairs.append((lbe, b[k][1]))
    if len(a) != len(b) or pairs != [(x.strip(), y.strip()) for x, y in by_order]:
        qa(f"{where}: LBE/type pairing by position differs from cell order ({len(a)} LBE lines, {len(b)} type lines)")
    return pairs


def extract_psf_tables(pdf_path, pages=TABLE_PAGES, qa=None):
    """{table_no: {'caption', 'header', 'records': [PSF], 'pages'}} from the PDF (pdfplumber ruled tables)."""
    import pdfplumber
    qa = qa or (lambda m: None)
    tables = {}
    with pdfplumber.open(pdf_path) as pdf:
        for pno in pages:
            page = pdf.pages[pno - 1]
            found = page.find_tables()
            if len(found) != 1:
                qa(f"p{pno}: {len(found)} ruled tables")
                continue
            tb = found[0]
            m = CAPTION.search(page.extract_text() or "")
            if not m:
                qa(f"p{pno}: no 'Table 5.2-n … (Sheet n of m)' caption")
                continue
            no, title = m.group(1), ws(m.group(2))
            rows = tb.extract()
            boxes = [r.cells for r in tb.rows]
            header = [ws(join_lines(c)) if c is not None else None for c in rows[0]]
            t = tables.setdefault(no, {"caption": f"Table {no} {title}", "header": header, "records": [], "pages": []})
            t["pages"].append(pno)
            if header != t["header"]:
                qa(f"p{pno}: header differs from first sheet: {header}")
            if t["caption"] != f"Table {no} {title}":
                qa(f"p{pno}: caption differs: {title}")
            recs = t["records"]
            cur, last_ssc = None, None
            for i, r in enumerate(rows[1:], 1):
                if len(r) != 6:
                    qa(f"p{pno} row {i}: {len(r)} columns")
                    continue
                if r[0] is not None and ws(r[0]):
                    pid = join_lines(r[0])
                    cont = bool(CONTINUED.search(pid))
                    pid = CONTINUED.sub("", pid)
                    desc = CONTINUED.sub("", join_lines(r[1]))
                    if cont:
                        cur = recs[-1] if recs else None
                        if cur is None or cur.psf_id != pid or cur.desc != desc:
                            qa(f"p{pno}: '(continued)' row {pid} does not continue the previous record")
                            continue
                        cur.pages.append(pno)
                    else:
                        cur = PSF(no, pid, desc, pno, pages=[pno])
                        recs.append(cur)
                        if no == "5.2-4":
                            cur.criteria = join_lines(r[2])
                            cur.sscs = ssc_names(r[5])
                    last_ssc = None
                elif cur is None:
                    qa(f"p{pno} row {i}: row before the first PSF ID")
                    continue
                where = f"{cur.psf_id} p{pno}"
                if no == "5.2-4":
                    lbe, typ = join_lines(r[3]), join_lines(r[4])
                    if r[3] is None or r[4] is None or not lbe or not typ:
                        qa(f"{where} row {i}: empty LBE/type cell")
                    else:
                        cur.lbes.append((lbe, typ))
                    if r[0] is None and r[5] is not None:
                        qa(f"{where} row {i}: SSC cell in a continuation row")
                    continue
                if r[2] is not None and r[0] is not None:
                    cur.lbes.extend(_pair_by_y(page, boxes[i][2], boxes[i][3], r[2] or "", r[3] or "", where, qa))
                ssc = ssc_names(r[4]) if r[4] is not None else last_ssc
                srdc = join_lines(r[5]) if r[5] is not None else None
                if srdc is None:
                    qa(f"{where} row {i}: merged SRDC cell")
                    continue
                if not ssc and not srdc:
                    continue            # '(continued)' row: LBEs only
                if not ssc or not srdc:
                    qa(f"{where} row {i}: SSC {ssc!r} without SRDC or vice versa")
                cur.rows.append((ssc or [], srdc))
                last_ssc = ssc
    for no, t in tables.items():
        ids = [r.psf_id for r in t["records"]]
        if ids != EXPECTED_PSF.get(no):
            qa(f"Table {no}: PSF IDs {ids} != expected {EXPECTED_PSF.get(no)}")
    return tables


# ---- independent check: opendataloader JSON cells (recursive text of nested paragraphs / list items) ----
def _node_text(node):
    parts = []
    c = (node.get("content") or "").strip()
    if c and node.get("type") not in ("table cell", "list"):
        parts.append(c)
    for it in node.get("list items", []) or []:
        parts.append(_node_text(it))
    for k in node.get("kids", []) or []:
        parts.append(_node_text(k))
    return " ".join(p for p in parts if p)


def _odl_grid(node):
    n_r = int(node.get("number of rows") or 0)
    n_c = int(node.get("number of columns") or 0)
    grid = [[None] * n_c for _ in range(n_r)]
    for row in node.get("rows", []):
        for cell in row.get("cells", []):
            r, c = int(cell["row number"]) - 1, int(cell["column number"]) - 1
            rs, cs = max(1, int(cell.get("row span", 1))), max(1, int(cell.get("column span", 1)))
            text = ws(_node_text(cell))
            for i in range(r, min(r + rs, n_r)):
                for j in range(c, min(c + cs, n_c)):
                    grid[i][j] = ("cell" if (i, j) == (r, c) else "span", text)
    return grid


def odl_psf_records(json_path, pages=TABLE_PAGES):
    """{psf_id: dict} rebuilt from the opendataloader table cells (handles the DL3-RR2 row split and the SRDC
    sentence cut across two rows)."""
    with open(json_path, encoding="utf-8") as f:
        tree = json.load(f)
    recs, cur = {}, None
    for node in tree.get("kids", []):
        if node.get("type") != "table" or node.get("page number") not in pages:
            continue
        grid = _odl_grid(node)
        nsrst = grid[0][5] is not None and grid[0][5][1] == "SSC(s)"
        for r in range(1, len(grid)):
            row = grid[r]
            k, pid = row[0] or ("none", "")
            if k == "cell" and pid:
                cont = bool(CONTINUED.search(pid))
                pid = CONTINUED.sub("", pid)
                if cont and pid in recs:
                    cur = recs[pid]
                else:
                    cur = recs[pid] = {"desc": row[1][1] if row[1] else "", "lbes": [], "types": [], "rows": [],
                                       "criteria": row[2][1] if (nsrst and row[2]) else "",
                                       "sscs": row[5][1] if (nsrst and row[5]) else ""}
            if cur is None:
                continue
            for col, key in ((3, "lbes"), (4, "types")) if nsrst else ((2, "lbes"), (3, "types")):
                if row[col] and row[col][0] == "cell":
                    cur[key] += row[col][1].split()
            if nsrst:
                continue
            ssc, srdc = row[4], row[5]
            srdc_t = srdc[1] if srdc and srdc[0] == "cell" else ""
            if ssc and ssc[1] and srdc_t:
                cur["rows"].append([ssc[1], srdc_t])
            elif srdc_t and cur["rows"]:
                cur["rows"][-1][1] = ws(cur["rows"][-1][1] + " " + srdc_t)
    return recs


def crosscheck_odl(tables, json_path):
    """Differences between the pdfplumber records and the opendataloader cells (empty = both extractions agree)."""
    odl = odl_psf_records(json_path)
    diffs = []
    for no, t in tables.items():
        for rec in t["records"]:
            o = odl.get(rec.psf_id)
            if o is None:
                diffs.append(f"{rec.psf_id}: not in ODL tables")
                continue
            if ws(rec.desc) != ws(CONTINUED.sub("", o["desc"])):
                diffs.append(f"{rec.psf_id}: description {rec.desc!r} vs ODL {o['desc']!r}")
            if [x for x, _ in rec.lbes] != o["lbes"] or [y for _, y in rec.lbes] != o["types"]:
                diffs.append(f"{rec.psf_id}: LBE/type lists differ ({len(rec.lbes)} vs ODL {len(o['lbes'])}/"
                             f"{len(o['types'])})")
            if no == "5.2-4":
                if ws(rec.criteria) != o["criteria"]:
                    diffs.append(f"{rec.psf_id}: criteria {rec.criteria!r} vs ODL {o['criteria']!r}")
                if ws(" ".join(rec.sscs)) != o["sscs"]:
                    diffs.append(f"{rec.psf_id}: SSC(s) {' '.join(rec.sscs)!r} vs ODL {o['sscs']!r}")
                continue
            mine = [[ws(" ".join(s)), ws(d)] for s, d in rec.rows]
            if mine != o["rows"]:
                for a, b in zip(mine, o["rows"]):
                    if a != b:
                        diffs.append(f"{rec.psf_id}: SSC/SRDC {a} vs ODL {b}")
                if len(mine) != len(o["rows"]):
                    diffs.append(f"{rec.psf_id}: {len(mine)} SSC/SRDC rows vs ODL {len(o['rows'])}")
    return diffs


# ---- rendering ----
def _lbe_field(label, pairs):
    """LBEs grouped by consecutive type run (source order kept): each LBE sits under its own type label."""
    if not pairs:
        return [f"- **{label}:** (none in source)"]
    if len(pairs) == 1 and pairs[0][0] == "None":
        return [f"- **{label}:** None / {pairs[0][1]}"]
    runs = []
    for lbe, typ in pairs:
        if runs and runs[-1][0] == typ:
            runs[-1][1].append(lbe)
        else:
            runs.append((typ, [lbe]))
    return [f"- **{label}:**"] + [f"  - {typ}: {', '.join(lbes)}" for typ, lbes in runs]


def render_record(rec, header, level, fix=lambda s: s):
    h = header
    lines = [f"{'#' * level} {rec.psf_id} — {fix(rec.desc)}", "",
             f"- **{h[0]}:** {rec.psf_id}", f"- **{h[1]}:** {fix(rec.desc)}"]
    if rec.table == "5.2-4":
        lines.append(f"- **{h[2]}:** {fix(rec.criteria)}")
        lines += _lbe_field(h[3], rec.lbes)
        sscs = [fix(s) for s in rec.sscs]
        if len(sscs) == 1:
            lines.append(f"- **{h[5]}:** {sscs[0]}")
        else:
            lines += [f"- **{h[5]}:**"] + [f"  - {s}" for s in sscs]
        return "\n".join(lines)
    lines += _lbe_field(f"{h[2]} / {h[3]}", rec.lbes)
    lines += ["", f"| {h[4]} | {h[5]} |", "|---|---|"]
    for sscs, srdc in rec.rows:
        cell = "; ".join(fix(s) for s in sscs).replace("|", "\\|")
        lines.append(f"| {cell} | {fix(srdc).replace('|', chr(92) + '|')} |")
    return "\n".join(lines)


def render_table_records(t, doc, aux, first_page):
    level = min(len("5.2".split(".")) + 2, 6)      # caption '### Table 5.2-n' (psar.assign_levels) + 1
    hmap = aux.hyphen_map if aux else {}

    def fixer(page):
        sups = [s.sup for s in aux.sups.get(page, [])] if aux else None
        return lambda s: N.text_pipeline(s, sups, hmap)

    parts, cur = [], first_page
    for rec in t["records"]:
        if rec.page != cur:
            lab = doc.page_labels.get(rec.page)
            parts.append(f"<!-- page {rec.page}{' | ' + lab if lab else ''} -->")
            cur = rec.page
        parts.append(render_record(rec, t["header"], level, fixer(rec.page)))
    return "\n\n".join(parts)


def psf_records(doc, aux):
    """Tables 5.2-1 … 5.2-4 -> caption heading + one record per PSF ID (spec D6)."""
    qa = lambda m: _qa(doc, m)       # noqa: E731
    tables = extract_psf_tables(doc.pdf_path, qa=qa)
    for d in crosscheck_odl(tables, doc.json_path):
        qa("ODL cross-check: " + d)
    done = set()
    for e in doc.els:
        if e.kind != "table":
            continue
        m = re.match(r"^Table (5\.2-[1-4]) ", e.table.caption or "")
        if not m or m.group(1) not in tables:
            continue
        t = tables[m.group(1)]
        if ws(e.table.caption) != t["caption"]:
            qa(f"caption {e.table.caption!r} vs PDF {t['caption']!r}")
        e.meta["rendered"] = render_table_records(t, doc, aux, e.page)
        e.meta["psf_records"] = [r.psf_id for r in t["records"]]
        e.table.pages = t["pages"]
        done.add(m.group(1))
    for no in ("5.2-1", "5.2-2", "5.2-3", "5.2-4"):
        if no not in done:
            qa(f"Table {no}: no table element to replace")
    doc.meta["psar_ch05_psf"] = {no: [(r.psf_id, len(r.lbes), len(r.rows) if no != "5.2-4" else len(r.sscs))
                                      for r in t["records"]] for no, t in tables.items()}


STEPS = [
    join_enumeration_breaks,
    split_merged_paragraphs,
    rpcs_lists,
    ordered_lists,
    table_notes,
    psf_records,
]
