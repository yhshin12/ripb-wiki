"""PSAR ch6 hook: synthetic unit tests + one smoke build of the real chapter (review_ch6 acceptance items)."""
import os
import re
import sys

import pytest

SCRIPTS = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, SCRIPTS)
from refclean.doc import Doc, El  # noqa: E402
from refclean.pdfaux import Aux, Line, SupRef  # noqa: E402
from refclean.profiles import psar_ch06 as P  # noqa: E402
from refclean.tables import Cell, Table, render_md  # noqa: E402

VAULT = os.path.dirname(SCRIPTS)
RAW = os.path.join(VAULT, "references", "raw")
KEY = "PSAR_ch06"


def _doc(els):
    return Doc(KEY, "x", RAW, VAULT, 1, {}, els)


# ------------------------------------------------------------------ units ----
def test_symbol_recombines_subscripts_and_markers():
    assert P._symbol("W (2)\ntw") == "Wtw (2)"
    assert P._symbol("L\nr") == "Lr"
    assert P._symbol("Y (8)\nj") == "Yj (8)"
    assert P._symbol("W(2)\ni") == "Wi(2)"
    assert P._symbol("D(3)(4)") == "D(3)(4)"
    assert P._symbol("") == ""


def test_parse_sheet_flattens_three_level_header():
    # leading empty column (Table 6.4-12 layout) and the trailing all-None row are dropped
    rows = [
        ["", "", None, "Normal and Severe", "Extreme and Abnormal", None],
        ["", "Design Load Cases(1)(5)", None, "C-9", "C-9(6)", "C-10"],
        ["", "Load Combination Equation No.", None, "9-5", "9-6", "9-6"],
        ["", "Safe Shutdown Earthquake", "E\nss", "", "", "1.0"],
        [None, None, None, None, None, None],
    ]
    names, body = P.parse_sheet(rows)
    assert names[2:] == ["Normal and Severe: C-9: 9-5", "Extreme and Abnormal: C-9(6): 9-6",
                         "Extreme and Abnormal: C-10: 9-6"]
    assert names[0] == names[1] == "Design Load Cases(1)(5): Load Combination Equation No."
    assert body == [["Safe Shutdown Earthquake", "Ess", "", "", "1.0"]]


def test_pdf_notes_joins_continuations_and_skips_footer():
    def ln(t, y, size=11.0):
        return Line(t, 73.0, y, 700.0, y + 10, size, ("Arial",), 0)
    lines = [ln("Accident Pipe Break Missile Impact Ym 1.0", 150), ln("Notes", 187),
             ln("(1) Refer to Section 6.4.2.2.", 204),
             ln("(3) Load combinations ... For any other load (e.g., Live) if the load reduces the effects of", 238),
             ln("other loads. Otherwise, the factor for that load", 252), ln("is zero.", 266),
             ln("(17)In ASCE/SEI 7-16", 507), ln("6.4-49 Revision 1", 725, 10.0), ln("SUBJECT TO DOE", 726, 7.2)]
    header, notes = P.pdf_notes(lines)
    assert header == "Notes"
    assert notes == ["(1) Refer to Section 6.4.2.2.",
                     "(3) Load combinations ... For any other load (e.g., Live) if the load reduces the effects of "
                     "other loads. Otherwise, the factor for that load is zero.",
                     "(17) In ASCE/SEI 7-16"]


def test_nested_dash_items():
    d = _doc([El("item", "Pipe Break Loads, subcategorized as:", 29), El("item", "- Pipe Break Reaction Loads (Yr)", 29),
              El("item", "- Pipe Break Missile Impact Loads (Ym)", 29), El("para", "x", 29)])
    P.nested_dash_items(d)
    assert [(e.text, e.level) for e in d.els[:3]] == [("Pipe Break Loads, subcategorized as:", 0),
                                                      ("Pipe Break Reaction Loads (Yr)", 1),
                                                      ("Pipe Break Missile Impact Loads (Ym)", 1)]


IBC = ("1.4 (D + F) 1.2 (D + F) + 1.6 (L + H) + 0.5 (Lr or S or R) 1.2 (D + F) + 1.6 (Lr or S or R) + 1.6 H + "
       "(f1 L or 0.5 W) 1.2 (D + F) + 1.0 W + f1 L + 1.6 H + 0.5 (Lr or S or R) 1.2 (D + F) + 1.0E + f1 L + 1.6 H + "
       "f2 S 0.9 D + 1.0 W + 1.6 H 0.9 (D + F) + 1.0 E + 1.6 H")


def test_formula_blocks_ibc_and_legend():
    d = _doc([El("para", IBC, 29), El("para", "Where:", 29), El("para", "D – Dead Load", 29),
              El("para", "E – determined from ASCE 7-16 or Ess – Combined effect of horizontal and vertical earthquake "
                         "induced forces as defined in Section 2.3.6 of ASCE 7-16", 29),
              El("para", "Ess – Safe Shutdown Earthquake", 29),
              El("para", "F – Load due to fluids with well-defined pressures and maximum heights H – Load due to "
                         "lateral earth pressures, ground water pressure or pressure of bulk materials L – Live Load", 29),
              El("para", "Lr – Roof Live Load S – Snow Load R – Rain Load W – Wind Load f1 = 1 (for places of public "
                         "assembly live loads in excess of 100 psf, and parking garages and 0.5 for other live loads)", 30),
              El("item", "f2 = 0.7 (for roof configurations that do not shed snow off the structure and 0.2 for other "
                         "roof configurations)", 30),
              El("para", "ACI 318-19 and AISC 360-16 load combinations are used if determined to be more stringent.", 30)])
    P.formula_blocks(d)
    items = [e for e in d.els if e.kind == "item"]
    assert [e.text for e in items[:7]] == ["1.4 (D + F)", "1.2 (D + F) + 1.6 (L + H) + 0.5 (Lr or S or R)",
                                           "1.2 (D + F) + 1.6 (Lr or S or R) + 1.6 H + (f1 L or 0.5 W)",
                                           "1.2 (D + F) + 1.0 W + f1 L + 1.6 H + 0.5 (Lr or S or R)",
                                           "1.2 (D + F) + 1.0E + f1 L + 1.6 H + f2 S", "0.9 D + 1.0 W + 1.6 H",
                                           "0.9 (D + F) + 1.0 E + 1.6 H"]
    legend = [e.text.split()[0] for e in items[7:]]
    assert legend == ["D", "E", "Ess", "F", "H", "L", "Lr", "S", "R", "W", "f1", "f2"]
    assert items[8].text.startswith("E – determined from ASCE 7-16 or Ess – Combined effect")
    assert d.els[7].text == "Where:" and d.els[-1].text.startswith("ACI 318-19")


def test_formula_blocks_cracked_properties():
    d = _doc([El("para", "t' = 0.707 × t E’ = 1.414 × E G’ = 1.414 × G γ' = 1.414 × γ", 32),
              El("para", "Where E’ = Modulus of elasticity of concrete for cracked section", 32),
              El("para", "E = Modulus of elasticity of concrete for uncracked section G’ = Shear modulus of concrete "
                         "for cracked section G = Shear modulus of concrete for uncracked section γ' = Weight density of "
                         "concrete for cracked section γ = Weight density of concrete for uncracked section t' = "
                         "Thickness of cracked wall or slab section t = Thickness of uncracked wall or slab section "
                         "Ig = Gross moment of inertia A = Gross area of concrete section", 33)])
    P.formula_blocks(d)
    assert [e.text for e in d.els[:4]] == ["t' = 0.707 × t", "E’ = 1.414 × E", "G’ = 1.414 × G", "γ' = 1.414 × γ"]
    assert d.els[4].kind == "para" and d.els[4].text == "Where"
    defs = [e.text.split(" = ")[0] for e in d.els[5:]]
    assert defs == ["E’", "E", "G’", "G", "γ'", "γ", "t'", "t", "Ig", "A"]


def test_transient_titles_become_bold_paragraphs_below_h6():
    d = _doc([El("heading", "6.4.3.1.1 Design Transients", 38, meta={"numbered": True, "num": "6.4.3.1.1"}),
              El("heading", "Service Level A Conditions", 39, meta={"sub": True}),
              El("para", "Service Level A Transient 1 – Cold Shutdown to Hot Standby", 39),
              El("para", "Service Level B Transient 6 - Reactor Power Runback", 42),
              El("para", "Test 1 – Hydrostatic or Pneumatic Test", 43),
              El("para", "Service Level A Transient 1 describes", 39)])
    P.transient_titles(d)
    assert [e.text for e in d.els[2:5]] == ["**Service Level A Transient 1 – Cold Shutdown to Hot Standby**",
                                            "**Service Level B Transient 6 - Reactor Power Runback**",
                                            "**Test 1 – Hydrostatic or Pneumatic Test**"]
    assert d.els[5].text == "Service Level A Transient 1 describes"


def test_glued_note_markers_need_pdf_superscript_evidence():
    t = Table(grid=[[Cell("SSC", 0, 0, bold=True), Cell("Tornado Wind3", 0, 1, bold=True)],
                    [Cell("FHB2", 1, 0), Cell("Yes1", 1, 1)], [Cell("NCB", 2, 0), Cell("Yes", 2, 1)]],
              page=77, pages=[77])
    d = _doc([El("table", "", 77, table=t)])
    aux = Aux(sups={77: [SupRef("Wind", "3", "Wind"), SupRef("FHB", "2", "FHB"), SupRef("Yes", "1", "Yes")]})
    P.glued_note_markers(d, aux)
    assert render_md(t).splitlines()[0] == "| SSC | Tornado Wind<sup>3</sup> |"
    assert render_md(t).splitlines()[2:] == ["| FHB<sup>2</sup> | Yes<sup>1</sup> |", "| NCB | Yes |"]


# ------------------------------------------------------------ smoke build ----
@pytest.fixture(scope="module")
def built():
    if not os.path.exists(os.path.join(RAW, "TP_Natrium_PSAR2025_ch6_Safety-Significant SSC Criteria and "
                                            "Capabilities.json")):
        pytest.skip("raw ch6 conversion not present")
    import clean_references as CR
    from refclean.doc import load_doc
    from refclean.emit import render
    from refclean.pdfaux import build_aux
    from refclean.profiles import DOCS, psar
    stem, _, chapter = DOCS[KEY]
    doc = load_doc(KEY, stem, CR.RAW, CR.OUT)
    aux = build_aux(doc.pdf_path, chapter=chapter, exclude=CR.table_regions(doc))
    aux.meta["render_figures"] = False
    for st in psar.steps(chapter):
        st(doc, aux)
    text, failed = CR.apply_patches(KEY, render(doc, psar.metadata(doc, chapter, aux)))
    return doc, aux, text, failed


def _section(text, start, end_pat=r"^#{1,6} "):
    i = text.index(start)
    m = re.compile(end_pat, re.M).search(text, i + len(start))
    return text[i:m.start() if m else len(text)]


def _row(section, label):
    line = next(ln for ln in section.split("\n") if ln.startswith(f"| {label} |"))
    return [c.strip() for c in line.strip().strip("|").split("|")]


def test_smoke_headings_and_subheading(built):
    doc, aux, text, failed = built
    nums = [e.meta["num"] for e in doc.els if e.kind == "heading" and e.meta.get("numbered")]
    assert len(nums) == 74 == len(set(nums)) == len(aux.headings)
    for n in ("6.1.1.4.2", "6.1.1.5", "6.4.1.3", "6.4.1.3.1", "6.4.2.2.5"):
        assert n in nums
    assert "##### 6.4.2.2.5 Loading Combinations\n\n###### SR Substructure Loading Combinations\n" in text
    assert doc.meta.get("unmatched_subheads") == [] and doc.meta.get("unmatched_headings") == []
    assert failed == []


def test_smoke_load_factor_counts_match_pdf(built):
    doc, aux, text, failed = built
    qa = doc.meta["ch6_load_tables"]
    assert {k: v["factors"] for k, v in qa.items()} == P.EXPECTED_FACTORS
    assert sum(v["factors"] for v in qa.values()) == 522
    assert all(v["odl_diff"] == [] for v in qa.values())
    for tid, n in P.EXPECTED_NOTES.items():
        if tid in qa:
            assert qa[tid]["note_numbers"] == list(range(1, n + 1))


def test_smoke_load_tables_attributed_by_page(built):
    doc, aux, text, failed = built
    by_id = {e.meta["ch6_load_table"]: e for e in doc.els if e.kind == "table" and e.meta.get("ch6_load_table")}
    assert set(by_id) == set(P.LOAD_TABLES)
    for tid, e in by_id.items():
        assert e.page == P.LOAD_TABLES[tid][0] and e.table.pages == list(P.LOAD_TABLES[tid])
        assert e.table.caption.startswith(f"Table {tid} ")
    assert "Substructure Analysis of Concrete" in by_id["6.4-7"].table.caption
    assert "Superstructure Analysis of Concrete" in by_id["6.4-11"].table.caption
    assert "Substructure Analysis of Steel" in by_id["6.4-8"].table.caption
    assert "Superstructure Analysis of Steel" in by_id["6.4-12"].table.caption
    # one header row; C-9 and C-9(6) are distinct columns
    t5 = _section(text, "### Table 6.4-5 ")
    header = t5.split("\n")[2]
    assert "| Normal and Severe: C-9: 9-5 | Extreme and Abnormal: C-9(6): 9-6 |" in header
    assert len(re.findall(r"^\|(?:---\|)+$", t5, re.M)) == 1
    assert "Design Load Cases" not in "".join(t5.split("\n")[4:])
    # SSE factors (all lost in the old conversion): C-10 and C-17 in 6.4-5; S-18, S-24, S-25 in 6.4-6
    assert _row(t5, "Safe Shutdown Earthquake") == ["Safe Shutdown Earthquake", "Ess"] + [""] * 10 + ["1.0"] + [""] * 4 + ["1.0"]
    t6 = _section(text, "### Table 6.4-6 ")
    assert "| Normal and Severe: S-17(6): NB2-6 | Extreme and Abnormal: S-18: NB2-6 |" in t6
    assert _row(t6, "Safe Shutdown Earthquake") == ["Safe Shutdown Earthquake", "Ess"] + [""] * 17 + ["1.0"] + [""] * 3 + ["0.7", "0.7"]
    sse = sum(1 for tid in ("6.4-7", "6.4-8", "6.4-11", "6.4-12")
              for v in _row(_section(text, f"### Table {tid} "), "Safe Shutdown Earthquake")[2:] if v)
    assert sse == 6   # 11 SSE factors in total over the six tables


def test_smoke_notes_complete_and_attached(built):
    doc, aux, text, failed = built
    t5 = _section(text, "### Table 6.4-5 ")
    assert "\nNotes\n\n- (1) Refer to Section 6.4.2.2" in t5
    assert "occurs simultaneously with the other loads. Otherwise, the factor for that load is zero." in t5
    t6 = _section(text, "### Table 6.4-6 ")
    assert "that on other gravity loads (e.g., L, Lr, S, Ccr) shall be zero." in t6
    t7 = _section(text, "### Table 6.4-7 ")
    assert "and Section 1.2 in RG 1.199." in t7 and "Interim Staff Guidance DC/COL-ISG-007." in t7
    t8 = _section(text, "### Table 6.4-8 ")
    assert "hydrodynamic loads are taken as Yj." in t8 and "the load factor on dead load is 0.90" in t8
    t11 = _section(text, "### Table 6.4-11 ")
    assert "- (4) Load factor is 1.4 (in lieu of 1.2 in ACI 349-13) are in accordance" in t11
    t12 = _section(text, "### Table 6.4-12 ")
    assert "DC/COL ISG-007." in t12   # source spelling kept
    t9 = _section(text, "### Table 6.4-9 ")
    assert "- (4) The overturning factor of safety" in t9
    assert not re.search(r"^\(\d+\)\S", text, re.M)
    assert not re.search(r"^\(?Sheet \d+ of \d+\)?$", text, re.M)


def test_smoke_formulas_legend_lambda(built):
    doc, aux, text, failed = built
    assert doc.meta["ch6_formulas"] == {"ibc_combinations": 7, "legend_entries": 12, "cracked_properties": 4,
                                        "definitions": 10}
    assert "- 1.4 (D + F)\n- 1.2 (D + F) + 1.6 (L + H) + 0.5 (Lr or S or R)\n" in text
    assert "- L – Live Load\n" in text and "- f2 = 0.7 (for roof configurations" in text
    assert ("λ = V / f\n\nWhere\n\n- λ = The wavelength\n- V = The lowest shear wave velocity\n"
            "- f = The highest frequency of interest (i.e., cutoff frequency)\n") in text
    assert "λ V f" not in text


def test_smoke_superscripts_and_transients(built):
    doc, aux, text, failed = built
    for s in ("Motion<sup>1</sup>", "FHB<sup>2</sup>", "RAB<sup>2</sup>", "Yes<sup>1</sup>", "Wind<sup>3</sup>",
              "Protection<sup>2</sup>"):
        assert s in text
    assert not re.search(r"\b(?:FHB2|RAB2|Yes1|Motion1|Wind3|Protection2)\b", text)
    assert "- <sup>1</sup> See Section 6.4.1.2.3" in text
    assert "Seismic Risk Category IV" in text and "Importance Factor, I = 1.25" in text
    titles = re.findall(r"^\*\*((?:Service Level [A-D] Transient \d+|Test \d) [–-] [^*]+)\*\*$", text, re.M)
    assert len(titles) == 30
    assert doc.meta["ch6_transients"] == 30


def test_smoke_source_defects_kept(built):
    doc, aux, text, failed = built
    assert sorted(doc.meta["ch6_source_notes"]) == sorted(["alpha", "xref", "mesh", "6.4-6", "6.4-8", "6.4-9", "6.4-16"])
    assert "are provided in Table 6.4-11 and Table 6.4-12." in text
    assert "| Accident Pipe Break Jet Impingement | Yi (7) |" in text
    assert "| A. 9 | Runback Recovery |" in text
    assert "For soft soil and backfill: = [(600 ft/sec) / (14 Hz)] / 5 = 8.6 feet (2.6 meters)" in text
    assert "| Overturning Factor of Safety | 1.1 | 1.5 | 1.1 | 1.1 | -- |  |" in text
    assert "- for systems with single supports, and" in text
    assert text.count("<!-- source:") == 7


def test_smoke_verify_residual_is_pinned(built):
    """The accepted PDF-vs-output residual, 29 of 22,629 tokens (0.13 %) on 2026-09-13.

    Composition: the '(Sheet n of 2)' labels of the six merged load-combination tables (14 tokens) and the glued
    note markers the output renders as `<sup>n</sup>` ('motion1', 'protection2', 'yes1', 'wind3', 'fhb2', 'rab2',
    9 tokens on p77), plus single hyphen-split words ('light-water', 'cooled', 'significant'). Tolerance +-10
    tokens: a larger change means text left the output somewhere else.
    """
    from refclean.verify import verify
    doc, aux, text, _failed = built
    res = verify(doc, aux, text)
    s = res["summary"]
    assert s["residue"] == {}
    assert s["headings_whitelist"] == s["headings_emitted"] == 74
    assert abs(s["missing_tokens"] - 29) <= 10, s["missing_tokens"]
    assert s["missing_pct"] < 0.2
    assert set(res["pages_missing"]) <= {77}
    assert [w for k, v in doc.meta.items() if k.endswith("_warnings") for w in v] == []
