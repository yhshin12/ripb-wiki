---
type: natrium
aliases: []
sources: [SER_KU1_CP]
status: checked
verified: 2026-10-16
term:
tags: [natrium, systems, decay-heat-removal, nrc-review]
terms_pending: []
---
# NRC의 원자로 보조 계통 평가 (NRC Evaluation of the Reactor Auxiliary Systems)

> [!abstract] 요약
> NRC staff는 원자로 공기 냉각 계통(`RAC`), 중간 공기 냉각 계통(`IAC`), 소듐 커버가스(cover gas)%%t:COVER_GAS%% 계통(`SCG`), 소듐 정화 계통(`SPS`), 제어봉 구동 계통(`CRD`) 각각에 대해 `PSAR` 정보가 construction permit 발급에 충분하다고 결론지었다. `RAC`는 계측을 뺀 기기가 Safety-Related%%t:SR%%인 계통으로 많은 Design Basis Accident%%t:DBA%%의 열제거를 맡고, `IAC`는 저출력·정지 시 주 열제거 수단인 Non-Safety-Related with Special Treatment%%t:NSRST%% 계통이며, `ISP`와 `RAC`를 쓸 수 없을 때 대체 열제거 수단이 된다. `RAC` 열전달 성능 확인, 누설률 정당화, `SCG` 격리 기능의 최종 설계 통합, 합금 718 구동축 설계 같은 항목은 operating license 단계에서 검토한다.

## 원문 사실
- "PSAR section 7.2 describes the reactor auxiliary system SSCs, which are responsible for decay heat removal and support for key safety functions." [SER_KU1_CP §7.2 p.454]
- "The RAC operates continuously without manual or automatic actuation, allowing for long-term emergency core cooling." [SER_KU1_CP §7.2.1 p.455]
- "All RAC components are SR, except for its instrumentation, which is NSRST." [SER_KU1_CP §7.2.1 p.455]
- "Many of the analyzed events, particularly DBAs, rely on the RAC for heat removal." [SER_KU1_CP §7.2.1.1.6 p.458]
- "The staff audited applicant calculations which confirmed the RAC’s capability to maintain adequate performance even with significant blockages." [SER_KU1_CP §7.2.1.1.6 p.458]
- "The staff audited analyses regarding RAC performance in adverse wind conditions and confirmed that RAC performance is maintained, largely due to the design and orientation of the inlet louver assemblies and the design of the chimney cowling." [SER_KU1_CP §7.2.1.1.6 p.458]
- "The staff notes that RAC heat transfer performance is the subject of an R&D item as discussed in SE chapter 13; the staff will confirm RAC performance at the OL stage." [SER_KU1_CP §7.2.1.1.6 p.458]
- "The staff determined that the preliminary RAC design is consistent with DL3-HR4 because all LBEs relying on RAC heat removal maintain fuel integrity and do not result in radiological release." [SER_KU1_CP §7.2.1.1.9.1 p.459]
- "The IAC transfers heat from the IHT to the atmosphere and is the primary means of reactor heat removal during low power and shutdown conditions." [SER_KU1_CP §7.2.2 p.460]
- "All components within the IAC are NSRST. The IAC supports one NSRST function, evaluated below." [SER_KU1_CP §7.2.2 p.460]
- "PSAR section 7.2.2.3 states that one IAC train is sufficient for the limiting decay heat load in both active and blower modes, while passive mode requires both IAC trains." [SER_KU1_CP §7.2.2.1.5 p.462]
- "Upon power loss, natural circulation develops in the IHT, and IAC dampers fail open, allowing natural convection airflow." [SER_KU1_CP §7.2.2.1.5 p.462]
- "The staff determined that the preliminary IAC design is consistent with this function because it allows for an alternate means of heat removal in the event the ISPs and RAC are unavailable." [SER_KU1_CP §7.2.2.1.10.1 p.464]
- "If an AHX sodium leak is detected, dampers will automatically close on the affected ASE." [SER_KU1_CP §7.2.2.1.9 p.464]
- "The primary SCG contains SR, NSRST, and NST SSCs, while the intermediate SCG contains NSRST and NST SSCs, as illustrated in PSAR figures 7.2.3-1 and 7.2.3-2, respectively." [SER_KU1_CP §7.2.3 p.465]
- "PSAR section 7.2.3.2.1 states that the portion of the SCG from the RV up to and including the first isolation valve is SR, part of the primary coolant boundary, and designed and constructed to ASME BPVC III-5." [SER_KU1_CP §7.2.3.1.1 p.466]
- "The staff also expects the SCG to have an associated SARRDL because gaseous radionuclides released from fuel during operation will flow through the primary coolant and enter the SCG." [SER_KU1_CP §7.2.3.1.6 p.470]
- "Note 1 to PSAR table 5.2-3 states that this function will be fail safe with SR detection and actuation signals, but it “has not yet been integrated into the design or analysis and is therefore not discussed further” in the PSAR, including in chapter 7." [SER_KU1_CP §7.2.3.1.8 p.472]
- "The staff will review leakage rate justifications at the OL stage relative to the design of the SSCs comprising each functional containment boundary." [SER_KU1_CP §7.2.3.1.8 p.472]
- "The staff audited the LBEs that rely on this function and determined that a SR SCG isolation function is appropriate for radionuclide retention." [SER_KU1_CP §7.2.3.1.15.1 p.475]
- "PSAR section 7.2.3.2.2 and table 5.2-3 state that the SCG supports seven functions which provide radionuclide retention." [SER_KU1_CP §7.2.3.1.15.1 p.475]
- "PSAR table 5.2-3 does not list any associated LBEs for DL3-RR7. During audit discussion, the applicant stated that the initial cause(s) of a primary overpressure event have not been defined at the preliminary design stage." [SER_KU1_CP §7.2.3.1.15.2 p.477]
- "The purification equipment consists of cold traps which remove impurities, and for the SPS-P, a cesium trap to remove cesium." [SER_KU1_CP §7.2.4 p.478]
- "The SR means to prevent continuous sodium release from the SPS is the SR SPS pump trip and the SPS siphon break, which are evaluated in SE sections 7.2.4.1.14 and 7.2.4.1.7." [SER_KU1_CP §7.2.4.1.6 p.483]
- "Accordingly, the KU1 design targets a low oxygen environment of less than 2 parts per million by weight (ppmw) during operating, shutdown, and refueling conditions." [SER_KU1_CP §7.2.4.1.8 p.484]
- "Hydrogen buildup in the spaces which make up portions of the functional containment is non-credible, as sodium does not react with the fuel or cladding to produce hydrogen (unlike high temperature zircaloy-water reactions in LWRs) and there are no other credible sources of significant amounts of hydrogen." [SER_KU1_CP §7.2.4.1.8 p.485]
- "However, the staff notes that the setpoint for this trip is yet to be determined and will be evaluated by the staff during the OL application review to ensure it supports the development of natural circulation." [SER_KU1_CP §7.2.4.1.14.1 p.487]
- "The staff notes that the SR means of stopping an SPS-P leak is through the securing of the SPS-P pumps (DL3-HR11) rather than through isolation valve closure." [SER_KU1_CP §7.2.4.1.14.3 p.489]
- "There are thirteen control rod drives, all located on top of the reactor head, in the HAA." [SER_KU1_CP §7.2.5 p.491]
- "The staff notes that alloy 718 is an approved material in ASME BPVC III-5 for bolting applications only, which does not include its planned use in the CRD driveline assembly." [SER_KU1_CP §7.2.5.1.1 p.492]
- "However, a potential common cause mechanism that could cause CRAs to fail to insert into the core is binding between the CRA and its associated duct, which could result from seismic motion or significant duct or CRA distortions." [SER_KU1_CP §7.2.5.1.8 p.496]
- "The staff determined that the preliminary CRD design is consistent with PDC 26 because it provides separate gravity scram and motor drive-in functions and uses different primary and secondary CRA designs to mitigate common-cause failure mechanism and ensure sufficient independence and diversity." [SER_KU1_CP §7.2.5.1.8 p.496]
- "DBAs rely entirely on the gravity scram function, as the motor drive-in function is NSRST." [SER_KU1_CP §7.2.5.1.11.1 p.498]
- "Only one of the events, the loss of offsite power with scram motor drive-in, results in the fuel performance acceptance criteria being exceeded. The source term analysis indicates that two-thirds of the fuel fails due to creep rupture." [SER_KU1_CP §7.2.5.1.11.1 p.498]
- "Based on the review described above, the staff concludes that the information in PSAR section 7.2.1 is sufficient and meets the applicable guidance and regulatory requirements identified in this section and at the beginning of this chapter for the issuance of a CP." [SER_KU1_CP §7.2.1.2 p.460]
- "Based on the review described above, the staff concludes that the information in PSAR section 7.2.2 is sufficient" [SER_KU1_CP §7.2.2.2 p.465]
- "Based on the review described above, the staff concludes that the information in PSAR section 7.2.3 is sufficient" [SER_KU1_CP §7.2.3.2 p.478]
- "Based on the review described above, the staff concludes that the information in PSAR section 7.2.4 is sufficient" [SER_KU1_CP §7.2.4.2 p.491]
- "Based on the review described above, the staff concludes that the information in PSAR section 7.2.5 is sufficient" [SER_KU1_CP §7.2.5.2 p.499]
- "identifies a SR SCG isolation function, DL3-RR10, “SCG Isolation,” which is associated with multiple DBEs and BDBEs." [SER_KU1_CP §7.2.3.1.8 p.472]
- "The staff will review the integration of this function into the final design during the OL review." [SER_KU1_CP §7.2.3.1.15.1 p.475]
- "However, several BDBEs do rely on the motor-driven scram function" [SER_KU1_CP §7.2.5.1.11.1 p.498]
- "the staff audited this analysis and found it to be based on conservative assumptions that bound the expected event sequence." [SER_KU1_CP §7.2.5.1.11.1 p.498]
- "the staff determined it is reasonable to leave for later consideration the development of a detailed design and analysis methodology for alloy 718 under ASME BPVC III-5 for its use in the final CRD driveline assembly design." [SER_KU1_CP §7.2.5.1.1 p.492]
- "The staff will review further details on the applicant’s approach to the design and construction of the CRD driveline assembly using alloy 718 consistent with ASME BPVC III-5 at the OL stage." [SER_KU1_CP §7.2.5.1.1 p.492]
- "and there are no other credible sources of significant amounts of hydrogen." [SER_KU1_CP §7.2.4.1.8 p.485]

## 해설
staff는 다섯 계통 각각의 `PSAR` 정보가 construction permit%%t:CP%% 발급에 충분하다고 결론지었다. 계통별 요점은 다음과 같다.

- **원자로 공기 냉각(`RAC`):** 수동·자동 작동 없이 계속 운전하며 장기 비상 노심 냉각을 제공한다. 계측을 뺀 모든 기기가 SR%%t:SR%%이고 계측은 NSRST%%t:NSRST%%이다. 분석된 사건, 특히 DBA%%t:DBA%% 다수가 `RAC` 열제거에 의존한다. 상당한 유로 막힘에서도 성능이 유지됨은 사업자 계산이 확인했고 staff가 이를 audit했으며, 불리한 바람 조건에서의 성능 유지는 staff가 audit로 확인했다. staff는 `RAC`에 의존하는 모든 Licensing Basis Event%%t:LBE%%에서 연료 건전성이 유지되고 방사성 방출이 없으므로 DL3-HR4와 정합한다고 보았다. 열전달 성능은 연구개발 항목이며 operating license%%t:OL%% 단계에서 확인한다.
- **중간 공기 냉각(`IAC`):** 저출력·정지 상태의 주 열제거 수단이며 모든 기기가 NSRST%%t:NSRST%%이다. `PSAR`에 따르면 능동·송풍기 모드는 한 계열로 충분하지만 피동 모드는 두 계열이 모두 필요하다. 전원 상실 시 `IHT`에 자연순환이 생기고 댐퍼가 열린 채로 고장 난다. staff는 `ISP`와 `RAC`를 쓸 수 없을 때 대체 열제거 수단이 된다는 점에서 해당 NSRST%%t:NSRST%% 기능과 정합한다고 보았다.
- **소듐 커버가스%%t:COVER_GAS%%(`SCG`):** 1차 `SCG`에는 SR%%t:SR%%, NSRST%%t:NSRST%%, Non-Safety-Related with No Special Treatment%%t:NST%% 기기가, 중간 `SCG`에는 NSRST%%t:NSRST%%와 NST%%t:NST%% 기기가 있다. `PSAR`에 따르면 원자로 용기에서 첫 격리 밸브까지는 SR%%t:SR%%이며 1차 냉각재 경계의 일부이다. staff는 `SCG`에도 specified acceptable system radionuclide release design limit%%t:SARRDL%%이 있을 것으로 보며, `SCG` 격리 기능(DL3-RR10)을 SR%%t:SR%%로 두는 것이 적절하다고 판단했다. 다만 `PSAR` 표 5.2-3 주석에 따르면 이 격리 기능은 아직 설계와 해석에 통합되지 않았고, staff는 그 통합을 OL%%t:OL%% 검토에서 확인한다. `PSAR`는 방사성핵종 보유 기능을 "seven functions"라 적는다. 사업자는 audit 논의에서 1차 과압 사건의 원인이 예비 설계 단계에서 정의되지 않았다고 밝혔다. 누설률 정당화는 OL%%t:OL%% 단계에서 검토한다.
- **소듐 정화(`SPS`):** 냉각 트랩으로 불순물을, 1차 `SPS`에서는 세슘 트랩으로 세슘을 제거한다. 산소 목표는 2 ppmw 미만이다. 연속 소듐 방출을 막는 SR%%t:SR%% 수단은 `SPS` 펌프 트립과 사이펀 차단이며, 1차 `SPS` 누설을 멈추는 SR%%t:SR%% 수단은 격리 밸브가 아니라 펌프 정지(DL3-HR11)이다. 이 트립의 설정값은 아직 정해지지 않았으며, staff는 OL%%t:OL%% 검토에서 설정값이 자연순환 형성을 뒷받침하는지 평가한다. 소듐은 연료나 피복과 반응해 수소를 만들지 않고 다른 유의한 수소 원천도 없으므로 기능적 격납 공간의 수소 축적은 credible하지 않다.
- **제어봉 구동(`CRD`):** 구동기 열세 개가 `HAA` 안 원자로 헤드 위에 있다. 중력 scram과 모터 삽입 기능을 분리하고 1차·2차 제어봉 설계를 달리해 공통원인 고장에 대응하므로 `PDC 26`과 정합한다고 보았다. 다만 지진이나 덕트 변형에 따른 제어봉-덕트 고착은 잠재적 공통원인 기제이다. DBA%%t:DBA%%는 중력 scram에만 의존한다. 다만 여러 Beyond Design Basis Event%%t:BDBE%%는 모터 구동 scram에 의존하며, 그 가운데 소외전원 상실과 모터 삽입 scram 사건 하나만 연료 성능 수용 기준을 넘고 원천항 해석에서 연료의 two-thirds가 크리프 파열로 파손된다. staff는 이 해석이 예상 사건 경위를 bounding하는 보수적 가정에 근거함을 audit로 확인했다. 합금 718은 `ASME BPVC III-5`에서 볼트 용도로만 승인되어 있으며, staff는 구동축 설계 방법론 개발을 나중으로 미루는 것이 합리적이라고 보고 OL%%t:OL%% 단계에서 검토한다.

## 관련 문서
- [[SER_KU1_CP]]
- [[Natrium_System_Reactor_Air_Cooling]]
- [[Natrium_System_Intermediate_Air_Cooling]]
- [[Natrium_System_Sodium_Cover_Gas]]
- [[Natrium_System_Sodium_Processing]]
- [[Natrium_System_Control_Rod_Drive]]
- [[Natrium_SER_Nuclear_Heat_Supply_Review]]
- [[Natrium_SER_Reactor_Auxiliary_PDC_Conformance]]
