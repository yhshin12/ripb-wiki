---
type: natrium
aliases: []
sources: [PSAR_ch03]
status: checked
verified: 2026-09-16
term:
tags: [natrium, lbe]
terms_pending: []
---
# Natrium Mechanistic Source Term 방법론 (Natrium Mechanistic Source Term Methodology)

> [!abstract] 요약
> 이 보고서는 Mechanistic Source Term%%t:MST%%을 특정 위치에서의 방사성 핵종 방출 특성으로 정의하고, 방출을 release categories로 묶어 시점, 위치, 방출량, 이동 barrier%%t:BARRIER%%와 메커니즘을 고려해 평가한다. 방법론 보고서의 1–8절이 참조 포함되며, 요약표들이 사건별 MST%%t:MST%%의 주요 동위원소와 누적 방출량을 적는다.

## 원문 사실
- "The mechanistic source term (MST) is defined as the characteristics of a radionuclide release at a particular location, including the physical and chemical properties of released material, release magnitude, heat content (or energy) of the carrier fluid, and location relative to local obstacles that would affect transport away from the release point and the temporal variations in these parameters (e.g., time of release duration) ... that are calculated using models and supporting scientific data that simulate the physical and chemical processes that describe the radionuclide inventories and the time-dependent radionuclide transport mechanisms that are necessary and sufficient to predict the source term." [PSAR_ch03 §3.2 p.23]
- "Radionuclide releases are grouped into smaller subsets of representative source terms or release categories." [PSAR_ch03 §3.2 p.23]
- "Radionuclide releases are assessed for each release category, including consideration of timing, location, amount released, and the radionuclide transport barriers and transport mechanisms." [PSAR_ch03 §3.2 p.23]
- "Radiological source terms are calculated using appropriate methods or codes." [PSAR_ch03 §3.2 p.23]
- "Uncertainties in the MSTs and associated transport phenomena are identified, characterized, and quantified to the extent practical." [PSAR_ch03 §3.2 p.23]
- "Documentation of the MST analysis shall provide traceability of the work." [PSAR_ch03 §3.2 p.23]
- "is documented in NAT-9392-A, “Radiological Source Term Methodology Report,” Revision 0 (Reference 3.2-1). Sections 1 through 8 of NAT-9392-A are incorporated by reference." [PSAR_ch03 §3.2 p.23]
- "Significant reduction in flow through the reactor core" [PSAR_ch03 §3.2 p.23]
- "Localized high power-to-flow conditions within core assemblies" [PSAR_ch03 §3.2 p.23]
- "Physical damage to the fuel (e.g., physical damage due to stochastic cladding failures during normal operation and potential impact damage due to scenarios like drop events)" [PSAR_ch03 §3.2 p.23]
- "Reactivity insertion such as uncontrolled control rod withdrawal" [PSAR_ch03 §3.2 p.23]
- "Assessments to evaluate model fidelity and accuracy, scalability of the models, and acceptance of the models are in process, and are captured in Section 5 of NAT-9392-A." [PSAR_ch03 §3.2 p.24]
- "These and other items identified for development in Sections 3.2, 3.3, and 5 of NAT-9392-A will be available by the operating license stage." [PSAR_ch03 §3.2 p.24]
- "These tables include a list of the isotopes which contribute to at least 95 percent of the total dose, and the cumulative activity release of each isotope in curies." [PSAR_ch03 §3.2.1 p.24]

| 표 | 제목 | 출처 |
|---|---|---|
| Table 3.2-1 | Protected Loss of Flow or Loss of Offsite Power | [PSAR_ch03 Table 3.2-1 p.25] |
| Table 3.2-2 | Local Fault Event | [PSAR_ch03 Table 3.2-2 p.26] |
| Table 3.2-3 | In-vessel Fuel Drop | [PSAR_ch03 Table 3.2-3 p.27] |
| Table 3.2-4 | Local Fault Event DBA | [PSAR_ch03 Table 3.2-4 p.28-29] |
| Table 3.2-5 | In-vessel Fuel Drop DBA, 1 Assembly | [PSAR_ch03 Table 3.2-5 p.30] |
| Table 3.2-6 | In-vessel Fuel Drop DBA, 2 Assemblies | [PSAR_ch03 Table 3.2-6 p.31] |
| Table 3.2-7 | Spent Fuel Release inside EVHM | [PSAR_ch03 Table 3.2-7 p.32] |
| Table 3.2-8 | Low Decay (LTA/LDA) Fuel Release inside EVHM | [PSAR_ch03 Table 3.2-8 p.33] |
| Table 3.2-9 | Spent Fuel Drop in Spent Fuel Pool, 1 Assembly | [PSAR_ch03 Table 3.2-9 p.34] |
| Table 3.2-10 | Primary Sodium Processing Leak | [PSAR_ch03 Table 3.2-10 p.35] |
| Table 3.2-11 | Primary Sodium Processing Leak DBA | [PSAR_ch03 Table 3.2-11 p.36] |
| Table 3.2-12 | Cover Gas Release, Confinement Success | [PSAR_ch03 Table 3.2-12 p.37] |
| Table 3.2-13 | Cover Gas Release, Confinement Bypass | [PSAR_ch03 Table 3.2-13 p.38] |
| Table 3.2-14 | Cover Gas Release DBA | [PSAR_ch03 Table 3.2-14 p.39] |
| Table 3.2-15 | Release from RWG Holdup Tank, Release via FHB exhaust | [PSAR_ch03 Table 3.2-15 p.40] |
| Table 3.2-16 | Release from RWG Holdup Tank, Release via RWG | [PSAR_ch03 Table 3.2-16 p.41] |
| Table 3.2-17 | Release from RWG Holdup Tank, Release via RWG DBA | [PSAR_ch03 Table 3.2-17 p.42] |
| Table 3.2-18 | Release of Tritium from SPS-I Cold Trap | [PSAR_ch03 Table 3.2-18 p.43] |

| LBE ID | MST 표 | 출처 |
|---|---|---|
| RFH-OERC-BL | Table 3.2-8 | [PSAR_ch03 §3.6.4.1.2 p.65] |
| RRS-CGR-BL | Table 3.2-12 | [PSAR_ch03 §3.7.3.1.2 p.72] |
| RRS-CGR-1 | Table 3.2-12 | [PSAR_ch03 §3.7.3.2.2 p.72] |
| RRS-ISPL-BL | Table 3.2-18 | [PSAR_ch03 §3.7.3.3.2 p.73] |
| RRS-SPLX-BL | Table 3.2-10 | [PSAR_ch03 §3.7.3.4.2 p.74] |
| RRS-SPLA-BL | Table 3.2-10 | [PSAR_ch03 §3.7.3.5.2 p.74] |
| RRS-RWG-1 | Table 3.2-15 | [PSAR_ch03 §3.7.3.6.2 p.75] |
| RRS-RWG-2 | Table 3.2-16 | [PSAR_ch03 §3.7.3.7.2 p.76] |
| RFH-FDIV-1 | Table 3.2-5 | [PSAR_ch03 §3.7.4.2.2 p.77] |
| RFH-FDIV-3 | Table 3.2-6 | [PSAR_ch03 §3.7.4.3.2 p.78] |
| RFH-FDSP-1 | Table 3.2-9 | [PSAR_ch03 §3.7.4.4.2 p.79] |
| RFH-ESWR-1 | Table 3.2-9 | [PSAR_ch03 §3.7.4.6.2 p.80] |
| LFF-SAO-BL | Table 3.2-2 | [PSAR_ch03 §3.7.5.1.2 p.82] |
| DHP-LOOP-3 | Table 3.2-1 | [PSAR_ch03 §3.8.1.6.2 p.85] |
| DHP-LOOP-4 | Table 3.2-1 | [PSAR_ch03 §3.8.1.7.2 p.86] |
| SUD-CGR-1 | Table 3.2-13 | [PSAR_ch03 §3.8.4.1.2 p.93] |
| SUD-CGR-2 | Table 3.2-13 | [PSAR_ch03 §3.8.4.2.2 p.93] |
| RFH-FDIV-2 | Table 3.2-3 | [PSAR_ch03 §3.8.5.1.2 p.94] |
| RFH-FDIV-4 | Table 3.2-3 | [PSAR_ch03 §3.8.5.2.2 p.95] |
| RFH-FDSP-2 | Table 3.2-9 | [PSAR_ch03 §3.8.5.3.2 p.96] |
| RFH-ESWR-2 | Table 3.2-9 | [PSAR_ch03 §3.8.5.4.2 p.96] |
| RFH-ESWR-3 | Table 3.2-7 | [PSAR_ch03 §3.8.5.5.2 p.97] |
| RFH-LMCA-1 | Table 3.2-8 | [PSAR_ch03 §3.8.5.6.2 p.98] |
| RFH-LMCA-2 | Table 3.2-8 | [PSAR_ch03 §3.8.5.7.2 p.98] |
| RFH-FDBL-1 | Table 3.2-7 | [PSAR_ch03 §3.8.5.8.2 p.99] |
| RFH-FDBL-2 | Table 3.2-7 | [PSAR_ch03 §3.8.5.9.2 p.100] |
| RFH-FDEM-1 | Table 3.2-8 | [PSAR_ch03 §3.8.5.10.2 p.101] |
| RFH-FDEM-2 | Table 3.2-8 | [PSAR_ch03 §3.8.5.11.2 p.101] |
| RFH-FDET-1 | Table 3.2-7 | [PSAR_ch03 §3.8.5.13.2 p.102] |
| RFH-FDPI-BL | Table 3.2-7 | [PSAR_ch03 §3.8.5.14.2 p.103] |
| RFH-FDPI-1 | Table 3.2-7 | [PSAR_ch03 §3.8.5.15.2 p.104] |
| RFH-FDRC-1 | Table 3.2-8 | [PSAR_ch03 §3.8.5.16.2 p.104] |
| LFF-SAO-1 | Table 3.2-4 | [PSAR_ch03 §3.8.6.1.2 p.105] |
| LFF-SAO-2 | Table 3.2-4 | [PSAR_ch03 §3.8.6.2.2 p.106] |
| RRS-CGR-CN | Table 3.2-14 | [PSAR_ch03 §3.9.4.1.2 p.111] |
| RRS-ISPL-CN | Table 3.2-18 | [PSAR_ch03 §3.9.4.2.2 p.112] |
| RRS-SPLX-CN | Table 3.2-11 | [PSAR_ch03 §3.9.4.3.2 p.113] |
| RRS-SPLA-CN | Table 3.2-11 | [PSAR_ch03 §3.9.4.4.2 p.113] |
| RRS-RWG-CN | Table 3.2-17 | [PSAR_ch03 §3.9.4.5.2 p.114] |
| RFH-FDIV-CN | Table 3.2-6 | [PSAR_ch03 §3.9.5.1.2 p.114] |
| RFH-FDSP-CN | Table 3.2-9 | [PSAR_ch03 §3.9.5.2.2 p.115] |
| RFH-ESWR-CN | Table 3.2-7 | [PSAR_ch03 §3.9.5.3.2 p.116] |
| LFF-SAO-CN | Table 3.2-4 | [PSAR_ch03 §3.9.6.1.1 p.117] |

## 해설
MST%%t:MST%% 정의는 방출 물질의 물리·화학적 성질, 방출 크기, 운반 유체의 열 함량, 방출점 주변 장애물에 대한 위치, 그리고 이 변수들의 시간 변화를 포함하는 방출 특성이며, 방사성 핵종 재고와 시간 의존 이동 메커니즘을 모사하는 모델과 과학 자료로 계산한다. 방출은 대표 선원항(source term)%%t:SOURCE_TERM%%이나 release categories로 묶고, 적절한 방법이나 코드로 계산하며, MST%%t:MST%%와 이동 현상의 불확실도를 실용적인 범위에서 식별·특성화·정량화하고, 추적 가능하게 문서화한다. 방법론은 `NAT-9392-A` Revision 0에 있고 그 `Sections 1 through 8`이 참조 포함된다. 절은 노심 유량의 큰 감소, 집합체 안의 국부 고출력 대 유량 조건, 정상 운전 중 확률적 피복 파손이나 낙하 같은 핵연료의 물리적 손상, 제어봉 인출 같은 반응도 삽입을 열거한다.

모델 충실도, 정확도, 확장성, 수용성 평가는 진행 중이며, 이와 함께 개발 대상으로 식별된 항목은 operating license%%t:OL%% 단계까지 제공된다. 요약표는 총선량의 적어도 95 percent를 차지하는 동위원소와 각 동위원소의 누적 방출량을 curie로 적는다. 사건별 대응을 보면 여러 Licensing Basis Event%%t:LBE%%가 같은 요약표를 쓴다. 예를 들어 `LTA` 또는 `LDA` 저붕괴 핵연료의 Ex-Vessel Handling Machine 내부 방출 표는 Anticipated Operational Occurrence%%t:AOO%% 하나와 여러 Beyond Design Basis Event%%t:BDBE%%에 쓰이고, 커버가스(cover gas)%%t:COVER_GAS%% 방출 표는 confinement 성공, confinement bypass, Design Basis Accident%%t:DBA%%용으로 나뉜다.

## 관련 문서
- [[Mechanistic_Source_Term_Conditions]]
- [[Event_Sequence_Family]]
- [[Natrium_PRA_Scope]]
- [[Natrium_LBE_Evaluation_Methods]]
- [[PSAR_ch03]]
