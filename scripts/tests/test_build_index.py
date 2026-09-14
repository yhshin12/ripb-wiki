import build_index as BI


def test_render_groups_and_summaries(mini_vault, make_note, good_note_body):
    make_note("Sample", good_note_body)
    make_note("Old", good_note_body.replace("시험 노트이다.", "옛 노트이다. 둘째 문장."), status="deprecated")
    make_note("Clash", good_note_body, status="disputed", type="natrium")
    text = BI.render(str(mini_vault))
    assert text.startswith(BI.HEADER)
    assert "## 원문 (source)\n\n- [[DOC_A]] — T\n" in text                     # card placeholder → title
    assert "- [[Sample]] — 가나(Licensing Basis Event)에 관한 시험 노트이다.\n" in text   # marker stripped
    assert "- [[Clash]] — 가나(Licensing Basis Event)에 관한 시험 노트이다. (disputed)\n" in text
    assert text.index("## 원문 (source)") < text.index("## 개념 (concept)") < text.index("## Natrium (natrium)") \
        < text.index("## 지도 (map)") < text.index("## 대체됨 (deprecated)")
    assert text.rstrip("\n").endswith("- [[Old]] — 가나(Licensing Basis Event)에 관한 옛 노트이다.")
    assert "둘째 문장" not in text


def test_check_and_write(mini_vault, make_note, good_note_body, monkeypatch):
    monkeypatch.setattr(BI, "VAULT", str(mini_vault))
    (mini_vault / "index.md").unlink()
    assert BI.main(["--check"]) == 1
    assert BI.main([]) == 0 and BI.main(["--check"]) == 0
    make_note("Sample", good_note_body)
    assert BI.main(["--check"]) == 1
    assert b"\r" not in (mini_vault / "index.md").read_bytes()


def test_internal_index(mini_vault, make_note, good_note_body, monkeypatch):
    monkeypatch.setattr(BI, "VAULT", str(mini_vault))
    make_note("HSFR_Trial", good_note_body, root="internal", type="hsfr")
    assert BI.main(["--root", "internal"]) == 0
    text = (mini_vault / "internal" / "index.md").read_text(encoding="utf-8")
    assert "[[HSFR_Trial]]" in text and "[[DOC_A]]" not in text
