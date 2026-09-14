import pytest

import append_log as AL

HEAD = "# log\n\n설명.\n\n## [2026-09-14] init | 시작\n- 첫 항목.\n"


def make_log(base, text=HEAD):
    base.mkdir(parents=True, exist_ok=True)
    p = base / "log.md"
    p.write_bytes(text.encode("utf-8"))
    return p


def test_append_keeps_previous_bytes(tmp_path):
    p = make_log(tmp_path)
    before = p.read_bytes()
    AL.append(str(tmp_path), None, "2026-09-20", "ingest", "NEI 18-04 §3", ["노트 3개 신규.", "검사 통과."])
    after = p.read_bytes()
    assert after.startswith(before)
    assert after[len(before):].decode("utf-8") == "\n## [2026-09-20] ingest | NEI 18-04 §3\n- 노트 3개 신규.\n- 검사 통과.\n"


def test_missing_final_newline_is_supplied(tmp_path):
    p = make_log(tmp_path, HEAD.rstrip("\n"))
    AL.append(str(tmp_path), None, "2026-09-20", "docs", "t", ["a"])
    assert "- 첫 항목.\n\n## [2026-09-20] docs | t\n- a\n" in p.read_text(encoding="utf-8")


@pytest.mark.parametrize("date,typ,title,items", [
    ("2026-9-20", "docs", "t", ["a"]),
    ("2026-09-20", "misc", "t", ["a"]),
    ("2026-09-20", "docs", "two\nlines", ["a"]),
    ("2026-09-20", "docs", "", ["a"]),
    ("2026-09-20", "docs", "t", []),
    ("2026-09-20", "docs", "t", ["a\r"]),
])
def test_invalid_entries_are_refused_and_file_untouched(tmp_path, date, typ, title, items):
    p = make_log(tmp_path)
    before = p.read_bytes()
    with pytest.raises(AL.LogError):
        AL.append(str(tmp_path), None, date, typ, title, items)
    assert p.read_bytes() == before


def test_internal_root_and_cli(tmp_path, monkeypatch):
    make_log(tmp_path)
    ip = make_log(tmp_path / "internal")
    monkeypatch.setattr(AL, "VAULT", str(tmp_path))
    assert AL.main(["--root", "internal", "--type", "docs", "--title", "내부", "--item", "x", "--date", "2026-09-20"]) == 0
    assert ip.read_bytes().decode("utf-8").endswith("## [2026-09-20] docs | 내부\n- x\n")
    assert AL.main(["--type", "nope", "--title", "t", "--item", "x"]) == 1
