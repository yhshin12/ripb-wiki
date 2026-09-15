---
type: natrium
aliases: []
sources:
- PSAR_ch05
status: checked
verified: 2026-09-16
term: null
tags:
- natrium
- pdc
terms_pending: []
---

# Natrium PDC 20–29 반응도 제어 (Natrium PDC Reactivity Control)

> [!abstract] 요약
> principal design criteria%%t:PDC%% 20–29는 보호 계통의 기능, 신뢰도와 시험 가능성, 독립성, 고장 모드, 제어 계통과의 분리, 반응도 제어 오작동 대응, 반응도 제어 계통, 반응도 한계, Anticipated Operational Occurrence%%t:AOO%% 방호를 다룬다. 이행 요약에 따르면 Reactor Protection System은 네 독립 division과 2-out-of-4 투표를 쓰고, 반응도 제어는 rod de-latch와 rod motor drive라는 두 수단과 primary·secondary 제어봉 두 세트로 이루어진다.

## 원문 사실
| Criterion | 출처 |
|---|---|
| PDC 20 - Protection System Functions | [PSAR_ch05 §5.3.3.1 p.30] |
| PDC 21 - Protection System Reliability and Testability | [PSAR_ch05 §5.3.3.2 p.31] |
| PDC 22 - Protection System Independence | [PSAR_ch05 §5.3.3.3 p.31] |
| PDC 23 - Protection System Failure Modes | [PSAR_ch05 §5.3.3.4 p.32] |
| PDC 24 - Separation of Protection and Control Systems | [PSAR_ch05 §5.3.3.5 p.32] |
| PDC 25 - Protection System Requirements for Reactivity Control Malfunctions | [PSAR_ch05 §5.3.3.6 p.33] |
| PDC 26 - Reactivity Control Systems | [PSAR_ch05 §5.3.3.7 p.33] |
| PDC 28 - Reactivity Limits | [PSAR_ch05 §5.3.3.8 p.35] |
| PDC 29 - Protection Against Anticipated Operational Occurrences | [PSAR_ch05 §5.3.3.9 p.35] |

| 절 | 제목 | 출처 |
|---|---|---|
| 5.3.3 | Reactivity Control | [PSAR_ch05 §5.3.3 p.30] |

- "The protection system shall be designed (1) to initiate automatically the operation of appropriate systems, including the reactivity control systems, to ensure that the specified acceptable system radionuclide release design limits is not exceeded as a result of anticipated operational occurrences and (2) to sense accident conditions and to initiate the operation of safety-significant systems and components." [PSAR_ch05 §5.3.3.1 p.30]

- "The RPS is designed to accept input signals from instruments to monitor and control plant conditions during postulated accidents and reliably initiate the SR scram and engineered safety feature functions as necessary to ensure reactor safety." [PSAR_ch05 §5.3.3.1 p.30]
- "The RPS is also designed to ensure SARRDL are not exceeded as a result of AOOs." [PSAR_ch05 §5.3.3.1 p.30]
- "The portions of the RPS which support SR functions are arranged into four redundant divisions each with physical, electrical, and functional independence from the other redundant divisions." [PSAR_ch05 §5.3.3.1 p.31]
- "Each process variable used by the RPS to perform a safety function is measured by four redundant sensing instruments or groups of instruments which are also divided into four divisions." [PSAR_ch05 §5.3.3.1 p.31]

| PDC | Relevant PSAR Chapters and Sections | 출처 |
|---|---|---|
| PDC 20 | Section 7.6.3 | [PSAR_ch05 §5.3.3.1 p.31] |
| PDC 20 | Section 7.6.4 | [PSAR_ch05 §5.3.3.1 p.31] |
| PDC 20 | Section 7.6.5 | [PSAR_ch05 §5.3.3.1 p.31] |

- "The protection system shall be designed for high functional reliability and inservice testability commensurate with the safety functions to be performed." [PSAR_ch05 §5.3.3.2 p.31]
- "Redundancy and independence designed into the protection system shall be sufficient to assure that (1) no single failure results in loss of the protection function and (2) removal from service of any component or channel does not result in loss of the required minimum redundancy unless the acceptable reliability of operation of the protection system can be otherwise demonstrated." [PSAR_ch05 §5.3.3.2 p.31]
- "The protection system shall be designed to permit periodic testing of its functioning when the reactor is in operation, including a capability to test channels independently to determine failures and losses of redundancy that may have occurred." [PSAR_ch05 §5.3.3.2 p.31]

- "Conformance with industry standards ensures that the RPS is designed for high functional reliability, redundancy, and inservice testability commensurate with the safety functions to be performed." [PSAR_ch05 §5.3.3.2 p.31]
- "The SR portions of the RPS are arranged into four redundant and independent divisions." [PSAR_ch05 §5.3.3.2 p.31]
- "Each process variable input used by the RPS to perform a safety function is measured by four redundant sensing instruments or groups of instruments which are also divided into four redundant and independent divisions." [PSAR_ch05 §5.3.3.2 p.31]
- "The RPS actuates reactor scram and ESF functions when at least 2 out of the 4 divisions independently determine that such action is required." [PSAR_ch05 §5.3.3.2 p.31]
- "The divisional arrangement and 2-out-of-4 voting design features allow inservice testability." [PSAR_ch05 §5.3.3.2 p.31]
- "The RPS design allows for any division to be taken out of service for testing at any time without loss of any safety function and without loss of minimum required redundancy." [PSAR_ch05 §5.3.3.2 p.31]

| PDC | Relevant PSAR Chapters and Sections | 출처 |
|---|---|---|
| PDC 21 | Section 7.6.3 | [PSAR_ch05 §5.3.3.2 p.31] |
| PDC 21 | Section 7.6.4 | [PSAR_ch05 §5.3.3.2 p.31] |
| PDC 21 | Section 7.6.5 | [PSAR_ch05 §5.3.3.2 p.31] |

- "The protection system shall be designed to assure that the effects of natural phenomena, and of normal operating, maintenance, testing, and postulated accident conditions on redundant channels do not result in loss of the protection function, or shall be demonstrated to be acceptable on some other defined basis." [PSAR_ch05 §5.3.3.3 p.31]
- "Design techniques, such as functional diversity or diversity in component design and principles of operation, shall be used to the extent practical to prevent loss of the protection function." [PSAR_ch05 §5.3.3.3 p.31]

- "Conformance with industry standards ensures that the RPS is designed to assure that the effects of natural phenomena, and of normal operating, maintenance, testing, and postulated accident conditions on redundant channels do not result in loss of the protection function." [PSAR_ch05 §5.3.3.3 p.32]
- "The RPS cabinets are contained in the NI Control Building substructure." [PSAR_ch05 §5.3.3.3 p.32]
- "The SR NI Control Building substructure is designed to provide appropriate seismic protection and protection from natural phenomena such that there is not a loss of the RPS safety function." [PSAR_ch05 §5.3.3.3 p.32]
- "The RPS vault rooms are designed to meet fire protection requirements." [PSAR_ch05 §5.3.3.3 p.32]

| PDC | Relevant PSAR Chapters and Sections | 출처 |
|---|---|---|
| PDC 22 | Section 7.6.3 | [PSAR_ch05 §5.3.3.3 p.32] |
| PDC 22 | Section 7.6.4 | [PSAR_ch05 §5.3.3.3 p.32] |
| PDC 22 | Section 7.6.5 | [PSAR_ch05 §5.3.3.3 p.32] |

- "The protection system shall be designed to fail into a safe state or into a state demonstrated to be acceptable on some other defined basis, if conditions such as disconnection of the system, loss of energy (e.g., electric power, instrument air), or postulated adverse environments (e.g., extreme heat or cold, fire, sodium and sodium reaction products, pressure, steam, water, and radiation) are experienced." [PSAR_ch05 §5.3.3.4 p.32]

- "The RPS, associated divisions, and the reactor trip breakers and ESF breakers fail safe on a loss of power." [PSAR_ch05 §5.3.3.4 p.32]
- "A shunt trip is also provided in addition to the undervoltage trip to increase the reactor trip breaker and the ESF breaker reliability and diversity." [PSAR_ch05 §5.3.3.4 p.32]
- "The RPS equipment is environmentally and seismically qualified to remain operable during anticipated adverse conditions." [PSAR_ch05 §5.3.3.4 p.32]
- "The RPS performs self-diagnostics and places outputs in a safe state if a critical fault is detected." [PSAR_ch05 §5.3.3.4 p.32]

| PDC | Relevant PSAR Chapters and Sections | 출처 |
|---|---|---|
| PDC 23 | Section 7.6.3 | [PSAR_ch05 §5.3.3.4 p.32] |
| PDC 23 | Section 7.6.4 | [PSAR_ch05 §5.3.3.4 p.32] |

- "The protection system shall be separated from control systems to the extent that failure of any single control system component or channel, or failure or removal from service of any single protection system component or channel which is common to the control and protection systems leaves intact a system satisfying all reliability, redundancy, and independence requirements of the protection system." [PSAR_ch05 §5.3.3.5 p.32]
- "Interconnection of the protection and control systems shall be limited so as to assure that safety is not significantly impaired." [PSAR_ch05 §5.3.3.5 p.32]

- "Conformance with industry standards ensures that the RPS is separated from control systems to the extent that failure of any single control system component or channel, or removal from service of any single protection system component or channel which is common to the control and protection systems leaves intact a system satisfying all reliability, redundancy, and independence requirements of the RPS." [PSAR_ch05 §5.3.3.5 p.33]
- "There is no direct communication from NI control systems to the RPS." [PSAR_ch05 §5.3.3.5 p.33]
- "The RPS is isolated and functionally independent of the non-safety control systems and uses input signals from independent instrument channels." [PSAR_ch05 §5.3.3.5 p.33]
- "One-way communication from the RPS to control systems is utilized via a data diode or hardwired connection." [PSAR_ch05 §5.3.3.5 p.33]
- "RPS components such as shared sensors are isolated from control systems using SR isolation hardware." [PSAR_ch05 §5.3.3.5 p.33]

| PDC | Relevant PSAR Chapters and Sections | 출처 |
|---|---|---|
| PDC 24 | Section 7.6.2 | [PSAR_ch05 §5.3.3.5 p.33] |
| PDC 24 | Section 7.6.3 | [PSAR_ch05 §5.3.3.5 p.33] |
| PDC 24 | Section 7.6.4 | [PSAR_ch05 §5.3.3.5 p.33] |
| PDC 24 | Section 7.6.5 | [PSAR_ch05 §5.3.3.5 p.33] |
| PDC 24 | Section 7.6.8 | [PSAR_ch05 §5.3.3.5 p.33] |

- "The protection system shall be designed to ensure that specified acceptable system radionuclide release design limits are not exceeded during any anticipated operational occurrence, accounting for a single malfunction of the reactivity control systems." [PSAR_ch05 §5.3.3.6 p.33]

- "The RPS reactor scram and ESF functions are designed to ensure that SARRDLs are not exceeded as a result of anticipated operational occurrences even when a single failure of the reactivity control system has occurred." [PSAR_ch05 §5.3.3.6 p.33]
- "The RPS is designed with four independent divisions." [PSAR_ch05 §5.3.3.6 p.33]
- "Failure of one division does not preclude completion of safety functions." [PSAR_ch05 §5.3.3.6 p.33]
- "XIS provides flux signals to RPS in support of SR protective functions, and the four XIS divisions correspond to the four RPS divisions." [PSAR_ch05 §5.3.3.6 p.33]
- "In addition, the NIC provides reactivity control during normal operations and under AOOs through power runback by RMC and Coolant Temperature Monitoring and Control System." [PSAR_ch05 §5.3.3.6 p.33]
- "The NIC is independent of the RPS and failure of the NIC does not impact RPS safety and reactivity control functions." [PSAR_ch05 §5.3.3.6 p.33]

| PDC | Relevant PSAR Chapters and Sections | 출처 |
|---|---|---|
| PDC 25 | Section 7.6.2 | [PSAR_ch05 §5.3.3.6 p.33] |
| PDC 25 | Section 7.6.3 | [PSAR_ch05 §5.3.3.6 p.33] |
| PDC 25 | Section 7.6.4 | [PSAR_ch05 §5.3.3.6 p.33] |

- "A minimum of two reactivity control systems or means shall provide:" [PSAR_ch05 §5.3.3.7 p.33]
- "A means of inserting negative reactivity at a sufficient rate and amount to assure, with appropriate margin for malfunctions, that the specified acceptable system radionuclide release design limits are not exceeded and safe shutdown is achieved and maintained during normal operation, including anticipated operational occurrences." [PSAR_ch05 §5.3.3.7 p.33]
- "A means which is independent and diverse from the other(s), shall be capable of controlling the rate of reactivity changes resulting from planned, normal power changes to assure that the specified acceptable system radionuclide release design limits are not exceeded." [PSAR_ch05 §5.3.3.7 p.34]
- "A means of inserting negative reactivity at a sufficient rate and amount to assure, with appropriate margin for malfunctions, that the capability to cool the core is maintained and a means of shutting down the reactor and maintaining, at a minimum, a safe shutdown condition following a postulated accident." [PSAR_ch05 §5.3.3.7 p.34]
- "A means for holding the reactor shutdown under conditions which allow for interventions such as fuel loading, inspection and repair shall be provided." [PSAR_ch05 §5.3.3.7 p.34]

- "Two reactivity control means, as well as a primary and secondary set of rods, are provided." [PSAR_ch05 §5.3.3.7 p.34]
- "The two reactivity control means are rod de-latch and rod motor drive." [PSAR_ch05 §5.3.3.7 p.34]
- "The RPS initiates rod de-latch to drop both the primary and secondary set of rods into the core using gravity (scram)." [PSAR_ch05 §5.3.3.7 p.34]
- "After rod de-latch, the RPS also sends a sends a signal to the rod motor drives to fully insert the rods into the core." [PSAR_ch05 §5.3.3.7 p.34]
- "There are no common cause failures between the rod de-latch and rod motor drive." [PSAR_ch05 §5.3.3.7 p.34]
- "The bundle geometry is also diverse with respect to the primary and secondary rod sets to eliminate common cause failure from effecting all rods." [PSAR_ch05 §5.3.3.7 p.34]
- "Each part of PDC 26 is met as follows:" [PSAR_ch05 §5.3.3.7 p.34]
- "The RPS initiates the de-latch of the Primary and Secondary sets of rods to insert negative reactivity at an amount and rate to maintain conditions less than the specified acceptable system radionuclide release limits design during normal operation, including anticipated operational occurrences." [PSAR_ch05 §5.3.3.7 p.34]
- "The reactor is safely shutdown including accounting for the appropriate malfunction." [PSAR_ch05 §5.3.3.7 p.34]
- "This consideration of malfunctions is accounted for in two different types of scenarios." [PSAR_ch05 §5.3.3.7 p.34]
- "In the first scenario the highest worth rod is assumed to be held in the fully withdrawn position as the malfunction with the other rods succeeding to drop by gravity, and achieves hot standby with margin." [PSAR_ch05 §5.3.3.7 p.34]
- "The second scenario considers either the primary or secondary set failing to insert as the malfunction with the other set succeeding to drop by gravity, and achieves safe shutdown following the event." [PSAR_ch05 §5.3.3.7 p.34]
- "The rod motor drive provides a means independent and diverse from de-latch by inserting sufficient negative reactivity at the rate necessary that the SARRDLs are not exceeded from planned, normal power changes." [PSAR_ch05 §5.3.3.7 p.34]
- "Additionally, the primary and secondary control rod bundle geometric designs are unique and provide protection against a common mode failure of rod binding." [PSAR_ch05 §5.3.3.7 p.34]
- "The RPS initiates the de-latch of the Primary and Secondary sets of rods to insert negative reactivity at a rate and amount to assure safe shutdown following a postulated accident, while maintaining the capability to cool the core." [PSAR_ch05 §5.3.3.7 p.34]
- "The reactor is safely shutdown including accounting for the appropriate malfunction." [PSAR_ch05 §5.3.3.7 p.34]
- "This consideration of malfunctions is accounted for in two different types of scenarios." [PSAR_ch05 §5.3.3.7 p.34]
- "In the first scenario the highest worth rod is assumed to be held in the fully withdrawn position as the malfunction with the other rods succeeding to drop by gravity, and achieves hot standby with margin." [PSAR_ch05 §5.3.3.7 p.34]
- "The second scenario considers either the primary or secondary set failing to insert as the malfunction with the other set succeeding to drop by gravity, and achieves safe shutdown following the event." [PSAR_ch05 §5.3.3.7 p.34]
- "Fully inserted primary and secondary control rods, along with administrative controls that preclude removal of more than one rod bundle form the reactor core, maintain the reactor shutdown under conditions which allow for fuel loading, inspection, and repair." [PSAR_ch05 §5.3.3.7 p.35]
- "Administrative controls include reloading control rods first during a refueling evolution." [PSAR_ch05 §5.3.3.7 p.35]

| PDC | Relevant PSAR Chapters and Sections | 출처 |
|---|---|---|
| PDC 26 | Section 3.12 | [PSAR_ch05 §5.3.3.7 p.35] |
| PDC 26 | Section 7.1.1 | [PSAR_ch05 §5.3.3.7 p.35] |
| PDC 26 | Section 7.1.2 | [PSAR_ch05 §5.3.3.7 p.35] |
| PDC 26 | Section 7.2.5 | [PSAR_ch05 §5.3.3.7 p.35] |
| PDC 26 | Section 7.6.2 | [PSAR_ch05 §5.3.3.7 p.35] |
| PDC 26 | Section 7.6.3 | [PSAR_ch05 §5.3.3.7 p.35] |

- "The reactivity control systems shall be designed with appropriate limits on the potential amount and rate of reactivity increase to ensure that the effects of postulated reactivity accidents can neither (1) result in damage to the safety-significant elements of the primary coolant boundary greater than limited local yielding nor (2) sufficiently disturb the core, its support structures or other reactor vessel internals to impair significantly the capability to cool the core." [PSAR_ch05 §5.3.3.8 p.35]

- "The design of the RCC, RMC, CRD, and RPS ensure that postulated reactivity AOOs, DBEs, and DBAs do not result in damage to the safety-significant elements of the primary coolant boundary greater than limited local yielding, nor result in disturbance of the core, its support structures, or other reactor vessel internals that significantly impair the capability to cool the core." [PSAR_ch05 §5.3.3.8 p.35]
- "The RES supports reactivity control functions by providing structural support to Control Rod Drive Mechanisms and drivelines, and maintaining control rod driveline alignment with control assemblies to limit the potential amount and rate of reactivity increase during postulated reactivity events." [PSAR_ch05 §5.3.3.8 p.35]
- "RES contributes to structurally supporting and maintaining the geometry of reactor core assemblies, to limit fuel assembly deflections, and provide adequate coolant flow and heat removal." [PSAR_ch05 §5.3.3.8 p.35]
- "The RMC and CRD control the maximum control rod withdrawal speed to limit the reactivity worth insertion rate." [PSAR_ch05 §5.3.3.8 p.35]
- "A CRD control interlock prevents withdrawal of more than one control rod at a time." [PSAR_ch05 §5.3.3.8 p.35]
- "The Control Rod Drive Mechanism also includes a brake to hold the control rod assembly at any selected position within the stroke of travel and prevent it from inadvertent insertion or withdrawal." [PSAR_ch05 §5.3.3.8 p.35]

| PDC | Relevant PSAR Chapters and Sections | 출처 |
|---|---|---|
| PDC 28 | Section 7.1.1 | [PSAR_ch05 §5.3.3.8 p.35] |
| PDC 28 | Section 7.1.2 | [PSAR_ch05 §5.3.3.8 p.35] |
| PDC 28 | Section 7.2.5 | [PSAR_ch05 §5.3.3.8 p.35] |
| PDC 28 | Section 7.6.2 | [PSAR_ch05 §5.3.3.8 p.35] |
| PDC 28 | Section 7.6.3 | [PSAR_ch05 §5.3.3.8 p.35] |

- "The protection and reactivity control systems shall be designed to assure an extremely high probability of accomplishing their safety functions in the event of anticipated operational occurrences." [PSAR_ch05 §5.3.3.9 p.35]

- "The design of the RCC, CRD, NIC, RPS, XIS, and Reactor Instrumentation System assure an extremely high probability of accomplishing their safety functions in the event of AOOs." [PSAR_ch05 §5.3.3.9 p.36]

| PDC | Relevant PSAR Chapters and Sections | 출처 |
|---|---|---|
| PDC 29 | Section 7.1.1 | [PSAR_ch05 §5.3.3.9 p.36] |
| PDC 29 | Section 7.2.5 | [PSAR_ch05 §5.3.3.9 p.36] |
| PDC 29 | Section 7.6.2 | [PSAR_ch05 §5.3.3.9 p.36] |
| PDC 29 | Section 7.6.3 | [PSAR_ch05 §5.3.3.9 p.36] |
| PDC 29 | Section 7.6.4 | [PSAR_ch05 §5.3.3.9 p.36] |
| PDC 29 | Section 7.6.5 | [PSAR_ch05 §5.3.3.9 p.36] |

## 해설
기준 20은 보호 계통이 AOO%%t:AOO%%에서 specified acceptable system radionuclide release design limit%%t:SARRDL%%을 넘지 않도록 반응도 제어 계통을 포함한 적절한 계통을 자동으로 기동하고, 사고 조건을 감지해 safety-significant 계통과 기기를 기동하게 한다. 이행 요약은 Reactor Protection System이 계측 입력을 받아 Safety-Related%%t:SR%% scram과 engineered safety feature 기능을 개시하고, SR%%t:SR%% 기능을 지원하는 부분이 물리적·전기적·기능적으로 독립된 네 중복 division으로 배치되며, 각 공정 변수가 네 division으로 나뉜 네 중복 계측으로 측정된다고 적는다. 기준 21은 안전 기능에 상응하는 높은 신뢰도와 가동 중 시험 가능성, 단일 고장이나 기기·채널 제거로 보호 기능이나 최소 중복성을 잃지 않는 중복성·독립성, 운전 중 채널별 시험 능력을 요구한다. 이행 요약에 따르면 Reactor Protection System은 네 division 가운데 적어도 2개가 독립적으로 필요하다고 판단하면 scram과 engineered safety feature 기능을 작동하고, 어느 division이든 안전 기능과 최소 중복성을 잃지 않고 시험을 위해 사용을 중지할 수 있다.

기준 22는 자연 현상과 정상 운전·정비·시험·가정 사고 조건이 중복 채널에 미치는 영향으로 보호 기능을 잃지 않게 하고 실용적인 범위에서 다양성 설계 기법을 쓰게 한다. 이행 요약은 Reactor Protection System 캐비닛이 `NI Control Building`의 SR%%t:SR%% 지하 구조물 안에 있어 지진과 자연 현상으로부터 보호되고, 캐비닛실이 화재 방호 요건을 만족한다고 적는다. 기준 23은 계통 분리, 에너지 상실, 극한 온도·화재·소듐과 소듐 반응 생성물·압력·증기·물·방사선 같은 가정 불리한 환경에서 보호 계통이 안전한 상태로 고장나게 한다. 이행 요약은 Reactor Protection System, division, reactor trip breaker, engineered safety feature breaker가 전력 상실 시 fail safe이고, undervoltage trip에 더해 shunt trip으로 차단기의 신뢰도와 다양성을 높이며, 장비가 환경·내진 검증을 받고 자기 진단에서 치명적 결함을 찾으면 출력을 안전 상태로 둔다고 적는다. 기준 24는 제어 계통이나 공유 보호 계통 기기·채널의 단일 고장이나 제거가 보호 계통 요건을 만족하는 계통을 남기도록 보호 계통과 제어 계통을 분리하게 한다. 이행 요약에 따르면 Nuclear Island 제어 계통에서 Reactor Protection System으로의 직접 통신은 없고, Reactor Protection System에서 제어 계통으로는 data diode나 hardwired 연결로 단방향 통신하며, 공유 센서는 SR%%t:SR%% 격리 하드웨어로 격리된다.

기준 25는 반응도 제어 계통의 단일 오작동을 고려해도 AOO%%t:AOO%% 중 SARRDL%%t:SARRDL%%을 넘지 않도록 보호 계통을 설계하게 한다. 이행 요약은 반응도 제어 계통의 단일 고장이 있어도 scram과 engineered safety feature 기능이 SARRDL%%t:SARRDL%%을 지키고, 한 division 고장이 안전 기능 완수를 막지 않으며, `NI Control System`이 Rod Monitoring and Control System과 Coolant Temperature Monitoring and Control System의 power runback으로 반응도를 제어하되 Reactor Protection System과 독립이라고 적는다. 조문은 single malfunction을, 이행 요약은 single failure를 적는다.

기준 26은 적어도 두 반응도 제어 계통이나 수단이 네 가지를 제공하게 한다. 정상 운전과 AOO%%t:AOO%%에서 오작동 여유를 두고 SARRDL%%t:SARRDL%%을 지키며 안전 정지를 달성·유지하는 음의 반응도 삽입, 다른 수단과 independent and diverse하게 계획된 정상 출력 변화의 반응도 변화 속도를 제어하는 수단, 가정 사고 뒤 노심 냉각 능력을 유지하며 안전 정지 상태를 달성·유지하는 수단, 핵연료 장전·검사·수리 같은 개입 조건에서 정지를 유지하는 수단이다. 이행 요약에 따르면 두 수단은 rod de-latch와 rod motor drive이다. Reactor Protection System이 de-latch로 primary와 secondary 제어봉 세트를 중력 낙하시킨 뒤 rod motor drive로 완전 삽입하며, 두 수단 사이에 공통원인 고장이 없고 두 세트의 다발 형상이 달라 모든 제어봉에 영향을 주는 공통원인 고장을 막는다. 오작동은 가장 큰 가치의 제어봉이 완전 인출 상태로 남는 시나리오(여유를 두고 hot standby 달성)와 한 세트가 삽입되지 않는 시나리오(사건 뒤 안전 정지 달성)로 고려한다. rod motor drive는 계획된 정상 출력 변화에서 SARRDL%%t:SARRDL%%을 지키는 independent and diverse 수단이며, 개입 조건의 정지는 완전 삽입된 제어봉과 둘 이상의 제어봉 다발 인출을 막는 행정 관리로 유지한다.

기준 28은 반응도 증가량과 증가 속도에 적절한 한계를 두어 가정 반응도 사고가 primary coolant boundary의 safety-significant elements에 limited local yielding을 넘는 손상을 주거나 노심 냉각 능력을 크게 해치지 않게 한다. 이행 요약은 Reactor Enclosure System의 구동 기구·구동 라인 지지와 정렬, 제어봉 최대 인출 속도 제한, 한 번에 둘 이상 인출을 막는 interlock, 구동 기구 brake를 든다. 기준 29는 AOO%%t:AOO%%에서 보호·반응도 제어 계통이 안전 기능을 수행할 확률이 극히 높게 한다.

## 관련 문서
- [[Natrium_PDC_Development]]
- [[SFR_DC_Protection_Systems]]
- [[SFR_DC_Reactivity_Control]]
- [[Natrium_Control_Heat_Generation]]
- [[PSAR_ch05]]
