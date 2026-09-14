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
