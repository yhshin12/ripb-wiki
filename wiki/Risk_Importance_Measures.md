---
type: concept
aliases: []
sources: [NEI_18-04]
status: disputed
verified:
term:
tags: []
terms_pending: []
---
# Risk Importance Measure와 절대 지표 (Risk Importance Measures and Absolute Risk Metrics)

> [!abstract] 요약
> 표 3-2는 PRA에서 흔히 쓰는 risk importance measure 8가지를 정리한다. 원문은 이 척도들이 전체 위험으로 정규화된 상대값만 주므로, 방출 빈도와 선원항(source term)%%t:SOURCE_TERM%%이 매우 작은 비경수형원전(non-light-water reactor)%%t:NON_LWR%%에서는 Licensing Basis Event%%t:LBE%%와 Structures, Systems, and Components%%t:SSC%%의 중요도를 절대값으로도 평가해야 한다고 본다. SSC%%t:SSC%% 판정에 평균값과 95th percentile 중 무엇을 쓰는지는 원문 두 곳이 어긋난다.

## 원문 사실
- "This can be achieved by rank ordering the PRA event sequences and sequence minimal cut-sets to identify their relative and absolute contribution to each risk metric and to calculate the risk importance measures that evaluate contributions to basic events that may be common to two or more sequences or cut-sets." [NEI_18-04 §3.3.6 p.35]
- "For any of the integrated risk metrics, such as the QHOs, the relative risk significance of any LBE can be calculated as a percentage of the LBE risk (product of the LBE frequency and LBE consequence) to the aggregated risk of all the LBEs." [NEI_18-04 §3.3.6 p.35]
- "The historical approach to evaluating risk importance produced only the relative importance of each basic event because the formulas are normalized against the total calculated risk for the plant, R(base)." [NEI_18-04 §3.3.6 p.36]
- "For advanced non-LWR plants, the frequencies of events involving a release of radioactive material may be very small and those events with releases may involve very small source terms compared with releases from an LWR core damage event." [NEI_18-04 §3.3.6 p.36]
- "Hence, it is appropriate to evaluate risk significance not only on a relative basis but also on an absolute basis." [NEI_18-04 §3.3.6 p.36]
- "For this purpose, the risks can be compared against the risk goals rather than the baseline risks." [NEI_18-04 §3.3.6 p.37]
- "A prevention or mitigation function of the SSC is necessary to meet the design objective of keeping all LBEs within the F-C Target." [NEI_18-04 §3.3.6 p.37]
- "This is determined by assuming failure of the SSC in performing a prevention or mitigation function and checking how the resulting LBE risks compare with the F-C Target." [NEI_18-04 §3.3.6 p.37]
- "The LBE is considered within the F-C Target when a point defined by the upper 95th percentile uncertainty of the LBE frequency and dose estimates is within the F-C Target." [NEI_18-04 §3.3.6 p.37]
- "An LBE is considered within the F-C Target when a point defined by the upper 95th percentile uncertainty on both the LBE frequency and dose is within the F-C Target." [NEI_18-04 §4.2.2 p.47]
- "In the LMP framework, an SSC is regarded as risk-significant if its PRA Safety Function is: a) required to keep one or more LBEs inside the F-C Target based on mean frequencies and consequences" [NEI_18-04 §6 p.90]
- "A significant contribution to each cumulative risk metric limit is satisfied when the total frequency of all LBEs with failure of the SSC exceeds 1% of the cumulative risk metric limit based on the mean estimates of frequencies and consequences." [NEI_18-04 §3.3.6 p.37]
- "When the total frequency of LBEs with all the basic events associated with the SSC exceeds the 1% criterion, the SSC is regarded as risk-significant." [NEI_18-04 §3.3.6 p.37]

| 항목 | 값 | 출처 |
|---|---|---|
| Risk Reduction | RR | [NEI_18-04 Table 3-2 p.36] |
| Fussell-Vesely | FV | [NEI_18-04 Table 3-2 p.36] |
| Risk Reduction Worth | RRW | [NEI_18-04 Table 3-2 p.36] |
| Criticality Importance | CR | [NEI_18-04 Table 3-2 p.36] |
| Risk Achievement | RA | [NEI_18-04 Table 3-2 p.36] |
| Risk Achievement Worth | RAW | [NEI_18-04 Table 3-2 p.36] |
| Partial Derivative | PD | [NEI_18-04 Table 3-2 p.36] |
| Birnbaum Importance | BI | [NEI_18-04 Table 3-2 p.36] |

## 해설
표 3-2의 척도는 둘 이상의 Event Sequence%%t:ES%%나 minimal cut set에 공통으로 나타나는 basic event의 위험 기여를 평가하기 위한 것이다. Fussell-Vesely나 Risk Achievement Worth 같은 여러 척도가 있으며 수식은 원문 표에 있다.

원문은 이 전통적 방식이 발전소 전체 위험으로 정규화되어 basic event의 상대적 중요도만 준다는 한계를 짚는다. 비경수형원전%%t:NON_LWR%%에서는 방출을 수반하는 사건의 빈도가 매우 작고 선원항%%t:SOURCE_TERM%%도 경수로 노심 손상 사건보다 매우 작을 수 있으므로, LBE%%t:LBE%%와 SSC%%t:SSC%%의 risk significance를 상대값뿐 아니라 절대값으로도 평가하는 것이 적절하다고 본다. 절대 평가는 기준 위험이 아니라 위험 목표와 비교하는 방식이다.

SSC%%t:SSC%% 판정의 첫 기준은 그 SSC%%t:SSC%%가 예방하거나 완화하는 기능이 모든 LBE%%t:LBE%%를 Frequency-Consequence Target%%t:FC_TARGET%% 안에 두는 데 필요한가이다. 본문은 그 기능이 고장났다고 가정하고, LBE%%t:LBE%%의 빈도와 선량의 95th percentile 상한 점이 F-C Target%%t:FC_TARGET%% 안에 있는지로 판정한다고 적는다. §4.2.2도 같은 상한 기준을 적는다. 반면 용어집의 Risk-Significant SSC%%t:RS_SSC%% 정의는 같은 기준을 평균 빈도와 평균 결말로 적는다. 두 서술이 어긋나므로 이 노트는 disputed로 둔다.

둘째 기준은 SSC%%t:SSC%%가 고장 난 LBE%%t:LBE%%들의 총 빈도가 cumulative risk target%%t:CUM_RISK_TARGET%% 중 하나의 한도에서 1%를 넘는가이며, 이때는 평균 추정값을 쓴다. 원문은 그 SSC%%t:SSC%%와 관련된 모든 basic event가 고장인 LBE%%t:LBE%%를 합산해 판정한다고 설명한다.

## 관련 문서
- [[Risk_Significant_SSC]]
- [[LBE_Risk_Significance]]
- [[PRA_Role_In_LBE_Selection]]
- [[F_C_Target]]
- [[NEI_18-04]]
- [[RG_1247_PRA_Elements_Internal_Events]]
