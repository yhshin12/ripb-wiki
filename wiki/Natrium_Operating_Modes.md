---
type: natrium
aliases: []
sources:
- PSAR_ch11
status: checked
verified: 2026-09-16
term: null
tags:
- natrium
terms_pending: []
---

# Natrium 운전 모드 (Natrium Operating Modes)

> [!abstract] 요약
> `PSAR` Chapter 11은 원자로 운전 모드를 소듐 온도, control rod drive(`CRD`) 상태, 원자로 냉각 방식의 포괄적 조합으로 정의한다. Mode-1(High Power Operation)과 Mode-2(Low Power Operation)는 둘 이상의 control rod assembly(`CRA`)가 `CRDM` driveline에 결합되고 각각 Nuclear Island Salt System과 Intermediate Air Cooling System으로 냉각되며, Mode-3(Shutdown)과 Mode-4(Refuel)는 결합된 `CRA`가 하나 이하이고 소듐 온도 `400 °F (204°C)`를 기준으로 나뉜다.

## 원문 사실
- "The operating modes for the reactor are defined in Table 11.5-2." [PSAR_ch11 §11.5.2 p.65]
- "Each operating mode is defined in terms of an inclusive combination of sodium temperature, control rod drive (CRD) status, and reactor cooling mechanism." [PSAR_ch11 §11.5.2 p.65]
- "The CRD is described in Section 7.2.5." [PSAR_ch11 §11.5.2 p.65]
- "Reactor heat removal is performed by rejecting heat from the Primary Heat Transport System (PHT) to the Intermediate Heat Transport System (IHT) and then to either the Nuclear Island Salt System (NSS) or Intermediate Air Cooling System (IAC) as described in Sections 7.1.3 and 7.1.4." [PSAR_ch11 §11.5.2 p.65]
- "Each mode is further described in Sections 11.5.2.1 through 11.5.2.4." [PSAR_ch11 §11.5.2 p.65]
- "Mode-1 is entered from Mode-2 during startup when heat removal is transferred from the IAC to the NSS via the Sodium-Salt Heat Exchangers (SHXs)." [PSAR_ch11 §11.5.2.1 p.65]
- "Mode-2 is entered during startup when the reactor scram breakers are closed and more than one control rod assembly (CRA) is coupled to its respective control rod drive mechanism (CRDM) driveline." [PSAR_ch11 §11.5.2.2 p.65]
- "Mode-2 supports control rod withdrawal to a critical state and power ascension within the heat removal capabilities of the IAC." [PSAR_ch11 §11.5.2.2 p.65]
- "Mode-2 can be entered during a shutdown or downpower when reactor power is lowered to within the capability of the IAC and heat removal is transferred from the NSS to the IAC via SHXs." [PSAR_ch11 §11.5.2.2 p.65]
- "Mode-2 is not required to be entered during a shutdown." [PSAR_ch11 §11.5.2.2 p.65]
- "If a reactor scram occurs prior to meeting the conditions for Mode-2, the plant can transition directly from Mode-1 to Mode-3." [PSAR_ch11 §11.5.2.2 p.65]
- "The purpose of Mode-3 is to serve as a transition state for plant startup and entry into Mode-2 or prior to entering Mode-4 during plant shutdown." [PSAR_ch11 §11.5.2.3 p.66]
- "The primary coolant boundary is established during startup in Mode-3." [PSAR_ch11 §11.5.2.3 p.66]
- "Mode-3 supports plant heatup through Primary Sodium Pump (PSP) operation." [PSAR_ch11 §11.5.2.3 p.66]
- "No more than one CRA is coupled to its CRDM driveline while in Mode-3, which ensures a sufficient number of CRAs are inserted to maintain the reactor shutdown." [PSAR_ch11 §11.5.2.3 p.66]
- "One CRA may be coupled to its CRDM driveline and manipulated to support testing." [PSAR_ch11 §11.5.2.3 p.66]
- "The purpose of Mode-4 is to support refueling activities." [PSAR_ch11 §11.5.2.4 p.66]
- "Primary sodium hot pool temperature is lowered to the refueling temperature below 400°F (204°C)." [PSAR_ch11 §11.5.2.4 p.66]
- "No more than one CRA is coupled to its CRDM driveline, which ensures a sufficient number of CRAs are inserted to maintain the reactor shutdown." [PSAR_ch11 §11.5.2.4 p.66]
- "One CRA may be coupled to its CRDM driveline and manipulated to support testing." [PSAR_ch11 §11.5.2.4 p.66]

| Mode | Title | CRD Status | Reactor Cooling Mechanism | Sodium Temperature | 출처 |
|---|---|---|---|---|---|
| 1 | High Power Operation | More than one CRA coupled to CRDM driveline | NSS<sup>(1)</sup> | N/A | [PSAR_ch11 Table 11.5-2 p.74] |
| 2 | Low Power Operation | More than one CRA coupled to CRDM driveline | IAC<sup>(2)</sup> | N/A | [PSAR_ch11 Table 11.5-2 p.74] |
| 3 | Shutdown | No more than one CRA coupled to CRDM driveline | N/A | > 400 °F (204°C) | [PSAR_ch11 Table 11.5-2 p.74] |
| 4 | Refuel | No more than one CRA coupled to CRDM driveline | N/A | ≤ 400 °F (204°C) | [PSAR_ch11 Table 11.5-2 p.74] |

- "The transition from Mode-2 to Mode-1 will be when the transfer of IHT heat removal has been fully transferred from IAC to NSS as denoted by the IAC blower being off and the top and bottom dampers being closed and latched." [PSAR_ch11 Table 11.5-2 p.74]
- "The transition from Mode-1 to Mode-2 will be when the transfer of IHT heat removal has been fully transferred from NSS to IAC as denoted by the NSS isolation valves being closed." [PSAR_ch11 Table 11.5-2 p.74]

## 해설
각 운전 모드는 소듐 온도, control rod drive(`CRD`) 상태, 원자로 냉각 방식의 포괄적 조합으로 정의된다. 원자로 열제거는 Primary Heat Transport System에서 Intermediate Heat Transport System으로, 다시 Nuclear Island Salt System이나 Intermediate Air Cooling System으로 열을 보내 이루어진다.

Mode-2(Low Power Operation)는 기동 중 reactor scram breaker가 닫히고 둘 이상의 control rod assembly(`CRA`)가 각자의 `CRDM` driveline에 결합될 때 들어가며, Intermediate Air Cooling System의 열제거 능력 안에서 control rod를 임계 상태까지 인출하고 출력을 올리는 것을 지원한다. shutdown이나 downpower 중 원자로 출력이 Intermediate Air Cooling System 능력 안으로 낮아지고 열제거가 sodium-salt heat exchanger를 거쳐 Nuclear Island Salt System에서 Intermediate Air Cooling System으로 넘어가면 Mode-2에 들어갈 수 있다. shutdown 중 반드시 Mode-2에 들어갈 필요는 없고, Mode-2 조건을 만족하기 전에 scram이 일어나면 Mode-1에서 곧바로 Mode-3로 전환할 수 있다. Mode-1(High Power Operation)은 기동 중 열제거가 Intermediate Air Cooling System에서 sodium-salt heat exchanger를 거쳐 Nuclear Island Salt System으로 넘어갈 때 Mode-2에서 들어간다. 표 주석은 Mode-2에서 Mode-1로의 전환을 Intermediate Heat Transport System 열제거가 Intermediate Air Cooling System에서 Nuclear Island Salt System으로 완전히 넘어간 때로 정하고, 그 완료를 Intermediate Air Cooling System blower 정지와 상·하부 damper의 `closed and latched` 상태로 나타낸다. Mode-1에서 Mode-2로의 전환은 열제거가 Nuclear Island Salt System에서 Intermediate Air Cooling System으로 완전히 넘어간 때이며, Nuclear Island Salt System 격리 밸브 닫힘으로 나타낸다.

Mode-3(Shutdown)의 목적은 기동 중 Mode-2에 들어가기 전, 또는 shutdown 중 Mode-4에 들어가기 전의 전환 상태 역할을 하는 것이다. 기동 중 Mode-3에서 primary coolant boundary가 확립되고, Primary Sodium Pump 운전으로 발전소 가열을 지원한다. Mode-4(Refuel)의 목적은 refueling 활동 지원이며, primary sodium hot pool 온도를 `400°F (204°C)` 아래의 refueling temperature로 낮춘다. Mode-3와 Mode-4에서는 `CRDM` driveline에 결합된 `CRA`가 하나 이하여서 원자로 정지를 유지할 만큼 충분한 `CRA`가 삽입되며, 시험을 위해 한 `CRA`를 결합해 조작할 수 있다. 표에서 Mode-3의 소듐 온도는 `> 400 °F (204°C)`, Mode-4는 `≤ 400 °F (204°C)`이다.

## 관련 문서
- [[Natrium_Technical_Specifications_Scope]]
- [[Natrium_NRC_Review_Reactivity_Control]]
- [[Natrium_Reactor_Heat_Transport_Systems]]
- [[Natrium_PRA_Scope]]
- [[PSAR_ch11]]
