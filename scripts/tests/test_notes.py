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


def test_load_offset_and_sections(tmp_path):
    p = tmp_path / "N.md"
    p.write_text("---\ntype: concept\n---\n\n# 제목 (Title)\n\n> [!abstract] 요약\n> 가나.\n\n## 원문 사실\n- a\n\n## 해설\nb\n",
                 encoding="utf-8")
    n = notes.load(str(p))
    assert n.name == "N" and n.offset == 4
    secs = notes.sections(n)
    assert [(t, line) for t, line, _ in secs] == [("", 5), ("원문 사실", 10), ("해설", 13)]
    assert (11, "- a") in secs[1][2]


def test_load_cards_reads_both_trees_and_skips_malformed(tmp_path):
    for d in ("wiki", "internal/wiki"):
        (tmp_path / d).mkdir(parents=True)
    notes.write_note(str(tmp_path / "wiki" / "DOC_A.md"), {"type": "source", "key": "DOC_A"}, "# A\n")
    notes.write_note(str(tmp_path / "internal" / "wiki" / "HELIOS_X.md"), {"type": "source", "key": "HELIOS_X"}, "# X\n")
    notes.write_note(str(tmp_path / "wiki" / "Concept.md"), {"type": "concept"}, "# C\n")
    (tmp_path / "wiki" / "Broken.md").write_text("---\ntype: source\n", encoding="utf-8")
    cards = notes.load_cards(str(tmp_path))
    assert set(cards) == {"DOC_A", "HELIOS_X"} and cards["HELIOS_X"]["root"] == "internal"
    assert notes.wiki_notes(str(tmp_path)) == [str(tmp_path / "wiki" / f) for f in ("Broken.md", "Concept.md", "DOC_A.md")]
