---
type: source
key: SER_KU1_CP
title: Safety Evaluation of the Kemmerer Power Station Unit 1 Construction Permit
  Application
file: references/SER_KU1_CP_Safety Evaluation of the Kemmerer Power Station Unit 1
  Construction Permit Application.md
pdf: references/raw/SER_KU1_CP_Safety Evaluation of the Kemmerer Power Station Unit
  1 Construction Permit Application.pdf
sha256_pdf: e28f1a00966cef387a91437f4bba8bd05a544a9722e404cb486fac1cc5a2f4b2
sha256_md: 9f1a8972ac836125376a252240b15a6a0cfca5c71abd171a9305204fce85e8b3
pdf_pages: 768
build:
  converter: opendataloader-pdf 2.5.7 (markdown_page_separator=<!-- page %page-number%
    -->, image_output=external, image_format=png, content_safety_off=off-page)
  cleaned: scripts/clean_references.py (refclean 0.1.0) 2026-10-16
  missing_pct: 0.32
ingest: in_progress
units:
- unit: "§3.2-§3.4 (MST, LBE 평가 방법론, LBE 요약)"
  status: complete
- unit: "§3.1 (PRA)"
  status: complete
- unit: "§3.5-§3.13 (AOO, DBE, BDBE, DBA, 10 CFR 50.155, fuel, nuclear, T-H, criticality)"
  status: complete
- unit: "Chapter 4 (plant risk, DID, IDP)"
  status: complete
- unit: "Chapters 5-6 (SSC classification, PDC, SR/NSRST, DBHL, reliability, special treatment, design)"
  status: complete
- unit: "Chapter 7 (system-level reviews: NHS, reactor auxiliary, fuel handling, radwaste, ancillary, I&C, electrical, buildings)"
  status: complete
- unit: "Chapters 1, 11, 13, Appendices A-B (facility, conduct of operations, R&D, permit conditions, exemptions)"
  status: complete
- unit: "잔여 R1: 1, 3-6, 11, 13장의 미인용 하위 절(운영 조직, 비상대비, 지진 해석, 노물리, BDBE/DBA 보강)"
  status: complete
- unit: "잔여 R2: 7장 계통별 PDC 정합성·programmatic special treatment 하위 절"
  status: pending
---

# Safety Evaluation of the Kemmerer Power Station Unit 1 Construction Permit Application (SER_KU1_CP)

> [!abstract] 요약
> (인제스트 완료 시 작성)

## 서지
- 키: `SER_KU1_CP`
- 원문: `references/raw/SER_KU1_CP_Safety Evaluation of the Kemmerer Power Station Unit 1 Construction Permit Application.pdf`

## 구조
<!-- sync:begin -->
- PDF 쪽 수: 768
- 인쇄 쪽: p2 = ii; p3 = iii; p4 = iv; p5 = v; p6 = vi; p7 = vii; p8 = viii; p9 = ix; p10 = x; p11 = xi; p12 = xii; p13 = xiii; p14 = xiv; p15 = xv; p16 = xvi; p17 = xvii; p18 = xviii; p19 = xix; p20 = xx; p21 = xxi; p22 = xxii; p23 = xxiii; p24-30 = 1-1..1-7; p32-41 = 1-9..1-18; p43-54 = 1-20..1-31; p55-151 = 2-1..2-97; p152-321 = 3-1..3-170; p322-333 = 4-1..4-12; p334-342 = 5-1..5-9; p344-360 = 5-11..5-27; p361-406 = 6-1..6-46; p407-608 = 7-1..7-202; p609-634 = 8-1..8-26; p635-645 = 9-1..9-11; p646-651 = 10-1..10-6; p652-709 = 11-1..11-58; p710-712 = 12-1..12-3; p713-723 = 13-1..13-11; p724-731 = 14-1..14-8
- 표 (0):
- 그림 (0):
- 비공개 (0):
<!-- sync:end -->

## 알려진 모순
- C59: §3.7.1.1의 `AST` 표기와 alternative shunt trip(DL4-RC6)의 불일치
- C60: §7.2.3.1.15.1의 "seven functions"와 여섯 항목 목록(`meta/contradictions.md`)

## 관련 문서
- [[Natrium_SER_MST_Methodology_Review]]
- [[Natrium_SER_Event_Source_Terms_Review]]
- [[Natrium_SER_LBE_Methodologies_Review]]
- [[Natrium_SER_Major_Accident_Review]]
- [[Natrium_SER_LBE_Summary_Review]]
- [[Natrium_SER_PRA_Review]]
- [[Natrium_SER_PRA_OL_Expectations]]
- [[Natrium_SER_AOO_DBE_Review]]
- [[Natrium_SER_BDBE_DBA_Review]]
- [[Natrium_SER_Core_Fuel_Design_Review]]
- [[Natrium_SER_Integrated_Evaluation_Review]]
- [[Natrium_SER_SSC_Classification_Review]]
- [[Natrium_SER_PDC_SR_NSRST_Review]]
- [[Natrium_SER_DBHL_Review]]
- [[Natrium_SER_SSC_Design_Review]]
- [[Natrium_SER_Nuclear_Heat_Supply_Review]]
- [[Natrium_SER_Reactor_Auxiliary_Review]]
- [[Natrium_SER_Fuel_Handling_And_Ancillary_Review]]
- [[Natrium_SER_IC_Electrical_Structures_Review]]
- [[Natrium_SER_Facility_Overview_Review]]
- [[Natrium_SER_Conduct_Of_Operations_Review]]
- [[Natrium_SER_RD_And_Permit_Conditions]]
- [[Natrium_SER_Exemptions_Review]]
