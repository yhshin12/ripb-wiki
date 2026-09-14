---
type: concept
aliases: []
sources: [NEI_18-04]
status: checked
verified: 2026-09-15
term:
tags: []
terms_pending: []
---
# LBE 선정 절차 (LBE Selection Process)

> [!abstract] 요약
> Licensing Basis Event%%t:LBE%% 선정 절차는 Task 1–10으로 이루어진 논리도로 제시되며, 과제에 정해진 순서가 없고 설계가 진행되는 동안 반복된다. 초기 목록은 결정론적으로 제안하고, PRA 결과를 반영하며 설계 단계마다 목록을 다듬어 최종 목록과 Safety-Related%%t:SR%% Structures, Systems, and Components%%t:SSC%% 목록을 확정한다.

## 원문 사실
- "A logic chart indicating the tasks to identify and evaluate LBEs in concert with the design evolution is shown in Figure 3-2." [NEI_18-04 §3.2.2 p.17]
- "The tasks identified in Figure 3-2 do not need to be performed in any specific order and their completion is recognized to be an iterative process." [NEI_18-04 §3.2.2 p.18]
- "the LBE selection and evaluation process may be performed using alternative tasks that provide comparable technical information as needed to identify a sufficiently complete set of design specific LBEs" [NEI_18-04 §3.2.2 p.18]
- "These events are to be selected deterministically and may be supported by qualitative risk insights based on all relevant and available experience, including prior experience from the design and licensing of reactors." [NEI_18-04 §3.2.2 Task 1 p.19]
- "The subsequent Tasks 3 through 10 may be repeated for each design phase or iteration until the list of LBEs becomes stable and is finalized." [NEI_18-04 §3.2.2 Task 2 p.20]
- "The PRA may be introduced at any stage of design, however the benefits of incorporation of risk insights into the design favor early introduction." [NEI_18-04 §3.2.2 Task 3 p.20]
- "Each of these families is assigned to an LBE category based on mean event sequence frequency of occurrence per plant-year summed over all the event sequences in the LBE family." [NEI_18-04 §3.2.2 Task 4 p.20]
- "It is noted that this DID evaluation does not change the selection of LBEs directly." [NEI_18-04 §3.2.2 Task 7e p.25]
- "This evaluation could lead to compensatory actions that change the design capability or programmatic controls on the design, which in turn would lead to changes in the PRA and thereby affect the selection or evaluation of LBEs." [NEI_18-04 §3.2.2 Task 7e p.25]
- "Establishing the final list of LBEs and SR SSCs signifies the completion of the LBE selection process and the selection of the SR SSCs." [NEI_18-04 §3.2.2 Task 10 p.26]
- "an initial set of LBEs is proposed based on engineering judgment in Task 1 of the process." [NEI_18-04 §3.2.3 p.26]
- "The simplifying perception that a design has stages that contain bright lines is a frequent description at the system level but is not correct at the plant level." [NEI_18-04 §3.2.3 p.27]
- "When the design and PRA are developed in a manner that is sufficient to meet requirements reflected in applicable PRA standards and regulatory guides, the LBEs can be finalized and included in the license application." [NEI_18-04 §3.2.3 p.27]

| 항목 | 값 | 출처 |
|---|---|---|
| Task 1 | Propose Initial List of LBEs | [NEI_18-04 §3.2.2 p.19] |
| Task 2 | Design Development and Analysis | [NEI_18-04 §3.2.2 p.20] |
| Task 3 | PRA Development/Update | [NEI_18-04 §3.2.2 p.20] |
| Task 4 | Identify/Revise List of AOOs, DBEs and BDBEs | [NEI_18-04 §3.2.2 p.20] |
| Task 5a | Identify Required Safety Functions (RSFs) | [NEI_18-04 §3.2.2 p.21] |
| Task 5b | Select/Revise Safety-Related SSCs | [NEI_18-04 §3.2.2 p.21] |
| Task 6 | Select Deterministic DBAs and Design Basis External Hazard Levels | [NEI_18-04 §3.2.2 p.21] |
| Task 7a | Evaluate LBEs Against F-C Target | [NEI_18-04 §3.2.2 p.22] |
| Task 7b | Evaluate Integrated Plant Risk against QHOs and 10 CFR 20 | [NEI_18-04 §3.2.2 p.24] |
| Task 7c | Evaluate Risk Significance of LBEs and SSCs Including Barriers | [NEI_18-04 §3.2.2 p.24] |
| Task 7d | Perform Deterministic Safety Analyses Against 10 CFR 50.34 | [NEI_18-04 §3.2.2 p.25] |
| Task 7e | Risk-Informed, Performance-Based Evaluation of Defense-in-Depth | [NEI_18-04 §3.2.2 p.25] |
| Task 8 | Decide on Completion of Design/LBE Development | [NEI_18-04 §3.2.2 p.25] |
| Task 9 | Proceed to Next Stage of Design Development | [NEI_18-04 §3.2.2 p.26] |
| Task 10 | Finalize List of LBEs and Safety-Related SSCs | [NEI_18-04 §3.2.2 p.26] |

## 해설
절차는 Task 1에서 초기 LBE%%t:LBE%% 목록을 결정론적으로 제안하는 데서 시작한다. 이어 Task 2와 Task 3에서 설계와 PRA를 발전시키고, Task 4에서 PRA가 모델링한 사건 시퀀스를 군으로 묶어 평균 빈도에 따라 LBE%%t:LBE%% 범주에 배정한다. 범주의 빈도 구간은 [[LBE_Frequency_Categories]]에 있다.

원문은 과제를 정해진 순서로 수행할 필요가 없다고 적는다. Task 3부터 Task 10까지는 LBE%%t:LBE%% 목록이 안정되어 확정될 때까지 설계 단계나 반복마다 다시 수행될 수 있고, 비슷한 기술 정보를 주는 다른 과제로 대체하는 것도 허용된다. PRA는 설계의 어느 단계에서든 도입할 수 있지만 원문은 이른 도입이 유리하다고 본다.

Task 5a부터 Task 6까지는 Required Safety Function%%t:RSF%%을 정하고 이를 수행할 SR%%t:SR%% SSC%%t:SSC%%를 고르는 과정이며 [[Required_Safety_Function]]에 정리했다. Task 7a부터 Task 7c까지의 평가, 즉 빈도 범주 판정과 발전소 전체 위험, 위험 중요 판정 기준은 [[LBE_Risk_Significance]]에 있다.

Task 7e의 Defense-in-Depth%%t:DID%% 평가는 LBE%%t:LBE%% 선정을 직접 바꾸지 않는다. 평가 결과로 설계나 절차적 관리가 바뀌면 PRA가 바뀌고, 그 경로를 거쳐 선정이나 평가에 영향을 줄 수 있다. Task 10에서 LBE%%t:LBE%%와 SR%%t:SR%% SSC%%t:SSC%% 최종 목록을 확정하면 선정 절차가 끝난다.

설계 단계에 관해 원문은, 설계에 뚜렷한 경계를 가진 단계가 있다는 단순한 인식이 계통 수준에서는 흔하지만 발전소 수준에서는 맞지 않다고 본다. 따라서 LBE%%t:LBE%% 목록도 설계가 성숙하는 동안 계속 다듬어지며, 설계와 PRA가 적용 표준과 규제 지침을 충족할 만큼 발전했을 때 확정되어 인허가 신청서에 들어간다.

## 관련 문서
- [[Licensing_Basis_Event]]
- [[LBE_Frequency_Categories]]
- [[Required_Safety_Function]]
- [[LBE_Risk_Significance]]
- [[NEI_18-04]]
