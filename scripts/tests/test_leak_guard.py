import os
import subprocess

import pytest

import leak_guard as LG


@pytest.fixture
def ivault(tmp_path):
    """A vault whose internal/ tree holds fictitious documents."""
    for d in ("internal/references/raw", "internal/wiki", "internal/meetings", "wiki"):
        os.makedirs(tmp_path / d)
    (tmp_path / "internal/references/raw/HSFR_X_Design Note.pdf").write_bytes(b"%PDF fake")
    (tmp_path / "internal/wiki/HSFR_Pump_Trial.md").write_text(
        "---\ntype: hsfr\ntitle: Zeta Loop Pump Trial\naliases: [ZLP, Zeta Loop Trial]\n---\n\n"
        "# 가상 시험 (Zeta Loop Pump Trial)\n", encoding="utf-8")
    (tmp_path / "internal/meetings/2026-01-02_kickoff.md").write_text("# Omega Kickoff Meeting\n", encoding="utf-8")
    return tmp_path


def test_internal_names_collects_stems_titles_h1_aliases(ivault):
    names = LG.internal_names(str(ivault))
    assert "hsfr_x_design note" in names
    assert "zeta loop pump trial" in names and "zeta loop trial" in names
    assert "가상 시험 (zeta loop pump trial)" in names and "가상 시험" not in names  # 5 chars < 8
    assert "omega kickoff meeting" in names and "2026-01-02_kickoff" in names
    assert "zlp" not in names


def test_allow_list_removes_names(ivault):
    (ivault / "internal" / "leak_allow.txt").write_text("Zeta Loop Trial\n", encoding="utf-8")
    assert "zeta loop trial" not in LG.internal_names(str(ivault))


def test_scan_is_case_and_space_insensitive():
    hits = LG.scan([("wiki/A.md:3", "see the  ZETA loop   pump trial here")], {"zeta loop pump trial"})
    assert hits == [("wiki/A.md:3", "zeta loop pump trial")]
    assert LG.scan([("x", "nothing")], {"zeta loop pump trial"}) == []


def test_staged_added_lines_reads_only_additions_and_paths(ivault):
    run = lambda *a: subprocess.run(["git", "-C", str(ivault), *a], check=True, capture_output=True)
    run("init", "-q")
    (ivault / "wiki" / "Old.md").write_text("keep\n", encoding="utf-8")
    run("add", "wiki/Old.md")
    (ivault / "wiki" / "Omega Kickoff Meeting.md").write_text("line one\nline two\n", encoding="utf-8")
    run("add", "-A", "wiki")
    items = LG.staged_added_lines(str(ivault))
    assert ("wiki/Omega Kickoff Meeting.md", "wiki/Omega Kickoff Meeting.md") in items
    assert ("wiki/Omega Kickoff Meeting.md:2", "line two") in items
    assert all(not t.startswith("+") for _, t in items)


def test_message_mode_exit_codes(ivault, tmp_path_factory, monkeypatch, capsys):
    monkeypatch.setattr(LG, "VAULT", str(ivault))
    msg = tmp_path_factory.mktemp("m") / "MSG"
    msg.write_text("docs: add Omega Kickoff Meeting summary\n", encoding="utf-8")
    assert LG.main(["--message", str(msg)]) == 1
    assert "omega kickoff meeting" in capsys.readouterr().out
    msg.write_text("docs: status\n", encoding="utf-8")
    assert LG.main(["--message", str(msg)]) == 0


def test_no_internal_tree_passes_with_notice(tmp_path, monkeypatch, capsys):
    monkeypatch.setattr(LG, "VAULT", str(tmp_path))
    f = tmp_path / "a.md"
    f.write_text("text\n", encoding="utf-8")
    assert LG.main(["--files", str(f)]) == 0
    assert "internal/ not present" in capsys.readouterr().out


def test_extra_probe_names_from_environment(tmp_path, monkeypatch):
    monkeypatch.setenv("RIPB_LEAK_EXTRA", "zz-leak-probe-4711")
    os.makedirs(tmp_path / "internal")
    assert "zz-leak-probe-4711" in LG.internal_names(str(tmp_path))
