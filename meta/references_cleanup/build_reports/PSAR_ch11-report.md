# PSAR ch11 (Conduct of Operations) — cleanup profile report

- Document: `references/raw/TP_Natrium_PSAR2025_ch11_Conduct of Operations.pdf` (77 pages), key `PSAR_ch11`
- Output: `references/TP_Natrium_PSAR2025_ch11_Conduct of Operations.md` (1,394 lines, 148,758 chars) + `references/figures/PSAR_ch11/Fig_11.1-1…-4.png`
- Build: `python C:\Obsidian\ripb\scripts\clean_references.py --only PSAR_ch11 --verify` (final run with figures)
- Files created (ownership per agent brief): `scripts/refclean/profiles/psar_ch11.py`, `scripts/refclean/tests/test_psar_ch11.py`. No patch file: every fix is expressible as a rule, so `patches/PSAR_ch11.json` is not needed (no class C items).
- Spec: `meta/references_cleanup/cleanup_review_2026-09-11.md` (D1–D7), `meta/references_cleanup/file_reviews/review_ch11.md` (§1, §4, §5).

## 1. Verification summary

| Quantity | Value |
|---|---|
| `unmatched_headings` / `unmatched_subheads` / `orphan_captions` / `failed_patches` | 0 / 0 / 0 / 0 |
| Heading whitelist vs emitted | 127 / 127 (all PDF-derived since the 2026-09-13 core patch) |
| PDF tokens | 20,417 |
| Missing tokens | 237 (1.16 %), all attributable to intended deletions (§4) |
| Residue checks (dot leaders, entities, `[[`, running header, DOE footer, sheet headings, `x10-n`, `<br>`) | 0 |
| Pages with > 3 missing tokens | 6 (§4) |
| Tests `scripts/refclean/tests/test_psar_ch11.py` | 19 passed |
| Full suite `scripts/refclean/tests` | 186 passed, 6 failed (all in `test_psar_ch05.py` / `test_psar_ch07.py`, other agents' files, unrelated to ch11) |

Output structure: 149 Markdown headings (127 numbered sections H2–H5, 1 chapter title H1, 4 figure captions, 4 table captions, 5 `References (11.x)`, 8 unnumbered subheadings), 60 page anchors (2 of them page-range anchors for the merged tables), 1 withheld callout, 4 figure PNGs (200 dpi), 4 logical tables in 4 Markdown tables.

## 2. Steps implemented (`profiles/psar_ch11.py`, `STEPS` in order)

All steps are PDF-guarded: an expected anchor that is not found is recorded in `doc.meta['ch11_warnings']` instead of changing text silently; the tests assert that the list is empty.

1. `drop_noise` — deletes the `LIST OF TABLES` / `LIST OF FIGURES` titles left on p4–5 after `drop_toc` removed their dot-leader entries (D4), and punctuation-only paragraphs. The latter removes the 7.0 pt "." in the right margin of p67 (review §1 #22), which had also split Table 11.5-1 into two table elements.
2. `add_missing_headings` — 5 numbered headings that the core whitelist misses: 11.2.1.4 (p23), 11.2.2.2.4, 11.2.2.2.5, 11.2.2.3 (p35), 11.2.6.2.1 (p40). Cause: `pdfaux.build_aux` takes the modal line `x0` of a page as the body margin; on these pages the list indent (90/108 pt) is modal, so the heading lines at 72 pt fail the margin test. Each title is verified against a PDF line at `x0 = 72 ± 2` before `structure.promote_headings` runs, and the refs are appended to `aux.headings` in document order so `--verify` reports the full whitelist (127).
3. `bold_subheads` — `Design Changes` (p28, Arial-Bold line, review §1 #6) becomes an unnumbered subheading; `psar.assign_levels` puts it at H5 under 11.2.1.9.
4. `split_glued_references` — the `References` heading glued to the end of the last paragraph of 11.5 (p66) and 11.6 (p77); the entries that follow are re-typed as list items (`structure.references_as_items`). `assign_levels` renames them `References (11.5)` / `References (11.6)`.
5. `split_merged_paragraphs` — splits paragraphs the converter merged, using PDF paragraph starts: a PyMuPDF line that starts a block or follows a > 6 pt vertical gap starts a paragraph; its **full first line** (≥ 4 words) is searched inside body paragraphs and accepted only after sentence-final punctuation. 8 splits: §11.3 intro 1 → 4 paragraphs (p51), 11.3.1 (`…scalable PEP EPZ size.` | `The key elements …`), 11.3.5.2 (p55), 11.6.2 Meteorology 1 → 3 and Hydrology 1 → 2 (p76). The full-line (not n-word) needle is what keeps `The executive responsible for project execution is responsible for …` (p7) from being split mid-paragraph.
6. `list_markers` — strips the literal `- ` that PDF "-" sub-bullets carry into the item text (11.3.1, p52: `- - Emergency Response Performance …`), and converts the single `●` paragraph on p55 (11.3.5.1) into a list item.
7. `numbered_list` — rebuilds the 11.2.1.4 technical-elements list 1–12 (p23–25) as one `raw_md` ordered list. It removes the `- N.` double markers, nests the three bullets under item 7 and item 10's six paragraphs and two bullet lists (nesting from the ODL `x0`: numbers 90 pt, continuation paragraphs 108 pt, bullets 126 pt), and re-types item 12 (a paragraph in the ODL output). Page anchors for p24 and p25 are emitted **inside** the list at the current item indent so the list is not broken; the remaining body paragraphs of p25 are carried in the same block so that no anchor is emitted twice.
8. `table_11_2_2`, `table_11_5_1` — see §3.
9. `table_11_5_2_notes` — `NSS (1)` / `IAC (2)` and the two notes carry 7.7 pt markers in the PDF; they become `NSS<sup>(1)</sup>`, `IAC<sup>(2)</sup>` and `<sup>(1)</sup> …` per the table-note ruling.

## 3. Tables

Table 11.5-1 (7 sheets, p67–73) and Table 11.2-2 (4 sheets, p47–50) are rebuilt from the PDF: cell geometry from `fitz.Page.find_tables()` (pdfplumber's algorithm), text from PyMuPDF words. pdfplumber's own text layer is not used because it merges `10 CFR` into `10CFR` on p67 (also noted in review §2). Cell paragraphs are recovered from line spacing (1.7–1.8 pt inside a paragraph, ≥ 4.7 pt between paragraphs in these tables) and from bullet glyphs; a line-final hyphen joins without a space (`(post-` + `construction)` → `(post-construction)`, consistent with the core hyphen map).

- **Row 5.0 (review §1 #1, H).** The ODL output cut the spanning cell at the column rules into 12 rows × 3 columns with 14 words split mid-word and 3 letters doubled (`res|sponsibility`, `org|ganization`, `program|m`). It is now one row whose text matches the PDF word for word (`… • delineation of responsibility; • description of organization; … • programs and manuals, to include a setpoint control program consistent with Option B of TSTF-493; • reporting requirements, to include a COLR`).
- **All other rows checked.** Table 11.5-1 now has 14 rows (1.0, 2.0, 2.1, 2.2, 3.0, 3.1–3.7, 4.0, 5.0) and Table 11.2-2 19 rows. Both are asserted token-for-token against an independent extractor (PyMuPDF words clipped to the table bbox, all sheets, repeated sheet headers counted once) in the tests; Table 11.2-1 (core rendering, p46) and Table 11.5-2 (p74) are checked the same way.
- **Cell-internal structure (review §1 #16).** Paragraph boundaries inside a cell are marked with `; ` where a space would glue two units: `• reactor trip switchgear; The RPS, XIS, and RIS are described in Section 7.6.`, `• PSP leakage; The PHT is described in Section 7.1.3.`, `• intake/exhaust flow rates; The RAC is described in Section 7.2.1.`, `HF in Concept Design: identification of scenarios for analysis; HF in Preliminary Design: …`, `Verification; Validation`. Rule: `; ` before a bullet and after a paragraph that does not end with sentence-final punctuation, otherwise a space — an extension of the spec's "enumeration separators stay `; `", since `<br>` is not allowed in the output.
- **Spanning section rows (1.0–5.0).** The cell spans Section Name … Basis. Filling right would repeat up to 1,000 characters three times per row without adding information, so the printed title line goes to `Section Name` (1.0 `Use and Application`, 2.0 `Safety Limits`, 3.0 `Limiting Conditions for Operation and Surveillance Requirements`) and the spanning text is written once under `Variable or Condition`; rows 4.0 and 5.0 have no printed title line, so `Section Name` stays empty. This is the one deliberate deviation from "merged cells filled" (which the plan defines as fill-down/right); vertical fills are unchanged.
- **Table 11.2-2 double row (review §1 #16).** `11.2.5 / 11.2.1.10` share one cell pair with no rule between them; the ODL output produced the fictitious title `Design of the Human-system Interface Design Goals and Design Bases`. It is now two rows that share the NUREG-0711 cell (fill-down).
- Sheet captions and sheet merging come from the core (`hdr_to_captions`, `attach_captions_and_merge`); the 11 sheet captions of the two tables appear as one caption each, at the level of the owning section + 1.

## 4. Missing tokens (237 = 1.16 %; the 144/0.71 % figures below are from the pre-patch build, see §7)

Computed from `references/raw/_verify/PSAR_ch11.json` with a per-page attribution: **all 144 missing tokens occur on p4–5 (List of Tables / List of Figures) and p15–18 (vector org-chart labels)**; the residual after subtracting those pages is 0.

- p4–5 (≈ 20 tokens: `list`, `tables`, `11.2-28`, `11.5-10p`, `11.1-10`…): deleted by decision D4; the frontmatter `tables:`/`figures:` lists replace them.
- p15–18 (≈ 124 tokens: `manager` 22, `project` 7, `director` 7, `es`/`h`, `sciences`, …): the label text of Figures 11.1-1, -3, -4, deleted as vector debris by decision D3. The labels are present in the rendered PNGs, including the four that the converter lost on the `/Rotate 90` pages (checked in `Fig_11.1-3.png`: `Quality Control Manager`, `QC Personnel`; `Fig_11.1-4.png`: `Director of NOS`, `Quality Assurance Manager`). No table text and no body text is missing.
- `pages_with_missing_gt3` = 12: p4, p5, p15, p17, p18 (the deletions above) and p49, p50, p69–73. The latter are an artifact of merged sheets: the text of those sheets sits under the page anchor of the first sheet (p47 / p67), outside `verify`'s ±1-page window. Pages without an anchor are exactly p1–5 (deleted content) and p48–50, p68–73 (merged sheets); there are no duplicate anchors.
- Extra tokens (`top_extra`) are markup (`sup` 8 from the note markers, `withheld` 5, `psar`/`ch11`/`fig`/`figures` from the four image paths, `11.5`/`11.6` from the `References (11.x)` titles), the fill-down copy in Table 11.2-2, and table header rows: `verify.pdf_page_text` drops those on table pages (see §6).

## 5. Dispatch items

| # | Item | Status |
|---|---|---|
| 1 | Table 11.5-1 row 5.0 rebuilt from PDF cell text; every other row of 11.5-1 (7 sheets) and 11.2-2 (4 sheets) checked | Done (§3); token-for-token equality with PyMuPDF words asserted in the tests |
| 2 | Operating-mode definitions (Mode-1…Mode-4) and Table 11.5-2 compared with PDF p65–66 and p74 word by word | Done. `test_operating_mode_definitions_match_pdf_word_by_word` compares the whole 11.5.2.1–11.5.2.4 span as an ordered word sequence; the Mode-2 definition broken over the p65/p66 page break is joined (`… during a shutdown or downpower when reactor power is lowered …`). Table 11.5-2 rows and both notes are asserted verbatim, with `> 400 °F (204°C)` and `≤ 400 °F (204°C)` inside the table |
| 3 | §11.3 heading + 1,684-char intro, §11.3.10 mid-line, §11.4 withheld marker, 7 underlined subheadings, 2 glued `References`; split paragraphs the core left merged | Done. All 127 numbered headings are Markdown headings at the depth-derived level and in document order; the 8 unnumbered subheadings (`Objectives and Scope`, `Methodology`, `Design Changes`, and the five 11.6.2 site-characteristic subheadings) and 5 `References (11.x)` are headings. Longest non-table line is now 992 chars (was 2,889) |
| 4 | `##### .` and other stray marks, `&gt;` in Mode-3, false list items (17), `- N.` double markers | Done. No punctuation-only heading, no `&amp;`/`&gt;`, no `[[`, no `●`, no `- N.` or `- - ` markers; the 17 false list items of review §1 #8/#9 are paragraphs (or joined continuations) and are asserted as such |
| 5 | Keep review §5 do-not-fix items | Done. `Program Plant and Methodologies`, `NRSRT`, `Section 2.3.3 Based upon`, `responsibilities.The`, `through designated channels. for problems`, `Organization- TerraPower/USO` and Table 11.2-2 `11.2.2.2` are asserted present. `ChiefNuclear` no longer occurs: it was an org-chart label and is deleted with the figure debris (D3), so no judgement was needed |

Review §1 H-severity items: #1 (row 5.0) fixed; #2 (missing sheet captions) fixed by the core re-conversion plus `hdr_to_captions`; #3 and #4 (glued headings, subheadings, `References`) fixed.

## 6. Remaining issues and core observations

1. **Figure label transcription (review §1 #11–#13, M).** Not done — a class C item outside this dispatch. The org charts are PNGs (D3), so the 22 boxes of Figure 11.1-2 (raster only) and the vector labels of 11.1-1/-3/-4 are not searchable text. Review §3 holds transcription drafts if the corpus decision changes.
2. **Frontmatter `withheld` key.** Spec §3 lists `withheld[]`, but `profiles/psar.py::metadata` does not emit it and a chapter hook cannot add frontmatter keys. Core patch request: in `profiles/psar.py::metadata` add `"withheld": doc.meta.get("withheld", [])`, and in `structure.withheld_callouts` record the enclosing section and page range in `doc.meta['withheld']` (ch11 would then carry `11.4 Aircraft Impact Assessment (PDF p60–64, SRI)`).
3. **`pdfaux.header_footer_band` on table pages.** The function takes the lowest page-wide rule in the top quarter as the header rule; on table pages the table's own row borders qualify, so `verify.pdf_page_text` drops the table header row and the first data rows from the PDF token bag (visible as `section`, `design`, `hfe`, `ta` in `top_extra`). Suggested core patch: accept only rules with `y1 < 0.10 × page height` as the header rule (the running-header rule is at y ≈ 65 pt, the first table border at y ≈ 100 pt), or ignore rules inside a known table bbox. The effect on ch11 is limited to the extra-token list; the tables themselves are verified independently by the profile tests.
4. **Body-margin detection.** `build_aux` derives the body margin per page from the modal line `x0` of lines longer than 40 characters, which fails on pages that are mostly list content (ch11 p23, p35, p40 — the five headings of §2 item 2). A document-wide modal margin with the per-page value as fallback would be more robust; other chapters with list-heavy pages are likely affected the same way.
5. **Page anchors inside merged tables.** Sheets 2…n of a merged table carry no anchor (p48–50, p68–73). This follows from "one logical table = one Markdown table" and cannot be fixed without comments inside the table block; `verify` reports it as `pages_with_missing_gt3`.
6. **Test suite.** `scripts/refclean/tests/test_psar_ch05.py::test_real_lbe_counts_and_type_pairing` fails in the shared suite; it belongs to the ch05 profile owned by another agent and is unaffected by this work (`test_psar_ch11.py`: 16 passed).

## 7. Core patch follow-up (2026-09-13)

The core patches requested in §6 (and the ones requested by the other profile agents) were applied. Effects on ch11 and the adaptations made in `profiles/psar_ch11.py`:

| Core change | Effect on ch11 | Adaptation |
|---|---|---|
| `pdfaux.numbered_headings` accepts the page **or** the document margin and any block line | all 127 numbered headings are now found by the core (whitelist 122 → 127); the five headings on p23/p35/p40 no longer need local promotion | `add_missing_headings` (and its title table) removed; replaced by `check_expected_headings`, which warns if any of the five is not emitted exactly once. The 127-heading order/level test is unchanged |
| `pdfaux.is_toc_page` flags titled LoT/LoF pages with ≥ 2 leaders | p4–5 are TOC pages: their elements are dropped by the core and `verify` skips them (−130 PDF tokens on the missing side) | `drop_noise` keeps the `LIST OF TABLES` / `LIST OF FIGURES` guard (now redundant) and the stray-“.” rule (still required for p67) |
| `structure.hdr_to_captions` dedupes running titles | the withheld marker of §11.4, which the PDF prints on each of p60–64 and which arrives as `hdr` elements, was reduced to an arbitrary two callouts (p60, p61) | new step `withheld_section`: exactly one callout under the section heading, and the section with its PDF page range in `doc.meta['withheld']` → frontmatter `withheld: ["11.4 Aircraft Impact Assessment (PDF p60-64, SRI)"]` (review §1 #23). Asserted by `test_withheld_section_once_with_frontmatter_range` |
| `tables.cell_md` ENUM tightened (`\(?\d{1,2}[.)](?!\d)`) | Table 11.2-1 row 11 rendered `11.2.6.1 11.2.6.2 11.2.6.3`: three distinct section numbers joined by spaces | new step `section_number_cells`: a cell whose lines are each a bare `\d+(\.\d+)+` is an enumeration and is joined with `; ` in the cell text, so the rendering no longer depends on `tables.ENUM`. Row 11 reads `11.2.6.1; 11.2.6.2; 11.2.6.3` again |
| `emit.render` gives multi-page tables a range anchor, `verify` credits every page of the range | `<!-- page 47-50 \| 11.2-29..11.2-32 -->` and `<!-- page 67-73 \| 11.5-3..11.5-9 -->`; the sheet pages are no longer reported as missing (12 → 6 pages with > 3 missing tokens) | new test `test_merged_tables_get_a_page_range_anchor`; §6 item 5 of this report is resolved |
| `profiles/psar.metadata` emits `withheld` from `doc.meta['withheld']` | frontmatter key available | filled by `withheld_section` (§6 item 2 resolved) |
| build report prints `*_warnings` / `*_qa` | — | new step `qa_metrics` publishes `ch11_qa` = `{section_number_cells: 1, paragraph_splits: 8, numbered_headings: 127, 11.2-2_rows: 19, 11.5-1_rows: 14, withheld: [...]}`; asserted in `test_no_warnings_no_failed_patches` |
| `tables._cell_text` recursive, `underlined_subheads` union, `hyphen_map` by column, `insert_subheads` punctuation guards, `fix_false_items` document margin, `attach_captions_and_merge` later-page rule, `drop_stray_footers`, `header_footer_band` 14 %/86 % | no change to the ch11 output other than the rows above (diff against the pre-patch build: only the four items listed here) | none |

**Answer to the open question (Table 11.2-1 `Section #` cell).** Three bare section numbers on three separate PDF lines are an enumeration, so `; ` is the intended separator (plan §3). It is handled in the profile, which is enough for ch11. A core rule would still be worth having, because the same pattern appears wherever a table lists several section numbers in one cell: extend `tables.ENUM` (or `cell_md`) so that a **whole line** matching `^\d+(?:\.\d+)+$` counts as an enumerator. That is narrow (a bare dotted number is never a wrapped sentence fragment) and would make `section_number_cells` redundant without changing its result; the profile step writes the joined text into the cell, so it is idempotent either way.

**Verification after the follow-up** (final run with figures, `--only PSAR_ch11 --verify`): 127/127 headings, residue 0, no warnings, no failed patches, missing 237 tokens = 1.16 % of 20,417, `pages_with_missing_gt3` = 6 (p15, p17, p18, p62, p63, p64). The missing tokens decompose exactly:

| Cause | Tokens | Intended |
|---|---|---|
| Figure label text on p15–18 (vector debris, rendered as PNG) | 133 | yes (D3) |
| Repeated sheet header rows of Tables 11.5-1 (6×) and 11.2-2 (3×), dropped on merge | 61 | yes (spec §3 “repeated header rows deleted”) |
| Withheld marker repeated on p61–64 (kept once, range in the frontmatter) | 42 | yes (review §1 #23) |
| `post` from the line-break hyphen in `Design Implementation (post-construction)` | 1 | verify-side artifact; the output keeps the hyphenated form |
| **Total** | **237** | |

The PDF token count rose from 20,287 to 20,417 because the new `header_footer_band` no longer treats table row borders as the running-header rule, so table header rows are counted on the PDF side; the LoT/LoF pages left the count at the same time. `top_extra` now contains `page` (59×) because `verify` counts the page-anchor comments as output tokens — cosmetic only.
