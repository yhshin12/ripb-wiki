---
type: concept
aliases: []
sources:
- NEI_18-04
status: checked
verified: 2026-10-30
term: null
tags:
- nei-18-04
terms_pending: []
---

# NEI 18-04 Task 7d의 결정론적 안전해석 (Deterministic Safety Analyses Against 10 CFR 50.34)

> [!abstract] 요약
> NEI 18-04 `Task 7d`는 인허가 신청서의 Design Basis Accident%%t:DBA%% 해석에 있는 전통적인 결정론적 안전해석에 해당하는 과업으로, 보수적 가정으로 수행되며 PRA의 일부인 Mechanistic Source Term%%t:MST%%·선량 불확실도 해석을 그 보수적 가정에 정보를 주는 데 쓸 수 있다(`are available to inform`). `Task 7a`의 두 문장은 결정론적 안전해석과 심층방어(Defense-in-Depth)%%t:DID%% 평가를 과업 제목과 다른 번호로 가리킨다.

## 원문 사실
- "This task corresponds to the traditional deterministic safety analysis that is found in the DBA analysis of the license application." [NEI_18-04 §3.2.2 Task 7d p.25]
- "It is performed using conservative assumptions." [NEI_18-04 §3.2.2 Task 7d p.25]
- "Deterministic analyses often use stylized scenarios for the purpose of demonstrating compliance with specific requirements, establish safety margins, and define equipment specifications and operational limits." [NEI_18-04 §3.2.2 Task 7d p.25]
- "Deterministic safety analysis can use conservative or best-estimate analytical methods with an appropriate accounting of uncertainties." [NEI_18-04 §3.2.2 Task 7d p.25]
- "The uncertainty analyses in the mechanistic source terms and radiological doses that are part of the PRA are available to inform the conservative assumptions used in this analysis and to avoid the arbitrary “stacking” of conservative assumptions that lack physical meaning." [NEI_18-04 §3.2.2 Task 7d p.25]
- "Because the selection of deterministic DBAs requires the selection of SR SSCs, this process also yields the selection of SR SSCs that are needed for the deterministic safety analysis in Task 7d." [NEI_18-04 §3.2.2 Task 2 p.20]
- "In this task, the definition and evaluation of LBEs should be used to support a RIPB evaluation of DID." [NEI_18-04 §3.2.2 Task 7e p.25]
- "Outcomes of this task include possible changes to the design to enhance the plant capabilities for DID, formulation of conservative assumptions for the deterministic safety analysis, and input to defining and enhancing programmatic elements of DID." [NEI_18-04 §3.2.2 Task 7e p.25]
- "The safety margin between the design-specific PRA results and the F-C Target provides one useful and practical demonstration of how the design fulfills the NRC’s expectations for enhanced safety." [NEI_18-04 §3.2.2 Task 7a p.22]
- "These margins also are useful in the evaluation of DID adequacy in Task 7d." [NEI_18-04 §3.2.2 Task 7a p.22]
- "DBE doses are evaluated against the F-C Target based on the mean estimates of consequence." [NEI_18-04 §3.2.2 Task 7a p.23]
- "This approach is based on the fact that the use of a conservative dose evaluation is appropriate for the deterministic safety analysis in Task 7a but is not consistent with the way in which uncertainties are addressed in risk-informed decision-making in general, where mean estimates supported by a robust uncertainty analysis are generally used to support risk significance determinations." [NEI_18-04 §3.2.2 Task 7a p.23]

## 해설
`Task 7d`는 인허가 신청서의 DBA%%t:DBA%% 해석에 있는 전통적인 결정론적 안전해석에 해당하며, 보수적 가정으로 수행된다. 결정론적 해석은 특정 요건 준수를 보이고, safety margin%%t:SAFETY_MARGIN%%을 정하고, 기기 사양과 운전 한계를 정의하려고 흔히(`often`) `stylized scenarios`를 쓴다. 결정론적 안전해석은 불확실도를 적절히 고려한 보수적 또는 best-estimate 해석 방법을 쓸 수 있다(`can`). PRA의 일부인 MST%%t:MST%%와 방사선 선량의 불확실도 해석은 이 해석의 보수적 가정에 정보를 주고 물리적 의미 없는 보수적 가정의 임의 `stacking`을 피하는 데 쓸 수 있다(`are available`).

설계 개발과 해석 과업은 결정론적 DBA%%t:DBA%% 선정에 Safety-Related%%t:SR%% Structures, Systems, and Components%%t:SSC%% 선정이 필요하므로, 이 과정이 `Task 7d`의 결정론적 안전해석에 필요한 SR%%t:SR%% SSC%%t:SSC%%도 선정한다고 적는다. `Task 7e`는 Licensing Basis Event%%t:LBE%%의 정의와 평가를 risk-informed and performance-based%%t:RIPB%% 심층방어%%t:DID%% 평가를 뒷받침하는 데 써야 하는(`should`) 과업이며, 그 결과에는 결정론적 안전해석의 보수적 가정 수립이 포함된다.

`Task 7a`는 Design Basis Event%%t:DBE%% 선량을 결과의 평균 추정으로 Frequency-Consequence Target%%t:FC_TARGET%%과 비교한다고 적고, 그 근거로 보수적 선량 평가는 결정론적 안전해석에는 적절하지만 일반적인 risk-informed decision-making의 불확실도 처리 방식과 맞지 않는다고 설명한다. 이 문장은 결정론적 안전해석을 `Task 7a`에 있다고 적고, 같은 과업의 다른 문장은 설계별 PRA 결과와 F-C Target%%t:FC_TARGET%% 사이의 safety margin%%t:SAFETY_MARGIN%%이 `Task 7d`의 심층방어%%t:DID%% 적절성 평가에도 쓸모 있다고 적는다. 과업 제목상 결정론적 안전해석은 `Task 7d`, 심층방어%%t:DID%% 평가는 `Task 7e`이므로 번호가 서로 어긋난다. 이 노트는 과업 제목을 기준으로 쓴다. 본문의 번호는 오기로 보이며 차후 확인이 필요하다(C17). Natrium `PSAR`의 DBA%%t:DBA%% 목록은 [[Natrium_DBA_List]]에 있다.

## 관련 문서
- [[LBE_Selection_Process]]
- [[Licensing_Basis_Event]]
- [[Mechanistic_Source_Term_Conditions]]
- [[DID_Integrated_Process]]
- [[F_C_Target]]
- [[Natrium_DBA_List]]
- [[NEI_18-04]]
