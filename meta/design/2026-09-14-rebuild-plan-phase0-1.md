# Vault Rebuild — Phase 0–1 Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Reset the vault to a clean git history with the new layout, rules and security boundaries (Phase 0), then bring the source layer to the state the ingest tooling needs: root-aware pipeline, `source.py` with source cards for all 9 cleaned documents, and the two waiting documents registered and converted (Phase 1).

**Architecture:** Phase 0 is a sequence of file-system and git operations with four user-confirmation points; nothing in `references/` is touched except a rename in Phase 1. Phase 1 adds one script (`scripts/source.py`) with its own tests under `scripts/tests/`, extends the existing refclean entry points with a `--root` argument, and registers new documents through the existing pipeline contract (registry `DOCS`, profile module, `--verify` + pytest gate).

**Tech Stack:** Python 3.12 at `C:\Code\Python\pykaeri\.venv12\Scripts\python.exe` (PyYAML 6.0.3, pytest 9.0.3, PyMuPDF, pdfplumber, opendataloader-pdf 2.5.7), JDK 17 at `C:\Program Files\Eclipse Adoptium\jdk-17.0.20.101-hotspot`, Git for Windows (Git Bash for shell steps).

**Spec:** `meta/design/2026-09-14-vault-rebuild-design.md` (decisions D1–D13; §3 layout, §4 pipeline, §9 phases). Phase 2 (tools: lint, verify_quotes, sync_terms, build_index, append_log, session_start, audit_sample, hooks, skills) is a separate plan written after this one completes, because it consumes the source-card format that Task 9 fixes.

## Global Constraints

- Python: always `C:\Code\Python\pykaeri\.venv12\Scripts\python.exe` (below: `$PY`). Never `python` from PATH.
- Shell steps are Git Bash. Absolute vault path `C:\Obsidian\ripb` = `/c/Obsidian/ripb`. Run every command from the vault root.
- `references/<stem>.md` and `references/figures/` are generated: never hand-edit. `references/raw/` is read-only except through `scripts/convert_references.py`. (Spec §4.1)
- Source-text wording stays verbatim; no "corrections" of source typos. (Spec §4.1)
- New files: UTF-8 without BOM, LF line endings. Python writes with `encoding="utf-8", newline="\n"`. (Spec §3.2)
- Wiki/note file names: ASCII `Snake_Case`, unique across `wiki/` and `internal/wiki/`, never equal to a file name under `references/`. (Spec §3.2)
- git #1 never tracks `inbox/`, `references/`, `internal/`, `raw/`. Public files (`wiki/`, `meta/`, `log.md`) never name internal documents; `wiki/` never contains `[[HSFR_` links. (Spec §3.3)
- Commits: `<type>(<scope>): <subject>` (types: init, chore, feat, fix, docs, refactor, test), body optional, and end every commit message with the trailer line `Co-Authored-By: Claude Fable 5.1 <noreply@anthropic.com>`. Push only when the user asks. (Spec D7)
- Confirmation points (marked **확인 지점**) are irreversible; the executor stops, shows the exact command and its effect, and waits for the user's explicit yes. A subagent must not execute a confirmation-point step itself — it reports back and the main session asks the user.
- Acceptance gate for anything touching the pipeline: `$PY -m pytest scripts/refclean/tests -q` → `211 passed` (or the new count stated in the task) and `$PY scripts/clean_references.py --only <KEY> --verify` exits 0.

---

## File Structure

| Path | Responsibility | Created / modified in |
|---|---|---|
| `internal/_legacy/ripb-before-rebuild.bundle` | complete old git history (all refs) | Task 1 |
| `internal/_legacy/raw-gemini.zip`, `internal/_legacy/log-before-rebuild.md` | Gemini-era raw folder and log | Task 2, Task 3 |
| `internal/meetings/*.md`, `internal/.gitignore`, `internal/.githooks/pre-commit` | internal repo (git #2) | Task 3, Task 4 |
| `meta/references_cleanup/**`, `meta/handover/*.md` | relocated pipeline record and handover | Task 3 |
| `.gitignore`, `.gitattributes`, `.githooks/pre-commit` | git #1 boundaries and pre-commit path guard | Task 4 |
| `CLAUDE.md`, `AGENTS.md`, `README.md`, `log.md`, `meta/status.md`, `.obsidian/app.json` | rules, state, Obsidian exclusions | Task 5 |
| `scripts/convert_references.py`, `scripts/clean_references.py` | `--root` argument; frontmatter path relocation | Task 7 |
| `scripts/refclean/profiles/__init__.py`, `scripts/refclean/tests/test_rg1232.py` | RG 1.232 stem rename | Task 8 |
| `scripts/source.py`, `templates/source_card.md`, `scripts/tests/test_source.py`, `scripts/tests/conftest.py` | source registration and source cards | Task 9 |
| `wiki/<KEY>.md` × 9 | source cards for the cleaned documents | Task 10 |
| `scripts/refclean/profiles/generic.py`, `scripts/refclean/tests/test_generic.py` | profile for plain documents (core steps only) | Task 11 |
| `wiki/RG_1.233.md`, `wiki/ACRS_ML25293A458.md`, `references/raw/RG_1.233_Guidance for a Technology-Inclusive, Risk-Informed, and Performance-Based Methodology for Non-Light-Water Reactors.pdf`, `references/raw/ACRS_ML25293A458_NRC Review of Kemmerer Unit 1 Construction Permit Application, Control of Heat Generation (ACRS Subcommittee, 2025-10-22).pdf` | the two waiting documents (stems = `<KEY>_<register title>`; `safe_stem` caps a stem at 150 characters, so register titles stay short and the full title lives in the cleaned frontmatter) | Task 11, Task 12 |

---

## Phase 0

### Task 0: Preconditions and baseline

**Files:** none modified.

- [ ] **Step 1: User confirms the cleanup session is closed**

Ask the user: "정제 세션 `ripb-c0`가 닫혔거나 더 이상 파일을 쓰지 않습니까?" Do not continue until the answer is yes (spec §9.1).

- [ ] **Step 2: Record the baseline**

Run:
```bash
cd /c/Obsidian/ripb && git status --short > "$TEMP/baseline_status.txt" && git log --oneline -3 && git ls-files | wc -l && "$PY" -m pytest scripts/refclean/tests -q 2>&1 | tail -1
```
Expected: last log line is `687c9d5 docs(design): …` (or a later commit of this plan); `git ls-files | wc -l` prints `452` or `453`; pytest prints `211 passed`. If pytest does not print `211 passed`, stop and report — the pipeline is not in the committed state.

- [ ] **Step 3: Verify nothing under `references/` differs from the last commit**

Run: `git status --short references/ | wc -l`
Expected: `0`. (Uncommitted regenerated output would be lost from the snapshot otherwise; if non-zero, list the files and ask the user.)

### Task 1: Final snapshot commit and bundle of the old history  **확인 지점**

**Files:**
- Create: `internal/_legacy/ripb-before-rebuild.bundle`

- [ ] **Step 1: Show the user what the snapshot will contain**

Run: `git add -A --dry-run | wc -l && git add -A --dry-run | head -30`
Expected: about 300 lines (the 267 old wiki notes, `GEMINI.md` deletion, `.gemini/`, `conversations/` incl. the handover note, `log.md`, `index.md`, the four Gemini-era scripts, `.obsidian/` changes). Show the head to the user and get the yes.

- [ ] **Step 2: Commit the snapshot on the old history**

```bash
git add -A && git commit -q -m "chore: final snapshot before vault rebuild (old history ends here)

Working tree as of 2026-09-14 including Gemini-era leftovers, the refclean
handover note and the rebuild design. Archived as a bundle in internal/_legacy/.

Co-Authored-By: Claude Fable 5.1 <noreply@anthropic.com>" && git log --oneline -1 && git status --short | wc -l
```
Expected: one new commit; `git status --short | wc -l` prints `0`.

- [ ] **Step 3: Bundle every ref and verify the bundle**

```bash
mkdir -p internal/_legacy && git bundle create internal/_legacy/ripb-before-rebuild.bundle --all && git bundle verify internal/_legacy/ripb-before-rebuild.bundle && git bundle list-heads internal/_legacy/ripb-before-rebuild.bundle
```
Expected: `verify` prints `… is okay`; `list-heads` lists `refs/heads/main`, `refs/remotes/origin/main` and `HEAD`. Size check: `ls -l internal/_legacy/` shows roughly 6–8 MB.

- [ ] **Step 4: Prove the bundle restores**

```bash
rm -rf "$TEMP/bundle_check" && git clone -q internal/_legacy/ripb-before-rebuild.bundle "$TEMP/bundle_check" && git -C "$TEMP/bundle_check" log --oneline -1 && ls "$TEMP/bundle_check/wiki" | wc -l && rm -rf "$TEMP/bundle_check"
```
Expected: the snapshot commit hash from Step 2 and `268` (267 notes + `assets/`; `wiki/index.md` was already deleted in the working tree).

No further commit: the bundle lives in `internal/`, which git #1 will ignore.

### Task 2: Archive the Gemini-era `raw/` and deduplicate `inbox/`  **확인 지점**

**Files:**
- Create: `internal/_legacy/raw-gemini.zip`
- Move: `raw/1.233 GUIDANCE FOR A TECHNOLOGY-INCLUSIVE~for non-light-water reactors.pdf` → `inbox/`
- Delete: `raw/`, `inbox/RG 1.232, Rev. 0, Guidance for Developing Principal Design Criteria for Non-Light-Water Reactors.pdf`

- [ ] **Step 1: Confirm the duplicate before deleting it**

```bash
sha256sum "inbox/RG 1.232, Rev. 0, Guidance for Developing Principal Design Criteria for Non-Light-Water Reactors.pdf" references/raw/RG_1.232.pdf
```
Expected: both lines start with `8eaa6f99f55366d362a8503b20e2190140677fecd8258a4faf9da8adaf04b985`. If they differ, do not delete; report.

- [ ] **Step 2: Move the only copy of RG 1.233 to the inbox and count the rest**

```bash
mv "raw/1.233 GUIDANCE FOR A TECHNOLOGY-INCLUSIVE~for non-light-water reactors.pdf" inbox/ && find raw -type f | wc -l
```
Expected: `90` (8 text files + 82 files in `Natrium_PSAR_ch3_lbe-summaries/`). Record the printed value as `N_RAW`.

- [ ] **Step 3: Zip `raw/` and verify the entry count**

```bash
"$PY" - <<'EOF'
import shutil, zipfile, os
shutil.make_archive("internal/_legacy/raw-gemini", "zip", root_dir="raw")
n = sum(1 for i in zipfile.ZipFile("internal/_legacy/raw-gemini.zip").infolist() if not i.is_dir())
print("zip entries:", n)
EOF
```
Expected: `zip entries:` equals `N_RAW`.

- [ ] **Step 4: Get the yes, then delete**

Show the user: "`raw/` (`N_RAW` files, zipped and verified) and the duplicate RG 1.232 PDF in `inbox/` will be deleted." After yes:
```bash
rm -rf raw && rm "inbox/RG 1.232, Rev. 0, Guidance for Developing Principal Design Criteria for Non-Light-Water Reactors.pdf" && ls inbox
```
Expected: `inbox` lists exactly `1.233 GUIDANCE FOR A TECHNOLOGY-INCLUSIVE~for non-light-water reactors.pdf` and `ML25293A458.pdf`.

No commit (paths are ignored / working-tree changes are captured by Task 6).

### Task 3: Remove Gemini-era artefacts and relocate records  **확인 지점**

**Files:**
- Delete: `wiki/` (all), `.gemini/`, `.antigravitycli/`, `index.md`, `schema/prompt_compile_raw.md`, `schema/prompt_lint_wiki.md`, `schema/template_concept.md`, `schema/template_map.md`, `scripts/batch_create_sfrdc.py`, `scripts/draw_eta.py`, `scripts/extract_psar.py`, `scripts/lint_wiki.py`, `scripts/patch_underlines.py`, `scripts/process_all_pdfs.py`, `scripts/wiki_utils.py`, `scripts/validate-template.sh`, `scripts/__pycache__/`
- Move: `schema/references_cleanup/` → `meta/references_cleanup/`; `conversations/2026-09-14_handover_references_cleanup.md` → `meta/handover/`; the 2 remaining meeting notes in `conversations/` → `internal/meetings/` (their file names are internal and are not written in public files); `log.md` → `internal/_legacy/log-before-rebuild.md`
- Modify: path strings `schema/references_cleanup` → `meta/references_cleanup` in `scripts/refclean/**/*.py`, `meta/references_cleanup/**/*.md`, `meta/handover/*.md`

- [ ] **Step 1: Show the deletion list and get the yes**

```bash
ls wiki | wc -l; ls -d .gemini .antigravitycli index.md schema/prompt_*.md schema/template_*.md scripts/{batch_create_sfrdc,draw_eta,extract_psar,lint_wiki,patch_underlines,process_all_pdfs,wiki_utils}.py scripts/validate-template.sh
```
Expected: `267` (plus `assets`) and the 15 paths listed without "No such file". Tell the user these are recoverable from the bundle (Task 1) and wait for yes.

- [ ] **Step 2: Delete**

```bash
rm -rf wiki .gemini .antigravitycli scripts/__pycache__ && rm -f index.md schema/prompt_compile_raw.md schema/prompt_lint_wiki.md schema/template_concept.md schema/template_map.md scripts/batch_create_sfrdc.py scripts/draw_eta.py scripts/extract_psar.py scripts/lint_wiki.py scripts/patch_underlines.py scripts/process_all_pdfs.py scripts/wiki_utils.py scripts/validate-template.sh && ls scripts schema
```
Expected: `scripts` lists `clean_references.py convert_references.py refclean`; `schema` lists only `references_cleanup`.

- [ ] **Step 3: Relocate records**

```bash
mkdir -p meta/handover internal/meetings && mv schema/references_cleanup meta/references_cleanup && rmdir schema && mv conversations/2026-09-14_handover_references_cleanup.md meta/handover/ && mv conversations/*.md internal/meetings/ && rmdir conversations && mv log.md internal/_legacy/log-before-rebuild.md && ls meta meta/handover internal/meetings internal/_legacy
```
Expected: `meta` has `design handover references_cleanup`; `internal/meetings` has the 2 meeting notes; `internal/_legacy` has the bundle, the zip and the old log.

- [ ] **Step 4: Rewrite the moved path in docstrings and records**

```bash
grep -rl "schema/references_cleanup" scripts/refclean meta | wc -l && grep -rl "schema/references_cleanup" scripts/refclean meta | xargs sed -i 's#schema/references_cleanup#meta/references_cleanup#g' && grep -rl "schema/references_cleanup" scripts/refclean meta | wc -l
```
Expected: first count > 0 (about 12 files), second count `0`.

- [ ] **Step 5: Pipeline still green**

Run: `"$PY" -m pytest scripts/refclean/tests -q 2>&1 | tail -1`
Expected: `211 passed`.

No commit (captured by Task 6).

### Task 4: Repository boundaries for both repos

**Files:**
- Create: `.gitignore` (replace), `.gitattributes`, `.githooks/pre-commit`, `internal/.gitignore`, `internal/.githooks/pre-commit`
- Create: git #2 in `internal/`

- [ ] **Step 1: Write `.gitignore`**

```gitignore
# 원문 전문 (저작권) — 로컬 전용, 소스 카드의 SHA-256으로 동일성 확인 (spec D11)
inbox/
references/
raw/

# 내부 자료 — 별도 로컬 git (spec D2)
internal/

# Obsidian 작업 상태 (PC별)
.obsidian/workspace.json
.obsidian/workspace-mobile.json
.obsidian/graph.json

# 도구 산출물
docs/superpowers/
.worktrees/
__pycache__/
*.pyc
*.tmp
.pytest_cache/
```

- [ ] **Step 2: Write `.gitattributes`**

```gitattributes
* text=auto eol=lf
*.png binary
*.jpg binary
*.pdf binary
*.bundle binary
*.zip binary
```

- [ ] **Step 3: Write `.githooks/pre-commit` (Phase 0 guard; Phase 2 adds lint and quote verification)**

```sh
#!/bin/sh
# Phase 0 관문 (spec §3.3): 원문·내부 경로는 공개 저장소에 들어오지 못한다.
staged=$(git diff --cached --name-only --diff-filter=ACMR)
bad=$(printf '%s\n' "$staged" | grep -E '^(references/|internal/|inbox/|raw/)')
if [ -n "$bad" ]; then
  echo "pre-commit: refused (local-only paths):"; printf '%s\n' "$bad"; exit 1
fi
# 공개 노트는 내부 노트로 링크하지 않는다.
notes=$(printf '%s\n' "$staged" | grep -E '^wiki/.*\.md$')
if [ -n "$notes" ]; then
  hits=$(printf '%s\n' "$notes" | xargs git diff --cached -U0 -- | grep -E '^\+' | grep -F '[[HSFR_')
  if [ -n "$hits" ]; then
    echo "pre-commit: refused ([[HSFR_ link in a public note):"; printf '%s\n' "$hits"; exit 1
  fi
fi
exit 0
```
Then: `chmod +x .githooks/pre-commit`.

- [ ] **Step 4: Internal repo files**

`internal/.gitignore`:
```gitignore
# 원문 전문 — 로컬 전용
references/
inbox/
# 크기: 압축본은 추적하지 않는다 (bundle은 추적)
_legacy/*.zip
__pycache__/
*.pyc
```
`internal/.githooks/pre-commit`:
```sh
#!/bin/sh
bad=$(git diff --cached --name-only --diff-filter=ACMR | grep -E '^(references/|inbox/)')
if [ -n "$bad" ]; then echo "pre-commit: refused (local-only paths):"; printf '%s\n' "$bad"; exit 1; fi
exit 0
```
`chmod +x internal/.githooks/pre-commit`.

- [ ] **Step 5: Initialise git #2 and make its first commit**

```bash
git -C internal init -q -b main && git -C internal config core.hooksPath .githooks && printf '* text=auto eol=lf\n*.bundle binary\n' > internal/.gitattributes && git -C internal add -A && git -C internal ls-files && git -C internal commit -q -m "init: internal repository (meetings, legacy bundle and log)

Co-Authored-By: Claude Fable 5.1 <noreply@anthropic.com>" && git -C internal log --oneline -1
```
Expected: `ls-files` shows `.gitattributes .githooks/pre-commit .gitignore _legacy/log-before-rebuild.md _legacy/ripb-before-rebuild.bundle meetings/<2 files>` and no `_legacy/raw-gemini.zip`.

- [ ] **Step 6: Hook test on git #2**

```bash
mkdir -p internal/references && echo x > internal/references/probe.md && git -C internal add -f references/probe.md && git -C internal commit -q -m "probe" ; echo "exit=$?" ; git -C internal reset -q && rm -r internal/references
```
Expected: `pre-commit: refused (local-only paths):` and `exit=1`; afterwards `git -C internal status --short` is empty.

### Task 5: CLAUDE.md, AGENTS.md, README.md, status, log, Obsidian exclusions

**Files:**
- Create: `CLAUDE.md`, `meta/status.md`, `log.md`
- Replace: `AGENTS.md`, `README.md`
- Modify: `.obsidian/app.json`

- [ ] **Step 1: Write `CLAUDE.md`**

````markdown
# CLAUDE.md — ripb vault 운영 규칙

이 vault는 TI-RIPB(Technology-Inclusive, Risk-Informed, Performance-Based) 원자력 안전해석 분야의 LLM wiki이다. 관리 주체는 Claude 하나이다. 설계와 결정 근거는 `meta/design/2026-09-14-vault-rebuild-design.md`(이하 "설계")에 있고, 현재 단계와 다음 작업은 `meta/status.md`에 있다. 절차는 `.claude/skills/`의 skill이 담는다(Phase 2 이후). 본문은 한국어, 경로·명령·식별자는 영어로 쓴다.

## 1. 역할과 원칙

- 원문이 말하는 것만 쓴다. 원문에 없는 내용은 "vault에 없음"이라고 쓴다. 배경지식으로 빈칸을 채우지 않는다.
- 빈 틀을 만들지 않는다. 자리표시자만 있는 노트, 존재하지 않는 노트로의 링크는 금지다. 필요한 주제는 누락 목록에 적는다.
- 용어의 한국어 표기를 추측하지 않고 후보도 내지 않는다. 미정 용어는 모아서 한 번에 사용자에게 묻는다(설계 §6).
- 되돌리기 어려운 작업(삭제, 이력 변경, push)은 실행 전에 사용자 확인을 받는다.

## 2. 구조와 데이터 흐름 (설계 §3, §4.2)

| 경로 | 내용 | git |
|---|---|---|
| `wiki/` | 노트. 단일 폴더, 범주는 frontmatter `type`과 접두어(`Natrium_`, `HSFR_`) | #1 |
| `wiki/Terminology.md` | 용어표 (단일 진실 원천) | #1 |
| `meta/` | 설계, 상태, 점검 보고, 정제 파이프라인 기록, 인수인계 | #1 |
| `templates/`, `scripts/`, `.claude/` | 노트 틀, 스크립트, hook·skill | #1 |
| `inbox/`, `inbox/internal/` | 새 원문 투입구 (공개 / 내부) | 제외 |
| `references/raw/` | 원본 PDF와 변환 원시 출력. `convert_references.py`만 쓴다 | 제외 |
| `references/<stem>.md`, `references/figures/` | 정제본 = 인용 대상. 생성물이며 손으로 고치지 않는다 | 제외 |
| `internal/` | 내부 자료: `references/`, `wiki/`, `meetings/`, `log.md`, `_legacy/`. 별도 로컬 git #2 | 제외 |

원문 흐름: `inbox/` → (`scripts/source.py register`) → `references/raw/` → (`convert_references.py` → `clean_references.py`) → `references/<stem>.md` → (인제스트) → `wiki/`. 인제스트 상태는 소스 카드(`wiki/<KEY>.md`, `type: source`)의 `ingest` 필드가 나타낸다.

## 3. 정제 파이프라인 계약 (설계 §4.1)

- `references/<stem>.md`와 `references/figures/`는 생성물이다. 수정은 `scripts/refclean/profiles/<doc>.py` 또는 `scripts/refclean/patches/<KEY>.json`(`find`/`replace`/`count`/`page`/`evidence`)을 거쳐 재빌드한다.
- `references/raw/`는 읽기 전용이다. `_verify/`만 빌드가 쓴다.
- 원문 오기를 교정하지 않는다. 파일별 금지 목록: `meta/references_cleanup/file_reviews/review_*.md` §5.
- 등록: `scripts/refclean/profiles/__init__.py`의 `DOCS[key] = (stem, profile, chapter)`. 문서 키가 소스 ID다.
- 빌드: `python scripts/clean_references.py --only <KEY> --verify` (내부 자료는 `--root internal`). 보고: `references/raw/_verify/<KEY>.json`.
- 수용 관문: `--verify`(누락률 ≤ 2 %) **와** `python -m pytest scripts/refclean/tests -q` 둘 다. 누락률은 회귀 탐지용이지 완전성 증명이 아니다(`refclean/verify.py` 첫머리의 맹점 목록).
- 정제본 형식: `<!-- page N | 인쇄쪽 -->` 쪽 표지(여러 쪽 표는 `<!-- page a-b | x..y -->`, RG 1.232는 레코드 안에서 비단조), `> [!withheld]`, 레코드 형식(`#### SFR-DC 4 — …`, `#### DL3-RC1 — …`), 표 주석 `<sup>n</sup>`, 각주 `[^n]`, 편집 표시 `<!-- source: … -->`·`<!-- header row supplied … -->`, 강조는 RG Table 1 redline·GDC-19 기울임·ch1 굵은 상태 용어만.
- Java: 변환에는 JDK 17이 필요하다(`JAVA17_BIN`, 기본 `C:\Program Files\Eclipse Adoptium\jdk-17.0.20.101-hotspot\bin`). 정제에는 필요 없다.

## 4. 노트 규칙과 인용 형식 (설계 §5)

- frontmatter: `type`(source | regulation | concept | natrium | synthesis | map | hsfr), `aliases`, `sources`(소스 키 목록), `status`(draft → checked → reviewed; disputed, deprecated), `verified`, `term`, `tags`.
- 본문: `# 한국어 제목 (English Title)` → `> [!abstract] 요약`(한국어 2–3문장) → `## 원문 사실` → `## 해설` → `## 관련 문서`.
- 원문 사실 절은 원문 문장(따옴표)과 표 값만 담고 항목마다 인용을 붙인다. 해설은 한국어로 쓰고 원문 사실 절만 근거로 삼는다.
- 인용: `[KEY §3.7.3.1 p.45]`, `[KEY Table 5.2-1 p.12]`, `[KEY SFR-DC 4 p.64]`, `[KEY §3.2.1 p.16-17]`. `p.N`은 PDF 쪽(쪽 표지의 첫 번호). 쪽이 없는 원문은 `[KEY §제목경로]`.
- 원문끼리 모순되면 둘 다 인용하고 `status: disputed`로 둔다.
- 파일명: ASCII `Snake_Case`, vault 전체에서 유일, `references/`의 파일명과 다르게. UTF-8(BOM 없음), LF.
- 그림은 원문에서 렌더링한 PNG만. 재구성 도식은 `synthesis` 노트에서만, "재구성" 표시와 요소별 출처 필수.

## 5. 용어 규칙 (설계 §6)

- 한국어 절에서 용어는 `%%t:ID%%` 표지를 붙인다. 문서마다 첫 등장은 "한국어(English)", 이후는 용어표의 "이후 표기".
- 용어표 `wiki/Terminology.md`가 바뀌면 `scripts/sync_terms.py`가 모든 노트에 전파한다(dry-run 기본, `--apply`).
- 미정 용어는 인제스트 단위마다 모아 번호 목록으로 한 번에 묻는다. 항목에는 English, 약어, 원문 정의 인용만 싣는다. 답은 한국어 표기 / 영어 유지 / 용어 아님.

## 6. 승인 규칙 (설계 §7.2, D7)

- 인제스트 1단위의 접점은 두 번이다. ① 계획 + 용어 질문, ② 변경 요약(새 노트·고친 노트, 검사 결과, 모순, 누락 주제, 미정 용어, 직접 볼 노트 2–3개).
- ②의 승인은 커밋 승인이다. 승인 뒤 log 추가, index 재생성, 커밋까지 한 번에 한다. push는 사용자가 요청할 때만.
- 사용자가 Obsidian에서 직접 고친 노트는 세션 시작 시 lint로 점검하여 결과를 보고한다.

## 7. 도구 (설계 §8)

- Python: `C:\Code\Python\pykaeri\.venv12\Scripts\python.exe`만 쓴다. PATH의 `python`은 쓰지 않는다.
- 스크립트(`scripts/`): `convert_references.py`, `clean_references.py` + `refclean/`(정제), `source.py`(원문 등록·소스 카드), `lint_wiki.py`, `verify_quotes.py`, `sync_terms.py`, `build_index.py`, `append_log.py`, `session_start.py`, `audit_sample.py`. 어느 것이 이미 있는지는 `meta/status.md`가 말한다.
- 규칙: 일괄 수정은 dry-run 기본. 어떤 스크립트도 `inbox/`, `references/raw/`의 내용을 바꾸지 않는다. 검사 실패는 0이 아닌 종료 코드. 파일은 내용을 검증한 뒤에만 쓴다.
- 테스트: `python -m pytest scripts/refclean/tests scripts/tests -q`.
- hook: git pre-commit(`.githooks/`, 두 저장소)이 원문·내부 경로와 공개 노트의 `[[HSFR_` 링크를 거부한다. Phase 2에서 lint·인용 검증이 추가된다.
- `log.md`는 추가만 한다(`append_log.py`, Phase 2 전에는 파일 끝에 항목을 덧붙인다). `index.md`는 `build_index.py`가 만든다(Phase 2 전에는 없다).

## 8. 보안 (설계 §3.3)

- git #1은 `inbox/`, `references/`, `internal/`, `raw/`를 추적하지 않는다. `git add -f`로 우회하지 않는다.
- 공개 파일(`wiki/`, `meta/`, `log.md`, `index.md`)에는 내부 문서의 이름도 쓰지 않는다. 공개 노트는 `[[HSFR_…]]`로 링크하지 않는다. 내부 작업은 `internal/log.md`, `internal/status.md`에만 기록한다.
- 구 이력과 구 자료는 `internal/_legacy/`에 있다(`git clone ripb-before-rebuild.bundle`로 복원).
````

- [ ] **Step 2: Replace `AGENTS.md`**

```markdown
# AGENTS.md

이 vault의 운영 규칙은 `CLAUDE.md` 하나다. 다른 에이전트도 그 파일을 따른다.
```

- [ ] **Step 3: Replace `README.md`**

```markdown
# ripb — TI-RIPB LLM wiki

TI-RIPB(Technology-Inclusive, Risk-Informed, Performance-Based) 원자력 안전해석 분야의 지식 기반이다. Obsidian vault이며, Claude Code가 원문을 인제스트하여 노트를 만들고 유지한다.

- 노트: `wiki/` (원문 사실은 영어 원문 + 위치 인용, 요약·해설은 한국어)
- 규칙: `CLAUDE.md`. 설계: `meta/design/`. 상태: `meta/status.md`.
- 원문(`references/`)과 내부 자료(`internal/`)는 이 저장소에 없다. 원문은 PDF와 `scripts/`의 파이프라인으로 재생성하며, 소스 카드의 SHA-256으로 동일성을 확인한다.

2026-05의 첫 구축분은 2026-09-14에 폐기하고 새 이력으로 시작했다(`meta/design/2026-09-14-vault-rebuild-design.md` §1).
```

- [ ] **Step 4: Write `meta/status.md`**

```markdown
---
updated: 2026-09-14
phase: 0
---
# 상태

## 현재 단계
Phase 0 (안정화, 이력 재시작) 진행 중. 계획: `meta/design/2026-09-14-rebuild-plan-phase0-1.md`.

## 존재하는 도구
- `scripts/convert_references.py`, `scripts/clean_references.py`, `scripts/refclean/` (정제 파이프라인, 테스트 211건)
- 없음: `source.py`, `lint_wiki.py`, `verify_quotes.py`, `sync_terms.py`, `build_index.py`, `append_log.py`, `session_start.py`, `audit_sample.py`, `index.md`, `wiki/Terminology.md`, `.claude/`

## 원문
| 키 | 정제본 | 소스 카드 | ingest |
|---|---|---|---|
| PSAR_ch01, ch03, ch04, ch05, ch06, ch07, ch11, RG_1.232, NEI_18-04 | 있음 (2026-09-13 빌드) | 없음 (Phase 1) | pending |
| RG 1.233, ACRS ML25293A458 | 없음 (`inbox/`) | 없음 | 대기 |

## 다음 작업
1. Phase 0 Task 6: 이력 재시작
2. Phase 1: `--root`, RG 1.232 이름 변경, `source.py`, 소스 카드 9장, inbox 2건 등록

## 미해결
- 없음
```

- [ ] **Step 5: Write the new `log.md`**

```markdown
# log

작업 1건당 항목 1개를 끝에 덧붙인다. 형식: `## [YYYY-MM-DD] <type> | <제목>` + 요점. 구 log(2026-05-02 ~ 2026-09-14)는 `internal/_legacy/log-before-rebuild.md`.

## [2026-09-14] init | vault 재구축 시작 (Phase 0)
- 구 이력 전체를 `internal/_legacy/ripb-before-rebuild.bundle`로 보존하고 새 이력을 시작했다.
- 구 wiki 267개 노트, Gemini 시기 스크립트·설정, 구 `raw/`(압축 보관)를 제거했다. 근거: `meta/design/2026-09-14-vault-rebuild-design.md` §1.
- 정제 파이프라인(`scripts/refclean/`, 커밋 31f826e)과 그 기록(`meta/references_cleanup/`)은 그대로 승계했다.
```

- [ ] **Step 6: Update `.obsidian/app.json`**

Replace the file with:
```json
{
  "promptDelete": false,
  "readableLineLength": false,
  "alwaysUpdateLinks": true,
  "defaultViewMode": "preview",
  "userIgnoreFilters": [
    "inbox/",
    "references/",
    "internal/references/",
    "internal/_legacy/"
  ]
}
```

- [ ] **Step 7: Check encodings and line endings of the new files**

```bash
for f in CLAUDE.md AGENTS.md README.md log.md meta/status.md .gitignore .gitattributes .githooks/pre-commit; do printf '%s: ' "$f"; head -c3 "$f" | od -An -tx1 | tr -d ' \n'; printf ' crlf=%s\n' "$(grep -c $'\r' "$f")"; done
```
Expected: no line starts with `efbbbf` (BOM) and every `crlf=0`.

No commit (captured by Task 6).

### Task 6: History reset and first commit  **확인 지점**

**Files:**
- Delete: `.git/`
- Create: new `.git/` with one commit

- [ ] **Step 1: Last look at the old repository**

```bash
git status --short | wc -l && git log --oneline -1 && git remote -v && git bundle verify internal/_legacy/ripb-before-rebuild.bundle
```
Expected: the status count is large (deletions from Tasks 2–5; fine), the log shows the snapshot commit, `origin` points at `github.com/yhshin12/ripb-wiki.git`, and the bundle is okay. Tell the user: "`.git`을 삭제하고 새 이력을 시작합니다. GitHub의 `yhshin12/ripb-wiki`(구 이력, 내부 문서 2건 포함)는 사용자가 삭제하거나 보관해야 합니다." Wait for yes.

- [ ] **Step 2: Reset**

```bash
rm -rf .git && git init -q -b main && git config core.hooksPath .githooks && git config user.name >/dev/null || echo "set user.name/email"
```
Expected: no output except possibly the reminder; `git config user.name` prints `yshin` (global config).

- [ ] **Step 3: Stage and prove the boundaries**

```bash
git add -A && git ls-files | grep -E '^(references/|internal/|inbox/|raw/)' | wc -l && git ls-files | wc -l && git ls-files | sed 's#/.*##' | sort | uniq -c
```
Expected: first number `0`; the per-top-level summary shows `.githooks .gitignore .gitattributes .obsidian AGENTS.md CLAUDE.md README.md log.md meta scripts` and nothing else (no `wiki` yet — it is empty; no `templates` yet).

- [ ] **Step 4: First commit**

```bash
git commit -q -m "init: vault rebuild — clean history, new layout and rules

Design: meta/design/2026-09-14-vault-rebuild-design.md (D1–D13).
Carries over the refclean pipeline (scripts/refclean, meta/references_cleanup)
from the previous history (bundle in internal/_legacy).

Co-Authored-By: Claude Fable 5.1 <noreply@anthropic.com>" && git log --oneline && git status --short | wc -l
```
Expected: exactly one commit; status count `0`.

- [ ] **Step 5: Hook test on git #1**

```bash
git add -f references/RG_1.232.md && git commit -q -m probe ; echo "exit=$?" ; git reset -q HEAD -- references/RG_1.232.md ; git status --short | wc -l
```
Expected: `pre-commit: refused (local-only paths):` / `references/RG_1.232.md`, `exit=1`, then `0`.

- [ ] **Step 6: Update status and log**

Edit `meta/status.md`: `phase: 1`, "현재 단계" → "Phase 1 (소스 계층 정합)", "다음 작업" → the Phase 1 list. Append to `log.md`:
```markdown

## [2026-09-14] chore | 새 이력 첫 커밋
- git #1 첫 커밋. `references/`, `internal/`, `inbox/`는 추적하지 않는다. pre-commit 관문 확인.
```
Commit: `git add meta/status.md log.md && git commit -q -m "docs(status): phase 0 complete" -m "Co-Authored-By: Claude Fable 5.1 <noreply@anthropic.com>"`.

---

## Phase 1

### Task 7: `--root` for the pipeline entry points

**Files:**
- Modify: `scripts/convert_references.py` (module constants + `main()`)
- Modify: `scripts/clean_references.py` (constants after line 30, `build()`, `main()`)
- Create: `scripts/tests/test_pipeline_root.py` (no `__init__.py` — same layout as `scripts/refclean/tests/`)

**Interfaces:**
- Produces: `convert_references.raw_dir_for(root: str | None) -> str`; `clean_references.set_root(root: str | None) -> None` (sets module globals `RAW`, `OUT`); `clean_references.relocate_paths(meta: dict, raw_dir: str) -> dict`; CLI flag `--root <subdir>` on both scripts (`--root internal` → `internal/references/raw`, `internal/references`).

- [ ] **Step 1: Write the failing tests**

`scripts/tests/test_pipeline_root.py`:
```python
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
```

- [ ] **Step 2: Run them to see them fail**

Run: `"$PY" -m pytest scripts/tests/test_pipeline_root.py -q`
Expected: 3 failures with `AttributeError: module … has no attribute 'raw_dir_for'` / `'set_root'` / `'relocate_paths'`.

- [ ] **Step 3: Implement in `convert_references.py`**

Replace the line `RAW_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "references", "raw")` with:
```python
VAULT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def raw_dir_for(root=None):
    """<vault>/references/raw, or <vault>/<root>/references/raw for a sub-vault such as 'internal'."""
    base = VAULT if not root else os.path.join(VAULT, root)
    return os.path.join(base, "references", "raw")


RAW_DIR = raw_dir_for(None)
```
In `main()`: add `ap.add_argument("--root", default=None, help="sub-vault, e.g. internal")`; after parsing, `raw_dir = raw_dir_for(args.root)`; replace every later `RAW_DIR` in `main()` with `raw_dir` (manifest path, glob, `output_dir=`, the `shutil.move` destination). Add `--root` to the usage docstring.

- [ ] **Step 4: Implement in `clean_references.py`**

Replace the two lines `RAW = os.path.join(VAULT, "references", "raw")` and `OUT = os.path.join(VAULT, "references")` with:
```python
RAW = OUT = None


def set_root(root=None):
    """Point RAW/OUT at <vault>/references[/raw] or <vault>/<root>/references[/raw]."""
    global RAW, OUT
    base = VAULT if not root else os.path.join(VAULT, root)
    RAW = os.path.join(base, "references", "raw")
    OUT = os.path.join(base, "references")


set_root(None)

PATH_FIELDS = ("source_pdf", "raw_json", "raw_md", "raw_json_tables")


def relocate_paths(meta, raw_dir):
    """Profiles write frontmatter paths as 'references/raw/<file>'; make them true for the actual raw_dir."""
    for k in PATH_FIELDS:
        v = meta.get(k)
        if isinstance(v, str) and v:
            meta[k] = os.path.relpath(os.path.join(raw_dir, os.path.basename(v)), VAULT).replace(os.sep, "/")
    return meta
```
In `build()`: right after `meta = prof.metadata(...)` insert `relocate_paths(meta, RAW)`. In `main()`: add `ap.add_argument("--root", default=None, help="sub-vault, e.g. internal")` and call `set_root(args.root)` immediately after `args = ap.parse_args()`. Add `--root` to the usage docstring.

- [ ] **Step 5: Tests pass, output unchanged**

Run: `"$PY" -m pytest scripts/tests/test_pipeline_root.py scripts/refclean/tests -q 2>&1 | tail -1`
Expected: `214 passed`.
Then prove the default build is byte-identical apart from the `cleaned:` date:
```bash
cp "references/TP_Natrium_PSAR2025_ch4_integrated evaluations.md" "$TEMP/ch4_before.md" && "$PY" scripts/clean_references.py --only PSAR_ch04 --no-figures --verify >/dev/null && diff <(grep -v '^cleaned:' "$TEMP/ch4_before.md") <(grep -v '^cleaned:' "references/TP_Natrium_PSAR2025_ch4_integrated evaluations.md") && echo IDENTICAL
```
Expected: `IDENTICAL`.

- [ ] **Step 6: Commit**

```bash
git add scripts/convert_references.py scripts/clean_references.py scripts/tests/test_pipeline_root.py && git commit -q -m "feat(pipeline): --root argument for sub-vault sources (internal/)" -m "Co-Authored-By: Claude Fable 5.1 <noreply@anthropic.com>"
```

### Task 8: Rename the RG 1.232 stem (spec §3.2)

**Files:**
- Rename: `references/raw/RG_1.232.pdf` → `references/raw/RG_1.232_Guidance for Developing Principal Design Criteria for Non-Light-Water Reactors.pdf`
- Regenerate: `references/raw/<new stem>.{json,md}`, `<new stem>_images/`, `references/<new stem>.md`
- Delete: `references/raw/RG_1.232.{json,md}`, `references/raw/RG_1.232_images/`, `references/RG_1.232.md`, the `RG_1.232.pdf` entry in `references/raw/_conversion.json`
- Modify: `scripts/refclean/profiles/__init__.py:12`, `scripts/refclean/tests/test_rg1232.py:20`

**Interfaces:**
- Produces: `DOCS["RG_1.232"] == ("RG_1.232_Guidance for Developing Principal Design Criteria for Non-Light-Water Reactors", "rg1232", None)`. Key unchanged, so `patches/RG_1.232.json`, `_verify/RG_1.232.json` and `figures/RG_1.232/` are unaffected.

- [ ] **Step 1: Keep the current output for comparison and rename the PDF**

```bash
NEW="RG_1.232_Guidance for Developing Principal Design Criteria for Non-Light-Water Reactors" && cp references/RG_1.232.md "$TEMP/rg_before.md" && mv references/raw/RG_1.232.pdf "references/raw/$NEW.pdf" && rm -r references/raw/RG_1.232.json references/raw/RG_1.232.md references/raw/RG_1.232_images && "$PY" - <<'EOF'
import json
p = "references/raw/_conversion.json"
m = json.load(open(p, encoding="utf-8")); m.pop("RG_1.232.pdf", None)
json.dump(m, open(p, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
print("conversion entries:", len(m))
EOF
```
Expected: `conversion entries: 8`.

- [ ] **Step 2: Update the registry and the test constant**

`scripts/refclean/profiles/__init__.py` line 12:
```python
    "RG_1.232": ("RG_1.232_Guidance for Developing Principal Design Criteria for Non-Light-Water Reactors", "rg1232", None),
```
`scripts/refclean/tests/test_rg1232.py` line 20:
```python
STEM = "RG_1.232_Guidance for Developing Principal Design Criteria for Non-Light-Water Reactors"
```

- [ ] **Step 3: Convert and clean under the new stem**

```bash
"$PY" scripts/convert_references.py --only "RG_1.232_" && "$PY" scripts/clean_references.py --only RG_1.232 --verify | tail -2 && rm references/RG_1.232.md && ls references | grep RG_
```
Expected: `converted: RG_1.232_Guidance ….pdf`; the verify line shows `missing_pct` ≤ 0.8 (was 0.74); `ls` shows only the new `references/RG_1.232_Guidance ….md`.

- [ ] **Step 4: Body identical to the previous build**

```bash
"$PY" - <<'EOF'
import os
new = "references/RG_1.232_Guidance for Developing Principal Design Criteria for Non-Light-Water Reactors.md"
old = os.path.join(os.environ["TEMP"], "rg_before.md")
def body(p):
    t = open(p, encoding="utf-8").read()
    return t.split("\n---\n", 1)[1]          # everything after the frontmatter
a, b = body(old), body(new)
print("BODY IDENTICAL" if a == b else f"DIFFERENT: {sum(1 for x, y in zip(a.splitlines(), b.splitlines()) if x != y)} lines")
EOF
```
Expected: `BODY IDENTICAL`. (Only the frontmatter differs: `source_pdf`, `raw_json`, `raw_md`, `cleaned`.)

- [ ] **Step 5: Suite green**

Run: `"$PY" -m pytest scripts/refclean/tests scripts/tests -q 2>&1 | tail -1`
Expected: `214 passed`.

- [ ] **Step 6: Commit**

```bash
git add scripts/refclean/profiles/__init__.py scripts/refclean/tests/test_rg1232.py && git commit -q -m "refactor(pipeline): RG 1.232 stem carries the title (no name clash with wiki/RG_1.232.md)" -m "Co-Authored-By: Claude Fable 5.1 <noreply@anthropic.com>"
```

### Task 9: `source.py` and the source-card template

**Files:**
- Create: `scripts/source.py`, `templates/source_card.md`, `scripts/tests/conftest.py`, `scripts/tests/test_source.py`

**Interfaces:**
- Consumes: `refclean.profiles.DOCS` (key → (stem, profile, chapter)); cleaned-file frontmatter keys `pdf_pages`, `tables`, `figures`, `withheld`, `page_labels`, `converter`, `cleaned`; `references/raw/_verify/<KEY>.json` → `["verify"]["summary"]["missing_pct"]`.
- Produces (module `source`): `VAULT`; `dirs(root) -> dict(root, raw, refs, wiki, inbox)`; `sha256(path) -> str`; `safe_stem(key, title) -> str`; `read_note(path) -> (fm: dict, body: str)`; `write_note(path, fm, body)`; `load_docs() -> dict` (overridable in tests); commands `register(pdf, key, title, root)`, `adopt(key, root)`, `sync(key, root)`, `finish(key, root)`, `status(root)`; CLI `python scripts/source.py {register|adopt|sync|finish|status} …`. Source-card frontmatter: `type, key, title, file, pdf, sha256_pdf, sha256_md, pdf_pages, build, ingest, units`. Sync block in the card body between `<!-- sync:begin -->` and `<!-- sync:end -->`.

- [ ] **Step 1: Write the template**

`templates/source_card.md`:
```markdown
# {title} ({key})

> [!abstract] 요약
> (인제스트 완료 시 작성)

## 서지
- 키: `{key}`
- 원문: `{pdf}`

## 구조
<!-- sync:begin -->
(sync 전)
<!-- sync:end -->

## 알려진 모순
- 없음

## 관련 문서
- 없음
```
(The empty summary is allowed for `type: source` while `ingest != complete`; Phase 2 lint must exempt it.)

- [ ] **Step 2: Write the test fixture**

`scripts/tests/conftest.py`:
```python
import os
import shutil
import sys

import pytest

SCRIPTS = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REAL_VAULT = os.path.dirname(SCRIPTS)
sys.path.insert(0, SCRIPTS)


@pytest.fixture
def vault(tmp_path, monkeypatch):
    """A throw-away vault with the real template and empty inbox/references/wiki (public and internal)."""
    import source
    for d in ("inbox", "inbox/internal", "references/raw", "wiki", "templates",
              "internal/references/raw", "internal/wiki"):
        os.makedirs(tmp_path / d)
    shutil.copy(os.path.join(REAL_VAULT, "templates", "source_card.md"), tmp_path / "templates" / "source_card.md")
    monkeypatch.setattr(source, "VAULT", str(tmp_path))
    monkeypatch.setattr(source, "load_docs", lambda: {"DOC_A": ("DOC_A_Some Title", "generic", None)})
    return tmp_path
```

- [ ] **Step 3: Write the failing tests**

`scripts/tests/test_source.py`:
```python
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
    card = source.register(str(pdf), key="HSFR_X", title="Design Note", root="internal")
    assert (vault / "internal" / "references" / "raw" / "HSFR_X_Design Note.pdf").exists()
    assert card.startswith(str(vault / "internal" / "wiki"))
    fm, _ = source.read_note(card)
    assert fm["pdf"] == "internal/references/raw/HSFR_X_Design Note.pdf"


def test_register_refuses_duplicate_by_hash(vault):
    a = make_pdf(vault / "inbox" / "a.pdf", b"SAME")
    source.register(str(a), key="DOC_A", title="T", root=None)
    b = make_pdf(vault / "inbox" / "b.pdf", b"SAME")
    # same bytes except the trailing file name -> make them truly identical
    with open(b, "wb") as f, open(vault / "references" / "raw" / "DOC_A_T.pdf", "rb") as g:
        f.write(g.read())
    with pytest.raises(source.SourceError, match="duplicate of DOC_A"):
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
```

- [ ] **Step 4: Run to see them fail**

Run: `"$PY" -m pytest scripts/tests/test_source.py -q 2>&1 | tail -3`
Expected: `ModuleNotFoundError: No module named 'source'` (collection error).

- [ ] **Step 5: Implement `scripts/source.py`**

```python
"""source.py — register source documents and maintain their source cards (spec §4.2, appendix B).

Usage (run from the vault root with the pykaeri venv python):
  python scripts/source.py register <pdf in inbox/> --key KEY --title "Title" [--root internal]
  python scripts/source.py adopt KEY [--root internal]        # card for a PDF already in references/raw (DOCS entry)
  python scripts/source.py sync  (KEY | --all) [--root internal]   # build fields + structure block from the cleaned file
  python scripts/source.py finish KEY [--root internal]       # sync, then ingest: complete
  python scripts/source.py status [--root internal]

Rules: the PDF is only moved, never modified; nothing under references/raw is written except the PDF itself.
"""
import argparse
import hashlib
import json
import os
import re
import shutil
import sys

import yaml

VAULT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FORBIDDEN = re.compile(r'[\\/:*?"<>|]')


class SourceError(Exception):
    pass


def dirs(root=None):
    base = VAULT if not root else os.path.join(VAULT, root)
    return {
        "root": base,
        "raw": os.path.join(base, "references", "raw"),
        "refs": os.path.join(base, "references"),
        "wiki": os.path.join(base, "wiki"),
        "inbox": os.path.join(VAULT, "inbox", root) if root else os.path.join(VAULT, "inbox"),
    }


def load_docs():
    sys.path.insert(0, os.path.join(VAULT, "scripts"))
    from refclean.profiles import DOCS
    return DOCS


def sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def safe_stem(key, title):
    t = FORBIDDEN.sub("", title)
    t = re.sub(r"\s+", " ", t).strip()
    return f"{key}_{t}"[:150].rstrip()


def rel(path):
    return os.path.relpath(path, VAULT).replace(os.sep, "/")


def read_note(path):
    with open(path, encoding="utf-8") as f:
        text = f.read()
    if not text.startswith("---\n"):
        return {}, text
    _, fm, body = text.split("---\n", 2)
    return (yaml.safe_load(fm) or {}), body.lstrip("\n")


def write_note(path, fm, body):
    text = "---\n" + yaml.safe_dump(fm, allow_unicode=True, sort_keys=False) + "---\n\n" + body
    if not text.endswith("\n"):
        text += "\n"
    assert "\r" not in text
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)


def card_path(key, root=None):
    return os.path.join(dirs(root)["wiki"], f"{key}.md")


def _all_cards():
    for r in (None, "internal"):
        w = dirs(r)["wiki"]
        if not os.path.isdir(w):
            continue
        for fn in os.listdir(w):
            if fn.endswith(".md"):
                fm, _ = read_note(os.path.join(w, fn))
                if fm.get("type") == "source":
                    yield fm


def _new_card(key, title, pdf_path, root):
    path = card_path(key, root)
    if os.path.exists(path):
        raise SourceError(f"card exists: {rel(path)}")
    with open(os.path.join(VAULT, "templates", "source_card.md"), encoding="utf-8") as f:
        body = f.read().format(title=title, key=key, pdf=rel(pdf_path))
    fm = {"type": "source", "key": key, "title": title, "file": "", "pdf": rel(pdf_path),
          "sha256_pdf": sha256(pdf_path), "sha256_md": "", "pdf_pages": 0, "build": {},
          "ingest": "pending", "units": []}
    os.makedirs(os.path.dirname(path), exist_ok=True)
    write_note(path, fm, body)
    return path


def register(pdf, key, title, root=None):
    d = dirs(root)
    pdf = os.path.abspath(pdf)
    if not os.path.isfile(pdf):
        raise SourceError(f"not a file: {pdf}")
    digest = sha256(pdf)
    for fm in _all_cards():
        if fm.get("sha256_pdf") == digest:
            raise SourceError(f"duplicate of {fm['key']} ({fm['pdf']}); left in inbox")
    if os.path.exists(card_path(key, root)):
        raise SourceError(f"card exists: {rel(card_path(key, root))}")
    dest = os.path.join(d["raw"], safe_stem(key, title) + ".pdf")
    if os.path.exists(dest):
        raise SourceError(f"target exists: {rel(dest)}")
    os.makedirs(d["raw"], exist_ok=True)
    shutil.move(pdf, dest)
    path = _new_card(key, title, dest, root)
    print(f"registered {key}: {rel(dest)}\n  card: {rel(path)}\n  next: convert_references.py"
          f"{' --root ' + root if root else ''} --only \"{os.path.basename(dest)[:20]}\" ; add DOCS['{key}'] ; "
          f"clean_references.py --only {key} --verify ; source.py sync {key}")
    return path


def _stem(key, root):
    docs = load_docs()
    if key in docs:
        return docs[key][0]
    fm, _ = read_note(card_path(key, root))
    return os.path.splitext(os.path.basename(fm["pdf"]))[0]


def adopt(key, root=None):
    docs = load_docs()
    if key not in docs:
        raise SourceError(f"{key} is not in DOCS")
    stem = docs[key][0]
    pdf = os.path.join(dirs(root)["raw"], stem + ".pdf")
    if not os.path.isfile(pdf):
        raise SourceError(f"missing PDF: {rel(pdf)}")
    title = stem[len(key) + 1:] if stem.startswith(key + "_") else stem
    path = _new_card(key, title, pdf, root)
    sync(key, root)
    return path


def _sync_block(fm_clean):
    lines = [f"- PDF 쪽 수: {fm_clean.get('pdf_pages', '')}", f"- 인쇄 쪽: {fm_clean.get('page_labels', '')}"]
    for label, k in (("표", "tables"), ("그림", "figures"), ("비공개", "withheld")):
        items = fm_clean.get(k) or []
        lines.append(f"- {label} ({len(items)}):")
        lines += [f"  - {x}" for x in items]
    return "\n".join(lines)


def sync(key, root=None):
    d = dirs(root)
    path = card_path(key, root)
    if not os.path.exists(path):
        raise SourceError(f"no card for {key}")
    fm, body = read_note(path)
    cleaned = os.path.join(d["refs"], _stem(key, root) + ".md")
    if os.path.isfile(cleaned):
        fmc, _ = read_note(cleaned)
        fm["file"] = rel(cleaned)
        fm["sha256_md"] = sha256(cleaned)
        fm["pdf_pages"] = int(fmc.get("pdf_pages") or 0)
        build = {"converter": fmc.get("converter", ""), "cleaned": fmc.get("cleaned", "")}
        vpath = os.path.join(d["raw"], "_verify", f"{key}.json")
        if os.path.isfile(vpath):
            with open(vpath, encoding="utf-8") as f:
                build["missing_pct"] = json.load(f).get("verify", {}).get("summary", {}).get("missing_pct")
        fm["build"] = build
        body = re.sub(r"<!-- sync:begin -->.*?<!-- sync:end -->",
                      "<!-- sync:begin -->\n" + _sync_block(fmc) + "\n<!-- sync:end -->", body, flags=re.S)
    else:
        print(f"{key}: no cleaned file yet ({rel(cleaned)})")
    write_note(path, fm, body)
    return path


def finish(key, root=None):
    sync(key, root)
    path = card_path(key, root)
    fm, body = read_note(path)
    if not fm["file"]:
        raise SourceError(f"{key}: no cleaned file; cannot finish")
    if any(u.get("status") != "complete" for u in fm.get("units", [])):
        raise SourceError(f"{key}: units not complete")
    fm["ingest"] = "complete"
    write_note(path, fm, body)
    print(f"{key}: ingest complete")
    return path


def status(root=None):
    d = dirs(root)
    rows = []
    wiki = d["wiki"]
    for fn in sorted(os.listdir(wiki)) if os.path.isdir(wiki) else []:
        fm, _ = read_note(os.path.join(wiki, fn))
        if fm.get("type") != "source":
            continue
        units = fm.get("units", [])
        done = sum(1 for u in units if u.get("status") == "complete")
        cleaned = os.path.join(VAULT, fm["file"]) if fm.get("file") else ""
        sha_ok = bool(cleaned) and os.path.isfile(cleaned) and sha256(cleaned) == fm.get("sha256_md")
        rows.append((fm["key"], fm.get("ingest", "?"), f"{done}/{len(units)}", "yes" if fm.get("file") else "no",
                     "ok" if sha_ok else ("-" if not cleaned else "CHANGED")))
    inbox = d["inbox"]
    waiting = [f for f in os.listdir(inbox) if f.lower().endswith(".pdf")] if os.path.isdir(inbox) else []
    print(f"{'key':<22}{'ingest':<12}{'units':<8}{'cleaned':<9}sha")
    for r in rows:
        print(f"{r[0]:<22}{r[1]:<12}{r[2]:<8}{r[3]:<9}{r[4]}")
    print(f"inbox waiting: {len(waiting)}" + (": " + ", ".join(waiting) if waiting else ""))
    return rows


def main():
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    p = sub.add_parser("register"); p.add_argument("pdf"); p.add_argument("--key", required=True); p.add_argument("--title", required=True); p.add_argument("--root")
    p = sub.add_parser("adopt"); p.add_argument("key"); p.add_argument("--root")
    p = sub.add_parser("sync"); p.add_argument("key", nargs="?"); p.add_argument("--all", action="store_true"); p.add_argument("--root")
    p = sub.add_parser("finish"); p.add_argument("key"); p.add_argument("--root")
    p = sub.add_parser("status"); p.add_argument("--root")
    a = ap.parse_args()
    sys.stdout.reconfigure(encoding="utf-8")
    try:
        if a.cmd == "register":
            register(a.pdf, a.key, a.title, a.root)
        elif a.cmd == "adopt":
            adopt(a.key, a.root)
        elif a.cmd == "sync":
            keys = [a.key] if a.key else [fm["key"] for fm in _all_cards()] if a.all else []
            if not keys:
                raise SourceError("sync: give KEY or --all")
            for k in keys:
                sync(k, a.root)
        elif a.cmd == "finish":
            finish(a.key, a.root)
        elif a.cmd == "status":
            status(a.root)
    except SourceError as e:
        print(f"error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
```

- [ ] **Step 6: Run the tests**

Run: `"$PY" -m pytest scripts/tests -q 2>&1 | tail -1`
Expected: `14 passed` (3 from Task 7 + 11 here). If `test_register_refuses_duplicate_by_hash` fails on the duplicate message, check that `_all_cards()` reads `sha256_pdf` from both trees.

- [ ] **Step 7: Commit**

```bash
git add scripts/source.py templates/source_card.md scripts/tests/conftest.py scripts/tests/test_source.py && git commit -q -m "feat(source): register/adopt/sync/finish/status for source documents and cards" -m "Co-Authored-By: Claude Fable 5.1 <noreply@anthropic.com>"
```

### Task 10: Source cards for the nine cleaned documents

**Files:**
- Create: `wiki/PSAR_ch01.md`, `wiki/PSAR_ch03.md`, `wiki/PSAR_ch04.md`, `wiki/PSAR_ch05.md`, `wiki/PSAR_ch06.md`, `wiki/PSAR_ch07.md`, `wiki/PSAR_ch11.md`, `wiki/RG_1.232.md`, `wiki/NEI_18-04.md`
- Modify: `meta/status.md`, `log.md`

- [ ] **Step 1: Adopt all registry keys**

```bash
for k in PSAR_ch01 PSAR_ch03 PSAR_ch04 PSAR_ch05 PSAR_ch06 PSAR_ch07 PSAR_ch11 RG_1.232 NEI_18-04; do "$PY" scripts/source.py adopt "$k" || break; done && "$PY" scripts/source.py status
```
Expected: nine cards; the status table shows `ingest pending`, `cleaned yes`, `sha ok` for all nine, `inbox waiting: 2`.

- [ ] **Step 2: Fix the titles the stem cannot supply**

`adopt` derives `title` from the stem after `<KEY>_`, which is right for `RG_1.232` and `NEI_18-04` but not for the seven PSAR stems (they start with `TP_Natrium_PSAR2025_`). For those seven, set the frontmatter `title` and the H1 by hand (the only hand-edit allowed on a card); the last two rows below are for checking only:

| key | title |
|---|---|
| PSAR_ch01 | General Plant and Site Description |
| PSAR_ch03 | Licensing Basis Events |
| PSAR_ch04 | Integrated Evaluations |
| PSAR_ch05 | Safety Functions, Design Criteria, and SSC Safety Classification |
| PSAR_ch06 | Safety-Significant SSC Criteria and Capabilities |
| PSAR_ch07 | Descriptions for Safety-Significant SSCs |
| PSAR_ch11 | Conduct of Operations |
| NEI_18-04 | Modernization of Technical Requirements for Licensing of Advanced Non-Light Water Reactors |
| RG_1.232 | Guidance for Developing Principal Design Criteria for Non-Light-Water Reactors |

Use a Python loop that calls `source.read_note`/`source.write_note` and replaces the first line `# <old> (<key>)` with `# <title> (<key>)`. Then add the known source-side contradiction to `wiki/PSAR_ch03.md` under `## 알려진 모순`: `- Table 3.5-2 titles RRS-ISPL-BL "RAB Barrier Fails to Retain Release"; §3.7.3.3 heading says "Successfully Retains" [PSAR_ch03 Table 3.5-2, §3.7.3.3]` (from the 2026-09-11 audit).

- [ ] **Step 3: Verify cards**

```bash
"$PY" - <<'EOF'
import glob, sys; sys.path.insert(0, "scripts"); import source
for p in sorted(glob.glob("wiki/*.md")):
    fm, body = source.read_note(p)
    assert fm["type"] == "source" and fm["file"] and fm["sha256_md"] and fm["pdf_pages"] > 0, p
    assert body.startswith(f"# {fm['title']} ({fm['key']})"), p
    print(fm["key"], fm["pdf_pages"], fm["build"]["missing_pct"])
EOF
```
Expected: nine lines; `missing_pct` values match the 2026-09-13 residuals (ch1 1.66, ch3 0.14, ch4 0.0, ch5 1.07, ch6 0.13, ch7 0.43, ch11 0.82, RG ≤ 0.8, NEI 1.13).

- [ ] **Step 4: Status, log, commit**

Update `meta/status.md` (source card column → "있음", 존재하는 도구 → add `source.py`, next work → Task 11–12) and append to `log.md`:
```markdown

## [2026-09-14] feat | 소스 카드 9장
- `scripts/source.py adopt`로 정제본 9건의 소스 카드를 만들었다(`wiki/<KEY>.md`, `ingest: pending`). RG 1.232 원문 파일명에 제목을 붙였다(재변환, 본문 동일).
```
```bash
git add wiki meta/status.md log.md && git commit -q -m "feat(wiki): source cards for the 9 cleaned documents" -m "Co-Authored-By: Claude Fable 5.1 <noreply@anthropic.com>"
```

### Task 11: Generic profile and RG 1.233

**Files:**
- Create: `scripts/refclean/profiles/generic.py`, `scripts/refclean/tests/test_generic.py`
- Modify: `scripts/refclean/profiles/__init__.py` (add `RG_1.233`)
- Create (untracked): `references/raw/RG_1.233_Guidance for a Technology-Inclusive, Risk-Informed, and Performance-Based Methodology for Non-Light-Water Reactors.pdf` and its conversion; `references/<same stem>.md`
- Create: `wiki/RG_1.233.md`

**Interfaces:**
- Consumes: `refclean.structure` steps `drop_toc, promote_headings, insert_subheads, fix_false_items, join_breaks, attach_captions_and_merge, attach_table_notes, normalise_text, references_as_items, normalise_item_levels`; `refclean.figures.figures_step(doc, aux, render=…)`; `refclean.profiles.psar.assign_levels(doc, aux)`.
- Produces: profile module `generic` with `steps() -> list` and `metadata(doc, aux) -> dict` (keys `doc_id, title, doc_type, issuer, revision, date, source_pdf, raw_json, pdf_pages, tables, figures, withheld, tags, aliases` — `source_pdf`/`raw_json` in the `references/raw/<stem>` form that `clean_references.relocate_paths` expects); registry entry `"RG_1.233": (<stem>, "generic", None)`. The generic profile takes its bibliographic values from a `META` dict keyed by doc key inside the module.

- [ ] **Step 1: Register and convert**

```bash
"$PY" scripts/source.py register "inbox/1.233 GUIDANCE FOR A TECHNOLOGY-INCLUSIVE~for non-light-water reactors.pdf" --key RG_1.233 --title "Guidance for a Technology-Inclusive, Risk-Informed, and Performance-Based Methodology for Non-Light-Water Reactors" && "$PY" scripts/convert_references.py --only RG_1.233 && ls references/raw | grep -c RG_1.233
```
Expected: `registered RG_1.233: references/raw/RG_1.233_Guidance for a Technology-Inclusive, Risk-Informed, and Performance-Based Methodology for Non-Light-Water Reactors.pdf`; `converted: …`; count `4` (pdf, json, md, `_images`). The register title is deliberately the short form (stem < 150 characters); the full RG title goes into `META` in Step 4. (`PROFILES` prefix `RG_` applies `detect_strikethrough`, harmless here.)

- [ ] **Step 2: Write the failing profile test**

`scripts/refclean/tests/test_generic.py`:
```python
"""Generic profile (core steps only) on RG 1.233: one in-memory build, gate = structure present, verify residual ≤ 2 %."""
import os
import sys

import pytest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

VAULT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
RAW = os.path.join(VAULT, "references", "raw")
KEY = "RG_1.233"


@pytest.fixture(scope="module")
def built():
    import clean_references as CR
    from refclean.doc import load_doc
    from refclean.emit import render
    from refclean.pdfaux import build_aux
    from refclean.profiles import DOCS, generic
    from refclean.verify import verify
    stem = DOCS[KEY][0]
    if not os.path.exists(os.path.join(RAW, stem + ".json")):
        pytest.skip("RG 1.233 conversion not available")
    doc = load_doc(KEY, stem, CR.RAW, CR.OUT)
    aux = build_aux(doc.pdf_path, chapter=None, exclude=CR.table_regions(doc))
    aux.meta["render_figures"] = False
    for step in generic.steps():
        step(doc, aux)
    text, failed = CR.apply_patches(KEY, render(doc, generic.metadata(doc, aux)))
    return doc, aux, text, failed, verify(doc, aux, text)


def test_metadata_and_anchors(built):
    doc, aux, text, failed, ver = built
    assert failed == []
    assert 'doc_id: "RG 1.233"' in text and "pdf_pages: 31" in text
    assert text.count("<!-- page ") >= 25


def test_no_toc_and_headings_present(built):
    _, _, text, _, _ = built
    body = text.split("\n---\n", 1)[1]
    assert ". . . . ." not in body
    for h in ("A. INTRODUCTION", "B. DISCUSSION", "C. STAFF REGULATORY GUIDANCE", "D. IMPLEMENTATION"):
        assert any(line.lstrip("# ").strip().upper().startswith(h) for line in body.splitlines() if line.startswith("#")), h


def test_verify_residual_within_gate(built):
    _, _, _, _, ver = built
    assert ver["summary"]["missing_pct"] <= 2.0, ver["summary"]
```
(If the heading texts of RG 1.233 differ from the four listed, read the PDF's first pages and replace them with the printed section titles — do not weaken the test to "some heading exists".)

- [ ] **Step 3: Run to see it fail**

Run: `"$PY" -m pytest scripts/refclean/tests/test_generic.py -q 2>&1 | tail -2`
Expected: `KeyError: 'RG_1.233'` or `ImportError: cannot import name 'generic'`.

- [ ] **Step 4: Implement the profile and register the key**

`scripts/refclean/profiles/generic.py`:
```python
"""Generic profile: the core pipeline only, for plain documents (guides, slide decks) that need no document-specific
steps. Bibliographic fields come from META[key]; add an entry when registering a document with this profile."""
from .. import structure as S
from ..figures import figures_step
from .psar import assign_levels

META = {
    "RG_1.233": {
        "doc_id": "RG 1.233", "doc_type": "Regulatory Guide", "issuer": "U.S. Nuclear Regulatory Commission",
        "revision": "0", "date": "2020-06",
        "title": ("Guidance for a Technology-Inclusive, Risk-Informed, and Performance-Based Methodology to Inform "
                  "the Licensing Basis and Content of Applications for Licenses, Certifications, and Approvals for "
                  "Non-Light-Water Reactors"),
        "tags": ["reference", "nrc", "regulatory-guide"], "aliases": ["RG 1.233"],
    },
}


def steps():
    return [
        S.drop_toc,
        S.withheld_callouts,
        lambda d, a: figures_step(d, a, render=a.meta.get("render_figures", True)),
        S.promote_headings,
        S.insert_subheads,
        S.fix_false_items,
        S.join_breaks,
        S.attach_captions_and_merge,
        S.attach_table_notes,
        S.normalise_text,
        S.references_as_items,
        S.normalise_item_levels,
        assign_levels,
    ]


def metadata(doc, aux):
    m = dict(META[doc.key])
    tables = [e.table.caption for e in doc.els if e.kind == "table" and e.table.caption]
    m.update({
        "source_pdf": f"references/raw/{doc.stem}.pdf",
        "raw_json": f"references/raw/{doc.stem}.json",
        "pdf_pages": doc.n_pages,
        "tables": tables,
        "figures": doc.meta.get("figures", []),
        "withheld": doc.meta.get("withheld", []),
    })
    return m
```
Registry (`profiles/__init__.py`), after the `NEI_18-04` entry:
```python
    "RG_1.233": ("RG_1.233_Guidance for a Technology-Inclusive, Risk-Informed, and Performance-Based Methodology "
                 "for Non-Light-Water Reactors", "generic", None),
```
(The stem must equal the PDF file name that `source.py register` produced in Step 1 — check with `ls references/raw | grep RG_1.233` and copy it exactly; `safe_stem` keeps commas.)

- [ ] **Step 5: Build, iterate to the gate, test**

```bash
"$PY" scripts/clean_references.py --only RG_1.233 --verify | tail -3 && "$PY" -m pytest scripts/refclean/tests/test_generic.py -q 2>&1 | tail -1
```
Expected: the build exits 0 with `missing_pct` ≤ 2.0 and the 3 tests pass. If the residual is above 2 %, look at `references/raw/_verify/RG_1.233.json` → `top_missing`/`pages_missing`: header/footer bands and figure debris are the usual causes; the allowed fixes are (a) a `patches/RG_1.233.json` entry with `count` and `evidence`, or (b) a document step appended in `generic.py` behind `if doc.key == "RG_1.233"`. Do not edit core modules. If the gate cannot be met within this task, record the residual and its cause in `wiki/RG_1.233.md` under `## 알려진 모순`, keep `ingest: pending`, and report — the ingest plan then schedules a dedicated profile.

- [ ] **Step 6: Sync the card, run the whole suite, commit**

```bash
"$PY" scripts/source.py sync RG_1.233 && "$PY" -m pytest scripts/refclean/tests scripts/tests -q 2>&1 | tail -1
```
Expected: `228 passed` (211 refclean + 3 generic + 3 root + 11 source).
```bash
git add scripts/refclean/profiles/generic.py scripts/refclean/profiles/__init__.py scripts/refclean/tests/test_generic.py wiki/RG_1.233.md && git commit -q -m "feat(pipeline): generic profile; RG 1.233 registered, converted and cleaned" -m "Co-Authored-By: Claude Fable 5.1 <noreply@anthropic.com>"
```

### Task 12: ACRS slide deck ML25293A458

**Files:**
- Modify: `scripts/refclean/profiles/generic.py` (`META` entry), `scripts/refclean/profiles/__init__.py`, `scripts/refclean/tests/test_generic.py`
- Create: `wiki/ACRS_ML25293A458.md`; (untracked) `references/raw/ACRS_ML25293A458_NRC Review of Kemmerer Unit 1 Construction Permit Application, Control of Heat Generation (ACRS Subcommittee, 2025-10-22).pdf` and its conversion and cleaned file
- Modify: `meta/status.md`, `log.md`

- [ ] **Step 1: Register and convert**

```bash
"$PY" scripts/source.py register inbox/ML25293A458.pdf --key ACRS_ML25293A458 --title "NRC Review of Kemmerer Unit 1 Construction Permit Application, Control of Heat Generation (ACRS Subcommittee, 2025-10-22)" && "$PY" scripts/convert_references.py --only ACRS_ && ls inbox | wc -l
```
Expected: registered, converted, `inbox` empty (`0`). (No `PROFILES` prefix matches `ACRS_`, so only `COMMON` options apply — correct for a slide deck.)

- [ ] **Step 2: Extend the test**

Append to `scripts/refclean/tests/test_generic.py`:
```python
@pytest.fixture(scope="module")
def built_acrs():
    import clean_references as CR
    from refclean.doc import load_doc
    from refclean.emit import render
    from refclean.pdfaux import build_aux
    from refclean.profiles import DOCS, generic
    from refclean.verify import verify
    key = "ACRS_ML25293A458"
    stem = DOCS[key][0]
    if not os.path.exists(os.path.join(RAW, stem + ".json")):
        pytest.skip("ACRS conversion not available")
    doc = load_doc(key, stem, CR.RAW, CR.OUT)
    aux = build_aux(doc.pdf_path, chapter=None, exclude=CR.table_regions(doc))
    aux.meta["render_figures"] = False
    for step in generic.steps():
        step(doc, aux)
    text, failed = CR.apply_patches(key, render(doc, generic.metadata(doc, aux)))
    return text, failed, verify(doc, aux, text)


def test_acrs_deck(built_acrs):
    text, failed, ver = built_acrs
    assert failed == []
    assert 'doc_id: "ML25293A458"' in text and "pdf_pages: 22" in text
    assert text.count("<!-- page ") >= 20          # one anchor per slide that carries text (a blank/cover slide may have none)
    assert "Control of Heat Generation" in text
    assert ver["summary"]["missing_pct"] <= 2.0, ver["summary"]
```

- [ ] **Step 3: Run to see it fail**

Run: `"$PY" -m pytest scripts/refclean/tests/test_generic.py -q 2>&1 | tail -2`
Expected: `KeyError: 'ACRS_ML25293A458'`.

- [ ] **Step 4: Register in `META` and `DOCS`**

`generic.py` `META`:
```python
    "ACRS_ML25293A458": {
        "doc_id": "ML25293A458", "doc_type": "NRC staff presentation (ACRS subcommittee)",
        "issuer": "U.S. Nuclear Regulatory Commission, NRR/DANU/UTB2 (Reed Anzalone)",
        "revision": "", "date": "2025-10-22",
        "title": "NRC Review of Kemmerer Unit 1 Construction Permit Application — Control of Heat Generation",
        "tags": ["reference", "nrc", "acrs", "natrium"], "aliases": ["ACRS Control of Heat Generation slides"],
    },
```
`profiles/__init__.py`: `"ACRS_ML25293A458": ("<exact stem from ls references/raw | grep ACRS_>", "generic", None),`.

- [ ] **Step 5: Build to the gate and test**

```bash
"$PY" scripts/clean_references.py --only ACRS_ML25293A458 --verify | tail -3 && "$PY" -m pytest scripts/refclean/tests/test_generic.py -q 2>&1 | tail -1
```
Expected: exit 0, `missing_pct` ≤ 2.0, `4 passed`. Same escalation rule as Task 11 Step 5 (patch file or a `doc.key`-guarded step; never core). If fewer than 20 anchors appear, list the slides without an anchor (`fitz` page text vs. output) and record the cause in the card's `## 알려진 모순` — do not lower the assertion.

- [ ] **Step 6: Sync, suite, status, log, commit**

```bash
"$PY" scripts/source.py sync ACRS_ML25293A458 && "$PY" scripts/source.py status && "$PY" -m pytest scripts/refclean/tests scripts/tests -q 2>&1 | tail -1
```
Expected: 11 cards listed, `inbox waiting: 0`, `229 passed`.
Update `meta/status.md` (phase: 1 complete → "다음 작업: Phase 2 계획 작성"; 원문 표에 RG_1.233, ACRS_ML25293A458 추가) and append to `log.md`:
```markdown

## [2026-09-14] feat | 대기 원문 2건 등록 (RG 1.233, ACRS ML25293A458)
- `source.py register` → 변환 → generic 프로파일로 정제 → 소스 카드. 누락률: (빌드 값 기입). Phase 1 완료.
```
```bash
git add scripts/refclean/profiles/generic.py scripts/refclean/profiles/__init__.py scripts/refclean/tests/test_generic.py wiki/ACRS_ML25293A458.md meta/status.md log.md && git commit -q -m "feat(pipeline): ACRS ML25293A458 registered and cleaned; phase 1 complete" -m "Co-Authored-By: Claude Fable 5.1 <noreply@anthropic.com>"
```

---

## Self-review notes

- Spec §9.2 items 0.1–0.8 map to Tasks 1–6 (0.5 → Task 4, 0.6 and 0.8 → Task 5). Spec §9.3 items 1.1–1.5 map to Tasks 7–12 (1.5 split into Tasks 11 and 12).
- Spec §3.2 name-clash rule is why Task 8 renames the RG 1.232 stem before Task 10 creates `wiki/RG_1.232.md`.
- Spec §4.2 "판별" (duplicate / revision) is implemented by hash in `source.register`; a revision gets a new key by the caller (`--key RG_1.232_Rev1`), which the design leaves manual.
- `source.py` frontmatter field names (`file, pdf, sha256_pdf, sha256_md, pdf_pages, build, ingest, units`) are the contract Phase 2's lint and ingest skill will read; they match spec appendix B except `adams`, `issuer`, `revision`, `date`, `doc_id`, which live in the cleaned file's frontmatter and are not duplicated on the card.
- Nothing in this plan writes to `references/raw/` except the PDF move in `register`, the converter, and the verify report — consistent with the pipeline contract.
