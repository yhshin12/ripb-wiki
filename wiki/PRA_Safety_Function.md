---
type: concept
aliases: [PSF]
sources: [NEI_18-04]
status: checked
verified: 2026-09-15
term: PSF
tags: []
terms_pending: []
---
# PRA Safety Function (PSF)

> [!abstract] 요약
> PRA Safety Function%%t:PSF%%은 PRA에 모델링된 Structures, Systems, and Components%%t:SSC%%의 기능 가운데 발전소 안의 방사성 물질 원천에서 방출을 막거나 완화하는 기능이다. 그중 Design Basis Event%%t:DBE%% 선량을 Frequency-Consequence Target%%t:FC_TARGET%% 안에 두는 데 필요한 것이 Required Safety Function%%t:RSF%%이며, 그 정의는 IAEA의 Fundamental Safety Function%%t:FSF%%에서 출발해 원자로별로 구체화된다.

## 원문 사실
- "Reactor design specific SSC functions modeled in a PRA that serve to prevent and/or mitigate a release of radioactive material or to protect one or more barriers to release." [NEI_18-04 §6 p.90]
- "A PSF, as used in the LMP, is any function by any SSC modeled in the PRA that is responsible for preventing or mitigating a release of radioactive material from any radioactive material source within the plant." [NEI_18-04 §3.3.4 p.31]
- "SSCs that perform the PRA Safety Functions that protect the barriers serve to prevent challenges to the barriers or enhance the effectiveness of barriers in preventing or limiting releases of radioactive material." [NEI_18-04 §3.3 p.29]
- "Some of these safety functions should be further classified as RSFs if they are necessary to ensure that all the DBEs have doses that fall within the F-C Target and also to ensure that the doses for the DBAs meet the requirements of 10 CFR 50.34 using conservative assumptions." [NEI_18-04 §3.3.4 p.31]
- "From these sets of SSCs, the designer selects a set of SR SSCs to perform each RSF." [NEI_18-04 §3.3.4 p.31]
- "RSFs are defined starting with generic Fundamental Safety Functions (FSFs) defined by the International Atomic Energy Agency (IAEA) of controlling heat generation, controlling heat removal, and retaining radionuclides." [NEI_18-04 §3.3.4 p.32]
- "These are refined as necessary into reactor technology-specific safety functions that reflect the reactor concept and unique characteristics of the reactors." [NEI_18-04 §3.3.4 p.32]
- "Safety functions common to all reactor technologies and designs; includes control heat generation, control heat removal and confinement of radioactive material" [NEI_18-04 §6 p.90]

## 해설
PSF%%t:PSF%%는 PRA에 모델링된 SSC%%t:SSC%% 기능 가운데, 발전소 안 어느 방사성 물질 원천에서든 방출을 막거나 완화하는 기능 전부를 가리킨다. 방벽을 보호해 방벽에 대한 부담을 막거나 방벽의 효과를 높이는 기능도 여기에 들어간다.

PSF%%t:PSF%% 가운데 모든 DBE%%t:DBE%% 선량을 F-C Target%%t:FC_TARGET%% 안에 두고, Design Basis Accident%%t:DBA%% 선량이 보수적 가정에서 10 CFR 50.34 요건을 만족하도록 하는 데 필요한 기능이 RSF%%t:RSF%%로 분류된다. 설계자는 이 기능을 수행할 수 있는 SSC%%t:SSC%% 가운데서 Safety-Related%%t:SR%% SSC%%t:SSC%%를 고른다. 선정 절차는 [[Required_Safety_Function]]에 있다.

RSF%%t:RSF%% 정의의 출발점은 IAEA가 정의한 FSF%%t:FSF%% 세 가지, 즉 controlling heat generation, controlling heat removal, retaining radionuclides이다. 원문은 이를 원자로 개념과 고유 특성에 맞는 원자로 기술별 safety function으로 구체화하고, 그 기능을 수행할 SSC%%t:SSC%%를 고르는 바탕으로 삼는다. 용어집의 FSF%%t:FSF%% 정의는 세 번째 기능을 confinement of radioactive material로 적어 표현이 조금 다르다.

## 관련 문서
- [[Required_Safety_Function]]
- [[PRA_Role_In_LBE_Selection]]
- [[Event_Sequence_Family]]
- [[NEI_18-04]]
