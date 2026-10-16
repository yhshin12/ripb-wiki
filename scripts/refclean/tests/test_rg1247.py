"""RG 1.247 profile: hyphen restoration unit check, and one in-memory build of RG_1.247 (Appendix A records)."""
import os
import re
import sys

import pytest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

VAULT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
RAW = os.path.join(VAULT, "references", "raw")
KEY = "RG_1.247"


def test_restore_hyphens_only_where_the_page_breaks_the_line():
    from refclean.profiles.rg1247 import restore_hyphens
    text, n = restore_hyphens("item HRE4 and as-intended-tooperate; HRE40 stays", [("HR", "E4"), ("to", "operate")])
    assert (text, n) == ("item HR-E4 and as-intended-to-operate; HRE40 stays", 2)


@pytest.fixture(scope="module")
def built():
    import clean_references as CR
    from refclean.doc import load_doc
    from refclean.emit import render
    from refclean.pdfaux import build_aux
    from refclean.profiles import DOCS, rg1247
    from refclean.verify import verify
    stem = DOCS[KEY][0]
    if not os.path.exists(os.path.join(RAW, stem + ".json")):
        pytest.skip("RG 1.247 conversion not available")
    doc = load_doc(KEY, stem, CR.RAW, CR.OUT)
    aux = build_aux(doc.pdf_path, chapter=None, exclude=CR.table_regions(doc))
    aux.meta["render_figures"] = False
    for step in rg1247.steps():
        step(doc, aux)
    text, failed = CR.apply_patches(KEY, render(doc, rg1247.metadata(doc, aux)))
    return text, failed, verify(doc, aux, text), doc


@pytest.mark.refs
def test_appendix_a_records(built):
    text, failed, ver, doc = built
    assert failed == []
    body = text.split("\n---\n", 1)[1]
    captions = re.findall(r"^### (Table A-(\d+)\. Staff Position on ASME/ANS RA-S-1\.4-2021, .+)$", body, re.M)
    assert [int(n) for _, n in captions] == list(range(1, 23))
    assert doc.meta["appendix_a_records"] == 1039
    assert "<!-- page 76 | A-6 -->" in body and "<!-- page 82-141" not in body
    rec = body[body.index("#### POS-A8"):]
    assert rec.startswith("#### POS-A8\n- Issue: Operations personnel")
    assert "- Position: Qualification\n- Resolution: For PRAs performed during the pre-operational stage" in rec
    assert ver["summary"]["missing_pct"] <= 0.44, ver["summary"]


@pytest.mark.refs
def test_line_end_hyphens_match_pdf(built):
    text, _, _, _ = built
    for word, n in (("pre-operational", 27), ("risk-significant", 24), ("as-intended-to-operate", 13), ("HR-E4", 2)):
        assert text.count(word) == n, word
    for joined in ("HRE4", "SFRE1", "HSA2", "tooperate", "postinitiator", "plantyear"):
        assert not re.search(rf"\b{joined}\b", text), joined
