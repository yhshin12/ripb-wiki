"""PSAR Chapter 1 hooks: unit tests on synthetic elements + one smoke run on the real document (no PNG rendering,
nothing written to references/)."""
import importlib
import os
import re
import sys

import fitz
import pytest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from refclean import tables as T  # noqa: E402
from refclean.doc import Doc, El  # noqa: E402
from refclean.pdfaux import Aux, FigureRef, Line  # noqa: E402
from refclean.profiles import psar_ch01 as C  # noqa: E402

VAULT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
RAW = os.path.join(VAULT, "references", "raw")
STEM = "TP_Natrium_PSAR2025_ch1_General Plant and Site Description"


def _doc(els, labels=None):
    return Doc("PSAR_ch01", STEM, RAW, os.path.join(VAULT, "references"), 115, labels or {}, els)


def _table(rows, page, caption="", bold_header=True):
    grid = [[T.Cell(t, i, j, bold=(i == 0 and bold_header)) for j, t in enumerate(r)] for i, r in enumerate(rows)]
    return El("table", "", page, table=T.Table(grid=grid, header_rows=1, page=page, pages=[page], caption=caption))


def _line(text, x0, y0, size=4.4, font="ArialMT", spans=None):
    h = size
    rect = fitz.Rect(x0, y0, x0 + 5 * len(text), y0 + h)
    return Line(text, rect.x0, rect.y0, rect.x1, rect.y1, size, (font,), 0,
                spans or [(text, rect, size, font, 0, 0)])


# ------------------------------------------------------------------ unit ----
def test_split_paragraphs():
    doc = _doc([El("para", "A “Facilities.” This preliminary safety analysis report (PSAR) includes x.", 19)])
    C.split_paragraphs(doc, splits=[(19, "“Facilities.”", "This preliminary safety")])
    assert [e.text for e in doc.els] == ["A “Facilities.”", "This preliminary safety analysis report (PSAR) includes x."]
    assert not doc.meta.get("psar_ch01_qa")


def test_join_page_breaks_only_function_word_page_cuts():
    doc = _doc([El("para", "functions through the manipulation of the", 26),
                El("para", "CRD. During shutdown and refueling.", 27),
                El("para", "Figure 1.1-1 provides an overview of the", 27),
                El("para", "Same page fragment.", 27),
                El("para", "Ends a sentence.", 27),
                El("para", "New paragraph on the next page.", 28)])
    C.join_page_breaks(doc)
    assert [e.text for e in doc.els] == [
        "functions through the manipulation of the CRD. During shutdown and refueling.",
        "Figure 1.1-1 provides an overview of the", "Same page fragment.", "Ends a sentence.",
        "New paragraph on the next page."]


def test_nest_dash_items():
    doc = _doc([El("item", "The intent … refers to one of the following:", 66, level=0),
                El("item", "- a different type of reactor design", 66, level=0),
                El("item", "- an SSC that is not part of the design", 66, level=0),
                El("para", "RGs that have been designated …", 66)])
    C.nest_dash_items(doc)
    assert [(e.text, e.level) for e in doc.els[:3]] == [
        ("The intent … refers to one of the following:", 0),
        ("a different type of reactor design", 1), ("an SSC that is not part of the design", 1)]


def test_bold_status_terms_follow_pdf_bold_spans():
    aux = Aux()
    r = fitz.Rect(72, 100, 170, 112)
    aux.meta["lines_by_page"] = {
        67: [Line("Partial Compliance - The regulation …", 72, 100, 500, 112, 11.0, ("Arial,Bold", "Arial"), 0,
                  [("Partial Compliance ", r, 11.0, "Arial,Bold", 16, 0), ("- The regulation …", r, 11.0, "Arial", 0, 0)]),
             Line("Not Applicable. Only applies to PWRs.", 72, 130, 500, 142, 11.0, ("Arial",), 1,
                  [("Not Applicable. Only applies to PWRs.", r, 11.0, "Arial", 0, 0)])]}
    doc = _doc([El("para", "Partial Compliance - The regulation is relevant.", 67),
                El("para", "Not Applicable – regular font on this page.", 67),
                El("para", "Partial Compliance - on another page.", 68)])
    C.bold_status_terms(doc, aux)
    assert [e.text for e in doc.els] == ["**Partial Compliance** - The regulation is relevant.",
                                         "Not Applicable – regular font on this page.",
                                         "Partial Compliance - on another page."]


T141_HDR = ["Guide Number", "Title", "Revision", "Conformance Status"]


def _t141(page=69):
    return _table([T141_HDR,
                   ["1.8", "Qualification", "4", "The guidance is not applicable to the design and construction "
                                                 "phase of the project and will be addressed at the OL stage."],
                   ["1.13", "Spent Fuel", "2", "Partial Conformance General exceptions:\n1.Although x.\nC.2 - y"],
                   ["1.28", "QA", "5", "Full Conformance RG 1.28 Revision 6 is the most recent."],
                   ["1.30", "QA install", "0", "Full Conformance"]],
                  page, caption="Table 1.4-1 Conformance with Regulatory Guides")


def test_table_141_status_split():
    doc = _doc([_t141()])
    C.table_141(doc)
    t = doc.els[0].table
    assert T.header_names(t) == T141_HDR + ["Comments"]
    body = [[c.text for c in row] for row in t.grid[1:]]
    assert body[0][3].startswith("The guidance is not applicable") and body[0][4] == ""
    assert body[1][3:] == ["Partial Conformance", "General exceptions:\n1.Although x.\nC.2 - y"]
    assert body[2][3:] == ["Full Conformance", "RG 1.28 Revision 6 is the most recent."]
    assert body[3][3:] == ["Full Conformance", ""]
    assert not doc.meta.get("psar_ch01_qa")


def test_table_141_unmerged_sheets_are_reported_not_half_split():
    """If the core merge regresses, the hook must not split one sheet and leave the rest 4-column."""
    doc = _doc([_t141(69), _t141(70)])
    C.table_141(doc)
    assert [len(e.table.grid[0]) for e in doc.els] == [4, 4]
    assert doc.meta["psar_ch01_qa"] == [
        "Table 1.4-1: 2 tables with header %r (core merge)" % T141_HDR]


def test_parse_legend_wrapped_entry_and_gap():
    lines = [_line("FACILITY NUMBER/DESCRIPTION:", 886.7, 139.8),
             _line("11 REACTOR BUILDING", 886.5, 149.4),
             _line("32A MEDIUM VOLTAGE HOUSING", 886.8, 154.7),
             _line("84 STEAM GENERATOR BUILDING/TURBINE FACILITY", 886.8, 159.9),
             _line("BUILDING (STEAM) RACK", 887.0, 165.2),
             _line("85 AUXILIARY BOILER", 886.8, 170.5),
             _line("X", 739.2, 175.0, size=1.9),
             _line("75", 886.8, 210.0)]            # far below: not part of the legend
    assert C.parse_legend(lines) == [("11", "REACTOR BUILDING"), ("32A", "MEDIUM VOLTAGE HOUSING"),
                                     ("84", "STEAM GENERATOR BUILDING/TURBINE FACILITY BUILDING (STEAM) RACK"),
                                     ("85", "AUXILIARY BOILER")]


def _acronym_aux():
    aux = Aux()
    aux.meta["body_size"] = 11.0
    aux.meta["lines_by_page"] = {17: [Line("VS30 Time-averaged", 73, 692.9, 449, 707.2, 11.0, ("Arial",), 0, [
        ("V", fitz.Rect(73, 692.9, 80.3, 705.2), 11.0, "Arial", 0, 0),
        ("S30", fitz.Rect(80.3, 698.6, 94.0, 707.2), 7.7, "Arial", 0, 0),
        ("Time-averaged", fitz.Rect(163, 692.9, 449, 705.2), 11.0, "Arial", 0, 0)])]}
    return aux


def _acronym_table(page=16, pages=(16, 17)):
    el = _table([["Term", "Description"], ["SSC", "structure, system, or component"],
                 ["VS30", "Time-averaged shear-wave velocity"]], page)
    el.table.pages = list(pages)
    return el


def test_acronym_list_heading_and_subscripts():
    doc = _doc([El("hdr", "LIST OF ACRONYMS AND ABBREVIATIONS", 16), _acronym_table()])
    C.acronym_list(doc, _acronym_aux())
    assert [e.kind for e in doc.els] == ["heading", "table"]
    assert doc.els[0].level == 2 and doc.els[0].text == "LIST OF ACRONYMS AND ABBREVIATIONS"
    assert [r[0].text for r in doc.els[1].table.grid[1:]] == ["SSC", "V<sub>S30</sub>"]
    assert not doc.meta.get("psar_ch01_qa")


def test_acronym_list_reports_a_failed_core_merge():
    doc = _doc([El("hdr", "LIST OF ACRONYMS AND ABBREVIATIONS", 16), _acronym_table(16, (16,)),
                El("hdr", "LIST OF ACRONYMS AND ABBREVIATIONS", 17), _acronym_table(17, (17,))])
    C.acronym_list(doc, _acronym_aux())
    assert [e.kind for e in doc.els] == ["heading", "table", "table"]       # extra running title still removed
    assert doc.meta["psar_ch01_qa"] == ["acronym list: 2 running titles (core dedupe)",
                                        "acronym list: 2 tables with header ['Term', 'Description'] (core merge)"]


def test_cell_fix_requires_exactly_one_hit():
    doc = _doc([_table([["A", "B"], ["NATD-LIC-RPRT0002-A", "x"]], 95)])
    C.table_cell_fixes(doc, fixes=[("NATD-LIC-RPRT0002-A", "NATD-LIC-RPRT-0002-A", 95, ""),
                                   ("Gone from the source", "x", 73, "")])
    assert doc.els[0].table.grid[1][0].text == "NATD-LIC-RPRT-0002-A"
    assert doc.meta["psar_ch01_qa"] == ["cell fix 'Gone from the source' (p73): 0 hits"]


def test_check_withheld_dedupes_and_flags():
    call = "> [!withheld] SRI — This information is withheld in accordance with 10 CFR 2.390"
    els = []
    for n in range(5, 18):
        els.append(El("heading", f"Figure 1.1-{n} X", 44 + n, meta={"figure": f"1.1-{n}"}))
        els.append(El("raw_md", call, 44 + n, meta={"withheld": True}))
    els.insert(2, El("raw_md", call, 49, meta={"withheld": True}))      # duplicate after Figure 1.1-5
    doc = _doc(els)
    C.check_withheld(doc)
    assert sum(1 for e in doc.els if e.meta.get("withheld")) == 13
    assert not doc.meta.get("psar_ch01_qa")


# ------------------------------------------------------------ real document ----
@pytest.fixture(scope="module")
def built():
    if not os.path.exists(os.path.join(RAW, STEM + ".json")):
        pytest.skip("raw PSAR ch1 conversion not available")
    import clean_references as CR
    from refclean.doc import load_doc
    from refclean.emit import render
    from refclean.pdfaux import build_aux
    prof = importlib.import_module("refclean.profiles.psar")
    doc = load_doc("PSAR_ch01", STEM, CR.RAW, CR.OUT)
    aux = build_aux(doc.pdf_path, chapter=1, exclude=CR.table_regions(doc))
    aux.meta["render_figures"] = False
    for step in prof.steps(1):
        step(doc, aux)
    text = render(doc, prof.metadata(doc, 1, aux))
    text, failed = CR.apply_patches("PSAR_ch01", text)
    body = text.split("\n---\n", 1)[1]
    return doc, aux, text, body, failed


def _table_after(body, first_line):
    """Rows (after the separator) of the Markdown table whose header line is `first_line`."""
    lines = body.split("\n")
    i = lines.index(first_line)
    rows = []
    for ln in lines[i + 2:]:
        if not ln.startswith("|"):
            break
        rows.append([c.strip() for c in ln.strip("|").split(" | ")])
    return rows


@pytest.mark.refs
def test_real_no_qa_issues(built):
    doc, aux, text, body, failed = built
    assert not doc.meta.get("psar_ch01_qa")
    assert failed == []
    assert sum(1 for e in doc.els if e.kind == "heading" and e.meta.get("numbered")) == 74
    assert doc.meta.get("psar_ch01_joined") and len(doc.meta["psar_ch01_joined"]) == 2


@pytest.mark.refs
def test_real_acronym_list(built):
    body = built[3]
    assert body.count("LIST OF ACRONYMS AND ABBREVIATIONS") == 1
    assert "\n## LIST OF ACRONYMS AND ABBREVIATIONS\n" in body
    rows = _table_after(body, "| Term | Description |")
    assert len(rows) == 487 and body.count("| Term | Description |") == 1
    assert ["V<sub>S</sub>", "Shear-Wave Velocity"] in rows
    assert ["V<sub>S30</sub>", "Time-averaged shear-wave velocity in the upper 30 meters"] in rows
    assert ["HCI", "hydrochloric acid"] in rows                         # source typo kept (review §5.2)


@pytest.mark.refs
def test_real_table_141(built):
    body = built[3]
    head = "| Guide Number | Title | Revision | Conformance Status | Comments |"
    assert body.count("Guide Number") == 1 and "(Sheet" not in body
    assert "### Table 1.4-1 Conformance with Regulatory Guides\n\n" + head in body
    rows = _table_after(body, head)
    assert len(rows) == 183 and all(len(r) == 5 for r in rows)
    status = [r[3] for r in rows]
    assert status.count("Full Conformance") == 96 and status.count("Partial Conformance") == 24
    assert sum(1 for s in status if s.startswith("The guidance is not applicable")) == 63
    assert sum(1 for r in rows if r[4]) == 26
    r183 = next(r for r in rows if r[0] == "1.183")
    assert "accident specific methodologies and assumptions" in r183[4]


@pytest.mark.refs
def test_real_tables_144_145_merged_with_captions(built):
    body = built[3]
    for cap, head, n in [("### Table 1.4-4 Applicability of TMI-Related Requirements",
                          "| Regulation | Description | Compliance Status | Section |", 47),
                         ("### Table 1.4-5 Consensus Codes and Standards",
                          "| Codes and Standards | Revision/Edition | Title |", 167)]:
        assert body.count(cap) == 1 and body.count(head) == 1
        assert cap + "\n\n" + head in body
        assert len(_table_after(body, head)) == n


@pytest.mark.refs
def test_real_site_layout_legend(built):
    body = built[3]
    img = "![Figure 1.2-1 Site Layout](figures/PSAR_ch01/Fig_1.2-1.png)"
    assert img + "\n\n| Facility number | Facility |" in body
    rows = _table_after(body, "| Facility number | Facility |")
    assert [r[0] for r in rows] == C.LEGEND_NUMBERS
    assert rows[0] == ["11", "REACTOR BUILDING"] and rows[-1] == ["85", "AUXILIARY BOILER"]
    assert ["84", "STEAM GENERATOR BUILDING/TURBINE FACILITY BUILDING (STEAM) RACK"] in rows
    assert "<!-- page 58 | 1.2-1 -->" in body and "<!-- page 59 | 1.2-2 -->" in body
    assert not re.search(r"^(?:- )?1\.2-[12] Revision 1$", body, re.M)


@pytest.mark.refs
def test_real_bold_status_terms(built):
    body = built[3]
    for term, dash in [("Full Conformance", "–"), ("Partial Conformance", "–"), ("Full Compliance", "–"),
                       ("Partial Compliance", "-"), ("Not Applicable", "–")]:
        assert body.count(f"\n**{term}** {dash} ") == 1
    assert body.count("**") == 10                                        # D7: no other emphasis


@pytest.mark.refs
def test_real_value_fixes_and_kept_typos(built):
    body = built[3]
    for good in ["NATD-LIC-RPRT-0002-A", "Initial Test Programs for Water-Cooled Nuclear Power Plants",
                 "Tamper-Indicating", "reliable long-term operation", "all non-essential systems",
                 "monitoring of in-plant radiation", "Preliminary Design Information - Containment Integrity",
                 "NUREG/CR-7046", "| 3.12, 3.13 |", "Part 3: Limit - All Parts",
                 "Nuclear facilities - Equipment important to safety - Seismic qualification",
                 "| 7.1.3; 11.2 |", "| 7.6.5; 11.2 |", "| 5.3.2.10, 7.6.7 |"]:
        assert good in body, good
    for bad in ["RPRT0002", "WaterCooled", "TamperIndicating", "longterm", "nonessential", "inplant",
                "Information Containment", "NUREG/ CR", "3.12,; 3.13", "Limit; - All", "facilities; - Equipment",
                "| 7.1.3 11.2 |", "| 7.6.5 11.2 |"]:
        assert bad not in body, bad
    for typo in ["Manufactures", "(PCO) and, provides", "conditions.Each", "during an station blackout", "areas.The",
                 "power- operated", "800F", "Division I |", "Low-, Medium- and High-Expansion", "noncondensible"]:
        assert typo in body, typo


@pytest.mark.refs
def test_real_paragraph_repairs(built):
    body = built[3]
    assert "Utilization Facilities.”\n\nThis preliminary safety analysis report (PSAR)" in body
    assert "through the manipulation of the CRD. During shutdown" in body
    assert "natural draft airflow instead of the IAC blower. The IAC is" in body
    assert "\n  - a different type of reactor design\n  - an SSC that is not part of the design" in body
    assert ("![Figure 1.3-1 Diverse Barriers in Functional Containment](figures/PSAR_ch01/Fig_1.3-1.png)\n\n"
            "\\*Sub-compartments within building provides additional confinement, depending on event.") in body


@pytest.mark.refs
def test_real_withheld_figures(built):
    body = built[3]
    assert "[[" not in body and "]]" not in body
    call = "> [!withheld] SRI — This information is withheld in accordance with 10 CFR 2.390"
    assert body.count(call) == 13
    for n in range(5, 18):
        m = re.search(rf"^### Figure 1\.1-{n} [^\n]+\n\n(.*?)(?=^#)", body, re.M | re.S)
        assert m, n
        assert [ln for ln in m.group(1).split("\n") if ln.strip() and not ln.startswith("<!--")] == [call], n


@pytest.mark.refs
def test_real_verify_residual_is_pinned(built):
    """The accepted PDF-vs-output residual, 437 of 26,258 tokens (1.66 %) on 2026-09-13.

    Composition: the 'X' fence markers and the numbered map callouts of Figure 1.2-1 Site Layout (p59, 331 tokens,
    figure debris deleted per D3), the barrier labels inside Figure 1.3-1 (p65, 16), and the 26 '(Sheet n of 26)'
    labels of Table 1.4-1 plus its table-border rows that `pdfaux.header_footer_band` cuts from the PDF side
    (see refclean/verify.py, blind spots 1-2). Tolerance +-10 tokens: a larger change means prose left the output.
    """
    from refclean.verify import verify
    doc, aux, text = built[0], built[1], built[2]
    res = verify(doc, aux, text)
    s = res["summary"]
    assert s["residue"] == {}
    assert s["headings_whitelist"] == s["headings_emitted"] == 74
    assert abs(s["missing_tokens"] - 437) <= 10, s["missing_tokens"]
    assert s["missing_pct"] < 1.8
    assert set(res["pages_missing"]) <= {59, 65, 69, 92}
    missing = dict(res["top_missing"])
    assert missing["x"] == 277 and missing["sheet"] == 26     # figure fence markers, sheet labels
