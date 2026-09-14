# PSAR_ch07 report — Kemmerer Unit 1 PSAR Chapter 7, Descriptions for Safety-Significant SSCs (Task 9e)

Status: DONE_WITH_CONCERNS. Every dispatch item and every H item of the three reviews is fixed and verified
against the PDF; the concerns are core-side defects that the module works around (§5) and three M items that were
deliberately not restored (§4).

Files created (ownership per brief): `scripts/refclean/profiles/psar_ch07.py` (14 steps),
`scripts/refclean/patches/PSAR_ch07.json` (8 manual class-C items), `scripts/refclean/tests/test_psar_ch07.py`
(4 unit tests on synthetic input, 8 PDF-level tests of the rebuilt tables, 7 checks of the built document).
Regenerated: `references/TP_Natrium_PSAR2025_ch7_Descriptions for Safety-Significant SSCs.md` (7,085 lines,
830 KB), `references/figures/PSAR_ch07/*.png` (43 PNGs, 18 MB), `references/raw/_verify/PSAR_ch07.json`.
No core module was modified.

## 1. Steps in `psar_ch07.STEPS` (run order)

| Step | What it does | Evidence (PDF) | Review item |
|---|---|---|---|
| `missing_headings` | Promotes the 7 numbered sections the core whitelist dropped (7.2.3.2.2 p122, 7.2.4.2.2 p138, 7.3.2.1.2 p182, 7.3.2.1.3 p183, 7.6.2 and 7.6.2.1 p251, 7.6.5.2.1 p295). Cause: `aux.body_x0[page]` is the modal x0 of long lines, which on table/bullet-dominated pages is the support column (314 pt), not the 72 pt body margin; the step uses the chapter-wide margin instead and appends the refs to `aux.headings` so the verifier's whitelist stays complete. | p122, 138, 182, 183, 251, 295 | ch7a #5, ch7b #2 (H), ch7c #5 |
| `missing_subheads` | Re-runs the underline detection with the union of **all** rule segments under a span and inserts the 26 underlined subheadings the core missed (p11 `Compressive Assembly`, p108 ×2, p204 ×4, p205, p207, p230 ×3, p231, p278, p301, p338, p340, p346 ×2, p347 ×2, p356, p357, p366 ×3). Figure boxes, ODL table boxes and the DL-table regions are excluded. | p11 (underline = 3 abutting rects 72–136, 136–146, 146–186 pt) | ch7a #6, ch7b #3, ch7c #6 |
| `misplaced_subheads` | Moves the 2 subheadings `structure.insert_subheads` attached to the wrong occurrence (`…divided into four subsystems: **Spent Fuel Pool** (SFP), …` p164; `…six major components; **In-Vessel Transfer Machine** (IVTM), …` p203). The wrong split is undone and the heading re-inserted where the subheading text is followed by the PDF line that follows the underlined line. | p164, p203 | ch7b §4.3 |
| `dl_tables` | **Rebuilds the 27 borderless `Function ID / Function Description / <SYS> Functional Support` tables (167 rows)** from PyMuPDF word positions: column boundaries from the underlined header (`Function` ID, `Function` Description, third header x0), rows start at a `DL\d-` token in column 1, the table ends at the first column-1 line that is not an ID, at a > 30 pt gap or at the footer band. Page-split sheets are merged (RCC 14–15, RES 31–32, SCG 122–123, SPS 138–139, FHP 168–169, FHE 188–189, UMC 255–256, RPS 268–270, XIS 283–284, RIS 295–296) and the repeated header rows dropped; a support cell that spans rows is filled down (NDC/NUP, 12 rows). The prose remnants are deleted by bbox and the table is inserted after the last element above it on its first page (this is what moves the RMS table back under 7.6.6.2.1). | pp. 14–356, all 38 page segments | ch7a #4 (H), ch7b #1 (H), ch7c #1–#4 (H) |
| `nested_nic_items` | The 21 NIC sub-system sub-bullets printed with `-` under a `●` item (`- - Gaseous Radwaste …`) lose the printed dash and nest one level under their parent. | p251–252 | ch7c #12 |
| `glyph_bullets` | Paragraph text that still carries `●` becomes list items (`● IEEE 603-2018 ● IEEE 379-2014 ● IEEE 384-2018` p298 → 3 items; p322/323 2 items). | p298, p322, p323 | ch7c #17 |
| `numbered_items` | The two `- 1. / - 2. / - 3.` runs become ordered Markdown lists. | p42 (Table 7.1.2-1 Note 1), p361 | ch7a #25, ch7c #20 |
| `table_notes` | Table-note markers as `<sup>*</sup>` / `<sup>**</sup>` in the header cells, the 21 `SR*`/`NSRST*` cells and at the start of the notes, so `* Classification …` is no longer parsed as a nested list and the marker keeps its meaning. 24 cells in Tables 7.1.2-4, 7.1.3-6, 7.2.3-1, 7.2.4-1. | p45, p77, p130, p146 | ch7a #17, #21; ch7b #9 |
| `group_rows` | Table 7.2.3-1: the two group rows (`Primary SCG`, `Intermediate SCG`) become a leading `Subsystem` column (23 rows), instead of a bogus second header row (`Component: Primary SCG`). | p130 | ch7a #18 |
| `subscripts` | `keff` → `k<sub>eff</sub>` (p187; the only symbol subscript in the chapter — `B4C` on p191 is printed at full size and stays as it is). | p187 spans (7.68 pt, lower baseline) | ch7b #15 |
| `registered_space` | `GT STRUDL®Version 40` → `GT STRUDL® Version 40` (the superscript `® ` carries the space in the PDF). | p370 | ch7c #17 |
| `pdf_paragraphs` | Re-aligns paragraph boundaries with the PDF: **34 joins** (a paragraph whose first PDF line is a continuation line, e.g. `… discussed in Section 7.6.5.3.1 through` + `Section 7.6.5.3.4. The following industry codes …`) and **176 splits** (a PDF paragraph start inside one element, with the text before it ending in the line above that start: RG title + conformance paragraph, run-in titles, `● Post-Construction … Chapter 12` + `Seismic classifications …` p309). Both directions need PDF evidence on both sides of the cut, so no boundary is invented. | whole chapter (line gaps: 1.8 pt inside a paragraph, ≥ 12.7 pt between) | ch7a #7–#8, ch7b #4–#5, ch7c #7–#8 |
| `standalone_subheads` | 4 title lines that are **not** underlined in the PDF but are siblings of underlined subheadings become subheadings: p169 `Structural Support (SR) – Load Path for SR SSCs`, `Temporary Load Path for SR SSCs (NSRST)`, `External Hazard Protection` (all three underlined in the FHE section, p189), p231 `NI Contol Building HVAC` (the other three HVAC titles on p230–231 are underlined). Class C. | p169, p231 (renders) | ch7b §4.3 |
| `references_headings` | 8 `References` / `Reference` labels left inside a paragraph or list item become headings and their entries become list items (`assign_levels` then names them `References (7.x.y)`); 28 References headings in total. | p18, p129, p261, p318, p342, p362, … | ch7a #6, ch7b #14, ch7c #19 |

`doc.meta` carries the QA payload: `dl_tables` (per table: pages, header, ID list, removed elements, both
token-coverage checks), `ch07_added_headings`, `ch07_added_subheads`, `ch07_moved_subheads`,
`ch07_para_joins`, `ch07_para_splits`, `ch07_reference_headings`.

## 2. DL-function tables — QA

* 27 tables / 167 rows = review counts (ch7a 7/41, ch7b 8/49, ch7c 12/77). The ID list of every table equals the
  expected list of review_ch7c §5.1 and the ch7a/ch7b table logs (test `test_dl_table_ids_match_the_reviews`).
* Text conservation, computed per table during the run: the 311 removed prose elements contain **0** tokens that
  are not in the rebuilt table, and the tables contain **0** tokens that were not in the removed elements
  (the NDC/NUP table is exempt from the second direction because its shared support cell is filled down).
* The named defects of the reviews are fixed and asserted by tests:
  * RPS (p268–270): `DL3- HR2` support ends `… the PSPs are tripped.`, `DL3-HR3` ends `… the ISPs are tripped.`
    (the sentence was printed before its ID); `DL4-HR7` and `DL4-RR8` are separate rows with their own support.
  * RIS (p295–296): `DL3-RC1e` (cold pool temperature), `DL3-RC1h` (hot pool level) and `DL3-RC1j` (PSP speed
    and PSP current) each carry their own support sentence; no orphan rows.
  * RMS (p308): the table is emitted under `7.6.6.2.1 Defense Line Functions`, before `7.6.6.2.2`.
  * Classification tags: the `(SR)`/`(NSRST)` second description line of the 6 affected rows (RCC DL3-RC1,
    RES DL3-RC1, IHT DL2-HR2, RAC DL3-HR4, IAC DL4-HR1, SPS DL3-HR11) is back in the description cell.
  * NDC/NUP (p328): all 12 rows carry `The NDC and NUP provide electric power to support performance of these
    functions.`
  * Repeated page headers (p15, p32, p123, p139, p169, p189, p256, p269, p270, p284, p296) are consumed by the
    merge; the FHP header that the review reported as lost is present (restored by `--include-header-footer`).
* RWG (p219) and NHV (p229) have no header row in the PDF. They get the same three column names with an HTML
  comment `<!-- header row supplied: the PDF prints this table without one (p.219) -->` above the table.
* Source typos inside the tables are kept: `DL3- HR2` (p269, p284), `poistion` (p256), `compares Them` (p268),
  `Scram – Gravity driven` vs `Scram - Gravity Driven` (RES vs RCC), `Below-the-Hook`, `DL4-HR1` support text
  repeated from DL3-HR5 (PHT, p63).

## 3. Verification

`python scripts/clean_references.py --only PSAR_ch07 --verify` (run of 2026-09-11, with figures; §7 has the
numbers after the final core of 2026-09-13):

| Metric | Core only (before this module) | After this module |
|---|---|---|
| missing tokens / PDF tokens | 512 / 117,186 (0.44 %) | **471 / 117,186 (0.40 %)** |
| residue (dot leader, entity, `[[`, running header, DOE footer, sheet heading, `x10-`, `<br>`) | 0 | **0** |
| headings whitelist / emitted | 282 / 282 | **289 / 289** |
| unmatched headings / unmatched subheads / orphan captions / failed patches | 0 / 1 / 0 / 0 | **0 / 0 / 0 / 0** |
| numbered section headings in the output | 282 (7 rendered as list items) | 289 = 67 (ch7a) + 76 (ch7b) + 146 (ch7c) |
| unnumbered subheadings / References headings | 238 / 20 | 268 / 28 |
| Markdown tables | 38 | 65 (38 captioned + 27 DL-function) |
| paragraphs > 2,000 chars | 7 | 0 (longest body line 1,906 chars) |

Composition of the missing tokens (per page, complete): 405 of 508 page-level misses are on figure pages and are
the deleted vector-figure debris — Figure 7.6.2-1 (p262, 150), Figure 7.2.3-1/-2 (p131/p132, 131), Figure
7.3.1-1/-2 (p178/p179, 50, CID-encoded labels such as `3rro`, `xho`), Figure 7.1.2-11 callouts (p56, 26, same
encoding), Figure 7.2.2-1 (p113, 24), Figures 7.7.1-1/-2 (p334/p335, 24 after the label callouts were added).
Of the remaining 103, 96 are on p270: the RPS table spans pp. 268–270 and is emitted under the p268 anchor, so
the verifier's ±1 page window does not see its last sheet — every one of those tokens is present in the document
(checked token by token). The last 7: `below-the`/`hook` (p197, the PDF line break `Below-the-⏎Hook` is joined by
the core hyphen map, intended), `keff` (p187 → `k<sub>eff</sub>`), and 4 figure-label tokens that also occur
elsewhere. **No body or table text is missing.**

Tests: `python -m pytest scripts/refclean/tests -q` → 188 passed at the time of writing (18 of them this chapter's).

## 4. Review H items and other findings — disposition

| Review | Item | Result |
|---|---|---|
| ch7a #1, #2 (H) | Table 7.1.2-4 / 7.1.3-6 `Notes` cells lost on the rotated pages | Restored by the re-conversion (`--content-safety-off off-page`): all 4 + 3 cells read `Primary coolant boundary component`; `described in Section 13.2.1` complete. Two remaining cell defects fixed by patch: `IHX Non-Tubing Components - Tubesheet, …` (the ` - ` was eaten as a line-end hyphen) and the two-value cells `SA-965 F304H; SA-240 304H`. |
| ch7a #3 (H) | `3.98 x 1015 n/cm2-s` | `3.98E+15 n/cm2-s` (core, from the PDF superscript map). Unit superscripts (`cm2`, `W/in3`, `m3/s`) stay as extracted per D2. |
| ch7a #4, ch7b #1, ch7c #1–#4 (H) | borderless DL tables | Rebuilt — §2. |
| ch7a #6 end-glued subheadings (H) | 6 run-in titles attached to the previous paragraph | All 6 are separate headings now (`Functional Requirements and Design Criteria` RES p27/IHT p86/IAC p108, `Guard Vessel` p39, `Regulatory Guidance` PHT p65/IHT p87). |
| ch7b #2 (H) | 76 numbered headings not rendered | All present (289/289 in the chapter). |
| ch7b #10 | FHP sentence order (`… as Table 7.3.1-2.` / `described in Section 6.3. …`) | Patch restores the printed sentence. |
| ch7b #8, ch7a #19 | multi-value cells merged without a separator | Patches: `150 (upper housing in HAA); Note 1 (lower housing)`, `30 (upper housing); 60 (lower housing)`, `Type 316 Stainless Steel; Alloy 718`, `150 (inlet stack); 525 (outlet stack)`, `150 (inlet duct); 525 (outlet duct)`. |
| ch7c #10, #11 | vector-figure debris, figures without text | Debris removed and all 43 figures rendered as PNGs by the core; the two SLD drawings additionally get a `> [!figure]` callout with their labels verbatim (`480V RXB MCC A/B` vs `480V FHB MCC A/B`, `PROVISION FOR CONNECTION TO PORTABLE DIESEL GENERATOR`), marked as transcribed from the drawing. |
| ch7c #13 | Table 7.6.3-1 group cells | Already filled down by the core (23 rows, group label in every row). |
| ch7a #9, ch7b #6, ch7c #9 | false list markers (`- Consistent with PDC …` 230, DL rows, RG lines) | 0 left: `- Consistent with PDC` 0 occurrences; every remaining list item has a printed bullet, number label or is a reference entry (checked against the PDF glyphs). |
| **Not fixed** | ch7a #11: the SSC classification of Figures 7.2.3-1/-2 exists only as box **colour** | Not restored. It would have to be derived (fill colour → SR/NSRST/NST/Non-SCG) and written as text that is not in the document; M severity. The rendered PNGs keep the information visually. |
| **Not fixed** | ch7a #16, ch7b #17, ch7c #18: italic PDC/RG titles (≈300 spans) | Deliberate: D7 keeps only the RG 1.232 redline, the GDC-19 "emphasis added" italics and the ch1 bold status terms. |
| **Not fixed** | Revision 1 change bars (ch7b 138, ch7c 37) | Deliberate: D7 ("개정 표시 막대는 복원하지 않는다"). |

Class-C decisions (documented so that a reviewer can reverse them): `<sup>*</sup>` for the `*`/`**` table-note
markers (spec §"Output conventions"), the supplied `Subsystem` column of Table 7.2.3-1, the supplied header rows
of the RWG/NHV tables (with the HTML comment), the 4 underline-less standalone titles promoted to subheadings,
the `; ` separators in the 5 two-value cells, and the two SLD label callouts.

## 5. Core patch requests (not applied — core modules are frozen)

1. **`pdfaux.build_aux` / `numbered_headings` — per-page body margin.** `aux.body_x0[page]` is the modal x0 of
   lines longer than 40 characters. On pages that a table's support column or a bullet list dominates it is not
   the body margin (ch7: p122/p138 → 314 pt, p182/p183/p251 → 90/108 pt, p295 → 314 pt), so `numbered_headings`
   rejects the section headings there (7 in ch7) and `structure.fix_false_items` uses the same wrong margin.
   Patch: keep a document-wide fallback and accept either.
   ```python
   # pdfaux.build_aux, after the body_x0 loop
   aux.meta["body_x0_doc"] = collections.Counter(aux.body_x0.values()).most_common(1)[0][0]
   # pdfaux.numbered_headings(...), replace
   -            if abs(first.x0 - body_x0.get(pno, first.x0)) > 3:
   -                continue
   +            margins = {body_x0.get(pno, first.x0), doc_margin}      # doc_margin = new parameter
   +            if all(abs(first.x0 - m) > 3 for m in margins):
   +                continue
   ```
2. **`pdfaux.underlined_subheads` — union of all underline segments.** For each span the loop keeps only the
   first overlapping rule (`break`), so a subheading whose underline is drawn as 2–3 abutting rectangles fails
   the `ul.width >= 0.85 × line width` test (26 missed subheadings in ch7, e.g. `Compressive Assembly` p11 with
   rects 72–136 / 136–146 / 146–186 pt).
   ```python
   -        for (t, sr, *_rest) in ln.spans:
   -            for r in marks:
   -                if <overlap>:
   -                    covered.append((t, sr, r)); break
   +        for (t, sr, *_rest) in ln.spans:
   +            rs = [r for r in marks if <overlap>]
   +            if rs:
   +                covered.append((t, sr, rs))      # union all of them when building `ul`
   ```
   (`profiles/psar_ch07.underlined_lines` is the fixed version.)
3. **`structure.insert_subheads` — occurrence choice.** The first occurrence that follows a sentence end and
   precedes an upper-case letter or `(` is accepted; in ch7 this matched `… four subsystems: Spent Fuel Pool
   (SFP), …` (p164) and `… six major components; In-Vessel Transfer Machine (IVTM), …` (p203) instead of the
   underlined line, splitting a sentence in two. Suggestion: carry the first line printed **below** the
   underlined line in `SubRef` and require the text after the split to start with it (that is what
   `profiles/psar_ch07.misplaced_subheads` repairs afterwards), or at least reject an occurrence whose
   continuation starts with `(`.
4. **`emit.render` / `verify` — page anchors for multi-page tables (cosmetic).** A table merged from 2–3 PDF
   pages is emitted under the anchor of its first page, so the covered pages get no anchor and `verify`'s ±1
   page window reports their rows as missing (ch7 p270: 96 tokens, all present). Either emit the covered pages'
   anchors after the table, or let `verify` widen the window to `table.pages`.

## 6. Reproduction

```
python scripts/clean_references.py --only PSAR_ch07 --verify     # 25 s, 43 PNGs
python -m pytest scripts/refclean/tests/test_psar_ch07.py -q     # 18 tests, ~1 s (PDF + built file)
```

## 7. Follow-up after the final core (2026-09-13)

Rebuilt against the final core. Both loose ends that the build reported as `unmatched_subheads` are fixed by one
new step, `retry_unmatched_subheads` (STEPS position 3):

* The core's `structure.insert_subheads` now requires the text before a subheading to end in `.?!”")` — the fix
  for the misplacement reported in §5.3 — so a subheading that follows a lead-in sentence ending in a **colon**
  stays inside the paragraph. Two of them in ch7:
  * **`RG 1.22, Revision 0, Periodic Testing of Protection System Actuation Functions`** (p265, after `The RPS
    conforms to RGs as follows:`). In this subsection the RG titles *are* underlined in the PDF and the core
    already promoted the other ten (pp. 266–267) to `#####`, so RG 1.22 was the only one left as a paragraph; it
    is a heading now, consistent with its siblings. Everywhere else in the chapter (XIS p282, RIS p294, RMS p307,
    AST p321, and all of 7.1–7.5) the RG titles are *italic only*, are not detected as subheadings, and stay
    paragraphs — intentional, D7 restores no italics.
  * **`External Hazard Protection for SR SSCs (SR)`** (p365, after `… which are designated as SR or NSRST:`).
    Underlined in the PDF; the same title is a `######` heading on pp. 340/346/347. It is a heading now.
  The step promotes an unmatched subheading only when the PDF prints it as a whole line of its own at the
  recorded underline position **and** the element text continues with the line printed directly below it; the
  heading text is cut with a whitespace-insensitive match so a trailing `)` stays with the heading. Underlined
  lines that fall inside a DL-table region (the second header line `Functional Support`, p328) are skipped and
  listed in `ch07_table_header_subheads` — they are table headers, not subheadings.
* Core changes absorbed: `missing_headings` and `missing_subheads` now find **0** items (the core's page-or-
  document margin rule covers all 7 headings, the underline-union covers all 26 subheadings) and
  `misplaced_subheads` finds 0 (the `SUB_TERMINAL` change). The three steps stay in place as regression guards —
  they re-add anything a later core change drops. The DL tables, lists, table notes, group rows and paragraph
  repair are unaffected (27 tables / 167 rows, 0/0 token-coverage anomalies, 21 nested NIC items, 24 note
  markers, 23 group rows, 34 joins / 176 splits, 8 References headings, 4 standalone subheadings — identical to
  §1).

Final state (`--only PSAR_ch07 --verify`, with figures, 43 PNGs):

| Metric | Value |
|---|---|
| missing tokens / PDF tokens | 507 / 118,355 (0.43 %) |
| residue | 0 |
| headings whitelist / emitted | 289 / 289 |
| unmatched headings / unmatched subheads / orphan captions / failed patches | 0 / 0 / 0 / 0 |
| pages with > 3 missing tokens | 9 — pp. 262, 132, 131, 178, 56, 113, 334, 179, 335, all of them figure pages |

Composition of the 507: **499** are tokens that the PDF prints only inside the vector figures (deleted debris —
Figure 7.6.2-1 150, Figures 7.2.3-1/-2 131, Figures 7.3.1-1/-2 50 CID-encoded labels, Figure 7.1.2-11 callouts 26,
Figure 7.2.2-1 24, Figures 7.7.1-1/-2 24 after the label callouts). The remaining **8** are intended
normalisations: `fast`+`neutron` (→ `fast-neutron`), `below-the`+`hook` (→ `Below-the-Hook`), `post`+`accident`
(→ `Post-Accident`), `keff` (→ `k<sub>eff</sub>`) and `reference` (→ the `References (7.6.7)` heading). No body
or table text is missing; the p270 artefact of the earlier run is gone (the core's range anchors and per-sheet
header credit).

Tests: `python -m pytest scripts/refclean/tests -q` → 193 passed (19 of them this chapter's); the ch7 tests are
unchanged and still green against the new core.
