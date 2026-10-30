---
type: natrium
aliases: []
sources:
- PSAR_ch07
- PSAR_ch01
- SER_KU1_CP
status: checked
verified: 2026-10-30
term: null
tags:
- natrium
- psar-ch7
terms_pending: []
---

# Natrium Nuclear Island Control System (NIC)

> [!abstract] 요약
> Nuclear Island Control System(`NIC`)은 대부분이 Distributed Control System(`DCS`) 위에 구현된 `I&C` 하위 계통의 모음으로, 계통 전체는 분류되지 않고 하위 계통마다 분류된다. `AMC`, `CTC`, `UMC`가 Non-Safety-Related with Special Treatment%%t:NSRST%% 기능(`DL2-HR2`, `DL4-HR2`, `DL4-HR3`, `DL4-RR1c`, `DL4-RR3a`–`c`, `DL4-RR4a`–`c`)을 지원하며, `RPS`에서 `NIC`로는 data diode나 hardwired 연결로 단방향 통신만 한다.

## 원문 사실
- "The Nuclear Island Control System (NIC) is a digital system with non-safety-related with special treatment (NSRST) and non-safety-related with no special treatment (NST) functions and is a group of instrumentation and control (I&C) subsystems." [PSAR_ch07 §7.6.2.1 p.251]
- "The NIC is implemented on a Nuclear Island Distributed Control System (DCS) which provides a means for gathering information from various sources, such as field sensors, human-system Interface (HSI), and data feeds from other I&C systems." [PSAR_ch07 §7.6.2.1 p.251]
- "The DCS also interfaces with various field actuators such that it can execute both manual and automatic logic based on the gathered information." [PSAR_ch07 §7.6.2.1 p.251]
- "While most of the NIC is implemented on a DCS, it also includes controls that are executed outside of the DCS." [PSAR_ch07 §7.6.2.1 p.251]
- "These are referred to as “vendor supplied” control systems." [PSAR_ch07 §7.6.2.1 p.251]
- "Vendor supplied control systems include interfaces for communication with the DCS." [PSAR_ch07 §7.6.2.1 p.251]
- "Auxiliary Monitoring and Control System (AMC) – The AMC monitors and controls Nuclear Island (NI) auxiliary systems." [PSAR_ch07 §7.6.2.1 p.251]
- "Fuel Handling Supervisory Control System (FHC) – The FHC monitors and controls the sub-systems and sub-components of the fuel handling systems (Section 7.3)." [PSAR_ch07 §7.6.2.1 p.251]
- "Plant Monitoring and Control System (PMC) – The PMC includes plant information processing and display devices, storage devices, and operator manual command devices which are used to execute plant wide monitoring and operating functions." [PSAR_ch07 §7.6.2.1 p.251]
- "Coolant Temperature Monitoring and Control System (CTC) – The CTC monitors and controls" [PSAR_ch07 §7.6.2.1 p.251]
- "Rod Monitoring and Control System (RMC) – The RMC monitors and controls the sub-systems and sub-components of the control rod drive (CRD) (Section 7.2.5)." [PSAR_ch07 §7.6.2.1 p.251]
- "Utility Monitoring and Control System (UMC) – The UMC monitors and controls the various auxiliary electrical and ancillary systems." [PSAR_ch07 §7.6.2.1 p.252]
- "NIC cabinets and components are located in the Main Control Room and Computer Room within the Nuclear Island Control Building (NCB)." [PSAR_ch07 §7.6.2.1.2 p.253]
- "The IO modules are located near the modular electric rooms as well as distributed throughout the NI for greater flexibility in the placement of sensors and actuators." [PSAR_ch07 §7.6.2.1.2 p.253]
- "HSIs and VDUs are located within the Main Control Room and Fuel Handling Control Room; with local HSIs and VDUs available in selected areas of the NI." [PSAR_ch07 §7.6.2.1.2 p.253]
- "Safety classification and associated NSRST functions are specific to each NIC sub-system and NIC component." [PSAR_ch07 §7.6.2.2 p.253]
- "The NIC as a whole is not classified." [PSAR_ch07 §7.6.2.2 p.253]
- "The process for classifying NIC sub-systems and components is described in Section 7.6.1.1.2." [PSAR_ch07 §7.6.2.2 p.253]
- "The NIC plant data highway, HSI bus, DCS infrastructure, HSIs, and VDUs are NST components." [PSAR_ch07 §7.6.2.2 p.253]
- "NSRST functions do not rely on these NST components." [PSAR_ch07 §7.6.2.2 p.253]
- "There are two types of sub-systems for the NIC: sub-systems with both NST and NSRST functions, and sub-systems with only NST functions." [PSAR_ch07 §7.6.2.2 p.253]
- "The devices with NSRST and NST functions use similar hardware and software, however devices with NSRST functions have special treatments applied." [PSAR_ch07 §7.6.2.2 p.253]
- "For sub-systems that only support NST functions, the equipment within the controller cabinets and remote IO cabinets are NST and no special treatments are applied." [PSAR_ch07 §7.6.2.2 p.253]
- "For sub-systems that support both NSRST and NST functions, the controllers, power supplies, and backplane and IO network are NSRST." [PSAR_ch07 §7.6.2.2 p.253]
- "The IO modules are a mix of both NST and NSRST, where the NSRST IO modules are used to support both NST and NSRST functions and the NST IO modules are limited to only supporting NST functions." [PSAR_ch07 §7.6.2.2 p.253]
- "The hardware devices used for NST and NSRST IO modules are the same." [PSAR_ch07 §7.6.2.2 p.253]
- "The NIC conforms to RGs as follows:" [PSAR_ch07 §7.6.2.2 p.253]
- "RG 1.75, Revision 3, Physical Independence of Electric Systems" [PSAR_ch07 §7.6.2.2 p.253]
- "NIC sub-systems that are classified as NSRST partially conform to RG 1.75 Revision 3." [PSAR_ch07 §7.6.2.2 p.253]
- "Conformance is partial because IEEE 384-2018, “IEEE Standard Criteria for Independence of Class 1E Equipment and Circuits,” IEEE 384-2018 (Reference 7.6.2-1) is used rather than the version of the standard endorsed by this RG." [PSAR_ch07 §7.6.2.2 p.253]
- "RG 1.89, Revision 2, Environmental Qualification of Certain Electric Equipment Important to Safety For Nuclear Power Plants" [PSAR_ch07 §7.6.2.2 p.254]
- "NIC sub-systems that are classified as NSRST fully conform to RG 1.89, Revision 2." [PSAR_ch07 §7.6.2.2 p.254]
- "RG 1.100, Revision 4, Seismic Qualification and Mechanical Equipment for Nuclear Power Plants" [PSAR_ch07 §7.6.2.2 p.254]
- "NIC sub-systems that are classified as NSRST fully conform to RG 1.100, Revision 4." [PSAR_ch07 §7.6.2.2 p.254]
- "RG 1.180, Revision 2, Guidelines for Evaluating Electromagnetic and Radio-Frequency Interference in Safety-Related Instrumentation and Control Systems" [PSAR_ch07 §7.6.2.2 p.254]
- "NIC sub-systems that are classified as NSRST fully conform to RG 1.180, Revision 4." [PSAR_ch07 §7.6.2.2 p.254]
- "RG 1.204, Revision 1, Guidelines for Lightning Protection for Production and Utilization Facilities" [PSAR_ch07 §7.6.2.2 p.254]
- "NIC sub-systems that are classified as NSRST fully conform to RG 1.204, Revision 1." [PSAR_ch07 §7.6.2.2 p.254]
- "PRA safety functions (PSFs) are determined through the plant-specific PRA described in Section 3.1." [PSAR_ch07 §7.6.2.2.1 p.254]
- "The safety-significant PSFs are identified as safety-related (SR) functions or NSRST functions as defined in Section 5.2." [PSAR_ch07 §7.6.2.2.1 p.254]
- "The NIC supports the following safety-significant functions, which are designated as NSRST to indicate the safety classification of NIC components relied upon to perform the function:" [PSAR_ch07 §7.6.2.2.1 p.254]
- "The AMC is a digital NIC sub-system with allocated plant functions supporting DL2, DL4, and DL5, including the following DL4 NSRST functions:" [PSAR_ch07 §7.6.2.2.1 p.254]
- "RMS components that are classified as NSRST fully conform to RG 1.180, Revision 4." [PSAR_ch07 §7.6.6.2 p.307]
- "RG 1.180, Rev. 2." [SER_KU1_CP §7.6.6 p.576]
- "In addition to the regulations and guidance provided at the beginning of this chapter, the staff used the following guidance in its evaluation of the NIC:" [SER_KU1_CP §7.6.2 p.546]
- "RG 1.180, “Guidelines for Evaluating Electromagnetic and Radio-Frequency Interference in Safety-Related Instrumentation and Control Systems,” Rev. 2 (ML19175A044);" [SER_KU1_CP §7.6.2 p.547]
- "CTC Coolant temperature monitoring and control system" [SER_KU1_CP Abbreviations and Acronyms p.11]

| Function ID | Function Description | AMC Functional Support | 출처 |
|---|---|---|---|
| DL4-RR3a | SPS supply valve isolation on leak detection | AMC receives sodium leak detection signals from the NFP and provides a signal to close the SPS-P pump supply side isolation valve on the detection of a sodium leak. | [PSAR_ch07 §7.6.2.2.1 p.254] |
| DL4-RR3b | SPS pump trip on leak Detection | AMC receives sodium leak detection signals from the NFP and provides a signal to trip the SPS-P pump on the detection of a sodium leak. | [PSAR_ch07 §7.6.2.2.1 p.254] |
| DL4-RR4a | Automatically close SCG isolation valves on leak detection | AMC receives radioactivity indication signals from the RMS, compares them to a setpoint, and provides a signal to close the SCG reactor vessel exhaust isolation valves that are downstream of the vapor cell. | [PSAR_ch07 §7.6.2.2.1 p.254] |

- "The CTC is a digital NIC sub-system with allocated plant functions supporting DL2, DL4, and DL5, including the following DL2 and DL4 NSRST functions:" [PSAR_ch07 §7.6.2.2.1 p.255]

| Function ID | Function Description | CTC Functional Support | 출처 |
|---|---|---|---|
| DL2-HR2 | Intermediate sodium pump (ISP) trip on low IHT level | CTC receives IHT expansion tank level signals from the IHT and provides a signal to trip the ISPs if a low level setpoint is reached. | [PSAR_ch07 §7.6.2.2.1 p.255] |
| DL4-HR2 | Primary sodium pump (PSP) trip automatic backup | CTC receives primary sodium hot pool temperature signals from the Reactor Instrumentation System (RIS) and provides a signal to trip the PSPs if the high-high primary sodium temperature is exceeded. | [PSAR_ch07 §7.6.2.2.1 p.255] |
| DL4-HR3 | ISP pump trip automatic Backup | CTC receives primary sodium hot pool temperature signals from the RIS and provides a signal to trip the ISPs if the high-high primary sodium temperature is exceeded. | [PSAR_ch07 §7.6.2.2.1 p.255] |

- "The FHC is a digital NIC sub-system with no allocated DL functions and does not provide any SR or NSRST functions, only NST functions." [PSAR_ch07 §7.6.2.2.1 p.255]
- "The PMC is a digital NIC sub-system with allocated plant functions supporting DL2, DL4, and DL5 and does not provide any SR or NSRST functions, only NST functions." [PSAR_ch07 §7.6.2.2.1 p.255]
- "The RMC is a digital NIC sub-system with allocated plant functions supporting DL2, DL4, and DL5 and does not provide any SR or NSRST functions, only NST functions." [PSAR_ch07 §7.6.2.2.1 p.255]
- "The UMC is a digital NIC sub-system with allocated plant functions supporting DL2, DL4, and DL5, including the following DL4 NSRST functions:" [PSAR_ch07 §7.6.2.2.1 p.255]

| Function ID | Function Description | UMC Functional Support | 출처 |
|---|---|---|---|
| DL4-RR1c | Head Access Area (HAA) HVAC operations following postulated release | The UMC receives radioactivity indication signals from the RMS and sends signals to the NHV to close the HAA isolation valves if a setpoint is exceeded. | [PSAR_ch07 §7.6.2.2.1 p.255] |
| DL4-RR3c | SPS cells barrier isolation leak detection | The UMC receives sodium leak detection signals from the NFP and sends signals to close dampers in the NHV to isolate ventilation to the SPS-P cells. | [PSAR_ch07 §7.6.2.2.1 p.255] |
| DL4-RR4b | SCG cells barrier isolation leak detection | The UMC receives radioactivity indication signals from the RMS and sends signals to close valves to isolate the SCG vapor trap cells if a setpoint is exceeded. | [PSAR_ch07 §7.6.2.2.1 p.255] |
| DL4-RR4c | Vapor trap cell isolation on overpressure | The UMC receives poistion indication signals for the reactor vessel relief valves and sends a signal to close valves to isolate the SCG vapor trap cells if a relief valve is open. | [PSAR_ch07 §7.6.2.2.1 p.255] |

- "Consistent with PDC 2, Design bases for protection against natural phenomena, the NSRST NIC SSCs are located either in the SR RXB or NCB substructures or the NSRST NCB superstructure, which is designed to withstand the effects of applicable external hazards without the loss of structural integrity." [PSAR_ch07 §7.6.2.2.2 p.256]
- "In this way, the design of the NIC ensures that the NSRST functions will be performed in the event of an earthquake, external flooding, high winds, and external climate." [PSAR_ch07 §7.6.2.2.2 p.256]
- "Consistent with PDC 10, Reactor design, the NIC functions to support reactivity control and decay heat removal during all normal, anticipated operational occurrence (AOO), and postulated accident conditions." [PSAR_ch07 §7.6.2.2.2 p.256]
- "The NIC subsystems, CTC (classified NSRST), RMC (classified NST), and PMC (classified NST), are designed and operated with appropriate controls and setpoint margins to ensure reactor limits are not exceeded during all normal, AOO, and postulated accident conditions" [PSAR_ch07 §7.6.2.2.2 p.256]
- "Consistent with PDC 13, Instrumentation and control, the NIC provides the capability to reliably monitor and control the plant systems during normal power operations, plant startup and shutdown, including steady state and anticipated plant transients." [PSAR_ch07 §7.6.2.2.2 p.256]
- "Appropriate controls are provided to maintain associated variables and systems within prescribed operating ranges." [PSAR_ch07 §7.6.2.2.2 p.256]
- "The backbone of NIC is implemented on a DCS which provides a means for monitoring and gathering information from various sources, such as field sensors, HSI, and data feeds from other I&C components." [PSAR_ch07 §7.6.2.2.2 p.256]
- "This information is used by DCS to monitor plant variables and execute both manual and automatic control of plant systems to maintain these variables and systems within prescribed operating ranges." [PSAR_ch07 §7.6.2.2.2 p.256]
- "Consistent with PDC 15, Primary coolant system design, the NIC functions to support reactivity control and decay heat removal during all normal, AOO, and postulated accident conditions." [PSAR_ch07 §7.6.2.2.2 p.256]
- "The NIC subsystems, CTC (classified NSRST), RMC (classified NST), and PMC (classified NST), are designed and operated with appropriate controls and setpoint margins to ensure primary coolant limits are not exceeded during all normal, AOO, and postulated accident conditions." [PSAR_ch07 §7.6.2.2.2 p.256]
- "Consistent with PDC 24, Separation of protection and control systems, the RPS is separated from the NIC NSRST and NST control systems to the extent that failure of any single control system component or channel, or failure or removal from service of any single protection system component or channel which is common to the control and protection systems, leaves intact a system satisfying all reliability, redundancy, and independence requirements of RPS, as required by Clause 5.6 of IEEE 603-2018, “IEEE Standard Criteria for Safety Systems for Nuclear Power Generating Stations” (Reference 7.6.2-2)." [PSAR_ch07 §7.6.2.2.2 p.256]
- "There is no direct communication from NIC systems to the RPS." [PSAR_ch07 §7.6.2.2.2 p.257]
- "The RPS is isolated and functionally independent of NSRST and NST control systems and uses input signals from independent instrument channels." [PSAR_ch07 §7.6.2.2.2 p.257]
- "One-way communication from RPS to NSRST and NST control systems is via a data diode or hardwired connection." [PSAR_ch07 §7.6.2.2.2 p.257]
- "Consistent with PDC 25, Protection system requirements for reactivity control malfunctions, the NIC provides reactivity control during normal operations and during AOOs through power runback performed by RMC and CTC." [PSAR_ch07 §7.6.2.2.2 p.257]
- "Consistent with PDC 26, Reactivity control systems, the NIC functions to support reactivity control and decay heat removal during all normal, AOO, and postulated accident conditions." [PSAR_ch07 §7.6.2.2.2 p.257]
- "The NIC subsystems, CTC (classified NSRST), RMC (classified NST), and PMC (classified NST), are designed and operated with appropriate controls and setpoint margins to ensure reactivity limits are not exceeded during all normal, AOO, and postulated accident conditions." [PSAR_ch07 §7.6.2.2.2 p.257]
- "Consistent with PDC 28, Reactivity Limits, the RMC and Control Rod Drive System control the maximum rod withdrawal speed to limit the nuclear reactivity worth insertion rate." [PSAR_ch07 §7.6.2.2.2 p.257]
- "A Control Rod Drive System control interlock prevents withdrawal of more than one rod at a time." [PSAR_ch07 §7.6.2.2.2 p.257]
- "The Control Rod Drive System also includes a brake to hold the control rod assembly at any selected position within the stroke of travel and prevents it from inadvertent insertion or withdrawal during any non-accident, accident, post-accident, and seismic conditions." [PSAR_ch07 §7.6.2.2.2 p.257]
- "Consistent with PDC 29, Protection against anticipated operational occurrences, the NIC functions to support reactivity control and decay heat removal during all normal, AOO, and postulated accident conditions." [PSAR_ch07 §7.6.2.2.2 p.257]
- "The NIC subsystems, CTC (classified NSRST), RMC (classified NST), and PMC (classified NST), are designed and operated with appropriate controls and setpoint margins to ensure reactivity limits are not exceeded during all normal, AOO, and postulated accident conditions." [PSAR_ch07 §7.6.2.2.2 p.257]
- "Consistent with PDC 60, Control of releases of radioactive materials to the environment, the NIC subsystems, AMC (classified NSRST) and PMC (classified NST), are designed and operated with appropriate controls and setpoint margins to support control of releases of radioactive material to the environment during all normal, AOO, and postulated accident conditions." [PSAR_ch07 §7.6.2.2.2 p.257]
- "Consistent with PDC 61, Fuel storage and handling and radioactivity control, the NIC functions to support control of releases of radioactive material to the environment during all normal, AOO, and postulated accident conditions." [PSAR_ch07 §7.6.2.2.2 p.257]
- "FHC provides interlocks and remote control of the In-Vessel Fuel Handling System equipment and sub-systems during normal operation." [PSAR_ch07 §7.6.2.2.2 p.257]
- "The interlocks prevent inadvertent operation of equipment and damage to system components and interfacing systems." [PSAR_ch07 §7.6.2.2.2 p.257]
- "In the event of control system malfunctions, manual controls provide redundancy." [PSAR_ch07 §7.6.2.2.2 p.257]
- "The NIC subsystems, FHC (classified NST) and PMC (classified NST), are designed and operated with appropriate controls and setpoint margins to ensure residual heat removal capability." [PSAR_ch07 §7.6.2.2.2 p.257]
- "Consistent with PDC 63, Monitoring fuel and waste storage, the NIC subsystems, FHC (classified NST) and PMC (classified NST), are designed and operated with appropriate controls and setpoint margins to detect conditions that may result in loss of residual heat removal capability." [PSAR_ch07 §7.6.2.2.2 p.258]
- "Consistent with PDC 64, Monitoring radioactivity releases, the NIC subsystems, AMC (classified NSRST), RMC (classified NST), and PMC (classified NST), are designed and operated with appropriate controls and setpoint margins to monitor the plant for radioactivity released from normal operations including AOO, and from postulated accidents." [PSAR_ch07 §7.6.2.2.2 p.258]
- "The Radiation Monitoring System and PMC monitor for radiological release through the exhaust air in the vent stack." [PSAR_ch07 §7.6.2.2.2 p.258]
- "Consistent with PDC 72, Sodium heating systems, the NIC subsystems, RMC (classified NST), CTC (classified NSRST), and PMC (classified NST), are designed and operated with appropriate controls and setpoint margins to ensure that the temperature distribution and rate of change of temperature in systems and components containing sodium are maintained within design limits." [PSAR_ch07 §7.6.2.2.2 p.258]
- "The NIC controllers have the capability of being redundant to mitigate single system hardware failures." [PSAR_ch07 §7.6.2.2.2 p.258]
- "The NIC subsystems perform both NSRST and NST functions." [PSAR_ch07 §7.6.2.3 p.258]
- "When required to meet quality, design, reliability, and performance requirements, special treatments are applied to all NIC NSRST SSCs and also to NIC NST SSCs, as needed." [PSAR_ch07 §7.6.2.3 p.258]
- "Special treatments are initially selected based on SSC safety classification as described in Section 6.3." [PSAR_ch07 §7.6.2.3 p.258]
- "The following programmatic special treatments are preliminarily identified as applicable to the NSRST NIC subsystems (AMC, CTC, and UMC):" [PSAR_ch07 §7.6.2.3 p.258]
- "Design Reliability Assurance Program, as described in Table 8.0-1" [PSAR_ch07 §7.6.2.3 p.258]
- "Equipment Qualification Program, as described in Table 8.0-1" [PSAR_ch07 §7.6.2.3 p.258]
- "Quality Assurance Program Description, as described in Section 8.1" [PSAR_ch07 §7.6.2.3 p.258]
- "Post-construction Inspection, Testing, and Analysis Program, as described in Chapter 12" [PSAR_ch07 §7.6.2.3 p.258]
- "Additionally, the Human Factors Engineering Program Plan, described in Section 11.2, is identified as a programmatic special treatment applicable to the NIC DCS and all NIC subsystems." [PSAR_ch07 §7.6.2.3 p.258]
- "Seismic classifications for NIC subsystem (AMC, CTC, and UMC) components are determined in accordance with the methods described in Section 6.4.1." [PSAR_ch07 §7.6.2.3 p.258]
- "Seismic special treatment is applied based on the seismic classification." [PSAR_ch07 §7.6.2.3 p.258]
- "The seismic classification of NIC subsystem (AMC, CTC, and UMC) components are SCN3." [PSAR_ch07 §7.6.2.3 p.258]
- "Seismic design, analysis, and qualification is performed as described in Section 6.4." [PSAR_ch07 §7.6.2.3 p.258]
- "NIC design includes elements of quality that minimize failures in the NSRST functions." [PSAR_ch07 §7.6.2.3 p.258]
- "These properties of qualification, reliability, robustness, security, and defense-in-depth features are discussed in Section 7.6.2.3.1 through Section 7.6.2.3.5." [PSAR_ch07 §7.6.2.3 p.258]
- "The NIC meets the quality standards established in the Quality Assurance Program Description." [PSAR_ch07 §7.6.2.3.1 p.259]
- "No part of the NIC or its sub-systems is required to operate during or after a seismic event." [PSAR_ch07 §7.6.2.3.1 p.259]
- "NIC equipment is mounted in cabinets using standard industrial practices to ensure that the equipment is sufficiently supported." [PSAR_ch07 §7.6.2.3.1 p.259]
- "If NIC equipment is installed near equipment that is required to operate during or following a seismic event, the NIC equipment is designed to ensure that it will not fail in a way that would prevent another SSC from performing its safety-significant function." [PSAR_ch07 §7.6.2.3.1 p.259]
- "This is done by using robust cabinets with adequate anchoring to ensure that any NIC equipment failures only affect devices within the cabinets and do not affect any external components." [PSAR_ch07 §7.6.2.3.1 p.259]
- "The seismic design of the NIC and its subsystems is described in Section 6.4.1." [PSAR_ch07 §7.6.2.3.1 p.259]
- "The Equipment Qualification Program described in Table 8.0-1 addresses the requirements, standards, and process for qualifying the NIC system equipment." [PSAR_ch07 §7.6.2.3.1 p.259]
- "The NIC is used by operators to determine the status of the plant and to operate NST and NSRST devices." [PSAR_ch07 §7.6.2.3.2 p.259]
- "Some NIC functions require higher levels of reliability." [PSAR_ch07 §7.6.2.3.2 p.259]
- "Achieving an acceptable level of reliability ensures that the system performs its functions when required." [PSAR_ch07 §7.6.2.3.2 p.259]
- "In addition to the elements discussed in Section 7.6.2.3.1, redundancy contributes to the reliability and availability achieved within the NIC." [PSAR_ch07 §7.6.2.3.2 p.259]
- "The NIC includes provisions for redundancy to increase system reliability for NSRST functions." [PSAR_ch07 §7.6.2.3.2 p.259]
- "Controllers and IO modules have the capability of being implemented with various levels of redundancy." [PSAR_ch07 §7.6.2.3.2 p.259]
- "With a redundant IO module and controller, the only common failure point is the physical termination of the field device." [PSAR_ch07 §7.6.2.3.2 p.259]
- "Except for the physical connection between the termination point and the IO modules, no single failures of any component within the NIC can cause a failure." [PSAR_ch07 §7.6.2.3.2 p.259]
- "The HSI bus and plant data highway is implemented using redundant equipment such that no single failure in a device on those networks will cause a failure of the network." [PSAR_ch07 §7.6.2.3.2 p.259]
- "Multiple HSIs and VDUs are provided in various locations in the facility (i.e., in the Main Control Room and Remote Shutdown Complex) such that a complete failure of one of these devices does not affect the ability of operators to access information or perform operations." [PSAR_ch07 §7.6.2.3.2 p.259]
- "Additionally, the DCS includes application and database servers that perform different functions." [PSAR_ch07 §7.6.2.3.2 p.259]
- "These servers are also redundant such that a failure in one device does not result in a failure of the DCS." [PSAR_ch07 §7.6.2.3.2 p.259]
- "Connections between the VDUs, HSIs, and servers and the HSI bus and plant data highway are redundant." [PSAR_ch07 §7.6.2.3.2 p.259]
- "NIC controller and remote IO cabinets contain redundant power supplies powered from separate sources such that a failure in a power supply, or in one of the power feeds, does not impact any NIC functions." [PSAR_ch07 §7.6.2.3.2 p.259]
- "When necessary, equipment with dual redundant power supplies is selected such that the loss of a single power supply or power feed will not result in a loss of functionality." [PSAR_ch07 §7.6.2.3.2 p.259]
- "The method for confirming specific reliability and capability targets for SSCs at the operating license stage is described in Section 6.2." [PSAR_ch07 §7.6.2.3.2 p.260]
- "An important element of the I&C robustness is separation from other I&C systems and isolation of signals from the field and other systems." [PSAR_ch07 §7.6.2.3.3 p.260]
- "The NIC includes a data interface between the RPS and the NIC." [PSAR_ch07 §7.6.2.3.3 p.260]
- "For this interface, the RPS sends data via a one-way data diode to the plant data highway via an RPS-NIC gateway." [PSAR_ch07 §7.6.2.3.3 p.260]
- "This gateway is used to perform data conversion into a format that is received by the NIC and ensures separation of the NIC from the RPS." [PSAR_ch07 §7.6.2.3.3 p.260]
- "The NIC also includes hardwired interfaces between the RPS and NIC." [PSAR_ch07 §7.6.2.3.3 p.260]
- "For these signals, an isolation device is provided to ensure that the NIC does not have an adverse impact on the RPS." [PSAR_ch07 §7.6.2.3.3 p.260]
- "Security for I&C systems is addressed through the physical security and cyber security programs that are described in Section 11.6." [PSAR_ch07 §7.6.2.3.4 p.260]
- "Some plant parameters are monitored by both the SR, and the NSRST and NST portions of the I&C systems." [PSAR_ch07 §7.6.2.3.5 p.260]
- "When diversity between the SR and NSRST or NST functions is required, redundant sensors are utilized where one sensor provides a signal to the SR I&C system and another sensor is used to provide a signal to the NSRST or NST I&C system." [PSAR_ch07 §7.6.2.3.5 p.260]
- "In cases where a SR sensor is shared between SR and NSRST or NST I&C systems, the sensor information is routed through a signal splitter which then sends information to the SR I&C systems, as well as the NST or NSRST I&C system." [PSAR_ch07 §7.6.2.3.5 p.260]
- "This signal splitter provides isolation so that the NSRST and NST side of the splitter cannot have an adverse impact on the SR side of the splitter." [PSAR_ch07 §7.6.2.3.5 p.260]
- "The plant data highway, HSI bus, HSIs, VDUs, and other DCS servers are classified as NST." [PSAR_ch07 §7.6.2.4 p.260]
- "Display and control functions on the NIC are NST functions and the HSIs are used to perform those functions." [PSAR_ch07 §7.6.2.4 p.260]
- "For those instances where the display of information is an NSRST function, a separate NSRST display device is provided." [PSAR_ch07 §7.6.2.4 p.260]
- "These NSRST display devices are placed within a loop that also includes a NIC IO module such that the information is acquired by both the NSRST display device and the IO module." [PSAR_ch07 §7.6.2.4 p.260]
- "This allows for this data to be displayed both on the NSRST display device as well as on an HSI." [PSAR_ch07 §7.6.2.4 p.260]
- "For those instances where the manual control of a device is an NSRST function, the NSRST manual actuation is performed using a hardwired switch." [PSAR_ch07 §7.6.2.4 p.260]
- "For functions where an NSRST hardwired switch is provided for manual actuation of a function, operators can also perform a manual actuation from an Main Control Room HSI, although this is an NST function." [PSAR_ch07 §7.6.2.4 p.260]
- "The NIC performs data-acquisition and display of Post-Accident Monitoring (PAM) for Type D and E variables as defined in IEEE 497-2016, “IEEE Standard Criteria for Accident Monitoring Instrumentation for Nuclear Power Generating Stations” (Reference 7.6.2-3)." [PSAR_ch07 §7.6.2.4 p.261]
- "The credited display of all other PAM variable types is outside of the scope of the NIC; however, PAM variables from the RPS are sent to the NIC so that all PAM variables are displayed on the NIC." [PSAR_ch07 §7.6.2.4 p.261]
- "The Safety Parameter Display System screens are used to consolidate safety parameters and PAM variables into a single device that is used to determine the status of the plant." [PSAR_ch07 §7.6.2.4 p.261]
- "The Safety Parameter Display System is a set of screens that are available from the NIC HSIs and is not a stand-alone system." [PSAR_ch07 §7.6.2.4 p.261]
- "the Coolant Temperature Monitoring and Control System (CTC)" [PSAR_ch01 §1.1.4.1.15 p.26]
- "Nuclear Island Coolant Temperature Control System | NSRST | DL2, DL4, DL5" [PSAR_ch07 Table 7.6.1-1 p.250]

- "Figure 7.6.2-1 Nuclear Island Control System Block Diagram" [PSAR_ch07 Figure 7.6.2-1 p.262]

![[PSAR_ch07_Fig_7.6.2-1.png]]

## 해설
Nuclear Island Control System(`NIC`)은 NSRST%%t:NSRST%% 기능과 Non-Safety-Related with No Special Treatment%%t:NST%% 기능을 가진 디지털 계통이며 `I&C` 하위 계통의 모음이다. `NIC`는 Nuclear Island Distributed Control System(`DCS`)에 구현되어 현장 센서, human-system interface(`HSI`), 다른 `I&C` 계통 자료를 모으고 현장 구동기와 연결되어 수동·자동 논리를 실행한다. `DCS` 밖에서 실행되는 “vendor supplied” 제어 계통도 포함하며, 이들은 `DCS`와 통신하는 인터페이스를 갖는다. 하위 계통은 `NI` 보조 계통을 감시·제어하는 `AMC`, 핵연료 취급 계통의 `FHC`, 발전소 전반 감시·운전 기능의 `PMC`, control rod drive를 감시·제어하는 `RMC`, 보조 전기·부대 계통의 `UMC`와, `CTC`이다. 캐비닛은 Nuclear Island Control Building(`NCB`)의 Main Control Room과 Computer Room에 있고, `HSI`와 `VDU`는 Main Control Room과 Fuel Handling Control Room에 있다.

`NIC` 전체는 분류되지 않으며 분류와 NSRST%%t:NSRST%% 기능은 하위 계통·구성품마다 정해진다. plant data highway, `HSI` bus, `DCS` infrastructure, `HSI`, `VDU`는 NST%%t:NST%% 구성품이고 NSRST%%t:NSRST%% 기능은 이들에 의존하지 않는다. NST%%t:NST%% 기능만 지원하는 하위 계통은 제어기·원격 `IO` 캐비닛 장비가 NST%%t:NST%%이고 special treatment를 적용하지 않는다. NSRST%%t:NSRST%%와 NST%%t:NST%% 기능을 함께 지원하는 하위 계통은 제어기, 전원, backplane과 `IO network`가 NSRST%%t:NSRST%%이고, `IO module`은 두 분류가 섞이되 하드웨어는 같다. NSRST%%t:NSRST%%로 분류된 `NIC` 하위 계통의 regulatory guide%%t:RG%% 부합은 `RG 1.75, Revision 3` 부분 부합(`IEEE 384-2018` 사용)과 `RG 1.89`, `RG 1.100`, `RG 1.204` 완전 부합이며, `RG 1.180`은 제목이 `Revision 2`인데 부합 문장은 `Revision 4`로 적혀 있다.

PRA Safety Function%%t:PSF%%은 plant-specific `PRA`로 정해지고, safety-significant PSF%%t:PSF%%는 Safety-Related%%t:SR%% 또는 NSRST%%t:NSRST%% 기능으로 식별된다. `AMC`는 `NFP`의 소듐 누설 탐지 신호로 `SPS-P` pump 공급측 격리 밸브를 닫고(`DL4-RR3a`) pump를 trip하며(`DL4-RR3b`), `RMS` 방사능 신호를 setpoint와 비교해 vapor cell 하류의 `SCG` 원자로 용기 배기 격리 밸브를 닫는다(`DL4-RR4a`). `CTC`는 `IHT` expansion tank 저수위에서 `ISP`를 trip하고(`DL2-HR2`), `RIS`의 hot pool high-high 온도에서 `PSP`와 `ISP`를 trip하는 자동 backup을 제공한다(`DL4-HR2`, `DL4-HR3`). `UMC`는 `RMS` 신호로 `HAA` 격리 밸브를 닫고(`DL4-RR1c`), `NFP` 신호로 `SPS-P` cell 환기 damper를 닫으며(`DL4-RR3c`), `RMS` 신호로 `SCG` vapor trap cell 격리 밸브를 닫고(`DL4-RR4b`), 원자로 용기 relief valve가 열리면 vapor trap cell을 격리한다(`DL4-RR4c`). `FHC`, `PMC`, `RMC`는 SR%%t:SR%%·NSRST%%t:NSRST%% 기능 없이 NST%%t:NST%% 기능만 제공한다.

principal design criteria%%t:PDC%% 2에 따라 NSRST%%t:NSRST%% `NIC` Structures, Systems, and Components%%t:SSC%%는 SR%%t:SR%% `RXB` 또는 `NCB` 하부구조나 외부 재해를 견디도록 설계된 NSRST%%t:NSRST%% `NCB` 상부구조에 있다. PDC%%t:PDC%% 10, 15, 26, 29에 대해 원문은 `CTC`(NSRST%%t:NSRST%%), `RMC`(NST%%t:NST%%), `PMC`(NST%%t:NST%%)가 적절한 제어와 `setpoint margin`으로 한계를 넘지 않게 한다고 적는다. PDC%%t:PDC%% 24에 따라 `RPS`는 `NIC` 제어 계통과 분리되고, `NIC`에서 `RPS`로의 직접 통신은 없으며, `RPS`에서 나가는 단방향 통신은 data diode 또는 hardwired 연결이다. PDC%%t:PDC%% 25의 반응도 제어는 `RMC`와 `CTC`의 power runback으로, PDC%%t:PDC%% 28의 반응도 한계는 `RMC`와 Control Rod Drive System의 최대 인출 속도 제어, 한 번에 둘 이상 인출을 막는 interlock, brake로 다룬다. PDC%%t:PDC%% 60, 61, 63, 64, 72에 대해서도 해당 하위 계통과 분류가 명시된다.

`NIC` NSRST%%t:NSRST%% 하위 계통(`AMC`, `CTC`, `UMC`)에는 Design Reliability Assurance Program, Equipment Qualification Program, Quality Assurance Program Description, Post-construction Inspection, Testing, and Analysis Program이 예비로 식별되고, Human Factors Engineering Program Plan은 `DCS`와 모든 하위 계통에 적용된다. 이 세 하위 계통 구성품의 지진 분류는 `SCN3`이며, `NIC`의 어떤 부분도 지진 중이나 뒤에 작동할 필요가 없다. 지진 뒤 작동해야 하는 장비 근처의 `NIC` 장비는 견고한 캐비닛과 고정으로 다른 SSC%%t:SSC%% 기능을 방해하지 않게 한다. 신뢰성을 위해 제어기와 `IO module`은 여러 수준의 이중화로 구현할 수 있고, `HSI` bus와 plant data highway, 서버, 전원은 이중화되며, 여러 `HSI`·`VDU`가 있다. 이중화된 `IO module`과 제어기를 쓰면 field device의 물리 종단만 공통 고장점이다. 견고성은 `RPS`→`NIC` 단방향 data diode와 `RPS-NIC gateway`, hardwired 신호의 격리 장치로, 심층방어(Defense-in-Depth)%%t:DID%%는 SR%%t:SR%%과 NSRST%%t:NSRST%%·NST%%t:NST%% 사이의 이중 센서나 격리 signal splitter로 다룬다.

`NIC`의 표시·제어 기능은 NST%%t:NST%%이고, 정보 표시가 NSRST%%t:NSRST%% 기능이면 별도의 NSRST%%t:NSRST%% 표시 장치를, 수동 제어가 NSRST%%t:NSRST%% 기능이면 hardwired switch를 쓴다. `NIC`는 `IEEE 497-2016`의 Type D·E `PAM` 변수를 수집·표시하고, 다른 종류의 `PAM` 변수는 credit되는 표시가 `NIC` 범위 밖이지만 `RPS`가 보내 모두 `NIC`에 표시된다. Safety Parameter Display System은 `NIC` `HSI`에서 볼 수 있는 화면 모음이며 독립 계통이 아니다.

`PSAR` Chapter 1과 Chapter 7 §7.6.2.1은 이 하위 계통을 `Coolant Temperature Monitoring and Control System (CTC)`로 적는 반면 `Table 7.6.1-1`은 `Nuclear Island Coolant Temperature Control System`으로 적는다.

**규정 대비 메모(C25(d), 신청자 문서 내부 불일치).** `CTC` 이름이 `PSAR` Chapter 1과 Chapter 7 §7.6.2.1에서는 Coolant Temperature Monitoring and Control System, Chapter 7 Table 7.6.1-1에서는 Nuclear Island Coolant Temperature Control System이다. `SER` 약어표는 Chapter 1과 같은 이름을 쓰지만, `SER`에는 이름 차이에 대한 판단이 없고(vault 기준) 판정할 권위 조항도 vault에 없다.

**규정 대비 메모(C26(d), 규정 불일치).** `PSAR`은 `NIC`·`RMS`의 NSRST%%t:NSRST%% 구성품이 RG%%t:RG%% 1.180 Revision 4에 완전 부합한다고 적지만, `SER`은 `NIC`(§7.6.2)와 `RMS`(§7.6.6) 평가 지침으로 RG%%t:RG%% 1.180 Rev. 2를 든다. `PSAR` 같은 절(§7.6.2.2)도 Revision 2를 지침으로 적는다. `SER`에는 이 개정판 차이에 대한 판단이 없다(vault 기준). 이 노트는 `SER`과 같은 절의 문장을 따라 Revision 2를 기준으로 쓴다. Revision 4는 오기로 보이며 차후 확인이 필요하다.

## 관련 문서
- [[Natrium_System_IC_Architecture]]
- [[Natrium_IC_Systems]]
- [[Natrium_NSRST_Functions]]
- [[Natrium_System_Reactor_Protection]]
- [[Natrium_System_Radiation_Monitoring]]
- [[Natrium_System_Control_Room_Indications]]
- [[Natrium_System_NI_Fire_Protection]]
- [[Natrium_System_NI_HVAC]]
- [[PSAR_ch07]]
- [[Natrium_SER_IC_Electrical_Structures_Review]]
- [[Natrium_SER_IC_PDC_Conformance]]
