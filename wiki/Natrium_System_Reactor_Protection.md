---
type: natrium
aliases: []
sources:
- PSAR_ch07
- PSAR_ch05
- PSAR_ch11
status: checked
verified: 2026-09-16
term: null
tags:
- natrium
- psar-ch7
terms_pending: []
---

# Natrium Reactor Protection System (RPS)

> [!abstract] 요약
> Reactor Protection System(`RPS`)은 네 division(A–D)의 2-out-of-4 voting으로 reactor scram과 engineered safety feature(`ESF`) 작동을 자동 개시하며 Safety-Related%%t:SR%%과 Non-Safety-Related with Special Treatment%%t:NSRST%% 기능을 함께 수행하는 계통이며, `RadICS` platform을 쓴다. 기능 표는 `DL3` 기능을 SR%%t:SR%%, `DL4`·`DL5` 기능을 NSRST%%t:NSRST%%로 적고, 여러 설계 세부는 Safety Evaluation의 plant-specific action item으로 operating license%%t:OL%% 단계에 넘겨진다.

## 원문 사실
- "The Reactor Protection System (RPS) accepts input signals from plant instrumentation, applies required logic, and automatically generates output signals to initiate safety functions, including reactor scram and engineered safety feature (ESF) actuations." [PSAR_ch07 §7.6.3.1 p.263]
- "The portions of the RPS which support these safety functions are arranged into four redundant divisions (A, B, C, and D)." [PSAR_ch07 §7.6.3.1 p.263]
- "Within each RPS division, the input signals are received by a chassis of electronics, referred to as a safety function chassis, which is dedicated to the performance of safety functions." [PSAR_ch07 §7.6.3.1 p.263]
- "The RPS also provides the capability to manually initiate each reactor scram and ESF actuation function from the Main Control Room (MCR), although these manual functions are not credited in the safety analysis." [PSAR_ch07 §7.6.3.1 p.263]
- "These manual reactor scram and ESF control circuits are diverse from the RPS automatic logic." [PSAR_ch07 §7.6.3.1 p.263]
- "The RPS utilizes SVDUs to display Type B, C, and F Post-Accident Monitoring (PAM) variables, as defined by IEEE 497-2016 “IEEE Standard Criteria for Accident Monitoring Instrumentation for Nuclear Power Generating Stations” (Reference 7.6.3-1)." [PSAR_ch07 §7.6.3.1 p.263]
- "The design of PAM capabilities is informed by IEEE 497-2016." [PSAR_ch07 §7.6.3.1 p.263]
- "A description of the conformance to IEEE 497-2016 as endorsed by Regulatory Guide (RG) 1.97, “Criteria for Accident Monitoring Instrumentation for Nuclear Power Plants,” Revision 5, will be provided at the operating license (OL) stage." [PSAR_ch07 §7.6.3.1 p.263]
- "For variables required for PAM which are not already provided to the RPS for the performance of safety functions, there is a separate, PAM-only, chassis in RPS Divisions A and B dedicated to processing signals from these variables." [PSAR_ch07 §7.6.3.1 p.264]
- "The PAM-only chassis is functionally separate from the safety function chassis, is composed of safety-grade platform components of the same type as the safety function chassis, and is treated as part of the SR protection system for simplicity." [PSAR_ch07 §7.6.3.1 p.264]
- "Segregating these variables onto the dedicated PAM-only chassis avoids additional burden on the safety function chassis and preserves the simplicity in the design and performance of the safety functions." [PSAR_ch07 §7.6.3.1 p.264]
- "By using two PAM-only chassis, the single failure criteria required for PAM Type B and C variables is satisfied." [PSAR_ch07 §7.6.3.1 p.264]
- "The RPS architecture is described in NAT-4950-A “I&C Architecture and Design Basis Topical Report,” Revision 2 (Reference 7.6.3-2), which includes a representative figure." [PSAR_ch07 §7.6.3.1.1 p.264]
- "NAT-4950-A is incorporated by reference into the SAR in its entirety." [PSAR_ch07 §7.6.3.1.1 p.264]
- "See Section 1.4.2 for a list of documents incorporated by reference into the SAR." [PSAR_ch07 §7.6.3.1.1 p.264]
- "The RadICS platform as described in the RadICS Topical Report (Reference 7.6.3-3) is used for the RPS." [PSAR_ch07 §7.6.3.1.1 p.264]
- "The generic open items and plant-specific action items described in Sections 6.0 and 7.0 of the Safety Evaluation for Topical Report 2016-RPC003-TR-001 (Reference 7.6.3-4) will be provided at the OL stage." [PSAR_ch07 §7.6.3.1.1 p.264]
- "A list of RPS equipment and associated safety and seismic classifications is provided in Table 7.6.3-1." [PSAR_ch07 §7.6.3.1.1 p.264]
- "A description of the seismic classification process is provided in Section 6.4.1." [PSAR_ch07 §7.6.3.1.1 p.264]
- "The RPS is designed to perform assigned safety-related (SR) and non-safety-related with special treatment (NSRST) functions and to assist in satisfying Principal Design Criteria (PDC)." [PSAR_ch07 §7.6.3.2 p.265]
- "A description of the process for assigning DL functions to the RPS is provided in Section 7.6.1.1.1." [PSAR_ch07 §7.6.3.2 p.265]
- "A description of the process for assigning the safety classification of the RPS is provided in Section 7.6.1.2." [PSAR_ch07 §7.6.3.2 p.265]
- "A list of RPS equipment, the safety classification of the equipment, and the seismic classification of the equipment is provided in Table 7.6.3-1." [PSAR_ch07 §7.6.3.2 p.265]
- "A description of the seismic classification process is provided in Section 6.4.1." [PSAR_ch07 §7.6.3.2 p.265]
- "Setpoints for the RPS are determined using a methodology that conforms to ANSI/ISA Standard 67.04.01-2018, “Setpoints for Nuclear Safety-Related Instrumentation,” (Reference 7.6.3-5) as endorsed by Regulatory Guide (RG) 1.105, “Setpoints for Safety-Related Instrumentation,” Revision 4, in order to ensure:" [PSAR_ch07 §7.6.3.2 p.265]
- "Setpoints for SR instrumentation are established to protect plant safety and analytical limits" [PSAR_ch07 §7.6.3.2 p.265]
- "Maintenance of instrument channels implementing these setpoints ensures they are functioning as required, consistent with the plant technical specifications" [PSAR_ch07 §7.6.3.2 p.265]
- "The setpoint control program is described in Section 2.0 of Table 11.5-1." [PSAR_ch07 §7.6.3.2 p.265]
- "Special treatments are applied to safety-significant equipment in the RPS to meet quality, design, reliability and performance requirements." [PSAR_ch07 §7.6.3.2 p.265]
- "Special treatments are initially selected based on structure, system, or component (SSC) safety classification as described in Section 6.3." [PSAR_ch07 §7.6.3.2 p.265]
- "Special treatments specific to RPS fundamental design principles are described in Section 7.6.3.1 through Section 7.6.3.3." [PSAR_ch07 §7.6.3.2 p.265]
- "The following programmatic special treatments are identified as applicable to the RPS:" [PSAR_ch07 §7.6.3.2 p.265]
- "Design Reliability Assurance Program (Table 8.0-1)" [PSAR_ch07 §7.6.3.2 p.265]
- "Equipment Qualification Program (Table 8.0-1)" [PSAR_ch07 §7.6.3.2 p.265]
- "Post-construction inspection, testing, and analysis program (Chapter 12)" [PSAR_ch07 §7.6.3.2 p.265]
- "Quality Assurance Program Description (Section 8.1)" [PSAR_ch07 §7.6.3.2 p.265]
- "Human Factors Engineering Program Plan (Section 11.2)" [PSAR_ch07 §7.6.3.2 p.265]
- "Codes, standards, and regulatory guides (RGs) are applied to RPS equipment that is part of the RadICS platform as described in the RadICS Topical Report." [PSAR_ch07 §7.6.3.2 p.265]
- "Application-specific elements of the RPS comply with newer codes, standards, and RGs identified for use as special treatment so long as they do not violate codes, standards, and RGs identified in the RadICS Topical Report or contradict the Safety Evaluation for Topical Report 2016-RPC003-TR-001." [PSAR_ch07 §7.6.3.2 p.265]
- "The RPS conforms to RGs as follows:" [PSAR_ch07 §7.6.3.2 p.265]
- "Application-specific elements of the RPS fully conform to RG 1.22, Revision 0." [PSAR_ch07 §7.6.3.2 p.265]
- "Application-specific elements of the RPS fully conform to RG 1.47, Revision 1." [PSAR_ch07 §7.6.3.2 p.266]
- "Application-specific elements of the RPS partially conform to RG 1.53, Revision 2." [PSAR_ch07 §7.6.3.2 p.266]
- "Conformance is partial because IEEE 379-2014, “IEEE Standard for Application of the Single-Failure Criterion to Nuclear Power Generating Station Safety Systems,” (Reference 7.6.3-6) is used rather than the version of the standard endorsed by this RG." [PSAR_ch07 §7.6.3.2 p.266]
- "Application-specific elements of the RPS partially conform to RG 1.75 Revision 3." [PSAR_ch07 §7.6.3.2 p.266]
- "Conformance is partial because IEEE 384-2018, “IEEE Standard Criteria for Independence of Class 1E Equipment and Circuits,” IEEE 384-2018 (Reference 7.6.3-7) is used rather than the version of the standard endorsed by this RG." [PSAR_ch07 §7.6.3.2 p.266]
- "The RPS partially conforms to RG 1.97, Revision 5." [PSAR_ch07 §7.6.3.2 p.266]
- "The RPS is one of several systems which supports PAM functions and, alone, is not capable of fully conforming with all of the requirements of the RG." [PSAR_ch07 §7.6.3.2 p.266]
- "The extent of conformance to RG 1.97, Revision 5, will be provided at the OL stage." [PSAR_ch07 §7.6.3.2 p.266]
- "Application-specific elements of the RPS fully conform to RG 1.100, Revision 4." [PSAR_ch07 §7.6.3.2 p.266]
- "RadICS platform components used in the RPS conform to an alternate version of the RG in accordance with the RadICS Topical Report and the Safety Evaluation for Topical Report 2016-RPC003-TR-001." [PSAR_ch07 §7.6.3.2 p.266]
- "The RPS fully conforms to RG 1.105, Revision 4." [PSAR_ch07 §7.6.3.2 p.266]
- "Application-specific elements of the RPS partially conform to RG 1.118, Revision 3." [PSAR_ch07 §7.6.3.2 p.266]
- "Conformance is partial because IEEE 338-2022, “IEEE Standard for Criteria for the Periodic Surveillance Testing of Nuclear Power Generating Station Safety Systems,” (Reference 7.6.3-8) is used rather than the version of the standard endorsed by this RG." [PSAR_ch07 §7.6.3.2 p.266]
- "Application-specific elements of the RPS fully conform to RG 1.152, Revision 4." [PSAR_ch07 §7.6.3.2 p.266]
- "RadICS platform components used in the RPS conform to an alternate version of the RG in accordance with the RadICS Topical Report and the Safety Evaluation for Topical Report 2016-RPC003-TR-001." [PSAR_ch07 §7.6.3.2 p.266]
- "Application-specific elements of the RPS partially conform to RG 1.153, Revision 1." [PSAR_ch07 §7.6.3.2 p.267]
- "Conformance is partial because IEEE 603-2018, “IEEE Standard Criteria for Safety Systems for Nuclear Power Generating Stations,” (Reference 7.6.3-9) is used for the application-specific elements rather than the version of the standard endorsed by this RG." [PSAR_ch07 §7.6.3.2 p.267]
- "RadICS platform components conform to RG 1.153, Revision 1, in accordance with the RadICS Topical Report and the Safety Evaluation for Topical Report 2016-RPC003-TR-001." [PSAR_ch07 §7.6.3.2 p.267]
- "Application-specific elements of the RPS fully conform to RG 1.180, Revision 2." [PSAR_ch07 §7.6.3.2 p.267]
- "RadICS platform components used in the RPS conform to an alternate version of the RG in accordance with the RadICS Topical Report and the Safety Evaluation for Topical Report 2016-RPC003-TR-001." [PSAR_ch07 §7.6.3.2 p.267]
- "PRA safety functions (PSFs) are determined through the plant-specific PRA described in Section 3.1." [PSAR_ch07 §7.6.3.2.1 p.267]
- "The safety-significant PSFs are identified as safety-related (SR) functions or non-safety-related with special treatment (NSRST) functions as defined in Section 5.2." [PSAR_ch07 §7.6.3.2.1 p.267]
- "The RPS supports the following safety-significant functions, which are designated as SR (for DL3 functions) or NSRST (for DL4 and DL5 functions) to indicate the safety classification of RPS components relied upon to perform the function:" [PSAR_ch07 §7.6.3.2.1 p.267]

| Function ID | Function Description | RPS Functional Support | 출처 |
|---|---|---|---|
| DL3-RC1a | Reactor scram on high-high neutron flux | RPS continuously monitors neutron flux signal inputs from the XIS and compares them to a power range, high range setpoint. When a setpoint is exceeded, all control rod assemblies (CRAs) are inserted by gravity. | [PSAR_ch07 §7.6.3.2.1 p.268] |
| DL3-RC1b | Reactor scram on high-high hot pool temperature | RPS continuously monitors primary sodium hot pool temperature signal inputs from the RIS and compares Them to a setpoint. When a setpoint is exceeded, all CRAs are inserted by gravity. | [PSAR_ch07 §7.6.3.2.1 p.268] |
| DL3-RC1c | Reactor scram on high-high primary sodium level | RPS continuously monitors primary sodium hot pool level signal inputs from the RIS and compares them to a setpoint. When a setpoint is exceeded, all CRAs are inserted by gravity. | [PSAR_ch07 §7.6.3.2.1 p.268] |
| DL3-RC1d | Reactor scram on high-high power-to-flow ratio | RPS continuously monitors neutron flux signal inputs from the XIS. RPS continuously monitors primary sodium pump (PSP) speed and current inputs from the RIS and calculates primary sodium flow. When the ratio of neutron flux to primary sodium flow exceeds a setpoint, all CRAs are inserted by gravity. | [PSAR_ch07 §7.6.3.2.1 p.268] |
| DL3-RC1e | Reactor scram on high-high cold pool temperature | RPS continuously monitors primary sodium cold pool temperature signal inputs from the RIS and compares them to a setpoint. When a setpoint is exceeded, all CRAs are inserted by gravity. | [PSAR_ch07 §7.6.3.2.1 p.268] |
| DL3-RC1f | Reactor scram on high-high positive neutron flux rate | RPS continuously monitors neutron flux signal inputs from the XIS, calculates the rate of change of neutron flux, and compares them to a setpoint. When a setpoint is exceeded, all CRAs are inserted by gravity. | [PSAR_ch07 §7.6.3.2.1 p.268] |
| DL3-RC1g | Reactor scram on high-high negative neutron flux rate | RPS continuously monitors neutron flux signal inputs from the XIS, calculates the rate of change of neutron flux, and compares them to a setpoint. When a setpoint is exceeded, all CRAs are inserted by gravity. | [PSAR_ch07 §7.6.3.2.1 p.268] |
| DL3-RC1h | Reactor scram on low-low primary sodium level | RPS continuously monitors primary sodium hot pool level signal inputs from the RIS and compares them to a setpoint. When a setpoint is exceeded, all CRAs are inserted by gravity. | [PSAR_ch07 §7.6.3.2.1 p.268] |
| DL3-RC1i | Reactor scram on low power, high neutron flux | RPS continuously monitors neutron flux signal inputs from the XIS and compares them to a power range, low range setpoint. When a setpoint is exceeded, all CRAs are inserted by gravity. | [PSAR_ch07 §7.6.3.2.1 p.268] |
| DL3-RC1j | Reactor scram on loss of primary sodium flow | RPS continuously monitors PSP speed and current inputs from the RIS, calculates primary sodium flow, and performs a calculation to determine loss of primary sodium flow. When a loss of primary sodium flow is determined, all CRAs are inserted by gravity. | [PSAR_ch07 §7.6.3.2.1 p.268] |
| DL3-RC2 | Reactor scram on loss of power | RPS outputs fail in the safe state in the event of a loss of incoming power. | [PSAR_ch07 §7.6.3.2.1 p.268] |
| DL3- HR2 | PSP trip on high-high primary sodium temperature | RPS continuously monitors primary sodium cold pool temperature signal inputs from the RIS and neutron flux signal inputs from the XIS and compares them to setpoints. If a scram signal exists in the RPS, primary sodium cold pool temperature is above a setpoint, and neutron flux is below a setpoint, the PSPs are tripped. | [PSAR_ch07 §7.6.3.2.1 p.268] |
| DL3-HR3 | Intermediate sodium pump (ISP) trip on high-high primary sodium temperature | RPS continuously monitors primary sodium cold pool temperature signal inputs from the RIS and neutron flux signal inputs from the XIS and compares them to setpoints. If a scram signal exists in the RPS, primary sodium cold pool temperature is above a setpoint, and neutron flux is below a setpoint, the ISPs are tripped. | [PSAR_ch07 §7.6.3.2.1 p.268] |
| DL3-HR11 | Sodium processing system (SPS) pump trip on low primary sodium level | RPS continuously monitors primary sodium hot pool level signal inputs from the RIS and compares them to a setpoint. When a setpoint is exceeded, the SPS-P pump is tripped. | [PSAR_ch07 §7.6.3.2.1 p.268] |
| DL3-HR12 | ISP trip on high-high primary sodium level | RPS continuously monitors primary sodium hot pool level signal inputs from the RIS and neutron flux signal inputs from the XIS and compares them to setpoints. If a scram signal exists in the RPS, primary sodium hot pool level is above a setpoint, and neutron flux is below a setpoint, the ISPs are tripped. | [PSAR_ch07 §7.6.3.2.1 p.268] |
| DL4-RC1 | Reactor scram-manual | All CRAs are inserted by gravity drop on manual switch. | [PSAR_ch07 §7.6.3.2.1 p.268] |
| DL4-RC3 | CRD driveline scram follow | RPS issues a failsafe control signal to mechanically drive Control rods in when any automatic or manual scram occurs. The RPS output signals that initiate CRD driveline scram follow are independent of the RTB demand output signals from the RPS. | [PSAR_ch07 §7.6.3.2.1 p.268] |
| DL4-RC4 | Automatic seismic trip | The RPS opens the RTBs upon receipt of a seismic trip demand signal from the anticipatory automatic seismic trip system (AST). | [PSAR_ch07 §7.6.3.2.1 p.268] |
| DL4-HR6 | Manual PSP trip | PSP pumps are tripped on manual switch. | [PSAR_ch07 §7.6.3.2.1 p.268] |
| DL4-HR7 | Manual ISP trip | ISP pumps are tripped on manual switch. | [PSAR_ch07 §7.6.3.2.1 p.268] |
| DL4-RR8 | Manual SPS pump trip on low primary sodium level | RPS continuously monitors and displays primary sodium hot pool level from signal inputs from the RIS. SPS-P pump is tripped on manual switch. | [PSAR_ch07 §7.6.3.2.1 p.268] |
| DL5-PAM1 | Post-accident monitoring | The RPS supports the display of Type B, C, and F PAM variables. | [PSAR_ch07 §7.6.3.2.1 p.268] |

- "Safety-Related Design Criteria corresponding to the SR functions applicable to the RPS are derived as described in Section 6.1.2 and identified in Section 5.2." [PSAR_ch07 §7.6.3.2.1 p.268]
- "The Safety-Related Design Criteria are incorporated into the design of the RPS as described in Section 7.6.3.1." [PSAR_ch07 §7.6.3.2.1 p.268]
- "The NSRST functions DL4-RC1, DL4-HR6, DL4-HR7, and DL4-RR8 are manual initiations of automatic safety functions." [PSAR_ch07 §7.6.3.2.1 p.268]
- "Based solely on the PRA model, these functions would be classified as non-safety-related with no special treatment (NST)." [PSAR_ch07 §7.6.3.2.1 p.268]
- "However, they are classified as NSRST for defense-in-depth purposes and compliance with IEEE 603-1991 for manual initiation of an automatic safety function." [PSAR_ch07 §7.6.3.2.1 p.268]
- "There are no non-safety-related with no special treatment DL functions allocated to the RPS." [PSAR_ch07 §7.6.3.2.1 p.268]
- "The CRAs are described in Section 7.1.1." [PSAR_ch07 §7.6.3.2.1 p.268]
- "The Primary Heat Transport System and Primary Sodium Pump are described in Section 7.1.3." [PSAR_ch07 §7.6.3.2.1 p.268]
- "The Intermediate Heat Transport System and Intermediate Sodium Pump are described in Section 7.1.4." [PSAR_ch07 §7.6.3.2.1 p.268]
- "The Sodium Processing System is described in Section 7.2.4." [PSAR_ch07 §7.6.3.2.1 p.268]
- "The CRD is described in Section 7.2.5." [PSAR_ch07 §7.6.3.2.1 p.268]
- "The Anticipatory Automatic Seismic Trip System is described in Section 7.6.8." [PSAR_ch07 §7.6.3.2.1 p.268]
- "PDC are identified in Section 5.3." [PSAR_ch07 §7.6.3.2.2 p.268]
- "The RPS conforms to PDC as described below." [PSAR_ch07 §7.6.3.2.2 p.268]
- "Consistent with PDC 2, Design based for protection against natural phenomena, in the event of adverse conditions due to natural phenomena, all RPS safety-significant SSCs maintain the capability to perform their required functions." [PSAR_ch07 §7.6.3.2.2 p.268]
- "Earthquakes- SR portions of the RPS are located in the NCB substructure, which is designed to withstand the effects of earthquakes in accordance with the methods described in Section 6.4.1." [PSAR_ch07 §7.6.3.2.2 p.271]
- "SR portions of the RPS are seismically qualified to remain operable in the SR NCB substructure during and after postulated earthquakes." [PSAR_ch07 §7.6.3.2.2 p.271]
- "External flooding- The RPS accounts for external flooding hazard by being located inside of the NCB, which is above the maximum flood level." [PSAR_ch07 §7.6.3.2.2 p.271]
- "High winds- To address the design basis extreme wind hazard, SR portions of the RPS are located in the SR NCB substructure, which is designed for the extreme wind hazard." [PSAR_ch07 §7.6.3.2.2 p.271]
- "Extreme climate- The RPS equipment is located in the climate-controlled NCB to mitigate temperature, humidity, and winter precipitation hazards." [PSAR_ch07 §7.6.3.2.2 p.271]
- "Consistent with PDC 3, Fire protection, each SR RPS division is located in its own division-specific RPS vault in the SR NCB substructure." [PSAR_ch07 §7.6.3.2.2 p.271]
- "The RPS vault room walls are all 3-hour fire rated and the doors have at least a 3-hour fire rating." [PSAR_ch07 §7.6.3.2.2 p.271]
- "Locating each SR RPS division in its own 3-hour fire rated vault room minimizes the likelihood of a fire simultaneously affecting multiple divisions and minimizes the likelihood that fire will affect any RPS SR function." [PSAR_ch07 §7.6.3.2.2 p.271]
- "Consistent with PDC 4, Environmental and dynamic effects design bases, the SR NCB substructure protects the SR portions of the RPS from external hazards caused by transportation incidents, incidents at offsite industrial and chemical facilities, and external missiles resulting from a turbine failure in the plant’s turbine generator set." [PSAR_ch07 §7.6.3.2.2 p.271]
- "The SR NCB substructure provides a mild environment for SR portions of the RPS, which are qualified to remain operable in such an environment during postulated external hazards." [PSAR_ch07 §7.6.3.2.2 p.271]
- "Consistent with PDC 10, Reactor design, the RPS DL3 reactor scram and ESF functions are design with appropriate margin to ensure that analytical limits established in the safety analysis are not exceeded as a result of anticipated operational occurrences (AOOs) which have not been mitigated by DL2 functions." [PSAR_ch07 §7.6.3.2.2 p.271]
- "Consistent with PDC 13, Instrumentation and control, the RPS accepts input signals from plant instrumentation in order to monitor plant variables and automatically generate reactor scram and ESF actuation signals when required in order to mitigate AOOs and design-basis events within prescribed design basis accident limits." [PSAR_ch07 §7.6.3.2.2 p.271]
- "The RPS serves to display these input variables and others to operators in the control room and in the Remote Shutdown Complex during normal and postulated post-accident conditions." [PSAR_ch07 §7.6.3.2.2 p.271]
- "All input instruments, RPS signal conditioning, and RPS displays associated with reactor scram, ESF, and PAM functions are designed to monitor associated variables of their anticipated ranges for normal operation, AOOs, and accident conditions as appropriate." [PSAR_ch07 §7.6.3.2.2 p.271]
- "Consistent with PDC 15, Primary coolant system design, the RPS DL3 reactor scram and ESF functions are designed with appropriate margin to ensure that analytical limits established in the safety analysis are not exceeded as a result of AOOs which have not been mitigated by DL2 functions." [PSAR_ch07 §7.6.3.2.2 p.271]
- "Consistent with PDC 20, Protection system functions, plant instrumentation continuously senses plant conditions and provides corresponding input signals to the RPS." [PSAR_ch07 §7.6.3.2.2 p.272]
- "The RPS is designed to continuously monitor those input signals, apply required logic, and automatically initiate DL3 reactor scram and ESF functions when the RPS senses an AOO which has not been mitigated by DL2 functions as designed, or when design basis event or accident conditions are sensed." [PSAR_ch07 §7.6.3.2.2 p.272]
- "The RPS is designed to perform these DL3 functions to ensure that analytical limits established in the safety analysis are not exceeded as a result of AOOs or design-basis events." [PSAR_ch07 §7.6.3.2.2 p.272]
- "Consistent with PDC 21, Protection system reliability and testability, the SR portions of the RPS are arranged into four redundant and independent divisions." [PSAR_ch07 §7.6.3.2.2 p.272]
- "Each process variable input used by RPS to perform a safety function is measured by four redundant sensing instruments (or groups of instruments) which are also divided into four redundant and independent divisions." [PSAR_ch07 §7.6.3.2.2 p.272]
- "The RPS actuates reactor scram and ESF functions when at least 2 out of the 4 divisions independently determine that such action is required." [PSAR_ch07 §7.6.3.2.2 p.272]
- "This divisional arrangement and 2-out-of-4 voting design features allow in-service testability." [PSAR_ch07 §7.6.3.2.2 p.272]
- "The system design allows for any division to be taken out of service for testing at any time without loss of any safety function and without loss of minimum required redundancy." [PSAR_ch07 §7.6.3.2.2 p.272]
- "The divisional arrangement and 2-out-of-4 voting design features promote high system reliability." [PSAR_ch07 §7.6.3.2.2 p.272]
- "The RPS is designed to withstand a failure of any division without loss of any safety function and without loss of minimum required redundancy." [PSAR_ch07 §7.6.3.2.2 p.272]
- "In fact, the RPS is designed to withstand a single failure in any operating division, even when one division has been taken out of service for testing." [PSAR_ch07 §7.6.3.2.2 p.272]
- "The capability to periodically test divisions independently while in-service to determine failures and losses of redundancy that may have occurred further promotes high system reliability." [PSAR_ch07 §7.6.3.2.2 p.272]
- "Consistent with PDC 22, Protection system independence, the SR portions of the RPS are arranged into four redundant and independent divisions." [PSAR_ch07 §7.6.3.2.2 p.272]
- "Each process variable input used by RPS to perform a safety function is measured by four redundant sensing instruments (or groups of instruments) which are also divided into four redundant and independent divisions." [PSAR_ch07 §7.6.3.2.2 p.272]
- "The RPS actuates reactor scram and ESF functions when at least 2 out of the 4 divisions independently determine that such action is required." [PSAR_ch07 §7.6.3.2.2 p.272]
- "Each of the four redundant RPS divisions are independent and physically separated from the other redundant RPS divisions to the degree necessary to ensure accomplishment of safety functions." [PSAR_ch07 §7.6.3.2.2 p.272]
- "All four redundant RPS divisions are independent and physically separated from the effects of design-basis events which they are designed to mitigate." [PSAR_ch07 §7.6.3.2.2 p.272]
- "The RPS equipment is located to minimize potential damage from hazards and is qualified to substantiate design basis performance requirements." [PSAR_ch07 §7.6.3.2.2 p.272]
- "All four redundant RPS divisions are independent and physically separated or isolated from other systems, including interconnected systems and equipment in proximity, to the degree necessary to ensure accomplishment of safety functions." [PSAR_ch07 §7.6.3.2.2 p.272]
- "The divisional arrangement and 2-out-of-4 voting design features allow for any division to be out of service for maintenance or testing without any loss of safety function." [PSAR_ch07 §7.6.3.2.2 p.272]
- "Consistent with PDC 23, Protection system failure modes, during normal operation (when reactor scram is not required), the RPS maintains voltage on the RTB undervoltage coils to keep RTBs in the closed position, thus maintaining power to the CRD solenoid operated valve coils which maintain argon pressure to hold the rods at controlled positions above or within the core." [PSAR_ch07 §7.6.3.2.2 p.273]
- "On loss of incoming power to RPS, the RPS voltage on the RTB undervoltage coils is lost, allowing the undervoltage release mechanism to open the RTBs, thus interrupting power to the CRD solenoid operated valve coils, venting CRD argon and allowing rods to drop fully into the core via gravity." [PSAR_ch07 §7.6.3.2.2 p.273]
- "In this way, the RPS reactor scram circuit is designed as “de-energize to trip”, consistent with PDC 23." [PSAR_ch07 §7.6.3.2.2 p.273]
- "All RPS ESF functions execute the tripping of pump breakers to stop the associated pump, which is evaluated to be the safe state." [PSAR_ch07 §7.6.3.2.2 p.273]
- "During normal operation (when ESF actuation is not required), the RPS maintains normally open relays in the closed position in order to maintain control power on the pump breaker undervoltage coils, thus keeping pump breakers in the closed position, maintaining normal power to the pumps." [PSAR_ch07 §7.6.3.2.2 p.273]
- "On loss of incoming power to RPS, the RPS voltage on the normally open relays is removed, allowing those relay contacts to open, interrupting control power to the pump breaker undervoltage coils, tripping the pump breakers, and stopping pump rotation." [PSAR_ch07 §7.6.3.2.2 p.273]
- "In this way, the RPS ESF circuits are designed as “de-energize to trip”, consistent with PDC 23." [PSAR_ch07 §7.6.3.2.2 p.273]
- "The SR RPS equipment is located in the mild environment of the SR NCB substructure." [PSAR_ch07 §7.6.3.2.2 p.273]
- "The SR RPS equipment is environmentally and seismically qualified to remain operable during anticipated adverse conditions at this location." [PSAR_ch07 §7.6.3.2.2 p.273]
- "Additionally, the RPS electronics (logic and input-output) modules perform continuous self-diagnostics." [PSAR_ch07 §7.6.3.2.2 p.273]
- "In the event that self-diagnostics detect a critical fault in the electronics that could affect performance of a safety function, the system places all outputs to the safe (tripped) state." [PSAR_ch07 §7.6.3.2.2 p.273]
- "The RPS also employs range-checking on analog input signals from system such as Nuclear Instrumentation System and Reactor Instrumentation System." [PSAR_ch07 §7.6.3.2.2 p.273]
- "Instrument channels are designed such that loss of power at the transmitting system is detected by RPS range-checking, in which case the RPS will place the associated circuit outputs in the safe state." [PSAR_ch07 §7.6.3.2.2 p.273]
- "The Nuclear Instrumentation System is described in Section 7.6.4, and the Reactor Instrumentation System is described in Section 7.6.5." [PSAR_ch07 §7.6.3.2.2 p.273]
- "Consistent with PDC 24, Separation of protection and control systems, the RPS is designed in accordance IEEE Std 603-2018 Clause 5.1, Single-Failure Criterion, Clause 5.6, Independence, and Clause 6.3, Interaction Between the Sense and Command Features and Other Systems." [PSAR_ch07 §7.6.3.2.2 p.273]
- "Accordingly, the RPS is designed with sufficient separation from control systems such that all reliability, redundancy, and independence requirements of the RPS remain intact, even when there is a single control system failure, or failure or removal from service of any component common to the RPS or any control system." [PSAR_ch07 §7.6.3.2.2 p.273]
- "The standard listed above for PDC 24 is applied in a manner that does not violate codes, standards, and RGs identified in the RadICS Topical Report as described in Section 7.6.3.2." [PSAR_ch07 §7.6.3.2.2 p.273]
- "Consistent with PDC 25, Protection system requirements for reactivity control malfunctions, the RPS is designed in accordance IEEE Std 603-2018 Clause 5.1, Single-Failure Criterion, Clause 5.6, Independence, and Clause 6.3, Interaction Between the Sense and Command Features and Other Systems." [PSAR_ch07 §7.6.3.2.2 p.274]
- "Accordingly, the RPS DL3 reactor scram and ESF functions are designed to ensure that analytical limits established in the safety analysis are not exceeded as a result of AOOs even when a single failure of the reactivity control system has occurred." [PSAR_ch07 §7.6.3.2.2 p.274]
- "The standard listed above for PDC 25 is applied in a manner that does not violate codes, standards, and RGs identified in the RadICS Topical Report as described in Section 7.6.3.2." [PSAR_ch07 §7.6.3.2.2 p.274]
- "Consistent with PDC 26, Reactivity control systems, the RPS DL3 reactor scram function is designed to insert sufficient negative reactivity promptly with appropriate margin to ensure analytical limits established in the safety analysis are not exceeded as a result of AOOs which have not been mitigated by DL2 functions as designed." [PSAR_ch07 §7.6.3.2.2 p.274]
- "The RPS DL3 reactor scram function is also designed to insert sufficient negative reactivity with appropriate margin to achieve and maintain a safe shutdown condition following a postulated accident." [PSAR_ch07 §7.6.3.2.2 p.274]
- "The RPS is designed such that whenever any division generates a DL3 reactor scram demand output, that RPS division also generates an independent signal to the CRD system to demand a DL4 CRD driveline scram follow." [PSAR_ch07 §7.6.3.2.2 p.274]
- "The CRD system initiates DL4 CRD driveline scram follow when at least 2 of 4 RPS divisions send a demand signal." [PSAR_ch07 §7.6.3.2.2 p.274]
- "Consistent with PDC 28, Reactivity limits, the RPS DL3 reactor scram function is designed with appropriate margin to ensure that analytical limits established in the safety analysis are not exceeded during postulated accidents." [PSAR_ch07 §7.6.3.2.2 p.274]
- "Consistent with PDC 29, Protection against AOOs, the RPS DL3 reactor scram and ESF functions are designed with appropriate margin to ensure that analytical limits established in the safety analysis are not exceeded as a result of AOOs which have not been mitigated by DL2 functions." [PSAR_ch07 §7.6.3.2.2 p.274]
- "The RPS design minimizes the potential for failures to occur in SSCs that perform SR functions." [PSAR_ch07 §7.6.3.3 p.274]
- "Qualification, reliability, robustness, security, diversity, and defense-in-depth features are discussed in Section 7.6.3.3.1 through Section 7.6.3.3.4." [PSAR_ch07 §7.6.3.3 p.274]
- "The following industry codes and standards are applied as special treatments to the overall design of safety-significant, application-specific equipment in the RPS that is outside the scope of the RadICS platform:" [PSAR_ch07 §7.6.3.3 p.274]

| 목록 항목 | 출처 |
|---|---|
| IEEE 603-2018 | [PSAR_ch07 §7.6.3.3 p.274] |

- "IEEE 7-4.3.2-2016 (Reference 7.6.3-10)" [PSAR_ch07 §7.6.3.3 p.274]

| 목록 항목 | 출처 |
|---|---|
| IEEE 379-2014 | [PSAR_ch07 §7.6.3.3 p.274] |
| IEEE 384-2018 | [PSAR_ch07 §7.6.3.3 p.274] |

- "The following industry codes, standards, and RGs are applied as special treatments for environmental, seismic, and electromagnetic capability qualification of safety-significant, application-specific equipment in the RPS that is outside the scope of the RadICS platform:" [PSAR_ch07 §7.6.3.3.1 p.275]
- "IEEE/IEC 60780-323-2016, “International Standard- Nuclear Facilities- Electrical equipment important to safety-Qualification,” (Reference 7.6.3-11)" [PSAR_ch07 §7.6.3.3.1 p.275]
- "IEEE/IEC 60980-344-2020 “International Standard - Nuclear facilities - Equipment important to safety - Seismic qualification” (Reference 7.6.3-12)" [PSAR_ch07 §7.6.3.3.1 p.275]
- "IEEE 420-2013, “IEEE Standard for the Decide and Qualification of Class 1E Control Boards, Panels, and Racks Used in Nuclear Power Generating Station” (Reference 7.6.3-13)" [PSAR_ch07 §7.6.3.3.1 p.275]
- "RG 1.180, Revision 2, “Guidelines for Evaluating Electromagnetic and Radio-Frequency Interference in Safety-Related Instrumentation and Control Systems”" [PSAR_ch07 §7.6.3.3.1 p.275]
- "The safety-significant equipment in the RPS is assigned seismic special treatment commensurate with the seismic classifications shown in Table 7.6.3-1." [PSAR_ch07 §7.6.3.3.1 p.275]
- "Seismic special treatment is described in Section 6.4.1." [PSAR_ch07 §7.6.3.3.1 p.275]
- "The method for confirming specific reliability and capability targets for SSCs at the OL stage is described in Section 6.2." [PSAR_ch07 §7.6.3.3.2 p.275]
- "The ability of the RPS to facilitate timely recognition, location, replacement, repair, and adjustment of malfunctioning equipment will be described as part of addressing the plant-specific action items from Section 7.0 of the Safety Evaluation for Topical Report 2016-RPC003-TR-001 at the OL stage." [PSAR_ch07 §7.6.3.3.2 p.275]
- "IEEE 603-2018 Clause 5.11, IEEE 384-2018, and IEEE 420-2013 are applied as special treatments to safety-significant, application-specific equipment in the RPS that is outside the scope of the RadICS platform in order to ensure equipment is distinctly identified for each redundant portion of the system." [PSAR_ch07 §7.6.3.3.2 p.275]
- "Identification of RPS equipment that is part of the RadICS platform is described in the RadICS Topical Report." [PSAR_ch07 §7.6.3.3.2 p.275]
- "RPS equipment is designed in accordance with IEEE 420-2013, including requirements regarding human factors, and is reviewed per the Human Factors Engineering Program Plan that is described in Section 11.2." [PSAR_ch07 §7.6.3.3.2 p.275]
- "The following industry codes and standards are applied as special treatments to the safety-significant equipment in the RPS to ensure that reliability and capability targets are met:" [PSAR_ch07 §7.6.3.3.2 p.276]

| 목록 항목 | 출처 |
|---|---|
| IEEE 338-2022 | [PSAR_ch07 §7.6.3.3.2 p.276] |

- "IEEE 603- 2018" [PSAR_ch07 §7.6.3.3.2 p.276]
- "The use of these codes and standards to satisfy plant-specific action items from Section 7.0 of the Safety Evaluation for Topical Report 2016-RPC003-TR-001 will be provided at the OL stage." [PSAR_ch07 §7.6.3.3.2 p.276]
- "This will include a system-level evaluation of the reliability of the final application-specific RPS design to address plant-specific action item 7.6." [PSAR_ch07 §7.6.3.3.2 p.276]
- "The RPS is capable of testing and calibration during power operation without loss of required safety functions at the system level." [PSAR_ch07 §7.6.3.3.2 p.276]
- "The design of RPS supports checking each channel (including sensor and any electronics) required for a safety function by one of the following means:" [PSAR_ch07 §7.6.3.3.2 p.276]
- "cross-checking between redundant channels with available readouts" [PSAR_ch07 §7.6.3.3.2 p.276]
- "introducing and varying substitute input" [PSAR_ch07 §7.6.3.3.2 p.276]
- "perturbing the monitored variable" [PSAR_ch07 §7.6.3.3.2 p.276]
- "Additional detail on the RPS capability for testing and calibration is included in Section 7.6.3.2.2 in the description of the RPS conformance to PDC 21." [PSAR_ch07 §7.6.3.3.2 p.276]
- "The capability for testing and calibration to satisfy plant-specific action items from Section 7.0 of the Safety Evaluation for Topical Report 2016-RPC003-TR-001 will be provided at the OL stage." [PSAR_ch07 §7.6.3.3.2 p.276]
- "This will include a system-level evaluation of system testing and surveillance of the final application-specific RPS design to address plant-specific action item 7.8." [PSAR_ch07 §7.6.3.3.2 p.276]
- "A description of maintenance bypass features will be provided as part of addressing the plant-specific action items described in Section 7.0 of the Safety Evaluation for Topical Report 2016-RPC003-TR-001 at the OL stage." [PSAR_ch07 §7.6.3.3.2 p.276]
- "Robustness of the RPS design is the degree to which it can perform its SR functions correctly in the presence of invalid inputs or stressful environmental conditions." [PSAR_ch07 §7.6.3.3.3 p.277]
- "The following elements are considered for system robustness:" [PSAR_ch07 §7.6.3.3.3 p.277]
- "Single failure is addressed by applying IEEE 379-2014 as a special treatment to the design of the RPS." [PSAR_ch07 §7.6.3.3.3 p.277]
- "A description of how single failures cannot adversely affect protection functions will be provided as part of addressing the plant-specific action items described in Section 7.0 of the Safety Evaluation for Topical Report 2016-RPC003-TR-001 at the OL stage." [PSAR_ch07 §7.6.3.3.3 p.277]
- "The RPS is designed so that, once initiated automatically or manually, the sequence of protective actions continue to completion." [PSAR_ch07 §7.6.3.3.3 p.277]
- "Deliberate operator action is required to return the RPS to normal." [PSAR_ch07 §7.6.3.3.3 p.277]
- "The characteristics of the RPS to accomplish safety functions under the full range of design basis conditions are described in the RadICS Topical Report." [PSAR_ch07 §7.6.3.3.3 p.277]
- "Application-specific elements are designed and qualified to accomplish safety functions under the full range of design basis conditions." [PSAR_ch07 §7.6.3.3.3 p.277]
- "Plant-specific information relating to system integrity to satisfy plant-specific action items from Section 7.0 of the Safety Evaluation for Topical Report 2016-RPC003-TR-001 will be provided at the OL stage." [PSAR_ch07 §7.6.3.3.3 p.277]
- "This will include the equipment environmental qualification of the final application-specific RPS design to address plant-specific action item 7.4." [PSAR_ch07 §7.6.3.3.3 p.277]
- "A description of independence for the RPS is provided in Section 7.6.3.2.2 in the description of the RPS conformance to PDC 22." [PSAR_ch07 §7.6.3.3.3 p.277]
- "A description of the interaction between RPS sense and command features and other systems is provided in Section 7.6.3.2.2 in the description of RPS conformance to PDC 24." [PSAR_ch07 §7.6.3.3.3 p.277]
- "A description of the implementation of operating bypass capabilities will be provided at the OL stage." [PSAR_ch07 §7.6.3.3.3 p.277]
- "The RPS consists of four redundant and independent divisions." [PSAR_ch07 §7.6.3.3.3 p.277]
- "Additional description of the reliability, testability, and independence of the RPS divisions is provided in Section 7.6.3.2.2 in the description of RPS conformance to PDC 21 and PDC 22." [PSAR_ch07 §7.6.3.3.3 p.277]
- "Diversity in support of defense-in-depth to address Common-Cause Failures is described in NAT-4950-A." [PSAR_ch07 §7.6.3.3.3 p.278]
- "The ability of the RPS to perform in a deterministic manner is described in the RadICS Topical Report and is evaluated in Section 3.7.2 of the Safety Evaluation for Topical Report 2016-RPC003-TR-001." [PSAR_ch07 §7.6.3.3.3 p.278]
- "Additional detail of the ability of the RPS to operate in a predictable and repeatable manner will be provided at the OL stage." [PSAR_ch07 §7.6.3.3.3 p.278]
- "A Secure Development and Operational Environment is established for the RPS that satisfies the applicable regulatory evaluation criteria of RG 1.152 Rev 4." [PSAR_ch07 §7.6.3.3.4 p.278]
- "A description of the Secure Development and Operational Environment will be provided as part of addressing the plant-specific action items described in Section 7.0 of the Safety Evaluation for Topical Report 2016-RPC003-TR-001 at the OL stage." [PSAR_ch07 §7.6.3.3.4 p.278]
- "Security for I&C systems is addressed through the physical security and cyber security programs that are described in Section 11.6." [PSAR_ch07 §7.6.3.3.4 p.278]

| General RPS Equipment Description | Component Description | Safety Classification | Seismic Classification | 출처 |
|---|---|---|---|---|
| RPS Electronics Cabinets | RPS Division A Cabinet | SR | SCS1 | [PSAR_ch07 Table 7.6.3-1 p.280] |
| RPS Electronics Cabinets | RPS Division B Cabinet | SR | SCS1 | [PSAR_ch07 Table 7.6.3-1 p.280] |
| RPS Electronics Cabinets | RPS Division C Cabinet | SR | SCS1 | [PSAR_ch07 Table 7.6.3-1 p.280] |
| RPS Electronics Cabinets | RPS Division D Cabinet | SR | SCS1 | [PSAR_ch07 Table 7.6.3-1 p.280] |
| RPS Data Gateway | RPS Data Gateway Cabinet | NST | None | [PSAR_ch07 Table 7.6.3-1 p.280] |
| RPS Divisional SVDUs (MCR) | RPS Division A SVDU | NSRST | SCN1 | [PSAR_ch07 Table 7.6.3-1 p.280] |
| RPS Divisional SVDUs (MCR) | RPS Division B SVDU | NSRST | SCN1 | [PSAR_ch07 Table 7.6.3-1 p.280] |
| RPS Divisional SVDUs (MCR) | RPS Division C SVDU | NSRST | SCN1 | [PSAR_ch07 Table 7.6.3-1 p.280] |
| RPS Divisional SVDUs (MCR) | RPS Division D SVDU | NSRST | SCN1 | [PSAR_ch07 Table 7.6.3-1 p.280] |
| RPS Manual Switches | RPS Division A Manual Switch Panel | NSRST | SCN1 | [PSAR_ch07 Table 7.6.3-1 p.280] |
| RPS Manual Switches | RPS Division B Manual Switch Panel | NSRST | SCN1 | [PSAR_ch07 Table 7.6.3-1 p.280] |
| RPS Manual Switches | RPS Division C Manual Switch Panel | NSRST | SCN1 | [PSAR_ch07 Table 7.6.3-1 p.280] |
| RPS Manual Switches | RPS Division D Manual Switch Panel | NSRST | SCN1 | [PSAR_ch07 Table 7.6.3-1 p.280] |
| Remote Shutdown SVDUs | RPS Remote Shutdown SVDU A | NSRST | SCN1 | [PSAR_ch07 Table 7.6.3-1 p.280] |
| Remote Shutdown SVDUs | RPS Remote Shutdown SVDU B | NSRST | SCN1 | [PSAR_ch07 Table 7.6.3-1 p.280] |
| Reactor Trip Breakers | RTB Enclosure Panel A1 | SR | SCS1 | [PSAR_ch07 Table 7.6.3-1 p.280] |
| Reactor Trip Breakers | RTB Enclosure Panel A2 | SR | SCS1 | [PSAR_ch07 Table 7.6.3-1 p.280] |
| Reactor Trip Breakers | RTB Enclosure Panel B1 | SR | SCS1 | [PSAR_ch07 Table 7.6.3-1 p.280] |
| Reactor Trip Breakers | RTB Enclosure Panel B2 | SR | SCS1 | [PSAR_ch07 Table 7.6.3-1 p.280] |
| Reactor Trip Breakers | RTB Enclosure Panel C1 | SR | SCS1 | [PSAR_ch07 Table 7.6.3-1 p.280] |
| Reactor Trip Breakers | RTB Enclosure Panel C2 | SR | SCS1 | [PSAR_ch07 Table 7.6.3-1 p.280] |
| Reactor Trip Breakers | RTB Enclosure Panel D1 | SR | SCS1 | [PSAR_ch07 Table 7.6.3-1 p.280] |
| Reactor Trip Breakers | RTB Enclosure Panel D2 | SR | SCS1 | [PSAR_ch07 Table 7.6.3-1 p.280] |

- "DL4-RR8 — Manual SPS Pump Trip on Leak Indication" [PSAR_ch05 DL4-RR8 p.20]
- "LCOs in this section will ensure RPS, XIS, and RIS can perform the following functions during the modes of applicability:; • reactor scram; • PSP trip; • Intermediate Sodium Pump trip" [PSAR_ch11 Table 11.5-1 p.67]

## 해설
Reactor Protection System(`RPS`)은 발전소 계측의 입력 신호를 받아 논리를 적용하고, reactor scram과 engineered safety feature(`ESF`) 작동을 포함한 안전 기능 개시 신호를 자동으로 만든다. 안전 기능을 지원하는 부분은 네 이중화 division(A, B, C, D)으로 배열되고, 각 division의 입력은 안전 기능 전용 전자 장치인 `safety function chassis`가 받는다. Main Control Room에서 각 scram·`ESF` 작동을 수동 개시할 수 있으나 이 수동 기능은 안전해석에서 credit되지 않으며, 수동 회로는 자동 논리와 diverse하다. `RPS`는 `SVDU`로 `IEEE 497-2016`의 Type B, C, F `PAM` 변수를 표시하고, 안전 기능 입력이 아닌 `PAM` 변수는 Division A와 B의 별도 `PAM-only chassis`가 처리한다. 이 chassis는 기능적으로 분리되고 같은 종류의 safety-grade 구성품으로 이루어지며 단순화를 위해 SR%%t:SR%% 보호 계통의 일부로 취급되고, 두 개를 두어 Type B·C 변수의 single failure 기준을 만족한다. `RG 1.97, Revision 5`가 승인한 `IEEE 497-2016` 부합 설명은 OL%%t:OL%% 단계에서 제공된다.

구조는 `NAT-4950-A`에 기술되고 `RPS`에는 `RadICS` Topical Report의 `RadICS` platform이 쓰인다. Safety Evaluation for Topical Report `2016-RPC003-TR-001`의 generic open item과 plant-specific action item은 OL%%t:OL%% 단계에서 제공된다. setpoint는 `RG 1.105, Revision 4`가 승인한 `ANSI/ISA Standard 67.04.01-2018` 방법론으로 정하며, setpoint control program은 `Table 11.5-1` Section 2.0에 있다. programmatic special treatment는 Design Reliability Assurance Program, Equipment Qualification Program, Post-construction inspection, testing, and analysis program, Quality Assurance Program Description, Human Factors Engineering Program Plan이다. `RadICS` platform 장비에는 Topical Report의 규격·지침이 적용되고, application-specific 요소는 그와 충돌하지 않는 범위에서 더 새로운 규격을 따른다. regulatory guide%%t:RG%% 부합은 application-specific 요소 기준으로 `RG 1.22`, `RG 1.47`, `RG 1.100`, `RG 1.152`, `RG 1.180` 완전 부합, `RG 1.105`는 `RPS` 전체가 완전 부합(일부는 platform 구성품이 대체 개정판 부합), `RG 1.53`, `RG 1.75`, `RG 1.118`, `RG 1.153`은 더 새로운 `IEEE` 표준 사용으로 부분 부합이다. `RG 1.97, Revision 5`는 `RPS` 혼자 모든 요건을 충족할 수 없어 부분 부합이며 범위는 OL%%t:OL%% 단계에서 제공된다.

기능 표에서 `DL3` 기능은 SR%%t:SR%%, `DL4`와 `DL5` 기능은 NSRST%%t:NSRST%%로 지정된다. `DL3-RC1a`–`DL3-RC1j`는 neutron flux, hot pool·cold pool 온도, primary sodium 수위, power-to-flow ratio, neutron flux rate, 저출력 고 neutron flux, primary sodium 유량 상실에 대한 reactor scram이고 모두 `CRA`를 중력으로 삽입한다. `DL3-RC2`는 전원 상실 시 출력이 안전 상태로 가는 scram이다. `DL3-HR2`, `DL3-HR3`, `DL3-HR12`는 scram 신호가 있고 cold pool 온도나 hot pool 수위가 setpoint를 넘고 neutron flux가 setpoint 아래일 때 `PSP` 또는 `ISP`를 trip하며, `DL3-HR11`은 hot pool 저수위에서 `SPS-P` pump를 trip한다. `DL4-RC1`, `DL4-HR6`, `DL4-HR7`, `DL4-RR8`은 수동 switch 기능이고, `DL4-RC3`은 `RTB` 요구 출력과 독립된 신호로 `CRD driveline scram follow`를 요구하며, `DL4-RC4`는 `AST` 신호로 `RTB`를 연다. `DL5-PAM1`은 Type B, C, F `PAM` 변수 표시이다. 네 수동 기능은 `PRA` 모델만으로는 Non-Safety-Related with No Special Treatment%%t:NST%%이지만 심층방어(Defense-in-Depth)%%t:DID%% 목적과 `IEEE 603-1991`의 수동 개시 요건 때문에 NSRST%%t:NSRST%%로 분류되며, `RPS`에 배정된 NST%%t:NST%% Defense Line%%t:DL%% 기능은 없다.

principal design criteria%%t:PDC%% 2에 따라 SR%%t:SR%% 부분은 SR%%t:SR%% `NCB` 하부구조에 있고 지진 검증을 받으며, `NCB`는 최대 홍수위 위에 있고 기후 제어된다. PDC%%t:PDC%% 3에 따라 각 division은 3-hour 내화 등급 벽과 3-hour 이상 내화 등급 문을 가진 전용 `RPS` vault에 있다. PDC%%t:PDC%% 21과 22에 따라 각 공정 변수는 네 division의 이중화 센서로 측정되고, 네 division 가운데 적어도 2개가 필요하다고 판단하면 작동한다. 이 배열은 운전 중 한 division을 시험에서 빼도 안전 기능과 최소 이중화를 잃지 않게 하고, 한 division이 시험 중이어도 운전 중 division의 단일 고장을 견딘다. PDC%%t:PDC%% 23에 따라 scram 회로는 `RTB` undervoltage coil 전압이 사라지면 `RTB`가 열려 `CRD` 전자밸브 전원이 끊기고 argon이 배기되어 봉이 낙하하는 “de-energize to trip” 설계이고, `ESF` 회로도 relay 전원 상실로 pump breaker가 trip되는 “de-energize to trip”이다. 자기진단이 치명 결함을 찾거나 range-checking이 송신 계통 전원 상실을 찾으면 출력은 안전 상태가 된다. PDC%%t:PDC%% 26에 따라 한 division이 `DL3` scram 요구를 내면 `DL4` driveline scram follow 요구 신호도 내고, `CRD` 계통은 네 division 가운데 2개의 요구로 이를 개시한다.

`IEEE 603-2018`, `IEEE 7-4.3.2-2016`, `IEEE 379-2014`, `IEEE 384-2018`이 `RadICS` platform 밖 application-specific 장비의 special treatment이고, 검증에는 `IEEE/IEC 60780-323-2016`, `IEEE/IEC 60980-344-2020`, `IEEE 420-2013`, `RG 1.180`이 쓰인다. 수리, 신뢰성 평가(action item 7.6), 시험·교정(action item 7.8), maintenance bypass, single failure 영향, system integrity(action item 7.4), operating bypass, 예측 가능·반복 가능 거동, Secure Development and Operational Environment는 OL%%t:OL%% 단계에서 제공된다. 보호 동작은 개시되면 끝까지 진행되고 복귀에는 운전원의 의도적 조치가 필요하다. `Table 7.6.3-1`에서 네 division 캐비닛과 `RTB` enclosure panel은 SR%%t:SR%%·`SCS1`, `SVDU`·수동 switch panel·Remote Shutdown `SVDU`는 NSRST%%t:NSRST%%·`SCN1`, `RPS Data Gateway Cabinet`은 NST%%t:NST%%·지진 분류 `None`이다.

`PSAR` Chapter 5 레코드 `DL4-RR8`은 이 기능을 `Manual SPS Pump Trip on Leak Indication`으로 적어 이 절의 `Manual SPS pump trip on low primary sodium level`과 이름이 다르다. `PSAR` Chapter 11 `Table 11.5-1`의 계측 `LCO` 행은 `RPS`, `XIS`, `RIS` 기능으로 reactor scram, `PSP` trip, `Intermediate Sodium Pump` trip만 적어 SR%%t:SR%% 기능 `DL3-HR11`의 `SPS` pump trip이 없다.

## 관련 문서
- [[Natrium_System_IC_Architecture]]
- [[Natrium_SR_Functions_Heat_Generation]]
- [[Natrium_SR_Functions_Heat_Removal]]
- [[Natrium_NSRST_Functions]]
- [[Natrium_Technical_Specifications_Scope]]
- [[Natrium_Seismic_Classification]]
- [[Natrium_System_Nuclear_Instrumentation]]
- [[Natrium_System_Reactor_Instrumentation]]
- [[Natrium_System_Anticipatory_Seismic_Trip]]
- [[Natrium_System_Control_Room_Indications]]
- [[PSAR_ch07]]
