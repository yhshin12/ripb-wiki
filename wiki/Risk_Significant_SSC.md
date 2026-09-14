---
type: concept
aliases: []
sources: [NEI_18-04]
status: disputed
verified:
term: RS_SSC
tags: []
terms_pending: []
---
# Risk-Significant SSC 판정 기준 (Risk-Significant SSC Criteria)

> [!abstract] 요약
> Structures, Systems, and Components%%t:SSC%%는 그 기능이 모든 Licensing Basis Event%%t:LBE%%를 Frequency-Consequence Target%%t:FC_TARGET%% 안에 두는 데 필요하거나, 세 cumulative risk target%%t:CUM_RISK_TARGET%% 가운데 하나에 한도의 1%를 넘게 기여하면 Risk-Significant SSC%%t:RS_SSC%%로 분류된다. 첫 기준에 평균값과 95th percentile 상한 중 무엇을 쓰는지는 본문과 용어집이 어긋난다.

## 원문 사실
- "An SSC is classified as risk-significant if any of the following risk significance criteria are met for any SSC function included within the LBEs:" [NEI_18-04 §4.2.2 p.47]
- "A prevention or mitigation function of the SSC is necessary to meet the design objective of keeping all LBEs within the F-C Target." [NEI_18-04 §4.2.2 p.47]
- "An LBE is considered within the F-C Target when a point defined by the upper 95th percentile uncertainty on both the LBE frequency and dose is within the F-C Target." [NEI_18-04 §4.2.2 p.47]
- "In addition, some non-SR SSCs perform functions that may be necessary to keep AOOs or high-consequence DBEs within the F-C Target; these non-SR SSCs are also regarded as risk-significant and are classified as NSRST." [NEI_18-04 §4.2.2 p.47]
- "A significant contribution to each cumulative risk metric limit is satisfied when total frequency of all LBEs with failure of the SSC exceeds 1% of the cumulative risk metric limit based on the mean estimates of frequencies and consequences." [NEI_18-04 §4.2.2 p.47]
- "This SSC risk significance criterion may be satisfied by an SSC whether or not it performs functions necessary to keep one or more LBEs within the F-C Target." [NEI_18-04 §4.2.2 p.47]
- "An SSC makes a significant contribution to this cumulative risk metric if the total frequency of exceeding a site boundary dose of 100 mrem associated with LBEs with the SSC failed is greater than 1E-02/plant-year." [NEI_18-04 §4.2.2 p.47]
- "An SSC makes a significant contribution to this cumulative metric if the individual risk of early fatalities associated with the LBEs with the SSC failed is greater than 5E-09/plant-year." [NEI_18-04 §4.2.2 p.47]
- "An SSC makes a significant contribution to this cumulative risk metric if the individual risk of latent cancer fatalities associated with the LBEs with the SSC failed is greater than 2E-08/plant-year." [NEI_18-04 §4.2.2 p.47]
- "The cumulative risk limit criteria in this SSC classification process are provided to address the situation in which an SSC may contribute to two or more LBEs that collectively may be risk-significant even though the individual LBEs may not be significant." [NEI_18-04 §4.2.2 p.47]
- "In such cases, the reliability and availability of such SSCs may need to be controlled to manage the total integrated risks over all the LBEs." [NEI_18-04 §4.2.2 p.47]
- "A risk-significant SSC function is one that is necessary to keep one or more LBEs within the F-C Target or is significant in relation to one of the LBE cumulative evaluation risk metric limits." [NEI_18-04 §4.1 Tasks 4B and 5B p.44]
- "The LBE is considered within the F-C Target when a point defined by the upper 95th percentile uncertainty of the LBE frequency and dose estimates is within the F-C Target." [NEI_18-04 §3.3.6 p.37]
- "In the LMP framework, an SSC is regarded as risk-significant if its PRA Safety Function is: a) required to keep one or more LBEs inside the F-C Target based on mean frequencies and consequences" [NEI_18-04 §6 p.90]

| 항목 | 값 | 출처 |
|---|---|---|
| total frequency of exceeding a site boundary dose of 100 mrem | 1E-02/plant-year | [NEI_18-04 §4.2.2 p.47] |
| individual risk of early fatalities | 5E-09/plant-year | [NEI_18-04 §4.2.2 p.47] |
| individual risk of latent cancer fatalities | 2E-08/plant-year | [NEI_18-04 §4.2.2 p.47] |

## 해설
§4.2.2는 두 기준 중 하나라도 만족하면 SSC%%t:SSC%%를 risk-significant로 분류한다. 첫째는 그 SSC%%t:SSC%%의 예방·완화 기능이 모든 LBE%%t:LBE%%를 F-C Target%%t:FC_TARGET%% 안에 두는 설계 목표에 필요한 경우이다. 여기서 LBE%%t:LBE%%가 F-C Target%%t:FC_TARGET%% 안에 있다는 것은 빈도와 선량의 95th percentile 상한 점이 그 안에 있다는 뜻이다. Safety-Related%%t:SR%%가 아닌 SSC%%t:SSC%%라도 Anticipated Operational Occurrence%%t:AOO%%나 결말이 큰 Design Basis Event%%t:DBE%%를 F-C Target%%t:FC_TARGET%% 안에 두는 기능을 하면 risk-significant이며 Non-Safety-Related with Special Treatment%%t:NSRST%%로 분류된다.

둘째는 SSC%%t:SSC%%가 고장 난 LBE%%t:LBE%%들의 총 빈도가 cumulative risk target%%t:CUM_RISK_TARGET%% 한도의 1%를 넘는 경우이며, 평균 추정값을 쓴다. 절대값으로는 100 mrem 초과 빈도가 1E-02/plant-year, 조기 사망 개인 위험이 5E-09/plant-year, 잠복 암 사망 개인 위험이 2E-08/plant-year를 넘으면 기여가 크다고 본다. 이 기준은 LBE%%t:LBE%%를 F-C Target%%t:FC_TARGET%% 안에 두는 기능이 없는 SSC%%t:SSC%%에도 적용된다.

원문은 누적 기준을 두는 이유로, 개별 LBE%%t:LBE%%는 크지 않아도 한 SSC%%t:SSC%%가 여러 LBE%%t:LBE%%에 기여해 합쳐서는 risk-significant일 수 있는 경우를 든다. 이런 SSC%%t:SSC%%는 전체 위험을 관리하기 위해 신뢰도와 가용도를 관리해야 할 수 있다.

첫 기준에서 상한을 쓴다는 서술은 §3.3.6과 §4.2.2에 모두 있다. 반면 용어집의 Risk-Significant SSC%%t:RS_SSC%% 정의는 같은 기준을 평균 빈도와 평균 결말로 적는다. 본문 두 곳과 용어집이 어긋나므로 이 노트는 disputed로 둔다. 같은 사안은 [[Risk_Importance_Measures]]와 [[LBE_Risk_Significance]]에도 기록되어 있다.

## 관련 문서
- [[SSC_Safety_Classification]]
- [[Safety_Significant_SSC]]
- [[Risk_Importance_Measures]]
- [[LBE_Risk_Significance]]
- [[NEI_18-04]]
