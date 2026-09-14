"""U.S. NRC Regulatory Guide 1.232, Rev. 0 (April 2018), "Guidance for Developing Principal Design Criteria for
Non-Light-Water Reactors" -- non-chapter document profile.

Spec: meta/references_cleanup/file_reviews/review_rg.md (section 1 findings, section 4 outline, section 5.1 record
layout, section 5.2 ordered rules, section 5.4 do-not-fix list) and decisions D1-D7 in
meta/references_cleanup/cleanup_review_2026-09-11.md.

Text sources:
- opendataloader JSON element stream for the running text (pages 1-29, 62, 104-105);
- PyMuPDF spans inside the opendataloader table-cell boxes for Table 1 (redline colours: red = deleted,
  blue #1f497c = inserted) and for the Appendix A-C tables (italic criterion titles, paragraph breaks = blank rows,
  line-end hyphens kept, GDC 19 "emphasis added" italics); the cell text is cross-checked against the JSON cell text;
- the raw md ``~~...~~`` marks (detect_strikethrough) only as a cross-check of the red spans.

Every explicit list below (footnotes, hyphens, joins, headings) comes from review_rg.md and was checked on the PDF.
"""
import collections
import difflib
import json
import os
import re

import fitz

from .. import normalize as N
from .. import structure as S
from ..doc import El
from ..figures import odl_to_visible

KEY = "RG_1.232"
RED, BLUE = 0xFF0000, 0x1F497C
TERMINAL = (".", ":", ";", "”", ")", '"', "?", "!")
PARA_GAP = 6.0              # pt between two text rows of one cell that marks a paragraph break (normal: 0.4-0.5)
BLANK_GAP = 8.0             # pt of empty space at a cell border that marks a source empty line (padding: 3-5)

# ------------------------------------------------------------------ explicit lists (review_rg.md) ----
# Section 1.2: the 14 footnote reference marks (7 pt superscripts glued to the preceding token by the converter).
FOOTNOTES = [
    # n, page of the mark, exact converter text, replacement
    (1, 1, "(Ref. 2)1.", "(Ref. 2)[^1]."),
    (2, 7, "10 CFR 50.342 states", "10 CFR 50.34[^2] states"),
    (3, 8, "information available.3 DOE", "information available.[^3] DOE"),
    (4, 11, "for developing PDC4.", "for developing PDC[^4]."),
    (5, 21, "applicants and licensees5 may", "applicants and licensees[^5] may"),
    (6, 21, "may voluntarily6 use", "may voluntarily[^6] use"),
    (7, 25, "REFERENCES7", "REFERENCES[^7]"),
    (8, 26, "ML14353A248)8.", "ML14353A248)[^8]."),
    (9, 27, "download.php?doc=77089 9", "download.php?doc=77089[^9]"),
    (10, 28, "sdc_report_2may2013.pdf 10.", "sdc_report_2may2013.pdf[^10]."),
    (11, 28, "SFRTechnologyOverview.pdf 11.", "SFRTechnologyOverview.pdf[^11]."),
    (12, 28, "S030645491500580012.", "S0306454915005800[^12]."),
    (13, 62, "loop-type designs.13 Applicants", "loop-type designs.[^13] Applicants"),
    (14, 104, "(MHTGR-DC).14 These", "(MHTGR-DC).[^14] These"),
]
FOOTNOTE_BODY_PAGES = {1: 1, 2: 7, 3: 8, 4: 11, 5: 21, 6: 21, 7: 25, 8: 26, 9: 27, 10: 28, 11: 28, 12: 28,
                       13: 62, 14: 104}

# Section 1.3: line-end hyphens removed by the converter ("A-" + newline + "B" -> "AB"); PDF evidence = the
# line-end pair list (identical to the PyMuPDF hyphen map for this PDF).  Applied to converter text only; the
# appendix/Table 1 text rebuilt from PDF rows keeps its line-end hyphens.  NOT in the list (source spelling):
# 'watercooled' (p7), 'fire- resistant' (p31), 'SFR-DC17' (no space, as printed).
HYPHEN_RESTORE = [
    (r"\bSFRDC(?=\s?\d)", "SFR-DC"),
    (r"\bMHTGRDC\b", "MHTGR-DC"),
    (r"\bSECY-150002\b", "SECY-15-0002"),
    (r"\bSECY94-084\b", "SECY-94-084"),
    (r"\bNUREG1368\b", "NUREG-1368"),
    (r"www\.gen4\.org", "www.gen-4.org"),
    (r"NPTDSmexico", "NPTDS-mexico"),
    (r"\bnonLWR", "non-LWR"),
    (r"\bNonLWR", "Non-LWR"),
    (r"\bNonLight\b", "Non-Light"),
    (r"\bpreapplication\b", "pre-application"),
    (r"\bsodiumcooled\b", "sodium-cooled"),
    (r"\bstructurespecific\b", "structure-specific"),
    (r"\bleaktightness\b", "leak-tightness"),
    (r"\bfireresistant\b", "fire-resistant"),
    (r"\btechnologyspecific\b", "technology-specific"),
    (r"\bheight-todiameter\b", "height-to-diameter"),
    (r"\bFacilitySpecific\b", "Facility-Specific"),
    (r"\bheatresistant\b", "heat-resistant"),
    (r"\blossof-coolant\b", "loss-of-coolant"),
    (r"\bliquidmetal\b", "liquid-metal"),
    (r"\bpressureretaining\b", "pressure-retaining"),
    (r"\bpressurizedwater\b", "pressurized-water"),
    (r"\bRadioactiveWaste-", "Radioactive-Waste-"),
    (r"\bMHTGRspecific\b", "MHTGR-specific"),
    (r"\boffnormal\b", "off-normal"),
    (r"\bsafetyrelated\b", "safety-related"),
    (r"\btechnologiesspecifically\b", "technologies—specifically"),
]
# joined forms (no dash) of every review-listed line-end pair; used to audit the joins made in PDF-rebuilt text
HYPHEN_JOINED = {"SFRDC", "MHTGRDC", "SECY150002", "SECY94084", "NUREG1368", "gen4", "NPTDSmexico", "nonLWR",
                 "nonLWRs", "NonLWRs", "NonLight", "preapplication", "sodiumcooled", "structurespecific",
                 "leaktightness", "fireresistant", "technologyspecific", "todiameter", "FacilitySpecific",
                 "heatresistant", "lossof", "liquidmetal", "pressureretaining", "pressurizedwater", "RadioactiveWaste",
                 "MHTGRspecific", "offnormal", "safetyrelated", "technologiesspecifically", "INLEXT10", "INLEXT11"}

# Paragraph fragments split by a page/column break or by an inserted footnote body (section 1 F14), joined here.
JOINS = [
    # page of the first fragment, its end, the start of the next fragment, separator
    (2, "include the", "PDC for a proposed facility.", " "),
    (8, "“Response to NRC Staff", "Questions on the U.S. Department of Energy Report", " "),
    (9, "public meeting held on October", "11, 2016 (Ref. 23)", " "),
    (27, "SDC-TF/2013/01", "May 1, 2013, p. 57.", " "),
    (28, "White Paper,” INL/EXT-", "10-17997, Rev.0", ""),
    (28, "Idaho National Laboratory, INL/EXT-", "11-22708, Rev.0", ""),
]

# Section 4 intended outline: (page, text as emitted, level). Order = document order after the two fixes.
HEADINGS = [
    (1, "GUIDANCE FOR DEVELOPING PRINCIPAL DESIGN CRITERIA FOR NON-LIGHT-WATER REACTORS", 1),
    (1, "A. INTRODUCTION", 2),
    (1, "Purpose", 3),
    (1, "Applicability", 3),
    (1, "Applicable Regulations", 3),
    (2, "Related Guidance, Communications, and Policy Statements", 3),
    (3, "Purpose of Regulatory Guides", 3),
    (3, "Paperwork Reduction Act", 3),
    (3, "Public Protection Notification", 3),
    (5, "B. DISCUSSION", 2),
    (5, "Reason for Issuance", 3),
    (5, "Background", 3),
    (5, "The NRC Regulatory Framework", 4),
    (6, "Role of the General Design Criteria in the Regulatory Framework", 4),
    (6, "NRC Policy on Advanced Reactors", 4),
    (7, "Role of the General Design Criteria for Non-LWRs", 4),
    (8, "DOE-NRC Initiative Phase 1", 4),
    (8, "DOE-NRC Initiative Phase 2", 4),
    (9, "Key Assumptions and Clarifications Regarding the non-LWR Design Criteria", 4),
    (10, "Harmonization with International Standards", 4),
    (11, "C. STAFF REGULATORY GUIDANCE", 2),
    (11, "Intended Use of This Regulatory Guide", 3),
    (12, "Non-LWR Crosswalk Table", 3),
    (21, "D. IMPLEMENTATION", 2),
    (21, "Use by Applicants and Licensees", 3),
    (21, "Use by NRC Staff", 3),
    (23, "ACRONYMS/ABBREVIATIONS", 2),
    (25, "REFERENCES[^7]", 2),
    (29, "Appendix A. Advanced Reactor Design Criteria", 2),
    (62, "Appendix B. Sodium-Cooled Fast Reactor Design Criteria", 2),
    (104, "Appendix C. Modular High-Temperature Gas-Cooled Reactor Design Criteria", 2),
]
APPENDIX_HEADING_SRC = {
    "APPENDIX A ADVANCED REACTOR DESIGN CRITERIA": "Appendix A. Advanced Reactor Design Criteria",
    "APPENDIX B SODIUM-COOLED FAST REACTOR DESIGN CRITERIA": "Appendix B. Sodium-Cooled Fast Reactor Design Criteria",
    "APPENDIX C MODULAR HIGH-TEMPERATURE GAS-COOLED REACTOR DESIGN CRITERIA":
        "Appendix C. Modular High-Temperature Gas-Cooled Reactor Design Criteria",
}
# headings buried in running text: (page, containing text fragment, heading text)
BURIED = [
    (6, "10 CFR 50.34(a)(3). NRC Policy on Advanced Reactors", "NRC Policy on Advanced Reactors"),
    (9, "public comments. Key Assumptions and Clarifications Regarding the non-LWR Design Criteria The NRC staff",
     "Key Assumptions and Clarifications Regarding the non-LWR Design Criteria"),
]

TABLE1_CAPTION = "TABLE 1: NON-LIGHT-WATER-REACTOR CROSSWALK"   # printed page header of p13-20
TABLE1_PAGES = (13, 20)
APPENDICES = [
    # letter, set name, first/last table page, aliases prefix (vault naming wiki/SFRDC_n.md)
    ("A", "ARDC", 30, 61, None),
    ("B", "SFR-DC", 63, 103, "SFRDC"),
    ("C", "MHTGR-DC", 106, 133, None),
]
EXPECTED_IDS = {
    "ARDC": [*range(1, 6), *range(10, 47), *range(50, 58), *range(60, 65)],
    "SFR-DC": [*range(1, 6), *range(10, 47), *range(50, 58), *range(60, 65), *range(70, 80)],
    "MHTGR-DC": [*range(1, 6), *range(10, 47), *range(50, 58), *range(60, 65), *range(70, 73)],
}
STATUS_RE = re.compile(r"^(Same as GDC|Same as ARDC|Not applicable to MHTGR)(\.?)(?=\s|$)")
STATUS_TAIL_RE = re.compile(r"\s+(Same as (?:GDC|ARDC)|Not applicable to MHTGR)\.?$")
XW_STATUS_RE = re.compile(r"(Modified for (?:ARDC|SFR-DC|MHTGR-DC)|DELETED and incorporated into ARDC 26)$")
XW_WHOLE_STATUS = ("Same as GDC", "Same as ARDC", "Not applicable to MHTGR.", "N/A")
EMPHASIS_CRITERIA = {"19"}      # D7: GDC 19 rationale "(with emphasis added)" italics, all three appendices


def ws(s):
    return " ".join((s or "").split())


# ------------------------------------------------------------------------------------ context ----
class _Span:
    __slots__ = ("text", "rect", "font", "color", "size", "chars")

    def __init__(self, text, rect, font, color, size, chars=None):
        self.text, self.rect, self.font, self.color, self.size = text, rect, font, color, size
        self.chars = chars or []          # [(c, fitz.Rect)] in visible coordinates

    @property
    def italic(self):
        return "Italic" in self.font

    def clip(self, rect):
        """The part of this span whose characters have their centre inside rect (None if empty).

        PDF spans may run across table-cell borders (e.g. Table 1 row 11: one span holds the GDC and the ARDC
        title), so cell text is assigned character by character."""
        keep = [(c, r) for c, r in self.chars if rect.contains(fitz.Point((r.x0 + r.x1) / 2, (r.y0 + r.y1) / 2))]
        if not keep:
            return None
        if len(keep) == len(self.chars):
            return self
        box = fitz.Rect(keep[0][1])
        for _c, r in keep[1:]:
            box |= r
        return _Span("".join(c for c, _r in keep), box, self.font, self.color, self.size, keep)


class _Ctx:
    """PDF spans per page (visible coordinates, whitespace spans kept) + JSON table nodes by id."""

    def __init__(self, doc):
        self.pdf = fitz.open(doc.pdf_path)
        with open(doc.json_path, encoding="utf-8") as f:
            tree = json.load(f)
        self.tables = {n.get("id"): n for n in tree.get("kids", []) if n.get("type") == "table"}
        self._spans = {}
        self.warnings = []
        self.hyphen_joins = collections.Counter()
        self.stats = {}

    def spans(self, pno):
        if pno not in self._spans:
            page = self.pdf[pno - 1]
            m = page.rotation_matrix
            out = []
            for b in page.get_text("rawdict")["blocks"]:
                for ln in b.get("lines", []):
                    for s in ln["spans"]:
                        chars = []
                        for ch in s.get("chars", []):
                            r = fitz.Rect(ch["bbox"]) * m
                            r.normalize()
                            chars.append((ch["c"], r))
                        if not chars:
                            continue
                        r = fitz.Rect(s["bbox"]) * m
                        r.normalize()
                        out.append(_Span("".join(c for c, _r in chars), r, s["font"], s["color"], s["size"], chars))
            self._spans[pno] = out
        return self._spans[pno]

    def close(self):
        self.pdf.close()


def _ctx(doc):
    c = doc.meta.get("_rg")
    if c is None:
        c = _Ctx(doc)
        doc.meta["_rg"] = c
    return c


def _fail(msg):
    raise ValueError(f"{KEY} profile: {msg}")


# --------------------------------------------------------------------------- text normalisation ----
def restore_hyphens(s):
    for pat, rep in HYPHEN_RESTORE:
        s = re.sub(pat, rep, s)
    return s


_MD_LEAD = re.compile(r"^(\d{1,3})([.)])(\s)|^([-+*>#])(\s)")


def md_safe(s):
    """Escape a leading character that would turn a running-text paragraph into a list/quote/heading."""
    return _MD_LEAD.sub(lambda m: (m.group(1) + "\\" + m.group(2) + m.group(3)) if m.group(1)
                        else ("\\" + m.group(4) + m.group(5)), s, count=1)


def text_pipeline(s):
    s = N.decode_entities(s)
    s = N.squash_ws(s)
    s = restore_hyphens(s)
    return N.obsidian_escape(s)


# --------------------------------------------------------------------------------- PDF cell text ----
def cell_rows(ctx, pno, odl_bbox):
    """Visual rows of the PDF text inside an opendataloader cell box: [{y0, y1, spans, blank}] top to bottom."""
    page = ctx.pdf[pno - 1]
    rect = odl_to_visible(odl_bbox, page)
    inside = []
    for s in ctx.spans(pno):
        if s.rect.intersects(rect):
            part = s.clip(rect)
            if part is not None:
                inside.append(part)
    rows = []
    for s in sorted(inside, key=lambda s: (s.rect.y0, s.rect.x0)):
        mid = (s.rect.y0 + s.rect.y1) / 2
        for row in rows:
            if row["y0"] - 1 <= mid <= row["y1"] + 1:
                row["spans"].append(s)
                row["y0"], row["y1"] = min(row["y0"], s.rect.y0), max(row["y1"], s.rect.y1)
                break
        else:
            rows.append({"y0": s.rect.y0, "y1": s.rect.y1, "spans": [s]})
    rows.sort(key=lambda r: r["y0"])
    for row in rows:
        row["spans"].sort(key=lambda s: s.rect.x0)
        row["blank"] = not "".join(s.text for s in row["spans"]).strip()
    return rect, rows


def row_runs(row):
    """[[text, italic, color], ...] for one visual row; a space is inserted between spans separated by a gap."""
    runs, prev = [], None
    for s in row["spans"]:
        t = s.text
        if prev is not None and s.rect.x0 - prev.rect.x1 > 1.0 and not prev.text.endswith(" ") \
                and not t.startswith(" "):
            t = " " + t
        runs.append([t, s.italic, s.color])
        prev = s
    return runs


def plain(runs):
    return "".join(r[0] for r in runs)


def _rstrip_runs(runs):
    while runs and not runs[-1][0].strip():
        runs.pop()
    if runs:
        runs[-1][0] = runs[-1][0].rstrip()


def _lstrip_runs(runs):
    while runs and not runs[0][0].strip():
        runs.pop(0)
    if runs:
        runs[0][0] = runs[0][0].lstrip()


def join_line(cur, runs, ctx=None):
    """Append the runs of the next visual row to a paragraph: a line-end '-' or '—' before an alphanumeric
    start is kept and joined without a space (PDF evidence: review_rg section 1.3); otherwise one space."""
    _rstrip_runs(cur)
    _lstrip_runs(runs)
    if not runs:
        return
    last, nxt = plain(cur), plain(runs)
    if last.endswith(("-", "—")) and nxt[:1].isalnum():
        if ctx is not None:
            left = re.search(r"([\w./]+)[-—]$", last)
            right = re.match(r"([\w]+)", nxt)
            ctx.hyphen_joins[(left.group(1) if left else "") + (right.group(1) if right else "")] += 1
    else:
        cur.append([" ", False, 0])
    cur.extend(runs)


def paragraphs(rows, top, bottom=None, ctx=None):
    """Rows of one cell -> (paragraphs as run lists, leading blank line?, trailing blank line?).

    A whitespace-only row (the source's empty paragraph) or a vertical gap > PARA_GAP ends a paragraph.
    An empty line at the very top or bottom of a cell has no whitespace row of its own, so it is detected as a
    gap larger than BLANK_GAP between the cell border and the first/last text row (normal padding: 3-5 pt).
    These two flags decide whether a page-boundary fragment continues the previous paragraph or starts a new one."""
    paras, cur = [], None
    lead_blank = trail_blank = False
    prev_y1, seen = None, False
    for row in rows:
        if row["blank"]:
            if cur:
                paras.append(cur)
                cur = None
            if not seen:
                lead_blank = True
            trail_blank = True
            continue
        gap = row["y0"] - (prev_y1 if prev_y1 is not None else top)
        if not seen and gap > BLANK_GAP:
            lead_blank = True
        if cur is not None and gap > PARA_GAP:
            paras.append(cur)
            cur = None
        runs = row_runs(row)
        if cur is None:
            _lstrip_runs(runs)
            cur = runs
        else:
            join_line(cur, runs, ctx)
        seen, trail_blank, prev_y1 = True, False, row["y1"]
    if cur:
        paras.append(cur)
    if bottom is not None and prev_y1 is not None and bottom - prev_y1 > BLANK_GAP:
        trail_blank = True
    for p in paras:
        _rstrip_runs(p)
    return [p for p in paras if plain(p).strip()], lead_blank, trail_blank


def runs_md(runs, emphasis=False):
    """Paragraph runs -> Markdown text; italics rendered as *...* only when emphasis is requested (D7)."""
    merged = []
    for text, ital, _col in runs:
        flag = bool(ital) and emphasis
        if merged and (merged[-1][1] == flag or not text.strip()):
            merged[-1][0] += text
        elif merged and not merged[-1][0].strip():
            merged[-1][0] += text
            merged[-1][1] = flag
        else:
            merged.append([text, flag])
    out = ""
    for text, flag in merged:
        if flag and text.strip():
            lead = text[:len(text) - len(text.lstrip())]
            trail = text[len(text.rstrip()):]
            out += f"{lead}*{text.strip()}*{trail}"
        else:
            out += text
    return ws(out)


def redline_md(runs):
    """Runs of a Table 1 cell -> text with ~~deleted~~ (red) and <ins>inserted</ins> (blue #1f497c) words."""
    parts = []
    for text, _ital, col in runs:
        kind = "del" if col == RED else "ins" if col == BLUE else "plain"
        if not text.strip():
            kind = "ws"
        parts.append([kind, text])
    # whitespace between two runs of the same marked kind belongs to that run
    merged = []
    for i, (kind, text) in enumerate(parts):
        if kind == "ws":
            nxt = next((k for k, _t in parts[i + 1:] if k != "ws"), None)
            prv = merged[-1][0] if merged else None
            if prv in ("del", "ins") and nxt == prv:
                merged[-1][1] += text
                continue
            kind = "plain"
        if merged and merged[-1][0] == kind:
            merged[-1][1] += text
        else:
            merged.append([kind, text])
    out = ""
    for kind, text in merged:
        if kind in ("del", "ins") and text.strip():
            lead = text[:len(text) - len(text.lstrip())]
            trail = text[len(text.rstrip()):]
            core = " ".join(text.split())
            out += lead + (f"~~{core}~~" if kind == "del" else f"<ins>{core}</ins>") + trail
        else:
            out += text
    return ws(out)


def strip_redline(s):
    return ws(re.sub(r"~~|</?ins>", "", s))


def _tok(s):
    s = s.replace("-", "").replace("—", " ").replace("–", " ")
    return re.findall(r"[a-z0-9]+", s.lower())


def diff_tokens(a, b):
    """Word-level differences between two texts (hyphens and punctuation ignored)."""
    ta, tb = _tok(a), _tok(b)
    sm = difflib.SequenceMatcher(None, ta, tb, autojunk=False)
    return [f"{op}: [{' '.join(ta[i1:i2])}] vs [{' '.join(tb[j1:j2])}]"
            for op, i1, i2, j1, j2 in sm.get_opcodes() if op != "equal"]


def _odl_cell_text(cell):
    """All text of a JSON table cell, including paragraphs nested under list items."""
    parts = []

    def walk(node):
        if node.get("content"):
            parts.append(node["content"])
        for kid in node.get("kids", []) or []:
            walk(kid)
        for it in node.get("list items", []) or []:
            walk(it)

    for kid in cell.get("kids", []) or []:
        walk(kid)
    return ws(" ".join(parts))


# -------------------------------------------------------------------------------------- steps ----
def page_labels(doc, aux):
    """Printed page labels from the PDF footers (the JSON has no footer elements for this conversion).

    p1 (cover) is unnumbered and labelled 1; p105 prints 'Page B-2' (source error) and is labelled C-2."""
    lines = aux.meta.get("lines_by_page", {})
    pats = [re.compile(r"^Appendix [ABC] to RG 1\.232, Rev\. 0, Page ([A-C]-\d+)$"),
            re.compile(r"^RG 1\.232, Rev\. 0, Page (\d+)$")]
    for pno, lns in lines.items():
        for ln in lns:
            for pat in pats:
                m = pat.match(ln.text.strip())
                if m:
                    doc.page_labels[pno] = m.group(1)
    doc.page_labels.setdefault(1, "1")
    if doc.page_labels.get(105) == "B-2":
        doc.page_labels[105] = "C-2"
        doc.meta["page_label_fix"] = "p105 footer printed 'Page B-2' (source error); anchored as C-2"


def cover(doc, aux):
    """Page 1 masthead -> frontmatter; cover text box -> closing 'Document information' section."""
    info = doc.meta.setdefault("rg_cover", {})
    keep = []
    for e in doc.els:
        if e.page == 1 and e.kind == "image":
            continue
        if e.page == 1 and e.kind == "heading":
            t = ws(e.text)
            if t == "U.S. NUCLEAR REGULATORY COMMISSION":
                info["issuer"] = t
                continue
            if t.startswith("REGULATORY GUIDE 1.232"):
                info["masthead"] = t
                continue
            m = re.match(r"^Issue Date:\s*(\w+ \d{4})\s*Technical Lead:\s*(.+)$", t)
            if m:
                info["issue_date_text"], info["technical_lead"] = m.group(1), m.group(2).strip()
                continue
        if e.page == 1 and e.kind == "para" and e.size and e.size < 10 and \
                ws(e.text).startswith(("Written suggestions regarding this guide", "Electronic copies of this RG")):
            info.setdefault("box", []).append(ws(e.text))
            continue
        keep.append(e)
    if len(info.get("box", [])) != 2 or "technical_lead" not in info:
        _fail(f"cover not recognised: {info}")
    box = " ".join(info["box"])
    adams = dict(re.findall(r"(ADAMS Accession Number \(No\.\)|regulatory analysis|draft guide DG-1330|"
                            r"public comments on DG-1330)\D{0,60}?(ML\d{5}[A-Z]\d{3})", box))
    info["adams"] = {"main": adams.get("ADAMS Accession Number (No.)"),
                     "regulatory_analysis": adams.get("regulatory analysis"),
                     "draft_guide_DG-1330": adams.get("draft guide DG-1330"),
                     "public_comment_responses": adams.get("public comments on DG-1330")}
    doc.els = keep


def drop_toc_and_residue(doc, aux):
    S.drop_toc(doc, aux)
    # p105: footer of Appendix C page 2 printed 'Appendix B to RG 1.232, Rev. 0, Page B-2' (review F18)
    n0 = len(doc.els)
    doc.els = [e for e in doc.els
               if not re.fullmatch(r"Appendix [ABC] to RG 1\.232, Rev\. 0, Page [A-C]-\d+", ws(e.text))]
    if n0 - len(doc.els) != 1:
        _fail("page-footer residue on p105 not found exactly once")


def footnotes(doc, aux):
    """Footnote bodies out of the text stream; glued reference marks -> [^n] (explicit list only)."""
    bodies = {}
    keep = []
    for e in doc.els:
        m = re.match(r"^(\d{1,2})\s+(\S.*)$", ws(e.text)) if e.kind in ("item", "heading", "para") else None
        if m and e.size and e.size < 10 and FOOTNOTE_BODY_PAGES.get(int(m.group(1))) == e.page:
            bodies[int(m.group(1))] = (e.page, m.group(2))
            continue
        keep.append(e)
    if sorted(bodies) != list(range(1, 15)):
        _fail(f"footnote bodies found: {sorted(bodies)}")
    doc.els = keep
    for n, page, find, rep in FOOTNOTES:
        hits = [e for e in doc.els if e.page == page and find in e.text]
        if len(hits) != 1 or hits[0].text.count(find) != 1:
            _fail(f"footnote mark {n} ({find!r}) found {len(hits)} times on p{page}")
        hits[0].text = hits[0].text.replace(find, rep)
        hits[0].meta.setdefault("fn_marks", []).append(n)
    doc.meta["rg_footnotes"] = bodies


def _find_el(doc, page, pred, what):
    for i, e in enumerate(doc.els):
        if e.page == page and pred(e):
            return i
    _fail(f"anchor not found on p{page}: {what}")


def body_structure(doc, aux):
    """Order swaps, bullets/sub-bullets, split paragraphs, buried headings (review F10, F11, F14, F15, F24)."""
    els = doc.els
    # F11: the xycut reading order put the left-aligned subheading before its centred parent heading (2 pairs)
    for page, parent, child in ((1, "A. INTRODUCTION", "Purpose"), (5, "B. DISCUSSION", "Reason for Issuance")):
        i = _find_el(doc, page, lambda e: e.kind == "heading" and ws(e.text) == child, child)
        j = _find_el(doc, page, lambda e: e.kind == "heading" and ws(e.text) == parent, parent)
        if i + 1 != j:
            _fail(f"expected '{child}' directly before '{parent}'")
        els[i], els[j] = els[j], els[i]
    # F15: raw bullet glyphs: '•' -> list item, 'o' (second level, indented) -> nested item
    for e in els:
        if e.kind not in ("para", "item") or e.page > 28:
            continue
        t = e.text.lstrip()
        if re.match(r"^[•●]\s", t):
            e.kind, e.level, e.text = "item", 0, re.sub(r"^[•●]\s+", "", t)
        elif re.match(r"^o\s", t) and e.bbox and e.bbox[0] >= 100:
            e.kind, e.level, e.text = "item", 1, re.sub(r"^o\s+", "", t)
    # F14: generic page/column-break continuation (lower-case start); table elements break the chain
    doc.els = els
    S.join_breaks(doc)
    els = doc.els
    # F14/F04: explicit joins
    for page, end, start, sep in JOINS:
        i = next((k for k, e in enumerate(els) if e.page == page and e.kind in ("para", "item")
                  and ws(e.text).endswith(end)), None)
        if i is None or i + 1 >= len(els) or not ws(els[i + 1].text).startswith(start):
            _fail(f"join anchor not found: p{page} …{end!r} + {start!r}")
        els[i].text = ws(els[i].text) + sep + ws(els[i + 1].text)
        del els[i + 1]
    # F10: 'Background The NRC Regulatory Framework' (two bold heading lines read as one paragraph)
    i = next((k for k, e in enumerate(els) if e.page == 5 and ws(e.text) == "Background The NRC Regulatory Framework"),
             None)
    if i is None:
        _fail("'Background The NRC Regulatory Framework' not found")
    e = els[i]
    els[i:i + 1] = [El("heading", "Background", 5, e.bbox, e.font, e.size, id=e.id),
                    El("heading", "The NRC Regulatory Framework", 5, e.bbox, e.font, e.size, id=e.id)]
    # F10: headings buried in running text
    for page, frag, head in BURIED:
        i = next((k for k, e in enumerate(els) if e.page == page and frag in ws(e.text)), None)
        if i is None:
            _fail(f"buried heading not found: {head}")
        e = els[i]
        t = ws(e.text)
        pos = t.index(head, t.index(frag))
        before, after = t[:pos].strip(), t[pos + len(head):].strip()
        new = []
        if before:
            new.append(El("para", before, e.page, e.bbox, e.font, e.size, id=e.id))
        new.append(El("heading", head, e.page, e.bbox, e.font, e.size, id=e.id))
        if after:
            new.append(El("para", after, e.page, e.bbox, e.font, e.size, id=e.id))
        els[i:i + 1] = new
    # F24: Appendix B column list printed as three lines but read as one paragraph
    i = next((k for k, e in enumerate(els) if e.page == 62 and ws(e.text).startswith("Column 1—Criterion Number Column 2")),
             None)
    if i is None:
        _fail("Appendix B column list not found")
    e = els[i]
    parts = re.split(r"\s(?=Column \d—)", ws(e.text))
    els[i:i + 1] = [El("item", p, e.page, e.bbox, e.font, e.size, 0, "arabic numbers", id=e.id) for p in parts]
    # remaining items: list depth 0 unless set above
    for e in els:
        if e.kind == "item" and e.level not in (0, 1):
            e.level = 0
    doc.els = els


def headings(doc, aux):
    """Assign the section 4 outline; every non-outline converter heading is demoted to a paragraph."""
    wanted = {(p, t): lvl for p, t, lvl in HEADINGS}
    for e in doc.els:
        if e.kind != "heading" or e.meta.get("rg_level"):
            continue
        t = ws(e.text)
        t = APPENDIX_HEADING_SRC.get(t, t)
        if (e.page, t) in wanted:
            e.text, e.level = t, wanted[(e.page, t)]
            e.meta["rg_level"] = True
        else:
            e.kind, e.level = "para", 0
            doc.meta.setdefault("rg_demoted", []).append(f"p{e.page} {t[:60]}")
    got = [(e.page, e.text) for e in doc.els if e.kind == "heading" and e.meta.get("rg_level")]
    exp = [(p, t) for p, t, _ in HEADINGS]
    if got != exp:
        missing = [x for x in exp if x not in got]
        extra = [x for x in got if x not in exp]
        doc.meta.setdefault("unmatched_headings", []).extend(f"{t} (p{p})" for p, t in missing)
        if missing or extra:
            _fail(f"outline mismatch; missing={missing} extra={extra}")
        _fail("outline order differs from section 4")


def normalise(doc, aux):
    """Entities, whitespace, the explicit hyphen list, Obsidian escapes -- converter text only."""
    for e in doc.els:
        if e.meta.get("final"):
            continue
        if e.kind in ("para", "item", "heading", "caption"):
            e.text = text_pipeline(e.text)


def _replace_els(doc, olds, new):
    """Replace the elements `olds` (by identity) with `new`, inserted where the first of them was."""
    ids = {id(x) for x in olds}
    first = next(k for k, e in enumerate(doc.els) if id(e) in ids)
    before = sum(1 for e in doc.els[:first] if id(e) not in ids)
    doc.els = [e for e in doc.els if id(e) not in ids]
    doc.els[before:before] = new


# -------------------------------------------------------------------------------------- Table 1 ----
def _table_els(doc, p0, p1):
    return [e for e in doc.els if e.kind == "table" and p0 <= e.page <= p1]


def _raw_md_strikes(doc):
    """{(criterion, col): [struck words]} from the raw md Table 1 rows (converter detect_strikethrough)."""
    path = os.path.join(doc.raw_dir, doc.stem + ".md")
    out = {}
    if not os.path.exists(path):
        return out
    with open(path, encoding="utf-8") as f:
        for line in f:
            if "IMPLEMENTATION" in line and line.startswith("#"):
                break
            m = re.match(r"^\|(\d{1,2})\|(.*)\|\s*$", line.strip())
            if not m:
                continue
            cells = m.group(2).split("|")
            for col, c in enumerate(cells[1:4], start=2):
                words = " ".join(re.findall(r"~~(.+?)~~", c)).split()
                if words:
                    out[(m.group(1), col)] = words
    return out


def crosswalk(doc, aux):
    """Table 1 (10 page tables, p13-20) -> one Markdown table with the redline kept (D7)."""
    ctx = _ctx(doc)
    tabs = _table_els(doc, *TABLE1_PAGES)
    if len(tabs) != 10:
        _fail(f"Table 1: expected 10 page tables, found {len(tabs)}")
    strikes = _raw_md_strikes(doc)
    hdr_of = {1: "GDC", 2: "ARDC", 3: "SFR-DC", 4: "MHTGR-DC"}
    rows, diffs, redline_cells = [], [], 0
    for te in tabs:
        node = ctx.tables[te.id]
        section = None
        for r in node["rows"]:
            cells = sorted(r["cells"], key=lambda c: c["column number"])
            texts = [_odl_cell_text(c) for c in cells]
            if len(cells) == 1 or cells[0].get("column span", 1) >= 5:
                section = ws(texts[0])
                continue
            if texts[0] == "Criterion":
                continue
            crit = texts[0]
            if not re.fullmatch(r"\d{1,2}", crit):
                _fail(f"Table 1 p{te.page}: unexpected row {texts[:2]}")
            if len(cells) != 5:
                _fail(f"Table 1 p{te.page}: row {crit} has {len(cells)} cells")
            vals = []
            for k, c in enumerate(cells[1:5], start=1):
                _rect, crows = cell_rows(ctx, te.page, c["bounding box"])
                runs = []
                for row in crows:
                    if row["blank"]:
                        continue
                    rr = row_runs(row)
                    if runs:
                        join_line(runs, rr)
                    else:
                        _lstrip_runs(rr)
                        runs = rr
                md = redline_md(runs) if k > 1 else ws(plain(runs))
                d = diff_tokens(strip_redline(md), texts[k])
                if d:
                    diffs.append(f"Table 1 row {crit} col {k + 1}: {d}")
                vals.append(md)
            gdc = vals[0]
            row = [section, crit, gdc]
            for k, md in enumerate(vals[1:], start=2):
                if "~~" in md or "<ins>" in md:
                    redline_cells += 1
                deleted = " ".join(re.findall(r"~~(.+?)~~", md)).split()
                if deleted != strikes.get((crit, k), []):      # raw md col 2 = ARDC ... col 4 = MHTGR-DC
                    diffs.append(f"Table 1 row {crit} {hdr_of[k]}: red {deleted} vs raw md ~~ {strikes.get((crit, k))}")
                p = strip_redline(md)
                if p in XW_WHOLE_STATUS:
                    row += ["", p]
                    continue
                m = XW_STATUS_RE.search(p)
                if m and md.endswith(m.group(1)):
                    row += [md[:-len(m.group(1))].strip(), m.group(1)]
                else:
                    row += [md, ""]
            rows.append((te.page, row))
    if len(rows) != 65:
        _fail(f"Table 1: expected 65 rows, found {len(rows)}")
    ctx.warnings += diffs
    ctx.stats["table1_rows"] = len(rows)
    ctx.stats["table1_redline_cells"] = redline_cells
    ctx.stats["table1_rows_by_crit"] = {r[1]: r for _p, r in rows}
    hdr = ["Section", "Criterion", "GDC title", "ARDC title", "ARDC status", "SFR-DC title", "SFR-DC status",
           "MHTGR-DC title", "MHTGR-DC status"]
    lines = ["| " + " | ".join(hdr) + " |", "|" + "---|" * len(hdr)]
    for _p, row in rows:
        lines.append("| " + " | ".join(N.obsidian_escape(x).replace("|", "\\|") for x in row) + " |")
    _replace_els(doc, tabs, [El("heading", TABLE1_CAPTION, tabs[0].page, level=4, meta={"rg_level": True, "final": True}),
                             El("raw_md", "\n".join(lines), tabs[0].page, meta={"final": True, "table1": True})])


# ---------------------------------------------------------------------------- Appendices A-C ----
def _sentence_case(h):
    words = h.split()
    return " ".join([words[0]] + [w if (w.isupper() and len(w) > 1) else w.lower() for w in words[1:]])


def _cell_frag(ctx, pno, cell, emphasis=False, want_title=False):
    rect, crows = cell_rows(ctx, pno, cell["bounding box"])
    paras, lead, trail = paragraphs(crows, rect.y0, rect.y1, ctx)
    title = None
    if want_title and paras:
        runs = paras[0]
        k = 0
        while k < len(runs) and (runs[k][1] or not runs[k][0].strip()):
            k += 1
        title = ws(plain(runs[:k]))
    return {"page": pno, "paras": paras, "lead": lead, "trail": trail, "title": title, "emphasis": emphasis,
            "odl": _odl_cell_text(cell)}


LIST_START = re.compile(r"^\(\d{1,2}\)\s|^\([a-z]\)\s")


def merge_fragments(frags, render):
    """Join the per-page fragments of one cell column into paragraphs [(page, text)].

    A page-boundary piece starts a new paragraph when the previous piece ends a sentence AND the source has an
    empty line at the end of the previous piece or at the start of the next one, or when the next piece starts a
    numbered list entry; otherwise it continues the paragraph (one space; no space after a line-end hyphen).
    The sentence-end condition is required because a cell may end well above its bottom border when the row height
    is set by the other column, which is not an empty source line."""
    out, prev_trail = [], False
    for f in frags:
        texts = [render(p, f["emphasis"]) for p in f["paras"]]
        texts = [t for t in texts if t]
        if not texts:
            continue          # an empty continuation cell carries no boundary information
        first, rest = texts[0], texts[1:]
        blank = (prev_trail or f["lead"]) and out and out[-1][1].rstrip().endswith(TERMINAL)
        if out and not (blank or LIST_START.match(first)):
            pg, last = out[-1]
            out[-1] = (pg, last + ("" if last.endswith(("-", "—")) and first[:1].isalnum() else " ") + first)
            f["joined"] = "mid" if not last.endswith(TERMINAL) else "sentence"
            f["join_ctx"] = (last[-45:], first[:45])
        else:
            if out:
                f["joined"] = "para"
                f["join_ctx"] = (out[-1][1][-45:], first[:45])
            out.append((f["page"], first))
        out += [(f["page"], t) for t in rest]
        prev_trail = f["trail"]
    return out


def _label(doc, p):
    return doc.page_labels.get(p, str(p))


def appendix_records(doc, aux):
    """Appendix A-C criterion tables (123 page tables) -> D6 criterion records."""
    ctx = _ctx(doc)
    xw = ctx.stats.get("table1_rows_by_crit", {})
    total = 0
    boundary_log = collections.Counter()
    for letter, cset, p0, p1, alias in APPENDICES:
        tabs = _table_els(doc, p0, p1)
        crits, order = {}, []
        rat_header = collections.Counter()
        cur = None
        for te in tabs:
            node = ctx.tables[te.id]
            section = None
            for r in node["rows"]:
                cells = sorted(r["cells"], key=lambda c: c["column number"])
                texts = [_odl_cell_text(c) for c in cells]
                if len(cells) == 1 or cells[0].get("column span", 1) >= 3:
                    section = ws(texts[0])
                    continue
                if texts[0] == "Criterion":
                    rat_header[ws(texts[2])] += 1
                    continue
                if len(cells) != 3:
                    _fail(f"Appendix {letter} p{te.page}: row with {len(cells)} cells")
                num = texts[0]
                if num:
                    if not re.fullmatch(r"\d{1,2}", num) or num in crits:
                        _fail(f"Appendix {letter} p{te.page}: bad criterion number {num!r}")
                    cur = {"num": num, "section": section, "sec_page": te.page, "text": [], "rat": []}
                    crits[num] = cur
                    order.append(num)
                    cur["text"].append(_cell_frag(ctx, te.page, cells[1], want_title=True))
                else:
                    if cur is None:
                        _fail(f"Appendix {letter} p{te.page}: continuation row before the first criterion")
                    cur["text"].append(_cell_frag(ctx, te.page, cells[1]))
                cur["rat"].append(_cell_frag(ctx, te.page, cells[2], emphasis=cur["num"] in EMPHASIS_CRITERIA))
        ids = [int(n) for n in order]
        if ids != EXPECTED_IDS[cset]:
            _fail(f"Appendix {letter}: criterion ids {ids}")
        rat_name = _sentence_case(rat_header.most_common(1)[0][0])
        # build elements
        new, sec_done = [], None
        for num in order:
            c = crits[num]
            if c["section"] != sec_done:
                sec_done = c["section"]
                new.append(El("heading", f"Appendix {letter} — Section {c['section']}", c["sec_page"], level=3,
                              meta={"rg_level": True, "final": True}))
            new += _record(doc, ctx, letter, cset, alias, c, rat_name, xw)
            for col, frs in (("text", c["text"][1:]), ("rationale", c["rat"][1:])):
                for f in frs:
                    if f.get("joined"):
                        boundary_log[f["joined"]] += 1
                        ctx.stats.setdefault("join_detail", []).append(
                            f"{f['joined']:8s} {cset} {c['num']} {col} p{f['page']}: …{f['join_ctx'][0]} ‖ {f['join_ctx'][1]}…")
        total += len(order)
        ctx.stats[f"appendix_{letter}"] = len(order)
        _replace_els(doc, tabs, new)
    ctx.stats["criteria"] = total
    ctx.stats["continuation_joins"] = dict(boundary_log)


def _record(doc, ctx, letter, cset, alias, c, rat_name, xw):
    num = c["num"]
    f0 = c["text"][0]
    if not f0["paras"]:
        _fail(f"{cset} {num}: empty title cell")
    full0 = ws(plain(f0["paras"][0]))
    title = f0["title"] or ""
    if not title or not full0.startswith(title):
        _fail(f"{cset} {num}: italic title not found ({title!r})")
    mt = STATUS_TAIL_RE.search(title)          # SFR-DC 18: the status line is italic too
    if mt:
        title = title[:mt.start()].strip()
    rest = full0[len(title):].strip()
    ms = STATUS_RE.match(rest)
    status_line = ms.group(0) if ms else ""
    body0 = rest[ms.end():].strip() if ms else rest
    # criterion text: first paragraph without title/status + remaining paragraphs + continuation pages
    f0_rest = dict(f0)
    f0_rest["paras"] = ([[[body0, False, 0]]] if body0 else []) + f0["paras"][1:]
    text_paras = merge_fragments([f0_rest] + c["text"][1:], lambda p, emph: ws(plain(p)))
    rat_paras = merge_fragments(c["rat"], runs_md)
    # status: appendix status line, else Table 1 (review section 5.1)
    col = {"ARDC": 4, "SFR-DC": 6, "MHTGR-DC": 8}[cset]
    xrow = xw.get(num)
    xstatus = xrow[col] if xrow else ""
    if status_line:
        status = status_line
        if xstatus and xstatus.rstrip(".") != status_line.rstrip("."):
            ctx.warnings.append(f"{cset} {num}: appendix status {status_line!r} vs Table 1 {xstatus!r}")
    elif xstatus:
        status = f"{xstatus} (source: Table 1)"
    elif c["section"].startswith("VII."):
        status = f"{c['section'].split('.', 1)[1].strip()} (source: Appendix {letter}, Section VII)"
    else:
        status = "(none in source)"
        ctx.warnings.append(f"{cset} {num}: no status in appendix or Table 1")
    # cross-check with the converter's cell text (before the status line may stand in for an empty text)
    pdf_all = " ".join([title, status_line] + [t for _p, t in text_paras] + [t for _p, t in rat_paras])
    odl_all = " ".join(f["odl"] for f in c["text"]) + " " + " ".join(f["odl"] for f in c["rat"])
    d = diff_tokens(pdf_all.replace("*", ""), odl_all)
    if d:
        ctx.warnings.append(f"{cset} {num} PDF vs JSON: {d}")
    if not text_paras and status_line:
        text_paras = [(f0["page"], status_line)]    # 'Not applicable to MHTGR.' is the whole Column 2 content
    if not text_paras:
        _fail(f"{cset} {num}: empty criterion text")
    pages = sorted({f["page"] for f in c["text"] + c["rat"]})
    src = (f"RG 1.232 Rev. 0, Appendix {letter}, p. {_label(doc, pages[0])} (PDF p. {pages[0]})" if len(pages) == 1
           else f"RG 1.232 Rev. 0, Appendix {letter}, pp. {_label(doc, pages[0])}–{_label(doc, pages[-1])} "
                f"(PDF pp. {pages[0]}–{pages[-1]})")
    gdc = f"GDC {num} — {xrow[2]}" if xrow and xrow[2] != "N/A" else "N/A (Table 1)"
    fields = [f"- **ID:** {cset} {num} ^{cset.lower()}-{num}"]
    if alias:
        fields.append(f"- **Aliases:** {alias} {num}")
    fields += [f"- **GDC counterpart (Table 1):** {gdc}",
               f"- **Title:** {title}",
               f"- **Status:** {status}",
               f"- **Source:** {src}"]
    p = f0["page"]
    out = [El("heading", f"{cset} {num} — {title.rstrip('.')}", p, level=4,
              meta={"rg_level": True, "final": True, "criterion": f"{cset} {num}"}),
           El("raw_md", "\n".join(N.obsidian_escape(x) for x in fields), p, meta={"final": True}),
           El("heading", "Criterion text", p, level=5, meta={"rg_level": True, "final": True})]
    out += [El("para", md_safe(N.obsidian_escape(t)), pg, meta={"final": True, "crit_text": f"{cset} {num}"})
            for pg, t in text_paras]
    rp = rat_paras[0][0] if rat_paras else p
    out.append(El("heading", rat_name, rp, level=5, meta={"rg_level": True, "final": True}))
    if rat_paras:
        out += [El("para", md_safe(N.obsidian_escape(t)), pg, meta={"final": True}) for pg, t in rat_paras]
    else:
        out.append(El("para", "(none in source)", rp, meta={"final": True}))
    return out


# ---------------------------------------------------------------------- acronyms / references ----
def acronyms(doc, aux):
    """ACRONYMS/ABBREVIATIONS (p23-24, tab-aligned: acronym x=72, expansion x=144) -> two-column table."""
    ctx = _ctx(doc)
    entries = []
    for pno in (23, 24):
        rows = collections.defaultdict(list)
        for s in ctx.spans(pno):
            t = s.text.strip()
            if not t or t == "ACRONYMS/ABBREVIATIONS" or t.startswith("RG 1.232, Rev. 0, Page") or s.rect.y1 > 740:
                continue
            rows[round((s.rect.y0 + s.rect.y1) / 2)].append(s)
        for y in sorted(rows):
            sps = sorted(rows[y], key=lambda s: s.rect.x0)
            acr = ws(" ".join(s.text for s in sps if s.rect.x0 < 130))
            exp = ws(" ".join(s.text for s in sps if s.rect.x0 >= 130))
            if acr:
                entries.append([acr, exp, pno])
            elif exp and entries:
                entries[-1][1] = ws(entries[-1][1] + " " + exp)
    if len(entries) != 42:
        _fail(f"acronyms: expected 42, found {len(entries)}")
    odl = " ".join(e.text for e in doc.els if e.page in (23, 24) and e.kind in ("para", "heading")
                   and ws(e.text) != "ACRONYMS/ABBREVIATIONS")
    d = diff_tokens(" ".join(a + " " + b for a, b, _p in entries), odl)
    if d:
        ctx.warnings.append(f"acronyms PDF vs JSON: {d}")
    lines = ["| Acronym | Definition |", "|---|---|"] + [f"| {a} | {N.obsidian_escape(b)} |" for a, b, _p in entries]
    i = next(k for k, e in enumerate(doc.els) if e.kind == "heading" and ws(e.text) == "ACRONYMS/ABBREVIATIONS")
    j = next(k for k, e in enumerate(doc.els) if k > i and e.kind == "heading")
    if any(e.page not in (23, 24) for e in doc.els[i + 1:j]):
        _fail("acronyms: unexpected elements between ACRONYMS/ABBREVIATIONS and REFERENCES")
    doc.els[i + 1:j] = [El("raw_md", "\n".join(lines), 23, meta={"final": True})]
    ctx.stats["acronyms"] = len(entries)


def references(doc, aux):
    """REFERENCES: the 39 numbered entries -> ordered list with ^ref-n block ids, one raw_md block per page."""
    ctx = _ctx(doc)
    i = next(k for k, e in enumerate(doc.els) if e.kind == "heading" and e.text.startswith("REFERENCES"))
    j = next(k for k, e in enumerate(doc.els) if k > i and e.kind == "heading")
    entries = []
    for e in doc.els[i + 1:j]:
        m = re.match(r"^(\d{1,2})\.\s+(\S.*)$", ws(e.text))
        if not m:
            _fail(f"references: unexpected element {e.text[:60]!r}")
        entries.append((int(m.group(1)), m.group(2), e.page))
    if [n for n, _t, _p in entries] != list(range(1, 40)):
        _fail(f"references: numbering {[n for n, _t, _p in entries]}")
    blocks = []
    for n, t, p in entries:
        line = f"{n}. {t} ^ref-{n}"
        if blocks and blocks[-1][0] == p:
            blocks[-1][1].append(line)
        else:
            blocks.append((p, [line]))
    doc.els[i + 1:j] = [El("raw_md", "\n".join(ls), p, meta={"final": True}) for p, ls in blocks]
    ctx.stats["references"] = len(entries)


# -------------------------------------------------------------------------------- footnote defs ----
def place_footnotes(doc, aux):
    """[^n]: definitions at the end of the section that contains the mark (before the next heading)."""
    bodies = doc.meta["rg_footnotes"]
    marks = {}
    for k, e in enumerate(doc.els):
        for n in re.findall(r"\[\^(\d{1,2})\]", e.text if e.kind != "table" else ""):
            marks.setdefault(int(n), k)
    if sorted(marks) != list(range(1, 15)):
        _fail(f"footnote marks in output: {sorted(marks)}")
    inserts = collections.defaultdict(list)
    for n, k in marks.items():
        j = k + 1
        while j < len(doc.els) and doc.els[j].kind != "heading":
            j += 1
        inserts[j].append(n)
    for j in sorted(inserts, reverse=True):
        new = []
        for n in sorted(inserts[j]):
            page, body = bodies[n]
            new.append(El("raw_md", f"[^{n}]: {text_pipeline(body)}", page, meta={"final": True, "footnote": n}))
        doc.els[j:j] = new


def document_information(doc, aux):
    """Cover text box (p1), verbatim, as the closing section (review section 5.2 rule 2)."""
    box = doc.meta["rg_cover"]["box"]
    doc.els.append(El("heading", "Document information", 1, level=2, meta={"rg_level": True, "final": True}))
    doc.els += [El("para", md_safe(text_pipeline(t)), 1, meta={"final": True}) for t in box]


def finish(doc, aux):
    """Sanity checks, a warnings summary for the report, close the PDF."""
    ctx = _ctx(doc)
    for e in doc.els:
        if e.kind == "heading" and not (1 <= e.level <= 6):
            _fail(f"heading without level: {e.text[:60]}")
        if e.kind in ("table", "image", "hdr"):
            _fail(f"unconverted element left: {e.kind} p{e.page}")
        if e.kind == "para" and not e.meta.get("final"):
            e.text = md_safe(e.text)
    odd = {k: v for k, v in ctx.hyphen_joins.items()
           if not any(k.startswith(j) or j.startswith(k) for j in HYPHEN_JOINED)}
    doc.meta["rg_stats"] = dict(ctx.stats, hyphen_joins_pdf=dict(ctx.hyphen_joins), hyphen_joins_unlisted=odd,
                                warnings=list(ctx.warnings))
    doc.meta["rg_stats"].pop("table1_rows_by_crit", None)
    # the cross-checks are only worth running if a failure is visible: the build report prints every `*_warnings`
    # list and every `*_qa` dict, and tests/test_rg1232.py asserts that rg_warnings is empty.
    doc.meta["rg_warnings"] = list(ctx.warnings) + [f"hyphen join not in the reviewed list: {k} -> {v}"
                                                   for k, v in sorted(odd.items())]
    st = ctx.stats
    doc.meta["rg_qa"] = {"criteria": st.get("criteria", 0), "appendix_A": st.get("appendix_A", 0),
                         "appendix_B": st.get("appendix_B", 0), "appendix_C": st.get("appendix_C", 0),
                         "table1_rows": st.get("table1_rows", 0), "table1_redline_cells": st.get("table1_redline_cells", 0),
                         "acronyms": st.get("acronyms", 0), "references": st.get("references", 0),
                         "pdf_vs_json_diffs": len(ctx.warnings), "hyphen_joins_unlisted": len(odd)}
    ctx.close()
    doc.meta.pop("_rg", None)


def steps():
    return [
        page_labels,
        cover,
        drop_toc_and_residue,
        footnotes,
        body_structure,
        headings,
        normalise,
        crosswalk,
        appendix_records,
        acronyms,
        references,
        place_footnotes,
        document_information,
        finish,
    ]


def metadata(doc, aux):
    info = doc.meta.get("rg_cover", {})
    adams = info.get("adams", {})
    stats = doc.meta.get("rg_stats", {})
    return {
        "doc_id": "RG 1.232",
        "title": "Guidance for Developing Principal Design Criteria for Non-Light-Water Reactors",
        "doc_type": "Regulatory Guide",
        "issuer": "U.S. Nuclear Regulatory Commission",
        "revision": "0",
        "date": "2018-04",
        "issue_date": "2018-04",
        "technical_lead": info.get("technical_lead", "Jan Mazza"),
        "adams_accession": adams.get("main"),
        "related_adams": {k: v for k, v in adams.items() if k != "main" and v},
        "source_pdf": f"references/raw/{doc.stem}.pdf",
        "raw_json": f"references/raw/{doc.stem}.json",
        "raw_md": f"references/raw/{doc.stem}.md",
        "pdf_pages": doc.n_pages,
        "page_label_notes": ("PDF p1-28 = body pages 1-27 (p1 unnumbered; p20 and p21 both printed 20); "
                             "p29-61 = A-1..A-33; p62-103 = B-1..B-42; p104-133 = C-1..C-30 "
                             "(p105 printed B-2, anchored as C-2)"),
        "criteria_sets": {"ARDC": stats.get("appendix_A", 0), "SFR-DC": stats.get("appendix_B", 0),
                          "MHTGR-DC": stats.get("appendix_C", 0), "crosswalk_rows": stats.get("table1_rows", 0)},
        "tables": ["Table 1: Non-Light-Water-Reactor Crosswalk",
                   "Acronyms/Abbreviations",
                   "Appendix A table: ARDC (criterion records)",
                   "Appendix B table: SFR-DC (criterion records)",
                   "Appendix C table: MHTGR-DC (criterion records)"],
        "figures": [],
        "tags": ["reference", "nrc", "regulatory-guide", "design-criteria", "non-lwr"],
        "aliases": ["RG 1.232", "Regulatory Guide 1.232", "RG 1.232 Rev. 0"],
    }
