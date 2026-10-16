---
type: natrium
aliases: []
sources: [SER_KU1_CP]
status: checked
verified: 2026-10-16
term:
tags: [natrium, ssc-classification, nrc-review]
terms_pending: []
---
# NRC의 SSC 안전 분류 평가 (NRC Evaluation of SSC Safety Classification)

> [!abstract] 요약
> NRC staff는 Kemmerer Unit 1의 Structures, Systems, and Components%%t:SSC%% 안전 분류 과정이 construction permit%%t:CP%% 신청에 수용 가능하다고 판단했다. 다만 NEI 18-04 방법론에서 의도치 않게 벗어난 점 두 가지와 기시사건 가능성을 줄이는 기능의 처리를 지적했고, 이 차이들이 시설 위험도에 미치는 영향은 작다고 보았다. 피동 Non-Safety-Related with Special Treatment%%t:NSRST%%의 열화 성능 credit은 합리적이라고 보되 최종 판단은 operating license%%t:OL%% 단계로 넘겼다.

## 원문 사실
- "Under this process, the most safety-significant SSCs are classified as SR, SSCs that perform safety-significant functions but are less safety-significant are classified as non-safety-related with special treatment (NSRST), and other SSCs are classified as nonsafety-related with no special treatment (NST)." [SER_KU1_CP §5.1 p.335]
- "Depending on the design, the SSCs classified as SR under the NEI 18-04 methodology are not necessarily the same as the SSCs that meet the definition of SR in 10 CFR 50.2." [SER_KU1_CP §5.1 p.335]
- "As such, Appendix B evaluates an exemption from the substantive requirements in 10 CFR Part 50 that refer to SR SSCs." [SER_KU1_CP §5.1 p.335]
- "USO unintentionally deviated from the LMP methodology in two ways while performing these risk-significant function determinations for the CPA:" [SER_KU1_CP §5.1 p.337]
- "1. Identification of RSFs was performed using the 95th percentile versus mean risk values." [SER_KU1_CP §5.1 p.337]
- "2. Identification of risk-significant NSRST functions needed to keep LBEs within the F-C target was not performed." [SER_KU1_CP §5.1 p.337]
- "The first deviation is conservative and may have resulted in a small number of SSCs that should have been classified as risk-significant NSRST being classified as SR, reducing the impacts of the second deviation." [SER_KU1_CP §5.1 p.337]
- "With this and the use of the 95th percentile in identifying RSF, the staff determined that the impact of this second deviation on the overall design and facility risk at the CP stage is small. USO has modified their process and workflow to ensure that this step for identifying risk-significant NSRST functions is performed moving forward, in a manner consistent with the LMP methodology." [SER_KU1_CP §5.1 p.337]
- "During its review of the PSAR, the staff identified that some preventative functions were not being evaluated through the SSC safety classification process." [SER_KU1_CP §5.1 p.338]
- "The process in NEI 18-04 indicates that preventative functions serving to reduce the likelihood of IEs are PSFs that should go through the same SSC classification process as mitigative functions." [SER_KU1_CP §5.1 p.338]
- "USO’s alternative process has the potential to result in some preventative SSCs that could have been classified as risk-significant being classified as NSRST for DID because evaluations of whether the function is needed to keep LBEs below the F-C target are not performed." [SER_KU1_CP §5.1 p.338]
- "Its implementation, and the resulting impact on SSC classifications can be left to the OL stage based on the limited scope of SSCs impacted and the conclusions listed above." [SER_KU1_CP §5.1 p.339]
- "However, based on USO’s interpretation of statement (a) that NSRST SSCs may continue to function but not perform RSFs, and statement (b), USO incorporated some passive NSRST SSCs performing at a degraded level in their DBA source term analyses." [SER_KU1_CP §5.1 p.339]
- "The staff determined that USO’s interpretation of the guidance and approach to ascribing some amount of degraded performance to passive NSRST SSCs in DBA source term analyses was reasonable, but acceptability is dependent on the design aspects of the SSCs and the level of degraded performance credited." [SER_KU1_CP §5.1 p.339]
- "Since the design is preliminary, a final determination on the acceptability of this approach to DBA source term analysis will be made at the OL stage when the methodology and complete scope of SSCs credited with degraded performance will be available for review." [SER_KU1_CP §5.1 p.339]
- "Because the LMP methodology reduces the use of SR equipment by using NSRST items to mitigate events in the AOO, BDBE, and 95th percentile consequence regions as well as provide DID, widespread failure of NSRST from a seismic event could result in an unacceptably high consequence." [SER_KU1_CP §5.1 p.340]
- "USO has expanded the scope of seismic interaction beyond support for systems or components located above or near SR and NSRST SSCs to buildings, including the reactor building (RXB) superstructure, and any component containing sodium." [SER_KU1_CP §5.1 p.341]
- "The impacts of differences from the LMP methodology noted above on the preliminary design have been assessed and found to be small relative to the overall facility risk." [SER_KU1_CP §5.1.1 p.342]
- "Because the SSC safety classification process relies on the results of the PRA to determine classification and risk significance, these SSCs will need to be incorporated in the PRA prior to the OL application to confirm that the appropriate SSC safety classification and risk significance was assigned." [SER_KU1_CP §5.2 p.344]
- "Based on its review as documented above and supported by the General Audit, the staff determined USO’s SSC safety classification process meets the requirements in 10 CFR 50.34(a)(1), (4), and 10 CFR 50.35 and is acceptable for the CP application considering the following:" [SER_KU1_CP §5.1.1 p.341]
- "In this additional step, various sets of non-SR functions were evaluated, collectively with the SR functions, to identify the minimum set of additional non-SR functions that were needed to ensure that all LBEs were below the F-C target when assessed at the mean risk values. The set of additional non-SR functions were classified as NSRST for DID." [SER_KU1_CP §5.1 p.337]

| Task* | LBEs Evaluated | Criteria Compared Against | Values Used | Resulting SSC Classification and risk importance category | 출처 |
|---|---|---|---|---|---|
| 7a.1 | DBEs and AOOs and BDBEs with uncertainty bands that extend into the DBE region | F-C target curve | Mean | SR RSF, risk-significant and safety-significant | [SER_KU1_CP Table 5.1-1 p.343] |
| 7a.2 | BDBEs with mean consequences that exceed 25 rem TEDE | F-C target curve | Mean | SR RSF, risk-significant and safety-significant | [SER_KU1_CP Table 5.1-1 p.343] |
| 7d | DBAs | 10 CFR 50.34 dose limits | 95th percentile or greater | SR RSF, safety-significant | [SER_KU1_CP Table 5.1-1 p.343] |
| 7a.3 | All non-DBA LBEs | F-C target curve | 95th percentile | NSRST, risk-significant and safety-significant | [SER_KU1_CP Table 5.1-1 p.343] |
| 7b | All non-DBA LBEs | 1% of cumulative risk metrics | Mean | NSRST, risk-significant and safety-significant | [SER_KU1_CP Table 5.1-1 p.343] |

## 해설
staff는 NEI 18-04 분류 체계를 다음과 같이 요약했다. 가장 safety-significant한 SSC%%t:SSC%%는 Safety-Related%%t:SR%%, safety-significant 기능을 하지만 그 정도가 덜한 것은 NSRST%%t:NSRST%%, 나머지는 Non-Safety-Related with No Special Treatment%%t:NST%%이다. 이 방법론의 SR%%t:SR%%이 10 CFR 50.2의 SR%%t:SR%% 정의와 반드시 같지 않으므로, 관련 요건의 면제는 `SER` Appendix B에서 평가된다. 표의 Task별 기준은 staff가 NEI 18-04 §3.2.2에서 정리한 것으로, Required Safety Function%%t:RSF%% 판정에는 mean, NSRST%%t:NSRST%% 위험도 중요 판정에는 95th percentile을 쓴다.

staff가 지적한 사업자의 의도치 않은 이탈은 두 가지이다.
- RSF%%t:RSF%%를 mean이 아닌 95th percentile로 식별했다.
- Frequency-Consequence Target%%t:FC_TARGET%% 유지에 필요한 위험도 중요 NSRST%%t:NSRST%% 기능을 식별하지 않았다.

첫째는 보수적이어서 위험도 중요 NSRST%%t:NSRST%%여야 할 일부 SSC%%t:SSC%%가 SR%%t:SR%%로 분류되었을 수 있고, 이것이 둘째의 영향을 줄인다. 사업자는 non-SR 기능 조합을 평가해 F-C Target%%t:FC_TARGET%% 유지에 필요한 최소 집합을 심층방어(Defense-in-Depth)%%t:DID%%용 NSRST%%t:NSRST%%로 분류하는 추가 단계를 수행했다. staff는 이 단계와 95th percentile 사용을 근거로 둘째 이탈의 영향이 작다고 판단했고, 사업자는 이후 절차를 Licensing Modernization Project%%t:LMP%% 방법론에 맞게 고쳤다.

나머지 지적 사항은 다음과 같다.
- **Prevention Function%%t:PREVENTION_FUNCTION%%:** 기시사건 가능성을 줄이는 Prevention Function%%t:PREVENTION_FUNCTION%% 일부가 분류 과정을 거치지 않았다. NEI 18-04는 이들도 Mitigation Function%%t:MITIGATION_FUNCTION%%과 같은 과정을 거치도록 한다. 사업자의 대안 과정은 위험도 중요로 분류되어야 할 예방용 SSC%%t:SSC%%를 심층방어%%t:DID%%용 NSRST%%t:NSRST%%로 분류할 가능성이 있으나, 영향 범위가 제한적이어서 OL%%t:OL%% 단계로 넘겼다.
- **피동 NSRST%%t:NSRST%%의 열화 성능 credit:** staff는 Design Basis Accident%%t:DBA%% 선원항(source term)%%t:SOURCE_TERM%% 해석에서 이를 credit한 사업자의 해석과 접근이 합리적이라고 보았다. 다만 수용성은 SSC%%t:SSC%% 설계와 credit된 열화 수준에 달려 있으며, 최종 판단은 OL%%t:OL%% 단계에서 한다.
- **지진 상호작용:** NSRST%%t:NSRST%%가 Anticipated Operational Occurrence%%t:AOO%%, Beyond Design Basis Event%%t:BDBE%%, 95th percentile 결과 영역의 사건을 완화하므로, 지진으로 NSRST%%t:NSRST%%가 광범위하게 실패하면 결과가 받아들일 수 없게 클 수 있다. 사업자는 지진 상호작용 범위를 건물과 소듐을 담은 모든 기기로 넓혔다.

staff는 이 차이들이 예비 설계에 미치는 영향이 전체 시설 위험도에 비해 작다고 결론지었다. PRA에 아직 반영되지 않은 SSC%%t:SSC%%는 OL%%t:OL%% 신청 전에 PRA에 넣어 분류를 확인해야 한다.

## 관련 문서
- [[SER_KU1_CP]]
- [[Natrium_SER_PDC_SR_NSRST_Review]]
- [[Risk_Significant_SSC]]
- [[Natrium_SER_LBE_Methodologies_Review]]
