import json

import pytest

import audit_sample as AS


def checked(make_note, body, n):
    return [make_note(f"Checked_{i}", body, status="checked", verified="2026-09-20") for i in range(n)]


def test_population_and_deterministic_sample(mini_vault, make_note, good_note_body, tmp_path):
    checked(make_note, good_note_body, 5)
    make_note("Draft", good_note_body)
    assert len(AS.population(str(mini_vault))) == 5
    a = AS.sample(str(mini_vault), 3, 7, str(tmp_path / "a"))
    b = AS.sample(str(mini_vault), 3, 7, str(tmp_path / "b"))
    assert a["notes"] == b["notes"] and len(a["notes"]) == 3 and a["population"] == 5
    assert len(AS.sample(str(mini_vault), 10, 7, str(tmp_path / "c"))["notes"]) == 5


def test_prompt_lists_sources_and_citations(mini_vault, make_note, good_note_body, tmp_path):
    checked(make_note, good_note_body, 1)
    AS.sample(str(mini_vault), 1, 1, str(tmp_path))
    text = (tmp_path / "Checked_0.prompt.md").read_text(encoding="utf-8")
    assert "`wiki/Checked_0.md`" in text and "정제본 `references/DOC_A_T.md`" in text
    assert "[DOC_A §3.2 p.3]" in text and "[DOC_A Table x p.2]" in text
    assert "파일을 수정하지 않는다" in text


def _result(path, facts, commentary):
    path.write_text(json.dumps({"facts": [{"line": 1, "verdict": v} for v in facts],
                                "commentary": [{"sentence": "s", "verdict": v} for v in commentary]},
                               ensure_ascii=False), encoding="utf-8")


def test_summarize_counts(mini_vault, make_note, good_note_body, tmp_path):
    checked(make_note, good_note_body, 2)
    meta = AS.sample(str(mini_vault), 2, 3, str(tmp_path))
    names = [n.split("/")[-1][:-3] for n in meta["notes"]]
    _result(tmp_path / f"{names[0]}.result.json", ["일치", "경미"], ["근거 있음"])
    with pytest.raises(AS.AuditError, match="missing"):
        AS.summarize(str(tmp_path))
    _result(tmp_path / f"{names[1]}.result.json", ["불일치"], ["원문과 모순"])
    assert AS.summarize(str(tmp_path)).endswith("| 3 | 2/2 | 1 | 50 % | 1/3 | 1 |")


def test_unknown_verdict_is_refused(mini_vault, make_note, good_note_body, tmp_path):
    checked(make_note, good_note_body, 1)
    AS.sample(str(mini_vault), 1, 1, str(tmp_path))
    _result(tmp_path / "Checked_0.result.json", ["맞음"], [])
    with pytest.raises(AS.AuditError, match="verdict"):
        AS.summarize(str(tmp_path))


def test_cli(mini_vault, make_note, good_note_body, tmp_path, monkeypatch):
    monkeypatch.setattr(AS, "VAULT", str(mini_vault))
    checked(make_note, good_note_body, 1)
    assert AS.main(["sample", "--n", "1", "--seed", "1", "--out", str(tmp_path)]) == 0
    assert AS.main(["summarize", str(tmp_path)]) == 1
