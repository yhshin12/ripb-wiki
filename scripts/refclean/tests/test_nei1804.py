"""NEI 18-04 profile: synthetic unit tests + one smoke build of the real document.

Acceptance items come from meta/references_cleanup/file_reviews/review_nei.md (§1 findings, §2 table log with the
correct matrices, §3 figure inventory, §4 outline, §5.2 rules R1-R9, §5.3 do-not-fix list).
"""
import os
import re
import sys

import pytest

SCRIPTS = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, SCRIPTS)
from refclean.doc import Doc, El  # noqa: E402
from refclean.pdfaux import Aux  # noqa: E402
from refclean.profiles import nei1804 as P  # noqa: E402
from refclean.tables import Cell, Table  # noqa: E402

VAULT = os.path.dirname(SCRIPTS)
RAW = os.path.join(VAULT, "references", "raw")
KEY = "NEI_18-04"
STEM = "NEI_18-04_Modernization of Technical Requirements for Licensing of Advanced Non-Light Water Reactors"


def _doc(els, n_pages=95):
    return Doc(KEY, "x", RAW, VAULT, n_pages, {}, els)


def _tab(rows, header_rows=1, page=1):
    grid = [[Cell(x, i, j) for j, x in enumerate(r)] for i, r in enumerate(rows)]
    return Table(grid=grid, header_rows=header_rows, page=page, pages=[page])


# ------------------------------------------------------------------ units ----
def test_prefix_end_ignores_punctuation_and_case():
    assert P._prefix_end("1 INTRODUCTION", P._key("1 Introduction")) == len("1 INTRODUCTION")
    assert P._prefix_end("3.2.1 Frequency-Consequence Evaluation Criteria",
                         P._key("3.2.1 Frequency-Consequence Evaluation Criteria")) is not None
    assert P._prefix_end("4.2 Definition of X", P._key("4.2.1 Safety-Significant SSCs")) is None


def test_match_heading_start_glued_and_trailing_bracket():
    # glued body text after the heading (review F12: '5.1 ... According to the NRC glossary, ...')
    e = El("item", "5.1 Defense-in-Depth Philosophy According to the NRC glossary, defense-in-depth is:", 56)
    kind, pos = P._match_heading(e, P._key("5.1 Defense-in-Depth Philosophy"))
    assert (kind, e.text[:pos].strip()) == ("start", "5.1 Defense-in-Depth Philosophy")
    # a heading ending with a closing bracket ('Task 5a: ... (RSFs)') must match to its end
    e2 = El("heading", "Task 5a: Identify Required Safety Functions (RSFs)", 21)
    assert P._match_heading(e2, P._key("Task 5a: Identify Required Safety Functions (RSFs)")) == \
        ("start", len(e2.text))
    # subheading glued to the end of the preceding paragraph (review F15, p58)
    e3 = El("para", "These capabilities, when combined, create layers-of-defense responses to plant challenges. "
                    "Programmatic Defense-in-Depth", 58)
    kind, pos = P._match_heading(e3, P._key("Programmatic Defense-in-Depth"))
    assert (kind, e3.text[pos:]) == ("end", "Programmatic Defense-in-Depth")
    # a lower-case continuation after the candidate is not a heading boundary
    e4 = El("para", "Task 5: Perform PRA is described below", 64)
    assert P._match_heading(e4, P._key("Task 5: Perform PRA")) is None


def test_split_at_starts_splits_glued_items_only_at_known_starts():
    starts = ["Plant Simulation and Modeling of LBEs", "State of Knowledge", "Margin to Performance-Based Targets"]
    assert P._split_at_starts("Plant Simulation and Modeling of LBEs State of Knowledge", starts) == \
        ["Plant Simulation and Modeling of LBEs", "State of Knowledge"]
    assert P._split_at_starts("Magnitude and Sources of Uncertainties", starts) == \
        ["Magnitude and Sources of Uncertainties"]


def test_list_table_fills_attribute_and_splits_rowspan_shift():
    # struct-tree shift (review R5b): items 2..n of a row-spanned attribute land in column 1 of the next rows
    t = _tab([["Attribute", "Evaluation Focus"],
              ["Layers of Defense", "Multiple Layers of Defense"],
              ["Extent of Layer Functional Independence", ""],
              ["Functional Barriers", ""],
              ["Emergency Planning", "Periodic drills\nEmergency response equipment maintenance programs"]])
    out = P.list_table(t, 70, [70])
    assert [P._texts(out, r) for r in range(out.n_rows)] == [
        ["Attribute", "Evaluation Focus"],
        ["Layers of Defense", "Multiple Layers of Defense"],
        ["Layers of Defense", "Extent of Layer Functional Independence"],
        ["Layers of Defense", "Functional Barriers"],
        ["Emergency Planning", "Periodic drills"],
        ["Emergency Planning", "Emergency response equipment maintenance programs"]]


def test_group_table_moves_group_rows_into_a_column_and_drops_repeated_headers():
    t = _tab([["LMP Term", "Acronym", "Definition"],
              ["Terms Associated with Functions", "", ""],
              ["PRA Safety Function", "PSF", "Reactor design specific SSC functions"],
              ["LMP Term", "Acronym", "Definition"],
              ["Terms Associated with Licensing Basis Events", "", ""],
              ["Licensing Basis Event", "LBE", "The entire collection of event sequences"]])
    out = P.group_table(t, "Category", 90, [90, 91])
    assert [P._texts(out, r) for r in range(out.n_rows)] == [
        ["Category", "LMP Term", "Acronym", "Definition"],
        ["Terms Associated with Functions", "PRA Safety Function", "PSF", "Reactor design specific SSC functions"],
        ["Terms Associated with Licensing Basis Events", "Licensing Basis Event", "LBE",
         "The entire collection of event sequences"]]


def test_render_table_join_modes():
    t = P._table([["A", "B"], ["x", "one\ntwo"]], 1, 1, [1], join="; ")
    assert P._render_table(t).splitlines()[-1] == "| x | one; two |"
    t2 = P._table([["A", "B"], ["x", "one\ntwo"]], 1, 1, [1])
    assert P._render_table(t2).splitlines()[-1] == "| x | one two |"


def test_join_breaks_keeps_line_end_hyphen_and_protects_lists():
    d = _doc([El("para", "all non-", 21), El("para", "safety-related SSCs that perform", 22)])
    P.join_breaks(d)
    assert [e.text for e in d.els] == ["all non-safety-related SSCs that perform"]
    # where-list items start with a lower-case symbol and must not be merged (review F11)
    d2 = _doc([El("item", "PPSSC,j = Probability of passive SSCs along sequence j", 73, meta={"where_item": True}),
               El("item", "rPB,j = Release fraction from the coolant pressure boundary", 73,
                  meta={"where_item": True})])
    P.join_breaks(d2)
    assert len(d2.els) == 2
    # a bulleted item never merges into the previous one
    d3 = _doc([El("item", "• first item without a full stop", 10), El("item", "• second item", 10)])
    P.join_breaks(d3)
    assert len(d3.els) == 2


def test_lists_levels_glyphs_false_items_and_inline_sub_item():
    els = [El("item", "• Safety-Related:", 38, (90.0, 0, 500.0, 10)),
           El("item", "o SSCs selected by the designer", 38, (108.0, 0, 500.0, 10)),
           El("item", " Risk margins are sufficient.", 84, (126.0, 0, 500.0, 10)),
           El("item", "As explained more fully in the sections on PRA development", 60, (72.0, 0, 500.0, 10)),
           El("item", "• Non-Safety-Related with No Special Treatment (NST): o All other SSCs", 38,
              (90.0, 0, 500.0, 10)),
           El("para", "• The Initiating Events (IEs) and event sequences", 32, (90.0, 0, 500.0, 10))]
    d = _doc(els)
    P.lists(d)
    got = [(e.kind, e.level, e.text) for e in d.els]
    assert got[0] == ("item", 0, "Safety-Related:")
    assert got[1] == ("item", 1, "SSCs selected by the designer")
    assert got[2] == ("item", 2, "Risk margins are sufficient.")
    assert got[3][0] == "para"                      # false list item at the body margin (review F28)
    assert got[4] == ("item", 0, "Non-Safety-Related with No Special Treatment (NST):")
    assert got[5] == ("item", 1, "All other SSCs")
    assert got[6][0] == "item"                      # bullet paragraph promoted to a list item (review F35)


def test_ordered_lists_group_numbered_items():
    d = _doc([El("item", "1. Mitigate DBEs within the F-C Target", 48, (90.0, 0, 500.0, 10)),
              El("item", "2. Prevent any high-consequence BDBEs", 48, (90.0, 0, 500.0, 10))])
    P.ordered_lists(d)
    assert [(e.kind, e.text) for e in d.els] == [
        ("raw_md", "1. Mitigate DBEs within the F-C Target\n2. Prevent any high-consequence BDBEs")]


def test_footnotes_reference_definition_and_ignore_bold_caption():
    body = El("para", "* Note that these upper tier regulations contain requirements.", 10,
              (72.0, 72.0, 535.0, 100.0), "Calibri", 9.0)
    els = [El("para", "**Figure 5-2. Framework for Establishing DID Adequacy**", 10, meta={"figure_caption": "5-2"}),
           El("para", "requirements, including but not limited to the following:*", 10),
           body,
           El("heading", "2 LICENSING BASIS DEVELOPMENT PROCESS", 11, meta={"numbered": True})]
    d = _doc(els)
    P.footnotes(d)
    texts = [e.text for e in d.els]
    assert "requirements, including but not limited to the following:[^p10]" in texts
    assert "[^p10]: Note that these upper tier regulations contain requirements." in texts
    assert texts.index("[^p10]: Note that these upper tier regulations contain requirements.") == \
        texts.index("2 LICENSING BASIS DEVELOPMENT PROCESS") - 1
    assert texts[0].endswith("Adequacy**")            # the '**' of a bold caption is not a footnote marker


@pytest.mark.refs
def test_metadata_keys():
    d = _doc([])
    d.meta["cover"] = {"title": "T", "series": "S"}
    m = P.metadata(d, Aux())
    assert m["doc_id"] == "NEI 18-04" and m["revision"] == "1" and m["date"] == "2019-08"
    assert m["adams"] == "ML19241A472" and m["docket"] == "PROJ0689"
    assert "PDF page - 8" in m["page_label_offset"]


# ------------------------------------------------------------------ smoke ----
@pytest.fixture(scope="module")
def built():
    if not os.path.exists(os.path.join(RAW, STEM + ".structtree.json")):
        pytest.skip("raw NEI 18-04 conversions not present")
    import clean_references as CR
    from refclean.doc import load_doc
    from refclean.emit import render
    from refclean.pdfaux import build_aux
    doc = load_doc(KEY, STEM, CR.RAW, CR.OUT)
    aux = build_aux(doc.pdf_path, chapter=None, exclude=CR.table_regions(doc))
    aux.meta["render_figures"] = False
    for st in P.steps():
        st(doc, aux)
    text, failed = CR.apply_patches(KEY, render(doc, P.metadata(doc, aux)))
    return doc, aux, text, failed


def _table_rows(text, caption):
    seg = text[text.index("**" + caption):]
    block = seg.split("\n\n")[1]
    return [ln for ln in block.split("\n") if ln.startswith("| ")]


@pytest.mark.refs
def test_smoke_patches_apply_and_no_residue(built):
    doc, aux, text, failed = built
    assert failed == []
    for pat in ("<br", "&amp;", "&lt;", "&gt;", "[[", "THIS PAGE INTENTIONALLY BLANK", "nei.org",
                "SEE TABLES FOLLOWING PAGES", ". . . ."):
        assert pat not in text, pat
    assert "\U0001d445\U0001d445" not in text and "\U0001d465\U0001d465" not in text   # corrupted Cambria Math


@pytest.mark.refs
def test_smoke_heading_tree(built):
    doc, aux, text, failed = built
    assert doc.meta["unmatched_headings"] == [] and doc.meta["unmatched_subheads"] == []
    numbered = [e for e in doc.els if e.kind == "heading" and e.meta.get("numbered")]
    subs = [e for e in doc.els if e.kind == "heading" and e.meta.get("sub")]
    assert len(numbered) == 55 and len(subs) == 68          # review §4: outline 55 + BoldItalic 68
    assert {e.level for e in numbered} == {2, 3, 4}
    assert text.count("\n# ") == 1                          # one H1 (document title)
    assert "\n## 1 INTRODUCTION\n" in text and "\n### 1.1 Purpose\n" in text
    assert "\n#### 4.2.1 Safety-Significant SSCs\n" in text  # review F12: was a list item
    assert "\n##### Task 5a: Identify Required Safety Functions (RSFs)\n" in text
    assert "\n#### Task 18: DID Adequacy Established; Document/Update DID Baseline Evaluation\n" in text
    # glued headings split from their body text (review F12/F15)
    assert "\n### 5.1 Defense-in-Depth Philosophy\n\nAccording to the NRC glossary" in text
    assert "\n##### Purpose of Special Treatment\n\nThe purpose of special treatment" in text


@pytest.mark.refs
def test_smoke_frontmatter_and_page_labels(built):
    doc, aux, text, failed = built
    head = text.split("---\n")[1]
    for line in ('doc_id: "NEI 18-04"', 'revision: "1"', 'date: "2019-08"', 'adams: "ML19241A472"',
                 'docket: "PROJ0689"', "pdf_pages: 95"):
        assert line in head, line
    assert doc.page_labels[9] == "1" and doc.page_labels[95] == "87" and doc.page_labels[2] == "ii"
    assert doc.meta["page_label_mismatch"] == {}
    assert "<!-- page 9 | 1 -->" in text
    assert head.count('  - "Table ') == 13 and head.count('  - "Figure ') == 11


@pytest.mark.refs
def test_smoke_sign_lost_exponents_and_notation(built):
    doc, aux, text, failed = built
    # review F01 (H): the three sign-lost exponents, restored from PDF line-end evidence
    assert doc.meta["sign_lost_evidence"] == {14: [("1", "4")], 16: [("", "2")], 47: [("", "2")]}
    assert "1×104" not in text and "102/plant-year" not in text
    assert "mean frequencies of 1E-04/plant-year to 1E-02/plant-year are classified as DBEs" in text
    assert "frequencies between 1E-04 to 1E-02/plant-year" in text
    assert "with the SSC failed is greater than 1E-02/plant-year" in text
    assert not re.search(r"10-\d", text) and not re.search(r"[×x]1E-", text)
    assert len(re.findall(r"\dE[+-]\d\d", text)) == 50


@pytest.mark.refs
def test_smoke_identifiers_and_source_typos(built):
    doc, aux, text, failed = built
    for broken in ("NEI-0004", "ASME/ANS-Ra-S-1.42013", "RIPBDM", "TIRIPB", "defense-indepth", "Defense-inDepth",
                   "risksignificant", "performancebased", "SafetyRelated"):
        assert broken not in text, broken
    for good in ("NEI-00-04", "ASME/ANS-Ra-S-1.4-2013", "RIPB-DM", "TI-RIPB", "defense-in-depth"):
        assert good in text, good
    # review §5.3: source typos are preserved
    for typo in ("industry consensus stan ", "The total mean -frequency", "radionuclide release s associated",
                 "complimentary", "threating", "5E-07/plant year"):
        assert typo in text, typo


@pytest.mark.refs
def test_smoke_table_4_1(built):
    doc, aux, text, failed = built
    rows = _table_rows(text, "Table 4-1.")
    assert len(rows) == 20                                   # header + 19 data rows (review §2)
    assert rows[0].startswith("| Group | Special Treatment Category | Applicability<sup>1</sup>: SR SSC |")
    assert sum(r.count("√") for r in rows) == 26
    risc2 = next(r for r in rows if "RISC-2 SSCs" in r and "RISC-1" not in r)
    cells = [c.strip() for c in risc2.strip().strip("|").split("|")]
    assert cells[2] == "" and cells[3] == "√" and cells[4] == ""   # check mark belongs to NSRST (review F04)
    assert "| Additional Special Treatment Requirements | Technical Specifications | √ | <sup>2</sup> |" in text
    for n in range(1, 6):
        assert "- <sup>%d</sup> " % n in text


@pytest.mark.refs
def test_smoke_table_5_2_rowspans_filled(built):
    doc, aux, text, failed = built
    rows = _table_rows(text, "Table 5-2.")
    assert len(rows) == 6 and rows[0].count("|") == 6
    layer5 = next(r for r in rows if r.startswith("| 5)"))
    assert "Maintain individual risks from all LBEs < QHOs with sufficient<sup>[d]</sup> margins" in layer5
    assert "No single barrier<sup>[c]</sup> or plant feature relied upon" in layer5
    assert "Meet F-C Target for all LBEs and cumulative risk metric targets" in layer5
    layer1 = next(r for r in rows if r.startswith("| 1)"))
    assert layer1.count("Maintain frequency of plant transients") == 2   # colspan filled into both columns
    assert "Maintain frequency of all DBEs < 1E-02/plant-year" in text
    for n in "abcd":
        assert "- [%s] " % n in text


@pytest.mark.refs
def test_smoke_list_tables_and_matrices(built):
    doc, aux, text, failed = built
    assert len(_table_rows(text, "Table 5-3.")) == 14        # 4 attributes x 13 focus items
    assert len(_table_rows(text, "Table 5-5.")) == 8         # 3 attributes x 7 focus items
    assert len(_table_rows(text, "Table 5-7.")) == 33        # 10 programs x 32 elements
    assert len(_table_rows(text, "Table 5-8.")) == 10
    assert "| Knowledge Level | Plant Simulation and Modeling of LBEs |" in text
    assert "| Knowledge Level | State of Knowledge |" in text          # glued struct-tree cell split
    r59 = _table_rows(text, "Table 5-9.")
    assert r59[0].startswith("| LBE IE Series Name | Functional: Margin Adequacy |")
    assert "Physical: No Single Feature Relied Upon" in r59[0]
    assert sum(r.count("√") for r in r59[1:]) == 21
    r510 = _table_rows(text, "Table 5-10.")
    assert "Compensation for Uncertainties: Mechanical Failures" in r510[0]
    assert sum(r.count("√") for r in r510[1:]) == 23
    assert len(_table_rows(text, "Table 5-4.")) == 8         # two sheets merged, repeated header dropped
    assert len(_table_rows(text, "Table 5-6.")) == 7         # Group column, both pages, 6 focus rows


@pytest.mark.refs
def test_smoke_acronyms_and_glossary(built):
    doc, aux, text, failed = built
    acr = text[text.index("## LIST OF ACRONYMS"):text.index("<!-- page 9 |")]
    rows = [ln for ln in acr.split("\n") if ln.startswith("| ")]
    assert len(rows) == 54                                   # header + 53 acronyms (IDP/IDPP split)
    assert "| IDP | Integrated Decision-Making Process |" in acr
    assert "| IDPP | Integrated Decision-Making Process Panel |" in acr
    assert "\\* These terms have special meanings" in acr     # line-leading '*' escaped for Obsidian
    gl = text[text.index("## 6 GLOSSARY OF TERMS"):]
    grows = [ln for ln in gl.split("\n") if ln.startswith("| ")]
    assert len(grows) == 36                                  # header + 35 terms, group rows became a column
    assert grows[0].startswith("| Category | LMP Term | Acronym | Definition | Source |")
    assert gl.count("| Terms Associated with Functions |") == 7
    assert "| Terms Associated with Probabilistic Risk Assessment | Mechanistic Source Term | MST |" in gl


@pytest.mark.refs
def test_smoke_formulas_and_where_list(built):
    doc, aux, text, failed = built
    assert "| Fussell-Vesely | FV | [R(base) − R(x<sub>i</sub> = 0)] / R(base) |" in text
    assert ("| Partial Derivative | PD | [R(x<sub>i</sub> + ∂x<sub>i</sub>) − R(x<sub>i</sub>)] / "
            "∂x<sub>i</sub> |") in text
    assert ("R<sub>j</sub> = Q × F<sub>IE,j</sub> × P<sub>ASSC,j</sub> × P<sub>PSSC,j</sub> × "
            "r<sub>fuel,j</sub> × r<sub>PB,j</sub> × r<sub>cont,j</sub>") in text
    where = text[text.index("\nwhere:\n"):text.index("The above model was developed")]
    assert len([ln for ln in where.split("\n") if ln.startswith("- ")]) == 8
    assert "- F<sub>IE,j</sub> = Frequency of the Initiating Event" in where
    assert "the term x<sub>i</sub> represents the probability" in text     # subscript restored from PDF spans


@pytest.mark.refs
def test_smoke_footnotes(built):
    doc, aux, text, failed = built
    labels = sorted(set(re.findall(r"\[\^(p\d+b?)\]", text)))
    assert len(labels) == 16 and doc.meta["footnotes_unreferenced"] == []
    for lab in labels:
        assert text.count("[^%s]" % lab) == 2                # one reference + one definition
        assert "\n[^%s]: " % lab in text
    assert "power.”[^p14] [SRP 15.0 and 10 CFR 50 Appendix A]" in text   # marker inside a table cell
    assert "event sequences[^p10b] that are associated" in text              # the single dagger footnote
    # the footnote body no longer splits the sentence (review F13)
    assert "all non-safety-related SSCs that perform these same functions are assumed to be unavailable" in text


@pytest.mark.refs
def test_smoke_lists(built):
    doc, aux, text, failed = built
    body = text[text.index("<!-- page 9 |"):]
    assert len([ln for ln in body.split("\n") if ln.startswith("  - ")]) == 20     # 'o' level
    assert len([ln for ln in body.split("\n") if ln.startswith("    - ")]) == 13   # Wingdings level
    assert not re.search(r"^- (As|At) ", body, re.M)          # false list items (review F28)
    assert not re.search(r"^\s*- \d+\. ", body, re.M)         # '- 1.' double markers (review F36)
    assert "\n1. Mitigate DBEs within the F-C Target" in body


@pytest.mark.refs
def test_smoke_figures(built):
    doc, aux, text, failed = built
    assert len(aux.figures) == 11 and doc.meta["figures_without_caption_element"] == []
    for num in ("3-1", "3-2", "3-3", "3-4", "4-1", "4-2", "4-3", "5-1", "5-2", "5-3", "5-4"):
        assert "](figures/NEI_18-04/Fig_%s.png)" % num in text
    assert text.count("**Figure ") == 11
    # vector-figure debris removed (review F17)
    for debris in ("Systems Engineering Inputs", "Acronymns", "Iterate as required", "Color Key", "\n### PRA\n"):
        assert debris not in text, debris
    # informative figure text kept in callouts
    assert text.count("> [!figure]") == 3
    assert "> Layers of defense are defined that provide for the prevention and mitigation of adverse events." in text
    assert "> - Input to LBE selection" in text
    assert "> - Non-Safety-Related SSCs with No Special Treatment (NST): SSCs performing non-safety-significant" in text
    assert "> \\* SR SSCs are also relied on during DBAs to meet 10 CFR 50.34 dose limits" in text
    # the caption of Figure 4-2 is split from the body sentence glued to it (review F17)
    assert "\n**Figure 4-2. Definition of Risk-Significant and Safety-Significant SSCs**\n" in text
    assert "\nThe following key points are used to define the different regions on the SSC Venn diagram:\n" in text


@pytest.mark.refs
def test_smoke_struct_tree_cells_present(built):
    """Every struct-tree table cell reaches the output, except where a documented transformation rewrites it."""
    import json
    doc, aux, text, failed = built
    from refclean.doc import elements_from_json
    with open(os.path.join(RAW, doc.stem + ".structtree.json"), encoding="utf-8") as f:
        els, _ = elements_from_json(json.load(f))
    out = re.sub(r"[^a-z0-9]", "", text.lower())
    exempt = re.compile(r"10-\d|\[[a-d]\]|\*|Applicability1|Guidance4|Process5|^\d\s|^Rj |^FIE|^PASSC|"
                        r"^PPSSC|^rfuel|^rPB|^rcont|Plant Simulation and Modeling of LBEs  State")
    missing = []
    for e in els:
        if e.kind != "table":
            continue
        for row in e.table.grid:
            for c in row:
                if c.filled or not c.text.strip():
                    continue
                for line in c.text.split("\n"):
                    norm = re.sub(r"[^a-z0-9]", "", line.lower())
                    if len(norm) > 12 and norm not in out and not exempt.search(line):
                        missing.append((e.page, line[:60]))
    assert missing == []


@pytest.mark.refs
def test_smoke_verify_residual_is_pinned(built):
    """The accepted PDF-vs-output residual, 385 of 34,001 tokens (1.13 %) on 2026-09-13.

    Composition: the labels inside the raster process figures, above all Figure 5-1 (p61, 88 tokens) and Figure 3-2
    (p28, 44) — raster-figure transcription is a class C item the ledger parks; the 'o' glyph of the second-level
    bullets, emitted as a nested '-' item (20); the copyright footer line on the pages where the footer sits inside
    the text band ('nei.org', '2019', 'rights', 'reserved', 13 each); and line-end hyphen splits that the PDF side
    tokenises separately ('safety-related' -> 'related', 'risk-informed' -> 'informed', 'non-safety', 'significant';
    see refclean/verify.py blind spot 5). Tolerance +-10 tokens: a larger change means prose left the output.
    """
    from refclean.verify import verify
    doc, aux, text, _failed = built
    res = verify(doc, aux, text)
    s = res["summary"]
    assert s["residue"] == {}
    assert abs(s["missing_tokens"] - 385) <= 10, s["missing_tokens"]
    assert s["missing_pct"] < 1.3
    assert [w for k, v in doc.meta.items() if k.endswith("_warnings") for w in v] == []
    assert doc.meta["page_label_mismatch"] == {}
    assert doc.meta["footnotes_unreferenced"] == []
    missing = dict(res["top_missing"])
    assert missing["o"] == 20                                  # second-level bullet glyph
    assert max(res["pages_missing"].values()) == 88 and 61 in res["pages_missing"]   # Figure 5-1 labels
