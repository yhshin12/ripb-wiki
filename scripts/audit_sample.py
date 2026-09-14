"""audit_sample.py — sample re-verification of checked notes (spec §7.4; skill wiki-audit).

Usage:
  python scripts/audit_sample.py sample [--n 10] [--seed INT] [--out DIR]
  python scripts/audit_sample.py summarize DIR
`sample` writes DIR/sample.json and DIR/<Note>.prompt.md. The main session gives each prompt to a read-only subagent
and saves its JSON answer as DIR/<Note>.result.json; `summarize` prints the meta/metrics.md row.
The seed defaults to the date (YYYYMMDD) so a sample can be redrawn.
The comparison prompt is defined here from spec §1 and §7.4; the 2026-09-11 audit prompt was not kept on disk.
"""
import argparse
import datetime
import json
import os
import random
import sys
import tempfile

import citations as C
import notes as N

SCRIPTS = os.path.dirname(os.path.abspath(__file__))
VAULT = os.path.dirname(SCRIPTS)
EXCLUDED = {"source", "map"}
FACT_VERDICTS = {"일치", "경미", "불일치", "원문 없음", "판정 불가"}
COMMENT_VERDICTS = {"근거 있음", "과잉 일반화", "원문 사실에 없음", "원문과 모순", "판정 불가"}
ERRORS = {"불일치", "원문 없음", "원문 사실에 없음", "원문과 모순"}

PROMPT = """# 표본 재검증: `{note}`

역할: 원문 대조 검증자. 읽기 전용 작업이며 파일을 수정하지 않는다. vault 원문(정제본과 PDF) 밖의 배경지식으로 판정하지 않는다.

## 대상
- 노트: `{note}`
- 원문:
{sources}
- 원문 사실 절의 인용:
{cites}

## 절차
1. 노트 전체를 읽는다.
2. `## 원문 사실`의 항목·표 행마다 인용한 정제본의 쪽 표지 `<!-- page N | … -->` 구간(±1쪽)을 읽고 판정한다. 정제본이 모호하면 PDF의 같은 쪽을 연다.
   판정: `일치` / `경미`(쪽·절 번호 오류, 뜻을 바꾸지 않는 생략) / `불일치`(원문과 다른 낱말·수치·주체·조건) / `원문 없음`(인용 위치와 문서 전체에서 찾지 못함) / `판정 불가`.
3. `> [!abstract] 요약`과 `## 해설`의 문장마다 판정한다.
   판정: `근거 있음`(근거가 된 원문 사실의 줄 번호) / `과잉 일반화`(원문 사실의 범위를 넘는 일반화) / `원문 사실에 없음` / `원문과 모순` / `판정 불가`.
4. 판정마다 원문 문장을 짧게 인용하고 `[KEY p.N]`을 붙인다.

## 출력
JSON 하나만 출력한다.
{{"note": "{note}", "facts": [{{"line": 0, "verdict": "일치", "evidence": "… [KEY p.N]"}}], "commentary": [{{"sentence": "…", "verdict": "근거 있음", "basis": "원문 사실 줄 0"}}]}}
"""


class AuditError(Exception):
    pass


def population(vault):
    out = []
    for p in N.wiki_notes(vault):
        try:
            fm, _ = N.read_note(p)
        except N.NoteError:
            continue
        if fm.get("status") == "checked" and isinstance(fm.get("type"), str) and fm.get("type") not in EXCLUDED:
            out.append(p)
    return out


def _citations(note):
    secs = {t: lines for t, _, lines in N.sections(note)}
    found = []
    for ln, line in secs.get("원문 사실", []):
        s = line.strip()
        if s.startswith("|"):
            s = [c.strip() for c in s.strip("|").split("|")][-1]
        found += [(ln, c) for c in C.split_trailing(s)[1]]
    return found


def prompt_for(vault, path, cards):
    note, rel = N.load(path), N.relpath(path, vault)
    cites = _citations(note)
    sources = []
    for key in sorted({c.key for _, c in cites}):
        fm = cards.get(key, {}).get("fm", {})
        sources.append(f"  - `{key}`: 정제본 `{fm.get('file') or '(카드 없음)'}`, PDF `{fm.get('pdf') or ''}`")
    return PROMPT.format(note=rel, sources="\n".join(sources) or "  - (인용 없음)",
                         cites="\n".join(f"  - 줄 {ln}: {c.raw}" for ln, c in cites) or "  - (인용 없음)")


def sample(vault, n, seed, out):
    pop = population(vault)
    chosen = sorted(random.Random(seed).sample(pop, min(n, len(pop))))
    os.makedirs(out, exist_ok=True)
    cards = N.load_cards(vault)
    for p in chosen:
        N.write_text(os.path.join(out, os.path.basename(p)[:-3] + ".prompt.md"), prompt_for(vault, p, cards))
    meta = {"date": datetime.date.today().isoformat(), "seed": seed, "population": len(pop),
            "notes": [N.relpath(p, vault) for p in chosen]}
    N.write_text(os.path.join(out, "sample.json"), json.dumps(meta, ensure_ascii=False, indent=1))
    return meta


def summarize(out):
    with open(os.path.join(out, "sample.json"), encoding="utf-8") as f:
        meta = json.load(f)
    missing = [os.path.basename(r)[:-3] for r in meta["notes"]
               if not os.path.isfile(os.path.join(out, os.path.basename(r)[:-3] + ".result.json"))]
    if missing:
        raise AuditError("result files missing: " + ", ".join(missing))
    bad_notes = facts = bad_facts = minor = 0
    for r in meta["notes"]:
        with open(os.path.join(out, os.path.basename(r)[:-3] + ".result.json"), encoding="utf-8") as f:
            res = json.load(f)
        fv = [x.get("verdict") for x in res.get("facts", [])]
        cv = [x.get("verdict") for x in res.get("commentary", [])]
        wrong = [v for v in fv if v not in FACT_VERDICTS] + [v for v in cv if v not in COMMENT_VERDICTS]
        if wrong:
            raise AuditError(f"{r}: unknown verdict {wrong[0]!r}")
        facts += len(fv)
        bad_facts += sum(v in ERRORS for v in fv)
        minor += sum(v == "경미" for v in fv)
        bad_notes += any(v in ERRORS for v in fv + cv)
    n = len(meta["notes"])
    rate = 100 * bad_notes / n if n else 0.0
    return (f"| {meta['date']} | {meta['seed']} | {n}/{meta['population']} | {bad_notes} | {rate:.0f} % | "
            f"{bad_facts}/{facts} | {minor} |")


def main(argv=None):
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    s = sub.add_parser("sample")
    s.add_argument("--n", type=int, default=10)
    s.add_argument("--seed", type=int, default=int(datetime.date.today().strftime("%Y%m%d")))
    s.add_argument("--out", default=os.path.join(tempfile.gettempdir(), "ripb_audit_" + datetime.date.today().isoformat()))
    m = sub.add_parser("summarize")
    m.add_argument("out")
    a = ap.parse_args(argv)
    sys.stdout.reconfigure(encoding="utf-8")
    try:
        if a.cmd == "sample":
            meta = sample(VAULT, a.n, a.seed, a.out)
            print(f"audit_sample: {len(meta['notes'])} of {meta['population']} checked notes, seed {meta['seed']} → {a.out}")
        else:
            print(summarize(a.out))
    except (AuditError, OSError, json.JSONDecodeError) as exc:
        print(f"audit_sample: error: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
