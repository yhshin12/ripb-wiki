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
- "BDBEs are rare events with frequencies less than 1E-04/plant-year but with upper bound frequencies greater than 5E-07/plant-year." [NEI_18-04 §3.2.1 p.16]

| 항목 | 값 | 출처 |
|---|---|---|
| AOO | 1E-02/plant-year and greater | [NEI_18-04 Table 3-1 p.14] |
| DBE | 1E-04/plant-year to 1E-02/plant-year | [NEI_18-04 Table 3-1 p.14] |
| BDBE | 5E-07/plant-year to 1E-04/plant-year | [NEI_18-04 Table 3-1 p.14] |
| DBA | derived from DBEs based on the capabilities and reliabilities of Safety-Related SSCs | [NEI_18-04 Table 3-1 p.14] |

## 해설
세 범주는 평균 빈도 하나로 갈린다. AOO%%t:AOO%%는 1E-02/plant-year 이상, DBE%%t:DBE%%는 1E-04/plant-year에서 1E-02/plant-year 사이, BDBE%%t:BDBE%%는 5E-07/plant-year에서 1E-04/plant-year 사이이다. 구간이 맞닿아 있으므로 빈도 추정값이 경계 근처면 범주가 바뀔 수 있다.

범주를 가르는 빈도는 안전 등급과 무관하게 계통 전체의 예상 거동을 반영한 값이다. 원문은 AOO%%t:AOO%%에 대해 이 점을 명시하며, DBE%%t:DBE%%와 BDBE%%t:BDBE%% 정의에도 같은 문장이 붙어 있다. 따라서 빈도는 안전 등급이 있는 설비만으로 계산한 값이 아니다.

DBA%%t:DBA%%는 성격이 다르다. 빈도 구간으로 정의되지 않고 DBE%%t:DBE%%에서 유도되며, 완화에 동원되는 설비를 Safety-Related SSC%%t:SSC%%로 한정한다고 가정한다. 즉 같은 ES%%t:ES%%를 보수적으로 다시 평가한 것이 DBA%%t:DBA%%이고, 그 목적은 설계 기준과 성능 목표를 정하는 데 있다.

## 관련 문서
- [[Licensing_Basis_Event]]
- [[F_C_Target]]
- [[NEI_18-04]]
