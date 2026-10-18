---
type: natrium
aliases: []
sources: [SER_KU1_CP]
status: checked
verified: 2026-10-17
term:
tags: [natrium, instrumentation-control, electrical, structures, nrc-review]
terms_pending: []
---
# NRC의 계측제어·전기·건물 평가 (NRC Evaluation of I&C, Electrical Systems, and Buildings)

> [!abstract] 요약
> NRC staff는 계측제어 계통, 전기 계통, 원자로·핵연료 취급·보조·제어 건물의 예비 설계 정보가 construction permit 발급에 충분하다고 결론지었다. 계측제어 검토 범위는 설계 성숙도 때문에 제한되었고 상세 검토는 operating license 단계로 넘겼다. 자동 지진 트립은 `RPS` 경로와 이와 다양한 `AST` 경로로 원자로 트립 차단기를 여는 Non-Safety-Related with Special Treatment%%t:NSRST%% 기능이다. `PSAR`에 따르면 Design Basis Accident%%t:DBA%% 대응 시 Safety-Related%%t:SR%% scram과 공학적 안전설비 기능에는 전력이 필요하지 않다.

## 원문 사실
- "Due to the preliminary nature of the KU1 I&C design the CP application review scope was limited to the DRG and DNRL-ISG-2022-01 items above. Detailed review of the I&C design will be performed at the OL stage when final design details are available." [SER_KU1_CP §7.6.1 p.545]
- "There are no direct digital data communications from either the NSRST or NST systems to the SR systems." [SER_KU1_CP §7.6.1 p.545]
- "The staff notes that 10 CFR 50.55a(h) incorporates by reference IEEE 603-1991, not the newer edition, IEEE 603-2018." [SER_KU1_CP §7.6.1.1.1 p.545]
- "The staff determined that this comparison demonstrating compliance with IEEE 603-1991 can reasonably be left for later consideration at the OL stage because a final design is needed to demonstrate full compliance and the standards are largely aligned." [SER_KU1_CP §7.6.1.1.1 p.545]
- "PSAR section 7.6.2 describes the NIC, a digital system with both NSRST and NST functions." [SER_KU1_CP §7.6.2 p.546]
- "The portions of the RPS that support these safety functions are arranged into four redundant divisions (A, B, C, and D)." [SER_KU1_CP §7.6.3 p.553]
- "The RPS also provides the capability to manually initiate each reactor scram and ESF actuation function from the MCR, although these manual functions are not credited in the safety analysis. These manual reactor scram and ESF control circuits are diverse from the RPS automatic logic." [SER_KU1_CP §7.6.3 p.553]
- "The RadICS platform, as described in the RadICS TR, is used for the RPS. The generic open items and plant-specific action items described in sections 6.0 and 7.0 of the SE for the RadICS TR will be provided at the OL stage." [SER_KU1_CP §7.6.3 p.553]
- "It actuates when at least two out of the four divisions independently determine such action is required." [SER_KU1_CP §7.6.3.1.8 p.558]
- "Because of the reliability of the gravity scram function, no AOOs or DBEs rely on the motor-driven scram function. Additionally, because DL4-RC3 is NSRST, it is not used to mitigate any DBAs." [SER_KU1_CP §7.6.3.1.11.3 p.562]
- "The RPS supports the NSRST function DL4-RC4, “Automatic seismic trip,” by opening the RTBs upon receipt of a seismic trip demand signal from the anticipatory automatic seismic trip system (AST). PSAR table 5.2-4 identifies that DL4-RC4 is required for DID adequacy with no associated LBEs." [SER_KU1_CP §7.6.3.1.11.4 p.562]
- "For DID, the XIS is designed as an analog system that does not contain software and therefore has no credible common-cause failure, consistent with clause 5.16 of IEEE 603-2018." [SER_KU1_CP §7.6.4.1.1 p.565]
- "No automatic control actions are provided by RMS." [SER_KU1_CP §7.6.6.1.1 p.576]
- "Additionally, PSAR section 7.6.7.1 states that no SR operator actions are required from the MCR." [SER_KU1_CP §7.6.7 p.580]
- "PSAR section 7.6.8 describes the AST. The AST measures ground motion, applies required signal processing and logic, and automatically generates output actuation signals to the RTBs through the interface device provided by the RPS. The AST is used during seismic BDBEs greater than the SSE to scram the reactor before the peak seismic wave reaches the facility." [SER_KU1_CP §7.6.8 p.581]
- "The AST consists of four channels placed in four different quadrants equidistantly spaced around the RXB. The RTB arrangement constitutes 2-out-of-4 logic for the reactor scram function." [SER_KU1_CP §7.6.8 p.581]
- "The AST supports the NSRST function DL4-RC4, “Automatic seismic trip,” by continuously monitoring signal inputs from triaxial accelerometers and sending an isolated signal to the shunt trip feature in the RTBs when the signal inputs exceed a bi-stable setpoint." [SER_KU1_CP §7.6.8.1.7 p.584]
- "Though not described in PSAR chapter 1, the alternative shunt trip discussed briefly in PSAR chapters 3 and 5 provides a DID pathway for tripping the reactor trip breakers and initiating a gravity scram." [SER_KU1_CP §1.3.3.3.2 p.43]
- "The following are NSRST alternative shunt trips that are identified as risk-significant defense line functions in PSAR table 5.2-4, but are not described in detail within the PSAR due to the timing of when USO added them to the PRA relative to the submittal of the PSAR:" [SER_KU1_CP §5.5 p.354]
- "PSAR section 7.7.1.3.1 states that during a loss of all AC power event, inverters remain powered by the batteries for 72 hours (Divisions A and B) and 2 hours (Divisions C and D) to keep the NSRST loads energized." [SER_KU1_CP §7.7.1.1 p.586]
- "PSAR section 7.7.1.2 states that electric power is not required in order to meet the SARRDLs for AOOs or postulated accidents. The SR scram and ESF functions discussed in PSAR section 7.6 are accomplished without the need for electric power in response to DBAs." [SER_KU1_CP §7.7.1.5 p.588]
- "The RXB substructure is classified as SR." [SER_KU1_CP §7.8.1 p.590]
- "The RXB superstructure is classified as NST." [SER_KU1_CP §7.8.1 p.590]
- "PSAR section 7.8.1.1.2 states that the HAA, which is part of the RXB substructure, provides a functional containment boundary that performs a radionuclide retention function." [SER_KU1_CP §7.8.1.1.3 p.592]
- "The NSRST barrier function DL4-RR1 refers to the functional containment boundary formed around the RES by the HAA barrier, the GV, and the HAA HVAC isolation. The sub-function DL4-RR1a represents the HAA portion of the boundary." [SER_KU1_CP §7.8.1.1.8 p.594]
- "The FHB superstructure is classified as NSRST. PSAR section 7.8.2.2 states that the seismic classification of the FHB superstructure is SCN1." [SER_KU1_CP §7.8.2.1.1 p.597]
- "The NRC has not established regulatory guidance or positions for NSRST/NST structural review." [SER_KU1_CP §7.8.2.1.1 p.598]
- "According to USO, the SPRA will not be available until the OL stage, and therefore, the performance targets cannot be confirmed at this time. Nonetheless, the staff determined that the design described in the PSAR provides reasonable assurance that performance targets can be met at the OL stage." [SER_KU1_CP §7.8.2.1.1 p.598]
- "Both below and above grade RAB structures support NSRST systems and are classified as NSRST." [SER_KU1_CP §7.8.3 p.599]
- "The below grade substructure and above grade superstructure are classified as SR and NSRST, respectively." [SER_KU1_CP §7.8.4 p.602]
- "The staff determined that the preliminary RPS design is consistent with DL4-RC4, as it provides adequate DID by opening the RTBs upon receipt of a seismic trip demand signal that is diverse from the isolated signal from the AST to the shunt trip feature of the RTBs." [SER_KU1_CP §7.6.3.1.11.4 p.562]
- "The staff determined that the preliminary AST design is consistent with DL4-RC4 because it provides adequate DID as the AST sends an isolated signal to the shunt trip feature in the RTB, diverse from the RPS, that opens the RTBs upon receipt of a seismic trip demand signal." [SER_KU1_CP §7.6.8.1.7 p.584]
- "as well as by the alternative shunt trip (DL4-RC6), which provides an alternate means of tripping the reactor trip breakers." [SER_KU1_CP §7.2.5.1.8 p.496]
- "Alternative shunt trip on high core exit temperature" [SER_KU1_CP §5.5 p.354]
- "Alternative shunt trip on low primary sodium pump outlet pressure" [SER_KU1_CP §5.5 p.354]
- "Alternative shunt trip on high IHT level" [SER_KU1_CP §5.5 p.354]
- "Alternative shunt trip on low IHT level" [SER_KU1_CP §5.5 p.354]
- "PSAR section 7.6.1 states the I&C systems are designed in accordance with IEEE 603-2018" [SER_KU1_CP §7.6.1.1.1 p.545]
- "consistent with PDC 21, the SR portions of the RPS are arranged into four redundant and independent divisions." [SER_KU1_CP §7.6.3.1.8 p.558]
- "If embedded digital devices are procured, guidance from SECY-22-0076 will be used." [SER_KU1_CP §7.6.4.1.1 p.565]
- "Based on the review described above, the staff concludes that the information in PSAR section 7.6.1 is sufficient and meets the applicable guidance and regulatory requirements identified in this section and at the beginning of this chapter for the issuance of a CP." [SER_KU1_CP §7.6.1.2 p.546]
- "Based on the review described above, the staff concludes that the information in PSAR section 7.7 is sufficient" [SER_KU1_CP §7.7.2 p.589]
- "Based on the review described above, the staff concludes that the information in PSAR section 7.8.1 is sufficient" [SER_KU1_CP §7.8.1.2 p.595]
- "Risk significance determinations will depend on the reliability of the primary trip function and potential consequences of failure and will be reviewed at the OL stage." [SER_KU1_CP §5.5 p.354]
- "PSAR section 7.8.4.1.2 states that the NCB substructure is designed in accordance with applicable PDC including PDC 2 and PDC 4." [SER_KU1_CP §7.8.4.1.1 p.603]
- "The seismic classification of the NCB substructure is SCS1." [SER_KU1_CP §7.8.4.1.1 p.603]
- "the staff determined that the preliminary design information for the NCB substructure is consistent with PDC 1, 2, and 4." [SER_KU1_CP §7.8.4.1.1 p.603]
- "PSAR section 7.8.4.2.2 states that the NSRST NCB superstructure is required to meet PDC 2 and PDC 4." [SER_KU1_CP §7.8.4.1.1 p.603]
- "The seismic classification is SCN1." [SER_KU1_CP §7.8.4.1.1 p.603]
- "the adequacy of the seismic design will be confirmed or adjusted at the OL to meet required performance targets based on the results of the SPRA" [SER_KU1_CP §7.8.4.1.1 p.604]
- "the staff determined that the preliminary design information for the NCB superstructure is consistent with PDC 1, 2, and 4." [SER_KU1_CP §7.8.4.1.1 p.604]

## 해설
**계측제어.** 설계가 예비 단계여서 construction permit%%t:CP%% 검토 범위는 `DRG`와 `DNRL-ISG-2022-01` 항목으로 제한되었고, 상세 검토는 operating license%%t:OL%% 단계에서 한다. NSRST%%t:NSRST%%나 Non-Safety-Related with No Special Treatment%%t:NST%% 계통에서 SR%%t:SR%% 계통으로 가는 직접 디지털 통신은 없다. `PSAR`는 계측제어 계통이 `IEEE 603-2018`에 따라 설계된다고 적지만 규정이 참조하는 것은 `IEEE 603-1991`이다. staff는 완전한 준수를 보이려면 최종 설계가 필요하고 두 표준이 대체로 정렬되어 있다는 이유로 이 비교를 OL%%t:OL%% 단계로 미뤘다.
- `NIC`는 NSRST%%t:NSRST%%와 NST%%t:NST%% 기능을 함께 가진 디지털 계통이다.
- `PSAR`에 따르면 `RPS`의 SR%%t:SR%% 부분은 네 개의 중복·독립 division으로 구성되고, 네 division 중 둘 이상이 독립적으로 판단하면 작동한다. `RadICS` 플랫폼을 쓰며, 그 `TR` 안전성평가의 일반 미결 항목과 plant-specific 조치 항목은 OL%%t:OL%% 단계에서 제출된다. 주제어실 수동 scram은 안전해석에서 credit하지 않는다. 중력 scram의 신뢰도 때문에 Anticipated Operational Occurrence%%t:AOO%%나 Design Basis Event%%t:DBE%% 가운데 모터 구동 scram에 의존하는 사건은 없다.
- 심층방어(Defense-in-Depth)%%t:DID%% 관점에서 `XIS`는 소프트웨어가 없는 아날로그 계통이어서 credible한 공통원인 고장이 없다. 내장 디지털 장치를 조달하면 `SECY-22-0076` 지침을 쓴다. `RMS`는 자동 제어 동작을 하지 않는다. `PSAR`에 따르면 주제어실에서 필요한 SR%%t:SR%% 운전원 조치는 없다.

**자동 지진 트립과 alternative shunt trip%%t:ALTERNATIVE_SHUNT_TRIP%%.** `AST`는 지반 운동을 측정해 원자로 트립 차단기로 신호를 보내며, Safe Shutdown Earthquake%%t:SSE%%보다 큰 지진 Beyond Design Basis Event%%t:BDBE%%에서 최대 지진파가 도달하기 전에 원자로를 정지시키려는 계통이다. `AST`는 네 채널로 구성되고 차단기 배열은 2-out-of-4 논리이다. DL4-RC4("Automatic seismic trip")는 NSRST%%t:NSRST%% 기능이며 `PSAR` 표 5.2-4에서 심층방어%%t:DID%% 적정성에 필요하지만 관련 Licensing Basis Event%%t:LBE%%는 없다. `RPS` 쪽은 지진 트립 요구 신호를 받아 차단기를 열고, `AST` 쪽은 차단기의 shunt trip 장치에 격리된 신호를 보낸다. staff는 두 경로가 서로 다양하다는 점을 근거로 각각 DL4-RC4와 정합한다고 판단했다. alternative shunt trip%%t:ALTERNATIVE_SHUNT_TRIP%%(DL4-RC6)은 원자로 트립 차단기를 여는 대체 수단이며, 중력 scram을 시작하는 심층방어%%t:DID%% 경로이다. 노심 출구 고온, 1차 소듐 펌프 출구 저압, `IHT` 고수위·저수위에 대한 alternative shunt trip%%t:ALTERNATIVE_SHUNT_TRIP%%은 risk-significant NSRST%%t:NSRST%% 기능으로 식별되었으나, 사업자가 `PSAR` 제출 시점에 비해 늦게 PRA에 추가해 `PSAR`에 상세히 기술되지 않았다. staff는 이 기능들의 risk significance 판정을 OL%%t:OL%% 단계에서 검토한다.

**전기 계통.** `PSAR`에 따르면 교류 전원 전부 상실 시 NSRST%%t:NSRST%% 부하용 인버터는 배터리로 Division A·B는 72시간, C·D는 2시간 유지된다. `PSAR`는 또 AOO%%t:AOO%%나 사고 시 specified acceptable system radionuclide release design limit%%t:SARRDL%%을 지키는 데 전력은 필요하지 않고, SR%%t:SR%% scram과 공학적 안전설비 기능도 DBA%%t:DBA%%에서 전력 없이 수행된다.

**건물.** 분류는 다음과 같다.
- 원자로 건물: 하부구조 SR%%t:SR%%, 상부구조 NST%%t:NST%%. 하부구조의 일부인 `HAA`가 기능적 격납 경계를 이룬다. DL4-RR1은 `HAA` barrier%%t:BARRIER%%, Guard Vessel%%t:GV%%, `HAA` 공조 격리가 `RES` 주위에 이루는 경계를 뜻하고, DL4-RR1a가 그 `HAA` 부분이다.
- 핵연료 취급 건물 상부구조: NSRST%%t:NSRST%%, 지진 등급 `SCN1`.
- 원자로 보조 건물: 지하·지상 구조 모두 NSRST%%t:NSRST%%.
- `NI` 제어 건물: 지하 하부구조 SR%%t:SR%%, 지상 상부구조 NSRST%%t:NSRST%%.

핵연료 취급 건물 상부구조에 관해 staff는 NRC가 NSRST%%t:NSRST%%·NST%%t:NST%% 구조물 검토에 대한 규제 지침이나 입장을 정하지 않았다고 적는다. 사업자에 따르면 지진 PRA는 OL%%t:OL%% 단계에야 나오므로 성능 목표를 지금 확인할 수 없다. 그래도 staff는 `PSAR`의 설계가 OL%%t:OL%% 단계에서 성능 목표를 충족할 수 있다는 합리적 확신을 준다고 판단했다.

**`NCB` 구조물(보강).** `NCB` 하부구조는 principal design criteria%%t:PDC%% 2와 PDC%%t:PDC%% 4 등에 따라 설계되며 지진 분류는 SCS1이다. NSRST%%t:NSRST%% `NCB` 상부구조는 PDC%%t:PDC%% 2와 PDC%%t:PDC%% 4를 충족해야 하고 지진 분류는 SCN1이며, 지진 설계의 적정성은 OL%%t:OL%% 단계에서 `SPRA` 결과에 따라 확인되거나 조정된다. staff는 두 구조의 예비 설계 정보가 PDC%%t:PDC%% 1, 2, 4와 일치한다고 판단했다.

## 관련 문서
- [[SER_KU1_CP]]
- [[Natrium_System_IC_Architecture]]
- [[Natrium_System_Reactor_Protection]]
- [[Natrium_System_NI_Control]]
- [[Natrium_System_Anticipatory_Seismic_Trip]]
- [[Natrium_System_NI_Auxiliary_Electrical]]
- [[Natrium_Building_Reactor]]
- [[Natrium_Building_Fuel_Handling]]
- [[Natrium_Building_Reactor_Auxiliary]]
- [[Natrium_Building_NI_Control]]
- [[Natrium_SER_BDBE_DBA_Review]]
- [[Natrium_SER_SSC_Design_Review]]
- [[Natrium_SER_IC_PDC_Conformance]]
- [[Natrium_SER_Electrical_Buildings_PDC_Conformance]]
