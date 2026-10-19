import check_absence as CA

BODY = """# 제목 (Title)

> [!abstract] 요약
> 요약 문장이다.

## 원문 사실

- "The criteria are listed in the table." [DOC_A §3.2 p.2]

## 해설

{line}

## 관련 문서

- [[DOC_A]]
"""


def _filler(make_note, n=30):
    for i in range(n):
        make_note(f"Filler_{i:02d}", BODY.format(line=f"일반 서술 {i}이다. design basis safety function."))


def _codes(vault):
    return [(f.path, f.code) for f in CA.check(str(vault))]


def test_new_statement_is_unreviewed_until_accepted(mini_vault, make_note):
    make_note("Crosswalk", BODY.format(line="MHTGR-DC와의 비교는 vault에 없다."))
    assert ("wiki/Crosswalk.md", "A1") in _codes(mini_vault)
    CA.accept(str(mini_vault))
    assert CA.check(str(mini_vault)) == []


def test_quoted_absence_in_source_facts_is_not_a_statement(mini_vault, make_note):
    p = make_note("Plain", BODY.format(line="해설 문장이다."))
    import notes
    assert CA.statements(notes.load(p)) == []


def test_new_note_with_rare_title_token_flags_statement(mini_vault, make_note):
    _filler(make_note)
    make_note("Crosswalk", BODY.format(line="MHTGR-DC와의 비교는 vault에 없다."))
    CA.accept(str(mini_vault))
    make_note("MHTGR_DC_Containment", BODY.format(line="MHTGR-DC 기준을 정리한다."))
    got = CA.check(str(mini_vault))
    assert [(f.path, f.code) for f in got] == [("wiki/Crosswalk.md", "A2")]
    assert "MHTGR_DC_Containment" in got[0].message


def test_common_tokens_do_not_flag(mini_vault, make_note):
    _filler(make_note)
    make_note("Crosswalk", BODY.format(line="design basis safety function의 비교는 vault에 없다."))
    CA.accept(str(mini_vault))
    make_note("Other", BODY.format(line="design basis safety function을 정리한다."))
    assert CA.check(str(mini_vault)) == []


def test_rewording_the_statement_needs_new_review(mini_vault, make_note):
    make_note("Crosswalk", BODY.format(line="MHTGR-DC와의 비교는 vault에 없다."))
    CA.accept(str(mini_vault))
    make_note("Crosswalk", BODY.format(line="MHTGR-DC와의 직접 비교는 vault에 없다."))
    assert _codes(mini_vault) == [("wiki/Crosswalk.md", "A1")]


def test_own_note_change_does_not_flag(mini_vault, make_note):
    _filler(make_note)
    make_note("Crosswalk", BODY.format(line="MHTGR-DC와의 비교는 vault에 없다."))
    CA.accept(str(mini_vault))
    make_note("Crosswalk", BODY.format(line="MHTGR-DC와의 비교는 vault에 없다.") + "\nMHTGR 추가 문단이다.\n")
    assert CA.check(str(mini_vault)) == []


def test_plural_abbreviation_matches_singular():
    assert "DBHL" in CA.line_tokens("DBHLs의 정의는 vault에 없다.")
    assert "hazard" in CA.line_tokens("external hazards는 원문에 없다.")


def test_assumption_is_not_an_absence_statement():
    assert not CA.ABSENCE.search("누설을 LBE로 가정하지 않으며")
    assert CA.ABSENCE.search("원문은 기준을 정하지 않는다")


def test_only_added_lines_count_as_new_evidence(mini_vault, make_note):
    _filler(make_note)
    make_note("Crosswalk", BODY.format(line="MHTGR-DC와의 비교는 vault에 없다."))
    make_note("Other", BODY.format(line="MHTGR 기준을 다룬다.\n\n둘째 문단이다."))
    CA.accept(str(mini_vault))
    make_note("Other", BODY.format(line="MHTGR 기준을 다룬다.\n\n고친 둘째 문단이다."))
    assert CA.check(str(mini_vault)) == []
    make_note("Other", BODY.format(line="MHTGR 기준을 다룬다.\n\nMHTGR-DC 비교표를 더한다."))
    assert [f.code for f in CA.check(str(mini_vault))] == ["A2"]
