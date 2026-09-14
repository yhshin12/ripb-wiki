---
title: ripb vault 재구축 설계
date: 2026-09-14
status: 사용자 검토 대기
decided: 2026-09-11 ~ 2026-09-14 (대화 세션 27c307ef)
supersedes: AGENTS.md (2026-06-12), GEMINI.md, schema/prompt_*.md
---

# ripb vault 재구축 설계

## 0. 요약

`C:\Obsidian\ripb`는 TI-RIPB 원자력 안전해석 분야의 Karpathy식 LLM wiki(Obsidian vault)이다. 2026-05에 Gemini CLI가 만든 wiki 267개 노트를 2026-09-11에 원문과 대조한 결과, 노트의 16 %에 사실 오류가 있었고 23 %는 빈 틀이었으며 출처를 쪽 단위로 밝힌 노트는 4.9 %였다. 원문 표를 기계적으로 옮긴 부분은 정확했고 LLM이 요약·해석·일반화한 부분에 오류가 몰려 있었다.

이에 따라 기존 wiki를 폐기하고(git 이력에만 보존) 기반을 새로 만든 뒤 원문을 다시 인제스트한다(방안 A, 2026-09-11 결정). 관리 주체는 Claude 하나이다. 새 체계의 원칙은 두 가지이다. 원문 사실은 기계적으로 옮기고 위치를 붙인다. 해석은 사실과 분리하고, 옮겨 온 사실만 근거로 쓴다.

원문 정제 파이프라인(`scripts/refclean/`)은 별도 세션이 2026-09-13에 완성하여 커밋 `31f826e`에 있다. 본 설계는 그 파이프라인을 소스 계층으로 그대로 채택한다.

## 1. 배경: 2026-09-11 감사 결과

대상 267개 노트 중 260개를 네 영역으로 나누어 원문과 대조하였다.

| 영역 | 노트 수 | 검증 통과 | 경미(누락·표현) | 사실 오류 |
|---|---|---|---|---|
| Natrium LBE + IE/End State | 31 | 10 | 13 | 8 |
| Natrium SSC + Table 5.2-x | 36 | 4 | 21 | 11 |
| RG 1.232 SFR-DC | 65 | 0 | 63 (빈 틀 62 포함) | 2 |
| NEI 18-04 개념 | 21 | 10 | 10 | 1 |
| 규제·일반 노트 | 131 | 원문 근거 84 / vault 밖 지식 42 / 출처 없음 5 | — | 21 |

근본 원인은 네 가지였다. 출처 표기가 권고에 그쳤다. 링크 대상이 없으면 노트를 만들어도 된다는 규칙이 배경지식 노트와 빈 틀을 낳았다. 커밋 메시지와 산출물이 달라도 걸러 낼 검증 절차가 없었다. 도구(event tree 스크립트의 기본값 결말, 정규식 누락, 인코딩 손상)가 경고 없이 실패했다. 대표 오류 목록은 부록 D에 있다.

## 2. 결정 사항

| ID | 결정 | 일자 |
|---|---|---|
| D1 | 방안 A: 전면 재구축. 기존 wiki는 삭제하고 git bundle에만 보존한다. | 09-11 |
| D2 | vault는 하나, git 저장소는 둘. 내부 자료(H-SFR 설계 문서, 회의록)는 `internal/`에 두고, 이 폴더는 공개 저장소(git #1)가 무시하며 원격 없는 로컬 git #2로 관리한다. | 09-11 |
| D3 | git 이력을 새로 시작한다. 구 `.git`은 bundle로 `internal/_legacy/`에 보관한다. GitHub `yhshin12/ripb-wiki`의 삭제·보관은 사용자가 한다. | 09-11 |
| D4 | 언어: "원문 사실" 절은 영어 원문 표현 + 위치 인용, 요약·해설은 한국어. 문서마다 전문 용어의 첫 등장은 "한국어(영어)". | 09-11 |
| D5 | 용어: 한국어 표기를 추측하지 않고 후보도 제시하지 않는다. 미정 용어는 인제스트 단위마다 모아 한 번에 묻는다. 용어표가 단일 진실 원천이며, 변경 시 스크립트가 모든 노트에 전파한다. | 09-11 |
| D6 | 규제·표준·기관 노트는 vault 원문이 말하는 범위만 담는다. CFR·IAEA 원문은 추가하지 않는다. | 09-11 |
| D7 | 변경 요약 승인 = 커밋 승인. push는 요청 시에만. | 09-11 |
| D8 | 인제스트 순서: 기초 개념 우선 + 시범 단위(NEI 18-04 §3). 부록 A. | 09-11 |
| D9 | `wiki/`는 단일 폴더. 범주는 frontmatter `type`과 파일명 접두어로 표현한다. | 09-13 |
| D10 | 내부 자료 투입구는 `inbox/internal/`. 처리 후 `internal/references/`로 옮긴다. | 09-13 |
| D11 | `references/`(정제본·그림 포함)는 git #1에서 제외한다. 재현성은 PDF SHA-256, 파이프라인, 소스 카드의 빌드 요약으로 확보한다. | 09-14 |
| D12 | `staging/` 폴더를 두지 않는다. 인제스트 상태는 소스 카드의 `ingest` 필드와 `meta/status.md`가 표현한다. 물리적 흐름은 `inbox/` → `references/raw/` 이동 한 번이다. | 09-14 |
| D13 | 소스 ID는 정제 파이프라인의 문서 키(`PSAR_ch03`, `RG_1.232`, `NEI_18-04`)를 쓴다. | 09-13 |

## 3. 디렉터리와 저장소 구조

```
ripb/                            Obsidian vault = git #1 (새 이력, GitHub 비공개)
├── CLAUDE.md                    운영 규칙의 단일 원천 (§8.4)
├── AGENTS.md                    "CLAUDE.md를 따를 것" 한 줄
├── README.md
├── index.md                     build_index.py가 생성. 손으로 고치지 않음
├── log.md                       append_log.py로 추가만 함
├── .gitignore  .gitattributes  .githooks/  .claude/{settings.json, skills/}
├── meta/                        vault 운영 문서 (git 추적)
│   ├── design/                  본 문서
│   ├── status.md                현재 단계, 다음 작업, 미해결 항목
│   ├── terms_state.json         용어표 마지막 동기화 상태
│   ├── lint/YYYY-MM-DD.md       의미 점검 보고
│   ├── metrics.md               표본 재검증 오류율
│   ├── references_cleanup/      정제 파이프라인의 사양·검토·원장 (구 schema/references_cleanup)
│   └── handover/                세션 인수인계 문서
├── inbox/                       (git 제외) 새 원문 투입구
│   └── internal/                (git 제외) 내부 원문 투입구
├── references/                  (git 제외, Obsidian 제외)
│   ├── raw/                     <stem>.pdf, <stem>.json, <stem>.md, _conversion.json, _verify/
│   ├── <stem>.md                정제본 = 인용 대상
│   └── figures/<KEY>/           원문에서 렌더링한 PNG
├── wiki/                        노트 (단일 폴더)
│   ├── Terminology.md           용어표
│   └── assets/                  노트 첨부 파일
├── templates/                   노트 틀 (구 schema/ 대체)
├── scripts/                     refclean/, convert_references.py, clean_references.py, source.py,
│                                lint_wiki.py, verify_quotes.py, sync_terms.py, build_index.py,
│                                append_log.py, session_start.py, audit_sample.py, tests/
└── internal/                    git #1 제외; git #2 (로컬 전용, 원격 없음)
    ├── references/              raw/, <stem>.md, figures/  (같은 파이프라인, --root 인자)
    ├── wiki/                    내부 자료 기반 노트 (파일명 접두어 HSFR_)
    ├── meetings/                회의록 (구 conversations/)
    ├── log.md  status.md        내부 작업 기록
    └── _legacy/                 구 .git bundle, 구 raw/ 압축본, 구 log
```

### 3.1 단일 폴더 wiki (D9)

Obsidian의 링크·검색·그래프·Bases는 파일명과 속성으로 동작하므로 폴더는 탐색기 표시만 바꾼다. 폴더는 노트마다 범주를 하나만 고르게 강제하지만 실제 노트는 여러 범주에 걸친다(RG 1.232는 원문이자 규제, `Natrium_SSC_RAC`는 Natrium이자 계통). 한 폴더에서는 파일 시스템이 이름 중복을 막아 주므로 `[[Plant]]` 같은 짧은 링크가 모호해지지 않는다. Claude의 탐색도 폴더 경로 대신 접두어·`type`·`index.md`로 이루어진다. 폴더는 기계적 경계가 필요한 곳(`internal/`, `wiki/assets/`, `meta/`)에만 둔다. 범주별 보기는 `type`으로 거르는 Bases 보기가 맡는다.

### 3.2 파일명

- 영어 `Snake_Case`, ASCII만 쓰며 vault 전체(`wiki/`, `internal/wiki/`)에서 유일하다.
- 설계 특정 노트는 `Natrium_`, `HSFR_` 접두어를 붙인다.
- 소스 카드는 문서 키로 짓는다: `NEI_18-04`, `RG_1.232`, `PSAR_ch03`.
- wiki 파일명은 `references/`·`internal/references/`의 파일명과 달라야 한다(링크 모호성 방지). 현재 `RG_1.232.md`가 충돌하므로 Phase 1에서 PDF 이름을 `RG_1.232_Guidance for Developing Principal Design Criteria for Non-Light-Water Reactors.pdf`로 바꾸고 재변환한다(NEI와 같은 `<KEY>_<title>` 형식).
- 인코딩은 UTF-8(BOM 없음), 줄 끝은 LF.

### 3.3 git과 보안

| 저장소 | 추적 | 제외 |
|---|---|---|
| git #1 (`ripb/`) | CLAUDE.md, meta/, wiki/, templates/, scripts/, .claude/, .obsidian/(workspace 제외), index.md, log.md | `inbox/`, `references/`, `internal/`, `docs/superpowers/`, `.obsidian/workspace*.json`, `.obsidian/graph.json`, `*.pyc`, `__pycache__/` |
| git #2 (`internal/`) | references와 압축본을 제외한 전부 | `references/`, `_legacy/*.zip` (크기). bundle은 추적 |

- git #1의 log·status·노트에는 내부 문서의 이름조차 쓰지 않는다. 공개 노트는 `[[HSFR_…]]`로 링크하지 않는다. 내부 노트가 공개 노트로 링크하는 것은 허용한다. lint가 검사한다.
- `.gitattributes`: `* text=auto eol=lf`, PNG·PDF는 binary.
- 두 저장소 모두 `core.hooksPath=.githooks`로 pre-commit 관문을 둔다.
- push는 요청 시에만 한다.

### 3.4 Obsidian 설정

- `app.json`의 `userIgnoreFilters`: `inbox/`, `references/`, `internal/references/`, `internal/_legacy/`.
- Shell Commands 플러그인에 용어 동기화(dry-run·apply), lint, index 재생성을 등록한다.
- Bases 보기 4종(`meta/views/*.base`): type별, status별, `disputed` 목록, 미정 용어를 쓰는 노트(`terms_pending`).

## 4. 소스 파이프라인과 데이터 흐름

### 4.1 파이프라인 (2026-09-13 완성분 채택)

`scripts/convert_references.py`(PDF → JSON·MD, opendataloader-pdf, JDK 17 필요) → `scripts/clean_references.py` + `scripts/refclean/`(핵심 8모듈, 문서 프로파일, 패치 파일) → `references/<stem>.md` + `references/figures/<KEY>/`. 계약과 관례는 `meta/references_cleanup/cleanup_review_2026-09-11.md`(결정 D1–D7 블록)와 인수인계 문서에 있다. 본 설계와 무관하게 유지되는 규칙은 다음과 같다.

- 정제본과 그림은 생성물이다. 손으로 고치지 않는다. 수정은 `profiles/<doc>.py` 또는 `patches/<KEY>.json`을 거쳐 재빌드한다.
- `references/raw/`는 읽기 전용이다. `_verify/`만 빌드가 쓴다.
- 원문 오기를 교정하지 않는다(파일별 금지 목록: `meta/references_cleanup/file_reviews/`).
- 수용 관문은 `--verify`와 `pytest scripts/refclean/tests` 둘 다이다(2026-09-14 기준 217건; 원문을 읽는 테스트는 `refs` marker가 붙어 원문이 없는 clone에서 skip된다). 누락률은 회귀 탐지용이지 완전성 증명이 아니다.

정제본 형식 중 인용에 쓰이는 요소:

| 요소 | 형식 |
|---|---|
| 쪽 표지 | `<!-- page 13 \| 5.2-9 -->` (PDF 쪽 \| 인쇄 쪽). 여러 쪽 표는 `<!-- page 12-16 \| 5.2-8..5.2-12 -->`. RG 1.232는 레코드 안에서 표지가 되돌아간다 |
| 제목 | 번호 절은 성분 수가 수준(`## 4.1`, `### 4.2.1`) |
| 레코드 | RG 1.232 부록 기준 `#### SFR-DC 4 — <title>`(ID 블록 `^sfr-dc-4`, Status, Source, Criterion text, NRC rationale). PSAR ch5 PSF `#### DL3-RC1 — <function>`(LBE 목록, SSC·SRDC 표) |
| 편집 표시 | `[!withheld]`, `[!figure]`, `<!-- source: -->`, `<!-- header row supplied -->`. 인용 검증은 이들을 원문 텍스트에서 제외한다 |
| 각주 | `[^n]` (RG 1.232 14개, NEI 18-04 16개) |

### 4.2 데이터 흐름 (D10, D12)

```
[사용자] inbox/            공개 원문          [사용자] inbox/internal/     내부 원문
            │                                             │
            │  source.py register                         │  source.py register --root internal
            │  · SHA-256으로 중복본·개정판 판별            │
            │  · 파일명 정규화(<KEY>_<title>.pdf)          │
            │  · references/raw/로 이동                    │
            │  · 소스 카드 생성 (ingest: pending)          │
            ▼                                             ▼
references/raw/<stem>.pdf                       internal/references/raw/<stem>.pdf
            │  convert → profile 등록 → clean → verify + pytest
            ▼
references/<stem>.md (+ figures/)               internal/references/<stem>.md
            │  wiki-ingest: 단위별 승인·커밋, 진행표는 소스 카드 안에
            ▼
wiki/ (소스 카드 ingest: complete)              internal/wiki/
```

- **감지:** 세션 시작 보고에 대기 건수와 진행 현황을 싣는다. "ingest"라고만 지시하면 진행 중인 원문을 먼저 잇고, 그다음 대기 목록을 부록 A 순서로 처리한다.
- **판별:** 기존 원문과 해시가 같으면 중복본으로 보고하고 인제스트하지 않는다. 개정판은 새 키(개정 번호 포함)를 받는다. 기존 노트의 인용은 구판 기준으로 유효하며, 대체된 사실은 인제스트 때 표시한다.
- **형식:** PDF는 쪽 단위 인용. 쪽 개념이 없는 원문(Markdown 회의록 등)은 `[KEY §제목경로]`로 인용한다. HWP·XLSX 등은 처음 들어올 때 변환 방식을 사용자에게 묻는다.
- **완료:** 마지막 단위의 커밋에서 소스 카드를 `ingest: complete`로 바꾼다.
- **불변 조건(lint):** `references/`의 모든 정제본에는 소스 카드가 있다. `ingest: complete`인 카드의 파일은 존재하고 SHA-256이 카드와 같다.

## 5. 노트 작성 규칙과 인용 형식

### 5.1 노트 틀

```markdown
---
type: concept          # source | regulation | concept | natrium | synthesis | map | hsfr
aliases: [LBE]
sources: [NEI_18-04]   # 소스 카드 키
status: draft          # draft → checked → reviewed; 필요 시 disputed · deprecated
verified:              # checked가 된 날짜
term:                  # 개념 노트가 대표하는 용어 ID (선택)
tags: []
terms_pending: []      # sync_terms.py가 유지: 이 노트의 미정 용어 표지 ID
---
# 한국어 제목 (English Title)

> [!abstract] 요약
> 한국어 2–3문장

## 원문 사실
- "<원문 문장 그대로>" [NEI_18-04 §3.2.1 p.16]

| 항목 | 값 | 출처 |
|---|---|---|
| <원문 표 셀> | <값> | [NEI_18-04 Table 3-1 p.16] |

## 해설
한국어. '원문 사실' 절의 항목만 근거로 삼는다.

## 관련 문서
- [[존재하는 노트만]]
```

### 5.2 인용 형식 (D13)

| 대상 | 형식 | 예 |
|---|---|---|
| 절 | `[KEY §절 p.N]` | `[PSAR_ch03 §3.7.3.1 p.45]` |
| 표·그림 | `[KEY Table x p.N]`, `[KEY Figure x p.N]` | `[PSAR_ch05 Table 5.2-1 p.12]` |
| 레코드 | `[KEY <레코드 ID> p.N]` | `[RG_1.232 SFR-DC 4 p.64]`, `[PSAR_ch05 DL3-RC1 p.12]` |
| 쪽 범위 | `p.N-M` | `[NEI_18-04 §3.2.1 p.16-17]` |
| 쪽 없는 원문 | `[KEY §제목경로]` | `[HSFR_MTG_2026-05-22 §반응도 LBE]` |

`p.N`은 PDF 쪽(쪽 표지의 첫 번호)이다. 인쇄 쪽은 사람이 PDF를 열 때 참고용이며 인용에는 쓰지 않는다.

### 5.3 원문 사실 절의 규칙

- 의역을 두지 않는다. 원문 문장(따옴표)이나 표 값만 쓴다. 긴 문단은 `...`로 줄인다.
- 문장·표 행마다 인용을 붙인다.
- 원문끼리 모순되면 두 사실을 모두 인용한 채 `status: disputed`로 표시한다. 한쪽을 덮어쓰지 않는다.

### 5.4 기계 검사 (`lint_wiki.py`, `verify_quotes.py`)

1. 원문 사실 절의 모든 항목에 인용 표기가 있다.
2. 소스 키가 소스 카드로 존재하고, 쪽 번호가 그 문서의 쪽 범위 안에 있다.
3. 따옴표 안 문장이 인용한 쪽(±1쪽; 범위 표지와 RG의 비단조 표지는 N을 포함하는 모든 표지 구간)의 정제본 텍스트에 그대로 있다. 공백은 정규화하고, Markdown 문법·편집 주석·callout 표시는 제거한 텍스트와 비교하며, `...`로 나뉜 조각은 따로 검사한다.
4. 원문 사실 표의 값이 인용한 쪽에 있다.
5. 해설 절의 모든 수치가 원문 사실 절에도 있다.
6. 해설의 용어·약어가 용어표에 등록되어 있고 표지가 붙어 있다(§6).
7. 구조: frontmatter 필드, 필수 절, H1, 파일명 규칙, 인코딩(BOM·U+FFFD), 자리표시자 없음, 링크 대상 존재, Markdown 링크 없음, 고아 노트, index 반영, alias 충돌, 공개 노트의 내부 링크 없음.

### 5.5 status

| 값 | 조건 |
|---|---|
| `draft` | 작성 중 |
| `checked` | 검사 1–7 통과, 변경 요약 승인, 커밋됨 |
| `reviewed` | 사용자가 해당 노트를 직접 읽고 확인했다고 지시한 경우에만 |
| `disputed` | 원문 간 모순 또는 사용자 이의. 해소될 때까지 유지 |
| `deprecated` | 개정판으로 대체됨. 링크는 유지, index에서 별도 표시 |

### 5.6 기타

- vault에 원문이 있는 문서는 소스 카드(`type: source`)가 곧 그 문서의 노트다. 원문이 없는 규제는 `type: regulation`으로 만들되 vault 원문이 그 규제를 언급하는 곳만 담는다(D6).
- 존재하지 않는 노트로 링크하지 않는다. 필요한 주제는 lint 보고의 "누락 주제"에 기록한다.
- 그림은 원문에서 렌더링한 PNG만 쓴다. LLM이 재구성한 도식은 `synthesis` 노트에서만 허용하며 "재구성"이라고 표시하고 요소마다 출처를 붙인다.
- 저장 기준(구 규칙 유지): 반복 재사용, 인계 필요, 결정 근거 추적, 실패 방법 기록, 팀 공통 규칙 중 하나 이상을 만족하는 답만 `synthesis` 노트로 저장한다.

## 6. 용어 관리 (D4, D5)

### 6.1 용어표 `wiki/Terminology.md`

| ID | English | 약어 | 한국어 | 이후 표기 | 금지 표기 | 정의 출처 | 상태 | 비고 |
|---|---|---|---|---|---|---|---|---|
| LBE | Licensing Basis Event | LBE | (사용자 입력) | 약어 / 한국어 | (선택) | `[NEI_18-04 §… p.N]` | 미정 / 확정 / 영어 유지 / 용어 아님 | |

- ID는 표지가 가리키는 고정 키다. 같은 약어가 문서마다 다른 뜻이면 ID로 구분한다(예: Natrium의 AST = Anticipatory Automatic Seismic Trip).
- 정의 출처는 원문 약어표(PSAR 1장)나 용어집(NEI 18-04)을 우선한다.
- 표는 빈 상태로 시작한다. 구 vault의 강제 규칙 3건(중대 사고, 소듐, 나트륨)은 첫 질문 묶음에 "구 규칙" 표시로 올리고 사용자가 다시 정한다.
- 사용자는 Obsidian에서 셀을 직접 고친다.

### 6.2 노트 속 표지

한국어 절(요약, 해설, 표의 한국어 셀)에만 붙인다. 원문 사실 절은 건드리지 않는다.

```
편집 화면: 〈한국어〉(Licensing Basis Event)%%t:LBE%%는 … 이후 LBE%%t:LBE%%는 …
읽기 화면: 〈한국어〉(Licensing Basis Event)는 … 이후 LBE는 …
```

`sync_terms.py`의 동작:

- 문서마다 첫 표지는 "한국어(English)"로, 나머지는 "이후 표기"로 다시 쓴다. H1은 첫 등장에서 제외한다.
- 한국어 표기의 마지막 음절 받침 유무가 바뀌면 표지 바로 뒤의 조사(은/는, 이/가, 을/를, 과/와, 으로/로)를 함께 고친다. 약어는 마지막 글자의 한국어 읽기로 판단한다.
- `term:` 필드가 있는 개념 노트는 제목과 한국어 alias도 갱신한다.
- 대상은 `wiki/`와 `internal/wiki/` 전체. 기본은 dry-run, `--apply`로 쓴다.

### 6.3 일괄 질문

1. 인제스트 단위에서 용어 후보를 추린다(원문 약어표·용어집 항목, 한국어 절에 쓸 전문 용어).
2. 용어표에 `미정` 행을 추가한다. 한국어 칸은 비워 둔다.
3. 채팅에 번호 목록으로 묻는다. 항목은 English, 약어, 원문 정의 인용(위치 포함)만 싣고 번역 후보는 싣지 않는다. 사용자의 답은 한국어 표기, "영어 유지", "용어 아님" 중 하나다. 채팅으로 답하거나 용어표를 직접 고친다.
4. 답을 받은 뒤 노트를 쓴다. 답이 없는 용어는 영어로 쓰고 표지만 달아 둔다.

### 6.4 변경 전파와 검사

- 용어표의 마지막 동기화 상태를 `meta/terms_state.json`에 둔다. 세션 시작 시와 답변 반영 직후 비교한다.
- 변경이 있으면 `sync_terms.py`를 실행하고, 바뀐 용어와 갱신된 노트 목록을 요약하여 승인 후 커밋한다.
- lint: 표지 ID가 용어표에 있는가, 표기가 일치하는가, 금지 표기가 없는가, 등록된 한국어 용어가 표지 없이 쓰인 곳은 없는가(경고).

## 7. 운영 절차

### 7.1 세션 시작

SessionStart hook이 `session_start.py`를 실행하여 다음을 한 번에 보고한다: `meta/status.md`, log 최근 항목, 두 저장소의 `git status`, 용어표 변경 여부, `inbox/` 대기 건수와 진행 현황, 구조 lint 결과. 사용자가 Obsidian에서 직접 고친 노트가 있으면 lint를 실행해 결과를 보고하고, 인용 규칙과 어긋난 곳을 알린다. 처리 여부는 사용자가 정한다.

### 7.2 인제스트 (원문 1단위: 절 묶음 또는 장)

| 단계 | 내용 |
|---|---|
| 0. 준비 | 정제본과 소스 카드가 있는지 확인한다. 없으면 §4.2대로 만든다. |
| **1. 계획 + 용어 질문 (접점 ①)** | 절 범위, 만들거나 고칠 노트 목록(제목·type), 미정 용어 목록을 한 메시지로 제시한다. |
| 2. 작성 | 원문 사실 → 해설 → 링크 순. 기존 노트에 새 원문의 사실을 더할 때는 새 인용을 붙인다. |
| 3. 검사 | lint, 인용 검증, 용어 동기화. 실패는 고친 뒤 다시 검사한다. 해소하지 못한 항목은 요약에 적는다. |
| **4. 변경 요약 (접점 ②)** | 새 노트·고친 노트 목록(한 줄 요약), 검사 결과, 원문 간 모순, 누락 주제, 남은 미정 용어, 사용자가 직접 볼 핵심 노트 2–3개. |
| 5. 승인 → 커밋 | log 추가, index 재생성, 커밋. 커밋된 노트는 `checked`. 반려되면 고쳐서 4단계부터. |

큰 장(PSAR 7장 등)은 추출·대조를 서브에이전트에 나눠 맡기고 노트는 본 세션이 쓴다.

### 7.3 질의

`index.md` → 관련 노트 → 필요 시 정제본 순으로 확인한 뒤, 노트 링크와 원문 위치를 붙여 답한다. vault에 없는 내용은 "vault에 없음"이라고 쓰고, 원문에는 있으나 노트에 없는 경우 그 사실을 밝힌다. 저장 기준(§5.6)을 통과한 답은 `synthesis` 노트로 저장을 제안한다. 질의 중 발견한 노트 오류는 즉시 보고하고 수정은 별도 승인을 받는다.

### 7.4 점검

| 종류 | 시점 | 내용 |
|---|---|---|
| 기계 검사 | 편집마다(hook), 커밋 전(pre-commit) | §5.4 |
| 의미 점검 | 원문 1건 인제스트 완료 시 | 노트 간 모순, 중복, 누락 주제, 새 원문 때문에 낡아진 서술. `meta/lint/YYYY-MM-DD.md` |
| 표본 재검증 | 원문 2건 완료 시 | `checked` 노트 10개를 무작위로 골라 서브에이전트가 원문과 대조. 오류율을 `meta/metrics.md`에 기록. 오류가 나오면 노트와 원인이 된 규칙·도구를 함께 고친다 |

### 7.5 기록

- `log.md`: 작업 1건당 항목 1개. 원문 범위, 새 노트·고친 노트 수, 검사 결과, 미정 용어 수. 항목은 그 작업의 커밋에 함께 들어가므로 커밋 해시는 적지 않는다(`git log -- log.md`로 찾는다).
- `internal/log.md`, `internal/status.md`: 내부 자료 작업은 여기에만 기록한다.
- `index.md`: `build_index.py`가 `type`과 요약 첫 문장으로 재생성한다.
- `meta/status.md`: 인제스트마다 갱신. 현재 단계, 다음 작업, 미해결 항목(`disputed`, 미정 용어, 누락 주제).

## 8. 도구와 자동화

### 8.1 스크립트

| 스크립트 | 역할 | 비고 |
|---|---|---|
| `convert_references.py`, `clean_references.py`, `refclean/` | 원문 정제 (§4.1) | 기존. `--root` 인자(internal용)만 추가 |
| `source.py register \| adopt \| sync \| finish \| status` | 등록(해시, 정규화, 이동, 소스 카드), 기존 원본의 카드 생성, 빌드 요약 반영, 완료 처리, 현황 | PDF는 `inbox/`에서 `references/raw/`로 옮기기만 하고 내용은 바꾸지 않는다 |
| `lint_wiki.py` | §5.4의 7과 §6.4 검사, `references/` 불변 조건 | 신규. 파일 1개 또는 전체 |
| `verify_quotes.py` | §5.4의 1–5 | 정제본 기준 |
| `sync_terms.py` | §6.2, §6.4 | dry-run 기본 |
| `build_index.py` | `index.md` 재생성 | |
| `append_log.py` | log 항목 추가 | 파일 전체를 다시 쓰지 않는다 |
| `audit_sample.py` | 표본 10개 추출과 대조 프롬프트 생성 | |
| `session_start.py` | §7.1 보고 | hook이 호출 |
| `notes.py`, `citations.py`, `terms.py` | 노트 입출력, 인용 구문·쪽 분할·정규화, 용어표·표기·조사 | 보조 모듈 |
| `leak_guard.py`, `hook_post_edit.py` | 공개 커밋의 내부 문서명 검사, PostToolUse 진입점 | hook이 호출 |

공통: 파이썬은 `C:\Code\Python\pykaeri\.venv12\Scripts\python.exe`. 일괄 수정은 dry-run 기본. 어떤 스크립트도 `inbox/`, `references/raw/`의 파일 내용을 바꾸지 않는다(`source.py register`의 이동과 빌드의 `_verify/` 기록만 예외). 검사 실패는 0이 아닌 종료 코드로 보고한다. 파일을 쓸 때는 문자열을 검증한 뒤에만 쓴다(정제 세션의 `verify.py` 손실 사례).

### 8.2 Hook

| 시점 | 동작 |
|---|---|
| Claude SessionStart | `session_start.py` |
| Claude PostToolUse (Edit·Write, `wiki/**/*.md`, `internal/wiki/**/*.md`) | 해당 파일에 `lint_wiki.py`, `verify_quotes.py`. 1초 안에 끝나도록 파일 단위 |
| git pre-commit (두 저장소) | 전체 lint, 인용 검증, index 최신 여부, 공개 저장소에 내부 문서명·`internal/` 경로 없음. 실패 시 거부 |

### 8.3 Skill

| Skill | 호출 | 내용 |
|---|---|---|
| `wiki-ingest` | "ingest", 시작 보고의 대기 건 | §4.2, §7.2 전체. 용어 질문·변경 요약 템플릿 포함 |
| `wiki-terms` | 답변 직후, "용어 반영" | 용어표 기록 → `sync_terms.py` → 승인·커밋 |
| `wiki-query` | 질문 | §7.3 |
| `wiki-lint` | 원문 1건 완료, "lint" | §7.4 의미 점검 |
| `wiki-audit` | 원문 2건 완료, "audit" | §7.4 표본 재검증. 2026-09-11 감사의 서브에이전트 프롬프트를 표준화 |

### 8.4 CLAUDE.md 구성

규칙과 경계만 담고 절차는 skill에 둔다. 사람이 읽는 본문은 한국어, 경로·명령·식별자는 영어.

1. 역할: Claude 단독 관리, 원문 우선, 빈 틀 금지, 용어 추측 금지
2. 구조와 데이터 흐름 (§3, §4.2 요약)
3. 정제 파이프라인 계약 (인수인계 문서 §3–4의 7개 항목 그대로)
4. 노트 규칙과 인용 형식 (§5)
5. 용어 규칙 (§6 요약)
6. 승인 규칙: 접점 ①②, 내용 승인 = 커밋 승인, push는 요청 시
7. 도구: 파이썬 경로, 스크립트 표, hook·skill 목록
8. 보안: git 제외 목록, `internal/` 규칙, 공개 기록에 내부 문서명 금지

### 8.5 템플릿 (`templates/`)

`note.md`, `source_card.md`(부록 B), `term_question.md`, `change_summary.md`.

### 8.6 테스트

`scripts/tests/`의 고정 노트로 테스트를 먼저 쓰고 구현한다. 필수 사례: `verify_quotes.py`의 일치·불일치·쪽 경계·범위 표지·비단조 표지·편집 주석 제외, `sync_terms.py`의 받침 변화에 따른 조사 보정과 첫 등장 규칙, `lint_wiki.py`의 `references/` 불변 조건과 내부 링크 금지, `source.py`의 중복본·개정판 판별, `leak_guard.py`의 내부 문서명 검출, `build_index.py --check`, `append_log.py`의 추가 전용 쓰기.

## 9. 전환 단계

### 9.1 착수 조건

정제 세션(`ripb-c0`)이 닫혔거나 더 이상 파일을 쓰지 않는다는 것을 사용자가 확인한다. 그전에는 `references/`, `scripts/refclean/`, `scripts/clean_references.py`, `scripts/convert_references.py`, `meta/references_cleanup/`(현 `schema/references_cleanup/`), `AGENTS.md`, `log.md`를 건드리지 않는다.

### 9.2 Phase 0: 안정화와 이력 재시작 (1세션)

표시한 확인 지점마다 사용자 확인을 받은 뒤 실행한다.

| 순서 | 작업 | 확인 |
|---|---|---|
| 0.1 | 구 이력에 최종 스냅숏을 커밋한다: 현재 미커밋 변경 전부(정제 세션의 log·인수인계 문서, Gemini 시기 잔여물, `.obsidian/` 변경). `references/`, `raw/`, `inbox/`는 제외되어 있다. | 확인 |
| 0.2 | `git bundle create internal/_legacy/ripb-before-rebuild.bundle --all`, `git bundle verify`. | |
| 0.3 | 구 `raw/`(2.7 MB)를 `internal/_legacy/raw-gemini.zip`으로 압축. RG 1.233 PDF는 `inbox/`로. 압축 후 `raw/` 삭제. `inbox/`의 RG 1.232 중복본은 해시 재확인 후 삭제. | 확인 |
| 0.4 | 삭제: 구 wiki(노트 267개, assets 28개), `.gemini/`, `.antigravitycli/`, `GEMINI.md`, 루트 `index.md`, 구 스크립트 8개(`batch_create_sfrdc`, `draw_eta`, `extract_psar`, 구 `lint_wiki`, `patch_underlines`, `process_all_pdfs`, `wiki_utils`, `validate-template.sh`), `schema/`의 템플릿·프롬프트. 이동: `schema/references_cleanup/` → `meta/references_cleanup/`, `conversations/` 회의록 2건 → `internal/meetings/`, 인수인계 문서 → `meta/handover/`, 구 `log.md` → `internal/_legacy/log-before-rebuild.md`. | 확인 |
| 0.5 | `.gitignore`, `.gitattributes`, `.githooks/`(자리), `internal/` 생성과 `git init`(git #2). | |
| 0.6 | CLAUDE.md 작성, AGENTS.md 축소, `meta/status.md`, 새 `log.md`(첫 항목에 bundle 위치 기록). | |
| 0.7 | `.git` 삭제 → `git init` → 첫 커밋(작업 트리는 그대로). GitHub 구 저장소의 삭제·보관은 사용자가 한다. 새 원격 URL을 받으면 요청 시 push. | 확인 |
| 0.8 | `.obsidian/app.json`의 `userIgnoreFilters` 갱신(§3.4). | |

### 9.3 Phase 1: 소스 계층 정합 (1–2세션)

| 순서 | 작업 |
|---|---|
| 1.1 | `convert_references.py`, `clean_references.py`에 `--root` 인자 추가. 기존 테스트 211건 통과 유지. |
| 1.2 | `source.py` 구현(테스트 포함). |
| 1.3 | RG 1.232 PDF 이름 변경(§3.2)과 재변환·재빌드·검증. |
| 1.4 | 정제본 9건의 소스 카드 작성(정제본 frontmatter와 `_verify/` 요약에서 서지·쪽 수·SHA-256·누락률을 가져옴). `ingest: pending`. |
| 1.5 | `inbox/`의 ACRS 슬라이드(ML25293A458, 22쪽)와 RG 1.233(31쪽)을 등록·변환·정제. 프로파일은 각각 신규(RG 1.233은 RG 1.232 프로파일 기반). |

### 9.4 Phase 2: 도구 (2–3세션)

§8의 스크립트 7종(신규), 템플릿 4종, 빈 용어표, hook 3종, skill 5종, Shell Commands 등록, Bases 보기 4종. §8.6대로 테스트 우선.

### 9.5 Phase 3: 시범 인제스트와 본 인제스트

- 시범: NEI 18-04 §3(LBE 정의, 빈도 구분, F-C Target) 1단위를 §7.2 전체로 수행하고, 템플릿·인용 검증·용어 질문·변경 요약·hook을 점검하여 CLAUDE.md와 skill을 보정한다.
- 본 인제스트: 부록 A 순서. 원문 1건마다 의미 점검, 2건마다 표본 재검증.

### 9.6 Phase 4: 운영

§7의 절차를 반복한다. 지표는 §10.

## 10. 지표

| 지표 | 현재(구 wiki) | 목표 |
|---|---|---|
| 주장 단위 인용을 갖춘 노트 비율 | 4.9 % | 100 % (synthesis 제외) |
| 깨진 링크 / 인코딩 손상 / 빈 틀 | 136 이상 / 4 / 62 | 0 / 0 / 0 |
| 표본 재검증 사실 오류율 | 16 % | 첫 측정 후 설정 |

비용 추정(2026-09-11, Opus 5 정가 기준): 세션당 $10–20, 총 28–33세션(기반 4–6 + 인제스트 22–27), 사용자 검토 9–16시간. 정제 파이프라인이 완성되어 기반 부분은 하한에 가깝다.

## 11. 위험

| 위험 | 대응 |
|---|---|
| 정제 세션과의 동시 편집 | §9.1 착수 조건 |
| 이력 재시작 뒤 복구 필요 | `git clone ripb-before-rebuild.bundle`로 언제든 구 이력 복원. 0.2에서 검증 |
| 줄 끝 혼재 | `.gitattributes`와 첫 커밋의 재정규화 |
| 중첩 저장소 | git #1이 `internal/`을 무시한다. lint가 git #1 추적 목록에 `internal/` 경로가 없음을 검사 |
| 정제본 재생성 시 인용 무효화 | 쪽 표지는 PDF 쪽이므로 정제 규칙이 바뀌어도 변하지 않는다. 소스 카드의 SHA-256이 바뀌면 인용 검증을 전체 재실행한다 |
| 다른 PC에서의 작업 | `references/`가 git에 없으므로 PDF를 옮기고 한 번 빌드해야 한다(JDK 17, 약 2분) |
| 세션 한도로 서브에이전트 중단 | 정제 세션의 경험대로 SendMessage로 재개하고, 문서별 파일 소유권을 나눈다 |

## 부록 A. 인제스트 순서 (D8)

1. NEI 18-04 §3 (시범)
2. NEI 18-04 나머지
3. RG 1.233
4. RG 1.232 (SFR-DC 65개 레코드는 스크립트로 추출; 삭제된 27은 삭제 표시)
5. PSAR 1장 (약어표 → 용어표 초기 질문)
6. PSAR 5장
7. PSAR 3장
8. PSAR 6장, 7장
9. PSAR 4장, 11장
10. ACRS 슬라이드 ML25293A458
11. H-SFR 내부 자료 (`inbox/internal/`)

새로 들어온 원문은 목록 끝에 붙는다.

## 부록 B. 소스 카드 필드

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

## 부록 C. 참조 문서

- 정제 파이프라인 인수인계: `meta/handover/2026-09-14_handover_references_cleanup.md` (Phase 0 이전 경로: `conversations/`)
- 정제 사양·검토·원장: `meta/references_cleanup/` (Phase 0 이전 경로: `schema/references_cleanup/`)
- 2026-09-11 감사의 상세 결과: 세션 27c307ef 대화 기록. 요약은 부록 D.

## 부록 D. 구 wiki의 대표 오류 (재인제스트 시 확인 목록)

원문을 다시 읽을 때 특히 확인할 곳이다. 아래는 구 wiki가 틀렸던 사실이며, 원문 대조로 확인된 것이다.

- 안전등급: IHT(DL3-HR3·HR12), FHP, RXB 하부구조, FHB 하부구조는 SR 기능을 가진다. 구 wiki는 NSRST로 적었다. [PSAR_ch05 Table 5.2-2, PSAR_ch06 §6.4.2, PSAR_ch07 §7.8.2]
- 약어: NSS = Nuclear Island Salt System(구: Nuclear Steam Supply). HAA = Head Access Area(구: Heat Exchanger Auxiliary Area). AST = Anticipatory Automatic Seismic Trip System(구 Map: Alternative Shunt Trip). NUP = NI Uninterruptible AC Power Supply System(구: Non-Class 1E). RAC = Reactor Air Cooling System(구 LOOP 요약: 격납건물 냉각). [PSAR_ch01 약어표]
- F-C Target은 수용·불수용의 경계가 아니다(구: "선 위는 수용 불가"). [NEI_18-04 §3.2.1, Task 7a]
- SFR-DC 70은 조건부("If an intermediate cooling system is provided")다(구: 의무 요건). RG 1.232 Appendix B는 65개 기준이며 27은 삭제됨(구: 62개 + 25·73·78 누락, 27을 유효로 표시).
- DBA(-CN) 시퀀스에는 방벽 성공을 부여하지 않는다(구 CGR·ISPL 노트). Table 5.2-3 Note 1의 -CN ID는 DBE가 아니다.
- 핵연료취급 LBE(FDBL·FDEM·FDPI·FDIV)의 사건표에는 -2 이후 시퀀스도 있다(구: 첫 시퀀스만).
- Event tree 그림 27개는 원문 그림이 아니었다. PSAR ch3에는 Figure 3.5-1만 있다.
- BDBE 하한은 5E-07/plant-yr(구 Cliff_Edge 노트: 1E-07). QHO는 5E-07(1마일)·2E-06(10마일).
- RA-S-1.4-2021을 승인한 것은 RG 1.247(trial)이다(구: RG 1.200). [PSAR_ch03 §3.1.1.1]
- Kemmerer Unit 1은 단일 원자로 부지다(구: 다중 모듈 예시). [PSAR_ch03 §3.1.1.4]
- LMP는 "led by nuclear utilities and supported by DOE"다(구: NEI 주도·NRC 협업). [RG 1.233 p.8]
- PSAR ch3의 Table 3.5-2는 RRS-ISPL-BL을 "RAB Barrier Fails to Retain Release"로, §3.7.3.3 제목은 "Successfully Retains"로 적는다. 원문 자체의 모순이며 `disputed`로 기록한다.
- 구 규칙의 번역 3건(중대 사고, 소듐, 나트륨)은 사용자가 다시 정한다. 기존 노트에도 "나트륨 공기 냉각 계통", "나트륨 냉각 고속로"처럼 규칙 위반이 있었다.
