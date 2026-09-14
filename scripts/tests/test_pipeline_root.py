"""--root: the pipeline reads/writes under <vault>/<root>/references (spec §4.2, internal documents)."""
import os
import sys

SCRIPTS = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
VAULT = os.path.dirname(SCRIPTS)
sys.path.insert(0, SCRIPTS)

import clean_references as CR  # noqa: E402
import convert_references as CV  # noqa: E402


def test_raw_dir_for_default_and_internal():
    assert CV.raw_dir_for(None) == os.path.join(VAULT, "references", "raw")
    assert CV.raw_dir_for("internal") == os.path.join(VAULT, "internal", "references", "raw")


def test_set_root_switches_raw_and_out():
    try:
        CR.set_root("internal")
        assert CR.RAW == os.path.join(VAULT, "internal", "references", "raw")
        assert CR.OUT == os.path.join(VAULT, "internal", "references")
    finally:
        CR.set_root(None)
    assert CR.RAW == os.path.join(VAULT, "references", "raw")
    assert CR.OUT == os.path.join(VAULT, "references")


def test_relocate_paths_rewrites_only_path_fields():
    meta = {"source_pdf": "references/raw/X.pdf", "raw_json": "references/raw/X.json",
            "raw_md": "references/raw/X.md", "raw_json_tables": "references/raw/X.structtree.json",
            "title": "references/raw/not-a-path"}
    out = CR.relocate_paths(dict(meta), os.path.join(VAULT, "internal", "references", "raw"))
    assert out["source_pdf"] == "internal/references/raw/X.pdf"
    assert out["raw_json_tables"] == "internal/references/raw/X.structtree.json"
    assert out["title"] == "references/raw/not-a-path"
    same = CR.relocate_paths(dict(meta), os.path.join(VAULT, "references", "raw"))
    assert same["source_pdf"] == "references/raw/X.pdf"
