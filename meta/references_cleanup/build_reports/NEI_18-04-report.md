# NEI_18-04 report — NEI 18-04 Rev. 1 (Task 11)

Status: DONE_WITH_CONCERNS. Every dispatch item and every H item of `review_nei.md` §1 is implemented and verified
against the PDF; the concerns (§5) are the verify-side artefacts of merged multi-page tables and two M items that
were deliberately not done (raster-figure transcription, italics).

Files created (ownership per brief): `scripts/refclean/profiles/nei1804.py` (14 steps + `metadata`),
`scripts/refclean/patches/NEI_18-04.json` (9 manual class-C transcriptions: the 8 Table 3-2 formulas and the R_j
equation), `scripts/refclean/tests/test_nei1804.py` (12 unit tests on synthetic elements + 13 checks on the real
document). Regenerated: `references/NEI_18-04_Modernization of Technical Requirements for Licensing of Advanced
Non-Light Water Reactors.md` (1,605 lines, 239 KB, 127 headings, 15 tables, 83 page anchors),
`references/figures/NEI_18-04/Fig_*.png` (11 PNGs, 2.9 MB), `references/raw/_verify/NEI_18-04.json`.
Core modules were not modified.

## 1. Steps in `nei1804.steps()` (run order)

| Step | What it does | Evidence | Review item |
|---|---|---|---|
| `set_page_labels` | Printed page labels from the PDF footer (`… nei.org 49`); the offset rule (printed = PDF page − 8) is the fallback and every footer that carries a number is checked against it (`doc.meta['page_label_mismatch']` is empty). | footers p2–p95 | R1 |
| `drop_noise` | Cover page → frontmatter + H1; front-matter footers (`© NEI 2019 … nei.org ii`, 7 list items); the landscape-page header `August 2019` (p14); `THIS PAGE INTENTIONALLY BLANK` (p41); `SEE TABLES FOLLOWING PAGES` (p89). Marks Cambria Math paragraphs as equations so they are never merged into running text. | p1, p14, p41, p89 | R2, F16, F25 |
| `S.drop_toc` (core) | Drops the TOC/LoF/LoT pages 4–7. | p4–p7 | F26 |
| `figures` | Local figure step (see §5 for why the core step is not used): caption → `**Figure 3-1. …**` paragraph + PNG embed, figure box clamped to the caption line and extended up to the last body line, debris inside the box dropped, `> [!figure]` callouts built from the PDF text layer for Figures 4-3, 5-1 and 5-2, body text glued after the Figure 4-2 caption split off. | p15–p61 renders | F17, F18, R4 |
| `tables` | Replaces the collapsed main-JSON tables with the struct-tree tables: 3-1, 3-2, 4-1, 5-1, 5-3…5-10, the acronym list and the Glossary; Table 5-2 is taken from the main JSON (its cell spans are correct there) with the rowspans filled; the `where:` list becomes 8 items. Fixes per R5: RISC-2 check mark moved to the NSRST column, rowspan shift in 5-3/5-5/5-7/5-8, Table 4-1 single header + `Group` column + notes 1–5, 5-9/5-10 header flattening, group rows of 5-6 and the Glossary into a leading column, repeated page headers dropped. | p8, p14, p36, p52–54, p67–95 renders | F02–F09, F19–F22, R5 |
| `headings` | pypdf outline (55 body sections, depth 0/1/2 → H2/H3/H4 under the H1 title) + the 68 Calibri-BoldItalic 11 pt subheadings (parent + 1), matched in document order by page and y; glued headings split; all other opendataloader headings demoted to paragraphs; `NOTICE`, `ABSTRACT`, `LIST OF ACRONYMS` kept as H2. | outline, PDF fonts | F12, F14–F16, R3 |
| `footnotes` | The 15 `*` and 1 `†` page footnotes become `[^pNN]` references with the definition at the end of the enclosing section; the footnote bodies no longer interrupt the running text. | p10–p71 | F13, R8 |
| `join_breaks` | Rejoins paragraphs and list items split by a page break or by an interposed footnote; a line-end hyphen joins without a space (`all non-` + `safety-related`). Where-list items, footnote definitions and equations are excluded. | p9→p10 … p62→p63 | F27, F13 |
| `lists` | Nesting from the PDF x0 of the item (90 pt → level 0, 108 pt → 1, 126 pt → 2), bullet glyphs stripped, false items at the body margin (`- As …`, `- At …`) demoted to paragraphs, bullet paragraphs promoted to items, the inline `o` sub-item on p38 split. | x0 of the ODL items | F28, F29, F35 |
| `subscripts` | Subscripts lost in extraction restored from PDF span geometry (span ≤ 0.75 × the preceding span, same baseline, lower top): `x<sub>i</sub>` (p35) and the 8 where-list symbols (p73). | p35, p73 spans | F11 |
| `sign_lost_exponents` | Review F01: where the PDF breaks `10-` at a line end and the next line starts with the exponent digit + `/plant`, the converter drops the minus sign. Evidence is taken from the PDF word positions (p14 `1×10-`⁄`4/plant-year`, p16 and p47 `10-`⁄`2/plant-year`) and the three values are restored. In the same step every remaining bare `10-N` before `/plant` becomes E-notation (review R6/§5.3: all 47 occurrences are exponents), which the core rule alone cannot do for paragraphs rejoined across a page break. | p14, p16, p47 | F01, F31 |
| `hyphen_supplement` | Line-end hyphens that the core line pairing misses because table rows merge several cells into one visual line; word pairs are taken inside one PDF text block with the core acceptance rule (the joined form never occurs inline): `NEI-0004 → NEI-00-04`, `Defense-inDepth → Defense-in-Depth`. | p52, p93 | F10, R7 |
| `S.normalise_text` (core) | Entities, whitespace, hyphen map (35 core + 2 supplement), exponents, Obsidian `$` escape. | – | F23, F33 |
| `post_fixes` | Numbered item runs → one Markdown ordered list (no `- 1.` double marker), table rendering (`; ` between list items inside a cell, otherwise a space), line-leading `*` escaped. | – | F30, F36 |

## 2. Dispatch items — result

| # | Item | Result |
|---|---|---|
| 1 | Frontmatter per R1 | Done: `doc_id: NEI 18-04`, `revision: 1`, `date: 2019-08`, `adams: ML19241A472`, `docket: PROJ0689` (both read from the PDF metadata), `series_title`, `issuer`, `source_pdf`, `raw_json`, `raw_json_tables`, `pdf_pages: 95`, `page_label_offset` (printed = PDF page − 8; front matter p2–8 = ii–viii), `tables` (13), `figures` (11), tags, aliases. Page anchors carry the printed label (`<!-- page 9 | 1 -->`). |
| 2 | Headings | Done: 55/55 outline sections (H2/H3/H4) + 68/68 BoldItalic subheadings (parent + 1) under one H1; 14 sections that were list items or plain text promoted, 6 glued headings split, false headings removed (`THIS PAGE INTENTIONALLY BLANK`, `### PRA`, `Systems Engineering Inputs`), 24 captions emitted as bold paragraphs before their table/figure. |
| 3 | H fixes | Done: `1×104/plant-year` → `1E-04`, `10-4 to 102/plant-year` → `1E-04 to 1E-02`, `greater than 102/plant-year` → `1E-02`, each from PDF line-end evidence; 50 exponents in E-notation, no `10-N` left; the 7 corrupted identifiers restored (`NEI-00-04`, `ASME/ANS-Ra-S-1.4-2013`, `RIPB-DM` ×2, `TI-RIPB`, `defense-in-depth` ×2, plus `Defense-in-Depth` in the Glossary); hyphens only from PDF line ends, source typos kept (`stan`, `mean -frequency`, `release s`, `complimentary`, `threating`, `5E-07/plant year`). |
| 4 | Tables | Done: 15 tables. Table 4-1 = 19 rows with 26 check marks matching the review matrix (RISC-2 row check mark in NSRST), single header, `Group` column, notes 1–5 as `<sup>n</sup>`; 5-3/5-5/5-7/5-8 rebuilt one row per item (13/7/32/9 rows) with the attribute filled down and the glued 5-8 cell split; 5-9/5-10 flattened headers with 21/23 check marks; 5-2 rowspans filled (Layer 5 now carries the Layer 4 guidelines, the two Overall Guidelines cells repeat on all five rows) with notes [a]–[d]; 5-4 and 5-6 merged across their two pages; acronyms 53 rows (IDP/IDPP split); Glossary 35 terms with a `Category` column. Table 3-2 formulas and the R_j equation transcribed via patches. |
| 5 | Footnotes, split sentences, lists | Done: 16 footnotes (`[^p10]`, `[^p10b]` for the `†` note, … `[^p71]`), each with exactly one reference and one definition at the end of its section; the 6 sentences that the footnote bodies split are rejoined; 33 nested list items restored (20 at level 1, 13 at level 2); the 6 false list items (`- As …`, `- At …`) are paragraphs. |
| 6 | Figures | Done: 11 figures, each with a bold caption, a PNG (200 dpi crop) and no debris; the 5 vector figures leave no label fragments (`Systems Engineering Inputs`, `Acronymns`, `Iterate as required`, `Color Key`, `### PRA` all absent); informative figure-only text kept in 3 `> [!figure]` callouts (Figure 5-2 bullet lists 7+8+6, Figure 5-1 two explanatory boxes, Figure 4-3 categories, legend and note). |

Review H items F01–F13 are all fixed (F02/F04–F09 by the struct-tree transplant with the R5 corrections, F03/F11 by
the patches, F01/F10/F12/F13 by the rules above).

## 3. Verification

`python scripts/clean_references.py --only NEI_18-04 --verify` (final run, figures rendered):

```
unmatched_headings: []   unmatched_subheads: []   orphan_captions: []
figures_without_caption_element: []   failed_patches: []
verify: pdf_tokens 33984, missing_tokens 452, missing_pct 1.33, pages_with_missing_gt3 22,
        residue {}, headings_whitelist 55, headings_emitted 55
```

`python -m pytest scripts/refclean/tests -q` → 188 passed (25 of them this document's).

**The 452 missing tokens (1.33 %), attributed by counting each missing occurrence against its source:**

| Tokens | Share | Cause |
|---:|---:|---|
| 236 | 52.2 % | text inside the five vector figures, deleted with the debris (the same content is in the PNG, and the informative part is in the three callouts) |
| 85 | 18.8 % | line-end hyphens restored: the PDF yields two tokens (`risk`, `significant`), the output one (`risk-significant`) |
| 49 | 10.8 % | the `© NEI 2019 … nei.org N` footer of the 13 landscape pages (the front-matter footers are dropped as noise, the body footers become page labels) |
| 26 | 5.8 % | repeated page headers and group-label rows of the merged tables (4-1, 5-4, 5-6, Glossary) |
| 20 | 4.4 % | the `o` bullet glyph stripped from the 20 nested list items |
| 36 | 8.0 % | `THIS PAGE INTENTIONALLY BLANK` (4) and `SEE TABLES FOLLOWING PAGES` (4), dropped by decision; subscript restorations `xi`, `Rj`, `FIE`, `PASSC`, `PPSSC`, `rfuel`, `rPB`, `rcont`, `Process5` (9); hyphenated tokens whose own form contains a hyphen (`defense-in`, `non-safety`, `nei-00`, `ans-ra-s-1.4`, 7); printed page numbers in the landscape footers (12) |

No table cell, footnote or body sentence is missing. Two independent checks confirm this:

- every non-empty struct-tree table cell line is present in the output, except where a documented transformation
  rewrites it (exponents, note markers, the split 5-8 cell, the where-list subscripts) — test
  `test_smoke_struct_tree_cells_present`;
- a 48-character sliding window over the PDF text of every body page finds gaps only at table row/column
  boundaries (group column inserted, one row per item), at dropped repeated headers, at the `o` glyphs, at the moved
  footnote definitions, and at page anchors between two paragraphs — no prose is absent.

`pages_with_missing_gt3 = 22` is dominated by pages that legitimately have no page anchor because their content
belongs to a table that starts earlier (p53–54 in Table 4-1, p78 in Table 5-6, p91–95 in the Glossary): the verifier
looks for a page's tokens only in the anchors p−1…p+1. The four glossary pages alone account for 1,488 of the
per-page counts.

## 4. Not fixed (with reason)

| Review item | Decision |
|---|---|
| F18 (M) — transcription of raster-only figure text: the F-C anchor values in Figure 3-1, the Layer 1–5 objective/success wording in Figure 5-3, the two notes under Figure 4-1 | Not done. These three figures have no text layer at all (they are images), so a transcription would be manual OCR of a rendered page; the review forbids estimating the values. The content is in the PNGs, and the caption is the image alt text. If it is wanted, it is a self-contained addition to `figure_callout()` with a fixed, hand-checked string per figure. |
| F37 (L) — italics of the quoted definitions (≈3.4 k characters) | Not restored, per decision D7 (only the RG 1.232 redline, the RG GDC-19 rationale and the ch1 status terms keep emphasis). The quotations are still delimited by their quotation marks. |
| F39 — source typos | Kept verbatim and asserted by a test (`stan`, `mean -frequency`, `release s`, `Acronymns` (inside the deleted Figure 5-4 debris), `complimentary`, `threating`, `5E-07/plant year`). |
| Synthetic column header of the acronym table (`Acronym` \| `Definition`) | The printed list has no header row and Markdown requires one; the two words are the only text in the output that is not in the source. |

## 5. Concerns and core observations (no core patch requested)

1. **The core figure step could not be used for this document**, so `nei1804.figures()` reimplements it (reusing
   `figures.render_png` and `figures.odl_to_visible`): (a) `figures_step` accepts any element that starts with
   `Figure N-M` as the caption, which on p57 would turn the body sentence *“Figure 5-1 illustrates the concept of
   layers of defense …”* into the caption and heading of Figure 5-1; (b) `pdfaux.figure_box` grows the box over every
   text block that touches a drawing, which for Figure 5-2 (p58) covers the whole page, so the body paragraphs under
   the caption would be deleted as debris, while for Figure 3-3 (p28) the box starts below the column title
   *“Systems Engineering Inputs”*, which would then remain as a stray heading. If the core ever wants these cases:
   match the caption against the `FigureRef.caption` text (not only its number), and clamp the box to the caption
   line. No change is required for the other documents, so none is proposed.
2. **Multi-page tables and page anchors.** One logical table = one Markdown table means pages 53, 54, 78 and 91–95
   have no anchor of their own; a citation of those pages resolves to the anchor of the page where the table starts.
   This is the price of the spec rule (D4/§3) and is the main term in `pages_with_missing_gt3`.
3. **`verify.py` re-normalises the PDF side with the per-page superscript evidence**, so the 12 exponents that this
   profile converts from the document-level `/plant` rule (paragraphs rejoined across a page break) count as missing
   tokens. The output values were checked against the PDF individually.
4. **Table 5-2 came from the main JSON, not from the struct tree.** The review expected a manual rewrite because the
   struct-tree version is misaligned; in the current conversion the main JSON carries the correct row/column spans
   and the core fill-down makes each row self-contained, so the table is assembled from those cells and checked
   cell by cell against the rendered p69. The result is the matrix the review asks for (Layer 5 shares the Layer 4
   guidelines, the Overall Guidelines columns repeat on all five rows).
5. **`(Sheet n of m)` / `continued` handling is not needed** for this document (no sheet captions), and
   `--include-header-footer` / `--content-safety-off off-page` remain unnecessary (review §5.1b).
