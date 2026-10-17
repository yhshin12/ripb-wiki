---
type: natrium
aliases: []
sources:
- ACRS_ML25293A458
- PSAR_ch05
- PSAR_ch07
status: disputed
verified: 2026-09-16
term: null
tags:
- natrium
- nrc-review
terms_pending: []
---

# Kemmerer Unit 1 Control Rod Drive System과 반응도 제어에 대한 NRC 직원 검토 (NRC Staff Review of Kemmerer Unit 1 Control Rod Drive and Reactivity Control)

> [!abstract] 요약
> 이 발표에서 NRC 직원은 Kemmerer Unit 1 제어봉 구동 계통의 중력 scram, 전력 상실 scram, driveline scram follow 설계와, 반응도 제어 계통·반응도 한계·primary coolant boundary 관련 principal design criteria%%t:PDC%% 검토 결과를 설명한다. 직원은 motor drive 기능의 독립성, 제어봉 집합체 설계의 다양성, `AST` 사용에 근거해 PDC%%t:PDC%% 26 접근을 수용 가능하다고 판단했고, rod insertion limit은 operating license%%t:OL%% 단계에서 식별될 예정이다.

## 원문 사실
- "Moves control rods in and out of the core and provides scram functions" [ACRS_ML25293A458 Control rod drive system (CRD) p.14]
- "Control rod drive mechanism (CRDM)" [ACRS_ML25293A458 Control rod drive system (CRD) p.14]
- "CRD motor drive assembly & controller" [ACRS_ML25293A458 Control rod drive system (CRD) p.14]
- "Control rod driveline assembly" [ACRS_ML25293A458 Control rod drive system (CRD) p.14]
- "Scram valve and cylinder assembly" [ACRS_ML25293A458 Control rod drive system (CRD) p.14]
- "DL3-RC1 Reactor scram" [ACRS_ML25293A458 Control rod drive system (CRD) p.14]
- "DL3-RC2 Reactor scram on loss of power" [ACRS_ML25293A458 Control rod drive system (CRD) p.14]
- "DL4-RC3 CRD driveline scram follow" [ACRS_ML25293A458 Control rod drive system (CRD) p.14]
- "DL3-RR1 Primary coolant boundary" [ACRS_ML25293A458 Control rod drive system (CRD) p.14]

![[ACRS_ML25293A458_Slide_14.png]]

- "Normal scram (DL3-RC1)" [ACRS_ML25293A458 Gravity scram functions p.15]
- "Reactor trip breakers are opened by RPS, scram SOVs de-energize , pressure from scram cylinder vents, gripper disengages from CRA, CRA falls into core by gravity" [ACRS_ML25293A458 Gravity scram functions p.15]
- "Scram on loss of power (DL3-RC2)" [ACRS_ML25293A458 Gravity scram functions p.15]
- "RPS signal or loss of power causes loss of voltage to RTB undervoltage coils, which causes undervoltage release mechanism to open RTBs" [ACRS_ML25293A458 Gravity scram functions p.15]
- "After RTBs open, same as above" [ACRS_ML25293A458 Gravity scram functions p.15]
- "Alternative shunt trips (DL4-RC6 and subfunctions)" [ACRS_ML25293A458 Gravity scram functions p.15]
- "AST provides alternate means of tripping RTBs via shunt trip feature" [ACRS_ML25293A458 Gravity scram functions p.15]
- "All elements supporting DL3-RC1 and RC2 are SR, designed with materials consistent with ASME Section III Division 5 (III-5), and subject to SR mechanical and electrical EQ" [ACRS_ML25293A458 Design to support gravity scram functions p.16]
- "CRD driveline assembly has some components made of Alloy 718 which is approved in III-5 for bolting applications only" [ACRS_ML25293A458 Design to support gravity scram functions p.16]
- "Sodium aerosol effect on CRD components mitigated by inert cover gas flow and bellows" [ACRS_ML25293A458 Design to support gravity scram functions p.16]
- "Scram system consists of 3 SOVs configured such that single failure would not cause loss of scram function" [ACRS_ML25293A458 Design to support gravity scram functions p.16]
- "Common cause failure considered in PRA and drives DL3-RC1 failure" [ACRS_ML25293A458 Design to support gravity scram functions p.16]
- "On receipt of driveline scram follow signal, CRD motors drive control rods in at maximum speed" [ACRS_ML25293A458 CRD driveline scram follow p.17]
- "RPS issues control signal (separate and independent from scram signal) to initiate motor drive in when any automatic or manual scram occurs" [ACRS_ML25293A458 CRD driveline scram follow p.17]
- "Supported by NSRST motor drive and associated controllers" [ACRS_ML25293A458 CRD driveline scram follow p.17]
- "Drive motors located on top of CRDM housing, motor controllers located in substructure of NI control building (NCB)" [ACRS_ML25293A458 CRD driveline scram follow p.17]
- "Functions independently of gripper release" [ACRS_ML25293A458 CRD driveline scram follow p.17]
- "PDCs related to quality and protection from phenomena (1, 2, 4, 80)" [ACRS_ML25293A458 Review of CRD p.18]
- "Designed to III-5, qualified under electrical/mechanical EQ for environmental conditions, and seismically qualified (SCS1 for SR and SCN1 for NSRST)" [ACRS_ML25293A458 Review of CRD p.18]
- "Minimum of two reactivity control systems or means must provide capability to:" [ACRS_ML25293A458 PDC 26 – Reactivity Control Systems p.19]

| 번호 | PDC 26 capability | Credited Capability | 출처 |
|---|---|---|---|
| 1) | insert negative reactivity at sufficient rate and amount to ensure SARRDLs are not exceeded and safe shutdown is achieved and maintained for AOOs; | Delatch and gravity scram of primary and secondary CRA. Reactor can be shut down with both banks assuming highest worth rod stuck out, or either bank. RPS or AST can cause a scram. | [ACRS_ML25293A458 PDC 26 – Reactivity Control Systems p.19] |
| 2) | independent and diverse from (1), (3), and (4), control the rate of reactivity changes during planned, normal power changes to ensure SARRDLs are not exceeded; | Motor drive control, with diversity provided by separate sets of CRAs. Secondary CRAs provide regulating function for small reactivity changes. | [ACRS_ML25293A458 PDC 26 – Reactivity Control Systems p.19] |
| 3) | cool the core, shut down the reactor, and maintain safe shutdown following a postulated accident; | Same means as (1) | [ACRS_ML25293A458 PDC 26 – Reactivity Control Systems p.19] |
| 4) | maintain the reactor shutdown during fuel loading, inspection and repair activities | Primary and secondary CRA insertion plus administrative controls for managing shutdown margin. | [ACRS_ML25293A458 PDC 26 – Reactivity Control Systems p.19] |

- "Based on the independence of the motor drive function from the gravity scram function, the diversity of CRA designs to mitigate common cause failures, and the use of AST, staff found the approach to PDC 26 acceptable." [ACRS_ML25293A458 PDC 26 – Reactivity Control Systems p.19]
- "PDC 28 requires limits on amount and rate of reactivity increase to ensure primary coolant boundary and core are not damaged" [ACRS_ML25293A458 PDC 28 – Reactivity Limits p.20]
- "CRA worth available for withdrawal is limited by core design and administratively by identification of appropriate rod insertion limits" [ACRS_ML25293A458 PDC 28 – Reactivity Limits p.20]
- "RILs not identified at CP but expected at OL" [ACRS_ML25293A458 PDC 28 – Reactivity Limits p.20]
- "Limit on CRA withdrawal rate is provided by physical design of CRD motor drives and interlocks that only enable one rod to be withdrawn from the core at a time" [ACRS_ML25293A458 PDC 28 – Reactivity Limits p.20]
- "CRDM housing attaches to rotatable plug assembly (RPA) on reactor head (RH) and forms portion of primary coolant boundary" [ACRS_ML25293A458 Primary coolant boundary PDCs (14, 15, 30, 31, 32) p.21]
- "CRDM housing is designed consistent with III-5, with overpressure protection provided by sodium cover gas system (SCG)" [ACRS_ML25293A458 Primary coolant boundary PDCs (14, 15, 30, 31, 32) p.21]

![[ACRS_ML25293A458_Slide_21.png]]

- "AST - Alternative Shunt Trip" [ACRS_ML25293A458 Acronyms p.22]

| PSF ID | PSF Description | NSRST SSC Safety Significance Criteria (Risk-Significant or DID) | 출처 |
|---|---|---|---|
| DL4-RC4 | Automatic Seismic Trip | Required for DID Adequacy | [PSAR_ch05 Table 5.2-4 p.17] |
| DL4-RC6 | Alternative Shunt Trip | Risk-Significant Function | [PSAR_ch05 Table 5.2-4 p.17] |

| PSF ID | SSC(s) | 출처 |
|---|---|---|
| DL4-RC4 | Anticipatory Automatic Seismic Trip System (AST) | [PSAR_ch05 Table 5.2-4 p.17] |
| DL4-RC4 | NI DC Power Supply System (NDC) | [PSAR_ch05 Table 5.2-4 p.17] |
| DL4-RC4 | NI Uninterruptible AC Power Supply System (NUP) | [PSAR_ch05 Table 5.2-4 p.17] |
| DL4-RC4 | Reactor Protection System (RPS) | [PSAR_ch05 Table 5.2-4 p.17] |
| DL4-RC6 | See Note 1 | [PSAR_ch05 Table 5.2-4 p.17] |

- "DL4-RC6(a-d) is identified as a defense line function in the most recent revision of the PRA." [PSAR_ch05 Table 5.2-4 Note 1 p.20]
- "The requirement has not yet been integrated into the design and is therefore not discussed further in the construction permit application." [PSAR_ch05 Table 5.2-4 Note 1 p.20]
- "The Anticipatory Automatic Seismic Trip System (AST) measures ground motion, applies required signal processing and logic, and automatically generates output actuation signals to the Reactor Trip Breakers (RTBs) through the interface device provided by the Reactor Protection System (RPS) when required by seismic conditions." [PSAR_ch07 §7.6.8.1 p.320]
- "The AST is used during seismic beyond design basis events greater than the safe shutdown earthquake to scram the reactor before the peak seismic wave reaches the facility." [PSAR_ch07 §7.6.8.1 p.320]
- "If the signal processing unit output exceeds the bi-stable unit setpoint, then the bi-stable unit ouputs an isolated signal to the shunt trip feature in the RTB." [PSAR_ch07 §7.6.8.1.1 p.320]
- "The AST is designed to perform a non-safety-related with special treatment (NSRST) function." [PSAR_ch07 §7.6.8.2 p.320]

## 해설
Control Rod Drive System은 제어봉을 노심 안팎으로 움직이고 scram 기능을 제공하며, 핵심 기기로는 control rod drive mechanism, motor drive assembly와 controller, control rod driveline assembly, scram valve와 cylinder assembly가 있다. safety-significant 기능은 원자로 scram(DL3-RC1), 전력 상실 시 scram(DL3-RC2), driveline scram follow(DL4-RC3), primary coolant boundary(DL3-RR1)이다.

정상 scram(DL3-RC1)에서는 Reactor Protection System이 reactor trip breaker를 열고 scram solenoid operated valve가 소자되어 scram cylinder 압력이 배출되며, gripper가 제어봉 집합체에서 풀려 집합체가 중력으로 낙하한다. 전력 상실 scram(DL3-RC2)에서는 Reactor Protection System 신호나 전력 상실로 차단기 저전압 코일의 전압이 사라져 저전압 해제 기구가 차단기를 열며, 차단기가 열린 뒤는 정상 scram과 같다. alternative shunt trip(DL4-RC6과 하위 기능)은 shunt trip 기능으로 차단기를 여는 대체 수단이다. DL3-RC1과 RC2를 지원하는 모든 요소는 Safety-Related%%t:SR%%이고, `ASME Section III Division 5`에 맞는 재료로 설계되며 SR%%t:SR%% 기계·전기 equipment qualification을 받는다. driveline assembly의 일부 부품은 `III-5`가 볼트 용도로만 승인한 Alloy 718로 만들어진다. 구동 부품에 대한 소듐 에어로졸 영향은 불활성 커버가스(cover gas)%%t:COVER_GAS%% 흐름과 bellows로 완화한다. scram 계통은 single failure로 scram 기능을 잃지 않게 배치된 solenoid operated valve 세 개로 이루어지며, common cause failure%%t:CCF%%는 PRA에서 고려되며 DL3-RC1 고장의 주된 요인이다.

driveline scram follow 신호를 받으면 구동 모터가 최대 속도로 제어봉을 밀어 넣는다. Reactor Protection System은 자동이나 수동 scram이 일어나면 scram 신호와 분리·독립된 제어 신호로 모터 구동 삽입을 시작하고, 이 기능은 Non-Safety-Related with Special Treatment%%t:NSRST%% 모터 구동과 제어기가 지원한다. 구동 모터는 구동 기구 housing 위에, 제어기는 `NI control building`의 substructure에 있으며, 기능은 gripper 해제와 독립적으로 작동한다. 품질과 현상 방호 관련 PDC%%t:PDC%% 1, 2, 4, 80은 `III-5` 설계, 환경 조건에 대한 전기·기계 equipment qualification, 내진 검증(SR%%t:SR%%은 `SCS1`, NSRST%%t:NSRST%%는 `SCN1`)으로 다룬다.

PDC%%t:PDC%% 26은 최소 두 반응도 제어 계통 또는 수단이 네 가지 능력을 제공하도록 요구하며, 발표는 능력마다 credit된 수단을 대응시킨다. Anticipated Operational Occurrence%%t:AOO%%에서 specified acceptable system radionuclide release design limit%%t:SARRDL%%을 넘지 않고 안전 정지를 달성·유지하는 음의 반응도 삽입은 primary·secondary 제어봉 집합체의 delatch와 중력 scram으로 이루어지며, 가장 큰 가치의 제어봉 하나가 인출 위치에 고착(stuck out)되었다고 가정해도 두 bank로, 또는 어느 한 bank만으로 정지할 수 있고, Reactor Protection System이나 `AST`가 scram을 일으킬 수 있다. 계획된 정상 출력 변화의 반응도 변화 속도 제어는 별개 제어봉 집합체 세트로 다양성을 둔 motor drive 제어이고, secondary 집합체가 작은 반응도 변화의 조절을 맡는다. 가정 사고 뒤 노심 냉각, 원자로 정지, 안전 정지 유지는 첫째와 같은 수단이고, 핵연료 장전·검사·수리 중 정지 유지는 primary·secondary 제어봉 집합체 삽입에 shutdown margin 관리를 위한 행정 관리를 더한 것이다. 직원은 motor drive 기능이 중력 scram과 독립이고, 제어봉 집합체 설계가 공통원인 고장을 완화하도록 다양하며, `AST`를 쓴다는 점에 근거해 PDC%%t:PDC%% 26 접근을 수용 가능하다고 판단했다.

PDC%%t:PDC%% 28에 대해서는 인출 가능한 제어봉 가치가 노심 설계와 rod insertion limit으로 제한되며, rod insertion limit은 construction permit%%t:CP%%에서 식별되지 않았고 OL%%t:OL%%에서 식별될 예정이다. 인출 속도 한계는 구동 모터의 물리적 설계와 한 번에 한 제어봉만 인출하게 하는 interlock이 제공한다. primary coolant boundary 관련 PDC%%t:PDC%%에 대해서는 구동 기구 housing이 원자로 헤드의 rotatable plug assembly에 붙어 경계의 일부를 이루고, `III-5`에 맞게 설계되며 Sodium Cover Gas System이 과압 보호를 제공한다.

이 발표의 약어표는 `AST`를 Alternative Shunt Trip으로 풀이한다. `PSAR` 5장의 Non-Safety-Related with Special Treatment 기능 표는 자동 지진 trip(DL4-RC4)의 Structures, Systems, and Components%%t:SSC%% 칸 네 항목 가운데 하나를 Anticipatory Automatic Seismic Trip System(`AST`)으로 적고, alternative shunt trip(DL4-RC6)의 SSC%%t:SSC%% 칸은 주석으로 넘긴다. 그 주석은 alternative shunt trip 계열이 최신 PRA 개정에서 defense line 기능으로 식별되었지만 요건이 아직 설계에 반영되지 않아 CP%%t:CP%% 신청에서 더 다루지 않는다고 적는다. `PSAR` Chapter 7도 `AST`를 Anticipatory Automatic Seismic Trip System으로 적으며, 이 계통은 지반 운동을 측정해 Safe Shutdown Earthquake%%t:SSE%%를 넘는 지진 Beyond Design Basis Event%%t:BDBE%%에서 최대 지진파가 도달하기 전에 원자로를 정지시키고, signal processing unit 출력이 bi-stable unit setpoint를 넘으면 bi-stable unit이 reactor trip breaker의 shunt trip 기능으로 신호를 보내며, NSRST%%t:NSRST%% 기능을 수행하도록 설계된다. 따라서 발표 약어표의 `AST`는 기능(alternative shunt trip)을, `PSAR`의 `AST`는 계통을 가리키며, 원문상 두 기능 모두 reactor trip breaker의 shunt trip을 거친다. 직원의 PDC%%t:PDC%% 26 판단은 `AST` 사용을 근거의 하나로 드는데, 이 판단과 `PSAR` 5장 주석의 설계 반영 상태 사이의 관계는 원문만으로 판정되지 않는다.

## 관련 문서
- [[Natrium_NRC_Review_Core_Design]]
- [[Natrium_Control_Heat_Generation]]
- [[Natrium_PDC_Reactivity_Control]]
- [[Natrium_NSRST_Functions]]
- [[Natrium_SR_Functions_Heat_Generation]]
- [[ACRS_ML25293A458]]
- [[PSAR_ch05]]
- [[PSAR_ch07]]
- [[Natrium_SER_Core_Fuel_Design_Review]]
