---
type: natrium
aliases: []
sources: [PSAR_ch04, PSAR_ch03, NEI_18-04]
status: checked
verified: 2026-09-16
term:
tags: [natrium]
terms_pending: []
---
# Natrium risk-significant LBE의 margin 평가 (Natrium LBE Margin)

> [!abstract] 요약
> `PSAR` Chapter 4의 두 표는 risk-significant Licensing Basis Event%%t:LBE%%의 빈도와 선량이 Frequency-Consequence Target%%t:FC_TARGET%%에서 얼마나 떨어져 있는지를 예비(preliminary) 값으로 평균값 기준 세 건과 95th percentile 기준 열한 건에 대해 비로 보인다. 이 margin 비는 목표 값을 사건 값으로 나눈 것이어서 NEI 18-04의 정의와 방향이 반대이고, `RFH-ESWR-2`의 95th percentile 빈도는 `PSAR` Chapter 3의 값과 다르다.

## 원문 사실
- "Table 4.2-1 and Table 4.2-2 present a summary of the preliminary margins between the frequencies and consequences of the risk-significant LBEs and the F-C target at both the mean and 95th percentile values." [PSAR_ch04 §4.2.1.1 p.8]
- "Only those LBEs identified as risk-significant using mean values are presented in Table 4.2-1." [PSAR_ch04 §4.2.1.1 p.8]
- "Table 4.2-2 presents all risk-significant LBEs." [PSAR_ch04 §4.2.1.1 p.8]
- "See Chapter 3 for the LBE description associated with the LBE identifications." [PSAR_ch04 §4.2.1.1 p.8]
- "The DID baseline to support plant operation will be established at the operating license (OL) stage." [PSAR_ch04 §4.2.1.1 p.8]

| LBE Category | LBE ID | Mean Frequency/ plant-yr | Mean Dose (rem) | F-C Target Frequency at LBE Dose/ plant-yr[a] | Mean Frequency Margin[b] | F-C Target Dose at LBE Frequency (rem)[c] | Mean Dose Margin[d] | 출처 |
|---|---|---|---|---|---|---|---|---|
| BDBE | RFH-ESWR-2 | 3.40E-05 | 3.31 | 1.81E-03 | 53.1 | 50.0 | 15.1 | [PSAR_ch04 Table 4.2-1 p.12] |
| BDBE | RFH-FDEM-2 | 5.25E-07 | 46.0 | 3.88E-05 | 73.8 | 727 | 15.8 | [PSAR_ch04 Table 4.2-1 p.12] |
| BDBE | RFH-LMCA-2 | 8.82E-07 | 46.0 | 3.88E-05 | 44.0 | 522 | 11.3 | [PSAR_ch04 Table 4.2-1 p.12] |

- "[a] Frequency value measured at the LBE mean dose level from the F-C target" [PSAR_ch04 Table 4.2-1 p.12]
- "[b] Ratio of the frequency in Note [a] to the LBE mean frequency (Mean Frequency Margin)" [PSAR_ch04 Table 4.2-1 p.12]
- "[c] Dose value measured at the LBE mean frequency from the F-C target" [PSAR_ch04 Table 4.2-1 p.12]
- "[d] Ratio of the dose in Note [c] to the LBE mean dose (Mean Dose Margin)" [PSAR_ch04 Table 4.2-1 p.12]

| LBE Name | LBE Category | 95th Perc. Freq. [/ plant-yr] | 95th Perc. Dose [rem] | F-C Target Freq. at LBE Dose [/ plant-yr][a] | Mean Frequency Margin[b] | F-C Target Dose at LBE Freq. [rem][c] | Mean Dose Margin[d] | 출처 |
|---|---|---|---|---|---|---|---|---|
| RFH-FDIV-1 | DBE | 8.73E-03 | 0.290 | 3.45E-01 | 39.5 | 1.10 | 3.79 | [PSAR_ch04 Table 4.2-2 p.13] |
| RFH-FDIV-3 | DBE | 4.32E-03 | 0.582 | 1.72E-01 | 39.8 | 1.80 | 3.09 | [PSAR_ch04 Table 4.2-2 p.13] |
| RFH-FDSP-1 | DBE | 3.36E-03 | 0.505 | 1.98E-01 | 59.0 | 2.14 | 4.25 | [PSAR_ch04 Table 4.2-2 p.13] |
| RFH-FDSP-2 | BDBE | 3.72E-04 | 1.01 | 9.86E-03 | 26.5 | 9.99 | 9.90 | [PSAR_ch04 Table 4.2-2 p.13] |
| RFH-ESWR-2 | BDBE | 1.31E-04 | 5.05 | 9.87E-04 | 7.53 | 20.7 | 4.10 | [PSAR_ch04 Table 4.2-2 p.13] |
| RFH-FDIV-2 | BDBE | 8.48E-05 | 1.62 | 5.03E-03 | 59.2 | 27.8 | 17.2 | [PSAR_ch04 Table 4.2-2 p.13] |
| RFH-ESWR-3 | BDBE | 4.94E-06 | 21.0 | 1.29E-04 | 26.1 | 173 | 8.22 | [PSAR_ch04 Table 4.2-2 p.13] |
| RFH-LMCA-2 | BDBE | 3.48E-06 | 70.0 | 2.02E-05 | 5.78 | 216 | 3.08 | [PSAR_ch04 Table 4.2-2 p.13] |
| RFH-FDBL-2 | BDBE | 2.33E-06 | 21.0 | 1.29E-04 | 55.3 | 280 | 13.3 | [PSAR_ch04 Table 4.2-2 p.13] |
| RFH-FDEM-2 | BDBE | 1.99E-06 | 70.0 | 2.02E-05 | 10.1 | 310 | 4.42 | [PSAR_ch04 Table 4.2-2 p.13] |
| RFH-FDPI-1 | BDBE | 1.93E-06 | 21.0 | 1.29E-04 | 66.6 | 316 | 15.0 | [PSAR_ch04 Table 4.2-2 p.13] |

- "[a] Frequency value measured at the LBE mean dose level from the F-C target" [PSAR_ch04 Table 4.2-2 p.13]
- "[b] Ratio of the frequency in Note [a] to the LBE mean frequency (Mean Frequency Margin)" [PSAR_ch04 Table 4.2-2 p.13]
- "[c] Dose value measured at the LBE mean frequency from the F-C target" [PSAR_ch04 Table 4.2-2 p.13]
- "[d] Ratio of the dose in Note [c] to the LBE mean dose (Mean Dose Margin)" [PSAR_ch04 Table 4.2-2 p.13]
- "In each case, margin is expressed as a ratio of the event’s mean value (frequency and dose) to the corresponding F-C Target value (frequency and dose)." [NEI_18-04 §5.7.1 p.72]
- "These margins are established for the LBEs having the highest risk significance within each of the three LBE categories (AOOs, DBEs, and BDBEs)." [NEI_18-04 §5.7.1 p.72]
- "This process is repeated for each individual LBE, grouped by LBE category as part of the DID evaluation during the design development." [NEI_18-04 §5.7.1 p.74]
- "A more conservative evaluation of margins, similar to the first form mentioned above, uses the 95th percentile upper bound values for both LBE frequency and dose to calculate the margins." [NEI_18-04 §5.7.1 p.74]
- "In the LMP framework, an AOO, DBE, or BDBE is regarded as risk-significant if the combination of the upper bound (95%tile) estimates of the frequency and consequence of the LBE are within 1% of the F-C Target AND the upper bound 30-day TEDE dose at the EAB exceeds 2.5 mrem." [NEI_18-04 §6 p.90]
- "mean estimates supported by a robust uncertainty analysis are generally used to support risk significance determinations." [NEI_18-04 §3.2.2 Task 7a p.23]

| 5th Percentile Frequency | Mean Frequency | 95th Percentile Frequency | 출처 |
|---|---|---|---|
| 4.90E-07 | 3.40E-05 | 1.61E-04 | [PSAR_ch03 §3.8.5.4.3 p.97] |

## 해설
`Table 4.2-1`과 `Table 4.2-2`는 risk-significant LBE%%t:LBE%%의 빈도·결과와 F-C Target%%t:FC_TARGET%% 사이의 예비 margin을 평균값과 95th percentile 값으로 요약한다. `Table 4.2-1`에는 평균값으로 risk-significant인 LBE%%t:LBE%%만 싣고 `Table 4.2-2`에는 모든 risk-significant LBE%%t:LBE%%를 싣는다고 적으므로, 평균값으로 판정한 LBE%%t:LBE%%는 전체의 일부이다. LBE%%t:LBE%% 설명은 `Chapter 3`에 있고, 운전을 뒷받침할 심층방어(Defense-in-Depth)%%t:DID%% baseline은 operating license%%t:OL%% 단계에서 확립된다.

평균값 표의 세 LBE%%t:LBE%%는 모두 Beyond Design Basis Event%%t:BDBE%%이다. `RFH-ESWR-2`는 평균 빈도 `3.40E-05`, 평균 선량 `3.31` rem에서 frequency margin `53.1`, dose margin `15.1`이다. `RFH-FDEM-2`와 `RFH-LMCA-2`는 평균 선량이 모두 `46.0` rem이어서 그 선량에서 읽은 F-C Target%%t:FC_TARGET%% 빈도가 `3.88E-05`로 같고, margin은 각각 `73.8`과 `15.8`, `44.0`과 `11.3`이다.

95th percentile 표는 Design Basis Event%%t:DBE%% 세 건과 BDBE%%t:BDBE%% 여덟 건을 싣는다. 표에서 frequency margin이 가장 작은 행은 `RFH-LMCA-2`(`5.78`, dose margin `3.08`)이고, 그다음이 `RFH-ESWR-2`(`7.53`)이다. 이 표는 95th percentile 빈도와 선량으로 값을 적지만, 열 이름과 주석은 `Table 4.2-1`과 같은 `Mean Frequency Margin`, `Mean Dose Margin`, `LBE mean dose`, `LBE mean frequency`를 쓴다.

두 표의 주석은 frequency margin을 LBE%%t:LBE%% 선량에서 읽은 F-C Target%%t:FC_TARGET%% 빈도를 LBE%%t:LBE%% 빈도로 나눈 비로, dose margin을 LBE%%t:LBE%% 빈도에서 읽은 F-C Target%%t:FC_TARGET%% 선량을 LBE%%t:LBE%% 선량으로 나눈 비로 정의한다. NEI 18-04는 margin을 사건의 평균값(빈도와 선량)을 대응하는 F-C Target%%t:FC_TARGET%% 값으로 나눈 비로 적으므로, 같은 이름의 양이 두 원문에서 서로 역수 관계이다.

margin을 구하는 범위에 대해 NEI 18-04는 세 LBE%%t:LBE%% 범주 각각에서 risk significance가 가장 높은 LBE%%t:LBE%%에 대해 정한다고 적는 한편, 빈도와 선량 모두에 95th percentile 상한값을 쓰는 더 보수적인 margin 평가를 들고, 이 과정을 설계 개발 중 심층방어%%t:DID%% 평가의 일부로 개별 LBE%%t:LBE%%마다 범주별로 반복한다고 적는다. risk significance 판정 값에 대해 NEI 18-04 용어집의 risk-significant LBE%%t:LBE%% 정의는 상한(95%tile) 추정을 쓰고, `Task 7a`는 일반적인 risk-informed decision-making에서 견고한 불확실도 해석이 뒷받침하는 평균 추정이 risk significance 판정에 일반적으로 쓰인다고 설명한다([[LBE_Risk_Significance]]).

`RFH-ESWR-2`의 95th percentile 빈도는 `Table 4.2-2`에서 `1.31E-04`, `PSAR` Chapter 3 `§3.8.5.4.3`의 불확실도 표에서 `1.61E-04`이며, 두 `PDF`의 글자열도 각각 이 값이다. `Table 4.2-2`의 frequency margin `7.53`은 F-C Target%%t:FC_TARGET%% 빈도 `9.87E-04`를 `1.31E-04`로 나눈 값과 맞는다. 같은 LBE%%t:LBE%%의 같은 양을 두 장이 다르게 적는다. 이 차이는 모순 목록(`meta/contradictions.md`)에 모아 두었다.

## 관련 문서
- [[DID_Risk_Margins]]
- [[F_C_Target]]
- [[LBE_Risk_Significance]]
- [[Natrium_Risk_Significant_LBEs]]
- [[Natrium_Integrated_Risk_Results]]
- [[Natrium_Plant_Capability_DID_Evaluation]]
- [[PSAR_ch04]]
