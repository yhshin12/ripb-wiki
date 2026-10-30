"""TerraPower presentation package profile: one in-memory build of TP-LIC-LET-0080 (letter and two public slide decks)."""
import os
import sys

import pytest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

VAULT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
RAW = os.path.join(VAULT, "references", "raw")
KEY = "TP-LIC-LET-0080"


def test_despace_closes_letter_spacing_only():
    from refclean.profiles.tp_slides import despace
    assert despace("1 . 0 2 0") == "1.020" and despace("E B R -I I") == "EBR-II" and despace("- - 2 σ") == "--2σ"
    assert despace("O v erall") == "Overall" and despace("N atrium") == "Natrium"
    assert despace("Type 1") == "Type 1" and despace("FFTF-SAR *") == "FFTF-SAR *"


@pytest.fixture(scope="module")
def built():
    import clean_references as CR
    from refclean.doc import load_doc
    from refclean.emit import render
    from refclean.pdfaux import build_aux
    from refclean.profiles import DOCS, tp_slides
    from refclean.verify import verify
    stem = DOCS[KEY][0]
    if not os.path.exists(os.path.join(RAW, stem + ".json")):
        pytest.skip("TP-LIC-LET-0080 conversion not available")
    doc = load_doc(KEY, stem, CR.RAW, CR.OUT, tp_slides.FLATTEN_TEXT_BLOCKS)
    aux = build_aux(doc.pdf_path, chapter=None, exclude=CR.table_regions(doc))
    aux.meta["render_figures"] = False
    for step in tp_slides.steps():
        step(doc, aux)
    text, failed = CR.apply_patches(KEY, render(doc, tp_slides.metadata(doc, aux)))
    return text, failed, verify(doc, aux, text)


@pytest.mark.refs
def test_hot_channel_factor_slides(built):
    text, failed, ver = built
    body = text.split("\n---\n", 1)[1]
    assert "SUBJECT TO DOE" not in body and "Copyright" not in body
    assert "<!-- page 54 | 33 -->\n\n## Coolant HCF Comparison" in body
    assert ("| Direct combination | `[[ ]]`(a)(4) | 1.020 | 1.071 | 1.221 | `[[ ]]`(a)(4) |\n"
            "| Statistical combination --2σ | `[[ ]]`(a)(4) | 1.089 | 1.087 | 1.067 | `[[ ]]`(a)(4) |\n"
            "| Overall combined --2σ | `[[ ]]`(a)(4) | 1.111 | 1.164 | 1.302 | `[[ ]]`(a)(4) |") in body
    p55 = body[body.index("<!-- page 55 | 34 -->"):body.index("<!-- page 56 | 35 -->")]
    assert "To compute the “2-sigma” inner cladding temperature:" in p55
    assert "<!-- source: equations transcribed to LaTeX from the slide image -->" in p55 and r"\frac{2}{3}" in p55
    assert "\U0001D447" not in p55                                # no doubled math-italic glyphs left
    assert "## Hot Channel Factor Overview\n\n> [!withheld] (a)(4)\n" in body       # lone opener -> callout
    assert "- Thermal hydraulic uncertainties" in body and "identified using `[[ ]]`(a)(4), `[[ ]]`ECI" in body
    assert failed == [] and ver["summary"]["missing_pct"] <= 1.0 and ver["summary"]["residue"] == {}
