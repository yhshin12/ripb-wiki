---
type: concept
aliases: [RSF]
sources: [NEI_18-04]
status: checked
verified: 2026-09-15
term: RSF
tags: []
terms_pending: []
---
# Required Safety Function (RSF)

> [!abstract] 요약
> Required Safety Function%%t:RSF%%은 Design Basis Event%%t:DBE%%의 결말이나 결말이 큰 Beyond Design Basis Event%%t:BDBE%%의 빈도를 Frequency-Consequence Target%%t:FC_TARGET%% 안에 두기 위해 반드시 수행되어야 하는 PRA Safety Function%%t:PSF%%이다. 이를 수행하도록 고른 설비가 Safety-Related%%t:SR%% Structures, Systems, and Components%%t:SSC%%이며, Design Basis Accident%%t:DBA%%는 이 설비만으로 기능을 수행한다고 가정해 정의된다.

## 원문 사실
- "A PRA Safety Function that is required to be fulfilled to maintain the consequence of one or more DBEs or the frequency of one or more high-consequence BDBEs inside the F-C Target" [NEI_18-04 §6 p.90]
- "Reactor design specific SSC functions modeled in a PRA that serve to prevent and/or mitigate a release of radioactive material or to protect one or more barriers to release." [NEI_18-04 §6 p.90]
- "SSCs that are credited in the fulfillment of RSFs and are capable to perform their RSFs in response to any Design Basis External Hazard Level" [NEI_18-04 §6 p.90]
- "A design specification of the level of severity or intensity of an external hazard for which the Safety-Related SSCs are designed to withstand with no adverse impact on their capability to perform their RSFs" [NEI_18-04 §6 p.90]
- "In Task 5a, the full set of DBEs are examined to identify the PSFs that are necessary and sufficient to meet the F-C Target for all DBEs and high-consequence BDBEs, and to conservatively ensure that 10 CFR 50.34 dose requirements can be met." [NEI_18-04 §3.2.2 Task 5a p.21]
- "High consequence BDBEs are those with consequences that exceed 10 CFR 50.34 dose criteria." [NEI_18-04 §3.2.2 Task 5a p.21]
- "RSFs for any high-consequence BDBEs are responsible for preventing them from increasing in frequency into the DBE region and outside the F-C Target by exhibiting sufficient reliability performance to keep the BDBE frequency sufficiently low." [NEI_18-04 §3.2.2 Task 5a p.21]
- "For each of these RSFs identified in Task 5a, a decision is made on which set of SSCs is selected to perform these RSFs among those found to be available on each DBE." [NEI_18-04 §3.2.2 Task 5b p.21]
- "Structures and physical barriers that are necessary to protect any SR SSCs in performing their RSFs in response to any design basis external event are also classified as SR." [NEI_18-04 §3.2.2 Task 5b p.21]
- "SR SSCs are also selected for any RSF associated with any high-consequence BDBEs in which the reliability of the SSC is necessary to keep the event in the BDBE frequency region." [NEI_18-04 §3.2.2 Task 5b p.21]
- "For each DBE identified in Task 4, a deterministic DBA is defined that includes the RSF challenges represented in the DBE but assumes that the RSFs are performed exclusively by SR SSCs, and all non-safety-related SSCs that perform these same functions are assumed to be unavailable." [NEI_18-04 §3.2.2 Task 6 p.21]
- "advanced non-LWRs will employ a diverse combination of inherent, passive, and active design features to perform the RSFs across layers of defense ... the application of a single failure criterion is not deemed to be necessary." [NEI_18-04 §3.2.2 Task 6 p.22]
- "With the understanding that SR SSCs are required to be capable of performing their RSFs in response to external events within the DBEHL, there will be no new DBAs introduced by external hazards." [NEI_18-04 §3.2.2 Task 6 p.22]

## 해설
RSF%%t:RSF%%는 DBE%%t:DBE%% 전체를 검토해 도출한다. DBE%%t:DBE%%에서는 결말을 F-C Target%%t:FC_TARGET%% 안으로 완화하는 기능이고, 결말이 10 CFR 50.34 선량 기준을 넘는 BDBE%%t:BDBE%%에서는 충분한 신뢰도로 빈도를 낮게 유지해 DBE%%t:DBE%% 영역으로 올라오지 않게 하는 기능이다. 모든 RSF%%t:RSF%%는 PSF%%t:PSF%% 가운데서 고른다.

각 RSF%%t:RSF%%를 수행할 SSC%%t:SSC%% 조합을 해당 DBE%%t:DBE%%에서 쓸 수 있는 설비 가운데 고르면 그것이 SR%%t:SR%% SSC%%t:SSC%%가 된다. SR%%t:SR%% SSC%%t:SSC%%를 외부 사건으로부터 보호하는 구조물과 물리적 barrier%%t:BARRIER%%도 SR%%t:SR%%로 분류된다. 결말이 큰 BDBE%%t:BDBE%%의 빈도를 묶어 두는 데 신뢰도가 필요한 설비도 같은 방식으로 SR%%t:SR%%이 된다.

Task 4에서 찾은 DBE%%t:DBE%% 하나마다 결정론적 DBA%%t:DBA%%를 하나씩 정의한다. DBA%%t:DBA%%는 그 DBE%%t:DBE%%의 RSF%%t:RSF%% 부담을 그대로 두되, 그 기능을 SR%%t:SR%% SSC%%t:SSC%%만 수행하고 같은 기능을 하는 비안전 등급 설비는 쓸 수 없다고 가정한다. 원문은 여러 Layers of Defense%%t:LAYERS_OF_DEFENSE%%에 걸쳐 고유·피동·능동 설계 특성을 조합한다는 점 등을 들어 단일 고장 기준이 필요하지 않다고 본다.

외부 재해에 대해서는 Design Basis External Hazard Level%%t:DBEHL%%을 정한다. 용어집은 DBEHL%%t:DBEHL%%을 SR%%t:SR%% SSC%%t:SSC%%가 RSF%%t:RSF%% 수행 능력에 악영향 없이 견디도록 설계되는 외부 재해의 심각도나 강도의 수준에 대한 설계 사양으로 정의한다. SR%%t:SR%% SSC%%t:SSC%%는 DBEHL%%t:DBEHL%% 안의 외부 사건에서도 RSF%%t:RSF%%를 수행해야 하므로, 외부 재해 때문에 새 DBA%%t:DBA%%가 생기지는 않는다.

## 관련 문서
- [[LBE_Selection_Process]]
- [[LBE_Frequency_Categories]]
- [[F_C_Target]]
- [[Required_Functional_Design_Criteria]]
- [[NEI_18-04]]
