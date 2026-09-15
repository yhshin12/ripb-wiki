---
type: natrium
aliases: []
sources:
- PSAR_ch06
- NEI_18-04
status: checked
verified: 2026-09-16
term: null
tags:
- natrium
terms_pending: []
---

# Natrium의 design-basis hazard level 상호작용 방지 요건 (Natrium DBHL-Related Requirements for Non-Safety-Related SSCs)

> [!abstract] 요약
> `PSAR` Chapter 6은 Non-Safety-Related with Special Treatment%%t:NSRST%%와 Non-Safety-Related with No Special Treatment%%t:NST%% Structures, Systems, and Components%%t:SSC%%의 고장이 design-basis hazard level%%t:DBHL%% 조건에서 Safety-Related%%t:SR%% SSC%%t:SSC%%의 기능 수행을 해치지 않도록 세 기준 가운데 적어도 하나를 적용한다. 재배치나 barrier로 불리한 지진 상호작용을 배제할 수 없는 `seismic interaction source`는 `ASCE 7-16` 설계에 `ASCE 43-19` `Limit State B` 평가를 더하고, 소듐을 담은 SSC%%t:SSC%%는 지진으로 인한 화재 가능성 때문에 별도의 `seismic interaction source`로 다룬다.

## 원문 사실
- "NSRST and NST SSCs are designed such that the DBHLs will not cause an NSRST or NST SSC to adversely impact the ability of an SR SSC to perform an SR function." [PSAR_ch06 §6.1.3 p.8]
- "DBHL-related interactions between NSRST or NST SSCs and SR SSCs are prevented by at least one of the following criteria:" [PSAR_ch06 §6.1.3 p.8]
- "The failure of the NSRST or NST SSC does not cause the NSRST or NST SSC to strike an SR SSC." [PSAR_ch06 §6.1.3 p.8]
- "The failure of the NSRST or NST SSC does not adversely impact the ability of an SR SSC to perform an SR function." [PSAR_ch06 §6.1.3 p.8]
- "The NSRST or NST SSC is analyzed and designed to prevent its failure under DBHL conditions." [PSAR_ch06 §6.1.3 p.8]
- "Design requirements implemented for the prevention of seismic and tornado DBHL-related interactions are described in Section 6.1.3.1 and Section 6.1.3.2, respectively." [PSAR_ch06 §6.1.3 p.8]
- "Interaction prevention design requirements for the other DBHLs identified in Section 6.1.1 will be developed at the OL stage, as necessary." [PSAR_ch06 §6.1.3 p.8]
- "Seismic interactions are identified through an area-based review process that considers safety-significant SSCs as seismic interaction targets." [PSAR_ch06 §6.1.3.1 p.8]
- "Credible seismic interaction source and target pairs are compiled considering physical zone of influence." [PSAR_ch06 §6.1.3.1 p.8]
- "Seismic interaction prevention design requirements are assigned to seismic interaction sources when adverse seismic interactions cannot be precluded through alternate methods such as physical rearrangement or barriers." [PSAR_ch06 §6.1.3.1 p.8]
- "NSRST and NST SSCs designed to prevent seismic DBHL-related interactions are designed in accordance with ASCE 7-16 (Reference 6.1-3) at a level consistent with the SCN1 seismic classification, as defined in Section 6.4.1.1 with parameters provided in Table 6.4-1B." [PSAR_ch06 §6.1.3.1 p.9]
- "Additional design evaluations demonstrate that the NSRST or NST seismic interaction source SSC will withstand the SSE at a seismic performance level greater than or equal to that of the seismic interaction target SSC with an acceptance criterion of moderate inelastic deformation." [PSAR_ch06 §6.1.3.1 p.9]
- "The design evaluations apply response parameters that correspond to ASCE 43-19 (Reference 6.1-4) Limit State B." [PSAR_ch06 §6.1.3.1 p.9]
- "ASCE 43-19 Limit State B is the target performance for collapse prevention for any SSC that is identified as a seismic interaction hazard to an SSC with a required safety function." [PSAR_ch06 §6.1.3.1 p.9]
- "If the ASCE 43-19 Limit State B capacity is not initially met, then additional requirements are incorporated into the SSC design to support meeting ASCE 43-19 Limit State B." [PSAR_ch06 §6.1.3.1 p.9]
- "ASCE 43-19 parameters are used in evaluations to supplement the ASCE 7-16 code of record calculations." [PSAR_ch06 §6.1.3.1 p.9]
- "The supplemental evaluations demonstrate the seismic capacity for the target performance equals or exceeds the SSE." [PSAR_ch06 §6.1.3.1 p.9]
- "To expedite the evaluation process, limitations and additional requirements are considered in the ASCE 7-16 seismic design process to support meeting a limit state consistent with ASCE 43-19 Limit State B including:" [PSAR_ch06 §6.1.3.1 p.9]
- "Limiting structural systems to those endorsed by ASCE 43-19" [PSAR_ch06 §6.1.3.1 p.9]
- "Including ductile detailing in design" [PSAR_ch06 §6.1.3.1 p.9]
- "Limiting ASCE 7 Response Modification Coefficients (R and Rp) based on ASCE 43 inelastic energy absorption factors (Fμ) for LS-B." [PSAR_ch06 §6.1.3.1 p.9]
- "For buildings, the seismic response parameters are based on ASCE 4 methodologies, or equivalent, that achieve an 80% non-exceedance probability for seismic demand." [PSAR_ch06 §6.1.3.1 p.9]
- "Design evaluations also demonstrate that seismic separation between an NSRST or NST SSC and adjacent SR SSCs will exceed the required seismic separation for the SSE." [PSAR_ch06 §6.1.3.1 p.9]
- "The methods of ASCE 43-19 Section 7.3 are applied for evaluation of seismic separation." [PSAR_ch06 §6.1.3.1 p.9]
- "Per ASCE 43-19 Section 7.3, elastically computed displacements are increased by a factor to account for the inelastic response." [PSAR_ch06 §6.1.3.1 p.9]
- "Construction tolerances are considered when determining the required minimum as-designed seismic separation." [PSAR_ch06 §6.1.3.1 p.9]
- "In addition to physical interaction sources addressed above, sodium containing SSCs are treated as a special seismic interaction source based on the potential for seismic-induced fire." [PSAR_ch06 §6.1.3.1 p.9]
- "Sodium-containing SSCs are subject to a requirement to demonstrate the ability to retain sodium inventory following an SSE." [PSAR_ch06 §6.1.3.1 p.9]
- "Seismic performance for sodium retention is targeted at a level equivalent to SR SSCs and can be achieved through design or alternative means." [PSAR_ch06 §6.1.3.1 p.9]
- "Seismic interaction sources, including NST SSCs, have design, analysis, and programmatic controls with a quality level consistent with that of NSRST SSCs." [PSAR_ch06 §6.1.3.1 p.9]
- "Programmatic controls include inspection and maintenance with the objective of confirming and maintaining the critical characteristics of the seismic interaction sources such that seismic interaction design evaluations remain valid." [PSAR_ch06 §6.1.3.1 p.9]
- "The consideration of NSRST SSCs as seismic interaction targets is addressed in Section 6.4.1.5.2." [PSAR_ch06 §6.1.3.1 p.10]
- "NSRST and NST SSCs designed to prevent tornado DBHL-related interactions are designed in accordance with the wind loads and provisions of ASCE 7-16 using the design basis tornado hazard wind speed, atmospheric pressure drop, and tornado missiles identified in Table 2.1-1." [PSAR_ch06 §6.1.3.2 p.10]
- "Interaction of NSRST and non-safety-related with no special treatment (NST) SSCs with SR SSCs is described in Section 6.1.3.1." [PSAR_ch06 §6.4.1.5.1 p.22]
- "In addition to seismic interaction consideration in 6.1.3.1 for DBHL, the seismic design process ensures seismic interactions from NSRST or NST SSCs will not adversely impact the ability of an SR SSC to perform its required safety function for all seismic hazards." [PSAR_ch06 §6.4.1.5.1 p.22]
- "Interaction of NSRST and NST SSCs with NSRST SSCs is considered in the seismic design process and ensures seismic interactions from NSRST or NST SSCs will not adversely impact the ability of a seismic significant NSRST SSC to perform its safety function." [PSAR_ch06 §6.4.1.5.2 p.22]
- "The seismic capability of the NSRST seismic interaction target SSC is based on its seismic classification, and the associated design for seismic interaction source failure modes supports this capability." [PSAR_ch06 §6.4.1.5.2 p.22]
- "It is noted that there will be design requirements to protect all SR SSCs from any adverse impacts of any DBEHLs." [NEI_18-04 §4 p.38]
- "This may lead to design requirements to prevent any adverse impacts from failure of an SSC classified as NST or NSRST that could otherwise prevent an SR SSC from performing its RSFs." [NEI_18-04 §4 p.38]

## 해설
NSRST%%t:NSRST%%와 NST%%t:NST%% SSC%%t:SSC%%는 DBHL%%t:DBHL%%이 이들로 하여금 SR%%t:SR%% SSC%%t:SSC%%의 SR%%t:SR%% 기능 수행을 해치게 하지 않도록 설계된다. 상호작용은 세 기준 가운데 적어도 하나로 방지된다. NSRST%%t:NSRST%%나 NST%%t:NST%% SSC%%t:SSC%%의 고장이 SR%%t:SR%% SSC%%t:SSC%%를 치지 않거나, 그 고장이 SR%%t:SR%% 기능 수행에 악영향을 주지 않거나, 그 SSC%%t:SSC%%가 DBHL%%t:DBHL%% 조건에서 고장나지 않도록 해석·설계되는 것이다. 지진과 토네이도 이외 재해에 대한 상호작용 방지 설계 요건은 필요하면 operating license%%t:OL%% 단계에서 개발된다.

지진 상호작용은 safety-significant SSC%%t:SSC%%를 `seismic interaction target`으로 보는 `area-based review process`로 식별하고, `physical zone of influence`를 고려해 신뢰할 만한 `source and target pairs`를 모은다. 재배치나 barrier%%t:BARRIER%% 같은 다른 방법으로 불리한 상호작용을 배제할 수 없을 때 `seismic interaction source`에 방지 설계 요건을 부여한다. 그런 NSRST%%t:NSRST%%·NST%%t:NST%% SSC%%t:SSC%%는 `Section 6.4.1.1`에 정의된 `SCN1` seismic classification과 일관된 수준으로 `ASCE 7-16`에 따라 설계되고, 추가 설계 평가로 source SSC%%t:SSC%%가 Safe Shutdown Earthquake%%t:SSE%%를 target SSC%%t:SSC%% 이상의 `seismic performance level`로, `moderate inelastic deformation`을 허용 기준으로 견딤을 보인다. 이 평가는 `ASCE 43-19` `Limit State B`에 해당하는 `response parameters`를 쓰며, `Limit State B`는 `required safety function`을 가진 SSC%%t:SSC%%에 대한 지진 상호작용 위험으로 식별된 SSC%%t:SSC%%의 `target performance for collapse prevention`이다. 처음에 `Limit State B` capacity를 만족하지 못하면 추가 요건을 설계에 넣는다. 건물의 `seismic response parameters`는 `seismic demand`에 대해 `80%` `non-exceedance probability`를 얻는 `ASCE 4` 방법이나 동등한 방법에 기반한다. 설계 평가는 NSRST%%t:NSRST%%나 NST%%t:NST%% SSC%%t:SSC%%와 인접 SR%%t:SR%% SSC%%t:SSC%% 사이의 `seismic separation`이 Safe Shutdown Earthquake%%t:SSE%%에 필요한 이격을 넘는다는 것도 보이며, 이격은 `ASCE 43-19` `Section 7.3` 방법으로 평가하고 필요한 최소 설계 이격을 정할 때 `construction tolerances`를 고려한다.

소듐을 담은 SSC%%t:SSC%%는 지진으로 인한 화재 가능성 때문에 별도의 `seismic interaction source`로 다루며, Safe Shutdown Earthquake%%t:SSE%% 뒤 `sodium inventory`를 보유할 수 있음을 보여야 한다. 소듐 보유를 위한 지진 성능은 SR%%t:SR%% SSC%%t:SSC%%와 동등한 수준을 목표로 하고 설계나 대체 수단으로 달성할 수 있다. NST%%t:NST%% SSC%%t:SSC%%를 포함한 `seismic interaction sources`는 NSRST%%t:NSRST%% SSC%%t:SSC%%와 일관된 품질 수준의 설계·해석·programmatic control을 가지며, 그 control에는 상호작용 설계 평가가 유효하도록 source의 `critical characteristics`를 확인·유지하는 검사와 보수가 포함된다. 토네이도 상호작용을 막도록 설계되는 NSRST%%t:NSRST%%·NST%%t:NST%% SSC%%t:SSC%%는 `Table 2.1-1`의 `design basis tornado` 풍속, 기압 강하, 토네이도 미사일을 써서 `ASCE 7-16`의 `wind loads and provisions`에 따라 설계된다.

지진 설계 과정은 DBHL%%t:DBHL%% 상호작용 고려에 더해 모든 지진 재해에서 NSRST%%t:NSRST%%·NST%%t:NST%% SSC%%t:SSC%%의 상호작용이 SR%%t:SR%% SSC%%t:SSC%%의 `required safety function` 수행을 해치지 않도록 하고, `seismic significant` NSRST%%t:NSRST%% SSC%%t:SSC%%의 safety function 수행도 해치지 않도록 한다. NSRST%%t:NSRST%% `seismic interaction target` SSC%%t:SSC%%의 seismic capability는 그 seismic classification에 기반한다([[Natrium_Seismic_Classification]]). NEI 18-04도 모든 SR%%t:SR%% SSC%%t:SSC%%를 Design Basis External Hazard Level%%t:DBEHL%%의 악영향으로부터 보호하는 설계 요건이 있을 것이며, 이로 인해 NST%%t:NST%%나 NSRST%%t:NSRST%% SSC%%t:SSC%% 고장이 SR%%t:SR%% SSC%%t:SSC%%의 Required Safety Function%%t:RSF%% 수행을 막지 않도록 하는 설계 요건이 생길 수 있다고 적는다.

## 관련 문서
- [[Natrium_Design_Basis_Hazard_Levels]]
- [[Natrium_Seismic_Classification]]
- [[Special_Treatment]]
- [[Natrium_SSC_Safety_Classification]]
- [[PSAR_ch06]]
