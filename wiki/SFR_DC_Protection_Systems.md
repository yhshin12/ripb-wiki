---
type: regulation
aliases: []
sources:
- RG_1.232
status: checked
verified: 2026-09-16
term: null
tags:
- sfr-dc
terms_pending: []
---

# SFR-DC 보호 계통 (SFR-DC Protection Systems, Criteria 20–25)

> [!abstract] 요약
> 기준 20–25는 보호 계통의 기능, 신뢰도와 시험 가능성, 독립성, 고장 모드, 제어 계통과의 분리, 반응도 제어 오작동에 대한 요건을 다룬다. 기준 20, 21, 22, 24는 general design criteria%%t:GDC%%와 같고 기준 25는 advanced reactor design criteria와 같으며, 기준 23은 가정한 불리한 환경의 예에 소듐과 소듐 반응 생성물을 더해 수정되었다.

## 원문 사실
- "The protection system shall be designed (1) to initiate automatically the operation of appropriate systems including the reactivity control systems, to assure that specified acceptable fuel design limits are not exceeded as a result of anticipated operational occurrences and (2) to sense accident conditions and to initiate the operation of systems and components important to safety." [RG_1.232 SFR-DC 20 p.72]
- "The protection system shall be designed for high functional reliability and inservice testability commensurate with the safety functions to be performed. Redundancy and independence designed into the protection system shall be sufficient to assure that (1) no single failure results in loss of the protection function and (2) removal from service of any component or channel does not result in loss of the required minimum redundancy unless the acceptable reliability of operation of the protection system can be otherwise demonstrated. The protection system shall be designed to permit periodic testing of its functioning when the reactor is in operation, including a capability to test channels independently to determine failures and losses of redundancy that may have occurred." [RG_1.232 SFR-DC 21 p.72]
- "The protection system shall be designed to assure that the effects of natural phenomena, and of normal operating, maintenance, testing, and postulated accident conditions on redundant channels do not result in loss of the protection function, or shall be demonstrated to be acceptable on some other defined basis. Design techniques, such as functional diversity or diversity in component design and principles of operation, shall be used to the extent practical to prevent loss of the protection function." [RG_1.232 SFR-DC 22 p.73]
- "The protection system shall be designed to fail into a safe state or into a state demonstrated to be acceptable on some other defined basis, if conditions such as disconnection of the system, loss of energy (e.g., electric power, instrument air), or postulated adverse environments (e.g., extreme heat or cold, fire, sodium and sodium reaction products, pressure, steam, water, and radiation) are experienced." [RG_1.232 SFR-DC 23 p.73]
- "In NUREG-1368, Table 3.3 (page 3-21) (Ref. 4), the NRC staff recommended adding the phrase “sodium and sodium reaction products” to the list of postulated adverse environments in the GDC. Therefore, “sodium and sodium reaction products” are added to the second list of examples in parentheses in SFR-DC 23." [RG_1.232 SFR-DC 23 p.73]
- "The protection system shall be designed to fail into a safe state or into a state demonstrated to be acceptable on some other defined basis if conditions such as disconnection of the system, loss of energy (e.g., electric power, instrument air), or postulated adverse environments (e.g., extreme heat or cold, fire, pressure, steam, water, and radiation) are experienced." [RG_1.232 ARDC 23 p.38]
- "The protection system shall be separated from control systems to the extent that failure of any single control system component or channel, or failure or removal from service of any single protection system component or channel which is common to the control and protection systems leaves intact a system satisfying all reliability, redundancy, and independence requirements of the protection system. Interconnection of the protection and control systems shall be limited so as to assure that safety is not significantly impaired." [RG_1.232 SFR-DC 24 p.73]
- "The protection system shall be designed to ensure that specified acceptable fuel design limits are not exceeded during any anticipated operational occurrence accounting for a single malfunction of the reactivity control systems." [RG_1.232 SFR-DC 25 p.74]
- "Text has been added to clarify that the protection system is designed to protect the specified acceptable fuel design limits for AOOs in combination with a single failure; the protection system does not have to protect the specified acceptable fuel design limits during a postulated accident in combination with a single failure. The example was deleted to make the ARDC technology inclusive." [RG_1.232 SFR-DC 25 p.74]

| Criterion | GDC title | SFR-DC title | SFR-DC status | 출처 |
|---|---|---|---|---|
| 20 | Protection system functions. |  | Same as GDC | [RG_1.232 Table 1 p.13-20] |
| 21 | Protection system reliability and testability. |  | Same as GDC | [RG_1.232 Table 1 p.13-20] |
| 22 | Protection system independence. |  | Same as GDC | [RG_1.232 Table 1 p.13-20] |
| 23 | Protection system failure modes. | Protection system failure modes. | Modified for SFR-DC | [RG_1.232 Table 1 p.13-20] |
| 24 | Separation of protection and control systems. |  | Same as GDC | [RG_1.232 Table 1 p.13-20] |
| 25 | Protection system requirements for reactivity control malfunctions. |  | Same as ARDC | [RG_1.232 Table 1 p.13-20] |

## 해설
기준 20은 보호 계통이 Anticipated Operational Occurrence%%t:AOO%%의 결과로 specified acceptable fuel design limits%%t:SAFDL%%를 넘지 않도록 반응도 제어 계통을 포함한 적절한 계통을 자동으로 기동하고, 사고 조건을 감지해 important to safety 계통과 기기를 기동하도록 설계하게 한다. 기준 21은 수행할 안전 기능에 상응하는 높은 기능 신뢰도와 가동중 시험 가능성을 요구한다. 설계에 반영한 중복성과 독립성은 단일 고장으로 보호 기능을 잃지 않게 하고, 어떤 기기나 채널을 운전에서 빼도 다른 방법으로 허용 신뢰도가 입증되지 않는 한 요구되는 최소 중복성을 잃지 않게 해야 하며, 원자로 운전 중에도 채널을 독립적으로 시험해 고장과 중복성 상실을 찾을 수 있어야 한다. 기준 22는 자연 현상과 정상 운전·정비·시험·가정 사고 조건이 중복 채널에 미치는 영향으로 보호 기능을 잃지 않게 하거나 다른 정의된 근거로 수용 가능함을 입증하게 하며, 기능 다양성이나 기기 설계·작동 원리의 다양성 같은 설계 기법을 실행 가능한 범위에서 쓰게 한다. 기준 24는 제어 계통의 단일 기기·채널 고장이나, 제어 계통과 보호 계통에 공통인 단일 기기·채널의 고장이나 운전 제외 뒤에도 보호 계통의 신뢰도·중복성·독립성 요건을 모두 만족하는 계통이 남도록 보호 계통을 제어 계통과 분리하고, 두 계통의 상호 연결을 안전을 크게 해치지 않는 수준으로 제한하게 한다. 네 기준은 GDC%%t:GDC%%와 같다.

기준 23은 계통 분리, 에너지 상실, 가정한 불리한 환경을 겪을 때 보호 계통이 안전 상태나 다른 정의된 근거로 수용 가능하다고 입증된 상태로 고장 나도록 설계하게 한다. advanced reactor design criteria의 같은 번호 기준과 달리 불리한 환경의 예에 소듐과 소듐 반응 생성물을 넣었으며, 근거는 NRC 직원이 이전 검토에서 이 문구를 추가하도록 권고했기 때문이라고 적는다. 기준 25는 반응도 제어 계통의 단일 오작동을 고려해 모든 AOO%%t:AOO%%에서 SAFDL%%t:SAFDL%%을 넘지 않도록 보호 계통을 설계하게 한다. 근거는 보호 계통이 단일 고장과 결합한 AOO%%t:AOO%%에서 이 한계를 보호하도록 설계되며, 단일 고장과 결합한 가정 사고에서는 그럴 필요가 없음을 명확히 하려고 문구를 더했고, 기술 포괄적으로 만들려고 예시를 지웠다고 설명한다.

## 관련 문서
- [[Principal_Design_Criteria_Non_LWR]]
- [[Non_LWR_Design_Criteria_Crosswalk]]
- [[SFR_DC_Reactivity_Control]]
- [[RG_1.232]]
