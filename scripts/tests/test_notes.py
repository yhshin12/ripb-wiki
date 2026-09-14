import pytest

import notes


def test_write_text_rejects_cr_bom_and_replacement_char(tmp_path):
    for bad in ("a\r\nb\n", "﻿a\n", "a�\n"):
        with pytest.raises(notes.NoteError):
            notes.write_text(str(tmp_path / "x.md"), bad)
    assert not (tmp_path / "x.md").exists()


def test_write_note_roundtrip(tmp_path):
    p = tmp_path / "n.md"
    notes.write_note(str(p), {"type": "concept", "aliases": ["가나"]}, "# 제목 (Title)\n")
    fm, body = notes.read_note(str(p))
    assert fm == {"type": "concept", "aliases": ["가나"]} and body == "# 제목 (Title)\n"
    assert b"\r" not in p.read_bytes()
