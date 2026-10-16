"""SER profile: one in-memory build of SER_KU1_CP (headings for all chapters, page labels, bracket closers)."""
import os
import re
import sys

import pytest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

VAULT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
RAW = os.path.join(VAULT, "references", "raw")
KEY = "SER_KU1_CP"


@pytest.fixture(scope="module")
def built():
    import clean_references as CR
    from refclean.doc import load_doc
    from refclean.emit import render
    from refclean.pdfaux import build_aux
    from refclean.profiles import DOCS, ser
    from refclean.verify import verify
    stem = DOCS[KEY][0]
    if not os.path.exists(os.path.join(RAW, stem + ".json")):
        pytest.skip("SER conversion not available")
    doc = load_doc(KEY, stem, CR.RAW, CR.OUT)
    aux = build_aux(doc.pdf_path, chapter=None, exclude=CR.table_regions(doc))
    aux.meta["render_figures"] = False
    for step in ser.steps():
        step(doc, aux)
    text, failed = CR.apply_patches(KEY, render(doc, ser.metadata(doc, aux)))
    return text, failed, verify(doc, aux, text), doc


@pytest.mark.refs
def test_ser_structure(built):
    text, failed, ver, doc = built
    assert failed == []
    body = text.split("\n---\n", 1)[1]
    assert "<!-- page 152 | 3-1 -->" in body
    for h in ("## 3.1 Probabilistic Risk Assessment", "### 3.2.1 Technical Evaluation",
              "#### 3.3.1.7 Major Accident Analysis", "## 3.4 Licensing Basis Event Summary"):
        assert re.search(rf"^{re.escape(h)}$", body, re.M), h
    assert not re.search(r"^#+ \]\]", body, re.M)
    assert ver["summary"]["missing_pct"] <= 0.32, ver["summary"]
    assert ver["summary"]["headings_emitted"] >= 881, ver["summary"]
