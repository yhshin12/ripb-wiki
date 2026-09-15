---
type: synthesis
aliases: []
sources: [NEI_18-04]
status: checked
verified: 2026-09-16
term: 
tags: [nei-18-04]
terms_pending: []
---
# NEI 18-04의 불확실도 처리 (Treatment of Uncertainties in NEI 18-04)

> [!abstract] 요약
> NEI 18-04는 불확실도를 Licensing Basis Event%%t:LBE%% 범주 지정, F-C Target 비교, 결정론적 안전해석, 심층방어(Defense-in-Depth)%%t:DID%% 적절성 평가에 걸쳐 다룬다. 이 synthesis 노트는 그 문장들을 원문 순서로 모은 것이며, 새 해석을 더하지 않는다.

## 원문 사실
- "The mean values of the frequencies are used to classify the LBEs into AOOs, DBEs, and BDBE categories." [NEI_18-04 §3.2.2 Task 7a p.22]
- "However, when the uncertainty bands ... defined by the 5th percentile and 95th percentile of the frequency estimates straddles a frequency boundary, the LBE is evaluated in both LBE categories." [NEI_18-04 §3.2.2 Task 7a p.22]
- "Uncertainties about the mean values are used to help evaluate the results against the frequency-consequence criteria and to identify the margins against the criteria." [NEI_18-04 §3.2.2 Task 7a p.22]
- "The uncertainties about these means are considered as part of the RIPB DID evaluation in Task 7e." [NEI_18-04 §3.2.2 Task 7a p.22]
- "It is recognized that the PRA may not fully resolve the impacts of all sources of uncertainty, such as modeling uncertainty." [NEI_18-04 §3.2.2 Task 7a p.23]
- "The LMP approach to PRA recommends following the guidance in NUREG-1855 to address uncertainties." [NEI_18-04 §3.2.2 Task 7a p.23]
- "Uncertainties not quantified in the PRA are important inputs to the evaluation of defense-in-depth adequacy in Task 7e." [NEI_18-04 §3.2.2 Task 7a p.23]
- "The uncertainty analyses in the mechanistic source terms and radiological doses that are part of the PRA are available to inform the conservative assumptions used in this analysis and to avoid the arbitrary “stacking” of conservative assumptions that lack physical meaning." [NEI_18-04 §3.2.2 Task 7d p.25]
- "This task involves the identification of risk-significant sources of uncertainty in both the frequency and consequence estimates, and evaluation against DID criteria." [NEI_18-04 §3.2.2 Task 7e p.25]
- "Programmatic DID is used to address uncertainties when evaluating plant capability DID as well as when programmatic protective strategies are defined." [NEI_18-04 §5.2 p.58]
- "The DID evaluation includes the identification of compensating protective measures to address the risk-significant sources of uncertainty in both the frequency and consequence estimates." [NEI_18-04 §5.2 p.60]
- "One of the primary motivations of employing DID attributes is to address uncertainties, including those that are reflected in the PRA estimates of frequencies and consequence as well as other uncertainties which are not sufficiently characterized for uncertainty quantification nor amenable to sensitivity analyses." [NEI_18-04 §5.3 Task 15 p.65]
- "The plant capability DID includes design margins that protect against uncertainties." [NEI_18-04 §5.3 Task 15 p.65]
- "Once the initial PRA is developed, LBEs are available for examination." [NEI_18-04 §5.9.4 p.85]
- "The margins between mean performance predictions and any insights into uncertainties around that performance should be evaluated as part of establishing an early DID baseline." [NEI_18-04 §5.9.4 p.85]
- "Other sources of uncertainty caused by PRA scope boundaries, model incompleteness, analytical methods or input data accuracy should be examined as well." [NEI_18-04 §5.9.4 p.85]
- "The greatest number of uncertainties exist in the beginning of the design cycle and are resolved systematically through the iterative design process." [NEI_18-04 §5.9.4 p.85]
- "Those are state-of-knowledge uncertainties that are transient in nature; they are unverified assumptions that are worked out over the design process and sometimes beyond." [NEI_18-04 §5.9.4 p.85]
- "Permanent uncertainties are typically broken down into two groups: those that are caused by variability or randomness, such as plant performance, and those that are results of gaps in knowledge." [NEI_18-04 §5.9.4 p.86]
- "DID adequacy evaluations should include both types of permanent uncertainties in reaching a final design adequacy conclusion." [NEI_18-04 §5.9.4 p.86]
- "Evaluations will also include quantified uncertainties for PRA-derived LBEs in two ways—frequency uncertainty and consequence uncertainty." [NEI_18-04 §5.9.4 p.86]

## 해설
NEI 18-04는 불확실도를 여러 과업에서 다룬다. LBE%%t:LBE%% 범주 지정은 빈도 평균값을 쓰지만, 빈도 추정의 5th·95th percentile로 정의한 `uncertainty bands`가 빈도 경계에 걸치면 LBE%%t:LBE%%를 두 범주에서 모두 평가한다. 평균값에 대한 불확실도는 결과를 frequency-consequence 기준과 비교하고 그 기준에 대한 margin을 찾는 것을 돕는 데(`help`) 쓰이며, 심층방어%%t:DID%% 평가에서도 고려된다. `Task 7a` 각주는 PRA가 `modeling uncertainty` 같은 모든 불확실도 원천의 영향을 다 해소하지 못할 수 있음을 인정하고, Licensing Modernization Project%%t:LMP%%의 PRA 접근이 불확실도 처리에 `NUREG-1855` 지침을 따르도록 권한다고 적으며, PRA에서 정량화되지 않은 불확실도가 심층방어%%t:DID%% 적절성 평가의 중요한 입력이라고 적는다([[LBE_Frequency_Categories]]).

결정론적 안전해석에서는 PRA의 일부인 Mechanistic Source Term%%t:MST%%과 선량 불확실도 해석을 보수적 가정에 정보를 주고 임의 `stacking`을 피하는 데 쓸 수 있다(`are available`)([[Deterministic_Safety_Analysis_Task_7d]]). `Task 7e`는 빈도와 결과 추정 양쪽의 risk-significant 불확실도 원천을 식별하고 심층방어%%t:DID%% 기준에 비추어 평가하는 과업이며, §5.2는 심층방어%%t:DID%% 평가가 이 원천에 대응하는 `compensating` protective measure%%t:PROTECTIVE_MEASURE%%의 식별을 포함한다고 적는다. Programmatic Defense-in-Depth%%t:PROGRAMMATIC_DID%%는 Plant Capability Defense-in-Depth%%t:PLANT_CAPABILITY_DID%%를 평가하거나 `programmatic protective strategies`를 정할 때 불확실도를 다루는 데 쓰이고, Plant Capability Defense-in-Depth%%t:PLANT_CAPABILITY_DID%%는 불확실도에 대비하는 design margin%%t:DESIGN_MARGIN%%을 포함한다. §5.3의 불확실도·margin 평가 과업(`Evaluate Uncertainties and Margins`)은 심층방어%%t:DID%% 속성을 쓰는 주된 동기의 하나가 PRA 추정에 반영된 불확실도와, 정량화할 만큼 충분히 특성화되지 않았고 민감도 해석에도 맞지 않는 다른 불확실도를 다루는 것이라고 적는다.

§5.9.4의 `Margin Adequacy` 항목은 초기 PRA가 만들어지면 LBE%%t:LBE%%를 검토할 수 있으며, 평균 성능 예측의 margin과 그 성능 주변 불확실도에 대한 통찰을 초기 심층방어%%t:DID%% baseline 확립의 일부로 평가해야 하고(`should`), PRA 범위 경계, 모델 불완전성, 해석 방법, 입력 자료 정확도에서 오는 다른 불확실도 원천도 검토해야 한다(`should`)고 적는다. `Sources of Uncertainties` 항목은 설계 초기에 불확실도가 가장 많고 반복 설계로 체계적으로 해소된다고 적고, 이것을 설계 과정 동안(때로는 그 뒤까지) 풀리는 미검증 가정인 일시적(`transient in nature`) state-of-knowledge 불확실도로 설명한다. 같은 항목은 `permanent uncertainties`가 흔히(`typically`) 발전소 성능 같은 변동성·무작위성에서 오는 것과 지식의 빈틈에서 오는 것으로 나뉘며, 심층방어%%t:DID%% 적절성 평가가 최종 설계 적절성 결론에 이르는 과정에서 두 종류를 모두 포함해야 한다(`should`)고 적는다. `Magnitude of Uncertainties` 항목은 심층방어%%t:DID%% 적절성 평가가 PRA에서 도출된 LBE%%t:LBE%%의 정량화된 불확실도도 빈도 불확실도와 결과 불확실도의 두 방식으로 포함한다(`will`)고 적는다([[DID_Baseline]]).

## 관련 문서
- [[LBE_Frequency_Categories]]
- [[Deterministic_Safety_Analysis_Task_7d]]
- [[DID_Risk_Margins]]
- [[Programmatic_DID]]
- [[Plant_Capability_DID]]
- [[DID_Baseline]]
- [[Mechanistic_Source_Term_Conditions]]
- [[NEI_18-04]]
