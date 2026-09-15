---
updated: 2026-09-15
phase: 3
---
# 상태

## 현재 단계
Phase 3 인제스트 진행 중. NEI 18-04 §3·§4·§5 전체 완료(노트 26개, 소스 카드 단위 7개, 2026-09-15). §6 용어집 확인과 finish가 남았다. 도구 계획: `meta/design/2026-09-14-rebuild-plan-phase2.md`.

## 존재하는 도구
- 정제: `scripts/convert_references.py`, `scripts/clean_references.py`, `scripts/refclean/` (psar·nei1804·rg1232·generic 프로파일, 공용 `levels.py`)
- 원문: `scripts/source.py` (`register`/`adopt`/`sync`/`finish`/`status`)
- 검사: `scripts/lint_wiki.py` (파일 단위 L01–L20, `--all` L30–L36), `scripts/verify_quotes.py` (V1–V5)
- 변경: `scripts/sync_terms.py` (dry-run 기본), `scripts/build_index.py` (`--check`), `scripts/append_log.py`
- 보고: `scripts/session_start.py`, `scripts/audit_sample.py`
- 보조: `scripts/notes.py`, `scripts/citations.py`, `scripts/terms.py`, `scripts/leak_guard.py`, `scripts/hook_post_edit.py`
- 생성물·설정: `index.md`, `internal/index.md`, `wiki/Terminology.md` (빈 표), `meta/terms_state.json`, `templates/` (source_card, note, term_question, change_summary), `.claude/settings.json`, `.claude/skills/` (wiki-ingest, wiki-terms, wiki-query, wiki-lint, wiki-audit), `meta/views/*.base` (Bases 보기 4종), Obsidian Shell Commands 4종
- 관문: git pre-commit(두 저장소: 경로, `[[HSFR_`, 내부 문서명, lint, 인용 검증, index), git commit-msg(내부 문서명), Claude SessionStart·PostToolUse hook (2026-09-15 동작 확인)
- 테스트: 390건 (`python -m pytest scripts/refclean/tests scripts/tests -q`; 원문을 읽는 109건은 `refs` marker)

## 원문
| 키 | 정제본 | 소스 카드 | ingest |
|---|---|---|---|
| PSAR_ch01, ch03, ch04, ch05, ch06, ch07, RG_1.232, NEI_18-04 | 있음 (2026-09-13 빌드 (RG_1.232, PSAR_ch04는 2026-09-14 재빌드)) | 있음 (`wiki/<KEY>.md`) | pending |
| PSAR_ch11 | 있음 (2026-09-14 재빌드, 출력 동일) | 있음 | pending |
| RG_1.233 | 있음 (2026-09-14 빌드) | 있음 (`wiki/RG_1.233.md`) | pending |
| ACRS_ML25293A458 | 있음 (2026-09-14 빌드) | 있음 (`wiki/ACRS_ML25293A458.md`) | pending |

## 다음 작업
1. NEI 18-04 §6 용어집 확인: 노트에 인용되지 않은 정의는 Plant, Multi-Reactor Module Plant, End State, PRA Technical Adequacy, Performance-Based, Risk-Informed, Safety Design Approach, NSRST·NST SSC 정의, DBEHL 정의, AOO·DBE·BDBE·DBA·LBE 용어집 정의(Table 3-1로 인용된 것과 대조). 처리 방식(기존 노트에 추가 / 새 노트 / 생략)을 사용자에게 묻고, 소스 카드 요약(abstract)을 쓴 뒤 `source.py finish NEI_18-04`와 `wiki-lint`.
2. 본 인제스트: 설계 부록 A 순서(다음은 RG 1.233). 원문 1건마다 `wiki-lint`, 2건마다 `wiki-audit`.

### 인계 메모 (2026-09-15 세션)
- 용어 결정 흐름: 사용자는 대부분 "영어 유지"를 고른다. 기관·문서·분석 기법 약어는 "용어 아님". 확정 한국어는 DID=심층방어, source term=선원항 두 건뿐이다.
- 영어 유지 용어를 한국어로 풀어 쓰지 않는다(예: "사건 시퀀스" 금지). lint는 용어표의 금지 표기만 잡으므로, 새 용어를 영어 유지로 기록할 때 흔한 한국어 풀어쓰기를 금지 표기에 함께 넣는다.
- H1: 대표 용어가 영어 유지면 `# English Name (약어)`, 약어가 없으면 `# 한국어 서술 (English Title)`.
- 약어가 있는 영어 유지 용어의 이후 표기는 사용자가 따로 말하지 않으면 "약어"로 둔다(2026-09-15 §4.4·§5 답에 적용). PIRT의 풀이(phenomena identification ranking table)는 원문에 없고 사용자가 제공했다.
- 2026-09-15에 barrier·Layers of Defense·safety margin·Mitigation Function 등의 흔한 한국어 풀어쓰기를 금지 표기로 넣었다. "예방·완화 기능"도 "완화 기능"에 걸리므로 "예방하거나 완화하는 기능"으로 쓴다. "방호 조치"(offsite protective actions)는 protective measure와 다른 말이라 금지하지 않았다.
- `sync_terms.py --apply`는 frontmatter를 YAML 블록 목록(`sources:\n- KEY`, `verified: null`)으로 다시 쓴다. lint는 두 형식을 모두 받는다.
- 긴 장은 작성 뒤 읽기 전용 서브에이전트로 해설과 원문을 대조하면 한정 표현 누락(may, include, helps, primarily)과 귀속 오류가 잡힌다. §4.4·§5에서 효과가 있었다.
- 해설 작성 규칙 재확인: 해설 수치는 원문 사실 절에 있어야 한다(V5). `30-day`처럼 하이픈 붙은 수는 추출되지 않는다. 인용 조각은 3단어 이상. 영어 표기 뒤 조사는 발음으로 직접 판정한다(Target·Function·Level은 받침 있음).

## 미해결
- ACRS_ML25293A458: 전용 프로파일 `acrs_slides.py` (2026-09-15 결정: 슬라이드 제목 `##`, 글머리표 제목 승격 방지, 캡션 없는 그림 37개를 `[!figure] Slide N`으로 포함). Phase 3에서 인제스트 순서 10번 전에 구현.
- `meta/metrics.md`는 첫 표본 재검증(`wiki-audit`) 때 만든다. 목표 오류율은 그때 사용자와 정한다(설계 §10).
- 원문 간 모순(disputed): SSC가 LBE를 F-C Target 안에 두는지 판정할 때 본문(§3.3.6 p.37, §4.2.2 p.47)은 95th percentile 상한, 용어집(§6 p.90)은 평균값. `Risk_Importance_Measures`, `LBE_Risk_Significance`, `Risk_Significant_SSC`가 disputed.
- 그림 처리 방침 미정: 정제본의 PNG를 노트에 embed할지, 문서별로 파일 이름이 겹치지 않는지 확인이 필요하다. NEI 18-04 Figure 3-1, 5-1–5-4는 넣지 않았다.
- lint L14가 `Seismic II/I`의 "II"를 미등록 약어로 잡는다. Special_Treatment 해설은 표지 없이 백틱으로 적었다. 검사 규칙 보완 여부 미정.
- NEI 18-04 §5.6.1의 "Task 7"은 §5.3 Task 7(F-C Target 비교)이 아니라 §3.2.2 LBE 선정 절차의 Task 7(7e DID 평가)로 읽고, Plant_Capability_DID에 두 번호 체계를 병기했다(disputed 아님, 2026-09-15 승인).
- NEI 18-04 §5.3 Task 1은 검사 빈도·범위를 "Task 14"에서 정한다고 적지만 Task 14는 RFDC 과업이다. 노트에 인용하지 않았다. 인용하게 되면 disputed 검토.
- 쪽 표지와 각주 표지가 어긋나는 경우(각주 `[^p71]`이 72–73쪽 블록에 있음) 각주 표지의 쪽으로 인용했다(LBE_Layers_Of_Defense_Review).
