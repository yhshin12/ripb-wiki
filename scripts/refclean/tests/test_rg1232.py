"""RG 1.232 profile: unit tests for the text rules + one build of the real document.

The build takes about 3 s (133 PDF pages) and runs once per test session.
"""
import os
import re
import sys

import pytest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from refclean.doc import load_doc  # noqa: E402
from refclean.emit import page_label_ranges, render  # noqa: E402
from refclean.pdfaux import build_aux  # noqa: E402
from refclean.profiles import rg1232 as P  # noqa: E402

VAULT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
RAW = os.path.join(VAULT, "references", "raw")
OUT = os.path.join(VAULT, "references")
STEM = "RG_1.232"


# ------------------------------------------------------------------ unit tests (no PDF) ----
@pytest.mark.parametrize("inp,out", [
    ("Refer to SFRDC 17 concerning", "Refer to SFR-DC 17 concerning"),
    ("Refer to SFRDC17 concerning", "Refer to SFR-DC17 concerning"),          # source spelling: no space
    ("requirements of SFRDC 34 and SFR-DC 35", "requirements of SFR-DC 34 and SFR-DC 35"),
    ("with MHTGRDC 15 (helium", "with MHTGR-DC 15 (helium"),
    ("SRM-SECY-15-002 - SECY-150002 -", "SRM-SECY-15-002 - SECY-15-0002 -"),
    ("GDC 26. SECY94-084, Policy", "GDC 26. SECY-94-084, Policy"),
    ("NUREG-0968 (Ref. 5) and NUREG1368", "NUREG-0968 (Ref. 5) and NUREG-1368"),
    ("https://www.gen4.org/gif/upload", "https://www.gen-4.org/gif/upload"),
    ("2015-06-29-07-03-NPTDSmexico/2-3-", "2015-06-29-07-03-NPTDS-mexico/2-3-"),
    ("applicants developing nonLWR designs", "applicants developing non-LWR designs"),
    ("Criteria for NonLight Water Reactors", "Criteria for Non-Light Water Reactors"),
    ("previous NRC preapplication reviews", "previous NRC pre-application reviews"),
    ("concepts: sodiumcooled fast reactors", "concepts: sodium-cooled fast reactors"),
    ("non-LWR technologiesspecifically, to", "non-LWR technologies\u2014specifically, to"),
    ("large height-todiameter ratio", "large height-to-diameter ratio"),
    ("recirculation of lossof-coolant accident", "recirculation of loss-of-coolant accident"),
    # source spellings that must stay (review section 5.4)
    ("criteria for watercooled nuclear power plants", "criteria for watercooled nuclear power plants"),
    ("Noncombustible and fire- resistant materials", "Noncombustible and fire- resistant materials"),
    ("NUREG-1338, Draft Preapplication Safety", "NUREG-1338, Draft Preapplication Safety"),
])
def test_restore_hyphens(inp, out):
    assert P.restore_hyphens(inp) == out


def test_redline_md():
    runs = [["Reactor ", False, 0x000000], ["helium", False, P.BLUE], [" ", False, 0],
            ["coolant", False, P.RED], [" pressure boundary.", False, 0x000000]]
    assert P.redline_md(runs) == "Reactor <ins>helium</ins> ~~coolant~~ pressure boundary."
    assert P.strip_redline(P.redline_md(runs)) == "Reactor helium coolant pressure boundary."
    # a blue insertion glued to the preceding word; red words split over two spans
    runs = [["Reactivity control system", False, 0], ["s ", False, P.BLUE],
            ["redundancy and ", False, P.RED], ["capacity", False, P.RED]]
    assert P.redline_md(runs) == "Reactivity control system<ins>s</ins> ~~redundancy and capacity~~"


def _frag(page, paras, lead=False, trail=False):
    return {"page": page, "paras": [[[t, False, 0]] for t in paras], "lead": lead, "trail": trail,
            "title": None, "emphasis": False, "odl": ""}


def _plain(p, emph):
    return P.ws(P.plain(p))


def test_merge_fragments_boundaries():
    # mid-sentence page break -> one paragraph, joined with a single space
    got = P.merge_fragments([_frag(65, ["the prompt inherent nuclear"]), _frag(66, ["feedback characteristics"])],
                            _plain)
    assert got == [(65, "the prompt inherent nuclear feedback characteristics")]
    # empty source line at the top of the continuation cell -> paragraph boundary
    got = P.merge_fragments([_frag(64, ["basis for the piping."]), _frag(65, ["Chemical consequences"], lead=True)],
                            _plain)
    assert got == [(64, "basis for the piping."), (65, "Chemical consequences")]
    # a numbered list entry always starts a new paragraph
    got = P.merge_fragments([_frag(74, ["postulated accident."]), _frag(75, ["(4) A means for holding"])], _plain)
    assert len(got) == 2
    # line-end hyphen at the page break: joined without a space
    got = P.merge_fragments([_frag(81, ["Refer to SFR-"]), _frag(82, ["DC 34 and"])], _plain)
    assert got == [(81, "Refer to SFR-DC 34 and")]


def test_md_safe():
    assert P.md_safe("10. CFR text") == "10\\. CFR text"
    assert P.md_safe("- not a list") == "\\- not a list"
    assert P.md_safe("(1) appropriate periodic inspection") == "(1) appropriate periodic inspection"


# ------------------------------------------------------------------- built document ----
@pytest.fixture(scope="session")
def built():
    doc = load_doc(STEM, STEM, RAW, OUT)
    aux = build_aux(doc.pdf_path, chapter=None)
    for step in P.steps():
        step(doc, aux)
    meta = P.metadata(doc, aux)
    meta["page_labels"] = page_label_ranges(doc.page_labels)
    return doc, aux, render(doc, meta)


def _records(text):
    """{'SFR-DC 4': {title, fields, text, rationale}} parsed back out of the rendered Markdown."""
    recs, cur, sub = {}, None, "fields"
    for line in text.split("\n"):
        m = re.match(r"^#### ((?:ARDC|SFR-DC|MHTGR-DC) \d{1,2}) \u2014 (.+)$", line)
        if m:
            cur = {"title": m.group(2), "fields": "", "text": "", "rationale": ""}
            recs[m.group(1)] = cur
            sub = "fields"
            continue
        if re.match(r"^#{1,4} ", line):
            cur = None
            continue
        if cur is None:
            continue
        if line.startswith("##### "):
            sub = "text" if line == "##### Criterion text" else "rationale"
            continue
        if line.startswith("<!-- page "):
            continue
        cur[sub] += line + "\n"
    return recs


def test_counts_and_nonempty(built):
    _doc, _aux, text = built
    recs = _records(text)
    assert len(recs) == 178
    for cset, n in (("ARDC", 55), ("SFR-DC", 65), ("MHTGR-DC", 58)):
        assert sum(1 for k in recs if k.startswith(cset + " ")) == n
    for key, r in recs.items():
        assert r["text"].strip(), f"{key}: empty criterion text"
        assert r["rationale"].strip(), f"{key}: empty rationale block"
        assert re.search(r"^- \*\*Status:\*\* \S", r["fields"], re.M), f"{key}: no status field"
        assert f"- **ID:** {key} ^" in r["fields"]
    assert text.count("##### Criterion text") == 178
    assert sum(1 for r in recs.values() if r["rationale"].strip() == "(none in source)") == 41


def test_sfr_dc_4_chemical_consequences(built):
    _doc, _aux, text = built
    r = _records(text)["SFR-DC 4"]
    assert r["title"] == "Environmental and dynamic effects design bases"
    assert "Modified for SFR-DC" in r["fields"]
    body = r["text"]
    assert body.count("Chemical consequences of accidents, such as sodium leakage, shall be appropriately "
                      "considered for the design of structures, systems, and components important to safety, "
                      "which must be protected.") == 1
    # the page-65 fragment is a paragraph of its own, not glued to the end of the previous one
    assert "for the piping. Chemical consequences" not in body
    paras = [p for p in body.split("\n\n") if p.strip() and not p.strip().startswith("<!--")]
    assert len(paras) >= 2


def test_sfr_dc_11_sentence_continuous(built):
    _doc, _aux, text = built
    r = _records(text)["SFR-DC 11"]
    assert ("the net effect of the prompt inherent nuclear feedback characteristics tends to compensate for a "
            "rapid increase in reactivity." in r["text"])


def test_footnotes(built):
    _doc, _aux, text = built
    assert "10 CFR 50.34[^2] states" in text
    for n in range(1, 15):
        assert text.count(f"[^{n}]") == 2, n
        assert re.search(r"^\[\^%d\]: \S" % n, text, re.M)
    for bad in ("10 CFR 50.342", "PDC4.", "REFERENCES7", "available.3", "(Ref. 2)1."):
        assert bad not in text


def test_crosswalk_table(built):
    _doc, _aux, text = built
    assert "#### TABLE 1: NON-LIGHT-WATER-REACTOR CROSSWALK" in text
    head = ("| Section | Criterion | GDC title | ARDC title | ARDC status | SFR-DC title | SFR-DC status | "
            "MHTGR-DC title | MHTGR-DC status |")
    assert text.count(head) == 1
    block = text.split(head, 1)[1].split("\n\n", 1)[0].strip().split("\n")
    rows = [r for r in block if r.startswith("| ")]
    assert len(rows) == 65
    row14 = next(r for r in rows if r.split("|")[2].strip() == "14")
    cells = [c.strip() for c in row14.strip("|").split("|")]
    assert cells[3] == "Reactor coolant ~~pressure~~ boundary."
    assert cells[4] == "Modified for ARDC"
    assert cells[5] == "<ins>Primary</ins> coolant ~~pressure~~ boundary."
    assert cells[7] == "Reactor <ins>helium</ins> ~~coolant~~ pressure boundary."
    assert ("| Inspection of <ins>passive</ins> ~~emergency core cooling~~ <ins>residual heat removal</ins> "
            "system. | Modified for MHTGR-DC |") in text
    assert "~~Combined reactivity control systems capability~~ | DELETED and incorporated into ARDC 26" in text


def test_heading_tree(built):
    _doc, _aux, text = built
    heads = [ln for ln in text.split("\n") if re.match(r"^#{1,6} ", ln)]
    assert heads.count("# GUIDANCE FOR DEVELOPING PRINCIPAL DESIGN CRITERIA FOR NON-LIGHT-WATER REACTORS") == 1
    assert sum(1 for h in heads if re.match(r"^# [^#]", h)) == 1
    h2 = [h for h in heads if re.match(r"^## [^#]", h)]
    assert h2 == ["## A. INTRODUCTION", "## B. DISCUSSION", "## C. STAFF REGULATORY GUIDANCE",
                  "## D. IMPLEMENTATION", "## ACRONYMS/ABBREVIATIONS", "## REFERENCES[^7]",
                  "## Appendix A. Advanced Reactor Design Criteria",
                  "## Appendix B. Sodium-Cooled Fast Reactor Design Criteria",
                  "## Appendix C. Modular High-Temperature Gas-Cooled Reactor Design Criteria",
                  "## Document information"]
    assert heads.index("## A. INTRODUCTION") < heads.index("### Purpose")            # reading-order swap fixed
    assert heads.index("## B. DISCUSSION") < heads.index("### Reason for Issuance")  # reading-order swap fixed
    assert heads.index("### Background") < heads.index("#### The NRC Regulatory Framework")
    assert "#### NRC Policy on Advanced Reactors" in heads                            # buried heading extracted
    assert "#### Key Assumptions and Clarifications Regarding the non-LWR Design Criteria" in heads
    assert "### Appendix B \u2014 Section I. Overall Requirements" in heads
    assert sum(1 for h in heads if re.match(r"^### Appendix [ABC] \u2014 Section ", h)) == 20


def test_acronyms_references_and_emphasis(built):
    _doc, _aux, text = built
    acr = text.split("| Acronym | Definition |", 1)[1].split("\n\n", 1)[0].strip().split("\n")
    assert len([r for r in acr if r.startswith("| ")]) == 42
    assert "| TRISO | tristructural isotropic fuel |" in text
    assert ("| FAUNA | Forschungsanlage zur Untersuchung nuklearer Aerosole (Research Facility for Investigating"
            " Nuclear Aerosols) |") in text
    assert len(re.findall(r"^\d{1,2}\. .* \^ref-\d{1,2}$", text, re.M)) == 39
    for n in (1, 17, 39):
        assert re.search(r"^%d\. .* \^ref-%d$" % (n, n), text, re.M)
    # D7: GDC 19 rationale "(with emphasis added)" italics, in all three appendices
    assert text.count("*actions can be taken* to operate the nuclear power unit *safely*") == 3
    assert text.count("*have certain knowledge*") == 3 and text.count("*make decisions*") == 3


def test_residue_and_frontmatter(built):
    _doc, _aux, text = built
    fm = text.split("---\n", 2)[1]
    assert 'doc_id: "RG 1.232"' in fm and 'revision: "0"' in fm and 'issue_date: "2018-04"' in fm
    assert 'adams_accession: "ML17325A611"' in fm and "page_label_notes:" in fm
    assert "p105 printed B-2" in fm
    for bad in ("Appendix B to RG 1.232, Rev. 0, Page B-2",   # Appendix C page-footer residue (F18)
                "TABLE OF CONTENTS", ". . . .", "&amp;", "[[", "<br>"):
        assert bad not in text
    assert "## Document information" in text and "under ADAMS Accession Number (No.) ML17325A611" in text


def test_hyphens_in_output(built):
    _doc, _aux, text = built
    for good in ("requirements of SFR-DC 34 and SFR-DC 35", "Refer to SFR-DC17 concerning", "SECY-15-0002", "www.gen-4.org", "INL/EXT-10-17997", "non-LWR",
                 "technologies\u2014specifically"):
        assert good in text, good
    body = re.sub(r"^- \*\*Aliases:\*\* .*$", "", text, flags=re.M)   # vault alias 'SFRDC n' is intentional
    for bad in ("SFRDC 34", "SFRDC17", "MHTGRDC", "SECY-150002", "gen4.org", "nonLWR", "NUREG1368"):
        assert bad not in body, bad
    # source spellings kept (review section 5.4)
    for keep in ("watercooled", "fire- resistant", "SFR-DC17", "(Criterion 1 \u2013 15)", "SFR-DFC", "SARRDLS",
                 "August 2017 2017", "Section VII\u2014Additional SFR-DC (Criteria 70\u201377)"):
        assert keep in text, keep


def test_hyphen_list_has_pdf_evidence(built):
    """Every HYPHEN_RESTORE entry must correspond to a line-end 'A-' + 'B' pair found in the PDF."""
    _doc, aux, _text = built
    joined = {k.replace("-", "").replace(".", "") for k in aux.hyphen_map}
    for pat, _rep in P.HYPHEN_RESTORE:
        key = re.sub(r"\\b|\(\?=.*|\\\.|\\", "", pat).replace("-", "")
        assert any(key in j or j in key for j in joined), pat


def test_computed_qa_is_clean(built):
    """The profile cross-checks every criterion, Table 1 cell and acronym row against the PDF text layer and the
    ODL JSON; the resulting warning list must be empty (it is printed under `warnings` in the build report)."""
    doc, _aux, _text = built
    assert doc.meta["rg_warnings"] == []
    assert doc.meta["rg_stats"]["hyphen_joins_unlisted"] == {}
    qa = doc.meta["rg_qa"]
    assert qa["pdf_vs_json_diffs"] == 0 and qa["hyphen_joins_unlisted"] == 0
    assert (qa["criteria"], qa["appendix_A"], qa["appendix_B"], qa["appendix_C"]) == (178, 55, 65, 58)
    assert (qa["table1_rows"], qa["table1_redline_cells"], qa["acronyms"], qa["references"]) == (65, 29, 42, 39)


def test_verify_residual_is_pinned(built):
    """The accepted PDF-vs-output residual, 337 of 45,533 tokens (0.74 %) on 2026-09-13.

    Composition: the column header of the appendix criterion tables ('… Title and Content', 'Rationale'), repeated
    on each of the 105 appendix pages but printed once in the record format of D6 ('content' alone is 113 tokens),
    the Table 1 header row ('Non-LWR', 'Current DC', 'Multiple Barriers', the roman numeral section heads) repeated
    on its 52 pages, and `SFR-DC17`-style tokens the PDF splits over a line end. No criterion, rationale or cell
    text is missing (test_counts_and_nonempty and the record tests cover those). Tolerance +-10 tokens.
    """
    from refclean.verify import verify
    doc, aux, text = built
    res = verify(doc, aux, text)
    s = res["summary"]
    assert s["residue"] == {}
    assert abs(s["missing_tokens"] - 337) <= 10, s["missing_tokens"]
    assert s["missing_pct"] < 0.8
    missing = dict(res["top_missing"])
    assert missing["content"] == 113                      # the repeated appendix column header
    assert not any(k.startswith("criterion") for k in missing)
