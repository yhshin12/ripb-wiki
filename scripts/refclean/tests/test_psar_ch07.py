"""PSAR ch7 hook: unit tests on synthetic input, PDF-level tests of the DL-function table reconstruction
(expected ID lists from review_ch7a §2, review_ch7b §2, review_ch7c §5.1) and checks of one real build made in
memory (no PNG rendering, nothing written to references/, so the tests exercise the code and not a stale file)."""
import collections
import os
import re
import sys

import pytest

HERE = os.path.dirname(os.path.abspath(__file__))
SCRIPTS = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, SCRIPTS)

from refclean.doc import Doc, El  # noqa: E402
from refclean.profiles import psar_ch07 as P  # noqa: E402

VAULT = os.path.dirname(SCRIPTS)
RAW = os.path.join(VAULT, "references", "raw")
STEM = "TP_Natrium_PSAR2025_ch7_Descriptions for Safety-Significant SSCs"
PDF = os.path.join(RAW, STEM + ".pdf")
KEY = "PSAR_ch07"

# (first PDF page, third column header) -> Function IDs in document order
EXPECTED = {
    (14, "RCC Functional Support"): ["DL3-RC1", "DL3-RR2", "DL3-HR5", "DL3-HR6", "DL3-HR7", "DL3-HR8", "DL3-HR9",
                                     "DL3-HR10", "DL3-HR13", "DL4-RC3"],
    (31, "RES Functional Support"): ["DL3-RC1", "DL3-HR4", "DL3-HR5", "DL3-RR1", "DL4-RR1"],
    (63, "PHT Functional Support"): ["DL3-HR1", "DL3-HR2", "DL3-HR5", "DL3-RR1a", "DL3-RR1d", "DL4-HR1", "DL4-HR2",
                                     "DL4-HR6"],
    (86, "IHT Functional Support"): ["DL2-HR2", "DL4-HR7", "DL3-HR3", "DL3-HR12", "DL4-HR1", "DL4-HR3", "DL4-DID1"],
    (96, "RAC Functional Support"): ["DL3-HR4", "DL5-PAM1"],
    (108, "IAC Functional Support"): ["DL4-HR1"],
    (122, "SCG Functional Support"): ["DL3-RR1c", "DL3-RR7", "DL4-HR1", "DL2-RR10", "DL4-RR4", "DL4-RR4a", "DL4-RR4c",
                                      "DL5-PAM1"],
    (138, "SPS Functional Support"): ["DL3-HR11", "DL3-RR1b", "DL3-RR4", "DL4-HR1", "DL2-RR7", "DL2-RR8", "DL4-RR8",
                                      "DL4-RR3", "DL4-RR3a", "DL4-RR3b", "DL4-RR3c", "DL5-PAM1"],
    (155, "CRD Functional Support"): ["DL3-RC1, DL3-RC2", "DL4-RC3", "DL3-RR1"],
    (168, "FHP Functional Support"): ["DL3-HR10", "DL3-HR13", "DL3-RR8", "DL3-RR5a", "DL4-HR4", "DL2-RR2", "DL5-PAM1"],
    (188, "FHE Functional Support"): ["DL3-HR6", "DL3-HR7", "DL3-HR8", "DL3-HR9", "DL3-RR3", "DL3-RR3a", "DL3-RR4",
                                      "DL3-RR5", "DL3-RR5a", "DL3-RR6", "DL4-RR5", "DL5-PAM1"],
    (207, "FHI Functional Support"): ["DL3-RR1f"],
    (219, None): ["DL2-RR4"],                                     # RWG: no header row in the PDF
    (229, None): ["DL4-RR1", "DL4-RR1a", "DL4-RR1c", "DL4-RR3", "DL4-RR3c", "DL4-RR4", "DL4-RR4b", "DL4-RR4c",
                  "DL4-RR7", "DL5-PAM1"],                         # NHV
    (237, "NNA Functional Support"): ["DL4-RR3a", "DL4-RR3b", "DL4-RR3c"],
    (254, "AMC Functional Support"): ["DL4-RR3a", "DL4-RR3b", "DL4-RR4a"],
    (255, "CTC Functional Support"): ["DL2-HR2", "DL4-HR2", "DL4-HR3"],
    (255, "UMC Functional Support"): ["DL4-RR1c", "DL4-RR3c", "DL4-RR4b", "DL4-RR4c"],
    (268, "RPS Functional Support"): ["DL3-RC1a", "DL3-RC1b", "DL3-RC1c", "DL3-RC1d", "DL3-RC1e", "DL3-RC1f",
                                      "DL3-RC1g", "DL3-RC1h", "DL3-RC1i", "DL3-RC1j", "DL3-RC2", "DL3- HR2",
                                      "DL3-HR3", "DL3-HR11", "DL3-HR12", "DL4-RC1", "DL4-RC3", "DL4-RC4", "DL4-HR6",
                                      "DL4-HR7", "DL4-RR8", "DL5-PAM1"],
    (283, "XIS Functional Support"): ["DL3-RC1a", "DL3-RC1d", "DL3-RC1f", "DL3-RC1g", "DL3-RC1i", "DL3- HR2",
                                      "DL3-HR3", "DL3-HR12", "DL5-PAM1"],
    (295, "RIS Functional Support"): ["DL3-RC1b", "DL3-RC1c", "DL3-RC1d", "DL3-RC1e", "DL3-RC1h", "DL3-RC1j",
                                      "DL3-HR2", "DL3-HR3", "DL3-HR11", "DL3-HR12", "DL4-HR2", "DL4-HR3", "DL4-RR8",
                                      "DL5-PAM1"],
    (308, "RMS Functional Support"): ["DL4-RR1c", "DL4-RR4a", "DL4-RR4b", "DL5-PAM1"],
    (322, "AST Functional Support"): ["DL4-RC4"],
    (328, "NDC and NUP Functional Support"): ["DL4-RC3", "DL4-RC4", "DL2-HR2", "DL4-HR2", "DL4-HR3", "DL4-HR6",
                                              "DL4-HR7", "DL4-RR3b", "DL4-RR4c", "DL4-RR7", "DL4-RR8", "DL5-PAM1"],
    (339, "Functional Support"): ["DL3-HR4", "DL4-RR1", "DL4-RR1a"],     # RXB substructure
    (350, "Functional Support"): ["DL4-RR7"],                            # FHB superstructure
    (356, "RAB Functional Support"): ["DL4-RR3"],
}


@pytest.fixture(scope="module")
def tables():
    if not os.path.exists(PDF):
        pytest.skip("source PDF not available")
    return P.build_dl_tables(P.extract_dl_segments(PDF))


@pytest.fixture(scope="module")
def built_doc():
    """One in-memory build of the real chapter (no PNG rendering, nothing written to references/)."""
    if not os.path.exists(os.path.join(RAW, STEM + ".json")):
        pytest.skip("raw PSAR ch7 conversion not available")
    import clean_references as CR
    from refclean.doc import load_doc
    from refclean.emit import render
    from refclean.pdfaux import build_aux
    from refclean.profiles import psar
    doc = load_doc(KEY, STEM, CR.RAW, CR.OUT)
    aux = build_aux(doc.pdf_path, chapter=7, exclude=CR.table_regions(doc))
    aux.meta["render_figures"] = False
    for step in psar.steps(7):
        step(doc, aux)
    text, failed = CR.apply_patches(KEY, render(doc, psar.metadata(doc, 7, aux)))
    return doc, aux, text, failed


@pytest.fixture(scope="module")
def built(built_doc):
    """The built Markdown (frontmatter + body), as references/<stem>.md would hold it."""
    return built_doc[2]


# ------------------------------------------------------------------ units ----
def test_cell_text_joins_lines():
    assert P._cell_text(["Passive Heat Removal in the", "Ex-Vessel Storage Tank (SR)"]) == \
        "Passive Heat Removal in the Ex-Vessel Storage Tank (SR)"
    assert P._cell_text(["Post-", "Accident Monitoring"]) == "Post-Accident Monitoring"   # line-end hyphen
    assert P._cell_text(["monitoring the following PAM variables:", "• Reactor Vessel Pressure",
                         "• Cover Gas Radiation"]) == \
        "monitoring the following PAM variables: Reactor Vessel Pressure; Cover Gas Radiation"


def test_fill_shared_support_spans_every_row():
    rows = [{"id": "DL4-RC3", "desc": [], "sup": [("The NDC and NUP", 1)]},
            {"id": "DL4-RC4", "desc": [], "sup": [("provide electric power to", 2)]},
            {"id": "DL2-HR2", "desc": [], "sup": [("support these functions.", 3)]},
            {"id": "DL5-PAM1", "desc": [], "sup": []}]
    t = {"rows": rows}
    P._fill_shared_support(t)
    joined = [" ".join(x[0] for x in r["sup"]) for r in rows]
    assert joined == ["The NDC and NUP provide electric power to support these functions."] * 4
    assert all(r.get("shared_support") for r in rows)


def test_nested_nic_items_strip_the_printed_dash():
    els = [El("item", "Auxiliary Monitoring and Control System (AMC) – The AMC monitors", 251),
           El("item", "- Gaseous Radwaste Processing System (Section 7.4.1)", 251),
           El("item", "- Sodium Cover Gas (SCG) (Section 7.2.3)", 251)]
    doc = Doc("PSAR_ch07", STEM, RAW, VAULT, 372, {}, els)
    P.nested_nic_items(doc, None)
    assert doc.meta["ch07_nested_items"] == 2
    assert [(e.level, e.text) for e in doc.els[1:]] == [
        (1, "Gaseous Radwaste Processing System (Section 7.4.1)"), (1, "Sodium Cover Gas (SCG) (Section 7.2.3)")]


def test_numbered_items_become_one_ordered_list():
    els = [El("item", "1. Analysis, using the applicable design rules", 42),
           El("item", "2. CMTRs are required", 42), El("item", "3. 100% volumetric examination", 42)]
    doc = Doc("PSAR_ch07", STEM, RAW, VAULT, 372, {}, els)
    P.numbered_items(doc, None)
    assert [e.kind for e in doc.els] == ["raw_md"]
    assert doc.els[0].text.splitlines() == ["1. Analysis, using the applicable design rules",
                                            "2. CMTRs are required", "3. 100% volumetric examination"]


# ------------------------------------------------------- DL function tables ----
def test_all_dl_tables_and_rows_are_found(tables):
    assert len(tables) == 27                                    # review_ch7a 7 + ch7b 8 + ch7c 12
    assert sum(len(t["cells"]) for t in tables) == 167          # 41 + 49 + 77 rows


def test_dl_table_ids_match_the_reviews(tables):
    got = {(t["segs"][0]["page"], t["header"]): [c[0] for c in t["cells"]] for t in tables}
    assert got == EXPECTED


def test_page_split_tables_are_merged(tables):
    pages = {(t["segs"][0]["page"], t["header"]): sorted({s["page"] for s in t["segs"]}) for t in tables}
    assert pages[(14, "RCC Functional Support")] == [14, 15]
    assert pages[(268, "RPS Functional Support")] == [268, 269, 270]
    assert pages[(255, "UMC Functional Support")] == [255, 256]


def test_rps_rows_keep_their_own_support_text(tables):
    """review_ch7c §1 #1: the DL3-HR3 support sentence was printed before its ID, and DL4-HR7/DL4-RR8 were merged."""
    rows = {c[0]: c for t in tables if t["segs"][0]["page"] == 268 for c in t["cells"]}
    assert rows["DL3- HR2"][2].endswith("the PSPs are tripped.")
    assert rows["DL3-HR3"][2].endswith("the ISPs are tripped.")
    assert rows["DL4-HR7"] == ("DL4-HR7", "Manual ISP trip", "ISP pumps are tripped on manual switch.")
    assert rows["DL4-RR8"][1] == "Manual SPS pump trip on low primary sodium level"
    assert rows["DL4-RR8"][2].startswith("RPS continuously monitors and displays primary sodium hot pool level")


def test_ris_rows_keep_their_own_support_text(tables):
    """review_ch7c §1 #2: RC1e, RC1h and RC1j shared one merged support paragraph."""
    rows = {c[0]: c for t in tables if t["segs"][0]["page"] == 295 for c in t["cells"]}
    assert "cold pool temperature" in rows["DL3-RC1e"][2]
    assert "hot pool level" in rows["DL3-RC1h"][2]
    assert "PSP speed and PSP current" in rows["DL3-RC1j"][2]


def test_classification_tags_stay_in_the_description(tables):
    """review_ch7a §1 #4(b) and review_ch7b §1 #1: the (SR)/(NSRST) line of five rows was read after the support."""
    by_page = {t["segs"][0]["page"]: {c[0]: c for c in t["cells"]} for t in tables}
    assert by_page[14]["DL3-RC1"][1] == "Scram - Gravity Driven Absorber Insertion by Latch Release (SR)"
    assert by_page[31]["DL3-RC1"][1] == "Scram – Gravity driven absorber insertion by latch release (SR)"
    assert by_page[86]["DL2-HR2"][1] == "ISP Trip on Low IHT level (NSRST)"
    assert by_page[96]["DL3-HR4"][1] == "Inherent - RAC Operation (SR)"
    assert by_page[108]["DL4-HR1"][1] == "IAC Passive Mode Operation (NSRST)"
    assert by_page[138]["DL3-HR11"][1] == "SPS Pump Trip on Low Primary Sodium Level (SR)"


def test_ndc_nup_shared_support_cell_is_filled_down(tables):
    rows = [c for t in tables if t["segs"][0]["page"] == 328 for c in t["cells"]]
    assert len(rows) == 12
    assert {c[2] for c in rows} == {"The NDC and NUP provide electric power to support performance of these functions."}


def test_source_typos_are_kept(tables):
    """review_ch7c §5.2 do-not-fix list."""
    cells = [c for t in tables for c in t["cells"]]
    assert any(c[0] == "DL3- HR2" for c in cells)                         # PDF p269/p284
    assert any("poistion" in c[2] for c in cells)                         # UMC DL4-RR4c, p256
    assert any("compares Them" in c[2] for c in cells)                    # RPS DL3-RC1b, p268


# ------------------------------------------------------------------ build ----
def test_built_tables_are_markdown(built):
    assert built.count("| Function ID | Function Description |") == 27
    assert "| DL3-RR1f | FHI Seal (SR) | The FHI seals to the head perform part of the primary coolant boundary" in built
    assert re.search(r"^Function ID Function Description", built, re.M) is None      # no prose remnants left


def test_built_rms_table_sits_under_its_own_section(built):
    dl = built.index("##### 7.6.6.2.1 Defense Line Functions")
    pdc = built.index("##### 7.6.6.2.2 Principal Design Criteria")
    row = built.index("| DL4-RR1c | Head Access Area (HAA) HVAC operations following postulated release", dl)
    assert dl < row < pdc                      # the same row text also appears in the UMC table (p255)


def test_built_headings_and_lists(built):
    assert len(re.findall(r"^#+ 7(?:\.\d+)+ ", built, re.M)) == 289       # 67 + 76 + 146 numbered sections
    assert "\n- Consistent with PDC" not in built                          # false list markers removed
    assert "\n- - " not in built and "\n  - - " not in built               # NIC sub-bullets nested, not doubled
    assert built.count("\n  - Gaseous Radwaste Processing System (Section 7.4.1)") == 1


def test_built_numbers_and_note_markers(built):
    assert "3.98E+15 n/cm2-s" in built and "3.98 x 1015" not in built
    assert "| Base Material<sup>*</sup> | Weld Material<sup>**</sup> |" in built
    assert "- <sup>*</sup> Classification is for integrity of the associated pressure boundary only" in built
    assert "| Vapor Trap | SR<sup>*</sup> |" in built
    assert "k<sub>eff</sub> ≤ 0.95" in built


def test_built_paragraphs_are_not_over_long(built):
    body = [ln for ln in built.splitlines() if not ln.startswith("|")]
    assert max((len(ln) for ln in body), default=0) < 2000


def test_built_keeps_source_repeats_and_typos(built):
    assert built.count("Security for I&C systems is addressed") == 6
    assert built.count("Design Reliability Assurance Program") >= 15
    assert "NI Contol Building HVAC" in built and "poistion" in built and "DL3- HR2" in built


def test_built_subheadings_after_a_colon_lead_in(built):
    """Subheadings the core leaves in the paragraph because the text before them ends in a colon (p265, p365)."""
    lines = built.splitlines()
    assert "##### RG 1.22, Revision 0, Periodic Testing of Protection System Actuation Functions" in lines
    assert lines.count("###### External Hazard Protection for SR SSCs (SR)") == 2
    assert not any(ln.strip() == "###### Functional Support" for ln in lines)   # DL table header line
    assert not any(ln.startswith(") The NCB substructure") for ln in lines)     # ")" stays with the heading


def test_built_qa_is_clean(built_doc):
    """Everything the profile computes about its own work must come out empty: the DL-table rebuild is the one step
    that deletes source text, so its two-way token coverage is the gate."""
    doc, aux, text, failed = built_doc
    assert failed == []
    assert doc.meta.get("unmatched_headings", []) == [] and doc.meta.get("unmatched_subheads", []) == []
    assert [w for k, v in doc.meta.items() if k.endswith("_warnings") for w in v] == []
    qa = doc.meta["ch07_dl_qa"]
    assert qa["tables"] == 27 and qa["rows"] == 167
    assert qa["removed_not_in_table"] == 0        # no removed prose token is missing from the rebuilt table
    assert qa["table_not_in_removed"] == 0        # no table token was invented
    assert all(x["removed_elements"] > 0 for x in doc.meta["dl_tables"])


def test_built_verify_residual_is_pinned(built_doc):
    """The accepted PDF-vs-output residual, 507 of 118,355 tokens (0.43 %) on 2026-09-13.

    It is figure text that D3 deletes with the figure box: the Figure 7.6.2-1 legend and controller boxes (p262,
    150 tokens), the two SLDs of 7.2.3 (p131-132, 131 tokens), and the block-diagram labels of p56/p113/p178/p179
    (100 tokens); the rest are the two figure-debris tables of p334/p335 and single label words. Tolerance +-10
    tokens: a larger change means text left the output somewhere else and must be explained before the pin moves.
    """
    from refclean.verify import verify
    doc, aux, text, _ = built_doc
    res = verify(doc, aux, text)
    s = res["summary"]
    assert s["residue"] == {}
    assert s["headings_whitelist"] == s["headings_emitted"] == 289
    assert abs(s["missing_tokens"] - 507) <= 10, s["missing_tokens"]
    assert s["missing_pct"] < 0.5
    # every page with more than 3 missing tokens is a figure page
    assert set(res["pages_missing"]) <= {56, 113, 131, 132, 178, 179, 262, 334, 335}
    missing = collections.Counter(dict(res["top_missing"]))
    assert missing["redundant"] == 18 and missing["skid"] == 18        # Figure 7.6.2-1 / SLD labels
