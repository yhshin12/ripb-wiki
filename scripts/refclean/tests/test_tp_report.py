"""TerraPower technical report profile: one in-memory build of TP-LIC-RPT-0011 (public version, redaction brackets)."""
import os
import re
import sys

import pytest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

VAULT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
RAW = os.path.join(VAULT, "references", "raw")
KEY = "TP-LIC-RPT-0011"


@pytest.fixture(scope="module")
def built():
    import clean_references as CR
    from refclean.doc import load_doc
    from refclean.emit import render
    from refclean.pdfaux import build_aux
    from refclean.profiles import DOCS, tp_report
    from refclean.verify import verify
    stem = DOCS[KEY][0]
    if not os.path.exists(os.path.join(RAW, stem + ".json")):
        pytest.skip("TP-LIC-RPT-0011 conversion not available")
    doc = load_doc(KEY, stem, CR.RAW, CR.OUT)
    aux = build_aux(doc.pdf_path, chapter=None, exclude=CR.table_regions(doc))
    aux.meta["render_figures"] = False
    for step in tp_report.steps():
        step(doc, aux)
    text, failed = CR.apply_patches(KEY, render(doc, tp_report.metadata(doc, aux)))
    return text, failed, verify(doc, aux, text), doc, aux


@pytest.mark.refs
def test_page_furniture_dropped_and_labels_from_running_header(built):
    text, failed, ver, doc, aux = built
    body = text.split("\n---\n", 1)[1]
    assert "Not Confidential" not in body and "Controlled Document" not in body
    assert "SUBJECT TO DOE" not in body and "| TP-LIC-RPT-0011 Rev 0 |" not in body
    assert "<!-- page 51 | 50 -->" in body and "<!-- page 2 | 1 -->" in body
    assert "- Document Number: | TP-LIC-RPT-0011 | Revision: | 0" in body     # p.2 control table, from the PDF


@pytest.mark.refs
def test_numbered_headings_including_chapters_and_withheld_titles(built):
    text, failed, ver, doc, aux = built
    heads = re.findall(r"^(#{1,6}) (\d(?:\.\d+)*)(?: (.*))?$", text, re.M)
    nums = [n for _, n, _ in heads]
    assert ("#", "1", "INTRODUCTION") in heads and ("####", "4.1.2.4", "Hot Channel Factors") in heads
    assert ("####", "3.2.1.4", "Hot Channel Factors") in heads and ("###", "8.1.16", "Hot Channel Factors") in heads
    assert ("###", "3.1.1", "") in heads                       # '3.1.1 [[': the title is withheld
    assert len(nums) == len(set(nums)) == 89
    assert ver["summary"]["headings_whitelist"] == ver["summary"]["headings_emitted"] == 89


@pytest.mark.refs
def test_redaction_brackets_become_callouts(built):
    text, failed, ver, doc, aux = built
    body = text.split("\n---\n", 1)[1]
    assert "[[" not in text and "]]" not in body
    hcf = body[body.index("#### 4.1.2.4 Hot Channel Factors"):body.index("#### 4.1.2.5")]
    assert "> [!withheld] (a)(4),ECI" in hcf and "##### Figure 4-1 Example relative temperature" in hcf
    # public text after a closing bracket stays
    assert re.search(r"### 4\.1\.3 Fuel Performance\n\n> \[!withheld\] \(a\)\(4\),ECI\n\nFurther discussion is provided "
                     r"in Section 6\.4", body)
    assert "10 CFR 50.34(a)(4)" in body                         # not a bracket label


@pytest.mark.refs
def test_only_figure_4_2_is_public(built):
    text, failed, ver, doc, aux = built
    assert [r.num for r in aux.figures if not r.withheld] == ["4-2"] and len(aux.figures) == 29
    assert "![Figure 4-2 Example deformation shapes" in text
    after = text[text.index("![Figure 4-2"):]
    assert "Due to the heterogenous geometry of the core" in after.split("### 4.2.1", 1)[0]
    assert ver["summary"]["missing_pct"] <= 0.3 and failed == []


@pytest.fixture(scope="module")
def built_nat():
    import clean_references as CR
    from refclean.doc import load_doc
    from refclean.emit import render
    from refclean.pdfaux import build_aux
    from refclean.profiles import DOCS, tp_report
    from refclean.verify import verify
    stem = DOCS["NAT-3049"][0]
    if not os.path.exists(os.path.join(RAW, stem + ".json")):
        pytest.skip("NAT-3049 conversion not available")
    doc = load_doc("NAT-3049", stem, CR.RAW, CR.OUT)
    aux = build_aux(doc.pdf_path, chapter=None, exclude=CR.table_regions(doc))
    aux.meta["render_figures"] = False
    for step in tp_report.steps():
        step(doc, aux)
    text, failed = CR.apply_patches("NAT-3049", render(doc, tp_report.metadata(doc, aux)))
    return text, failed, verify(doc, aux, text)


@pytest.mark.refs
def test_white_paper_letter_legend_control_table_and_captions(built_nat):
    text, failed, ver = built_nat
    body = text.split("\n---\n", 1)[1]
    # the letter explains the marks: they stay as text (code spans), not callouts
    assert "identified using `[[ ]]`(a)(4), `[[ ]]`(ECI), or `[[ ]]`(a)(4),(ECI)." in body
    assert "- Natrium Document No.: NAT-3049 | Rev. No.: 0A | Page: 1 of 21" in body and "<!-- page 6 | 1 -->" in body
    assert "## 3.4 Relationship Between the Nascent Model and Hot Channel Factors\n\n> [!withheld] (a)(4)\n" in body
    # a caption glued to the next body line is cut after the caption read from the PDF
    assert "### Figure 1 Natrium Type 1 Assembly Sketch\n\n> [!withheld] (a)(4)(ECI)\n" in body
    assert '[2] J. Muraoka, R. E. Peterson, R. G. Brown, W. D. Yule, D. S. Dutt, and J. E. Hanson, “Assessment of FFTF Hot Channel Factors”' in body
    assert ver["summary"]["missing_pct"] <= 0.5 and ver["summary"]["residue"] == {} and failed == []
