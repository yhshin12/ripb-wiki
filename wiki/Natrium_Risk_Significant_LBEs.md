---
type: natrium
aliases: []
sources:
- PSAR_ch03
- PSAR_ch04
- NEI_18-04
- SER_KU1_CP
status: checked
verified: 2026-10-30
term: null
tags:
- natrium
- lbe
terms_pending: []
---

# Natrium의 Risk-Significant LBE와 high-consequence BDBE (Natrium Risk-Significant LBEs)

> [!abstract] 요약
> 이 보고서는 부지 경계 선량이 `30-day` 동안 2.5 mrem을 넘고 그 선량의 빈도가 Frequency-Consequence Target%%t:FC_TARGET%%의 one percent 안에 있는 Licensing Basis Event%%t:LBE%%를 risk-significant로, 선량이 10 CFR 50.34 기준을 넘는 Beyond Design Basis Event%%t:BDBE%%를 high-consequence로 분류한다. 요약표에서 risk-significant로 표시된 LBE%%t:LBE%%는 모두 `RFH-` 식별자를 가진 사건이고, high-consequence BDBE%%t:BDBE%%는 Ex-Vessel Handling Machine 관련 두 건이다.

## 원문 사실
- "LBEs are classified as risk-significant if the LBE site boundary dose exceeds 2.5 mrem over 30 days and the frequency of the dose is within one percent of the F-C target." [PSAR_ch03 §3.5.1 p.53]
- "BDBEs are classified as high-consequence if the dose exceeds 10 CFR 50.34 criteria." [PSAR_ch03 §3.5.1 p.53]
- "High-consequence BDBEs are identified in Table 3.5-3." [PSAR_ch03 §3.5.1 p.53]
- "Descriptions of the AOO, DBE, and BDBE evaluations, identification of radionuclide sources, risk-significant licensing basis events (LBEs), high-consequence BDBEs, and the event end states are provided in Sections 3.6 through 3.8." [PSAR_ch03 §3.5.1 p.53]
- "Plots of the frequencies, consequences, and uncertainties of the LBEs, with comparison to the NEI 18-04 F-C target, are shown in Figure 3.5-1." [PSAR_ch03 §3.5.1 p.53]
- "Denotes high-consequence BDBE" [PSAR_ch03 Table 3.5-3 p.57-59]
- "The tables show that the risk-significant LBEs maintain margin to the F-C target curve." [SER_KU1_CP §4.2.1.1.1 p.327]
- "The BLTC is not expected to be mated with the PIC during the washing operation. Therefore, the mated BLTC/PIC (DL3-RR5a) is the appropriate radionuclide barrier for the drop events (RFH-FDPI), but not for the washing events (RFH-ESWR)." [SER_KU1_CP §3.6.1.4 p.250]
- "While uncertainty in the design remains, the staff determined that the information provided was sufficient to support the CP based on:" [SER_KU1_CP §3.6.1.4 p.250]
- "The PIC radionuclide retention barrier SSCs are currently classified as SR through the DL3-RR5a SR function." [SER_KU1_CP §3.6.1.4 p.250]
- "The additional preventative controls are expected to reduce the frequencies for these LBEs farther from the F-C target curve, as described in the PIC supplement." [SER_KU1_CP §3.6.1.4 p.250]
- "These are conservative assumptions that could be adjusted as the event specific mechanistic source term is developed at the OL stage." [SER_KU1_CP §3.6.1.4 p.250]
- "For RFH-ESWR-2, a BDBE with a 95th percentile frequency extending into the DBE region, the PIC barrier is assumed to have failed" [SER_KU1_CP §3.8.1.5 p.296]
- "The staff’s review of updated analyses for these events, including any associated DBAs, is being deferred to the OL stage based on the understanding that additional preventative controls will move this event to lower frequencies, and its frequency band will no longer extend into the DBE region." [SER_KU1_CP §3.7.1.5 p.272]
- "The dose criteria in 10 CFR 50.34 include a 2-hour dose criterion of 25 rem TEDE at the EAB and a 25 rem TEDE criterion at the LPZ boundary when calculated for the full duration of the event release." [SER_KU1_CP §3.3.1.8 p.223]
- "The postulated initiating event is a sodium-water reaction in the Pool Immersion Cell (PIC) during fuel handling activities while the PIC and BLTC are mated that causes fuel cladding failure." [PSAR_ch03 §3.9.5.3.1 p.116]

| LBE ID | Title | Risk Significant | 출처 |
|---|---|---|---|
| RFH-FDIV-1 | Fuel Handling Event Occurs While Moving Fuel Assembly in the Reactor Vessel with a Single Assembly Failed and Functional Containment Barriers Successfully Retain Release | Yes | [PSAR_ch03 Table 3.5-2 p.55-56] |
| RFH-FDIV-3 | Fuel Handling Event Occurs While Moving Fuel Assembly in the Reactor Vessel with Two Assemblies Failed and Functional Containment Barriers Successfully Retain Release | Yes | [PSAR_ch03 Table 3.5-2 p.55-56] |
| RFH-FDSP-1 | Fuel Handling Event Occurs While Moving Fuel Assembly in the SFP with a Single Assembly Failed and FHB Barrier Fails to Retain Release | Yes | [PSAR_ch03 Table 3.5-2 p.55-56] |
| RFH-ESWR-2 | Excessive Sodium-Water Reaction in the PIC with PIC and BLTC Barrier Fails to Retain Release (FHB Credited) | Yes | [PSAR_ch03 Table 3.5-3 p.57-59] |
| RFH-ESWR-3 | Excessive Sodium-Water Reaction in the PIC with PIC and BLTC Barrier Fails to Retain Release (FHB Not Credited) | Yes | [PSAR_ch03 Table 3.5-3 p.57-59] |
| RFH-FDBL-2 | Fuel Handling Event Occurs While Moving Fuel Assembly in the BLTC with BLTC Barrier Fails to Retain Release | Yes | [PSAR_ch03 Table 3.5-3 p.57-59] |
| RFH-FDEM-2* | Fuel Handling Event Occurs While Moving Fuel Assembly or an LTA or LDA in the EVHM with EVHM Barrier Fails to Retain Release | Yes | [PSAR_ch03 Table 3.5-3 p.57-59] |
| RFH-FDIV-2 | Fuel Handling Event Occurs While Moving Fuel Assembly in the Reactor Vessel with a Single Assembly Failed and Functional Containment Barriers Fail to Retain Release | Yes | [PSAR_ch03 Table 3.5-3 p.57-59] |
| RFH-FDPI-1 | Fuel Handling Event Occurs While Moving Fuel Assembly in the PIC with PIC Barrier Fails to Retain Release | Yes | [PSAR_ch03 Table 3.5-3 p.57-59] |
| RFH-FDSP-2 | Fuel Handling Event Occurs While Moving Fuel Assembly in the SFP with Two Assemblies Failed and FHB Barrier Fails to Retain Release | Yes | [PSAR_ch03 Table 3.5-3 p.57-59] |
| RFH-LMCA-2* | Loss of EVHM Active Cooling While Handling Fuel Assembly or an LTA or LDA without Passive Cooling, EVHM Barrier Fails to Retain Release | Yes | [PSAR_ch03 Table 3.5-3 p.57-59] |

| LBE ID | 항목 | 5th Percentile | Mean | 95th Percentile | 출처 |
|---|---|---|---|---|---|
| RFH-FDIV-1 | 30-day EAB TEDE [rem] | 8.38E-02 | 1.83E-01 | 2.90E-01 | [PSAR_ch03 §3.7.4.2.3 p.77] |
| RFH-FDIV-1 | Frequency | 8.32E-05 | 2.26E-03 | 8.73E-03 | [PSAR_ch03 §3.7.4.2.3 p.77] |
| RFH-FDIV-3 | 30-day EAB TEDE [rem] | 1.67E-01 | 3.66E-01 | 5.82E-01 | [PSAR_ch03 §3.7.4.3.3 p.78] |
| RFH-FDIV-3 | Frequency | 4.33E-05 | 1.19E-03 | 4.32E-03 | [PSAR_ch03 §3.7.4.3.3 p.78] |
| RFH-FDSP-1 | 30-day EAB TEDE [rem] | 1.20E-01 | 3.31E-01 | 5.05E-01 | [PSAR_ch03 §3.7.4.4.3 p.79] |
| RFH-FDSP-1 | Frequency | 3.24E-05 | 8.77E-04 | 3.36E-03 | [PSAR_ch03 §3.7.4.4.3 p.79] |
| RFH-FDIV-2 | 30-day EAB TEDE [rem] | 3.88E-01 | 6.74E-01 | 1.62E+00 | [PSAR_ch03 §3.8.5.1.3 p.95] |
| RFH-FDIV-2 | Frequency | 3.06E-07 | 2.27E-05 | 8.48E-05 | [PSAR_ch03 §3.8.5.1.3 p.95] |
| RFH-FDSP-2 | 30-day EAB TEDE [rem] | 2.40E-01 | 6.62E-01 | 1.01E+00 | [PSAR_ch03 §3.8.5.3.3 p.96] |
| RFH-FDSP-2 | Frequency | 2.41E-06 | 9.74E-05 | 3.72E-04 | [PSAR_ch03 §3.8.5.3.3 p.96] |
| RFH-ESWR-2 | 30-day EAB TEDE [rem] | 1.20E+00 | 3.31E+00 | 5.05E+00 | [PSAR_ch03 §3.8.5.4.3 p.97] |
| RFH-ESWR-2 | Frequency | 4.90E-07 | 3.40E-05 | 1.61E-04 | [PSAR_ch03 §3.8.5.4.3 p.97] |
| RFH-ESWR-3 | 30-day EAB TEDE [rem] | 1.00E+01 | 1.40E+01 | 2.10E+01 | [PSAR_ch03 §3.8.5.5.3 p.97] |
| RFH-ESWR-3 | Frequency | 3.12E-08 | 1.38E-06 | 4.94E-06 | [PSAR_ch03 §3.8.5.5.3 p.97] |
| RFH-LMCA-2 | 30-day EAB TEDE [rem] | 3.20E+01 | 4.60E+01 | 7.00E+01 | [PSAR_ch03 §3.8.5.7.3 p.99] |
| RFH-LMCA-2 | Frequency | 9.72E-09 | 8.82E-07 | 3.48E-06 | [PSAR_ch03 §3.8.5.7.3 p.99] |
| RFH-FDBL-2 | 30-day EAB TEDE [rem] | 1.00E+01 | 1.40E+01 | 2.10E+01 | [PSAR_ch03 §3.8.5.9.3 p.100] |
| RFH-FDBL-2 | Frequency | 2.41E-08 | 6.10E-07 | 2.33E-06 | [PSAR_ch03 §3.8.5.9.3 p.100] |
| RFH-FDEM-2 | 30-day EAB TEDE [rem] | 3.20E+01 | 4.60E+01 | 7.00E+01 | [PSAR_ch03 §3.8.5.11.3 p.102] |
| RFH-FDEM-2 | Frequency | 7.28E-09 | 5.25E-07 | 1.99E-06 | [PSAR_ch03 §3.8.5.11.3 p.102] |
| RFH-FDPI-1 | 30-day EAB TEDE [rem] | 1.00E+01 | 1.40E+01 | 2.10E+01 | [PSAR_ch03 §3.8.5.15.3 p.104] |
| RFH-FDPI-1 | Frequency | 1.98E-08 | 5.10E-07 | 1.93E-06 | [PSAR_ch03 §3.8.5.15.3 p.104] |

- "LBEs are classified as risk-significant if the LBE site boundary dose exceeds 2.5 mrem over 30 days and the frequency of the dose is within 1% of the F-C Target." [NEI_18-04 §3.2.2 Task 7c p.24]
- "In the LMP framework, an AOO, DBE, or BDBE is regarded as risk-significant if the combination of the upper bound (95%tile) estimates of the frequency and consequence of the LBE are within 1% of the F-C Target AND the upper bound 30-day TEDE dose at the EAB exceeds 2.5 mrem." [NEI_18-04 §6 p.90]
- "To consider the effects of uncertainties, the upper 95th percentile estimates of both frequency and dose should be used." [NEI_18-04 §3.3.5 p.35]
- "DBE doses are evaluated against the F-C Target based on the mean estimates of consequence." [NEI_18-04 §3.2.2 Task 7a p.23]

| LBE Name | LBE Category | 95th Perc. Freq. [/ plant-yr] | 95th Perc. Dose [rem] | 출처 |
|---|---|---|---|---|
| RFH-ESWR-2 | BDBE | 1.31E-04 | 5.05 | [PSAR_ch04 Table 4.2-2 p.13] |

- "Figure 3.5-1 F-C Chart for LBEs with Uncertainty Bands" [PSAR_ch03 Figure 3.5-1 p.62]

![[PSAR_ch03_Fig_3.5-1.png]]

## 해설
판정 문장은 NEI 18-04 Task 7c 본문과 거의 같고 1%를 one percent로 적으며, 빈도와 선량에 평균과 95th percentile 가운데 어느 추정값을 쓰는지 적지 않는다. NEI 18-04는 불확실도를 고려해 빈도와 선량 모두 상위 95th percentile 추정값을 쓰라고 하고 용어집도 상한 추정값의 조합으로 정의하지만, Design Basis Event%%t:DBE%% 선량은 결말의 평균 추정값으로 F-C Target%%t:FC_TARGET%%과 비교한다고도 적는다.

DBE%%t:DBE%% 요약표에서 risk-significant로 표시된 것은 원자로 용기 안 핵연료 이동 중 집합체 하나 또는 둘이 파손되고 functional containment barrier%%t:BARRIER%%가 방출을 가두는 두 사건과, Spent Fuel Pool에서 집합체 하나가 파손되고 Fuel Handling Building barrier%%t:BARRIER%%가 방출을 가두지 못하는 사건이다. BDBE%%t:BDBE%% 요약표에서는 Pool Immersion Cell의 과도한 소듐-물 반응 두 건, bottom loading transfer cask·Ex-Vessel Handling Machine·Pool Immersion Cell의 barrier%%t:BARRIER%% 실패 사건, 원자로 용기 안 단일 집합체 파손과 functional containment barrier%%t:BARRIER%% 실패, Spent Fuel Pool의 두 집합체 파손, 피동 냉각 없는 Ex-Vessel Handling Machine 능동 냉각 상실이 표시된다. 이 가운데 Ex-Vessel Handling Machine barrier%%t:BARRIER%% 실패 사건과 피동 냉각 없는 능동 냉각 상실 사건이 high-consequence BDBE%%t:BDBE%%로 표시된다.

수치 표에 따르면 risk-significant DBE%%t:DBE%% 세 건의 평균 `30-day` Exclusion Area Boundary%%t:EAB%% total effective dose equivalent는 1.83E-01에서 3.66E-01 rem이고, 평균 빈도는 8.77E-04에서 2.26E-03이다. high-consequence BDBE%%t:BDBE%% 두 건의 평균 선량은 모두 4.60E+01 rem(95th percentile 7.00E+01 rem)이고 평균 빈도는 5.25E-07과 8.82E-07이다. 나머지 risk-significant BDBE%%t:BDBE%%의 평균 선량은 6.62E-01에서 1.40E+01 rem이며, Pool Immersion Cell barrier%%t:BARRIER%% 실패 사건의 평균 빈도는 5.10E-07이다. NRC staff는 10 CFR 50.34 선량 기준을 EAB%%t:EAB%%에서 `2-hour` 25 rem total effective dose equivalent%%t:TEDE%%, low-population zone%%t:LPZ%% boundary에서 사건 방출 전 기간에 대해 25 rem TEDE%%t:TEDE%%로 적는다. 이 기준과 위 `30-day` 선량 값의 비교는 이 노트가 인용한 원문에 없다.

`RFH-ESWR-2`의 95th percentile 빈도는 `PSAR` Chapter 3 `§3.8.5.4.3`에서 `1.61E-04`, `PSAR` Chapter 4 `Table 4.2-2`에서 `1.31E-04`로 다르고, 95th percentile 선량 `5.05`는 두 장이 같다. 두 원문이 같은 양을 다르게 적는다([[Natrium_LBE_Risk_Margins]]).

**NRC staff 평가.** NRC staff는 `PSAR` 표에서 risk-significant LBE%%t:LBE%%가 F-C target 곡선에 대해 여유를 유지한다고 확인했다. 또 staff는 Anticipated Operational Occurrence%%t:AOO%%·DBE%%t:DBE%% 평가 절에서 Pool Immersion Cell 세척 사건(RFH-ESWR)에 대해 결합된 cask와 cell을 적절한 방사성핵종 barrier%%t:BARRIER%%로 보지 않는다.

**규정 대비 메모(C1, 신청자 문서 내부 불일치).** `PSAR` Chapter 3과 Chapter 4는 `RFH-ESWR-2`의 95th percentile 빈도를 각각 `1.61E-04`와 `1.31E-04`로 다르게 적는다. `SER`은 이 사건을 95th percentile 빈도가 DBE%%t:DBE%% 영역으로 연장되는 BDBE%%t:BDBE%%로만 적어 어느 값도 배제하지 않으므로, 판정할 권위 조항이 없다. 이 노트는 `1.31E-04`를 기준으로 쓴다. `Table 4.2-2`의 frequency margin이 이 값과 맞기 때문이다. Chapter 3의 `1.61E-04`는 오기로 보이며 차후 확인이 필요하다.

**규정 대비 메모(C64, 규정 불일치).** `PSAR`은 Pool Immersion Cell 소듐-물 반응 사건을 `PIC`와 `BLTC`가 결합된 상태의 사건으로 적는다. `SER`은 세척 중에는 `BLTC`가 `PIC`와 결합되지 않을 것으로 보아, 결합 barrier인 DL3-RR5a는 낙하 사건에는 적절하나 세척 사건에는 적절하지 않다고 적었다. 그럼에도 `SER`은 `PIC` barrier Structures, Systems, and Components%%t:SSC%%가 DL3-RR5a를 통해 Safety-Related%%t:SR%%로 분류된 점, 추가 예방 조치가 빈도를 낮출 것으로 예상되는 점, 선원항(source term)%%t:SOURCE_TERM%% 해석의 가정이 보수적인 점을 근거로 construction permit%%t:CP%% 단계에는 충분하다고 판단했고, 그 가정은 operating license%%t:OL%% 단계에서 사건별 Mechanistic Source Term%%t:MST%%를 개발하며 조정될 수 있다고 적었다.

## 관련 문서
- [[LBE_Risk_Significance]]
- [[Natrium_LBE_Risk_Margins]]
- [[F_C_Target]]
- [[Natrium_LBE_Selection]]
- [[RG_1233_LBE_Staff_Position]]
- [[PSAR_ch03]]
- [[Natrium_SER_Integrated_Evaluation_Review]]
- [[Natrium_SER_AOO_DBE_Review]]
