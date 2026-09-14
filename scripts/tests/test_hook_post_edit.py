import io
import json
import os

import hook_post_edit as H


def payload(path, cwd):
    return {"hook_event_name": "PostToolUse", "tool_name": "Edit", "cwd": cwd, "tool_input": {"file_path": path}}


def test_target_selects_wiki_notes_only(mini_vault):
    v = str(mini_vault)
    assert H.target(payload(os.path.join(v, "wiki", "A.md"), v), v) == os.path.join(v, "wiki", "A.md")
    assert H.target(payload(os.path.join(v, "internal", "wiki", "B.md"), v), v) == os.path.join(v, "internal", "wiki", "B.md")
    assert H.target(payload("wiki/C.md", v), v) == os.path.join(v, "wiki", "C.md")
    assert H.target(payload(os.path.join(v, "wiki", "assets", "x.md"), v), v) is None
    assert H.target(payload(os.path.join(v, "scripts", "x.py"), v), v) is None
    assert H.target({"tool_input": {}}, v) is None


def run(monkeypatch, vault, path, capsys):
    monkeypatch.setattr(H, "VAULT", str(vault))
    assert H.main(io.StringIO(json.dumps(payload(path, str(vault))))) == 0
    return capsys.readouterr().out


def test_errors_are_returned_to_claude(mini_vault, make_note, good_note_body, monkeypatch, capsys):
    p = make_note("Bad", good_note_body.replace("## 해설", "## 설명").replace("p.3]", "p.13]"))
    out = json.loads(run(monkeypatch, mini_vault, p, capsys))
    assert out["decision"] == "block"
    assert "L06" in out["reason"] and "V2" in out["reason"] and "wiki/Bad.md" in out["reason"]


def test_clean_note_prints_nothing(mini_vault, make_note, good_note_body, monkeypatch, capsys):
    assert run(monkeypatch, mini_vault, make_note("Good", good_note_body), capsys) == ""


def test_warnings_become_context_without_block(mini_vault, make_note, good_note_body, monkeypatch, capsys):
    p = make_note("Warn", good_note_body.replace("세 종류이다.", "RAC도 있다."))
    out = json.loads(run(monkeypatch, mini_vault, p, capsys))
    assert "decision" not in out
    assert "L13" in out["hookSpecificOutput"]["additionalContext"]


def test_template_shaped_note_is_reported(mini_vault, make_note, good_note_body, monkeypatch, capsys):
    p = make_note("Template_Like", good_note_body, type={"type": None})
    out = json.loads(run(monkeypatch, mini_vault, p, capsys))
    assert out["decision"] == "block" and "L04" in out["reason"]


def test_bad_stdin_is_ignored(monkeypatch, capsys, mini_vault):
    monkeypatch.setattr(H, "VAULT", str(mini_vault))
    assert H.main(io.StringIO("not json")) == 0
    assert capsys.readouterr().out == ""
