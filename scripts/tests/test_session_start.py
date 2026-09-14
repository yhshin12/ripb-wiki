import subprocess

import pytest

import session_start as SS


def git(vault, *a):
    subprocess.run(["git", "-C", str(vault), "-c", "user.name=t", "-c", "user.email=t@example.invalid", *a],
                   check=True, capture_output=True)


@pytest.fixture
def svault(mini_vault):
    (mini_vault / "meta" / "status.md").write_text(
        "---\nupdated: x\n---\n# 상태\n\n## 현재 단계\nPhase 3.\n\n## 다음 작업\n1. 시범.\n\n## 미해결\n- 없음\n",
        encoding="utf-8", newline="\n")
    (mini_vault / "log.md").write_text("# log\n\n## [2026-09-14] init | a\n- x\n\n## [2026-09-15] feat | b\n- y\n",
                                       encoding="utf-8", newline="\n")
    return mini_vault


def test_report_parts_without_git(svault):
    (svault / "inbox" / "new.pdf").write_bytes(b"%PDF")
    text = SS.report(str(svault))
    assert "### 다음 작업\n1. 시범." in text
    assert "## [2026-09-15] feat | b" in text
    assert "git #1: git 저장소 아님" in text
    assert "변경 2건: LBE, RAC" in text                      # no terms_state.json yet
    assert "inbox 대기: 1 (new.pdf)" in text and "DOC_A: ingest pending, 단위 0/0" in text
    assert "lint_wiki: 오류 0, 경고 0" in text and "verify_quotes: 오류 0" in text
    assert "## 커밋되지 않은 노트 변경\n없음" in text


def test_uncommitted_note_edits_are_checked(svault, make_note, good_note_body):
    git(svault, "init", "-q")
    git(svault, "add", "-A")
    git(svault, "commit", "-q", "-m", "base")
    make_note("Sample", good_note_body.replace("## 해설", "## 설명"))
    text = SS.report(str(svault))
    assert "git #1: 변경 1건" in text
    assert "- wiki/Sample.md: 오류 1" in text and "L06" in text


def test_failures_become_lines_and_exit_zero(svault, monkeypatch, capsys):
    (svault / "wiki" / "Terminology.md").write_text("broken\n", encoding="utf-8", newline="\n")
    monkeypatch.setattr(SS, "VAULT", str(svault))
    assert SS.main() == 0
    out = capsys.readouterr().out
    assert "용어표 오류" in out and "## 검사 (공개 트리)" in out
