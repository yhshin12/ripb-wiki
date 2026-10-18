---
type: concept
aliases: []
sources: [NEI_18-04]
status: checked
verified: 2026-10-17
term:
tags: []
terms_pending: []
---
# Risk Importance Measure와 절대 지표 (Risk Importance Measures and Absolute Risk Metrics)

> [!abstract] 요약
> 표 3-2는 PRA에서 흔히 쓰는 risk importance measure 8가지를 정리한다. 원문은 이 척도들이 전체 위험으로 정규화된 상대값만 주므로, 방출 빈도와 선원항(source term)%%t:SOURCE_TERM%%이 매우 작은 비경수형원전(non-light-water reactor)%%t:NON_LWR%%에서는 Licensing Basis Event%%t:LBE%%와 Structures, Systems, and Components%%t:SSC%%의 중요도를 절대값으로도 평가해야 한다고 본다. SSC%%t:SSC%% 판정 기준은 [[Risk_Significant_SSC]]에 모아 둔다.

## 원문 사실
- "This can be achieved by rank ordering the PRA event sequences and sequence minimal cut-sets to identify their relative and absolute contribution to each risk metric and to calculate the risk importance measures that evaluate contributions to basic events that may be common to two or more sequences or cut-sets." [NEI_18-04 §3.3.6 p.35]
- "For any of the integrated risk metrics, such as the QHOs, the relative risk significance of any LBE can be calculated as a percentage of the LBE risk (product of the LBE frequency and LBE consequence) to the aggregated risk of all the LBEs." [NEI_18-04 §3.3.6 p.35]
- "The historical approach to evaluating risk importance produced only the relative importance of each basic event because the formulas are normalized against the total calculated risk for the plant, R(base)." [NEI_18-04 §3.3.6 p.36]
- "For advanced non-LWR plants, the frequencies of events involving a release of radioactive material may be very small and those events with releases may involve very small source terms compared with releases from an LWR core damage event." [NEI_18-04 §3.3.6 p.36]
- "Hence, it is appropriate to evaluate risk significance not only on a relative basis but also on an absolute basis." [NEI_18-04 §3.3.6 p.36]
- "For this purpose, the risks can be compared against the risk goals rather than the baseline risks." [NEI_18-04 §3.3.6 p.37]

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

§3.3.6 뒷부분의 SSC%%t:SSC%% risk significance 판정 기준은 [[Risk_Significant_SSC]]에 모아 둔다.

## 관련 문서
- [[Risk_Significant_SSC]]
- [[LBE_Risk_Significance]]
- [[PRA_Role_In_LBE_Selection]]
- [[F_C_Target]]
- [[NEI_18-04]]
- [[RG_1247_PRA_Elements_Internal_Events]]
