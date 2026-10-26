import json

import coverage_sections as CS

CLEANED = """<!-- page 1 -->

# Cover

<!-- page 2 | 1 -->

## 3.2 Frequency

Body of section three point two that is long enough.

### 3.2.1 Details

Body of the subsection three point two point one.

<!-- page 3 | 2 -->

### Table 5.2-1 Functions

#### DL3-RC1 — Scram

Record body text for the scram function record.

### Unnumbered Topic

Body of an unnumbered heading on page three.

## References (3)

- A reference list entry that is long enough to count.
"""


def _cleaned(mini_vault, text=CLEANED):
    (mini_vault / "references" / "DOC_A_T.md").write_text(text, encoding="utf-8", newline="\n")


def _titles(findings):
    return [f.message.split("uncited: ")[1].split(" (")[0] for f in findings]


def _note(make_note, *cites):
    body = "# 시험 (Test)\n\n## 원문 사실\n" + "".join(f'- "Some quoted text here." {c}\n' for c in cites)
    make_note("Cov", body)


def test_no_notes_reports_every_long_heading_but_references(mini_vault):
    _cleaned(mini_vault)
    got = _titles(CS.check(str(mini_vault), min_chars=10))
    assert got == ["3.2 Frequency", "3.2.1 Details", "DL3-RC1 — Scram", "Unnumbered Topic"]


def test_descendant_citation_covers_ancestor_but_not_sibling(mini_vault, make_note):
    _cleaned(mini_vault)
    _note(make_note, "[DOC_A §3.2.1 p.2]")
    got = _titles(CS.check(str(mini_vault), min_chars=10))
    assert "3.2 Frequency" not in got and "3.2.1 Details" not in got


def test_ancestor_citation_on_same_page_covers_child(mini_vault, make_note):
    _cleaned(mini_vault)
    _note(make_note, "[DOC_A §3.2 p.2]")
    assert "3.2.1 Details" not in _titles(CS.check(str(mini_vault), min_chars=10))


def test_ancestor_citation_on_other_page_does_not_cover_child(mini_vault, make_note):
    _cleaned(mini_vault)
    _note(make_note, "[DOC_A §3.2 p.3]")
    assert "3.2.1 Details" in _titles(CS.check(str(mini_vault), min_chars=10))


def test_enclosing_table_citation_covers_record_only(mini_vault, make_note):
    _cleaned(mini_vault)
    _note(make_note, "[DOC_A Table 5.2-1 p.3]")
    got = _titles(CS.check(str(mini_vault), min_chars=10))
    # the unnumbered heading inherits §3.2 from its parent, so a table citation on its page does not cover it
    assert "DL3-RC1 — Scram" not in got and "Unnumbered Topic" in got


def test_unnumbered_heading_inherits_parent_section(mini_vault, make_note):
    _cleaned(mini_vault)
    _note(make_note, "[DOC_A §3.2 p.2]")
    assert "Unnumbered Topic" not in _titles(CS.check(str(mini_vault), min_chars=10))


def test_source_cards_and_terminology_do_not_count(mini_vault):
    _cleaned(mini_vault)    # the fixture's terminology table cites [DOC_A §3.2 p.3]
    assert "3.2 Frequency" in _titles(CS.check(str(mini_vault), min_chars=10))


def test_record_citation_covers_record(mini_vault, make_note):
    _cleaned(mini_vault)
    _note(make_note, "[DOC_A DL3-RC1 p.9]")
    assert "DL3-RC1 — Scram" not in _titles(CS.check(str(mini_vault), min_chars=10))


def test_exclusions_by_heading_and_pages(mini_vault):
    _cleaned(mini_vault)
    (mini_vault / "meta" / "coverage_exclusions.json").write_text(json.dumps(
        {"DOC_A": [{"heading": "^Unnumbered", "reason": "r"}, {"pages": "2", "reason": "r"}]}), encoding="utf-8")
    assert _titles(CS.check(str(mini_vault), min_chars=10)) == ["DL3-RC1 — Scram"]


def test_min_chars_skips_short_sections(mini_vault):
    _cleaned(mini_vault)
    assert CS.check(str(mini_vault), min_chars=1000) == []


def test_main_exit_code(mini_vault, monkeypatch, capsys):
    _cleaned(mini_vault)
    monkeypatch.setattr(CS, "VAULT", str(mini_vault))
    assert CS.main(["--min-chars", "10"]) == 1
    assert "uncited sections" in capsys.readouterr().out
    assert CS.main(["--min-chars", "1000"]) == 0


def test_partial_source_is_skipped_unless_named(mini_vault):
    import notes as N
    _cleaned(mini_vault)
    p = str(mini_vault / "wiki" / "DOC_A.md")
    fm, body = N.read_note(p)
    fm["ingest"] = "partial"
    N.write_note(p, fm, body)
    assert CS.check(str(mini_vault), min_chars=10) == []
    assert "3.2 Frequency" in _titles(CS.check(str(mini_vault), only="DOC_A", min_chars=10))
