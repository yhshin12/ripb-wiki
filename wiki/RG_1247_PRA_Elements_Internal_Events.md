---
type: regulation
aliases: []
sources: [RG_1.247, RG_1.253]
status: checked
verified: 2026-10-16
term:
tags: [rg-1247, pra, pra-elements]
terms_pending: []
---
# 비경수형원전 PRA의 내부 사건·정량화 요소 (RG 1.247 PRA Elements: Internal Events, Quantification, Consequence, and Risk Integration)

> [!abstract] 요약
> `RG 1.247` C.1.3은 모든 방사성 원천, hazard, Plant Operating State%%t:POS%%, 분석 수준을 다루는 비경수형원전(non-light-water reactor)%%t:NON_LWR%% PRA에 필요한 요소를 정하고, 하나라도 빠진 PRA는 완전하지 않다고 본다. 이 노트는 내부 사건 요소(POS%%t:POS%%, 기시사건, 사건 경위, 성공 기준, 계통, 인간 신뢰도, 자료)와 정량화·결과 요소(사건 경위 정량화, mechanistic source term, 방사선 결과, risk integration, 문서화)의 목적과 주요 특성을 정리한다. risk integration 요소에 대한 입장은 경수로 지침 `RG 1.200`에는 없던 것이다.

## 원문 사실
- "The characteristics and attributes of the PRA elements define specific requirements that should be met to successfully perform those technical analyses and achieve a defined objective." [RG_1.247 §C.1.3 p.18]
- "Table 1 lists the PRA elements necessary for an acceptable NLWR PRA that addresses all radiological sources, all hazards, all POSs, and all levels of PRA analysis." [RG_1.247 §C.1.3 p.18]
- "A PRA that is missing one or more of these elements would not be considered complete." [RG_1.247 §C.1.3 p.18]

| Table 1 항목 | 출처 |
|---|---|
| plant operating state analysis | [RG_1.247 Table 1 p.18] |
| initiating event analysis | [RG_1.247 Table 1 p.18] |
| event sequence analysis | [RG_1.247 Table 1 p.18] |
| success criteria development | [RG_1.247 Table 1 p.18] |
| systems analysis | [RG_1.247 Table 1 p.18] |
| human reliability analysis | [RG_1.247 Table 1 p.18] |
| data analysis internal flood PRA | [RG_1.247 Table 1 p.18] |
| internal fire PRA | [RG_1.247 Table 1 p.18] |
| seismic PRA | [RG_1.247 Table 1 p.18] |
| hazard screening PRA | [RG_1.247 Table 1 p.18] |
| high wind PRA | [RG_1.247 Table 1 p.18] |
| external flooding PRA | [RG_1.247 Table 1 p.18] |
| other hazards PRA | [RG_1.247 Table 1 p.18] |
| event sequence quantification | [RG_1.247 Table 1 p.18] |
| mechanistic source term analysis | [RG_1.247 Table 1 p.18] |
| radiological consequence analysis | [RG_1.247 Table 1 p.18] |
| risk integration | [RG_1.247 Table 1 p.18] |

- "The staff did not develop a staff position in RG 1.200 on the risk integration PRA element as it relates to LWR PRA acceptability; however, the staff is promulgating a position in this RG on risk integration as it relates to NLWR PRA acceptability given the scope of the ASME/ANS NLWR PRA standard and to address the needs of regulatory submittals." [RG_1.247 §C.1.3 p.19]
- "The objectives of the POS analysis PRA element are to identify operating evolutions (e.g., full-power, LPSD types of conditions) important to risk and parse them into distinct operating states in which the plant conditions are assumed to be relatively constant." [RG_1.247 §C.1.3.1 p.19]
- "The POS safety functions to consider include reactivity control, reactor coolant chemistry control, decay heat removal control, reactor coolant system (RCS) inventory/barrier control, radionuclide transport barrier control, and ex-vessel fission product control (e.g., off-gas tanks/fuel salt storage tanks/spent fuel pools)." [RG_1.247 §C.1.3.1 p.19]
- "POS definitions should include all sources of radioactive material within the scope of the PRA, including ex-vessel sources, unless there is a documented technical justification for excluding ex-vessel sources." [RG_1.247 §C.1.3.1 p.19]
- "The objectives of the initiating event analysis are to identify and characterize events that challenge plant operation during any POSs and that require successful mitigation by plant equipment and personnel to prevent or to mitigate a release of radiological material." [RG_1.247 §C.1.3.2 p.20]
- "Initiating events are grouped so that events in the same group have similar requirements for mitigation." [RG_1.247 §C.1.3.2 p.20]
- "The objective of the event sequence analysis PRA element is to model chronologically (to the extent practical) the different possible progressions of events (i.e., event sequences) that can occur from the start of the initiating event to either successful mitigation or release." [RG_1.247 §C.1.3.3 p.21]
- "The objective of the success criteria analysis PRA element is to determine the minimum requirements for each function (and ultimately the systems used to perform the functions) to prevent or to mitigate a release given an initiating event." [RG_1.247 §C.1.3.4 p.21]
- "The objective of the systems analysis PRA element is to identify the various combinations of failures that can prevent a system from performing its function as defined by the success criteria." [RG_1.247 §C.1.3.5 p.22]
- "The scope of considered HFEs does not include human-induced security events (e.g., sabotage, malevolent acts)." [RG_1.247 §C.1.3.5 p.22]
- "The models include both active and passive components and failure modes that impact the functions of the system." [RG_1.247 §C.1.3.5 p.22]
- "The objectives of the HRA PRA element are to identify and define the HFEs that can negatively impact normal or emergency plant operation and quantify their probabilities." [RG_1.247 §C.1.3.6 p.23]
- "The credit for recovery actions is justified." [RG_1.247 §C.1.3.6 p.23]
- "The data analysis PRA element quantifies the equipment failure probabilities and equipment unavailabilities of the modeled systems." [RG_1.247 §C.1.3.7 p.24]
- "Estimation is based on the relevant generic industry and technology- and design-/plant-specific evidence." [RG_1.247 §C.1.3.7 p.24]
- "The objective of the event sequence quantification analysis PRA element is to develop a frequency estimate of event sequences and event sequence families at any stage of the plant life cycle, while ensuring that all risk-significant contributors are represented and understood." [RG_1.247 §C.1.3.15 p.43]
- "The event sequences are quantified using appropriate models and codes and a truncation limit sufficiently low to show convergence of the PRA results." [RG_1.247 §C.1.3.15 p.43]
- "The objective of the mechanistic source term analysis is to characterize the radiological release to the environment resulting from each event sequence leading to a release." [RG_1.247 §C.1.3.16 p.44]
- "Radionuclide releases are grouped into smaller subsets of representative source terms or release categories." [RG_1.247 §C.1.3.16 p.44]
- "These PRA analysis elements are developed using the assumption that exposure to radionuclides released to the atmosphere is the dominant exposure pathway." [RG_1.247 §C.1.3.17 p.45]
- "These elements do not address exposure due to direct radiation from radiological sources within the facility or exposures due to releases of radioactive material to aqueous pathways such as surface water or ground water." [RG_1.247 §C.1.3.17 p.45]
- "At least one full annual cycle of hourly meteorological data that are representative of long-term meteorological conditions of the site is compiled." [RG_1.247 §C.1.3.17 p.46]
- "The objectives of the risk integration PRA element are to develop criteria used to determine risk significance, to express overall risk in terms of appropriate risk metrics, and to characterize and quantify the uncertainty associated with the calculated risk metrics." [RG_1.247 §C.1.3.18 p.49]
- "At a minimum, relative risk-significance criteria should be used to develop the PRA, including but not limited to Fussell-Vesely or Birnbaum importance measures, unless otherwise justified." [RG_1.247 §C.1.3.18 p.49]
- "The objective of expressing overall risk in terms of appropriate risk metrics is to provide a vehicle by which risk contributions from multiple reactors and other radiological sources can be integrated." [RG_1.247 §C.1.3.18 p.50]
- "The documentation of the PRA model provides the information necessary to easily reproduce and justify results." [RG_1.247 §C.1.3.19 p.51]
- "A source of model uncertainty is one that is related to an issue for which there is no consensus approach or model (e.g., choice of data source, success criteria, human reliability model)." [RG_1.247 §C.1.3.19 p.51]
- "C.1.3.17 (RC) Radiological Consequence Analysis; C.1.3.18 (RI) Risk Integration" [RG_1.253 Table A-1 p.34]

## 해설
**요소의 구성.** PRA 요소의 characteristics와 attributes는 각 기술 해석을 수행하고 목적을 달성하려고 충족해야 할 요구를 정한다. Table 1은 모든 방사성 원천, 모든 hazard, 모든 POS%%t:POS%%, 모든 분석 수준을 다루는 PRA에 필요한 요소를 열거하며, 하나라도 빠진 PRA는 완전하지 않다고 본다. Table 1은 열일곱 개 항목을 글머리로 나열한다. 원문은 자료 분석과 내부 침수를 "data analysis internal flood PRA" 한 항목으로 인쇄하지만, 자료 분석 요소는 §C.1.3.7이 따로 다루고 내부 침수 요소는 [[RG_1247_PRA_Elements_Hazards]]가 다루는 별도 절이다. 문서화(§C.1.3.19)는 Table 1의 항목에 없다. [[RG_1253_CP_PRA_Acceptability]]의 Table A-1 인용에는 C.1.3.1부터 C.1.3.18 Risk Integration까지의 요소가 있다. staff는 경수로 지침 `RG 1.200`에서는 두지 않았던 risk integration 요소의 입장을 이 지침에서 새로 둔다.

**내부 사건 요소.**
- POS%%t:POS%%: 위험에 중요한 운전 변화(전출력, `LPSD`)를 찾아 조건이 비교적 일정한 운전 상태로 나눈다. 고려할 안전 기능에는 반응도 제어, 냉각재 화학 제어, 붕괴열 제거, 냉각재 계통 재고·barrier%%t:BARRIER%% 제어, 방사성핵종 이동 barrier%%t:BARRIER%% 제어, 용기 외 핵분열생성물 제어가 들어간다. 용기 외 원천은 문서화된 기술적 정당화가 없는 한 포함한다.
- 기시사건: 어떤 POS%%t:POS%%에서든 발전소 운전에 도전하고 방출 방지·완화가 필요한 사건을 식별하며, 완화 요구가 비슷한 사건끼리 묶는다.
- 사건 경위: 기시사건부터 완화 성공이나 방출까지의 진행을 가능한 한 시간 순으로 모델링한다.
- 성공 기준: 기시사건에서 방출을 방지·완화하는 데 필요한 기능별 최소 요구를 정한다.
- 계통: 계통 기능을 잃게 하는 고장 조합을 찾고, 능동·피동 기기를 모두 포함한다. 고려하는 human failure event에 보안 사건(사보타주 등)은 들지 않는다.
- 인간 신뢰도: 정상·비상 운전에 악영향을 주는 human failure event를 정의하고 확률을 정량화하며, 복구 조치의 credit은 정당화해야 한다.
- 자료: 모델링한 계통의 기기 고장 확률과 비가용도를 일반 산업 자료와 기술·설계·발전소 고유 자료로 추정한다.

**정량화와 결과 요소.**
- 사건 경위 정량화: 수명 주기의 어느 단계에서든 사건 경위와 사건 경위 family의 빈도를 추정하되, 모든 risk-significant 기여 요인을 나타내야 한다. PRA 결과의 수렴을 보일 만큼 낮은 truncation limit를 쓴다.
- mechanistic source term: 방출에 이르는 각 사건 경위의 환경 방출을 특성화하고, 대표 원천항이나 방출 범주로 묶는다.
- 방사선 결과: 대기 방출에 의한 피폭이 지배 경로라고 가정하며, 시설 내 원천의 직접 방사선과 지표수·지하수 경로는 다루지 않는다. 부지의 장기 기상을 대표하는 최소 한 해 분량의 시간별 기상 자료를 쓴다.
- risk integration: risk significance 기준을 정하고, 전체 위험을 적절한 척도로 나타내며, 그 불확실성을 정량화한다. 달리 정당화하지 않는 한 최소한 Fussell-Vesely나 Birnbaum 같은 상대 중요도 기준을 써야 하며, 위험 척도는 여러 원자로와 다른 방사성 원천의 기여를 통합하는 수단이다.
- 문서화: 결과를 재현하고 정당화할 수 있어야 하며, 모델 불확실성 원천은 합의된 접근이나 모델이 없는 쟁점과 관련된 것으로 정의된다.

## 관련 문서
- [[RG_1.247]]
- [[RG_1247_PRA_Acceptability_Framework]]
- [[RG_1247_PRA_Elements_Hazards]]
- [[Risk_Importance_Measures]]
- [[RG_1253_CP_PRA_Acceptability]]
