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
# SSC 설계 요건의 도출과 barrier 요건 (Development of SSC Design and Performance Requirements)

> [!abstract] 요약
> Structures, Systems, and Components%%t:SSC%%의 설계 요건은 Safety-Related%%t:SR%%, Non-Safety-Related with Special Treatment%%t:NSRST%%, Non-Safety-Related with No Special Treatment%%t:NST%% 세 범주마다 정해진다. 출발점은 소유자 요건을 충족하는 데 필요한 SSC%%t:SSC%% 기능의 식별이고, 방사성 물질 방출의 예방·완화에 관련된 SSC%%t:SSC%%에서 첫째 우선순위는 Licensing Basis Event%%t:LBE%% 전체에 나타난 기능에 대한 능력과 신뢰도이다. SR%%t:SR%%과 비안전 등급 SSC%%t:SSC%%는 모두 LBE%%t:LBE%% 전체와 대조되며, barrier%%t:BARRIER%% 요건은 개별 물리적 barrier%%t:BARRIER%%만 보아서는 정할 수 없고 PRA가 뒷받침하는 LBE%%t:LBE%% 평가와 연결된다.

## 원문 사실
- "This section describes the approach for defining the design requirements for each of the three SSC safety categories: SR, NSRST, and NST." [NEI_18-04 §4.4 p.48]
- "These design requirements begin with the identification of the SSC functions that are necessary to meet owner requirements for energy production, investment protection, worker and public safety, and licensing." [NEI_18-04 §4.4 p.48]
- "SSC functions associated with the prevention and mitigation of release of radioactive material from the plant are modeled in the PRA and are represented in the LBEs." [NEI_18-04 §4.4 p.48]
- "The first priority in establishing the design requirements for all the SSCs associated with the prevention and mitigation of release of radioactive material is to ensure that the capability and reliability of each SSC are sufficient for all the SSC functions represented in the LBEs, including the AOOs, DBEs, BDBEs, and DBAs." [NEI_18-04 §4.4 p.48]
- "A related priority is to provide reasonable confidence that the reliability and capability of the SSCs are achieved and maintained throughout the lifetime of the plant." [NEI_18-04 §4.4 p.48]
- "Those SSCs that are classified as SR are expected to meet applicable regulatory requirements as well as reactor-specific and design-specific SRDC derived from the RFDC." [NEI_18-04 §4.4 p.48]
- "Although the SR SSCs are derived from an evaluation of the RSFs to mitigate the DBEs and DBAs, the SR and non-safety-related SSCs are evaluated against the full set of LBEs—including the AOOs and BDBEs, as well as normal plant operation—at the plant level to ensure that the F-C Target is met." [NEI_18-04 §4.4.3 p.49]
- "This leads to design requirements for both the SR and non-safety-related SSCs across the full set of LBEs, including the DBAs." [NEI_18-04 §4.4.3 p.49]
- "SSCs that provide functions that support the retention of radioactive material within barriers have associated regulatory design requirements that are derived from the evaluation of the LBE against the F-C Target and the RFDCs." [NEI_18-04 §4.4.4 p.49]
- "These functions include barrier functions in which the SSC serves as a physical or functional barrier to the transport of radionuclides and indirect functions in which performance of an SSC function serves to protect one or more other SSCs that may be classified as barriers." [NEI_18-04 §4.4.4 p.49]
- "However, a more complete perspective on the role of barriers and the SSCs that protect each barrier needs to consider the barrier response to each of the LBEs derived from the PRA." [NEI_18-04 §4.4.4 p.49]
- "The LBEs delineate the barrier failure modes, the challenges to barrier integrity, and the interactions between SSCs that influence the effectiveness of each barrier within a given layer of defense and the extent of independence among layers of defense." [NEI_18-04 §4.4.4 p.49]
- "The evaluation of mechanistic source terms that help determine the offsite doses provides another performance metric for evaluating the effectiveness of each barrier within a given layer of defense." [NEI_18-04 §4.4.4 p.49]
- "When viewed across all the LBEs, each barrier plays a specific role within a given layer of defense in the retention of radionuclides; however, those roles are different in different LBEs." [NEI_18-04 §4.4.4 p.50]
- "A full picture of the synergistic roles that each of the SSCs that comprise these layers of defense plays must consider the ways in which the SSCs mutually support the FSF of radionuclide retention." [NEI_18-04 §4.4.4 p.50]
- "It is noted that some non-LWRs employ functional barriers that are different from the physical barriers frequently employed in the past." [NEI_18-04 §4.4.4 p.50]
- "the term “barrier” is used to denote any plant feature within a given layer of defense that is responsible for either prevention of radionuclide release or reduction in the quantity of radionuclide release during an event." [NEI_18-04 §4.4.4 p.50]
- "It comprises physical barriers and any other features that are responsible for mitigating the quantity of material released, including time delays that permit radionuclide decay." [NEI_18-04 §4.4.4 p.50]
- "In summary, the definition of requirements for barriers cannot be fully developed simply by examining the capability of discrete physical barriers to retain radionuclides." [NEI_18-04 §4.4.4 p.50]
- "It is important to assure that barriers and other contributions to layers of defense are functionally independent." [NEI_18-04 §4.4.4 p.50]
- "A systematic development of SSC design requirements must consider a full spectrum of barrier challenges, barrier interactions, and barrier dependencies within layers of defense." [NEI_18-04 §4.4.4 p.50]
- "A full examination of the barrier challenges, interactions and dependencies requires the performance of a technically sound PRA." [NEI_18-04 §4.4.4 p.50]
- "Hence, it is logical that the approach to formulating requirements for barriers and other SSCs be linked to a systematic identification and evaluation of LBEs supported by a PRA." [NEI_18-04 §4.4.4 p.50]
- "Layers of defense are those plant capabilities and programmatic elements that provide, collectively, independent means for the prevention and mitigation of adverse events." [NEI_18-04 §6 p.90]

## 해설
원문은 SSC%%t:SSC%% 설계 요건이 에너지 생산, 투자 보호, 작업자와 공중의 안전, 인허가에 필요한 SSC%%t:SSC%% 기능을 식별하는 데서 시작한다고 적는다. 방사성 물질 방출의 예방과 완화에 관련된 기능은 PRA에 모델링되어 LBE%%t:LBE%%에 나타난다. 이런 SSC%%t:SSC%%의 설계 요건에서 첫째 우선순위는 Anticipated Operational Occurrence%%t:AOO%%, Design Basis Event%%t:DBE%%, Beyond Design Basis Event%%t:BDBE%%, Design Basis Accident%%t:DBA%%를 포함한 모든 LBE%%t:LBE%%의 기능에 대해 능력과 신뢰도가 충분하도록 하는 것이다. 이와 연관된 우선순위는 그 능력과 신뢰도가 발전소 수명 동안 달성되고 유지된다는 합리적 확신을 주는 것이다.

SR%%t:SR%% SSC%%t:SSC%%는 적용 가능한 규제 요건과 함께, Required Functional Design Criteria%%t:RFDC%%에서 도출한 원자로별·설계별 Safety-Related Design Criteria%%t:SRDC%%를 만족할 것으로 기대된다. 도출 과정은 [[Required_Functional_Design_Criteria]]에 있다. SR%%t:SR%% SSC%%t:SSC%%는 DBE%%t:DBE%%와 DBA%%t:DBA%%를 완화하는 Required Safety Function%%t:RSF%% 평가에서 선정되지만, SR%%t:SR%%과 비안전 등급 SSC%%t:SSC%%는 모두 AOO%%t:AOO%%, BDBE%%t:BDBE%%, 정상 운전까지 포함한 LBE%%t:LBE%% 전체와 발전소 수준에서 대조되어 Frequency-Consequence Target%%t:FC_TARGET%% 만족 여부를 확인받는다. 따라서 두 부류 모두에 LBE%%t:LBE%% 전체에 걸친 설계 요건이 생긴다.

barrier%%t:BARRIER%% 안에 방사성 물질을 붙잡아 두는 것을 돕는 기능을 하는 SSC%%t:SSC%%에는 F-C Target%%t:FC_TARGET%%에 대한 LBE%%t:LBE%% 평가와 RFDC%%t:RFDC%%에서 도출된 규제 설계 요건이 붙는다. 이 기능에는 SSC%%t:SSC%% 자체가 방사성 핵종 이동에 대한 물리적·기능적 barrier%%t:BARRIER%%가 되는 기능과, barrier%%t:BARRIER%%로 분류될 수 있는 다른 SSC%%t:SSC%%를 보호하는 간접 기능이 있다. 원문은 일부 비경수형원전(non-light-water reactor)%%t:NON_LWR%%이 과거에 흔히 쓰던 물리적 barrier%%t:BARRIER%%와 다른 기능적 barrier%%t:BARRIER%%를 쓴다는 점을 짚은 뒤, 이 절차에서 barrier%%t:BARRIER%%를 Layers of Defense%%t:LAYERS_OF_DEFENSE%% 가운데 한 층 안에서 사건 중 방사성 핵종 방출을 막거나 방출량을 줄이는 모든 발전소 특성으로 정의한다. 여기에는 물리적 barrier%%t:BARRIER%%뿐 아니라 방출량을 줄이는 다른 특성, 예컨대 방사성 붕괴를 허용하는 시간 지연도 포함된다.

원문은 개별 물리적 barrier%%t:BARRIER%%가 방사성 핵종을 붙잡아 두는 능력만 보아서는 barrier%%t:BARRIER%% 요건을 완전히 정할 수 없다고 본다. 각 barrier%%t:BARRIER%%와 이를 보호하는 SSC%%t:SSC%%의 역할을 온전히 보려면 PRA에서 도출한 각 LBE%%t:LBE%%에 대한 barrier%%t:BARRIER%% 응답을 고려해야 한다. 한 barrier%%t:BARRIER%%의 역할은 LBE%%t:LBE%%마다 다르며, LBE%%t:LBE%%는 barrier%%t:BARRIER%% 고장 모드, barrier%%t:BARRIER%% 건전성에 대한 부담, 각 barrier%%t:BARRIER%%의 효과에 영향을 주는 SSC%%t:SSC%% 간 상호작용, 층 사이의 독립성 정도를 드러낸다. 부지 밖 선량 결정에 기여하는 Mechanistic Source Term%%t:MST%%의 평가는 barrier%%t:BARRIER%% 효과를 평가하는 또 하나의 성능 지표이다. Layers of Defense%%t:LAYERS_OF_DEFENSE%%를 이루는 SSC%%t:SSC%%들의 상승적 역할을 온전히 파악하려면 SSC%%t:SSC%%가 radionuclide retention이라는 Fundamental Safety Function%%t:FSF%%을 서로 뒷받침하는 방식을 고려해야 한다. barrier%%t:BARRIER%%와 Layers of Defense%%t:LAYERS_OF_DEFENSE%%에 대한 다른 기여 요소가 기능적으로 독립임을 보장하는 것이 중요하다. 체계적인 SSC%%t:SSC%% 설계 요건 개발은 Layers of Defense%%t:LAYERS_OF_DEFENSE%% 안의 barrier%%t:BARRIER%% 부담·상호작용·의존성 전 범위를 고려해야 하고, 이를 빠짐없이 검토하려면 기술적으로 타당한 PRA가 필요하다. 그래서 원문은 barrier%%t:BARRIER%%와 다른 SSC%%t:SSC%%의 요건을 PRA가 뒷받침하는 체계적인 LBE%%t:LBE%% 식별·평가와 연결하는 것이 논리적이라고 결론짓는다.

## 관련 문서
- [[Required_Functional_Design_Criteria]]
- [[Special_Treatment]]
- [[SSC_Reliability_And_Capability]]
- [[SSC_Safety_Classification]]
- [[Licensing_Basis_Event]]
- [[F_C_Target]]
- [[NEI_18-04]]
