import pytest

import terms as T

HEAD = "| ID | English | 약어 | 한국어 | 이후 표기 | 금지 표기 | 정의 출처 | 상태 | 비고 |\n|---|---|---|---|---|---|---|---|---|\n"


def table(*rows):
    return "# 용어표 (Terminology)\n\n## 용어\n\n" + HEAD + "".join(rows) + "\n## 관련 문서\n- 없음\n"


ROWS = ("| LBE | Licensing Basis Event | LBE | 가나 | 약어 | 가나다; 나가 | [DOC_A §3 p.2] | 확정 | |\n"
        "| RAC | Reactor Air Cooling System | RAC |  | 약어 |  | [DOC_B 약어표 p.5] | 미정 | |\n"
        "| PLANT | Plant |  |  |  |  |  | 용어 아님 | |\n")


def test_parse_table_fields():
    t = T.parse_table(table(ROWS))
    assert set(t) == {"LBE", "RAC", "PLANT"}
    assert t["LBE"].forbidden == ("가나다", "나가") and t["LBE"].later == "약어" and t["RAC"].state == "미정"
    assert T.parse_table(table()) == {}


@pytest.mark.parametrize("row,msg", [
    ("| LBE | A | L | 가 | 약어 |  |  | 확정 | |\n| LBE | B | L | 나 | 약어 |  |  | 확정 | |\n", "duplicate ID"),
    ("| X1 | A |  |  |  |  |  | 보류 | |\n", "state"),
    ("| X1 | A |  |  | 한국어 |  |  | 확정 | |\n", "한국어"),
    ("| X1 | A |  |  | 약어 |  |  | 미정 | |\n", "약어"),
    ("| X1 | A |  |  |  |  |  | 미정 |\n", "cells"),
    ("| 1 x | A |  |  |  |  |  | 미정 | |\n", "ID"),
])
def test_parse_table_errors_name_the_line(row, msg):
    with pytest.raises(T.TermError, match=msg) as e:
        T.parse_table(table(row))
    assert "line " in str(e.value)


def test_missing_header_is_an_error():
    with pytest.raises(T.TermError, match="header"):
        T.parse_table("# 용어표\n\n| ID | English |\n|---|---|\n")


def test_display_rules():
    t = T.parse_table(table(ROWS, "| DBE | Design Basis Event | DBE | 가닥 | 한국어 |  |  | 확정 | |\n"
                               "| NST | No Special Treatment | NST |  |  |  |  | 영어 유지 | |\n"))
    assert T.display(t["LBE"], True) == "가나(Licensing Basis Event)" and T.display(t["LBE"], False) == "LBE"
    assert T.display(t["DBE"], False) == "가닥"
    assert T.display(t["RAC"], True) == "Reactor Air Cooling System" and T.display(t["RAC"], False) == "RAC"
    assert T.display(t["NST"], False) == "No Special Treatment"
    assert T.display(t["PLANT"], True) is None


@pytest.mark.parametrize("word,fin", [
    ("가나", "none"), ("가닥", "other"), ("가날", "rieul"), ("LBE", "none"), ("RAM", "other"), ("SFR", "rieul"),
    ("PSAR2", "none"), ("가닥(Licensing Basis Event)", "other"), ("Licensing Basis Event", None), ("LBEs", None),
])
def test_final_consonant(word, fin):
    assert T.final(word) == fin


@pytest.mark.parametrize("after,fin,out", [
    ("는 다음", "other", "은 다음"), ("가 있다", "other", "이 있다"), ("를 본다", "other", "을 본다"),
    ("와 함께", "other", "과 함께"), ("로 간다", "other", "으로 간다"), ("으로 간다", "none", "로 간다"),
    ("으로 간다", "rieul", "로 간다"), ("은 다음", "none", "는 다음"), ("이며 다음", "none", "이며 다음"),
    ("는 다음", None, "는 다음"), (". 다음", "other", ". 다음"), ("는", "other", "은"),
])
def test_retarget_particles(after, fin, out):
    assert T.retarget(after, fin) == out


def test_marker_and_snapshot():
    assert T.MARKER.findall("LBE%%t:LBE%%는 DL3%%t:DL3-RC%%") == ["LBE", "DL3-RC"]
    snap = T.snapshot(T.parse_table(table(ROWS)))
    assert snap["LBE"] == {"english": "Licensing Basis Event", "abbr": "LBE", "korean": "가나", "later": "약어",
                           "forbidden": ["가나다", "나가"], "state": "확정"}
