# 모순 재분류 상세 메모 (2026-10-17)

`meta/contradictions.md` §판정(2026-10-17)의 근거 자료이다. 항목마다 권위 문서·신청자 문서 구분, 기준 조항과 SER 판단의 원문 인용, 한국어 메모, 노트 상태 권고를 담는다. 읽기 전용 서브에이전트 네 개가 작성했고 모든 인용은 정제본과 대조했다. 판정 원칙은 `meta/contradictions.md`를 따른다(이 파일의 "판단 보류"·"사용자 결정" 표기는 2026-10-17 원칙으로 정리되었다).


---

<!-- part a: C1–C22 -->

# 모순 재분류 C1–C22 (권위 문서 기준, 2026-10-17)

범위: `meta/contradictions.md` C1–C22(C16, C17 포함; 표에는 C17·C16이 C27 뒤에 있음). 권위 문서는 SER_KU1_CP, ACRS_ML25293A458, RG_1.232, RG_1.233, RG_1.247, RG_1.253, NEI_18-04이고, 신청자 문서는 PSAR_ch01, ch03–ch07, ch11이다.

인용 검증: 아래의 원문 인용 140건(`(새 인용)` 전부와 노트에서 가져온 문장)은 (세션 검증 스크립트)(입력 `ra\q.txt`, `ra\q2.txt`)로 정제본 `references/<KEY>_*.md`의 해당 쪽 표지 구간에 글자 그대로(공백 정규화) 있음을 확인했다(결과 ALL OK). 표 행 인용(`| … |`)은 셀 단위로 확인했다. 노트·모순 목록과 쪽이 다른 경우는 정제본 쪽 표지를 따랐다(C10의 ch6 §6.4.3.1.1은 p.38).

표기 약속: "U(표기)"는 권위 문서끼리 다르지만 그 차이가 표기·교차참조·편집 수준이고 요건 내용은 갈리지 않는 경우이다. 규칙(U → disputed 유지)을 그대로 적용할지 사용자 결정이 필요한 항목에 붙였다.

---

## C1 RFH-ESWR-2 95th percentile 빈도 (ch3 1.61E-04 대 ch4 1.31E-04)
- 분류: I
- 관련 문서: PSAR_ch03, PSAR_ch04 (신청자); SER_KU1_CP (권위, 수치 없음)
- 차이: ch3 불확실도 표는 `| 4.90E-07 | 3.40E-05 | 1.61E-04 |` [PSAR_ch03 §3.8.5.4.3 p.97], ch4 `Table 4.2-2`는 `| RFH-ESWR-2 | BDBE | 1.31E-04 | 5.05 | 9.87E-04 | 7.53 | …` [PSAR_ch04 Table 4.2-2 p.13]로 같은 LBE의 같은 양을 다르게 적는다.
- 권위 문서 확인 범위: SER_KU1_CP 전체에서 `RFH-ESWR-2`(10건)를 검색했다. SER은 95th percentile 빈도 수치를 적지 않고 범주만 적는다. (새 인용) "For RFH-ESWR-2, a BDBE with a 95th percentile frequency extending into the DBE region, the PIC barrier is assumed to have failed" [SER_KU1_CP §3.8.1.5 p.296]. 두 PSAR 값(1.61E-04, 1.31E-04)은 모두 1E-04를 넘으므로 이 SER 서술과 둘 다 맞는다. SER은 이 사건의 재평가를 OL로 미룬다: (새 인용) "The staff’s review of updated analyses for these events, including any associated DBAs, is being deferred to the OL stage based on the understanding that additional preventative controls will move this event to lower frequencies, and its frequency band will no longer extend into the DBE region." [SER_KU1_CP §3.7.1.5 p.272]. 수치를 판정할 권위 문서 조항은 없다.
- 메모(한국어): 신청자 문서 두 장이 같은 LBE의 95th percentile 빈도를 다르게 적으며(ch4 margin 7.53은 1.31E-04와 맞음), 권위 문서는 범주(DBE 영역으로 연장)만 적어 어느 값도 배제하지 않는다.
- 노트 상태: Natrium_LBE_Risk_Margins: 해제(C3도 N) | Natrium_Risk_Significant_LBEs: C1 기준 해제(범위 밖 C64 판정에 따름)

## C2 risk-significant LBE 개수 (ch4 "Eight" 대 Table 4.2-2 11행)
- 분류: I
- 관련 문서: PSAR_ch04, PSAR_ch03 (신청자); SER_KU1_CP (권위, 개수 없음)
- 차이: "Eight risk-significant LBEs are identified." [PSAR_ch04 §4.2.1.2 p.8] 대 "Table 4.2-2 presents all risk-significant LBEs." [PSAR_ch04 §4.2.1.1 p.8](표 11행).
- 권위 문서 확인 범위: SER에서 `eight|eleven|risk-significant LBE|risk significant LBE`를 검색했다. SER §4.2.1.1.1은 개수를 적지 않는다: (새 인용) "USO reported no risk-significant AOOs but identified several risk-significant DBEs and BDBEs." [SER_KU1_CP §4.2.1.1.1 p.327]. 개수를 판정할 권위 문서 조항은 없다.
- 메모(한국어): ch4 본문 개수(8)와 같은 장 표·ch3 요약표(11)가 다르며, SER은 "several"로만 적어 판정 근거가 되지 않는다.
- 노트 상태: Natrium_Plant_Capability_DID_Evaluation: 해제(C4도 I)

## C3 margin 비의 방향 (ch4 목표/사건 대 NEI 사건/목표)
- 분류: N
- 관련 문서: PSAR_ch04 (신청자); NEI_18-04, SER_KU1_CP (권위)
- 기준 조항(N): "In each case, margin is expressed as a ratio of the event’s mean value (frequency and dose) to the corresponding F-C Target value (frequency and dose)." [NEI_18-04 §5.7.1 p.72]
- 신청자 문서: "[b] Ratio of the frequency in Note [a] to the LBE mean frequency (Mean Frequency Margin)" [PSAR_ch04 Table 4.2-1 p.12]; "[d] Ratio of the dose in Note [c] to the LBE mean dose (Mean Dose Margin)" [PSAR_ch04 Table 4.2-1 p.12]
- SER 판단: (새 인용) "Based on this, the staff determined that margin evaluation is consistent with the guidance in NEI 21-07 by demonstrating that risk-significant LBEs maintain margin to the F-C target curve." [SER_KU1_CP §4.2.1.1.1 p.327]
- 메모(한국어): PSAR은 margin을 F-C Target 값/LBE 값으로 정의해 NEI 18-04 §5.7.1의 LBE 값/F-C Target 값과 역수 관계이다. SER은 margin 평가를 수용했으나 비의 방향은 언급하지 않는다.
- 노트 상태: Natrium_LBE_Risk_Margins: 해제

## C4 DL function 표기 (DL3-RR1 이름, DL3-RR3a 유무·이름)
- 분류: I
- 관련 문서: PSAR_ch04, PSAR_ch05, PSAR_ch07 (신청자); SER_KU1_CP (권위, 판정 없음)
- 차이: `| RFH-FDIV-1 | DL3-RR1 | Primary System Boundary including RES Barrier | …` [PSAR_ch04 Table 4.2-3 p.14] 대 "DL3-RR1 — Primary Coolant Boundary including RES Barrier" [PSAR_ch05 Table 5.2-3 p.12]; ch4의 `DL3-RR3a` "Ex-Vessel Handling Machine to Head Barrier Function"은 ch5 표에 없고 ch7은 "EVHM Transfer Barrier Function (SR)"로 적는다.
- 권위 문서 확인 범위: SER에서 `DL3-RR1\b|DL3-RR3a|Primary (System|Coolant) Boundary including`을 검색했다. SER은 PSAR 표기를 그대로 옮겨 적을 뿐(예: (새 인용) "DL3-RR3a – EVHM Transfer Barrier (SR)" [SER_KU1_CP §7.3.2.1.12.3 p.518], SER Table 6.1-1은 ch5 이름 "Primary Coolant Boundary including RES Barrier") 기능 이름의 정오를 판정하지 않는다. 기능 ID 명명에 관한 권위 문서 조항은 없다.
- 메모(한국어): 신청자 문서 세 장의 기능 이름·하위 ID 차이이며, SER은 ch5·ch7 이름을 섞어 인용하므로 판정 근거가 되지 않는다.
- 노트 상태: Natrium_Plant_Capability_DID_Evaluation: 해제(C2와 같음)

## C5 Programmatic DID ("evaluated and included" 대 "provided at the OL stage")
- 분류: N
- 관련 문서: PSAR_ch04, PSAR_ch01 (신청자); RG_1.253, SER_KU1_CP (권위)
- 기준 조항(N): "a. Clarification: The NRC anticipates that the DID discussion at the CP stage may be limited to plant capabilities because programmatic capabilities may not have been established yet." [RG_1.253 §C.5.a p.19]
- 신청자 문서: "Evaluation of programmatic DID will be provided at the OL stage." [PSAR_ch04 §4.2.1.2 p.8] 대 "… are evaluated and included in the design and plant programs development in Chapters 6, 7, and 8." [PSAR_ch04 §4.2.2 p.9]
- SER 판단: (새 인용) "PSAR section 4.2.2 identified that the guidelines for programmatic DID adequacy provided in section 5.8 of NEI 18-04 were evaluated and included in the design and plant programs in PSAR chapters 6, 7, and 8." [SER_KU1_CP §4.2.1.2 p.330]; "As such, the staff determined that the limited detail provided in the PSAR on programmatic DID is reasonable." [SER_KU1_CP §4.2.1.2 p.331]; "The staff will perform a more detailed evaluation of DID adequacy, including programmatic measures, at the OL" [SER_KU1_CP §4.2.2 p.331]
- 메모(한국어): RG 1.253 C.5.a는 CP 단계 DID 논의를 plant capability로 한정할 수 있게 하고, SER은 §4.2.2의 "evaluated and included"를 지침 반영으로 읽은 뒤 상세 평가를 OL로 미루었다. 따라서 권위 문서 기준으로 programmatic DID 평가는 OL 단계 사항이며, ch4 두 문장의 차이는 이 기준 안에서 해소된다.
- 노트 상태: Natrium_Programmatic_And_Integrated_DID: 해제

## C6 DL 전략 (CCF 기인 DBE PIE에 한 DL 대 둘 이상의 독립 feature)
- 분류: N
- 관련 문서: PSAR_ch04 (신청자); NEI_18-04, RG_1.233, SER_KU1_CP (권위)
- 기준 조항(N): "The guidelines in Table 5-2 require that two or more independent plant design or operational features be provided to meet the plant capability requirements." [NEI_18-04 §5.6.2 p.69]; "An important qualitative overall guideline is that two or more independent plant design or operational features be provided to meet the layer-specific guidelines for each LBE." [RG_1.233 §C.3 Plant Capability Defense in Depth p.20]
- 신청자 문서: "Among DLs 2, 3, and 4, at least one DL can mitigate any DBE PIE caused by a CCF in DL2 or DL4, with the mitigation means being independent from the effects of the initiating CCF." [PSAR_ch04 §4.2.1 p.7]
- SER 판단: "The staff noted that in this approach, DL2 and DL4 are independent from DL3, but DL2 and DL4 may include common systems and may not be fully independent." [SER_KU1_CP §4.2.1.1.2 p.329]; "The staff determined these exceptions are reasonable because they ensure at least one independent function is available beyond the initiating CCF." [SER_KU1_CP §4.2.1.1.2 p.329]
- 메모(한국어): PSAR은 DL2·DL4의 CCF로 생긴 DBE PIE에 대해 독립 수단을 하나로 두어 NEI 18-04·RG 1.233의 "two or more independent" 지침보다 낮다. SER은 이 예외를 인지하고 합리적이라고 판단했다(수용).
- 노트 상태: Natrium_Defense_Lines: 해제 | Natrium_SER_Integrated_Evaluation_Review: checked 유지(변경 없음)

## C7 AST 약어와 DL4-RC6
- 분류: 하위 항목별
### C7-a 약어 AST의 뜻
- 분류: U(표기)
- 관련 문서: ACRS_ML25293A458, SER_KU1_CP (권위); PSAR_ch05, ch07 (신청자)
- 기준 조항(U): "AST - Alternative Shunt Trip" [ACRS_ML25293A458 Acronyms p.22] 대 (새 인용) "AST Anticipatory automatic seismic trip system" [SER_KU1_CP Abbreviations and Acronyms p.10]
- 메모(한국어): 두 권위 문서가 같은 약어를 다른 기능에 쓴다. ACRS 발표는 AST를 alternative shunt trip(DL4-RC6)으로, SER은 anticipatory automatic seismic trip system(DL4-RC4)으로 정의한다. PSAR은 SER과 같다("The Anticipatory Automatic Seismic Trip System (AST) measures ground motion" [PSAR_ch07 §7.6.8.1 p.320]). 내용 면에서는 두 권위 문서가 갈리지 않는다: ACRS의 PDC 26 판단 근거("the use of AST" [ACRS_ML25293A458 PDC 26 – Reactivity Control Systems p.19], 여기서 AST = alternative shunt trip)와 SER의 PDC 26 판단 근거(아래 C7-b의 DL4-RC6 문장)가 같은 기능을 가리킨다. 규칙상 U이므로 disputed 유지 대상이나, 차이가 약어에 한정되므로 해제 여부는 사용자 결정이 필요하다.
### C7-b NRC 직원 PDC 26 판단(AST 사용) 대 ch5 주석(DL4-RC6 설계 미반영)
- 분류: N
- 기준 조항(N): "Based on the independence of the motor drive function from the gravity scram function, the diversity of CRA designs to mitigate common cause failures, and the use of AST, staff found the approach to PDC 26 acceptable." [ACRS_ML25293A458 PDC 26 – Reactivity Control Systems p.19]
- 신청자 문서: (새 인용) "The requirement has not yet been integrated into the design and is therefore not discussed further in the construction permit application." [PSAR_ch05 Table 5.2-4 Note 1 p.20]
- SER 판단: (새 인용) "This is mitigated by the CRD driveline scram follow function (DL4-RC3), which is actuated by a separate signal from RPS than the scram, as well as by the alternative shunt trip (DL4-RC6), which provides an alternate means of tripping the reactor trip breakers." [SER_KU1_CP §7.2.5.1.8 p.496]; "The following are NSRST alternative shunt trips that are identified as risk-significant defense line functions in PSAR table 5.2-4, but are not described in detail within the PSAR due to the timing of when USO added them to the PRA relative to the submittal of the PSAR:" [SER_KU1_CP §5.5 p.354]; (새 인용) "Therefore, the staff determined that the finalization of this aspect of the design can be left to the OL stage" [SER_KU1_CP §5.5 p.354]
- 메모(한국어): 권위 문서는 PDC 26 판단에서 DL4-RC6을 근거의 하나로 들지만 PSAR 설계에는 아직 반영되지 않았다. SER은 이 미반영을 인지하고 확정을 OL로 미루었다(OL 이연).
### C7-c ch7 AST 절은 DL4-RC4만 수행하고 RTB shunt trip feature로 신호를 보냄
- 분류: N(기준과 일치)
- 기준 조항: "The AST supports the NSRST function DL4-RC4, “Automatic seismic trip,” by continuously monitoring signal inputs from triaxial accelerometers and sending an isolated signal to the shunt trip feature in the RTBs when the signal inputs exceed a bi-stable setpoint." [SER_KU1_CP §7.6.8.1.7 p.584]
- 메모(한국어): ch7 서술은 SER과 같다. "shunt trip feature"라는 말이 ACRS의 "AST provides alternate means of tripping RTBs via shunt trip feature" [ACRS_ML25293A458 Gravity scram functions p.15]와 겹쳐 보이는 것은 C7-a의 약어 차이에서 생기므로 이 하위 항목은 독립 모순이 아니다.
- 노트 상태: Natrium_NRC_Review_Reactivity_Control: 유지(C7-a, 사용자 결정 필요) | Natrium_System_Anticipatory_Seismic_Trip: 유지(C7-a, 사용자 결정 필요) | Natrium_SER_IC_Electrical_Structures_Review: checked 유지

## C8 ch6 §6.1.2의 RFDC–PDC 비교 교차참조 (ch5에 RFDC 표기 없음)
- 분류: I
- 관련 문서: PSAR_ch06, PSAR_ch05 (신청자); RG_1.253, SER_KU1_CP (권위, 일반 원칙만)
- 차이: "The Required Functional Design Criteria are compared to the Principal Design Criteria (PDC) in Section 5.3 to confirm that the PDC are complete for the design." [PSAR_ch06 §6.1.2 p.8]이나 ch5 정제본에는 RFDC 표기와 비교 결과가 없다.
- 권위 문서 확인 범위: SER, RG 1.253, RG 1.233, RG 1.232에서 `RFDC|functional design criteria`를 검색했다. SER은 RFDC를 약어표에만 적고 RFDC–PDC 비교를 다루지 않는다. RG 1.253은 Chapter 5 내용에 대한 일반 원칙만 둔다: (새 인용) "For SSCs, the applicant should describe the required safety functions (RSFs), the required functional design criteria (RFDC), the PDC, and the classification of SR and NSRST SSCs." [RG_1.253 §C.6 p.19]. SER은 SRDC를 ch5 표에서 확인했다: (새 인용) "PSAR section 6.1.2 states that the SRDC are provided in PSAR tables 5.2-1, 5.2.-2 and 5.2-3 to show their connection to the SR functions." [SER_KU1_CP §6.1.1.2 p.370]
- 메모(한국어): ch6이 가리키는 비교가 ch5에 없는 교차참조 결함이다. RG 1.253 C.6의 일반 원칙(Chapter 5에 RFDC 기술)은 있으나, ch5의 SRDC 표가 이를 충족하는지에 대한 권위 문서 판단은 없다.
- 노트 상태: Natrium_SRDC_Summary: checked 유지(변경 없음)

## C9 RXB 분류 (ch6 하부 SR·상부 NST 대 ch5 Reactor Building = NSRST DL4-RR1 SSC)
- 분류: N
- 관련 문서: PSAR_ch05, ch06, ch07 (신청자); SER_KU1_CP (권위)
- 기준 조항(N): "The NSRST barrier function DL4-RR1 refers to the functional containment boundary formed around the RES by the HAA barrier, the GV, and the HAA HVAC isolation. The sub-function DL4-RR1a represents the HAA portion of the boundary." [SER_KU1_CP §7.8.1.1.8 p.594]; (새 인용) "the staff determined that the preliminary design of the RXB substructure is consistent with the six identified safety-significant functions listed at the beginning of this section." [SER_KU1_CP §7.8.1.1.8 p.594]; (새 인용) "USO classified the RXB superstructure as NST because it does not perform safety-significant PSFs." [SER_KU1_CP §7.8.1.1.10 p.594]
- 신청자 문서: "The RXB, FHB, and NCB substructures are classified as SR structures and the safety classification of the RAB substructure is NSRST." [PSAR_ch06 §6.4.2 p.24]; "The RXB superstructure is NST." [PSAR_ch06 §6.4.2 p.24]; "Reactor Building (RXB)" [PSAR_ch05 Table 5.2-4 p.19]
- 메모(한국어): SER은 구조물 분류(SR 하부구조, NST 상부구조)와 기능 분류(하부구조가 NSRST DL4-RR1·DL4-RR1a를 지원)를 구분하며, ch6·ch7은 이와 같다. ch5는 SSC를 건물 단위("Reactor Building")로 적어 단위가 거칠 뿐 SER 기준과 충돌하지 않는다.
- 노트 상태: Natrium_Building_Reactor: C9는 disputed 근거가 아님(현재 disputed는 범위 밖 C26·C28·C41 판정에 따름) | Natrium_SER_IC_Electrical_Structures_Review: checked 유지

## C10 ch6 LBE 기술 절 범위 ("3.4 through 3.9" 대 "3.6 through 3.9")
- 분류: I
- 관련 문서: PSAR_ch06 (신청자)
- 차이: "licensing basis events are described in Sections 3.4 through 3.9" [PSAR_ch06 §6.2 p.12] 대 (새 인용) "The licensing basis events are described in Section 3.6 through 3.9." [PSAR_ch06 §6.4.3.1.1 p.38](노트·모순 목록의 쪽 표기는 정제본 쪽 표지 p.38로 확인).
- 권위 문서 확인 범위: SER에서 `3.4 through 3.9`를 검색했다. SER은 PSAR 구조를 서술할 뿐이다: (새 인용) "The overall set of selected LBEs and descriptions of each LBE, including frequencies and radiological consequences, consistent with the NEI 21-07 guidance, are provided in PSAR sections 3.4 through 3.9." [SER_KU1_CP §1.3.3.3 p.43]. 절 범위를 정하는 권위 문서 조항은 없다. ch3 제목은 3.4가 LBE 선정 방법, 3.5가 LBE 요약, 3.6–3.9가 AOO·DBE·BDBE·DBA 개별 기술이다.
- 메모(한국어): 두 문장이 가리키는 절 범위가 다르나, ch3 절 구성상 3.6–3.9는 개별 LBE 기술 절이고 3.4–3.9는 방법과 요약을 포함한 범위이다.
- 노트 상태: Natrium_Reliability_Capability_Targets: checked 유지

## C11 ch5 PDC 구현과 RG 1.232
- 분류: 하위 항목별
### C11-a PDC 80–82와 MHTGR-DC 70–72 대응
- 분류: N
- 기준 조항(N): (새 인용) "Applicants may use this RG to develop all or part of the PDC and are free to choose among the ARDC, SFR-DC, or MHTGR-DC to develop each PDC after considering the underlying safety basis for the criterion and evaluating the rationale for the adaptation described in this RG." [RG_1.232 §B Purpose p.11]
- 신청자 문서: "Principal Design Criteria (PDC) were developed based on the SFR-DC in Regulatory Guide (RG) 1.232, Revision 0, …" [PSAR_ch05 §5.3 p.21]
- SER 판단: (새 인용) "Consistent with RG 1.232 appendix B, the applicant included PDC 80, PDC 81, and PDC 82 based on the unique features in the KU1 design." [SER_KU1_CP §5.4 fn17 p.350]
- 메모(한국어): PSAR §5.3은 PDC가 SFR-DC에 기반한다고만 적고 80–82가 MHTGR-DC 70–72에서 왔다는 사실을 적지 않는다. RG 1.232는 기준별로 ARDC·SFR-DC·MHTGR-DC를 골라 쓰도록 허용하고, SER은 80–82의 포함을 RG 1.232 부록 B와 일관된다고 보았다(수용).
### C11-b PDC 73 "inserted" 대 SFR-DC 73 "inerted"
- 분류: N
- 기준 조항(N): "protection, such as inerted enclosures or guard" [RG_1.232 SFR-DC 73 p.98]
- 신청자 문서: "protection, such as inserted enclosures or guard" [PSAR_ch05 §5.3.6.4 p.45]
- SER 판단: SER은 PSAR 문구를 그대로 옮긴다: (새 인용) "Systems from which sodium leakage constitutes a significant safety hazard shall include measures for protection, such as inserted enclosures or GVs." [SER_KU1_CP §7.3.2.1.10 p.517]. 이 낱말에 대한 판단은 없다.
- 메모(한국어): PSAR PDC 73 문언이 RG 1.232 SFR-DC 73의 "inerted"와 한 낱말 다르다. 원문 오기는 교정하지 않으며, SER은 차이를 지적하지 않았다.
### C11-c PDC 78 구현(질소 경계 압력차 불요) 대 기준 조건 (2)
- 분류: N
- 기준 조항(N): (새 인용) "(2) the fluid contained in the structure, system, or component is maintained at a higher pressure than the primary coolant during normal operation, anticipated operational occurrences, shutdown, and accident conditions." [RG_1.232 SFR-DC 78 p.101]
- 신청자 문서: "A pressure differential between the nitrogen and the primary coolant system in these systems is not required because leakage will not result in contaminating the nonradioactive part of the heat transport system, and leakage across the interface in either direction does not result in failure of the intended SR and NSRST functions." [PSAR_ch05 §5.3.6.9 p.48]
- SER 판단: (새 인용) "Because of this, the staff determined that the preliminary design of the SPS is consistent with PDC 78." [SER_KU1_CP §7.2.4.1.13 p.487](같은 문단은 cold trap·cell의 격리 가능성과 누설이 안전 기능 상실로 이어지지 않음을 근거로 든다)
- 메모(한국어): PSAR은 화학적으로 양립하는 질소와의 단일 passive barrier에 대해 기준 조건 (2)의 고압 유지를 요구하지 않는다고 적어 SFR-DC 78 조건과 다르다. SER은 격리 가능성과 기능 영향 부재를 근거로 PDC 78과 일관된다고 판단했다(수용).
### C11-d PDC 46(시험) 구현 요약 = PDC 45(검사) 요약
- 분류: N
- 기준 조항(N): (새 인용) "The structural and equipment cooling systems shall be designed to permit appropriate periodic functional testing to ensure (1) the structural and leaktight integrity of their components" [RG_1.232 SFR-DC 46 p.88]
- 신청자 문서: "The NHV system is designed to permit appropriate periodic inspection of its NST heat removal functions that support normal operation of safety-significant SSCs." [PSAR_ch05 §5.3.4.11 p.41](§5.3.4.10 PDC 45 요약과 같은 문장)
- SER 판단: (새 인용) "The staff determined that the preliminary NHV design is consistent with PDC 46 because safety significant SSCs are passively cooled and do not rely on active structural and equipment cooling systems during DBAs" [SER_KU1_CP §7.5.1.1.10 p.537](정제본에서는 이 문장이 §7.5.1.1.11 제목 바로 뒤에 놓여 있으나 내용은 PDC 46 판정이다)
- 메모(한국어): PDC 46의 이행 요약이 시험이 아니라 검사를 적어 기준의 periodic functional testing과 대응하지 않는다. SER은 safety-significant SSC가 피동 냉각되어 능동 냉각에 의존하지 않는다는 이유로 PDC 46과 일관된다고 판단했다(수용).
- 노트 상태: Natrium_PDC_Development, Natrium_PDC_Additional, Natrium_PDC_Fluid_Heat_Transport: checked 유지(변경 없음)

## C12 ch3 LBE 방법론 관련 다섯 하위 항목
- 분류: 하위 항목별
### C12-a seismic DBA 대 "외부 재해로 새 DBA 없음"
- 분류: N
- 기준 조항(N): "With the understanding that SR SSCs are required to be capable of performing their RSFs in response to external events within the DBEHL, there will be no new DBAs introduced by external hazards." [NEI_18-04 §3.2.2 Task 6 p.22]; "The PRA results, including consideration of external hazards, will also validate a designer’s initial selections of DBAs and SR SSCs protected against DBEHLs, and ensure no new DBAs are introduced by external hazards." [RG_1.233 §C.1.c p.14]
- 신청자 문서: (새 인용) "The phenomena caused by the design basis seismic hazard are not covered by other DBA evaluations, so a seismic DBA was developed." [PSAR_ch03 §3.4 p.52]
- SER 판단: (새 인용) "There are no DBEs related to this DBA, which was added to address design basis hazards associated with a seismic event at the CP stage as discussed in PSAR section 3.4." [SER_KU1_CP §3.8.1.3 p.292]; (새 인용) "Based on the staff’s review described above, the staff concluded that the information provided relative to the reactivity DBA was consistent with the guidance provided in NEI 21-07" [SER_KU1_CP §3.8.1.3 p.293]
- 메모(한국어): PSAR은 외부 재해(설계기준 지진)에서 DBA(SEV-SSE-CN)를 새로 두어 NEI 18-04 Task 6·RG 1.233 C.1.c의 기대와 다르다. SER은 이 DBA를 이탈로 지적하지 않고 검토해 NEI 21-07과 일관된다고 판단했다(수용).
### C12-b straddling LBE의 DBA OL 이연 대 "without deviation"
- 분류: N
- 기준 조항(N): "An LBE with a mean frequency less than 1E-04/plant-year with a 95th percentile above 1E-04/plant-year is evaluated as a BDBE and a DBE." [NEI_18-04 §3.2.2 Task 7a p.22]
- 신청자 문서: "is implemented without deviation for licensing basis event (LBE) selection and evaluation." [PSAR_ch03 §3.4 p.52]
- SER 판단: "The second deviation from RG 1.233 was that USO did not generate DBAs for AOOs and BDBEs with frequency bands that extend into the DBE region when identifying and classifying LBEs." [SER_KU1_CP §3.4.1 p.225]; "USO updated its process to identify DBAs for AOOs and BDBEs with uncertainty bands that extend into the DBE region for its OL application as stated in section 3.9 of the PSAR." [SER_KU1_CP §3.4.1 p.226]
- 메모(한국어): PSAR은 경계에 걸친 LBE의 DBA를 OL로 미루면서 방법론 이탈이 없다고 적는다. SER은 이를 RG 1.233에서의 이탈로 지적하고, OL 신청에서 고친 절차를 쓰는 것으로 정리했다(이탈 지적 + OL 이연).
### C12-c "within one percent of the F-C target"(95th 미지정) 대 95th percentile 기준
- 분류: N
- 기준 조항(N): "To consider the effects of uncertainties, the applicant should use the upper 95th percentile estimates of both frequency and dose." [RG_1.233 §C.1 p.13]; "In the LMP framework, an AOO, DBE, or BDBE is regarded as risk-significant if the combination of the upper bound (95%tile) estimates of the frequency and consequence of the LBE are within 1% of the F-C Target AND the upper bound 30-day TEDE dose at the EAB exceeds 2.5 mrem." [NEI_18-04 §6 p.90]
- 신청자 문서: "LBEs are classified as risk-significant if the LBE site boundary dose exceeds 2.5 mrem over 30 days and the frequency of the dose is within one percent of the F-C target." [PSAR_ch03 §3.5.1 p.53]
- SER 판단: (새 인용) "PSAR table 4.2-2 provides the margins from the 95th percentile frequency and risk to the F-C target curve for LBEs identified as risk significant based on the 95th percentile risk." [SER_KU1_CP §4.2.1.1.1 p.327]; "Based on this, the staff determined that margin evaluation is consistent with the guidance in NEI 21-07 …" [SER_KU1_CP §4.2.1.1.1 p.327]
- 메모(한국어): ch3 문장은 NEI 18-04 Task 7c 문장("… and the frequency of the dose is within 1% of the F-C Target." [NEI_18-04 §3.2.2 Task 7c p.24])을 거의 그대로 옮겨 percentile을 지정하지 않으나, RG 1.233 C.1과 NEI 18-04 용어집은 95th percentile을 지정한다. PSAR ch4 Table 4.2-2는 95th percentile로 판정한 LBE를 싣고 SER은 이를 수용했다. Task 7c의 "within 1%"와 §4.2.2의 "exceeds 1%" 문제는 NEI 18-04 내부 후보로 별도 판정 대상이다.
### C12-d ch3 BDBE의 alternative shunt trip credit 대 ch5 DL4-RC6 설계 미반영
- 분류: N
- 기준 조항(N, SER): "With the frequencies and consequences included in the PSAR analyses, evaluation of this DBA is anticipated to elevate the alternative shunt trip credited in this LBE from NSRST to SR." [SER_KU1_CP §3.7.1.1 p.264]
- 신청자 문서: "The requirement has not yet been integrated into the design and is therefore not discussed further in the construction permit application." [PSAR_ch05 Table 5.2-4 Note 1 p.20]
- SER 판단: (새 인용) "Based on these considerations, the staff determined that review of this evaluation can reasonably be deferred to the OL stage based on the preliminary nature of the design." [SER_KU1_CP §3.7.1.1 p.264]; "Therefore, the staff determined that the finalization of this aspect of the design can be left to the OL stage" [SER_KU1_CP §5.5 p.354]
- 메모(한국어): ch3 BDBE는 DL4-RC6을 credit하나 ch5는 설계 미반영이라고 적는다. SER은 이 기능이 SR로 격상될 가능성까지 적고 검토와 설계 확정을 OL로 미루었다(OL 이연).
### C12-e ch1 §1.3.1·ch3 §3.4 "without deviation" 대 SER의 이탈 확인
- 분류: N
- 기준 조항(N, SER): "Two deviations from the methodology were identified based on the staff’s review." [SER_KU1_CP §3.4.1 p.225]; "USO unintentionally deviated from the LMP methodology in two ways while performing these risk-significant function determinations for the CPA" [SER_KU1_CP §5.1 p.337]
- 신청자 문서: (새 인용) "There were no deviations from the endorsed methodology or the staff positions in the regulatory guide." [PSAR_ch01 §1.3.1 p.60]; "is implemented without deviation for licensing basis event (LBE) selection and evaluation." [PSAR_ch03 §3.4 p.52]
- SER 판단: (새 인용) "determined that the identification and classification of LBEs was consistent with NEI 18-04 and RG 1.233, with the two exceptions noted above." [SER_KU1_CP §3.4.2 p.228]; "the staff determined that the impact of this second deviation on the overall design and facility risk at the CP stage is small" [SER_KU1_CP §5.1 p.337]
- 메모(한국어): PSAR은 이탈이 없다고 적으나 SER은 LBE 선정에서 두 가지, SSC 분류에서 의도치 않은 두 가지 이탈을 확인하고, 각각을 예외로 두거나 영향이 작다고 판단했다.
- 노트 상태: Natrium_DBA_List: C12 기준 해제(범위 밖 C58·C62·C64 판정에 따름) | Natrium_LBE_Selection: 해제 | Natrium_BDBE_List: C12 기준 해제(범위 밖 C46·C63·C64 판정에 따름) | Natrium_Licensing_Basis_Methodology, Natrium_SSC_Safety_Classification, Natrium_SER_LBE_Summary_Review: checked 유지

## C13 RG 1.233 내부 세 하위 항목
- 분류: 하위 항목별
### C13-a C.1 평균값 분류 대 C.1.b BDBE 하한 95th percentile
- 분류: U 아님(권위 문서 안에서 조화 문장 확인) → 해소
- 관련 문서: RG_1.233, NEI_18-04, SER_KU1_CP (권위)
- 기준 조항: "The mean values of the frequencies are used to classify the LBEs into AOOs, DBEs, and BDBE categories." [RG_1.233 §C.1 p.11]; "The F-C target and related discussions in NEI 18-04 include an upper bound event sequence frequency (i.e., 95th percentile) of 5E-07/plant-year to define the lower range of BDBEs." [RG_1.233 §C.1.b p.14]
- 조화 문장: "An event sequence family with a mean frequency less than 5E-07/plant year but with a 95%tile frequency estimate above 5E-07/plant-year is evaluated as a BDBE." [NEI_18-04 §3.2.2 Task 7a p.22]
- SER 적용: "While USO did use the 95th percentile frequency when determining which events to evaluate as BDBEs, mean frequency was used when determining which events would be classified and included in the CP application as BDBEs." [SER_KU1_CP §3.4.1 p.225](SER은 이를 첫째 이탈로 본다)
- 메모(한국어): 범주 분류는 평균값으로 하되, 평균이 5E-07 미만이어도 95th percentile이 5E-07을 넘으면 BDBE로 평가한다는 NEI 18-04 Task 7a의 경계 규칙이 두 서술을 잇는다. SER도 이 읽기로 신청자의 평균값 사용을 이탈로 판정했다. 따라서 권위 문서끼리 상충하지 않는다고 판단한다.
### C13-b C.2.a 지원 SSC 분류 범위 대 NEI 18-04 "PRA-modeled SSCs"
- 분류: 판단 보류
- 관련 문서: RG_1.233, NEI_18-04 (권위)
- 기준 조항: "The staff expects that SSCs that provide essential support (including required human actions) for SR or NSRST SSCs will be classified in a manner consistent with the higher-level function, even if the supporting SSC is not explicitly modeled in the PRA." [RG_1.233 §C.2.a p.18] 대 "Safety-significant SSCs are within the scope of the PRA-modeled SSCs and include SSCs that perform a risk-significant function and those that are needed to meet DID criteria." [NEI_18-04 §4.1 Task 3 p.43]
- 메모(한국어): RG 1.233은 NEI 18-04를 "with the following clarifications"로 승인하며(C.2 Staff Position [RG_1.233 §C.2 p.18]), C.2.a는 NEI 18-04 문장의 범위를 넘는 기대를 둔다. 권위 문서의 정의("NEI 18-04 = RG 1.233이 승인한 방법론")를 승인 조건까지 포함한 것으로 읽으면 RG 1.233 명확화가 우선하여 상충이 없고(해소), NEI 18-04 문장 자체를 독립 권위로 읽으면 U이다. 이 해석 원칙은 사용자 결정 사항이다. SER에서 지원 SSC 분류에 대한 직접 판단은 찾지 못했다(`essential support|supporting SSC` 검색).
### C13-c 비경수형원전 PRA standard 승인 상태
- 분류: U 아님(발행 시점 차이) → 해소
- 관련 문서: RG_1.233, RG_1.247, NEI_18-04, SER_KU1_CP (권위)
- 기준 조항: "However, the NRC has not yet endorsed a consensus code or standard for non-LWR PRAs." [RG_1.233 §C.1.e p.15] 대 "referred to hereafter as the ASME/ANS NLWR PRA standard, which is endorsed in this RG with exceptions" [RG_1.247 §B Reason for Issuance p.9]
- 발행일: (새 인용) "Issue Date: June 2020" [RG_1.233 p.1]; (새 인용) "Issue Date: March 2022" [RG_1.247 p.1]
- SER 적용: (새 인용) "the staff determined that the KU1 PRA was developed in a manner consistent with applicable guidance and in reasonable conformance with the non-LWR PRA standard ASME/ANS RA-S-1.4-2021, as endorsed by RG 1.247." [SER_KU1_CP §3.1.3 p.156]
- 메모(한국어): RG 1.233(2020-06)의 미승인 서술은 RG 1.247(2022-03, trial use)의 승인으로 대체되었고 SER은 RG 1.247 승인본을 적용했다. 동시점 상충이 아니므로 해소로 본다. Non_LWR_PRA_Regulatory_Role 해설의 "두 지침의 발행 순서는 이 노트가 인용한 원문에 없다"는 위 발행일 인용으로 보완할 수 있다.
- 노트 상태: RG_1233_LBE_Staff_Position: 해제(C13-a) | RG_1233_SSC_Classification_Staff_Position: 판단 보류(C13-b) | Non_LWR_PRA_Regulatory_Role: checked 유지

## C14 RG 1.232 내부 일곱 하위 항목
- 분류: 하위 항목별(모두 단일 권위 문서 RG_1.232 내부)
### C14-1 SFR-DC 35: 조문의 단일 고장 문단 대 Table 1 "Same as ARDC"
- 분류: U
- 기준 조항(U): "Suitable redundancy in components and features and suitable interconnections, leak detection, isolation, and containment capabilities shall be provided to ensure that the system safety function can be accomplished, assuming a single failure." [RG_1.232 SFR-DC 35 p.82] 대 Table 1 행 `| … | 35 | Emergency core cooling. | Emergency core cooling. | Modified for ARDC |  | Same as ARDC | …` [RG_1.232 Table 1 p.13-20](ARDC 35 조문에는 이 문단이 없음)
- 메모(한국어): Table 1은 SFR-DC 35를 ARDC와 같다고 표시하나 부록 B 조문은 ARDC 35에 없는 단일 고장 문단을 둔다. 단일 고장 요건의 적용 여부가 걸린 실질 차이이다.
### C14-2 SFR-DC 56: 조문 "reactor containment structure" 대 근거 "reactor 삭제"
- 분류: U(표기)
- 기준 조항(U): (새 인용) "Each line that connects directly to the containment atmosphere and penetrates the reactor containment structure shall be provided with containment isolation valves" [RG_1.232 SFR-DC 56 p.93] 대 "The word “primary” in the title and the text was removed, and the word “reactor” was also removed because the containment is a barrier between the fission products and the environment." [RG_1.232 SFR-DC 56 p.93]
- 메모(한국어): 근거는 조문에서 "reactor"를 지웠다고 적으나 조문에는 "reactor containment structure"가 남아 있다.
### C14-3 Table 1 행 26: 삭제 표시 "capacity" 대 GDC 제목 "capability"
- 분류: U(표기)
- 기준 조항(U): "Reactivity control system redundancy and capability." [RG_1.232 Table 1 p.13](GDC 26 열) 대 같은 행 ARDC 열의 삭제 표시 `~~redundancy and capacity~~`(Non_LWR_Design_Criteria_Crosswalk 표 행 26)
- 메모(한국어): 같은 행에서 GDC 제목은 capability, ARDC 열의 삭제 표시는 capacity로 적혀 있다. 제목 표기 차이이다.
### C14-4 SFR-DC 26 (2)/(3)
- 분류: 판단 보류
- 메모(한국어): 모순 목록은 "SFR-DC 26 (2)/(3)"이라는 표지만 남기고, 노트(SFR_DC_Reactivity_Control)와 meta 기록(lint, review_rg, git 이력)에 차이의 내용이 없다. 조문 (1)–(4)와 근거 (1)–(4)를 다시 대조했으나 서로 배제하는 문장을 특정하지 못했다(근거는 ARDC 26 번호로 서술하고 SFR-DC 26 상태는 Same as ARDC). 차이의 내용이 확인되기 전에는 분류하지 않는다.
### C14-5 SFR-DC 75: 근거가 인용하는 문구가 조문에 없음
- 분류: U(표기)
- 기준 조항(U): "Components that are part of the intermediate coolant boundary shall be designed, fabricated, erected, and tested to quality standards commensurate with the importance of the safety functions to be performed." [RG_1.232 SFR-DC 75 p.98] 대 (새 인용) "The statement “commensurate with the system’s importance to safety” clarifies that the staff expects a graded approach to be used in determining the quality requirements for the ICS." [RG_1.232 SFR-DC 75 p.98]
- 메모(한국어): 근거가 인용한 문구는 SFR-DC 75 조문에 없고 SFR-DC 77 조문에 있다. 등급별 품질 접근이라는 취지는 두 문장에서 같다.
### C14-6 SFR-DC 55: IHX tubing과 중간 계통 배관의 경계 소속
- 분류: U
- 기준 조항(U): (새 인용) "The tubing of the intermediate heat exchanger and associated intermediate coolant system piping are a part of the primary coolant boundary." [RG_1.232 SFR-DC 55 p.92] 대 (새 인용) "that penetrates containment and is not part of the primary coolant boundary (in its entirety)." [RG_1.232 SFR-DC 55 p.92], (새 인용) "The use of the term “primary” indicates that the SFR-DC is applicable to the primary cooling system, not the intermediate cooling system." [RG_1.232 SFR-DC 55 p.92]
- 메모(한국어): 같은 근거 절이 중간 계통 배관을 primary coolant boundary의 일부라고 적는 한편, 중간 계통은 SFR-DC 57이 다룰 closed system이고 SFR-DC 55는 중간 계통에 적용되지 않는다고 적는다. 격납 관통 중간 계통 배관에 55와 57 가운데 무엇이 적용되는지가 모호한 실질 차이이다.
### C14-7 Section VII "Criteria 70–77" 대 실제 70–79
- 분류: U(표기)
- 기준 조항(U): "Section VII—Additional SFR-DC (Criteria 70–77)" [RG_1.232 App.B intro p.62] 대 부록 B·Table 1의 SFR-DC 78·79 행
- 메모(한국어): 절 머리의 범위 표기(70–77)가 실제 수록 기준(70–79)과 다르다. 정제 검토(review_rg.md)는 이를 원문 오기로 기록했다.
- 노트 상태: 모두 현재 checked. 규칙(U → disputed)을 그대로 적용하면 SFR_DC_Residual_Heat_Removal_And_ECC(C14-1), SFR_DC_Reactor_Containment(C14-2, C14-6)가 disputed 대상이고, U(표기)만 걸린 SFR_DC_Intermediate_Coolant_System(C14-5), Non_LWR_Design_Criteria_Crosswalk(C14-3, C14-7)는 사용자 결정이 필요하다. SFR_DC_Reactivity_Control(C14-4)은 판단 보류.

## C15 ch1 IAC 열교환기 이름 (Intermediate Heat Exchanger 대 Sodium-Air Heat Exchanger)
- 분류: N
- 관련 문서: PSAR_ch01 (신청자); SER_KU1_CP (권위)
- 기준 조항(N, SER 서술): (새 인용) "The PSAR states that IAC provides active and passive means of controlling heat removal by pulling heat from the reactor core using the intermediate heat exchangers into the IHT and discharging them to the atmosphere through sodium-air heat exchangers." [SER_KU1_CP §1.3.3.3.2 p.43]
- 신청자 문서: "The IAC has two active modes of operation that perform the FSF of controlling heat removal by using the IAC blower to transfer heat from the IHT via the Intermediate Heat Exchanger." [PSAR_ch01 §1.3.2.3 p.63] 대 "The IHT transfers heat to the IAC through the Sodium-Air Heat Exchanger (AHX) for decay heat removal and for reactor startup and shutdown operations." [PSAR_ch01 §1.1.4.1.5 p.23]
- 메모(한국어): SER은 열 경로를 노심 → IHX → IHT → sodium-air heat exchanger → 대기로 적어, IHT에서 IAC로 가는 단계의 기기를 AHX로 둔다. ch1 §1.3.2.3은 그 단계를 IHX로 적어 SER 서술과 다르고, §1.1.4.1.5는 SER과 같다. SER 문장은 PSAR 요약 서술이며 명명에 대한 별도 판정은 아니다.
- 노트 상태: Natrium_Control_Heat_Removal: checked 유지

## C16 ch11 EPZ 방법 (RG 1.242 App. A) 대 RG 1.233 §C.4 LBE 기반 기대; 선량 기간 없음
- 분류: N
- 관련 문서: PSAR_ch11 (신청자); RG_1.233, SER_KU1_CP (권위)
- 기준 조항(N): "For non-LWRs, the spectrum of events for evaluating the need for emergency planning zones is expected to be the LBEs as described in NEI 18-04, adjusted as necessary to reflect the specific criteria in the emergency planning decision-making process (e.g., dose calculations over a period of 96 hours …)" [RG_1.233 §C.4 Emergency Preparedness p.22]
- 신청자 문서: "The guidance in RG 1.242, Appendix A, was used to determine the PEP EPZ size." [PSAR_ch11 §11.3.3.1 p.53]
- SER 판단: (새 인용) "… is projected to exceed 10 millisievert (mSv) (1 rem) total effective dose equivalent (TEDE) over" 4 days (96 hours) [SER_KU1_CP §11.3.1.1.2 p.672](NAT-3056 기준 설명); (새 인용) "This same PRA was used in the Licensing Modernization Project-based PSAR analysis." [SER_KU1_CP §11.3.1.1.2 p.674]; (새 인용) "Therefore, the staff determined that the preliminary KU1 PEP EPZ size determination analysis information is acceptable and meets the applicable PSAR preliminary plan discussion requirement in 10 CFR 50.34(a)(10)(ii)" [SER_KU1_CP §11.3.1.1.3 p.676]
- 메모(한국어): ch11은 RG 1.242 App. A 방법만 적고 RG 1.233 §C.4가 기대하는 LBE 기반 사건 범위나 선량 기간을 적지 않는다. SER은 EPZ 분석이 LMP PSAR과 같은 PRA를 쓰고 96시간 1 rem TEDE 기준을 쓴다고 확인한 뒤 수용했다. 선량 기간 공백은 SER이 채운다.
- 노트 상태: Natrium_Emergency_Preparedness_EPZ: C16 기준 해제(범위 밖 C52 판정에 따름)

## C17 NEI 18-04 과업 번호 (Task 7a 본문의 "Task 7a"·"Task 7d" 교차참조)
- 분류: U(표기)
- 관련 문서: NEI_18-04 (권위)
- 기준 조항(U): "These margins also are useful in the evaluation of DID adequacy in Task 7d." [NEI_18-04 §3.2.2 Task 7a p.22]; "… the use of a conservative dose evaluation is appropriate for the deterministic safety analysis in Task 7a …" [NEI_18-04 §3.2.2 Task 7a p.23] 대 "This task corresponds to the traditional deterministic safety analysis that is found in the DBA analysis of the license application." [NEI_18-04 §3.2.2 Task 7d p.25], "In this task, the definition and evaluation of LBEs should be used to support a RIPB evaluation of DID." [NEI_18-04 §3.2.2 Task 7e p.25]
- 메모(한국어): Task 7a 본문은 결정론적 안전해석을 Task 7a로, DID 평가를 Task 7d로 가리키나 과업 제목·본문은 각각 Task 7d, Task 7e이다. 같은 문서의 다른 곳(Task 2의 "deterministic safety analysis in Task 7d", Task 4·7a 각주의 "Task 7e")은 제목과 맞으므로 교차참조 오기 수준이다. RG 1.233과 SER에서 이 번호를 바로잡는 문장은 찾지 못했다.
- 노트 상태: LBE_Selection_Process, Deterministic_Safety_Analysis_Task_7d: 현재 checked. 규칙상 U이나 표기 한정이므로 disputed 적용 여부는 사용자 결정 필요.

## C18 DL3-RR1f FHI Seal (ch7에만 있는 ID)
- 분류: I
- 관련 문서: PSAR_ch07, PSAR_ch05 (신청자); SER_KU1_CP (권위, 판정 없음)
- 차이: `| DL3-RR1f | FHI Seal (SR) | The FHI seals to the head perform part of the primary coolant boundary barrier function. |` [PSAR_ch07 §7.3.3.2 p.207] 대 ch5 Table 5.2-3에는 DL3-RR1f가 없고 FHI는 DL3-RR1의 SSC로 적힘.
- 권위 문서 확인 범위: SER에서 `DL3-RR1f|DL3-RR1\b`를 검색했다. SER은 두 표기를 모두 쓴다: (새 인용) "PSAR section 7.3.3.2 states that the FHI has one SR function, DL3-RR1f, “FHI Seal,” related to radionuclide retention." [SER_KU1_CP §7.3.3.1.9 p.525]; (새 인용) "The staff determined the preliminary FHI design is consistent with PDC 16 because the evaluations indicate that FHI components contribute to the RES isolation function (DL3-RR1) that controls the release of radionuclides to the environment." [SER_KU1_CP §7.3.3.1.6 p.524]. 하위 ID 체계를 정하는 권위 문서 조항은 없다.
- 메모(한국어): ch7은 FHI 기능을 하위 ID DL3-RR1f로, ch5는 상위 ID DL3-RR1의 SSC로 적으며, SER은 두 표기를 모두 받아들여 판정 근거가 되지 않는다.
- 노트 상태: Natrium_System_In_Vessel_Fuel_Handling: checked 유지

## C19 DL2-RR4 이름 (ch7 "RWG Radionuclide Boundary" 대 ch5 "Gaseous Radwaste Barrier")
- 분류: I
- 관련 문서: PSAR_ch07, PSAR_ch05 (신청자); SER_KU1_CP (권위, 판정 없음)
- 차이: `| DL2-RR4 | Retain Radionuclide - RWG Radionuclide Boundary (NSRST) | …` [PSAR_ch07 §7.4.1.2 p.219] 대 "DL2-RR4 — Gaseous Radwaste Barrier" [PSAR_ch05 Table 5.2-4 p.18]
- 권위 문서 확인 범위: SER에서 `DL2-RR4`를 검색했다. SER은 ch7 이름을 옮겨 쓴다: (새 인용) "PSAR section 7.4.1.2 describes the functional requirements and design criteria related to the RWG’s NSRST function, DL2-RR4, “Retain Radionuclide – RWG Radionuclide Boundary.”" [SER_KU1_CP §7.4.1.1.3 p.528]. 기능 이름을 정하는 권위 문서 조항은 없다.
- 메모(한국어): 분류·계통이 같은 기능의 이름 차이이며, SER의 인용은 PSAR 문장의 옮김이어서 판정이 아니다.
- 노트 상태: Natrium_System_Gaseous_Radwaste_Processing: checked 유지

## C20 DL4-RR7 전원 SSC (ch5 NDC·NUP 대 ch7 NHV 절 NLV)
- 분류: N
- 관련 문서: PSAR_ch05, PSAR_ch07 (신청자); SER_KU1_CP (권위)
- 기준 조항(N, SER): (새 인용) "The NUP and NDC provide power to support the following NSRST safety functions, as shown in PSAR table 5.2-4:" [SER_KU1_CP §7.7.1.7 p.588] … (새 인용) "DL4-RR7 – Fuel Handling Building Barrier" [SER_KU1_CP §7.7.1.7 p.589]
- 신청자 문서: "The NSRST isolation dampers and valves are provided with NST power by the Nuclear Island AC Electrical Power Low Voltage System (NLV)." [PSAR_ch07 §7.5.1.3 p.230]
- SER 판단: SER은 NLV 문장을 HAA 격리(DL4-RR1 계열) 문단에 두고, DL4-RR7은 별도 문단에서 FHB 공기의 수집·여과 기능으로 다룬다: (새 인용) "PSAR section 7.5.1.3 describes that NSRST NHV valves and dampers are powered by the NST NI AC electrical power low voltage system (NLV) and are designed to fail closed upon loss of power to ensure the radionuclide retention function is accomplished." [SER_KU1_CP §7.5.1.1.13 p.538]
- 메모(한국어): SER은 DL4-RR7을 NUP·NDC가 전원을 주는 기능으로 적어 ch5·ch7 §7.7.1.2와 같고, ch7 NHV 절의 NLV 문장은 격리 damper·valve(fail closed)에 관한 것으로 읽는다. 권위 문서 기준으로 DL4-RR7 전원은 NUP·NDC이며 신청자 문서 간 차이는 해소된다.
- 노트 상태: Natrium_System_NI_HVAC: 해제(C21도 N)

## C21 PDC 64 공동 stack 배기 건물 (ch5 RXB·FHB·RAB 대 ch7 RXB·FHB·RAB·FAB)
- 분류: N
- 관련 문서: PSAR_ch05, PSAR_ch07 (신청자); SER_KU1_CP (권위)
- 기준 조항(N, SER): (새 인용) "Exhaust from these areas within the RXB, FHB, RAB, and FAB passes through a combined stack for effluent monitoring by the RMS, as described in PSAR section 7.6.6." [SER_KU1_CP §7.5.1.1.11 p.537]
- 신청자 문서: "Exhaust from the RXB, FHB, and RAB pass through a combined stack for effluent monitoring." [PSAR_ch05 §5.3.5.5 p.43] 대 "Exhaust from RXB, FHB, RAB, and FAB is through the main plant stack for effluent monitoring by the Radiation Monitoring System described in Section 7.6.6." [PSAR_ch07 §7.5.1.2 p.227]
- SER 판단: (새 인용) "Because the preliminary NHV design allows for monitoring radioactivity from effluent discharge paths during both normal operations and accident conditions, the staff determined that it is consistent with PDC 64." [SER_KU1_CP §7.5.1.1.11 p.538]
- 메모(한국어): SER의 PDC 64 평가는 FAB를 포함한 네 건물을 적어 ch7과 같고, ch5 §5.3.5.5는 FAB를 빠뜨린다. SER은 이 구성으로 PDC 64와 일관된다고 판단했다.
- 노트 상태: Natrium_System_NI_HVAC: 해제(C20과 같음)

## C22 RPS·RIS 하위 ID와 DL4-RR8 이름
- 분류: 하위 항목별
### C22-a ch7 DL3-RC1a–j 하위 ID가 ch5 표에 없음
- 분류: I
- 차이: `| DL3-RC1a | Reactor scram on high-high neutron flux | …` [PSAR_ch07 §7.6.3.2.1 p.268] 등 열 개의 하위 ID가 ch5 Table 5.2-4에 없다.
- 권위 문서 확인 범위: SER에서 `DL3-RC1[a-j]`를 검색했다. SER은 ch7 하위 ID를 그대로 쓴다(예: (새 인용) "DL3-RC1a | High-high neutron flux | XIS" [SER_KU1_CP §7.6.3.1.11.1 p.561]). 하위 ID 체계를 정하는 권위 문서 조항은 없다.
- 메모(한국어): 하위 ID 세분화 수준의 신청자 문서 간 차이이며 SER은 ch7 체계를 그대로 따른다.
### C22-b DL4-RR8 이름 (Leak Indication 대 Low Primary Sodium Level)
- 분류: I
- 차이: "DL4-RR8 — Manual SPS Pump Trip on Leak Indication" [PSAR_ch05 DL4-RR8 p.20] 대 `| DL4-RR8 | Manual SPS pump trip on low primary sodium level | …` [PSAR_ch07 §7.6.3.2.1 p.268]
- 권위 문서 확인 범위: SER에서 `DL4-RR8`을 검색했다. SER도 두 이름을 모두 쓴다: (새 인용) "DL4-RR8, Manual SPS Pump Trip on Low Primary Sodium Level (NSRST)" [SER_KU1_CP §7.2.4.1.14.1 p.487]; (새 인용) "DL4-RR8 – Manual Sodium Processing System Pump Trip on Leak Indication" [SER_KU1_CP §7.7.1.7 p.589]. 이름을 판정할 권위 문서 조항은 없다.
- 메모(한국어): 같은 ID에 서로 다른 개시 조건 이름이 붙어 있고 SER도 두 이름을 각 절에서 옮겨 적어 판정 근거가 되지 않는다.
- 노트 상태: Natrium_System_Reactor_Protection, Natrium_System_Reactor_Instrumentation: C22는 disputed 근거가 아님(범위 밖 C24·C25 판정에 따름) | Natrium_System_NI_Auxiliary_Electrical: checked 유지

---

## 표 1. 항목별 분류 요약

| 항목 | 하위 항목 | 분류 | 기준 권위 문서 / 근거 | SER 판단 |
|---|---|---|---|---|
| C1 | — | I | 수치 판정 조항 없음 | OL 이연(사건 재평가) |
| C2 | — | I | 개수 판정 조항 없음 | 없음("several") |
| C3 | — | N | NEI_18-04 §5.7.1 | margin 평가 수용(방향 언급 없음) |
| C4 | — | I | 명명 조항 없음 | 없음(두 이름 혼용) |
| C5 | — | N | RG_1.253 §C.5.a | 수용, OL 상세 평가 |
| C6 | — | N | NEI_18-04 §5.6.2, RG_1.233 §C.3 | 예외 수용 |
| C7 | a 약어 | U(표기) | ACRS Acronyms 대 SER Abbreviations | — |
| C7 | b PDC 26·DL4-RC6 | N | ACRS PDC 26 | OL 이연 |
| C7 | c ch7 AST 절 | N(기준과 일치) | SER §7.6.8.1.7 | 일관 |
| C8 | — | I | RG_1.253 §C.6 일반 원칙만 | 없음 |
| C9 | — | N | SER §7.8.1.1.8, §7.8.1.1.10 | 일관 |
| C10 | — | I | 절 범위 조항 없음 | 없음 |
| C11 | a PDC 80–82 | N | RG_1.232 §B | 수용 |
| C11 | b PDC 73 inserted | N | RG_1.232 SFR-DC 73 | 언급 없음 |
| C11 | c PDC 78 질소 | N | RG_1.232 SFR-DC 78 (2) | 수용 |
| C11 | d PDC 46 | N | RG_1.232 SFR-DC 46 | 수용 |
| C12 | a seismic DBA | N | NEI_18-04 Task 6, RG_1.233 §C.1.c | 수용 |
| C12 | b straddling LBE | N | NEI_18-04 Task 7a | 이탈 지적 + OL 이연 |
| C12 | c within one percent | N | RG_1.233 §C.1, NEI_18-04 §6 | 수용(95th 표) |
| C12 | d DL4-RC6 credit | N | SER §3.7.1.1 | OL 이연 |
| C12 | e without deviation | N | SER §3.4.1, §5.1 | 이탈 지적(예외·영향 작음) |
| C13 | a 평균 대 95th | U 아님(조화) | NEI_18-04 Task 7a 경계 규칙 | 같은 읽기로 이탈 판정 |
| C13 | b 지원 SSC | 판단 보류 | RG_1.233 §C.2.a 대 NEI_18-04 §4.1 | 없음 |
| C13 | c PRA standard | U 아님(시점) | RG_1.247(2022) > RG_1.233(2020) | RG 1.247 적용 |
| C14 | 1 SFR-DC 35 | U | RG_1.232 내부 | — |
| C14 | 2 SFR-DC 56 | U(표기) | RG_1.232 내부 | — |
| C14 | 3 Table 1 row 26 | U(표기) | RG_1.232 내부 | — |
| C14 | 4 SFR-DC 26 (2)/(3) | 판단 보류 | 차이 내용 미확인 | — |
| C14 | 5 SFR-DC 75 | U(표기) | RG_1.232 내부 | — |
| C14 | 6 SFR-DC 55 | U | RG_1.232 내부 | — |
| C14 | 7 Section VII | U(표기) | RG_1.232 내부 | — |
| C15 | — | N | SER §1.3.3.3.2 서술 | 명명 판정 없음 |
| C16 | — | N | RG_1.233 §C.4 | 수용(96 h, 같은 PRA) |
| C17 | — | U(표기) | NEI_18-04 내부 | — |
| C18 | — | I | 하위 ID 조항 없음 | 없음(두 표기 수용) |
| C19 | — | I | 명명 조항 없음 | 없음 |
| C20 | — | N | SER §7.7.1.7 | 일관 |
| C21 | — | N | SER §7.5.1.1.11 | 수용 |
| C22 | a DL3-RC1a–j | I | 하위 ID 조항 없음 | 없음 |
| C22 | b DL4-RR8 이름 | I | 명명 조항 없음 | 없음(두 이름 혼용) |

집계(하위 항목 단위 40건): N 19(C3, C5, C6, C7-b, C7-c, C9, C11-a–d, C12-a–e, C15, C16, C20, C21), I 9(C1, C2, C4, C8, C10, C18, C19, C22-a, C22-b), U 2(C14-1, C14-6), U(표기) 6(C7-a, C14-2, C14-3, C14-5, C14-7, C17), U 아님·해소 2(C13-a, C13-c), 판단 보류 2(C13-b, C14-4). 합계 19 + 9 + 2 + 6 + 2 + 2 = 40.

## 표 2. 노트별 disputed 유지/해제 (C1–C22 기준)

| 노트 | 현재 status | 관련 항목(분류) | 권고 | 비고 |
|---|---|---|---|---|
| Natrium_LBE_Risk_Margins | disputed | C1(I), C3(N) | 해제 | 범위 밖 항목 없음 |
| Natrium_Risk_Significant_LBEs | disputed | C1(I) | C1 기준 해제 | 범위 밖 C64 판정에 따름 |
| Natrium_Plant_Capability_DID_Evaluation | disputed | C2(I), C4(I) | 해제 | 범위 밖 항목 없음 |
| Natrium_Programmatic_And_Integrated_DID | disputed | C5(N) | 해제 | — |
| Natrium_Defense_Lines | disputed | C6(N) | 해제 | — |
| Natrium_NRC_Review_Reactivity_Control | disputed | C7-a(U 표기), C7-b(N), C7-c(N) | 유지(규칙) | U(표기) 해제 여부 사용자 결정 |
| Natrium_System_Anticipatory_Seismic_Trip | disputed | C7-a(U 표기), C7-b(N), C7-c(N) | 유지(규칙) | U(표기) 해제 여부 사용자 결정 |
| Natrium_DBA_List | disputed | C12(N) | C12 기준 해제 | 범위 밖 C58·C62·C64 판정에 따름 |
| Natrium_LBE_Selection | disputed | C12(N) | 해제 | — |
| Natrium_BDBE_List | disputed | C12(N) | C12 기준 해제 | 범위 밖 C46·C63·C64 판정에 따름 |
| RG_1233_LBE_Staff_Position | disputed | C13-a(해소) | 해제 | 해설의 "기준 통계량이 다르다" 문장은 NEI Task 7a 경계 규칙으로 보완 필요 |
| RG_1233_SSC_Classification_Staff_Position | disputed | C13-b(판단 보류) | 보류 | RG 1.233 명확화 우선 원칙을 사용자가 정하면 해소 또는 U |
| Natrium_Emergency_Preparedness_EPZ | disputed | C16(N) | C16 기준 해제 | 범위 밖 C52 판정에 따름 |
| Natrium_System_NI_HVAC | disputed | C20(N), C21(N) | 해제 | 범위 밖 항목 없음 |
| Natrium_Building_Reactor | disputed | C9(N) | C9는 근거 아님 | disputed는 범위 밖 C26·C28·C41 판정에 따름 |
| Natrium_System_Reactor_Protection | disputed | C22(I) | C22는 근거 아님 | 범위 밖 C24 판정에 따름 |
| Natrium_System_Reactor_Instrumentation | disputed | C22(I) | C22는 근거 아님 | 범위 밖 C25 판정에 따름 |
| SFR_DC_Residual_Heat_Removal_And_ECC | checked | C14-1(U) | 규칙상 disputed 대상 | 새 disputed 지정은 사용자 확인 |
| SFR_DC_Reactor_Containment | checked | C14-2(U 표기), C14-6(U) | 규칙상 disputed 대상 | 새 disputed 지정은 사용자 확인 |
| SFR_DC_Intermediate_Coolant_System | checked | C14-5(U 표기) | 사용자 결정 | 표기 한정 |
| Non_LWR_Design_Criteria_Crosswalk | checked | C14-3, C14-7(U 표기) | 사용자 결정 | 표기 한정 |
| SFR_DC_Reactivity_Control | checked | C14-4(판단 보류) | 보류 | 차이 내용 미확인 |
| LBE_Selection_Process | checked | C17(U 표기) | 사용자 결정 | 표기 한정 |
| Deterministic_Safety_Analysis_Task_7d | checked | C17(U 표기) | 사용자 결정 | 표기 한정 |
| Non_LWR_PRA_Regulatory_Role | checked | C13-c(해소) | checked 유지 | 발행일 인용 보완 가능 |
| Natrium_SER_Integrated_Evaluation_Review, Natrium_SER_IC_Electrical_Structures_Review, Natrium_Licensing_Basis_Methodology, Natrium_SSC_Safety_Classification, Natrium_SER_LBE_Summary_Review, Natrium_SRDC_Summary, Natrium_Reliability_Capability_Targets, Natrium_PDC_Development, Natrium_PDC_Additional, Natrium_PDC_Fluid_Heat_Transport, Natrium_Control_Heat_Removal, Natrium_System_In_Vessel_Fuel_Handling, Natrium_System_Gaseous_Radwaste_Processing, Natrium_System_NI_Auxiliary_Electrical | checked | C6, C7, C9, C12, C8, C10, C11, C15, C18, C19, C22 | checked 유지 | 상태 변경 없음 |

사용자 결정이 필요한 원칙 두 가지:
1. U(표기): 권위 문서끼리의 차이가 약어·교차참조·편집 수준이고 요건 내용이 갈리지 않을 때(C7-a, C14-2, C14-3, C14-5, C14-7, C17)도 disputed로 둘지.
2. 승인 명확화 우선: RG 1.233이 NEI 18-04를 승인하며 붙인 명확화가 NEI 18-04 문장과 다를 때(C13-b) 명확화를 기준으로 보아 해소할지.

---

<!-- part b: C23–C45 -->

# 모순 재분류 C23–C45 (2026-10-17)

범례: 권위 = `SER_KU1_CP`, `ACRS_ML25293A458`, `RG_1.232`, `RG_1.233`, `RG_1.247`, `RG_1.253`, `NEI_18-04`. 신청자 = `PSAR_ch01`, `PSAR_ch03`–`PSAR_ch07`, `PSAR_ch11`. "갈래 A/B"는 2026-09-16 판정(`meta/contradictions.md` 판정 절)이다. 갈래 B 항목은 처음부터 `status`를 바꾸지 않았으므로 어떤 노트의 disputed 원인도 아니다. `(새 인용)` 표시 인용은 모두 (세션 검증 스크립트)로 정제본에 글자 그대로 있고 쪽 표지가 일치함을 확인했다(결과는 문서 끝).

## C23 RPS SVDU·수동 제어의 지진 범주 표기
- 분류: N
- 관련 문서: PSAR_ch07, PSAR_ch06 (신청자); SER_KU1_CP (권위)
- 신청자 원문: "The RPS divisional SVDUs and manual controls are classified as NSRST and are assigned seismic special treatments as part of NSRST Seismic Special Treatment Category Graded Seismic Risk Significant category A." [PSAR_ch07 §7.6.7.1.2 p.315]; "RPS Division A SVDU | NSRST | SCN1" [PSAR_ch07 Table 7.6.3-1 p.280]
- 기준 조항: (새 인용) "According to USO’s methodology and classification scheme as summarized in PSAR table 6.4-1B and section 6.4.1.1, NSRST SSCs are classified as either SCN1, SCN2, or SCN3." [SER_KU1_CP §6.4.1.1.1 p.391]
- SER 판단: (새 인용) "The staff determined that the approach to initial seismic classification is reasonable, and that the design codes associated with each seismic classification are reasonable based on the risk-informed approach described in NEI 18-04, as endorsed in RG 1.233." [SER_KU1_CP §6.4.1.1.1 p.392]
- 메모: SER이 검토·수용한 NSRST 지진 분류는 SCN1–SCN3 세 범주뿐이다. ch7 §7.6.7.1.2의 "Graded Seismic Risk Significant category A"는 이 체계에 없는 명칭이며, 같은 장 Table 7.6.3-1의 SCN1은 SER 체계와 맞는다. SER은 SVDU의 지진 범주를 따로 다루지 않는다(SER §7.6.7, §6.4.1 검색: "SVDU", "Graded", "Risk Significant category" 일치 없음).
- 노트 상태: Natrium_System_Control_Room_Indications: 해제

## C24 ch11 Table 11.5-1 계측 LCO 기능 목록에 SPS pump trip(DL3-HR11) 없음
- 분류: I
- 관련 문서: PSAR_ch11, PSAR_ch07 (신청자)
- 신청자 원문: "LCOs in this section will ensure RPS, XIS, and RIS can perform the following functions during the modes of applicability:; • reactor scram; • PSP trip; • Intermediate Sodium Pump trip" [PSAR_ch11 Table 11.5-1 p.67]
- 메모: ch11의 계측 LCO 기능 목록은 ch7 `RPS`의 SR 기능 `DL3-HR11`(SPS pump trip)을 빠뜨린다. 판정할 권위 조항이 없다. SER §11.5.1은 TS 대상 목록을 범주 수준("Instrumentation")으로만 다루고 상세 평가를 OL로 넘긴다. 근거: (새 인용) "The staff finds that USO’s probable subjects of TSs are consistent with important parameters determined as a result of the preliminary safety analyses in the PSAR, with special attention given to items (e.g., SLs, and LCOs) that may significantly influence the final design, and that the probable subjects of TSs are supported by appropriate bases." [SER_KU1_CP §11.5.1 p.701]. 검색 범위: SER §11.5, §7.6.3.1.11.5, Table 6.1-1, 전문 "Table 11.5-1"·"SPS pump trip"·"DL3-HR11".
- 노트 상태: Natrium_System_Reactor_Protection: 해제 (같은 노트의 C22는 범위 밖·갈래 B)

## C25 ch1 대 ch7 I&C 기술
- 분류: I (하위 항목 모두 I)
- 관련 문서: PSAR_ch01, PSAR_ch07 (신청자)
- (a) RV-GV 누설 탐지의 RPS 입력 여부: ch1은 "RIS also provides the RV-GV annulus liquid sodium leak detection parameters as an input to RPS." [PSAR_ch01 §1.1.4.1.14 p.26]라고 적으나 ch7 Table 7.6.5-1은 NSRST 변수로 두고 RPS 기능 표에 없다. SER §7.6.5.1.8.1의 RIS 지원 기능 목록에도 누설 탐지가 없고 SER §7.1.2(RES 누설 감시)는 탐지 수단만 적는다. 판정 조항 없음.
- (b) ch1 RPS 입력 목록에 PSP current detector 없음: SER 전문 "current detector"·"PSP current" 일치 없음. 판정 조항 없음.
- (c) ERM 문장 `off-site exposure`(ch1) 대 `personnel exposure`(ch7): SER §7.6.6은 ERM 목적 문장을 다루지 않는다(검색 "ERM", "effluent radiation monitor", "off-site exposure", "personnel exposure"). 판정 조항 없음.
- (d) CTC 명칭: ch1 "Coolant Temperature Monitoring and Control System" 대 ch7 Table 7.6.1-1 "Nuclear Island Coolant Temperature Control System". SER 약어표와 본문은 ch1 형태("coolant temperature monitoring and control system (CTC)", §7.1.3)를 쓰나 명칭을 판정하지는 않는다. 명칭 차이이므로 I로 둔다.
- 노트 상태: Natrium_System_Reactor_Instrumentation: 해제 (C22는 범위 밖·갈래 B); Natrium_System_Radiation_Monitoring: C26·C39 결과에 따름(아래 표); Natrium_System_NI_Control: C26 결과에 따름

## C26 ch7 내부 불일치 네 건
- 분류: 하위 항목별
- 관련 문서: PSAR_ch07 (신청자); SER_KU1_CP (권위)
- (a) I — FHB 이격 거리: "The SR FHB (Section 7.8.2) substructure is located approximately 40 feet east of the RXB substructure and does not affect the RXB substructure design." [PSAR_ch07 §7.8.1.1.1 p.337] 대 "As shown on the site layout plan in Figure 1.2-1, the FHB is located approximately 28 feet to the east of the Reactor Building and approximately 40 feet to the north of the Fuel Auxiliary Building." [PSAR_ch07 §7.8.2 p.345]. 앞 문장은 하부구조 간, 뒤 문장은 건물 간 거리이며 두 기준점의 관계는 vault에 없다. SER §7.8.1은 하부구조 간 40 ft만 옮겨 적고 28 ft는 다루지 않는다: (새 인용) "The substructures of the RAB and FHB are located approximately 16 ft west and 40 ft east of the RXB, respectively, and are structurally separated from the RXB." [SER_KU1_CP §7.8.1 p.590]. 판정 조항 없음.
- (b) I — XIS: Table 7.6.1-1은 "Nuclear Instrumentation System | SR | DL2, DL3, DL5" [PSAR_ch07 Table 7.6.1-1 p.250]이고, §7.6.4.2.1은 "designated as SR (for DL3 functions) or NSRST (for the DL5 function) to indicate the safety classification of RPS components relied upon to perform the function" [PSAR_ch07 §7.6.4.2.1 p.283]라고 적는다. SER §7.6.4는 XIS가 SR·NSRST 기능을 함께 수행한다고만 적고 DL2 표기나 "RPS components" 문언을 다루지 않는다. 판정 조항 없음.
- (c) N — RAB 상부구조 PDC 1: 신청자 원문 "The RAB superstructure is designed to ensure that NSRST systems and components are protected from the effects of applicable hazards defined in Section 6.1.3 and is structurally designed to meet PDC 1, PDC 2, PDC 3, and PDC 4 as described in Section 7.8.3.1.2." [PSAR_ch07 §7.8.3.2.2 p.359]이나 §7.8.3.1.2에는 PDC 2·3·4·16 문단만 있다. SER 판단: (새 인용) "the staff determined that the preliminary design information for the RAB substructure and superstructure are consistent with PDC 1, 2, and 4." [SER_KU1_CP §7.8.3.1.1 p.600]. SER은 PDC 1 부합을 판단했으므로 PSAR의 빠진 문단은 교차참조 결함으로 기록한다.
- (d) N — RG 1.180 개정판: 신청자 원문 "NIC sub-systems that are classified as NSRST fully conform to RG 1.180, Revision 4." [PSAR_ch07 §7.6.2.2 p.254], "RMS components that are classified as NSRST fully conform to RG 1.180, Revision 4." [PSAR_ch07 §7.6.6.2 p.307]이 같은 절 제목 행의 "RG 1.180, Revision 2"와 다르다. 기준: (새 인용) "RG 1.180, “Guidelines for Evaluating Electromagnetic and Radio-Frequency Interference in Safety-Related Instrumentation and Control Systems,” Rev. 2 (ML19175A044);" [SER_KU1_CP §7.6.2 p.547], (새 인용) "RG 1.180, Rev. 2." [SER_KU1_CP §7.6.6 p.576]. SER은 NIC·RMS 평가에 Rev. 2를 썼고, 부합 문장의 "Revision 4"는 SER 기준과 다르다. SER은 이 차이를 지적하지 않는다.
- 노트 상태: Natrium_Building_Reactor: 해제 (C28·C41 I, C9는 범위 밖·갈래 B); Natrium_Building_Fuel_Handling: 해제 (C38 N); Natrium_System_Nuclear_Instrumentation: 해제; Natrium_Building_Reactor_Auxiliary: 해제; Natrium_System_NI_Control: 해제; Natrium_System_Radiation_Monitoring: 해제 (C39 I)

## C27 DL3-RR10 SCG Isolation (ch5 표 주석 대 ch7 SCG 기능 표)
- 분류: N
- 관련 문서: PSAR_ch05, PSAR_ch07 (신청자); SER_KU1_CP (권위)
- 신청자 원문: "DL3-RR10 is added at the CP stage to mitigate radionuclide release from SCG pathways in the following LBEs" [PSAR_ch05 Table 5.2-3 Note 1 p.16]; ch7 SCG 표 DL3-RR1c 행 "Closure of the isolation valves is not an SR primary coolant boundary function." [PSAR_ch07 §7.2.3.2.2 p.122]
- SER 판단: "The staff audited the LBEs that rely on this function and determined that a SR SCG isolation function is appropriate for radionuclide retention." [SER_KU1_CP §7.2.3.1.15.1 p.475]; "The staff will review the integration of this function into the final design during the OL review." [SER_KU1_CP §7.2.3.1.15.1 p.475]
- 메모: SER은 `DL3-RR10`을 SR 기능으로 인정하고 설계 통합을 OL에서 검토한다. ch7 SCG 기능 표에는 `DL3-RR10`이 없고 격리 밸브 닫힘을 SR primary coolant boundary 기능이 아니라고 적어, SER이 인정한 SR 격리 기능을 아직 반영하지 않았다. ch7 문장은 `DL3-RR1c`(경계 기능)에 한정되므로 `DL3-RR10` 자체를 부정하지는 않는다.
- 노트 상태: Natrium_System_Sodium_Cover_Gas: 해제 (C29 I); Natrium_SER_Reactor_Auxiliary_Review: 현재 checked, 변경 없음

## C28 DL4-RR1 하위 ID (ch5 대 ch7)
- 분류: I
- 관련 문서: PSAR_ch05, PSAR_ch07 (신청자)
- 메모: ch5는 `DL4-RR1`·`DL4-RR1a`·`DL4-RR1b`를 따로 적고 ch7 `RES` 표는 한 행 "HAA Barrier, GV Leak Prevention Function", `RXB` 표는 `DL4-RR1`·`DL4-RR1a`를 쓴다. SER은 두 표기를 모두 그대로 옮겨 쓰고(§7.1.2.1.18.2 p.433의 RES 한 행 표기, §7.5.1.1.13 p.538·§7.8.1.1.8 p.594의 `DL4-RR1`·`DL4-RR1a`) 어느 쪽이 맞는지 판정하지 않는다. 검색 범위: SER 전문 "DL4-RR1".
- 노트 상태: Natrium_System_Reactor_Enclosure: 현재 checked, 변경 없음; Natrium_Building_Reactor: 해제 (C26 참조)

## C29 DL3-RR1 하위 ID DL3-RR1a–d가 ch5 표에 없음
- 분류: I
- 관련 문서: PSAR_ch07, PSAR_ch05 (신청자)
- 메모: ch7 `PHT`·`SPS`·`SCG` 표의 `DL3-RR1a`–`DL3-RR1d`가 ch5 Table 5.2-3에 없다. SER은 ch7의 하위 ID를 그대로 써서 각 계통을 평가하지만(§7.1.3.1.17.3 p.445 등) ch5 표의 누락을 다루지 않는다. 검색 범위: SER 전문 "DL3-RR1".
- 노트 상태: Natrium_System_Primary_Heat_Transport: C30·C31 결과에 따름; Natrium_System_Sodium_Processing: 현재 checked, 변경 없음; Natrium_System_Sodium_Cover_Gas: 해제

## C30 DL3-HR2 조건 (ch5 SRDC 대 ch7 논리)
- 분류: N
- 관련 문서: PSAR_ch05, PSAR_ch07 (신청자); SER_KU1_CP (권위)
- 기준 조항: (새 인용) "If a scram signal exists in the RPS, primary sodium cold pool temperature exceeds a setpoint, and neutron flux is below a setpoint, the PSPs (DL3-HR2) and ISPs (DL3-HR3) are tripped." [SER_KU1_CP §7.6.3.1.11.5 p.562]
- SER 판단: (새 인용) "The staff therefore determined that the preliminary RPS design is consistent with DL3-HR2 and DL3-HR3 because all LBEs relying on the RPS maintain fuel integrity and do not result in radiological release." [SER_KU1_CP §7.6.3.1.11.5 p.562]
- 메모: SER은 ch7의 세 조건(scram 신호, cold pool 온도, 저중성자속) 논리를 기준으로 RPS가 `DL3-HR2`에 부합한다고 판단했다. ch5 SRDC의 "high temperature limit with a low flux signal"은 이 논리의 일부만 적은 것으로, SER은 ch5 SRDC 문언(SE Table 6.1-1)과 ch7 논리를 함께 수용했다.
- 노트 상태: Natrium_System_Primary_Heat_Transport: 해제

## C31 ch1 대 ch7 계통 문언
- 분류: 하위 항목별
- 관련 문서: PSAR_ch01, PSAR_ch07 (신청자); SER_KU1_CP (권위)
- (a) N — IAC 역할: ch1 "The IAC is the preferred heat removal system for the reactor during upset events." [PSAR_ch01 §1.1.4.1.6 p.23] 대 ch7 "The IAC is the primary and preferred means of reactor heat removal during low power and shutdown conditions." [PSAR_ch07 §7.2.2.1 p.105]. 기준: "The IAC transfers heat from the IHT to the atmosphere and is the primary means of reactor heat removal during low power and shutdown conditions." [SER_KU1_CP §7.2.2 p.460]. SER은 ch7 기술을 따르며 ch1의 "upset events" 문언은 다루지 않는다.
- (b) I — SPS-I "same"(ch1 §1.1.4.1.8 p.24) 대 "similar"(ch7 §7.2.4.1 p.133). SER §7.2.4는 이 비교를 하지 않는다(검색 "SPS-I").
- (c) I — PHT 기능 문언 "The PHT safety function"(ch1 §1.1.4.1.4 p.22) 대 "A safety-significant function"(ch7 §7.1.3.1 p.57). SER에 해당 문장 없음(검색 "maintain primary sodium temperatures").
- (d) I — IHT–PHT 경계: ch1 "The boundary between the IHT and PHT occurs at the IHX nozzle to IHT pipe welds." [PSAR_ch01 §1.1.4.1.5 p.23] 대 ch7의 IHX 구성품 열거. SER §7.1.4는 IHX nozzle 연결 배관 위치만 적고 경계를 판정하지 않는다(검색 "IHX nozzle", "boundary between").
- 노트 상태: Natrium_System_Intermediate_Air_Cooling·Natrium_System_Sodium_Processing: 현재 checked, 변경 없음; Natrium_System_Primary_Heat_Transport: 해제

## C32 PDC 26 (1)·(2) 문구
- 분류: N
- 관련 문서: PSAR_ch03, PSAR_ch05 (신청자); RG_1.232, SER_KU1_CP (권위)
- 신청자 원문: "that the specified acceptable system radionuclide release design limits for the fission product barriers are not exceeded and safe shutdown is achieved and maintained" [PSAR_ch03 §3.12.2 p.123]; "that the specified acceptable system radionuclide release design limits are not exceeded and safe shutdown is achieved and maintained during normal operation" [PSAR_ch05 §5.3.3.7 p.33]
- 기준 조항: (새 인용) "(1) A means of inserting negative reactivity at a sufficient rate and amount to assure, with appropriate margin for malfunctions, that the design limits for the fission product barriers are not exceeded and safe shutdown is achieved and maintained during normal operation, including anticipated operational occurrences." [RG_1.232 SFR-DC 26 p.74]
- SER 판단: (새 인용) "The staff found the PDC for the Natrium plant to be acceptable, as documented in its SE included with the approved version of NATD-LIC-RPRT-0002-A." [SER_KU1_CP §5.3 p.344]; (새 인용) "(1) insert negative reactivity at sufficient rate and amount to ensure SARRDLs are not exceeded and safe shutdown is achieved and maintained for AOOs; (2) control the rate of reactivity changes during planned, normal power changes to ensure SARRDLs are not exceeded" [SER_KU1_CP §7.2.5.1.8 p.495]
- 메모: Natrium PDC 26은 RG 1.232 SFR-DC 26의 "design limits for the fission product barriers"를 SARRDL로 바꾸었고, SER은 이 PDC를 승인된 토픽 보고서를 통해 수용하고 SARRDL로 기술한다. ch5는 SER이 수용한 문언과 같고, ch3 §3.12.2는 두 표현을 합친 "SARRDL for the fission product barriers"를 써서 SER이 수용한 PDC 문언과 다르다. RG 1.232 안에서는 SFR-DC 26과 MHTGR-DC 26이 기술별로 다를 뿐 상충하지 않는다.
- 노트 상태: Natrium_Nuclear_Design: 해제 (C34 I; C37은 아래 참조)

## C33 ch3 §3.13.2의 PDC 10·15 문언
- 분류: N
- 관련 문서: PSAR_ch03, PSAR_ch05 (신청자); RG_1.232, SER_KU1_CP (권위)
- 신청자 원문: "the thermal hydraulic design provides adequate transfer of heat from the fuel to the coolant to ensure that the Specified Acceptable System Radionuclide Release Design Limits will not be exceeded during normal operation and unplanned transients." [PSAR_ch03 §3.13.2 p.125]; "the thermal hydraulic design provides adequate margin such that critical parameters of the safety-significant elements of the primary coolant boundary will not be exceeded during normal operation and anticipated operational occurrences." [PSAR_ch03 §3.13.2 p.125]
- 기준 조항: (새 인용) "The reactor core and associated coolant, control, and protection systems shall be designed with appropriate margin to assure that specified acceptable fuel design limits are not exceeded during any condition of normal operation, including the effects of anticipated operational occurrences." [RG_1.232 SFR-DC 10 p.65]; (새 인용) "The primary coolant system and associated auxiliary, control, and protection systems shall be designed with sufficient margin to ensure that the design conditions of the primary coolant boundary are not exceeded during any condition of normal operation, including anticipated operational occurrences." [RG_1.232 SFR-DC 15 p.67]
- SER 판단: (새 인용) "PDC 10 requires the reactor core and associated coolant, control, and protection systems to be designed with appropriate margin to ensure that specified acceptable system radionuclide release design limits (SARRDLs) are not exceeded during normal operation or AOOs." [SER_KU1_CP §7.1.1.1.3 p.411]; (새 인용) "PDC 15 requires the design conditions of the primary coolant boundary to not be exceeded during conditions of normal operation, including AOOs." [SER_KU1_CP §7.1.2.1.6 p.425]
- 메모: 권위 문서(RG 1.232와 SER의 PDC 기술)는 PDC 10의 적용 범위를 AOO로, PDC 15의 대상을 design conditions로 적는다. ch5는 이와 같고, ch3 §3.13.2는 "unplanned transients"와 "critical parameters"로 바꾸어 적었다. SFR-DC 10의 SAFDL이 Natrium PDC에서 SARRDL로 바뀐 것은 C32와 같은 승인된 변경이다.
- 노트 상태: Natrium_Core_Thermal_Hydraulic_Design: 해제

## C34 prompt 반응도 되먹임 항목 (4 대 5)
- 분류: I
- 관련 문서: PSAR_ch03, PSAR_ch05, PSAR_ch07 (신청자)
- 메모: ch3·ch5는 prompt 되먹임을 네 개로, ch7 §7.1.1.2는 control rod driveline axial expansion을 더한 다섯 개로 적는다. SER은 되먹임 기구를 다시 다른 목록으로 적으며 어느 것이 prompt인지 판정하지 않는다: (새 인용) "Reactivity feedback mechanisms associated with the design of RCC include Doppler, non-fuel material temperature coefficients, coolant temperature coefficients, fuel axial expansion, and fuel bowing." [SER_KU1_CP §7.1.1.1.3 p.411]. 이 목록은 판정 기준이 아니므로 I로 둔다. 검색 범위: SER §3.11.1.4, §7.1.1.1.3, 전문 "axial expansion", "driveline"; ACRS "feedback".
- 노트 상태: Natrium_Nuclear_Design: 해제; Natrium_System_Reactor_Core: 해제

## C35 임계 판정 기준 (USL 대 k_eff ≤ 0.95)
- 분류: N
- 관련 문서: PSAR_ch03, PSAR_ch07 (신청자); SER_KU1_CP (권위)
- 신청자 원문: "k<sub>eff</sub> + 2σ < USL (Equation 3.14-1)" [PSAR_ch03 §3.14.2 p.128]; "via a geometrically sub-critical configuration which limits k<sub>eff</sub> ≤ 0.95 based on the most reactive fuel configuration." [PSAR_ch07 §7.3.2.2 p.187]
- SER 판단: (새 인용) "Each of the preliminary calculations showed the maximum calculated keff remained below the applicable USL." [SER_KU1_CP §3.13.1.3 p.319]; (새 인용) "The staff determined that the preliminary FHE design is consistent with PDC 62 because it provides an acceptable means of criticality prevention based on the evaluation of the supporting criticality analyses for the EVST and NAPS, provided in SE section 3.13" [SER_KU1_CP §7.3.2.1.7 p.516]
- 메모: SER은 ex-vessel 설비를 포함해 USL 방법(ch3 §3.14.2)을 판정 기준으로 썼고, ch7 §7.3.2.2의 고정값 k_eff ≤ 0.95는 SER이 쓴 기준이 아니다. SER은 0.95 문장을 언급하지 않는다(SER 전문 "0.95" 일치 없음).
- 노트 상태: Natrium_Fuel_Criticality_Safety: 해제 (C36 N); Natrium_System_Ex_Vessel_Fuel_Handling: 해제

## C36 10 CFR 50.68(b)(7) 예외 표기
- 분류: N
- 관련 문서: PSAR_ch03, PSAR_ch07 (신청자); SER_KU1_CP (권위)
- 신청자 원문: "This section demonstrates conformance with Principal Design Criterion 62, “Prevention of Criticality in Fuel Storage and Handling” (as described in Section 5.3) and 10 CFR 50.68, except for the U-235 enrichment limit defined in 10 CFR 50.68(b)(7)." [PSAR_ch03 §3.14 p.127]; "Consistent with PDC 62, Prevention of criticality in fuel storage and handling, criticality in the fuel storage and handling system is prevented in accordance with 10 CFR 50.68(b) and the criticality analysis is described in Section 3.14." [PSAR_ch07 §7.3.1.2 p.167]
- SER 판단: (새 인용) "Therefore, the NRC hereby grants USO an exemption from the requirements of 10 CFR 50.68(b)(7) to allow the applicant to follow the requirements of 10 CFR 50.68(b) in lieu of" [SER_KU1_CP App. B.2.4 p.737]; (새 인용) "Exemption to 10 CFR 50.68(b)(7) is addressed in NAT-9403, “Regulatory Exemptions” (ML24088A084), and evaluated in appendix B of this SE." [SER_KU1_CP §3.13 p.315]
- 메모: NRC는 50.68(b)(7) 농축도 한계에 대한 면제를 부여했다. ch3는 이 예외를 적고 ch7 §7.3.1.2는 예외 없이 50.68(b) 부합으로 적어 SER의 면제 조건을 반영하지 않는다.
- 노트 상태: Natrium_Fuel_Criticality_Safety: 해제; Natrium_System_Water_Pool_Fuel_Handling: 해제

## C37 NAT-9393-A 제목
- 분류: U (제목 표기만)
- 관련 문서: ACRS_ML25293A458, SER_KU1_CP (권위); PSAR_ch03 (신청자)
- 기준 조항: (새 인용) "Demonstrated using approved TR NAT-9393-A, “Reactor Stability Methodology” (ML25211A275) reviewed by ACRS in March and April 2025" [ACRS_ML25293A458 Applicable PDCs p.11]; (새 인용) "PSAR section 3.12.1.6 incorporates by reference applicable sections of NAT-9393-A, “Stability Methodology Topical Report,” Rev. 0 (ML25211A276)" [SER_KU1_CP §7.1.1.1.3 p.411]; (새 인용) "NAT-9393‑A, “Reactor Stability Methodology,” Rev. 0 (ML25211A276)." [SER_KU1_CP §3.11 p.302]
- 메모: 권위 문서끼리 제목이 다르다. SER 안에서도 "Stability Methodology Topical Report"(§7.1.1.1.3)와 "Reactor Stability Methodology"(§3.11)가 함께 쓰이고, 표 1.8은 "Stability Methodology"이다. 새 관찰: ACRS 발표의 ML 번호는 ML25211A275, SER은 ML25211A276이다. ch3 제목은 SER §7.1.1.1.3과 같다. 내용 차이는 아니며, C37은 갈래 B로 어느 노트의 disputed 원인도 아니었다.
- 노트 상태: Natrium_Nuclear_Design: 이 항목으로는 변경 없음 (C32·C34 기준 해제); Natrium_NRC_Review_Core_Design: 현재 checked, 판단 보류 — U이지만 제목 표기만 다르므로 disputed 부여 여부는 사용자 결정 필요

## C38 ch7 RG 1.142 개정판 (FHB Rev. 2 대 NCB Rev. 3)
- 분류: N
- 관련 문서: PSAR_ch07 (신청자); SER_KU1_CP (권위)
- 신청자 원문: "The acceptance criteria for the FHB reinforced concrete structures and the SFP are in accordance with the limits defined in ACI 349-13 as modified by RG 1.142, “Safety-Related Concrete Structures for Nuclear Power Plants (Other than Reactor Vessels and Containments),” Revision 2, for the load combinations, as applicable, provided in Table 6.4-5 for SR reinforced concrete structures." [PSAR_ch07 §7.8.2.1.3 p.348]
- 기준 조항: (새 인용) "RG 1.142, Rev. 3;" [SER_KU1_CP §7.8.2 p.596] (staff가 FHB 평가에 쓴 지침 목록); NCB도 같은 목록 [SER_KU1_CP §7.8.4 p.602]
- 메모: SER은 FHB와 NCB 모두 RG 1.142 Rev. 3으로 평가했다. ch7 FHB 절의 "Revision 2"는 SER 기준과 다르고 NCB 절의 "Revision 3"은 같다. SER은 FHB 절의 개정판 차이를 지적하지 않는다.
- 노트 상태: Natrium_Building_Fuel_Handling: 해제; Natrium_Building_NI_Control: 해제

## C39 ch7 RMS 제어 ("Controls are provided by RMS" 대 "No automatic control actions")
- 분류: I
- 관련 문서: PSAR_ch07 (신청자); SER_KU1_CP 참고
- 메모: §7.6.6.2.2는 RMS가 제어를 제공한다고, §7.6.6.3은 자동 제어 동작이 없다고 적는다. SER은 두 문장을 모두 옮겨 적되 판정하지 않는다: (새 인용) "No automatic control actions are provided by RMS." [SER_KU1_CP §7.6.6.1.1 p.576]; (새 인용) "Controls are provided by RMS and NIC to maintain these variables and systems within prescribed operating ranges." [SER_KU1_CP §7.6.6.1.3 p.578]. SER의 PDC 13 판단은 감시 기능만 근거로 한다. SER 문장은 PSAR에 없는 "and NIC"를 더하는데, 이것이 수동 제어나 NIC 경유 제어를 뜻하는지는 vault에 없다. 판정 기준이 되는 권위 조항이 없으므로 I로 두되, SER이 두 문장을 그대로 담고 있다는 점은 주의 사항으로 남긴다.
- 노트 상태: Natrium_System_Radiation_Monitoring: 해제

## C40 ACI 301 판 (§6.4.2.4.1 대 Table 6.4-3)
- 분류: N
- 관련 문서: PSAR_ch06 (신청자); SER_KU1_CP (권위)
- 신청자 원문: "The structural concrete work applied in safety-significant structures is performed in accordance with ACI 301-16 (Reference 6.4-16)." [PSAR_ch06 §6.4.2.4.1 p.37]; "| ACI 301-05 | Structural Concrete Specification | X |  |" [PSAR_ch06 Table 6.4-3 p.58]
- SER 판단: (새 인용) "Concrete works follow ACI 301-16." [SER_KU1_CP §6.4.1.2.1 p.398]; (새 인용) "The staff determined that the applicant’s information on the concrete and steel material properties is acceptable because it conforms to applicable design and ASTM codes and standards." [SER_KU1_CP §6.4.1.2.1 p.398]
- 메모: SER은 safety-significant 구조물 콘크리트 공사의 기준을 ACI 301-16으로 보고 수용했다. Table 6.4-3이 SR에 ACI 301-05를 표시한 것은 SER 기준과 다르다. SER은 표의 차이를 지적하지 않고 최종 재료 확인을 OL로 넘긴다.
- 노트 상태: Natrium_Safety_Significant_Structures: 해제 (C41 I)

## C41 하부구조의 강재
- 분류: I
- 관련 문서: PSAR_ch06, PSAR_ch01, PSAR_ch07 (신청자); SER_KU1_CP 참고
- 메모: ch6은 강재 형강을 하부구조 주 부재로 쓰지 않는다고, ch1·ch7은 RXB 하부구조를 "reinforced concrete and steel"로 적는다. SER은 RXB를 "embedded concrete substructure"로 기술하면서 SR 하부구조의 강구조 설계 코드로 ANSI/AISC N690-18도 든다(§6.4.1.2.1 p.397, §7.8.1 p.590). 이 기술은 주 부재 문제를 판정하지 않으며, 두 신청자 문장이 실제로 배타적인지(강재가 매립물·거푸집일 가능성)도 vault에 없다. 검색 범위: SER §6.4.1.2.1, §7.8.1, §7.8.4, 전문 "steel shapes", "primary member".
- 노트 상태: Natrium_Safety_Significant_Structures: 해제; Natrium_Major_Structures: 현재 checked, 변경 없음; Natrium_Building_Reactor: 해제

## C42 §6.4.2.2.5의 SR 하부구조 하중조합 표 지칭 오류
- 분류: N
- 관련 문서: PSAR_ch06 (신청자); SER_KU1_CP (권위)
- 신청자 원문: "The loading combinations used for the design of concrete and structural steel of SR substructures, primarily based on ANSI/AISC N690-18 and ACI 349-13, are provided in Table 6.4-11 and Table 6.4-12." [PSAR_ch06 §6.4.2.2.5 p.29]
- 기준 조항: (새 인용) "The load combinations for SR concrete substructures are in PSAR table 6.4-5, and for structural steel in table 6.4-6." [SER_KU1_CP §6.4.1.2.1 p.397]
- 메모: SER은 SR 하부구조 조합 표를 Table 6.4-5·6.4-6으로 지칭한다. §6.4.2.2.5의 "Table 6.4-11 and Table 6.4-12"는 SER 기준과 다른 교차참조 결함이다. 원문 오기는 고치지 않는다.
- 노트 상태: Natrium_Structural_Loads_And_Combinations: C44 결과에 따름

## C43 NSRST 표(6.4-7·6.4-11) 머리 칸의 ACI 349-13
- 분류: N (SER 기준으로 불일치 아님)
- 관련 문서: PSAR_ch06 (신청자); SER_KU1_CP (권위)
- 신청자 원문: "Design Load Cases (1)(5): Load Combination Equation No. in ACI 349-13" [PSAR_ch06 Table 6.4-7 p.65-66]
- 기준 조항: (새 인용) "For extraordinary events, load combinations and factors from ACI 349-13 for concrete and ANSI/AISC N690 for steel will be used, as detailed in PSAR tables 6.4-7, 6.4-8, 6.4-11, and 6.4-12." [SER_KU1_CP §6.4.1.2.2 p.399]
- 메모: SER은 NSRST 구조물의 extraordinary events 조합에 ACI 349-13을 쓰는 것으로 읽는다. 따라서 NSRST 표의 ACI 349-13 머리 칸은 주 설계 코드 ACI 318-19와 충돌하지 않고, SER 기준에서는 해소된다.
- 노트 상태: Natrium_Structural_Loads_And_Combinations: C44 결과에 따름

## C44 OBE 취급 범위
- 분류: N
- 관련 문서: PSAR_ch06 (신청자); SER_KU1_CP (권위)
- 신청자 원문: "The overturning factor of safety, sliding factor of safety and Floatation Factor of Safety is 1.5 when OBE is used and 1.1 when SSE is used." [PSAR_ch06 Table 6.4-9 Note 4 p.69]; "The OBE is set at 1/3 of the SSE which eliminates the need for explicit response or design analysis per 10 CFR 50 Appendix S; however, the cyclic effects of OBE are included in the fatigue analysis as described in Section 6.4.3.2." [PSAR_ch06 §6.4.3.3.1 p.46]
- 기준 조항: "USO did not develop a separate seismic analysis involving the OBE in accordance with RG 1.61, because the OBE is one-third of the SSE." [SER_KU1_CP §6.4.1.1.2 p.392]
- SER 판단: (새 인용) "The staff determined that the development of the design ground motions for SR and NSRST SSCs is reasonable because, i) they rely on the seismic hazard analysis that was reviewed and accepted by the staff in SE section 2.6.2, and ii) USO is following guidance in RG 1.61 to define the OBE based on the SSE." [SER_KU1_CP §6.4.1.1.2 p.393]
- 메모: SER은 구조물을 포함한 SR SSC 전반에 대해 별도 OBE 지진해석을 하지 않는다고 기술하고 이를 수용했다. ch6 구조물 표의 OBE 계수·안전율 행은 이 기준과 문언상 맞지 않으나, SER은 같은 조합 표도 ACI 349-13·RG 1.142와 부합한다고 보았다(§6.4.1.2.1 p.397). 구조물 OBE 행의 실제 적용 여부는 vault에 없다.
- 노트 상태: Natrium_Structural_Loads_And_Combinations: 해제 (C42·C43 N, C48은 범위 밖·갈래 B); Natrium_ASME_Component_Loads_And_Limits: 해제 (C47은 범위 밖·갈래 B); Natrium_Seismic_Classification: 현재 checked, 변경 없음

## C45 RG 1.76 제목
- 분류: N
- 관련 문서: PSAR_ch06, PSAR_ch01 (신청자); SER_KU1_CP (권위)
- 신청자 원문: "| RG 1.76 | Rev. 1 | Design Basis Tornado for Nuclear Power Plants | Full |" [PSAR_ch06 Table 6.4-4 p.59-60]; "RG 1.76, “Design-Basis Tornado and Tornado Missiles for Nuclear Power Plants,” Revision 1." [PSAR_ch06 §6.4.2.2.3 p.28]
- 기준 조항: (새 인용) "RG 1.76, “Design-Basis Tornado and Tornado Missiles for Nuclear Power Plants,” Rev. 1 (ML070360253);" [SER_KU1_CP §6.1 p.361]
- 메모: SER은 RG 1.76 Rev. 1의 제목을 "Design-Basis Tornado and Tornado Missiles for Nuclear Power Plants"로 적는다. ch6 Table 6.4-4의 제목은 이와 다르고, §6.4.2.2.3과 ch1 Table 1.4-1은 같다. 이 표 행은 Natrium_Safety_Significant_Structures(원문 사실 표)에도 실려 있다.
- 노트 상태: Natrium_Tornado_Winter_Precipitation_Design: 현재 checked, 변경 없음; Natrium_RG_Conformance: 이 항목으로는 해제 가능, 최종 상태는 범위 밖 C52·C53(갈래 A) 판정에 따름

---

## 표 1. 항목별 분류 요약

| # | 분류 | 기준 권위 문서 | 비고 |
|---|---|---|---|
| C23 | N | SER §6.4.1.1.1 | 갈래 A |
| C24 | I | (없음; SER §11.5.1 범주 수준) | 갈래 A |
| C25 | I (a–d 모두) | (없음) | 갈래 A |
| C26 | (a) I, (b) I, (c) N, (d) N | SER §7.8.3.1.1, §7.6.2, §7.6.6 | 갈래 A |
| C27 | N | SER §7.2.3.1.15.1 | 갈래 A |
| C28 | I | (없음; SER은 두 표기를 옮겨 씀) | 갈래 B |
| C29 | I | (없음) | 갈래 B |
| C30 | N | SER §7.6.3.1.11.5 | 갈래 A |
| C31 | (a) N, (b) I, (c) I, (d) I | SER §7.2.2 | 갈래 B |
| C32 | N | RG 1.232 SFR-DC 26; SER §5.3, §7.2.5.1.8 | 갈래 A |
| C33 | N | RG 1.232 SFR-DC 10·15; SER §7.1.1.1.3, §7.1.2.1.6 | 갈래 A |
| C34 | I | (없음; SER 목록은 기준 아님) | 갈래 A |
| C35 | N | SER §3.13.1.3, §7.3.2.1.7 | 갈래 A |
| C36 | N | SER §3.13, App. B.2.4 | 갈래 A |
| C37 | U (제목만) | ACRS 대 SER, SER 내부 | 갈래 B, ML 번호 차이 새 관찰 |
| C38 | N | SER §7.8.2, §7.8.4 | 갈래 A |
| C39 | I | (없음; SER은 두 문장을 옮겨 씀) | 갈래 A |
| C40 | N | SER §6.4.1.2.1 | 갈래 A |
| C41 | I | (없음) | 갈래 B |
| C42 | N | SER §6.4.1.2.1 | 갈래 B |
| C43 | N (해소) | SER §6.4.1.2.2 | 갈래 B |
| C44 | N | SER §6.4.1.1.2 | 갈래 A |
| C45 | N | SER §6.1 | 갈래 B |

건수(하위 항목 단위, 23항목 → 31건): U 1, N 18, I 12, 판단 보류 0. 항목 단위로는 U 1(C37), N 13(C23, C27, C30, C32, C33, C35, C36, C38, C40, C42, C43, C44, C45), I 7(C24, C25, C28, C29, C34, C39, C41), 혼합 2(C26: I 2·N 2, C31: N 1·I 3).

## 표 2. 노트별 최종 disputed 유지/해제

| 노트 | 현재 | 범위 내 근거 항목 | 결과 | 범위 밖 의존 |
|---|---|---|---|---|
| Natrium_System_Control_Room_Indications | disputed | C23 N | 해제 | 없음 |
| Natrium_System_Reactor_Protection | disputed | C24 I | 해제 | C22(갈래 B) |
| Natrium_System_Reactor_Instrumentation | disputed | C25 I | 해제 | C22(갈래 B) |
| Natrium_System_Radiation_Monitoring | disputed | C25 I, C26(d) N, C39 I | 해제 | 없음 |
| Natrium_System_NI_Control | disputed | C25 I, C26(d) N | 해제 | 없음 |
| Natrium_Building_Reactor | disputed | C26(a) I, C28 I, C41 I | 해제 | C9(갈래 B) |
| Natrium_Building_Fuel_Handling | disputed | C26(a) I, C38 N | 해제 | 없음 |
| Natrium_System_Nuclear_Instrumentation | disputed | C26(b) I | 해제 | 없음 |
| Natrium_Building_Reactor_Auxiliary | disputed | C26(c) N | 해제 | 없음 |
| Natrium_System_Sodium_Cover_Gas | disputed | C27 N, C29 I | 해제 | 없음 |
| Natrium_System_Primary_Heat_Transport | disputed | C29 I, C30 N, C31 N/I | 해제 | 없음 |
| Natrium_Nuclear_Design | disputed | C32 N, C34 I, C37 U(갈래 B) | 해제 (C37 U를 disputed 사유로 볼지는 사용자 결정) | 없음 |
| Natrium_Core_Thermal_Hydraulic_Design | disputed | C33 N | 해제 | 없음 |
| Natrium_System_Reactor_Core | disputed | C34 I | 해제 | 없음 |
| Natrium_Fuel_Criticality_Safety | disputed | C35 N, C36 N | 해제 | 없음 |
| Natrium_System_Ex_Vessel_Fuel_Handling | disputed | C35 N | 해제 | 없음 |
| Natrium_System_Water_Pool_Fuel_Handling | disputed | C36 N | 해제 | 없음 |
| Natrium_Building_NI_Control | disputed | C38 N | 해제 | 없음 |
| Natrium_Safety_Significant_Structures | disputed | C40 N, C41 I | 해제 | 없음 |
| Natrium_Structural_Loads_And_Combinations | disputed | C42 N, C43 N, C44 N | 해제 | C48(갈래 B) |
| Natrium_ASME_Component_Loads_And_Limits | disputed | C44 N | 해제 | C47(갈래 B) |
| Natrium_RG_Conformance | disputed | C45 N | 범위 내 근거로는 해제 가능; 최종 미정 | C52·C53(갈래 A) |
| Natrium_NRC_Review_Core_Design | checked | C37 U | 판단 보류 (제목 표기 U; 갈래 B였음) | 없음 |
| Natrium_SER_Reactor_Auxiliary_Review | checked | C27 N | 변경 없음 | C60 |
| Natrium_System_Reactor_Enclosure | checked | C28 I | 변경 없음 | 없음 |
| Natrium_System_Sodium_Processing | checked | C29 I, C31 I | 변경 없음 | 없음 |
| Natrium_System_Intermediate_Air_Cooling | checked | C31 N | 변경 없음 | 없음 |
| Natrium_Major_Structures | checked | C41 I | 변경 없음 | C50 |
| Natrium_Seismic_Classification | checked | C44 N | 변경 없음 | 없음 |
| Natrium_Tornado_Winter_Precipitation_Design | checked | C45 N | 변경 없음 | 없음 |

범위 안에 U 항목으로 disputed가 유지되는 노트는 없다. Natrium_RG_Conformance만 범위 밖 갈래 A 항목(C52·C53)에 따라 최종 상태가 정해진다.

## 인용 검증

(세션 검증 스크립트) 실행 결과: 이 문서의 인용 70개(새 인용 33개, 노트 원문 사실 절에서 가져온 인용 37개)가 모두 해당 정제본에 글자 그대로 있고, 직전 쪽 표지가 인용의 쪽과 일치한다(ok 70, bad 0).

---

<!-- part c: C46–C66 -->

# 모순 재분류 C46–C66 (2026-10-17)

범위: `meta/contradictions.md` C46–C66 (21건, C65는 하위 4건으로 분리). 권위 문서 = `SER_KU1_CP`, `ACRS_ML25293A458`, `RG_1.232`, `RG_1.233`, `RG_1.247`, `RG_1.253`, `NEI_18-04`. 신청자 문서 = `PSAR_ch01`, `PSAR_ch03`–`PSAR_ch07`, `PSAR_ch11`.

모든 `(새 인용)`은 (세션 검증 스크립트)로 정제본에서 글자 그대로 확인했다(69건 중 68건 exact, 1건은 목록 줄바꿈 때문에 공백 정규화 일치; 누락 0). 쪽은 정제본 쪽 표지의 첫 번호이다. 노트 원문 사실 절에 이미 있는 인용은 `(새 인용)` 표시 없이 그 줄을 그대로 옮겼다.

분류 원칙의 적용: SER이 같은 사항을 기술하거나 판단한 경우는 SER 문장이 판정(수용·지적) 성격이 아니라 기술(description) 성격이어도 지시대로 N으로 두고, 그 성격을 메모에 밝혔다.

---

## C46 설계 과도와 LBE 대응 (ch6 과도 이름 대 ch3 사건 이름)
- 분류: I
- 관련 문서: PSAR_ch06, PSAR_ch03 (신청자). SER_KU1_CP는 설계 과도 집합을 다루나 과도–LBE 대응과 과도 이름은 다루지 않음 (권위).
- 기준 조항(N/U): 해당 없음. 확인 범위: `SER_KU1_CP` 전문에서 "design transient", "Loss of One Intermediate", "Loss of All Primary Pumps" 검색; `RG_1.253`, `NEI_18-04`, `RG_1.233`, `RG_1.232`에서 "design transient", "cyclic load" 검색. 과도와 LBE의 대응을 요구하거나 이름을 정하는 조항 없음.
- SER 관련 문장(판정 대상은 과도 집합과 횟수이며 대응표가 아님):
  - (새 인용) "During the audit, the staff confirmed the design transients and the preliminary number of occurrences for each design transient." [SER_KU1_CP §6.4.1.3 p.401]
  - (새 인용) "Based on the staff’s review, the staff determines the identified plant transients and the number of transients is appropriate for the design life." [SER_KU1_CP §6.4.1.3 p.401]
- 메모(한국어): ch6 안에서 B.3 과도 이름이 본문과 Table 6.4-16에서 다르고(Pump 대 Loop), ch3은 C.1에 해당하는 사건을 다른 이름으로 적으며, 과도 ID–LBE ID 대응표가 없다. SER은 과도 목록과 횟수를 적정하다고 보았을 뿐 이름·대응은 판단하지 않았다.
- 노트 상태: Natrium_ASME_Design_Transients: 변동 없음(checked, C46으로 disputed된 적 없음) · Natrium_BDBE_List: C46은 disputed 사유 아님(최종은 C12 판정에 따름)

## C47 ch7의 ch6 절 참조(GV·CRDM) 대 ch6 절 범위
- 분류: I
- 관련 문서: PSAR_ch07, PSAR_ch06 (신청자). SER_KU1_CP (권위)는 §6.4.4의 적용 범위만 확인.
- 기준 조항(N/U): 해당 없음. 확인 범위: `SER_KU1_CP`에서 "Section VIII", "section 6.4.3", "section 6.4.4", "CRDM … load/stress" 검색. ch7의 교차참조 자체를 판단한 문장 없음.
- SER 관련 문장:
  - (새 인용) "The applicant clarified during the audit that this section is only applicable to piping systems and piping supports that select ASME BPVC Section III as their design code." [SER_KU1_CP §6.4.1.4 p.403]
  - (새 인용) "PSAR table 7.1.2-1 states that the GV will be designed and constructed to ASME BPVC section VIII (VIII), division 1 (VIII-1)." [SER_KU1_CP §7.1.2.1.1 p.417]
- 메모(한국어): ch7은 Section VIII Division 1 GV의 해석 방법을 §6.4.3(Section III Division 5 기기)으로, CRDM 하중·응력 한계를 §6.4.4(Section III 배관)로 넘긴다. SER은 §6.4.4가 Section III 배관에만 적용된다는 신청자 설명을 기록해 ch6 쪽 범위를 확인하지만, ch7 참조의 적부는 다루지 않는다.
- 노트 상태: Natrium_ASME_Component_Loads_And_Limits: C47은 disputed 사유 아님(최종은 C44 판정에 따름) · Natrium_Piping_And_Industrial_Codes: 변동 없음(checked)

## C48 Table 6.4-6 SE 조합 범주 표기와 주석 번호
- 분류: I
- 관련 문서: PSAR_ch06 (신청자). SER_KU1_CP (권위)는 Table 6.4-5·6.4-6 하중조합을 일괄 수용.
- 기준 조항(N/U): 해당 없음. vault의 권위 문서에 하중 범주(Normal/Severe/Extreme/Abnormal)를 정하는 조항 없음(범주 정의는 ACI 349-13·ANSI/AISC N690-18 소관이며 두 표준의 원문은 vault에 없음). 확인 범위: `SER_KU1_CP`에서 "table 6.4-5", "table 6.4-6", "severe environmental", "extreme environmental", "ACI 349", "AISC N690" 검색.
- SER 관련 문장:
  - (새 인용) "The load combinations for SR concrete substructures are in PSAR table 6.4-5, and for structural steel in table 6.4-6." [SER_KU1_CP §6.4.1.2.1 p.397]
  - (새 인용) "The staff determined that USO’s information on loads and load combinations is appropriate for the design of SR structures because the load combinations and the load factors are consistent with ACI 349-13, RG 1.142, ANSI/AISC N690-18, and RG 1.243." [SER_KU1_CP §6.4.1.2.1 p.397]
- 메모(한국어): Table 6.4-6의 `S-17(6)` 범주 표기(Normal and Severe)가 Table 6.4-5 `C-9(6)`(Extreme and Abnormal)과 다르고 계수 1.4의 주석 번호가 1.6 주석을 가리키는 것은 신청자 표 내부의 표기 차이이다. SER은 하중조합과 계수가 ACI 349-13·N690-18과 일치한다고 일괄 판단했으나 범주 표기와 주석 번호는 언급하지 않았다.
- 노트 상태: Natrium_Structural_Loads_And_Combinations: C48은 disputed 사유 아님(최종은 C44 판정에 따름)

## C49 NIC 하위 계통과 DCS
- 분류: N
- 관련 문서: PSAR_ch01 (신청자), SER_KU1_CP (권위)
- 기준 조항(N/U): SER의 NIC 기술(판정 문장이 아니라 PSAR ch7 요약).
  - (새 인용) "The NIC is a group of I&C subsystems and is primarily implemented on a NI distributed control system (DCS)." [SER_KU1_CP §7.6.2 p.546]
  - (새 인용) "While most of the NIC is implemented on a DCS, it also includes controls executed outside of the DCS." [SER_KU1_CP §7.6.2 p.546]
  - SER §7.6.2의 하위 계통 목록은 AMC, CTC, FHC, PMC, RMC, UMC 여섯이며 DCS는 목록에 없다 [SER_KU1_CP §7.6.2 p.546].
- SER 판단(있으면): ch1 문구에 대한 판단 없음.
- 메모(한국어): SER은 DCS를 NIC의 구현 플랫폼으로 기술하고 하위 계통 목록에 넣지 않으므로, ch1 §1.1.4.1.15의 하위 계통 열거와 일치하고 ch1 §1.1.4.3.5의 "the primary subsystem of the NIC" 표현과 다르다. SER 기준으로는 DCS를 하위 계통이 아니라 구현 플랫폼으로 적는 것이 맞다.
- 노트 상태: Natrium_IC_Systems: 변동 없음(checked) · Natrium_Support_Systems: 변동 없음(checked). 두 노트에 SER 기준 메모 추가 대상.

## C50 PHT·IHT의 RXB·RAB 수용 목록 중복
- 분류: N
- 관련 문서: PSAR_ch01 (신청자), SER_KU1_CP (권위)
- 기준 조항(N/U): SER의 계통 위치 기술.
  - (새 인용) "because the PHT is housed within the SR RXB substructure" [SER_KU1_CP §7.1.3.1.2 p.437]
  - (새 인용) "PSAR section 7.1.4.1 states that the IHT loop piping and components are primarily located within the reactor auxiliary building (RAB), except for piping within the RXB connecting to the IHX nozzles and yard area piping connecting to the IAC AHXs." [SER_KU1_CP §7.1.4 p.446]
- SER 판단(있으면): PHT 문장은 PDC 2 부합 판단의 근거 문장이다. ch1 목록 자체에 대한 판단은 없음.
- 메모(한국어): IHT가 두 건물 목록에 모두 있는 것은 SER 기술(주로 RAB, 일부 배관은 RXB)과 일치한다. PHT를 RAB 목록에 "primary systems"로 넣은 ch1 §1.1.4.4.4는 SER이 PHT를 RXB 하부구조 안에 둔다고 적은 것과 다르다.
- 노트 상태: Natrium_Major_Structures: 변동 없음(checked) · Natrium_Reactor_Heat_Transport_Systems: 변동 없음(checked)

## C51 신청자 표기와 모회사 관계
- 분류: N (하위 2건 모두 N)
- 관련 문서: PSAR_ch01, PSAR_ch11 (신청자), SER_KU1_CP (권위)
- 기준 조항(N/U):
  - (1) 명칭: (새 인용) "Related to the U.S. SFR Owner, LLC Construction Permit Application for the Kemmerer Power Station Unit 1" [SER_KU1_CP 표제 p.1]
  - (2) 관계: (새 인용) "Although USO is a wholly owned subsidiary of TerraPower, it is a distinct legal entity." [SER_KU1_CP §8.2.1 p.621]; (새 인용) "The staff notes that while USO is a wholly owned subsidiary of TerraPower" [SER_KU1_CP §1.7 p.49]
- SER 판단(있으면): 판정 문장 없음(기술).
- 메모(한국어): (1) SER은 `U.S. SFR Owner, LLC`로 적어 ch1 §1.2와 같고 ch1 §1.1의 `US SFR Owner, LLC`와 다르다. (2) SER은 `wholly owned subsidiary`로 적어 ch11 §11.1과 같고, ch1 §1.1의 `a subsidiary`는 SER보다 덜 특정한 표현이다. 부기: SER §2.2.2에는 관계를 반대로 적은 문장이 있다 — (새 인용) "owned by TerraPower, LLC (TerraPower), a 100 percent owned subsidiary of USO, the applicant" [SER_KU1_CP §2.2.2 p.58]. 이는 SER 내부 불일치(U 후보)로 C51 범위 밖의 새 항목이며, 이번 재분류에서는 판단 보류로 둔다(contradictions.md 미기록).
- 노트 상태: Natrium_Kemmerer_Site: 변동 없음(checked) · Natrium_Plant_Overview: 변동 없음(checked) · Natrium_Project_Organization: 변동 없음(checked)

## C52 RG 1.242 부합 표시 대 OL 제출, 제목 표기
- 분류: N (하위 2건: 부합 표시 N, 제목 표기 N)
- 관련 문서: PSAR_ch01, PSAR_ch11 (신청자), SER_KU1_CP (권위)
- 기준 조항(N/U):
  - (새 인용) "which states that the analysis of the emergency planning zone (EPZ) size required in 10 CFR 50.33(g)(2) may be preliminary for CPs consistent with the preliminary design of the facility as described in the PSAR." [SER_KU1_CP §11.3 p.670] (SER이 인용한 RG 1.242 §C 항목 2.c)
  - (새 인용) "RG 1.242, “Performance-Based Emergency Preparedness for Small Modular Reactors, Non-Light-Water Reactors, and Non-Power Production or Utilization Facilities,” Rev. 0 (ML23226A036)" [SER_KU1_CP §11.3 p.669]
- SER 판단(있으면): (새 인용) "The PSAR does not state that the applicant plans to deviate from the 10 CFR 50.160 requirements or the guidance of RG 1.242." [SER_KU1_CP §11.3 p.669]
- 메모(한국어): SER은 RG 1.242가 CP 단계의 예비 EPZ 크기 분석과 예비 계획에 적용되는 지침 항목을 가진다고 보고 그 지침으로 CP 신청을 평가했으며 이탈이 없다고 적었다. 따라서 Table 1.4-1의 `Full Conformance`와 ch11의 "계획은 OL 단계 제출"은 SER 기준에서 양립하며, §1.4.1의 "OL 단계 대상 RG는 부합 표시 없음" 규칙과의 차이는 신청자 표기 관행의 문제로 남는다. 제목은 SER 표기(`Performance-Based`, `Non-Light-Water Reactors`)와 비교하면 Table 1.4-1은 `Non-Light-Water-Reactors`, ch11은 `Performance Based`로 각각 한 곳씩 다르다.
- 노트 상태: Natrium_RG_Conformance: 해제(C52·C53 모두 N, C45는 갈래 B) · Natrium_Emergency_Preparedness_EPZ: C52 측은 해제, 최종은 C16 판정에 따름

## C53 RG 1.8·1.114·5.84: OL 단계 표시 대 ch11 현재형 적용
- 분류: N
- 관련 문서: PSAR_ch01, PSAR_ch11 (신청자), SER_KU1_CP (권위)
- 기준 조항(N/U) 및 SER 판단:
  - RG 1.8: (새 인용) "The staff determined that the PSAR proposes education and experience requirements for key personnel that are consistent with the guidance of RG 1.8 and therefore that the application is consistent with criterion 11.2(g)." [SER_KU1_CP §11.1.1.7 p.662]; 같은 SER은 Table 1.4-1의 OL 표시도 기록한다 — (새 인용) "Radiation protection training is addressed by PSAR table 1.4-1, which states that conformance with RG 8.27, “Radiation Protection Training for Personnel at Light-Water-Cooled Nuclear Power Plants,” Rev. 0 (ML003739628), and RG 1.8, “Qualification and Training of Personnel for Nuclear Power Plants” Rev. 4 (ML19101A395), will be addressed at the OL stage." [SER_KU1_CP §10.1.1 p.647]
  - RG 1.114: (새 인용) "PSAR section 11.1.5.3 states that the rules of practice for control room activities, as described by administrative procedures, incorporate the guidance of RG 1.114." [SER_KU1_CP §11.1.1.9 p.662]; (새 인용) "The staff determined that the applicant has described preliminary plans for licensed operator staffing to the extent warranted for a PSAR as required under 10 CFR 50.34(a)(6) and that further review of compliance with the staffing requirements of 50.54(m) would occur as part of the staff’s review of a future OL application." [SER_KU1_CP §11.1.1.9 p.663]
  - RG 5.84: (새 인용) "The staff therefore determined that the FFD program description contained in PSAR section 11.6.1 defines adequate FFD program measures for the worker population identified in 10 CFR 26.4(f)." [SER_KU1_CP §11.6.1.6 p.707]
- 메모(한국어): SER은 ch11의 현재형 서술(RG 1.8이 승인한 ANSI/ANS-3.1, RG 1.114 지침, RG 5.84가 승인한 NEI 06-06)을 CP 단계 예비 계획으로 평가해 수용하고, 동시에 Table 1.4-1의 OL 단계 표시도 기록한다. SER 기준에서 두 서술은 "CP 단계 예비 약속 + OL 단계 부합 입증"으로 양립하며, 신청자 문서의 차이는 Table 1.4-1이 CP 단계 약속을 표시하지 않는 데 있다.
- 노트 상태: Natrium_RG_Conformance: 해제 · Natrium_Operating_Organization: 해제(C53만 해당) · Natrium_Security_And_Fitness_For_Duty: 해제(C53만 해당)

## C54 Table 1.4-4 50.34(f)(3)(ii) 행의 Section 칸 `11.4`
- 분류: N
- 관련 문서: PSAR_ch01, PSAR_ch11 (신청자), SER_KU1_CP (권위)
- 기준 조항(N/U):
  - (새 인용) "The QA list is discussed in section 2 of TR TP-QA-PD-0001 which is incorporated by reference into the PSAR as shown in PSAR table 1.4-2." [SER_KU1_CP Table 1.8-3 p.51-54]
- SER 판단(있으면): (새 인용) "As stated in the QA TR, the list includes all SR and NSRST SSCs, which as discussed in staff position C.6.a.(2) of RG 1.253 includes both SR and NSRST SSCs. Based on this, the staff determined that 10 CFR 50.34(f)(3)(ii) is met as discussed in the QA TR, which is incorporated by reference into the PSAR." [SER_KU1_CP Table 1.8-3 p.51-54]
- 메모(한국어): SER은 (f)(3)(ii)의 근거를 §11.4가 아니라 참조 포함된 QA TR(TP-QA-PD-0001 section 2)로 두고 충족으로 판단했다. Table 1.4-4의 Section 칸 `11.4`(Aircraft Impact Assessment)는 SER이 근거로 든 위치와 다르다. QA TR 원문은 vault에 없다.
- 노트 상태: Natrium_TMI_Requirements: 변동 없음(checked; C54는 갈래 C로 disputed 사유 아님). SER 기준 메모 추가 대상.

## C55 Table 1.4-4 50.34(f)(2)(xvii) 행의 Section 칸 `11.2`
- 분류: N
- 관련 문서: PSAR_ch01, PSAR_ch11 (신청자), SER_KU1_CP (권위)
- 기준 조항(N/U):
  - (새 인용) "Although KU1 uses a functional containment, PSAR table 1.4-4 notes that portions of this item (i.e., those related to containment pressure, containment radiation intensity, and providing for effluent monitoring) are applicable. See section 11.2 of this SE." [SER_KU1_CP Table 1.8-3 p.51-54]
  - (새 인용) "Section 11.2 of the PSAR incorporates by reference, in its entirety, NAT-2965-A." [SER_KU1_CP §11.2.1.3 p.669]
- SER 판단(있으면): (새 인용) "The staff determined that the applicant has described how the design would satisfy the technically relevant requirements of 10 CFR 50.34(f) to an extent that is reasonable for a PSAR and that further evaluation of the completed implementation of these items can occur as part of the OL application." [SER_KU1_CP §11.2.1.3 p.669]
- 메모(한국어): SER은 (f)(2)(xvii)를 PSAR §11.2가 참조 포함한 NAT-2965-A(HFE 프로그램)를 통해 평가하고 CP 단계 수준으로 충분하다고 판단했으며 완료 평가를 OL로 미루었다. 따라서 §11.2 본문에 격납 계측 서술이 없는 것은 내용이 참조 포함 TR에 있다는 SER 기술로 설명된다. NAT-2965-A 원문은 vault에 없다. 부기: SER Table 1.8-3에는 `10 CFR 50.34(f)(2)(xvii)` 행이 두 번 있고 둘째 행은 "In-plant Radiation Monitoring | 10.1"이다(SER 표 내부 표기; 이번 판정 대상 아님).
- 노트 상태: Natrium_TMI_Requirements: 변동 없음(checked). SER 기준 메모 추가 대상.

## C56 열전달 경로(NSS→EI tank 대 NSS→ESS→TSS)와 SHX 표기
- 분류: N
- 관련 문서: PSAR_ch01 (신청자), SER_KU1_CP (권위)
- 기준 조항(N/U): SER의 기술(판정 아님).
  - (새 인용) "Section 1.1.4.2.1 of the PSAR describes the salt systems, which consist of the nuclear island salt system (NSS), energy island salt system (ESS), and the TSS." [SER_KU1_CP §1.3.3.1.1 p.37]
  - (새 인용) "how the NSS isolation valves provide the boundary between the NSS and ESS (and thus the NI and EI)" [SER_KU1_CP §1.3.3.1.1 p.37]
  - (새 인용) "The sodium-salt heat exchanger (SHX) provides the interface between the salt-based NSS and the sodium-based IHT" [SER_KU1_CP §1.3.3.1.1 p.37]
- SER 판단(있으면): 없음.
- 메모(한국어): SER은 NSS와 ESS 사이에 NI/EI 경계가 있는 경로(§1.1.4.2 서술)를 따르므로, ch1 §1.1.3의 "NSS가 EI hot salt storage tank로 보낸다"는 ESS를 생략한 요약 표현이다. 열교환기 이름은 SER이 `sodium-salt heat exchanger (SHX)`로 통일해 적는다.
- 노트 상태: Natrium_Energy_Island_Systems: 변동 없음(checked) · Natrium_Plant_Overview: 변동 없음(checked)

## C57 RG 1.232 Section VI 제목(Reactivity 대 Radioactivity)
- 분류: U (표기 수준)
- 관련 문서: RG_1.232 (권위, 한 문서 내부)
- 기준 조항(N/U):
  - 목록 표기: (새 인용) "Section VI—Fuel and Radioactivity Control (Criteria 60–64)" [RG_1.232 App.C intro p.105] (같은 문자열이 p.12, p.62에도 있음)
  - 절 제목 표기: (새 인용) "Section VI. Fuel and Reactivity Control" [RG_1.232 App.C Section VI p.131] (같은 문자열이 App.B p.94에도 있음)
- 메모(한국어): 부록 A·각 부록 머리 목록·Table 1은 `Fuel and Radioactivity Control`, 부록 B와 C의 Section VI 절 제목은 `Fuel and Reactivity Control`이다. contradictions.md는 `Reactivity` 표기의 위치를 "App.C intro p.105"로 적었으나, 정제본에서 p.105는 `Radioactivity` 목록이고 `Reactivity` 제목은 p.131(App.C)과 p.94(App.B)이다. 정제본의 절 제목 접두어("Appendix C — ")는 정제 profile이 붙인 것이며, raw 변환본에는 "VI. Fuel and Reactivity Control" 표 행으로 있다. 기준 내용(Criteria 60–64)에는 차이가 없다.
- 노트 상태: MHTGR_DC_Fuel_And_Radioactivity_Control: 판단 보류(현재 checked). U 규칙상 disputed 대상이나 제목 표기 차이뿐이고 2026-09-16 판정에서 갈래 B였으므로, disputed 신규 지정 여부는 사용자 결정이 필요하다. contradictions.md의 쪽 인용 정정(p.105 → p.131, App.B p.94 추가) 필요.

## C58 주요사고 선정 근거와 DBA 선량
- 분류: N
- 관련 문서: PSAR_ch03 (신청자), SER_KU1_CP, RG_1.253 (권위)
- 기준 조항(N/U): (새 인용) "If assessment a major accident is not conservative or bounding for a specific non-LWR design in this regard or an applicant proposes to use a DBA that is not a major accident, justification for assessment of the radiological consequences at the EAB and LPZ outer boundary using a different event will be needed." [RG_1.253 §C.3.b fn.10 p.14]
- SER 판단(있으면):
  - (새 인용) "The staff notes that although the offsite radiological consequences of the selected major accident are bounding for at-power in-vessel DBAs, that is not true for the ex-vessel and fuel handling DBAs." [SER_KU1_CP §3.3.1.7 p.221]
  - (새 인용) "This means that the consequences of the major accident analyzed by USO do not bound the consequences of all DBAs as was done in reactor licensing precedents. This would necessitate additional justification as discussed in footnote 10 to RG 1.253 option 1." [SER_KU1_CP §3.3.1.7 p.221]
  - (새 인용) "the staff determined the selection of the PSAR section 3.9.6.1 core blockage and local faults DBA as the major accident, as supported by the assessment of DBAs in the LMP methodology, appropriately addresses the purpose and intent of the 10 CFR 50.34(a)(1)(ii)(D) safety analysis of a major accident postulated from considerations of possible credible accidental events." [SER_KU1_CP §3.3.1.7 p.222]
- 신청자 쪽: "This event was selected as the major accident, as it represents the potential hazard not exceeded by any other in-vessel design basis event or in-vessel DBA." [PSAR_ch03 §3.3.3 p.47]
- 메모(한국어): PSAR은 LFF-SAO-CN이 모든 in-vessel DBA를 넘지 않는다고 적지만, SER은 그 bounding 범위를 "at-power in-vessel DBAs"로 한정하고 fuel handling DBA(RFH-FDIV-CN 포함)는 bound하지 않는다고 확인했다. SER은 RG 1.253 option 1 각주 10의 추가 정당화가 필요하다고 지적한 뒤, LMP의 DBA 평가가 뒷받침한다는 이유로 선정을 수용했다.
- 노트 상태: Natrium_DBA_List: C58 측은 해제, 최종은 C12 판정에 따름

## C59 SER 안의 `AST` 표기(Alternative Shunt Trip 대 anticipatory automatic seismic trip)
- 분류: U
- 관련 문서: SER_KU1_CP (권위, 한 문서 내부)
- 기준 조항(N/U):
  - "In DHP-L1PP-4, the normal scram system fails to function and the scram breakers are tripped by the anticipatory automatic seismic trip system (AST), causing the control rods to fall into the core by gravity." [SER_KU1_CP §3.7.1.1 p.262]
  - "Loss of One Primary Sodium Pump with Alternative Shunt Trip" [SER_KU1_CP Table 3.7-1 p.276]
  - (새 인용) "evaluation of this DBA is anticipated to elevate the alternative shunt trip credited in this LBE from NSRST to SR." [SER_KU1_CP §3.7.1.1 p.264]
  - 별개 기능 근거: "The AST supports the NSRST function DL4-RC4, “Automatic seismic trip,” by continuously monitoring signal inputs from triaxial accelerometers and sending an isolated signal to the shunt trip feature in the RTBs when the signal inputs exceed a bi-stable setpoint." [SER_KU1_CP §7.6.8.1.7 p.584]; "The following are NSRST alternative shunt trips that are identified as risk-significant defense line functions in PSAR table 5.2-4, but are not described in detail within the PSAR due to the timing of when USO added them to the PRA relative to the submittal of the PSAR:" [SER_KU1_CP §5.5 p.354]
- 메모(한국어): SER은 DHP-L1PP-4의 사건명과 p.264 문장에서 alternative shunt trip(DL4-RC6 계열)을 credit한다고 적으면서, 사건 서술 p.262에서는 정지 차단기를 anticipatory automatic seismic trip system(AST, DL4-RC4)이 트립한다고 적는다. SER의 다른 절은 두 기능을 별개로 다루므로 이 사건에서 어느 기능이 credit되는지가 SER 안에서 모호하다. C7(신청자·ACRS의 AST 약어 전개)과 연결된다.
- 노트 상태: Natrium_SER_BDBE_DBA_Review: disputed 지정 대상(현재 checked; U 규칙)

## C60 SER의 SCG 방사성핵종 보유 기능 수("seven" 대 목록 6항목)
- 분류: U
- 관련 문서: SER_KU1_CP (권위, 한 문서 내부)
- 기준 조항(N/U):
  - "PSAR section 7.2.3.2.2 and table 5.2-3 state that the SCG supports seven functions which provide radionuclide retention." [SER_KU1_CP §7.2.3.1.15.1 p.475]
  - 바로 뒤 목록(새 인용, 공백 정규화 일치): DL3-RR1c, DL3-RR10, DL2-RR10, DL4-RR4a, DL4-RR4, DL4-RR4c의 6항목 [SER_KU1_CP §7.2.3.1.15.1 p.475]
- 메모(한국어): SER은 기능 수를 7로 적고 6개만 열거한다. 빠진 하나가 무엇인지(또는 수가 오기인지)는 SER 원문에서 판단할 수 없다. PSAR ch5 Table 5.2-4에 SCG 관련 `DL4-RR4b`(SCG Cells Barrier Isolation on Leak Detection)가 있으나 SER이 이를 뜻하는지는 원문에 근거가 없어 추정하지 않는다.
- 노트 상태: Natrium_SER_Reactor_Auxiliary_Review: disputed 지정 대상(현재 checked; U 규칙). 다만 결함이 개수 표기에 한정되므로 사용자가 기록만으로 처리할 수도 있다(판단 보류 여지 있음).

## C61 RG 1.247의 NEI 20-09 승인 범위(with exceptions 대 without exception)
- 분류: U
- 관련 문서: RG_1.247 (권위, 한 문서 내부)
- 기준 조항(N/U):
  - "Also, it endorses, with staff exceptions, a national consensus PRA standard provided by standards development organizations and industry guidance on PRA peer review." [RG_1.247 §A Purpose p.1]
  - "Regulatory Position C.2.2 presents the staff position on the use of PRA peer reviews to this effect, including staff endorsement with exceptions, of related industry PRA peer review guidance." [RG_1.247 §C.2 p.54]
  - 대: "In May 2021, NEI published industry PRA peer review guidance in NEI 20-09, Revision 1, “Performance of PRA Peer Reviews Using the ASME/ANS Advanced Non-LWR PRA Standard” (Ref. 17), which is endorsed in this RG with no exceptions." [RG_1.247 §B Reason for Issuance p.9]; "endorses NEI 20-09, Revision 1, in its entirety and with no exceptions as a means of satisfying the peer review requirements in the ASME/ANS NLWR PRA standard" [RG_1.247 §B Background p.10]; "For the reasons given below, the staff finds that the guidance in NEI 20-09, Revision 1, is acceptable in that regard and endorses NEI 20-09, Revision 1, without exception." [RG_1.247 §C.2.2 p.56]
- 메모(한국어): RG 1.247은 §A와 C.2 도입에서 산업계 peer review 지침을 예외와 함께 승인한다고 적고, §B와 C.2.2에서 NEI 20-09 Rev.1을 예외 없이 승인한다고 적는다. §A 문장의 "with staff exceptions"가 표준에만 걸리는지 peer review 지침까지 걸리는지는 문법상 모호하다. C.2.2가 실제 승인 조항이므로 "예외 없음"이 실효 입장으로 읽힐 수 있으나, 이를 정하는 문장은 원문에 없다.
- 노트 상태: RG_1247_Standards_Peer_Review_Documentation: disputed 지정 대상(현재 checked) · RG_1247_PRA_Acceptability_Framework: disputed 지정 대상(현재 checked; C66도 U) · RG_1.247: 소스 카드(status 필드 없음), 해당 없음

## C62 RFH-ESWR-CN 선원항의 보수성
- 분류: N
- 관련 문서: PSAR_ch03 (신청자), SER_KU1_CP (권위)
- 신청자 쪽: "The mechanistic source term modeled as the failure of all fuel pins in one high burnup fuel assembly in the EVHM is used because a fuel assembly failure in the EVHM will result in more severe consequences than a failure in the mated PIC and BLTC." [PSAR_ch03 §3.9.5.3.2 p.116]
- 기준 조항(N/U): DBA 선량 기준(25 rem TEDE)은 SER 판단 문장에 포함됨. 선원항 선택을 직접 규정하는 권위 문서 조항은 vault에 없음(일반 원칙: 보수적 결정론 해석).
- SER 판단(있으면):
  - "Unlike the DBEs, the source term for RFH-ESWR-CN is based off of the EVHM source term which appears to the staff to have resulted in a lower release fraction from the fuel." [SER_KU1_CP §3.8.1.5 p.296]
  - "RFH-ESWR-1 source term with the DBA consequence methodology would result in a TEDE of approximately 7.3 rem versus the 0.609 rem reported for this DBA, which is higher but still within the 25 rem TEDE acceptance criterion and thus acceptable." [SER_KU1_CP §3.8.1.5 p.297]
- 메모(한국어): PSAR은 EVHM 선원항이 더 가혹하다는 이유로 선택했지만, SER은 그 선원항이 방출분율을 낮춘 것으로 보이며 RFH-ESWR-1 선원항이면 약 7.3 rem이라고 추정했다. SER은 그래도 25 rem 기준 안이므로 수용했다(이탈 지적 + 수용).
- 노트 상태: Natrium_DBA_List: C62 측은 해제, 최종은 C12 판정에 따름 · Natrium_SER_BDBE_DBA_Review: C62 측 변동 없음(최종은 C59에 따름)

## C63 LFF-SAO-2 사건 정의와 MST 서술
- 분류: N
- 관련 문서: PSAR_ch03 (신청자), SER_KU1_CP (권위)
- 기준 조항(N/U): SER의 사건 의도 기술.
  - "LFF-SAO-2 is intended to assume that the primary functional containment boundary fails but the HAA is successful" [SER_KU1_CP §3.7.1.6 p.274]
  - "However, the description for the mechanistic source term for LFF-SAO-2 in the PSAR states that the primary coolant boundary is intact and the HAA is failed." [SER_KU1_CP §3.7.1.6 p.274]
- SER 판단(있으면):
  - "During the audit (ML25302A443), USO determined that this analysis was erroneous (see audit question 3-95)" [SER_KU1_CP §3.7.1.6 p.274]
  - "Based on the margins reported in the existing analysis and staff confirmatory analyses that staff determined that this event was appropriately categorized as a BDBE for the PSAR but anticipates that the description of the event will be corrected at the OL stage." [SER_KU1_CP §3.7.1.6 p.274]
- 메모(한국어): PSAR MST 서술(일차 경계 건전·HAA 실패)은 SER이 확인한 사건 의도(일차 functional containment 실패·HAA 성공)와 반대이며, 신청자도 audit에서 오류로 인정했다. SER은 BDBE 분류를 유지하고 서술 정정을 OL로 이연했다.
- 노트 상태: Natrium_BDBE_List: C63 측은 해제, 최종은 C12 판정에 따름 · Natrium_MST_Methodology: 변동 없음(checked) · Natrium_SER_BDBE_DBA_Review: C63 측 변동 없음(최종은 C59에 따름)

## C64 ESWR 사건의 barrier(PIC·BLTC 결합 가정)
- 분류: N
- 관련 문서: PSAR_ch03 (신청자), SER_KU1_CP (권위)
- 신청자 쪽: "The postulated initiating event is a sodium-water reaction in the Pool Immersion Cell (PIC) during fuel handling activities while the PIC and BLTC are mated that causes fuel cladding failure." [PSAR_ch03 §3.9.5.3.1 p.116]
- 기준 조항(N/U) 및 SER 판단:
  - "The BLTC is not expected to be mated with the PIC during the washing operation. Therefore, the mated BLTC/PIC (DL3-RR5a) is the appropriate radionuclide barrier for the drop events (RFH-FDPI), but not for the washing events (RFH-ESWR)." [SER_KU1_CP §3.6.1.4 p.250]
  - "During the audit, USO identified that the PIC design has changed since the PSAR submittal and that the analysis of the ESWR events in PSAR are based on the outdated preliminary design information." [SER_KU1_CP §3.2.1.3 p.203]
  - (새 인용) "While uncertainty in the design remains, the staff determined that the information provided was sufficient to support the CP based on:" [SER_KU1_CP §3.6.1.4 p.250]
- 메모(한국어): PSAR은 세척 사건을 PIC·BLTC 결합 상태로 해석했으나, SER은 세척 중 결합되지 않으므로 DL3-RR5a는 낙하 사건에만 적절하다고 지적했다. SER은 PIC barrier가 DL3-RR5a로 SR 분류된 점, 예방 조치, 보수적 선원항 가정을 근거로 CP 단계에서는 충분하다고 판단했다(이탈 지적 + CP 수용 + OL 재해석 예상).
- 노트 상태: Natrium_DBE_List: 변동 없음(checked) · Natrium_BDBE_List: C64 측 해제, 최종은 C12에 따름 · Natrium_DBA_List: C64 측 해제, 최종은 C12에 따름 · Natrium_Risk_Significant_LBEs: C64 측 해제, 최종은 C1에 따름 · Natrium_SER_AOO_DBE_Review: 변동 없음(checked)

## C65 표기 차이 묶음
- 분류: 하위 항목별(아래)

### C65(1) ASME/ANS RA-S-1.4-2021 승인 표현(SER "with clarifications" 대 RG 1.247 "with exceptions")
- 분류: U
- 관련 문서: SER_KU1_CP, RG_1.247 (권위끼리)
- 기준 조항(N/U):
  - "which endorses, with clarifications, the American Society of Mechanical Engineers (ASME) and American Nuclear Society (ANS) RA-S-1.4-2021 non-light-water reactor (non-LWR) PRA standard" [SER_KU1_CP §3.1.1 p.153]
  - "referred to hereafter as the ASME/ANS NLWR PRA standard, which is endorsed in this RG with exceptions" [RG_1.247 §B Reason for Issuance p.9]
- 메모(한국어): 승인 문서인 RG 1.247은 "exceptions", 그 RG를 인용한 SER은 "clarifications"로 적는다. 승인의 성격(예외 대 명확화)이 두 권위 문서에서 다르다. 승인 당사자인 RG 1.247의 표현이 우선한다고 볼 근거는 있으나, 권위 문서 간 우선순위는 사용자 결정에 없다.
- 노트 상태: Natrium_SER_PRA_Review: 판단 보류(현재 checked). U이나 SER의 인용 표현 차이에 한정되므로 disputed 지정 여부는 사용자 결정 필요. C13(PRA standard 상태)과 연결.

### C65(2) DL4-RC6c/d 이름(PSAR "High High"/"Low Low" 대 SER "high"/"low")
- 분류: N
- 관련 문서: PSAR_ch05 (신청자), SER_KU1_CP (권위)
- 신청자 쪽: `DL4-RC6c` "Alternative Shunt Trip on High High IHT level", `DL4-RC6d` "Alternative Shunt Trip on Low Low IHT level" [PSAR_ch05 Table 5.2-4 p.17]
- 기준 조항(N/U): "Alternative shunt trip on high IHT level" [SER_KU1_CP §5.5 p.354]; "Alternative shunt trip on low IHT level" [SER_KU1_CP §5.5 p.354]
- SER 판단(있으면): 이름에 대한 판단 없음. 두 기능 모두 risk-significant NSRST로 같게 분류.
- 메모(한국어): SER은 설정점 단계 표기("High High"/"Low Low")를 생략한 이름을 쓴다. 분류와 계통은 같으므로 이름 표기 차이이다.
- 노트 상태: Natrium_SER_PDC_SR_NSRST_Review: 변동 없음(checked)

### C65(3) 누적 위험 목표 조동사(RG 1.253 "should" 대 NEI 18-04 "shall")
- 분류: U
- 관련 문서: RG_1.253, NEI_18-04 (권위끼리)
- 기준 조항(N/U):
  - "The average individual risk of early fatality within 1 mile of the EAB from all LBEs, based on mean estimates of frequencies and consequences should not exceed 5E-07/plant-year" [RG_1.253 §5 p.18]
  - "The average individual risk of early fatality within 1 mile of the EAB from all LBEs based on mean estimates of frequencies and consequences shall not exceed 5E-07/plant-year to ensure that the NRC safety goal QHO for early fatality risk is met." [NEI_18-04 §3.2.2 Task 7b p.24]
  - (셋째 목표도 같은 양상; 첫째 목표는 두 문서 모두 "should not exceed")
- 메모(한국어): 수치(1/plant-year, 5E-07, 2E-06)는 같고 둘째·셋째 목표의 조동사만 다르다. RG 1.253은 지침 문체("should")로 세 목표를 통일했고 NEI 18-04는 둘에 "shall"을 쓴다. 의무 수준의 차이로 읽을지 문체 차이로 읽을지를 정하는 문장은 두 문서에 없다.
- 노트 상태: Cumulative_Risk_Targets: 판단 보류(현재 checked). U이나 수치가 같고 조동사 차이에 한정되므로 disputed 지정 여부는 사용자 결정 필요.

### C65(4) RAC 성격(PSAR "Inherent" 대 SER "passive")
- 분류: N
- 관련 문서: PSAR_ch05 (신청자), SER_KU1_CP (권위)
- 신청자 쪽: `DL3-HR4` "Inherent - RAC Operation" [PSAR_ch05 Table 5.2-2 p.9]
- 기준 조항(N/U) 및 SER 판단: "The PSAR states that the RAC is an inherent means of controlling heat removal; however, the staff considers it to be passive because it relies on maintaining an open flow path." [SER_KU1_CP §1.3.3.3.2 p.43]
- 메모(한국어): SER은 열린 유로 유지에 의존한다는 이유로 RAC를 inherent가 아니라 passive로 본다. SR 분류는 같다. 부기: PSAR ch7 기능 표는 "The RAC provides passive emergency core cooling capability and operates continuously." [PSAR_ch07 §7.2.1.2 p.96]로 적어 SER과 같은 표현을 쓴다(노트 Natrium_System_Reactor_Air_Cooling의 기존 인용).
- 노트 상태: Natrium_SER_Facility_Overview_Review: 변동 없음(checked)

## C66 PRA 범위(RG 1.247 C.1.1 "must always" 대 RG 1.253 A.3.3·A.3.7 CP 최소 범위)
- 분류: U
- 관련 문서: RG_1.247, RG_1.253 (권위끼리)
- 기준 조항(N/U):
  - (새 인용) "For licensing activities, a PRA for the seismic hazard group must always be developed; other hazards should also be included if they cannot be screened out with appropriate justification." [RG_1.247 §C.1.1 p.15]
  - (새 인용) "All POSs (e.g., at-power and low-power and shutdown (LPSD) types of POSs) should be addressed." [RG_1.247 §C.1.1 p.15]
  - 대: (새 인용) "A.3.3 Regarding PRA acceptability, the minimum scope of the CP PRA logic model should include the internal events hazard group for the reactor in the at-power POS." [RG_1.253 §A.3.3 p.33]
  - (새 인용) "A.3.7 The CP applicant may disposition certain hazards by crediting DBHLs in lieu of explicitly modeling these hazards in the PRA or accounting for them through a risk-informed supplementary evaluation." [RG_1.253 §A.3.7 p.33]
  - 부분 조정 문장(RG 1.247 안): (새 인용) "justification that the PRA has been performed in such a way that its results are acceptable, commensurate with the level of maturity of the design." [RG_1.247 §C.4.2 p.65]
- 메모(한국어): RG 1.247 C.1.1은 인허가 활동에 지진 hazard group PRA를 "항상" 요구하고 모든 POS를 다루라고 적으나, RG 1.253은 CP PRA의 최소 범위를 출력 운전 POS의 내부 사건으로 두고 DBHL credit을 허용한다. RG 1.247 C.4.2의 "설계 성숙도에 상응하는" 정당화 문장은 문서화 요건으로 범위 요건(C.1.1)을 직접 완화하지 않으며, "must always"를 CP 단계에 맞추어 조정하는 문장은 두 문서 어디에도 없다. 적용 단계의 차이로 읽힐 수 있으나 원문이 그렇게 명시하지 않는다.
- 노트 상태: RG_1247_PRA_Acceptability_Framework: disputed 지정 대상(현재 checked) · RG_1253_CP_PRA_Acceptability: disputed 지정 대상(현재 checked)

---

## 표 1. 항목별 분류 요약

| 항목 | 분류 | 기준 문서·위치 | SER 판단 | 비고 |
|---|---|---|---|---|
| C46 | I | 없음(SER §6.4.1.3은 과도 집합만 수용) | 과도 집합·횟수 적정 | 이전 갈래 C |
| C47 | I | 없음(SER §6.4.1.4는 §6.4.4 범위만 확인) | 없음 | 교차참조 결함 |
| C48 | I | 없음(SER §6.4.1.2.1 일괄 수용) | 하중조합 일괄 적정 | 표 내부 표기 |
| C49 | N | SER §7.6.2 p.546 | 기술만 | DCS = 구현 플랫폼 |
| C50 | N | SER §7.1.3.1.2 p.437, §7.1.4 p.446 | 기술만 | PHT의 RAB 목록 기재가 SER과 다름 |
| C51 | N | SER 표제 p.1, §8.2.1 p.621, §1.7 p.49 | 기술만 | SER §2.2.2 p.58 역관계 문장(U 후보, 범위 밖) |
| C52 | N | SER §11.3 p.669–670 | 이탈 없음 | 제목 표기는 양쪽 다 SER과 한 곳씩 다름 |
| C53 | N | SER §11.1.1.7 p.662, §11.1.1.9 p.662–663, §11.6.1.6 p.707, §10.1.1 p.647 | CP 단계 수용 | 예비 약속 + OL 입증 |
| C54 | N | SER Table 1.8-3 p.51-54 | 충족(QA TR 근거) | 이전 갈래 C |
| C55 | N | SER Table 1.8-3 p.51-54, §11.2.1.3 p.669 | CP 수준 충분, OL 완료 평가 | 이전 갈래 C |
| C56 | N | SER §1.3.3.1.1 p.37 | 기술만 | ch1 §1.1.3은 ESS 생략 요약 |
| C57 | U | RG_1.232 p.12·62·105 대 p.94·131 | — | 표기 수준; 인용 쪽 정정 필요 |
| C58 | N | RG_1.253 §C.3.b fn.10 p.14 | 비bound 지적 후 수용 | |
| C59 | U | SER §3.7.1.1 p.262 대 p.264·Table 3.7-1 p.276 | — | C7과 연결 |
| C60 | U | SER §7.2.3.1.15.1 p.475 | — | 개수 7 대 목록 6 |
| C61 | U | RG_1.247 §A p.1, §C.2 p.54 대 §B p.9–10, §C.2.2 p.56 | — | |
| C62 | N | (일반 원칙) | 저평가 지적 후 수용 | |
| C63 | N | SER §3.7.1.6 p.274 | 오류 확인, OL 정정 이연 | |
| C64 | N | SER §3.6.1.4 p.250, §3.2.1.3 p.203 | 이탈 지적 후 CP 수용 | |
| C65(1) | U | SER §3.1.1 p.153 대 RG_1.247 §B p.9 | — | C13과 연결 |
| C65(2) | N | SER §5.5 p.354 | 이름 판단 없음 | |
| C65(3) | U | RG_1.253 §5 p.18 대 NEI_18-04 Task 7b p.24 | — | 수치 같음 |
| C65(4) | N | SER §1.3.3.3.2 p.43 | passive로 판단 | ch7은 SER과 같은 표현 |
| C66 | U | RG_1.247 §C.1.1 p.15 대 RG_1.253 §A.3.3·A.3.7 p.33 | — | |

건수(하위 항목 단위, 24건): U 7 (C57, C59, C60, C61, C65(1), C65(3), C66) · N 14 (C49, C50, C51, C52, C53, C54, C55, C56, C58, C62, C63, C64, C65(2), C65(4)) · I 3 (C46, C47, C48) · 판단 보류 분류 0 (노트 상태 판단 보류 4건은 표 2).

## 표 2. 노트별 최종 disputed 유지/해제 (이 범위 기준)

| 노트 | 현재 status | 이 범위의 관련 항목 | 결론 | 근거 |
|---|---|---|---|---|
| Natrium_RG_Conformance | disputed | C52 N, C53 N (+C45 갈래 B) | 해제 | 걸린 A 항목 C52·C53이 모두 N |
| Natrium_Operating_Organization | disputed | C53 N | 해제 | C53만 해당 |
| Natrium_Security_And_Fitness_For_Duty | disputed | C53 N | 해제 | C53만 해당 |
| Natrium_Emergency_Preparedness_EPZ | disputed | C52 N | 범위 밖 항목에 따름 | C52 측 해제; C16 판정 필요 |
| Natrium_DBA_List | disputed | C58 N, C62 N, C64 N | 범위 밖 항목에 따름 | 이 범위에 U 없음; C12 판정 필요 |
| Natrium_BDBE_List | disputed | C46 I, C63 N, C64 N | 범위 밖 항목에 따름 | 이 범위에 U 없음; C12 판정 필요 |
| Natrium_Risk_Significant_LBEs | disputed | C64 N | 범위 밖 항목에 따름 | C1 판정 필요 |
| Natrium_Structural_Loads_And_Combinations | disputed | C48 I (+C42·C43 갈래 B) | 범위 밖 항목에 따름 | C44 판정 필요 |
| Natrium_ASME_Component_Loads_And_Limits | disputed | C47 I | 범위 밖 항목에 따름 | C44 판정 필요 |
| Natrium_SER_BDBE_DBA_Review | checked | C59 U, C62 N, C63 N | disputed 지정 | C59 U(SER 내부, credit 기능 모호) |
| Natrium_SER_Reactor_Auxiliary_Review | checked | C60 U | disputed 지정(판단 보류 여지) | 개수 표기 결함에 한정 |
| RG_1247_Standards_Peer_Review_Documentation | checked | C61 U | disputed 지정 | RG 1.247 내부 승인 범위 상충 |
| RG_1247_PRA_Acceptability_Framework | checked | C61 U, C66 U | disputed 지정 | 두 U 항목 |
| RG_1253_CP_PRA_Acceptability | checked | C66 U | disputed 지정 | RG 1.247 대 RG 1.253 범위 |
| MHTGR_DC_Fuel_And_Radioactivity_Control | checked | C57 U | 판단 보류 | 제목 표기뿐; 이전 갈래 B |
| Natrium_SER_PRA_Review | checked | C65(1) U | 판단 보류 | SER 인용 표현 차이 |
| Cumulative_Risk_Targets | checked | C65(3) U | 판단 보류 | 조동사 차이, 수치 동일 |
| Natrium_ASME_Design_Transients | checked | C46 I | 유지(checked, 변동 없음) | 메모 기록 |
| Natrium_Piping_And_Industrial_Codes | checked | C47 I | 변동 없음 | 메모 기록 |
| Natrium_IC_Systems | checked | C49 N | 변동 없음 | SER 기준 메모 |
| Natrium_Support_Systems | checked | C49 N | 변동 없음 | SER 기준 메모 |
| Natrium_Major_Structures | checked | C50 N | 변동 없음 | SER 기준 메모 |
| Natrium_Reactor_Heat_Transport_Systems | checked | C50 N | 변동 없음 | SER 기준 메모 |
| Natrium_Kemmerer_Site | checked | C51 N | 변동 없음 | SER 기준 메모 |
| Natrium_Plant_Overview | checked | C51 N, C56 N | 변동 없음 | SER 기준 메모 |
| Natrium_Project_Organization | checked | C51 N | 변동 없음 | SER 기준 메모 |
| Natrium_TMI_Requirements | checked | C54 N, C55 N | 변동 없음 | SER 기준 메모 |
| Natrium_Energy_Island_Systems | checked | C56 N | 변동 없음 | SER 기준 메모 |
| Natrium_MST_Methodology | checked | C63 N | 변동 없음 | SER 기준 메모 |
| Natrium_DBE_List | checked | C64 N | 변동 없음 | SER 기준 메모 |
| Natrium_SER_AOO_DBE_Review | checked | C64 N | 변동 없음 | |
| Natrium_SER_PDC_SR_NSRST_Review | checked | C65(2) N | 변동 없음 | |
| Natrium_SER_Facility_Overview_Review | checked | C65(4) N | 변동 없음 | |
| RG_1.247 (소스 카드) | (status 없음) | C61 U | 해당 없음 | 소스 카드 |

부기(범위 밖 새 후보, contradictions.md 미기록):
1. SER §2.2.2 p.58 "TerraPower, LLC (TerraPower), a 100 percent owned subsidiary of USO" 대 SER §1.7 p.49·§8.2.1 p.621 "USO is a wholly owned subsidiary of TerraPower" — SER 내부 관계 역전(U 후보).
2. SER Table 1.8-3 p.51-54의 `10 CFR 50.34(f)(2)(xvii)` 행 중복(둘째 행 "In-plant Radiation Monitoring | 10.1") — SER 표 내부 번호 표기.
3. contradictions.md C57의 `Reactivity` 위치 인용 정정 필요(p.105 → App.C p.131, App.B p.94 추가).

---

<!-- part d: NEI 18-04 disputed 노트와 상위 dispute 후보 -->

# 재분류 D: NEI 18-04 disputed 노트 4개, NEI 18-04 내부 불일치 후보 3건, 상위 dispute 탐색

작성 2026-10-17. 읽기 전용 분석이며 vault 파일은 바꾸지 않았다. 아래 항목은 `meta/contradictions.md`에 C 번호가 없으므로 `D-n`(대상 범위)과 `새 후보 U<n>`(추가 과제)으로 번호를 붙였다.

판정 표기:
- 분류는 지시서대로 U/N/I이다. U 항목에는 "해소 여부"를 덧붙였다. **해소**는 다른 권위 문서가 같은 사항을 명시적으로 해석·보완해 운용 기준이 하나로 정해진 경우이다. **미해소**는 그런 문장이 없는 경우이다. **표기**는 수치·판정에 영향이 없는 문언 차이이다.
- 노트 상태 권고: 미해소 U가 남으면 유지, 해소된 U만 있으면 해제(해소 근거를 메모로 단다)로 적었다. 해소 판정이 개별 신청 SE(SER_KU1_CP)에만 근거하는 경우는 따로 표시했다.
- 인용 검증: `(새 인용)` 표시 문장과 노트에서 가져온 문장 모두 (세션 검증 스크립트)로 정제본에 글자 그대로 있는지, 쪽 표지가 맞는지 확인했다(인용 70여 건 전부 확인. 생략부호가 든 1건 "However, when the uncertainty bands ... straddles ..."는 LBE_Frequency_Categories 원문 사실 절의 줄을 그대로 옮긴 것이고, 생략부호 앞뒤 부분은 정제본 p.22에 있다). `(새 인용)`은 vault 노트 어디에도 없는 문장이다.

---

## D-1 BDBE 빈도 하한의 통계량 (LBE_Frequency_Categories)
- 분류: U (NEI 18-04 내부) — 해소(RG 1.233 C.1.b와 SER의 명시 해석)
- 관련 문서: NEI_18-04, RG_1.233, SER_KU1_CP (모두 권위)
- 기준 조항(U, 상충의 양쪽):
  - "Event sequences with mean frequencies of 5E-07/plant-year to 1E-04/plant-year are classified as BDBEs." [NEI_18-04 Table 3-1 p.14]
  - "BDBEs are rare events with frequencies less than 1E-04/plant-year but with upper bound frequencies greater than 5E-07/plant-year." [NEI_18-04 §3.2.1 p.16]
  - "An event sequence family with a mean frequency less than 5E-07/plant year but with a 95%tile frequency estimate above 5E-07/plant-year is evaluated as a BDBE." [NEI_18-04 §3.2.2 Task 7a p.22]
- 해석 조항(권위):
  - "The F-C target and related discussions in NEI 18-04 include an upper bound event sequence frequency (i.e., 95th percentile) of 5E-07/plant-year to define the lower range of BDBEs." [RG_1.233 §C.1.b p.14]
  - "Applicants should not consider this demarcation of lowest-event frequencies on the F-C target and category definitions a hard-and-fast cutoff but instead should consider it in the context of other parts of the methodology described in NEI 18-04." [RG_1.233 §C.1.b p.14]
  - (새 인용) "The staff assessed the BDBEs to ensure they were appropriately categorized as BDBEs based on their frequency (upper 95th percentile frequency above 5E-07 and mean frequency less than 1E-04)." [SER_KU1_CP §3.7.1 p.261]
- SER 판단: "While USO did use the 95th percentile frequency when determining which events to evaluate as BDBEs, mean frequency was used when determining which events would be classified and included in the CP application as BDBEs." [SER_KU1_CP §3.4.1 p.225]; "The staff intends to continue to evaluate BDBEs based on the 95th percentile frequency when reviewing the OL application." [SER_KU1_CP §3.7.1 p.261]
- 메모(한국어): NEI 18-04는 표 3-1에서 BDBE 하한을 평균 빈도로, §3.2.1·Task 4·Task 7a에서 95th percentile 상한 빈도로 적어 내부가 어긋난다. RG 1.233 C.1.b는 하한을 95th percentile로 읽는다고 명시하고, SER은 이를 "upper 95th percentile frequency above 5E-07 and mean frequency less than 1E-04"라는 분류 기준으로 적용하며 평균을 쓴 사업자 처리를 방법론 이탈로 판정했다. 따라서 권위 문서 수준의 운용 기준은 "상한 1E-04는 평균, 하한 5E-07은 95th percentile"로 정해진다. RG 1.233 본문도 "The mean values of the frequencies are used to classify the LBEs into AOOs, DBEs, and BDBE categories." [RG_1.233 §C.1 p.11]라고 적어 NEI와 같은 구조의 문장을 가지므로, 이 판정은 C13의 "C.1.b 95th vs mean" 하위 항목과 함께 내려야 한다(같은 쟁점).
- 노트 상태: LBE_Frequency_Categories: 해제 (해설 마지막 문단에 RG 1.233 C.1.b와 SER §3.7.1 p.261 메모 추가 권고). RG_1233_LBE_Staff_Position(C13으로 disputed)은 이 범위 밖이나 같은 근거로 해소 후보이다.

## D-2 Risk-significant LBE 판정 통계량 (LBE_Risk_Significance 첫째 쟁점)
- 분류: U (NEI 18-04 내부) — 해소(RG 1.233이 95th percentile을 명시)
- 관련 문서: NEI_18-04, RG_1.233 (권위)
- 기준 조항(U, 상충의 양쪽):
  - "mean estimates supported by a robust uncertainty analysis are generally used to support risk significance determinations." [NEI_18-04 §3.2.2 Task 7a p.23]
  - (새 인용) "The primary purpose of comparing the frequencies and consequences of LBEs against the F-C Target is to evaluate the risk significance of individual LBEs." [NEI_18-04 §3.2.2 Task 7a p.23]
  - "To consider the effects of uncertainties, the upper 95th percentile estimates of both frequency and dose should be used." [NEI_18-04 §3.3.5 p.35]
  - "In the LMP framework, an AOO, DBE, or BDBE is regarded as risk-significant if the combination of the upper bound (95%tile) estimates of the frequency and consequence of the LBE are within 1% of the F-C Target AND the upper bound 30-day TEDE dose at the EAB exceeds 2.5 mrem." [NEI_18-04 §6 p.90]
- 해석 조항(권위):
  - "NEI 18-04 defines risk-significant LBEs as those with frequencies and consequences within 1 percent of the F-C target, with site boundary doses exceeding 2.5 mrem." [RG_1.233 §C.1 p.13]
  - "To consider the effects of uncertainties, the applicant should use the upper 95th percentile estimates of both frequency and dose." [RG_1.233 §C.1 p.13]
- SER 판단: 판정 통계량을 정하는 문장은 없다. SER은 PSAR이 두 기준의 risk-significant LBE를 각각 표로 낸 것을 그대로 기술한다: (새 인용) "Table 4.2-1 of the PSAR provides the margins from the mean frequency and dose to the F-C target curve for LBEs identified as risk-significant based on the mean risk." [SER_KU1_CP §4.2.1.1.1 p.327]; (새 인용) "PSAR table 4.2-2 provides the margins from the 95th percentile frequency and risk to the F-C target curve for LBEs identified as risk significant based on the 95th percentile risk." [SER_KU1_CP §4.2.1.1.1 p.327]. 즉 SER은 평균 기준의 식별도 이탈로 지적하지 않았다.
- 메모(한국어): Task 7a는 risk significance 판정에 일반적으로 평균을 쓴다는 관행을 근거로 들고, §3.3.5와 용어집은 risk-significant LBE 판정에 빈도·선량 모두 95th percentile 상한을 쓰라고 적는다. RG 1.233은 risk-significant LBE 정의를 옮기면서 "the applicant should use the upper 95th percentile estimates"라고 명시한다. Task 7a의 평균 문장은 DBE 선량의 F-C Target 비교와 여유도 평가(평균 여유와 95th 여유를 함께 보는 구조, "The NEI 18-04 methodology for assessing DID includes an assessment of plant risk margins that compares the mean values of each LBE frequency and dose to the F-C target." [RG_1.233 §C.3 p.21])로 읽으면 RG 1.233의 95th 규정과 양립한다. 다만 RG 1.233이 Task 7a 문장을 직접 지칭해 정리하지는 않는다.
- 노트 상태: LBE_Risk_Significance — D-3의 판정과 함께 정한다(아래 표 2).

## D-3 Risk-significant SSC 첫 기준(F-C Target 안 유지)의 통계량 (LBE_Risk_Significance 둘째 쟁점, Risk_Importance_Measures, Risk_Significant_SSC)
- 분류: U (NEI 18-04 내부) — 해소(SER의 명시 해석; RG 1.233은 이 사항을 다루지 않음)
- 관련 문서: NEI_18-04, SER_KU1_CP, RG_1.233 (권위)
- 기준 조항(U, 상충의 양쪽):
  - "In the LMP framework, an SSC is regarded as risk-significant if its PRA Safety Function is: a) required to keep one or more LBEs inside the F-C Target based on mean frequencies and consequences" [NEI_18-04 §6 p.90]
  - "The LBE is considered within the F-C Target when a point defined by the upper 95th percentile uncertainty of the LBE frequency and dose estimates is within the F-C Target." [NEI_18-04 §3.3.6 p.37]
  - "An LBE is considered within the F-C Target when a point defined by the upper 95th percentile uncertainty on both the LBE frequency and dose is within the F-C Target." [NEI_18-04 §4.2.2 p.47]
- SER 판단(해석):
  - "F-C target curve | Mean | SR RSF, risk-significant and safety-significant" [SER_KU1_CP Table 5.1-1 p.343] (Task 7a.1·7a.2 행)
  - (새 인용) "| 7a.3 | All non-DBA LBEs | Remove individual functions and evaluate impact on individual LBEs | F-C target curve | 95th percentile | NSRST, risk-significant and safety-significant |" [SER_KU1_CP Table 5.1-1 p.343]
  - (새 인용) "These risk-significant functions are designated as required safety functions (RSFs) and result in safety related (SR) classifications if they are necessary to meet the F-C target for DBEs or high-consequence BDBEs when evaluated using mean risk values." [SER_KU1_CP §5.1 p.337]
  - "Risk-significant NSRST functions are those needed to maintain the 95th percentile LBE results below the F-C target and those that have a greater than 1 percent impact on the cumulative risk metrics." [SER_KU1_CP §5.5 p.353]
  - "Identification of RSFs was performed using the 95th percentile versus mean risk values." [SER_KU1_CP §5.1 p.337] (사업자의 이탈로 지적)
- 메모(한국어): NEI 18-04 본문(§3.3.6, §4.2.2)은 SSC 첫 기준에서 LBE가 F-C Target 안에 있는지를 95th percentile 상한 점으로, 용어집은 평균으로 판정한다고 적는다. SER Table 5.1-1("SSC Classification Steps in NEI 18-04 Methodology")은 두 통계량을 단계별로 나눈다. DBE와 DBE 영역에 걸치는 AOO·BDBE, 고결말 BDBE에서 RSF(SR)를 정할 때는 평균을, 모든 비DBA LBE에서 risk-significant NSRST 기능을 정할 때는 95th percentile을 쓴다. 이 정리로 용어집의 평균 문장은 RSF 판정에, 본문의 95th 문장은 risk-significant 판정 일반에 대응한다. 다만 (1) 이 해석은 개별 신청 SE의 표이고 RG 1.233에는 대응 문장이 없으며, (2) 용어집 문장은 "one or more LBEs" 전체에 평균을 적용하므로 SER 표와 글자 그대로 일치하지는 않는다. 둘째 기준(누적 위험 목표 1 %)은 NEI 본문·용어집·SER Table 5.1-1(7b 행, Mean)이 모두 평균으로 일치한다.
- 노트 상태: Risk_Importance_Measures: 해제(SER 해석 근거, 사용자 확인 권장); Risk_Significant_SSC: 해제(같음); LBE_Risk_Significance: 해제(D-2는 RG 1.233, D-3은 SER 근거). 사용자가 "개별 신청 SE의 해석은 일반 지침의 모순을 해소하지 않는다"는 기준을 택하면 D-3에 걸린 세 노트는 유지이고, 그 경우 LBE_Risk_Significance도 유지이다.

## D-4 §5.3 Task 1의 "Task 14" 참조 (NEI 18-04 내부 후보 1)
- 분류: U (NEI 18-04 내부, 교차참조) — 표기, 오기 여부는 판단 보류
- 관련 문서: NEI_18-04 (권위)
- 기준 조항(U):
  - (새 인용) "Final decisions on the frequency and extent of inspections will be made later in Task 14." [NEI_18-04 §5.3 Task 1 p.63]
  - "RFDC provide a bridge between the DBAs and the formulation of Safety Related Design Criteria (SRDC) for the SR SSCs." [NEI_18-04 §5.3 Task 14 p.65]
  - "These include numerical targets for SSC reliability and availability, design margins for performance of the PSFs, and monitoring of performance against these targets with appropriate corrective actions when targets are not fully realized." [NEI_18-04 §5.3 Task 16 p.65]
- 메모(한국어): Task 1은 검사의 빈도와 범위를 Task 14에서 정한다고 적으나, §5.3의 Task 14 제목과 본문은 SR SSC의 RFDC 정의이고 검사를 언급하지 않는다. 특수 처리 요건을 정하는 과업은 Task 16이다. 다만 Task 16 본문도 "inspection"이라는 낱말을 쓰지 않으므로, "Task 14"가 Task 16의 오기라고 원문만으로 단정할 수 없다(판단 보류). 같은 문서의 과업 번호 결함 C17과 같은 유형이며, 다른 권위 문서에 이 문장을 해석하는 조항은 없다(RG 1.233·RG 1.253·SER에서 "Task 14" 검색 결과 없음).
- 노트 상태: 이 문장을 인용한 노트 없음(DID_Integrated_Process, Required_Functional_Design_Criteria는 Task 14 제목·본문만 인용). 해당 disputed 노트 없음. 갈래 B(기록만)와 같은 처리를 권고한다.

## D-5 용어집 Risk-Informed 항목의 출처 칸 (NEI 18-04 내부 후보 2)
- 분류: U (NEI 18-04 내부) — 표기
- 관련 문서: NEI_18-04 (권위)
- 기준 조항(U):
  - (새 인용) "| Risk-Informed | RI | An approach to decision-making in which insights from probabilistic risk assessments are considered with other sources of insights | Adapted from NRC Glossary definition of performance-based regulation in order to apply to both design decisions and regulatory decision-making |" [NEI_18-04 §6 p.90]
  - (새 인용) "| Performance-Based | PB | An approach to decision-making that focuses on desired objective, calculable or measurable, observable outcomes" [NEI_18-04 §6 p.90] (같은 표에서 이 행의 출처 칸도 "Adapted from NRC Glossary definition of performance-based regulation in order to apply to both design decisions and regulatory decision-making"이다)
- 메모(한국어): RI 항목의 출처 칸이 바로 위 PB 항목의 출처 칸과 글자 그대로 같아, risk-informed 정의의 출처를 "performance-based regulation" 정의로 적는다. 정의 본문은 서로 다르다. 출처 칸 복제로 보이나 원문 오기는 교정하지 않으며, 어느 권위 문서도 이 칸을 다루지 않는다.
- 노트 상태: Integrated_Decision_Making_Process는 RI 정의 본문만 인용하고 출처 칸은 인용하지 않는다. 해당 disputed 노트 없음. 기록만 권고.

## D-6 Task 7c "within 1%"와 §4.2.2 "exceeds 1%" (NEI 18-04 내부 후보 3)
- 분류: U (NEI 18-04 내부, 문언) — 해소(NEI 자체 수치와 SER의 해석)
- 관련 문서: NEI_18-04, SER_KU1_CP (권위)
- 기준 조항(U):
  - "SSCs are classified as risk-significant if the SSC function is necessary to keep any LBEs inside the F-C Target, or if the total frequency of LBEs with the SSCs failed is within 1% of any of the three cumulative risk targets identified in Task 7b." [NEI_18-04 §3.2.2 Task 7c p.24]
  - "A significant contribution to each cumulative risk metric limit is satisfied when total frequency of all LBEs with failure of the SSC exceeds 1% of the cumulative risk metric limit based on the mean estimates of frequencies and consequences." [NEI_18-04 §4.2.2 p.47]
  - (새 인용) "b) if the total frequency LBEs that involve failure of the SSC PRA Safety Function contributes at least 1% to any of the LMP cumulative risk targets." [NEI_18-04 §6 p.90]
- 해석 조항(권위):
  - "An SSC makes a significant contribution to this cumulative risk metric if the total frequency of exceeding a site boundary dose of 100 mrem associated with LBEs with the SSC failed is greater than 1E-02/plant-year." [NEI_18-04 §4.2.2 p.47] (조기 사망 5E-09, 잠복 암 2E-08도 같은 절에 수치로 있음)
  - "Risk-significant NSRST functions are those needed to maintain the 95th percentile LBE results below the F-C target and those that have a greater than 1 percent impact on the cumulative risk metrics." [SER_KU1_CP §5.5 p.353]
  - (새 인용) "| 7b | All non-DBA LBEs | Remove individual functions and evaluate total frequency of all associated LBEs | 1% of cumulative risk metrics | Mean | NSRST, risk-significant and safety-significant |" [SER_KU1_CP Table 5.1-1 p.343]
- 메모(한국어): 같은 기준을 Task 7c는 "within 1% of", §4.2.2는 "exceeds 1% of", 용어집은 "contributes at least 1%"로 적는다. "within 1% of"를 글자대로 읽으면 목표값의 1 % 이내(목표 근처)로도 읽힐 수 있어 문언이 모호하다. 그러나 §4.2.2가 세 목표마다 한도의 1 %에 해당하는 절대값(1/plant-year의 1E-02, 5E-07의 5E-09, 2E-06의 2E-08)을 제시하고, SER도 "greater than 1 percent impact"로 적용하므로 운용 기준은 "한도의 1 % 초과"로 하나이다. 경계값을 포함하는지("exceeds" 대 "at least")만 남으며 이는 판정 결과에 사실상 영향이 없는 표기 차이이다.
- 노트 상태: Cumulative_Risk_Targets(checked), LBE_Risk_Significance가 Task 7c 문장을 인용한다. 이 항목으로 새로 disputed가 될 노트는 없다.

---

# 추가 과제: 상위 dispute 탐색

검토 범위: 권위 문서 노트의 원문 사실과 해설 가운데 "어긋/상충/모순/다르" 표현이 있는 노트(RG_1.232, SFR_DC_Residual_Heat_Removal_And_ECC, NRC_Endorsement_Of_NEI_18-04, RG_1233_LBE_Staff_Position, Natrium_SER_Integrated_Evaluation_Review 등), `meta/lint/2026-10-16.md` 전체, 그리고 지시된 우선 쌍에 대한 정제본 직접 검색(RG 1.233 §C 전문, RG 1.253 §C.4–C.6·부록 A.1·A.3, NEI 18-04 §3.2·§4.1·§4.2·§5.3·§6, SER §3.4.1·§3.7.1·§4.1.1·§5.1·§5.5·Table 5.1-1). ACRS_ML25293A458 노트는 기존 C7·C37 외에 따로 대조하지 않았다(범위 한계).

이미 기록된 항목과 겹치는 우선 쌍은 새 후보로 올리지 않았다: RG 1.233 C.1.b의 95th 대 mean과 C.2.a support SSC 범위(C13), RG 1.253 대 NEI 18-04의 누적 목표 서법(C65(3), 아래 U4에서 확장), RG 1.247 대 RG 1.253 PRA 범위(C66), RG 1.232 내부(C14, C57).

## 새 후보 U1 피동 NSRST 저하 성능의 DBA credit 대 "SR SSC만" 규정
- 분류: U (SER staff 판단 대 NEI 18-04·RG 1.233 문언) — 미해소
- 관련 문서: SER_KU1_CP, NEI_18-04, RG_1.233 (권위)
- 기준 조항(U, 한쪽):
  - "These specific SSCs are classified as SR in Task 5A and are the only ones included in the DBA analysis of the DBAs." [NEI_18-04 §4.1 Tasks 4A and 5A p.44]
  - "DBAs are derived from the DBEs by prescriptively assuming that only Safety Related SSCs are available to mitigate postulated event sequence consequences to within the 10 CFR 50.34 dose limits." [NEI_18-04 Table 3-1 p.14]
  - (새 인용) "Design-basis accidents (DBAs) are derived from DBEs by assuming that only safety-related (SR) SSCs are available to mitigate the events." [RG_1.233 §C.1 p.11]
- 기준 조항(U, 다른 쪽, SER이 근거로 든 NEI 문장):
  - "DBAs are then constructed, starting with each DBE, and then assuming that only the SR SSCs perform their associated RSFs." [NEI_18-04 §5.3 Task 10 p.64]
  - "It is appropriate that for the inherent capabilities of passive functions, degradation of the passive function is considered, as opposed to complete failure (i.e., a physical non-existence of that function)." [NEI_18-04 §5.6.2 p.69]
  - (새 인용) "A deterministic DBA is associated with each DBE that includes the required safety function challenges, but the DBA analysis is performed with the assumption that the required safety functions are performed by SR SSCs." [RG_1.233 §C.1 p.12]
- SER 판단: "However, based on USO's interpretation of statement (a) that NSRST SSCs may continue to function but not perform RSFs, and statement (b), USO incorporated some passive NSRST SSCs performing at a degraded level in their DBA source term analyses." / "The staff determined that USO's interpretation of the guidance and approach to ascribing some amount of degraded performance to passive NSRST SSCs in DBA source term analyses was reasonable, but acceptability is dependent on the design aspects of the SSCs and the level of degraded performance credited." / "Since the design is preliminary, a final determination on the acceptability of this approach to DBA source term analysis will be made at the OL stage when the methodology and complete scope of SSCs credited with degraded performance will be available for review." [SER_KU1_CP §5.1 p.339]
- 메모(한국어): NEI 18-04 §5.3 Task 10과 RG 1.233 p.12의 문언("SR SSC가 RSF를 수행한다고 가정")은 비SR SSC의 비RSF 기능을 배제하지 않는 것으로 읽힐 여지가 있고, SER은 이 읽기와 §5.6.2의 피동 기능 저하 문장을 근거로 피동 NSRST의 저하 성능 credit을 "reasonable"하다고 보았다. 그러나 NEI 18-04 §4.1("the only ones included in the DBA analysis"), 표 3-1("only Safety Related SSCs are available to mitigate"), RG 1.233 p.11("only safety-related (SR) SSCs are available to mitigate the events")은 DBA 완화에 동원되는 SSC를 SR로 한정한다. SER은 이 세 문장을 언급하지 않는다. 또 §5.6.2의 저하 문장은 Table 5-2 심층방어 지침의 맥락에 있고 DBA 해석을 지칭하지 않는다. SER 스스로 최종 판단을 OL 단계로 미루었으므로 권위 문서 사이의 해석 차이가 남는다.
- 노트 상태: SSC_Safety_Classification(checked)이 NEI §4.1과 SER §5.1을 함께 싣고 해설에서 둘을 병기한다. Natrium_SSC_Safety_Classification, Natrium_SER_SSC_Classification_Review(checked)는 SER 쪽만 싣는다. 규칙대로면 SSC_Safety_Classification을 disputed로 둘 후보이다. 사용자 판정 필요.

## 새 후보 U2 DBE 영역에 걸치는 AOO·BDBE의 DBA 지정
- 분류: U (NEI 18-04·RG 1.233 문언의 모호성 대 SER 해석) — 해소(SER이 모호성을 명시하고 NEI 21-07로 해석; NEI 21-07 원문은 vault에 없음)
- 관련 문서: NEI_18-04, RG_1.233, SER_KU1_CP (권위; SER이 인용한 NEI 21-07은 RG 1.253이 승인한 지침이나 vault 원문 없음)
- 기준 조항(U, 모호한 쪽):
  - "DBAs are derived from the DBEs by prescriptively assuming that only Safety Related SSCs are available to mitigate postulated event sequence consequences to within the 10 CFR 50.34 dose limits." [NEI_18-04 Table 3-1 p.14]
  - "However, when the uncertainty bands ... defined by the 5th percentile and 95th percentile of the frequency estimates straddles a frequency boundary, the LBE is evaluated in both LBE categories." [NEI_18-04 §3.2.2 Task 7a p.22]
  - (새 인용) "However, as described in NEI 18-04 Section 3.2.2, "LBE Selection Process," when the uncertainty bands defined by the 5th percentile and 95th percentile of the frequency estimates straddles a frequency boundary, the LBE is evaluated in both LBE categories." [RG_1.233 §C.1 p.11]
- SER 판단(해석):
  - (새 인용) "The language from NEI 18-04 above is not explicit on which evaluations it refers to when it states "the LBE is evaluated."" [SER_KU1_CP §3.4.1 p.226]
  - (새 인용) "Therefore, identifying and evaluating DBAs for these AOOs and BDBEs that extend into the DBE region is an important verification step and the statement in NEI 21-07 highlighted above confirms this approach." [SER_KU1_CP §3.4.1 p.226]
  - (새 인용) "DBAs are also considered LBEs; however, they are derived from the set of DBEs and AOOs and BDBEs with frequency bands extending into the DBE region by deterministically assuming that only safety-related SSCs are available to respond to the event." [SER_KU1_CP §3.4.1 p.225]
  - "The second deviation from RG 1.233 was that USO did not generate DBAs for AOOs and BDBEs with frequency bands that extend into the DBE region when identifying and classifying LBEs." [SER_KU1_CP §3.4.1 p.225]
- 메모(한국어): NEI 18-04와 RG 1.233은 DBA를 DBE에서 유도한다고만 적고, 경계에 걸치는 LBE를 "양쪽 범주에서 평가한다"는 문장이 DBA 지정까지 포함하는지는 적지 않는다. SER은 이 모호성을 명시하고 NEI 21-07 Appendix A를 근거로 DBA 지정까지 포함한다고 해석하여, DBA의 모집합을 "DBE와 DBE 영역에 걸치는 AOO·BDBE"로 넓혔다. 권위 문서가 명시적으로 해석했으므로 해소로 본다. 남는 점은 둘이다. (1) SER은 이를 "deviation from RG 1.233"이라 부르지만 RG 1.233 본문에는 DBA 지정을 직접 요구하는 문장이 없다. (2) 해석의 근거 문장(NEI 21-07)은 SER의 재인용으로만 vault에 있다.
- 노트 상태: Natrium_LBE_Selection(C12로 disputed), Natrium_SER_LBE_Summary_Review, Natrium_SER_BDBE_DBA_Review(checked). 이 항목으로 새로 disputed가 될 노트는 없다. 개념 노트(LBE_Frequency_Categories 해설의 "DBA는 DBE에서 유도") 쪽에 SER 해석을 메모로 다는 것을 권고한다.

## 새 후보 U3 RSF는 mean, risk-significant NSRST는 95th라는 SER 정리
- 분류: U — 해소. D-3과 같은 사항이므로 판정과 인용은 D-3을 따른다.
- 메모(한국어): SER Table 5.1-1은 NEI 18-04 본문(95th)과 용어집(mean)의 차이를 단계별 통계량으로 나누어 정리한다. RSF 판정에 평균을 쓰는 정리는 NEI 18-04 Task 3의 (새 인용) "there are some safety functions classified as RSFs that must be fulfilled to meet the F-C Target for the DBEs using realistic assumptions" [NEI_18-04 §4.1 Task 3 p.42]와도 모순되지 않는다. 별도 disputed 대상은 없다.

## 새 후보 U4 누적 위험 목표의 서법과 한정어 (C65(3) 확장)
- 분류: U (RG 1.233 대 NEI 18-04 대 RG 1.253 대 SER) — 표기(수치 동일), 미해소
- 관련 문서: RG_1.233, NEI_18-04, RG_1.253, SER_KU1_CP (권위)
- 기준 조항(U):
  - "The total frequency of exceeding a site boundary dose of 100 millirem (mrem) from all LBEs shall not exceed 1/plant-year." [RG_1.233 §C.1 p.13] (셋째까지 모두 "shall")
  - "The total mean frequency of exceeding a site boundary dose of 100 mrem from all LBEs should not exceed 1/plant-year." [NEI_18-04 §3.2.2 Task 7b p.24]
  - "The average individual risk of early fatality within 1 mile of the EAB from all LBEs based on mean estimates of frequencies and consequences shall not exceed 5E-07/plant-year" [NEI_18-04 §3.2.2 Task 7b p.24]
  - "The average individual risk of early fatality within 1 mile of the EAB from all LBEs, based on mean estimates of frequencies and consequences should not exceed 5E-07/plant-year" [RG_1.253 §5 p.18] (셋 모두 "should")
  - (새 인용) "These three cumulative risk metrics as defined in NEI 18-04 are:" [SER_KU1_CP §4.1.1 p.323], 이어서 "The average individual risk of early fatality within one mile of the exclusion area boundary (EAB) from LBEs, based on mean estimates of frequencies and consequences, should not exceed 5E-07 per plant-year." [SER_KU1_CP §4.1.1 p.323]
  - 참고: "The staff notes that the methods, approaches, and data described in the regulatory guidance positions below are considered guidance and not requirements." [RG_1.253 §C p.10]
- 메모(한국어): 세 목표의 수치(1/plant-year, 5E-07, 2E-06)는 네 문서에서 같다. 서법은 RG 1.233이 셋 모두 "shall", NEI 18-04가 "should·shall·shall", RG 1.253과 SER이 셋 모두 "should"이다. SER은 "should" 문장을 "as defined in NEI 18-04"라고 소개하지만 NEI 원문의 둘째·셋째 목표는 "shall"이다. 또 RG 1.233의 첫 목표에는 NEI·RG 1.253의 "mean" 한정어가 없다. 어느 권위 문서도 이 목표가 의무 기준인지 지침상의 목표인지를 서로 맞추어 정리하지 않는다. 판정 결과(목표 충족 여부)에는 영향이 없으므로 C65(3)에 RG 1.233·SER을 더해 하나로 기록할 것을 권고한다.
- 노트 상태: Cumulative_Risk_Targets, RG_1253_Integrated_Evaluation_And_SSC_Positions, Natrium_SER_Integrated_Evaluation_Review, Natrium_Integrated_Risk_Results(모두 checked). C65가 갈래 B(기록만)로 정해지면 disputed 불요. 규칙을 엄격히 적용할지는 사용자 판정 필요.

## 새 후보 U5 SER 안의 "mean"과 "50th percentile"
- 분류: U (SER_KU1_CP 내부) — 표기
- 관련 문서: SER_KU1_CP (권위)
- 기준 조항(U):
  - "This is because USO used the mean frequency when categorizing events as BDBEs against the 5E-07 lower bound." [SER_KU1_CP §3.7.1 p.261]
  - (새 인용) "the staff determined that USO's use of the 50th percentile did not impact the conclusions in the PSAR." [SER_KU1_CP §3.7.1 p.261]
- 메모(한국어): 같은 문단이 사업자의 BDBE 분류 통계량을 처음에는 평균(mean), 결론 문장에서는 50th percentile(중앙값)로 적는다. 평균과 중앙값은 일반적으로 다른 통계량이다. 같은 SER §3.4.1 p.225와 이 문단 앞부분이 모두 "mean"이므로 운용 기준의 해석에는 영향이 없다고 보이나, 원문 오기는 교정하지 않는다.
- 노트 상태: 이 문장을 인용한 노트 없음. 기록만 권고.

## 새 후보 U6 OQE 포함 대 NEI 18-04 누적 위험 범위 (검토 결과 U 아님)
- 분류: N (신청자 이탈, SER 수용) — 권위 문서끼리의 상충은 아님
- 관련 문서: NEI_18-04, SER_KU1_CP (권위), PSAR_ch04 (신청자)
- 기준 조항(N): "The average individual risk of early fatality within 1 mile of the EAB from all LBEs based on mean estimates of frequencies and consequences shall not exceed 5E-07/plant-year" [NEI_18-04 §3.2.2 Task 7b p.24]; "Event sequences with upper 95th percentile frequencies less than 5E-07/plant-year are retained in the PRA results and used to confirm that there are no cliff-edge effects." [NEI_18-04 §3.2.2 Task 4 p.21]
- SER 판단: "The staff compared the cumulative risk metrics in PSAR section 4.1 to the guidance in NEI 18-04 and determined that the metrics were consistent with the exception that OQEs from the PRA were included in the integrated plant performance evaluation in addition to the LBEs required in the LMP methodology." / "The staff determined that this deviation was acceptable because the content of information in PSAR section 4.1 is consistent with the guidance for the content of construction permit (CP) applications found in section C.4.1 of NEI 21-07 as endorsed by RG 1.253 with certain clarifications, and the inclusion of the OQEs adds additional information in the integrated plant performance evaluation." [SER_KU1_CP §4.1.1 p.323]
- 메모(한국어): NEI 18-04는 누적 목표를 "all LBEs"에 대해 평가하고 LBE 하한 아래 사건은 cliff edge 확인용으로 PRA에 남긴다고 적는다. 사업자는 하한 아래 사건(OQE)까지 누적 평가에 넣었고, SER은 이를 NEI 18-04 방법론에서의 이탈로 명시한 뒤 수용했다. SER이 같은 절에서 RG 1.233·RG 1.253과 "consistent"하다고 적은 것은 내용 지침(NEI 21-07 C.4.1)에 대한 판단이므로 이탈 판정과 모순되지 않는다. 권위 문서끼리의 상충이 아니므로 U가 아니다.
- 노트 상태: Natrium_Integrated_Risk_Results, Natrium_SER_Integrated_Evaluation_Review(checked). disputed 불요. N 항목으로 contradictions.md에 기록할지는 다른 범위 판정과 함께 정한다.

## 새 후보 U7 RG 1.232의 단일고장 기준 대 RG 1.233·NEI 18-04 (검토 결과 해소)
- 분류: U — 해소(RG 1.233 C.1.d가 명시적으로 정리)
- 관련 문서: RG_1.232, RG_1.233, NEI_18-04 (권위)
- 기준 조항: "RG 1.232 describes an approach that maintains the single-failure criterion, but acknowledges the potential future benefits of risk informing the non-LWR design criteria." [RG_1.233 §C.1.d p.15]; "The staff finds that the NEI 18-04 methodology, including assessments of event sequences and DID, obviates the need to use the single-failure criterion as it is applied to the deterministic evaluations of AOOs and DBAs for LWRs." [RG_1.233 §C.1.d p.15]
- 메모(한국어): RG 1.232 설계기준(예: SFR-DC 35의 단일고장 문단)은 단일고장 기준을 유지하고, NEI 18-04 방법론은 이를 쓰지 않는다. RG 1.233 C.1.d가 두 접근의 관계(NEI 18-04를 쓰면 불요, 다른 방법론이면 유지 또는 정당화)를 명시하므로 상충이 아니다.
- 노트 상태: 변경 없음.

## 새 후보 U8 RG 1.253의 PDC 범위(NSRST 포함) 대 RG 1.233의 "NSRST는 RFDC와 직접 연결되지 않음" (검토 결과 해소)
- 분류: U — 해소(RG 1.253 C.6.a(2)가 두 층 PDC로 명시)
- 관련 문서: RG_1.233, RG_1.253 (권위)
- 기준 조항: "NEI 18-04 states that NSRST SSCs are not directly associated with RFDC but are subject to special treatment as a result of risk significance or assessments of DID." [RG_1.233 §C.2 p.17]; "For applicants using the LMP process endorsed in RG 1.233, SSCs important to safety include both SR and NSRST SSCs." [RG_1.253 §C.6.a(2) p.20]; "This two-tiered approach proposed in NEI 21-07, Revision 1, divides PDC into PDC-RFDC and PDC-CDC." [RG_1.253 §C.6.a(2) p.20]
- 메모(한국어): RG 1.253은 PDC가 NSRST 기능도 다루어야 한다고 하면서, NSRST는 RFDC가 아니라 PDC-CDC로 다룬다는 구조를 함께 적는다. RG 1.233의 문장(NSRST는 RFDC와 직접 연결되지 않음)과 양립한다.
- 노트 상태: 변경 없음.

## 새 후보 U9 RG 1.233의 PRA 범위 대 RG 1.253 A.3.3 CP 최소 범위 (검토 결과 해소; C66과 대비)
- 분류: U — 해소(RG 1.233 문장 자체가 단계 한정어를 가짐)
- 관련 문서: RG_1.233, RG_1.253 (권위)
- 기준 조항: "The scope of the PRA, when completed, should cover internal and external hazards and provide an estimate of radiological consequences when the design is completed and site characteristics are defined." [RG_1.233 §C.1 p.11]; "the minimum scope of the CP PRA logic model should include the internal events hazard group for the reactor in the at-power POS." [RG_1.253 §A.3.3 p.33]
- 메모(한국어): RG 1.233은 전 hazard 범위를 "when completed", "when the design is completed and site characteristics are defined"로 한정하므로 RG 1.253의 CP 최소 범위와 상충하지 않는다. RG 1.247 C.1.1의 "must always"에는 이런 한정어가 없어 C66이 남는 것과 대비된다.
- 노트 상태: 변경 없음.

---

## 표 1. 항목별 분류 요약

| 항목 | 내용 | 분류 | 해소 여부 | 근거 권위 조항 |
|---|---|---|---|---|
| D-1 | BDBE 하한 mean 대 95th | U (NEI 내부) | 해소 | RG_1.233 §C.1.b p.14; SER §3.7.1 p.261, §3.4.1 p.225 |
| D-2 | RS LBE 판정 mean 대 95th | U (NEI 내부) | 해소 | RG_1.233 §C.1 p.13 |
| D-3 | RS SSC 첫 기준 mean 대 95th | U (NEI 내부) | 해소(SER 근거, 사용자 확인 권장) | SER Table 5.1-1 p.343, §5.1 p.337, §5.5 p.353 |
| D-4 | §5.3 Task 1의 "Task 14" | U (NEI 내부) | 표기, 오기 여부 판단 보류 | 없음 |
| D-5 | 용어집 RI 출처 칸 | U (NEI 내부) | 표기 | 없음 |
| D-6 | Task 7c "within 1%" 대 "exceeds 1%" | U (NEI 내부) | 해소 | NEI §4.2.2 p.47 수치; SER §5.5 p.353 |
| U1 | 피동 NSRST 저하 성능 DBA credit | U (SER 대 NEI·RG 1.233) | 미해소(SER도 OL 이연) | NEI §4.1 p.44, Table 3-1 p.14; RG_1.233 §C.1 p.11; SER §5.1 p.339 |
| U2 | DBE 영역 AOO·BDBE의 DBA 지정 | U (NEI·RG 1.233 모호) | 해소(SER 해석) | SER §3.4.1 p.225-226 |
| U3 | RSF mean / NSRST 95th | U | 해소(D-3과 같음) | SER Table 5.1-1 p.343 |
| U4 | 누적 목표 서법·한정어 | U (4문서) | 표기, 미해소 | RG_1.233 §C.1 p.13; NEI Task 7b p.24; RG_1.253 §5 p.18; SER §4.1.1 p.323 |
| U5 | SER "mean" 대 "50th percentile" | U (SER 내부) | 표기 | 없음 |
| U6 | OQE 포함 | N (U 아님) | SER 수용 | SER §4.1.1 p.323 |
| U7 | RG 1.232 단일고장 대 NEI 18-04 | U | 해소 | RG_1.233 §C.1.d p.15 |
| U8 | PDC 범위 NSRST 포함 | U | 해소 | RG_1.253 §C.6.a(2) p.20 |
| U9 | RG 1.233 PRA 범위 대 RG 1.253 A.3.3 | U | 해소 | RG_1.233 §C.1 p.11 |

건수: 대상 범위 9개 하위 항목(D-1–D-6 가운데 D-2·D-3이 LBE_Risk_Significance의 두 쟁점) — U 6건(해소 4, 표기 2[D-4는 오기 여부 판단 보류 포함]), N 0, I 0. 추가 과제 9건 — U 8건(미해소 1: U1; 미해소 표기 1: U4; 표기 1: U5; 해소 5: U2, U3, U7, U8, U9), N 1건(U6).

## 표 2. 노트별 disputed 유지/해제 권고

| 노트 | 현재 | 권고 | 근거 항목 | 비고 |
|---|---|---|---|---|
| LBE_Frequency_Categories | disputed | 해제 | D-1(해소) | 해설에 RG 1.233 C.1.b와 SER §3.7.1 p.261 메모 추가. C13 하위 항목과 판정 일치 필요 |
| LBE_Risk_Significance | disputed | 해제 | D-2(해소, RG), D-3(해소, SER) | D-3을 SER 근거로 해소하지 않기로 하면 유지 |
| Risk_Importance_Measures | disputed | 해제 | D-3(해소, SER) | 같은 조건부 |
| Risk_Significant_SSC | disputed | 해제 | D-3(해소, SER) | 같은 조건부. lint 2026-10-16 낡은 서술 8항(SER Table 5.1-1 미반영)도 함께 해소 |
| SSC_Safety_Classification | checked | disputed 후보 | U1(미해소) | NEI §4.1과 SER §5.1을 함께 싣는 노트. 사용자 판정 필요 |
| Cumulative_Risk_Targets 외 누적 목표 노트 3개 | checked | 변경 없음(권고) | U4(표기) | C65(3) 확장으로 기록만 |
| RG_1233_LBE_Staff_Position | disputed(C13) | 범위 밖 | D-1과 같은 쟁점 | C13 판정 때 D-1 근거를 함께 검토 |
| Natrium_LBE_Selection | disputed(C12) | 범위 밖 | U2(해소) | U2로는 상태 변화 없음 |
