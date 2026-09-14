# Vault Rebuild — Phase 2 (도구) Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** 설계 §8의 도구(스크립트 7종과 보조 모듈, 템플릿 3종, 빈 용어표, hook 3종, skill 5종, Shell Commands, Bases 보기 4종)를 테스트 우선으로 구현하고, Phase 1에서 넘긴 후속 항목을 모두 처리하여 Phase 3 시범 인제스트를 시작할 수 있는 상태로 만든다.

**Architecture:** 공통 기능은 세 보조 모듈로 모은다. `scripts/notes.py`(노트 입출력·절 분할·카드 조회), `scripts/citations.py`(인용 구문·쪽 분할·텍스트 정규화), `scripts/terms.py`(용어표 파싱·표기·조사). 검사 스크립트(`lint_wiki.py`, `verify_quotes.py`)와 변경 스크립트(`sync_terms.py`, `build_index.py`, `append_log.py`)는 이 모듈만 쓰며, 모든 함수는 vault 경로를 인자로 받아 임시 vault에서 시험한다. hook은 이 스크립트를 부르는 얇은 진입점(`hook_post_edit.py`, `session_start.py`, `.githooks/pre-commit`)이다. 정제 파이프라인(`scripts/refclean/`)의 동작은 바꾸지 않는다(Task 3의 함수 이동은 출력 동일성으로 검증).

**Tech Stack:** Python 3.12 (`C:\Code\Python\pykaeri\.venv12\Scripts\python.exe`, PyYAML 6.0.3, pytest 9.0.3, PyMuPDF), Git for Windows (Git Bash), Claude Code hooks·skills, Obsidian 1.9+ (Bases 코어 플러그인 활성), obsidian-shellcommands 0.23.0.

**Spec:** `meta/design/2026-09-14-vault-rebuild-design.md` (§5 노트·인용, §6 용어, §7 운영, §8 도구, §9.4 Phase 2). 선행 계획: `meta/design/2026-09-14-rebuild-plan-phase0-1.md`.

## Global Constraints

- Python: 항상 `C:\Code\Python\pykaeri\.venv12\Scripts\python.exe`(아래 `$PY`). Git Bash에서는 `PY=/c/Code/Python/pykaeri/.venv12/Scripts/python.exe`. PATH의 `python`은 쓰지 않는다.
- 모든 명령은 vault 루트 `/c/Obsidian/ripb`에서 실행한다.
- `references/`, `references/raw/`, `inbox/`의 파일 내용은 어떤 스크립트도 바꾸지 않는다. 테스트는 `tmp_path`의 임시 vault만 쓴다. (설계 §8.1)
- 일괄 수정 스크립트는 dry-run이 기본이고 `--apply`로만 쓴다. 검사 실패는 종료 코드 1, 사용법 오류는 2. (설계 §8.1)
- 파일 쓰기: UTF-8(BOM 없음), LF, `encoding="utf-8", newline="\n"`. 쓰기 전에 문자열을 검증한다(`notes.write_text`만 사용). (설계 §3.2, §8.1)
- 공개 파일(`wiki/`, `meta/`, `log.md`, `index.md`, `CLAUDE.md`, `.claude/`, 이 계획)에는 내부 문서의 이름·키·제목을 쓰지 않는다. 테스트의 내부 문서 예시는 `HSFR_X`, `Design Note`처럼 가공의 이름만 쓴다. (설계 §3.3)
- 테스트: 새 스크립트 테스트는 `scripts/tests/`. 수용 관문은 `$PY -m pytest scripts/refclean/tests scripts/tests -q` 전부 통과. 현재 기준 234건(refclean 215 + scripts 19); 각 Task가 늘어난 건수를 적는다.
- 커밋: `<type>(<scope>): <subject>`(type: feat, fix, test, docs, chore, refactor), 메시지 끝에 `Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>`. push는 사용자가 요청할 때만. (설계 D7)
- **확인 지점** 표시가 있는 단계는 실행자가 멈추고 사용자에게 명령과 효과를 보인 뒤 명시적 승인을 기다린다. 서브에이전트는 확인 지점을 직접 실행하지 않고 본 세션에 보고한다.
- 한국어 용어 표기를 추측하지 않는다. 테스트의 한국어 표기는 조사 규칙을 시험하기 위한 가공 문자열(`가나`, `가닥`, `가날`)만 쓴다. (설계 D5)

---

## 계획 단계의 결정 (Task 0에서 사용자 확인)

설계가 정하지 않았거나 구현 중 드러난 모순을 아래와 같이 정한다. 각 항목은 권고안이며, Task 0에서 사용자가 승인하거나 바꾼 결과를 이 절에 기록한 뒤 구현한다.

| ID | 사안 | 권고 | 근거 |
|---|---|---|---|
| P1 | log 항목과 소스 카드 `units[].commit`에 커밋 해시를 쓰는 규칙(설계 §7.5, 부록 B) | 자기 커밋의 해시는 기록하지 않는다. `units` 항목은 `{unit, status}`만 둔다. 해시는 `git log -- log.md`로 찾는다 | log 추가와 커밋이 같은 커밋이므로 해시를 미리 알 수 없다. 사후 기입은 매번 별도 커밋을 만든다 |
| P2 | 용어 상태별 표시 형식 | 확정: 첫 등장 `한국어(English)`, 이후 `이후 표기` 열이 `약어`면 약어, `한국어`면 한국어. 영어 유지·미정: 첫 등장 `English`, 이후 `이후 표기`가 `약어`이고 약어가 있으면 약어, 아니면 English. 용어 아님: 표지를 두지 않는다(lint 오류, `sync_terms --apply`가 표지만 제거) | 설계 §6.2는 확정 용어의 형식만 정한다. §6.3의 "답이 없는 용어는 영어로 쓰고 표지만 달아 둔다"를 형식으로 옮겼다 |
| P3 | 영어 표기 뒤 조사 | 약어(대문자·숫자)는 마지막 글자의 한국어 읽기로 판단한다. 영어 단어(소문자 포함)는 자동 교정하지 않고 dry-run 보고에 "조사 확인 필요"로 싣는다 | 설계 §6.2는 약어만 규칙을 준다. 영어 단어의 발음은 철자로 판정할 수 없다 |
| P4 | `wiki/Terminology.md`의 frontmatter | `type: map`, `status: draft`. lint의 노트 절 구조 검사에서 제외하고 표 형식 검사만 한다 | `type` 열거값(§5.1) 안에서 고른다 |
| P5 | Bases "미정 용어 목록" 보기 | `sync_terms.py`가 각 노트 frontmatter에 `terms_pending: [ID…]`(미정 상태 표지 ID)를 유지하고, Base는 `terms_pending`이 비어 있지 않은 노트를 보인다. 용어표 자체의 미정 행은 Terminology.md를 연다 | Bases는 노트 속성만 거를 수 있고 Markdown 표의 행은 거를 수 없다 |
| P6 | 인용 비교의 정규화 세부 | 양쪽에 같은 정규화: HTML 주석·`[!withheld]` callout 전체·callout 머리줄·`<sup>…</sup>`(내용 포함)·각주 참조 `[^n]`·블록 ID `^id`·이미지 embed 제거, 그 밖의 HTML 태그는 태그만 제거, `**`·`*` 강조 제거, `\x` 이스케이프 해제, 제목·목록·인용 접두어와 표 구분자 제거, 굽은 따옴표→곧은 따옴표, en·em dash→`-`, 공백 하나로 압축. `...`·`…`로 나뉜 조각은 3단어 이상이어야 한다 | 설계 §5.4-3을 구현 가능한 규칙으로 옮겼다. `<sup>`는 정제본에서 표 주석 번호로만 쓰인다(지수는 E 표기로 정규화됨). 조각 최소 길이는 한두 단어 조각이 우연히 일치하는 것을 막는다 |
| P7 | 해설의 약어 검사(설계 §5.4-6) | 해설·요약에서 표지 없이 쓰인 토큰 중 `^[A-Z]{2,6}s?$`(숫자·하이픈 없음)만 대상으로 한다. 용어표에 없으면 오류, 용어표에 있는데 표지가 없으면 경고. `DL3-RC1`, `DHP-L1PP-BL`, `SFR-DC` 같은 ID와 소스 키는 대상이 아니다 | LBE·PSF ID까지 등록을 요구하면 용어표가 ID 목록이 된다. Phase 3 시범에서 보정한다 |
| P8 | 노트 종류별 필수 절 | concept·regulation·natrium·hsfr: H1, 요약 callout, `## 원문 사실`, `## 해설`, `## 관련 문서`(이 순서). synthesis·map: H1, 요약 callout, `## 관련 문서`. source: `templates/source_card.md`의 절(H1, 요약, `## 서지`, `## 구조`, `## 알려진 모순`, `## 관련 문서`) | 설계 §5.1 틀은 하나이지만 synthesis(재구성)와 map(목록)은 원문 사실 절을 갖지 않는다 |
| P9 | Bases 파일 위치 | `meta/views/*.base` | 설계 §3.1은 기계적 경계에만 폴더를 둔다. 보기 파일은 노트가 아니다 |
| P10 | 공개 파일의 내부 문서명 검사 이름 목록 | 커밋 시점에 `internal/`을 읽어 만든다(내부 원문·정제본 stem과 그 제목 부분, 내부 노트의 파일명·`title`·H1·aliases, `internal/meetings/`의 파일명·H1). 8자 미만 이름은 제외한다. 오탐 예외 목록은 `internal/leak_allow.txt`(내부 저장소)에 둔다 | 이름 목록을 공개 저장소에 두면 그 자체가 유출이다(R14) |

**확정 (2026-09-14):** P1–P10 모두 권고안대로 승인.

---

## Phase 1에서 넘긴 항목의 대응

| 항목 | 처리 Task |
|---|---|
| `source.py`: register 실패 시 되돌리기, `load_docs`의 `sys.path` 중복 삽입, 공개·내부 트리 간 키 충돌, sync 표지 누락 시 오류, `assert "\r"` 대체, status의 MISSING 상태, 손상된 카드가 중복 검사를 건너뛰는 문제(R20) | Task 2 |
| `generic.py`: 미등록 키의 명확한 오류, `assign_levels`를 `psar`에서 가져오는 의존 | Task 3 |
| 설계 부록 B 카드 필드와 §8.1 "이동만" 문구 수정 | Task 4 |
| pre-commit의 내부 문서명 내용 검사(설계 §8.2, R14) | Task 5 |
| `.obsidian` Shell Commands가 Gemini CLI를 실행함 | Task 16 |
| `internal/.gitattributes` binary 목록, CLAUDE.md §7 hook 요약 | Task 4, Task 18 |
| 원문 파일에 의존하는 테스트의 pytest marker | Task 1 |
| ACRS 슬라이드: 캡션 없는 그림 37개, 슬라이드 제목 미추출(R18) — 인제스트 전 방침 결정 | Task 19 (결정만; 구현은 Phase 3에서 부록 A 10번 전) |
| 커밋 작성자 이메일(개인 Gmail) — 첫 push 전 확인 | 해소됨: 2026-09-14 사용자 결정으로 push 완료. 이후 push도 요청 시에만 |

---

## 세션 구분

| 세션 | Task | 끝 상태 |
|---|---|---|
| A | 0–5 | 결정 확정, 테스트 marker, source·generic 보강, 설계 수정, 내부 문서명 관문 |
| B | 6–11 | `notes`·`citations`·`terms`, 템플릿·용어표, `verify_quotes`, `lint_wiki`, `build_index`·`append_log` |
| C | 12–19 | `sync_terms`, `session_start`, `audit_sample`, hook, skill, Shell Commands, Bases, 마무리, ACRS 결정 |

세션 사이에는 `meta/status.md`의 "다음 작업"에 다음 Task 번호를 적는다.

---

## File Structure

| Path | 책임 | Task |
|---|---|---|
| `scripts/pytest.ini`, `scripts/refclean/tests/conftest.py` | `refs` marker 등록, 원문 부재 시 skip, 표시 누락 감시 | 1 |
| `scripts/refclean/tests/test_*.py` (원문을 읽는 테스트) | `@pytest.mark.refs` 부착 | 1 |
| `scripts/notes.py` | `NoteError`, `read_note`, `write_note`, `write_text`, `sections`, `wiki_notes`, `load_cards`, `tree` | 2 (입출력), 6 (나머지) |
| `scripts/source.py`, `scripts/tests/test_source.py` | 후속 7건 보강 | 2 |
| `scripts/refclean/levels.py`, `profiles/psar.py`, `profiles/generic.py`, `tests/test_generic.py` | `assign_levels` 공용화, 미등록 키 오류 | 3 |
| `meta/design/2026-09-14-vault-rebuild-design.md`, `internal/.gitattributes` | 설계 수정, binary 목록 | 4 |
| `scripts/leak_guard.py`, `scripts/tests/test_leak_guard.py`, `.githooks/pre-commit` | 공개 커밋의 내부 문서명 검사 | 5 |
| `scripts/citations.py`, `scripts/tests/test_citations.py` | 인용 구문, 쪽 분할, 정규화, 인용문·수치 추출 | 6 |
| `scripts/terms.py`, `scripts/tests/test_terms.py` | 용어표 파싱·검증, 표기, 받침·조사 | 7 |
| `templates/note.md`, `templates/term_question.md`, `templates/change_summary.md`, `wiki/Terminology.md` | 틀, 빈 용어표 | 7 |
| `scripts/tests/conftest.py` (fixture `mini_vault`) | 검사 스크립트용 임시 vault | 8 |
| `scripts/verify_quotes.py`, `scripts/tests/test_verify_quotes.py` | 설계 §5.4 1–5 | 8 |
| `scripts/lint_wiki.py`, `scripts/tests/test_lint_wiki.py` | 설계 §5.4-6·7, §6.4, `references/` 불변 조건 | 9 |
| `scripts/build_index.py`, `scripts/tests/test_build_index.py`, `index.md` | index 생성·최신 여부 | 10 |
| `scripts/append_log.py`, `scripts/tests/test_append_log.py` | log 추가 | 11 |
| `scripts/sync_terms.py`, `scripts/tests/test_sync_terms.py`, `meta/terms_state.json` | 용어 전파 | 12 |
| `scripts/session_start.py`, `scripts/tests/test_session_start.py` | 세션 시작 보고 | 13 |
| `scripts/audit_sample.py`, `scripts/tests/test_audit_sample.py` | 표본 추출과 대조 프롬프트 | 14 |
| `scripts/hook_post_edit.py`, `scripts/tests/test_hook_post_edit.py`, `.claude/settings.json`, `.githooks/pre-commit`, `internal/.githooks/pre-commit` | hook 3종 | 15 |
| `.obsidian/plugins/obsidian-shellcommands/data.json`, `meta/views/*.base` | Obsidian 명령·보기 | 16 |
| `.claude/skills/wiki-{ingest,terms,query,lint,audit}/SKILL.md` | skill 5종 | 17 |
| `CLAUDE.md`, `meta/status.md`, `log.md`, 소스 카드 11장 | 마무리 | 18 |
| `meta/status.md` | ACRS 방침 기록 | 19 |

---

# 세션 A

### Task 0: 착수 확인과 결정 확정  **확인 지점**

**Files:**
- Modify: `meta/design/2026-09-14-rebuild-plan-phase2.md` (결정 절에 사용자 답 기록)

- [ ] **Step 1: 기준 상태 기록**

```bash
cd /c/Obsidian/ripb && git status --short | wc -l && git log --oneline -1 && "$PY" -m pytest scripts/refclean/tests scripts/tests -q 2>&1 | tail -1
```
Expected: `0`, 이 계획을 담은 커밋, `234 passed`. 다르면 멈추고 보고한다.

- [ ] **Step 2: 결정 P1–P10을 사용자에게 한 메시지로 묻는다**

각 항목의 권고와 근거를 번호 목록으로 보이고 "승인 / 변경(내용)"을 받는다. 답을 결정 표 아래에 `**확정 (YYYY-MM-DD):** P1 승인, …` 한 줄로 기록한다. 변경된 항목이 있으면 해당 Task의 코드·테스트를 답에 맞춰 고친 뒤 진행한다.

- [ ] **Step 3: 커밋**

```bash
git add meta/design/2026-09-14-rebuild-plan-phase2.md && git commit -q -m "docs(design): phase 2 plan decisions confirmed

Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>"
```

### Task 1: 원문 의존 테스트의 `refs` marker

원문(`references/`)은 git에 없으므로(설계 D11) 다른 PC의 clone에서는 원문을 읽는 테스트가 실패한다. marker로 구분하고, 원문이 없으면 skip하며, 표시가 빠진 테스트는 실패시킨다.

**Files:**
- Create: `scripts/pytest.ini`, `scripts/refclean/tests/conftest.py`
- Modify: 원문을 읽는 `scripts/refclean/tests/test_*.py` 함수들 (Step 2의 목록)

**Interfaces:**
- Produces: marker `refs`. `references/raw/*.pdf`가 없으면 `refs` 테스트는 skip된다.

- [ ] **Step 1: 원문을 여는 테스트를 목록화한다 (임시 plugin, scratchpad)**

scratchpad(`$SCRATCH`)에 `refs_inventory.py`를 만든다:

```python
import json
import os
import sys

import pytest

VAULT = os.environ["RIPB_VAULT"]
REFS = os.path.normcase(os.path.join(VAULT, "references")) + os.sep
state = {"on": False, "hit": False}
rows = []


def _audit(event, args):
    if state["on"] and event == "open" and args and isinstance(args[0], (str, bytes, os.PathLike)):
        p = os.path.normcase(os.path.abspath(os.fsdecode(args[0])))
        if p.startswith(REFS):
            state["hit"] = True


sys.addaudithook(_audit)


def _wrap(phase):
    @pytest.hookimpl(wrapper=True)
    def hook(item):
        state.update(on=True, hit=False)
        try:
            return (yield)
        finally:
            state["on"] = False
            rows.append({"id": item.nodeid, "phase": phase, "hit": state["hit"],
                         "fixtures": list(item.fixturenames)})
    return hook


pytest_runtest_setup = _wrap("setup")
pytest_runtest_call = _wrap("call")


def pytest_sessionfinish(session):
    with open(os.environ["RIPB_INV"], "w", encoding="utf-8") as f:
        json.dump(rows, f, indent=1)
```

Run:
```bash
cd /c/Obsidian/ripb && RIPB_VAULT="C:/Obsidian/ripb" RIPB_INV="$SCRATCH/inv.json" PYTHONPATH="$SCRATCH" "$PY" -m pytest scripts/refclean/tests -q -p refs_inventory 2>&1 | tail -1
```
Expected: `215 passed`, `$SCRATCH/inv.json` 생성.

- [ ] **Step 2: 표시할 테스트 집합을 계산한다**

규칙: (a) call 단계에서 원문을 연 테스트, (b) setup 단계에서 원문을 연 테스트, (c) (b)의 테스트가 요청한 fixture를 같은 모듈에서 요청한 모든 테스트(module scope fixture는 첫 테스트의 setup에서만 파일을 연다). pytest 내장 fixture는 (c)에서 제외한다.

`$SCRATCH/refs_select.py`:
```python
import json
import sys

rows = json.load(open(sys.argv[1], encoding="utf-8"))
BUILTIN = {"tmp_path", "tmp_path_factory", "monkeypatch", "capsys", "capfd", "request"}
mod = lambda nid: nid.split("::")[0]
hit = {r["id"] for r in rows if r["hit"]}
fx = {}
for r in rows:
    if r["id"] in hit and r["phase"] == "setup":
        fx.setdefault(mod(r["id"]), set()).update(set(r["fixtures"]) - BUILTIN)
mark = set(hit)
for r in rows:
    if set(r["fixtures"]) & fx.get(mod(r["id"]), set()):
        mark.add(r["id"])
for nid in sorted({n.split("[")[0] for n in mark}):
    print(nid)
```
Run: `"$PY" "$SCRATCH/refs_select.py" "$SCRATCH/inv.json" > "$SCRATCH/refs_ids.txt" && wc -l < "$SCRATCH/refs_ids.txt"`
Expected: 0보다 크고 215보다 작은 수(아래 `N_REFS`, 매개변수화 전 함수 단위). (c)로 들어온 fixture가 원문과 무관하면(합성 `El` 목록 등) 그 테스트를 목록에서 빼고 이유를 커밋 메시지에 적는다.

- [ ] **Step 3: decorator를 붙인다 (scratchpad 스크립트)**

`$SCRATCH/refs_mark.py`:
```python
import ast
import sys
from collections import defaultdict

by_file = defaultdict(set)
for line in open(sys.argv[1], encoding="utf-8"):
    if line.strip():
        parts = line.strip().split("::")
        by_file[parts[0]].add(tuple(parts[1:]))
for path, names in by_file.items():
    src = open(path, encoding="utf-8").read()
    tree = ast.parse(src)
    lines = src.split("\n")
    inserts = []

    def visit(body, prefix):
        for node in body:
            if isinstance(node, ast.ClassDef):
                visit(node.body, prefix + (node.name,))
            elif isinstance(node, ast.FunctionDef) and prefix + (node.name,) in names:
                if any(ast.unparse(d) == "pytest.mark.refs" for d in node.decorator_list):
                    continue
                first = min([d.lineno for d in node.decorator_list] + [node.lineno])
                raw = lines[first - 1]
                inserts.append((first - 1, raw[: len(raw) - len(raw.lstrip())] + "@pytest.mark.refs"))

    visit(tree.body, ())
    for idx, text in sorted(inserts, reverse=True):
        lines.insert(idx, text)
    out = "\n".join(lines)
    if not any(isinstance(n, ast.Import) and any(a.name == "pytest" for a in n.names) for n in tree.body):
        out = "import pytest\n" + out
    open(path, "w", encoding="utf-8", newline="\n").write(out)
    print(path, len(inserts))
```
Run: `"$PY" "$SCRATCH/refs_mark.py" "$SCRATCH/refs_ids.txt"`
Expected: 삽입 수의 합 = `N_REFS`. `git diff scripts/refclean/tests | grep '^[+-]' | grep -v '^+++\|^---' | grep -v '@pytest.mark.refs\|import pytest'`의 출력이 비어 있다.

- [ ] **Step 4: marker 등록과 감시 conftest를 쓴다**

`scripts/pytest.ini`:
```ini
[pytest]
markers =
    refs: reads the local-only references/ tree (PDFs, raw conversions, cleaned files); skipped when references/raw has no PDF
```

`scripts/refclean/tests/conftest.py`:
```python
"""`refs` marker guard (spec D11: references/ is not in git).

- refs-marked tests are skipped when references/raw holds no PDF (fresh clone).
- an unmarked test that opens a file under references/ during setup or call fails, so new tests get marked.
  Blind spot: files opened from C code (PyMuPDF `fitz.open`) raise no audit event.
"""
import os
import sys

import pytest

VAULT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
REFS = os.path.normcase(os.path.join(VAULT, "references")) + os.sep
RAW = os.path.join(VAULT, "references", "raw")
REFS_PRESENT = os.path.isdir(RAW) and any(f.lower().endswith(".pdf") for f in os.listdir(RAW))
_state = {"on": False, "hits": []}


def _audit(event, args):
    if _state["on"] and event == "open" and args and isinstance(args[0], (str, bytes, os.PathLike)):
        p = os.path.normcase(os.path.abspath(os.fsdecode(args[0])))
        if p.startswith(REFS):
            _state["hits"].append(p)


sys.addaudithook(_audit)


def pytest_collection_modifyitems(config, items):
    if REFS_PRESENT:
        return
    skip = pytest.mark.skip(reason="references/raw has no PDF (local-only inputs, spec D11)")
    for item in items:
        if item.get_closest_marker("refs"):
            item.add_marker(skip)


def _guard(item):
    marked = item.get_closest_marker("refs") is not None
    _state.update(on=not marked, hits=[])
    try:
        result = yield
    finally:
        _state["on"] = False
    if _state["hits"]:
        raise AssertionError(f"unmarked test opened {_state['hits'][0]}; add @pytest.mark.refs")
    return result


@pytest.hookimpl(wrapper=True)
def pytest_runtest_setup(item):
    return (yield from _guard(item))


@pytest.hookimpl(wrapper=True)
def pytest_runtest_call(item):
    return (yield from _guard(item))
```

- [ ] **Step 5: 세 방식으로 검증한다**

```bash
cd /c/Obsidian/ripb && "$PY" -m pytest scripts/refclean/tests scripts/tests -q 2>&1 | tail -1 && "$PY" -m pytest scripts/refclean/tests -q -m "not refs" 2>&1 | tail -1 && "$PY" -m pytest scripts/refclean/tests -q -m refs 2>&1 | tail -1
```
Expected: `234 passed`; `… passed, … deselected` 두 줄의 passed 합이 215. `PytestUnknownMarkWarning` 없음.

감시 확인: `test_doc.py`에서 `@pytest.mark.refs` 한 줄을 임시로 지우고 그 테스트만 실행하면 `unmarked test opened … add @pytest.mark.refs`로 실패한다. 확인 뒤 그 줄을 되돌리고 전체를 다시 실행해 `234 passed`를 확인한다.

- [ ] **Step 6: 커밋**

```bash
git add scripts/pytest.ini scripts/refclean/tests && git commit -q -m "test(refclean): refs marker for tests that read references/

Marked from an audit-hook inventory of setup/call file opens; a conftest
guard fails unmarked tests that open references/ and skips marked ones
when references/raw has no PDF.

Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>"
```

### Task 2: `notes.py` 입출력 분리와 `source.py` 보강 7건

**Files:**
- Create: `scripts/notes.py`
- Modify: `scripts/source.py`
- Test: `scripts/tests/test_notes.py`(신규), `scripts/tests/test_source.py`

**Interfaces:**
- Produces: `notes.NoteError(Exception)`; `notes.read_note(path) -> tuple[dict, str]`; `notes.dump_note(fm: dict, body: str) -> str`; `notes.write_text(path, text) -> None`(CR·BOM·U+FFFD가 있으면 `NoteError`, 끝 개행 보장); `notes.write_note(path, fm, body) -> None`. `source.SourceError is notes.NoteError`; `source.SCRIPTS`(scripts 폴더 절대 경로).

- [ ] **Step 1: 실패하는 테스트를 쓴다**

`scripts/tests/test_notes.py`:
```python
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
```

`scripts/tests/test_source.py`: 기존 `test_register_refuses_duplicate_by_hash`의 `match="duplicate of DOC_A"`를 `match="duplicate of references/raw/DOC_A_T.pdf"`로 바꾸고(원본 해시 검사가 먼저 걸린다), 파일 끝에 추가한다.
```python
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
    source.load_docs()
    source.load_docs()
    assert sys.path.count(source.SCRIPTS) == 1


def test_register_refuses_key_used_in_other_tree(vault):
    source.register(str(make_pdf(vault / "inbox" / "internal" / "n.pdf")), key="HSFR_X", title="Design Note",
                    root="internal")
    with pytest.raises(source.SourceError, match="card exists"):
        source.register(str(make_pdf(vault / "inbox" / "p.pdf")), key="HSFR_X", title="Other", root=None)


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
```
(`test_sync_raises_when_markers_missing`의 adopt는 첫 sync에서 표지가 아직 있으므로 통과하고, 표지를 지운 뒤의 sync만 실패한다. adopt 안의 sync는 정제본이 없어 표지 검사에 이르지 않는다.)

- [ ] **Step 2: 실패를 확인한다**

Run: `"$PY" -m pytest scripts/tests -q 2>&1 | tail -3`
Expected: `test_notes.py` 수집 오류 `No module named 'notes'`.

- [ ] **Step 3: `scripts/notes.py`를 만든다**

```python
"""notes.py — note files shared by the vault scripts: YAML frontmatter + Markdown body (spec §5.1, §8.1).

Every write goes through write_text, which refuses CR, BOM and U+FFFD before touching the file.
"""
import yaml


class NoteError(Exception):
    pass


def read_note(path):
    with open(path, encoding="utf-8") as f:
        text = f.read()
    if not text.startswith("---\n"):
        return {}, text
    try:
        _, fm_text, body = text.split("---\n", 2)
    except ValueError as exc:
        raise NoteError(f"{path}: bad frontmatter ({type(exc).__name__})") from exc
    try:
        fm = yaml.safe_load(fm_text)
    except yaml.YAMLError as exc:
        raise NoteError(f"{path}: bad frontmatter ({type(exc).__name__})") from exc
    if fm is not None and not isinstance(fm, dict):
        raise NoteError(f"{path}: bad frontmatter (not a mapping)")
    return (fm or {}), body.lstrip("\n")


def dump_note(fm, body):
    return "---\n" + yaml.safe_dump(fm, allow_unicode=True, sort_keys=False) + "---\n\n" + body


def write_text(path, text):
    for bad, name in (("\r", "CR"), ("﻿", "BOM"), ("�", "U+FFFD")):
        if bad in text:
            raise NoteError(f"{path}: {name} in text; not written")
    if not text.endswith("\n"):
        text += "\n"
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)


def write_note(path, fm, body):
    write_text(path, dump_note(fm, body))
```

- [ ] **Step 4: `source.py`를 고친다**

1. `import yaml`, `class SourceError`, `def read_note`, `def write_note`를 지운다. `VAULT = …` 줄을 다음으로 바꾼다.
```python
from notes import NoteError as SourceError, read_note, write_note  # noqa: E402,F401

SCRIPTS = os.path.dirname(os.path.abspath(__file__))
VAULT = os.path.dirname(SCRIPTS)
```

2. `load_docs`:
```python
def load_docs():
    if SCRIPTS not in sys.path:
        sys.path.insert(0, SCRIPTS)
    from refclean.profiles import DOCS
    return DOCS
```

3. 두 트리의 키 충돌: `card_path` 아래에 추가한다.
```python
def _existing_card(key):
    for r in (None, "internal"):
        if os.path.exists(card_path(key, r)):
            return card_path(key, r)
    return None
```
`_new_card`의 `if os.path.exists(path): raise …`와 `register`의 `if os.path.exists(card_path(key, root)): raise …`를 둘 다 다음으로 바꾼다.
```python
    taken = _existing_card(key)
    if taken:
        raise SourceError(f"card exists: {rel(taken)}")
```

4. 원본 해시 중복 검사(R20): `register`에서 `digest = sha256(pdf)` 바로 뒤, 카드 기반 검사 앞에 넣는다.
```python
    for r in (None, "internal"):
        raw = dirs(r)["raw"]
        for fn in (sorted(os.listdir(raw)) if os.path.isdir(raw) else []):
            p = os.path.join(raw, fn)
            if fn.lower().endswith(".pdf") and os.path.isfile(p) and sha256(p) == digest:
                raise SourceError(f"duplicate of {rel(p)}; left in inbox")
```

5. 되돌리기: `register`의 `shutil.move(pdf, dest)`와 `path = _new_card(...)`를 다음으로 바꾼다.
```python
    shutil.move(pdf, dest)
    try:
        path = _new_card(key, title, dest, root)
    except Exception:
        shutil.move(dest, pdf)
        raise
```

6. sync 표지: `sync`의 `block = _sync_block(fmc)` 앞에 넣는다.
```python
        if "<!-- sync:begin -->" not in body or "<!-- sync:end -->" not in body:
            raise SourceError(f"{rel(path)}: sync markers missing")
```

7. MISSING: `status`의 `cleaned = …`부터 `rows.append(…)`까지를 바꾼다.
```python
        cleaned = os.path.join(VAULT, fm["file"]) if fm.get("file") else ""
        if not cleaned:
            sha = "-"
        elif not os.path.isfile(cleaned):
            sha = "MISSING"
        else:
            sha = "ok" if sha256(cleaned) == fm.get("sha256_md") else "CHANGED"
        rows.append((fm["key"], fm.get("ingest", "?"), f"{done}/{len(units)}",
                     "yes" if fm.get("file") else "no", sha))
```

- [ ] **Step 5: 통과를 확인한다**

Run: `"$PY" -m pytest scripts/refclean/tests scripts/tests -q 2>&1 | tail -1`
Expected: `244 passed` (234 + notes 2 + source 8).

- [ ] **Step 6: 실제 vault에서 읽기 전용 확인**

Run: `"$PY" scripts/source.py status`
Expected: 11행, ingest `pending`, sha 열 모두 `ok`, 끝 줄 `inbox waiting: 0`.

- [ ] **Step 7: 커밋**

```bash
git add scripts/notes.py scripts/source.py scripts/tests/test_notes.py scripts/tests/test_source.py && git commit -q -m "fix(source): rollback, cross-tree keys, raw-hash duplicates, sync markers, MISSING

Note I/O moves to scripts/notes.py; writes refuse CR/BOM/U+FFFD instead of
an assert. load_docs inserts scripts/ once.

Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>"
```

### Task 3: `assign_levels` 공용화와 generic 프로파일의 미등록 키 오류

**Files:**
- Create: `scripts/refclean/levels.py`
- Modify: `scripts/refclean/profiles/psar.py`, `scripts/refclean/profiles/generic.py`
- Test: `scripts/refclean/tests/test_generic.py`

**Interfaces:**
- Produces: `refclean.levels.assign_levels(doc, aux=None)`, `refclean.levels.CHAPTER_TITLE`, `depth`, `_owner`. `psar`는 같은 이름을 다시 내보낸다(`psar.assign_levels is levels.assign_levels`). `generic.metadata`는 미등록 키에 `KeyError("generic profile has no META entry for '<key>'; add one to scripts/refclean/profiles/generic.py")`.

- [ ] **Step 1: 실패하는 테스트를 쓴다** (`test_generic.py` 끝에 추가; 이 파일은 이미 `sys.path`를 설정한다. 원문을 읽지 않으므로 `refs` 표시를 붙이지 않는다)

```python
def test_levels_module_is_shared_by_psar_and_generic():
    from refclean import levels
    from refclean.profiles import generic, psar
    assert psar.assign_levels is levels.assign_levels
    assert levels.assign_levels in generic.steps()


def test_generic_metadata_names_the_fix_for_unregistered_key():
    from refclean.doc import Doc
    from refclean.profiles import generic
    d = Doc("NOPE_1", "x", RAW, VAULT, 1, {}, [])
    with pytest.raises(KeyError, match="no META entry for 'NOPE_1'"):
        generic.metadata(d, None)
```
`test_generic.py` 머리에 `import pytest`가 없으면 추가한다.

- [ ] **Step 2: 실패를 확인한다**

Run: `"$PY" -m pytest scripts/refclean/tests/test_generic.py -q 2>&1 | tail -3`
Expected: `No module named 'refclean.levels'`와 `KeyError: 'NOPE_1'`(match 불일치)로 2건 실패.

- [ ] **Step 3: 함수를 옮긴다**

1. `psar.py`의 `CHAPTER_TITLE`(9행), `depth`, `_owner`, `assign_levels` 정의 전체(마지막 줄까지)를 잘라 `scripts/refclean/levels.py`에 그대로 붙인다. 파일 머리:
```python
"""Heading levels for numbered-section documents (shared by the psar and generic profiles)."""
import re
```
옮긴 본문이 `re` 외의 모듈 수준 이름을 쓰면(`grep -n "S\.\|El(\|importlib" scripts/refclean/levels.py`) 그 import도 `levels.py`에 옮겨 적는다.

2. `psar.py`의 import 끝에 넣는다.
```python
from ..levels import CHAPTER_TITLE, _owner, assign_levels, depth  # noqa: F401  (re-exported for chapter hooks and tests)
```
`psar.py`에 `re`를 쓰는 다른 코드가 남아 있으면 `import re`는 그대로 둔다.

3. `generic.py`: `from .psar import assign_levels`를 `from ..levels import assign_levels`로 바꾸고 `metadata` 첫 줄을 바꾼다.
```python
def metadata(doc, aux):
    if doc.key not in META:
        raise KeyError(f"generic profile has no META entry for {doc.key!r}; "
                       "add one to scripts/refclean/profiles/generic.py")
    m = dict(META[doc.key])
```

- [ ] **Step 4: 테스트 통과**

Run: `"$PY" -m pytest scripts/refclean/tests scripts/tests -q 2>&1 | tail -1`
Expected: `246 passed`.

- [ ] **Step 5: 출력 동일성 확인 (psar 1건, generic 2건)**

재빌드는 파이프라인 계약의 정상 경로이다. `cleaned:` 줄의 날짜만 달라질 수 있다.
```bash
cd /c/Obsidian/ripb && for k in PSAR_ch11 RG_1.233 ACRS_ML25293A458; do
  f=$(grep '^file:' "wiki/$k.md" | sed 's/^file: //'); cp "$f" "$SCRATCH/$k.before.md"
  "$PY" scripts/clean_references.py --only "$k" --verify > "$SCRATCH/$k.build.txt" 2>&1; echo "$k build exit $?"
  diff <(grep -v '^cleaned:' "$SCRATCH/$k.before.md") <(grep -v '^cleaned:' "$f") > /dev/null && echo "$k identical" || echo "$k DIFFERS"
done
```
Expected: 세 키 모두 `build exit 0`, `identical`. (`file:` 값이 YAML 접힘으로 두 줄이면 `"$PY" -c "import sys; sys.path.insert(0,'scripts'); import notes; print(notes.read_note('wiki/$k.md')[0]['file'])"`로 경로를 얻는다.) `DIFFERS`가 나오면 멈추고 `diff` 출력을 보고한다.

- [ ] **Step 6: 카드 동기화와 커밋**

```bash
"$PY" scripts/source.py sync PSAR_ch11 && "$PY" scripts/source.py sync RG_1.233 && "$PY" scripts/source.py sync ACRS_ML25293A458 && git status --short
git add scripts/refclean wiki/PSAR_ch11.md wiki/RG_1.233.md wiki/ACRS_ML25293A458.md && git commit -q -m "refactor(refclean): shared levels module; generic profile names the fix for unknown keys

Rebuilt PSAR_ch11, RG_1.233 and ACRS_ML25293A458: output identical except
the cleaned date.

Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>"
```
Expected: `git status`에는 `scripts/refclean` 변경과, 날짜가 바뀐 경우에만 카드 3장이 보인다.

### Task 4: 설계 문서 수정과 `internal/.gitattributes`

**Files:**
- Modify: `meta/design/2026-09-14-vault-rebuild-design.md`, `internal/.gitattributes` (git #2)

- [ ] **Step 1: 설계 §4.1 테스트 수**

찾기: `` 수용 관문은 `--verify`와 `pytest scripts/refclean/tests`(211건) 둘 다이다. ``
바꾸기: `` 수용 관문은 `--verify`와 `pytest scripts/refclean/tests` 둘 다이다(2026-09-14 기준 217건; 원문을 읽는 테스트는 `refs` marker가 붙어 원문이 없는 clone에서 skip된다). ``

- [ ] **Step 2: 설계 §5.1 frontmatter에 `terms_pending` 추가 (P5)**

찾기: `tags: []` (§5.1 코드 블록 안)
바꾸기:
```
tags: []
terms_pending: []      # sync_terms.py가 유지: 이 노트의 미정 용어 표지 ID
```

- [ ] **Step 3: 설계 §7.5 log 항목 (P1)**

찾기: `- `log.md`: 작업 1건당 항목 1개. 원문 범위, 새 노트·고친 노트 수, 검사 결과, 미정 용어 수, 커밋 해시.`
바꾸기: `- `log.md`: 작업 1건당 항목 1개. 원문 범위, 새 노트·고친 노트 수, 검사 결과, 미정 용어 수. 항목은 그 작업의 커밋에 함께 들어가므로 커밋 해시는 적지 않는다(`git log -- log.md`로 찾는다).`

- [ ] **Step 4: 설계 §8.1 표와 공통 규칙**

찾기: `| `source.py register \| finish \| status` | 등록(해시, 정규화, 이동, 소스 카드), 완료 처리, 현황 | 원문 파일은 이동만 한다 |`
바꾸기: `| `source.py register \| adopt \| sync \| finish \| status` | 등록(해시, 정규화, 이동, 소스 카드), 기존 원본의 카드 생성, 빌드 요약 반영, 완료 처리, 현황 | PDF는 `inbox/`에서 `references/raw/`로 옮기기만 하고 내용은 바꾸지 않는다 |`

같은 표의 `session_start.py` 행 아래에 행을 추가한다.
```
| `notes.py`, `citations.py`, `terms.py` | 노트 입출력, 인용 구문·쪽 분할·정규화, 용어표·표기·조사 | 보조 모듈 |
| `leak_guard.py`, `hook_post_edit.py` | 공개 커밋의 내부 문서명 검사, PostToolUse 진입점 | hook이 호출 |
```

찾기: `어떤 스크립트도 `inbox/`, `references/raw/`의 내용을 바꾸지 않는다.`
바꾸기: `어떤 스크립트도 `inbox/`, `references/raw/`의 파일 내용을 바꾸지 않는다(`source.py register`의 이동과 빌드의 `_verify/` 기록만 예외).`

- [ ] **Step 5: 설계 §3.4 Bases 위치 (P9)**

찾기: `- Bases 보기 4종: type별, status별, `disputed` 목록, 미정 용어 목록.`
바꾸기: `- Bases 보기 4종(`meta/views/*.base`): type별, status별, `disputed` 목록, 미정 용어를 쓰는 노트(`terms_pending`).`

- [ ] **Step 6: 설계 부록 B 교체**

부록 B의 YAML 블록과 그 아래 문단을 다음으로 바꾼다.
````markdown
```yaml
type: source
key: PSAR_ch03
title: Licensing Basis Events
file: references/TP_Natrium_PSAR2025_ch3_Licensing Basis Events.md   # sync가 채움
pdf: references/raw/TP_Natrium_PSAR2025_ch3_Licensing Basis Events.pdf
sha256_pdf: …          # register/adopt가 채움
sha256_md: …           # sync가 채움
pdf_pages: 132         # sync가 정제본 frontmatter에서
build: {converter: …, cleaned: …, missing_pct: 0.14}   # sync가 정제본 frontmatter와 _verify/<KEY>.json에서
ingest: pending        # pending | in_progress | complete
units:                 # 진행표 (커밋 해시는 두지 않는다)
  - {unit: "§3.1–3.3", status: pending}
```

서지 필드(`doc_id`, `issuer`, `revision`, `date`, `adams_accession`)는 정제본 frontmatter에만 두고 카드에 복제하지 않는다. 본문은 `templates/source_card.md`를 따른다: `## 서지`(키, 원문 경로), `## 구조`(`<!-- sync:begin -->`…`<!-- sync:end -->` 사이를 `source.py sync`가 다시 씀: PDF 쪽 수, 인쇄 쪽, 표·그림·비공개 목록), `## 알려진 모순`(예: PSAR ch3 Table 3.5-2와 §3.7.3.3 제목의 RRS-ISPL-BL 불일치), `## 관련 문서`.
````

- [ ] **Step 7: 설계 §8.6 필수 사례 보강**

찾기: `` `source.py`의 중복본·개정판 판별. ``
바꾸기: `` `source.py`의 중복본·개정판 판별, `leak_guard.py`의 내부 문서명 검출, `build_index.py --check`, `append_log.py`의 추가 전용 쓰기. ``

- [ ] **Step 8: `internal/.gitattributes`**

파일 전체를 다음으로 바꾼다.
```
* text=auto eol=lf
*.bundle binary
*.pdf binary
*.png binary
*.zip binary
```

- [ ] **Step 9: 확인과 커밋 (두 저장소)**

```bash
cd /c/Obsidian/ripb && grep -c "terms_pending" meta/design/2026-09-14-vault-rebuild-design.md && grep -c "커밋 해시는" meta/design/2026-09-14-vault-rebuild-design.md && git diff --stat
git add meta/design/2026-09-14-vault-rebuild-design.md && git commit -q -m "docs(design): card fields, move-only wording, log hash rule, helper modules

Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>"
git -C internal add .gitattributes && git -C internal commit -q -m "chore: binary attributes for pdf, png, zip

Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>"
```
Expected: 첫 grep 2 이상(§3.4, §5.1), 둘째 grep 2(§7.5, 부록 B). diff는 설계 문서 한 파일.

### Task 5: 공개 커밋의 내부 문서명 관문 (`leak_guard.py`, R14)

2026-09-14에 회의록 제목이 계획 문서에 적혔다가 push 전에 지워졌다(R14). 경로 관문은 있으나 내용 관문이 없다. 이름 목록은 커밋 시점에 `internal/`에서 만든다(P10). 커밋 메시지도 push되므로 `commit-msg` hook으로 함께 검사한다.

**Files:**
- Create: `scripts/leak_guard.py`, `scripts/tests/test_leak_guard.py`, `.githooks/commit-msg`
- Modify: `.githooks/pre-commit`

**Interfaces:**
- Consumes: `notes.read_note`, `notes.NoteError` (Task 2)
- Produces: `leak_guard.internal_names(vault: str) -> set[str]`(정규화된 이름); `leak_guard.scan(items: list[tuple[str, str]], names: set[str]) -> list[tuple[str, str]]`(`(위치, 이름)`); `leak_guard.staged_added_lines(repo: str) -> list[tuple[str, str]]`; CLI `leak_guard.py --staged | --message FILE | --files PATH...`, 검출 시 종료 코드 1. Task 9의 `lint_wiki.py --all`이 `internal_names`와 `scan`을 쓴다.

- [ ] **Step 1: 실패하는 테스트를 쓴다**

`scripts/tests/test_leak_guard.py`:
```python
import os
import subprocess

import pytest

import leak_guard as LG


@pytest.fixture
def ivault(tmp_path):
    """A vault whose internal/ tree holds fictitious documents."""
    for d in ("internal/references/raw", "internal/wiki", "internal/meetings", "wiki"):
        os.makedirs(tmp_path / d)
    (tmp_path / "internal/references/raw/HSFR_X_Design Note.pdf").write_bytes(b"%PDF fake")
    (tmp_path / "internal/wiki/HSFR_Pump_Trial.md").write_text(
        "---\ntype: hsfr\ntitle: Zeta Loop Pump Trial\naliases: [ZLP, Zeta Loop Trial]\n---\n\n"
        "# 가상 시험 (Zeta Loop Pump Trial)\n", encoding="utf-8")
    (tmp_path / "internal/meetings/2026-01-02_kickoff.md").write_text("# Omega Kickoff Meeting\n", encoding="utf-8")
    return tmp_path


def test_internal_names_collects_stems_titles_h1_aliases(ivault):
    names = LG.internal_names(str(ivault))
    assert "hsfr_x_design note" in names
    assert "zeta loop pump trial" in names and "zeta loop trial" in names
    assert "가상 시험 (zeta loop pump trial)" in names and "가상 시험" not in names  # 5 chars < 8
    assert "omega kickoff meeting" in names and "2026-01-02_kickoff" in names
    assert "zlp" not in names


def test_allow_list_removes_names(ivault):
    (ivault / "internal" / "leak_allow.txt").write_text("Zeta Loop Trial\n", encoding="utf-8")
    assert "zeta loop trial" not in LG.internal_names(str(ivault))


def test_scan_is_case_and_space_insensitive():
    hits = LG.scan([("wiki/A.md:3", "see the  ZETA loop   pump trial here")], {"zeta loop pump trial"})
    assert hits == [("wiki/A.md:3", "zeta loop pump trial")]
    assert LG.scan([("x", "nothing")], {"zeta loop pump trial"}) == []


def test_staged_added_lines_reads_only_additions_and_paths(ivault):
    run = lambda *a: subprocess.run(["git", "-C", str(ivault), *a], check=True, capture_output=True)
    run("init", "-q")
    (ivault / "wiki" / "Old.md").write_text("keep\n", encoding="utf-8")
    run("add", "wiki/Old.md")
    (ivault / "wiki" / "Omega Kickoff Meeting.md").write_text("line one\nline two\n", encoding="utf-8")
    run("add", "-A", "wiki")
    items = LG.staged_added_lines(str(ivault))
    assert ("wiki/Omega Kickoff Meeting.md", "wiki/Omega Kickoff Meeting.md") in items
    assert ("wiki/Omega Kickoff Meeting.md:2", "line two") in items
    assert all(not t.startswith("+") for _, t in items)


def test_message_mode_exit_codes(ivault, tmp_path_factory, monkeypatch, capsys):
    monkeypatch.setattr(LG, "VAULT", str(ivault))
    msg = tmp_path_factory.mktemp("m") / "MSG"
    msg.write_text("docs: add Omega Kickoff Meeting summary\n", encoding="utf-8")
    assert LG.main(["--message", str(msg)]) == 1
    assert "omega kickoff meeting" in capsys.readouterr().out
    msg.write_text("docs: status\n", encoding="utf-8")
    assert LG.main(["--message", str(msg)]) == 0


def test_no_internal_tree_passes_with_notice(tmp_path, monkeypatch, capsys):
    monkeypatch.setattr(LG, "VAULT", str(tmp_path))
    f = tmp_path / "a.md"
    f.write_text("text\n", encoding="utf-8")
    assert LG.main(["--files", str(f)]) == 0
    assert "internal/ not present" in capsys.readouterr().out


def test_extra_probe_names_from_environment(tmp_path, monkeypatch):
    monkeypatch.setenv("RIPB_LEAK_EXTRA", "zz-leak-probe-4711")
    os.makedirs(tmp_path / "internal")
    assert "zz-leak-probe-4711" in LG.internal_names(str(tmp_path))
```

- [ ] **Step 2: 실패를 확인한다**

Run: `"$PY" -m pytest scripts/tests/test_leak_guard.py -q 2>&1 | tail -2`
Expected: `No module named 'leak_guard'`.

- [ ] **Step 3: `scripts/leak_guard.py`를 쓴다**

```python
"""leak_guard.py — refuse public commits that name internal documents (spec §3.3, §8.2; ruling R14).

The name list is built at run time from internal/ (never stored in the public repo):
file stems under internal/references and internal/references/raw; stem, key, title, H1 and aliases of
internal/wiki notes; stem, title and H1 of internal/meetings notes. Names are case-folded with whitespace
collapsed; names shorter than MIN_LEN characters are ignored. internal/leak_allow.txt (private repo) lists
false positives; RIPB_LEAK_EXTRA (';'-separated) adds probe names for smoke tests.

Usage:
  python scripts/leak_guard.py --staged          # pre-commit: added lines and paths of staged files
  python scripts/leak_guard.py --message FILE    # commit-msg
  python scripts/leak_guard.py --files PATH...   # whole files
"""
import argparse
import os
import re
import subprocess
import sys

from notes import NoteError, read_note

SCRIPTS = os.path.dirname(os.path.abspath(__file__))
VAULT = os.path.dirname(SCRIPTS)
MIN_LEN = 8


def norm(s):
    return re.sub(r"\s+", " ", str(s)).strip().casefold()


def _h1(body):
    for line in body.split("\n"):
        if line.startswith("# "):
            return line[2:].strip()
    return ""


def internal_names(vault):
    base = os.path.join(vault, "internal")
    raw = set()
    for sub in ("references", os.path.join("references", "raw")):
        d = os.path.join(base, sub)
        for fn in (os.listdir(d) if os.path.isdir(d) else []):
            if os.path.isfile(os.path.join(d, fn)):
                raw.add(os.path.splitext(fn)[0])
    for sub in ("wiki", "meetings"):
        d = os.path.join(base, sub)
        for fn in (os.listdir(d) if os.path.isdir(d) else []):
            p = os.path.join(d, fn)
            if not (fn.endswith(".md") and os.path.isfile(p)):
                continue
            raw.add(fn[:-3])
            try:
                fm, body = read_note(p)
            except NoteError:
                fm, body = {}, open(p, encoding="utf-8").read()
            raw.update(str(fm[k]) for k in ("key", "title") if fm.get(k))
            raw.update(str(a) for a in (fm.get("aliases") or []))
            if _h1(body):
                raw.add(_h1(body))
    raw.update(x for x in os.environ.get("RIPB_LEAK_EXTRA", "").split(";") if x)
    allow_path = os.path.join(base, "leak_allow.txt")
    allow = set()
    if os.path.isfile(allow_path):
        allow = {norm(l) for l in open(allow_path, encoding="utf-8") if l.strip()}
    return {n for n in map(norm, raw) if len(n) >= MIN_LEN and n not in allow}


def scan(items, names):
    hits = []
    for where, text in items:
        low = norm(text)
        hits.extend((where, n) for n in sorted(names) if n in low)
    return hits


def staged_added_lines(repo):
    git = ["git", "-C", repo, "-c", "core.quotepath=false"]
    paths = subprocess.run(git + ["diff", "--cached", "--name-only", "-z", "--diff-filter=ACMR"],
                           capture_output=True, check=True).stdout.decode("utf-8").split("\0")
    items = [(p, p) for p in paths if p]
    diff = subprocess.run(git + ["diff", "--cached", "--no-color", "--no-ext-diff", "-U0", "--diff-filter=ACMR"],
                          capture_output=True, check=True).stdout.decode("utf-8", errors="replace")
    path, lineno = None, 0
    for line in diff.split("\n"):
        if line.startswith("+++ "):
            path = line[6:] if line.startswith("+++ b/") else None
        elif line.startswith("@@"):
            m = re.search(r"\+(\d+)", line)
            lineno = int(m.group(1)) if m else 0
        elif line.startswith("+") and path:
            items.append((f"{path}:{lineno}", line[1:]))
            lineno += 1
    return items


def main(argv=None):
    ap = argparse.ArgumentParser()
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--staged", action="store_true")
    g.add_argument("--message")
    g.add_argument("--files", nargs="+")
    a = ap.parse_args(argv)
    sys.stdout.reconfigure(encoding="utf-8")
    if not os.path.isdir(os.path.join(VAULT, "internal")):
        print("leak_guard: internal/ not present; nothing to check")
        return 0
    names = internal_names(VAULT)
    if a.staged:
        items = staged_added_lines(VAULT)
    elif a.message:
        items = [("commit message", open(a.message, encoding="utf-8").read())]
    else:
        items = []
        for p in a.files:
            with open(p, encoding="utf-8", errors="replace") as f:
                items += [(f"{p}:{i}", t) for i, t in enumerate(f.read().split("\n"), 1)]
    hits = scan(items, names)
    for where, n in hits:
        print(f"leak_guard: {where}: internal name \"{n}\"")
    return 1 if hits else 0


if __name__ == "__main__":
    sys.exit(main())
```

`test_staged_added_lines_reads_only_additions_and_paths`의 두 번째 기대 `("wiki/Omega Kickoff Meeting.md:2", "line two")`는 `@@ -0,0 +1,2 @@` 머리의 시작 줄 1에서 센다.

- [ ] **Step 4: 통과를 확인한다**

Run: `"$PY" -m pytest scripts/refclean/tests scripts/tests -q 2>&1 | tail -1`
Expected: `253 passed`.

- [ ] **Step 5: hook에 연결한다**

`.githooks/pre-commit`의 마지막 `exit 0` 앞에 넣는다.
```bash
# 공개 커밋의 추가 줄·경로에 내부 문서명이 없어야 한다 (spec §8.2, R14).
PY="${RIPB_PY:-/c/Code/Python/pykaeri/.venv12/Scripts/python.exe}"
ROOT="$(git rev-parse --show-toplevel)"
if ! "$PY" "$ROOT/scripts/leak_guard.py" --staged; then
  echo "pre-commit: refused (internal document names; see above)"
  exit 1
fi
```

`.githooks/commit-msg`:
```bash
#!/bin/bash
# 커밋 메시지도 공개된다 (spec §3.3, R14).
PY="${RIPB_PY:-/c/Code/Python/pykaeri/.venv12/Scripts/python.exe}"
ROOT="$(git rev-parse --show-toplevel)"
if ! "$PY" "$ROOT/scripts/leak_guard.py" --message "$1"; then
  echo "commit-msg: refused (internal document names; see above)"
  exit 1
fi
exit 0
```
```bash
chmod +x .githooks/commit-msg && git add .githooks/commit-msg && git update-index --chmod=+x .githooks/commit-msg
```

- [ ] **Step 6: 기존 공개 파일 전체를 한 번 검사한다 (R14 사후 점검)**

```bash
cd /c/Obsidian/ripb && git ls-files -z | xargs -0 "$PY" scripts/leak_guard.py --files; echo "exit $?"
```
Expected: 출력 없이 `exit 0`. 검출이 있으면 멈추고 파일·줄만 사용자에게 보고한다(이름 자체를 공개 파일에 옮겨 적지 않는다).

- [ ] **Step 7: 탐침으로 hook을 시험한다**

```bash
cd /c/Obsidian/ripb && export RIPB_LEAK_EXTRA="zz-leak-probe-4711"
printf 'probe zz-leak-probe-4711\n' > meta/_probe.md && git add meta/_probe.md && git commit -q -m "test: probe"; echo "pre-commit exit $?"
git reset -q meta/_probe.md && rm meta/_probe.md
git commit -q --allow-empty -m "test: zz-leak-probe-4711"; echo "commit-msg exit $?"
unset RIPB_LEAK_EXTRA && git log --oneline -1
```
Expected: `pre-commit: refused …`와 `pre-commit exit 1`; `commit-msg: refused …`와 `commit-msg exit 1`; 마지막 커밋은 Task 4의 커밋 그대로.

- [ ] **Step 8: 커밋**

```bash
git add scripts/leak_guard.py scripts/tests/test_leak_guard.py .githooks/pre-commit .githooks/commit-msg && git commit -q -m "feat(hooks): refuse internal document names in public commits and messages

Names are collected from internal/ at commit time; nothing is stored in
the public repo. Ruling R14.

Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>"
```

- [ ] **Step 9: 세션 A 종료 기록**

`meta/status.md`의 "다음 작업" 1번을 `Phase 2 세션 B: Task 6부터 (meta/design/2026-09-14-rebuild-plan-phase2.md)`로 바꾸고 커밋한다(`docs(status): phase 2 session A done`).

# 세션 B

### Task 6: 노트 구조 접근(`notes.py` 확장)과 인용 모듈(`citations.py`)

**Files:**
- Modify: `scripts/notes.py`
- Create: `scripts/citations.py`, `scripts/tests/test_citations.py`
- Test: `scripts/tests/test_notes.py`

**Interfaces:**
- Consumes: `notes.read_note` (Task 2)
- Produces:
  - `notes.Note(path: str, fm: dict, body: str, offset: int)`와 속성 `name`(확장자 없는 파일명); `notes.load(path) -> Note`(`offset` = 본문 첫 줄 앞의 파일 줄 수); `notes.sections(note) -> list[tuple[str, int, list[tuple[int, str]]]]`(H2 제목, 제목 줄 번호, `(파일 줄 번호, 줄)` 목록; 첫 H2 앞은 제목 `""`); `notes.tree(vault, root=None) -> dict`(키 `root`, `wiki`, `refs`, `raw`); `notes.wiki_notes(vault, root=None) -> list[str]`(`wiki/`의 `.md` 파일, 정렬); `notes.load_cards(vault) -> dict[str, dict]`(`key -> {"root", "fm", "path"}`, 두 트리, 손상된 노트는 건너뜀).
  - `citations.Citation(key, locator, p1, p2, raw)`(frozen dataclass; 쪽 없으면 `p1 = p2 = None`); `citations.parse_citation(inner: str) -> Citation | None`; `citations.split_trailing(text: str) -> tuple[str, list[Citation]]`; `citations.page_map(text: str) -> dict[int, str]`; `citations.has_pages(text) -> bool`; `citations.normalize(text: str) -> str`; `citations.quotes(text) -> list[str]`; `citations.fragments(quote) -> list[str]`; `citations.numbers(text) -> set[str]`.

- [ ] **Step 1: 실패하는 테스트를 쓴다**

`scripts/tests/test_notes.py` 끝에 추가:
```python
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
    notes.write_note(str(tmp_path / "internal" / "wiki" / "HSFR_X.md"), {"type": "source", "key": "HSFR_X"}, "# X\n")
    notes.write_note(str(tmp_path / "wiki" / "Concept.md"), {"type": "concept"}, "# C\n")
    (tmp_path / "wiki" / "Broken.md").write_text("---\ntype: source\n", encoding="utf-8")
    cards = notes.load_cards(str(tmp_path))
    assert set(cards) == {"DOC_A", "HSFR_X"} and cards["HSFR_X"]["root"] == "internal"
    assert notes.wiki_notes(str(tmp_path)) == [str(tmp_path / "wiki" / f) for f in ("Broken.md", "Concept.md", "DOC_A.md")]
```

`scripts/tests/test_citations.py`:
```python
import citations as C

CLEANED = """---
pdf_pages: 12
---

<!-- page 1 -->

# Cover

<!-- page 2 | 1 -->

## 3.2 Frequency

The **F-C Target** is not a boundary between “acceptable” and unacceptable.[^1] ^fc-target

| Event | Frequency<sup>1</sup> |
|---|---|
| AOO | 1E-02/plant-year |

<!-- page 3 | 2 -->

> [!withheld] SRI — This information is withheld in accordance with 10 CFR 2.390.

> [!figure] Figure 3-1 text
> Licensing basis events include AOOs, DBEs, and BDBEs.

<!-- page 5-7 | 4..6 -->

| Table 5-1 | Value |
|---|---|
| Range row | 5E-07 |

<!-- page 9 | 8 -->

Criterion text on nine\\* continues.

<!-- page 8 | 7 -->

Back on eight: sodium leakage shall be considered.

<!-- page 9 | 8 -->

<!-- source: note supplied by the build -->
Tail of nine.
"""


def test_parse_citation_forms():
    c = C.parse_citation("NEI_18-04 §3.2.1 p.16-17")
    assert (c.key, c.locator, c.p1, c.p2) == ("NEI_18-04", "§3.2.1", 16, 17)
    c = C.parse_citation("RG_1.232 SFR-DC 4 p.64")
    assert (c.key, c.locator, c.p1, c.p2) == ("RG_1.232", "SFR-DC 4", 64, 64)
    c = C.parse_citation("PSAR_ch05 Table 5.2-1 p.12")
    assert (c.locator, c.p1) == ("Table 5.2-1", 12)
    c = C.parse_citation("MTG_2026-01-02 §반응도 절")
    assert (c.key, c.locator, c.p1, c.p2) == ("MTG_2026-01-02", "§반응도 절", None, None)
    assert C.parse_citation("^1") is None and C.parse_citation("!abstract") is None


def test_split_trailing():
    text, cites = C.split_trailing('"A [sic] b." [DOC_A §1 p.2] [DOC_B Table 1 p.3]  ')
    assert text == '"A [sic] b."' and [c.key for c in cites] == ["DOC_A", "DOC_B"]
    assert C.split_trailing("see [[Other_Note]]") == ("see [[Other_Note]]", [])
    assert C.split_trailing("footnote[^1]") == ("footnote[^1]", [])


def test_page_map_ranges_and_non_monotonic_anchors():
    pages = C.page_map(CLEANED)
    assert "Cover" in pages[1] and "pdf_pages" not in "".join(pages.values())
    assert all("Range row" in pages[p] for p in (5, 6, 7))
    assert "Criterion text on nine" in pages[9] and "Tail of nine" in pages[9]
    assert "sodium leakage" in pages[8] and 4 not in pages
    assert C.has_pages(CLEANED) and not C.has_pages("# no anchors\n")


def test_page_map_matches_refclean_verify():
    from refclean.verify import md_pages
    ours, theirs = C.page_map(CLEANED), md_pages(CLEANED)
    assert set(ours) == set(theirs)
    assert all(C.normalize(ours[p]) == C.normalize(theirs[p]) for p in ours)


def test_normalize_removes_editorial_markup():
    pages = {p: C.normalize(t) for p, t in C.page_map(CLEANED).items()}
    assert 'The F-C Target is not a boundary between "acceptable" and unacceptable.' in pages[2]
    assert "fc-target" not in pages[2] and "[^1]" not in pages[2]
    assert "Event Frequency AOO 1E-02/plant-year" in pages[2]
    assert "withheld" not in pages[3] and "Figure 3-1 text" not in pages[3]
    assert "Licensing basis events include AOOs, DBEs, and BDBEs." in pages[3]
    assert "Criterion text on nine* continues." in pages[9]
    assert "supplied by the build" not in pages[9]


def test_quotes_and_fragments():
    item = '"Licensing basis events ... include AOOs, DBEs, and BDBEs." and "second one here"'
    assert C.quotes(item) == ["Licensing basis events ... include AOOs, DBEs, and BDBEs.", "second one here"]
    assert C.fragments(C.quotes(item)[0]) == ["Licensing basis events", "include AOOs, DBEs, and BDBEs."]
    assert C.fragments("a…b c d") == ["a", "b c d"]


def test_numbers_ignore_locators_citations_and_markers():
    text = ("빈도 5E-07/plant-year와 1,000개, 3.40 값. §3.7.3.1과 Table 3-1, p.16, DL3-RC1, "
            "[NEI_18-04 §3.2.1 p.16] LBE%%t:LBE%%, [[Note_2]]")
    assert C.numbers(text) == {"5E-7", "1000", "3.40"}
    assert C.numbers("5E-07") == C.numbers("5E-7")
```

- [ ] **Step 2: 실패를 확인한다**

Run: `"$PY" -m pytest scripts/tests/test_notes.py scripts/tests/test_citations.py -q 2>&1 | tail -2`
Expected: `No module named 'citations'`와 `module 'notes' has no attribute 'load'`.

- [ ] **Step 3: `notes.py`에 추가한다**

파일 머리의 import를 `import os`와 `from dataclasses import dataclass`, `import yaml`로 바꾸고 파일 끝에 추가한다.
```python
@dataclass
class Note:
    path: str
    fm: dict
    body: str
    offset: int

    @property
    def name(self):
        return os.path.splitext(os.path.basename(self.path))[0]


def load(path):
    fm, body = read_note(path)
    with open(path, encoding="utf-8") as f:
        text = f.read()
    return Note(path, fm, body, text.count("\n", 0, len(text) - len(body)))


def sections(note):
    out = [("", note.offset + 1, [])]
    for i, line in enumerate(note.body.split("\n"), note.offset + 1):
        if line.startswith("## "):
            out.append((line[3:].strip(), i, []))
        else:
            out[-1][2].append((i, line))
    return out


def tree(vault, root=None):
    base = os.path.join(vault, root) if root else vault
    return {"root": base, "wiki": os.path.join(base, "wiki"), "refs": os.path.join(base, "references"),
            "raw": os.path.join(base, "references", "raw")}


def wiki_notes(vault, root=None):
    w = tree(vault, root)["wiki"]
    if not os.path.isdir(w):
        return []
    return [os.path.join(w, f) for f in sorted(os.listdir(w))
            if f.endswith(".md") and os.path.isfile(os.path.join(w, f))]


def load_cards(vault):
    cards = {}
    for r in (None, "internal"):
        for p in wiki_notes(vault, r):
            try:
                fm, _ = read_note(p)
            except NoteError:
                continue
            if fm.get("type") == "source" and fm.get("key"):
                cards[str(fm["key"])] = {"root": r, "fm": fm, "path": p}
    return cards
```
(`test_load_offset_and_sections`: 파일은 `---`, `type`, `---`, 빈 줄의 4줄 뒤에 본문이 시작하므로 `offset == 4`, H1은 5행.)

- [ ] **Step 4: `scripts/citations.py`를 쓴다**

```python
"""citations.py — citation syntax, page split and text normalisation for quote checks (spec §5.2, §5.4; plan P6).

Citation: `[KEY locator p.N]`, `[KEY locator p.N-M]`, or `[KEY §heading path]` for sources without pages.
Citations are the bracket groups at the end of a list item or table cell (split_trailing).
"""
import re
from dataclasses import dataclass

KEY = r"[A-Za-z][A-Za-z0-9_.\-]*"
_INNER = re.compile(rf"^({KEY}) (.+)$")
_PAGE = re.compile(r"^(?P<loc>.*?)\s*\bp\.(?P<p1>\d+)(?:-(?P<p2>\d+))?$")
_TRAIL = re.compile(r"(?:\s*\[[^\[\]\n]+\])+\s*$")
_ONE = re.compile(r"\[([^\[\]\n]+)\]")
# same pattern as refclean.verify.ANCHOR
ANCHOR = re.compile(r"^<!-- page (\d+)(?:-(\d+))?(?: \| [^>]*)? -->$")


@dataclass(frozen=True)
class Citation:
    key: str
    locator: str
    p1: int | None
    p2: int | None
    raw: str


def parse_citation(inner):
    m = _INNER.match(inner.strip())
    if not m:
        return None
    key, rest = m.group(1), m.group(2).strip()
    pm = _PAGE.match(rest)
    if pm:
        p1 = int(pm.group("p1"))
        return Citation(key, pm.group("loc").strip(), p1, int(pm.group("p2") or p1), f"[{inner}]")
    return Citation(key, rest, None, None, f"[{inner}]")


def split_trailing(text):
    m = _TRAIL.search(text)
    if not m:
        return text, []
    cites = [parse_citation(x) for x in _ONE.findall(m.group(0))]
    if not cites or any(c is None for c in cites):
        return text, []
    return text[:m.start()].rstrip(), cites


def page_map(text):
    pages, cur, buf = {}, None, []

    def flush():
        if cur is not None:
            for p in cur:
                pages[p] = pages.get(p, "") + "\n" + "\n".join(buf)

    for line in text.split("\n"):
        m = ANCHOR.match(line.strip())
        if m:
            flush()
            a, b = int(m.group(1)), int(m.group(2) or m.group(1))
            cur, buf = list(range(a, b + 1)), []
            continue
        buf.append(line)
    flush()
    return pages


def has_pages(text):
    return any(ANCHOR.match(line.strip()) for line in text.split("\n"))


_TYPO = str.maketrans({"‘": "'", "’": "'", "‚": "'", "′": "'", "“": '"', "”": '"',
                       "„": '"', "″": '"', "–": "-", "—": "-", "‐": "-", "‑": "-",
                       " ": " "})


def normalize(text):
    kept, withheld = [], False
    for line in text.split("\n"):
        s = line.strip()
        if s.startswith(">"):
            inner = s.lstrip(">").strip()
            if re.match(r"\[!withheld\]", inner, re.I):
                withheld = True
                continue
            if withheld or re.match(r"\[![A-Za-z-]+\]", inner):
                continue
            line = inner
        else:
            withheld = False
        kept.append(line)
    t = "\n".join(kept)
    t = re.sub(r"<!--.*?-->", " ", t, flags=re.S)
    t = re.sub(r"<sup>.*?</sup>", "", t, flags=re.S)
    t = re.sub(r"!\[\[[^\]]*\]\]", " ", t)
    t = re.sub(r"\[\^\d+\]:?", "", t)
    t = re.sub(r"</?[A-Za-z][^>]*>", "", t)
    t = re.sub(r"(?m)\s\^[A-Za-z0-9-]+\s*$", "", t)
    t = re.sub(r"(?m)^\s*#{1,6}\s+", "", t)
    t = re.sub(r"(?m)^\s*(?:[-*+]|\d+[.)])\s+", "", t)
    t = re.sub(r"(?m)^\s*\|?(?:\s*:?-{3,}:?\s*\|?)+\s*$", "", t)
    t = t.replace("**", "")
    t = re.sub(r"(?<!\\)\*", "", t)
    t = re.sub(r"\\(.)", r"\1", t)
    t = t.replace("|", " ").translate(_TYPO)
    return re.sub(r"\s+", " ", t).strip()


def quotes(text):
    return re.findall(r'"([^"]+)"', text)


def fragments(quote):
    return [f.strip() for f in re.split(r"\.\.\.|…", quote) if f.strip()]


_STRIP_FOR_NUMBERS = [
    re.compile(r"\[\[[^\]]*\]\]"),
    re.compile(r"\[[^\[\]\n]+\]"),
    re.compile(r"%%t:[^%]+%%"),
    re.compile(r"§\S+"),
    re.compile(r"\b(?:Table|Figure|Section|Chapter|Appendix)\s+\S+"),
    re.compile(r"\bp\.\d+(?:-\d+)?"),
]
_NUM = re.compile(r"(?<![A-Za-z0-9_.\-])(\d+(?:[.,]\d+)*(?:[Ee][-+]?\d+)?)(?![A-Za-z0-9_\-]|[.,]\d)")


def _canon(n):
    m = re.fullmatch(r"(.+?)[Ee]([-+]?)(\d+)", n)
    if m:
        return f"{m.group(1)}E{m.group(2) if m.group(2) == '-' else ''}{int(m.group(3))}"
    if re.fullmatch(r"\d{1,3}(?:,\d{3})+", n):
        return n.replace(",", "")
    return n


def numbers(text):
    for pat in _STRIP_FOR_NUMBERS:
        text = pat.sub(" ", text)
    return {_canon(n) for n in _NUM.findall(text)}
```

`_NUM`의 경계는 ASCII 문자 클래스로 쓴다. Python의 `\w`는 한글을 포함하므로 `\w`를 쓰면 `1,000개`가 역추적으로 `1`만 추출된다. 앞쪽 조건은 `DL3-RC1`의 `3`·`1`(앞이 영문자)을, 뒤쪽 조건 `[.,]\d`는 수의 중간에서 끊기는 역추적을 막는다.

- [ ] **Step 5: 통과를 확인한다**

Run: `"$PY" -m pytest scripts/refclean/tests scripts/tests -q 2>&1 | tail -1`
Expected: `263 passed` (253 + notes 2 + citations 8).

- [ ] **Step 6: 실제 정제본에 대한 읽기 전용 점검**

```bash
cd /c/Obsidian/ripb && "$PY" - <<'EOF'
import sys; sys.path.insert(0, "scripts")
import notes, citations as C
for key, c in sorted(notes.load_cards(".").items()):
    text = open(c["fm"]["file"], encoding="utf-8").read()
    pages = C.page_map(text)
    print(key, len(pages), max(pages), c["fm"]["pdf_pages"], sum(len(C.normalize(t)) for t in pages.values()))
EOF
```
Expected: 11행. 각 행에서 `max(pages) <= pdf_pages`. 예외가 없어야 한다. 결과 표를 커밋 메시지 본문에 붙인다.

- [ ] **Step 7: 커밋**

```bash
git add scripts/notes.py scripts/citations.py scripts/tests/test_notes.py scripts/tests/test_citations.py && git commit -q -m "feat(scripts): note structure access and citation/page/normalisation module

Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>"
```

### Task 7: 용어 모듈(`terms.py`), 템플릿 3종, 빈 용어표

**Files:**
- Create: `scripts/terms.py`, `scripts/tests/test_terms.py`, `templates/note.md`, `templates/term_question.md`, `templates/change_summary.md`, `wiki/Terminology.md`

**Interfaces:**
- Produces: `terms.COLUMNS`(9개 열 이름), `terms.STATES = {"미정", "확정", "영어 유지", "용어 아님"}`, `terms.MARKER`(정규식, 그룹 1 = ID); `terms.Term(id, english, abbr, korean, later, forbidden: tuple, source, state, note)`(frozen); `terms.TermError(Exception)`; `terms.parse_table(text: str) -> dict[str, Term]`; `terms.load(path) -> dict[str, Term]`; `terms.display(term, first: bool) -> str | None`(P2); `terms.final(word: str) -> "none" | "rieul" | "other" | None`(P3); `terms.retarget(after: str, fin) -> str`(표지 뒤 조사 보정); `terms.snapshot(terms) -> dict`(`meta/terms_state.json`용).

- [ ] **Step 1: 실패하는 테스트를 쓴다**

`scripts/tests/test_terms.py`:
```python
import pytest

import terms as T

HEAD = "| ID | English | 약어 | 한국어 | 이후 표기 | 금지 표기 | 정의 출처 | 상태 | 비고 |\n|---|---|---|---|---|---|---|---|---|\n"


def table(*rows):
    return "# 용어표 (Terminology)\n\n## 용어\n\n" + HEAD + "".join(rows) + "\n## 관련 문서\n- 없음\n"


ROWS = ("| LBE | Licensing Basis Event | LBE | 가나 | 약어 | 가나다; 나가 | [DOC_A §3 p.2] | 확정 | |\n"
        "| RAC | Reactor Air Cooling System | RAC |  | 약어 |  | [DOC_B 약어표 p.5] | 미정 | |\n"
        "| PLANT | Plant |  |  |  |  |  | 용어 아님 | |\n")


def test_parse_table_fields():
    t = T.parse_table(table(ROWS))
    assert set(t) == {"LBE", "RAC", "PLANT"}
    assert t["LBE"].forbidden == ("가나다", "나가") and t["LBE"].later == "약어" and t["RAC"].state == "미정"
    assert T.parse_table(table()) == {}


@pytest.mark.parametrize("row,msg", [
    ("| LBE | A | L | 가 | 약어 |  |  | 확정 | |\n| LBE | B | L | 나 | 약어 |  |  | 확정 | |\n", "duplicate ID"),
    ("| X1 | A |  |  |  |  |  | 보류 | |\n", "state"),
    ("| X1 | A |  |  | 한국어 |  |  | 확정 | |\n", "한국어"),
    ("| X1 | A |  |  | 약어 |  |  | 미정 | |\n", "약어"),
    ("| X1 | A |  |  |  |  |  | 미정 |\n", "cells"),
    ("| 1 x | A |  |  |  |  |  | 미정 | |\n", "ID"),
])
def test_parse_table_errors_name_the_line(row, msg):
    with pytest.raises(T.TermError, match=msg) as e:
        T.parse_table(table(row))
    assert "line " in str(e.value)


def test_missing_header_is_an_error():
    with pytest.raises(T.TermError, match="header"):
        T.parse_table("# 용어표\n\n| ID | English |\n|---|---|\n")


def test_display_rules():
    t = T.parse_table(table(ROWS, "| DBE | Design Basis Event | DBE | 가닥 | 한국어 |  |  | 확정 | |\n"
                               "| NST | No Special Treatment | NST |  |  |  |  | 영어 유지 | |\n"))
    assert T.display(t["LBE"], True) == "가나(Licensing Basis Event)" and T.display(t["LBE"], False) == "LBE"
    assert T.display(t["DBE"], False) == "가닥"
    assert T.display(t["RAC"], True) == "Reactor Air Cooling System" and T.display(t["RAC"], False) == "RAC"
    assert T.display(t["NST"], False) == "No Special Treatment"
    assert T.display(t["PLANT"], True) is None


@pytest.mark.parametrize("word,fin", [
    ("가나", "none"), ("가닥", "other"), ("가날", "rieul"), ("LBE", "none"), ("RAM", "other"), ("SFR", "rieul"),
    ("PSAR2", "none"), ("가닥(Licensing Basis Event)", "other"), ("Licensing Basis Event", None), ("LBEs", None),
])
def test_final_consonant(word, fin):
    assert T.final(word) == fin


@pytest.mark.parametrize("after,fin,out", [
    ("는 다음", "other", "은 다음"), ("가 있다", "other", "이 있다"), ("를 본다", "other", "을 본다"),
    ("와 함께", "other", "과 함께"), ("로 간다", "other", "으로 간다"), ("으로 간다", "none", "로 간다"),
    ("으로 간다", "rieul", "로 간다"), ("은 다음", "none", "는 다음"), ("이며 다음", "none", "이며 다음"),
    ("는 다음", None, "는 다음"), (". 다음", "other", ". 다음"), ("는", "other", "은"),
])
def test_retarget_particles(after, fin, out):
    assert T.retarget(after, fin) == out


def test_marker_and_snapshot():
    assert T.MARKER.findall("LBE%%t:LBE%%는 DL3%%t:DL3-RC%%") == ["LBE", "DL3-RC"]
    snap = T.snapshot(T.parse_table(table(ROWS)))
    assert snap["LBE"] == {"english": "Licensing Basis Event", "abbr": "LBE", "korean": "가나", "later": "약어",
                           "forbidden": ["가나다", "나가"], "state": "확정"}
```

- [ ] **Step 2: 실패를 확인한다**

Run: `"$PY" -m pytest scripts/tests/test_terms.py -q 2>&1 | tail -2`
Expected: `No module named 'terms'`.

- [ ] **Step 3: `scripts/terms.py`를 쓴다**

```python
"""terms.py — the terminology table wiki/Terminology.md and term display rules (spec §6; plan P2, P3).

Table columns: ID | English | 약어 | 한국어 | 이후 표기 | 금지 표기 | 정의 출처 | 상태 | 비고.
금지 표기 holds several forms separated by '; '. Only the user fills 한국어 (spec D5).
"""
import re
from dataclasses import dataclass

COLUMNS = ["ID", "English", "약어", "한국어", "이후 표기", "금지 표기", "정의 출처", "상태", "비고"]
STATES = {"미정", "확정", "영어 유지", "용어 아님"}
LATER = {"약어", "한국어", ""}
ID_RE = re.compile(r"^[A-Za-z0-9][A-Za-z0-9_\-]*$")
MARKER = re.compile(r"%%t:([A-Za-z0-9][A-Za-z0-9_\-]*)%%")
READ = {"A": "에이", "B": "비", "C": "씨", "D": "디", "E": "이", "F": "에프", "G": "지", "H": "에이치", "I": "아이",
        "J": "제이", "K": "케이", "L": "엘", "M": "엠", "N": "엔", "O": "오", "P": "피", "Q": "큐", "R": "알",
        "S": "에스", "T": "티", "U": "유", "V": "브이", "W": "더블유", "X": "엑스", "Y": "와이", "Z": "제트",
        "0": "영", "1": "일", "2": "이", "3": "삼", "4": "사", "5": "오", "6": "육", "7": "칠", "8": "팔", "9": "구"}
PAIRS = {"은": ("은", "는"), "는": ("은", "는"), "이": ("이", "가"), "가": ("이", "가"), "을": ("을", "를"),
         "를": ("을", "를"), "과": ("과", "와"), "와": ("과", "와"), "으로": ("으로", "로"), "로": ("으로", "로")}
_JOSA = re.compile(r"^(으로|로|은|는|이|가|을|를|과|와)(?![가-힣])")


class TermError(Exception):
    pass


@dataclass(frozen=True)
class Term:
    id: str
    english: str
    abbr: str
    korean: str
    later: str
    forbidden: tuple
    source: str
    state: str
    note: str


def _cells(line):
    s = line.strip()
    return [c.strip() for c in s.strip("|").split("|")]


def parse_table(text):
    lines = text.split("\n")
    start = next((i for i, l in enumerate(lines) if l.strip().startswith("|") and _cells(l) == COLUMNS), None)
    if start is None:
        raise TermError("terminology header row not found (columns: " + " | ".join(COLUMNS) + ")")
    out = {}
    for i in range(start + 2, len(lines)):
        line = lines[i]
        if not line.strip().startswith("|"):
            break
        where = f"line {i + 1}"
        c = _cells(line)
        if len(c) != len(COLUMNS):
            raise TermError(f"{where}: {len(c)} cells, expected {len(COLUMNS)}")
        tid, eng, abbr, kor, later, forb, src, state, note = c
        if not ID_RE.match(tid):
            raise TermError(f"{where}: bad ID {tid!r}")
        if tid in out:
            raise TermError(f"{where}: duplicate ID {tid}")
        if state not in STATES:
            raise TermError(f"{where}: {tid}: state {state!r} not in {sorted(STATES)}")
        if later not in LATER:
            raise TermError(f"{where}: {tid}: 이후 표기 {later!r} must be 약어, 한국어 or empty")
        if state == "확정" and not kor:
            raise TermError(f"{where}: {tid}: 확정 needs 한국어")
        if later == "한국어" and state != "확정":
            raise TermError(f"{where}: {tid}: 이후 표기 한국어 needs 상태 확정")
        if later == "약어" and not abbr:
            raise TermError(f"{where}: {tid}: 이후 표기 약어 needs 약어")
        forbidden = tuple(x.strip() for x in forb.split(";") if x.strip())
        out[tid] = Term(tid, eng, abbr, kor, later, forbidden, src, state, note)
    return out


def load(path):
    with open(path, encoding="utf-8") as f:
        return parse_table(f.read())


def display(term, first):
    if term.state == "용어 아님":
        return None
    if term.state == "확정":
        if first:
            return f"{term.korean}({term.english})"
        return term.abbr if term.later == "약어" else term.korean
    if not first and term.later == "약어" and term.abbr:
        return term.abbr
    return term.english


def final(word):
    w = re.sub(r"\([^()]*\)\s*$", "", word).strip()
    if not w:
        return None
    c = w[-1]
    if "가" <= c <= "힣":
        k = (ord(c) - 0xAC00) % 28
        return "none" if k == 0 else ("rieul" if k == 8 else "other")
    if c in READ and re.fullmatch(r"[A-Z0-9][A-Z0-9\-]*", w):
        return final(READ[c])
    return None


def retarget(after, fin):
    m = _JOSA.match(after)
    if not m or fin is None:
        return after
    with_final, without = PAIRS[m.group(1)]
    if with_final == "으로":
        new = without if fin in ("none", "rieul") else with_final
    else:
        new = without if fin == "none" else with_final
    return new + after[m.end():]


def snapshot(terms):
    return {t.id: {"english": t.english, "abbr": t.abbr, "korean": t.korean, "later": t.later,
                   "forbidden": list(t.forbidden), "state": t.state} for t in terms.values()}
```

(`final("PSAR2")`: `2` → `이` → 받침 없음. `final("LBEs")`: 소문자가 있어 약어가 아니므로 `None`, P3.)

- [ ] **Step 4: 통과를 확인한다**

Run: `"$PY" -m pytest scripts/refclean/tests scripts/tests -q 2>&1 | tail -1`
Expected: `295 passed` (263 + terms 32: 1 + 6 + 1 + 1 + 10 + 12 + 1 — parametrize 사례를 각각 센다).

- [ ] **Step 5: 템플릿과 빈 용어표를 쓴다**

`templates/note.md` (설계 §5.1; `{…}`는 작성 시 채우는 자리이며 lint가 wiki 노트에서 이를 금지한다):
```markdown
---
type: {type}
aliases: []
sources: []
status: draft
verified:
term:
tags: []
terms_pending: []
---
# {한국어 제목} ({English Title})

> [!abstract] 요약
> {한국어 2–3문장}

## 원문 사실
- "{원문 문장 그대로}" [{KEY} {위치} p.{N}]

| 항목 | 값 | 출처 |
|---|---|---|
| {원문 표 셀} | {값} | [{KEY} Table {x} p.{N}] |

## 해설
{한국어. '원문 사실' 절의 항목만 근거로 삼는다.}

## 관련 문서
- [[{존재하는 노트}]]
```

`templates/term_question.md` (설계 §6.3; 번역 후보를 싣지 않는다):
```markdown
## 용어 질문 — {인제스트 단위}

아래 용어의 표기를 항목마다 하나로 답해 주십시오: 한국어 표기 / "영어 유지" / "용어 아님". `wiki/Terminology.md`를 직접 고쳐도 됩니다. 답이 없는 용어는 영어로 쓰고 표지만 달아 둡니다.

1. **{English}** ({약어 또는 "약어 없음"}) — ID `{ID}`
   - 원문 정의: "{정의 문장}" [{KEY} {위치} p.{N}]
```

`templates/change_summary.md` (설계 §7.2 4단계):
```markdown
## 변경 요약 — {인제스트 단위}

**승인하면 log 추가, index 재생성, 커밋까지 한 번에 진행합니다(push 제외).**

### 새 노트 ({n})
- [[{노트}]] — {한 줄 요약}

### 고친 노트 ({n})
- [[{노트}]] — {무엇을 고쳤는가}

### 검사 결과
- lint_wiki: 오류 {n}, 경고 {n}
- verify_quotes: 인용 {n}건 중 불일치 {n}
- sync_terms: 갱신 노트 {n}

### 원문 간 모순
- {없음 또는 사실 A [인용] / 사실 B [인용] → status: disputed}

### 누락 주제
- {주제} — {언급 위치 [인용]}

### 남은 미정 용어
- {ID} ({English})

### 직접 볼 노트
1. [[{노트}]] — {이유}
```

`wiki/Terminology.md` (P4):
```markdown
---
type: map
aliases: [용어표]
sources: []
status: draft
verified:
term:
tags: [terminology]
terms_pending: []
---
# 용어표 (Terminology)

> [!abstract] 요약
> vault 노트가 쓰는 전문 용어의 표기 규칙을 모은 단일 원천이다. 한국어 칸은 사용자만 채우며, 변경은 `scripts/sync_terms.py`가 모든 노트에 전파한다.

## 용어

| ID | English | 약어 | 한국어 | 이후 표기 | 금지 표기 | 정의 출처 | 상태 | 비고 |
|---|---|---|---|---|---|---|---|---|

## 표기 규칙
- 상태: 미정 / 확정 / 영어 유지 / 용어 아님. 이후 표기: 약어 / 한국어. 금지 표기는 `; `로 구분한다.
- 확정: 첫 등장 "한국어(English)", 이후 이후 표기. 영어 유지·미정: 첫 등장 English, 이후 약어(이후 표기가 약어일 때) 또는 English.

## 관련 문서
- 없음
```

- [ ] **Step 6: 용어표가 파싱되는지 확인한다**

Run: `"$PY" -c "import sys; sys.path.insert(0,'scripts'); import terms; print(terms.load('wiki/Terminology.md'))"`
Expected: `{}`.

- [ ] **Step 7: 커밋**

```bash
git add scripts/terms.py scripts/tests/test_terms.py templates/note.md templates/term_question.md templates/change_summary.md wiki/Terminology.md && git commit -q -m "feat(terms): terminology table parser, display and particle rules; note templates

Empty wiki/Terminology.md (spec §6.1). Display rules per plan P2, particle
correction for Hangul and abbreviations only (P3).

Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>"
```

### Task 8: 인용 검증 (`verify_quotes.py`, 설계 §5.4 1–5)

**Files:**
- Modify: `scripts/notes.py` (`Finding` 추가), `scripts/tests/conftest.py` (fixture 추가)
- Create: `scripts/verify_quotes.py`, `scripts/tests/test_verify_quotes.py`

**Interfaces:**
- Consumes: `notes.load`, `notes.sections`, `notes.load_cards`, `notes.wiki_notes`, `notes.NoteError` (Task 2, 6); `citations.*` (Task 6)
- Produces:
  - `notes.Finding(path: str, line: int, code: str, message: str, level: str = "error")`(frozen; `str()` = `"{path}:{line}: {level} {code} {message}"`). lint·hook·session_start가 같은 형식을 쓴다.
  - `verify_quotes.Sources(vault, cards)`와 `.get(key) -> dict | None`, `.window(citation) -> str`; `verify_quotes.verify_note(vault, path, sources) -> list[Finding]`; `verify_quotes.main(argv) -> int`. 코드: `V1` 항목·인용 형식, `V2` 소스 키·쪽 범위, `V3` 인용문, `V4` 표 값, `V5` 해설 수치.
  - conftest fixture `mini_vault`(Path), `make_note(name, body, **fm) -> str`, `good_note_body -> str`. Task 9–14가 쓴다.

- [ ] **Step 1: `notes.Finding`과 fixture를 추가한다**

`scripts/notes.py` 끝에 추가:
```python
@dataclass(frozen=True)
class Finding:
    path: str
    line: int
    code: str
    message: str
    level: str = "error"

    def __str__(self):
        return f"{self.path}:{self.line}: {self.level} {self.code} {self.message}"


def relpath(path, vault):
    return os.path.relpath(path, vault).replace(os.sep, "/")
```

`scripts/tests/conftest.py` 끝에 추가:
```python
MINI_CLEANED = """---
pdf_pages: 12
---

<!-- page 1 -->

# Cover

<!-- page 2 | 1 -->

## 3.2 Frequency

The **F-C Target** is not a boundary between “acceptable” and unacceptable.[^1] ^fc-target

| Event | Frequency<sup>1</sup> |
|---|---|
| AOO | 1E-02/plant-year |

<!-- page 3 | 2 -->

> [!withheld] SRI — This information is withheld in accordance with 10 CFR 2.390.

> [!figure] Figure 3-1 text
> Licensing basis events include AOOs, DBEs, and BDBEs.

<!-- page 5-7 | 4..6 -->

| Table 5-1 | Value |
|---|---|
| Range row | 5E-07 |

<!-- page 9 | 8 -->

Criterion text on nine\\* continues.

<!-- page 8 | 7 -->

Back on eight: sodium leakage shall be considered.

<!-- page 9 | 8 -->

<!-- source: note supplied by the build -->
Tail of nine.
"""

CARD_BODY = """# T (DOC_A)

> [!abstract] 요약
> (인제스트 완료 시 작성)

## 서지
- 키: `DOC_A`

## 구조
<!-- sync:begin -->
- PDF 쪽 수: 12
<!-- sync:end -->

## 알려진 모순
- 없음

## 관련 문서
- 없음
"""

TERMINOLOGY = """---
type: map
aliases: [용어표]
sources: []
status: draft
verified:
term:
tags: [terminology]
terms_pending: []
---
# 용어표 (Terminology)

> [!abstract] 요약
> 시험용 용어표이다.

## 용어

| ID | English | 약어 | 한국어 | 이후 표기 | 금지 표기 | 정의 출처 | 상태 | 비고 |
|---|---|---|---|---|---|---|---|---|
| LBE | Licensing Basis Event | LBE | 가나 | 약어 | 나가 | [DOC_A §3.2 p.3] | 확정 | |
| RAC | Reactor Air Cooling System | RAC |  | 약어 |  | [DOC_A §3.2 p.3] | 미정 | |

## 관련 문서
- 없음
"""

GOOD_NOTE = """# 가나 시험 (Sample Concept)

> [!abstract] 요약
> 가나(Licensing Basis Event)%%t:LBE%%에 관한 시험 노트이다.

## 원문 사실
- "Licensing basis events include AOOs, DBEs, and BDBEs." [DOC_A §3.2 p.3]

| 항목 | 값 | 출처 |
|---|---|---|
| AOO | 1E-02/plant-year | [DOC_A Table x p.2] |

## 해설
빈도 1E-02/plant-year가 표에 있다. LBE%%t:LBE%%는 세 종류이다.

## 관련 문서
- [[DOC_A]]
"""


@pytest.fixture
def mini_vault(tmp_path):
    """Public tree with one source card (DOC_A, 12 pages), its cleaned file, and a two-row terminology table."""
    import hashlib

    import notes
    for d in ("wiki", "references/raw", "internal/wiki", "internal/references/raw", "inbox", "meta", "templates"):
        os.makedirs(tmp_path / d, exist_ok=True)
    cleaned = tmp_path / "references" / "DOC_A_T.md"
    cleaned.write_text(MINI_CLEANED, encoding="utf-8")
    pdf = tmp_path / "references" / "raw" / "DOC_A_T.pdf"
    pdf.write_bytes(b"%PDF fake DOC_A")
    fm = {"type": "source", "key": "DOC_A", "title": "T", "file": "references/DOC_A_T.md",
          "pdf": "references/raw/DOC_A_T.pdf", "sha256_pdf": hashlib.sha256(pdf.read_bytes()).hexdigest(),
          "sha256_md": hashlib.sha256(cleaned.read_bytes()).hexdigest(), "pdf_pages": 12, "build": {},
          "ingest": "pending", "units": []}
    notes.write_note(str(tmp_path / "wiki" / "DOC_A.md"), fm, CARD_BODY)
    (tmp_path / "wiki" / "Terminology.md").write_text(TERMINOLOGY, encoding="utf-8")
    return tmp_path


@pytest.fixture
def make_note(mini_vault):
    import notes

    def make(name, body, root=None, **fm):
        base = {"type": "concept", "aliases": [], "sources": ["DOC_A"], "status": "draft", "verified": None,
                "term": None, "tags": [], "terms_pending": []}
        base.update(fm)
        p = (mini_vault / root / "wiki" if root else mini_vault / "wiki") / f"{name}.md"
        notes.write_note(str(p), base, body)
        return str(p)
    return make


@pytest.fixture
def good_note_body():
    return GOOD_NOTE
```
(`MINI_CLEANED`는 파이썬 일반 문자열이므로 소스의 `nine\\*`는 시험 정제본에 `nine\*`(Markdown 이스케이프된 별표)로 저장된다. `test_citations.py`의 `CLEANED`와 같은 표기이다.)

- [ ] **Step 2: 실패하는 테스트를 쓴다**

`scripts/tests/test_verify_quotes.py`:
```python
import pytest

import notes as N
import verify_quotes as VQ


def run(vault, path):
    return VQ.verify_note(str(vault), path, VQ.Sources(str(vault), N.load_cards(str(vault))))


def body_with(facts, commentary="가."):
    return (f"# 가 (T)\n\n> [!abstract] 요약\n> 가.\n\n## 원문 사실\n{facts}\n\n## 해설\n{commentary}\n\n"
            "## 관련 문서\n- 없음\n")


def test_good_note_passes(mini_vault, make_note, good_note_body):
    assert run(mini_vault, make_note("Sample", good_note_body)) == []


LBE = '"Licensing basis events include AOOs, DBEs, and BDBEs."'


@pytest.mark.parametrize("item,code", [
    (f"{LBE} [DOC_A §3.2 p.4]", None),                                   # ±1 page
    (f"{LBE} [DOC_A §3.2 p.5]", "V3"),                                   # outside window
    ('"Licensing basis events include AOOs and DBEs." [DOC_A §3.2 p.3]', "V3"),
    ('"The F-C Target is not a boundary between “acceptable” and unacceptable." [DOC_A §3.2 p.2]', None),
    ('"Back on eight: sodium leakage shall be considered." [DOC_A SFR-DC 4 p.8]', None),
    ('"Back on eight: sodium leakage shall be considered." [DOC_A SFR-DC 4 p.10]', "V3"),  # non-monotonic anchors
    ('"Criterion text on nine\\* continues." [DOC_A SFR-DC 4 p.9]', None),
    ('"This information is withheld in accordance with 10 CFR 2.390." [DOC_A §3 p.3]', "V3"),  # editorial
    ('"supplied by the build" [DOC_A §3 p.9]', "V3"),                     # HTML comment
    ('"Licensing basis ... include AOOs, DBEs, and BDBEs." [DOC_A §3.2 p.3]', "V3"),         # short fragment
    ('"Licensing basis events ... include AOOs, DBEs, and BDBEs." [DOC_A §3.2 p.3]', None),
    (LBE, "V1"),
    ("Licensing basis events include AOOs. [DOC_A §3.2 p.3]", "V3"),     # not quoted
    (f"{LBE} [DOC_X §3.2 p.3]", "V2"),
    (f"{LBE} [DOC_A §3.2 p.13]", "V2"),
    (f"{LBE} [DOC_A §3.2]", "V2"),                                        # page required
])
def test_fact_items(mini_vault, make_note, item, code):
    got = [f.code for f in run(mini_vault, make_note("Item", body_with(f"- {item}")))]
    assert got == ([] if code is None else [code])


@pytest.mark.parametrize("row,code", [
    ("| AOO | 1E-02/plant-year | [DOC_A Table x p.2] |", None),
    ("| Range row | 5E-07 | [DOC_A Table 5-1 p.6] |", None),
    ("| Range row | 5E-08 | [DOC_A Table 5-1 p.6] |", "V4"),
    ("| AOO | 1E-02/plant-year | |", "V1"),
])
def test_fact_tables(mini_vault, make_note, row, code):
    facts = f"| 항목 | 값 | 출처 |\n|---|---|---|\n{row}"
    got = [f.code for f in run(mini_vault, make_note("Tbl", body_with(facts)))]
    assert got == ([] if code is None else [code])


def test_table_needs_source_column_and_prose_is_refused(mini_vault, make_note):
    facts = "| 항목 | 값 |\n|---|---|\n| AOO | 1E-02/plant-year |\n\n원문에 따르면 AOO가 있다."
    assert [f.code for f in run(mini_vault, make_note("Tbl", body_with(facts)))] == ["V1", "V1"]


def test_commentary_numbers_must_appear_in_facts(mini_vault, make_note):
    facts = "| 항목 | 값 | 출처 |\n|---|---|---|\n| AOO | 1E-02/plant-year | [DOC_A Table x p.2] |"
    assert run(mini_vault, make_note("N1", body_with(facts, "값은 1E-2/plant-year이다."))) == []
    got = run(mini_vault, make_note("N2", body_with(facts, "값은 5E-07이다.")))
    assert [(f.code, f.message) for f in got] == [("V5", "number 5E-7 in 해설 is not in 원문 사실")]


def test_cli_exit_codes(mini_vault, make_note, good_note_body, monkeypatch, capsys):
    monkeypatch.setattr(VQ, "VAULT", str(mini_vault))
    good = make_note("Sample", good_note_body)
    assert VQ.main([good]) == 0
    make_note("Bad", good_note_body.replace("p.3]", "p.13]"))
    assert VQ.main(["--all"]) == 1
    assert "wiki/Bad.md" in capsys.readouterr().out
```

- [ ] **Step 3: 실패를 확인한다**

Run: `"$PY" -m pytest scripts/tests/test_verify_quotes.py -q 2>&1 | tail -2`
Expected: `No module named 'verify_quotes'`.

- [ ] **Step 4: `scripts/verify_quotes.py`를 쓴다**

```python
"""verify_quotes.py — checks of the 원문 사실 section against the cleaned sources (spec §5.4 items 1-5; plan P6).

V1 every list item / table row carries a trailing citation; the section holds only items and rows; tables end in 출처
V2 the source key has a card and a cleaned file; p.N lies in 1..pdf_pages; paged sources need p.N
V3 each quoted fragment (split at ... / …, at least MIN_WORDS words) occurs in the cited pages ±1 after normalisation
V4 each table value occurs in the cited pages ±1
V5 every number in 해설 also occurs in 원문 사실

Usage: python scripts/verify_quotes.py PATH... | --all [--root internal]
"""
import argparse
import os
import re
import sys

import citations as C
import notes as N

SCRIPTS = os.path.dirname(os.path.abspath(__file__))
VAULT = os.path.dirname(SCRIPTS)
FACTS, COMMENTARY = "원문 사실", "해설"
MIN_WORDS = 3


class Sources:
    """Cleaned texts per source key, normalised per page, loaded once."""

    def __init__(self, vault, cards):
        self.vault, self.cards, self._cache = vault, cards, {}

    def get(self, key):
        if key not in self._cache:
            card = self.cards.get(key)
            rel = (card or {}).get("fm", {}).get("file") or ""
            path = os.path.join(self.vault, rel)
            if not card or not rel or not os.path.isfile(path):
                self._cache[key] = None
            else:
                with open(path, encoding="utf-8") as f:
                    text = f.read()
                body = text.split("\n---\n", 1)[1] if text.startswith("---\n") and "\n---\n" in text else text
                pages = {p: C.normalize(t) for p, t in C.page_map(text).items()}
                self._cache[key] = {"pages": pages, "all": C.normalize(body), "paged": bool(pages),
                                    "n": int(card["fm"].get("pdf_pages") or 0)}
        return self._cache[key]

    def window(self, cite):
        s = self.get(cite.key)
        if cite.p1 is None:
            return s["all"]
        return " ".join(s["pages"].get(p, "") for p in range(cite.p1 - 1, cite.p2 + 2))


def _cells(line):
    return [c.strip() for c in line.strip().strip("|").split("|")]


def _check_cites(src, cites, rel, ln):
    out, ok = [], []
    for c in cites:
        s = src.get(c.key)
        if c.key not in src.cards:
            out.append(N.Finding(rel, ln, "V2", f"unknown source key {c.key}"))
        elif s is None:
            out.append(N.Finding(rel, ln, "V2", f"{c.key}: cleaned file missing"))
        elif c.p1 is None and s["paged"]:
            out.append(N.Finding(rel, ln, "V2", f"{c.raw}: page required (source has page anchors)"))
        elif c.p1 is not None and not (1 <= c.p1 <= c.p2 <= s["n"]):
            out.append(N.Finding(rel, ln, "V2", f"{c.raw}: page outside 1-{s['n']}"))
        else:
            ok.append(c)
    return out, ok


def _item(ln, text, src, rel, fact_text):
    body, cites = C.split_trailing(text)
    if not cites:
        return [N.Finding(rel, ln, "V1", "item has no citation")]
    fact_text.append(body)
    out, ok = _check_cites(src, cites, rel, ln)
    if not ok:
        return out
    qs = C.quotes(body)
    if not qs:
        return out + [N.Finding(rel, ln, "V3", "item has no quoted source text")]
    for q in qs:
        for frag in C.fragments(q):
            nf = C.normalize(frag)
            if len(nf.split()) < MIN_WORDS:
                out.append(N.Finding(rel, ln, "V3", f"fragment shorter than {MIN_WORDS} words: \"{frag}\""))
            elif not any(nf in src.window(c) for c in ok):
                out.append(N.Finding(rel, ln, "V3", f"not found at cited pages (±1): \"{frag[:80]}\""))
    return out


def _table(block, src, rel, fact_text):
    head = _cells(block[0][1])
    if head[-1] != "출처":
        return [N.Finding(rel, block[0][0], "V1", "원문 사실 table needs a last column 출처")]
    out = []
    for ln, line in block[2:]:
        cells = _cells(line)
        if len(cells) != len(head):
            out.append(N.Finding(rel, ln, "V1", f"row has {len(cells)} cells, header has {len(head)}"))
            continue
        _, cites = C.split_trailing(cells[-1])
        if not cites:
            out.append(N.Finding(rel, ln, "V1", "row has no citation"))
            continue
        fact_text.extend(cells[:-1])
        errs, ok = _check_cites(src, cites, rel, ln)
        out += errs
        for cell in (cells[:-1] if ok else []):
            nc = C.normalize(cell)
            if nc and not any(nc in src.window(c) for c in ok):
                out.append(N.Finding(rel, ln, "V4", f"table value not found at cited pages (±1): \"{cell[:80]}\""))
    return out


def verify_note(vault, path, src):
    note = N.load(path)
    rel = N.relpath(path, vault)
    secs = {title: lines for title, _, lines in N.sections(note)}
    if FACTS not in secs:
        return []
    out, fact_text, rows, i = [], [], secs[FACTS], 0
    while i < len(rows):
        ln, line = rows[i]
        s = line.strip()
        if not s:
            i += 1
        elif s.startswith("|"):
            block = []
            while i < len(rows) and rows[i][1].strip().startswith("|"):
                block.append(rows[i])
                i += 1
            out += _table(block, src, rel, fact_text)
        else:
            if re.match(r"^\s*- ", line):
                out += _item(ln, s[2:], src, rel, fact_text)
            else:
                out.append(N.Finding(rel, ln, "V1", "원문 사실 holds list items and table rows only"))
            i += 1
    fact_numbers = C.numbers("\n".join(fact_text))
    for ln, line in secs.get(COMMENTARY, []):
        for n in sorted(C.numbers(line) - fact_numbers):
            out.append(N.Finding(rel, ln, "V5", f"number {n} in 해설 is not in 원문 사실"))
    return out


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("paths", nargs="*")
    ap.add_argument("--all", action="store_true")
    ap.add_argument("--root")
    a = ap.parse_args(argv)
    if not a.paths and not a.all:
        ap.error("give PATH... or --all")
    sys.stdout.reconfigure(encoding="utf-8")
    src = Sources(VAULT, N.load_cards(VAULT))
    paths = [os.path.abspath(p) for p in a.paths] or N.wiki_notes(VAULT, a.root)
    findings = []
    for p in paths:
        try:
            findings += verify_note(VAULT, p, src)
        except N.NoteError as exc:
            findings.append(N.Finding(N.relpath(p, VAULT), 1, "V0", str(exc)))
    for f in findings:
        print(f)
    errors = sum(1 for f in findings if f.level == "error")
    print(f"verify_quotes: {len(paths)} notes, {errors} errors")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
```

- [ ] **Step 5: 통과를 확인한다**

Run: `"$PY" -m pytest scripts/refclean/tests scripts/tests -q 2>&1 | tail -1`
Expected: `319 passed` (295 + 24: 1 + 16 + 4 + 1 + 1 + 1).

- [ ] **Step 6: 실제 vault**

Run: `"$PY" scripts/verify_quotes.py --all; echo "exit $?"`
Expected: `verify_quotes: 12 notes, 0 errors`, `exit 0` (소스 카드 11장과 용어표에는 원문 사실 절이 없다).

- [ ] **Step 7: 커밋**

```bash
git add scripts/notes.py scripts/verify_quotes.py scripts/tests/conftest.py scripts/tests/test_verify_quotes.py && git commit -q -m "feat(verify_quotes): citation, quote, table value and commentary number checks

Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>"
```

### Task 9: 구조·용어 lint (`lint_wiki.py`)

두 부분으로 나누어 각각 커밋한다. Part 1은 파일 단위 검사(PostToolUse hook이 쓰는 모드), Part 2는 vault 전체 검사(pre-commit이 쓰는 `--all`).

**Files:**
- Create: `scripts/lint_wiki.py`, `scripts/tests/test_lint_wiki.py`

**Interfaces:**
- Consumes: `notes.*`, `notes.Finding` (Task 2, 6, 8); `terms.load`, `terms.display`, `terms.final`, `terms.retarget`, `terms.MARKER`, `terms.TermError` (Task 7); `leak_guard.internal_names`, `leak_guard.scan` (Task 5, Part 2)
- Produces: `lint_wiki.Context(vault)`(속성 `vault`, `public: dict[stem, path]`, `internal: dict[stem, path]`, `cards`, `terms`, `terms_error`, `assets: set[str]`); `lint_wiki.lint_file(ctx, path) -> list[Finding]`; `lint_wiki.lint_vault(ctx, root=None) -> list[Finding]`(Part 2); `lint_wiki.main(argv) -> int`(오류가 있으면 1, 경고만 있으면 0).
- 코드: L01 인코딩, L02 frontmatter 파싱, L03 파일명, L04 필드·열거값, L05 소스 키, L06 H1·요약·절, L07 자리표시자, L08 링크 대상, L09 Markdown 링크, L10 공개→내부 링크, L11 용어 표지·표기·조사, L12 금지 표기, L13 표지 없는 등록 용어(경고), L14 미등록 약어, L15 `terms_pending` 불일치(경고), L20 용어표 형식; Part 2: L30 파일명 중복·충돌, L31 alias 충돌, L32 고아 노트(경고), L33 index 최신 여부(Task 10), L34 `references/` 불변 조건, L35 git 추적 경로, L36 공개 파일의 내부 문서명.

#### Part 1: 파일 단위 검사

- [ ] **Step 1: 실패하는 테스트를 쓴다**

`scripts/tests/test_lint_wiki.py`:
```python
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
    ("- [[DOC_A]]", "- [[HSFR_Anything]]", ("L10", "error")),
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


def test_frontmatter_filename_and_encoding(mini_vault, make_note, good_note_body):
    assert ("L04", "error") in lint(mini_vault, make_note("Typed", good_note_body, type="essay"))
    assert ("L04", "error") in lint(mini_vault, make_note("Checked", good_note_body, status="checked"))
    assert ("L05", "error") in lint(mini_vault, make_note("Keyless", good_note_body, sources=["DOC_Z"]))
    assert ("L03", "error") in lint(mini_vault, make_note("Bad Name", good_note_body))
    crlf = mini_vault / "wiki" / "Crlf.md"
    crlf.write_bytes(open(make_note("Tmp", good_note_body), "rb").read().replace(b"\n", b"\r\n"))
    assert ("L01", "error") in lint(mini_vault, str(crlf))
    broken = mini_vault / "wiki" / "Broken.md"
    broken.write_text("---\ntype: [\n---\n# x\n", encoding="utf-8")
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
    make_note("HSFR_Secret", good_note_body, root="internal", type="hsfr")
    pub = make_note("Sample", good_note_body.replace("- [[DOC_A]]", "- [[HSFR_Secret]]"))
    assert ("L10", "error") in lint(mini_vault, pub)
    assert lint(mini_vault, make_note("HSFR_Other", good_note_body, root="internal", type="hsfr")) == []


def test_terminology_format_error(mini_vault):
    t = mini_vault / "wiki" / "Terminology.md"
    t.write_text(t.read_text(encoding="utf-8").replace("| 미정 |", "| 보류 |"), encoding="utf-8")
    assert ("L20", "error") in lint(mini_vault, str(t))


def test_cli_file_mode(mini_vault, make_note, good_note_body, monkeypatch, capsys):
    monkeypatch.setattr(LW, "VAULT", str(mini_vault))
    assert LW.main([make_note("Sample", good_note_body)]) == 0
    assert LW.main([make_note("Bad", good_note_body.replace("## 해설", "## 설명"))]) == 1
    out = capsys.readouterr().out
    assert "wiki/Bad.md" in out and "L06" in out
```

- [ ] **Step 2: 실패를 확인한다**

Run: `"$PY" -m pytest scripts/tests/test_lint_wiki.py -q 2>&1 | tail -2`
Expected: `No module named 'lint_wiki'`.

- [ ] **Step 3: `scripts/lint_wiki.py` (Part 1)를 쓴다**

```python
"""lint_wiki.py — structure and terminology lint of wiki notes (spec §5.4 items 6-7, §6.4, §4.2; plan P1, P4, P7, P8).

Usage: python scripts/lint_wiki.py PATH... | --all [--root internal]
File checks (L01-L20) run on each PATH; --all adds the vault-wide checks (L30-L36).
Errors exit 1; warnings alone exit 0.
"""
import argparse
import os
import re
import sys

import notes as N
import terms as T

SCRIPTS = os.path.dirname(os.path.abspath(__file__))
VAULT = os.path.dirname(SCRIPTS)
TYPES = {"source", "regulation", "concept", "natrium", "synthesis", "map", "hsfr"}
STATUSES = {"draft", "checked", "reviewed", "disputed", "deprecated"}
INGEST = {"pending", "in_progress", "complete"}
NOTE_FIELDS = ("type", "aliases", "sources", "status", "verified", "term", "tags", "terms_pending")
CARD_FIELDS = ("type", "key", "title", "file", "pdf", "sha256_pdf", "sha256_md", "pdf_pages", "build", "ingest", "units")
SECTIONS = {"full": ["원문 사실", "해설", "관련 문서"], "short": ["관련 문서"],
            "source": ["서지", "구조", "알려진 모순", "관련 문서"]}
FILENAME = re.compile(r"^[A-Za-z0-9]+(?:[_.\-][A-Za-z0-9]+)*\.md$")
H1 = re.compile(r"^# \S.* \(.+\)$")
LINK = re.compile(r"(!?)\[\[([^\]|#]+)(?:#[^\]|]*)?(?:\|[^\]]*)?\]\]")
MDLINK = re.compile(r"(?<!!)\[[^\]\n]*\]\([^)\n]*\)")
PLACEHOLDER = re.compile(r"\bTBD\b|\bTODO\b|\(작성 예정\)|\{[^{}\n]{1,40}\}")
CARD_PENDING_TEXT = ("(인제스트 완료 시 작성)", "(sync 전)")
ABBR = re.compile(r"(?<![A-Za-z0-9_\-])([A-Z]{2,6})s?(?![A-Za-z0-9_\-])")
SENTINEL = ""


class Context:
    def __init__(self, vault):
        self.vault = vault
        self.public = {os.path.basename(p)[:-3]: p for p in N.wiki_notes(vault)}
        self.internal = {os.path.basename(p)[:-3]: p for p in N.wiki_notes(vault, "internal")}
        self.cards = N.load_cards(vault)
        self.terms, self.terms_error = {}, None
        tpath = os.path.join(vault, "wiki", "Terminology.md")
        if os.path.isfile(tpath):
            try:
                self.terms = T.load(tpath)
            except T.TermError as exc:
                self.terms_error = str(exc)
        self.assets = set()
        for d in (os.path.join(vault, "wiki", "assets"), os.path.join(vault, "references", "figures"),
                  os.path.join(vault, "internal", "references", "figures")):
            for _, _, files in os.walk(d):
                self.assets.update(files)


def _body_lines(note):
    return list(enumerate(note.body.split("\n"), note.offset + 1))


def _fields(ctx, note, F):
    fm, typ = note.fm, note.fm.get("type")
    for k in (CARD_FIELDS if typ == "source" else NOTE_FIELDS):
        if k not in fm:
            F(2, "L04", f"frontmatter field {k} missing")
    if typ == "source":
        if fm.get("key") != note.name:
            F(2, "L04", f"key {fm.get('key')!r} differs from the file name")
        if fm.get("ingest") not in INGEST:
            F(2, "L04", f"ingest {fm.get('ingest')!r} not in {sorted(INGEST)}")
        for u in fm.get("units") or []:
            if not isinstance(u, dict) or set(u) - {"unit", "status"} or u.get("status") not in INGEST:
                F(2, "L04", f"bad unit {u!r} (fields: unit, status)")
        return
    st = fm.get("status")
    if st not in STATUSES:
        F(2, "L04", f"status {st!r} not in {sorted(STATUSES)}")
    if st in ("checked", "reviewed") and not fm.get("verified"):
        F(2, "L04", f"status {st} needs a verified date")
    for k in ("aliases", "sources", "tags", "terms_pending"):
        if k in fm and not isinstance(fm[k], list):
            F(2, "L04", f"{k} must be a list")
    for key in (fm.get("sources") if isinstance(fm.get("sources"), list) else []):
        if key not in ctx.cards:
            F(2, "L05", f"source key {key} has no source card")


def _structure(note, F):
    typ = note.fm.get("type")
    lines = _body_lines(note)
    nonblank = [(i, l) for i, l in lines if l.strip()]
    first = nonblank[0][0] if nonblank else note.offset + 1
    if not nonblank or not H1.match(nonblank[0][1]):
        F(first, "L06", "first line must be '# 한국어 제목 (English Title)'")
    elif len(nonblank) < 2 or nonblank[1][1].strip() != "> [!abstract] 요약":
        F(first, "L06", "H1 must be followed by '> [!abstract] 요약'")
    if sum(1 for _, l in lines if l.startswith("# ")) > 1:
        F(first, "L06", "more than one H1")
    kind = "source" if typ == "source" else ("short" if typ in ("synthesis", "map") else "full")
    need = SECTIONS[kind]
    got = [t for t, _, _ in N.sections(note) if t in need]
    missing = [s for s in need if s not in got]
    if missing:
        F(first, "L06", "missing sections: " + ", ".join(missing))
    elif got != need:
        F(first, "L06", "sections out of order: " + " → ".join(need))


def _placeholders(note, F):
    pending_card = note.fm.get("type") == "source" and note.fm.get("ingest") != "complete"
    for i, l in _body_lines(note):
        for t in CARD_PENDING_TEXT:
            if t in l:
                if pending_card:
                    l = l.replace(t, "")
                else:
                    F(i, "L07", f"placeholder {t!r}")
        m = PLACEHOLDER.search(l)
        if m:
            F(i, "L07", f"placeholder {m.group(0)!r}")


def _links(ctx, note, is_internal, F):
    for i, l in _body_lines(note):
        for m in LINK.finditer(l):
            embed, target = m.group(1) == "!", m.group(2).strip()
            if embed:
                if os.path.basename(target) not in ctx.assets:
                    F(i, "L08", f"embedded file not found: {target}")
            elif target in ctx.public:
                continue
            elif target in ctx.internal or target.startswith("HSFR_"):
                if not is_internal:
                    F(i, "L10", f"public note links to internal note [[{target}]]")
                elif target not in ctx.internal:
                    F(i, "L08", f"link target does not exist: [[{target}]]")
            else:
                F(i, "L08", f"link target does not exist: [[{target}]]")
        if MDLINK.search(l):
            F(i, "L09", "Markdown link; use [[wikilink]]")


def _scan_text(line):
    s = T.MARKER.sub(SENTINEL, line)
    s = re.sub(r"`[^`]*`", " ", s)
    s = re.sub(r"\[\[[^\]]*\]\]", " ", s)
    return re.sub(r"\[[^\[\]\n]+\]", " ", s)


def _korean_lines(note):
    out = []
    for title, _, lines in N.sections(note):
        if title in ("", "해설"):
            out += [(i, l) for i, l in lines if not l.startswith("# ")]
    return out


def _terms(ctx, note, F):
    seen, pending = set(), set()
    for i, l in _korean_lines(note):
        for m in T.MARKER.finditer(l):
            tid, term = m.group(1), ctx.terms.get(m.group(1))
            if term is None:
                F(i, "L11", f"term marker {tid} is not in Terminology")
                continue
            if term.state == "용어 아님":
                F(i, "L11", f"term {tid} is 용어 아님; remove the marker")
                continue
            if term.state == "미정":
                pending.add(tid)
            want = T.display(term, tid not in seen)
            seen.add(tid)
            if not l[:m.start()].endswith(want):
                F(i, "L11", f"term {tid}: expected '{want}' before the marker")
                continue
            after = l[m.end():]
            fixed = T.retarget(after, T.final(want))
            if fixed != after:
                F(i, "L11", f"term {tid}: particle after '{want}' should start '{fixed[:2]}'")
        s = _scan_text(l)
        for term in ctx.terms.values():
            for bad in term.forbidden:
                if bad in s:
                    F(i, "L12", f"forbidden form '{bad}' (term {term.id})")
            if term.state == "확정" and term.korean and \
                    re.search(re.escape(term.korean) + r"(?:\([^()]*\))?+(?!" + SENTINEL + ")", s):
                F(i, "L13", f"'{term.korean}' without marker %%t:{term.id}%%", "warning")
        for m in ABBR.finditer(s):
            if s[m.end():m.end() + 1] == SENTINEL:
                continue
            base = m.group(1)
            if any(base in (t.abbr, t.id) for t in ctx.terms.values()):
                F(i, "L13", f"'{base}' without term marker", "warning")
            else:
                F(i, "L14", f"abbreviation '{base}' is not in Terminology")
    listed = note.fm.get("terms_pending") or []
    if isinstance(listed, list) and sorted(listed) != sorted(pending):
        F(2, "L15", f"terms_pending {sorted(listed)} differs from markers {sorted(pending)}; run sync_terms.py --apply",
          "warning")


def lint_file(ctx, path):
    rel = N.relpath(path, ctx.vault)
    out = []

    def F(line, code, msg, level="error"):
        out.append(N.Finding(rel, line, code, msg, level))

    with open(path, "rb") as f:
        raw = f.read()
    if raw.startswith(b"\xef\xbb\xbf"):
        F(1, "L01", "BOM")
    if b"\r" in raw:
        F(1, "L01", "CR line endings")
    if "�" in raw.decode("utf-8", errors="replace"):
        F(1, "L01", "invalid UTF-8 or U+FFFD")
    if not FILENAME.match(os.path.basename(path)):
        F(1, "L03", "file name must be ASCII letters, digits, '_', '.', '-'")
    try:
        note = N.load(path)
    except (N.NoteError, UnicodeDecodeError) as exc:
        F(1, "L02", str(exc))
        return out
    if not note.fm:
        F(1, "L02", "frontmatter missing")
        return out
    if note.fm.get("type") not in TYPES:
        F(2, "L04", f"type {note.fm.get('type')!r} not in {sorted(TYPES)}")
        return out
    _fields(ctx, note, F)
    _structure(note, F)
    _placeholders(note, F)
    _links(ctx, note, rel.startswith("internal/"), F)
    if note.name == "Terminology" and ctx.terms_error:
        F(1, "L20", ctx.terms_error)
    if note.fm.get("type") != "source":
        _terms(ctx, note, F)
    return out


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("paths", nargs="*")
    ap.add_argument("--all", action="store_true")
    ap.add_argument("--root")
    a = ap.parse_args(argv)
    if not a.paths and not a.all:
        ap.error("give PATH... or --all")
    sys.stdout.reconfigure(encoding="utf-8")
    ctx = Context(VAULT)
    # without PATHs: the public tree, or internal/ with --root internal (each repo's pre-commit lints its own notes)
    paths = [os.path.abspath(p) for p in a.paths] or N.wiki_notes(VAULT, a.root)
    findings = []
    for p in paths:
        findings += lint_file(ctx, p)
    for f in findings:
        print(f)
    errors = sum(1 for f in findings if f.level == "error")
    print(f"lint_wiki: {len(paths)} notes, {errors} errors, {len(findings) - errors} warnings")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
```

주의: `test_note_findings`의 `("> [!abstract] 요약\n", "")` 사례에서 요약 줄이 없어진 노트는 L06만 기대한다(`in` 비교). `_korean_lines`는 H1 줄만 제외하므로 `> 가나(…)` 줄은 여전히 첫 등장으로 검사된다.

- [ ] **Step 4: 통과를 확인한다**

Run: `"$PY" -m pytest scripts/refclean/tests scripts/tests -q 2>&1 | tail -1`
Expected: `342 passed` (319 + 23: 1 + 16 + 1 + 1 + 1 + 1 + 1 + 1).

- [ ] **Step 5: 실제 vault의 파일 단위 lint**

Run: `"$PY" scripts/lint_wiki.py wiki/*.md; echo "exit $?"`
Expected: `lint_wiki: 12 notes, 0 errors, 0 warnings`, `exit 0`. 소스 카드의 sync 블록(표·그림 제목)에서 L07(`{…}`)이나 L14가 나오면 멈추고 해당 줄을 보고한다. 원문 제목은 고치지 않으며, 규칙(`PLACEHOLDER` 또는 카드의 sync 블록 제외)을 조정할지 사용자에게 묻는다.

- [ ] **Step 6: 커밋**

```bash
git add scripts/lint_wiki.py scripts/tests/test_lint_wiki.py && git commit -q -m "feat(lint_wiki): per-file structure, link and terminology checks

Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>"
```

#### Part 2: vault 전체 검사

범위 규칙: `root=None`은 공개 트리의 결과만, `root="internal"`은 `internal/` 경로의 결과만 남긴다(L35는 공개 저장소의 문제이므로 `root=None`에서만 계산하고 거르지 않는다). 파일명 충돌(L30)은 두 트리를 합쳐 판정하되, 뒤에 나온 쪽 경로에 보고한다(공개 트리를 먼저 읽는다). `references/`가 없는 clone에서는 L34를 건너뛰고 경고 한 줄을 남긴다.

- [ ] **Step 7: 실패하는 테스트를 추가한다** (`test_lint_wiki.py` 끝)

```python
import shutil
import subprocess


def vault_codes(vault, root=None):
    return [(f.path, f.code, f.level) for f in LW.lint_vault(LW.Context(str(vault)), root)]


def test_clean_vault_has_no_vault_findings(mini_vault):
    assert vault_codes(mini_vault) == []


def test_name_collisions(mini_vault, make_note, good_note_body):
    make_note("Sample", good_note_body)
    make_note("SAMPLE", good_note_body, root="internal", type="hsfr")
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
    (mini_vault / "references" / "Orphan_Ref.md").write_text("x\n", encoding="utf-8")
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
    make_note("HSFR_Trial", good_note_body, root="internal", type="hsfr", title="Zeta Loop Pump Trial")
    (mini_vault / "meta" / "status.md").write_text("다음: Zeta Loop Pump Trial 정리\n", encoding="utf-8")
    run("add", "meta/status.md", "wiki")
    run("add", "-f", "internal/wiki/HSFR_Trial.md")
    got = vault_codes(mini_vault)
    assert ("internal/wiki/HSFR_Trial.md", "L35", "error") in got
    assert ("meta/status.md", "L36", "error") in got
    assert not [g for g in vault_codes(mini_vault, root="internal") if g[1] in ("L35", "L36")]


def test_cli_all(mini_vault, monkeypatch):
    monkeypatch.setattr(LW, "VAULT", str(mini_vault))
    assert LW.main(["--all"]) == 0
    (mini_vault / "references" / "Orphan_Ref.md").write_text("x\n", encoding="utf-8")
    assert LW.main(["--all"]) == 1
```

- [ ] **Step 8: 실패를 확인한다**

Run: `"$PY" -m pytest scripts/tests/test_lint_wiki.py -q 2>&1 | tail -2`
Expected: 8건 실패(`module 'lint_wiki' has no attribute 'lint_vault'`), 나머지 23건 통과.

- [ ] **Step 9: `lint_vault`를 추가한다**

`lint_wiki.py`의 import에 `hashlib`, `subprocess`를 추가하고, 상수 아래에 넣는다.
```python
PUBLIC_TRACKED = re.compile(r"^(wiki/|meta/|templates/|\.claude/|log\.md$|index\.md$|CLAUDE\.md$|AGENTS\.md$|README\.md$)")
LOCAL_ONLY = re.compile(r"(?i)^(internal|references|inbox|raw)/")
```

`main` 앞에 추가:
```python
def _sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def _tracked(vault):
    if not os.path.isdir(os.path.join(vault, ".git")):
        return None
    r = subprocess.run(["git", "-C", vault, "-c", "core.quotepath=false", "ls-files", "-z"], capture_output=True)
    return [p for p in r.stdout.decode("utf-8").split("\0") if p] if r.returncode == 0 else None


def lint_vault(ctx, root=None):
    v, out = ctx.vault, []

    def F(path, line, code, msg, level="error"):
        out.append(N.Finding(path, line, code, msg, level))

    notes_all = list(ctx.public.items()) + list(ctx.internal.items())
    names = {}
    for stem, p in notes_all:
        rel = N.relpath(p, v)
        if stem.casefold() in names:
            F(rel, 1, "L30", f"file name collides with {names[stem.casefold()]} (case-insensitive)")
        else:
            names[stem.casefold()] = rel
    refs_present = {}
    for r in (None, "internal"):
        d = N.tree(v, r)["refs"]
        refs_present[r] = os.path.isdir(d)
        for fn in (sorted(os.listdir(d)) if refs_present[r] else []):
            if fn.endswith(".md") and fn[:-3].casefold() in names:
                F(names[fn[:-3].casefold()], 1, "L30", f"file name equals cleaned file {N.relpath(os.path.join(d, fn), v)}")

    alias_owner, inbound, loaded = {}, {}, {}
    for stem, p in notes_all:
        rel = N.relpath(p, v)
        try:
            note = N.load(p)
        except (N.NoteError, UnicodeDecodeError):
            continue
        loaded[stem] = (rel, note.fm)
        aliases = note.fm.get("aliases") if isinstance(note.fm.get("aliases"), list) else []
        for a in aliases:
            k = str(a).casefold()
            if k in names and names[k] != rel:
                F(rel, 2, "L31", f"alias '{a}' equals the note name {names[k]}")
            elif k in alias_owner and alias_owner[k] != rel:
                F(rel, 2, "L31", f"alias '{a}' is also used by {alias_owner[k]}")
            else:
                alias_owner.setdefault(k, rel)
        for m in LINK.finditer(note.body):
            if not m.group(1) and m.group(2).strip() != stem:
                inbound.setdefault(m.group(2).strip(), set()).add(stem)
    for stem, (rel, fm) in loaded.items():
        if fm.get("type") not in ("source", "map") and not inbound.get(stem):
            F(rel, 1, "L32", "no other note links here", "warning")

    for r in (None, "internal"):
        d = N.tree(v, r)["refs"]
        cards = {k: c for k, c in ctx.cards.items() if c["root"] == r}
        if not refs_present[r]:
            if cards:
                F(N.relpath(d, v), 1, "L34", "references/ not present; source invariants skipped", "warning")
            continue
        card_files = {c["fm"].get("file") for c in cards.values()}
        for fn in sorted(os.listdir(d)):
            rel = N.relpath(os.path.join(d, fn), v)
            if fn.endswith(".md") and rel not in card_files:
                F(rel, 1, "L34", "cleaned file has no source card")
        for key, c in sorted(cards.items()):
            fm, crel = c["fm"], N.relpath(c["path"], v)
            if fm.get("file") and not os.path.isfile(os.path.join(v, fm["file"])):
                F(crel, 2, "L34", f"cleaned file missing: {fm['file']}")
            elif fm.get("ingest") == "complete":
                for fld, sha in (("file", "sha256_md"), ("pdf", "sha256_pdf")):
                    p = os.path.join(v, fm.get(fld) or "")
                    if not os.path.isfile(p) or _sha256(p) != fm.get(sha):
                        F(crel, 2, "L34", f"ingest complete but {fld} is missing or its SHA-256 differs from the card")

    if root is None:
        tracked = _tracked(v)
        if tracked is not None:
            for p in tracked:
                if LOCAL_ONLY.match(p):
                    F(p, 1, "L35", "local-only path is tracked by git #1")
            if os.path.isdir(os.path.join(v, "internal")):
                import leak_guard as LG
                inames = LG.internal_names(v)
                for p in tracked:
                    full = os.path.join(v, p)
                    if not PUBLIC_TRACKED.match(p) or not os.path.isfile(full):
                        continue
                    with open(full, encoding="utf-8", errors="replace") as fh:
                        for i, line in enumerate(fh.read().split("\n"), 1):
                            for _, n in LG.scan([(p, line)], inames):
                                F(p, i, "L36", f"internal document name \"{n}\" in a public file")
    return [f for f in out if f.code == "L35" or f.path.startswith("internal/") == (root == "internal")]
```

`main`의 `for p in paths: findings += lint_file(ctx, p)` 다음 줄에 넣는다.
```python
    if a.all:
        findings += lint_vault(ctx, a.root)
```

- [ ] **Step 10: 통과를 확인한다**

Run: `"$PY" -m pytest scripts/refclean/tests scripts/tests -q 2>&1 | tail -1`
Expected: `350 passed`.

- [ ] **Step 11: 실제 vault 전체 lint**

```bash
cd /c/Obsidian/ripb && "$PY" scripts/lint_wiki.py --all; echo "exit $?"; "$PY" scripts/lint_wiki.py --all --root internal | tail -1
```
Expected: 첫 명령 `lint_wiki: 12 notes, 0 errors, 0 warnings`, `exit 0`. 내부 트리의 결과(둘째 줄)는 개수만 기록하고 내용은 `internal/status.md`에만 적는다. 공개 트리에서 L36이 나오면 멈추고 파일·줄만 보고한다.

- [ ] **Step 12: 커밋**

```bash
git add scripts/lint_wiki.py scripts/tests/test_lint_wiki.py && git commit -q -m "feat(lint_wiki): vault-wide names, aliases, orphans, source invariants, git and leak checks

Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>"
```

### Task 10: index 생성 (`build_index.py`)과 lint L33

index 재생성은 생성물 한 파일을 쓰는 작업이므로 기본 동작이 쓰기이고, `--check`가 최신 여부만 판정한다(노트 일괄 수정의 dry-run 규칙 대상이 아니다).

**Files:**
- Create: `scripts/build_index.py`, `scripts/tests/test_build_index.py`, `index.md`
- Modify: `scripts/lint_wiki.py` (L33), `scripts/tests/conftest.py` (`mini_vault`가 index를 만든다), `scripts/tests/test_lint_wiki.py`

**Interfaces:**
- Consumes: `notes.wiki_notes`, `notes.load`, `notes.write_text`, `notes.relpath`, `terms.MARKER`
- Produces: `build_index.HEADER: str`; `build_index.index_path(vault, root=None) -> str`(`index.md` 또는 `internal/index.md`); `build_index.summary(note) -> str`; `build_index.render(vault, root=None) -> str`; `build_index.write(vault, root=None) -> str`(쓴 경로); `build_index.main(argv) -> int`(`--check`에서 오래되었으면 1).

- [ ] **Step 1: 실패하는 테스트를 쓴다**

`scripts/tests/test_build_index.py`:
```python
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
```

`scripts/tests/test_lint_wiki.py` 끝에 추가:
```python
def test_index_staleness(mini_vault, make_note, good_note_body):
    assert vault_codes(mini_vault) == []
    make_note("Sample", good_note_body)
    assert ("index.md", "L33", "error") in vault_codes(mini_vault)
```

`scripts/tests/conftest.py`의 `mini_vault`에서 `return tmp_path` 바로 앞에 넣는다.
```python
    import build_index
    build_index.write(str(tmp_path))
```

- [ ] **Step 2: 실패를 확인한다**

Run: `"$PY" -m pytest scripts/tests -q 2>&1 | tail -2`
Expected: `mini_vault`를 쓰는 테스트 전부가 `No module named 'build_index'`로 오류.

- [ ] **Step 3: `scripts/build_index.py`를 쓴다**

```python
"""build_index.py — regenerate index.md (public) or internal/index.md from note types and summaries (spec §7.5).

Usage: python scripts/build_index.py [--root internal] [--check]
Writes by default (one generated file); --check exits 1 when the file is missing or stale.
Line per note: `- [[Name]] — <first sentence of the 요약 callout>`; source cards whose summary is still the
template text show their title. disputed notes are flagged; deprecated notes move to a separate section.
"""
import argparse
import os
import re
import sys

import notes as N
import terms as T

SCRIPTS = os.path.dirname(os.path.abspath(__file__))
VAULT = os.path.dirname(SCRIPTS)
ORDER = [("source", "원문"), ("regulation", "규제"), ("concept", "개념"), ("natrium", "Natrium"),
         ("synthesis", "종합"), ("map", "지도"), ("hsfr", "H-SFR")]
HEADER = "# index\n\n<!-- build_index.py가 생성한다. 손으로 고치지 않는다. -->\n"
TEMPLATE_SUMMARY = "(인제스트 완료 시 작성)"


def index_path(vault, root=None):
    return os.path.join(vault, root, "index.md") if root else os.path.join(vault, "index.md")


def summary(note):
    lines = note.body.split("\n")
    text = ""
    for i, line in enumerate(lines):
        if line.strip() == "> [!abstract] 요약":
            block = []
            for nxt in lines[i + 1:]:
                if not nxt.startswith(">"):
                    break
                block.append(nxt[1:].strip())
            text = T.MARKER.sub("", " ".join(block)).strip()
            break
    if not text or text == TEMPLATE_SUMMARY:
        return str(note.fm.get("title") or "")
    m = re.match(r"^(.+?[.!?])(?:\s|$)", text)
    return m.group(1) if m else text


def render(vault, root=None):
    groups, deprecated = {t: [] for t, _ in ORDER}, []
    for p in N.wiki_notes(vault, root):
        try:
            note = N.load(p)
        except (N.NoteError, UnicodeDecodeError):
            continue
        typ, status = note.fm.get("type"), note.fm.get("status")
        if typ not in groups:
            continue
        line = f"- [[{note.name}]] — {summary(note)}" + (" (disputed)" if status == "disputed" else "")
        (deprecated if status == "deprecated" else groups[typ]).append(line)
    parts = [HEADER]
    for typ, label in ORDER:
        if groups[typ]:
            parts.append(f"\n## {label} ({typ})\n\n" + "\n".join(groups[typ]) + "\n")
    if deprecated:
        parts.append("\n## 대체됨 (deprecated)\n\n" + "\n".join(deprecated) + "\n")
    return "".join(parts)


def write(vault, root=None):
    path = index_path(vault, root)
    N.write_text(path, render(vault, root))
    return path


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--root")
    ap.add_argument("--check", action="store_true")
    a = ap.parse_args(argv)
    sys.stdout.reconfigure(encoding="utf-8")
    path, text = index_path(VAULT, a.root), render(VAULT, a.root)
    rel = N.relpath(path, VAULT)
    if a.check:
        have = open(path, encoding="utf-8").read() if os.path.isfile(path) else None
        print(f"build_index: {rel} {'up to date' if have == text else 'missing or stale'}")
        return 0 if have == text else 1
    N.write_text(path, text)
    print(f"build_index: wrote {rel} ({text.count(chr(10) + '- [[')} notes)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
```

- [ ] **Step 4: lint에 L33을 넣는다**

`lint_wiki.py`의 `lint_vault`에서 마지막 `return` 바로 앞에 넣는다.
```python
    import build_index as BI
    ipath = BI.index_path(v, root)
    have = open(ipath, encoding="utf-8").read() if os.path.isfile(ipath) else None
    if have != BI.render(v, root):
        F(N.relpath(ipath, v), 1, "L33", "index is missing or stale; run build_index.py" + (f" --root {root}" if root else ""))
```

- [ ] **Step 5: 통과를 확인한다**

Run: `"$PY" -m pytest scripts/refclean/tests scripts/tests -q 2>&1 | tail -1`
Expected: `354 passed`.

- [ ] **Step 6: 실제 index를 만든다**

```bash
cd /c/Obsidian/ripb && "$PY" scripts/build_index.py && head -8 index.md && "$PY" scripts/lint_wiki.py --all | tail -1
```
Expected: `build_index: wrote index.md (12 notes)`; `## 원문 (source)` 아래 소스 카드 11줄; lint `0 errors`. (내부 index는 Task 15에서 내부 hook을 연결할 때 만든다.)

- [ ] **Step 7: 커밋**

```bash
git add scripts/build_index.py scripts/tests/test_build_index.py scripts/lint_wiki.py scripts/tests/conftest.py scripts/tests/test_lint_wiki.py index.md && git commit -q -m "feat(index): build_index.py and generated index.md; lint L33 staleness

Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>"
```

### Task 11: log 추가 (`append_log.py`)

**Files:**
- Create: `scripts/append_log.py`, `scripts/tests/test_append_log.py`

**Interfaces:**
- Produces: `append_log.TYPES`; `append_log.LogError(Exception)`; `append_log.entry(date: str, typ: str, title: str, items: list[str]) -> str`; `append_log.append(vault, root, date, typ, title, items) -> str`(쓴 경로); `append_log.main(argv) -> int`. 항목 형식은 기존 `log.md`와 같다: 빈 줄, `## [YYYY-MM-DD] <type> | <제목>`, `- <요점>` 줄들. 커밋 해시는 쓰지 않는다(P1).

- [ ] **Step 1: 실패하는 테스트를 쓴다**

`scripts/tests/test_append_log.py`:
```python
import pytest

import append_log as AL

HEAD = "# log\n\n설명.\n\n## [2026-09-14] init | 시작\n- 첫 항목.\n"


def make_log(base, text=HEAD):
    base.mkdir(parents=True, exist_ok=True)
    p = base / "log.md"
    p.write_bytes(text.encode("utf-8"))
    return p


def test_append_keeps_previous_bytes(tmp_path):
    p = make_log(tmp_path)
    before = p.read_bytes()
    AL.append(str(tmp_path), None, "2026-09-20", "ingest", "NEI 18-04 §3", ["노트 3개 신규.", "검사 통과."])
    after = p.read_bytes()
    assert after.startswith(before)
    assert after[len(before):].decode("utf-8") == "\n## [2026-09-20] ingest | NEI 18-04 §3\n- 노트 3개 신규.\n- 검사 통과.\n"


def test_missing_final_newline_is_supplied(tmp_path):
    p = make_log(tmp_path, HEAD.rstrip("\n"))
    AL.append(str(tmp_path), None, "2026-09-20", "docs", "t", ["a"])
    assert "- 첫 항목.\n\n## [2026-09-20] docs | t\n- a\n" in p.read_text(encoding="utf-8")


@pytest.mark.parametrize("date,typ,title,items", [
    ("2026-9-20", "docs", "t", ["a"]),
    ("2026-09-20", "misc", "t", ["a"]),
    ("2026-09-20", "docs", "two\nlines", ["a"]),
    ("2026-09-20", "docs", "", ["a"]),
    ("2026-09-20", "docs", "t", []),
    ("2026-09-20", "docs", "t", ["a\r"]),
])
def test_invalid_entries_are_refused_and_file_untouched(tmp_path, date, typ, title, items):
    p = make_log(tmp_path)
    before = p.read_bytes()
    with pytest.raises(AL.LogError):
        AL.append(str(tmp_path), None, date, typ, title, items)
    assert p.read_bytes() == before


def test_internal_root_and_cli(tmp_path, monkeypatch):
    make_log(tmp_path)
    ip = make_log(tmp_path / "internal")
    monkeypatch.setattr(AL, "VAULT", str(tmp_path))
    assert AL.main(["--root", "internal", "--type", "docs", "--title", "내부", "--item", "x", "--date", "2026-09-20"]) == 0
    assert ip.read_text(encoding="utf-8").endswith("## [2026-09-20] docs | 내부\n- x\n")
    assert AL.main(["--type", "nope", "--title", "t", "--item", "x"]) == 1
```

- [ ] **Step 2: 실패를 확인한다**

Run: `"$PY" -m pytest scripts/tests/test_append_log.py -q 2>&1 | tail -2`
Expected: `No module named 'append_log'`.

- [ ] **Step 3: `scripts/append_log.py`를 쓴다**

```python
"""append_log.py — append one entry to log.md or internal/log.md (spec §7.5; plan P1).

Usage: python scripts/append_log.py --type ingest --title "NEI 18-04 §3" --item "..." [--item ...]
                                    [--date YYYY-MM-DD] [--root internal]
The file is opened in append mode; earlier bytes are never rewritten. Commit hashes are not recorded.
"""
import argparse
import datetime
import os
import re
import sys

SCRIPTS = os.path.dirname(os.path.abspath(__file__))
VAULT = os.path.dirname(SCRIPTS)
TYPES = ("init", "chore", "feat", "fix", "docs", "ingest", "terms", "lint", "audit", "query")


class LogError(Exception):
    pass


def _one_line(value, what):
    if not value or not value.strip():
        raise LogError(f"{what} is empty")
    for bad, name in (("\n", "newline"), ("\r", "CR"), ("﻿", "BOM"), ("�", "U+FFFD")):
        if bad in value:
            raise LogError(f"{what} contains {name}")
    return value.strip()


def entry(date, typ, title, items):
    if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", date or ""):
        raise LogError(f"date {date!r} is not YYYY-MM-DD")
    if typ not in TYPES:
        raise LogError(f"type {typ!r} not in {TYPES}")
    if not items:
        raise LogError("at least one --item is required")
    lines = [f"- {_one_line(i, 'item')}\n" for i in items]
    return f"\n## [{date}] {typ} | {_one_line(title, 'title')}\n" + "".join(lines)


def append(vault, root, date, typ, title, items):
    path = os.path.join(vault, root, "log.md") if root else os.path.join(vault, "log.md")
    if not os.path.isfile(path):
        raise LogError(f"{path} does not exist")
    text = entry(date, typ, title, items)
    with open(path, "rb") as f:
        data = f.read()
    with open(path, "a", encoding="utf-8", newline="\n") as f:
        f.write(("" if data.endswith(b"\n") else "\n") + text)
    return path


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--type", required=True)
    ap.add_argument("--title", required=True)
    ap.add_argument("--item", action="append", default=[])
    ap.add_argument("--date", default=datetime.date.today().isoformat())
    ap.add_argument("--root")
    a = ap.parse_args(argv)
    sys.stdout.reconfigure(encoding="utf-8")
    try:
        path = append(VAULT, a.root, a.date, a.type, a.title, a.item)
    except LogError as exc:
        print(f"append_log: error: {exc}", file=sys.stderr)
        return 1
    print(f"append_log: appended to {os.path.relpath(path, VAULT)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
```

- [ ] **Step 4: 통과를 확인한다**

Run: `"$PY" -m pytest scripts/refclean/tests scripts/tests -q 2>&1 | tail -1`
Expected: `363 passed` (354 + 9: 1 + 1 + 6 + 1).

- [ ] **Step 5: 커밋과 세션 B 종료 기록**

```bash
git add scripts/append_log.py scripts/tests/test_append_log.py && git commit -q -m "feat(log): append-only log entries

Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>"
```
`meta/status.md`의 "다음 작업" 1번을 `Phase 2 세션 C: Task 12부터`로 바꾸고, "존재하는 도구"에 `notes.py`, `citations.py`, `terms.py`, `leak_guard.py`, `verify_quotes.py`, `lint_wiki.py`, `build_index.py`, `append_log.py`를 옮겨 적는다. 이어서 `"$PY" scripts/append_log.py --type feat --title "Phase 2 세션 B: 검사 도구" --item "verify_quotes, lint_wiki, build_index, append_log와 보조 모듈 3종. 테스트 363건."`를 실행하고, `"$PY" scripts/build_index.py --check`(0)를 확인한 뒤 `git add meta/status.md log.md && git commit -q -m "docs(status): phase 2 session B done"`(끝에 Co-Authored-By 줄).

# 세션 C

### Task 12: 용어 전파 (`sync_terms.py`)

**Files:**
- Create: `scripts/sync_terms.py`, `scripts/tests/test_sync_terms.py`, `meta/terms_state.json`
- Modify: `scripts/notes.py` (`korean_lines` 이동), `scripts/lint_wiki.py` (`_korean_lines` 삭제 후 `N.korean_lines` 사용)

**Interfaces:**
- Consumes: `terms.*` (Task 7), `notes.*` (Task 2, 6, 8)
- Produces: `notes.korean_lines(note) -> list[tuple[int, str]]`(첫 H2 앞 블록에서 H1을 뺀 줄과 `해설` 절의 줄); `sync_terms.STATE = "meta/terms_state.json"`; `sync_terms.load_state(vault) -> dict[str, Term]`; `sync_terms.terms_changed(vault) -> list[str]`(용어표와 마지막 동기화 상태가 다른 ID, 정렬); `sync_terms.plan_note(note, terms, old, rel, report) -> tuple[dict, str]`; `sync_terms.main(argv) -> int`(충돌이 있으면 1). Task 13의 `session_start`가 `terms_changed`를 쓴다.

동작 규칙:
- 대상: `wiki/`, `internal/wiki/`의 노트 중 `type: source`를 뺀 전부. 범위: `notes.korean_lines`(설계 §6.2 "한국어 절에만"; 표의 한국어 셀은 Phase 3 시범 뒤 추가 여부를 정한다).
- 표지 앞 표시 문자열을 찾는 방법: 이전 상태(`terms_state.json`)의 용어와 현재 용어표의 용어 각각에 대해 첫 등장·이후 표기를 후보로 두고, 긴 후보부터 표지 바로 앞 문자열의 끝과 비교한다. 어느 후보와도 맞지 않으면 충돌로 보고하고 그 표지는 고치지 않는다(사용자가 손으로 고친 경우).
- 조사: 새 표시의 `terms.final`로 `terms.retarget`. 영어 단어 뒤의 조사는 고치지 않고 `check particle`로 보고한다(P3).
- `용어 아님`: 표지만 지우고 표시 문자열은 둔다.
- `terms_pending`: 남은 표지 중 `미정` ID의 정렬 목록(P5).
- `term: ID` 노트: 용어가 `확정`이면 H1을 `# 한국어 (English)`로, aliases에서 이전 한국어를 빼고 새 한국어를 넣는다.
- dry-run이 기본. `--apply`는 노트를 쓰고, 충돌이 없을 때만 `terms_state.json`을 갱신한다(충돌 표지의 이전 표시 후보를 잃지 않기 위해).

- [ ] **Step 1: `korean_lines`를 옮긴다**

`scripts/notes.py` 끝에 추가:
```python
def korean_lines(note):
    """Korean prose lines that carry term markers (spec §6.2): the block before the first H2 without the H1, and 해설."""
    out = []
    for title, _, lines in sections(note):
        if title in ("", "해설"):
            out += [(i, l) for i, l in lines if not l.startswith("# ")]
    return out
```
`scripts/lint_wiki.py`에서 `_korean_lines` 함수를 지우고 `_terms` 안의 `_korean_lines(note)`를 `N.korean_lines(note)`로 바꾼다.

Run: `"$PY" -m pytest scripts/tests -q 2>&1 | tail -1` → Expected: `146 passed` (이동만 했으므로 Task 11 이후와 같은 수).

- [ ] **Step 2: 실패하는 테스트를 쓴다**

`scripts/tests/test_sync_terms.py`:
```python
import json

import pytest

import lint_wiki as LW
import notes as N
import sync_terms as ST

LBE_ROW = "| LBE | Licensing Basis Event | LBE | 가나 | 약어 | 나가 | [DOC_A §3.2 p.3] | 확정 | |"
RAC_ROW = "| RAC | Reactor Air Cooling System | RAC |  | 약어 |  | [DOC_A §3.2 p.3] | 미정 | |"


def set_row(vault, old, new):
    t = vault / "wiki" / "Terminology.md"
    text = t.read_text(encoding="utf-8")
    assert old in text
    t.write_text(text.replace(old, new), encoding="utf-8")


@pytest.fixture
def synced(mini_vault, monkeypatch):
    monkeypatch.setattr(ST, "VAULT", str(mini_vault))
    assert ST.main(["--apply"]) == 0
    return mini_vault


def body_of(path):
    return N.read_note(path)[1]


def test_dry_run_writes_nothing(synced, make_note, good_note_body):
    p = make_note("Sample", good_note_body)
    set_row(synced, LBE_ROW, LBE_ROW.replace("가나 |", "가닥 |"))
    before = open(p, "rb").read()
    assert ST.main([]) == 0
    assert open(p, "rb").read() == before
    state = json.load(open(synced / "meta" / "terms_state.json", encoding="utf-8"))
    assert state["terms"]["LBE"]["korean"] == "가나"


def test_korean_change_rewrites_displays_and_particles(synced, make_note, good_note_body):
    p = make_note("Sample", good_note_body)
    set_row(synced, LBE_ROW, LBE_ROW.replace("가나 |", "가닥 |"))
    assert ST.main(["--apply"]) == 0
    b = body_of(p)
    assert "> 가닥(Licensing Basis Event)%%t:LBE%%에 관한" in b and "LBE%%t:LBE%%는 세 종류" in b
    set_row(synced, LBE_ROW.replace("가나 |", "가닥 |"), LBE_ROW.replace("가나 | 약어 |", "가닥 | 한국어 |"))
    assert ST.main(["--apply"]) == 0
    assert "가닥%%t:LBE%%은 세 종류" in body_of(p)
    assert LW.lint_file(LW.Context(str(synced)), p) == []


def test_pending_to_confirmed_updates_display_and_pending_field(synced, make_note, good_note_body):
    body = good_note_body.replace("세 종류이다.", "Reactor Air Cooling System%%t:RAC%%도 있고 RAC%%t:RAC%%를 쓴다.")
    p = make_note("Sample", body)
    assert ST.main(["--apply"]) == 0
    assert N.read_note(p)[0]["terms_pending"] == ["RAC"]
    set_row(synced, RAC_ROW, "| RAC | Reactor Air Cooling System | RAC | 가날 | 약어 |  | [DOC_A §3.2 p.3] | 확정 | |")
    assert ST.main(["--apply"]) == 0
    fm, b = N.read_note(p)
    assert "가날(Reactor Air Cooling System)%%t:RAC%%도 있고 RAC%%t:RAC%%를 쓴다." in b
    assert fm["terms_pending"] == []
    assert LW.lint_file(LW.Context(str(synced)), p) == []


def test_not_a_term_removes_marker_and_keeps_text(synced, make_note, good_note_body):
    p = make_note("Sample", good_note_body)
    set_row(synced, LBE_ROW, "| LBE | Licensing Basis Event | LBE |  |  |  |  | 용어 아님 | |")
    assert ST.main(["--apply"]) == 0
    b = body_of(p)
    assert "%%t:LBE%%" not in b and "> 가나(Licensing Basis Event)에 관한" in b and "LBE는 세 종류" in b


def test_conflict_is_reported_left_alone_and_state_kept(synced, make_note, good_note_body, capsys):
    p = make_note("Sample", good_note_body.replace("LBE%%t:LBE%%는", "엘비이%%t:LBE%%는"))
    set_row(synced, LBE_ROW, LBE_ROW.replace("가나 |", "가닥 |"))
    before = body_of(p)
    assert ST.main(["--apply"]) == 1
    assert "conflict wiki/Sample.md" in capsys.readouterr().out
    assert "엘비이%%t:LBE%%는" in body_of(p) and "가닥(Licensing Basis Event)%%t:LBE%%에" in body_of(p)
    assert body_of(p) != before
    assert ST.terms_changed(str(synced)) == ["LBE"]          # state not advanced


def test_particle_after_english_is_reported(synced, make_note, good_note_body, capsys):
    make_note("Sample", good_note_body.replace("세 종류이다.", "Reactor Air Cooling System%%t:RAC%%는 미정이다."))
    capsys.readouterr()
    ST.main([])
    assert "check particle wiki/Sample.md" in capsys.readouterr().out


def test_term_note_title_and_alias_follow_table(synced, make_note, good_note_body):
    p = make_note("Licensing_Basis_Event", good_note_body, term="LBE", aliases=["가나", "LBE"])
    set_row(synced, LBE_ROW, LBE_ROW.replace("가나 |", "가닥 |"))
    assert ST.main(["--apply"]) == 0
    fm, b = N.read_note(p)
    assert b.startswith("# 가닥 (Licensing Basis Event)\n") and fm["aliases"] == ["LBE", "가닥"]


def test_terms_changed(synced):
    assert ST.terms_changed(str(synced)) == []
    set_row(synced, LBE_ROW, LBE_ROW.replace("가나 |", "가닥 |"))
    assert ST.terms_changed(str(synced)) == ["LBE"]
```

- [ ] **Step 3: 실패를 확인한다**

Run: `"$PY" -m pytest scripts/tests/test_sync_terms.py -q 2>&1 | tail -2`
Expected: `No module named 'sync_terms'`.

- [ ] **Step 4: `scripts/sync_terms.py`를 쓴다**

```python
"""sync_terms.py — propagate wiki/Terminology.md to the term markers of every note (spec §6.2, §6.4; plan P2, P3, P5).

Usage: python scripts/sync_terms.py [--apply]
Dry-run by default. --apply writes the notes and, when there is no conflict, meta/terms_state.json.
Exit 1 on a table error or a conflict (display text before a marker matches neither the previous nor the current
table; left unchanged for the user).
"""
import argparse
import json
import os
import re
import sys

import notes as N
import terms as T

SCRIPTS = os.path.dirname(os.path.abspath(__file__))
VAULT = os.path.dirname(SCRIPTS)
STATE = os.path.join("meta", "terms_state.json")
_JOSA_AHEAD = re.compile(r"^(으로|로|은|는|이|가|을|를|과|와)(?![가-힣])")


def load_state(vault):
    p = os.path.join(vault, STATE)
    if not os.path.isfile(p):
        return {}
    with open(p, encoding="utf-8") as f:
        data = json.load(f)["terms"]
    return {tid: T.Term(tid, d["english"], d["abbr"], d["korean"], d["later"], tuple(d["forbidden"]), "", d["state"], "")
            for tid, d in data.items()}


def terms_changed(vault):
    new = T.snapshot(T.load(os.path.join(vault, "wiki", "Terminology.md")))
    p = os.path.join(vault, STATE)
    old = {}
    if os.path.isfile(p):
        with open(p, encoding="utf-8") as f:
            old = json.load(f)["terms"]
    return sorted(k for k in set(new) | set(old) if new.get(k) != old.get(k))


def plan_note(note, terms, old, rel, report):
    lines, seen = note.body.split("\n"), set()
    for ln, _ in N.korean_lines(note):
        idx = ln - note.offset - 1
        line, pos = lines[idx], 0
        while True:
            m = T.MARKER.search(line, pos)
            if not m:
                break
            tid, head, after = m.group(1), line[:m.start()], line[m.end():]
            term = terms.get(tid)
            if term is None:
                report["conflicts"].append(f"conflict {rel}:{ln} {tid}: not in Terminology")
                pos = m.end()
                continue
            if term.state == "용어 아님":
                line, pos = head + after, len(head)
                continue
            first = tid not in seen
            seen.add(tid)
            cands = sorted({d for t in (old.get(tid), term) if t for d in (T.display(t, True), T.display(t, False)) if d},
                           key=len, reverse=True)
            hit = next((c for c in cands if head.endswith(c)), None)
            if hit is None:
                report["conflicts"].append(f"conflict {rel}:{ln} {tid}: text before the marker matches no display form")
                pos = m.end()
                continue
            want = T.display(term, first)
            fin = T.final(want)
            if fin is None and _JOSA_AHEAD.match(after):
                report["particles"].append(f"check particle {rel}:{ln} {tid}: after '{want}'")
            new_head = head[:len(head) - len(hit)] + want
            line = new_head + m.group(0) + T.retarget(after, fin)
            pos = len(new_head) + len(m.group(0))
        lines[idx] = line
    body, fm = "\n".join(lines), dict(note.fm)
    tid = fm.get("term")
    if tid in terms and terms[tid].state == "확정":
        t = terms[tid]
        blines = body.split("\n")
        for i, l in enumerate(blines):
            if l.startswith("# "):
                blines[i] = f"# {t.korean} ({t.english})"
                break
        body = "\n".join(blines)
        prev = old.get(tid).korean if old.get(tid) else None
        aliases = [a for a in (fm.get("aliases") or []) if not (prev and a == prev and a != t.korean)]
        if t.korean not in aliases:
            aliases.append(t.korean)
        fm["aliases"] = aliases
    remaining = N.Note(note.path, fm, body, note.offset)
    pending = sorted({m.group(1) for _, l in N.korean_lines(remaining) for m in T.MARKER.finditer(l)
                      if m.group(1) in terms and terms[m.group(1)].state == "미정"})
    if "terms_pending" in fm or pending:
        fm["terms_pending"] = pending
    return fm, body


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--apply", action="store_true")
    a = ap.parse_args(argv)
    sys.stdout.reconfigure(encoding="utf-8")
    try:
        terms = T.load(os.path.join(VAULT, "wiki", "Terminology.md"))
    except (OSError, T.TermError) as exc:
        print(f"sync_terms: error: {exc}")
        return 1
    old, report, updated = load_state(VAULT), {"conflicts": [], "particles": []}, []
    for p in N.wiki_notes(VAULT) + N.wiki_notes(VAULT, "internal"):
        try:
            note = N.load(p)
        except (N.NoteError, UnicodeDecodeError):
            continue
        if note.fm.get("type") == "source":
            continue
        rel = N.relpath(p, VAULT)
        fm, body = plan_note(note, terms, old, rel, report)
        if fm != note.fm or body != note.body:
            updated.append(rel)
            if a.apply:
                N.write_note(p, fm, body)
    for r in updated:
        print(("updated " if a.apply else "would update ") + r)
    for line in report["conflicts"] + report["particles"]:
        print(line)
    if a.apply and not report["conflicts"]:
        N.write_text(os.path.join(VAULT, STATE),
                     json.dumps({"terms": T.snapshot(terms)}, ensure_ascii=False, indent=1, sort_keys=True))
    mode = "" if a.apply else " (dry-run; --apply to write)"
    print(f"sync_terms: {len(updated)} notes, {len(report['conflicts'])} conflicts, "
          f"{len(report['particles'])} particle checks{mode}")
    return 1 if report["conflicts"] else 0


if __name__ == "__main__":
    sys.exit(main())
```

`test_conflict_is_reported_left_alone_and_state_kept`: 요약의 첫 표지는 이전 표시(`가나(…)`)와 맞으므로 새 표시로 바뀌고, 해설의 `엘비이` 표지만 충돌로 남는다. 충돌이 있으므로 상태 파일은 그대로이고 `terms_changed`는 `["LBE"]`이다.

- [ ] **Step 5: 통과를 확인한다**

Run: `"$PY" -m pytest scripts/refclean/tests scripts/tests -q 2>&1 | tail -1`
Expected: `371 passed`.

- [ ] **Step 6: 실제 vault에서 상태 파일을 만든다**

```bash
cd /c/Obsidian/ripb && "$PY" scripts/sync_terms.py && "$PY" scripts/sync_terms.py --apply && cat meta/terms_state.json
```
Expected: 두 번 모두 `sync_terms: 0 notes, 0 conflicts, 0 particle checks`; 파일 내용 `{"terms": {}}`.

- [ ] **Step 7: 커밋**

```bash
git add scripts/notes.py scripts/lint_wiki.py scripts/sync_terms.py scripts/tests/test_sync_terms.py meta/terms_state.json && git commit -q -m "feat(terms): sync_terms.py propagates the terminology table to note markers

Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>"
```

### Task 13: 세션 시작 보고 (`session_start.py`)

**Files:**
- Create: `scripts/session_start.py`, `scripts/tests/test_session_start.py`

**Interfaces:**
- Consumes: `notes.*`; `sync_terms.terms_changed` (Task 12); `lint_wiki.Context`, `lint_file`, `lint_vault` (Task 9); `verify_quotes.Sources`, `verify_note` (Task 8)
- Produces: `session_start.changed_paths(repo) -> list[tuple[str, str]] | None`(git 저장소가 아니면 None); `session_start.report(vault) -> str`; `session_start.main(argv=None) -> 0`(항상 0; 부분 실패는 보고 줄이 된다). Task 15의 SessionStart hook이 호출한다.

보고 구성(설계 §7.1): 상태(`meta/status.md`의 현재 단계·다음 작업·미해결), log 최근 3건, 두 저장소의 `git status`, 용어표 변경 여부, `inbox/`·`inbox/internal/` 대기 건수와 소스 카드 진행, 공개 트리 검사 요약(lint·인용 검증), 커밋되지 않은 노트 변경(사용자가 Obsidian에서 고친 노트 포함)의 lint·인용 검증 결과. 보고는 Claude의 컨텍스트로만 들어가며 파일로 쓰지 않는다.

- [ ] **Step 1: 실패하는 테스트를 쓴다**

`scripts/tests/test_session_start.py`:
```python
import subprocess

import pytest

import session_start as SS


def git(vault, *a):
    subprocess.run(["git", "-C", str(vault), "-c", "user.name=t", "-c", "user.email=t@example.invalid", *a],
                   check=True, capture_output=True)


@pytest.fixture
def svault(mini_vault):
    (mini_vault / "meta" / "status.md").write_text(
        "---\nupdated: x\n---\n# 상태\n\n## 현재 단계\nPhase 3.\n\n## 다음 작업\n1. 시범.\n\n## 미해결\n- 없음\n",
        encoding="utf-8")
    (mini_vault / "log.md").write_text("# log\n\n## [2026-09-14] init | a\n- x\n\n## [2026-09-15] feat | b\n- y\n",
                                       encoding="utf-8")
    return mini_vault


def test_report_parts_without_git(svault):
    (svault / "inbox" / "new.pdf").write_bytes(b"%PDF")
    text = SS.report(str(svault))
    assert "### 다음 작업\n1. 시범." in text
    assert "## [2026-09-15] feat | b" in text
    assert "git #1: git 저장소 아님" in text
    assert "변경 2건: LBE, RAC" in text                      # no terms_state.json yet
    assert "inbox 대기: 1 (new.pdf)" in text and "DOC_A: ingest pending, 단위 0/0" in text
    assert "lint_wiki: 오류 0, 경고 0" in text and "verify_quotes: 오류 0" in text
    assert "## 커밋되지 않은 노트 변경\n없음" in text


def test_uncommitted_note_edits_are_checked(svault, make_note, good_note_body):
    git(svault, "init", "-q")
    git(svault, "add", "-A")
    git(svault, "commit", "-q", "-m", "base")
    make_note("Sample", good_note_body.replace("## 해설", "## 설명"))
    text = SS.report(str(svault))
    assert "git #1: 변경 1건" in text
    assert "- wiki/Sample.md: 오류 1" in text and "L06" in text


def test_failures_become_lines_and_exit_zero(svault, monkeypatch, capsys):
    (svault / "wiki" / "Terminology.md").write_text("broken\n", encoding="utf-8")
    monkeypatch.setattr(SS, "VAULT", str(svault))
    assert SS.main() == 0
    out = capsys.readouterr().out
    assert "용어표 오류" in out and "## 검사 (공개 트리)" in out
```
(`test_uncommitted_note_edits_are_checked`: `## 설명`으로 바꾼 노트는 L06 한 건만 낸다. `해설` 절이 없으므로 V5와 L13–L15 검사 대상도 없다.)

- [ ] **Step 2: 실패를 확인한다**

Run: `"$PY" -m pytest scripts/tests/test_session_start.py -q 2>&1 | tail -2`
Expected: `No module named 'session_start'`.

- [ ] **Step 3: `scripts/session_start.py`를 쓴다**

```python
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
```

- [ ] **Step 4: 통과를 확인한다**

Run: `"$PY" -m pytest scripts/refclean/tests scripts/tests -q 2>&1 | tail -1`
Expected: `374 passed`.

- [ ] **Step 5: 실제 vault에서 실행하고 시간을 잰다**

Run: `time "$PY" scripts/session_start.py`
Expected: 일곱 절이 모두 있고, `용어표`는 `변경 없음`, `검사`는 `오류 0`, `커밋되지 않은 노트 변경`은 `없음`. 실행 시간(real)을 기록한다. 10 s를 넘으면 Task 15의 hook `timeout`을 그 두 배로 잡는다.

- [ ] **Step 6: 커밋**

```bash
git add scripts/session_start.py scripts/tests/test_session_start.py && git commit -q -m "feat(session): session start report for the SessionStart hook

Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>"
```

### Task 14: 표본 재검증 도구 (`audit_sample.py`)

설계 §8.3은 "2026-09-11 감사의 서브에이전트 프롬프트를 표준화"하라고 한다. 그 프롬프트는 저장된 파일이 없고, 2026-09-14에 데스크톱 세션 기록 검색으로도 찾지 못했다. 아래 프롬프트는 설계 §1(검증 통과 / 경미 / 사실 오류의 3구분, 노트 단위 오류율)과 §7.4를 기준으로 새로 정의한 것이며, 오류율은 2026-09-11 수치(노트의 16 %)와 같은 노트 단위로 센다.

**Files:**
- Create: `scripts/audit_sample.py`, `scripts/tests/test_audit_sample.py`

**Interfaces:**
- Consumes: `notes.*`, `citations.split_trailing`
- Produces: `audit_sample.AuditError`; `audit_sample.population(vault) -> list[str]`(`status: checked`이고 type이 source·map이 아닌 공개 노트); `audit_sample.prompt_for(vault, path, cards) -> str`; `audit_sample.sample(vault, n, seed, out) -> dict`(`out/sample.json`과 `out/<Note>.prompt.md`); `audit_sample.summarize(out) -> str`(`meta/metrics.md` 표의 한 행); CLI `sample [--n 10] [--seed INT] [--out DIR]`, `summarize DIR`. Task 17의 `wiki-audit` skill이 쓴다.
- 판정값: 원문 사실 `일치 / 경미 / 불일치 / 원문 없음 / 판정 불가`; 해설·요약 `근거 있음 / 과잉 일반화 / 원문 사실에 없음 / 원문과 모순 / 판정 불가`. 오류 노트 = `불일치`·`원문 없음`·`원문 사실에 없음`·`원문과 모순`이 하나 이상인 노트.
- `meta/metrics.md` 표 머리(파일은 첫 측정 때 `wiki-audit`가 만든다): `| 날짜 | seed | 표본/모집단 | 오류 노트 | 노트 오류율 | 불일치·원문 없음 항목/전체 항목 | 경미 |`.

- [ ] **Step 1: 실패하는 테스트를 쓴다**

`scripts/tests/test_audit_sample.py`:
```python
import json

import pytest

import audit_sample as AS


def checked(make_note, body, n):
    return [make_note(f"Checked_{i}", body, status="checked", verified="2026-09-20") for i in range(n)]


def test_population_and_deterministic_sample(mini_vault, make_note, good_note_body, tmp_path):
    checked(make_note, good_note_body, 5)
    make_note("Draft", good_note_body)
    assert len(AS.population(str(mini_vault))) == 5
    a = AS.sample(str(mini_vault), 3, 7, str(tmp_path / "a"))
    b = AS.sample(str(mini_vault), 3, 7, str(tmp_path / "b"))
    assert a["notes"] == b["notes"] and len(a["notes"]) == 3 and a["population"] == 5
    assert len(AS.sample(str(mini_vault), 10, 7, str(tmp_path / "c"))["notes"]) == 5


def test_prompt_lists_sources_and_citations(mini_vault, make_note, good_note_body, tmp_path):
    checked(make_note, good_note_body, 1)
    AS.sample(str(mini_vault), 1, 1, str(tmp_path))
    text = (tmp_path / "Checked_0.prompt.md").read_text(encoding="utf-8")
    assert "`wiki/Checked_0.md`" in text and "정제본 `references/DOC_A_T.md`" in text
    assert "[DOC_A §3.2 p.3]" in text and "[DOC_A Table x p.2]" in text
    assert "파일을 수정하지 않는다" in text


def _result(path, facts, commentary):
    path.write_text(json.dumps({"facts": [{"line": 1, "verdict": v} for v in facts],
                                "commentary": [{"sentence": "s", "verdict": v} for v in commentary]},
                               ensure_ascii=False), encoding="utf-8")


def test_summarize_counts(mini_vault, make_note, good_note_body, tmp_path):
    checked(make_note, good_note_body, 2)
    meta = AS.sample(str(mini_vault), 2, 3, str(tmp_path))
    names = [n.split("/")[-1][:-3] for n in meta["notes"]]
    _result(tmp_path / f"{names[0]}.result.json", ["일치", "경미"], ["근거 있음"])
    with pytest.raises(AS.AuditError, match="missing"):
        AS.summarize(str(tmp_path))
    _result(tmp_path / f"{names[1]}.result.json", ["불일치"], ["원문과 모순"])
    assert AS.summarize(str(tmp_path)).endswith("| 3 | 2/2 | 1 | 50 % | 1/3 | 1 |")


def test_unknown_verdict_is_refused(mini_vault, make_note, good_note_body, tmp_path):
    checked(make_note, good_note_body, 1)
    AS.sample(str(mini_vault), 1, 1, str(tmp_path))
    _result(tmp_path / "Checked_0.result.json", ["맞음"], [])
    with pytest.raises(AS.AuditError, match="verdict"):
        AS.summarize(str(tmp_path))


def test_cli(mini_vault, make_note, good_note_body, tmp_path, monkeypatch):
    monkeypatch.setattr(AS, "VAULT", str(mini_vault))
    checked(make_note, good_note_body, 1)
    assert AS.main(["sample", "--n", "1", "--seed", "1", "--out", str(tmp_path)]) == 0
    assert AS.main(["summarize", str(tmp_path)]) == 1
```

- [ ] **Step 2: 실패를 확인한다**

Run: `"$PY" -m pytest scripts/tests/test_audit_sample.py -q 2>&1 | tail -2`
Expected: `No module named 'audit_sample'`.

- [ ] **Step 3: `scripts/audit_sample.py`를 쓴다**

```python
"""audit_sample.py — sample re-verification of checked notes (spec §7.4; skill wiki-audit).

Usage:
  python scripts/audit_sample.py sample [--n 10] [--seed INT] [--out DIR]
  python scripts/audit_sample.py summarize DIR
`sample` writes DIR/sample.json and DIR/<Note>.prompt.md. The main session gives each prompt to a read-only subagent
and saves its JSON answer as DIR/<Note>.result.json; `summarize` prints the meta/metrics.md row.
The seed defaults to the date (YYYYMMDD) so a sample can be redrawn.
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
        if fm.get("status") == "checked" and fm.get("type") not in EXCLUDED:
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
    return f"| {meta['date']} | {meta['seed']} | {n}/{meta['population']} | {bad_notes} | {rate:.0f} % | {bad_facts}/{facts} | {minor} |"


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
```

- [ ] **Step 4: 통과를 확인한다**

Run: `"$PY" -m pytest scripts/refclean/tests scripts/tests -q 2>&1 | tail -1`
Expected: `379 passed`.

- [ ] **Step 5: 커밋**

```bash
git add scripts/audit_sample.py scripts/tests/test_audit_sample.py && git commit -q -m "feat(audit): sample checked notes, write comparison prompts, summarize verdicts

Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>"
```

### Task 15: hook 3종 (PostToolUse, SessionStart, pre-commit 확장)  **확인 지점**

설정 형식의 근거(2026-09-14 조사, https://code.claude.com/docs/en/hooks-guide.md, https://code.claude.com/docs/en/hooks.md): `.claude/settings.json`의 `hooks.<Event>[].matcher`와 `hooks[].{type: "command", command, timeout(초)}`; PostToolUse 입력 JSON의 `tool_input.file_path`는 절대 경로이고 `cwd`가 함께 온다; SessionStart의 일반 stdout은 Claude 컨텍스트에 추가된다; Windows에서는 Git Bash가 설치되어 있으면 Git Bash가 명령을 실행하며 `${CLAUDE_PROJECT_DIR}`를 쓴다. PostToolUse의 결과를 Claude에게 되돌리는 방식은 조사에서 확정되지 않았다. 따라서 1차 방식은 stdout JSON `{"decision": "block", "reason": …}`(도구는 이미 실행되었고 `reason`이 Claude에게 전달되는 형식)이고, Step 7에서 실제 세션으로 확인하며, 전달되지 않으면 종료 코드 2 + stderr로 바꾼다.

hook이 저장소 설정을 바꾸고 이후 모든 세션에서 자동 실행되므로 `.claude/settings.json`을 쓰기 전에 사용자 확인을 받는다.

**Files:**
- Create: `scripts/hook_post_edit.py`, `scripts/tests/test_hook_post_edit.py`, `.claude/settings.json`
- Modify: `.githooks/pre-commit`, `internal/.githooks/pre-commit` (git #2)

**Interfaces:**
- Consumes: `lint_wiki.Context`, `lint_wiki.lint_file` (Task 9); `verify_quotes.Sources`, `verify_quotes.verify_note` (Task 8)
- Produces: `hook_post_edit.target(payload: dict, vault: str) -> str | None`(검사 대상 노트의 절대 경로 또는 None); `hook_post_edit.respond(findings) -> str`(stdout에 쓸 문자열, 없으면 `""`); `hook_post_edit.main(stdin=None) -> 0`.

- [ ] **Step 1: 실패하는 테스트를 쓴다**

`scripts/tests/test_hook_post_edit.py`:
```python
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


def test_bad_stdin_is_ignored(monkeypatch, capsys, mini_vault):
    monkeypatch.setattr(H, "VAULT", str(mini_vault))
    assert H.main(io.StringIO("not json")) == 0
    assert capsys.readouterr().out == ""
```

- [ ] **Step 2: 실패를 확인한다**

Run: `"$PY" -m pytest scripts/tests/test_hook_post_edit.py -q 2>&1 | tail -2`
Expected: `No module named 'hook_post_edit'`.

- [ ] **Step 3: `scripts/hook_post_edit.py`를 쓴다**

```python
"""hook_post_edit.py — Claude PostToolUse hook for Edit/Write/MultiEdit (spec §8.2).

Reads the hook JSON on stdin. For wiki/*.md and internal/wiki/*.md it runs the per-file lint and the quote check.
Errors: stdout JSON {"decision": "block", "reason": …} so Claude sees them (the edit itself already happened).
Warnings only: stdout JSON with hookSpecificOutput.additionalContext. Clean or not a note: no output.
Always exits 0; an internal failure is written to stderr only.
"""
import json
import os
import re
import sys

import notes as N

SCRIPTS = os.path.dirname(os.path.abspath(__file__))
VAULT = os.path.dirname(SCRIPTS)
NOTE = re.compile(r"^(internal/)?wiki/[^/]+\.md$")
MAX = 30


def target(payload, vault):
    path = (payload.get("tool_input") or {}).get("file_path")
    if not path:
        return None
    if not os.path.isabs(path):
        path = os.path.join(payload.get("cwd") or vault, path)
    path = os.path.normpath(path)
    rel = os.path.relpath(path, vault).replace(os.sep, "/")
    return path if NOTE.match(rel) else None


def respond(findings):
    if not findings:
        return ""
    lines = "\n".join(str(f) for f in findings[:MAX])
    more = f"\n… {len(findings) - MAX} more" if len(findings) > MAX else ""
    if any(f.level == "error" for f in findings):
        return json.dumps({"decision": "block",
                           "reason": "lint_wiki/verify_quotes found problems in the edited note; fix them:\n" + lines + more},
                          ensure_ascii=False)
    return json.dumps({"hookSpecificOutput": {"hookEventName": "PostToolUse",
                                              "additionalContext": "lint_wiki warnings:\n" + lines + more}},
                      ensure_ascii=False)


def main(stdin=None):
    sys.stdout.reconfigure(encoding="utf-8")
    try:
        payload = json.load(stdin or sys.stdin)
        path = target(payload, VAULT)
        if not path or not os.path.isfile(path):
            return 0
        import lint_wiki as LW
        import verify_quotes as VQ
        ctx = LW.Context(VAULT)
        findings = LW.lint_file(ctx, path)
        try:
            findings += VQ.verify_note(VAULT, path, VQ.Sources(VAULT, ctx.cards))
        except (N.NoteError, UnicodeDecodeError):
            pass                                  # L02 already reports it
        out = respond(findings)
        if out:
            print(out)
    except Exception as exc:
        print(f"hook_post_edit: {type(exc).__name__}: {exc}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
```

- [ ] **Step 4: 통과와 시간 확인**

Run: `"$PY" -m pytest scripts/refclean/tests scripts/tests -q 2>&1 | tail -1`
Expected: `384 passed`.

```bash
cd /c/Obsidian/ripb && time (printf '{"cwd":"C:/Obsidian/ripb","tool_input":{"file_path":"C:/Obsidian/ripb/wiki/RG_1.232.md"}}' | "$PY" scripts/hook_post_edit.py)
```
Expected: 출력 없음, real 1 s 안팎(설계 §8.2 목표). 2 s를 넘으면 기록하고 `Context`의 `assets` 수집을 링크 검사 시점으로 늦추는 개선을 status 미해결에 적는다(이 Task에서는 고치지 않는다).

- [ ] **Step 5: 사용자 확인 후 `.claude/settings.json`을 쓴다**

사용자에게 아래 파일 내용과 효과("이후 이 저장소의 모든 Claude 세션에서 시작 보고가 자동 실행되고, wiki 노트 편집마다 검사 결과가 Claude에게 전달됨")를 보이고 승인을 받는다.

```json
{
  "hooks": {
    "SessionStart": [
      {
        "matcher": "startup|resume|clear",
        "hooks": [
          {
            "type": "command",
            "command": "\"/c/Code/Python/pykaeri/.venv12/Scripts/python.exe\" \"${CLAUDE_PROJECT_DIR}/scripts/session_start.py\"",
            "timeout": 60
          }
        ]
      }
    ],
    "PostToolUse": [
      {
        "matcher": "Edit|Write|MultiEdit",
        "hooks": [
          {
            "type": "command",
            "command": "\"/c/Code/Python/pykaeri/.venv12/Scripts/python.exe\" \"${CLAUDE_PROJECT_DIR}/scripts/hook_post_edit.py\"",
            "timeout": 30
          }
        ]
      }
    ]
  }
}
```
SessionStart `timeout`은 Task 13 Step 5에서 잰 시간이 30 s를 넘으면 그 두 배로 올린다.

- [ ] **Step 6: pre-commit을 확장한다**

`.githooks/pre-commit`에서 leak_guard 블록 뒤, 마지막 `exit 0` 앞에 넣는다.
```bash
# 전체 검사 (spec §8.2). 작업 트리를 검사하므로 일부만 stage한 경우에도 전체 기준으로 판정된다.
for check in "lint_wiki.py --all" "verify_quotes.py --all" "build_index.py --check"; do
  if ! out=$("$PY" "$ROOT/scripts/"$check 2>&1); then
    printf '%s\n' "$out"
    echo "pre-commit: refused ($check)"
    exit 1
  fi
done
```

내부 저장소: 먼저 현재 결과를 본다.
```bash
cd /c/Obsidian/ripb && "$PY" scripts/lint_wiki.py --all --root internal | tail -1 && "$PY" scripts/verify_quotes.py --all --root internal | tail -1
```
오류가 0이면 `"$PY" scripts/build_index.py --root internal`로 `internal/index.md`를 만들고 `internal/.githooks/pre-commit`의 `exit 0` 앞에 넣는다.
```bash
PY="${RIPB_PY:-/c/Code/Python/pykaeri/.venv12/Scripts/python.exe}"
SCRIPTS="$(git rev-parse --show-toplevel)/../scripts"
for check in "lint_wiki.py --all --root internal" "verify_quotes.py --all --root internal" "build_index.py --check --root internal"; do
  if ! out=$("$PY" "$SCRIPTS/"$check 2>&1); then
    printf '%s\n' "$out"
    echo "pre-commit: refused ($check)"
    exit 1
  fi
done
```
오류가 0이 아니면(예: 내부 정제본에 소스 카드가 없음, L34) 내부 관문 연결을 멈추고 오류 개수만 사용자에게 보고하여 "지금 연결(먼저 오류 해소) / 내부 인제스트 때 연결" 중 하나를 받는다. 오류 내용은 `internal/status.md`에만 적는다.

- [ ] **Step 7: 실제 세션에서 hook을 확인한다**

1. 이 세션을 다시 시작한다(데스크톱 앱의 새 세션 또는 `claude` 재실행). 첫 컨텍스트에 `# ripb 세션 시작 보고`가 들어왔는지 확인한다.
2. 새 세션에서 Claude가 `wiki/Hook_Probe.md`를 `templates/note.md` 그대로(자리표시자 포함) Write한다. 기대: Claude가 L07·V1 등 검사 결과를 hook 응답으로 받는다.
3. 받지 못하면 `respond`의 오류 분기를 "stderr에 같은 문자열을 쓰고 종료 코드 2"로 바꾸고(`main`이 `2`를 반환하도록), 테스트 `test_errors_are_returned_to_claude`를 stderr·종료 코드 기준으로 고친 뒤 2를 반복한다. 어느 방식이 동작했는지 커밋 메시지에 적는다.
4. `wiki/Hook_Probe.md`를 지운다(아직 커밋되지 않은 탐침 파일; 삭제 전 `git status --short wiki/`로 이 파일만 새 파일인지 확인).

- [ ] **Step 8: pre-commit 확장을 확인한다**

```bash
cd /c/Obsidian/ripb && printf -- '---\ntype: concept\n---\n# x\n' > wiki/Gate_Probe.md && git add wiki/Gate_Probe.md && git commit -q -m "test: gate"; echo "exit $?"; git reset -q wiki/Gate_Probe.md && rm wiki/Gate_Probe.md
```
Expected: `lint_wiki` 출력과 `pre-commit: refused (lint_wiki.py --all)`, `exit 1`.

- [ ] **Step 9: 커밋 (두 저장소)**

```bash
git add scripts/hook_post_edit.py scripts/tests/test_hook_post_edit.py .claude/settings.json .githooks/pre-commit && git commit -q -m "feat(hooks): SessionStart report, PostToolUse note checks, full pre-commit gate

Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>"
```
내부 관문을 연결한 경우에만:
```bash
git -C internal add .githooks/pre-commit index.md && git -C internal commit -q -m "feat(hooks): internal lint, quote and index gate

Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>"
```

### Task 16: Obsidian Shell Commands와 Bases 보기  **확인 지점**

Shell Commands 플러그인의 유일한 명령이 Gemini CLI를 실행한다(Phase 1 이관 항목). 이를 vault 도구 명령 4개로 바꾼다. 사용자의 Obsidian 설정을 바꾸므로 확인을 받고, 플러그인이 설정을 덮어쓰지 않도록 Obsidian을 닫은 상태에서 쓴다.

Bases 문법의 근거(2026-09-14 조사, https://obsidian.md/help/bases/syntax, https://obsidian.md/help/bases/functions, https://obsidian.md/help/bases/views): 최상위 `filters`(`and`/`or`/`not` 목록)와 `views`; 뷰 키 `type: table`, `name`, `filters`, `groupBy: {property, direction}`, `order`. `direction`은 문서 예시의 `DESC`만 쓴다. `sort` 키는 문서에 없어 쓰지 않는다. 목록 속성이 비었는지는 `isEmpty()`로 판정하고, 속성이 없는 노트의 동작이 문서에 없으므로 `file.hasProperty`를 함께 건다. `!`로 시작하는 식은 YAML 태그로 읽히므로 따옴표로 감싼다.

**Files:**
- Modify: `.obsidian/plugins/obsidian-shellcommands/data.json`
- Create: `meta/views/wiki_by_type.base`, `meta/views/wiki_by_status.base`, `meta/views/wiki_disputed.base`, `meta/views/wiki_terms_pending.base`

- [ ] **Step 1: 사용자 확인**

다음을 보이고 승인을 받는다: "Gemini CLI 실행 명령(`Launch Gemini CLI for this vault`)을 지우고 `ripb: 용어 동기화 (dry-run)`, `ripb: 용어 동기화 적용`(실행 전 확인), `ripb: lint 전체`, `ripb: index 재생성` 4개를 등록합니다. 작업 동안 Obsidian을 닫아 주십시오." Obsidian이 닫혔다는 답을 받은 뒤 진행한다.

- [ ] **Step 2: `data.json`의 `shell_commands`를 바꾼다 (scratchpad 스크립트)**

`$SCRATCH/shellcmds.py`:
```python
import json

PATH = "C:/Obsidian/ripb/.obsidian/plugins/obsidian-shellcommands/data.json"
PY = r"C:\Code\Python\pykaeri\.venv12\Scripts\python.exe"
data = json.load(open(PATH, encoding="utf-8"))
template = data["shell_commands"][0]
assert template["alias"] == "Launch Gemini CLI for this vault", template["alias"]


def entry(cid, alias, args, confirm=False):
    e = json.loads(json.dumps(template))
    e.update({"id": cid, "alias": alias, "icon": "lucide-terminal-square", "confirm_execution": confirm,
              "platform_specific_commands": {"default": f"{PY} {{{{vault_path}}}}\\scripts\\{args}"},
              "ignore_error_codes": [1]})
    e["output_handlers"] = {"stdout": {"handler": "modal", "convert_ansi_code": True},
                            "stderr": {"handler": "modal", "convert_ansi_code": True}}
    return e


data["shell_commands"] = [
    entry("ripbterms0", "ripb: 용어 동기화 (dry-run)", "sync_terms.py"),
    entry("ripbterms1", "ripb: 용어 동기화 적용", "sync_terms.py --apply", confirm=True),
    entry("ripblint00", "ripb: lint 전체", "lint_wiki.py --all"),
    entry("ripbindex0", "ripb: index 재생성", "build_index.py"),
]
open(PATH, "w", encoding="utf-8", newline="\n").write(json.dumps(data, ensure_ascii=False, indent=2))
print([c["alias"] for c in data["shell_commands"]])
```
Run: `"$PY" "$SCRATCH/shellcmds.py"`
Expected: 네 alias 목록. `ignore_error_codes: [1]`은 검사 실패(종료 코드 1)를 플러그인 오류 알림 대신 결과 창으로 보이게 한다. 명령은 경로에 공백이 없어 따옴표 없이 cmd·PowerShell 양쪽에서 실행된다.

- [ ] **Step 3: Bases 파일 4개를 쓴다**

`meta/views/wiki_by_type.base`:
```yaml
filters:
  and:
    - file.inFolder("wiki")
views:
  - type: table
    name: type별
    groupBy:
      property: note.type
      direction: DESC
    order:
      - file.name
      - note.type
      - note.status
      - note.sources
```

`meta/views/wiki_by_status.base`:
```yaml
filters:
  and:
    - file.inFolder("wiki")
views:
  - type: table
    name: status별
    groupBy:
      property: note.status
      direction: DESC
    order:
      - file.name
      - note.type
      - note.status
      - note.verified
```

`meta/views/wiki_disputed.base`:
```yaml
filters:
  and:
    - file.inFolder("wiki")
    - 'status == "disputed"'
views:
  - type: table
    name: disputed
    order:
      - file.name
      - note.type
      - note.sources
```

`meta/views/wiki_terms_pending.base`:
```yaml
filters:
  and:
    - file.inFolder("wiki")
    - file.hasProperty("terms_pending")
    - '!terms_pending.isEmpty()'
views:
  - type: table
    name: 미정 용어를 쓰는 노트
    order:
      - file.name
      - note.type
      - note.terms_pending
```

- [ ] **Step 4: 사용자와 함께 Obsidian에서 확인한다**

사용자에게 Obsidian을 다시 열고 다음을 확인해 달라고 요청한다: (1) 명령 팔레트의 `Execute: ripb: lint 전체`가 결과 창에 `lint_wiki: 12 notes, 0 errors, 0 warnings`를 한국어가 깨지지 않게 보이는지, (2) `meta/views/wiki_by_type.base`가 원문(source) 11행과 지도(map) 1행으로 묶여 보이는지, (3) 나머지 세 보기가 오류 없이 열리는지(disputed·미정 용어 보기는 현재 0행). 한국어가 깨지면 증상(깨진 출력 일부)과 플러그인 설정의 기본 셸을 기록하고, 대응 방식은 사용자와 정한다(스크립트는 이미 stdout을 UTF-8로 쓴다). 보기에서 오류가 나면 오류 문구를 받아 해당 `.base`만 고친다.

- [ ] **Step 5: 커밋**

```bash
cd /c/Obsidian/ripb && git add .obsidian/plugins/obsidian-shellcommands/data.json meta/views && git commit -q -m "chore(obsidian): vault tool commands replace the Gemini launcher; four Bases views

Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>"
```

### Task 17: skill 5종 (`.claude/skills/`)

형식의 근거(2026-09-14 조사, https://code.claude.com/docs/en/skills.md): 위치 `.claude/skills/<name>/SKILL.md`, frontmatter의 필수 필드는 `description`(언제 쓰는지 포함). `name`은 디렉터리 이름과 같게 적는다. 절차만 담고 규칙은 CLAUDE.md를 가리킨다(설계 §8.4). skill 문서를 쓸 때는 `superpowers:writing-skills`의 지침을 따른다.

**Files:**
- Create: `.claude/skills/wiki-ingest/SKILL.md`, `.claude/skills/wiki-terms/SKILL.md`, `.claude/skills/wiki-query/SKILL.md`, `.claude/skills/wiki-lint/SKILL.md`, `.claude/skills/wiki-audit/SKILL.md`

**Interfaces:**
- Consumes: Task 2–16의 모든 CLI(`source.py`, `lint_wiki.py`, `verify_quotes.py`, `sync_terms.py`, `build_index.py`, `append_log.py`, `audit_sample.py`), `templates/*.md`

- [ ] **Step 1: `wiki-ingest`**

````markdown
---
name: wiki-ingest
description: ripb vault에 원문 1단위(절 묶음 또는 장)를 인제스트할 때 쓴다. "ingest", "인제스트", 세션 시작 보고의 inbox 대기·진행 중 원문, 새 원문 등록 요청이 해당한다.
---

# wiki-ingest

규칙은 `CLAUDE.md`, 근거는 `meta/design/2026-09-14-vault-rebuild-design.md` §4.2, §5, §6.3, §7.2. 명령은 모두 `C:\Code\Python\pykaeri\.venv12\Scripts\python.exe`로 vault 루트에서 실행한다.

## 0. 준비
1. `scripts/source.py status`에서 `in_progress` 원문을 먼저 잇는다. 없으면 설계 부록 A 순서의 첫 `pending`.
2. inbox에 새 파일이 있으면 등록 키·제목을 사용자에게 확인한 뒤: `source.py register <pdf> --key KEY --title "…"`(내부 자료는 `--root internal`) → `convert_references.py` → `scripts/refclean/profiles/__init__.py`의 `DOCS` 등록과 프로파일 → `clean_references.py --only KEY --verify`와 pytest → `source.py sync KEY`. PDF가 아닌 형식은 변환 방식을 사용자에게 묻는다.
3. 이번 단위를 소스 카드 `units`에 `{unit: "<범위>", status: in_progress}`로 넣고 `ingest: in_progress`로 둔다.

## 1. 접점 ① — 계획과 용어 질문 (한 메시지)
- 절 범위, 만들거나 고칠 노트(파일명, type, 한 줄 내용), 기존 노트와의 관계.
- 용어 후보: 원문 약어표·용어집 항목과 해설에 쓸 전문 용어 중 `wiki/Terminology.md`에 없는 것. 용어표에 `미정` 행을 넣고(한국어 칸은 비움) `templates/term_question.md` 형식으로 묻는다. 번역 후보를 싣지 않는다.
- 답을 받은 뒤 쓴다. 용어 답은 `wiki-terms`로 반영한다.

## 2. 작성 (`templates/note.md`)
- 순서: 원문 사실 → 해설 → 링크.
- 원문 사실: 정제본 문장을 그대로 복사해 곧은 따옴표 `"…"`로 감싼다(원문 안의 “ ”는 그대로). 긴 문단은 `...`로 줄이되 조각마다 3단어 이상. 표는 `| 항목 | 값 | 출처 |`이고 모든 행에 인용. 인용은 `[KEY 위치 p.N]`, N은 쪽 표지의 첫 번호.
- 해설: 원문 사실 항목만 근거로 쓰고, 수치는 원문 사실에 있는 것만. 전문 용어에는 `%%t:ID%%` 표지를 붙이고 표기는 용어표 규칙대로(미정이면 English).
- 링크는 존재하는 노트만. 없는 주제는 변경 요약의 "누락 주제"에 적는다.
- 원문끼리 모순되면 둘 다 인용하고 `status: disputed`.
- 큰 장은 추출·대조를 읽기 전용 서브에이전트에 나누고, 노트는 이 세션이 쓴다.

## 3. 검사
- 편집마다 PostToolUse hook이 검사 결과를 돌려준다. 오류는 바로 고친다.
- 단위 끝: `lint_wiki.py --all`, `verify_quotes.py --all`, `sync_terms.py`(충돌 0 확인, 필요하면 `--apply`), `build_index.py`. 해소하지 못한 항목은 변경 요약에 적는다. 원문의 오기는 고치지 않는다.

## 4. 접점 ② — 변경 요약 (`templates/change_summary.md`)
직접 볼 노트 2–3개를 이유와 함께 고른다. 반려되면 고친 뒤 이 단계부터 다시 한다.

## 5. 승인 뒤 한 번에
1. 이번 단위의 새·고친 노트: `status: checked`, `verified: <오늘>`.
2. 소스 카드의 해당 unit `status: complete`; 마지막 단위면 `source.py finish KEY`.
3. `append_log.py --type ingest --title "<KEY> <범위>" --item "새 노트 n, 고친 노트 n" --item "검사: …" --item "미정 용어 n"`.
4. `build_index.py`; `meta/status.md`의 다음 작업·미해결(disputed, 미정 용어, 누락 주제) 갱신.
5. 바뀐 파일만 `git add` → `git commit`(pre-commit 관문 통과). push는 사용자가 요청할 때만.
6. 원문 1건을 마치면 `wiki-lint`, 원문 2건마다 `wiki-audit`를 제안한다.

## 내부 자료
`internal/` 트리와 `--root internal`을 쓰고, 기록은 `internal/log.md`·`internal/status.md`에만 한다. 공개 파일과 커밋 메시지에 내부 문서명을 쓰지 않는다.
````

- [ ] **Step 2: `wiki-terms`**

````markdown
---
name: wiki-terms
description: 사용자가 용어 질문에 답했을 때, "용어 반영"을 요청했을 때, 세션 시작 보고가 용어표 변경을 알릴 때 쓴다. 용어표 기록, sync_terms.py 전파, 승인과 커밋.
---

# wiki-terms

규칙: `CLAUDE.md` §5, 설계 §6. 한국어 표기를 추측하거나 제안하지 않는다.

1. 답을 `wiki/Terminology.md`에 기록한다. 한국어 표기 → `한국어` 칸에 사용자가 준 문자열 그대로, `상태: 확정`. "영어 유지" → `상태: 영어 유지`. "용어 아님" → `상태: 용어 아님`. 약어가 있는 용어의 `이후 표기`(약어/한국어)를 사용자가 정하지 않았으면 묻는다.
2. `lint_wiki.py wiki/Terminology.md`로 L20이 없는지 확인한다.
3. `sync_terms.py`(dry-run)로 갱신될 노트, `conflict`, `check particle`을 확인한다.
4. `conflict`(표지 앞 표기를 손으로 고친 곳)는 해당 줄을 보여 주고 어느 표기를 따를지 묻는다. `check particle`(영어 표기 뒤 조사)은 목록으로 보이고 사용자의 답대로 고친다.
5. 요약(바뀐 용어, 갱신 노트, 충돌·조사 처리) → 승인 → `sync_terms.py --apply` → `lint_wiki.py --all` → `build_index.py --check` → `append_log.py --type terms --title "용어 반영" --item "…"` → 커밋.
````

- [ ] **Step 3: `wiki-query`**

````markdown
---
name: wiki-query
description: ripb vault가 다루는 내용(TI-RIPB, NEI 18-04, RG 1.232·1.233, Natrium Kemmerer Unit 1 PSAR, ACRS 자료)에 관한 질문에 답할 때 쓴다.
---

# wiki-query

1. `index.md` → 관련 노트(원문 사실 절과 인용) → 필요하면 정제본 `references/<stem>.md`의 해당 쪽 순으로 확인한다.
2. 답에는 노트 링크 `[[Note]]`와 원문 위치 `[KEY 위치 p.N]`을 붙인다. vault에 없으면 "vault에 없음"이라고 쓴다. 원문에는 있으나 노트에 없으면 그 사실과 위치를 밝힌다. 배경지식으로 빈칸을 채우지 않는다.
3. 질의 중 발견한 노트 오류는 바로 보고하고, 수정은 별도 승인을 받는다.
4. 반복 재사용, 인계 필요, 결정 근거 추적, 실패 방법 기록, 팀 공통 규칙 중 하나 이상에 해당하는 답은 `synthesis` 노트로 저장을 제안한다. 저장은 `wiki-ingest`의 검사·변경 요약·승인 절차를 따른다.
5. 내부 자료에 근거한 답은 공개 파일에 기록하지 않는다.
````

- [ ] **Step 4: `wiki-lint`**

````markdown
---
name: wiki-lint
description: 원문 1건의 인제스트가 끝났을 때, 또는 사용자가 "lint"나 "점검"을 요청할 때 쓴다. 기계 검사 뒤 노트 간 의미 점검을 하고 meta/lint/YYYY-MM-DD.md 보고서를 쓴다.
---

# wiki-lint

1. 기계 검사: `lint_wiki.py --all`, `verify_quotes.py --all`, `build_index.py --check`, `sync_terms.py`. 결과를 요약한다.
2. 의미 점검 범위: 완료한 원문의 노트, 그 노트와 링크로 이어진 노트, `sources`가 겹치는 노트.
3. 점검 항목과 근거: 노트 간 모순(같은 대상의 다른 수치·분류), 중복(같은 개념의 두 노트, 겹치는 alias), 누락 주제(원문 사실·해설이 언급하나 노트가 없는 주제), 낡은 서술(새 원문이 대체한 사실, `deprecated` 후보). 판정마다 해당 노트들의 원문 사실 항목을 인용과 함께 근거로 적는다.
4. 보고서 `meta/lint/YYYY-MM-DD.md`: `# 의미 점검 YYYY-MM-DD (<KEY>)` 아래 `## 기계 검사`, `## 모순`, `## 중복`, `## 누락 주제`, `## 낡은 서술`, `## 제안 조치`. 해당 없는 절은 "없음". 내부 자료 점검은 `internal/status.md`에만 적는다.
5. 사용자에게 요약을 보이고, 조치는 항목별로 승인을 받는다. 보고서는 승인 뒤 `append_log.py --type lint`와 함께 커밋한다.
````

- [ ] **Step 5: `wiki-audit`**

````markdown
---
name: wiki-audit
description: 원문 2건의 인제스트가 끝날 때마다, 또는 사용자가 "audit"나 "표본 재검증"을 요청할 때 쓴다. checked 노트 10개를 무작위로 골라 읽기 전용 서브에이전트가 원문과 대조하고 오류율을 meta/metrics.md에 기록한다.
---

# wiki-audit

1. `audit_sample.py sample --n 10 --out <scratchpad>/audit_<YYYY-MM-DD>`. 출력의 seed와 모집단 수를 기록한다.
2. 각 `<Note>.prompt.md`를 읽기 전용 서브에이전트 하나에 준다(파일 편집 금지를 지시에 명시, 병렬 실행). 답 JSON을 이 세션이 `<Note>.result.json`으로 저장한다. JSON이 아니면 한 번 다시 요청한다. 세션 한도로 멈춘 서브에이전트는 SendMessage로 재개한다.
3. `audit_sample.py summarize <dir>`로 표 행을 얻는다.
4. `meta/metrics.md`에 행을 덧붙인다. 파일이 없으면 `# 표본 재검증 지표`와 머리 `| 날짜 | seed | 표본/모집단 | 오류 노트 | 노트 오류율 | 불일치·원문 없음 항목/전체 항목 | 경미 |`로 만든다. 첫 측정 행 아래에 목표 오류율을 사용자와 정해 적는다(설계 §10).
5. 오류 판정(불일치, 원문 없음, 원문 사실에 없음, 원문과 모순)은 이 세션이 원문으로 다시 확인한다. 확인된 오류마다 노트 수정안과 원인(규칙·도구·절차)을 보고하고, 승인 뒤 노트와 원인을 함께 고친다(설계 §7.4).
6. 승인 뒤 `append_log.py --type audit`과 함께 커밋한다.
````

- [ ] **Step 6: frontmatter와 관문 확인**

```bash
cd /c/Obsidian/ripb && "$PY" - <<'EOF'
import sys; sys.path.insert(0, "scripts")
import glob, notes
for p in sorted(glob.glob(".claude/skills/*/SKILL.md")):
    fm, body = notes.read_note(p)
    name = p.replace("\\", "/").split("/")[-2]
    assert fm.get("name") == name and fm.get("description"), p
    print(name, len(body.splitlines()))
EOF
git ls-files -z | xargs -0 "$PY" scripts/leak_guard.py --files; echo "leak exit $?"
```
Expected: 다섯 skill 이름과 줄 수, `leak exit 0`.

- [ ] **Step 7: 새 세션에서 발견 여부를 확인하고 커밋**

새 세션을 열어 사용 가능한 skill 목록에 `wiki-ingest`, `wiki-terms`, `wiki-query`, `wiki-lint`, `wiki-audit`가 보이는지 확인한다(보이지 않으면 경로와 frontmatter를 다시 확인한다).
```bash
git add .claude/skills && git commit -q -m "feat(skills): wiki-ingest, wiki-terms, wiki-query, wiki-lint, wiki-audit

Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>"
```

### Task 18: 마무리 — CLAUDE.md, 상태, log, 전체 관문

**Files:**
- Modify: `CLAUDE.md`, `meta/status.md`, `log.md`, `meta/design/2026-09-14-rebuild-plan-phase2.md`(표지 주석 제거)

- [ ] **Step 1: 전체 관문**

```bash
cd /c/Obsidian/ripb && "$PY" -m pytest scripts/refclean/tests scripts/tests -q 2>&1 | tail -1 \
 && "$PY" scripts/lint_wiki.py --all | tail -1 && "$PY" scripts/verify_quotes.py --all | tail -1 \
 && "$PY" scripts/build_index.py --check && "$PY" scripts/sync_terms.py | tail -1 && "$PY" scripts/source.py status | tail -1
```
Expected: 테스트 수는 Task 15의 기대값, lint `0 errors`, verify `0 errors`, index `up to date`, sync `0 notes, 0 conflicts`, `inbox waiting: 0`. 하나라도 다르면 멈추고 보고한다.

- [ ] **Step 2: CLAUDE.md §7 갱신**

§7 도구의 스크립트 목록 문장을 다음으로 바꾼다.
```markdown
- 스크립트(`scripts/`): 정제 `convert_references.py`, `clean_references.py` + `refclean/`; 원문 `source.py`; 검사 `lint_wiki.py`(파일 단위 L01–L20, `--all` L30–L36), `verify_quotes.py`(V1–V5); 변경 `sync_terms.py`(dry-run 기본), `build_index.py`(`--check`), `append_log.py`; 보고 `session_start.py`, `audit_sample.py`; 보조 `notes.py`, `citations.py`, `terms.py`, `leak_guard.py`, `hook_post_edit.py`.
```
§7의 테스트 줄을 바꾼다.
```markdown
- 테스트: `python -m pytest scripts/refclean/tests scripts/tests -q`. 원문을 읽는 테스트는 `@pytest.mark.refs`이며 `references/raw`에 PDF가 없으면 skip된다. 새 테스트가 `references/`를 열면서 표시가 없으면 실패한다.
```
§7의 hook 줄을 바꾼다(Task 15에서 확정한 형식 그대로).
```markdown
- hook: Claude SessionStart → `session_start.py`; PostToolUse(Edit·Write·MultiEdit, `wiki/`·`internal/wiki/`의 `.md`) → `hook_post_edit.py`(lint 파일 단위 + 인용 검증, 실패 시 Claude에게 되돌림); git pre-commit(두 저장소) → 경로 관문, 공개 노트 `[[HSFR_` 거부, `leak_guard.py --staged`(공개), `lint_wiki.py --all`, `verify_quotes.py --all`, `build_index.py --check`; git commit-msg(공개) → `leak_guard.py --message`.
```
§7의 `log.md` 줄을 바꾼다.
```markdown
- `log.md`는 `append_log.py`로만 추가한다(커밋 해시는 적지 않는다). `index.md`는 `build_index.py`가 만든다.
```
§6 승인 규칙은 그대로 둔다. §4 frontmatter 목록에 `terms_pending`을 추가한다: `` `tags`, `terms_pending`(sync_terms가 유지) ``.

- [ ] **Step 3: 상태와 log**

`meta/status.md`: `phase: 3`; "현재 단계"를 `Phase 2 (도구) 완료. 다음은 Phase 3 시범 인제스트(NEI 18-04 §3). 계획: meta/design/2026-09-14-rebuild-plan-phase2.md.`로, "존재하는 도구"를 CLAUDE.md §7과 같은 목록으로, "다음 작업"을 `1. Phase 3 시범 인제스트 계획 (NEI 18-04 §3; wiki-ingest skill 점검 포함)`으로 바꾼다. "미해결"의 ACRS 항목은 Task 19의 결정으로 갱신한다.

```bash
"$PY" scripts/append_log.py --type feat --title "Phase 2 완료: 도구" \
  --item "검사(lint_wiki, verify_quotes), 변경(sync_terms, build_index, append_log), 보고(session_start, audit_sample), 관문(leak_guard, hook 3종), skill 5종, Obsidian 명령·보기." \
  --item "Phase 1 이관 항목 처리: source.py 보강 7건, generic 프로파일, 설계 부록 B·§8.1 수정, refs marker, 내부 문서명 관문."
```

- [ ] **Step 4: 커밋 (Task 15에서 확장한 pre-commit 관문을 거친다)**

```bash
"$PY" scripts/build_index.py --check && git add CLAUDE.md meta/status.md log.md && git commit -q -m "docs: phase 2 complete; CLAUDE.md tools, hooks and tests

Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>" && git log --oneline -1
```
Expected: 관문 통과 후 커밋 1건. push하지 않는다.

### Task 19: ACRS 슬라이드 처리 방침 결정 (R18)  **확인 지점**

`ACRS_ML25293A458` 정제본은 슬라이드 제목이 제목으로 추출되지 않고, 글머리표 문장 일부가 제목으로 올라가며, 캡션 없는 그림 37개가 포함되지 않았다(`wiki/ACRS_ML25293A458.md`, `meta/status.md` 미해결). 인제스트 순서는 부록 A의 10번이므로 구현은 Phase 3에서 그 차례 전에 한다. 이 Task는 방침만 정한다.

- [ ] **Step 1: 사실 확인 (읽기 전용)**

```bash
cd /c/Obsidian/ripb && f=$("$PY" -c "import sys; sys.path.insert(0,'scripts'); import notes; print(notes.load_cards('.')['ACRS_ML25293A458']['fm']['file'])") \
 && grep -c '^<!-- page ' "$f" && grep -c '^#' "$f" && ls "references/figures/ACRS_ML25293A458" 2>/dev/null | wc -l \
 && ls references/raw/*ACRS_ML25293A458*.png references/raw/*ACRS_ML25293A458*_images 2>/dev/null | head -3
```
결과(쪽 표지 수 22 기대, 제목 수, 포함된 그림 수, 원시 변환의 이미지 위치)를 기록한다.

- [ ] **Step 2: 사용자에게 선택지를 묻는다**

한 메시지로 다음을 제시하고 답을 받는다.
1. **전용 프로파일** `profiles/acrs_slides.py`: 쪽마다 첫 텍스트 블록(가장 큰 글꼴)을 `## <슬라이드 제목>`으로 올리고, 글머리표 문장의 제목 승격을 막고, 캡션 없는 그림을 `[!figure] Slide N` callout과 PNG로 넣는다. 비용: 프로파일·테스트 1세션. 인용은 `[ACRS_ML25293A458 slide 제목 p.N]`.
2. **그림 정책만**: generic 프로파일에 "캡션 없는 그림도 쪽 번호 이름으로 포함" 옵션을 추가하고, 제목 문제는 두어 인용을 쪽 단위(`[ACRS_ML25293A458 p.N]`)로만 한다. 비용: 반 세션. 인용 위치가 덜 구체적이다.
3. **보류**: 부록 A 10번 차례에 다시 판단한다. 그 전까지 이 원문을 인용하지 않는다.

권고: 1. 슬라이드 원문은 제목이 곧 절 구조이므로 인용 위치(설계 §5.2)가 제목에 의존한다. 그림이 슬라이드 내용의 큰 부분이다(37개).

- [ ] **Step 3: 결정을 기록하고 커밋**

`meta/status.md`의 미해결 ACRS 항목을 `ACRS_ML25293A458: <선택> (YYYY-MM-DD 결정, Phase 3에서 부록 A 10번 전에 구현)`으로 바꾸고, 소스 카드 `## 알려진 모순` 아래가 아니라 `## 서지`의 기존 제한 사항 문단에 같은 줄을 덧붙인다. `build_index.py --check` 후 커밋(`docs(status): ACRS slide deck handling decided`).
