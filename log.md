# log

작업 1건당 항목 1개를 끝에 덧붙인다. 형식: `## [YYYY-MM-DD] <type> | <제목>` + 요점. 구 log(2026-05-02 ~ 2026-09-14)는 `internal/_legacy/log-before-rebuild.md`.

## [2026-09-14] init | vault 재구축 시작 (Phase 0)
- 구 이력 전체를 `internal/_legacy/ripb-before-rebuild.bundle`로 보존하고 새 이력을 시작했다.
- 구 wiki 267개 노트, Gemini 시기 스크립트·설정, 구 `raw/`(압축 보관)를 제거했다. 근거: `meta/design/2026-09-14-vault-rebuild-design.md` §1.
- 정제 파이프라인(`scripts/refclean/`, 커밋 31f826e)과 그 기록(`meta/references_cleanup/`)은 그대로 승계했다.

## [2026-09-14] chore | 새 이력 첫 커밋
- git #1 첫 커밋. `references/`, `internal/`, `inbox/`는 추적하지 않는다. pre-commit 관문 확인.

## [2026-09-14] feat | 소스 카드 9장
- `scripts/source.py adopt`로 정제본 9건의 소스 카드를 만들었다(`wiki/<KEY>.md`, `ingest: pending`). RG 1.232 원문 파일명에 제목을 붙였다(재변환, 본문 동일).

## [2026-09-14] feat | 대기 원문 2건 등록 (RG 1.233, ACRS ML25293A458)
- `source.py register` → 변환 → generic 프로파일로 정제 → 소스 카드. 누락률: RG 1.233 0.12 %, ACRS ML25293A458 0.11 %. Phase 1 완료.

## [2026-09-15] feat | Phase 2 완료: 도구
- 검사(lint_wiki L01–L36, verify_quotes V1–V5), 변경(sync_terms, build_index, append_log), 보고(session_start, audit_sample), 보조 모듈(notes, citations, terms, leak_guard, hook_post_edit).
- 관문: Claude SessionStart·PostToolUse hook, git pre-commit 전체 검사(두 저장소), commit-msg 내부 문서명 검사. 탐침으로 거부 동작 확인.
- skill 5종(wiki-ingest/terms/query/lint/audit), 템플릿 3종, 빈 용어표, Bases 보기 4종, Obsidian 명령 4종(Gemini 실행 명령 제거).
- Phase 1 이관 항목 처리: source.py 보강 7건, generic 프로파일 2건, 설계 부록 B·§8.1 수정, refs marker(원문 의존 테스트 109건), internal .gitattributes.
- 결함 1건 수정: 템플릿의 dict 형 frontmatter 값이 lint·index·audit·sync를 중단시키던 문제. 회귀 테스트 5건 추가.
- 테스트 388건 통과. lint·인용 검증 오류 0, index 최신, 용어 동기화 변경 0.

## [2026-09-15] ingest | NEI 18-04 §3.1, §3.2.1 (시범)
- 새 노트 3개(Licensing_Basis_Event, LBE_Frequency_Categories, F_C_Target), 고친 노트 1개(소스 카드 NEI_18-04 단위 등록·완료).
- 용어 11건을 영어 유지로 확정(LBE, AOO, DBE, BDBE, DBA, F-C Target, SSC, ES, QHO, EAB, TLST). 미정 용어 0.
- 검사: lint 오류 0·경고 0, 인용 검증 오류 0, 용어 충돌 0, 조사 확인 5건 중 2건 수정. 작성 중 PostToolUse hook이 링크·용어 첫 등장·해설 수치 문제 8건을 잡아 고쳤다.
- 시범에서 드러난 규칙 보완 2건은 meta/status.md 다음 작업에 적었다: 영어 유지 용어 노트의 H1 형식, 기관·규정 약어의 용어표 등록과 lint 경고 처리.

## [2026-09-15] docs | 시범 인제스트 뒤 규칙 보완 2건
- 영어 유지 용어 노트의 H1은 '# English Name (약어)'로 쓴다(CLAUDE.md §4, 설계 §5.6).
- 기관·규정 약어 7건(NRC, EPA, CFR, PRA, LWR, SRP, PAG)을 용어표에 '용어 아님'으로 등록했다. lint는 그 상태의 약어에 표지가 없어도 경고하지 않는다(테스트 1건 추가, 389건 통과).

## [2026-09-15] ingest | NEI 18-04 §3.2.2, §3.2.3
- 새 노트 3개(LBE_Selection_Process, Required_Safety_Function, LBE_Risk_Significance), 고친 노트 2개(F_C_Target 링크, 소스 카드 단위).
- 용어: 영어 유지 12건(RSF, PSF, SR, DBEHL, DID, IE, MST, RIPB, LMP, Risk-Significant LBE, Risk-Significant SSC, cumulative risk target), 용어 아님 3건(FMEA, HAZOP, PHA). 미정 용어 0.
- 검사: lint 오류 0·경고 0, 인용 검증 오류 0, 용어 충돌 0, 조사 확인 20건 모두 올바름.
- 발견한 도구 결함: 인용 정규화가 [^p23] 형태의 각주 참조를 지우지 않는다. 별도 커밋으로 수정한다.

## [2026-09-15] ingest | NEI 18-04 §3.3
- 새 노트 5개(PRA_Role_In_LBE_Selection, Non_LWR_PRA_Scope, PRA_Safety_Function, Event_Sequence_Family, Risk_Importance_Measures), 고친 노트 6개(LBE_Risk_Significance 사실 추가, 이전 노트 4개의 용어 풀어쓰기 수정, 소스 카드).
- 원문 간 모순 1건: SSC가 LBE를 F-C Target 안에 두는지 판정할 때 용어집은 평균값, §3.3.6은 95th percentile 상한. Risk_Importance_Measures와 LBE_Risk_Significance를 disputed로 둠.
- 용어: 영어 유지 3건(FSF, POS, Event Sequence Family), 용어 아님 15건, 금지 표기 4건 추가. 미정 용어 0.
- 검사: lint 오류 0·경고 0, 인용 검증 오류 0(노트 23개), 용어 충돌 0.

## [2026-09-15] terms | 용어 반영: 심층방어, 선원항; H1 규칙 보완
- DID를 영어 유지에서 확정(심층방어, 이후 표기 한국어)으로 바꾸고 노트 3개에 전파했다. 금지 표기는 '심층 방어'만 남겼다.
- source term을 확정(선원항)으로 추가했다. Mechanistic Source Term(MST)은 영어 유지로 둔다.
- 약어 없는 영어 유지 용어의 노트는 H1을 '# 한국어 서술 (English Title)'로 쓰고 용어 자체는 영어로 둔다(CLAUDE.md §4, 설계 §5.6).

## [2026-09-15] ingest | NEI 18-04 §4 도입, §4.1–§4.3
- 새 노트 3개(SSC_Safety_Classification, Safety_Significant_SSC, Risk_Significant_SSC), 고친 노트 2개(Risk_Importance_Measures에 §4.2.2 인용 추가, 소스 카드 단위).
- 원문 간 모순 이어짐: §4.2.2도 95th percentile 상한을 써 용어집(평균값)과 어긋난다. Risk_Significant_SSC를 disputed로 둠(disputed 노트 3개).
- 용어: 영어 유지 5건(NSRST, NST, Safety-Significant SSC, special treatment, IDP), 용어 아님 3건(reliability target, capability target, NEI), 금지 표기 4개 추가. 미정 용어 0.
- 검사: lint 오류 0·경고 0, 인용 검증 오류 0(노트 26개), 용어 충돌 0. 다음 세션 인계 메모를 meta/status.md에 적었다.

## [2026-09-15] ingest | NEI 18-04 §4.4, §5
- 새 노트 12 (§4.4: SSC 설계 요건, RFDC, special treatment, 신뢰도·능력·safety margin; §5: DID 적절성 체계, 통합 절차, Plant Capability DID, LBE와 Layers of Defense 대조, risk margin, Programmatic DID, IDP, DID baseline), 고친 노트 12 (금지 표기 제거 11곳, 링크 추가)
- 검사: lint 오류 0·경고 0, verify_quotes 오류 0, sync_terms 충돌 0, 서브에이전트 원문 대조 뒤 한정 표현·귀속 수정
- 미정 용어 0; §6 용어집 확인과 finish 남음

## [2026-09-15] terms | 용어 반영: §4.4·§5 용어
- 영어 유지 26 (RFDC, SRDC, Prevention/Mitigation Function, Layers of Defense, barrier, safety margin, RAP, IDPP, RISC, SSE, Seismic II/I, Plant Capability DID, Programmatic DID, RIPB-DM, TI-RIPB, PB, RI, Safety Design Approach, levels of defense, protective measure, compensatory action, risk margin, design margin, reliability/availability mission, cliff edge effects, PIRT)
- 용어 아님 6 (MR, LER, QA, MHTGR, Technical Specifications, SAMG)

## [2026-09-15] ingest | NEI 18-04 ABSTRACT, §1–§2, §6 (finish)
- 새 노트 1 (TI_RIPB_Process_Overview), 고친 노트 10 (용어집 정의 추가: LBE 범주, LBE, NSRST·NST, DBEHL, ES·End State·POS·Plant·Multi-Reactor Module Plant, PRA Technical Adequacy·MST, IE, RI·PB, Safety Design Approach)
- 검사: lint 오류 0·경고 0, verify_quotes 오류 0, sync_terms 충돌 0, 서브에이전트 원문 대조 뒤 수정
- disputed 추가: LBE_Frequency_Categories (BDBE 빈도 하한, 평균값 대 상한값)
- NEI_18-04 ingest complete

## [2026-09-15] terms | 용어 반영: 용어집 용어
- 영어 유지 4 (Plant, Multi-Reactor Module Plant, End State, PRA Technical Adequacy)

## [2026-09-16] terms | 용어 반영: 2026-09-15–16 결정
- 영어 유지: RG 1.232·RG 1.233·PSAR 약어(GDC, PDC, SFR, SARRDL, LOCA, DL, OL, CP 등), OQE, PIE, CCF, DBHL(DBEHL과 별개), SAFDL, EPZ
- 확정 한국어: cover gas=커버가스, non-LWR=비경수형원전
- 용어 아님: ARDC, SFR-DC, MHTGR-DC, primary coolant boundary, functional containment, independent and diverse 등 15

## [2026-09-16] feat | 정제: ACRS 슬라이드 프로파일, RG 1.233 패치, generic 보완
- acrs_slides 프로파일과 테스트 추가
- RG_1.233 패치 52건
- generic 프로파일·테스트 수정

## [2026-09-16] lint | 의미 점검 2026-09-15 (NEI 18-04)
- 보고서 meta/lint/2026-09-15.md
- 용어 반영과 금지 표기에 따른 기존 노트 수정

## [2026-09-16] ingest | RG_1.232 본문·App. B
- 새 노트 16 (PDC 역할, 기준 대조표, SFR-DC 기준군 14)
- 검사: lint 0, verify_quotes 0, 서브에이전트 원문 대조
- 원문 내부 불일치는 meta/contradictions.md C14에 모음

## [2026-09-16] ingest | RG_1.233 본문
- 새 노트 9 (배경, NEI 18-04 endorsement, LBE·SSC·DID 직원 입장, 신청서 내용, PRA 역할, MST, 단일 고장 기준)
- 검사: lint 0, verify_quotes 0

## [2026-09-16] ingest | PSAR ch1 (U1–U2), ch3, ch4, ch5, ch6 (U1), ch7 (§7.6.8 일부), ch11 (U1)
- 새 노트 46, 고친 노트 3 (Fundamental Safety Functions, DID Approach, Risk-Significant LBEs)
- 검사: lint 0, verify_quotes 0, 서브에이전트 원문 대조 뒤 수정
- 원문 모순 16건을 meta/contradictions.md에 모음 (disputed 판정은 전체 인제스트 뒤)

## [2026-09-16] ingest | ACRS_ML25293A458 (finish)
- 새 노트 2 (노심 설계 검토, 반응도 제어 검토)
- AST 약어 불일치를 meta/contradictions.md C7에 모음
- ACRS_ML25293A458 ingest complete; status.md 갱신

## [2026-09-16] feat | 그림 정책: figures/ 폴더와 검사 도구
- references/figures의 렌더링 그림 73개를 figures/<KEY>_<name>.png로 복사 (scripts/collect_figures.py, withheld 그림은 PNG가 없어 제외)
- lint L08이 figures/의 embed를 찾도록 수정, verify_quotes V1이 원문 사실의 그림 embed 줄을 허용 (테스트 추가)
- CLAUDE.md §2 구조표와 §4 그림 규칙 갱신 (2026-09-16 사용자 결정)

## [2026-09-16] lint | lint 조치 A7·A9와 그림 삽입
- 새 노트 4 (Cumulative_Risk_Targets, Deterministic_Safety_Analysis_Task_7d, Layers_Of_Defense, Uncertainty_Treatment), 서브에이전트 원문 대조 뒤 수정
- A9: NEI 18-04 Task 7a의 과업 번호 불일치를 meta/contradictions.md C17로 기록; A1·A4·A6은 disputed 판정과 함께 보류
- 그림 삽입: NEI 18-04 Figure 3-1–5-4, PSAR ch1 Figure 1.1-1–1.1-4·1.3-1, ch3 Figure 3.5-1, ACRS 슬라이드 7장 (노트 13)

## [2026-09-16] ingest | PSAR_ch04, PSAR_ch05 (finish)
- 소스 카드 요약 작성, ingest complete

## [2026-09-16] ingest | PSAR ch6 §6.4.1.2-§6.4.5, PSAR ch1 §1.1.4.2-§1.2·§1.4, RG 1.232 App. C
- 새 노트 23(ch6 7, ch1 8, MHTGR-DC 8), 이번 커밋의 미커밋 새 노트 60
- 검사: lint_wiki --all 오류 0(index 재생성 포함), verify_quotes --all 오류 0, sync_terms conflict 0
- 읽기 전용 검토 4회: 인용문·쪽번호·표 값 불일치 0, 해설 오류 16건 수정
- 새 모순 18건(C40-C57, 누계 57)
- 미정 용어 후보 20건 추가(meta/status.md)

## [2026-09-16] terms | 용어 반영 2026-09-16 배치 (27건)
- 영어 유지 1건: Operating Basis Earthquake(OBE), 이후 표기 약어
- 용어 아님 26건: FIRS, ISRS, SSI, SSSI, seismic anchor motion, accidental torsion, equivalent static load method, dynamic amplification factor, maximum considered earthquake, limit state design method, Lateral Force Resisting System, stay-in-place formwork, steel embedment, extraordinary events, Risk Category, design transient, Service Loading, service stress limit, core support structure, design-by-rule, design-by-analysis, conformance/compliance 상태 표기, topical report, technical report, consensus codes and standards
- 표지 12곳 부착(노트 4개), sync_terms conflict 0, lint 0, verify 0

## [2026-09-16] lint | 모순 57건 판정과 보류 lint 조치
- disputed 28건: 노트 38개의 status를 disputed로
- 기록만 25건(표기·개정판·하위 ID·교차참조 결함), 공백 4건
- A1: LBE_Risk_Significance 해설에 평균·상한 병기
- A4: Integrated_Decision_Making_Process 해설에 SR 예외 명시
- 검사: lint 0, verify_quotes 0, index 176

## [2026-10-14] audit | 첫 표본 재검증 (seed 20261014, 10/122)
- 노트 오류율 20 % (2/10), 원문 사실 항목 오류 0/417; 목표 ≤ 10 %
- 수정: MHTGR_DC_Reactor_Building_Criteria(Section VII 위치), Mechanistic_Source_Term_Conditions(원문 사실 추가), Natrium_Topical_Technical_Reports(과잉 일반화 삭제)
- 원인 조치: wiki-ingest 작성 뒤 대조 지시에 문장별 근거 줄과 배타 표현 확인 추가

## [2026-10-14] terms | 용어 반영 2026-10-14 보완 인제스트 (10건)
- 영어 유지: ERO, ERF, ED, EAL, emergency classification, emergency response functions, ingestion pathway, GV, cold trap, cesium trap
- sync_terms: 갱신 노트 0, 충돌 0

## [2026-10-16] terms | 용어 반영 2026-10-16 (6건)
- 확정: DECONTAMINATION_FACTOR=제염계수, MAJOR_ACCIDENT=주요사고, UNCERTAINTY_BAND=불확도범위
- 영어 유지: TATNF, ALTERNATIVE_SHUNT_TRIP, POOL_SCRUBBING (적절한 한국어 없음)
- sync_terms: 갱신 노트 0, 충돌 0
