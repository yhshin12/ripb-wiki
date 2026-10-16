---
type: natrium
aliases: []
sources: [PSAR_ch01]
status: checked
verified: 2026-10-16
term:
tags: [natrium]
terms_pending: []
---
# Natrium Instrumentation and Control 계통 (Natrium Instrumentation and Control Systems)

> [!abstract] 요약
> `PSAR` 1장의 계통 개요는 Natrium Instrumentation and Control 계통이 Licensing Basis Event%%t:LBE%%와 Design Basis Accident%%t:DBA%%의 예방과 결과 완화로 원자로, 발전소, 인원, 공중을 불안전한 운전으로부터 보호하고 안전 정지를 보장한다고 적는다. `RPS`와 Nuclear Instrumentation System(`XIS`)은 각각 이중화된 네 division으로 이루어지고, `NIC`는 Non-Safety-Related with No Special Treatment%%t:NST%%와 Non-Safety-Related with Special Treatment%%t:NSRST%% 기능을 수행하는 여러 감시·제어 하위 계통으로 이루어진다.

## 원문 사실
- "The I&C systems also protect the reactor, plant, personnel, and the public from unsafe operation through the prevention and mitigation of consequences of licensing basis events (LBEs) and design basis accidents (DBAs) and ensures safe shutdown." [PSAR_ch01 §1.1.4.1.10 p.25]
- "The systems implement the fundamental I&C system design principles of qualification, reliability, robustness, security, and defense-in-depth." [PSAR_ch01 §1.1.4.1.10 p.25]
- "The primary function of the RPS is to, with precision and reliability, accept input signals from plant instrumentation, apply necessary logic, and automatically generate output signals to initiate safety functions including reactor scram and engineered safety feature functions when required by plant conditions." [PSAR_ch01 §1.1.4.1.11 p.25]
- "The RPS are arranged into four redundant and independent divisions." [PSAR_ch01 §1.1.4.1.11 p.25]
- "Each RPS division receives two parallel power feeds from the NUP, with each division’s power supply maintaining independence and separation from the others." [PSAR_ch01 §1.1.4.1.11 p.25]
- "The XIS comprises of four redundant divisions, each of which includes a division-specific flux detectors and signal conditioning." [PSAR_ch01 §1.1.4.1.12 p.25]
- "Each XIS division is separate and independent from the other XIS divisions." [PSAR_ch01 §1.1.4.1.12 p.25]
- "The RMS consists of three main subsystems: area radiation monitoring, effluent radiation monitoring, process radiation monitoring." [PSAR_ch01 §1.1.4.1.13 p.25]
- "The effluent radiation monitoring subsystem’s primary function is to protect the health and safety of the public and to provide assurance that off-site exposure does not exceed 10 CFR 20 limits." [PSAR_ch01 §1.1.4.1.13 p.25]
- "Parameters include hot pool level, hot pool temperature, cold pool temperature, and PSP shaft speed." [PSAR_ch01 §1.1.4.1.14 p.26]
- "RIS also provides the RV-GV annulus liquid sodium leak detection parameters as an input to RPS." [PSAR_ch01 §1.1.4.1.14 p.26]
- "The NIC is a group of I&C subsystems that perform non-safety-related with no special treatment (NST) and NSRST functions." [PSAR_ch01 §1.1.4.1.15 p.26]
- "The subsystems that are part of the NIC include the Rod Monitoring and Control System (RMC), the Coolant Temperature Monitoring and Control System (CTC), the Utility Monitoring and Control System (UMC), the Auxiliary Monitoring and Control System (AMC), the Fuel Handling Supervisory Control System (FHC), and the Plant Monitoring and Control System (PMC)." [PSAR_ch01 §1.1.4.1.15 p.26]
- "the RMC includes monitoring, indication, alarm, power runback, normal insertion and withdrawal, and rod withdrawal inhibit functions through the manipulation of the CRD" [PSAR_ch01 §1.1.4.1.16 p.26]
- "While the CTC has no active control function of the RAC, the CTC can influence the RAC performance through control of PHT." [PSAR_ch01 §1.1.4.1.17 p.27]
- "The FHC supports three remote control states, remote automatic, remote step, and remote manual." [PSAR_ch01 §1.1.4.1.20 p.28]
- "The PMC does not have ability to perform automatic control." [PSAR_ch01 §1.1.4.1.21 p.28]
- "The instrumentation and control (I&C) systems provide manual and automatic control of plant systems during modes of operation and transient conditions." [PSAR_ch01 §1.1.4.1.10 p.25]
- "The Nuclear Instrumentation System (XIS) provides instrumentation to sense neutron flux leakage from the core during fuel movement, reactor startup, power operations, shutdown, and accident conditions." [PSAR_ch01 §1.1.4.1.12 p.25]
- "Reactor Instrumentation System (RIS) provides measurements for parameters and sends these signals in an appropriate format to RPS, and NIC, for control, safety functions, post-accident monitoring, and informational purposes." [PSAR_ch01 §1.1.4.1.14 p.26]
- "During normal, startup, shutdown transition operations, anticipated operational occurrences, and design basis events, the RMC includes monitoring, indication, alarm, power runback, normal insertion and withdrawal, and rod withdrawal inhibit functions through the manipulation of the CRD." [PSAR_ch01 §1.1.4.1.16 p.26]
- "The UMC processes information from various sources such as input-output from field devices and from digital interfaces to other systems." [PSAR_ch01 §1.1.4.1.18 p.27]
- "The UMC takes this information and makes it available to the plant data highway for use by the PMC for indication and controls as well as making it available to other NIC systems and resources." [PSAR_ch01 §1.1.4.1.18 p.27]
- "The UMC continually monitors various parameters and variables within the NI for interfacing systems." [PSAR_ch01 §1.1.4.1.18 p.27]
- "It collects data from field instrumentation, such as temperature, pressure, and radiation levels." [PSAR_ch01 §1.1.4.1.18 p.27]
- "It is equipped to perform both manual and automatic controls allowing operators to manage and adjust auxiliary systems as necessary." [PSAR_ch01 §1.1.4.1.18 p.27]
- "Systems the UMC interfaces with include PMC, Seismic Monitoring System (SMS), NI AC Electrical Power Medium Voltage System (NMV), NI AC Electrical Power Low Voltage System (NLV), NI DC Power Supply System (NDC), NI Uninterruptible AC Power Supply System (NUP), NI Heat Tracing System (NHT)." [PSAR_ch01 §1.1.4.1.18 p.27]
- "The AMC processes information from various sources such as input-output from field devices and from digital interfaces to other systems." [PSAR_ch01 §1.1.4.1.19 p.27]
- "The AMC takes this information and makes it available to the plant data highway for use by the PMC for indication and controls as well as making it available to other NIC systems and resources." [PSAR_ch01 §1.1.4.1.19 p.27]
- "The AMC continually monitors various parameters and variables within the NI for interfacing systems." [PSAR_ch01 §1.1.4.1.19 p.27]
- "It collects data from field instrumentation, such as temperature, pressure, and radiation levels." [PSAR_ch01 §1.1.4.1.19 p.27]
- "It is equipped to perform both manual and automatic controls allowing operators to manage and adjust auxiliary systems as necessary." [PSAR_ch01 §1.1.4.1.19 p.27]
- "Systems the AMC interfaces with include PMC, RMS, Gaseous Radioactive Waste System (RWG), Liquid Radioactive Waste System (RWL), Solid Radioactive Waste System (RWS), SCG, and SPS." [PSAR_ch01 §1.1.4.1.19 p.27]

## 해설
Instrumentation and Control 계통은 운전 모드와 과도 조건에서 발전소 계통을 수동·자동으로 제어하며, 또 LBE%%t:LBE%%와 DBA%%t:DBA%%의 예방과 결과 완화로 원자로, 발전소, 인원, 공중을 불안전한 운전으로부터 보호하고 안전 정지를 보장한다. 이 계통들은 qualification, reliability, robustness, security, 심층방어(Defense-in-Depth)%%t:DID%%라는 기본 설계 원칙을 구현한다.

`RPS`의 주 기능은 발전소 계측의 입력 신호를 정밀하고 신뢰성 있게 받아 필요한 논리를 적용하고, 발전소 조건이 요구할 때 원자로 scram과 engineered safety feature 기능을 시작하는 출력 신호를 자동으로 내는 것이다. `RPS`는 이중화되고 독립적인 네 division으로 배치되며, 각 division은 `NUP`에서 두 병렬 전원을 받고 전원의 독립과 분리를 유지한다. `XIS`는 연료 이동, 기동, 출력 운전, 정지, 사고 조건에서 노심의 중성자속 누설을 감지하는 계측을 제공하며, division별 flux detector와 signal conditioning을 갖춘 이중화된 네 division으로 이루어지며, division끼리 분리·독립이다.

`RMS`는 area, effluent, process 방사선 감시의 세 하위 계통으로 이루어지고, effluent 감시 하위 계통의 주 기능은 공중의 건강과 안전을 보호하고 소외 피폭이 `10 CFR 20` 한계를 넘지 않음을 보장하는 것이다. Reactor Instrumentation System(`RIS`)은 제어, 안전 기능, 사고 후 감시, 정보 제공을 위해 변수를 측정해 `RPS`와 `NIC`에 신호를 보낸다. 그 변수에는 hot pool 수위, hot pool 온도, cold pool 온도, `PSP` 축 속도가 있고, `RIS`는 원자로 용기와 guard vessel 사이 annulus의 액체 소듐 누설 탐지 변수를 `RPS`에 입력한다.

`NIC`는 NST%%t:NST%%와 NSRST%%t:NSRST%% 기능을 수행하는 Instrumentation and Control 하위 계통 묶음이며, Rod Monitoring and Control System, Coolant Temperature Monitoring and Control System, Utility Monitoring and Control System, Auxiliary Monitoring and Control System, Fuel Handling Supervisory Control System, Plant Monitoring and Control System을 포함한다. Rod Monitoring and Control System은 정상, 기동, 정지 전환 운전, Anticipated Operational Occurrence%%t:AOO%%, Design Basis Event%%t:DBE%% 동안 Control Rod Drive System 조작으로 감시, 지시, 경보, power runback, 정상 삽입·인출, rod withdrawal inhibit 기능을 수행한다. Coolant Temperature Monitoring and Control System은 Reactor Air Cooling System을 능동 제어하지 않지만 `PHT` 제어로 그 성능에 영향을 줄 수 있다. Fuel Handling Supervisory Control System은 remote automatic, remote step, remote manual 세 원격 제어 상태를 지원하고, Plant Monitoring and Control System은 자동 제어 능력이 없다.

Utility Monitoring and Control System과 Auxiliary Monitoring and Control System은 현장 기기와 다른 계통의 디지털 접속에서 정보를 받아 plant data highway로 `PMC`와 다른 `NIC` 계통에 제공하고, 온도·압력·방사선 준위 같은 현장 계측 자료를 수집하며, 보조 계통을 수동·자동으로 제어할 수 있다. Utility Monitoring and Control System은 `PMC`, Seismic Monitoring System, 중·저압 교류 전원 계통, 직류 전원 계통, 무정전 교류 전원 계통, heat tracing 계통과, Auxiliary Monitoring and Control System은 `PMC`, `RMS`, 기체·액체·고체 방사성 폐기물 계통, `SCG`, `SPS`와 접속한다.

## 관련 문서
- [[Natrium_Reactor_Heat_Transport_Systems]]
- [[Natrium_NRC_Review_Reactivity_Control]]
- [[Natrium_SSC_Safety_Classification]]
- [[PSAR_ch01]]
