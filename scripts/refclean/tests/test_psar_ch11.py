"""PSAR ch11 (Conduct of Operations) profile: unit tests on synthetic elements + checks of the real build
against the PDF (review_ch11 §1, §4, §5)."""
import collections
import contextlib
import io
import os
import re
import sys

import pytest

HERE = os.path.dirname(os.path.abspath(__file__))
SCRIPTS = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, SCRIPTS)

from refclean.doc import Doc, El  # noqa: E402
from refclean.profiles import psar_ch11 as P  # noqa: E402

VAULT = os.path.dirname(SCRIPTS)
RAW = os.path.join(VAULT, "references", "raw")
STEM = "TP_Natrium_PSAR2025_ch11_Conduct of Operations"
PDF = os.path.join(RAW, STEM + ".pdf")
TOKEN = re.compile(r"[A-Za-z0-9]+(?:[.\-][A-Za-z0-9]+)*")


def _doc(els):
    return Doc("PSAR_ch11", STEM, RAW, VAULT, 77, {}, els)


# ------------------------------------------------------------------ units ----
def test_cell_text_separators():
    assert P.cell_text(["Variables include:", "• a", "• b", "The PHT is described in Section 7.1.3."]) == \
        "Variables include:; • a; • b; The PHT is described in Section 7.1.3."
    assert P.cell_text(["HF in Concept Design: identification of scenarios for analysis",
                        "HF in Preliminary Design: participation"]) == \
        "HF in Concept Design: identification of scenarios for analysis; HF in Preliminary Design: participation"
    assert P.cell_text(["Sentence one.", "Sentence two."]) == "Sentence one. Sentence two."
    assert P.cell_text(["Verification", "Validation"]) == "Verification; Validation"


def test_drop_noise_and_list_markers():
    d = _doc([El("para", "LIST OF TABLES", 4), El("para", ".", 67), El("para", "Body text.", 67),
              El("item", "- Emergency Response Performance – x", 52, level=1),
              El("para", "● Federal resources are available.", 55)])
    P.drop_noise(d)
    P.list_markers(d)
    assert [(e.kind, e.text) for e in d.els] == [
        ("para", "Body text."), ("item", "Emergency Response Performance – x"),
        ("item", "Federal resources are available.")]


def test_section_number_cells():
    from refclean.tables import Cell, Table
    t = Table(grid=[[Cell("Section #", 0, 0)], [Cell("11.2.6.1\n11.2.6.2\n11.2.6.3", 1, 0)],
                    [Cell("Procedures,\nTraining,\nVerification and Validation", 2, 0)]])
    d = _doc([El("table", "", 46, table=t)])
    P.section_number_cells(d)
    assert t.grid[1][0].text == "11.2.6.1; 11.2.6.2; 11.2.6.3"      # enumeration of section numbers
    assert t.grid[2][0].text == "Procedures,\nTraining,\nVerification and Validation"   # wrapped text untouched
    assert d.meta["ch11_qa"]["section_number_cells"] == 1


def test_split_glued_references():
    d = _doc([El("para", "One CRA may be manipulated to support testing. References", 66),
              El("para", "11.5-1 U.S. NRC, DANU-ISG-2022-08, “Advanced Reactor …,” March 2024.", 66)])
    P.split_glued_references(d)
    assert [(e.kind, e.text) for e in d.els] == [
        ("para", "One CRA may be manipulated to support testing."), ("heading", "References"),
        ("item", "11.5-1 U.S. NRC, DANU-ISG-2022-08, “Advanced Reactor …,” March 2024.")]
    assert d.els[1].meta.get("keep_heading")


# ------------------------------------------------------------ real build ----
pytestmark_real = pytest.mark.skipif(not os.path.exists(PDF), reason="raw ch11 input not present")


@pytest.fixture(scope="module")
def built():
    import clean_references as C
    from refclean.emit import render
    from refclean.pdfaux import build_aux
    from refclean.doc import load_doc
    from refclean.profiles import psar
    stem, _, chapter = C.DOCS["PSAR_ch11"]
    doc = load_doc("PSAR_ch11", stem, C.RAW, C.OUT)
    aux = build_aux(doc.pdf_path, chapter=chapter, exclude=C.table_regions(doc))
    aux.meta["render_figures"] = False
    for st in psar.steps(chapter):
        st(doc, aux)
    text = render(doc, psar.metadata(doc, chapter, aux))
    text, failed = C.apply_patches("PSAR_ch11", text)
    return doc, aux, text, failed


def _body(text):
    return text.split("\n---\n", 1)[1]


def _table_after(text, caption):
    lines = text.split("\n")
    i = next(k for k, ln in enumerate(lines) if ln.startswith("#") and caption in ln)
    j = i + 1
    while not lines[j].startswith("|"):
        j += 1
    rows = []
    while j < len(lines) and lines[j].startswith("|"):
        rows.append(lines[j])
        j += 1
    return rows


def _pdf_words(pages, clip_table=False, body=True):
    import fitz
    from refclean.pdfaux import header_footer_band
    out = []
    pdf = fitz.open(PDF)
    for pno in pages:
        page = pdf[pno - 1]
        rect = None
        if clip_table:
            with contextlib.redirect_stdout(io.StringIO()):
                rect = fitz.Rect(page.find_tables().tables[0].bbox)
        top, bot = header_footer_band(page)
        for w in page.get_text("words", sort=not clip_table):     # table cells: content-stream (cell) order
            c = fitz.Point((w[0] + w[2]) / 2, (w[1] + w[3]) / 2)
            if rect is not None and not rect.contains(c):
                continue
            if body and not clip_table and not top <= c.y <= bot:
                continue
            out.append(w[4])
    pdf.close()
    return out


def _toks(s):
    s = re.sub(r"(?<=[a-z])-\s+(?=[a-z])", "-", s)      # PDF line-end hyphen: 'post-' 'construction)'
    return collections.Counter(t.lower() for t in TOKEN.findall(s))


REVIEW_HEADINGS = """11.1 11.1.1 11.1.1.1 11.1.1.2 11.1.1.3 11.1.1.4 11.1.1.5 11.1.2 11.1.2.1 11.1.2.2 11.1.2.3 11.1.2.4
11.1.2.5 11.1.3 11.1.3.1 11.1.3.2 11.1.3.3 11.1.4 11.1.4.1 11.1.4.1.1 11.1.4.1.2 11.1.4.1.3 11.1.4.1.4 11.1.4.1.5
11.1.4.1.6 11.1.4.2 11.1.4.2.1 11.1.4.3 11.1.4.4 11.1.4.4.1 11.1.4.4.2 11.1.4.4.3 11.1.5 11.1.5.1 11.1.5.2 11.1.5.3
11.2 11.2.1 11.2.1.1 11.2.1.2 11.2.1.3 11.2.1.4 11.2.1.5 11.2.1.6 11.2.1.7 11.2.1.7.1 11.2.1.7.2 11.2.1.7.3 11.2.1.8
11.2.1.9 11.2.1.10 11.2.1.11 11.2.1.12 11.2.1.13 11.2.1.14 11.2.1.15 11.2.1.16 11.2.2 11.2.2.1 11.2.2.2 11.2.2.2.1
11.2.2.2.2 11.2.2.2.3 11.2.2.2.4 11.2.2.2.5 11.2.2.3 11.2.3 11.2.3.1 11.2.3.2 11.2.3.3 11.2.4 11.2.4.1 11.2.4.1.1
11.2.4.1.2 11.2.4.1.3 11.2.5 11.2.6 11.2.6.1 11.2.6.2 11.2.6.2.1 11.2.6.2.2 11.2.6.2.3 11.2.6.3 11.2.6.4 11.2.7
11.2.7.1 11.2.7.2 11.2.7.3 11.3 11.3.1 11.3.2 11.3.2.1 11.3.2.2 11.3.3 11.3.3.1 11.3.3.2 11.3.4 11.3.4.1 11.3.4.2 11.3.5
11.3.5.1 11.3.5.2 11.3.6 11.3.6.1 11.3.6.2 11.3.6.3 11.3.7 11.3.8 11.3.9 11.3.9.1 11.3.9.2 11.3.9.2.1 11.3.9.2.2
11.3.9.2.3 11.3.9.3 11.3.10 11.4 11.5 11.5.1 11.5.2 11.5.2.1 11.5.2.2 11.5.2.3 11.5.2.4 11.6 11.6.1 11.6.2""".split()


@pytestmark_real
def test_no_warnings_no_failed_patches(built):
    doc, _, _, failed = built
    assert doc.meta.get("ch11_warnings") is None
    assert failed == []
    assert doc.meta.get("unmatched_headings") == []
    assert doc.meta["ch11_qa"] == {"section_number_cells": 1, "paragraph_splits": 8, "numbered_headings": 127,
                                   "11.2-2_rows": 19, "11.5-1_rows": 14,
                                   "withheld": ["11.4 Aircraft Impact Assessment (PDF p60-64, SRI)"]}


@pytestmark_real
def test_withheld_section_once_with_frontmatter_range(built):
    doc, _, text, _ = built
    assert text.count("> [!withheld] SRI — This information is withheld in accordance with 10 CFR 2.390.") == 1
    assert "\n## 11.4 Aircraft Impact Assessment\n\n> [!withheld] SRI" in text
    assert doc.meta["withheld"] == ["11.4 Aircraft Impact Assessment (PDF p60-64, SRI)"]
    # the recorded range is exactly the set of PDF pages that print the marker
    _, aux, _, _ = built
    pages = sorted(p for p, lines in aux.meta["lines_by_page"].items()
                   if any("This information is withheld" in ln.text for ln in lines))
    assert pages == [60, 61, 62, 63, 64]


@pytestmark_real
def test_merged_tables_get_a_page_range_anchor(built):
    _, _, text, _ = built
    assert "<!-- page 47-50 | 11.2-29..11.2-32 -->" in text          # Table 11.2-2, 4 sheets
    assert "<!-- page 67-73 | 11.5-3..11.5-9 -->" in text            # Table 11.5-1, 7 sheets


@pytestmark_real
def test_all_127_numbered_headings_in_order_with_levels(built):
    _, _, text, _ = built
    found = re.findall(r"^(#+) (11(?:\.\d+)+) \S", text, re.M)
    assert [n for _, n in found] == REVIEW_HEADINGS
    assert all(len(h) == len(n.split(".")) for h, n in found)


@pytestmark_real
def test_unnumbered_headings(built):
    _, _, text, _ = built
    for h in ["#### Objectives and Scope", "#### Methodology", "##### Design Changes",
              "#### Geography and Demography", "#### Nearby Industrial, Transportation, and Military Facilities",
              "#### Meteorology and Meteorological Dispersion", "#### Hydrology",
              "#### Geology, Seismology, and Geotechnical", "# Chapter 11 Conduct of Operations"]:
        assert text.count("\n" + h + "\n") == 1, h
    refs = re.findall(r"^### References \((11\.\d)\)$", text, re.M)
    assert refs == ["11.1", "11.2", "11.3", "11.5", "11.6"]
    # glued forms are gone
    assert "support testing. References" not in text and "security operations. References" not in text
    assert "\n## 11.4 Aircraft Impact Assessment\n\n> [!withheld] SRI — This information is withheld" in text


@pytestmark_real
def test_residue_and_markers(built):
    _, _, text, _ = built
    body = _body(text)
    assert not re.search(r"^#+ \.\s*$", body, re.M)
    assert "LIST OF TABLES" not in body and "LIST OF FIGURES" not in body
    assert not re.search(r"^\s*- \d{1,2}\. ", body, re.M)      # '- 1. …' double markers
    assert not re.search(r"^\s*- - ", body, re.M)
    assert "●" not in body and "&gt;" not in body and "&amp;" not in body and "[[" not in body
    assert "| 3 | Shutdown | No more than one CRA coupled to CRDM driveline | N/A | > 400 °F (204°C) |" in body


@pytestmark_real
def test_false_list_items_are_not_items(built):
    _, _, text, _ = built
    starts = ["Section 11.1.3.1 through", "Section 11.1.4.1 through", "Section 11.2.1 provides", "Section 5.4 of",
              "Section 11.2.2 through", "Section 11.2.6.4)", "Section 11.2.7).", "As in other industries",
              "At the end of the development stage", "10 CFR 50.160 and the guidance", "Mode-1 is entered",
              "Mode-2 is entered", "downpower when", "The purpose of Mode-3", "The purpose of Mode-4",
              "Section 2.5.3.2.5 provides", "Section 2.5.4.6 contains"]
    for s in starts:
        assert not re.search(r"^\s*- " + re.escape(s), text, re.M), s


@pytestmark_real
def test_numbered_list_11_2_1_4(built):
    _, _, text, _ = built
    for n in range(1, 13):
        assert re.search(rf"^{n}\. \S", text, re.M), n
    assert "\n   - The approach used in conducting the HSI design" in text
    assert "\n   <!-- page 24 | 11.2-6 -->\n" in text
    assert "\n    Verification is the process of determining" in text
    assert "\n    - Control area and equipment layout" in text
    assert "\n    <!-- page 25 | 11.2-7 -->\n" in text
    assert text.count("<!-- page 25 | 11.2-7 -->") == 1
    assert "\n12. Human Performance Monitoring – Continuous monitoring" in text


@pytestmark_real
def test_paragraph_splits_from_pdf(built):
    doc, _, text, _ = built
    assert doc.meta.get("ch11_para_splits") == 8
    sec = text.split("## 11.3 Emergency Preparedness\n", 1)[1].split("\n### 11.3.1 ", 1)[0]
    paras = [p for p in sec.strip().split("\n\n") if p and not p.startswith("<!--")]
    assert [p.split()[0:2] for p in paras] == [["This", "section"], ["A", "performance-based"],
                                               ["The", "emergency"], ["A", "preliminary"]]
    assert "\n\nThe key elements of the emergency preparedness plan to meet 10 CFR 50.160 will include:" in text
    assert "\n\nAs described in Section 5.2.1, the SR functions are the probabilistic" in text
    assert "\n\nSince safety-significant structures are designed to be able" in text
    assert "\n\nSection 2.5.1 describes the different types" in text
    assert "\n\nApplicable state and local government certified all hazards plans" in text
    # a sentence-internal repeat of a paragraph opening is not a boundary (p7, 11.1.1.2)
    assert "described in Chapter 2. The executive responsible for project execution is responsible for coordination" in text
    long_lines = [ln[:60] for ln in _body(text).split("\n") if not ln.startswith("|") and len(ln) > 2000]
    assert long_lines == []


@pytestmark_real
def test_operating_mode_definitions_match_pdf_word_by_word(built):
    _, _, text, _ = built
    words = _pdf_words([65, 66])
    i = next(k for k, w in enumerate(words) if w == "11.5.2.1" and words[k + 1] == "Mode-1:")
    j = words.index("References")
    pdf_seq = words[i:j]
    sec = text.split("#### 11.5.2.1 ", 1)[1].split("### References (11.5)", 1)[0]
    sec = "11.5.2.1 " + sec
    out_seq = [w for w in re.sub(r"<!--.*?-->|^#+ ", " ", sec, flags=re.M).split()]
    assert out_seq == pdf_seq


@pytestmark_real
def test_table_11_5_2_matches_pdf(built):
    _, _, text, _ = built
    rows = _table_after(text, "Table 11.5-2 Operating Modes")
    assert rows[2:] == [
        "| 1 | High Power Operation | More than one CRA coupled to CRDM driveline | NSS<sup>(1)</sup> | N/A |",
        "| 2 | Low Power Operation | More than one CRA coupled to CRDM driveline | IAC<sup>(2)</sup> | N/A |",
        "| 3 | Shutdown | No more than one CRA coupled to CRDM driveline | N/A | > 400 °F (204°C) |",
        "| 4 | Refuel | No more than one CRA coupled to CRDM driveline | N/A | ≤ 400 °F (204°C) |"]
    notes = text.split("| 4 | Refuel |", 1)[1].split("<!-- page 75", 1)[0]
    pdf = _pdf_words([74])
    k = pdf.index("(1)", pdf.index("N/A"))
    note_seq = [w for w in pdf[pdf.index("The", k) - 1:]]
    out_seq = re.sub(r"^.*?\n\n", "", notes, count=1, flags=re.S).replace("<sup>", "").replace("</sup>", "")
    out_seq = [w for w in out_seq.split() if w != "-"]
    assert out_seq == note_seq


@pytestmark_real
def test_table_11_5_1_rebuilt_against_pdf(built):
    _, _, text, _ = built
    rows = _table_after(text, "Table 11.5-1 ")
    secs = [r.split("|")[1].strip() for r in rows[2:]]
    assert secs == ["1.0", "2.0", "2.1", "2.2", "3.0", "3.1", "3.2", "3.3", "3.4", "3.5", "3.6", "3.7", "4.0", "5.0"]
    r50 = rows[-1]
    assert r50 == ("| 5.0 |  | Administrative Controls are the provisions relating to organization and management, "
                   "procedures, record keeping, review and audit, and reporting necessary to assure operation of the "
                   "facility in a safe manner. The administrative controls to be included in the technical "
                   "specifications will be provided at the OL stage. Probable administrative controls include:; "
                   "• delineation of responsibility; • description of organization; • unit staff qualifications; "
                   "• requirements for procedures; • programs and manuals, to include a setpoint control program "
                   "consistent with Option B of TSTF-493; • reporting requirements, to include a COLR |  |")
    assert "| 1.0 | Use and Application | The Use and Application section" in text
    assert "• PSP leakage; The PHT is described in Section 7.1.3." in text
    assert "• intake/exhaust flow rates; The RAC is described in Section 7.2.1." in text
    assert "• reactor trip switchgear; The RPS, XIS, and RIS are described in Section 7.6." in text
    # every word of the 7 sheets exactly once (sheet headers once), independent extractor (PyMuPDF words)
    pdf = _toks(" ".join(_pdf_words(range(67, 74), clip_table=True)))
    header = _toks("Section Section Name Variable or Condition Basis")
    for _ in range(6):
        pdf -= header
    assert _toks("\n".join(rows[:1] + rows[2:])) == pdf


@pytestmark_real
def test_table_11_2_2_rebuilt_against_pdf(built):
    _, _, text, _ = built
    rows = _table_after(text, "Table 11.2-2 ")
    secs = [r.split("|")[1].strip() for r in rows[2:]]
    assert secs == ["11.2.1", "11.2.2", "11.2.3", "11.2.3.1", "11.2.2.2", "11.2.4", "11.2.3.3", "11.2.4.1",
                    "11.2.5", "11.2.1.10", "11.2.5", "11.2.5", "11.2.5", "11.2.5", "11.2.6.1", "11.2.6.2",
                    "11.2.6.3", "11.2.6.4", "11.2.7"]
    assert "| 11.2.1.10 | Design Goals and Design Bases | Design human-machine interface system; " \
           "design physical working environment |  |" in text
    assert "identification of scenarios for analysis; HF in Preliminary Design: participation" in text
    assert "| Verification; Validation |" in text
    pdf = _toks(" ".join(_pdf_words(range(47, 51), clip_table=True)))
    header = _toks("SECTION CONTENT NUREG-0711 DEVELOPMENT OF HFE REVIEW GUIDANCE FOR ADVANCED REACTORS")
    for _ in range(3):
        pdf -= header
    pdf += _toks("Design human-machine interface system; design physical working environment")   # fill-down
    assert _toks("\n".join(rows[:1] + rows[2:])) == pdf


@pytestmark_real
def test_table_11_2_1_core_render_matches_pdf(built):
    _, _, text, _ = built
    rows = _table_after(text, "Table 11.2-1 ")
    assert len(rows) == 15
    assert "| 11 | Human Factors Verification and Validation | Procedures, Training, Verification and Validation " \
           "| 11.2.6.1; 11.2.6.2; 11.2.6.3 |" in rows
    assert _toks("\n".join(rows)) == _toks(" ".join(_pdf_words([46], clip_table=True)))


@pytestmark_real
def test_do_not_fix_source_typos_kept(built):
    _, _, text, _ = built
    for s in ["Natrium Human Factors Engineering Program Plant and Methodologies",
              "non-safety-related with special treatment (NRSRT) functions", "Section 2.3.3 Based upon",
              "responsibilities.The", "through designated channels. for problems",
              "| 11.2.2.2 | Allocation of Function |", "Organization- TerraPower/USO"]:
        assert s in text, s


def test_verify_residual_is_pinned(built):
    """The accepted PDF-vs-output residual, 168 of 20,417 tokens (0.82 %) on 2026-09-13.

    Composition: the box labels of the three organisation charts, Figures 11.1-2/-3/-4 (p15, p17, p18: 114 tokens
    such as 'manager' 22x and 'director' 7x) — transcription of a raster org chart is a class C item the ledger
    parks — and the withheld sentence of section 11.4, printed on each of p62-p64 but emitted once as the
    `> [!withheld]` callout (27 tokens). Tolerance +-10 tokens: a larger change means prose left the output.
    """
    from refclean.verify import verify
    doc, aux, text, _failed = built
    res = verify(doc, aux, text)
    s = res["summary"]
    assert s["residue"] == {}
    assert s["headings_whitelist"] == s["headings_emitted"] == 127
    assert abs(s["missing_tokens"] - 168) <= 10, s["missing_tokens"]
    assert s["missing_pct"] < 1.0
    assert set(res["pages_missing"]) <= {15, 17, 18, 62, 63, 64}
    assert doc.meta.get("ch11_warnings", []) == []
    assert [w for k, v in doc.meta.items() if k.endswith("_warnings") for w in v] == []
