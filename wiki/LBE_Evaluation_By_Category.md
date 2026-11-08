---
type: synthesis
aliases: []
sources: [NEI_18-04, RG_1.233, SER_KU1_CP]
status: checked
verified: 2026-11-08
term:
tags: [nei-18-04]
terms_pending: []
---
# LBE 범주별 평가 방식 (Evaluation of LBEs by Category)

> [!abstract] 요약
> NEI 18-04의 과업 구조에서 결정론적 안전해석 과업은 Design Basis Accident%%t:DBA%%를 대상으로 하며, Safety-Related%%t:SR%% Structures, Systems, and Components%%t:SSC%%만의 credit으로 10 CFR 50.34 선량 한계를 보인다. Anticipated Operational Occurrence%%t:AOO%%, Design Basis Event%%t:DBE%%, Beyond Design Basis Event%%t:BDBE%%는 빈도 평균값으로 범주를 정하고, DBE%%t:DBE%% 선량은 결과 평균으로 Frequency-Consequence Target%%t:FC_TARGET%%과 비교한다. 원문에는 결정론적 안전해석을 DBA%%t:DBA%%에만 한다고 직접 쓴 문장이 없고, 심층방어(Defense-in-Depth)%%t:DID%% 평가 고려사항은 risk-significant Licensing Basis Event%%t:LBE%%의 결정론적 해석도 묻는다.

## 원문 사실
- "LBEs include AOOs, DBEs, BDBEs, and DBAs." [NEI_18-04 Table 3-1 p.14]
- "During design development, it is necessary to select an initial set of LBEs which may not be complete but are necessary to develop the basic elements of the safety design." [NEI_18-04 §3.2.2 Task 1 p.19]
- "These events are to be selected deterministically and may be supported by qualitative risk insights based on all relevant and available experience, including prior experience from the design and licensing of reactors." [NEI_18-04 §3.2.2 Task 1 p.19]
- "Because the selection of deterministic DBAs requires the selection of SR SSCs, this process also yields the selection of SR SSCs that are needed for the deterministic safety analysis in Task 7d." [NEI_18-04 §3.2.2 Task 2 p.20]
- "For each DBE identified in Task 4, a deterministic DBA is defined that includes the RSF challenges represented in the DBE but assumes that the RSFs are performed exclusively by SR SSCs, and all non-safety-related SSCs that perform these same functions are assumed to be unavailable." [NEI_18-04 §3.2.2 Task 6 p.21]
- "These DBAs are then used in DBA analysis of the license application for supporting the conservative deterministic safety analysis." [NEI_18-04 §3.2.2 Task 6 p.21]
- "The selection of conservative assumptions to be used in the DBA analysis will be informed by the quantitative uncertainty analysis of consequences that will be performed for the corresponding DBEs." [NEI_18-04 §3.2.2 Task 6 p.22]
- "The codes and thermal hydraulic models used within the PRA will be subject to the technical adequacy requirements in the supporting PRA standards, whereas the codes and models used in DBA analysis are expected to satisfy Regulatory Guide 1.203 requirements for evaluation models." [NEI_18-04 §3.2.2 Task 6 p.22]
- "The deterministic and probabilistic safety evaluations that are performed for the full set of LBEs are covered in the following five tasks." [NEI_18-04 §3.2.2 Task 7 p.22]
- "Task 7a: Evaluate LBEs Against F-C Target" [NEI_18-04 §3.2.2 Task 7a p.22]
- "The mean values of the frequencies are used to classify the LBEs into AOOs, DBEs, and BDBE categories." [NEI_18-04 §3.2.2 Task 7a p.22]
- "However, when the uncertainty bands ... defined by the 5th percentile and 95th percentile of the frequency estimates straddles a frequency boundary, the LBE is evaluated in both LBE categories." [NEI_18-04 §3.2.2 Task 7a p.22]
- "An LBE with a mean frequency less than 1E-04/plant-year with a 95th percentile above 1E-04/plant-year is evaluated as a BDBE and a DBE." [NEI_18-04 §3.2.2 Task 7a p.22]
- "DBE doses are evaluated against the F-C Target based on the mean estimates of consequence." [NEI_18-04 §3.2.2 Task 7a p.23]
- "This approach is based on the fact that the use of a conservative dose evaluation is appropriate for the deterministic safety analysis in Task 7a but is not consistent with the way in which uncertainties are addressed in risk-informed decision-making in general, where mean estimates supported by a robust uncertainty analysis are generally used to support risk significance determinations." [NEI_18-04 §3.2.2 Task 7a p.23]
- "The upper bound consequences for each DBA, defined as the 95th percentile of the uncertainty distribution, shall meet the 10 CFR 50.34 dose limit at the EAB." [NEI_18-04 §3.2.2 Task 7a p.23]
- "Task 7d: Perform Deterministic Safety Analyses Against 10 CFR 50.34" [NEI_18-04 §3.2.2 Task 7d p.25]
- "This task corresponds to the traditional deterministic safety analysis that is found in the DBA analysis of the license application." [NEI_18-04 §3.2.2 Task 7d p.25]
- "It is performed using conservative assumptions." [NEI_18-04 §3.2.2 Task 7d p.25]
- "Deterministic safety analysis can use conservative or best-estimate analytical methods with an appropriate accounting of uncertainties." [NEI_18-04 §3.2.2 Task 7d p.25]
- "Second, the deterministic DBAs are selected based on prescriptive rules and analyzed using conservative assumptions." [NEI_18-04 §3.3 p.30]
- "DBAs are then constructed, starting with each DBE, and then assuming that only the SR SSCs perform their associated RSFs." [NEI_18-04 §5.3 Task 10 p.64]
- "Task 11: Perform Safety Analysis of DBAs" [NEI_18-04 §5.3 Task 11 p.65]
- "Conservative deterministic safety analyses of the DBAs are performed in a manner that is analogous to that for current generation LWRs in this task." [NEI_18-04 §5.3 Task 11 p.65]
- "Programmatic DID considerations are taken into account in the formulation of the conservative assumptions for these analyses which need to show that the site boundary doses meet 10 CFR 50.34 acceptance limits." [NEI_18-04 §5.3 Task 11 p.65]
- "Has appropriate conservatism been applied in bounding deterministic safety analysis of more risk-significant LBEs?" [NEI_18-04 Table 5-6 p.77]
- "Is there reasonable agreement between the deterministic safety analysis of DBAs and the upper bound consequences of risk-informed DBA included in the LBE set?" [NEI_18-04 Table 5-6 p.77]
- "Are the risk-significant LBEs all properly modeled on the plant reference simulator and adequately confirmed by deterministic safety analysis?" [NEI_18-04 Table 5-6 p.77]
- "Are hazards not included in the PRA low risk to the public based on bounding deterministic analysis?" [NEI_18-04 Table 5-6 p.77]
- "describes an additional deterministic assessment of selected event sequences to supplement the consideration of AOOs, DBEs, and BDBEs for non-LWRs." [RG_1.233 §C.1 p.12]
- "A deterministic DBA is associated with each DBE that includes the required safety function challenges, but the DBA analysis is performed with the assumption that the required safety functions are performed by SR SSCs." [RG_1.233 §C.1 p.12]
- "A designer would classify a safety function as a “required safety function” if that function is needed to keep the frequency or consequence of a DBE below the F-C target using realistic assumptions, or the consequences of a DBA below the reference values included in NRC regulations using conservative assumptions." [RG_1.233 §C.2 p.16]
- "The NEI 18-04 methodology for assessing DID includes an assessment of plant risk margins that compares the mean values of each LBE frequency and dose to the F-C target." [RG_1.233 §C.3 Plant Capability Defense in Depth p.21]
- "A more conservative evaluation of margins is also performed that compares the 95th percentile upperbound values of each LBE frequency and dose to the F-C target." [RG_1.233 §C.3 Plant Capability Defense in Depth p.21]
- "Addressing DBAs in a separate section or chapter from the other LBEs could support maintaining the distinction between the deterministic analyses that assume only SR SSCs and the assessments of the remaining LBEs." [RG_1.233 §C.4 Informing the Content of Applications p.24]
- "Several of the events have 95th percentile frequencies that extend into the DBE range and should have DBAs identified per footnote 37 of Appendix A to NEI 21-07, including DHP-L1PP-1, DHP-L1PP-4, and OTH-LMAC-1." [SER_KU1_CP §3.7.1.1 p.263]

## 해설
**두 평가 방식.** NEI 18-04의 표 정의에서 LBE%%t:LBE%%는 AOO%%t:AOO%%, DBE%%t:DBE%%, BDBE%%t:BDBE%%, DBA%%t:DBA%%를 모두 포함한다. LBE%%t:LBE%% 평가 과업군의 첫 문장은 `the full set of LBEs`에 대한 결정론적·확률론적 평가가 다섯 과업에 걸쳐 있다고 적는다. 그 가운데 F-C Target%%t:FC_TARGET%% 평가 과업은 빈도 평균값으로 AOO%%t:AOO%%, DBE%%t:DBE%%, BDBE%%t:BDBE%% 범주를 정하고, DBE%%t:DBE%% 선량을 결과의 평균 추정으로 F-C Target%%t:FC_TARGET%%과 비교한다. 원문은 평균값을 쓰는 이유로, 보수적 선량 평가가 결정론적 안전해석에는 적절하지만 risk-informed decision-making의 일반적인 불확실도 처리 방식과는 맞지 않는다는 점을 든다. DBA%%t:DBA%%는 각 DBE%%t:DBE%%에서 Required Safety Function%%t:RSF%%을 SR%%t:SR%% SSC%%t:SSC%%만 수행하고 같은 기능을 하는 non-safety-related SSC%%t:SSC%%는 쓸 수 없다고 가정하여 만든다. DBA%%t:DBA%%는 규정된 규칙으로 고르고 보수적 가정으로 해석하며, 그 해석은 `site boundary` 선량이 10 CFR 50.34 한계를 만족함을 보여야 한다. [[RG_1.233]]도 RSF%%t:RSF%% 판정 기준에서 DBE%%t:DBE%%에는 `realistic assumptions`, DBA%%t:DBA%%에는 `conservative assumptions`를 짝짓는다.

**결정론적 안전해석의 대상.** 제목에 결정론적 안전해석이 들어간 과업은 §3.2.2의 `Task 7d`(`Perform Deterministic Safety Analyses Against 10 CFR 50.34`)이고, §5.3에서는 `Task 11: Perform Safety Analysis of DBAs` 본문이 DBA%%t:DBA%%의 보수적 결정론적 안전해석을 적는다. 두 과업의 본문은 해석 대상을 DBA%%t:DBA%%로 적는다. [[RG_1.233]] §C.1은 NEI 18-04가 AOO%%t:AOO%%, DBE%%t:DBE%%, BDBE%%t:BDBE%%의 고려를 보완하는 `additional deterministic assessment of selected event sequences`를 기술한다고 적고, 이어서 각 DBE%%t:DBE%%에 결정론적 DBA%%t:DBA%%가 대응한다고 적는다. §C.4는 DBA%%t:DBA%%를 다른 LBE%%t:LBE%%와 다른 절이나 장에서 다루면 `the deterministic analyses that assume only SR SSCs`와 `the assessments of the remaining LBEs`의 구분을 유지하는 데 도움이 될 수 있다고(`could`) 적는다. 그러나 원문에는 결정론적 안전해석을 DBA%%t:DBA%%에만 한다고 직접 쓴 문장이 없다. 이 노트의 결론은 과업 구조와 위 [[RG_1.233]] 문장에서 읽은 것이다.

**과업 번호 표기.** 설계 개발과 해석 과업은 결정론적 안전해석을 `Task 7d`에 있다고 적는다. 반면 F-C Target%%t:FC_TARGET%% 평가 과업(`Task 7a: Evaluate LBEs Against F-C Target`)의 한 문장은 결정론적 안전해석을 `Task 7a`에 있다고 적는다. 이 노트는 과업 제목을 따라 `Task 7d`로 쓴다([[Deterministic_Safety_Analysis_Task_7d]]).

**DBA%%t:DBA%% 밖의 결정론적 해석.** programmatic 심층방어%%t:DID%% 속성의 평가 고려사항 표에서 결정론적 해석을 묻는 고려사항은 네 개이며, 그 가운데 세 개는 DBA%%t:DBA%% 밖의 대상을 묻는다. 첫째, 더 risk-significant한 LBE%%t:LBE%%의 `bounding deterministic safety analysis`에 적절한 보수성이 적용되었는가. 둘째, risk-significant LBE%%t:LBE%%가 `deterministic safety analysis`로 적절히 확인되었는가. 셋째, PRA에 포함되지 않은 hazard가 `bounding deterministic analysis`에 근거해 공중에 대한 위험이 낮은가. 같은 표는 DBA%%t:DBA%%의 결정론적 안전해석과 LBE%%t:LBE%% 집합에 포함된 `risk-informed DBA`의 상한 결과가 합리적으로 일치하는지도 묻는다. 따라서 결정론적 해석은 과업 수준에서는 DBA%%t:DBA%%를 대상으로 하지만, 심층방어%%t:DID%% 평가 단계에서는 risk-significant LBE%%t:LBE%%와 PRA 밖 hazard에도 쓰일 수 있다. 설계 초기의 LBE%%t:LBE%% 초기 목록을 결정론적으로(`deterministically`) 고르는 것은 사건 선정 방식이며, 사건 해석 방식이 아니다.

**해석 방법과 가정.** `Task 7d`는 이 과업이 보수적 가정으로 수행된다고 적는다. 같은 과업은 결정론적 안전해석이 불확실도를 적절히 고려한 보수적 또는 best-estimate 해석 방법을 쓸 수 있다고도(`can`) 적는다. 원문은 이 두 문장의 관계를 설명하지 않는다. DBA%%t:DBA%% 해석의 보수적 가정을 고를 때는 대응 DBE%%t:DBE%%에 대해 수행할 결과의 정량적 불확실도 해석을 참고한다(`will be informed by`). PRA의 코드와 열수력 모형은 PRA 표준의 기술적 적합성 요건을 따르고, DBA%%t:DBA%% 해석의 코드와 모형은 `Regulatory Guide 1.203`의 evaluation model 요건을 만족할 것으로 기대된다(`expected to`).

**범주 경계와 상한값.** 범주 지정은 평균값을 쓰지만, 빈도의 5th–95th percentile 구간이 경계에 걸치면 LBE%%t:LBE%%를 두 범주 모두에서 평가한다. 예를 들어 평균 빈도가 1E-04/plant-year보다 낮고 95th percentile이 1E-04/plant-year보다 높은 LBE%%t:LBE%%는 BDBE%%t:BDBE%%이자 DBE%%t:DBE%%로 평가한다. DBA%%t:DBA%%는 각 DBE%%t:DBE%%에서 만들므로, 이렇게 DBE%%t:DBE%%로도 평가되는 사건은 DBA%%t:DBA%% 유도와 연결될 수 있다. Kemmerer `SER`에서 staff는 95th percentile 빈도가 DBE%%t:DBE%% 영역에 들어가는 사건(DHP-L1PP-1, DHP-L1PP-4, OTH-LMAC-1 등)에 NEI 21-07에 따라 DBA%%t:DBA%%를 식별해야 한다고(`should`) 지적했다([[Natrium_SER_BDBE_DBA_Review]]). DBA%%t:DBA%% 선량은 불확실도 분포의 95th percentile 상한으로 `EAB`의 10 CFR 50.34 한계를 만족해야 한다. [[RG_1.233]] §C.3의 `Plant Capability Defense in Depth` 소절은 심층방어%%t:DID%% 평가가 각 LBE%%t:LBE%% 빈도와 선량의 평균값을 F-C Target%%t:FC_TARGET%%과 비교하는 risk margin 평가를 포함한다고 적는다. 같은 소절은 95th percentile 상한값을 F-C Target%%t:FC_TARGET%%과 비교하는 더 보수적인 margin 평가도 수행한다고 적는다([[RG_1233_DID_Staff_Position]]).

## 관련 문서
- [[Deterministic_Safety_Analysis_Task_7d]]
- [[LBE_Selection_Process]]
- [[Licensing_Basis_Event]]
- [[LBE_Frequency_Categories]]
- [[LBE_Risk_Significance]]
- [[Required_Safety_Function]]
- [[Uncertainty_Treatment]]
- [[DID_Integrated_Process]]
- [[Programmatic_DID]]
- [[RG_1233_LBE_Staff_Position]]
- [[RG_1233_SSC_Classification_Staff_Position]]
- [[RG_1233_DID_Staff_Position]]
- [[Natrium_SER_BDBE_DBA_Review]]
- [[F_C_Target]]
