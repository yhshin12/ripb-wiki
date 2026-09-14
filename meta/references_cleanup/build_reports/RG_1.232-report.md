# RG_1.232 — refclean document profile report (Task 10)

**Status: DONE_WITH_CONCERNS.** Every dispatch item and every H-severity finding of `review_rg.md` is implemented and
checked against the PDF. The concerns are (i) two page-boundary paragraph joins that the source layout leaves
ambiguous, (ii) one defect found in a frozen core module (`tables._cell_text`), and (iii) a per-page artefact of the
verifier that follows from emitting Table 1 as one Markdown table. All three are described in §6.

Document: U.S. NRC Regulatory Guide 1.232, Rev. 0, April 2018, "Guidance for Developing Principal Design Criteria for
Non-Light-Water Reactors" (133 pp., 109 of them `/Rotate 90`, untagged, no outline).

Files created (ownership per brief):

| File | Contents |
|---|---|
| `scripts/refclean/profiles/rg1232.py` | 14 ordered steps + `metadata()`; explicit lists for footnotes, hyphens, joins and the outline, each taken from `review_rg.md` and re-checked on the PDF |
| `scripts/refclean/patches/RG_1.232.json` | `[]` — no manual (class C) item remained; every fix is a rule or a PDF-verified fixed list inside the module |
| `scripts/refclean/tests/test_rg1232.py` | 32 tests: 22 unit tests on the pure text rules + 10 checks on the real document (build ≈ 3 s, session-scoped fixture) |

Regenerated: `references/RG_1.232.md` (4,363 lines, 369,255 B, 153 page anchors), `references/raw/_verify/RG_1.232.json`.
No figure PNGs: the only raster in the PDF is the decorative NRC seal on the cover (no caption), which is dropped;
`figures: []` in the frontmatter.

## 1. Text sources and why

The converter JSON alone cannot carry this document: Table 1's redline is colour-coded, the appendix criterion titles
are italic runs inside a glued cell string, and the appendix paragraph structure is expressed by empty lines that the
converter collapses. The profile therefore uses three sources:

| Source | Used for |
|---|---|
| opendataloader JSON element stream | all running text (pp. 1–29, 62, 104–105), table geometry (cell boxes, row/column numbers), and as the word-level reference for every rebuilt cell |
| PyMuPDF spans **inside the JSON cell boxes**, character by character | Table 1 cells (colour → `~~deleted~~` / `<ins>inserted</ins>`), Appendix A–C cells (italic title, empty-line paragraph structure, line-end hyphens, GDC 19 emphasis), acronym columns (x = 72 / x = 144), page labels from the footers |
| raw md `~~…~~` (`detect_strikethrough`) | cross-check only: the red spans found in the PDF must equal the converter's strikethrough marks, per cell |

Character-level assignment is required: single PDF spans cross cell borders (e.g. p13 row 11, one span holds the GDC
title *and* the ARDC title; p20 row 76 likewise), so span-level clipping puts text in the wrong column.

Every rebuilt cell is compared with the JSON cell text at word level (hyphens, punctuation and case ignored).
**The final run reports 0 differences** over the 178 criteria, the 65 crosswalk rows and the acronym table
(`doc.meta['rg_stats']['warnings'] == []`).

## 2. Steps in `rg1232.steps()` (run order)

| Step | What it does | Evidence |
|---|---|---|
| `page_labels` | Printed page labels from the PDF footers (the JSON has no footer elements for this conversion): `RG 1.232, Rev. 0, Page n` and `Appendix X to RG 1.232, Rev. 0, Page X-n`. p1 (cover, unnumbered) = `1`; p105 prints `Page B-2` (source error) and is anchored `C-2`, recorded in `page_label_notes`. | p2–p133 footers |
| `cover` | p1 masthead (`U.S. NUCLEAR REGULATORY COMMISSION`, `REGULATORY GUIDE 1.232, REVISION 0`, `Issue Date: April 2018 Technical Lead: Jan Mazza`) and the seal image → frontmatter; the two cover-box paragraphs → `doc.meta` for the closing section; the four ADAMS numbers are parsed out of the box text. | p1 (render) |
| `drop_toc_and_residue` | `S.drop_toc` (p4); removes the one footer line that the header/footer filter passed because it is misprinted (`Appendix B to RG 1.232, Rev. 0, Page B-2` on p105, review F18) — asserted to match exactly once. | p4, p105 |
| `footnotes` | Lifts the 14 footnote bodies (9 pt, leading number, expected page) out of the stream and replaces the 14 glued marks from review §1.2 with `[^n]` — each anchor must occur exactly once on its page, otherwise the build fails. | pp. 1, 7, 8, 11, 21, 25–28, 62, 104 |
| `body_structure` | The two reading-order swaps (`Purpose` ↔ `A. INTRODUCTION`, `Reason for Issuance` ↔ `B. DISCUSSION`); `•`/`o` glyphs → list items at depth 0/1; `S.join_breaks` for lower-case page-break continuations; 6 explicit joins (review F14/F04, incl. `INL/EXT-` + `10-17997`); `Background` + `The NRC Regulatory Framework` split into two headings; the two buried headings extracted; the Appendix B column list split into three items (F24). Each anchor must match, otherwise the build fails. | pp. 1–2, 5–6, 8–9, 21–22, 27–28, 62 |
| `headings` | Assigns the §4 outline (31 headings, page + text + level) and demotes every other converter heading (only `TRISO tristructural isotropic fuel`, which becomes an acronym-table row). The emitted heading list must equal the outline **in order**. | review §4 |
| `normalise` | Entities, whitespace, the explicit hyphen list, `$` escape — converter text only (rebuilt PDF text keeps its own hyphens). | review §1.3 |
| `crosswalk` | The 10 page tables of Table 1 → one Markdown table, 65 rows, columns `Section \| Criterion \| GDC title \| ARDC title \| ARDC status \| SFR-DC title \| SFR-DC status \| MHTGR-DC title \| MHTGR-DC status`; red → `~~…~~`, blue `#1f497c` → `<ins>…</ins>`; title/status split by the printed status phrases; caption `TABLE 1: NON-LIGHT-WATER-REACTOR CROSSWALK` restored as an H4. | pp. 13–20 |
| `appendix_records` | The 123 appendix page tables → 20 section headings + 178 criterion records (D6 layout, review §5.1): title from the leading italic run, status line by regex (incl. SFR-DC 18, whose status line is italic too), body and rationale as paragraphs, continuation rows merged. | pp. 30–61, 63–103, 106–133 |
| `acronyms` | 42 entries from the PDF tab columns (acronym x = 72, expansion x = 144; the wrapped FAUNA expansion is rejoined) → one two-column table. | pp. 23–24 |
| `references` | The 39 numbered entries → an ordered list with `^ref-n` block ids, one block per PDF page so the page anchors stay correct. | pp. 25–28 |
| `place_footnotes` | `[^n]:` definitions at the end of the section that contains the mark (before the next heading of any level), in number order; each definition keeps the page of its printed body. | — |
| `document_information` | `## Document information` + the two cover-box paragraphs verbatim (review §5.2 rule 2). | p1 |
| `finish` | Guards: every heading has a level 1–6, no `table`/`image`/`hdr` element survives, leading `-`/`*`/`n.` in paragraphs escaped; writes `doc.meta['rg_stats']` (counts, joins, hyphen audit, warnings) and closes the PDF. | — |

## 3. Dispatch items — result

| # | Item | Result |
|---|---|---|
| 1 | Frontmatter per §5.3; cover box in a closing section | Done: `doc_id: RG 1.232`, `revision: 0`, `issue_date: 2018-04`, `adams_accession: ML17325A611`, `related_adams` (3), `criteria_sets` (55/65/58/65), `page_labels` = `p1-28 = 1..27; p29-61 = A-1..A-33; p62-103 = B-1..B-42; p104-133 = C-1..C-30` plus `page_label_notes` for the two source numbering errors. `## Document information` holds both cover-box paragraphs verbatim. |
| 2 | Heading tree per §4 | Done: 1 H1 (title), 10 H2 (`A.`–`D.`, ACRONYMS, REFERENCES, three appendices, Document information), 33 H3, 187 H4, 356 H5. Both order swaps fixed, `REFERENCES[^7]` fixed, the 4 buried/flattened headings extracted (`Background`, `The NRC Regulatory Framework`, `NRC Policy on Advanced Reactors`, `Key Assumptions and Clarifications…`), the 5 spurious headings removed (3 masthead lines, footnote 3, `TRISO …`), Table 1 caption restored. |
| 3 | 14 footnotes `[^n]` + definitions; broken sentences rejoined | Done: each `[^n]` occurs exactly twice (mark + definition); `10 CFR 50.34[^2] states`, `(Ref. 2)[^1].`, `PDC[^4]`, `…S0306454915005800[^12].`; none of `10 CFR 50.342`, `PDC4.`, `REFERENCES7`, `available.3`, `(Ref. 2)1.` remains. The 5 sentences that the inserted footnote bodies had cut (pp. 1–2, 8–9, 21–22, 27–28, 104–105) are rejoined. |
| 4 | Line-end hyphens from the review list only | Done: 28 patterns, each with PDF line-end evidence (test `test_hyphen_list_has_pdf_evidence` checks each against the PyMuPDF hyphen map). Restored in converter text (e.g. `SECY-15-0002`, `www.gen-4.org`, `NPTDS-mexico`, `non-LWR`, `technologies—specifically`, `INL/EXT-10-17997`) and kept automatically in the PDF-rebuilt cells (audit: 45 joins, all in the review list, `hyphen_joins_unlisted: {}`). `watercooled`, `fire- resistant`, `SFR-DC17` remain as printed. |
| 5 | Table 1 crosswalk: one table, 9 columns, redline, caption | Done: 65 rows; 29 cells carry redline (33 `~~…~~` groups, 23 `<ins>…</ins>`), which is exactly the review §1.1 list; the red words equal the converter's `~~…~~` marks cell by cell (0 mismatches); the 11 previously lost spans (e.g. MHTGR-DC 34 `Modified`, MHTGR-DC 72 final period) are present. |
| 6 | D6 records for Appendices A/B/C | Done: 55 + 65 + 58 = 178 records under 20 `### Appendix X — Section …` headings, each `#### SET n — Title` + `- **ID/Aliases/GDC counterpart/Title/Status/Source**` + `##### Criterion text` + `##### NRC rationale for adaption(s) to GDC` (`(none in source)` in 41 records). 92 continuation fragments merged: 62 mid-sentence (one space), 28 at a paragraph boundary (blank line), 2 ambiguous (see §5). Title/status/body separated in all 178. |
| 7 | Acronyms, references, GDC-19 italics, Appendix-C footer residue | Done: 42-row `Acronym \| Definition` table; 39-entry ordered list with `^ref-n` anchors (Ref. 34/37/38 repaired); the GDC 19 "(with emphasis added)" italics restored in all three appendices (`*actions can be taken*`, `*safely*`, `*controls*`, `*have certain knowledge*`, `*make decisions*` — 5 runs × 3); the misprinted p105 footer removed. |

## 4. Review findings — coverage

| Finding | Result |
|---|---|
| F01 redline (29 cells) | Fixed from the PDF colours; cross-checked against the converter `~~…~~` marks. |
| F02 20 lost spans / 16 cells | Present (re-conversion) and confirmed cell by cell by the word-level diff (0 differences). |
| F03 14 footnote marks | Fixed (explicit list only). |
| F04/F05 hyphens (21 identifiers + 45 words + em dash + 2 INL splits) | Fixed from the review list; `watercooled`, `fire- resistant`, `SFR-DC17` kept. |
| F06 123 blocks, 73 continuation rows, 62 split criteria | Fixed: records; continuation rows merged with the sentence/paragraph rule. |
| F07 title/status/body glued (178 + 81 cells) | Fixed: italic run → title, status regex, remainder → body; Table 1 title/status split into two columns. |
| F08 paragraph structure lost in cells | Fixed: paragraphs rebuilt from the PDF empty lines / line gaps, not from the converter's `<br><br>`. |
| F09 14 footnote bodies inside sentences | Fixed: bodies moved to `[^n]:` definitions at the end of the enclosing section. |
| F10/F11 heading defects (spurious 5, order 2, buried 4, caption 1, 27 section titles, 178 criterion headings) | Fixed (§4 outline + record headings). |
| F12 cover | Fixed: masthead → frontmatter, box → closing section. |
| F13 TOC | Dropped. |
| F14 13 split paragraphs | Fixed (generic join + 6 explicit joins). |
| F15 raw bullets / flattened sub-bullets | Fixed: `•` → depth 0, `o` → depth 1. |
| F16 42 acronyms in two paragraphs | Fixed: two-column table from the PDF tab columns. |
| F17 references | Fixed: ordered list, `^ref-n`, entries 34/37/38 repaired. |
| F18 p105 footer residue | Removed. |
| F19 Table 1 caption | Restored once, as an H4. |
| F20 frontmatter / page anchors | Done (153 anchors, 4 page-label schemes). |
| F21 GDC 19 emphasis | Restored (D7). |
| F22 other italics, F23 bare URLs | Not restored (D7 allows only the redline, GDC 19 emphasis and ch1 bold); URLs left bare — the review rates both L/optional. |
| F24 Appendix B column list | Split into three items. |
| F25 source spellings | Kept and asserted in the tests (`(Criterion 1 – 15)`, `SFR-DFC`, `SARRDLS`, `August 2017 2017`, `Section VII—Additional SFR-DC (Criteria 70–77)`, `VI. Fuel and Reactivity Control`, `Adaption`/`Adaptions`, the duplicate footnotes). |

## 5. Verification

`python scripts/clean_references.py --only RG_1.232 --verify` (final run, figures enabled):

| Metric | Value |
|---|---|
| pdf_tokens / missing_tokens | 45,469 / 406 (**0.89 %**) |
| residue (dot leader, entity, `[[`, running header, DOE footer, sheet heading, `x10-`, `<br>`) | 0 |
| failed patches / unmatched headings / orphan captions | 0 / 0 / 0 |
| pages_with_missing_gt3 | 52 (artefact, see below) |
| profile self-checks (`rg_stats.warnings`) | 0 |
| tests | `pytest scripts/refclean/tests -q` → 163 passed (32 of them this document's) |

`headings_whitelist 0 / headings_emitted 0` is expected: `build_aux(chapter=None)` leaves `aux.headings` empty and the
verifier counts only that list; this profile carries its own outline and asserts it itself.

**The 406 missing tokens, in full (no page-level token is unexplained):**

| Count | Cause |
|---:|---|
| 224 | repeated table headers and page-footer words: `Criterion`, `… Title and Content`, `NRC Rationale for Adaption(s) to GDC` on each of the 133 table pages, and `RG 1.232, Rev. 0, Page …` where the footer sits inside the body band (`content` 113, `page` 69, `sfr`/`dc`/`current`/`and`/`title`/`status` …). The output keeps one header per logical table (the record layout) and the page label in the anchor. |
| 97 | line-end hyphen restorations: the PDF text layer splits `non-` + `LWR`, `SFR-` + `DC17`, `pre-` + `application`, `leak-` + `tightness`, `INL/EXT-` + `10-17997`, so the token bag holds two tokens where the output correctly holds one (`non` 21, `lwr` 16, `dc17` 7, …). |
| 72 | section labels repeated on every page of a multi-page table (`II. Multiple Barriers` ×10, `IV. Fluid Systems` …); each section is kept once, as an H3. |
| 8 | footnote marks detached from their token (`50.342` → `50.34[^2]`, `PDC4.` → `PDC[^4].`, `designs.13` → `designs.[^13]`, …). |
| 5 | the `o` glyph of the second-level bullets, converted to Markdown nesting. |

**pages_with_missing_gt3 = 52** is a page-anchor artefact, not lost text:

- pp. 15–20 (six pages, 116–278 tokens each) hold the middle of Table 1. The dispatch requires one Markdown table,
  and a Markdown table cannot contain a page-anchor comment, so the whole table is anchored on p13; the verifier's
  ±1-page window cannot find those rows. The tokens are present (the global `missing_tokens` is 406 in total).
- The remaining ~46 pages miss 4–17 tokens each; after excluding the repeated header/section/footer tokens, what is
  left is the hyphen and footnote classes above plus text that was deliberately merged into a paragraph anchored on
  the previous page (mid-sentence continuations). A re-run of the per-page check ignoring the repeated header and
  section tokens leaves 14 pages: the six Table 1 pages and eight pages with 4–5 tokens, all of them hyphen or
  footnote artefacts.

Content checks in the tests: 178 criteria with non-empty text and a status field; SFR-DC 4 carries the
"Chemical consequences of accidents…" paragraph as its own paragraph (page-boundary blank line honoured);
SFR-DC 11's sentence runs continuously across the p65/p66 break; 14 footnotes; Table 1 row 14 redline in all three
columns; 20 appendix section headings; 42 acronyms; 39 references; 3 × GDC 19 emphasis; heading order.

## 6. Concerns and open items

1. **Two ambiguous paragraph joins (source layout gives no evidence).** SFR-DC 77 rationale (p99→p100) and
   MHTGR-DC 61 rationale (p131→p132) end a sentence exactly at the page break with no empty line at the bottom of the
   first cell and none at the top of the second. They are emitted as one continuous paragraph. The same sentence
   appears elsewhere in the document both as its own paragraph (ARDC 43, SFR-DC 46) and mid-paragraph (ARDC 46), so
   neither reading can be proved from the source; word content is unaffected. All other 90 page-boundary fragments
   have positive evidence (62 mid-sentence, 28 with an empty line on one side).
2. **Core defect found — `refclean/tables.py::_cell_text` drops text.** It reads a cell's `kids`, and for a `list`
   kid only the `content` of each list item; a list item's own `kids` (nested paragraphs) are ignored. In this PDF
   that loses a whole rationale paragraph in three cells (ARDC 26 p41, SFR-DC 26 p76, MHTGR-DC 26 p121:
   "The term “independent and diverse” indicates …"). This profile does not use `from_odl` for text, so the output is
   complete, but other documents that keep converter table cells are affected. Suggested patch (not applied — core is
   frozen):

   ```python
   # scripts/refclean/tables.py
   def _cell_text(cell):
       parts, bold = [], []

       def walk(node):
           t = (node.get("content") or "").strip()
           if t:
               parts.append(t)
               bold.append("Bold" in (node.get("font") or ""))
           for kid in node.get("kids", []) or []:
               walk(kid)
           for it in node.get("list items", []) or []:
               walk(it)

       for kid in cell.get("kids", []) or []:
           walk(kid)
       return "\n".join(parts), bool(bold) and all(bold)
   ```

   (The only behaviour change is that nested paragraphs are no longer lost; flat cells render identically.)
3. **Page anchors inside records are not monotonic.** A criterion record prints the criterion text (pages N…N+k) and
   then the rationale, which starts again on page N. The anchors follow the printed text, so `<!-- page N -->` can
   reappear after `<!-- page N+k -->`. This keeps citations exact (`RG 1.232, p. B-13`) at the cost of a non-monotonic
   anchor sequence; the verifier's per-page window is the only consumer that minds.
4. **`Background` subheading depth is a judgement call** (review §6 lists it as class C): the seven subheadings under
   `Background` and `The NRC Regulatory Framework` print in the same face (TNR Bold 11 pt) as `Background` itself. The
   review's intended outline treats them as children, and that is what is emitted (H4 under an H3).
5. **Appendix heading wording.** The body headings keep their printed capitals (`A. INTRODUCTION`); the appendix
   headings use the table-of-contents wording (`Appendix A. Advanced Reactor Design Criteria`) instead of the
   two-line cover form (`APPENDIX A` / `ADVANCED REACTOR DESIGN CRITERIA`), as proposed in review §4. Both spellings
   are source text.
6. **`Aliases: SFRDC n`** is emitted only for Appendix B, to match the vault's note names (`wiki/SFRDC_n.md`). It is
   the only generated string in a record; everything else is source text or a field label.

## 7. Reproduce

```
python C:\Obsidian\ripb\scripts\clean_references.py --only RG_1.232 --verify
python -m pytest C:\Obsidian\ripb\scripts\refclean\tests\test_rg1232.py -q
```

Build time ≈ 3 s (133 pages, character-level span extraction on the 123 table pages).
