---
type: natrium
aliases: []
sources:
- PSAR_ch07
- PSAR_ch01
status: checked
verified: 2026-09-16
term: null
tags:
- natrium
- psar-ch7
terms_pending: []
---

# Natrium Reactor Instrumentation System (RIS)

> [!abstract] 요약
> Reactor Instrumentation System(`RIS`)은 원자로 용기 안이나 근처의 변수를 측정해 `RPS`와 `NIC`에 신호를 보내는 계기 channel의 모음이며, Safety-Related%%t:SR%% 입력은 네 division으로 나뉜다. `DL3` scram·trip 기능, `NIC`로 가는 `DL4-HR2`·`DL4-HR3`, `DL4-RR8`, `DL5-PAM1`을 지원하고, 정보 표시·자동 제어·명령 기능은 갖지 않는다.

## 원문 사실
- "The Reactor Instrumentation System (RIS) contains instrumentation to measure selected parameters in or near the reactor vessel and transmit corresponding signals to the Reactor Protection System (RPS) and the Nuclear Island Control System (NIC) for use in protective, control, accident monitoring, and surveillance functions." [PSAR_ch07 §7.6.5.1 p.293]
- "The RIS is designed to ensure that SR parameters are measured and transmitted to the RPS within the time assumed in the safety analysis." [PSAR_ch07 §7.6.5.1 p.293]
- "The RIS is a collection of individual RIS instrument channels, where a channel is defined as a single sensor and its associated cabling and signal amplification electronics." [PSAR_ch07 §7.6.5.1 p.293]
- "An individual RIS instrument channel may support one or multiple functions which are classified as safety-related (SR), non-safety-related with special treatment (NSRST), or non-safety-related with no special treatment (NST)." [PSAR_ch07 §7.6.5.1 p.293]
- "The RIS also includes cables which run from the sensors in or near the reactor vessel to the signal conditioning electronics cabinets, and from the signal conditioning electronics cabinets to the RPS and NIC terminal blocks." [PSAR_ch07 §7.6.5.1 p.293]
- "The NIC is described in Section 7.6.2 and the RPS in Section 7.6.3." [PSAR_ch07 §7.6.5.1 p.293]
- "The RIS has four redundant and independent divisions for parameters that provide SR inputs to the RPS via SR cabling." [PSAR_ch07 §7.6.5.1.1 p.293]
- "Signal splitters are used to duplicate the SR inputs and provide them to the NIC as NSRST and NST signals." [PSAR_ch07 §7.6.5.1.1 p.293]
- "A block diagram of the RIS is shown in Figure 7.6.5-1." [PSAR_ch07 §7.6.5.1.1 p.293]
- "A summary of variables monitored by the RIS, the number of instruments that monitor each variable, and the safety classification of the components is shown in Table 7.6.5-1." [PSAR_ch07 §7.6.5.1.1 p.293]
- "The RIS measurement sensors are located in or near the reactor vessel in the Reactor Building (RXB)." [PSAR_ch07 §7.6.5.1.2 p.293]
- "Safety-significant portions of the RIS are located in the RXB and Nuclear Island Control Building (NCB) substructures." [PSAR_ch07 §7.6.5.1.2 p.293]
- "The RXB is described in Section 7.8.1." [PSAR_ch07 §7.6.5.1.2 p.293]
- "The NCB substructure is described in Section 7.8.4." [PSAR_ch07 §7.6.5.1.2 p.293]
- "The RIS is designed to perform assigned SR, NSRST, and NST functions and to assist in satisfying Principal Design Criteria (PDC)." [PSAR_ch07 §7.6.5.2 p.293]
- "A description of the process for assigning Defense Line (DL) functions to the RIS is provided in Section 7.6.1.1.1." [PSAR_ch07 §7.6.5.2 p.293]
- "A description of the process for describing the safety classification of the RIS is provided in Section 7.6.1.1.2." [PSAR_ch07 §7.6.5.2 p.293]
- "Special treatments are applied to safety-significant equipment in the RIS to meet quality, design, reliability, and performance requirements." [PSAR_ch07 §7.6.5.2 p.293]
- "Special treatments are initially selected based on structure, system, or component (SSC) safety classification as described in Section 6.3." [PSAR_ch07 §7.6.5.2 p.293]
- "The following programmatic special treatments are identified as applicable to the RIS:" [PSAR_ch07 §7.6.5.2 p.293]
- "Design Reliability Assurance Program (Table 8.0-1)" [PSAR_ch07 §7.6.5.2 p.293]
- "Equipment Qualification Program (Table 8.0-1)" [PSAR_ch07 §7.6.5.2 p.293]
- "Post-construction inspection, testing, and analysis program (Chapter 12)" [PSAR_ch07 §7.6.5.2 p.293]
- "Quality Assurance Program Description (Section 8.1)" [PSAR_ch07 §7.6.5.2 p.294]
- "Human Factors Engineering Program Plan (Section 11.2)" [PSAR_ch07 §7.6.5.2 p.294]
- "The RIS conforms to RGs as follows:" [PSAR_ch07 §7.6.5.2 p.294]
- "RG 1.22, Revision 0, Periodic Testing of Protection System Actuation Functions" [PSAR_ch07 §7.6.5.2 p.294]
- "The RIS fully conforms to RG 1.22, Revision 0." [PSAR_ch07 §7.6.5.2 p.294]
- "RG 1.53, Revision 2, Application of the Single-Failure Criterion to Safety Systems" [PSAR_ch07 §7.6.5.2 p.294]
- "The RIS partially conforms to RG 1.53, Revision 2." [PSAR_ch07 §7.6.5.2 p.294]
- "Conformance is partial because IEEE 379-2014, “IEEE Standard for Application of the Single-Failure Criterion to Nuclear Power Generating Station Safety Systems,” (Reference 7.6.5-1) is used rather than the version of the standard endorsed by this RG." [PSAR_ch07 §7.6.5.2 p.294]
- "RG 1.75, Revision 3, Physical Independence of Electric Systems" [PSAR_ch07 §7.6.5.2 p.294]
- "The RIS partially conforms to RG 1.75, Revision 3." [PSAR_ch07 §7.6.5.2 p.294]
- "Conformance is partial because IEEE 384-2018, “IEEE Standard Criteria for Independence of Class 1E Equipment and Circuits,” (Reference 7.6.5-2) is used rather than the version of the standard endorsed by this RG." [PSAR_ch07 §7.6.5.2 p.294]
- "RG 1.97, Revision 5, Criteria for Accident Monitoring Instrumentation for Nuclear Power Plants" [PSAR_ch07 §7.6.5.2 p.294]
- "The RIS partially conforms to RG 1.97, Revision 5." [PSAR_ch07 §7.6.5.2 p.294]
- "The RIS is one of several systems which supports PAM functions and, alone, is not capable of fully conforming with all of the requirements of the RG." [PSAR_ch07 §7.6.5.2 p.294]
- "The extent of conformance to RG 1.97, Revision 5, will be provided at the OL stage." [PSAR_ch07 §7.6.5.2 p.294]
- "RG 1.100, Revision 4, Seismic Qualification of Electric and Mechanical Equipment for Nuclear Power Plants" [PSAR_ch07 §7.6.5.2 p.294]
- "The RIS fully conforms to RG 1.100, Revision 4." [PSAR_ch07 §7.6.5.2 p.294]
- "RG 1.118, Revision 3, Periodic Testing of Electric Power and Protection Systems" [PSAR_ch07 §7.6.5.2 p.294]
- "The RIS partially conforms to RG 1.118, Revision 3." [PSAR_ch07 §7.6.5.2 p.294]
- "Conformance is partial because IEEE 338-2022, “IEEE Standard for Criteria for the Periodic Surveillance Testing of Nuclear Power Generating Station Safety Systems,” (Reference 7.6.5-3) is used rather than the version of the standard endorsed by this RG." [PSAR_ch07 §7.6.5.2 p.294]
- "RG 1.153, Revision 1, Criteria for Safety Systems" [PSAR_ch07 §7.6.5.2 p.294]
- "The RIS partially conforms to RG 1.153, Revision 1." [PSAR_ch07 §7.6.5.2 p.294]
- "Conformance is partial because IEEE 603-2018, “IEEE Standard Criteria for Safety Systems for Nuclear Power Generating Stations,” (Reference 7.6.5-4) is used rather than the version of the standard endorsed by this RG." [PSAR_ch07 §7.6.5.2 p.294]
- "RG 1.180, Revision 2, Guidelines for Evaluating Electromagnetic and Radio-Frequency Interference in Safety-Related Instrumentation and Control Systems" [PSAR_ch07 §7.6.5.2 p.294]
- "The RIS fully conforms to RG 1.180, Revision 2." [PSAR_ch07 §7.6.5.2 p.295]
- "PRA safety functions (PSFs) are determined through the plant-specific PRA described in Section 3.1." [PSAR_ch07 §7.6.5.2.1 p.295]
- "The safety-significant PSFs are identified as SR functions or NSRST functions as defined in Section 5.2." [PSAR_ch07 §7.6.5.2.1 p.295]
- "The RIS supports the following safety-significant functions, which are designated as SR (for DL3 functions) or NSRST (for DL 4 and DL 5 functions) to indicate the safety classification of RIS components relied upon to perform the function:" [PSAR_ch07 §7.6.5.2.1 p.295]

| Function ID | Function Description | RIS Functional Support | 출처 |
|---|---|---|---|
| DL3-RC1b | Reactor scram on high-high hot pool temperature | RIS includes sensors that monitor primary sodium hot pool temperature and send signals from the sensors to the RPS. | [PSAR_ch07 §7.6.5.2.1 p.295] |
| DL3-RC1c | Reactor scram on high-high primary sodium level | RIS includes sensors that monitor primary sodium hot pool level and send signals from the sensors to the RPS. | [PSAR_ch07 §7.6.5.2.1 p.295] |
| DL3-RC1d | Reactor scram on high-high power-to-flow ratio | RIS includes sensors that monitor primary sodium pump (PSP) speed and PSP current and send signals from the sensors to the RPS. | [PSAR_ch07 §7.6.5.2.1 p.295] |
| DL3-RC1e | Reactor scram on high-high cold pool temperature | RIS includes sensors that monitor primary sodium cold pool temperature and send signals from the sensors to the RPS. | [PSAR_ch07 §7.6.5.2.1 p.295] |
| DL3-RC1h | Reactor scram on low-low primary sodium level | RIS includes sensors that monitor primary sodium hot pool level and send signals from the sensors to the RPS. | [PSAR_ch07 §7.6.5.2.1 p.295] |
| DL3-RC1j | Reactor scram on loss of primary sodium flow | RIS includes sensors that monitor PSP speed and PSP current and send signals from the sensors to the RPS. | [PSAR_ch07 §7.6.5.2.1 p.295] |
| DL3-HR2 | PSP trip on high-high primary sodium temperature | RIS includes sensors that monitor primary sodium cold pool temperature and send signals to the RPS. | [PSAR_ch07 §7.6.5.2.1 p.295] |
| DL3-HR3 | Intermediate sodium pump (ISP) trip on high-high primary sodium temperature | RIS includes sensors that monitor primary sodium cold pool temperature and send signals to the RPS. | [PSAR_ch07 §7.6.5.2.1 p.295] |
| DL3-HR11 | Sodium processing system (SPS) pump trip on low primary sodium level | RIS includes sensors that monitor primary sodium hot pool level and send signals to the RPS. | [PSAR_ch07 §7.6.5.2.1 p.295] |
| DL3-HR12 | ISP trip on high-high primary sodium level | RIS includes sensors that monitor primary sodium hot pool level and send signals to the RPS. | [PSAR_ch07 §7.6.5.2.1 p.295] |
| DL4-HR2 | PSP trip automatic backup | RIS includes sensors that monitor primary sodium hot pool temperature and send signals to the NIC. | [PSAR_ch07 §7.6.5.2.1 p.295] |
| DL4-HR3 | ISP trip automatic backup | RIS includes sensors that monitor primary sodium hot pool temperature and send signals to the NIC. | [PSAR_ch07 §7.6.5.2.1 p.295] |
| DL4-RR8 | Manual SPS pump trip on low primary sodium level | RIS includes sensors that monitor primary sodium hot pool level and send signals to the RPS. | [PSAR_ch07 §7.6.5.2.1 p.295] |
| DL5-PAM1 | Post-accident monitoring | RIS includes sensors that monitor Type B, C, and F PAM variables and send signals to the RPS. | [PSAR_ch07 §7.6.5.2.1 p.295] |

- "Safety-Related Design Criteria corresponding to the SR functions applicable to the RIS are derived as described in Section 6.1.2 and identified in Section 5.2." [PSAR_ch07 §7.6.5.2.1 p.295]
- "The Safety-Related Design Criteria are incorporated into the design of the RIS as described in Section 7.6.5.1." [PSAR_ch07 §7.6.5.2.1 p.295]
- "The RIS provides signals to control Primary Heat Transport System flow, PSP flow, initiate power runback, and inhibit rod withdrawal in support of NST DL2 functions." [PSAR_ch07 §7.6.5.2.1 p.295]
- "The Primary Heat Transport System and PSP are described in Section 7.1.3." [PSAR_ch07 §7.6.5.2.1 p.295]
- "The Intermediate Heat Transport System and Intermediate Sodium Pump are described in Section 7.1.4." [PSAR_ch07 §7.6.5.2.1 p.295]
- "Sodium Cover Gas system is described in Section 7.2.3." [PSAR_ch07 §7.6.5.2.1 p.295]
- "Sodium Processing System is described in Section 7.2.4." [PSAR_ch07 §7.6.5.2.1 p.295]
- "PDC are identified in Section 5.3." [PSAR_ch07 §7.6.5.2.2 p.295]
- "The RIS conforms to PDC as described below." [PSAR_ch07 §7.6.5.2.2 p.295]
- "Consistent with PDC 2, Design bases for protection against natural phenomena, in the event of adverse conditions due to natural phenomena, all RIS safety-significant SSCs maintain the capability to perform their safety functions." [PSAR_ch07 §7.6.5.2.2 p.295]
- "Earthquakes- Safety-significant portions of the RIS are located in the RXB and NCB substructures, which are designed to withstand earthquakes." [PSAR_ch07 §7.6.5.2.2 p.295]
- "Safety-significant portions of the RIS are seismically qualified to remain operable in the RXB and NCB substructures during and after earthquakes." [PSAR_ch07 §7.6.5.2.2 p.295]
- "External flooding- The RIS accounts for external flooding hazard by being located inside of the RXB and NCB, which is above the maximum flood level." [PSAR_ch07 §7.6.5.2.2 p.295]
- "High winds- To address the design basis extreme wind hazard, safety-significant portions of the RIS are located in the SR RXB and NCB substructures, which are designed for the extreme wind hazard." [PSAR_ch07 §7.6.5.2.2 p.295]
- "Extreme climate- The RIS equipment is located in the climate-controlled RXB and NCB to mitigate temperature, humidity, and winter precipitation hazards." [PSAR_ch07 §7.6.5.2.2 p.295]
- "Consistent with PDC 3, Fire protection, RIS equipment is located within the SR RXB and NCB substructures." [PSAR_ch07 §7.6.5.2.2 p.295]
- "The NCB walls and doors are 3-hour fire rated." [PSAR_ch07 §7.6.5.2.2 p.295]
- "RIS equipment in the NCB is located in a division-specific, 3-hour fire rated room, which minimizes the likelihood of a fire affecting multiple RIS divisions at the same time." [PSAR_ch07 §7.6.5.2.2 p.295]
- "RIS equipment in the RXB is grouped by division and spaced apart to minimize the likelihood of a fire affecting multiple RIS divisions at the same time." [PSAR_ch07 §7.6.5.2.2 p.295]
- "Consistent with PDC 4, Environmental and dynamic effects design bases, the SR RXB and NCB substructures protect the RIS from external hazards caused by transportation incidents, incidents at offsite industrial and chemical facilities, and external missiles resulting from a turbine failure in the plant’s turbine generator set." [PSAR_ch07 §7.6.5.2.2 p.297]
- "The SR NCB substructure provides a mild environment for the SR portions of the RIS located there." [PSAR_ch07 §7.6.5.2.2 p.297]
- "SR portions of the RIS located in the RXB substructure are qualified for harsh environments." [PSAR_ch07 §7.6.5.2.2 p.297]
- "Consistent with PDC 13, Instrumentation and control, the RIS provides instrumentation to monitor variables in or near the reactor vessel and transmit corresponding signals to RPS and NIC for use in protective, control, accident monitoring, and surveillance functions during normal operations, anticipated operational occurrences, and postulated accidents to maintain variables and systems within prescribed operating ranges." [PSAR_ch07 §7.6.5.2.2 p.297]
- "Consistent with PDC 15, Primary coolant system design, the parameters monitored by the RIS, and input to the RPS and NIC, are selected to support the design for sufficient margin to ensure that the design conditions of the safety-significant elements of the primary coolant boundary are not exceeded during any condition of normal operation, including anticipated operational occurrences." [PSAR_ch07 §7.6.5.2.2 p.297]
- "Consistent with PDC 20, Protection system functions, the RIS continuously monitors parameters necessary to sense accident conditions and provides signals to the RPS for the performance of protection functions." [PSAR_ch07 §7.6.5.2.2 p.297]
- "Consistent with PDC 21, Protection system reliability and testability, the RIS is designed with redundant divisions for high functional reliability and inservice testability." [PSAR_ch07 §7.6.5.2.2 p.297]
- "The use of four independent divisions ensures a single failure does not result in a loss of the protection functions and ensures that removal from service of any component or division does not result in the loss of the required minimum redundancy." [PSAR_ch07 §7.6.5.2.2 p.297]
- "Consistent with PDC 22, Protection system independence, the RIS is designed to assure that the effects of natural phenomena and the effects of normal operating, maintenance, testing, and postulated accident conditions on redundant divisions do not result in the loss of a safety function." [PSAR_ch07 §7.6.5.2.2 p.297]
- "The SR portions of the RIS are arranged into four redundant and independent divisions." [PSAR_ch07 §7.6.5.2.2 p.297]
- "RIS provides process variable input to RPS with four redundant sensing instruments (or groups of instruments) which are divided into four redundant and independent divisions." [PSAR_ch07 §7.6.5.2.2 p.297]
- "Each of the four redundant RIS divisions are independent and physically separated from the other RIS divisions to the degree necessary to ensure accomplishment of safety functions and allow maintenance and testing." [PSAR_ch07 §7.6.5.2.2 p.297]
- "The RIS equipment is located to minimize potential damage from hazards and is qualified to substantiate design basis performance requirements." [PSAR_ch07 §7.6.5.2.2 p.297]
- "The divisional arrangement of RIS and RPS and the 2-out-of-4 voting design features within RPS allow for any division to be out of service for maintenance or testing without loss of a safety function." [PSAR_ch07 §7.6.5.2.2 p.297]
- "Consistent with PDC 24, Separation of protection and control systems, the RIS inputs to the NIC are electronically isolated and independent of the inputs to the RPS, which ensures that control system failures or removal of control system components will not impact RPS functionality." [PSAR_ch07 §7.6.5.2.2 p.298]
- "The RIS has redundant divisions, which ensure that removal of any RIS division will not impact the protection or control functions." [PSAR_ch07 §7.6.5.2.2 p.298]
- "Consistent with PDC 29, Protection against anticipated operational occurrences, the design of protection and reactivity control systems assure an extremely high probability of accomplishing their safety functions in the event of anticipated operational occurrences." [PSAR_ch07 §7.6.5.2.2 p.298]
- "The RIS supports the RPS and NIC in satisfying this PDC by providing highly reliable inputs through qualification and multiple divisions." [PSAR_ch07 §7.6.5.2.2 p.298]
- "The RIS design includes elements of quality that minimize the potential for failures to occur in SSCs associated with SR functions." [PSAR_ch07 §7.6.5.3 p.298]
- "These properties of qualification, reliability, robustness, security, diversity, and defense-in-depth features are discussed in Section 7.6.5.3.1 through Section 7.6.5.3.4." [PSAR_ch07 §7.6.5.3 p.298]
- "The following industry codes and standards are applied as special treatments to the overall design of safety-significant equipment in the RIS:" [PSAR_ch07 §7.6.5.3 p.298]

| 목록 항목 | 출처 |
|---|---|
| IEEE 603-2018 | [PSAR_ch07 §7.6.5.3 p.298] |
| IEEE 379-2014 | [PSAR_ch07 §7.6.5.3 p.298] |
| IEEE 384-2018 | [PSAR_ch07 §7.6.5.3 p.298] |

- "The following industry codes and standards and RG are applied as special treatments to RIS for environmental, seismic, and electromagnetic compatibility qualification:" [PSAR_ch07 §7.6.5.3.1 p.298]
- "IEEE/IEC 60780-323-2016 “International Standard - Nuclear facilities - Electrical equipment important to safety - Qualification” (Reference 7.6.5-5)" [PSAR_ch07 §7.6.5.3.1 p.298]
- "IEEE/IEC 60980-344-2020, “International Standard-Nuclear Facilities-Equipment important to safety-Seismic qualification,” (Reference 7.6.5-6)" [PSAR_ch07 §7.6.5.3.1 p.298]
- "IEEE 420-2013 “IEEE Standard for the Design and Qualification of Class 1E Control Boards, Panels, and Racks Used in Nuclear Power Generating Stations” (Reference 7.6.5-7)" [PSAR_ch07 §7.6.5.3.1 p.298]
- "RG 1.180, Revision 2, “Guidelines for Evaluating Electromagnetic and Radio-Frequency Interference in Safety-Related Instrumentation and Control Systems”" [PSAR_ch07 §7.6.5.3.1 p.298]
- "The safety-significant equipment in the RIS is assigned seismic special treatment commensurate with a seismic classification of SCS1." [PSAR_ch07 §7.6.5.3.1 p.298]
- "Seismic classification is described in Section 6.4.1." [PSAR_ch07 §7.6.5.3.1 p.298]
- "The method for confirming specific reliability and capability targets for SSCs at the operating license (OL) stage is described in Section 6.2." [PSAR_ch07 §7.6.5.3.2 p.298]
- "SR equipment in the RIS is designed to facilitate timely recognition, location, adjustment, repair, and replacement of malfunctioning equipment." [PSAR_ch07 §7.6.5.3.2 p.299]
- "SR equipment in the RIS is distinctly identified for each redundant portion of the system, in accordance with the requirements of IEEE 384-2018 and IEEE 420-2013." [PSAR_ch07 §7.6.5.3.2 p.299]
- "Some equipment in the RIS provides signals to the RPS and NIC that support Post-Accident Monitoring functionality." [PSAR_ch07 §7.6.5.3.2 p.299]
- "The design of Post-Accident Monitoring capabilities is informed by IEEE 497-2016 “IEEE Standard Criteria for Accident Monitoring Instrumentation for Nuclear Power Generating Stations” (Reference 7.6.5-8)." [PSAR_ch07 §7.6.5.3.2 p.299]
- "A description of the conformance to IEEE 497-2016, as endorsed by Regulatory Guide 1.97, Revision 5, will be provided at the OL stage." [PSAR_ch07 §7.6.5.3.2 p.299]
- "RIS equipment is designed in accordance with IEEE 420-2013, including requirements regarding human factors." [PSAR_ch07 §7.6.5.3.2 p.299]
- "The display of information provided from the RIS to the RPS and NIC is reviewed per the Human Factors Engineering Program Plan described in Section 11.2." [PSAR_ch07 §7.6.5.3.2 p.299]
- "IEEE 338-2022 is applied as a special treatment to the safety-significant equipment in the RIS to ensure that reliability and capability targets are met." [PSAR_ch07 §7.6.5.3.2 p.299]
- "SR portions of the RIS are capable of testing and calibration during power operation without loss of SR functions at the system level." [PSAR_ch07 §7.6.5.3.2 p.299]
- "The design of RIS supports checking each channel (including sensor and any electronics) required for a safety function by one of the following means:" [PSAR_ch07 §7.6.5.3.2 p.299]
- "cross-checking between redundant channels with available readouts" [PSAR_ch07 §7.6.5.3.2 p.299]
- "introducing and varying substitute input" [PSAR_ch07 §7.6.5.3.2 p.299]
- "perturbing the monitored variable" [PSAR_ch07 §7.6.5.3.2 p.299]
- "Instrument channels supporting Post-Accident Monitoring have testing capability to facilitate timely recognition, location, adjustment, and repair of malfunctioning equipment." [PSAR_ch07 §7.6.5.3.2 p.299]
- "SR portions of the RIS are designed such that when one division (or a portion of one division) is bypassed for maintenance, there is no loss of safety function at the system level." [PSAR_ch07 §7.6.5.3.2 p.299]
- "A description of the implementation of maintenance bypass capabilities for the RIS will be provided at the OL stage." [PSAR_ch07 §7.6.5.3.2 p.299]
- "Robustness of the RIS design is the degree to which it can perform its SR functions correctly in the presence of invalid inputs or abnormal environmental conditions." [PSAR_ch07 §7.6.5.3.3 p.300]
- "The following elements (as appropriate) are considered for system robustness:" [PSAR_ch07 §7.6.5.3.3 p.300]
- "Single failure is addressed by applying IEEE 379-2014 as a special treatment to the design of RIS as described in Section 7.6.5.3." [PSAR_ch07 §7.6.5.3.3 p.300]
- "The RIS instrumentation provides selected measurements in or near the reactor vessel and transmits corresponding signals to the RPS and the NIC for use in protective, control, accident monitoring, and surveillance functions." [PSAR_ch07 §7.6.5.3.3 p.300]
- "Safety-significant equipment in the RIS is designed to perform DL functions provided in Section 7.6.5.2.1 under the full range of applicable conditions." [PSAR_ch07 §7.6.5.3.3 p.300]
- "IEEE 384-2018, which provides detailed criteria for independence, is applied as a special treatment to safety-significant equipment in the RIS." [PSAR_ch07 §7.6.5.3.3 p.300]
- "The RIS instrumentation provides selected measurements in or near the reactor vessel and transmits corresponding signals to the RPS and the NIC for use in protective, control, accident monitoring, and surveillance functions." [PSAR_ch07 §7.6.5.3.3 p.300]
- "No information displays are part of the RIS." [PSAR_ch07 §7.6.5.3.3 p.300]
- "The RIS instrumentation provides selected measurements in or near the reactor vessel and transmits corresponding signals to the RPS and the NIC for use in protective, control, accident monitoring, and surveillance functions." [PSAR_ch07 §7.6.5.3.3 p.300]
- "No automatic control is performed by the RIS." [PSAR_ch07 §7.6.5.3.3 p.300]
- "The RIS instrumentation provides selected measurements in or near the reactor vessel and transmits corresponding signals to the RPS and the NIC for use in protective, control, accident monitoring, and surveillance functions." [PSAR_ch07 §7.6.5.3.3 p.300]
- "The RIS does not have command features which interact with other systems." [PSAR_ch07 §7.6.5.3.3 p.300]
- "A description of the implementation of operating bypass capabilities for the RIS will be provided at the OL stage." [PSAR_ch07 §7.6.5.3.3 p.300]
- "The RIS includes instrument channels which support SR, NSRST, and NST sensing functions." [PSAR_ch07 §7.6.5.3.3 p.301]
- "The architecture of the RIS is such that appropriate channel redundancy is provided through the use of four redundant and independent divisions." [PSAR_ch07 §7.6.5.3.3 p.301]
- "A description of diversity in support of defense-in-depth to address Common-Cause Failures is provided in NAT-4950-A, “I&C Architecture and Design Basis Topical Report” Revision 2 (Reference 7.6.5-9)." [PSAR_ch07 §7.6.5.3.3 p.301]
- "NAT-4950-A is incorporated by reference into the SAR." [PSAR_ch07 §7.6.5.3.3 p.301]
- "See Section 1.4.2 for a list of documents incorporated by reference into the SAR." [PSAR_ch07 §7.6.5.3.3 p.301]
- "SR channels of the RIS are designed so that their behavior is predictable, such that the same set of inputs will produce the same outputs within a known, guaranteed cycle time, and functions are consistently completed within the response time allocated by safety analysis." [PSAR_ch07 §7.6.5.3.3 p.301]
- "A description of the predictable and repeatable behavior of the RIS will be provided at the OL stage." [PSAR_ch07 §7.6.5.3.3 p.301]
- "Security for I&C systems is addressed through the physical security and cyber security programs that are described in Section 11.6." [PSAR_ch07 §7.6.5.3.4 p.301]
- "RIS also provides the RV-GV annulus liquid sodium leak detection parameters as an input to RPS." [PSAR_ch01 §1.1.4.1.14 p.26]
- "Reactor Vessel-Guard Vessel Liquid Sodium Detection | 3 | NSRST" [PSAR_ch07 Table 7.6.5-1 p.303]
- "Core Exit Temperature | 15 | NSRST" [PSAR_ch07 Table 7.6.5-1 p.303]
- "Reactor Head Temperature | 3 | NST" [PSAR_ch07 Table 7.6.5-1 p.303]
- "The RIS has four redundant and independent divisions for parameters that provide SR inputs to the RPS via SR cabling." [PSAR_ch07 §7.6.5.1.1 p.293]
- "Parameters include hot pool level, hot pool temperature, cold pool temperature, and PSP shaft speed." [PSAR_ch01 §1.1.4.1.14 p.26]
- "PSP Current Detector | 8 | SR" [PSAR_ch07 Table 7.6.5-1 p.303]

- "Figure 7.6.5-1 Reactor Instrumentation System Block Diagram" [PSAR_ch07 Figure 7.6.5-1 p.304]

![[PSAR_ch07_Fig_7.6.5-1.png]]

## 해설
Reactor Instrumentation System(`RIS`)은 원자로 용기 안이나 근처의 선택된 변수를 측정하는 계측을 담고, 보호·제어·사고 감시·surveillance 기능을 위해 `RPS`와 `NIC`에 신호를 보낸다. SR%%t:SR%% 변수가 안전해석이 가정한 시간 안에 `RPS`로 전달되도록 설계된다. `RIS`는 개별 계기 channel의 모음이며 channel은 센서 하나와 그 cabling, 신호 증폭 전자 장치로 정의된다. 한 channel은 SR%%t:SR%%, Non-Safety-Related with Special Treatment%%t:NSRST%%, Non-Safety-Related with No Special Treatment%%t:NST%% 기능 가운데 하나 이상을 지원할 수 있다(`may`). SR%%t:SR%% 입력은 네 이중화·독립 division의 SR%%t:SR%% cabling으로 `RPS`에 가고, signal splitter가 이를 복제해 NSRST%%t:NSRST%%·NST%%t:NST%% 신호로 `NIC`에 준다. 센서는 `RXB`의 원자로 용기 안이나 근처에 있고, safety-significant 부분은 `RXB`와 `NCB` 하부구조에 있다.

programmatic special treatment는 Design Reliability Assurance Program, Equipment Qualification Program, Post-construction inspection, testing, and analysis program, Quality Assurance Program Description, Human Factors Engineering Program Plan이다. regulatory guide%%t:RG%% 부합은 `RG 1.22`, `RG 1.100`, `RG 1.180` 완전 부합이고, `RG 1.53`, `RG 1.75`, `RG 1.118`, `RG 1.153`은 더 새로운 `IEEE` 표준 사용으로 부분 부합이다. `RG 1.97, Revision 5`는 `RIS`가 여러 `PAM` 지원 계통 가운데 하나라 부분 부합이며 범위는 operating license%%t:OL%% 단계에서 제공된다.

기능 표는 `DL3` 기능을 SR%%t:SR%%, `DL4`와 `DL5` 기능을 NSRST%%t:NSRST%%로 지정한다. `RIS`는 hot pool 온도(`DL3-RC1b`), hot pool 수위(`DL3-RC1c`, `DL3-RC1h`, `DL3-HR11`, `DL3-HR12`, `DL4-RR8`), `PSP` 속도와 전류(`DL3-RC1d`, `DL3-RC1j`), cold pool 온도(`DL3-RC1e`, `DL3-HR2`, `DL3-HR3`) 센서 신호를 `RPS`로 보낸다. `DL4-HR2`와 `DL4-HR3`에서는 hot pool 온도 신호를 `NIC`로 보내고, `DL5-PAM1`에서는 Type B, C, F `PAM` 변수를 `RPS`로 보낸다. 또 `PHT` 유량, `PSP` 유량, power runback, rod withdrawal 억제를 위한 신호로 NST%%t:NST%% `DL2` 기능을 지원한다.

principal design criteria%%t:PDC%% 2와 4에 따라 safety-significant 부분은 `RXB`와 `NCB` 하부구조에 있고 지진 검증을 받으며, `NCB` 쪽은 mild environment, `RXB` 하부구조의 SR%%t:SR%% 부분은 harsh environment에 대해 검증된다. PDC%%t:PDC%% 3에 따라 `NCB`의 장비는 division별 3-hour 내화 등급 실에, `RXB`의 장비는 division별로 묶어 떨어뜨려 배치된다. PDC%%t:PDC%% 15에 대해 원문은 `RIS`가 감시하는 변수가 primary coolant boundary의 safety-significant 요소 설계 조건을 넘지 않도록 충분한 `margin`을 두는 설계를 지원하도록 선택된다고 적는다. PDC%%t:PDC%% 21과 22에 따라 네 독립 division이 단일 고장과 구성품·division 제외에 대해 보호 기능과 최소 이중화를 유지하고, `RPS`의 2-out-of-4 voting과 함께 한 division을 보수·시험에서 뺄 수 있다. PDC%%t:PDC%% 24에 따라 `NIC`로 가는 입력은 `RPS` 입력과 전자적으로 격리·독립된다.

`IEEE 603-2018`, `IEEE 379-2014`, `IEEE 384-2018`이 규격 special treatment이고, 검증에는 `IEEE/IEC 60780-323-2016`, `IEEE/IEC 60980-344-2020`, `IEEE 420-2013`, `RG 1.180`이 쓰이며, 신뢰도·능력 목표를 위해 `IEEE 338-2022`가 적용된다. safety-significant 장비의 지진 special treatment는 `SCS1` 분류에 상응한다. SR%%t:SR%% 부분은 출력 운전 중 계통 수준의 SR%%t:SR%% 기능을 잃지 않고 시험·교정할 수 있고, 한 division을 보수 bypass해도 계통 수준 안전 기능을 잃지 않는다. `RIS`에는 정보 표시 장치가 없고 자동 제어를 하지 않으며 다른 계통과 상호작용하는 명령 기능이 없다. `IEEE 497-2016` 부합, maintenance bypass와 operating bypass 구현, 예측 가능·반복 가능 거동 설명은 OL%%t:OL%% 단계에서 제공되고, common cause failure%%t:CCF%% 대응 다양성은 `NAT-4950-A`에 기술된다.

`PSAR` Chapter 1은 `RIS`가 RV-GV annulus 액체 소듐 누설 탐지 변수를 `RPS` 입력으로 제공한다고 적는다. Chapter 7 `Table 7.6.5-1`은 `Reactor Vessel-Guard Vessel Liquid Sodium Detection`을 계기 3개의 NSRST%%t:NSRST%%로 적고, 이 절의 기능 표에는 이 변수를 쓰는 기능이 없다. Chapter 1은 변수로 hot pool level, hot pool temperature, cold pool temperature, `PSP` shaft speed를 예시하며(`include`), `Table 7.6.5-1`의 SR%%t:SR%% `PSP Current Detector`는 이 예시에 들어 있지 않다. `Core Exit Temperature`(NSRST%%t:NSRST%%)와 `Reactor Head Temperature`(NST%%t:NST%%)도 이 절 기능 표에 대응 기능이 없다.

## 관련 문서
- [[Natrium_System_IC_Architecture]]
- [[Natrium_System_Reactor_Protection]]
- [[Natrium_System_NI_Control]]
- [[Natrium_SR_Functions_Heat_Removal]]
- [[Natrium_IC_Systems]]
- [[PSAR_ch07]]
