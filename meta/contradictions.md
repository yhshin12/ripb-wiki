# 원문 모순 모음

모든 원문의 인제스트를 마친 뒤 disputed 여부를 한꺼번에 판정한다(2026-09-16 사용자 결정). 그때까지 새로 발견한 모순은 여기에 모으고, 노트의 `status`는 바꾸지 않는다. 이전에 사용자가 결정한 disputed(NEI 18-04: LBE_Frequency_Categories, LBE_Risk_Significance, Risk_Importance_Measures, Risk_Significant_SSC)는 그대로 둔다.

각 항목은 관련 노트의 원문 사실 절에 두 쪽 인용이 있다.

## 원문 간 수치·표기 불일치

| # | 내용 | 근거 | 관련 노트 |
|---|---|---|---|
| C1 | `RFH-ESWR-2` 95th percentile 빈도: PSAR ch3 1.61E-04, ch4 Table 4.2-2 1.31E-04 (두 PDF 글자열 확인). ch4 margin 7.53은 1.31E-04와 맞음 | [PSAR_ch03 §3.8.5.4.3 p.97], [PSAR_ch04 Table 4.2-2 p.13] | Natrium_LBE_Risk_Margins, Natrium_Risk_Significant_LBEs |
| C2 | risk-significant LBE 개수: ch4 §4.2.1.2 "Eight", Table 4.2-2 11행, ch3 요약표 11건 | [PSAR_ch04 §4.2.1.2 p.8], [PSAR_ch04 Table 4.2-2 p.13] | Natrium_Plant_Capability_DID_Evaluation |
| C3 | margin 비의 방향: ch4 표 주석은 목표 값/사건 값, NEI 18-04는 사건 값/목표 값 | [PSAR_ch04 Table 4.2-1 p.12], [NEI_18-04 §5.7.1 p.72] | Natrium_LBE_Risk_Margins |
| C4 | DL function 표기: ch4 `DL3-RR1` "Primary System Boundary including RES Barrier"와 `DL3-RR3a`, ch5 "Primary Coolant Boundary including RES Barrier"와 `DL3-RR3` | [PSAR_ch04 Table 4.2-3 p.14], [PSAR_ch05 Table 5.2-3 p.12] | Natrium_Plant_Capability_DID_Evaluation |
| C5 | Programmatic DID: ch4 §4.2.2 "are evaluated and included", §4.2.1.2와 ch1 "will be provided at the OL stage" | [PSAR_ch04 §4.2.2 p.9], [PSAR_ch04 §4.2.1.2 p.8] | Natrium_Programmatic_And_Integrated_DID |
| C6 | DL 전략: CCF 기인 DBE PIE에 적어도 한 DL (ch4) vs 둘 이상의 독립 feature (NEI 18-04, RG 1.233) | [PSAR_ch04 §4.2.1 p.7], [NEI_18-04 §5.6.2 p.69] | Natrium_Defense_Lines |
| C7 | 약어 `AST`: ACRS Alternative Shunt Trip, PSAR ch5·ch7 Anticipatory Automatic Seismic Trip System; NRC 직원의 PDC 26 판단은 AST 사용을 근거로 들고 ch5 주석은 DL4-RC6 요건이 설계에 아직 반영되지 않았다고 적음 | [ACRS_ML25293A458 Acronyms p.22], [PSAR_ch05 Table 5.2-4 Note 1 p.20] | Natrium_NRC_Review_Reactivity_Control |
| C8 | ch6 §6.1.2 RFDC–PDC 비교가 §5.3에 있다고 적으나 ch5에 RFDC 표기 없음 | [PSAR_ch06 §6.1.2 p.8], [PSAR_ch05 §5.3 p.21] | Natrium_SRDC_Summary |
| C9 | ch6 RXB 하부구조 SR·상부구조 NST vs ch5가 Reactor Building을 NSRST 기능 DL4-RR1의 SSC로 적음 (ch6 U2에서 확인) | [PSAR_ch06 §6.4.2 p.24], [PSAR_ch05 Table 5.2-4] | (미작성) |
| C10 | ch6 LBE 기술 절: §6.2 "Sections 3.4 through 3.9", §6.4.3.1.1 "Section 3.6 through 3.9" | [PSAR_ch06 §6.2 p.12] | Natrium_Reliability_Capability_Targets |
| C11 | ch5 PDC: PDC 80–82와 MHTGR-DC 70–72 대응, PDC 73 "inserted" vs RG "inerted", PDC 78 구현(질소 경계 압력차 불요) vs 기준, PDC 46 구현 요약 = PDC 45 | PSAR_ch05 §5.3 | Natrium_PDC_* |
| C12 | ch3: seismic DBA vs NEI "외부 재해로 새 DBA 없음"; straddling LBE OL 이연 vs "without deviation"; within one percent vs NEI 95th; ch3 BDBE의 alternative shunt trip credit vs ch5 DL4-RC6 미반영 | PSAR_ch03 | Natrium_DBA_List, Natrium_LBE_Selection, Natrium_BDBE_List |
| C13 | RG 1.233: C.1.b 95th vs mean; C.2.a support SSC 범위 vs NEI; PRA standard 상태 | RG_1.233 §C | RG_1233_* |
| C14 | RG 1.232 내부: SFR-DC 35 문언/근거, SFR-DC 56 문언/근거, Table 1 row 26 capacity/capability, SFR-DC 26 (2)/(3), SFR-DC 75 문구, SFR-DC 55 IHX tubing, Section VII 70–77 | RG_1.232 App.B, Table 1 | SFR_DC_*, Non_LWR_Design_Criteria_Crosswalk |
| C15 | ch1 IAC 열교환기 이름: 안전 개요 "Intermediate Heat Exchanger", 계통 설명 "Sodium-Air Heat Exchanger" | PSAR_ch01 §1.3.2.3, §1.1.4.1.5 | Natrium_Control_Heat_Removal |
| C17 | NEI 18-04 과업 번호: Task 7a 본문이 "the deterministic safety analysis in Task 7a"와 "evaluation of DID adequacy in Task 7d"라고 적으나, 결정론적 안전해석은 Task 7d, DID 평가는 Task 7e 제목에 있다 (2026-09-15 lint A9) | [NEI_18-04 §3.2.2 Task 7a p.22-23], [NEI_18-04 §3.2.2 Task 7d p.25] | LBE_Selection_Process, Deterministic_Safety_Analysis_Task_7d |
| C16 | ch11 EPZ 방법 RG 1.242 App. A vs RG 1.233 §C.4의 NEI 18-04 LBE 기반 기대; ch11에 선량 계산 기간 없음 | [PSAR_ch11 §11.3.3.1 p.53], [RG_1.233 §C.4 Emergency Preparedness p.22] | Natrium_Emergency_Preparedness_EPZ |
