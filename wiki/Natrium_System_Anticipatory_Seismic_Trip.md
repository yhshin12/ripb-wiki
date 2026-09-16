---
type: natrium
aliases: []
sources:
- PSAR_ch07
- PSAR_ch01
- PSAR_ch05
- ACRS_ML25293A458
status: checked
verified: 2026-09-16
term: null
tags:
- natrium
- psar-ch7
terms_pending: []
---

# Natrium Anticipatory Automatic Seismic Trip System (AST)

> [!abstract] 요약
> Anticipatory Automatic Seismic Trip System(`AST`)은 지반 운동을 측정해 Safe Shutdown Earthquake%%t:SSE%%보다 큰 seismic beyond design basis event에서 최대 지진파 도달 전에 `RTB`의 shunt trip feature로 scram 신호를 보내는 Non-Safety-Related with Special Treatment%%t:NSRST%% 계통이다. 네 channel과 `RTB`의 2-out-of-4 배열로 `DL4-RC4`를 수행하며, 장비 위치와 일부 principal design criteria%%t:PDC%% 구현 세부는 operating license%%t:OL%% 단계로 넘겨진다.

## 원문 사실
- "The Anticipatory Automatic Seismic Trip System (AST) measures ground motion, applies required signal processing and logic, and automatically generates output actuation signals to the Reactor Trip Breakers (RTBs) through the interface device provided by the Reactor Protection System (RPS) when required by seismic conditions." [PSAR_ch07 §7.6.8.1 p.320]
- "The RTB interface device is located downstream of the RPS logic process, where an analog relay matrix is deployed as an isolation device to control the RTB power supply." [PSAR_ch07 §7.6.8.1 p.320]
- "The AST is used during seismic beyond design basis events greater than the safe shutdown earthquake to scram the reactor before the peak seismic wave reaches the facility." [PSAR_ch07 §7.6.8.1 p.320]
- "Seismic design is described in Section 6.4.1." [PSAR_ch07 §7.6.8.1 p.320]
- "The RPS is described in Section 7.6.3." [PSAR_ch07 §7.6.8.1 p.320]
- "The AST consists of four channels, each channel includes triaxial seismic accelerometers, a signal processing unit, and a bi-stable unit." [PSAR_ch07 §7.6.8.1.1 p.320]
- "The triaxial accelerometers are placed in four different quadrants equidistantly spaced around the Reactor Building (RXB)." [PSAR_ch07 §7.6.8.1.1 p.320]
- "The RXB is described in Section 7.8.1." [PSAR_ch07 §7.6.8.1.1 p.320]
- "Each signal processing unit receives input from the triaxial accelerometers and produces an output to the bistable unit." [PSAR_ch07 §7.6.8.1.1 p.320]
- "If the signal processing unit output exceeds the bi-stable unit setpoint, then the bi-stable unit ouputs an isolated signal to the shunt trip feature in the RTB." [PSAR_ch07 §7.6.8.1.1 p.320]
- "The RTB arrangement constitutes 2-out-of-4 logic for the reactor scram function." [PSAR_ch07 §7.6.8.1.1 p.320]
- "The RTB arrangement prevents spurious actuation caused by a failure of a single AST channel since two RTBs allocated to different AST channels are needed to cause a reactor trip." [PSAR_ch07 §7.6.8.1.1 p.320]
- "The AST signals and interfaces are shown in Figure 7.6.8-1." [PSAR_ch07 §7.6.8.1.1 p.320]
- "The triaxial seismic accelerometers are located in boreholes at four locations at 90-degree angles around the RXB." [PSAR_ch07 §7.6.8.1.2 p.320]
- "The signal processing takes place in cabinets in the Nuclear Island Control Building substructure." [PSAR_ch07 §7.6.8.1.2 p.320]
- "The specific locations of cabinets and other AST structures, systems, or components (SSCs) will be described at the operating license (OL) stage." [PSAR_ch07 §7.6.8.1.2 p.320]
- "The AST is designed to perform a non-safety-related with special treatment (NSRST) function." [PSAR_ch07 §7.6.8.2 p.320]
- "A description of the process for assigning NSRST functions to the AST is provided in Section 7.6.1.1.1." [PSAR_ch07 §7.6.8.2 p.320]
- "A description of the process for describing the safety classification of the AST is provided in Section 7.6.1.2." [PSAR_ch07 §7.6.8.2 p.320]
- "The NSRST function assigned to the AST is described in Section 7.6.8.2.1." [PSAR_ch07 §7.6.8.2 p.320]
- "The application of PDC to the AST is described in Section 7.6.8.2.2." [PSAR_ch07 §7.6.8.2 p.320]
- "Special treatments are applied to safety-significant AST SSCs to meet quality, design, reliability, and performance requirements." [PSAR_ch07 §7.6.8.2 p.320]
- "Special treatments are initially selected based on SSC safety classification as described in Section 6.3." [PSAR_ch07 §7.6.8.2 p.320]
- "Special treatments specific to AST fundamental design principles are described in Section 7.6.8.3." [PSAR_ch07 §7.6.8.2 p.320]
- "The following programmatic special treatments are identified as applicable to the AST and the associated summary program descriptions are provided:" [PSAR_ch07 §7.6.8.2 p.320]
- "Design Reliability Assurance Program (Table 8.0-1)" [PSAR_ch07 §7.6.8.2 p.321]
- "Equipment Qualification Program (Table 8.0-1)" [PSAR_ch07 §7.6.8.2 p.321]
- "Post-construction inspection, testing, and analysis program (Chapter 12)" [PSAR_ch07 §7.6.8.2 p.321]
- "Quality Assurance Program Description (Section 8.1)" [PSAR_ch07 §7.6.8.2 p.321]
- "The AST conforms to regulatory guides (RGs) as follows:" [PSAR_ch07 §7.6.8.2 p.321]
- "RG 1.53, Revision 2, Application of the Single-Failure Criterion to Safety Systems" [PSAR_ch07 §7.6.8.2 p.321]
- "The AST partially conform to RG 1.53, Revision 2." [PSAR_ch07 §7.6.8.2 p.321]
- "Conformance is partial because IEEE 379-2014, “IEEE Standard for Application of the Single-Failure Criterion to Nuclear Power Generating Station Safety Systems,” (Reference 7.6.8-1) is used rather than the version of the standard endorsed by this RG." [PSAR_ch07 §7.6.8.2 p.321]
- "RG 1.100, Revision 4, Seismic Qualification and Mechanical Equipment for Nuclear Power Plants" [PSAR_ch07 §7.6.8.2 p.321]
- "The AST partially conforms to RG 1.100, Revision 4." [PSAR_ch07 §7.6.8.2 p.321]
- "Conformance is partial because IEEE/IEC 60980-344-2020, “Nuclear Facilities- Equipment Important to Safety-Seismic Qualification,” (Reference 7.6.8-2) is used rather than the version of the standard endorsed by this RG." [PSAR_ch07 §7.6.8.2 p.321]
- "RG 1.118, Revision 3, Periodic Testing of Electric Power and Protection Systems" [PSAR_ch07 §7.6.8.2 p.321]
- "The AST partially conforms to RG 1.118, Revision 3." [PSAR_ch07 §7.6.8.2 p.321]
- "Conformance is partial because IEEE 338-2022, “IEEE Standard for Criteria for the Periodic Surveillance Testing of Nuclear Power Generating Station Safety Systems,” (Reference 7.6.8-3) is used rather than the version of the standard endorsed by this RG." [PSAR_ch07 §7.6.8.2 p.321]
- "RG 1.180, Revision 2, Guidelines for Evaluating Electromagnetic and Radio-Frequency Interference in Safety-Related Instrumentation and Control Systems" [PSAR_ch07 §7.6.8.2 p.321]
- "The AST fully conforms to RG 1.180, Revision 2." [PSAR_ch07 §7.6.8.2 p.321]
- "PRA safety functions (PSFs) are determined through the plant-specific PRA described in Section 3.1." [PSAR_ch07 §7.6.8.2.1 p.321]
- "The safety-significant PSFs are identified as safety-related (SR) functions or NSRST functions as defined in Section 5.2." [PSAR_ch07 §7.6.8.2.1 p.321]

| Function ID | Function Description | AST Functional Support | 출처 |
|---|---|---|---|
| DL4-RC4 | Automatic seismic trip | The AST continuously monitors signal inputs from triaxial accelerometers and sends an isolated signal to the shunt trip feature in the RTBs when the signal inputs exceed a bi-stable setpoint. | [PSAR_ch07 §7.6.8.2.1 p.322] |

- "PDC are described in Section 5.3." [PSAR_ch07 §7.6.8.2.2 p.322]
- "The AST conforms to PDC as described below." [PSAR_ch07 §7.6.8.2.2 p.322]
- "Consistent with PDC 2, Design based for protection against natural phenomena, the AST is seismically qualified for postulated earthquake." [PSAR_ch07 §7.6.8.2.2 p.322]
- "The AST SSCs are protected from external flooding, high winds, and extreme climate." [PSAR_ch07 §7.6.8.2.2 p.322]
- "Below grade SSCs are provided with subgrade waterproofing and evaluated for hydrologic loads if applicable." [PSAR_ch07 §7.6.8.2.2 p.322]
- "Additional details of the implementation of this PDC will be provided with equipment locations at the OL stage." [PSAR_ch07 §7.6.8.2.2 p.322]
- "Consistent with PDC 3, Fire protection, the AST is protected from fire hazards based upon the location of its SSCs." [PSAR_ch07 §7.6.8.2.2 p.322]
- "Additional details of the implementation of this PDC will be provided with equipment locations at the OL stage." [PSAR_ch07 §7.6.8.2.2 p.322]
- "Consistent with PDC 4, Environmental and dynamic effects design basis, the AST processing cabinets are located in and protected from external hazards by the Nuclear Island Control Building." [PSAR_ch07 §7.6.8.2.2 p.322]
- "The NCB is described in Section 7.8.4.1." [PSAR_ch07 §7.6.8.2.2 p.322]
- "Consistent with PDC 13, Instrumentation and control, the AST monitors and measures ground motion, applies required processing and logic to calculate the seismic threat level, and automatically generates signals to open the RTBs." [PSAR_ch07 §7.6.8.2.2 p.322]
- "The AST monitors the anticipated range of seismic activities to ensure a reactor scram is initiated with adequate margin during a seismic event." [PSAR_ch07 §7.6.8.2.2 p.322]
- "Consistent with PDC 24, Separation of protection and control systems, interconnection of the RPS and the AST is limited to the interface with the RTBs." [PSAR_ch07 §7.6.8.2.2 p.322]
- "The RPS is separated and isolated from the AST to the extent that any single failure of an AST component or channel, or failure or removal from service of a single protection system component or channel which is common to the AST and RPS, leaves intact a system satisfying all reliability, redundancy, and independence requirements of the RPS." [PSAR_ch07 §7.6.8.2.2 p.322]
- "The AST design includes elements of quality that minimize the potential for failures to occur in SSCs associated with NSRST functions." [PSAR_ch07 §7.6.8.3 p.322]
- "These properties of qualification, reliability, robustness, security, diversity, and defense-in-depth features are discussed in Section 7.6.8.3.1 through Section 7.6.8.3.4." [PSAR_ch07 §7.6.8.3 p.322]
- "The following industry codes and standards are applied as special treatments to the overall design of safety-significant AST SSCs:" [PSAR_ch07 §7.6.8.3 p.322]

| 목록 항목 | 출처 |
|---|---|
| IEEE 379-2014, | [PSAR_ch07 §7.6.8.3 p.322] |

- "IEEE 384-2018, “IEEE Standard Criteria for Independence of Class 1E Equipment and Circuits” (Reference 7.6.8-4)" [PSAR_ch07 §7.6.8.3 p.323]
- "Seismic classifications for AST components are determined in accordance with the methods described in Section 6.4.1." [PSAR_ch07 §7.6.8.3 p.323]
- "Seismic special treatments are applied based on the seismic classification." [PSAR_ch07 §7.6.8.3 p.323]
- "The seismic classification of AST components is SCN1." [PSAR_ch07 §7.6.8.3 p.323]
- "Seismic design, analysis, and qualification is performed as described in Section 6.4." [PSAR_ch07 §7.6.8.3 p.323]
- "The AST is qualified per the Equipment Qualification Program described in Table 8.0-1." [PSAR_ch07 §7.6.8.3.1 p.323]
- "The method for confirming specific reliability and capability targets for SSCs at the OL stage is described in Section 6.2." [PSAR_ch07 §7.6.8.3.2 p.323]
- "IEEE 384-2018 is applied as a special treatment to the AST to ensure equipment is distinctly identified for each redundant portion of the system." [PSAR_ch07 §7.6.8.3.2 p.323]
- "The AST equipment is designed and reviewed per the Human Factors Engineering Program Plan described in Section 11.2." [PSAR_ch07 §7.6.8.3.2 p.323]
- "Reliability of the AST is addressed through the Design Reliability Assurance Program described in Table 8.0-1." [PSAR_ch07 §7.6.8.3.2 p.323]
- "The AST conforms to IEEE 338-2022 for testing and calibration capabilities." [PSAR_ch07 §7.6.8.3.2 p.323]
- "Robustness of the AST design is the degree to which it can perform its NSRST function in the presence of invalid inputs or stressful environmental conditions." [PSAR_ch07 §7.6.8.3.3 p.323]
- "The following elements are considered for system robustness:" [PSAR_ch07 §7.6.8.3.3 p.323]
- "Single failure is addressed by applying IEEE 379-2014 as a special treatment to the design of the AST." [PSAR_ch07 §7.6.8.3.3 p.323]
- "IEEE 384-2018 is applied as a special treatment to the AST in order to meet independence requirements." [PSAR_ch07 §7.6.8.3.3 p.324]
- "Security for I&C systems is addressed through the physical security and cyber security programs that are described in Section 11.6." [PSAR_ch07 §7.6.8.3.4 p.324]
- "Anticipatory Automatic Seismic Trip System" [PSAR_ch01 §LIST OF ACRONYMS AND ABBREVIATIONS p.5]
- "AST - Alternative Shunt Trip" [ACRS_ML25293A458 Acronyms p.22]
- "AST provides alternate means of tripping RTBs via shunt trip feature" [ACRS_ML25293A458 Gravity scram functions p.15]
- "Alternative shunt trips (DL4-RC6 and subfunctions)" [ACRS_ML25293A458 Gravity scram functions p.15]
- "Alternative Shunt Trip on High Core Exit Temperature" [PSAR_ch05 Table 5.2-4 p.17]
- "The requirement has not yet been integrated into the design and is therefore not discussed further in the construction permit application." [PSAR_ch05 Table 5.2-4 p.20]
- "DL4-RC6(a-d) is identified as a defense line function in the most recent revision of the PRA." [PSAR_ch05 Table 5.2-4 p.20]

- "Figure 7.6.8-1 AST Signals and Interface" [PSAR_ch07 Figure 7.6.8-1 p.325]

![[PSAR_ch07_Fig_7.6.8-1.png]]

## 해설
Anticipatory Automatic Seismic Trip System(`AST`)은 지반 운동을 측정하고 신호 처리와 논리를 적용해, 지진 조건이 요구하면 `RPS`가 제공하는 interface device를 거쳐 Reactor Trip Breaker(`RTB`)에 작동 신호를 자동으로 보낸다. `RTB` interface device는 `RPS` 논리 공정 하류에 있고, 아날로그 relay matrix가 격리 장치로서 `RTB` 전원을 제어한다. 원문은 `AST`가 Safe Shutdown Earthquake%%t:SSE%%보다 큰 seismic beyond design basis event에서 최대 지진파가 시설에 닿기 전에 원자로를 scram하는 데 쓰인다고 적는다.

`AST`는 네 channel로 이루어지고, 각 channel은 triaxial 지진 가속도계, 신호 처리 장치, bi-stable unit을 갖는다. 가속도계는 `RXB` 둘레 네 사분면에 같은 간격으로, 90-degree 각도의 네 위치 borehole에 있다. 신호 처리 출력이 bi-stable unit setpoint를 넘으면 bi-stable unit이 격리 신호를 `RTB`의 shunt trip feature로 보낸다. `RTB` 배열은 reactor scram 기능에 대해 2-out-of-4 논리를 이루며, 서로 다른 `AST` channel에 배정된 두 `RTB`가 있어야 trip하므로 한 channel 고장에 의한 spurious actuation을 막는다. 신호 처리는 `NCB` 하부구조 캐비닛에서 이루어지고, 캐비닛과 다른 `AST` Structures, Systems, and Components%%t:SSC%%의 구체 위치는 OL%%t:OL%% 단계에서 기술된다.

`AST`는 NSRST%%t:NSRST%% 기능을 수행하도록 설계되고, 기능 표의 유일한 기능은 `DL4-RC4`(Automatic seismic trip)이다. programmatic special treatment는 Design Reliability Assurance Program, Equipment Qualification Program, Post-construction inspection, testing, and analysis program, Quality Assurance Program Description이다. regulatory guide%%t:RG%% 부합은 `RG 1.53, Revision 2`, `RG 1.100, Revision 4`, `RG 1.118, Revision 3`이 부분 부합이고 `RG 1.180, Revision 2`는 완전 부합이다. 부분 부합의 이유는 각각 `IEEE 379-2014`, `IEEE/IEC 60980-344-2020`, `IEEE 338-2022`를 해당 RG%%t:RG%%가 인정한 판 대신 쓰기 때문이다.

PDC%%t:PDC%% 2에 따라 `AST`는 가상 지진에 대해 지진 검증을 받고 외부 홍수, 강풍, 극한 기후에서 보호되며, 지표 아래 SSC%%t:SSC%%는 방수 처리와 필요 시 수문 하중 평가를 받는다. PDC%%t:PDC%% 2와 3의 구현 세부는 장비 위치와 함께 OL%%t:OL%% 단계에서 제공된다. PDC%%t:PDC%% 4에 따라 처리 캐비닛은 `NCB`가 외부 재해에서 보호한다. PDC%%t:PDC%% 13에 따라 `AST`는 지진 위협 수준을 계산해 `RTB`를 여는 신호를 만들고, 예상 지진 활동 범위를 감시해 적절한 여유로 scram이 개시되게 한다. PDC%%t:PDC%% 24에 따라 `RPS`와 `AST`의 상호 연결은 `RTB` 인터페이스로 한정되며, `AST` 구성품이나 channel의 단일 고장이 `RPS`의 신뢰도·이중화·독립성 요건을 해치지 않도록 분리·격리된다.

`IEEE 379-2014`와 `IEEE 384-2018`이 설계 special treatment이며, 각각 single failure와 독립성·식별에 적용된다. 구성품 지진 분류는 `SCN1`이다. 신뢰성은 Design Reliability Assurance Program으로, 시험·교정 능력은 `IEEE 338-2022` 부합으로, 인간공학은 Human Factors Engineering Program Plan으로 다룬다.

약어 `AST`의 뜻은 원문마다 다르다. `PSAR` Chapter 1 약어표와 Chapter 7은 Anticipatory Automatic Seismic Trip System으로 적고, `ACRS_ML25293A458` 발표 약어표는 `Alternative Shunt Trip`으로 적으며 `AST`가 shunt trip feature로 `RTB`를 trip하는 대체 수단을 제공한다고 적는다. `PSAR` Chapter 5 표에는 `Alternative Shunt Trip on High Core Exit Temperature`가 있고, `DL4-RC6(a-d)`가 최신 `PRA` 개정에서 defense line 기능으로 식별되었으나 그 요건이 아직 설계에 반영되지 않았다는 주석이 있다. `ACRS` 발표도 alternative shunt trip을 `DL4-RC6`과 그 하위 기능으로 묶으므로, Chapter 7의 `AST`가 수행하는 `DL4-RC4`와는 다른 기능이다. 이 차이는 `meta/contradictions.md` C7에 모았다.

## 관련 문서
- [[Natrium_System_Reactor_Protection]]
- [[Natrium_System_IC_Architecture]]
- [[Natrium_NRC_Review_Reactivity_Control]]
- [[Natrium_NSRST_Functions]]
- [[Natrium_Seismic_Classification]]
- [[PSAR_ch07]]
