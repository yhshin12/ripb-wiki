---
updated: 2026-10-19
phase: 3
---
# 상태

## 현재 단계
Phase 3 인제스트 완료(커밋 `67437bc`), 모순 57건 판정 완료(커밋 `cd77fdc`). 남은 범위는 PSAR ch11 §11.4(withheld)와 RG 1.232 부록 A(사용자 결정으로 인제스트하지 않음)뿐이다. 도구 계획: `meta/design/2026-09-14-rebuild-plan-phase2.md`.

## 존재하는 도구
- 정제: `scripts/convert_references.py`, `scripts/clean_references.py`, `scripts/refclean/` (psar·nei1804·rg1232·generic·acrs_slides 프로파일, 공용 `levels.py`, `patches/*.json`; SER_KU1_CP patch 3건은 2026-10-18 추가)
- 원문: `scripts/source.py` (`register`/`adopt`/`sync`/`finish`/`status`)
- 검사: `scripts/lint_wiki.py` (파일 단위 L01–L20, `--all` L30–L36), `scripts/verify_quotes.py` (V1–V5), `scripts/coverage_sections.py` (절 단위 누락, 제외 목록 `meta/coverage_exclusions.json`), `scripts/check_absence.py` (부재 진술 재점검 A1·A2, 원장 `meta/absence_ledger.json`, wiki-lint 끝에 `--accept`)
- 변경: `scripts/sync_terms.py` (dry-run 기본), `scripts/build_index.py` (`--check`), `scripts/append_log.py`
- 보고: `scripts/session_start.py`, `scripts/audit_sample.py`
- 보조: `scripts/notes.py`, `scripts/citations.py`, `scripts/terms.py`, `scripts/leak_guard.py`, `scripts/hook_post_edit.py`
- 생성물·설정: `index.md`, `internal/index.md`, `wiki/Terminology.md`, `meta/terms_state.json`, `templates/`, `.claude/settings.json`, `.claude/skills/`, `meta/views/*.base`, Obsidian Shell Commands 4종
- 관문: git pre-commit(두 저장소: 경로, `[[HELIOS_`, 내부 문서명, lint, 인용 검증, index), git commit-msg(내부 문서명), Claude SessionStart·PostToolUse hook
- 테스트: 427건 (`python -m pytest scripts/refclean/tests scripts/tests -q`)

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
| SER_KU1_CP | complete | 1, 3–7, 11, 13장, 부록 A–B, 잔여 R1·R2(노트 30개) | 없음(2, 8–10, 12, 14장은 대응 PSAR 장이 vault에 없어 제외; 나머지 제외 절은 `meta/coverage_exclusions.json`) |
| RG_1.253 | complete | 전체 | 없음(Table A-2·A-3은 주석 문단만 인용; 2026-10-20 정제본에서 표 복원, 행 단위 미인제스트) |
| RG_1.247 | complete | 전체(본문 C.1–C.4, 부록 A의 qualification·주요 clarification, 부록 B) | 없음(부록 A "No objection" 레코드는 개별 노트로 옮기지 않음) |
| TP-LIC-RPT-0011 | partial | hot channel factor 단위(§1.1 Table 1-1, §3.2–3.2.1.4, §4.1.2–4.1.2.4, Figure 4-1, §5.2, §6, §8.1.16) | 수시 인제스트(설계 §4.3): 질의가 생길 때 단위로 |

## 다음 작업
0. 2026-10-18 `wiki-lint` 의미 점검(SER 잔여 R1·R2, 계통 묶음 재점검)과 조치 1–8 적용을 마쳤다(`meta/lint/2026-10-18.md`). A6(`Risk_Significant_SSC` 단일 기록처화)도 적용했다.
1. (완료) 2026-10-19 `wiki-audit` seed 20261019: 노트 오류율 10 %(1/10, 목표 충족), 원문 사실 항목 오류 0/892. 2026-09-16 배치 46노트 요약·해설 점검에서 같은 유형 오류 0건, 과잉 일반화 4건(Natrium_PDC_Development 요약의 "가장 흔한 변경", Natrium_SR_Functions_Retaining_Radionuclides 요약의 "DL3-RR1부터 DL3-RR10까지"(RR9 없음), Natrium_DBE_List·Natrium_BDBE_List 요약의 "원자로 쪽" 범위)은 2026-10-19 사용자 승인으로 고쳤다.
2. 정제 파이프라인 보완: 2026-10-20에 여러 쪽 표 뒤 쪽 표지, NEI 18-04 각주 정의 위치, SER §7.3.1.1.9.3 제목, ACRS 글머리표 분할 2곳, RG_1.247 Table 1(상자 안 목록), RG_1.253 Table A-2·A-3(신문식 4단 → 시트별 요건 표)을 고쳤다. 남은 후보:
   - RG_1.247 부록 A의 굵은 글씨(staff 추가 문구, 84쪽 313 span)·취소선(삭제 문구) 소실. 복원하려면 정제본 형식 계약(CLAUDE.md §3 강조 허용 범위)을 넓혀야 하므로 사용자 결정이 필요하다.
   - RG_1.247 Figure 1(p.11 이미지): `figures.py`의 `FIG_TXT`가 `Figure 1.` 형식 캡션을 인식하지 않아 그림이 렌더링되지 않는다.
   - 쪽 경계를 넘는 문단: 문단이 시작 쪽 표지 아래에 통째로 놓여, 다음 쪽 문장도 시작 쪽으로 인용된다(예: RG_1.247 §C.1.3.8 p.24-25, 2026-10-20 인용 1건 정정). ±0쪽 엄격 대조에서 원문 사실 인용 175건이 인용 쪽에서 문장을 찾지 못한다(±1쪽 안에서는 찾음). 처리 방식(문단 안 쪽 표지 또는 인용 정정)을 정한다.
3. 남은 미정 용어 후보 질문. 용어표의 `미정` 행: `FOM`, `NASCENT`(2026-10-26 NAT-3049 인제스트).
4. `coverage_sections.py`는 절 단위로만 센다. 같은 절 안의 staff 판단 문장이 빠져도 잡지 못한다(2026-10-18 점검에서 약 80문장 확인). 판단 문장 단위 검사가 필요한지 결정한다.

### 인계 메모
- 용어 결정 흐름: 사용자는 대부분 "영어 유지"를 고른다. 기관·문서·분석 기법 약어는 "용어 아님". 확정 한국어는 DID=심층방어, source term=선원항, cover gas=커버가스, non-LWR=비경수형원전.
- 영어 유지 용어를 한국어로 풀어 쓰지 않는다. 용어표에 없는 규제·설계 용어(design basis ~, protective action, reasonable assurance/confidence, seismic demand 등)도 한국어로 옮기지 말고 영어로 둔다(2026-09-16 검토 결과).
- H1: 대표 용어가 영어 유지면 `# English Name (약어)`, 약어가 없으면 `# 한국어 서술 (English Title)`.
- 약어가 있는 영어 유지 용어의 이후 표기는 약어.
- 긴 장은 추출을 읽기 전용 서브에이전트에 맡기고(`extract/*.md`, 인용 ±1쪽 재검증), 노트는 생성 스크립트로 쓰고, 작성 뒤 읽기 전용 서브에이전트로 해설을 원문과 대조한다. 2026-09-16 배치에서 오류 10, 수정 권고 53건을 잡았다.
- 해설 규칙: 수치는 원문 사실 절에 있어야 한다(V5, 백틱 안의 수도 검사됨, `Chapter`/`Section`/`§` 뒤 번호는 제외). 인용 조각 3단어 이상. `1차`처럼 숫자가 든 한국어도 V5에 걸린다.
- 단순 수치·번호 차이(2026-10-30 사용자 결정): 더 적합한 값을 기준으로 쓰고 노트에 오기로 보이며 차후 확인이 필요하다고 적어 종결한다.
- 모순 판정 원칙(2026-10-17 사용자 결정): 권위 문서(NRC 문서, RG 1.233이 승인한 NEI 18-04)끼리의 실질 상충만 disputed. PSAR과 권위 문서의 차이, PSAR 내부 차이는 해설의 "규정 대비 메모"로 해소. 권위 문서끼리 표기 차이는 기록만. RG 명확화가 NEI 문장보다 우선하고, SER의 해석은 해소·SER의 문언 밖 확장은 dispute. 새 모순은 `meta/contradictions.md`에 모은다.

## 미해결
- 모순: 2026-10-30 사용자 결정으로 `meta/contradictions.md`에는 미결 항목만 둔다. 종결 항목은 노트의 규정 대비 메모와 소스 카드에 있고, 남은 항목의 근거는 같은 파일의 상세 절에 있다. 2026-10-17 재분류 메모는 삭제했으며 git 이력에서 볼 수 있다. 남은 항목 4건: C14-1, C14-6, C67, C81. disputed 노트 4개.
- 누락 주제(2026-10-16 의미 점검): other quantified events(OQE), Pin Removal Cell, Pool Immersion Cell과 ESWR 사건군, SHX(허가 조건 대상), RIM 프로그램, D-RAP, 항공기 충돌 평가, complementary design criteria, Prevention Function의 분류 처리, 피동 NSRST 저하 성능의 DBA credit, PRA 형상 관리·self-assessment·peer review, 사용후연료 PRA, DG-1404와 RG 1.253의 관계, 10 CFR 50.34(f)의 비경수형원전 적용성, SER의 "seventeen AOOs and BDBEs" 목록. vault에 원문이 없는 문서: NEI 21-07, NEI 20-09, ASME/ANS RA-S-1.4-2021 본문, NUREG-1855.
- 누락 주제(2026-10-18 의미 점검, 원문이 vault에 없음): PSAR ch2 부지 주제(기상탑, 5 miles 안 산업시설, 교통 hazard, 화산 평가), compressive assembly R&D(PSAR ch13), 10 CFR 50.155의 OL 이연, NAT-4770, ANSI/ANS-3.2와 RG 1.33의 관계, "Cold Shutdown"·"Hot Standby"와 Mode 3·4의 대응.
- 누락 주제(2026-10-26 TP-LIC-RPT-0011 인제스트): HCF 산정 방법·값(§3.2.1.4, §4.1.2.4, §8.1.16, Table 8-13–8-17)은 공개본에서 비공개; SER이 인용한 ML25276A289의 판(NRC 서버 403); 보고서 참고문헌 [17]–[44] 비공개. 정제 한계: 콜론 형식 표 캡션("Table 1-1: …")이 표에 붙지 않음(공용 `CAPTION_RE` 변경은 SER·PSAR ch7에 영향).
- 첫 `wiki-audit`(2026-10-14, seed 20261014): 노트 오류율 20 % (2/10), 원문 사실 항목 오류 0/417. 목표 노트 오류율 ≤ 10 %. 오류 2건은 해설의 원문 사실 근거 누락과 문서 구조 배타 진술; `wiki-ingest` 대조 지시를 보완함. `meta/metrics.md`.
- 다음 용어 질문 후보(노트에는 영어로 둠): redundant/redundancy, partially·fully conform, margin(setpoint margin 등), qualified(seismically/environmentally), PEP, LBE family, plant functional/physical capability DID, DID baseline, severe accident, Design Reliability Assurance Program, seismic classification, SCS1/SCS2/SCN1–SCN3, Seismic Category I, maximum considered earthquake, OBE, LCO, LSSS, SL, COLR, ERO, ERF, technical specifications, emergency preparedness, protective action, emergency response functions, control rod assembly, refueling, downpower, passive, design basis ~, reasonable assurance/confidence, stylized scenarios, permanent uncertainties, integrated risk, plant challenges; 낮은 우선순위: 결정론적 안전해석, 보수적 가정, 미지 요소, 불리한 사건, 보호 전략, 모델링 불확실도. 2026-09-16 배치에서 더한 후보: steel embedment, extraordinary events, consensus codes and standards, design transient, Level A–D Service Loading, service stress limit, core support structure, design-by-rule/design-by-analysis, Foundation Input Response Spectra, in-structure response spectra, seismic anchor motion, accidental torsion, Lateral Force Resisting System, limit state design method, stay-in-place formwork, dynamic amplification factor, factors of safety, functional containment, radionuclide retention, stack.
- NEI 18-04 용어집 RI 항목의 출처 칸 오기 가능성(고치지 않음).
- lint L14가 로마 숫자(`Seismic II/I`, `Seismic Risk Category III/IV`)를 약어로 잡는다. 백틱으로 피하고 있음.
- NEI 18-04 §5.3 Task 1의 "Task 14" 참조 불일치(노트에 인용하지 않음).
