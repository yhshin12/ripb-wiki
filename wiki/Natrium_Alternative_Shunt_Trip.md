---
type: natrium
aliases: [DL4-RC6]
sources: [PSAR_ch03, PSAR_ch05, PSAR_ch07, SER_KU1_CP, ACRS_ML25293A458]
status: disputed
verified: 2026-10-30
term: ALTERNATIVE_SHUNT_TRIP
tags: [natrium, reactivity, protection]
terms_pending: []
---
# Natrium alternative shunt trip 기능 (Alternative Shunt Trip, DL4-RC6)

> [!abstract] 요약
> alternative shunt trip은 정상 scram이 실패한 Beyond Design Basis Event%%t:BDBE%%에서 reactor trip breaker를 shunt trip feature로 열어 중력 scram을 시작하는 Non-Safety-Related with Special Treatment%%t:NSRST%% 기능이다. `PSAR`은 이를 risk-significant로 표시하고 네 하위 기능의 트립 변수를 이름으로 적지만, 요건이 아직 설계에 반영되지 않아 Structures, Systems, and Components%%t:SSC%%와 상세 설계를 기술하지 않는다. NRC staff는 한 사건이 operating license%%t:OL%% 단계에서도 uncertainty band가 Design Basis Event 영역에 걸치면 Design Basis Accident%%t:DBA%% 평가가 이 기능을 Safety-Related%%t:SR%%로 올릴 것으로 예상하는 한편, 다른 절에서는 현재 분류가 최종 분류에 비해 적절하거나 보수적일 것으로 예상한다. 이 두 판단의 관계는 `SER`에서 해소되지 않는다.

## 원문 사실
- "DL4-RC6(a-d) is identified as a defense line function in the most recent revision of the PRA. The requirement has not yet been integrated into the design and is therefore not discussed further in the construction permit application." [PSAR_ch05 Table 5.2-4 Note 1 p.20]
- "The following are NSRST alternative shunt trips that are identified as risk-significant defense line functions in PSAR table 5.2-4, but are not described in detail within the PSAR due to the timing of when USO added them to the PRA relative to the submittal of the PSAR:" [SER_KU1_CP §5.5 p.354]
- "Though not described in PSAR chapter 1, the alternative shunt trip discussed briefly in PSAR chapters 3 and 5 provides a DID pathway for tripping the reactor trip breakers and initiating a gravity scram." [SER_KU1_CP §1.3.3.3.2 p.43]
- "Alternative shunt trips (DL4-RC6 and subfunctions)" [ACRS_ML25293A458 Gravity scram functions p.15]
- "AST provides alternate means of tripping RTBs via shunt trip feature" [ACRS_ML25293A458 Gravity scram functions p.15]
- "as well as by the alternative shunt trip (DL4-RC6), which provides an alternate means of tripping the reactor trip breakers." [SER_KU1_CP §7.2.5.1.8 p.496]
- "A shunt trip is also provided in addition to the undervoltage trip to increase the reactor trip breaker and the ESF breaker reliability and diversity." [PSAR_ch05 §5.3.3.4 p.32]
- "the RPS maintains voltage on the RTB undervoltage coils to keep RTBs in the closed position" [PSAR_ch07 §7.6.3.2.2 p.273]
- "In this way, the RPS reactor scram circuit is designed as “de-energize to trip”, consistent with PDC 23." [PSAR_ch07 §7.6.3.2.2 p.273]
- "If DHP-L1PP-4 remains as a BDBE with uncertainty bands that extend into the DBE range at the OL, a new DBA will be needed." [SER_KU1_CP §3.7.1.1 p.264]
- "With the frequencies and consequences included in the PSAR analyses, evaluation of this DBA is anticipated to elevate the alternative shunt trip credited in this LBE from NSRST to SR." [SER_KU1_CP §3.7.1.1 p.264]
- "the staff determined that review of this evaluation can reasonably be deferred to the OL stage based on the preliminary nature of the design." [SER_KU1_CP §3.7.1.1 p.264]
- "In RPD-CW1ACS-4, the normal protection system is assumed to fail to function and the scram breakers are tripped by AST, causing the control rods to fall into the core by gravity." [SER_KU1_CP §3.7.1.3 p.267]
- "The alternative shunt trip circuit scrams the reactor." [PSAR_ch03 §3.8.3.4.1 p.91]
- "The AST supports the NSRST function DL4-RC4, “Automatic seismic trip,” by continuously monitoring signal inputs from triaxial accelerometers and sending an isolated signal to the shunt trip feature in the RTBs when the signal inputs exceed a bi-stable setpoint." [SER_KU1_CP §7.6.8.1.7 p.584]
- "The RTB arrangement constitutes 2-out-of-4 logic for the reactor scram function." [PSAR_ch07 §7.6.8.1.1 p.320]

| PSF | 기능 | 분류 | 연관 LBE | 출처 |
|---|---|---|---|---|
| DL4-RC6 | Alternative Shunt Trip | Risk-Significant Function | BDBE: DHP-L1PP-4, DHP-LOOP-4, DHS-ISTL-4, OTH-LMAC-4, RPD-CW1ACS-4, RPD-SS-4 | [PSAR_ch05 Table 5.2-4 p.17] |
| DL4-RC6a | Alternative Shunt Trip on High Core Exit Temperature | Risk-Significant Function | BDBE: RPD-CW1ACS-4 | [PSAR_ch05 Table 5.2-4 p.17] |
| DL4-RC6b | Alternative Shunt Trip on Low Primary Sodium Pump Outlet Pressure | Risk-Significant Function | BDBE: DHP-L1PP-4, DHP-LOOP-4, OTH-LMAC-4 | [PSAR_ch05 Table 5.2-4 p.17] |
| DL4-RC6c | Alternative Shunt Trip on High High IHT level | Risk-Significant Function | None / N/A | [PSAR_ch05 Table 5.2-4 p.17] |
| DL4-RC6d | Alternative Shunt Trip on Low Low IHT level | Risk-Significant Function | None / N/A | [PSAR_ch05 Table 5.2-4 p.17] |

| 항목 | 값 | 출처 |
|---|---|---|
| DL3-RC1a | Reactor scram on high-high neutron flux | [PSAR_ch07 §7.6.3.2.1 p.268] |
| DL3-RC1b | Reactor scram on high-high hot pool temperature | [PSAR_ch07 §7.6.3.2.1 p.268] |
| DL3-RC1c | Reactor scram on high-high primary sodium level | [PSAR_ch07 §7.6.3.2.1 p.268] |
| DL3-RC1d | Reactor scram on high-high power-to-flow ratio | [PSAR_ch07 §7.6.3.2.1 p.268] |
| DL3-RC1e | Reactor scram on high-high cold pool temperature | [PSAR_ch07 §7.6.3.2.1 p.268] |
| DL3-RC1f | Reactor scram on high-high positive neutron flux rate | [PSAR_ch07 §7.6.3.2.1 p.268] |
| DL3-RC1g | Reactor scram on high-high negative neutron flux rate | [PSAR_ch07 §7.6.3.2.1 p.268] |
| DL3-RC1h | Reactor scram on low-low primary sodium level | [PSAR_ch07 §7.6.3.2.1 p.268] |
| DL3-RC1i | Reactor scram on low power, high neutron flux | [PSAR_ch07 §7.6.3.2.1 p.268] |
| DL3-RC1j | Reactor scram on loss of primary sodium flow | [PSAR_ch07 §7.6.3.2.1 p.268] |

| 항목 | 값 | 분류 | 출처 |
|---|---|---|---|
| Core Exit Temperature | 15 | NSRST | [PSAR_ch07 Table 7.6.5-1 p.303] |
| RTB Enclosure Panel A1 | SR | SCS1 | [PSAR_ch07 Table 7.6.3-1 p.280] |
| RTB Enclosure Panel D2 | SR | SCS1 | [PSAR_ch07 Table 7.6.3-1 p.280] |
- "The staff determined that because these are backups to SR trip functions, the classification of risk-significant NSRST is expected to be appropriate or conservative relative to the final safety classification." [SER_KU1_CP §5.5 p.354]
- "Therefore, the staff determined that the finalization of this aspect of the design can be left to the OL stage" [SER_KU1_CP §5.5 p.354]
- "because they provide redundant trip capability to the SR functions discussed in SE section 5.4." [SER_KU1_CP §5.5 p.354]
- "Unspecified reactor scram (fails), alternative shunt trip on high core exit temperature" [SER_KU1_CP Table 3.7-1 p.280]
- "AST Anticipatory automatic seismic trip system" [SER_KU1_CP Abbreviations and Acronyms p.10]
- "AST - Alternative Shunt Trip" [ACRS_ML25293A458 Acronyms p.22]
- "Alternative shunt trip on high IHT level" [SER_KU1_CP §5.5 p.354]
- "Alternative shunt trip on low IHT level" [SER_KU1_CP §5.5 p.354]

## 해설
**기능의 위치.** 이 기능은 여섯 BDBE%%t:BDBE%%에 연관되며, reactor trip breaker%%t:REACTOR_TRIP_BREAKER%%를 여는 대체 수단이다. `RPS`의 scram 회로는 RTB%%t:REACTOR_TRIP_BREAKER%% undervoltage 코일의 전압을 끊어 트립하는 "de-energize to trip" 방식이고, alternative shunt trip은 차단기의 shunt trip%%t:SHUNT_TRIP%% feature를 쓴다. `PSAR` Chapter 5의 §5.3.3.4는 alternative shunt trip을 따로 지칭하지 않고, 일반적으로 shunt trip%%t:SHUNT_TRIP%%이 undervoltage trip%%t:UNDERVOLTAGE_TRIP%%에 더해 차단기의 신뢰도와 다양성을 높인다고 적는다.

**트립 변수.** 하위 기능 이름이 드러내는 변수는 core exit temperature, primary sodium pump outlet pressure, `IHT` level이다. 위 표의 DL3-RC1a–j 이름에 있는 변수는 neutron flux와 그 변화율, hot·cold pool 온도, primary sodium level, power-to-flow ratio, primary sodium flow이므로, 기능 이름 수준에서 두 목록은 겹치지 않는다. 이것은 이름의 비교이며, DL4-RC6의 입력으로서의 센서 수·위치·측정 원리·설정치와 로직 구현은 vault에 없다. Core Exit Temperature는 `RIS` 변수 표에 NSRST%%t:NSRST%% 계기로 있으나, 이 계기가 DL4-RC6a의 입력인지는 vault에 없다.

**사건 대응.** `PSAR` 기준으로 DL4-RC6a는 한 사건, DL4-RC6b는 세 사건에 대응한다. `SER` Table 3.7-1의 사건 행에는 DL4-RC6a만 하위 기능으로 나타난다. 상위 기능 목록의 DHS-ISTL-4와 RPD-SS-4에는 대응하는 하위 기능이 적혀 있지 않고, DL4-RC6c와 DL4-RC6d는 risk-significant로 표시되어 있으나 `Associated LBE`가 None / N/A이다.

**분류 상태.** 현재 분류는 NSRST%%t:NSRST%%이고 risk-significant이다. §3.7.1.1에서 staff는 DHP-L1PP-4가 OL%%t:OL%%에서도 불확도범위(uncertainty band)%%t:UNCERTAINTY_BAND%%가 Design Basis Event%%t:DBE%% 영역에 걸치는 BDBE%%t:BDBE%%로 남으면 새 DBA%%t:DBA%%가 필요하고, 그 평가가 이 기능을 SR%%t:SR%%로 올릴 것으로 예상한다. 이 평가의 검토는 OL%%t:OL%% 단계로 미루어졌다. §5.5에서 staff는 이 기능이 SR%%t:SR%% trip의 backup이므로 risk-significant NSRST%%t:NSRST%% 분류가 최종 분류에 비해 적절하거나 보수적일 것으로 예상하고, 설계 확정을 OL%%t:OL%% 단계에 맡긴다.

**규정 대비 메모(C81, 상위 dispute).** §3.7.1.1의 상향 예상과 §5.5의 적절하거나 보수적이라는 예상은 같은 기능의 최종 분류에 대해 방향이 다르다. §3.7.1.1은 DHP-L1PP-4가 OL%%t:OL%%에서도 불확도범위%%t:UNCERTAINTY_BAND%%가 DBE%%t:DBE%% 영역에 걸치는 조건을 달지만, 두 문장 어느 쪽도 다른 쪽을 언급하지 않는다. 따라서 권위 문서인 `SER` 안에서 모호하다.

**차단기 배치.** `PSAR` Table 7.6.3-1은 RTB%%t:REACTOR_TRIP_BREAKER%% Enclosure Panel A1부터 D2까지를 SR%%t:SR%%로 적고, seismic trip 절은 RTB%%t:REACTOR_TRIP_BREAKER%% 배치가 "2-out-of-4 logic"을 이룬다고 적는다. 패널 안의 차단기 수, 차단기 기종, alternative shunt trip의 투표 논리는 vault에 없다.

**규정 대비 메모(C7, C59).** 약어 `AST`는 `ACRS` 발표에서 alternative shunt trip이고 `SER`·`PSAR`에서 anticipatory automatic seismic trip system이다. 자동 지진 트립 DL4-RC4도 RTB%%t:REACTOR_TRIP_BREAKER%%의 shunt trip%%t:SHUNT_TRIP%% feature로 신호를 보내며, 두 기능이 회로를 공유하는지는 vault에 없다. 정상 scram 실패 사건의 사건 서술에 있는 `AST` 표기 오기는 [[Natrium_SER_BDBE_DBA_Review]]의 C59 메모에, principal design criteria%%t:PDC%% 판단과의 관계는 [[Natrium_NRC_Review_Reactivity_Control]]의 C7 메모에 기록되어 있다.

**규정 대비 메모(C65, 규정 불일치).** `PSAR`은 DL4-RC6c·d의 이름을 High High·Low Low로, `SER`은 high·low로 적는다. 분류는 같다.

## 관련 문서
- [[Natrium_NSRST_Functions]]
- [[Natrium_System_Reactor_Protection]]
- [[Natrium_System_Anticipatory_Seismic_Trip]]
- [[Natrium_System_Control_Rod_Drive]]
- [[Natrium_NRC_Review_Reactivity_Control]]
- [[Natrium_SER_BDBE_DBA_Review]]
- [[Natrium_BDBE_List]]
- [[Natrium_Control_Heat_Generation]]
