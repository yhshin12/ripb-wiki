"""session_start.py — the session start report for the Claude SessionStart hook (spec §7.1).

Usage: python scripts/session_start.py
Prints Markdown to stdout and always exits 0; a failing part becomes an '(오류: …)' line.
"""
import os
import re
import subprocess
import sys

import notes as N

SCRIPTS = os.path.dirname(os.path.abspath(__file__))
VAULT = os.path.dirname(SCRIPTS)
MAX = 15
NOTE_PATH = re.compile(r"^wiki/[^/]+\.md$")


def _read(path):
    with open(path, encoding="utf-8") as f:
        return f.read()


def _section(text, title):
    m = re.search(rf"^## {re.escape(title)}\n(.*?)(?=^## |\Z)", text, re.S | re.M)
    return m.group(1).strip() if m else ""


def changed_paths(repo):
    if not os.path.isdir(os.path.join(repo, ".git")):
        return None
    r = subprocess.run(["git", "-C", repo, "-c", "core.quotepath=false", "status", "--porcelain=v1", "-z",
                        "--untracked-files=all"], capture_output=True)
    if r.returncode != 0:
        return None
    toks, items, i = r.stdout.decode("utf-8", errors="replace").split("\0"), [], 0
    while i < len(toks):
        t = toks[i]
        if len(t) > 3:
            items.append((t[:2], t[3:]))
            if t[0] in "RC":
                i += 1
        i += 1
    return items


def part_status(vault):
    p = os.path.join(vault, "meta", "status.md")
    if not os.path.isfile(p):
        return "meta/status.md 없음"
    text = _read(p)
    return "\n".join(f"### {t}\n{_section(text, t) or '(비어 있음)'}" for t in ("현재 단계", "다음 작업", "미해결"))


def part_log(vault):
    heads = [l for l in _read(os.path.join(vault, "log.md")).split("\n") if l.startswith("## [")]
    return "\n".join(heads[-3:]) or "(항목 없음)"


def part_git(vault):
    lines = []
    for label, repo in (("git #1", vault), ("git #2 (internal)", os.path.join(vault, "internal"))):
        items = changed_paths(repo)
        if items is None:
            lines.append(f"- {label}: git 저장소 아님")
            continue
        lines.append(f"- {label}: 변경 {len(items)}건")
        lines += [f"  - {x} {p}" for x, p in items[:MAX]]
    return "\n".join(lines)


def part_terms(vault):
    import sync_terms
    try:
        ids = sync_terms.terms_changed(vault)
    except Exception as exc:
        return f"용어표 오류: {exc}"
    if not ids:
        return "변경 없음"
    return f"마지막 동기화 이후 변경 {len(ids)}건: {', '.join(ids)} → sync_terms.py 실행 필요"


def part_sources(vault):
    lines = []
    for label, d in (("inbox", os.path.join(vault, "inbox")), ("inbox/internal", os.path.join(vault, "inbox", "internal"))):
        files = sorted(f for f in (os.listdir(d) if os.path.isdir(d) else []) if os.path.isfile(os.path.join(d, f)))
        lines.append(f"- {label} 대기: {len(files)}" + (f" ({', '.join(files[:MAX])})" if files else ""))
    for key, c in sorted(N.load_cards(vault).items()):
        units = c["fm"].get("units") or []
        done = sum(1 for u in units if isinstance(u, dict) and u.get("status") == "complete")
        lines.append(f"- {key}: ingest {c['fm'].get('ingest')}, 단위 {done}/{len(units)}")
    return "\n".join(lines)


def _check(vault, paths, with_vault):
    import lint_wiki as LW
    import verify_quotes as VQ
    ctx = LW.Context(vault)
    src = VQ.Sources(vault, ctx.cards)
    lint, vq = [], []
    for p in paths:
        lint += LW.lint_file(ctx, p)
        try:
            vq += VQ.verify_note(vault, p, src)
        except (N.NoteError, UnicodeDecodeError) as exc:
            vq.append(N.Finding(N.relpath(p, vault), 1, "V0", str(exc)))
    if with_vault:
        lint += LW.lint_vault(ctx)
    return lint, vq


def part_checks(vault):
    lint, vq = _check(vault, N.wiki_notes(vault), True)
    errors = [f for f in lint + vq if f.level == "error"]
    lines = [f"- lint_wiki: 오류 {sum(f.level == 'error' for f in lint)}, 경고 {sum(f.level != 'error' for f in lint)}",
             f"- verify_quotes: 오류 {len(vq)}"]
    return "\n".join(lines + [f"  - {f}" for f in errors[:MAX]])


def part_edited(vault):
    paths = []
    for base, prefix in ((vault, ""), (os.path.join(vault, "internal"), "internal")):
        for x, p in (changed_paths(base) or []):
            if NOTE_PATH.match(p) and "D" not in x:
                paths.append(os.path.join(vault, prefix, p) if prefix else os.path.join(vault, p))
    if not paths:
        return "없음"
    lines = []
    for p in paths:
        lint, vq = _check(vault, [p], False)
        fs = lint + vq
        lines.append(f"- {N.relpath(p, vault)}: 오류 {sum(f.level == 'error' for f in fs)}, "
                     f"경고 {sum(f.level != 'error' for f in fs)}")
        lines += [f"  - {f}" for f in fs[:MAX]]
    return "\n".join(lines)


PARTS = [("상태 (meta/status.md)", part_status), ("log 최근 3건", part_log), ("git", part_git), ("용어표", part_terms),
         ("원문과 인제스트", part_sources), ("검사 (공개 트리)", part_checks), ("커밋되지 않은 노트 변경", part_edited)]


def report(vault):
    out = ["# ripb 세션 시작 보고 (scripts/session_start.py)"]
    for title, fn in PARTS:
        try:
            body = fn(vault)
        except Exception as exc:
            body = f"(오류: {type(exc).__name__}: {exc})"
        out.append(f"\n## {title}\n{body}")
    return "\n".join(out) + "\n"


def main(argv=None):
    sys.stdout.reconfigure(encoding="utf-8")
    try:
        print(report(VAULT))
    except Exception as exc:
        print(f"session_start: {type(exc).__name__}: {exc}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
