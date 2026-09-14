---
type: concept
aliases: []
sources:
- NEI_18-04
status: disputed
verified: 2026-09-15
term: null
tags: []
terms_pending: []
---

# LBE 평가 기준 (LBE Evaluation Criteria, Tasks 7a–7c)

> [!abstract] 요약
> Licensing Basis Event%%t:LBE%%는 평균 빈도로 범주를 정하되, 빈도 불확실도 구간이 범주 경계에 걸치면 양쪽 범주에서 모두 평가한다. 발전소 전체 위험은 세 가지 cumulative risk target%%t:CUM_RISK_TARGET%%으로 평가하고, 개별 LBE%%t:LBE%%와 Structures, Systems, and Components%%t:SSC%%는 Frequency-Consequence Target%%t:FC_TARGET%%과 그 목표들에 대한 기여로 Risk-Significant LBE%%t:RS_LBE%%, Risk-Significant SSC%%t:RS_SSC%% 여부를 판정한다.

## 원문 사실
- "The figure does not define specific acceptance criteria for the analysis of LBEs but rather serves as a tool to focus the attention of the designer and those reviewing the design and related operational programs to the most significant events and possible means to address those events." [NEI_18-04 §3.2.2 Task 7a p.22]
- "The mean values of the frequencies are used to classify the LBEs into AOOs, DBEs, and BDBE categories." [NEI_18-04 §3.2.2 Task 7a p.22]
- "However, when the uncertainty bands ... defined by the 5th percentile and 95th percentile of the frequency estimates straddles a frequency boundary, the LBE is evaluated in both LBE categories." [NEI_18-04 §3.2.2 Task 7a p.22]
- "An LBE with mean frequency above 1E-02/plant-year and 5th percentile less than 1E-02/plant-year is evaluated as an AOO and DBE." [NEI_18-04 §3.2.2 Task 7a p.22]
- "An LBE with a mean frequency less than 1E-04/plant-year with a 95th percentile above 1E-04/plant-year is evaluated as a BDBE and a DBE." [NEI_18-04 §3.2.2 Task 7a p.22]
- "An event sequence family with a mean frequency less than 5E-07/plant year but with a 95%tile frequency estimate above 5E-07/plant-year is evaluated as a BDBE." [NEI_18-04 §3.2.2 Task 7a p.22]
- "DBE doses are evaluated against the F-C Target based on the mean estimates of consequence." [NEI_18-04 §3.2.2 Task 7a p.23]
- "mean estimates supported by a robust uncertainty analysis are generally used to support risk significance determinations." [NEI_18-04 §3.2.2 Task 7a p.23]
- "The upper bound consequences for each DBA, defined as the 95th percentile of the uncertainty distribution, shall meet the 10 CFR 50.34 dose limit at the EAB." [NEI_18-04 §3.2.2 Task 7a p.23]
- "The total mean frequency of exceeding a site boundary dose of 100 mrem from all LBEs should not exceed 1/plant-year." [NEI_18-04 §3.2.2 Task 7b p.24]
- "The average individual risk of early fatality within 1 mile of the EAB from all LBEs based on mean estimates of frequencies and consequences shall not exceed 5E-07/plant-year to ensure that the NRC safety goal QHO for early fatality risk is met." [NEI_18-04 §3.2.2 Task 7b p.24]
- "The average individual risk of latent cancer fatalities within 10 miles of the EAB from all LBEs based on mean estimates of frequencies and consequences shall not exceed 2E-06/plant-year to ensure that the NRC safety goal QHO for latent cancer fatality risk is met." [NEI_18-04 §3.2.2 Task 7b p.24]
- "Having these cumulative risk targets as part of the process provides a mechanism to ensure that the F-C Target is conservatively defined for use as a tool for focusing attention on matters important to managing the risks from non-LWRs." [NEI_18-04 §3.2.2 Task 7b p.24]
- "LBEs are classified as risk-significant if the LBE site boundary dose exceeds 2.5 mrem over 30 days and the frequency of the dose is within 1% of the F-C Target." [NEI_18-04 §3.2.2 Task 7c p.24]
- "SSCs are classified as risk-significant if the SSC function is necessary to keep any LBEs inside the F-C Target, or if the total frequency of LBEs with the SSCs failed is within 1% of any of the three cumulative risk targets identified in Task 7b." [NEI_18-04 §3.2.2 Task 7c p.24]
- "In the LMP framework, an AOO, DBE, or BDBE is regarded as risk-significant if the combination of the upper bound (95%tile) estimates of the frequency and consequence of the LBE are within 1% of the F-C Target AND the upper bound 30-day TEDE dose at the EAB exceeds 2.5 mrem." [NEI_18-04 §6 p.90]
- "Risk-significant LBEs are those with frequencies within 1% of the F-C Target with site boundary doses exceeding 2.5 mrem (see crosshatched region of Figure 3-4)." [NEI_18-04 §3.3.5 p.35]
- "To consider the effects of uncertainties, the upper 95th percentile estimates of both frequency and dose should be used." [NEI_18-04 §3.3.5 p.35]
- "The use of the 1% metric is consistent with the approach to defining risk-significant event sequences in the PRA standards." [NEI_18-04 §3.3.5 p.35]
- "The 2.5 mrem cut-off is selected as this is approximately 10% of the dose that an average person at the site boundary would receive in 30 days due to background radiation." [NEI_18-04 §3.3.5 p.35]
- "In the LMP framework, an SSC is regarded as risk-significant if its PRA Safety Function is: a) required to keep one or more LBEs inside the F-C Target based on mean frequencies and consequences" [NEI_18-04 §6 p.90]
- "The LBE is considered within the F-C Target when a point defined by the upper 95th percentile uncertainty of the LBE frequency and dose estimates is within the F-C Target." [NEI_18-04 §3.3.6 p.37]

## 해설
범주 배정에는 빈도의 평균값을 쓴다. 다만 5th percentile과 95th percentile로 정한 불확실도 구간이 범주 경계에 걸치면 그 LBE%%t:LBE%%는 두 범주에서 모두 평가된다. 평균이 1E-02/plant-year를 넘고 5th percentile이 그보다 낮으면 Anticipated Operational Occurrence%%t:AOO%%이자 Design Basis Event%%t:DBE%%로, 평균이 1E-04/plant-year보다 낮고 95th percentile이 그보다 높으면 Beyond Design Basis Event%%t:BDBE%%이자 DBE%%t:DBE%%로 평가한다. 평균이 5E-07/plant-year보다 낮아도 95th percentile이 그 위면 BDBE%%t:BDBE%%로 평가한다.

DBE%%t:DBE%% 선량은 평균 결말로 F-C Target%%t:FC_TARGET%%과 비교한다. 원문은 불확실도 분석을 거친 평균값으로 판단하는 것이 일반적 관행이라는 점을 근거로 든다. 반면 각 Design Basis Accident%%t:DBA%%의 상한 결말(95th percentile)은 Exclusion Area Boundary%%t:EAB%%에서 10 CFR 50.34 선량 한도를 만족해야 한다. 원문은 F-C Target%%t:FC_TARGET%% 그림 자체가 합격 기준이 아니라 중요한 사건에 주의를 모으는 도구라고 적는다.

cumulative risk target%%t:CUM_RISK_TARGET%%은 세 가지이다. 모든 LBE%%t:LBE%%에서 부지 경계 선량 100 mrem을 넘을 총 평균 빈도가 1/plant-year를 넘지 않을 것, EAB%%t:EAB%%에서 1마일 안의 조기 사망 개인 위험이 5E-07/plant-year를 넘지 않을 것, 10마일 안의 잠복 암 사망 개인 위험이 2E-06/plant-year를 넘지 않을 것이다. 뒤의 두 목표는 Quantitative Health Objective%%t:QHO%%를 만족시키기 위한 것이다. 원문은 이 cumulative risk target%%t:CUM_RISK_TARGET%%들이 F-C Target%%t:FC_TARGET%%이 보수적으로 정의되었음을 보장하는 장치라고 설명한다.

LBE%%t:LBE%%는 부지 경계 선량이 30일 동안 2.5 mrem을 넘고 그 빈도가 F-C Target%%t:FC_TARGET%%의 1% 이내에 들면 Risk-Significant LBE%%t:RS_LBE%%로 분류된다. 용어집은 같은 기준을 더 구체적으로 적어, 빈도와 결말의 상한(95%tile) 추정값과 EAB%%t:EAB%%의 30일 선량을 쓴다고 명시한다. SSC%%t:SSC%%는 그 기능이 어떤 LBE%%t:LBE%%를 F-C Target%%t:FC_TARGET%% 안에 두는 데 필요하거나, 그 SSC%%t:SSC%%가 고장 난 LBE%%t:LBE%%들의 총 빈도가 세 cumulative risk target%%t:CUM_RISK_TARGET%% 가운데 하나의 1% 이내이면 Risk-Significant SSC%%t:RS_SSC%%로 분류된다.

본문의 뒤 절은 Risk-Significant LBE%%t:RS_LBE%% 판정에 빈도와 선량 모두 95th percentile 상한을 쓰라고 명시해 용어집과 같다. 1%는 PRA 표준이 risk-significant event sequence를 정하는 방식과 같고, 2.5 mrem은 부지 경계의 평균적인 사람이 배경 방사선으로 30일 동안 받는 선량의 약 10%이다. 한편 SSC%%t:SSC%%가 LBE%%t:LBE%%를 F-C Target%%t:FC_TARGET%% 안에 두는지 볼 때, 용어집은 평균값을 쓴다고 적고 본문의 뒤 절은 95th percentile 상한을 쓴다고 적어 서로 어긋난다. 이 노트는 그 판정을 담고 있으므로 disputed로 둔다. 상세는 [[Risk_Importance_Measures]]에 있다.

## 관련 문서
- [[Risk_Importance_Measures]]
- [[LBE_Selection_Process]]
- [[F_C_Target]]
- [[LBE_Frequency_Categories]]
- [[Required_Safety_Function]]
- [[NEI_18-04]]
