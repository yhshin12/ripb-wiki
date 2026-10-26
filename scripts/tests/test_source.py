import json
import os

import pytest

import source


def make_pdf(path, payload=b"%PDF-1.4 fake "):
    """A small fake PDF whose bytes differ per file name (so hashes differ unless made equal on purpose)."""
    with open(path, "wb") as f:
        f.write(payload + os.path.basename(str(path)).encode())
    return path


def test_safe_stem_strips_forbidden_chars():
    assert source.safe_stem("RG_1.233", 'Guidance: for a "Technology-Inclusive"/Method?') == \
        "RG_1.233_Guidance for a Technology-Inclusive Method"


def test_register_moves_pdf_and_writes_card(vault):
    pdf = make_pdf(vault / "inbox" / "some file.pdf")
    card = source.register(str(pdf), key="DOC_A", title="Some Title", root=None)
    assert not pdf.exists()
    assert (vault / "references" / "raw" / "DOC_A_Some Title.pdf").exists()
    fm, body = source.read_note(card)
    assert fm["type"] == "source" and fm["key"] == "DOC_A" and fm["ingest"] == "pending"
    assert fm["pdf"] == "references/raw/DOC_A_Some Title.pdf"
    assert fm["sha256_pdf"] == source.sha256(str(vault / "references" / "raw" / "DOC_A_Some Title.pdf"))
    assert fm["file"] == "" and fm["units"] == []
    assert "# Some Title (DOC_A)" in body and "<!-- sync:begin -->" in body


def test_register_internal_goes_to_internal_tree(vault):
    pdf = make_pdf(vault / "inbox" / "internal" / "secret.pdf")
    card = source.register(str(pdf), key="HELIOS_X", title="Design Note", root="internal")
    assert (vault / "internal" / "references" / "raw" / "HELIOS_X_Design Note.pdf").exists()
    assert card.startswith(str(vault / "internal" / "wiki"))
    fm, _ = source.read_note(card)
    assert fm["pdf"] == "internal/references/raw/HELIOS_X_Design Note.pdf"


def test_register_refuses_duplicate_by_hash(vault):
    a = make_pdf(vault / "inbox" / "a.pdf", b"SAME")
    source.register(str(a), key="DOC_A", title="T", root=None)
    b = make_pdf(vault / "inbox" / "b.pdf", b"SAME")
    # same bytes except the trailing file name -> make them truly identical
    with open(b, "wb") as f, open(vault / "references" / "raw" / "DOC_A_T.pdf", "rb") as g:
        f.write(g.read())
    with pytest.raises(source.SourceError, match="duplicate of references/raw/DOC_A_T.pdf"):
        source.register(str(b), key="DOC_B", title="T2", root=None)
    assert b.exists()


def test_register_refuses_existing_key(vault):
    a = make_pdf(vault / "inbox" / "a.pdf")
    source.register(str(a), key="DOC_A", title="T", root=None)
    b = make_pdf(vault / "inbox" / "b.pdf")
    with pytest.raises(source.SourceError, match="card exists"):
        source.register(str(b), key="DOC_A", title="T", root=None)


def _cleaned(vault, stem, root=None):
    base = vault / "internal" if root else vault
    p = base / "references" / f"{stem}.md"
    p.write_text('---\ndoc_id: "X"\npdf_pages: 12\ntables:\n  - "Table 1 A"\nfigures:\n  - "Figure 1 B"\n'
                 'withheld: []\npage_labels: "p1 = i"\nconverter: "odl 2.5.7"\ncleaned: "clean 2026-09-14"\n---\n\nbody\n',
                 encoding="utf-8")
    vdir = base / "references" / "raw" / "_verify"
    vdir.mkdir(exist_ok=True)
    (vdir / "DOC_A.json").write_text(json.dumps({"verify": {"summary": {"missing_pct": 0.42}}}), encoding="utf-8")
    return p


def test_adopt_creates_card_from_registry(vault):
    make_pdf(vault / "references" / "raw" / "DOC_A_Some Title.pdf")
    card = source.adopt("DOC_A", root=None)
    fm, _ = source.read_note(card)
    assert fm["key"] == "DOC_A" and fm["title"] == "Some Title" and fm["ingest"] == "pending"


def test_sync_fills_build_fields_and_block(vault):
    make_pdf(vault / "references" / "raw" / "DOC_A_Some Title.pdf")
    card = source.adopt("DOC_A", root=None)
    cleaned = _cleaned(vault, "DOC_A_Some Title")
    source.sync("DOC_A", root=None)
    fm, body = source.read_note(card)
    assert fm["file"] == "references/DOC_A_Some Title.md"
    assert fm["sha256_md"] == source.sha256(str(cleaned))
    assert fm["pdf_pages"] == 12
    assert fm["build"] == {"converter": "odl 2.5.7", "cleaned": "clean 2026-09-14", "missing_pct": 0.42}
    block = body.split("<!-- sync:begin -->")[1].split("<!-- sync:end -->")[0]
    assert "Table 1 A" in block and "Figure 1 B" in block and "p1 = i" in block


def test_sync_without_cleaned_file_leaves_file_empty(vault):
    make_pdf(vault / "references" / "raw" / "DOC_A_Some Title.pdf")
    card = source.adopt("DOC_A", root=None)
    source.sync("DOC_A", root=None)
    fm, _ = source.read_note(card)
    assert fm["file"] == "" and fm["build"] == {}


def test_finish_requires_cleaned_file_and_completed_units(vault):
    make_pdf(vault / "references" / "raw" / "DOC_A_Some Title.pdf")
    card = source.adopt("DOC_A", root=None)
    with pytest.raises(source.SourceError, match="no cleaned file"):
        source.finish("DOC_A", root=None)
    _cleaned(vault, "DOC_A_Some Title")
    fm, body = source.read_note(card)
    fm["units"] = [{"unit": "§1", "status": "complete", "commit": "abc"}, {"unit": "§2", "status": "pending", "commit": ""}]
    source.write_note(card, fm, body)
    with pytest.raises(source.SourceError, match="units not complete"):
        source.finish("DOC_A", root=None)
    fm["units"][1]["status"] = "complete"
    source.write_note(card, fm, body)
    source.finish("DOC_A", root=None)
    fm, _ = source.read_note(card)
    assert fm["ingest"] == "complete" and fm["sha256_md"]


def test_status_lists_cards(vault, capsys):
    make_pdf(vault / "references" / "raw" / "DOC_A_Some Title.pdf")
    source.adopt("DOC_A", root=None)
    source.status(root=None)
    out = capsys.readouterr().out
    assert "DOC_A" in out and "pending" in out


def test_write_note_is_utf8_lf_without_bom(vault):
    p = vault / "wiki" / "N.md"
    source.write_note(str(p), {"type": "source", "title": "한글"}, "본문\n")
    raw = p.read_bytes()
    assert not raw.startswith(b"\xef\xbb\xbf") and b"\r" not in raw
    fm, body = source.read_note(str(p))
    assert fm["title"] == "한글" and body == "본문\n"


def test_status_ignores_subdirectories(vault):
    os.makedirs(vault / "wiki" / "assets")
    make_pdf(vault / "references" / "raw" / "DOC_A_Some Title.pdf")
    source.adopt("DOC_A", root=None)
    rows = source.status(root=None)
    assert any(r[0] == "DOC_A" for r in rows)


def test_read_note_bad_frontmatter_raises(tmp_path):
    unclosed = tmp_path / "unclosed.md"
    unclosed.write_text("---\ntype: source\n", encoding="utf-8")
    with pytest.raises(source.SourceError, match="bad frontmatter"):
        source.read_note(str(unclosed))

    bad_yaml = tmp_path / "bad_yaml.md"
    bad_yaml.write_text("---\ntags: [a, b\n---\nbody\n", encoding="utf-8")
    with pytest.raises(source.SourceError, match="bad frontmatter"):
        source.read_note(str(bad_yaml))


def test_malformed_note_does_not_block_register_or_status(vault, capsys):
    broken = vault / "wiki" / "Broken.md"
    broken.write_text("---\ntype: source\n", encoding="utf-8")
    pdf = make_pdf(vault / "inbox" / "new.pdf")
    source.register(str(pdf), key="DOC_B", title="New Doc", root=None)
    capsys.readouterr()
    source.status(root=None)
    out, err = capsys.readouterr()
    assert "DOC_B" in out
    assert "wiki/Broken.md" in err


def test_sync_preserves_backslashes_in_captions(vault):
    make_pdf(vault / "references" / "raw" / "DOC_A_Some Title.pdf")
    card = source.adopt("DOC_A", root=None)
    cleaned = vault / "references" / "DOC_A_Some Title.md"
    cleaned.write_text(
        '---\ndoc_id: "X"\npdf_pages: 12\n'
        "tables:\n  - 'Table 1 A \\ B \\1 end'\n"
        "figures: []\nwithheld: []\n"
        'page_labels: "p1 = i"\nconverter: "odl 2.5.7"\ncleaned: "clean 2026-09-14"\n---\n\nbody\n',
        encoding="utf-8",
    )
    source.sync("DOC_A", root=None)
    _, body = source.read_note(card)
    assert "Table 1 A \\ B \\1 end" in body


def test_sync_all_uses_each_cards_own_root(vault, monkeypatch):
    make_pdf(vault / "references" / "raw" / "DOC_A_Some Title.pdf")
    public_card = source.adopt("DOC_A", root=None)
    internal_pdf = make_pdf(vault / "inbox" / "internal" / "n.pdf")
    internal_card = source.register(str(internal_pdf), key="HELIOS_X", title="Design Note", root="internal")
    _cleaned(vault, "DOC_A_Some Title")
    _cleaned(vault, "HELIOS_X_Design Note", root="internal")
    monkeypatch.setattr("sys.argv", ["source.py", "sync", "--all"])
    source.main()
    fm_pub, _ = source.read_note(public_card)
    fm_int, _ = source.read_note(internal_card)
    assert fm_pub["file"] == "references/DOC_A_Some Title.md"
    assert fm_int["file"] == "internal/references/HELIOS_X_Design Note.md"


import sys


def test_source_error_is_note_error():
    import notes
    assert source.SourceError is notes.NoteError


def test_register_rolls_back_when_card_creation_fails(vault, monkeypatch):
    pdf = make_pdf(vault / "inbox" / "a.pdf")

    def boom(*a, **k):
        raise OSError("disk full")

    monkeypatch.setattr(source, "_new_card", boom)
    with pytest.raises(OSError):
        source.register(str(pdf), key="DOC_A", title="T", root=None)
    assert pdf.exists()
    assert not (vault / "references" / "raw" / "DOC_A_T.pdf").exists()


def test_load_docs_inserts_scripts_dir_once():
    # other test modules may already have put scripts/ on sys.path; load_docs must not add another copy
    before = sys.path.count(source.SCRIPTS)
    source.load_docs()
    source.load_docs()
    assert sys.path.count(source.SCRIPTS) == max(before, 1)


def test_register_refuses_key_used_in_other_tree(vault):
    source.register(str(make_pdf(vault / "inbox" / "internal" / "n.pdf")), key="HELIOS_X", title="Design Note",
                    root="internal")
    with pytest.raises(source.SourceError, match="card exists"):
        source.register(str(make_pdf(vault / "inbox" / "p.pdf")), key="HELIOS_X", title="Other", root=None)


def test_sync_raises_when_markers_missing(vault):
    make_pdf(vault / "references" / "raw" / "DOC_A_Some Title.pdf")
    card = source.adopt("DOC_A", root=None)
    fm, body = source.read_note(card)
    source.write_note(card, fm, body.replace("<!-- sync:end -->", ""))
    _cleaned(vault, "DOC_A_Some Title")
    with pytest.raises(source.SourceError, match="sync markers missing"):
        source.sync("DOC_A", root=None)


def test_write_note_rejects_cr(vault):
    with pytest.raises(source.SourceError, match="CR"):
        source.write_note(str(vault / "wiki" / "N.md"), {"type": "source"}, "a\r\nb\n")


def test_status_reports_missing_cleaned_file(vault):
    make_pdf(vault / "references" / "raw" / "DOC_A_Some Title.pdf")
    source.adopt("DOC_A", root=None)
    cleaned = _cleaned(vault, "DOC_A_Some Title")
    source.sync("DOC_A", root=None)
    cleaned.unlink()
    rows = source.status(root=None)
    assert [r[4] for r in rows if r[0] == "DOC_A"] == ["MISSING"]


def test_register_detects_duplicate_even_if_card_is_malformed(vault):
    source.register(str(make_pdf(vault / "inbox" / "a.pdf", b"SAME")), key="DOC_A", title="T", root=None)
    (vault / "wiki" / "DOC_A.md").write_text("---\ntype: source\n", encoding="utf-8")
    second = vault / "inbox" / "b.pdf"
    second.write_bytes((vault / "references" / "raw" / "DOC_A_T.pdf").read_bytes())
    with pytest.raises(source.SourceError, match="duplicate of references/raw/DOC_A_T.pdf"):
        source.register(str(second), key="DOC_B", title="T2", root=None)
    assert second.exists()


def test_finish_partial_marks_on_demand_source(vault):
    make_pdf(vault / "references" / "raw" / "DOC_A_Some Title.pdf")
    card = source.adopt("DOC_A", root=None)
    _cleaned(vault, "DOC_A_Some Title")
    with pytest.raises(source.SourceError, match="no completed unit"):
        source.finish("DOC_A", root=None, partial=True)
    fm, body = source.read_note(card)
    fm["units"] = [{"unit": "§4.1", "status": "in_progress"}]
    source.write_note(card, fm, body)
    with pytest.raises(source.SourceError, match="units not complete"):
        source.finish("DOC_A", root=None, partial=True)
    fm["units"][0]["status"] = "complete"
    source.write_note(card, fm, body)
    source.finish("DOC_A", root=None, partial=True)
    fm, _ = source.read_note(card)
    assert fm["ingest"] == "partial" and fm["sha256_md"]
