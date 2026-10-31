---
type: source
key: TP-LIC-RPT-0011
title: Core Nuclear and Thermal Hydraulic Design Technical Report
file: references/TP-LIC-RPT-0011_Core Nuclear and Thermal Hydraulic Design Technical
  Report.md
pdf: references/raw/TP-LIC-RPT-0011_Core Nuclear and Thermal Hydraulic Design Technical
  Report.pdf
sha256_pdf: 9cd2c27b336251d2c633aa4d82432f016278ff5a4af2f517c27991b29c730e77
sha256_md: 9b46b0f4c5ea3833de4b5cac45fbe99b749aeb3b00417d5b818108998ba3ce80
pdf_pages: 94
build:
  converter: opendataloader-pdf 2.5.7 (markdown_page_separator=<!-- page %page-number%
    -->, image_output=external, image_format=png, content_safety_off=off-page)
  cleaned: scripts/clean_references.py (refclean 0.1.0) 2026-10-26
  missing_pct: 0.27
ingest: partial
units:
- unit: hot channel factor (§1.1 Table 1-1, §3.2–3.2.1.4, §4.1.2–4.1.2.4, Figure 4-1,
    §5.2, §6, §8.1.16)
  status: complete
---

# Core Nuclear and Thermal Hydraulic Design Technical Report (TP-LIC-RPT-0011)

> [!abstract] 요약
> TerraPower의 `TP-LIC-RPT-0011` Revision 0은 Kemmerer Unit 1 건설허가 신청의 노심 핵설계·열수력·노심 기계 해석 방법을 정리한 기술 보고서로, `PSAR` Chapter 3 §3.12–3.13이 평가 모형과 코드를 이 보고서에 넘긴다.
> vault의 원문은 ADAMS 공개본이며, 그림 스물아홉 개 가운데 Figure 4-2만 공개되고 Hot Channel Factor%%t:HCF%% 관련 본문과 표를 포함한 상당 부분이 비공개이다.
> 이 원문은 수시 인제스트 대상이며, 인제스트한 단위는 frontmatter의 `units`가 나타낸다.

## 서지
- 키: `TP-LIC-RPT-0011`
- 원문: `references/raw/TP-LIC-RPT-0011_Core Nuclear and Thermal Hydraulic Design Technical Report.pdf`

## 구조
<!-- sync:begin -->
- PDF 쪽 수: 94
- 인쇄 쪽: p2-94 = 1..93
- 표 (0):
- 그림 (29):
  - 1-1 Coolant Flow Path through the RES and RCC
  - 2-1 Core Assembly Loading for Cycle 1 (Assembly Pitch in Inches)
  - 2-2 Illustration of Cascade Reloading Sequence
  - 2-3 Example Fuel Shuffling Cascade with
  - 2-4 Core Inlet Nozzle Orifice Zone Map
  - 2-5 Illustration of a Universal Stack Nozzle (Dimensions in Inches)
  - 2-6 Vertical Arrangement of Modeled Regions within the Core Assemblies
  - 2-7 Fuel Assembly Design
  - 2-8 Control Rod Assembly Design
  - 2-9 Primary (Left) and Secondary (Right) Control Assembly Cross-Section
  - 2-10 Reflector Assembly Design
  - 2-11 Shield Assembly Design
  - 3-1 
  - 4-1 Example relative temperature and uncertainty profiles with layered hot channel factor
  - 4-2 Example deformation shapes resulting from thermal bowing and assembly restraint
  - 4-3 
  - 8-1 k-effective as a Function of Time
  - 8-2 Maximum Core Assembly Burnup (%FIMA) vs. Time
  - 8-3 Total Assembly Power (MW) at BOL
  - 8-4 Maximum Fuel Assembly Burnup Distribution (%FIMA) at EOEC
  - 8-5 Maximum Assembly DPA at the EOEC
  - 8-6 Core Mid-Plane Pin Linear Power (W/cm) at BOL
  - 8-7 BOL Core Average Axial Power Shapes
  - 8-8 HFP BOL All Rods Critical Individual Assembly Worth
  - 8-9 ARI keff vs Isothermal Temperature at BOL
  - 8-10 Assembly Total Coolant Temperature Coefficient at EOEC, m¢/K
  - 8-11 Assembly Total Doppler Coefficient at BOEC, m¢/K
  - 8-12 Core Decay Heat with Uncertainties and Biases
  - 8-13 Subchannel Temperature Distribution at Outlet at BOL HFP Conditions
- 비공개 (28):
  - Figure 1-1 Coolant Flow Path through the RES and RCC
  - Figure 2-1 Core Assembly Loading for Cycle 1 (Assembly Pitch in Inches)
  - Figure 2-2 Illustration of Cascade Reloading Sequence
  - Figure 2-3 Example Fuel Shuffling Cascade with
  - Figure 2-4 Core Inlet Nozzle Orifice Zone Map
  - Figure 2-5 Illustration of a Universal Stack Nozzle (Dimensions in Inches)
  - Figure 2-6 Vertical Arrangement of Modeled Regions within the Core Assemblies
  - Figure 2-7 Fuel Assembly Design
  - Figure 2-8 Control Rod Assembly Design
  - Figure 2-9 Primary (Left) and Secondary (Right) Control Assembly Cross-Section
  - Figure 2-10 Reflector Assembly Design
  - Figure 2-11 Shield Assembly Design
  - Figure 3-1 
  - Figure 4-1 Example relative temperature and uncertainty profiles with layered hot channel factor
  - Figure 4-3 
  - Figure 8-1 k-effective as a Function of Time
  - Figure 8-2 Maximum Core Assembly Burnup (%FIMA) vs. Time
  - Figure 8-3 Total Assembly Power (MW) at BOL
  - Figure 8-4 Maximum Fuel Assembly Burnup Distribution (%FIMA) at EOEC
  - Figure 8-5 Maximum Assembly DPA at the EOEC
  - Figure 8-6 Core Mid-Plane Pin Linear Power (W/cm) at BOL
  - Figure 8-7 BOL Core Average Axial Power Shapes
  - Figure 8-8 HFP BOL All Rods Critical Individual Assembly Worth
  - Figure 8-9 ARI keff vs Isothermal Temperature at BOL
  - Figure 8-10 Assembly Total Coolant Temperature Coefficient at EOEC, m¢/K
  - Figure 8-11 Assembly Total Doppler Coefficient at BOEC, m¢/K
  - Figure 8-12 Core Decay Heat with Uncertainties and Biases
  - Figure 8-13 Subchannel Temperature Distribution at Outlet at BOL HFP Conditions
<!-- sync:end -->

## 알려진 모순
- 표기 차이: `PSAR` Chapter 3 §3.12.1.1과 §3.13.1, 참고문헌 3.12-1과 3.13-1은 이 보고서를 "Core Design and Thermal Hydraulic Technical Report"로 인용하고, 표지 제목은 "Core Nuclear and Thermal Hydraulic Design Technical Report"이다. 문서 번호와 Revision 0은 같다.

## 관련 문서
- [[Natrium_Core_Thermal_Hydraulic_Design]]
- [[Natrium_Topical_Technical_Reports]]
- [[PSAR_ch03]]
- [[Natrium_Hot_Channel_Factors]]
