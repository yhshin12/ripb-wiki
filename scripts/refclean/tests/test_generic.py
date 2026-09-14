"""Generic profile (core steps only) on RG 1.233: one in-memory build, gate = structure present, verify residual ≤ 2 %."""
import os
import sys

import pytest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

VAULT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
RAW = os.path.join(VAULT, "references", "raw")
KEY = "RG_1.233"


@pytest.fixture(scope="module")
def built():
    import clean_references as CR
    from refclean.doc import load_doc
    from refclean.emit import render
    from refclean.pdfaux import build_aux
    from refclean.profiles import DOCS, generic
    from refclean.verify import verify
    stem = DOCS[KEY][0]
    if not os.path.exists(os.path.join(RAW, stem + ".json")):
        pytest.skip("RG 1.233 conversion not available")
    doc = load_doc(KEY, stem, CR.RAW, CR.OUT)
    aux = build_aux(doc.pdf_path, chapter=None, exclude=CR.table_regions(doc))
    aux.meta["render_figures"] = False
    for step in generic.steps():
        step(doc, aux)
    text, failed = CR.apply_patches(KEY, render(doc, generic.metadata(doc, aux)))
    return doc, aux, text, failed, verify(doc, aux, text)


def test_metadata_and_anchors(built):
    doc, aux, text, failed, ver = built
    assert failed == []
    assert 'doc_id: "RG 1.233"' in text and "pdf_pages: 31" in text
    assert text.count("<!-- page ") >= 25


def test_no_toc_and_headings_present(built):
    _, _, text, _, _ = built
    body = text.split("\n---\n", 1)[1]
    assert ". . . . ." not in body
    for h in ("A. INTRODUCTION", "B. DISCUSSION", "C. STAFF REGULATORY GUIDANCE", "D. IMPLEMENTATION"):
        assert any(line.lstrip("# ").strip().upper().startswith(h) for line in body.splitlines() if line.startswith("#")), h


def test_verify_residual_within_gate(built):
    _, _, _, _, ver = built
    assert ver["summary"]["missing_pct"] <= 2.0, ver["summary"]


@pytest.fixture(scope="module")
def built_acrs():
    import clean_references as CR
    from refclean.doc import load_doc
    from refclean.emit import render
    from refclean.pdfaux import build_aux
    from refclean.profiles import DOCS, generic
    from refclean.verify import verify
    key = "ACRS_ML25293A458"
    stem = DOCS[key][0]
    if not os.path.exists(os.path.join(RAW, stem + ".json")):
        pytest.skip("ACRS conversion not available")
    doc = load_doc(key, stem, CR.RAW, CR.OUT)
    aux = build_aux(doc.pdf_path, chapter=None, exclude=CR.table_regions(doc))
    aux.meta["render_figures"] = False
    for step in generic.steps():
        step(doc, aux)
    text, failed = CR.apply_patches(key, render(doc, generic.metadata(doc, aux)))
    return text, failed, verify(doc, aux, text)


def test_acrs_deck(built_acrs):
    text, failed, ver = built_acrs
    assert failed == []
    assert 'doc_id: "ML25293A458"' in text and "pdf_pages: 22" in text
    assert text.count("<!-- page ") >= 20          # one anchor per slide that carries text (a blank/cover slide may have none)
    assert "Control of Heat Generation" in text
    assert ver["summary"]["missing_pct"] <= 2.0, ver["summary"]
