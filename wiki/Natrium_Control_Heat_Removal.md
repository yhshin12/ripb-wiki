---
type: natrium
aliases: []
sources:
- PSAR_ch01
status: checked
verified: 2026-09-16
term: null
tags:
- natrium
terms_pending: []
---

# Natrium의 controlling heat removal (Natrium Controlling Heat Removal)

> [!abstract] 요약
> Fundamental Safety Function%%t:FSF%%인 controlling heat removal은 Defense Line%%t:DL%%에 걸쳐 능동, 피동, 고유 수단을 가지며, 서로 다른 두 잔열 제거 계통인 Intermediate Air Cooling System과 Reactor Air Cooling System이 수행한다. 앞의 계통은 blower를 쓰는 능동 수단과 자연 통풍을 쓰는 피동 수단을, 뒤의 계통은 guard vessel 바깥 공기의 자연 순환을 쓰는 고유 수단을 제공한다.

## 원문 사실
- "The FSF of controlling heat removal has active, passive, and inherent means of being achieved across the DLs." [PSAR_ch01 §1.3.2.3 p.63]
- "Two diverse residual heat removal systems, the Intermediate Air Cooling System (IAC) and Reactor Air Cooling (RAC), perform functions that satisfy the FSF of controlling heat removal." [PSAR_ch01 §1.3.2.3 p.63]
- "The IAC provides an active and passive means of performing the FSF of controlling heat removal." [PSAR_ch01 §1.3.2.3 p.63]
- "The RAC provides an inherent means of performing the FSF of controlling heat removal." [PSAR_ch01 §1.3.2.3 p.63]
- "This includes mechanisms for the natural circulation of sodium under certain off-normal conditions." [PSAR_ch01 §1.3.2.3 p.63]
- "The IAC has two active modes of operation that perform the FSF of controlling heat removal by using the IAC blower to transfer heat from the IHT via the Intermediate Heat Exchanger." [PSAR_ch01 §1.3.2.3 p.63]
- "The IAC also provides a passive means of performing the FSF of controlling heat removal using natural draft airflow instead of the IAC blower." [PSAR_ch01 §1.3.2.3 p.63]
- "The IAC is the primary means of heat removal during plant start-up, shutdown, and off-normal conditions." [PSAR_ch01 §1.3.2.3 p.63]
- "The RAC provides an inherent means of performing the FSF of controlling heat removal using natural circulation of air around the exterior of the guard vessel." [PSAR_ch01 §1.3.2.3 p.64]
- "The RAC operates continuously, with no operator actions or moving parts required to perform its function, and removes decay heat during normal operation, anticipated operational occurrences, design basis events, and design basis accidents." [PSAR_ch01 §1.3.2.3 p.64]
- "Since RAC is an open system, the surrounding environment is both the ultimate coolant source and heat sink for the RAC." [PSAR_ch01 §1.3.2.3 p.64]
- "Meteorological data for evaluating the ultimate heat sink is provided in Section 2.4.1.4." [PSAR_ch01 §1.3.2.3 p.64]
- "The RAC primary objective is to provide passive decay heat removal to the environment through natural convection of air." [PSAR_ch01 §1.1.4.1.3 p.22]
- "The RAC is inherently reliable since it is not subject to the types of failure modes normally associated with active cooling systems (such as via pumped flow through heat exchangers)." [PSAR_ch01 §1.1.4.1.3 p.22]
- "It is continually in service with no operator actions nor SSC state change to initiate cooling operation." [PSAR_ch01 §1.1.4.1.3 p.22]
- "RAC heat removal performance is monitored during system operation including post-accident conditions." [PSAR_ch01 §1.1.4.1.3 p.22]
- "The RV is designed to thermally radiate heat across the argon gas space to the GV." [PSAR_ch01 §1.1.4.1.3 p.22]
- "This increases the capacity of RAC heat removal without increasing the surface area of the GV." [PSAR_ch01 §1.1.4.1.3 p.22]
- "The IHT transfers heat to the IAC through the Sodium-Air Heat Exchanger (AHX) for decay heat removal and for reactor startup and shutdown operations." [PSAR_ch01 §1.1.4.1.5 p.23]
- "In this role, the IHT provides part of the normal, preferred pathway for rejection of decay heat." [PSAR_ch01 §1.1.4.1.5 p.23]
- "The IAC is the preferred heat removal system for the reactor during upset events." [PSAR_ch01 §1.1.4.1.6 p.23]
- "The IAC transfers heat to the atmosphere in three system modes of operation." [PSAR_ch01 §1.1.4.1.6 p.23]
- "In active mode, there is forced circulation of the sodium in the intermediate loop provided by the ISP and forced air flow across the AHX provided by the IAC air blower." [PSAR_ch01 §1.1.4.1.6 p.23]
- "In blower mode, there is natural circulation of the sodium in the intermediate loop and forced air flow across the AHX provided by the IAC air blower." [PSAR_ch01 §1.1.4.1.6 p.23]
- "In passive mode, there is natural circulation of the sodium in the intermediate loop and natural convection flow of the air across the AHX." [PSAR_ch01 §1.1.4.1.6 p.23]

## 해설
controlling heat removal은 서로 다른 두 잔열 제거 계통인 Intermediate Air Cooling System과 Reactor Air Cooling System이 수행한다. Intermediate Air Cooling System에는 blower로 Intermediate Heat Transport System의 열을 옮기는 두 능동 운전 모드와, blower 대신 자연 통풍을 쓰는 피동 수단이 있다. 계통 설명 절은 대기로 열을 옮기는 세 운전 모드를 구분한다. active mode에서는 중간 루프 소듐이 강제 순환하고 blower가 sodium-air heat exchanger를 지나는 공기를 강제로 흘리며, blower mode에서는 소듐이 자연 순환하고 공기는 blower로 강제로 흐르고, passive mode에서는 소듐과 공기가 모두 자연 순환한다.

두 서술은 열전달 기기의 이름이 다르다. 안전 개요 절은 blower가 Intermediate Heat Exchanger를 거쳐 Intermediate Heat Transport System의 열을 옮긴다고 적고, 계통 설명 절은 Intermediate Heat Transport System이 Sodium-Air Heat Exchanger를 거쳐 Intermediate Air Cooling System으로 열을 전달한다고 적는다. 두 이름이 같은 경로의 다른 기기를 가리키는지는 vault에 없다. 역할 표현도 다르다. 안전 개요 절은 이 계통을 발전소 기동, 정지, off-normal 조건에서의 주 열제거 수단으로 적고, 계통 설명 절은 upset events 동안 원자로의 preferred heat removal system으로 적는다. 계통 설명 절은 또 Intermediate Heat Transport System이 붕괴열 제거와 원자로 기동·정지 운전을 위해 이 계통으로 열을 전달하며, 붕괴열 방출의 정상적이고 선호되는 경로의 일부라고 적는다.

Reactor Air Cooling System은 guard vessel 외부를 도는 공기의 자연 순환으로 controlling heat removal의 고유 수단을 제공하며, 이 수단에는 특정 off-normal 조건에서 소듐이 자연 순환하는 메커니즘이 포함된다. 계통은 운전원 조치나 움직이는 부품 없이 연속 운전하며, 정상 운전, Anticipated Operational Occurrence%%t:AOO%%, Design Basis Event%%t:DBE%%, Design Basis Accident%%t:DBA%% 동안 붕괴열을 제거한다. 개방 계통이므로 주변 환경이 최종 냉각재 원천이자 열침원이다. 계통 설명 절에 따르면 주목적은 공기 자연 대류로 환경에 피동 붕괴열 제거를 제공하는 것이고, 펌프 유동 열교환기 같은 능동 냉각 계통의 일반적 고장 모드를 겪지 않아 본질적으로 신뢰성이 높다. 냉각을 시작하는 데 운전원 조치나 Structures, Systems, and Components%%t:SSC%% 상태 변화가 필요 없고, 사고 후를 포함한 운전 중 열제거 성능을 감시한다. 원자로 용기는 argon 기체 공간을 가로질러 guard vessel로 열을 복사하도록 설계되어, guard vessel 표면적을 늘리지 않고 열제거 용량을 키운다.

## 관련 문서
- [[Natrium_Fundamental_Safety_Functions]]
- [[Natrium_Control_Heat_Generation]]
- [[Natrium_Functional_Containment]]
- [[SFR_DC_Residual_Heat_Removal_And_ECC]]
- [[PSAR_ch01]]
