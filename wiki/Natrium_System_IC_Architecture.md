---
type: natrium
aliases: []
sources:
- PSAR_ch07
status: checked
verified: 2026-09-16
term: null
tags:
- natrium
- psar-ch7
terms_pending: []
---

# Natrium Instrumentation and Control 계통 구조와 분류 (Natrium I&C Systems Architecture)

> [!abstract] 요약
> `PSAR` Chapter 7 §7.6.1은 instrumentation and control(`I&C`) 계통의 설계 기준, 분류, 통신 전략, Post-Accident Monitoring(`PAM`) 범위를 요약하고 세부를 `NAT-4950-A`에 넘긴다. `Table 7.6.1-1`은 `RPS`·Nuclear Instrumentation System·Reactor Instrumentation System을 Safety-Related%%t:SR%%, Anticipatory Automatic Seismic Trip System·Radiation Monitoring System과 `NIC` 하위 계통 셋을 Non-Safety-Related with Special Treatment%%t:NSRST%%로 적고, `NIC` 자체는 분류하지 않는다.

## 원문 사실
- "Instrumentation and control (I&C) systems provide automatic actuation in response to licensing-basis events, contribute to satisfying Principal Design Criteria (PDC), and provide means for manual actuation of components in support of defense-in-depth." [PSAR_ch07 §7.6.1 p.246]
- "The design basis of I&C systems is described in Section 7.6.1.1." [PSAR_ch07 §7.6.1 p.246]
- "The I&C system architecture is described in Section 7.6.1.2." [PSAR_ch07 §7.6.1 p.246]
- "Safety-significant I&C systems are described in Section 7.6.2 through Section 7.6.6 and Section 7.6.8." [PSAR_ch07 §7.6.1 p.246]
- "Control rooms and indications are described in Section 7.6.7." [PSAR_ch07 §7.6.1 p.246]
- "The I&C systems are designed using IEEE 603-2018, “IEEE Standard Criteria for Safety Systems for Nuclear Power Generating Stations,” (Reference 7.6.1-1) as described in Sections 7.6.2 through 7.6.6 and Section 7.6.8." [PSAR_ch07 §7.6.1 p.246]
- "IEEE 603-2018 provides an equivalent or greater level of safety as IEEE 603-1991, “IEEE Standard Criteria for Safety Systems for Nuclear Power Generating Stations,” (Reference 7.6.1-2) and is therefore sufficient to show compliance with regulation." [PSAR_ch07 §7.6.1 p.246]
- "I&C systems are designed to perform assigned safety-related (SR), non-safety-related with special treatment (NSRST), and non-safety-related with no special treatment (NST) functions and to assist in satisfying PDC." [PSAR_ch07 §7.6.1.1 p.246]
- "Additional design requirements result from regulations, regulatory guidance, and industry codes and standards." [PSAR_ch07 §7.6.1.1 p.246]
- "The relationship of I&C systems to plant-level Defense Lines (DLs), the classification of I&C systems, compliance with regulations, and the assignment of special treatments are described in Section 7.6.1.1.1 through Section 7.6.1.1.4." [PSAR_ch07 §7.6.1.1 p.246]
- "A description of how specific safety-significant I&C systems support satisfying PDC is provided in Section 7.6.2 through Section 7.6.6 and Section 7.6.8." [PSAR_ch07 §7.6.1.1 p.246]
- "The relationship of I&C systems to DLs is described in NAT-4950-A, “I&C Architecture and Design Basis Topical Report,” Revision 2 (Reference 7.6.1-3)." [PSAR_ch07 §7.6.1.1.1 p.246]
- "NAT-4950-A, is incorporated by reference into the SAR." [PSAR_ch07 §7.6.1.1.1 p.246]
- "See Section 1.4.2 for a list of documents incorporated by reference into the SAR." [PSAR_ch07 §7.6.1.1.1 p.246]
- "The classification of I&C systems and associated DLs that the I&C systems support are shown in Table 7.6.1-1." [PSAR_ch07 §7.6.1.1.1 p.246]
- "Specific DL functions for the I&C systems are described in Section 7.6.2 through Section 7.6.6 and Section 7.6.8." [PSAR_ch07 §7.6.1.1.1 p.246]
- "The DLs are described in Section 4.2.1.2." [PSAR_ch07 §7.6.1.1.1 p.246]
- "An overview of the I&C system classification process is provided in NAT-4950-A." [PSAR_ch07 §7.6.1.1.2 p.246]
- "I&C system classification is described in Section 5.1." [PSAR_ch07 §7.6.1.1.2 p.246]
- "Descriptions of compliance with regulatory requirements and conformance with regulatory guidance and industry codes and standards for I&C systems are provided in NAT-4950-A." [PSAR_ch07 §7.6.1.1.3 p.246]
- "Special treatments are initially selected based on SSC safety classification as described in Section 6.3." [PSAR_ch07 §7.6.1.1.4 p.247]
- "Special treatments that have been assigned to particular safety-significant I&C SSCs are described in Section 7.6.2 through Section 7.6.6 and Section 7.6.8." [PSAR_ch07 §7.6.1.1.4 p.247]
- "The method for confirming specific reliability and capability targets for SSCs at the operating license stage is described in Section 6.2." [PSAR_ch07 §7.6.1.1.4 p.247]
- "The I&C system architecture incorporates the following fundamental I&C design principles consistent with Design Review Guide (DRG): Instrumentation and Controls for Non-Light-Water Reactor (Non-LWR) Reviews (Reference 7.6.1-4):" [PSAR_ch07 §7.6.1.2 p.247]

| 목록 항목 | 출처 |
|---|---|
| Independence | [PSAR_ch07 §7.6.1.2 p.247] |

- "Communications and logical independence" [PSAR_ch07 §7.6.1.2 p.247]

| 목록 항목 | 출처 |
|---|---|
| Redundancy | [PSAR_ch07 §7.6.1.2 p.247] |
| Diversity | [PSAR_ch07 §7.6.1.2 p.247] |
| System Integrity | [PSAR_ch07 §7.6.1.2 p.247] |
| Reliable I&C | [PSAR_ch07 §7.6.1.2 p.247] |

- "Human Factors Engineering" [PSAR_ch07 §7.6.1.2 p.247]
- "The fundamental I&C design principles are described in NAT-4950-A." [PSAR_ch07 §7.6.1.2 p.247]
- "Human factors are considered in the design of I&C systems." [PSAR_ch07 §7.6.1.2 p.247]
- "Human factors engineering is described in Section 11.2." [PSAR_ch07 §7.6.1.2 p.247]
- "The I&C system architecture, to include representative figures, is shown in NAT-4950-A." [PSAR_ch07 §7.6.1.2.1 p.247]
- "Since I&C systems are classified as SR, NSRST, and NST, the I&C architecture implements the following communication strategy to support the fundamental I&C design principles:" [PSAR_ch07 §7.6.1.2.1 p.247]
- "There are no direct digital data communications from either the NSRST and NST systems to the SR systems." [PSAR_ch07 §7.6.1.2.1 p.247]
- "One-way communication from SR I&C systems to the NSRST or NST systems is via isolated hardwire or through data-diode and gateways." [PSAR_ch07 §7.6.1.2.1 p.247]
- "The SR I&C systems do not have inter-divisional communications with the exception of the RPS voting." [PSAR_ch07 §7.6.1.2.1 p.247]
- "Additional information relating to communications for the I&C architecture is provided in NAT-4950-A." [PSAR_ch07 §7.6.1.2.1 p.247]
- "SR I&C Systems" [PSAR_ch07 §7.6.1.2.1 p.248]
- "NSRST I&C Systems" [PSAR_ch07 §7.6.1.2.1 p.248]
- "The Reactor Protection System (RPS) accepts input signals from plant instrumentation, applies required logic, and automatically generates output signals to initiate safety functions." [PSAR_ch07 §7.6.1.2.1 p.248]
- "The RPS also serves to display information to operators in the Main Control Room and Remote Shutdown Complex during normal and post-accident conditions." [PSAR_ch07 §7.6.1.2.1 p.248]
- "The RPS is described in Section 7.6.3." [PSAR_ch07 §7.6.1.2.1 p.248]
- "The Main Control Room and Remote Shutdown Complex are described in Section 7.6.7.1 and Section 7.6.7.2, respectively." [PSAR_ch07 §7.6.1.2.1 p.248]
- "The Nuclear Instrumentation System provides instrumentation to sense neutron flux during fuel movement, reactor startup, power operations, reactor shutdown, and licensing-basis events." [PSAR_ch07 §7.6.1.2.1 p.248]
- "The Nuclear Instrumentation System amplifies and conditions the instrument signals and provides input signals to the RPS and Nuclear Island Control System (NIC) for use in protective, control, and monitoring functions." [PSAR_ch07 §7.6.1.2.1 p.248]
- "The Nuclear Instrumentation System is described in Section 7.6.4." [PSAR_ch07 §7.6.1.2.1 p.248]
- "The Reactor Instrumentation System provides instrumentation to monitor selected parameters in or near the reactor vessel and transmits corresponding signals to the RPS and NIC for use in protective, control, and monitoring functions." [PSAR_ch07 §7.6.1.2.1 p.248]
- "The Reactor Instrumentation System is described in Section 7.6.5." [PSAR_ch07 §7.6.1.2.1 p.248]
- "The NIC is a group of I&C systems that perform NSRST and NST control and monitoring functions." [PSAR_ch07 §7.6.1.2.1 p.248]
- "The NIC is implemented on a Distributed Control System platform that provides a means for gathering information from field sensors, executing both manual and automatic logic, interfacing with field actuators, and providing a means for operator interface." [PSAR_ch07 §7.6.1.2.1 p.248]
- "The NIC also includes controls that are executed by control systems outside of the Distributed Control System that include interfaces for communication with the Distributed Control System." [PSAR_ch07 §7.6.1.2.1 p.248]
- "The NIC and associated I&C systems are described in Section 7.6.2." [PSAR_ch07 §7.6.1.2.1 p.248]
- "The Radiation Monitoring System provides radiation activity indications for use in the protection of plant personnel and the surrounding environment during operating, refueling, and post-accident conditions." [PSAR_ch07 §7.6.1.2.1 p.248]
- "The Radiation Monitoring System also performs continuous radiation monitoring and sampling analysis of selected radioactive processes, as well as monitoring for the selected release points where radioactive effluents leave the site boundary." [PSAR_ch07 §7.6.1.2.1 p.248]
- "The Radiation Monitoring System is described in Section 7.6.6." [PSAR_ch07 §7.6.1.2.1 p.248]
- "The Anticipatory Automatic Seismic Trip System senses ground motion and provides a reactor scram signal to the RPS in response to a seismic beyond design basis event." [PSAR_ch07 §7.6.1.2.1 p.248]
- "The Anticipatory Automatic Seismic Trip System is described in Section 7.6.8." [PSAR_ch07 §7.6.1.2.1 p.248]
- "Post-Accident Monitoring functionality is provided for Type B, C, D, and F variables as defined by IEEE 497-2016, “IEEE Standard Criteria for Accident Monitoring Instrumentation for Nuclear Power Generating Stations,” (Reference 7.6.1-5)." [PSAR_ch07 §7.6.1.2.1 p.248]
- "There are no Type A Post-Accident Monitoring variables in the I&C design." [PSAR_ch07 §7.6.1.2.1 p.248]
- "The design of Post-Accident Monitoring capabilities is informed by IEEE 497-2016." [PSAR_ch07 §7.6.1.2.1 p.248]
- "A description of the conformance to IEEE 497-2016 as endorsed by Regulatory Guide 1.97, “Criteria for Accident Monitoring Instrumentation for Nuclear Power Plants,” Revision 5, will be provided at the operating license stage." [PSAR_ch07 §7.6.1.2.1 p.248-249]
- "The Post-Accident Monitoring functionality is provided using the NIC and RPS systems." [PSAR_ch07 §7.6.1.2.1 p.249]

| System | Classification | Associated DL | 출처 |
|---|---|---|---|
| Nuclear Island Control System | Not Applicable | The NIC is a collection of sub-systems and is described in Section 7.6.2. The NIC is not classified as a system and is not assigned DLs as a system. Sub-systems of the NIC are classified and assigned DLs. | [PSAR_ch07 Table 7.6.1-1 p.250] |
| Nuclear Island Rod Monitoring and Control System | NST | DL2, DL4, DL5 | [PSAR_ch07 Table 7.6.1-1 p.250] |
| Nuclear Island Coolant Temperature Control System | NSRST | DL2, DL4, DL5 | [PSAR_ch07 Table 7.6.1-1 p.250] |
| Nuclear Island Utility Monitoring Control System | NSRST | DL2, DL4, DL5 | [PSAR_ch07 Table 7.6.1-1 p.250] |
| Nuclear Island Auxiliary Monitoring and Control System | NSRST | DL2, DL4, DL5 | [PSAR_ch07 Table 7.6.1-1 p.250] |
| Nuclear Island Plant Monitoring and Control System | NST | DL2, DL4, DL5 | [PSAR_ch07 Table 7.6.1-1 p.250] |
| Nuclear Island Fuel Handling Supervisory Control System | NST | No DLs identified | [PSAR_ch07 Table 7.6.1-1 p.250] |
| Reactor Protection System | SR | DL3, DL4, DL5 | [PSAR_ch07 Table 7.6.1-1 p.250] |
| Nuclear Instrumentation System | SR | DL2, DL3, DL5 | [PSAR_ch07 Table 7.6.1-1 p.250] |
| Reactor Instrumentation System | SR | DL2, DL3, DL4,DL5 | [PSAR_ch07 Table 7.6.1-1 p.250] |
| Anticipatory Automatic Seismic Trip System | NSRST | DL4 | [PSAR_ch07 Table 7.6.1-1 p.250] |
| Radiation Monitoring System | NSRST | DL4, DL5 | [PSAR_ch07 Table 7.6.1-1 p.250] |

## 해설
`PSAR` Chapter 7 §7.6.1에 따르면 instrumentation and control(`I&C`) 계통은 licensing-basis event에 대한 자동 작동을 제공하고, principal design criteria%%t:PDC%% 충족에 기여하며, 구성품을 수동으로 작동시키는 수단을 심층방어(Defense-in-Depth)%%t:DID%% 지원 차원에서 제공한다. `I&C` 계통은 SR%%t:SR%%, NSRST%%t:NSRST%%, Non-Safety-Related with No Special Treatment%%t:NST%% 기능을 수행하도록 설계되고, 규제·지침·산업 표준에서 추가 요건이 나온다. 설계에는 `IEEE 603-2018`을 쓰며, 원문은 이 표준이 `IEEE 603-1991`과 동등하거나 더 높은 안전 수준을 제공하므로 규제 준수를 보이기에 충분하다고 적는다.

Defense Line%%t:DL%%과의 관계, 분류 과정 개요, 규제 요건 준수와 지침·표준 부합은 `NAT-4950-A`(`I&C Architecture and Design Basis Topical Report`, Revision 2)에 기술되며, 이 보고서는 `SAR`에 참조로 통합된다. `I&C` 분류는 Section 5.1에, special treatment 초기 선정은 Section 6.3에, 신뢰도·능력 목표 확인 방법은 Section 6.2에 있다. 계통 구조는 `DRG`(`Instrumentation and Controls for Non-Light-Water Reactor (Non-LWR) Reviews`)와 일치하는 `fundamental I&C design principles`(Independence, Communications and logical independence, Redundancy, Diversity, System Integrity, Reliable I&C, Human Factors Engineering)를 반영한다.

`I&C` 계통이 SR%%t:SR%%, NSRST%%t:NSRST%%, NST%%t:NST%%로 나뉘므로 구조는 다음 통신 전략을 쓴다. NSRST%%t:NSRST%%·NST%%t:NST%% 계통에서 SR%%t:SR%% 계통으로 가는 직접 디지털 자료 통신은 없고, SR%%t:SR%% 계통에서 나가는 단방향 통신은 격리된 hardwire 또는 data-diode와 gateway를 거친다. SR%%t:SR%% `I&C` 계통은 `RPS` voting을 제외하면 division 간 통신이 없다.

원문은 SR%%t:SR%% `I&C` 계통으로 Reactor Protection System(`RPS`), Nuclear Instrumentation System, Reactor Instrumentation System을, NSRST%%t:NSRST%% `I&C` 계통 제목 아래 Nuclear Island Control System(`NIC`), Radiation Monitoring System, Anticipatory Automatic Seismic Trip System을 설명한다. `Table 7.6.1-1`에서 `RPS`는 SR%%t:SR%%이고 `DL3`, `DL4`, `DL5`를, Nuclear Instrumentation System은 SR%%t:SR%%이고 `DL2`, `DL3`, `DL5`를, Reactor Instrumentation System은 SR%%t:SR%%이고 `DL2`–`DL5`를 지원한다. Anticipatory Automatic Seismic Trip System은 NSRST%%t:NSRST%%(`DL4`), Radiation Monitoring System은 NSRST%%t:NSRST%%(`DL4`, `DL5`)이다. `NIC`는 하위 계통의 모음이라 계통 단위로 분류되거나 DL%%t:DL%%을 배정받지 않으며, 하위 계통 가운데 Coolant Temperature Control, Utility Monitoring Control, Auxiliary Monitoring and Control System은 NSRST%%t:NSRST%%, Rod Monitoring and Control, Plant Monitoring and Control, Fuel Handling Supervisory Control System은 NST%%t:NST%%이다. Fuel Handling Supervisory Control System에는 식별된 DL%%t:DL%%이 없다.

Post-Accident Monitoring 기능은 `IEEE 497-2016`이 정의한 Type B, C, D, F 변수에 제공되며, 설계에 Type A 변수는 없다. 이 기능은 `NIC`와 `RPS`로 제공되고, `RG 1.97, Revision 5`가 승인한 `IEEE 497-2016` 부합 설명은 operating license%%t:OL%% 단계에서 제공된다.

## 관련 문서
- [[Natrium_IC_Systems]]
- [[Natrium_SSC_Safety_Classification]]
- [[Natrium_Defense_Lines]]
- [[Natrium_System_NI_Control]]
- [[Natrium_System_Reactor_Protection]]
- [[Natrium_System_Nuclear_Instrumentation]]
- [[Natrium_System_Reactor_Instrumentation]]
- [[Natrium_System_Radiation_Monitoring]]
- [[Natrium_System_Anticipatory_Seismic_Trip]]
- [[Natrium_System_Control_Room_Indications]]
- [[PSAR_ch07]]
- [[Natrium_SER_IC_Electrical_Structures_Review]]
