---
updated: 2026-10-16
phase: 3
---
# 상태

## 현재 단계
Phase 3 인제스트 완료(커밋 `67437bc`), 모순 57건 판정 완료(커밋 `cd77fdc`). 남은 범위는 PSAR ch11 §11.4(withheld)와 RG 1.232 부록 A(사용자 결정으로 인제스트하지 않음)뿐이다. 도구 계획: `meta/design/2026-09-14-rebuild-plan-phase2.md`.

## 존재하는 도구
- 정제: `scripts/convert_references.py`, `scripts/clean_references.py`, `scripts/refclean/` (psar·nei1804·rg1232·generic·acrs_slides 프로파일, 공용 `levels.py`, `patches/RG_1.233.json`)
- 원문: `scripts/source.py` (`register`/`adopt`/`sync`/`finish`/`status`)
- 검사: `scripts/lint_wiki.py` (파일 단위 L01–L20, `--all` L30–L36), `scripts/verify_quotes.py` (V1–V5), `scripts/coverage_sections.py` (절 단위 누락, 제외 목록 `meta/coverage_exclusions.json`)
- 변경: `scripts/sync_terms.py` (dry-run 기본), `scripts/build_index.py` (`--check`), `scripts/append_log.py`
- 보고: `scripts/session_start.py`, `scripts/audit_sample.py`
- 보조: `scripts/notes.py`, `scripts/citations.py`, `scripts/terms.py`, `scripts/leak_guard.py`, `scripts/hook_post_edit.py`
- 생성물·설정: `index.md`, `internal/index.md`, `wiki/Terminology.md`, `meta/terms_state.json`, `templates/`, `.claude/settings.json`, `.claude/skills/`, `meta/views/*.base`, Obsidian Shell Commands 4종
- 관문: git pre-commit(두 저장소: 경로, `[[HELIOS_`, 내부 문서명, lint, 인용 검증, index), git commit-msg(내부 문서명), Claude SessionStart·PostToolUse hook
- 테스트: 395건 (`python -m pytest scripts/refclean/tests scripts/tests -q`)

## 원문
| 키 | ingest | 끝낸 범위 | 남은 범위 |
|---|---|---|---|
| NEI_18-04 | complete | 전체 | 없음 |
| ACRS_ML25293A458 | complete | 22쪽 | 없음 |
| RG_1.232 | complete | 본문, App. B, App. C | App. A(사용자 결정으로 인제스트하지 않음) |
| RG_1.233 | complete | §A–§D 전체 본문 | 없음(약어 목록·참고문헌은 인제스트 대상 아님) |
| PSAR_ch01 | complete | §1.1–§1.4 전체 | 없음 |
| PSAR_ch03 | complete | 전체 | 없음 |
| PSAR_ch04 | complete | 전체 | 없음 |
| PSAR_ch05 | complete | 전체 | 없음 |
| PSAR_ch06 | complete | §6.1–§6.4.5 전체 | 없음 |
| PSAR_ch07 | complete | §7.1–§7.8 전체 | 없음 |
| PSAR_ch11 | in_progress | §11.1, §11.2, §11.3, §11.5, §11.6 | §11.4(withheld만 남음) |
| SER_KU1_CP | in_progress | 1, 3–7, 11, 13장, 부록 A–B(노트 23개) | 3–7·11장 등의 미인용 하위 절(PDC·기능별 정합성 판단 등, 약 370절). 2, 8–10, 12, 14장은 대응 PSAR 장이 vault에 없어 제외 |
| RG_1.253 | complete | 전체 | 없음(Table A-2·A-3은 정제본 표가 깨져 주석 문단만 인용) |
| RG_1.247 | complete | 전체(본문 C.1–C.4, 부록 A의 qualification·주요 clarification, 부록 B) | 없음(부록 A "No objection" 레코드는 개별 노트로 옮기지 않음) |

## 다음 작업
0. `SER_KU1_CP` 잔여 하위 절의 처리 방침(노트 보강 또는 coverage 제외)을 사용자와 정한다. 내부 자료 작업 상태는 `internal/status.md`.
0a. `wiki-audit`(RG_1.253·RG_1.247 인제스트 뒤)와 `wiki-lint` 의미 점검(SER, RG_1.253, RG_1.247).
0b. 정제 파이프라인 보완 후보: RG_1.247 Table 1 내용 누락, 부록 A 굵은 글씨·취소선 소실(현재 노트는 issue 문장 위주), C.1.3.8 쪽 표지 위치; RG_1.253 Table A-2·A-3 표 구조 깨짐.
1. lint 조치 A6 결정(`Risk_Significant_SSC` 단일 기록처화와 `Risk_Importance_Measures` disputed 해제).
2. NEI 18-04 내부 불일치 3건(§5.3 Task 1의 "Task 14" 참조, 용어집 RI 출처 칸, Task 7c "within 1%"와 §4.2.2 "exceeds 1%")을 `meta/contradictions.md`에 기록할지 결정.
3. 남은 미정 용어 후보 질문.
4. `wiki-lint` 의미 점검(2026-09-16 배치 전체).
5. 다음 `wiki-audit`: 다음 원문 2건 인제스트 뒤, 또는 수정된 대조 절차로 만든 노트가 생긴 뒤.

### 인계 메모
- 용어 결정 흐름: 사용자는 대부분 "영어 유지"를 고른다. 기관·문서·분석 기법 약어는 "용어 아님". 확정 한국어는 DID=심층방어, source term=선원항, cover gas=커버가스, non-LWR=비경수형원전.
- 영어 유지 용어를 한국어로 풀어 쓰지 않는다. 용어표에 없는 규제·설계 용어(design basis ~, protective action, reasonable assurance/confidence, seismic demand 등)도 한국어로 옮기지 말고 영어로 둔다(2026-09-16 검토 결과).
- H1: 대표 용어가 영어 유지면 `# English Name (약어)`, 약어가 없으면 `# 한국어 서술 (English Title)`.
- 약어가 있는 영어 유지 용어의 이후 표기는 약어.
- 긴 장은 추출을 읽기 전용 서브에이전트에 맡기고(`extract/*.md`, 인용 ±1쪽 재검증), 노트는 생성 스크립트로 쓰고, 작성 뒤 읽기 전용 서브에이전트로 해설을 원문과 대조한다. 2026-09-16 배치에서 오류 10, 수정 권고 53건을 잡았다.
- 해설 규칙: 수치는 원문 사실 절에 있어야 한다(V5, 백틱 안의 수도 검사됨, `Chapter`/`Section`/`§` 뒤 번호는 제외). 인용 조각 3단어 이상. `1차`처럼 숫자가 든 한국어도 V5에 걸린다.
- disputed 판정은 모든 원문 인제스트 뒤로 미룬다(2026-09-16 사용자 결정). 새 모순은 `meta/contradictions.md`에 모은다.

## 미해결
- 첫 `wiki-audit`(2026-10-14, seed 20261014): 노트 오류율 20 % (2/10), 원문 사실 항목 오류 0/417. 목표 노트 오류율 ≤ 10 %. 오류 2건은 해설의 원문 사실 근거 누락과 문서 구조 배타 진술; `wiki-ingest` 대조 지시를 보완함. `meta/metrics.md`.
- 원문 간 모순(disputed, 이전 결정): NEI 18-04 SSC risk significance 평균/상한(`Risk_Importance_Measures`, `LBE_Risk_Significance`, `Risk_Significant_SSC`), BDBE 빈도 하한(`LBE_Frequency_Categories`).
- 모순 57건 판정 완료(2026-09-16): disputed 28건(노트 38개), 기록만 25건, 공백 4건. `meta/contradictions.md` §판정.
- 다음 용어 질문 후보(노트에는 영어로 둠): redundant/redundancy, partially·fully conform, margin(setpoint margin 등), qualified(seismically/environmentally), PEP, LBE family, plant functional/physical capability DID, DID baseline, severe accident, Design Reliability Assurance Program, seismic classification, SCS1/SCS2/SCN1–SCN3, Seismic Category I, maximum considered earthquake, OBE, LCO, LSSS, SL, COLR, ERO, ERF, technical specifications, emergency preparedness, protective action, emergency response functions, control rod assembly, refueling, downpower, passive, design basis ~, reasonable assurance/confidence, stylized scenarios, permanent uncertainties, integrated risk, plant challenges; 낮은 우선순위: 결정론적 안전해석, 보수적 가정, 미지 요소, 불리한 사건, 보호 전략, 모델링 불확실도. 2026-09-16 배치에서 더한 후보: steel embedment, extraordinary events, consensus codes and standards, design transient, Level A–D Service Loading, service stress limit, core support structure, design-by-rule/design-by-analysis, Foundation Input Response Spectra, in-structure response spectra, seismic anchor motion, accidental torsion, Lateral Force Resisting System, limit state design method, stay-in-place formwork, dynamic amplification factor, factors of safety, functional containment, radionuclide retention, stack.
- 2026-09-16 완료한 lint 조치: A7(새 노트 4), A9(C17 기록), A1(LBE_Risk_Significance 해설에 평균·상한 병기), A4(Integrated_Decision_Making_Process 해설에 SR 예외 명시). 남은 결정: A6(Risk_Significant_SSC를 단일 기록처로 두고 Risk_Importance_Measures의 disputed 해제).
- NEI 18-04 용어집 RI 항목의 출처 칸 오기 가능성(고치지 않음).
- lint L14가 로마 숫자(`Seismic II/I`, `Seismic Risk Category III/IV`)를 약어로 잡는다. 백틱으로 피하고 있음.
- ACRS 정제본에서 한 글머리표가 두 문단으로 갈라진 곳 2곳(p.5, p.10): `acrs_slides.py` 보완 대상.
- NEI 18-04 §5.3 Task 1의 "Task 14" 참조 불일치(노트에 인용하지 않음).
