---
type: natrium
aliases: []
sources: [PSAR_ch06, NEI_18-04, SER_KU1_CP]
status: checked
verified: 2026-09-16
term:
tags: [natrium]
terms_pending: []
---
# Natrium reliability target과 capability target (Natrium Reliability and Capability Targets)

> [!abstract] 요약
> `PSAR` Chapter 6은 Structures, Systems, and Components%%t:SSC%%가 PRA Safety Function%%t:PSF%%을 수행한다는 보증을 PRA에서 평가한 reliability와 capability의 달성·감시로 얻는다고 적고, reliability target을 SSC%%t:SSC%%가 지정된 기능을 완수할 확률에 대한 성능 목표로, capability target을 적절한 margin을 두고 PSF%%t:PSF%%를 수행하는 능력에 초점을 둔 성능 목표로 정의하며, 정량 reliability target은 Design Reliability Assurance Program이 산출하고 정량 capability target은 해석 모델에 기반한다. 두 target 모두 Safety-Related와 Non-Safety-Related with Special Treatment SSC%%t:SSC%%에 대해 아직 확정되지 않았고 operating license 단계에서 확인된다.

## 원문 사실
- "Assurance that a structure, system, or component (SSC) performs its probabilistic risk assessment (PRA) safety function is accomplished by achieving and monitoring the levels of reliability and capability of the SSC that are assessed in the PRA." [PSAR_ch06 §6.2 p.12]
- "The PRA is described in Section 3.1, licensing basis events are described in Sections 3.4 through 3.9, and PRA safety functions are described in Section 5.2." [PSAR_ch06 §6.2 p.12]
- "A reliability target is a performance goal established for the probability that an SSC will complete its specified function to achieve plant-level risk and reliability goals." [PSAR_ch06 §6.2 p.12]
- "Quantitative reliability targets are the output of the Design Reliability Assurance Program, which is described in Section 8.0." [PSAR_ch06 §6.2 p.12]
- "The reliability targets for safety-related and non-safety-related with special treatment SSCs have not yet been confirmed." [PSAR_ch06 §6.2 p.12]
- "The Design Reliability Assurance Program will confirm, at the operating license (OL) stage, that the reliability performance targets assumed in the PRA have been met." [PSAR_ch06 §6.2 p.12]
- "A capability target is a performance goal focused on the ability of an SSC to perform its PRA safety function with adequate margins." [PSAR_ch06 §6.2 p.12]
- "Lifetime degradation is considered as part of the capability." [PSAR_ch06 §6.2 p.12]
- "Specific operational performance criteria are included as part of the profile of the success of a PRA safety function." [PSAR_ch06 §6.2 p.12]
- "These quantitative targets are based on analytical models used to demonstrate the capability of the plant to respond to hazards." [PSAR_ch06 §6.2 p.12]
- "The capability targets for safety-related and non-safety-related with special treatment SSCs have not yet been confirmed." [PSAR_ch06 §6.2 p.12]
- "The output of analytical models will confirm, at the OL stage, that the capability targets assumed in the PRA have been met." [PSAR_ch06 §6.2 p.12]
- "For SSCs classified as safety-related or non-safety-related with special treatment, the process for using the reliability and capability to develop special treatment requirements is described in Section 6.3." [PSAR_ch06 §6.2 p.12]
- "Assurance is first accomplished by achieving and monitoring the levels of reliability and availability that are assessed in the PRA and that are determined to be necessary to meet the LBE risk evaluation criteria." [NEI_18-04 §4.4.5 p.50]
- "Assurance is further accomplished by achieving and monitoring the capabilities of the SSCs in the performance of their mitigation functions with adequate margins to address uncertainties." [NEI_18-04 §4.4.5 p.50]
- "All safety-significant SSCs, including those in the SR and NSRST categories, should be included in a Reliability Assurance Program (RAP) similar to that described in SRP 17.4." [NEI_18-04 §4.4.5 p.56]
- "Additional special treatment requirements for SR SSCs should be developed to provide assurance that the capability to perform their RSFs is maintained during the operating lifetime of the plant." [NEI_18-04 §4.4.5 p.56]
- "Specifically, the staff noted that certain reliability targets were set below the typical values established for comparable safety functions in other reactor designs." [SER_KU1_CP §6.2.1 p.386]
- "At the CP stage, there are insufficient technical justifications to fully substantiate the adequacy of these lower targets." [SER_KU1_CP §6.2.1 p.386]
- "the determination on the proposed targets and if they are technically achievable or provide sufficient margin to ensure reliable performance of the associated safety functions will occur at the OL stage" [SER_KU1_CP §6.2.1 p.386]

## 해설
`PSAR` Chapter 6에 따르면 SSC%%t:SSC%%가 PSF%%t:PSF%%를 수행한다는 보증은 PRA에서 평가한 SSC%%t:SSC%%의 reliability와 capability 수준을 달성하고 감시해서 얻는다. PRA는 `Section 3.1`, Licensing Basis Event%%t:LBE%%는 `Sections 3.4 through 3.9`, PSF%%t:PSF%%는 `Section 5.2`에 기술된다. NEI 18-04는 먼저 PRA에서 평가되고 LBE%%t:LBE%% 위험 평가 기준을 만족하는 데 필요한 reliability와 availability를 달성·감시하고, 다음으로 불확실도를 다룰 적절한 margin을 두고 `mitigation functions`를 수행하는 SSC%%t:SSC%% capability를 달성·감시해 보증한다고 적는다. `PSAR` 문장은 reliability와 capability를 한 문장에 적고 availability를 적지 않는다.

reliability target은 SSC%%t:SSC%%가 지정된 기능을 완수할 확률에 대해 발전소 수준의 위험·신뢰도 목표를 달성하도록 정한 성능 목표이며, 정량 reliability target은 `Section 8.0`에 기술된 Design Reliability Assurance Program의 산출물이다. Safety-Related%%t:SR%%과 Non-Safety-Related with Special Treatment%%t:NSRST%% SSC%%t:SSC%%의 reliability target은 아직 확정되지 않았고, 이 프로그램이 operating license%%t:OL%% 단계에서 PRA에 가정된 reliability 성능 목표가 만족되었음을 확인할 예정이다. NEI 18-04는 SR%%t:SR%%과 NSRST%%t:NSRST%%를 포함한 모든 safety-significant SSC%%t:SSC%%가 `SRP 17.4`와 비슷한 Reliability Assurance Program%%t:RAP%%에 포함되어야 한다(`should`)고 적는다.

capability target은 SSC%%t:SSC%%가 적절한 margin을 두고 PSF%%t:PSF%%를 수행하는 능력에 초점을 둔 성능 목표이며, 수명 중 열화가 capability의 일부로 고려된다. 구체적인 운전 성능 기준이 PSF%%t:PSF%% 성공 profile의 일부로 포함되고, 이 정량 target은 재해에 대응하는 발전소 능력을 보이는 해석 모델에 기반한다. SR%%t:SR%%과 NSRST%%t:NSRST%% SSC%%t:SSC%%의 capability target도 아직 확정되지 않았고, 해석 모델의 결과가 OL%%t:OL%% 단계에서 PRA에 가정된 capability target이 만족되었음을 확인할 예정이다. NEI 18-04는 SR%%t:SR%% SSC%%t:SSC%%가 발전소 운전 수명 동안 Required Safety Function%%t:RSF%% 수행 능력을 유지하도록 추가 special treatment%%t:SPECIAL_TREATMENT%% 요건을 개발해야 한다(`should`)고 적는다. SR%%t:SR%%과 NSRST%%t:NSRST%%로 분류된 SSC%%t:SSC%%에 대해 reliability와 capability로 special treatment%%t:SPECIAL_TREATMENT%% 요건을 개발하는 과정은 `Section 6.3`에 있다([[Natrium_Special_Treatment_Process]]). target의 수치는 vault에 없다.

**NRC staff 평가.** NRC staff는 일부 reliability target이 다른 원자로 설계의 비교 가능한 안전 기능에 쓰이는 전형적 값보다 낮게 설정되었고, construction permit%%t:CP%% 단계에는 이 낮은 target의 적정성을 뒷받침할 기술적 정당화가 부족하다고 적는다. target의 달성 가능성과 여유에 대한 판단은 OL%%t:OL%% 단계에서 한다.

## 관련 문서
- [[SSC_Reliability_And_Capability]]
- [[Natrium_Special_Treatment_Process]]
- [[Natrium_SRDC_Summary]]
- [[Special_Treatment]]
- [[PSAR_ch06]]
- [[Natrium_SER_SSC_Design_Review]]
