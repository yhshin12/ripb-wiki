---
type: natrium
aliases: []
sources:
- PSAR_ch07
status: disputed
verified: 2026-09-16
term: null
tags:
- natrium
- psar-ch7
terms_pending: []
---

# Natrium Nuclear Instrumentation System (XIS)

> [!abstract] 요약
> Nuclear Instrumentation System(`XIS`)은 노심에서 누설되는 neutron flux를 감지해 `RPS`와 `NIC`에 신호를 주는 네 division의 아날로그 Safety-Related%%t:SR%% 계통이다. `RPS`의 neutron flux 관련 `DL3` scram·trip 기능과 `DL5-PAM1`을 지원하고, SR%%t:SR%% 기능을 수행하는 소프트웨어가 현재 설계에 없어 원문은 신뢰할 만한 common cause failure%%t:CCF%%가 없다고 적는다.

## 원문 사실
- "The analog Nuclear Instrumentation System (XIS) provides instrumentation to sense neutron flux leakage from the core during fuel movement, reactor startup, power operations, shutdown, and accident conditions." [PSAR_ch07 §7.6.4.1 p.281]
- "The XIS is designed to ensure that neutron flux is detected and signals are generated and sent to the RPS within the time assumed in the safety analysis." [PSAR_ch07 §7.6.4.1 p.281]
- "There is one High Temperature Fission Chamber detector for each division (four total)." [PSAR_ch07 §7.6.4.1 p.281]
- "Each detector and associated electronics have the ability to provide three signal ranges, power range, wide range, and source range." [PSAR_ch07 §7.6.4.1 p.281]
- "The source range signal includes an audible count rate variable." [PSAR_ch07 §7.6.4.1 p.281]
- "A wide range neutron flux signal is sent to the RPS and NIC for display as a Type B and D Post-Accident Monitoring (PAM) variable, as defined by IEEE 497-2016, “IEEE Standard Criteria for Accident Monitoring Instrumentation for Nuclear Power Generating Stations,” (Reference 7.6.4-1)." [PSAR_ch07 §7.6.4.1 p.281]
- "The display of PAM variables by the RPS is described in Section 7.6.3.1." [PSAR_ch07 §7.6.4.1 p.281]
- "The XIS is comprised of four redundant divisions, each of which includes a division-specific flux detector and signal conditioning." [PSAR_ch07 §7.6.4.1.1 p.281]
- "Each XIS division is separate and independent from the other XIS divisions." [PSAR_ch07 §7.6.4.1.1 p.281]
- "XIS provides flux signals to RPS in support of safety-related (SR) protective functions, and the four XIS divisions correspond to the four RPS divisions." [PSAR_ch07 §7.6.4.1.1 p.281]
- "Each XIS division interfaces with the corresponding RPS division only, thus maintaining the required XIS divisional separation and RPS divisional separation." [PSAR_ch07 §7.6.4.1.1 p.281]
- "The XIS also provides signals to the NIC in support of control functions which are non-safety-related with no special treatment (NST)." [PSAR_ch07 §7.6.4.1.1 p.282]
- "The NIC subsystems such as Rod Monitoring and Control System and NI Coolant Temperature Monitoring and Control System, which use the XIS signals in real-time control schemes, are provided with isolated hardwired signals from XIS." [PSAR_ch07 §7.6.4.1.1 p.282]
- "The XIS is an SR system supporting SR, non-safety-related with special treatment (NSRST), and NST functions." [PSAR_ch07 §7.6.4.2 p.282]
- "The equipment used to provide the SR neutron flux measurements and functions are also used to support the NSRST and NST functions." [PSAR_ch07 §7.6.4.2 p.282]
- "A description of the process for assigning the safety classification of the XIS is provided in Section 7.6.1.1.2." [PSAR_ch07 §7.6.4.2 p.282]
- "The XIS conforms to regulatory guides (RGs) as follows:" [PSAR_ch07 §7.6.4.2 p.282]
- "RG 1.47, Revision 1, Bypassed and Inoperable Status Indication for Nuclear Power Plant Safety Systems The XIS fully conform to RG 1.47, Revision 1." [PSAR_ch07 §7.6.4.2 p.282]
- "RG 1.53, Revision 2, Application of the Single-Failure Criterion to Safety Systems" [PSAR_ch07 §7.6.4.2 p.282]
- "The XIS partially conforms to RG 1.53, Revision 2." [PSAR_ch07 §7.6.4.2 p.282]
- "Conformance is partial because IEEE 379-2014, “IEEE Standard for Application of the Single-Failure Criterion to Nuclear Power Generating Station Safety Systems,” (Reference 7.6.4-2) is used rather than the version of the standard endorsed by this RG." [PSAR_ch07 §7.6.4.2 p.282]
- "RG 1.75, Revision 3, Physical Independence of Electric Systems" [PSAR_ch07 §7.6.4.2 p.282]
- "Application-specific elements of the RPS partially conform to RG 1.75 Revision 3." [PSAR_ch07 §7.6.4.2 p.282]
- "Conformance is partial because IEEE 384-2018, “IEEE Standard Criteria for Independence of Class 1E Equipment and Circuits,” IEEE 384-2018 (Reference 7.6.4-3) is used rather than the version of the standard endorsed by this RG." [PSAR_ch07 §7.6.4.2 p.282]
- "RG 1.97, Revision 5, Criteria for Accident Monitoring Instrumentation for Nuclear Power Plants" [PSAR_ch07 §7.6.4.2 p.283]
- "The XIS partially conforms to RG 1.97, Revision 5." [PSAR_ch07 §7.6.4.2 p.283]
- "The XIS is one of several systems which supports PAM functions and, alone, is not capable of fully conforming with all of the requirements of the RG." [PSAR_ch07 §7.6.4.2 p.283]
- "The extent of conformance to RG 1.97, Revision 5, will be provided at the operating license stage." [PSAR_ch07 §7.6.4.2 p.283]
- "RG 1.100, Revision 4, Seismic Qualification and Mechanical Equipment for Nuclear Power Plants The XIS fully conforms to RG 1.100, Revision 4." [PSAR_ch07 §7.6.4.2 p.283]
- "RG 1.118, Revision 3, Periodic Testing of Electric Power and Protection Systems" [PSAR_ch07 §7.6.4.2 p.283]
- "The XIS partially conform to RG 1.118, Revision 3." [PSAR_ch07 §7.6.4.2 p.283]
- "Conformance is partial because IEEE 338-2022, “IEEE Standard for Criteria for the Periodic Surveillance Testing of Nuclear Power Generating Station Safety Systems,” (Reference 7.6.4-4) is used rather than the version of the standard endorsed by this RG." [PSAR_ch07 §7.6.4.2 p.283]
- "RG 1.152, Revision 4, Criteria for Use of Computers in Safety Systems of Nuclear Power Plants" [PSAR_ch07 §7.6.4.2 p.283]
- "The XIS fully conforms to RG 1.152, Revision 4." [PSAR_ch07 §7.6.4.2 p.283]
- "RG 1.153, Revision 1, Criteria for Safety Systems" [PSAR_ch07 §7.6.4.2 p.283]
- "The XIS partially conforms to RG 1.153, Revision 1." [PSAR_ch07 §7.6.4.2 p.283]
- "Conformance is partial because IEEE 603-2018, “IEEE Standard Criteria for Safety Systems for Nuclear Power Generating Stations,” (Reference 7.6.4-5) is used for the application-specific elements rather than the version of the standard endorsed by this RG." [PSAR_ch07 §7.6.4.2 p.283]
- "RG 1.180, Revision 2, Guidelines for Evaluating Electromagnetic and Radio-Frequency Interference in Safety-Related Instrumentation and Control Systems" [PSAR_ch07 §7.6.4.2 p.283]
- "The XIS fully conforms to RG 1.180, Revision 2." [PSAR_ch07 §7.6.4.2 p.283]
- "PRA safety functions (PSFs) are determined through the plant-specific PRA described in Section 3.1." [PSAR_ch07 §7.6.4.2.1 p.283]
- "The safety-significant PSFs are identified as safety-related (SR) functions or NSRST functions as defined in Section 5.2." [PSAR_ch07 §7.6.4.2.1 p.283]
- "The XIS supports the following safety-significant functions, which are designated as SR (for DL3 functions) or NSRST (for the DL5 function) to indicate the safety classification of RPS components relied upon to perform the function:" [PSAR_ch07 §7.6.4.2.1 p.283]

| Function ID | Function Description | XIS Functional Support | 출처 |
|---|---|---|---|
| DL3-RC1a | Reactor scram on high-high neutron flux | XIS includes sensors that monitor neutron flux and send signals to the RPS. | [PSAR_ch07 §7.6.4.2.1 p.283] |
| DL3-RC1d | Reactor scram on high-high power-to-flow Ratio | XIS includes sensors that monitor neutron flux and send signals to the RPS. | [PSAR_ch07 §7.6.4.2.1 p.283] |
| DL3-RC1f | Reactor scram on high-high positive neutron flux rate | XIS includes sensors that monitor neutron flux and send signals to the RPS. | [PSAR_ch07 §7.6.4.2.1 p.283] |
| DL3-RC1g | Reactor scram on high-high negative neutron flux rate | XIS includes sensors that monitor neutron flux and send signals to the RPS. | [PSAR_ch07 §7.6.4.2.1 p.283] |
| DL3-RC1i | Reactor scram on low power, high neutron | XIS includes sensors that monitor neutron flux and send signals to the RPS. | [PSAR_ch07 §7.6.4.2.1 p.283] |
| DL3- HR2 | PSP trip on high-high primary sodium temperature | XIS includes sensors that monitor neutron flux and send signals to the RPS. | [PSAR_ch07 §7.6.4.2.1 p.283] |
| DL3-HR3 | Intermediate Sodium Pump (ISP) trip on high-high primary sodium temperature | XIS includes sensors that monitor neutron flux and send signals to the RPS. | [PSAR_ch07 §7.6.4.2.1 p.283] |
| DL3-HR12 | ISP trip on high-high primary sodium level | XIS includes sensors that monitor neutron flux and send signals to the RPS. | [PSAR_ch07 §7.6.4.2.1 p.283] |
| DL5-PAM1 | Post-accident monitoring | XIS includes sensors that monitor neutron flux and send signals to the RPS and NIC for display as Type B and D PAM variables. | [PSAR_ch07 §7.6.4.2.1 p.283] |

- "Safety-Related Design Criteria corresponding to the SR functions applicable to the XIS are derived as described in Section 6.1.2 and identified in Section 5.2." [PSAR_ch07 §7.6.4.2.1 p.283]
- "The Safety-Related Design Criteria are incorporated into the design of the RPS part of the I&C architecture as described in Section 7.6.4.1." [PSAR_ch07 §7.6.4.2.1 p.283]
- "The neutron flux measurement signals are replicated and isolated and are sent to the NI Coolant Temperature Monitoring and Control System and Rod Monitoring and Control System to support NST DL2 functions and the NST Audible Count Rate monitoring devices in the MCR and FHCR." [PSAR_ch07 §7.6.4.2.1 p.283]
- "Principal Design Criteria (PDC) are identified in Section 5.3." [PSAR_ch07 §7.6.4.2.2 p.283]
- "Compliance with PDC that are applicable to the XIS is described below." [PSAR_ch07 §7.6.4.2.2 p.283]
- "Consistent with PDC 2, Design Bases for Protection Against Natural Phenomenon System Bases, the XIS is designed so that in the event of adverse conditions due to natural phenomena, all XIS structures, systems, and components (SSCs) maintain the capability to perform their safety-significant functions." [PSAR_ch07 §7.6.4.2.2 p.283]
- "Earthquakes – Safety-significant portions of the XIS are located in the SR RXB and NCB substructures which are designed to withstand earthquakes." [PSAR_ch07 §7.6.4.2.2 p.283]
- "SR portions of the XIS are seismically qualified to remain operable in the SR RXB and NCB substructures during and after earthquakes." [PSAR_ch07 §7.6.4.2.2 p.283]
- "External Flooding – The XIS accounts for external flooding hazard by being located inside of the RXB and NCB, which is located above the maximum flood level." [PSAR_ch07 §7.6.4.2.2 p.285]
- "High Winds – To address the design basis extreme wind hazard (tornado and associated missiles), SR portions of XIS are located in the SR RXB and NCB substructures, which are designed for the extreme wind hazard." [PSAR_ch07 §7.6.4.2.2 p.285]
- "Extreme Climate – XIS equipment is located in the climate-controlled RXB and NCB to mitigate temperature, humidity, and winter precipitation hazards." [PSAR_ch07 §7.6.4.2.2 p.285]
- "Consistent with PDC 3, Fire protection, XIS equipment is located within the SR RXB and NCB substructure." [PSAR_ch07 §7.6.4.2.2 p.285]
- "The NCB walls and doors are 3-hour fire rated." [PSAR_ch07 §7.6.4.2.2 p.285]
- "XIS equipment in the NCB is located in a division-specific, 3-hour fire rated room, which minimized the likelihood of a fire affecting multiple XIS divisions at the same time." [PSAR_ch07 §7.6.4.2.2 p.285]
- "XIS equipment in the RXB is grouped by division and spaced apart to minimize the likelihood of a fire affecting multiple XIS divisions at the same time." [PSAR_ch07 §7.6.4.2.2 p.285]
- "Consistent with PDC 4, Environmental and dynamic effects design bases, the SR RXB and NCB substructures protect the XIS from external hazards caused by transportation incidents, incidents at offsite industrial and chemical facilities, and external missiles resulting from a turbine failure in the plant's turbine generator set." [PSAR_ch07 §7.6.4.2.2 p.285]
- "The SR NCB substructure provides a mild environment for the SR portions of the XIS located there." [PSAR_ch07 §7.6.4.2.2 p.285]
- "Safety-significant portions of the XIS located in the RXB substructure are qualified for harsh environments." [PSAR_ch07 §7.6.4.2.2 p.285]
- "Consistent with PDC 13, Instrumentation and Control, the XIS accepts input signals from instrumentation to monitor plant variables and interfaces with the RPS." [PSAR_ch07 §7.6.4.2.2 p.285]
- "All instrumentation and XIS signal conditioning associated with reactor scram, engineered safety feature (ESF), and PAM functions are designed to monitor associated variables within their anticipated ranges for normal operation, anticipated operational occurrences, and accident conditions as appropriate." [PSAR_ch07 §7.6.4.2.2 p.285]
- "Consistent with PDC 15, Primary Coolant System Design, the XIS supporting DL3 reactor scram and ESF functions are designed with appropriate margin to ensure that analytical limits established in the safety analysis are not exceeded as a result of anticipated operational occurrences which have not been mitigated by DL2 functions." [PSAR_ch07 §7.6.4.2.2 p.285]
- "Consistent with PDC 20, Protection System Functions, the XIS is designed to continuously monitor neutron flux and provide those signals to the RPS." [PSAR_ch07 §7.6.4.2.2 p.285]
- "The XIS is designed to support RPS, which performs these DL3 functions to ensure that analytical limits established in the safety analysis are not exceeded because of anticipated operational occurrences or design-basis events." [PSAR_ch07 §7.6.4.2.2 p.285]
- "Consistent with PDC 21, Protection System Reliability and Testability, the SR portions of the XIS are arranged into four redundant and independent divisions." [PSAR_ch07 §7.6.4.2.2 p.285]
- "XIS provides process variable input to the RPS by four redundant sensing instruments which are also divided into four redundant and independent divisions." [PSAR_ch07 §7.6.4.2.2 p.285]
- "This divisional arrangement of XIS and RPS and 2-out-of-4 voting design within RPS allows in-service testability of the XIS." [PSAR_ch07 §7.6.4.2.2 p.286]
- "The system design allows for any division to be taken out of service for testing at any time without loss of any safety function and without loss of minimum required redundancy.The divisional arrangement of XIS and RPS and 2-out-of-4 voting design features within RPS promote high system reliability." [PSAR_ch07 §7.6.4.2.2 p.286]
- "The XIS is designed to withstand a failure of any division without loss of any safety function and without loss of minimum required redundancy." [PSAR_ch07 §7.6.4.2.2 p.286]
- "The XIS is designed to withstand a single failure in any operating division, even when one division has been taken out of service for testing." [PSAR_ch07 §7.6.4.2.2 p.286]
- "The capability to periodically test divisions independently while in-service to determine failures and losses of redundancy that may have occurred further promotes high system reliability.RG 1.75 R3." [PSAR_ch07 §7.6.4.2.2 p.286]
- "Consistent with PDC 22, Protection System Independence, the SR portions of the XIS are arranged into four redundant and independent divisions." [PSAR_ch07 §7.6.4.2.2 p.286]
- "XIS provides process variable input to RPS to perform a safety function by four redundant sensing instruments which are also divided into four redundant and independent divisions." [PSAR_ch07 §7.6.4.2.2 p.286]
- "The RPS actuates reactor scram and ESF functions when at least 2 out of the 4 divisions independently determine that such action is required." [PSAR_ch07 §7.6.4.2.2 p.286]
- "Each of the four redundant XIS divisions are independent and physically separated from the other redundant XIS divisions to the degree necessary to ensure accomplishment of safety functions." [PSAR_ch07 §7.6.4.2.2 p.286]
- "All four redundant XIS divisions are independent and physically separated from the effects of design basis events which they are designed to mitigate." [PSAR_ch07 §7.6.4.2.2 p.286]
- "The XIS equipment is located to minimize potential damage from hazards and is qualified to substantiate design basis performance requirements." [PSAR_ch07 §7.6.4.2.2 p.286]
- "All four redundant XIS divisions are independent and physically separated or isolated from other systems, including interconnected systems and equipment in proximity, to the degree necessary to ensure accomplishment of safety functions." [PSAR_ch07 §7.6.4.2.2 p.286]
- "The divisional arrangement of XIS and RPS and 2-out-of-4 voting design features within RPS allow for any division to be out of service for maintenance or testing without any loss of safety function." [PSAR_ch07 §7.6.4.2.2 p.286]
- "The XIS is designed to assure that the effects of natural phenomena and of normal operating, maintenance, testing, and postulated accident conditions on redundant channels do not result in loss of any safety function." [PSAR_ch07 §7.6.4.2.2 p.286]
- "Consistent with PDC 23, Protection System Failure Modes, during normal operation (when neutron flux is within normal range, i.e., reactor scram is not required), the XIS maintains associated analog signals representing neutron flux." [PSAR_ch07 §7.6.4.2.2 p.286]
- "On loss of incoming power to XIS, the neutron flux signals to RPS are lost, thus RPS will place the associated circuit outputs in the safe state due to RPS employing range-checking on analog input signals from XIS." [PSAR_ch07 §7.6.4.2.2 p.286]
- "The SR XIS equipment is located in mild and harsh environments of the SR NCB and RXB substructures, respectively." [PSAR_ch07 §7.6.4.2.2 p.286]
- "The SR XIS equipment is environmentally and seismically qualified to remain operable during anticipated adverse conditions at these locations." [PSAR_ch07 §7.6.4.2.2 p.286]
- "The XIS electronics modules perform continuous self-diagnostics." [PSAR_ch07 §7.6.4.2.2 p.287]
- "If self-diagnostics detect a critical fault in the electronics that could affect performance of a safety function, the system places all outputs to the safe state." [PSAR_ch07 §7.6.4.2.2 p.287]
- "Consistent with PDC 24, Separation of Protection and Control Systems, the XIS is designed in accordance IEEE Std 603-2018 Clause 5.1 Single-Failure Criterion, Clause 5.6 Independence, and Clause 6.3 Interaction Between the Sense and Command Features and Other Systems." [PSAR_ch07 §7.6.4.2.2 p.287]
- "The XIS is designed with sufficient separation from control systems such that all reliability, redundancy, and independence requirements of the XIS remain intact, even when there is a single control system failure, or failure or removal from service of any component common to the XIS or any control system." [PSAR_ch07 §7.6.4.2.2 p.287]
- "Consistent with PDC 25, Protection System Requirements for Reactivity Control Malfunctions, the XIS is designed in accordance with IEEE Std 603-2018 Clause 5.1 Single-Failure Criterion, Clause 5.6 Independence, and Clause 6.3 Interaction Between the Sense and Command Features and Other Systems." [PSAR_ch07 §7.6.4.2.2 p.287]
- "The RPS DL3 reactor scram and ESF functions supported by XIS neutron flux signals are designed to ensure that analytical limits established in the safety analysis are not exceeded as a result of anticipated operational occurrences even when a single failure of the reactivity control system has occurred." [PSAR_ch07 §7.6.4.2.2 p.287]
- "Consistent with PDC 29, Protection Against Anticipated Operational Occurrences, the RPS DL3 reactor scram and ESF functions supported by XIS neutron flux signals are designed with appropriate margin to ensure that analytical limits established in the safety analysis are not exceeded as a result of anticipated operational occurrences which have not been mitigated by DL2 functions." [PSAR_ch07 §7.6.4.2.2 p.287]
- "The XIS performs both SR and NSRST functions and the special treatments are applied to all XIS SR SSCs and, as required by Clause 5.12 of IEEE 603-2018, these special treatments are also applied to all NSRST and NST SSCs." [PSAR_ch07 §7.6.4.3 p.287]
- "Special treatments are initially selected as described in Section 6.3." [PSAR_ch07 §7.6.4.3 p.287]
- "The following programmatic special treatments are preliminarily identified as applicable to the XIS to meet quality, design, reliability, and performance requirements:" [PSAR_ch07 §7.6.4.3 p.287]
- "Quality Assurance Program Description, as described in Section 8.1" [PSAR_ch07 §7.6.4.3 p.287]
- "Human Factors Engineering Program Plan, as described in Section 11.2" [PSAR_ch07 §7.6.4.3 p.287]
- "Equipment Qualification Program, as described in Table 8.0-1" [PSAR_ch07 §7.6.4.3 p.287]
- "Post-Construction Inspection, Testing, and Acceptance Program, as described in Chapter 12" [PSAR_ch07 §7.6.4.3 p.287]
- "Design Reliability Assurance Program, as described in Table 8.0-1" [PSAR_ch07 §7.6.4.3 p.287]
- "SSC specific special treatments are preliminarily identified as applicable to the XIS to meet quality, design, reliability, and performance requirements." [PSAR_ch07 §7.6.4.3 p.288]
- "Seismic classifications for XIS components are determined in accordance with the methods described in Section 6.4.1." [PSAR_ch07 §7.6.4.3 p.288]
- "Seismic special treatment is applied based on the seismic classification." [PSAR_ch07 §7.6.4.3 p.288]
- "The seismic classification of XIS components is SCS1." [PSAR_ch07 §7.6.4.3 p.288]
- "Seismic design, analysis, and qualification is performed as described in Section 6.4." [PSAR_ch07 §7.6.4.3 p.288]
- "XIS components are qualified to withstand seismic loads associated with the safe shutdown earthquake (described in Section 2.6.2) without loss of the capability to perform safety-significant functions." [PSAR_ch07 §7.6.4.3 p.288]
- "The following codes and standards are applied as special treatments to the XIS to meet quality, design, reliability, and performance requirements:" [PSAR_ch07 §7.6.4.3 p.288]

| 목록 항목 | 출처 |
|---|---|
| IEEE 338-2022 | [PSAR_ch07 §7.6.4.3 p.288] |
| IEEE 379-2014 | [PSAR_ch07 §7.6.4.3 p.288] |
| IEEE 384-2018 | [PSAR_ch07 §7.6.4.3 p.288] |

- "IEEE 420-2013, “IEEE Standard for the Design and Qualification of Class 1E Control Boards, Panels, and Racks Used in Nuclear Power Generating Stations,” (Reference 7.6.4-6)" [PSAR_ch07 §7.6.4.3 p.288]

| 목록 항목 | 출처 |
|---|---|
| IEEE 603-2018 | [PSAR_ch07 §7.6.4.3 p.288] |

- "IEEE 7-4.3.2-2016 (Reference 7.6.4-7)" [PSAR_ch07 §7.6.4.3 p.288]
- "The XIS design includes elements of quality that minimize the potential for failures to occur that could impact SR and NSRST functions." [PSAR_ch07 §7.6.4.3 p.288]
- "These properties of qualification, reliability, robustness, security, and defense-in-depth features are discussed in Section 7.6.4.3.1 through Section 7.6.4.3.5." [PSAR_ch07 §7.6.4.3 p.288]
- "The XIS meets the quality standards established in the Quality Assurance Program Description." [PSAR_ch07 §7.6.4.3.1 p.288]
- "The SR XIS equipment is located in mild and harsh environments of the SR NCB and RXB substructures, respectively." [PSAR_ch07 §7.6.4.3.1 p.288]
- "The SR XIS equipment is environmentally and seismically qualified to remain operable during anticipated adverse conditions at these locations." [PSAR_ch07 §7.6.4.3.1 p.288]
- "The Equipment Qualification Program described in Section 8.0 addresses the requirements, standards, and process for qualifying the XIS equipment." [PSAR_ch07 §7.6.4.3.1 p.288]
- "The XIS is designed for high functional reliability and in-service testability commensurate with the safety functions performed." [PSAR_ch07 §7.6.4.3.2 p.288]
- "The method for confirming specific reliability and capability targets for SSCs at the operating license stage is described in Section 6.2." [PSAR_ch07 §7.6.4.3.2 p.288]
- "The XIS is designed to permit periodic testing when the reactor is in operation, including a capability to test channels independently to determine failures and losses of redundancy that may have occurred." [PSAR_ch07 §7.6.4.3.2 p.289]
- "The XIS channels are included in the overall bypass schemes for placing SR channels into Maintenance Bypass to ensure that the correct functions are allocated to protection systems." [PSAR_ch07 §7.6.4.3.2 p.289]
- "The goals of the XIS reliability include minimizing out-of-service time for repair and reducing the frequency or automation of surveillance testing." [PSAR_ch07 §7.6.4.3.2 p.289]
- "To support this, the XIS meets the following:" [PSAR_ch07 §7.6.4.3.2 p.289]
- "The neutron flux channels are designed to accommodate periodic calibration and checks for associated protective and PAM functions as required by RG 1.118 and Clause 5.7 of IEEE 603-2018." [PSAR_ch07 §7.6.4.3.2 p.289]
- "XIS channels which support SR functions are designed to facilitate timely recognition, location, replacement, repair, and adjustment of malfunctioning equipment in accordance with Clause 5.10 of IEEE 603-2018." [PSAR_ch07 §7.6.4.3.2 p.289]
- "XIS channels which support Post-Accident Monitoring are designed to facilitate timely recognition, location, replacement, repair, and adjustment of malfunctioning equipment in accordance with Section 6.11 of IEEE 497-2016." [PSAR_ch07 §7.6.4.3.2 p.289]
- "The power range and wide range channels require periodic calorimetric adjustments." [PSAR_ch07 §7.6.4.3.2 p.289]
- "These adjustments align the XIS readouts to match power levels determined by accurate calorimetric calculations using core thermal power as measured by temperature and coolant flow rate measurements (within a separate system)." [PSAR_ch07 §7.6.4.3.2 p.289]
- "These adjustments are via individual range gain and offset adjustments locally at the XIS cabinets." [PSAR_ch07 §7.6.4.3.2 p.289]
- "Robustness of the XIS design is the degree to which it can perform its SR functions in the presence of invalid inputs or abnormal environmental conditions." [PSAR_ch07 §7.6.4.3.3 p.289]
- "The robust instrumentation and control design for XIS reflects the use of design methods and adherence to engineering best practices to ensure its functions are achieved for all operational states and accident conditions." [PSAR_ch07 §7.6.4.3.3 p.289]
- "The instrumentation and control design requirements address the full range of operating environments associated with normal operation, transient, and accident conditions, as well as internal and external hazards." [PSAR_ch07 §7.6.4.3.3 p.289]
- "The following elements address XIS system robustness:" [PSAR_ch07 §7.6.4.3.3 p.289]
- "Single Failure Criterion - The XIS meets single failure criterion by complying with RG 1.53 and IEEE 379-2014 as required by Clause 5.1 of IEEE 603-2018." [PSAR_ch07 §7.6.4.3.3 p.289]
- "Completion of Protective Action - The XIS supports the SR functions of RPS as required by Clause 5.2 of IEEE 603-2018." [PSAR_ch07 §7.6.4.3.3 p.289]
- "System Integrity - The XIS is designed to accomplish its safety functions under the full range of applicable worst case environmental conditions, including design basis accident conditions, at installed locations as required by Clause 5.5 of IEEE 603-2018." [PSAR_ch07 §7.6.4.3.3 p.289]
- "Independence - The XIS meets independence criteria between XIS channels and between the XIS SR and non-SR equipment by complying with RG 1.75 and IEEE 384-2018 as required by Clause 5.6 of IEEE 603-2018." [PSAR_ch07 §7.6.4.3.3 p.290]
- "Interaction between sense and command features and other systems - The XIS is powered from the NI Uninterruptible AC Power Supply System (NUP)." [PSAR_ch07 §7.6.4.3.3 p.290]
- "The NUP power feeds to XIS are organized into four NSRST divisions, corresponding to the four divisions of XIS." [PSAR_ch07 §7.6.4.3.3 p.290]
- "Each of the four divisions of NUP maintains independence and separation from the other NUP divisions, as well as between the NSRST NUP divisions and NST equipment." [PSAR_ch07 §7.6.4.3.3 p.290]
- "Additionally, appropriate isolation is provided at the interconnection of the SR XIS and other NSRST systems such that no credible failure on the NSRST side of the isolation can prevent any portion of the SR XIS from performing its safety functions." [PSAR_ch07 §7.6.4.3.3 p.290]
- "These isolation device(s) are classified as part of the SR XIS as required by Clause 6.3 of IEEE 603-2018." [PSAR_ch07 §7.6.4.3.3 p.290]
- "Maintenance Bypasses - The XIS provides maintenance bypass capabilities as required by Clause 6.7 of IEEE 603-2018." [PSAR_ch07 §7.6.4.3.3 p.290]
- "Redundancy - The XIS contain sufficient redundancy to meet single failure criterion by complying with RG 1.53 and IEEE 379-2014 as required by Clause 5.1 of IEEE 603-2018." [PSAR_ch07 §7.6.4.3.3 p.290]
- "Security for I&C systems is addressed through the physical security and cyber security programs that are described in Section 11.6." [PSAR_ch07 §7.6.4.3.4 p.290]
- "The XIS provides inputs to the DL2 control functions in the NI Coolant Temperature Monitoring and Control System and Rod Monitoring and Control System and the defense-in-depth DL3 RPS SR functions." [PSAR_ch07 §7.6.4.3.5 p.290]
- "The XIS is currently designed as an analog system that does not contain software to perform any SR functions." [PSAR_ch07 §7.6.4.3.5 p.290]
- "As such, there are no credible Common-Cause Failures or a potential to degrade or defeat the XIS safety functions as required by Clause 5.16 of IEEE 603-2018." [PSAR_ch07 §7.6.4.3.5 p.290]
- "In the event that procured components contain embedded digital devices, it is required that these devices conform with applicable industry standards and regulatory guidance." [PSAR_ch07 §7.6.4.3.5 p.290]
- "For embedded digital devices utilized to perform SR and NSRST functions, a Common-Cause Failure analysis is performed per the guidance in SECY-22-0076, “Expansion of Current Policy on Potential Common-Cause Failures in Digital Instrumentation and Control Systems,” and SRM-SECY-22-0076, “Staff Requirements – SECY-22-0076 – Expansion of Current Policy on Potential Common-Cause Failures in Digital Instrumentation and Control Systems.”" [PSAR_ch07 §7.6.4.3.5 p.290]
- "Manual control of the DL3 functions that rely on the XIS inputs is provided within the RPS as required by Clause 6.2 of IEEE 603-2018." [PSAR_ch07 §7.6.4.3.5 p.290]
- "The XIS operational aspects are displayed via the RPS and NIC." [PSAR_ch07 §7.6.4.4 p.290]
- "The NIC subsystem, Plant Monitoring and Control System, has access to XIS inputs, such as XIS flux measurements." [PSAR_ch07 §7.6.4.4 p.290]
- "XIS PAM information is transmitted to the RPS." [PSAR_ch07 §7.6.4.4 p.290]
- "This ensures XIS status and information is displayed as required by Clause 5.8 of IEEE 603-2018." [PSAR_ch07 §7.6.4.4 p.290]
- "NST audible count rate devices in the MCR and FHCR provide operators with source range indication via an audible signal which corresponds to count rate." [PSAR_ch07 §7.6.4.4 p.290]
- "The XIS operator interfaces consider the guidance of NUREG-0700, “Human-System Interface Design Review Guidelines,” (Reference 7.6.4-8) and NUREG-0711, “Human Factors Engineering Program Review Model,” (Reference 7.6.4-9) as required by Clause 5.14 of IEEE 603-2018." [PSAR_ch07 §7.6.4.4 p.291]
- "XIS operator interfaces are addressed as part of the Human Factors Engineering Program Plan that is described in Section 11.2." [PSAR_ch07 §7.6.4.4 p.291]
- "Nuclear Instrumentation System | SR | DL2, DL3, DL5" [PSAR_ch07 Table 7.6.1-1 p.250]

- "Figure 7.6.4-1 XIS Overview" [PSAR_ch07 Figure 7.6.4-1 p.292]

![[PSAR_ch07_Fig_7.6.4-1.png]]

## 해설
아날로그 Nuclear Instrumentation System(`XIS`)은 핵연료 이동, 원자로 기동, 출력 운전, 정지, 사고 조건에서 노심에서 누설되는 neutron flux를 감지하며, 신호가 안전해석이 가정한 시간 안에 `RPS`로 가도록 설계된다. wide range neutron flux 신호는 `IEEE 497-2016`의 Type B·D `PAM` 변수로 `RPS`와 `NIC`에 보내진다. `XIS`는 division별 flux 검출기와 신호 조정을 갖춘 네 이중화 division으로 이루어지고, 각 division은 대응하는 `RPS` division하고만 연결되어 division 분리를 유지한다. 검출기는 division마다 High Temperature Fission Chamber 한 개(총 `four`)이고 검출기와 전자 장치는 power range, wide range, source range 세 신호 범위를 내며, source range 신호에는 audible count rate 변수가 있다. `NIC`에는 Non-Safety-Related with No Special Treatment%%t:NST%% 제어 기능을 위한 신호를 주며, 실시간 제어에 쓰는 `Rod Monitoring and Control System`과 `NI Coolant Temperature Monitoring and Control System`은 격리된 hardwired 신호를 받는다.

`XIS`는 SR%%t:SR%%, Non-Safety-Related with Special Treatment%%t:NSRST%%, NST%%t:NST%% 기능을 지원하는 SR%%t:SR%% 계통이며, SR%%t:SR%% 측정에 쓰는 장비가 NSRST%%t:NSRST%%·NST%%t:NST%% 기능도 지원한다. regulatory guide%%t:RG%% 부합은 `RG 1.47`, `RG 1.100`, `RG 1.152`, `RG 1.180` 완전 부합이고 `RG 1.53`, `RG 1.118`, `RG 1.153`은 더 새로운 `IEEE` 표준 사용으로 부분 부합이다. `RG 1.75` 부분 부합 문장은 주어가 `Application-specific elements of the RPS`로 적혀 있다. `RG 1.97, Revision 5`는 여러 계통 가운데 하나라 부분 부합이고 범위는 operating license%%t:OL%% 단계에서 제공된다.

기능 표는 `DL3` 기능을 SR%%t:SR%%, `DL5` 기능을 NSRST%%t:NSRST%%로 지정한다고 적으나 분류 대상은 `RPS components`로 적혀 있다. `XIS`는 `DL3-RC1a`, `DL3-RC1d`, `DL3-RC1f`, `DL3-RC1g`, `DL3-RC1i`, `DL3-HR2`, `DL3-HR3`, `DL3-HR12`에 neutron flux 신호를 주고, `DL5-PAM1`에는 `RPS`와 `NIC`에 Type B·D 변수를 준다. 복제·격리된 신호는 NST%%t:NST%% `DL2` 기능과 `MCR`·`FHCR`의 NST%%t:NST%% Audible Count Rate 장치로 간다. `Table 7.6.1-1`은 `XIS`의 연관 Defense Line%%t:DL%%을 `DL2`, `DL3`, `DL5`로 적는다.

principal design criteria%%t:PDC%% 2와 4에 따라 safety-significant 부분은 SR%%t:SR%% `RXB`와 `NCB` 하부구조에 있고, `NCB` 쪽은 mild environment, `RXB` 하부구조 쪽은 harsh environment에 대해 검증된다. PDC%%t:PDC%% 3에 따라 `NCB`의 `XIS` 장비는 division별 3-hour 내화 등급 실에, `RXB`의 장비는 division별로 묶어 떨어뜨려 배치된다. PDC%%t:PDC%% 21과 22에 따라 네 division과 `RPS` 안의 2-out-of-4 voting이 운전 중 시험, 한 division 제외, 단일 고장 내성을 가능하게 한다. PDC%%t:PDC%% 23에 따라 `XIS` 전원이 상실되면 flux 신호가 사라지고 `RPS`가 range-checking으로 해당 출력을 안전 상태로 둔다. 전자 모듈은 계속 자기진단하며 치명 결함 시 출력을 안전 상태로 둔다. PDC%%t:PDC%% 24와 25는 `IEEE 603-2018` Clause 5.1, 5.6, 6.3에 따른 설계로 다룬다.

`IEEE 603-2018` Clause 5.12에 따라 SR%%t:SR%% Structures, Systems, and Components%%t:SSC%%의 special treatment는 NSRST%%t:NSRST%%·NST%%t:NST%% SSC%%t:SSC%%에도 적용된다. programmatic special treatment는 Quality Assurance Program Description, Human Factors Engineering Program Plan, Equipment Qualification Program, Post-Construction Inspection, Testing, and Acceptance Program, Design Reliability Assurance Program으로 예비 식별되고, 규격 special treatment는 `IEEE 338-2022`, `IEEE 379-2014`, `IEEE 384-2018`, `IEEE 420-2013`, `IEEE 603-2018`, `IEEE 7-4.3.2-2016`이다. 구성품 지진 분류는 `SCS1`이며 Safe Shutdown Earthquake%%t:SSE%% 하중에서 기능을 잃지 않도록 검증된다. power range와 wide range channel은 주기적 calorimetric 조정이 필요하고, 조정은 `XIS` 캐비닛에서 range별 gain과 offset으로 한다. `XIS`는 `NI Uninterruptible AC Power Supply System`(`NUP`)의 네 NSRST%%t:NSRST%% division에서 전원을 받고, SR%%t:SR%% `XIS`와 NSRST%%t:NSRST%% 계통 사이 격리 장치는 SR%%t:SR%% `XIS`의 일부로 분류된다.

`XIS`는 현재 SR%%t:SR%% 기능을 수행하는 소프트웨어가 없는 아날로그 계통으로 설계되어, 원문은 `IEEE 603-2018` Clause 5.16이 요구하는 신뢰할 만한 CCF%%t:CCF%%나 안전 기능 저하 가능성이 없다고 적는다. 조달 구성품에 embedded digital device가 있으면 산업 표준과 규제 지침을 따라야 하고, SR%%t:SR%%·NSRST%%t:NSRST%% 기능에 쓰이면 `SECY-22-0076`과 `SRM-SECY-22-0076` 지침으로 CCF%%t:CCF%% 분석을 한다. `XIS` 입력에 의존하는 `DL3` 기능의 수동 제어는 `RPS` 안에 있다. 운전 정보는 `RPS`와 `NIC`로 표시되고, `MCR`과 `FHCR`의 NST%%t:NST%% audible count rate 장치가 source range를 소리로 알린다.

## 관련 문서
- [[Natrium_System_IC_Architecture]]
- [[Natrium_System_Reactor_Protection]]
- [[Natrium_System_NI_Control]]
- [[Natrium_SR_Functions_Heat_Generation]]
- [[Natrium_IC_Systems]]
- [[Natrium_System_NI_Auxiliary_Electrical]]
- [[PSAR_ch07]]
