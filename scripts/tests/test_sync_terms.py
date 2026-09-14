import json

import pytest

import lint_wiki as LW
import notes as N
import sync_terms as ST

LBE_ROW = "| LBE | Licensing Basis Event | LBE | 가나 | 약어 | 나가 | [DOC_A §3.2 p.3] | 확정 | |"
RAC_ROW = "| RAC | Reactor Air Cooling System | RAC |  | 약어 |  | [DOC_A §3.2 p.3] | 미정 | |"


def set_row(vault, old, new):
    t = vault / "wiki" / "Terminology.md"
    text = t.read_text(encoding="utf-8")
    assert old in text
    t.write_text(text.replace(old, new), encoding="utf-8", newline="\n")


@pytest.fixture
def synced(mini_vault, monkeypatch):
    monkeypatch.setattr(ST, "VAULT", str(mini_vault))
    assert ST.main(["--apply"]) == 0
    return mini_vault


def body_of(path):
    return N.read_note(path)[1]


def test_dry_run_writes_nothing(synced, make_note, good_note_body):
    p = make_note("Sample", good_note_body)
    set_row(synced, LBE_ROW, LBE_ROW.replace("가나 |", "가닥 |"))
    before = open(p, "rb").read()
    assert ST.main([]) == 0
    assert open(p, "rb").read() == before
    state = json.load(open(synced / "meta" / "terms_state.json", encoding="utf-8"))
    assert state["terms"]["LBE"]["korean"] == "가나"


def test_korean_change_rewrites_displays_and_particles(synced, make_note, good_note_body):
    p = make_note("Sample", good_note_body)
    set_row(synced, LBE_ROW, LBE_ROW.replace("가나 |", "가닥 |"))
    assert ST.main(["--apply"]) == 0
    b = body_of(p)
    assert "> 가닥(Licensing Basis Event)%%t:LBE%%에 관한" in b and "LBE%%t:LBE%%는 세 종류" in b
    set_row(synced, LBE_ROW.replace("가나 |", "가닥 |"), LBE_ROW.replace("가나 | 약어 |", "가닥 | 한국어 |"))
    assert ST.main(["--apply"]) == 0
    assert "가닥%%t:LBE%%은 세 종류" in body_of(p)
    assert LW.lint_file(LW.Context(str(synced)), p) == []


def test_pending_to_confirmed_updates_display_and_pending_field(synced, make_note, good_note_body):
    body = good_note_body.replace("세 종류이다.", "Reactor Air Cooling System%%t:RAC%%도 있고 RAC%%t:RAC%%를 쓴다.")
    p = make_note("Sample", body)
    assert ST.main(["--apply"]) == 0
    assert N.read_note(p)[0]["terms_pending"] == ["RAC"]
    set_row(synced, RAC_ROW, "| RAC | Reactor Air Cooling System | RAC | 가날 | 약어 |  | [DOC_A §3.2 p.3] | 확정 | |")
    assert ST.main(["--apply"]) == 0
    fm, b = N.read_note(p)
    assert "가날(Reactor Air Cooling System)%%t:RAC%%도 있고 RAC%%t:RAC%%를 쓴다." in b
    assert fm["terms_pending"] == []
    assert LW.lint_file(LW.Context(str(synced)), p) == []


def test_not_a_term_removes_marker_and_keeps_text(synced, make_note, good_note_body):
    p = make_note("Sample", good_note_body)
    set_row(synced, LBE_ROW, "| LBE | Licensing Basis Event | LBE |  |  |  |  | 용어 아님 | |")
    assert ST.main(["--apply"]) == 0
    b = body_of(p)
    assert "%%t:LBE%%" not in b and "> 가나(Licensing Basis Event)에 관한" in b and "LBE는 세 종류" in b


def test_conflict_is_reported_left_alone_and_state_kept(synced, make_note, good_note_body, capsys):
    p = make_note("Sample", good_note_body.replace("LBE%%t:LBE%%는", "엘비이%%t:LBE%%는"))
    set_row(synced, LBE_ROW, LBE_ROW.replace("가나 |", "가닥 |"))
    before = body_of(p)
    assert ST.main(["--apply"]) == 1
    assert "conflict wiki/Sample.md" in capsys.readouterr().out
    assert "엘비이%%t:LBE%%는" in body_of(p) and "가닥(Licensing Basis Event)%%t:LBE%%에" in body_of(p)
    assert body_of(p) != before
    assert ST.terms_changed(str(synced)) == ["LBE"]          # state not advanced


def test_particle_after_english_is_reported(synced, make_note, good_note_body, capsys):
    make_note("Sample", good_note_body.replace("세 종류이다.", "Reactor Air Cooling System%%t:RAC%%는 미정이다."))
    capsys.readouterr()
    ST.main([])
    assert "check particle wiki/Sample.md" in capsys.readouterr().out


def test_term_note_title_and_alias_follow_table(synced, make_note, good_note_body):
    p = make_note("Licensing_Basis_Event", good_note_body, term="LBE", aliases=["가나", "LBE"])
    set_row(synced, LBE_ROW, LBE_ROW.replace("가나 |", "가닥 |"))
    assert ST.main(["--apply"]) == 0
    fm, b = N.read_note(p)
    assert b.startswith("# 가닥 (Licensing Basis Event)\n") and fm["aliases"] == ["LBE", "가닥"]


def test_terms_changed(synced):
    assert ST.terms_changed(str(synced)) == []
    set_row(synced, LBE_ROW, LBE_ROW.replace("가나 |", "가닥 |"))
    assert ST.terms_changed(str(synced)) == ["LBE"]
