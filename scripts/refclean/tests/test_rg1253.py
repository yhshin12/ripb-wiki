"""RG 1.253 profile: one in-memory build of RG_1.253 (Appendix A Tables A-2 and A-3 rebuilt per sheet)."""
import os
import re
import sys

import pytest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

VAULT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
RAW = os.path.join(VAULT, "references", "raw")
KEY = "RG_1.253"


@pytest.fixture(scope="module")
def built():
    import clean_references as CR
    from refclean.doc import load_doc
    from refclean.emit import render
    from refclean.pdfaux import build_aux
    from refclean.profiles import DOCS, rg1253
    from refclean.verify import verify
    stem = DOCS[KEY][0]
    if not os.path.exists(os.path.join(RAW, stem + ".json")):
        pytest.skip("RG 1.253 conversion not available")
    doc = load_doc(KEY, stem, CR.RAW, CR.OUT)
    aux = build_aux(doc.pdf_path, chapter=None, exclude=CR.table_regions(doc))
    aux.meta["render_figures"] = False
    for step in rg1253.steps():
        step(doc, aux)
    text, failed = CR.apply_patches(KEY, render(doc, rg1253.metadata(doc, aux)))
    return text, failed, verify(doc, aux, text), doc


@pytest.mark.refs
def test_column_tables_one_table_per_sheet_with_every_requirement(built):
    import fitz
    text, failed, ver, doc = built
    assert failed == [] and doc.meta["column_tables_unparsed"] == []
    assert [(t["table"], t["page"]) for t in doc.meta["column_tables"]] == \
        [("A-2", p) for p in range(39, 43)] + [("A-3", p) for p in range(43, 49)]
    rows = re.findall(r"^\| (C\.1\.3\.\d+ \([A-Z]+\)) \| (HLR-[A-Z]+-[A-Z]) \| ([A-Z]+-[A-Z]\d+) \| (Yes|CC-I|CC-II) \|$",
                      text, re.M)
    pdf = fitz.open(doc.pdf_path)
    ids = [w[4] for p in range(38, 48) for w in pdf[p].get_text("words") if re.fullmatch(r"[A-Z]+-[A-Z]\d+", w[4])]
    assert sorted(r[2] for r in rows) == sorted(ids) and len(ids) == 1155
    assert all(h.split("-")[1] == sr.split("-")[0] and h[-1] == sr.split("-")[1][0] for _, h, sr, _ in rows)
    # carried across a column and a sheet: column 3 of p.39 opens with ES-C9 under HLR-ES-C; p.40 with SY-B16
    assert "| C.1.3.3 (ES) | HLR-ES-C | ES-C9 | CC-II |" in text
    p40 = text[text.index("<!-- page 40 -->"):]
    assert p40.split("| Entry |\n|---|---|---|---|\n", 1)[1].startswith("| C.1.3.5 (SY) | HLR-SY-B | SY-B16 | Yes |")
    # the sheet 6 caption starts at the foot of p.47
    p48 = text[text.index("<!-- page 48 -->"):]
    assert p48.split("\n")[2].startswith("## Table A-3. Non-LWR CP Applications Based on the LMP Methodology: ")
    assert "<!-- source: the caption's first line is printed at the foot of p.47 -->" in p48
    assert ver["summary"]["missing_pct"] <= 0.2
