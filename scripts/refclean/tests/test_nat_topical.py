"""Approved topical report profile: in-memory builds of NAT-9390-A, NAT-9394-A, NAT-9395-A (public versions)."""
import os
import re
import sys

import pytest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

VAULT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
RAW = os.path.join(VAULT, "references", "raw")
KEYS = ("NAT-9390-A", "NAT-9394-A", "NAT-9395-A")
CACHE = {}


def build(key):
    if key in CACHE:
        return CACHE[key]
    import clean_references as CR
    from refclean.doc import load_doc
    from refclean.emit import render
    from refclean.pdfaux import build_aux
    from refclean.profiles import DOCS, nat_topical
    from refclean.verify import verify
    stem = DOCS[key][0]
    if not os.path.exists(os.path.join(RAW, stem + ".json")):
        pytest.skip(f"{key} conversion not available")
    doc = load_doc(key, stem, CR.RAW, CR.OUT)
    aux = build_aux(doc.pdf_path, chapter=None, exclude=CR.table_regions(doc))
    aux.meta["render_figures"] = False
    for step in nat_topical.steps():
        step(doc, aux)
    text, failed = CR.apply_patches(key, render(doc, nat_topical.metadata(doc, aux)))
    CACHE[key] = (text, failed, verify(doc, aux, text), doc)
    return CACHE[key]


@pytest.mark.refs
@pytest.mark.parametrize("key", KEYS)
def test_two_parts_clean_and_within_the_gate(key):
    text, failed, ver, doc = build(key)
    body = text.split("\n---\n", 1)[1]
    assert body.index("# NRC Safety Evaluation") < body.index("## LIMITATIONS AND CONDITIONS") < body.index("# Topical Report")
    for junk in ("OFFICIAL USE ONLY", "Controlled Document", "SUBJECT TO DOE", "Not Confidential"):
        assert junk not in body
    assert not re.search(r"(?<!`)\[\[", body) and not re.search(r"(?<![\]`])\]\](?![`(])", body)
    assert ver["summary"]["missing_pct"] <= 1.0 and ver["summary"]["residue"] == {} and failed == []


@pytest.mark.refs
def test_se_bracket_text_is_never_public():
    text, failed, ver, doc = build("NAT-9394-A")
    assert doc.meta["se_dropped"] == ["output from GOTHIC, MELCOR, or a manual calculation which feeds"]
    assert "output from GOTHIC, MELCOR" not in text
    assert re.search(r"TerraPower states that the\n\n> \[!withheld\] \(no label\)\n\ninto the system leak rate", text)


@pytest.mark.refs
def test_public_text_between_two_runs_survives():
    text, failed, ver, doc = build("NAT-9394-A")
    assert doc.meta["report_dropped"] == []
    assert "There are no known gaps" in text and "Available experimental data is the historical data" in text


@pytest.mark.refs
def test_figure_sentence_is_not_a_caption_and_emptied_table_keeps_caption():
    text, failed, ver, doc = build("NAT-9395-A")
    assert "The Natrium Type 1 fuel assembly rod parameters are given in Table 5-28." in text   # p.64, was swallowed
    assert "It has approximately" in text
    assert "Table 5-32 Geometric Parameters for Evaluation of Numerical Techniques" in text      # p.198


@pytest.mark.refs
def test_report_assumptions_are_not_headings_but_the_se_sections_are():
    text, failed, ver, doc = build("NAT-9394-A")
    assert not re.search(r"^#+ 3\.2 This report is based", text, re.M)
    assert re.search(r"^#+ 5\.1 In-Vessel Transients with Radiological Release Methodology", text, re.M)
    assert "<!-- page 18 | 9 -->" in text            # SE page label from "- 9 -"
    assert "<!-- page 40 | 12 -->" in text           # report page label from "Page 12 of 65"
    assert re.search(r"^<!-- page 74 \| \d+ -->$", text, re.M)      # landscape sheet: label outside the top band
