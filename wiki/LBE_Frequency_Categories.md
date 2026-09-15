---
type: concept
aliases: []
sources: [NEI_18-04]
status: disputed
verified:
term:
tags: []
terms_pending: []
---
# LBE 범주와 빈도 구간 (LBE Categories and Frequency Bands)

> [!abstract] 요약
> Anticipated Operational Occurrence%%t:AOO%%, Design Basis Event%%t:DBE%%, Beyond Design Basis Event%%t:BDBE%%는 평균 빈도 구간으로 구분된다. Design Basis Accident%%t:DBA%%는 빈도로 정의되지 않고 DBE%%t:DBE%%에서 유도되며, Safety-Related Structures, Systems, and Components%%t:SSC%%만 동원된다고 가정한 Event Sequence%%t:ES%%이다.

## 원문 사실
- "Anticipated event sequences expected to occur one or more times during the life of a nuclear power plant, which may include one or more reactor modules. Event sequences with mean frequencies of 1E-02/plant-year and greater are classified as AOOs." [NEI_18-04 Table 3-1 p.14]
- "Infrequent event sequences that are not expected to occur in the life of a nuclear power plant, which may include one or more reactor modules, but are less likely than AOOs. Event sequences with mean frequencies of 1E-04/plant-year to 1E-02/plant-year are classified as DBEs." [NEI_18-04 Table 3-1 p.14]
- "Rare event sequences that are not expected to occur in the life of a nuclear power plant, which may include one or more reactor modules, but are less likely than a DBE. Event sequences with mean frequencies of 5E-07/plant-year to 1E-04/plant-year are classified as BDBEs." [NEI_18-04 Table 3-1 p.14]
- "Postulated event sequences that are used to set design criteria and performance objectives for the design of Safety Related SSCs. DBAs are derived from DBEs based on the capabilities and reliabilities of Safety-Related SSCs needed to mitigate and prevent event sequences, respectively." [NEI_18-04 Table 3-1 p.14]
- "DBAs are derived from the DBEs by prescriptively assuming that only Safety Related SSCs are available to mitigate postulated event sequence consequences to within the 10 CFR 50.34 dose limits." [NEI_18-04 Table 3-1 p.14]
- "AOOs take into account the expected response of all SSCs within the plant, regardless of safety classification." [NEI_18-04 Table 3-1 p.14]
- "DBEs take into account the expected response of all SSCs within the plant regardless of safety classification." [NEI_18-04 Table 3-1 p.14]
- "BDBEs take into account the expected response of all SSCs within the plant regardless of safety classification." [NEI_18-04 Table 3-1 p.14]
- "LBE categories are based on mean event sequence frequency of occurrence per plant-year." [NEI_18-04 §3.2.1 p.16]
- "However, when the uncertainty bands ... defined by the 5th percentile and 95th percentile of the frequency estimates straddles a frequency boundary, the LBE is evaluated in both LBE categories." [NEI_18-04 §3.2.2 Task 7a p.22]
- "An event sequence family with a mean frequency less than 5E-07/plant year but with a 95%tile frequency estimate above 5E-07/plant-year is evaluated as a BDBE." [NEI_18-04 §3.2.2 Task 7a p.22]
- "BDBEs are rare events with frequencies less than 1E-04/plant-year but with upper bound frequencies greater than 5E-07/plant-year." [NEI_18-04 §3.2.1 p.16]
- "Each of these families is assigned to an LBE category based on mean event sequence frequency of occurrence per plant-year summed over all the event sequences in the LBE family." [NEI_18-04 §3.2.2 Task 4 p.20]
- "BDBEs are rare events with frequencies less than 1E-04/plant-year but with upper bound frequencies greater than 5E-07/plant-year." [NEI_18-04 §3.2.2 Task 4 p.21]
- "Event sequences with upper 95th percentile frequencies less than 5E-07/plant-year are retained in the PRA results and used to confirm that there are no cliff-edge effects." [NEI_18-04 §3.2.2 Task 4 p.21]
- "Event sequences with mean frequencies of 1E-02/plant-year and greater are classified as AOOs. AOOs take into account the expected response of all SSCs within the plant, regardless of safety classification." [NEI_18-04 §6 p.90]
- "DBEs take into account the expected response of all SSCs within the plant regardless of safety classification." [NEI_18-04 §6 p.90]
- "The objective and scope of DBEs form the safety design basis of the plant." [NEI_18-04 §6 p.90]
- "Event sequences with frequencies of 5E-07/plant-year to 1E-04/plant -year are classified as BDBEs." [NEI_18-04 §6 p.90]
- "BDBEs take into account the expected response of all SSCs within the plant regardless of safety classification." [NEI_18-04 §6 p.90]
- "Postulated accidents that are used to set design criteria and performance objectives for the design of Safety-Related SSCs." [NEI_18-04 §6 p.90]
- "DBAs are derived from DBEs based on the capabilities and reliabilities of Safety-Related SSCs needed to mitigate and prevent accidents, respectively." [NEI_18-04 §6 p.90]

| 항목 | 값 | 출처 |
|---|---|---|
| AOO | 1E-02/plant-year and greater | [NEI_18-04 Table 3-1 p.14] |
| DBE | 1E-04/plant-year to 1E-02/plant-year | [NEI_18-04 Table 3-1 p.14] |
| BDBE | 5E-07/plant-year to 1E-04/plant-year | [NEI_18-04 Table 3-1 p.14] |
| DBA | derived from DBEs based on the capabilities and reliabilities of Safety-Related SSCs | [NEI_18-04 Table 3-1 p.14] |

## 해설
표 3-1에서 세 범주는 평균 빈도로 갈린다. AOO%%t:AOO%%는 1E-02/plant-year 이상, DBE%%t:DBE%%는 1E-04/plant-year에서 1E-02/plant-year 사이, BDBE%%t:BDBE%%는 5E-07/plant-year에서 1E-04/plant-year 사이이다. Task 7a는 5th percentile과 95th percentile로 정한 불확실도 구간이 범주 경계에 걸치면 그 Licensing Basis Event%%t:LBE%%를 두 범주에서 모두 평가하고, 평균이 5E-07/plant-year보다 낮아도 95th percentile이 그 위이면 BDBE%%t:BDBE%%로 평가한다고 적는다. 경계 규칙 전체는 [[LBE_Risk_Significance]]에 있다.

범주를 가르는 빈도는 안전 등급과 무관하게 발전소 안의 모든 SSC%%t:SSC%%의 예상 응답을 반영한 값이다. 표 3-1과 용어집은 모두 AOO%%t:AOO%%, DBE%%t:DBE%%, BDBE%%t:BDBE%% 정의에 이 문장을 둔다. 따라서 빈도는 안전 등급이 있는 설비만으로 계산한 값이 아니다.

DBA%%t:DBA%%는 성격이 다르다. 빈도 구간으로 정의되지 않고 DBE%%t:DBE%%에서 유도되며, 완화에 동원되는 설비를 Safety-Related SSC%%t:SSC%%로 한정한다고 가정한다. 즉 같은 ES%%t:ES%%를 보수적으로 다시 평가한 것이 DBA%%t:DBA%%이고, 그 목적은 설계 기준과 성능 목표를 정하는 데 있다.

§6 용어집의 정의는 표 3-1과 대체로 같지만 세 곳에서 표현이 다르다. DBE%%t:DBE%% 정의에는 DBE%%t:DBE%%의 목적과 범위가 발전소의 안전 설계기준을 이룬다는 문장이 더 있다. BDBE%%t:BDBE%% 정의는 구간을 5E-07/plant-year에서 1E-04/plant-year로 같게 적되, 표 3-1의 mean이라는 한정어 없이 frequencies로만 적는다. DBA%%t:DBA%% 정의는 표 3-1의 event sequences 대신 accidents라는 말을 쓴다. 구간 수치는 두 곳이 같다.

BDBE%%t:BDBE%% 빈도 하한의 기준은 원문 안에서 어긋난다. 표 3-1은 평균 빈도 5E-07/plant-year 이상을 BDBE%%t:BDBE%%로 정의하고, §3.2.1과 §3.2.2의 LBE%%t:LBE%% 범주 지정 과업도 범주가 평균 빈도에 기반한다고 적는다. 그러나 같은 두 곳은 BDBE%%t:BDBE%%를 빈도가 1E-04/plant-year보다 낮지만 상한 빈도가 5E-07/plant-year보다 높은 사건으로 적는다. §3.2.2의 그 과업은 이어서 95th percentile 상한 빈도가 5E-07/plant-year보다 낮은 ES%%t:ES%%를 PRA 결과에 남겨 cliff edge effects%%t:CLIFF_EDGE_EFFECT%%가 없음을 확인하는 데 쓴다고 적는다. 하한을 평균값으로 보는지 상한값으로 보는지가 다르므로 이 노트는 disputed로 둔다.

## 관련 문서
- [[Licensing_Basis_Event]]
- [[F_C_Target]]
- [[LBE_Risk_Significance]]
- [[LBE_Selection_Process]]
- [[NEI_18-04]]
