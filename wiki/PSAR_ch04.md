---
type: source
key: PSAR_ch04
title: Integrated Evaluations
file: references/TP_Natrium_PSAR2025_ch4_integrated evaluations.md
pdf: references/raw/TP_Natrium_PSAR2025_ch4_integrated evaluations.pdf
sha256_pdf: 834f13637f1937a62bd531c8c216e6224ca989402267b64bb9fe15f765a561c8
sha256_md: 24ef2ba47415baaa60ea83af97ee2f85d7754fe50148b79962244fa13a7d010d
pdf_pages: 16
build:
  converter: opendataloader-pdf 2.5.7 (markdown_page_separator=<!-- page %page-number%
    -->, image_output=external, image_format=png, content_safety_off=off-page, include_header_footer=True)
  cleaned: scripts/clean_references.py (refclean 0.1.0) 2026-10-20
  missing_pct: 0.0
ingest: complete
units:
- unit: U1 §4.1, §4.2.1.1, Tables 4.2-1 and 4.2-2 (integrated risk, LBE margins)
  status: complete
- unit: U2 §4.2 remainder, Tables 4.2-3 to 4.2-5 (Defense Lines, plant capability,
    programmatic and integrated DID)
  status: complete
---

# Integrated Evaluations (PSAR_ch04)

> [!abstract] 요약
> Kemmerer Unit 1 `PSAR` 4장은 발전소 통합 위험을 NEI 18-04의 세 cumulative risk target%%t:CUM_RISK_TARGET%%과 비교하고, risk-significant Licensing Basis Event%%t:LBE%%의 margin, Defense Line%%t:DL%% 전략, 심층방어(Defense-in-Depth)%%t:DID%% 적절성 평가를 요약한다. Programmatic 쪽 평가와 통합 평가 결과, baseline 확립은 operating license%%t:OL%% 단계로 넘긴다.

## 서지
- 키: `PSAR_ch04`
- 원문: `references/raw/TP_Natrium_PSAR2025_ch4_integrated evaluations.pdf`

## 구조
<!-- sync:begin -->
- PDF 쪽 수: 16
- 인쇄 쪽: p2 = i; p3 = ii; p4-5 = 4.1-1..4.1-2; p6-16 = 4.2-1..4.2-11
- 표 (5):
  - Table 4.2-1 Mean Risk Margins for Risk-Significant LBEs
  - Table 4.2-2 95th Percentile Risk Margins for Risk-Significant LBEs
  - Table 4.2-3 Evaluation of DL Functions for Risk-Significant DBEs
  - Table 4.2-4 Evaluation of DL Functions for Risk-Significant BDBEs
  - Table 4.2-5 DBA with Single Feature Reliance
- 그림 (0):
- 비공개 (0):
<!-- sync:end -->

## 알려진 모순
- risk-significant LBE 개수: §4.2.1.2는 "Eight"라고 적으나 Table 4.2-2는 11행을 싣고 PSAR_ch03 요약표도 11건이다 [PSAR_ch04 §4.2.1.2 p.8] [PSAR_ch04 Table 4.2-2 p.13]. [[Natrium_Plant_Capability_DID_Evaluation]]. 판정은 C2.
- `RFH-ESWR-2` 95th percentile 빈도: Table 4.2-2는 1.31E-04, PSAR_ch03 §3.8.5.4.3은 1.61E-04 (두 PDF 글자열 확인) [PSAR_ch04 Table 4.2-2 p.13] [PSAR_ch03 §3.8.5.4.3 p.97]. [[Natrium_LBE_Risk_Margins]], [[Natrium_Risk_Significant_LBEs]]. 판정은 C1.
- DL function 표기: Table 4.2-3의 `DL3-RR1` "Primary System Boundary including RES Barrier"와 `DL3-RR3a`는 PSAR_ch05 Table 5.2-3의 "Primary Coolant Boundary including RES Barrier", `DL3-RR3` "EVHM Cask barrier"와 다르다 [PSAR_ch04 Table 4.2-3 p.14] [PSAR_ch05 Table 5.2-3 p.12].
- margin 비의 방향: 표 주석은 목표 값/사건 값, NEI 18-04 §5.7.1은 사건 값/목표 값 [PSAR_ch04 Table 4.2-1 p.12] [NEI_18-04 §5.7.1 p.73].
- Programmatic DID: §4.2.2 "are evaluated and included"와 §4.2.1.2 "will be provided at the OL stage" (PSAR 내부 문언) [PSAR_ch04 §4.2.2 p.9] [PSAR_ch04 §4.2.1.2 p.8].

## 관련 문서
- [[Natrium_Defense_Lines]]
- [[Natrium_Integrated_Risk_Results]]
- [[Natrium_LBE_Risk_Margins]]
- [[Natrium_Plant_Capability_DID_Evaluation]]
- [[Natrium_Programmatic_And_Integrated_DID]]
