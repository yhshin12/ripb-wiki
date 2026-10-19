import pytest

import notes as N
import verify_quotes as VQ


def run(vault, path):
    return VQ.verify_note(str(vault), path, VQ.Sources(str(vault), N.load_cards(str(vault))))


def body_with(facts, commentary="가."):
    return (f"# 가 (T)\n\n> [!abstract] 요약\n> 가.\n\n## 원문 사실\n{facts}\n\n## 해설\n{commentary}\n\n"
            "## 관련 문서\n- 없음\n")


def test_good_note_passes(mini_vault, make_note, good_note_body):
    assert run(mini_vault, make_note("Sample", good_note_body)) == []


LBE = '"Licensing basis events include AOOs, DBEs, and BDBEs."'


@pytest.mark.parametrize("item,code", [
    (f"{LBE} [DOC_A §3.2 p.4]", None),                                   # ±1 page
    (f"{LBE} [DOC_A §3.2 p.5]", "V3"),                                   # outside window
    ('"Licensing basis events include AOOs and DBEs." [DOC_A §3.2 p.3]', "V3"),
    ('"The F-C Target is not a boundary between “acceptable” and unacceptable." [DOC_A §3.2 p.2]', None),
    ('"Back on eight: sodium leakage shall be considered." [DOC_A SFR-DC 4 p.8]', None),
    ('"Back on eight: sodium leakage shall be considered." [DOC_A SFR-DC 4 p.10]', "V3"),  # non-monotonic anchors
    ('"Criterion text on nine\\* continues." [DOC_A SFR-DC 4 p.9]', None),
    ('"This information is withheld in accordance with 10 CFR 2.390." [DOC_A §3 p.3]', "V3"),  # editorial
    ('"supplied by the build" [DOC_A §3 p.9]', "V3"),                     # HTML comment
    ('"Licensing basis ... include AOOs, DBEs, and BDBEs." [DOC_A §3.2 p.3]', "V3"),         # short fragment
    ('"Licensing basis events ... include AOOs, DBEs, and BDBEs." [DOC_A §3.2 p.3]', None),
    (LBE, "V1"),
    ("Licensing basis events include AOOs. [DOC_A §3.2 p.3]", "V3"),     # not quoted
    (f"{LBE} [DOC_X §3.2 p.3]", "V2"),
    (f"{LBE} [DOC_A §3.2 p.13]", "V2"),
    (f"{LBE} [DOC_A §3.2]", "V2"),                                        # page required
])
def test_fact_items(mini_vault, make_note, item, code):
    got = [f.code for f in run(mini_vault, make_note("Item", body_with(f"- {item}")))]
    assert got == ([] if code is None else [code])


@pytest.mark.parametrize("row,code", [
    ("| AOO | 1E-02/plant-year | [DOC_A Table x p.2] |", None),
    ("| Range row | 5E-07 | [DOC_A Table 5-1 p.6] |", None),
    ("| Range row | 5E-08 | [DOC_A Table 5-1 p.6] |", "V4"),
    ("| AOO | 1E-02/plant-year | |", "V1"),
])
def test_fact_tables(mini_vault, make_note, row, code):
    facts = f"| 항목 | 값 | 출처 |\n|---|---|---|\n{row}"
    got = [f.code for f in run(mini_vault, make_note("Tbl", body_with(facts)))]
    assert got == ([] if code is None else [code])


def test_table_needs_source_column_and_prose_is_refused(mini_vault, make_note):
    facts = "| 항목 | 값 |\n|---|---|\n| AOO | 1E-02/plant-year |\n\n원문에 따르면 AOO가 있다."
    assert [f.code for f in run(mini_vault, make_note("Tbl", body_with(facts)))] == ["V1", "V1"]


def test_figure_embed_line_is_allowed_in_facts(mini_vault, make_note):
    facts = f'- {LBE} [DOC_A §3.2 p.3]\n\n![[DOC_A_Fig_1.png]]'
    assert run(mini_vault, make_note("Fig", body_with(facts))) == []
    facts = f'- {LBE} [DOC_A §3.2 p.3]\n\n![[DOC_A_Fig_1.png]] 설명'
    assert [f.code for f in run(mini_vault, make_note("Fig2", body_with(facts)))] == ["V1"]


def test_commentary_numbers_must_appear_in_facts(mini_vault, make_note):
    facts = "| 항목 | 값 | 출처 |\n|---|---|---|\n| AOO | 1E-02/plant-year | [DOC_A Table x p.2] |"
    assert run(mini_vault, make_note("N1", body_with(facts, "값은 1E-2/plant-year이다."))) == []
    got = run(mini_vault, make_note("N2", body_with(facts, "값은 5E-07이다.")))
    assert [(f.code, f.message) for f in got] == [("V5", "number 5E-7 in 해설 is not in 원문 사실")]


def test_cli_exit_codes(mini_vault, make_note, good_note_body, monkeypatch, capsys):
    monkeypatch.setattr(VQ, "VAULT", str(mini_vault))
    good = make_note("Sample", good_note_body)
    assert VQ.main([good]) == 0
    make_note("Bad", good_note_body.replace("p.3]", "p.13]"))
    assert VQ.main(["--all"]) == 1
    assert "wiki/Bad.md" in capsys.readouterr().out


def test_page_labelled_footnote_counts_on_its_own_page(mini_vault, make_note):
    cleaned = ("<!-- page 1 -->\n\nCover.\n\n<!-- page 2 -->\n\nBody text on two[^p2].\n\n<!-- page 5 -->\n\n"
               "Body text on five.\n\n[^p2]: The footnote sentence belongs to page two.\n")
    (mini_vault / "references" / "DOC_A_T.md").write_text(cleaned, encoding="utf-8", newline="\n")
    good = make_note("Fn", body_with('- "The footnote sentence belongs to page two." [DOC_A §3 p.2]'))
    assert run(mini_vault, good) == []
