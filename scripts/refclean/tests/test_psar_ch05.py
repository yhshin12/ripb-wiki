"""PSAR Chapter 5 hooks: unit tests on synthetic elements + checks of one real build (no PNG rendering, nothing
written to references/). The real-document checks compare the PSF records with a third, independent extraction
(PyMuPDF `find_tables`) besides the opendataloader cross-check that runs inside the step."""
import collections
import importlib
import os
import re
import sys

import fitz
import pytest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from refclean import tables as T  # noqa: E402
from refclean.doc import Doc, El  # noqa: E402
from refclean.pdfaux import Aux, Line  # noqa: E402
from refclean.profiles import psar_ch05 as C  # noqa: E402

VAULT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
RAW = os.path.join(VAULT, "references", "raw")
STEM = "TP_Natrium_PSAR2025_ch5_Safety Functions, Design Criteria, and SSC Safety Classification"

# Review ch45 §2a: number of LBE entries per PSF (0 = 'None' / 'N/A').
LBE_COUNTS = {
    "DL3-RC1": 31, "DL3-RC2": 0, "DL3-HR1": 14, "DL3-HR2": 14, "DL3-HR3": 12, "DL3-HR4": 9, "DL3-HR5": 9,
    "DL3-HR6": 1, "DL3-HR7": 1, "DL3-HR8": 1, "DL3-HR9": 0, "DL3-HR10": 2, "DL3-HR11": 2, "DL3-HR12": 5,
    "DL3-HR13": 0, "DL3-RR1": 6, "DL3-RR2": 51, "DL3-RR3": 4, "DL3-RR4": 2, "DL3-RR5": 3, "DL3-RR5a": 2,
    "DL3-RR6": 2, "DL3-RR7": 0, "DL3-RR8": 0, "DL3-RR10": 7,
    "DL4-RC1": 0, "DL4-RC3": 6, "DL4-RC4": 0, "DL4-RC6": 6, "DL4-RC6a": 1, "DL4-RC6b": 3, "DL4-RC6c": 0,
    "DL4-RC6d": 0, "DL2-HR2": 0, "DL4-HR1": 11, "DL4-HR2": 0, "DL4-HR3": 0, "DL4-HR4": 1, "DL4-HR6": 0,
    "DL4-HR7": 0, "DL2-RR2": 1, "DL2-RR4": 0, "DL2-RR7": 0, "DL2-RR8": 0, "DL2-RR10": 0, "DL4-RR1": 7,
    "DL4-RR1a": 4, "DL4-RR1b": 0, "DL4-RR1c": 2, "DL4-RR3": 1, "DL4-RR3a": 0, "DL4-RR3b": 0, "DL4-RR3c": 0,
    "DL4-RR4": 0, "DL4-RR4a": 0, "DL4-RR4b": 0, "DL4-RR4c": 0, "DL4-RR5": 0, "DL4-RR7": 1, "DL4-RR8": 0,
    "DL4-DID1": 0, "DL5-PAM1": 0,
}
TABLE_OF = {pid: no for no, ids in C.EXPECTED_PSF.items() for pid in ids}


def _doc(els, labels=None):
    return Doc("PSAR_ch05", STEM, RAW, os.path.join(VAULT, "references"), 52, labels or {}, els)


# ------------------------------------------------------------------ unit ----
def test_expected_psf_list():
    ids = [p for no in ("5.2-1", "5.2-2", "5.2-3", "5.2-4") for p in C.EXPECTED_PSF[no]]
    assert len(ids) == 62 and len(set(ids)) == 62 and set(ids) == set(LBE_COUNTS)
    assert sum(1 for p in ids if TABLE_OF[p] != "5.2-4") == 25
    assert sum(LBE_COUNTS.values()) == 222


def test_join_lines_and_ssc_names():
    assert C.join_lines("Scram - Gravity Driven Absorber\nInsertion by Latch Release") == \
        "Scram - Gravity Driven Absorber Insertion by Latch Release"
    assert C.join_lines("to prevent\nover-\npressurization") == "to prevent over-pressurization"
    assert C.ssc_names("Nuclear Island (NI) DC Power Supply System (NDC)\nNI Uninterruptible AC Power Supply "
                       "System (NUP)") == ["Nuclear Island (NI) DC Power Supply System (NDC)",
                                           "NI Uninterruptible AC Power Supply System (NUP)"]
    assert C.ssc_names("Anticipatory Automatic Seismic\nTrip System (AST)\nSee Note 1") == \
        ["Anticipatory Automatic Seismic Trip System (AST)", "See Note 1"]


def test_lbe_field_groups_type_runs_in_source_order():
    assert C._lbe_field("Associated LBE / Type", [("None", "N/A")]) == ["- **Associated LBE / Type:** None / N/A"]
    assert C._lbe_field("Associated LBE ID", [("A-1", "AOO"), ("B-1", "AOO"), ("C-1", "DBE"), ("D-1", "AOO")]) == [
        "- **Associated LBE ID:**", "  - AOO: A-1, B-1", "  - DBE: C-1", "  - AOO: D-1"]


def test_render_records_use_verbatim_headers():
    sr = C.PSF("5.2-3", "DL3-RR4", "EVST Barrier", 15, lbes=[("RFH-FDET-BL", "BDBE"), ("RFH-FDET-1", "BDBE")],
               rows=[(["Ex-Vessel Fuel Handling System (FHE)", "Sodium Processing System (SPS)"], "During x."),
                     (["Ex-Vessel Fuel Handling System (FHE)"], "When y.")])
    hdr = ["PSF-ID", "SR Function Description", "Associated LBE", "Type", "SR SSC(s)", "SRDC"]
    assert C.render_record(sr, hdr, 4).split("\n") == [
        "#### DL3-RR4 — EVST Barrier", "", "- **PSF-ID:** DL3-RR4", "- **SR Function Description:** EVST Barrier",
        "- **Associated LBE / Type:**", "  - BDBE: RFH-FDET-BL, RFH-FDET-1", "", "| SR SSC(s) | SRDC |", "|---|---|",
        "| Ex-Vessel Fuel Handling System (FHE); Sodium Processing System (SPS) | During x. |",
        "| Ex-Vessel Fuel Handling System (FHE) | When y. |"]
    ns = C.PSF("5.2-4", "DL4-RR3a", "SPS Supply Valve Isolation on Leak Detection", 19, lbes=[("None", "N/A")],
               criteria="Required for DID Adequacy",
               sscs=["Auxiliary Monitoring and Control System (AMC)", "NI Fire Protection System (NFP)"])
    hdr4 = ["PSF ID", "PSF Description", "NSRST SSC Safety Significance Criteria (Risk-Significant or DID)",
            "Associated LBE ID", None, "SSC(s)"]
    assert C.render_record(ns, hdr4, 4).split("\n")[2:] == [
        "- **PSF ID:** DL4-RR3a", "- **PSF Description:** SPS Supply Valve Isolation on Leak Detection",
        "- **NSRST SSC Safety Significance Criteria (Risk-Significant or DID):** Required for DID Adequacy",
        "- **Associated LBE ID:** None / N/A", "- **SSC(s):**",
        "  - Auxiliary Monitoring and Control System (AMC)", "  - NI Fire Protection System (NFP)"]


def test_join_enumeration_breaks():
    doc = _doc([El("para", "(1) specified limits are not exceeded as a result of occurrences and", 28),
                El("para", "(2) safety functions are maintained.", 28),
                El("para", "provided that the following conditions are met:", 48),
                El("para", "(1) postulated leakage does not result in failure", 48),
                El("para", "Methods include use of:", 45),
                El("item", "seals and inert gases to prevent oxygen ingress", 45),
                El("item", "leakage detection equipment", 45)])
    C.join_enumeration_breaks(doc)
    assert [e.text for e in doc.els] == [
        "(1) specified limits are not exceeded as a result of occurrences and (2) safety functions are maintained.",
        "provided that the following conditions are met:", "(1) postulated leakage does not result in failure",
        "Methods include use of:", "seals and inert gases to prevent oxygen ingress", "leakage detection equipment"]


def test_rpcs_lists_split_join_and_references():
    rp = lambda p: El("heading", "Relevant PSAR Chapters and Sections", p, meta={"sub": True})   # noqa: E731
    doc = _doc([rp(27), El("para", "Section 3.13, Section 7.1.2, Section 7.2.5,", 27), El("para", "Section 7.6", 27),
                El("heading", "5.3.2.7 PDC 16 - Containment Design", 27, meta={"numbered": True, "num": "5.3.2.7"}),
                rp(50), El("para", "Section 7.8.1 References 5.3-1 TerraPower, “Principal Design Criteria for the "
                                   "Natrium Advanced Reactor,”", 50),
                El("para", "NATD-LIC-RPRT-0002-A, Revision 1", 50)])
    C.rpcs_lists(doc)
    assert [(e.kind, e.text) for e in doc.els] == [
        ("heading", "Relevant PSAR Chapters and Sections"), ("item", "Section 3.13"), ("item", "Section 7.1.2"),
        ("item", "Section 7.2.5"), ("item", "Section 7.6"), ("heading", "5.3.2.7 PDC 16 - Containment Design"),
        ("heading", "Relevant PSAR Chapters and Sections"), ("item", "Section 7.8.1"), ("heading", "References"),
        ("item", "5.3-1 TerraPower, “Principal Design Criteria for the Natrium Advanced Reactor,” "
                 "NATD-LIC-RPRT-0002-A, Revision 1")]
    assert doc.els[8].meta.get("keep_heading") and doc.meta["psar_ch05_rpcs_lists"] == 2
    assert not doc.meta.get("psar_ch05_qa")


def test_ordered_lists():
    doc = _doc([El("item", "1. Doppler – temperature changes in the fuel.", 25, list_style="arabic numbers"),
                El("item", "Section 7.5.1", 30, list_style="unordered")])
    C.ordered_lists(doc)
    assert [(e.kind, e.text) for e in doc.els] == [("para", "1. Doppler – temperature changes in the fuel."),
                                                   ("item", "Section 7.5.1")]
    assert doc.meta["psar_ch05_ordered_items"] == 1


def test_table_notes_superscript_marker_and_page_break():
    aux = Aux()
    aux.meta["body_size"] = 11.0
    r = fitz.Rect(73, 682, 78, 691)
    aux.meta["lines_by_page"] = {20: [Line("1 DL4-RC6(a-d) is identified", 73, 682, 900, 695, 11.0, ("Arial",), 0,
                                           [("1", r, 7.68, "Arial", 0, 0),
                                            ("DL4-RC6(a-d) is identified", fitz.Rect(87, 682, 900, 695), 11.0,
                                             "Arial", 0, 0)])]}
    t = T.Table(grid=[[T.Cell("PSF ID", 0, 0)]], page=17, pages=[17, 18, 19, 20], caption="Table 5.2-4 NSRST Functions",
                notes=["Note: 1 DL4-RC6(a-d) is identified as a defense line function. The requirement is therefore "
                       "not discussed further in the construction permit"])
    doc = _doc([El("table", "", 17, table=t), El("para", "application.", 20),
                El("heading", "5.3 Principal Design Criteria", 21, meta={"numbered": True})])
    C.table_notes(doc, aux)
    assert t.notes == ["Note:", "<sup>1</sup> DL4-RC6(a-d) is identified as a defense line function. The requirement "
                                "is therefore not discussed further in the construction permit application."]
    assert [e.kind for e in doc.els] == ["table", "heading"] and not doc.meta.get("psar_ch05_qa")


def test_split_merged_paragraphs():
    doc = _doc([El("para", "Characterization of natural phenomena for the site is described in Chapter 2. Design "
                           "basis hazard levels are established using the site characterization information.", 22),
                El("para", "Design basis hazard levels are established using the site characterization.", 22)])
    C.split_merged_paragraphs(doc, starts={22: ["Design basis hazard levels are established using the site ch"]})
    assert [e.text for e in doc.els] == [
        "Characterization of natural phenomena for the site is described in Chapter 2.",
        "Design basis hazard levels are established using the site characterization information.",
        "Design basis hazard levels are established using the site characterization."]


# ------------------------------------------------------------ real document ----
@pytest.fixture(scope="module")
def built():
    if not os.path.exists(os.path.join(RAW, STEM + ".json")):
        pytest.skip("raw PSAR ch5 conversion not available")
    import clean_references as CR
    from refclean.doc import load_doc
    from refclean.emit import render
    from refclean.pdfaux import build_aux
    prof = importlib.import_module("refclean.profiles.psar")
    doc = load_doc("PSAR_ch05", STEM, CR.RAW, CR.OUT)
    aux = build_aux(doc.pdf_path, chapter=5, exclude=CR.table_regions(doc))
    aux.meta["render_figures"] = False
    for step in prof.steps(5):
        step(doc, aux)
    text = render(doc, prof.metadata(doc, 5, aux))
    text, failed = CR.apply_patches("PSAR_ch05", text)
    body = text.split("\n---\n", 1)[1]
    return doc, aux, text, body, failed


def _records(body):
    """{psf_id: record markdown} for every '#### DLn-… — …' record (up to the next heading / anchor-free end)."""
    out = {}
    for m in re.finditer(r"^#### (DL\d-[A-Z]+\d+[a-z]?) — .*?(?=^#{1,4} |\Z)", body, re.M | re.S):
        assert m.group(1) not in out, m.group(1)
        out[m.group(1)] = m.group(0)
    return out


def _lbe_pairs(rec):
    pairs = []
    m = re.search(r"^- \*\*Associated LBE[^*]*:\*\* None / (\S+)$", rec, re.M)
    if m:
        return []
    for tm in re.finditer(r"^  - (AOO|DBE|BDBE): (.+)$", rec, re.M):
        pairs += [(x, tm.group(1)) for x in tm.group(2).split(", ")]
    return pairs


def test_real_no_qa_issues(built):
    doc, aux, text, body, failed = built
    assert doc.meta.get("psar_ch05_qa", []) == []
    assert failed == [] and doc.meta.get("unmatched_headings") == [] and doc.meta.get("unmatched_subheads") == []
    assert len(aux.headings) == 67
    assert sum(1 for e in doc.els if e.kind == "heading" and e.meta.get("numbered")) == 67


def test_real_62_psf_records_once_in_order(built):
    body = built[3]
    ids = re.findall(r"^#### (DL\d-[A-Z]+\d+[a-z]?) — ", body, re.M)
    assert ids == [p for no in ("5.2-1", "5.2-2", "5.2-3", "5.2-4") for p in C.EXPECTED_PSF[no]]
    for no, cap in [("5.2-1", "SR Functions Supporting Control of Heat Generation"),
                    ("5.2-2", "SR Functions Supporting Control of Heat Removal"),
                    ("5.2-3", "SR Functions Supporting Retaining Radionuclides"), ("5.2-4", "NSRST Functions")]:
        assert body.count(f"\n### Table {no} {cap}\n") == 1
        first = C.EXPECTED_PSF[no][0]
        assert re.search(rf"### Table {re.escape(no)} {cap}\n\n#### {first} — ", body)
    assert "(Sheet" not in body and "(continued)" not in body and "<br>" not in body
    assert "\n| PSF ID |" not in body and "\n| PSF-ID |" not in body       # no flat grid tables left


def test_real_record_headers_verbatim_per_table(built):
    recs = _records(built[3])
    for pid, rec in recs.items():
        no = TABLE_OF[pid]
        idf = "PSF-ID" if no == "5.2-3" else "PSF ID"
        assert f"\n- **{idf}:** {pid}\n" in rec, pid
        if no == "5.2-4":
            for f in ("PSF Description", "NSRST SSC Safety Significance Criteria (Risk-Significant or DID)",
                      "Associated LBE ID", "SSC(s)"):
                assert f"- **{f}:**" in rec, (pid, f)
            assert "| SR SSC(s) | SRDC |" not in rec
        else:
            lbe = "Associated LBE(s)" if no == "5.2-1" else "Associated LBE"
            assert f"- **SR Function Description:** " in rec and f"- **{lbe} / Type:**" in rec, pid
            assert rec.count("| SR SSC(s) | SRDC |") == 1, pid


def test_real_lbe_counts_and_type_pairing(built):
    doc, recs = built[0], _records(built[3])
    total, runs = 0, 0
    for pid, rec in recs.items():
        pairs = _lbe_pairs(rec)
        assert len(pairs) == LBE_COUNTS[pid], pid
        if LBE_COUNTS[pid] == 0:
            assert re.search(r"^- \*\*Associated LBE[^*]*:\*\* None / N/A$", rec, re.M), pid
        total += len(pairs)
        runs += len(re.findall(r"^  - (?:AOO|DBE|BDBE): ", rec, re.M))
    # 222 typed LBE entries (review §2a) rendered as 52 type runs: every list is grouped by type in source order
    assert total == 222 and runs == 52
    # every LBE list is contiguous by type in the source (one run per type), so no LBE is reordered
    for pid, rec in recs.items():
        labels = re.findall(r"^  - (AOO|DBE|BDBE): ", rec, re.M)
        assert len(labels) == len(set(labels)), pid


def _pymupdf_cells():
    """Independent extraction: PyMuPDF find_tables per page -> {psf_id: {'lbes','types','ssc','srdc'}}."""
    pdf = fitz.open(os.path.join(RAW, STEM + ".pdf"))
    out, cur = {}, None
    for pno in range(6, 21):
        tabs = pdf[pno - 1].find_tables().tables
        assert len(tabs) == 1, pno
        rows = tabs[0].extract()
        nsrst = (rows[0][5] or "").strip() == "SSC(s)"
        for r in rows[1:]:
            if r[0]:
                pid = C.CONTINUED.sub("", C.join_lines(r[0]))
                cur = out.setdefault(pid, {"lbes": [], "types": [], "ssc": [], "srdc": [], "pages": set()})
            cur["pages"].add(pno)
            li, ti = (3, 4) if nsrst else (2, 3)
            if r[li]:
                cur["lbes"] += r[li].split()
            if r[ti]:
                cur["types"] += r[ti].split()
            if r[5 if nsrst else 4]:
                cur["ssc"].append(r[5 if nsrst else 4])
            if not nsrst and r[5]:
                cur["srdc"].append(" ".join(r[5].split()))
    pdf.close()
    return out


def test_real_records_match_pymupdf_tables(built):
    recs, ref = _records(built[3]), _pymupdf_cells()
    assert set(ref) == set(recs)
    for pid, rec in recs.items():
        r = ref[pid]
        pairs = _lbe_pairs(rec)
        if pairs:
            assert [x for x, _ in pairs] == r["lbes"] and [y for _, y in pairs] == r["types"], pid
        else:
            assert r["lbes"] == ["None"] * len(r["lbes"]) and len(r["lbes"]) >= 1, pid
        ssc_lines = [ln.strip() for cell in r["ssc"] for ln in cell.split("\n") if ln.strip()]
        if TABLE_OF[pid] == "5.2-4":
            m = re.search(r"^- \*\*SSC\(s\):\*\*(.*?)(?=\Z|^#|^<!--)", rec, re.M | re.S)
            names = [x.strip() for x in re.findall(r"^  - (.+)$", m.group(1), re.M)] or [m.group(1).strip()]
            assert names == ssc_lines, pid
            continue
        rows = [ln for ln in rec.split("\n") if ln.startswith("| ") and not ln.startswith("| SR SSC(s)")]
        cells = [[c.strip() for c in ln.strip("|").split(" | ")] for ln in rows]
        assert [c[1] for c in cells] == r["srdc"], pid                     # every SRDC word, in order
        mine = [n for c in cells for n in c[0].split("; ")]
        assert set(mine) == set(ssc_lines) and all(n in mine for n in ssc_lines), pid


def test_real_dl3_rr2_merged(built):
    rec = _records(built[3])["DL3-RR2"]
    assert len(_lbe_pairs(rec)) == 51
    assert rec.count("| Reactor Core System (RCC) |") == 1
    assert ("| Reactor Core System (RCC) | During accident conditions, the fuel cladding shall retain radionuclide "
            "fission products to establish reasonable assurance radionuclide release results in calculated "
            "radiological dose under the 10 CFR 50.34 dose criteria at a safe shutdown condition. |") in rec
    assert "IPI-IHEL-1" in rec and "SUD-IHEL-1" in rec                  # continuation sheet (p14) LBEs


def test_real_table_notes_after_last_record(built):
    body = built[3]
    note1 = ("- Note 1: DL3-RR10 is added at the CP stage to mitigate radionuclide release from SCG pathways in the "
             "following LBEs: LFF-SAO-BL, RFH-FDIV-1, RFH-FDIV-3, LFF-SAO-CN, RFH-FDIV-CN, DHP-LOOP-3, DHP-LOOP-4, "
             "LFF-SAO-1, and LFF-SAO-2.")
    assert body.count(note1) == 1
    assert re.search(r"\| See Note 1 \| See Note 1 \|\n\n" + re.escape(note1) +
                     r".*?including mitigation provided by DL3-RR10\.\n\n<!-- page 17-20 \| 5\.2-13\.\.5\.2-16 -->\n\n"
                     r"### Table 5\.2-4", body, re.S)
    note2 = ("Note:\n- <sup>1</sup> DL4-RC6(a-d) is identified as a defense line function in the most recent revision "
             "of the PRA. The requirement has not yet been integrated into the design and is therefore not discussed "
             "further in the construction permit application.\n\n<!-- page 21 | 5.3-1 -->\n\n## 5.3 Principal")
    assert note2 in body
    assert re.search(r"- Nuclear Instrumentation System \(XIS\)\n\n" + re.escape(note2[:40]), body)
    assert not re.search(r"^application\.$", body, re.M)


def test_real_amc_and_restored_ssc_names(built):
    recs = _records(built[3])
    for pid in ("DL4-RR3a", "DL4-RR3b", "DL4-RR4a"):
        assert "  - Auxiliary Monitoring and Control System (AMC)\n" in recs[pid], pid
    assert "- **SSC(s):** Gaseous Radwaste Processing System (RWG)" in recs["DL2-RR4"]
    assert "- **SSC(s):** Water Pool Fuel Handling System (FHP)" in recs["DL2-RR2"]
    assert "Auxiliary NI Fire" not in built[3]


def test_real_page_anchors(built):
    """One range anchor per merged table (core) plus one anchor per further sheet page (this profile); no page is
    announced twice and no range start is repeated."""
    body = built[3]
    single = [int(x) for x in re.findall(r"^<!-- page (\d+) \|", body, re.M)]
    ranges = [(int(a), int(b)) for a, b in re.findall(r"^<!-- page (\d+)-(\d+) \|", body, re.M)]
    assert ranges == [(6, 7), (8, 11), (12, 16), (17, 20)]                  # the four PSF tables
    assert single == sorted(single) and len(single) == len(set(single))
    assert [x for x in single if 6 <= x <= 20] == [7, 9, 10, 11, 13, 14, 15, 16, 18, 19, 20]
    assert [x for x in single if x < 6 or x > 20] == [4, 5] + list(range(21, 53))
    for a, b in ranges:
        assert a not in single                                             # the range start is not repeated
    assert "<!-- page 13 | 5.2-9 -->\n\n#### DL3-RR2 — Cladding barrier" in body
    assert "<!-- page 14 | 5.2-10 -->\n\n#### DL3-RR3 — EVHM Cask barrier" in body


def test_real_pdc_headings_and_subheadings(built):
    doc, aux, text, body, failed = built
    pdc = re.findall(r"^#### (5\.3\.\d+\.\d+) (PDC \d+ - .+)$", body, re.M)
    want = [(h.num, h.title) for h in aux.headings if re.match(r"^5\.3\.\d+\.\d+$", h.num)]
    assert pdc == want and len(pdc) == 53
    assert [int(re.match(r"PDC (\d+)", t).group(1)) for _, t in pdc] == \
        list(range(1, 6)) + list(range(10, 27)) + list(range(28, 38)) + [44, 45, 46] + list(range(60, 65)) + \
        list(range(70, 83))
    assert "\n### 5.3.3 Reactivity Control\n\n#### 5.3.3.1 PDC 20 - Protection System Functions\n" in body
    # Both labels are emitted by the core (structure.insert_subheads) alone: the profile's former repair step was
    # deleted in the 2026-09-13 fix wave after it was shown to convert/split/insert nothing, so these two counts
    # are now the regression check for the header-band label handling.
    assert body.count("\n##### Implementation Summary\n") == 53
    assert body.count("\n##### Relevant PSAR Chapters and Sections\n") == 53
    for m in re.finditer(r"^##### Relevant PSAR Chapters and Sections\n\n((?:- .*\n)+)", body, re.M):
        assert all(re.fullmatch(r"- (?:Section|Chapter) \d+(?:\.\d+)*", ln) for ln in m.group(1).split("\n") if ln)
    assert len(re.findall(r"^##### Relevant PSAR Chapters and Sections\n\n- (?:Section|Chapter) ", body, re.M)) == 53
    assert ("##### Relevant PSAR Chapters and Sections\n\n- Section 3.13\n- Section 7.1.2\n- Section 7.1.3\n"
            "- Section 7.2.3\n- Section 7.2.4\n- Section 7.2.5\n- Section 7.6\n") in body          # PDC 15 wrap
    assert ("- Section 7.8.1\n\n### References (5.3)\n\n- 5.3-1 TerraPower, “Principal Design Criteria for the "
            "Natrium Advanced Reactor,” NATD-LIC-RPRT-0002-A, Revision 1\n") in body


def test_real_no_false_list_markers(built):
    doc, body = built[0], built[3]
    assert not re.search(r"^\s*- \d+\.\s", body, re.M)                    # bullet + number (B21)
    assert not re.search(r"^\s*- 5\.\d+(?:\.\d+)* [A-Z]", body, re.M)     # headings as items
    assert len(re.findall(r"^\d\. ", body, re.M)) == 12
    assert "\n1. Doppler – temperature changes in the fuel alter associated neutron cross-sections.\n" in body
    # every remaining item in §5.2-§5.5 prose is an RPCS reference, a References entry, or a printed '●' bullet
    pdf = fitz.open(doc.pdf_path)
    bullets = sum(1 for p in range(21, 51) for ln in pdf[p - 1].get_text().split("\n") if ln.strip() == "●")
    pdf.close()
    others = [e for e in doc.els if e.kind == "item" and e.page >= 21 and not e.meta.get("rpcs")
              and not re.match(r"^\d+\.\d+-\d+ ", e.text)]
    assert len(others) == bullets == 21
    assert "\n- seals and inert gases to prevent oxygen ingress into sodium containing vessels\n" in body  # PDC 73


def test_real_paragraph_repairs(built):
    body = built[3]
    for joined in ["as a result of anticipated operational occurrences and (2) safety functions that rely on electric",
                   "(1) material properties, (2) the effects of irradiation and coolant composition",
                   "These limits shall be based on consideration of (1) chemical attack, (2) fouling",
                   "shall be designed to permit (1) periodic inspection and functional testing of important areas"]:
        assert joined in body, joined
    assert "the following conditions are met:\n\n(1) postulated leakage at the interface location" in body  # PDC 78
    assert "is described in Chapter 2.\n\nDesign basis hazard levels are established" in body            # B22
    assert "RWS, RWL, and RWG.\n\nFuel handling systems provide heat removal capabilities" in body
    assert len(built[0].meta.get("psar_ch05_para_splits", [])) == 13


def test_real_source_wording_kept(built):
    body = built[3]
    assert body.count("Water Fuel Pool Handling System (FHP)") == 3      # DL3-HR10, DL3-HR13, DL5-PAM1 (sic)
    assert body.count("Water Pool Fuel Handling System (FHP)") >= 6
    for sic in ["sends a sends a signal", "from effecting all rods", "radionuclide release limits design",
                "one rod bundle form the reactor core", "will satisfactorily perform their safety functions is "
                "described in Section 8.1", "design limits is not exceeded"]:
        assert sic in body, sic


def test_real_verify_residual_is_explained(built):
    from refclean.verify import verify
    doc, aux, text = built[0], built[1], built[2]
    res = verify(doc, aux, text)
    assert res["summary"]["residue"] == {}
    assert res["summary"]["headings_whitelist"] == res["summary"]["headings_emitted"] == 67
    missing = collections.Counter(dict(res["top_missing"]))
    # The LBE field states each type once per run instead of once per LBE line: the 222 AOO/DBE/BDBE tokens of
    # the four tables become 52 type-run labels. No LBE ID is lost (test_real_lbe_counts_and_type_pairing).
    assert missing["aoo"] + missing["dbe"] + missing["bdbe"] == 222 - 52
    rest = {k: v for k, v in missing.items() if k not in ("aoo", "dbe", "bdbe")}
    # the only other loss: the '(continued)' label of the DL3-RR2 sheet split, dropped when the record was merged
    assert rest == {"continued": 2}
    assert sum(missing.values()) == 172 and res["summary"]["missing_pct"] < 1.1
