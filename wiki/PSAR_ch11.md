---
type: source
key: PSAR_ch11
title: Conduct of Operations
file: references/TP_Natrium_PSAR2025_ch11_Conduct of Operations.md
pdf: references/raw/TP_Natrium_PSAR2025_ch11_Conduct of Operations.pdf
sha256_pdf: e41d9e7866716fed4560b3871ffa98f806bd04f354ce4716500080d97fdf20f0
sha256_md: a2f5a47db04c02778e0bf636c51947014b0d3cee281de4eee7bc70727b99310a
pdf_pages: 77
build:
  converter: opendataloader-pdf 2.5.7 (markdown_page_separator=<!-- page %page-number%
    -->, image_output=external, image_format=png, content_safety_off=off-page, include_header_footer=True)
  cleaned: scripts/clean_references.py (refclean 0.1.0) 2026-09-14
  missing_pct: 0.82
ingest: complete
units:
- unit: U1 §11.3 (EP approach, PEP EPZ), §11.5 (technical specifications, operating
    modes)
  status: complete
- unit: '보완: §11.3.3.2-§11.3.10 (ERO, 기관, 방호 조치, ERF, 훈련, 성능 감시)'
  status: complete
---

# Conduct of Operations (PSAR_ch11)

> [!abstract] 요약
> Kemmerer Unit 1 `PSAR` 11장은 운영 조직(§11.1), 인적 요소 공학(§11.2), 비상 대비(§11.3), 항공기 충돌 평가(§11.4), 기술지침서(§11.5), 직무 적합성과 보안(§11.6)을 다룬다. vault는 비상 대비 접근법과 비상계획구역, 비상 대응 조직과 시설, 기술지침서와 운전 모드를 노트로 옮겼고, §11.4의 비공개 처리된 내용은 인용하지 않았다.

## 서지
- 키: `PSAR_ch11`
- 원문: `references/raw/TP_Natrium_PSAR2025_ch11_Conduct of Operations.pdf`

## 구조
<!-- sync:begin -->
- PDF 쪽 수: 77
- 인쇄 쪽: p2 = i; p3 = ii; p4 = iii; p5 = iv; p6-18 = 11.1-1..11.1-13; p19-50 = 11.2-1..11.2-32; p51-59 = 11.3-1..11.3-9; p60-64 = 11.4-1..11.4-5; p65-74 = 11.5-1..11.5-10; p75-77 = 11.6-1..11.6-3
- 표 (4):
  - Table 11.2-1 NUREG-0711 Technical Elements Compared to Section 11.2
  - Table 11.2-2 Development of HFE Review Guidance for Advanced Reactors
  - Table 11.5-1 Proposed Variables and Conditions for Technical Specifications
  - Table 11.5-2 Operating Modes
- 그림 (4):
  - 11.1-1 Executive Management Organization
  - 11.1-2 Natrium Project Organization
  - 11.1-3 Construction Organization
  - 11.1-4 Operating Organization and Technical Support
- 비공개 (1):
  - 11.4 Aircraft Impact Assessment (PDF p60-64, SRI)
<!-- sync:end -->

## 알려진 모순
- 없음

## 관련 문서
- [[Natrium_Emergency_Preparedness_EPZ]]
- [[Natrium_Operating_Modes]]
- [[Natrium_Technical_Specifications_Scope]]
