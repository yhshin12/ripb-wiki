---
updated: 2026-09-16
phase: 3
---
# 상태

## 현재 단계
Phase 3 인제스트 진행 중. 완료: NEI 18-04(2026-09-15), ACRS_ML25293A458(2026-09-16). 진행 중(단위 완료, 원문 남음): RG 1.232, RG 1.233, PSAR ch1·ch3·ch4·ch5·ch6·ch7·ch11. 도구 계획: `meta/design/2026-09-14-rebuild-plan-phase2.md`.

## 존재하는 도구
- 정제: `scripts/convert_references.py`, `scripts/clean_references.py`, `scripts/refclean/` (psar·nei1804·rg1232·generic·acrs_slides 프로파일, 공용 `levels.py`, `patches/RG_1.233.json`)
- 원문: `scripts/source.py` (`register`/`adopt`/`sync`/`finish`/`status`)
- 검사: `scripts/lint_wiki.py` (파일 단위 L01–L20, `--all` L30–L36), `scripts/verify_quotes.py` (V1–V5)
- 변경: `scripts/sync_terms.py` (dry-run 기본), `scripts/build_index.py` (`--check`), `scripts/append_log.py`
- 보고: `scripts/session_start.py`, `scripts/audit_sample.py`
- 보조: `scripts/notes.py`, `scripts/citations.py`, `scripts/terms.py`, `scripts/leak_guard.py`, `scripts/hook_post_edit.py`
- 생성물·설정: `index.md`, `internal/index.md`, `wiki/Terminology.md`, `meta/terms_state.json`, `templates/`, `.claude/settings.json`, `.claude/skills/`, `meta/views/*.base`, Obsidian Shell Commands 4종
- 관문: git pre-commit(두 저장소: 경로, `[[HSFR_`, 내부 문서명, lint, 인용 검증, index), git commit-msg(내부 문서명), Claude SessionStart·PostToolUse hook
- 테스트: 395건 (`python -m pytest scripts/refclean/tests scripts/tests -q`)

## 원문
| 키 | ingest | 끝낸 범위 | 남은 범위 |
|---|---|---|---|
| NEI_18-04 | complete | 전체 | 없음 |
| ACRS_ML25293A458 | complete | 22쪽 | 없음 |
| RG_1.232 | in_progress | 본문, App. B | App. A, App. C |
| RG_1.233 | in_progress | 전체 본문 | 남은 부분 확인 |
| PSAR_ch01 | in_progress | §1.3, §1.1.1–§1.1.4.1 | §1.1.4.2–§1.2(계통·부지), §1.4(RG 부합, TMI, 규격) |
| PSAR_ch03 | in_progress | §3.1–§3.10 | §3.11–§3.14 |
| PSAR_ch04 | in_progress | 전체 | 없음(요약 작성 후 finish) |
| PSAR_ch05 | in_progress | 전체 | 없음(요약 작성 후 finish) |
| PSAR_ch06 | in_progress | §6.1–§6.4.1.1 | §6.4.1.2–§6.4.5, 구조·기계 설계 표 |
| PSAR_ch07 | in_progress | §7.6.8 일부 | 전체 계통 27개(2026-09-16 결정: 전체) |
| PSAR_ch11 | in_progress | §11.3, §11.5 | §11.1, §11.2(HFE), §11.4(withheld), §11.6 |

## 다음 작업
1. `wiki-lint`: 2026-09-15 보고서의 조치 가운데 disputed와 무관한 것(A7 새 노트, A9 기록)과 이번 배치 전체의 의미 점검.
2. 그림 정책 구현(2026-09-16 결정): vault 루트 `figures/`에 `KEY_그림명.png`로 모으고 노트에서 참조한다. withheld 그림은 제외.
3. 남은 인제스트: 위 표의 남은 범위. PSAR ch7은 전체 계통.
4. 모든 원문 인제스트 뒤 `meta/contradictions.md`의 모순을 한꺼번에 판정(disputed).
5. `wiki-audit` 첫 표본 재검증.

### 인계 메모
- 용어 결정 흐름: 사용자는 대부분 "영어 유지"를 고른다. 기관·문서·분석 기법 약어는 "용어 아님". 확정 한국어는 DID=심층방어, source term=선원항, cover gas=커버가스, non-LWR=비경수형원전.
- 영어 유지 용어를 한국어로 풀어 쓰지 않는다. 용어표에 없는 규제·설계 용어(design basis ~, protective action, reasonable assurance/confidence, seismic demand 등)도 한국어로 옮기지 말고 영어로 둔다(2026-09-16 검토 결과).
- H1: 대표 용어가 영어 유지면 `# English Name (약어)`, 약어가 없으면 `# 한국어 서술 (English Title)`.
- 약어가 있는 영어 유지 용어의 이후 표기는 약어.
- 긴 장은 추출을 읽기 전용 서브에이전트에 맡기고(`extract/*.md`, 인용 ±1쪽 재검증), 노트는 생성 스크립트로 쓰고, 작성 뒤 읽기 전용 서브에이전트로 해설을 원문과 대조한다. 2026-09-16 배치에서 오류 10, 수정 권고 53건을 잡았다.
- 해설 규칙: 수치는 원문 사실 절에 있어야 한다(V5, 백틱 안의 수도 검사됨, `Chapter`/`Section`/`§` 뒤 번호는 제외). 인용 조각 3단어 이상. `1차`처럼 숫자가 든 한국어도 V5에 걸린다.
- disputed 판정은 모든 원문 인제스트 뒤로 미룬다(2026-09-16 사용자 결정). 새 모순은 `meta/contradictions.md`에 모은다.

## 미해결
- `meta/metrics.md`는 첫 `wiki-audit` 때 만든다.
- 원문 간 모순(disputed, 이전 결정): NEI 18-04 SSC risk significance 평균/상한(`Risk_Importance_Measures`, `LBE_Risk_Significance`, `Risk_Significant_SSC`), BDBE 빈도 하한(`LBE_Frequency_Categories`).
- 새 모순 16건: `meta/contradictions.md`.
- NEI 18-04 용어집 RI 항목의 출처 칸 오기 가능성(고치지 않음).
- lint L14가 로마 숫자(`Seismic II/I`, `Seismic Risk Category III/IV`)를 약어로 잡는다. 백틱으로 피하고 있음.
- ACRS 정제본에서 한 글머리표가 두 문단으로 갈라진 곳 2곳(p.5, p.10): `acrs_slides.py` 보완 대상.
- NEI 18-04 §5.3 Task 1의 "Task 14" 참조 불일치(노트에 인용하지 않음).
