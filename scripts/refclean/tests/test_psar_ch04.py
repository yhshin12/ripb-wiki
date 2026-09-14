"""PSAR Chapter 4 (Integrated Evaluations): output-level checks of one real build made in memory (no PNG
rendering, nothing written to references/).

ch4 is the only document that needs no chapter hook — it is produced by the core pipeline alone (`profiles/psar.py`
plus `psar_ch04.py` does not exist), so these tests are the regression gate for the core on a whole document:
Task 7 acceptance items (heading tree, Table 4.2-2 with its `[d]` column, `5E-07`, no TOC, page anchors) and
Task 9g (two-row table headers flattened, table notes as a list).
"""
import os
import re
import sys

import pytest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

VAULT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
RAW = os.path.join(VAULT, "references", "raw")
KEY = "PSAR_ch04"
STEM = "TP_Natrium_PSAR2025_ch4_integrated evaluations"

# The 15 numbered sections of ch4, in printed order (PDF p4-p11; the ch4 TOC lists exactly these).
HEADINGS = [
    ("4.1", 2, "Overall Plant Risk Performance Summary"),
    ("4.1.1", 3, "Site Boundary Dose"),
    ("4.1.2", 3, "Exclusion Area Boundary Early Fatality Risk"),
    ("4.1.3", 3, "Latent Cancer Risk"),
    ("4.2", 2, "Defense-in-Depth"),
    ("4.2.1", 3, "Plant Capability Summary"),
    ("4.2.1.1", 4, "LBE Margin"),
    ("4.2.1.2", 4, "Layers of Defense Evaluation"),
    ("4.2.1.3", 4, "Single Feature Reliance"),
    ("4.2.1.4", 4, "Prevention-Mitigation Balance"),
    ("4.2.2", 3, "Programmatic DID Summary"),
    ("4.2.2.1", 4, "Evaluation of Significant Uncertainties"),
    ("4.2.2.2", 4, "Programs Required for safety-related SSC Performance Monitoring"),   # source case kept
    ("4.2.2.3", 4, "Programs Required for NSRST SSC Performance Monitoring"),
    ("4.2.3", 3, "Integrated DID Evaluation"),
]

# Table 4.2-2 'Mean Dose Margin[d]' column, top to bottom (PDF p13).
DOSE_MARGIN_D = ["3.79", "3.09", "4.25", "9.90", "4.10", "17.2", "8.22", "3.08", "13.3", "4.42", "15.0"]


@pytest.fixture(scope="module")
def built():
    if not os.path.exists(os.path.join(RAW, STEM + ".json")):
        pytest.skip("raw PSAR ch4 conversion not available")
    import clean_references as CR
    from refclean.doc import load_doc
    from refclean.emit import render
    from refclean.pdfaux import build_aux
    from refclean.profiles import psar
    doc = load_doc(KEY, STEM, CR.RAW, CR.OUT)
    aux = build_aux(doc.pdf_path, chapter=4, exclude=CR.table_regions(doc))
    aux.meta["render_figures"] = False
    for step in psar.steps(4):
        step(doc, aux)
    text, failed = CR.apply_patches(KEY, render(doc, psar.metadata(doc, 4, aux)))
    body = text.split("\n---\n", 1)[1]
    return doc, aux, text, body, failed


def _table_block(body, caption):
    """(notes, header cells, body rows) of the Markdown table under the heading containing `caption`."""
    lines = body.split("\n")
    i = next(k for k, ln in enumerate(lines) if ln.startswith("#") and caption in ln)
    j = next(k for k in range(i, len(lines)) if lines[k].startswith("| "))
    k = j
    while k < len(lines) and lines[k].startswith("|"):
        k += 1
    notes = [ln for ln in lines[k:k + 8] if ln.startswith("- ") or ln == "Notes:"]
    rows = [[c.strip() for c in ln.strip().strip("|").split("|")] for ln in lines[j:k]]
    return notes, rows[0], rows[2:]


@pytest.mark.refs
def test_headings_are_the_fifteen_numbered_sections(built):
    doc, aux, text, body, failed = built
    assert failed == []
    got = [(m.group(2), len(m.group(1)), m.group(3)) for m in re.finditer(r"^(#{2,6}) (\d+(?:\.\d+)+) (.+)$", body, re.M)
           if not m.group(3).startswith("Table ")]
    assert got == HEADINGS
    assert len(aux.headings) == 15 == sum(1 for e in doc.els if e.kind == "heading" and e.meta.get("numbered"))
    assert doc.meta.get("unmatched_headings", []) == [] and doc.meta.get("unmatched_subheads", []) == []
    assert body.split("\n")[1:4] == ["<!-- page 4 | 4.1-1 -->", "", "# Chapter 4 Integrated Evaluations"]
    assert len(re.findall(r"^# ", body, re.M)) == 1                         # one H1: the chapter title
    assert "\n### References (4.1)\n" in body and "\n### References (4.2)\n" in body


@pytest.mark.refs
def test_table_4_2_2_dose_margin_column(built):
    body = built[3]
    notes, hdr, rows = _table_block(body, "Table 4.2-2")
    assert hdr[0] == "LBE Name" and hdr[-1] == "Mean Dose Margin[d]"
    assert len(hdr) == 8 and len(rows) == 11
    assert [r[-1] for r in rows] == DOSE_MARGIN_D
    assert [r[0] for r in rows][:3] == ["RFH-FDIV-1", "RFH-FDIV-3", "RFH-FDSP-1"]
    assert rows[0][2] == "8.73E-03" and rows[-1][2] == "1.93E-06"           # exponents normalised (D2)
    assert notes[0] == "Notes:"
    assert notes[1:] == ["- [a] Frequency value measured at the LBE mean dose level from the F-C target",
                         "- [b] Ratio of the frequency in Note [a] to the LBE mean frequency (Mean Frequency Margin)",
                         "- [c] Dose value measured at the LBE mean frequency from the F-C target",
                         "- [d] Ratio of the dose in Note [c] to the LBE mean dose (Mean Dose Margin)"]


@pytest.mark.refs
def test_tables_4_2_3_and_4_2_4_two_row_headers_flattened(built):
    """Task 9g: the two-row header becomes 'Parent: Child'; the notes list stays with 4.2-1/4.2-2."""
    body = built[3]
    _, hdr, rows = _table_block(body, "Table 4.2-3")
    assert hdr == ["DBE ID", "Maintain Frequency of all BDBEs < 1E-04/plant-year: DL Function",
                   "Maintain Frequency of all BDBEs < 1E-04/plant-year: Description",
                   "Any single design or operation feature relied upon to meet quantitative objectives for DBE?"]
    assert len(rows) == 5 and rows[0][:2] == ["RFH-FDIV-1", "DL3-RR1"]
    assert all(all(c for c in r) for r in rows)                             # row-spanned DBE ID filled down
    _, hdr, rows = _table_block(body, "Table 4.2-4")
    assert hdr == ["BDBE ID", "Functions to Maintain Individual Risks < QHOs: DL Function",
                   "Functions to Maintain Individual Risks < QHOs: Description",
                   "Any single design or operational feature relied upon?"]
    assert len(rows) == 8 and [r[0] for r in rows] == sorted(r[0] for r in rows)
    notes, hdr, rows = _table_block(body, "Table 4.2-1")
    assert hdr[-1] == "Mean Dose Margin[d]" and len(rows) == 3 and notes[0] == "Notes:" and len(notes) == 5


@pytest.mark.refs
def test_exponents_and_no_residue(built):
    body = built[3]
    assert "shall not exceed 5E-07 per plant-year" in body                  # spec D2 example
    assert "target of 5E-07 per plant-year is satisfied" in body and "2E-06 per plant-year" in body
    assert not re.search(r"\d\s?[x×]\s?10-\d", body) and "x10-" not in body
    assert body.count("E-0") + body.count("E+0") >= 40
    for bad in ("SUBJECT TO DOE", "Kemmerer Unit 1 PSAR\n", "TABLE OF CONTENTS", "LIST OF TABLES", "[[", "<br>", "&amp;"):
        assert bad not in body, bad
    assert not re.search(r"(?:\.\s){4,}", body)                             # no dot leaders


@pytest.mark.refs
def test_page_anchors_cover_every_body_page(built):
    doc, body = built[0], built[3]
    # the p7 anchor is indented: it falls inside the bullet list of section 4.2 (emit.render keeps it in the list)
    anchors = [(int(a), lab) for a, lab in re.findall(r"^ *<!-- page (\d+) \| (\S+) -->$", body, re.M)]
    assert [p for p, _ in anchors] == list(range(4, 17))                    # p1 cover, p2-p3 TOC/LoT dropped
    assert "  <!-- page 7 | 4.2-2 -->" in body
    assert anchors[0] == (4, "4.1-1") and anchors[-1] == (16, "4.2-11")
    assert all(doc.page_labels[p] == lab for p, lab in anchors)


@pytest.mark.refs
def test_verify_is_complete(built):
    """ch4 is the one document the metric can account for entirely: no figure, no withheld section, no merged
    sheet, so `missing_tokens` is 0 of 3,586 (0.00 %) on 2026-09-13. Tolerance +-10 tokens."""
    from refclean.verify import verify
    doc, aux, text = built[0], built[1], built[2]
    res = verify(doc, aux, text)
    s = res["summary"]
    assert s["residue"] == {} and s["pages_with_missing_gt3"] == 0
    assert s["headings_whitelist"] == s["headings_emitted"] == 15
    assert abs(s["missing_tokens"] - 0) <= 10, res["top_missing"]
    assert s["missing_pct"] < 0.3
