---
type: concept
aliases: [F-C Target]
sources: [NEI_18-04]
status: checked
verified: 2026-09-15
term: FC_TARGET
tags: []
terms_pending: []
---
# F-C Target (Frequency-Consequence Target)

> [!abstract] 요약
> Frequency-Consequence Target%%t:FC_TARGET%%은 빈도–결말 도표 위의 기준선이며, 개별 Licensing Basis Event%%t:LBE%%의 risk significance와 risk margin을 평가하는 데 쓰인다. 원문은 이 선이 수용과 불수용을 가르는 경계가 아니라고 못박는다.

## 원문 사실
- "A target line on a frequency-consequence chart that is used to evaluate the risk significance of LBEs and to evaluate risk margins that contribute to evidence of adequate defense-in-depth" [NEI_18-04 §6 p.90]
- "hereafter referred to as the F-C Target, is shown in Figure 3-1." [NEI_18-04 §3.2.1 p.15]
- "The F-C Target in this figure is based on the following considerations that comprise Top Level Safety Targets (TLSTs)" [NEI_18-04 §3.2.1 p.16]
- "The F-C Target values shown in the figure should not be considered as a demarcation of acceptable and unacceptable results. The F-C Target provides a general reference to assess events, SSCs, and programmatic controls in terms of sensitivities and available margins." [NEI_18-04 §3.2.1 p.16]
- "The F-C Target for high-frequency AOOs down to a frequency of 1E-01/plant-year are based on an iso-risk profile defined by the annual exposure limits of 10 CFR 20, i.e., 100 mrem/plant-year." [NEI_18-04 §3.2.1 p.16]
- "The F-C Target for lower frequency AOOs at frequencies of 1E-01/plant-year down to 1E-02/plant-year are set at a reference value of 1 rem corresponding with the Environmental Protection Agency (EPA) Protective Action Guide (PAG) limits and consistent with the goal of avoiding the need for offsite emergency response for any AOO." [NEI_18-04 §3.2.1 p.16]
- "The F-C Target for DBEs range from 1 rem at 1E-02/plant-year to 25 rem at 1E-04/plant-year with the dose calculated at the Exclusion Area Boundary (EAB) for the 30-day period following the onset of the release." [NEI_18-04 §3.2.1 p.16]
- "The F-C Target for the BDBEs range from 25 rem at 1E-04/plant-year to 750 rem at 5E-07/plant-year to ensure that the Quantitative Health Objective (QHO) for early health effects is not exceeded for individual BDBEs." [NEI_18-04 §3.2.1 p.16]
- "The lines between the anchor points are straight lines on a log frequency vs. log dose graph." [NEI_18-04 §3.2.1 p.17]
- "Event sequences with frequencies less than 5E-07/plant-year are retained in the PRA results and used to confirm there are no cliff edge effects." [NEI_18-04 §3.2.1 p.17]
- "the F-C Target is selected such that the risk, defined as the product of the frequency and consequence, does not increase as the frequency decreases." [NEI_18-04 §3.2.1 p.17]
- "the LBE process includes an activity to assure that the total frequency of exceeding 100 mrem summed over all the AOOs, DBEs, and BDBEs does not exceed 1/year." [NEI_18-04 §3.2.1 p.17]

| 항목 | 값 | 출처 |
|---|---|---|
| high-frequency AOOs | 100 mrem/plant-year | [NEI_18-04 §3.2.1 p.16] |
| 1E-01/plant-year down to 1E-02/plant-year | 1 rem | [NEI_18-04 §3.2.1 p.16] |
| 1E-02/plant-year | 1 rem | [NEI_18-04 §3.2.1 p.16] |
| 1E-04/plant-year | 25 rem | [NEI_18-04 §3.2.1 p.16] |
| 5E-07/plant-year | 750 rem | [NEI_18-04 §3.2.1 p.16] |

## 해설
F-C Target%%t:FC_TARGET%%은 빈도축과 선량축을 가진 도표 위의 한 선이다. 원문이 정의하는 쓰임은 두 가지로, 개별 LBE%%t:LBE%%의 risk significance를 판정하는 것과 Defense-in-Depth%%t:DID%%가 충분하다는 근거가 되는 risk margin을 평가하는 것이다.

선의 모양은 구간마다 다른 근거에서 나온다. 빈도가 높은 Anticipated Operational Occurrence%%t:AOO%% 구역은 연간 선량 한도 100 mrem에서 나온 등위험 곡선을 따르고, 1E-01/plant-year에서 1E-02/plant-year 구간은 1 rem을 기준값으로 삼는다. Design Basis Event%%t:DBE%% 구역은 1E-02/plant-year의 1 rem에서 1E-04/plant-year의 25 rem까지, Beyond Design Basis Event%%t:BDBE%% 구역은 거기서 5E-07/plant-year의 750 rem까지 이어진다. 앵커 점 사이는 로그–로그 도표에서 직선이다. 선량은 Exclusion Area Boundary%%t:EAB%%에서 방출이 시작된 뒤의 기간에 대해 계산하며, 그 기간은 원문 사실의 인용에 있다.

원문이 거듭 강조하는 점은 이 선이 합격과 불합격을 가르지 않는다는 것이다. 이 선은 사건과 Structures, Systems, and Components%%t:SSC%%, 절차적 관리 수단을 민감도와 여유의 관점에서 보는 기준이다. 구 wiki가 "선 위는 수용 불가"로 적었던 서술은 원문과 어긋난다.

전체 구간에서 빈도가 낮아질수록 위험(빈도와 결말의 곱)이 커지지 않도록 선이 잡혀 있다. 빈도가 5E-07/plant-year보다 낮은 Event Sequence%%t:ES%%도 버리지 않고 남겨 절벽 효과가 없는지 확인하는 데 쓴다. 개별 사건에 대한 이 기준과 별도로, 100 mrem을 넘는 빈도의 합이 연 1을 넘지 않도록 하는 cumulative risk target%%t:CUM_RISK_TARGET%%이 있다.

## 관련 문서
- [[Licensing_Basis_Event]]
- [[LBE_Frequency_Categories]]
- [[LBE_Risk_Significance]]
- [[NEI_18-04]]
