# 원문 모순 모음

이 파일은 사용자 판단이 남은 항목만 담는다. 종결한 항목은 관련 노트 해설의 `**규정 대비 메모(항목, 갈래).**`와 소스 카드의 `## 알려진 모순`에 있다. 이 파일에서 지운 항목의 이력은 git에 있고, 2026-10-17 재분류의 상세 메모는 `git show 3d5d07d:meta/contradictions_memos_2026-10-17.md`로 볼 수 있다.

## 판정 원칙

1. 권위 문서는 NRC 문서(`SER_KU1_CP`, NRC staff의 `ACRS_ML25293A458` 발표, `RG_1.232`·`RG_1.233`·`RG_1.247`·`RG_1.253`)와 RG 1.233이 승인한 `NEI_18-04`이다. 신청자 문서(`PSAR_ch*`)가 권위 문서와 다르면 **규정 불일치**로 보고 노트에 메모를 달아 종결한다.
2. 신청자 문서끼리만 다르고 판정할 권위 조항이 없으면 **신청자 문서 내부 불일치**로 메모를 달아 종결한다.
3. 권위 문서끼리 표기·제목·교차참조만 다르고 요건 내용이 같으면 **기록만** 하고 종결한다.
4. RG가 NEI 18-04를 승인하며 붙인 명확화는 NEI 18-04 문장보다 우선한다.
5. SER이 RG·NEI 문언의 모호함을 해석한 경우는 SER 기준으로 해소하고, 문언과 다른 범위를 허용한 경우는 **상위 dispute**로 남긴다.
6. 단순 수치·번호 차이는 둘 중 더 적합한 값을 기준으로 적고, 노트에 오기로 보이며 차후 확인이 필요하다고 적어 종결한다(2026-10-30 사용자 결정).

## 남은 항목

| # | 쟁점 | 근거 | 관련 노트 |
|---|---|---|---|
| C14-1 | RG 1.232 SFR-DC 35: 조문의 단일 고장 문단과 Table 1의 "Same as ARDC" 표시가 다르다 | RG_1.232 App.B, Table 1 | SFR_DC_Residual_Heat_Removal_And_ECC (disputed) |
| C14-6 | RG 1.232 SFR-DC 55: IHX tubing과 중간 계통 배관의 경계 소속 | RG_1.232 SFR-DC 55 | SFR_DC_Reactor_Containment (disputed) |
| C67 | 피동 NSRST의 저하 성능 DBA credit: SER은 합리적이라 보고, NEI 18-04와 RG 1.233은 DBA 완화에 SR SSC만 쓴다고 적는다 | [SER_KU1_CP §5.1 p.339], [NEI_18-04 §4.1 Tasks 4A and 5A p.44], [RG_1.233 §C.1 p.11] | SSC_Safety_Classification (disputed) |
| C81 | alternative shunt trip의 최종 분류: SER §3.7.1.1은 SR 상향을 예상하고, §5.5는 현재 분류가 적절하거나 보수적일 것으로 예상한다 | [SER_KU1_CP §3.7.1.1 p.264], [SER_KU1_CP §5.5 p.354] | Natrium_Alternative_Shunt_Trip (disputed) |

## 남은 항목 상세

인용은 2026-10-17 재분류 메모에서 옮겼다. C81의 상세는 `Natrium_Alternative_Shunt_Trip` 해설의 규정 대비 메모에 있다.

### C14-1 SFR-DC 35

- 조문: "Suitable redundancy in components and features and suitable interconnections, leak detection, isolation, and containment capabilities shall be provided to ensure that the system safety function can be accomplished, assuming a single failure." [RG_1.232 SFR-DC 35 p.82]
- Table 1: `| … | 35 | Emergency core cooling. | Emergency core cooling. | Modified for ARDC |  | Same as ARDC | …` [RG_1.232 Table 1 p.13-20]
- 메모: Table 1은 SFR-DC 35를 ARDC와 같다고 표시하나 부록 B 조문은 ARDC 35에 없는 단일 고장 문단을 둔다. 단일 고장 요건의 적용 여부가 걸린 실질 차이이다.

### C14-6 SFR-DC 55

- 한쪽: "The tubing of the intermediate heat exchanger and associated intermediate coolant system piping are a part of the primary coolant boundary." [RG_1.232 SFR-DC 55 p.92]
- 다른 쪽: "that penetrates containment and is not part of the primary coolant boundary (in its entirety)." [RG_1.232 SFR-DC 55 p.92]; "The use of the term “primary” indicates that the SFR-DC is applicable to the primary cooling system, not the intermediate cooling system." [RG_1.232 SFR-DC 55 p.92]
- 메모: 같은 근거 절이 중간 계통 배관을 primary coolant boundary의 일부라고 적는 한편, 중간 계통은 SFR-DC 57이 다룰 closed system이고 SFR-DC 55는 중간 계통에 적용되지 않는다고 적는다. 격납 관통 중간 계통 배관에 55와 57 가운데 무엇이 적용되는지가 모호하다.

### C67 피동 NSRST의 저하 성능 credit

- SR 한정: "These specific SSCs are classified as SR in Task 5A and are the only ones included in the DBA analysis of the DBAs." [NEI_18-04 §4.1 Tasks 4A and 5A p.44]; "DBAs are derived from the DBEs by prescriptively assuming that only Safety Related SSCs are available to mitigate postulated event sequence consequences to within the 10 CFR 50.34 dose limits." [NEI_18-04 Table 3-1 p.14]; "Design-basis accidents (DBAs) are derived from DBEs by assuming that only safety-related (SR) SSCs are available to mitigate the events." [RG_1.233 §C.1 p.11]
- SER이 근거로 든 문장: "DBAs are then constructed, starting with each DBE, and then assuming that only the SR SSCs perform their associated RSFs." [NEI_18-04 §5.3 Task 10 p.64]; "It is appropriate that for the inherent capabilities of passive functions, degradation of the passive function is considered, as opposed to complete failure (i.e., a physical non-existence of that function)." [NEI_18-04 §5.6.2 p.69]
- SER 판단: "The staff determined that USO’s interpretation of the guidance and approach to ascribing some amount of degraded performance to passive NSRST SSCs in DBA source term analyses was reasonable, but acceptability is dependent on the design aspects of the SSCs and the level of degraded performance credited." [SER_KU1_CP §5.1 p.339]; "Since the design is preliminary, a final determination on the acceptability of this approach to DBA source term analysis will be made at the OL stage when the methodology and complete scope of SSCs credited with degraded performance will be available for review." [SER_KU1_CP §5.1 p.339]
- SER의 같은 규칙: "they are derived from the set of DBEs and AOOs and BDBEs with frequency bands extending into the DBE region by deterministically assuming that only safety-related SSCs are available to respond to the event." [SER_KU1_CP §3.4.1 p.225]; "Conservative consequences evaluation in which only available SR SSCs perform their function" [SER_KU1_CP Table 5.1-1 p.342]
- 메모: SER §5.1의 해당 소절은 SR 한정 세 문장을 다루지 않고, §3.4.1과 Table 5.1-1의 같은 규칙과의 관계도 설명하지 않는다. §5.6.2의 저하 문장은 Table 5-2 심층방어 지침의 맥락에 있고 DBA 해석을 지칭하지 않는다. SER 스스로 최종 판단을 OL 단계로 미루었으므로 권위 문서 사이의 해석 차이가 남는다.
