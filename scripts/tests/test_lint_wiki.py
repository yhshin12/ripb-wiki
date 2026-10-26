import pytest

import lint_wiki as LW
import notes as N


def lint(vault, path):
    return [(f.code, f.level) for f in LW.lint_file(LW.Context(str(vault)), path)]


def test_good_note_card_and_terminology_are_clean(mini_vault, make_note, good_note_body):
    for p in (make_note("Sample", good_note_body), str(mini_vault / "wiki" / "DOC_A.md"),
              str(mini_vault / "wiki" / "Terminology.md")):
        assert lint(mini_vault, p) == [], p


@pytest.mark.parametrize("old,new,expected", [
    ("# 가나 시험 (Sample Concept)", "# 가나 시험", ("L06", "error")),
    ("> [!abstract] 요약\n", "", ("L06", "error")),
    ("## 해설", "## 설명", ("L06", "error")),
    ("- [[DOC_A]]", "- [[No_Such_Note]]", ("L08", "error")),
    ("- [[DOC_A]]", "- ![[missing.png]]", ("L08", "error")),
    ("- [[DOC_A]]", "- [DOC_A](DOC_A.md)", ("L09", "error")),
    ("- [[DOC_A]]", "- [[HELIOS_Anything]]", ("L10", "error")),
    ("- [[DOC_A]]", "- [[HSFR_Anything]]", ("L10", "error")),     # former prefix
    ("세 종류이다.", "세 종류이다. TBD", ("L07", "error")),
    ("세 종류이다.", "{한국어 2–3문장}", ("L07", "error")),
    ("가나(Licensing Basis Event)%%t:LBE%%에", "LBE%%t:LBE%%에", ("L11", "error")),     # first occurrence form
    ("LBE%%t:LBE%%는", "LBE%%t:LBE%%은", ("L11", "error")),                            # particle
    ("LBE%%t:LBE%%는", "LBE%%t:NOPE%%는", ("L11", "error")),                           # unknown ID
    ("세 종류이다.", "나가 세 종류이다.", ("L12", "error")),
    ("세 종류이다.", "RAC도 있다.", ("L13", "warning")),
    ("세 종류이다.", "XYZ도 있다. DL3-RC1은 식별자이다.", ("L14", "error")),
    ("세 종류이다.", "Reactor Air Cooling System%%t:RAC%%도 있다.", ("L15", "warning")),
])
def test_note_findings(mini_vault, make_note, good_note_body, old, new, expected):
    assert old in good_note_body
    assert expected in lint(mini_vault, make_note("Sample", good_note_body.replace(old, new)))


def test_abbreviation_ids_are_not_terms(mini_vault, make_note, good_note_body):
    body = good_note_body.replace("세 종류이다.", "DL3-RC1과 DHP-L1PP-BL은 식별자이다.")
    assert lint(mini_vault, make_note("Sample", body)) == []


def test_not_a_term_abbreviation_is_silent(mini_vault, make_note, good_note_body):
    t = mini_vault / "wiki" / "Terminology.md"
    rac = "| RAC | Reactor Air Cooling System | RAC |  | 약어 |  | [DOC_A §3.2 p.3] | 미정 | |"
    nrc = "| NRC | U.S. Nuclear Regulatory Commission | NRC |  |  |  | [DOC_A §3.2 p.3] | 용어 아님 | |"
    t.write_text(t.read_text(encoding="utf-8").replace(rac, rac + "\n" + nrc), encoding="utf-8", newline="\n")
    assert lint(mini_vault, make_note("Sample", good_note_body.replace("세 종류이다.", "NRC도 있다."))) == []


def test_frontmatter_filename_and_encoding(mini_vault, make_note, good_note_body):
    assert ("L04", "error") in lint(mini_vault, make_note("Typed", good_note_body, type="essay"))
    assert ("L04", "error") in lint(mini_vault, make_note("Checked", good_note_body, status="checked"))
    assert ("L05", "error") in lint(mini_vault, make_note("Keyless", good_note_body, sources=["DOC_Z"]))
    assert ("L03", "error") in lint(mini_vault, make_note("Bad Name", good_note_body))
    crlf = mini_vault / "wiki" / "Crlf.md"
    crlf.write_bytes(open(make_note("Tmp", good_note_body), "rb").read().replace(b"\n", b"\r\n"))
    assert ("L01", "error") in lint(mini_vault, str(crlf))
    broken = mini_vault / "wiki" / "Broken.md"
    broken.write_text("---\ntype: [\n---\n# x\n", encoding="utf-8", newline="\n")
    assert lint(mini_vault, str(broken)) == [("L02", "error")]


def test_card_rules(mini_vault):
    p = str(mini_vault / "wiki" / "DOC_A.md")
    fm, body = N.read_note(p)
    fm["ingest"] = "complete"
    N.write_note(p, fm, body)
    assert ("L07", "error") in lint(mini_vault, p)          # (인제스트 완료 시 작성) left after completion
    fm["ingest"], fm["units"] = "pending", [{"unit": "§1", "status": "complete", "commit": "abc"}]
    N.write_note(p, fm, body)
    assert ("L04", "error") in lint(mini_vault, p)          # units carry no commit field (P1)


def test_internal_link_rules(mini_vault, make_note, good_note_body):
    make_note("HELIOS_Secret", good_note_body, root="internal", type="helios")
    pub = make_note("Sample", good_note_body.replace("- [[DOC_A]]", "- [[HELIOS_Secret]]"))
    assert ("L10", "error") in lint(mini_vault, pub)
    assert lint(mini_vault, make_note("HELIOS_Other", good_note_body, root="internal", type="helios")) == []


def test_terminology_format_error(mini_vault):
    t = mini_vault / "wiki" / "Terminology.md"
    t.write_text(t.read_text(encoding="utf-8").replace("| 미정 |", "| 보류 |"), encoding="utf-8", newline="\n")
    assert ("L20", "error") in lint(mini_vault, str(t))


def test_cli_file_mode(mini_vault, make_note, good_note_body, monkeypatch, capsys):
    monkeypatch.setattr(LW, "VAULT", str(mini_vault))
    assert LW.main([make_note("Sample", good_note_body)]) == 0
    assert LW.main([make_note("Bad", good_note_body.replace("## 해설", "## 설명"))]) == 1
    out = capsys.readouterr().out
    assert "wiki/Bad.md" in out and "L06" in out


import shutil
import subprocess


def vault_codes(vault, root=None):
    return [(f.path, f.code, f.level) for f in LW.lint_vault(LW.Context(str(vault)), root)]


def test_clean_vault_has_no_vault_findings(mini_vault):
    assert vault_codes(mini_vault) == []


def test_name_collisions(mini_vault, make_note, good_note_body):
    make_note("Sample", good_note_body)
    make_note("SAMPLE", good_note_body, root="internal", type="helios")
    make_note("DOC_A_T", good_note_body)
    assert ("internal/wiki/SAMPLE.md", "L30", "error") in vault_codes(mini_vault, root="internal")
    assert ("wiki/DOC_A_T.md", "L30", "error") in vault_codes(mini_vault)


def test_alias_collisions(mini_vault, make_note, good_note_body):
    make_note("One", good_note_body, aliases=["공통"])
    make_note("Two", good_note_body, aliases=["공통", "one"])
    got = [(p, c) for p, c, _ in vault_codes(mini_vault)]
    assert got.count(("wiki/Two.md", "L31")) == 2 and ("wiki/One.md", "L31") not in got


def test_orphan_warning(mini_vault, make_note, good_note_body):
    make_note("Lonely", good_note_body)
    assert ("wiki/Lonely.md", "L32", "warning") in vault_codes(mini_vault)
    make_note("Hub", good_note_body.replace("- [[DOC_A]]", "- [[Lonely]]"), type="map")
    assert ("wiki/Lonely.md", "L32", "warning") not in vault_codes(mini_vault)


def test_reference_invariants(mini_vault):
    (mini_vault / "references" / "Orphan_Ref.md").write_text("x\n", encoding="utf-8", newline="\n")
    assert ("references/Orphan_Ref.md", "L34", "error") in vault_codes(mini_vault)
    p = str(mini_vault / "wiki" / "DOC_A.md")
    fm, body = N.read_note(p)
    fm["ingest"], fm["sha256_md"] = "complete", "0" * 64
    N.write_note(p, fm, body)
    assert ("wiki/DOC_A.md", "L34", "error") in vault_codes(mini_vault)
    (mini_vault / "references" / "DOC_A_T.md").unlink()
    assert ("wiki/DOC_A.md", "L34", "error") in vault_codes(mini_vault)


def test_reference_invariants_skipped_without_references_tree(mini_vault):
    shutil.rmtree(mini_vault / "references")
    assert vault_codes(mini_vault) == [("references", "L34", "warning")]


def test_git_tracked_local_paths_and_public_names(mini_vault, make_note, good_note_body):
    run = lambda *a: subprocess.run(["git", "-C", str(mini_vault), *a], check=True, capture_output=True)
    run("init", "-q")
    make_note("HELIOS_Trial", good_note_body, root="internal", type="helios", title="Zeta Loop Pump Trial")
    (mini_vault / "meta" / "status.md").write_text("다음: Zeta Loop Pump Trial 정리\n", encoding="utf-8", newline="\n")
    run("add", "meta/status.md", "wiki")
    run("add", "-f", "internal/wiki/HELIOS_Trial.md")
    got = vault_codes(mini_vault)
    assert ("internal/wiki/HELIOS_Trial.md", "L35", "error") in got
    assert ("meta/status.md", "L36", "error") in got
    assert not [g for g in vault_codes(mini_vault, root="internal") if g[1] in ("L35", "L36")]


def test_cli_all(mini_vault, monkeypatch):
    monkeypatch.setattr(LW, "VAULT", str(mini_vault))
    assert LW.main(["--all"]) == 0
    (mini_vault / "references" / "Orphan_Ref.md").write_text("x\n", encoding="utf-8", newline="\n")
    assert LW.main(["--all"]) == 1


def test_non_scalar_frontmatter_values_are_findings_not_crashes(mini_vault, make_note, good_note_body):
    # `type: {type}` left from templates/note.md parses as a YAML mapping
    assert ("L04", "error") in lint(mini_vault, make_note("DictType", good_note_body, type={"type": None}))
    assert ("L04", "error") in lint(mini_vault, make_note("DictStatus", good_note_body, status={"s": None}))
    p = str(mini_vault / "wiki" / "DOC_A.md")
    fm, body = N.read_note(p)
    fm["ingest"], fm["units"] = {"i": None}, [{"unit": "§1", "status": {"s": None}}]
    N.write_note(p, fm, body)
    assert lint(mini_vault, p).count(("L04", "error")) == 2
    assert isinstance(vault_codes(mini_vault), list)


def test_index_staleness(mini_vault, make_note, good_note_body):
    assert vault_codes(mini_vault) == []
    make_note("Sample", good_note_body)
    assert ("index.md", "L33", "error") in vault_codes(mini_vault)


def test_partial_card_rules(mini_vault):
    p = str(mini_vault / "wiki" / "DOC_A.md")
    fm, body = N.read_note(p)
    fm["ingest"], fm["units"] = "partial", [{"unit": "§1", "status": "complete"}]
    N.write_note(p, fm, body)
    got = lint(mini_vault, p)
    assert ("L04", "error") not in got                      # partial is a valid card state
    assert ("L07", "error") in got                          # the summary placeholder must be written
    fm["units"] = [{"unit": "§1", "status": "partial"}]
    N.write_note(p, fm, body)
    assert ("L04", "error") in lint(mini_vault, p)          # partial is not a unit state


def test_reference_invariants_apply_to_partial_cards(mini_vault):
    p = str(mini_vault / "wiki" / "DOC_A.md")
    fm, body = N.read_note(p)
    fm["ingest"], fm["sha256_md"] = "partial", "0" * 64
    N.write_note(p, fm, body)
    assert ("wiki/DOC_A.md", "L34", "error") in vault_codes(mini_vault)
