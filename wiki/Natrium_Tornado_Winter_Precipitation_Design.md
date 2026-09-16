---
type: natrium
aliases: []
sources: [PSAR_ch06]
status: checked
verified: 2026-09-16
term:
tags: [natrium]
terms_pending: []
---
# Natrium 토네이도와 극한 겨울 강수 설계 (Natrium Tornado and Extreme Winter Precipitation Design)

> [!abstract] 요약
> `PSAR` §6.4.2.2.3과 Table 6.4-13·6.4-14는 설계기준 토네이도를 `RG 1.76`의 `geographic Region III` 값으로 정한다. 최대 풍속 160 miles per hour, 압력강하 0.6 pounds per square inch, 강하율 0.2 pounds per square inch per second이며 비산물은 Schedule 40 Pipe, Automobile, Solid Steel Sphere 세 종류다.
> Extreme winter precipitation load는 `DC/COL-ISG-007`에 따라 75 psf이며 `ASCE 7-16`의 지상 적설하중으로 취급한다.
> Table 6.4-15는 네 건물의 하부·상부구조와 Reactor Air Cooling System별로 토네이도 풍하중, 비산물 방호, 극한 겨울 강수의 적용 여부를 적는다.

## 원문 사실
- "Tornado loads include tornado wind pressure, tornado-generated differential pressure, and tornado-generated missiles." [PSAR_ch06 §6.4.2.2.3 p.28]
- "The maximum wind speed used is 160 miles per hour (260 kilometers per hour) and tornado effects are combined with other loads as prescribed in applicable codes and regulatory guidance." [PSAR_ch06 §6.4.2.2.3 p.28]
- "Tornado wind pressure parameters listed in Table 6.4-13 reflect geographic Region III as defined in Table 1 of RG 1.76, “Design-Basis Tornado and Tornado Missiles for Nuclear Power Plants,” Revision 1." [PSAR_ch06 §6.4.2.2.3 p.28]
- "Tornado-generated differential pressure drop is 0.6 pounds per square inch (4 kilopascals) and the rate of pressure drop is 0.2 pounds per square inch per second (1 kilopascal per second) rate as defined in Table 1 of RG 1.76 for geographic Region III and as listed in Table 6.4-13." [PSAR_ch06 §6.4.2.2.3 p.28]
- "The tornado-generated missile parameters reflect geographic Region III as defined in Table 2 of RG 1.76 and as listed in Table 6.4-14." [PSAR_ch06 §6.4.2.2.3 p.28]
- "The automobile missile is considered to impact elevations less than 30 feet above all grade levels." [PSAR_ch06 §6.4.2.2.3 p.28]
- "Vertical velocities are taken as 0.67 of the corresponding horizontal velocities." [PSAR_ch06 §6.4.2.2.3 p.28]
- "Missiles are considered as striking in all directions." [PSAR_ch06 §6.4.2.2.3 p.28]
- "The site is located in Wyoming, far from coastal areas as discussed in Section 2.4.1.3.4." [PSAR_ch06 §6.4.2.2.3 p.28]
- "Due to the site location, there are no direct impacts from hurricane loading conditions at the site." [PSAR_ch06 §6.4.2.2.3 p.28]
- "The NSRST superstructures are designed for the extreme winter precipitation load of 75 psf in accordance with Interim Staff Guidance DC/COL-ISG-007." [PSAR_ch06 §6.4.2.2.3 p.28]
- "The extreme winter precipitation load is considered as a ground snow load per ASCE 7-16." [PSAR_ch06 §6.4.2.2.3 p.28]
- "Design Basis Tornado Parameters" [PSAR_ch06 Table 6.4-13 p.75]

| Tornado Parameters | Values | Unit | 출처 |
|---|---|---|---|
| Maximum Wind Speed | 160 | miles per hour | [PSAR_ch06 Table 6.4-13 p.75] |
| Translational Speed | 32 | miles per hour | [PSAR_ch06 Table 6.4-13 p.75] |
| Maximum Rotational Speed | 128 | miles per hour | [PSAR_ch06 Table 6.4-13 p.75] |
| Radius of Maximum Rotational Speed | 150 | feet | [PSAR_ch06 Table 6.4-13 p.75] |
| Pressure Drop | 0.6 | pounds per square inch | [PSAR_ch06 Table 6.4-13 p.75] |
| Rate of Pressure Drop | 0.2 | pounds per square inch per second | [PSAR_ch06 Table 6.4-13 p.75] |

- "Design Basis Tornado Missile Spectrum and Maximum Speed" [PSAR_ch06 Table 6.4-14 p.76]

| Missile | Dimension | Mass (pounds) | Horizontal Velocity (feet per second) | Vertical Velocity (feet per second) | 출처 |
|---|---|---|---|---|---|
| Schedule 40 Pipe | 6.625 in diameter × 15 ft long | 287 | 79 | 53 | [PSAR_ch06 Table 6.4-14 p.76] |
| Automobile | 14.9ft × 5.6ft × 4.9ft | 2,595 | 79 | 53 | [PSAR_ch06 Table 6.4-14 p.76] |
| Solid Steel Sphere | 1 in diameter | 0.147 | 20 | 14 | [PSAR_ch06 Table 6.4-14 p.76] |

- "Safety-significant substructures are designed for tornado wind loading and missiles as shown in Table 6.4-15." [PSAR_ch06 §6.4.2.3.1 p.31]
- "Each of the NSRST superstructures are designed to withstand applicable tornado-induced missiles as described in shown in Table 6.4-15." [PSAR_ch06 §6.4.2.3.3 p.35]
- "Applicability of Tornado and Extreme Winter Precipitation Events to Safety-Significant SSCs" [PSAR_ch06 Table 6.4-15 p.77]

| SSC | SSC | SSC | Tornado Wind<sup>3</sup> | Small Tornado Missile Protection<sup>2</sup> | Automobile Tornado Missile Protection<sup>2</sup> | Extreme Winter Precipitation Event | 출처 |
|---|---|---|---|---|---|---|---|
| RXB | Substructure | Substructure | Yes | Yes | Yes | N/A | [PSAR_ch06 Table 6.4-15 p.77] |
| RXB | Superstructure (NST) | Column | Yes | Yes | Yes | Yes | [PSAR_ch06 Table 6.4-15 p.77] |
| RXB | Superstructure (NST) | Building Envelope | No | No | No | Yes | [PSAR_ch06 Table 6.4-15 p.77] |
| RXB | Reactor Air Cooling System |  | Yes | Yes<sup>1</sup> | Yes<sup>1</sup> | Yes | [PSAR_ch06 Table 6.4-15 p.77] |
| FHB<sup>2</sup> | Substructure | Substructure | Yes | No | No | N/A | [PSAR_ch06 Table 6.4-15 p.77] |
| FHB<sup>2</sup> | Superstructure | Column | Yes | Yes | Yes | Yes | [PSAR_ch06 Table 6.4-15 p.77] |
| FHB<sup>2</sup> | Superstructure | Building Envelope | No | No | No | Yes | [PSAR_ch06 Table 6.4-15 p.77] |
| RAB<sup>2</sup> | Substructure | Substructure | N/A | No | No | N/A | [PSAR_ch06 Table 6.4-15 p.77] |
| RAB<sup>2</sup> | Superstructure | Column | Yes | Yes | Yes | Yes | [PSAR_ch06 Table 6.4-15 p.77] |
| RAB<sup>2</sup> | Superstructure | Building Envelope | No | No | Yes | Yes | [PSAR_ch06 Table 6.4-15 p.77] |
| NCB | Substructure | Substructure | Yes | Yes | Yes | N/A | [PSAR_ch06 Table 6.4-15 p.77] |
| NCB | Superstructure | Column | Yes | Yes | Yes | Yes | [PSAR_ch06 Table 6.4-15 p.77] |
| NCB | Superstructure | Building Envelope | No | No | No | Yes | [PSAR_ch06 Table 6.4-15 p.77] |

- "RAC stacks and supports are permitted to sustain localized damage due to tornado missile impacts provided: (1) airflow through RAC remains at a sufficient level to maintain cooling requirements, and (2) analysis shows the undamaged portions of the RAC can still withstand tornado winds." [PSAR_ch06 Table 6.4-15 Note 1 p.77]
- "Solid radioactive waste processing, liquid radioactive waste processing, and gaseous radioactive waste processing equipment located within the FHB are appropriately protected as needed from external missiles. The RAB structure is designed to protect the sodium piping and associated systems and components containing sodium from automobile missiles." [PSAR_ch06 Table 6.4-15 Note 2 p.77]
- "The Building Envelope is designed for normal wind loading as the building is considered as fully enclosed during normal design wind event. The Building Envelope is not credited to protect the building interior from tornado loading conditions." [PSAR_ch06 Table 6.4-15 Note 3 p.77]

## 해설
토네이도 하중은 풍압, 기압차, 비산물의 세 가지로 이루어지고 모두 `RG 1.76`의 `geographic Region III` 값을 쓴다. 설계기준 토네이도의 최대 풍속은 160 miles per hour이고 이동속도 32 miles per hour, 최대 회전속도 128 miles per hour, 최대 회전속도 반경 150 feet이다. 기압차는 0.6 pounds per square inch, 강하율은 0.2 pounds per square inch per second이다. 비산물은 질량 287 pounds의 Schedule 40 Pipe, 2,595 pounds의 Automobile, 0.147 pounds의 Solid Steel Sphere 세 종류이며, 앞의 둘은 수평 79 feet per second·수직 53 feet per second, 마지막은 수평 20 feet per second·수직 14 feet per second이다. 자동차 비산물은 모든 지표면 위 30 feet보다 낮은 표고에 충돌한다고 보고, 수직속도는 대응 수평속도의 0.67배로 잡으며 비산물은 모든 방향에서 온다고 본다.

부지가 Wyoming의 내륙에 있어 허리케인의 직접 영향은 없다고 적는다. Extreme winter precipitation load는 `DC/COL-ISG-007`에 따라 75 pounds per square foot(psf)이며 `ASCE 7-16`의 지상 적설하중으로 다룬다.

Table 6.4-15는 구조물별 적용 여부를 나눈다. Reactor Building 하부구조, `NI` Control Building 하부구조, 그리고 네 건물의 상부구조 기둥은 토네이도 풍하중과 두 비산물 방호가 모두 Yes이다. Fuel Handling Building 하부구조는 풍하중만 Yes이고 비산물 방호는 No이며, Reactor Auxiliary Building 하부구조는 풍하중이 N/A이다. Building Envelope은 정상 풍하중으로만 설계하며 토네이도 하중에서 내부를 보호하는 몫으로 credit하지 않는다. 다만 Reactor Auxiliary Building 외피만은 자동차 비산물 방호가 Yes인데, 주석은 Reactor Auxiliary Building 구조가 나트륨 배관과 나트륨을 담은 계통·기기를 자동차 비산물로부터 보호하도록 설계된다고 적는다. 같은 주석은 Fuel Handling Building 안의 고체·액체·기체 방사성폐기물 처리 기기도 필요에 따라 외부 비산물로부터 적절히 방호된다고 적는다. Reactor Air Cooling System은 풍하중과 두 비산물 방호가 Yes이되, 주석은 냉각 요건을 유지할 만큼 공기 유동이 남고 손상되지 않은 부분이 토네이도 풍하중을 견딤을 해석으로 보이면 굴뚝과 지지물의 국부 손상을 허용한다고 적는다. 하부구조에는 극한 겨울 강수가 N/A, 모든 상부구조에는 Yes이다.

## 관련 문서
- [[Natrium_Safety_Significant_Structures]]
- [[Natrium_Structural_Loads_And_Combinations]]
- [[Natrium_Design_Basis_Hazard_Levels]]
- [[Natrium_Hazard_Screening]]
- [[Natrium_Hazard_Interaction_Requirements]]
- [[Natrium_System_Reactor_Air_Cooling]]
- [[Natrium_Building_Reactor_Auxiliary]]
- [[PSAR_ch06]]
