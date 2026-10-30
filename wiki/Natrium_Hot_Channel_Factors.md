---
type: natrium
aliases: []
sources:
- TP-LIC-LET-0080
- NAT-3049
- TP-LIC-RPT-0011
- ACRS_ML25293A458
status: checked
verified: 2026-10-30
term: HCF
tags:
- natrium
- thermal-hydraulics
terms_pending:
- FOM
- NASCENT
---

# Hot Channel Factor (HCF)

> [!abstract] 요약
> TerraPower의 사전 신청 단계 회의 자료는 Natrium의 첨두피복재온도(peak cladding temperature)%%t:PEAK_CLADDING_TEMPERATURE%% 해석에서 불확도를 Hot Channel Factor%%t:HCF%%로 반영하며, HCF%%t:HCF%%를 direct와 statistical로 나누고 다섯 불확도 범주로 분류한다고 적는다.
> 같은 자료는 냉각재·막·피복재 온도 상승에 direct HCF%%t:HCF%%를 곱해 더하고 statistical HCF%%t:HCF%%의 기여를 제곱합 제곱근으로 결합해 `2-sigma` 피복재 내면 온도를 구하는 식을 보이며, Natrium 값은 비공개이고 `EBR-II`·`FFTF`의 냉각재 HCF%%t:HCF%% 조합 값만 공개한다.
> 이 방법은 사전 신청 단계 자료의 것이며, 건설허가 신청의 `TP-LIC-RPT-0011`이 같은 방법을 쓰는지는 그 보고서의 해당 절이 비공개여서 vault에 없다.

## 원문 사실
- "pre-application engagement meeting" [TP-LIC-LET-0080 p.1]
- "The following pre-CPA licensing activities for the core thermal hydraulics group are planned:" [TP-LIC-LET-0080 Licensing Plan p.17]
- "Nascent white paper submitted (March 2023)" [TP-LIC-LET-0080 Licensing Plan p.17]
- "This report is developed in support of a construction permit application" [TP-LIC-RPT-0011 §1 p.9]
- "Hot channel factors: consistent with usage in historic SFR applications" [ACRS_ML25293A458 Methods p.12]
- "Cladding temperature is an important Figure of Merit" [TP-LIC-LET-0080 Typical Axial Temperature Profile p.30]
- "Impacts creep and Fuel-Cladding Chemical Interaction limits" [TP-LIC-LET-0080 Typical Axial Temperature Profile p.30]
- "Cladding temperature constraints are typically more limiting than fuel or coolant temperature constraints" [TP-LIC-LET-0080 Typical Axial Temperature Profile p.30]
- "In SFRs the steady-state peak cladding temperature occurs near the top of the heated length" [TP-LIC-LET-0080 Typical Axial Temperature Profile p.30]
- "One key Figure of Merit (FoM) used in the analysis of Natrium fuel assemblies is the peak cladding temperature." [NAT-3049 §3.1 p.12]
- "This is an important FoM because the performance of the fuel cladding can be degraded by the temperature-dependent phenomena such as thermal creep and Fuel-Cladding Chemical Interaction (FCCI)." [NAT-3049 §3.1 p.12]
- "Core Cooling Hydraulics evaluates the core flow and pressure loss, margin to sodium boiling, and the peak clad and fuel temperatures with a 1D thermal hydraulic model of the core." [TP-LIC-LET-0080 Core Cooling Hydraulics p.33]
- "The peak fluid temperature is computed using the Nascent model." [TP-LIC-LET-0080 Core Cooling Hydraulics p.33]
- "Analysis is performed at steady-state rated/off-rated conditions to meet temperature limits accounting for uncertainties with Hot Channel Factors." [TP-LIC-LET-0080 Core Cooling Hydraulics p.33]
- "Specifically, the Nascent (Natrium Simplified Coolant Energy Transport) model used to predict the steady-state peak coolant temperature in an assembly subchannels." [NAT-3049 §2 p.11]
- "Scope: peak fluid temperature in fuel assemblies" [TP-LIC-LET-0080 Nascent Model Overview p.41]
- "Finally, the related topics of the Mongoose++ subchannel solver and Hot Channel Factors are briefly discussed." [NAT-3049 §3 p.11]
- "Uncertainties in the Nascent model predictions will be applied using Hot Channel Factors" [TP-LIC-LET-0080 Nascent Model Uncertainties p.50]
- "The statistical HCF will account for:" [TP-LIC-LET-0080 Nascent Model Uncertainties p.50]
- "Sensitivity in peak temperature due to uncertainty in constitutive models" [TP-LIC-LET-0080 Nascent Model Uncertainties p.50]
- "The direct HCF will account for:" [TP-LIC-LET-0080 Nascent Model Uncertainties p.50]
- "Localized temperature peaking due to wire azimuthal position" [TP-LIC-LET-0080 Nascent Model Uncertainties p.50]
- "Bias that yields conservative predictions relative to OSU" [TP-LIC-LET-0080 Nascent Model Uncertainties p.50]
- "HCFs fall into five different categories:" [TP-LIC-LET-0080 Detailed HCFs p.53]
- "For conceptual and preliminary design either Natrium specific values are determined, or historical values are shown to be conservative with a development plan." [TP-LIC-LET-0080 Detailed HCFs p.53]
- "For final design Natrium specific values will be determined." [TP-LIC-LET-0080 Detailed HCFs p.53]
- "Currently the Natrium Type 1 HCFs are similar to historical designs" [TP-LIC-LET-0080 Coolant HCF Comparison p.54]
- "The statistical uncertainty replaces the direct bias for flow distribution, and the inlet flow distribution uncertainty treated statistically" [TP-LIC-LET-0080 Coolant HCF Comparison p.54]
- "To compute the “2-sigma” inner cladding temperature:" [TP-LIC-LET-0080 Application of Hot Channel Factors p.55]
- "J. Muraoka, R. E. Peterson, R. G. Brown, W. D. Yule, D. S. Dutt, and J. E. Hanson, “Assessment of FFTF Hot Channel Factors”, Hanford Engineering Development Laboratory, HEDL-TI-75226 (1976)." [NAT-3049 §7 p.25]
- "A. J. Friedland, “CRBRP Core Assemblies Hot Channel Factors Preliminary Analysis”, Westinghouse Advanced Reactors Division, WARD-D-0050 Rev. 3 (1979)." [NAT-3049 §7 p.25]
- "Y. S. Tang, R. D. Coffield Jr., and R. A. Markley, ... Thermal Analysis of Liquid Metal Fast Breeder Reactors" [NAT-3049 §7 p.25]

| HCF 범주 (Detailed HCFs) | 출처 |
|---|---|
| Control/measurement uncertainties | [TP-LIC-LET-0080 Detailed HCFs p.53] |
| Manufacturing uncertainties | [TP-LIC-LET-0080 Detailed HCFs p.53] |
| Material property uncertainties | [TP-LIC-LET-0080 Detailed HCFs p.53] |
| Nuclear uncertainties | [TP-LIC-LET-0080 Detailed HCFs p.53] |
| Thermal hydraulic uncertainties | [TP-LIC-LET-0080 Detailed HCFs p.53] |

| 냉각재 HCF 조합 ((a)(4)는 비공개 표시) | Natrium Type 1 | EBR-II | FFTF-Metal | FFTF-SAR | FFTF-SAR* | 출처 |
|---|---|---|---|---|---|---|
| Direct combination | (a)(4) | 1.020 | 1.071 | 1.221 | (a)(4) | [TP-LIC-LET-0080 Coolant HCF Comparison p.54] |
| Statistical combination --2σ | (a)(4) | 1.089 | 1.087 | 1.067 | (a)(4) | [TP-LIC-LET-0080 Coolant HCF Comparison p.54] |
| Overall combined --2σ | (a)(4) | 1.111 | 1.164 | 1.302 | (a)(4) | [TP-LIC-LET-0080 Coolant HCF Comparison p.54] |

| 본문의 전부 또는 일부가 비공개인 절·슬라이드·그림·표 제목 | 출처 |
|---|---|
| Relationship Between the Nascent Model and Hot Channel Factors | [NAT-3049 §3.4 p.13] |
| Peak Clad Temperature Overview | [TP-LIC-LET-0080 Peak Clad Temperature Overview p.40] |
| Hot Channel Factor Overview | [TP-LIC-LET-0080 Hot Channel Factor Overview p.52] |
| Nascent Model Uncertainties | [TP-LIC-LET-0080 Nascent Model Uncertainties p.50] |
| Detailed HCFs | [TP-LIC-LET-0080 Detailed HCFs p.53] |
| 3.2.1.4 Hot Channel Factors | [TP-LIC-RPT-0011 §3.2.1.4 p.37] |
| 4.1.2.4 Hot Channel Factors | [TP-LIC-RPT-0011 §4.1.2.4 p.50] |
| Figure 4-1 Example relative temperature and uncertainty profiles with layered hot channel factor | [TP-LIC-RPT-0011 Figure 4-1 p.51] |
| 8.1.16 Hot Channel Factors | [TP-LIC-RPT-0011 §8.1.16 p.88] |
| Table 8-13: Hot Channel Factors for Fuel Assemblies | [TP-LIC-RPT-0011 Table 8-13 p.89] |

![[TP-LIC-LET-0080_Slide_p55.png]]
- "Application of Hot Channel Factors" [TP-LIC-LET-0080 Application of Hot Channel Factors p.55]

## 해설
**출처와 시점.** 이 노트의 방법 서술은 TerraPower가 건설허가 신청 전 사전 신청 단계에 NRC에 낸 `Core Thermal Hydraulic Methods` 회의 자료(`TP-LIC-LET-0080`)와 Natrium Simplified Coolant Energy Transport%%t:NASCENT%% 백서(`NAT-3049`)의 공개본에서 왔다. 건설허가 신청의 [[TP-LIC-RPT-0011]]은 HCF%%t:HCF%%를 다루는 절·그림·표의 본문과 값이 공개본에서 비공개여서([[Natrium_Core_Thermal_Hydraulic_Design]]), 그 보고서가 이 노트의 방법과 같은지는 vault에 없다. `ACRS` 발표는 HCF%%t:HCF%%가 과거 sodium-cooled fast reactor 적용과 일관된다고 적으나, 이 문장이 같은 방법임을 보이지는 않는다.

**PCT%%t:PEAK_CLADDING_TEMPERATURE%%와 해석 위치.** 회의 자료는 피복재 온도를 중요한 Figure of Merit%%t:FOM%%로 두며, creep와 `Fuel-Cladding Chemical Interaction` 한계에 영향을 주고 연료·냉각재 온도 제약보다 대개 더 제한적이라고 적는다. sodium-cooled fast reactor에서 정상상태 PCT%%t:PEAK_CLADDING_TEMPERATURE%%는 가열 길이 상단 부근에 생긴다. 백서도 PCT%%t:PEAK_CLADDING_TEMPERATURE%%를 Natrium 핵연료 집합체 해석의 핵심 FoM%%t:FOM%%으로 두고, 그 이유를 thermal creep와 `FCCI` 같은 온도 의존 현상으로 든다. Core Cooling Hydraulics 방법은 노심의 `1D` 열수력 모형으로 유량·압력 손실, 소듐 비등 여유, 첨두 피복재·연료 온도를 평가하고, 첨두 유체 온도는 Nascent%%t:NASCENT%% 모형으로 계산하며, 정격·비정격 정상상태에서 HCF%%t:HCF%%로 불확도를 반영해 온도 한계를 만족시킨다. Nascent%%t:NASCENT%%의 범위는 핵연료 집합체의 첨두 유체 온도이다.

**HCF%%t:HCF%%의 두 종류와 다섯 범주.** Nascent%%t:NASCENT%% 예측의 불확도는 HCF%%t:HCF%%로 반영한다. statistical HCF%%t:HCF%%는 구성 모형 불확도로 인한 첨두 온도 민감도를, direct HCF%%t:HCF%%는 wire 방위각 위치에 따른 국부 온도 첨두와 `OSU` 대비 보수적 예측을 낳는 편향(뒤 문구 일부 비공개)을 맡는다. HCF%%t:HCF%%는 control/measurement, manufacturing, material property, nuclear, thermal hydraulic 불확도의 다섯 범주로 나뉜다. 개념·예비 설계에서는 Natrium 고유 값을 정하거나 과거 값이 보수적임을 개발 계획과 함께 보이고, 최종 설계에서는 Natrium 고유 값을 정한다. 같은 슬라이드(`Detailed HCFs`)의 나머지 내용은 비공개이다.

**결합식.** `Application of Hot Channel Factors` 슬라이드(위 그림)는 `2-sigma` 피복재 내면 온도를 구하는 식 세 개를 보인다. direct HCF%%t:HCF%%는 냉각재·막·피복재 온도 상승에 각각 곱해 선형으로 더한다. statistical 기여는 첨자 `j`마다 direct HCF%%t:HCF%%를 곱한 세 온도 상승에 statistical HCF%%t:HCF%%에서 1을 뺀 값을 가중해 구하고, 그 제곱합 제곱근에 계수를 곱해 입구 온도와 direct 항에 더한다. 계수와 각 항의 시그마 수준은 그림의 식에 있으며, 정제본은 식을 슬라이드 이미지에서 LaTeX로 옮긴 전사로 싣는다. 이 식은 피복재 내면까지를 다루며, 연료 중심선까지의 확장은 이 자료의 공개본에 없다(식 아래 영역은 비공개).

**냉각재 HCF%%t:HCF%% 비교.** 회의 자료는 현재 Natrium Type 1 HCF%%t:HCF%%가 과거 설계와 비슷하다고 적지만 Natrium 열의 값은 비공개이다. 공개된 조합 값은 `EBR-II`, `FFTF-Metal`, `FFTF-SAR`의 direct, statistical, overall 조합 값이며, direct와 overall 조합에서는 `FFTF-SAR` 값이 가장 크고, statistical 조합에서는 가장 작다. 별표 열(`FFTF-SAR*`)은 유량 분포의 direct bias를 statistical 불확도로 바꾸고 입구 유량 분포 불확도를 statistical로 다룬 경우이며 그 값도 비공개이다.

**과거 문헌.** 백서의 참고문헌에는 `FFTF` HCF%%t:HCF%% 평가(`HEDL-TI-75226`), `CRBRP` 노심 집합체 HCF%%t:HCF%% 예비 해석(`WARD-D-0050` Rev. 3), `LMFBR` 열해석 문헌이 있다. 백서 §3.4(Nascent%%t:NASCENT%%와 HCF%%t:HCF%%의 관계)와 회의 자료의 `Peak Clad Temperature Overview`, `Hot Channel Factor Overview` 슬라이드 본문은 비공개이다.

## 관련 문서
- [[Natrium_Core_Thermal_Hydraulic_Design]]
- [[TP-LIC-RPT-0011]]
- [[TP-LIC-LET-0080]]
- [[NAT-3049]]
- [[Natrium_LBE_Evaluation_Methods]]
- [[Natrium_NRC_Review_Core_Design]]
