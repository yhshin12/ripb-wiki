# references/ Cleanup Pipeline Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Produce clean, RAG-ready `references/<stem>.md` (plus rendered figure PNGs) for the 9 source PDFs from the raw opendataloader output in `references/raw/`, reproducibly, with verbatim source wording.

**Architecture:** A Python package `scripts/refclean/` reads the opendataloader **JSON** (typed elements with page, bbox, font, row/col spans; header/footer as separate elements) plus PDF-side auxiliary data extracted with PyMuPDF (heading whitelist, underlined subheadings, superscripts, line-end hyphens, figure regions). Generic transforms (noise removal, headings, paragraphs, tables, figures, text normalisation) run first; document profiles (PSAR chapters, RG 1.232, NEI 18-04) add document-specific steps and explicit patch files for manual fixes. An emitter writes frontmatter + Markdown with page anchors; a verifier compares the output with the PDF text.

**Tech Stack:** Python 3.12 (`C:\Code\Python\pykaeri\.venv12\Scripts\python.exe`), PyMuPDF 1.28 (`fitz`), pdfplumber 0.11.9, pypdf 6.10, pytest 9, opendataloader-pdf 2.5.7 (JDK 17).

**Spec:** `meta/references_cleanup/cleanup_review_2026-09-11.md` (conventions §3, pipeline §4, per-file items §5–§7) and the per-file evidence in `meta/references_cleanup/file_reviews/review_*.md` (§5 of each = ordered rules, do-not-fix lists, identifier lists). Line numbers in the reviews refer to the superseded default-option md; locate by text.

## Global Constraints

- Source wording verbatim: restructure and normalise only; never paraphrase; source typos stay (each review §5 "자동 수정 금지").
- Exponents: `1E-07` form, mantissa kept (`3.40x10-5` → `3.40E-05`, `5×10-7` → `5E-07`, `10-4` → `1E-04`); positive exponents `3.98 x 1015` → `3.98E+15` only with PDF superscript evidence. Unit superscripts (`m2`, `cm2`) are left as extracted. Existing `8.13E-02` values unchanged.
- No TOC / List of Tables / List of Figures in output; frontmatter `tables:`/`figures:` lists replace them.
- One cleaned file per source PDF, same stem: `references/<stem>.md`.
- Figures: every figure caption gets a PNG rendered from its PDF region, stored at `references/figures/<doc_key>/Fig_<number>.png` (doc keys: `NEI_18-04`, `RG_1.232`, `PSAR_ch01`, `PSAR_ch03`, `PSAR_ch04`, `PSAR_ch05`, `PSAR_ch06`, `PSAR_ch07`, `PSAR_ch11`). Vector-figure text debris is deleted. Withheld figures get only the withheld callout.
- Emphasis (D7): preserve only RG 1.232 Table 1 redline (`~~deleted~~`, `<ins>inserted</ins>`), RG GDC-19 rationale "emphasis added" italics, ch1 bold status terms. No other italics; no change bars.
- Record format (D6): RG 1.232 Appendices A–C criteria and PSAR ch5 Tables 5.2-1–5.2-4 (PSF records). ch7 DL-function tables stay Markdown tables.
- Page anchors `<!-- page N | LABEL -->` (LABEL = printed page, e.g. `4.2-7`, omitted if unknown) before the first element of each PDF page.
- Withheld marker → `> [!withheld] SRI — This information is withheld in accordance with 10 CFR 2.390` (sentence verbatim as printed, including a final period if present).
- Obsidian safety: no `[[`/`]]` outside intended wikilinks, escape `$` and line-leading `*` that are not list markers.
- Scripts live in `scripts/`; inputs in `references/raw/` are read-only; tests under `scripts/refclean/tests/`.

## File Structure

| File | Responsibility |
|---|---|
| `scripts/convert_references.py` | (exists) add `json` to output formats |
| `scripts/clean_references.py` | CLI: `--only <substr>`, `--no-figures`, `--verify`; runs profile → emit → write |
| `scripts/refclean/__init__.py` | package marker, version string |
| `scripts/refclean/doc.py` | JSON → `Doc` (flat `El` stream, page labels, header/footer handling) |
| `scripts/refclean/pdfaux.py` | PyMuPDF auxiliary data (`Aux`): numbered-heading whitelist, underlined subheadings, superscripts, line-end hyphen dictionary, figure boxes |
| `scripts/refclean/normalize.py` | pure text normalisers (entities, bullets, exponents, hyphen map, whitespace, Obsidian escapes) |
| `scripts/refclean/structure.py` | cover/TOC removal, heading promotion + splitting, subheading insertion, paragraph/list repair, withheld callouts |
| `scripts/refclean/tables.py` | `Table` model from JSON cells, span fill-down, header detection, sheet merge, `<br>` handling, Markdown and record rendering |
| `scripts/refclean/figures.py` | caption detection, debris removal, PNG rendering |
| `scripts/refclean/emit.py` | frontmatter + Markdown serialisation with page anchors |
| `scripts/refclean/verify.py` | PDF-vs-output bag-of-words per page, residue checks, heading coverage, table spot checks |
| `scripts/refclean/profiles/{base,psar,rg1232,nei1804}.py` | document profiles (metadata + ordered steps) |
| `scripts/refclean/patches/<doc_key>.json` | explicit manual fixes (anchor text → replacement, with PDF page evidence) |
| `scripts/refclean/tests/test_*.py` | unit tests (synthetic fixtures) + smoke tests on real files |

### Core data model (produced by Task 1, consumed by all later tasks)

```python
@dataclass
class El:
    kind: str                 # 'heading' | 'para' | 'item' | 'table' | 'image' | 'caption' | 'hdr' | 'raw_md'
    text: str = ""            # heading/para/item/caption/hdr text; raw_md = pre-rendered Markdown
    page: int = 0             # 1-based PDF page
    bbox: tuple = ()          # (x0, y0, x1, y1), PDF points, origin bottom-left (as in ODL JSON)
    font: str = ""
    size: float = 0.0
    level: int = 0            # heading: final Markdown level (1..6); item: nesting depth (0..)
    list_style: str = ""      # item: ODL 'numbering style' ('unordered', 'arabic numbers', ...)
    table: "Table|None" = None
    id: int = 0               # ODL element id
    meta: dict = field(default_factory=dict)   # e.g. {'num': '4.2.1'}, {'caption_of': id}, {'drop': True}

@dataclass
class Doc:
    key: str                  # doc key, e.g. 'PSAR_ch04'
    stem: str                 # file stem shared by pdf/json/md
    raw_dir: str              # references/raw
    out_dir: str              # references
    n_pages: int
    page_labels: dict         # {pdf_page: 'label'}
    els: list                 # list[El] in reading order
```

```python
@dataclass
class Cell:
    text: str                 # cell paragraphs joined with '\n'
    row: int; col: int        # 0-based grid position of the top-left
    rowspan: int = 1; colspan: int = 1
    bold: bool = False
    filled: bool = False      # True when copied by span fill-down

@dataclass
class Table:
    grid: list                # list[list[Cell]] n_rows x n_cols after span expansion
    header_rows: int = 1
    page: int = 0; pages: list = field(default_factory=list)
    caption: str = ""         # e.g. 'Table 4.2-2 95th Percentile Risk Margins for Risk-Significant LBEs'
    notes: list = field(default_factory=list)
    id: int = 0
```

```python
@dataclass
class Aux:
    headings: list            # [HeadingRef(num:str, title:str, page:int)] in document order
    subheads: list            # [SubRef(text:str, page:int, y:float)] underlined / bold-italic unnumbered subheadings
    sups: dict                # {page: [SupRef(base:str, sup:str, before:str)]}  superscripts with 12 chars of preceding text
    hyphen_map: dict          # {'sodiumcooled': 'sodium-cooled', 'technologiesspecifically': 'technologies—specifically'}
    figures: list             # [FigureRef(num:str, caption:str, page:int, box:tuple, withheld:bool)]
```

A profile is `class Profile: key, stem, meta: dict, steps: list[Callable[[Doc, Aux], None]]`; steps mutate `doc.els` in order. `emit.render(doc, profile) -> str`.

---

### Task 0: Conversion emits JSON; spec header records final decisions

**Files:** Modify `scripts/convert_references.py` (COMMON `format="markdown,json"`); modify `meta/references_cleanup/cleanup_review_2026-09-11.md` (prepend a "확정 결정 (2026-09-11)" block: D1–D7 as decided, JSON input, figure location); modify `AGENTS.md` §3 (pointer to `meta/references_cleanup/` as the full spec; raw folder also holds `<stem>.json`).

- [ ] Run `python scripts/convert_references.py --force`; expect 9 × `<stem>.json` in `references/raw/`, md byte-identical to before (compare sha256 of the 9 md files before/after).
- [ ] Commit is NOT made (vault commit policy: user approves change summaries; push only on request).

### Task 1: `doc.py` — JSON to element stream

**Interfaces:** Produces `load_doc(key, stem, raw_dir, out_dir) -> Doc`, dataclasses `El`, `Doc`, `Cell`, `Table` (tables built via `tables.from_odl(node) -> Table`, stubbed here with a minimal implementation that Task 5 extends).

Rules:
- Walk `kids` in order. `heading`/`paragraph`/`caption` → `El(kind='heading'|'para'|'caption')`. `list` → one `El(kind='item')` per list item (content text; nested `kids` lists → items with `level+1`). `table` → `El(kind='table', table=from_odl(node))`. `image` → `El(kind='image')`.
- `footer`: extract the printed page label with `^(\S+)\s+Revision\s+\d+$` from any kid (PSAR), `^Appendix [ABC] to RG 1\.232, Rev\. 0, Page ([A-C]-\d+)$|^RG 1\.232, Rev\. 0, Page (\d+)$` (RG), `^© NEI 2019\. All rights reserved\. nei\.org\s+(\S+)$` (NEI); store in `doc.page_labels[page]`; emit nothing.
- `header`: for each kid text, strip a leading `Kemmerer Unit 1 PSAR` (and whitespace); if a remainder exists → `El(kind='hdr', text=remainder)` (these are table/figure captions or subheadings repeated per page); else emit nothing.
- Test (`tests/test_doc.py`): a synthetic JSON with one header (`Kemmerer Unit 1 PSAR Table 6.4-7 X (Sheet 1 of 2)`), one footer (`6.4-12 Revision 1` + DOE line), a list with 2 items, a 2×2 table → assert `page_labels == {5: '6.4-12'}`, kinds `['hdr','item','item','table']`, hdr text `Table 6.4-7 X (Sheet 1 of 2)`.
- Smoke: `load_doc('PSAR_ch04', ...)` on the real file: 16 page labels for p2–p16 (`i`, `ii`, `4.1-1`…`4.2-11`), ≥ 5 tables.

### Task 2: `pdfaux.py` — PDF auxiliary data

**Interfaces:** Produces `build_aux(doc, profile_kind) -> Aux` and the dataclasses `HeadingRef`, `SubRef`, `SupRef`, `FigureRef`.

Rules (PyMuPDF, visible/rotated coordinates via `page.rotation_matrix`):
- **Numbered headings (PSAR):** a text line whose full text matches `^(\d+(?:\.\d+)+)\s+(\S.*?)\s*$`, number starts with the chapter number, title has no dot leader, line is the first line of its block, the block's first span starts ≤ 2 pt from the body left margin of that page, and the page is not a TOC/LoT/LoF page (page text contains `. . . .` leaders ≥ 5 times). Continuation: if the next line of the same block has the same x0 and the heading line does not end with `.`, and the block has ≤ 3 lines, append it (wrapped titles). Exclude reference entries (`^\d+\.\d+-\d+ `). Keep document order and dedupe exact repeats.
- **NEI:** headings = `pypdf` outline (title, depth 0/1/2, page) + lines in font `*BoldItalic*` 11 pt that are a whole line (`Task …`, unnumbered subheads) with page.
- **RG 1.232:** headings = whole lines in `*Bold*` ≥ 11 pt on portrait pages p1–p28 plus appendix titles (`APPENDIX [A-C]\.`).
- **Underlined subheadings (PSAR):** thin horizontal marks (height < 1.6 pt) whose top is within ±3 pt of a span bottom and whose width ≤ covered text width + 40 pt; the covered text (joined spans on that line) is a subheading unless it is inside a table cell region (ODL table bbox on that page) → then skip. Output in order with page and y.
- **Superscripts:** spans with size ≤ 0.8 × modal body size and baseline ≥ 1 pt above the previous span on the same line; record `base` = last token of previous span, `sup` = span text, `before` = previous 12 chars.
- **Hyphen map:** for each line ending in `-` or `—` followed by a line starting with a letter, candidate = `left + right` joined without the dash; accept if the joined form never occurs inline anywhere in the PDF text; map joined form → `left-right` (or `left—right`).
- **Figures:** captions `^(?:Kemmerer Unit 1 PSAR\s+)?Figure\s+(\d+(?:\.\d+)*-\d+|\d+-\d+)\.?\s+(.+)$` on non-TOC pages; box = union of drawings/images/text between header rule and footer rule (see scratch prototype `render_figure.py`); `withheld=True` if the page text contains `This information is withheld`.
- Tests (`tests/test_pdfaux.py`, real PDFs): ch4 headings = the 15 numbered sections listed in the ch4 TOC (4.1, 4.1.1–4.1.3, 4.2, 4.2.1, 4.2.1.1–4.2.1.4, 4.2.2, 4.2.2.1–4.2.2.3, 4.2.3); ch5 subheads count of `Implementation Summary` = 53; hyphen map for RG contains `sodiumcooled → sodium-cooled` and not `watercooled`; ch7 figures include `7.2.3-1` on page 131.

### Task 3: `normalize.py` — text normalisers (pure functions, TDD)

**Interfaces:** `decode_entities(s)`, `bullets(s)`, `exponents(s, sups_on_page=None)`, `apply_hyphen_map(s, m)`, `obsidian_escape(s)`, `squash_ws(s)`.

Test table (`tests/test_normalize.py`) — each row is an assertion `f(inp) == out`:

| fn | input | output |
|---|---|---|
| exponents | `shall not exceed 5×10-7 per plant-year` | `shall not exceed 5E-07 per plant-year` |
| exponents | `3.40x10-5` | `3.40E-05` |
| exponents | `3.72 x10-4` | `3.72E-04` |
| exponents | `1 x 10-2/plant-year` | `1E-02/plant-year` |
| exponents | `below 1x10-2 per plant-year and 1x10-4` | `below 1E-02 per plant-year and 1E-04` |
| exponents | `10 CFR 50.34`, `NUREG-1855`, `SECY-16-0012`, `Table 3.10-1`, `DG-1330` | unchanged |
| exponents (sups=['-4']) | `between 10-4 to` | `between 1E-04 to` |
| exponents (sups=[]) | `Criteria 10-19` | unchanged |
| exponents (sups=['15']) | `3.98 x 1015 n/cm2-s` | `3.98E+15 n/cm2-s` |
| decode_entities | `I&amp;C`, `&lt; USL`, `&gt; 400 °F` | `I&C`, `< USL`, `> 400 °F` |
| bullets | `• item`, `● item`, `o sub`, `\uf0a7 x` | `- item`, `- item`, `  - sub`, `- x` |
| apply_hyphen_map | `sodiumcooled fast` with `{'sodiumcooled':'sodium-cooled'}` | `sodium-cooled fast` |
| obsidian_escape | `approximately $0.30.` | `approximately \$0.30.` |

### Task 4: `structure.py` — generic structure transforms

**Interfaces:** step functions `drop_cover(doc, aux)`, `drop_toc(doc, aux)` (returns harvested caption list into `doc.meta`), `promote_headings(doc, aux)`, `insert_subheads(doc, aux)`, `join_page_breaks(doc, aux)`, `fix_false_items(doc, aux)`, `withheld_callouts(doc, aux)`, `normalise_text(doc, aux)`.

Rules:
- `drop_cover`: drop page-1 elements (logos, title block, DOE line); title/issuer go to frontmatter via profile.
- `drop_toc`: drop every element on TOC/LoT/LoF pages (page text has ≥ 5 dot-leader lines) and any element whose text has `(\.\s?){4,}\s*\S+$`; harvest `Table …`/`Figure …` titles into `doc.meta['lot']`/`['lof']`.
- `promote_headings`: for each `HeadingRef` in order, find the first element at/after the cursor whose text starts with, contains, or ends with `num + ' ' + title` (whitespace-normalised). Split the element into up to three: text before (kept as its original kind), the heading (`kind='heading'`, `meta.num`, level = number of components, PSAR `4.1` → 2), text after (kind `para`). Elements already of kind heading whose text is not in the whitelist and is not a caption/References/document title → demote to `para`. Stop cursor at match to preserve order. Report unmatched refs.
- `insert_subheads`: same cursor search for `SubRef.text` restricted to the SubRef page ±1; split glued text; level = enclosing numbered heading level + 1, capped at 6 (beyond 6 → `**text**` para).
- `join_page_breaks`: previous body element (para/item) ends without `[.:;?!”")]` and the next body element (skipping page anchors, hdr, images) starts with a lowercase letter, `(Reference`, `Section `, a digit+unit continuation → merge texts with one space (next element's list marker dropped); do not merge across headings, captions, tables.
- `fix_false_items`: items with `list_style` not `unordered` whose text does not start with a list label and whose x0 equals the page body margin → `para` (covers `Consistent with PDC …`, `As explained …`).
- `withheld_callouts`: sequences `[[` / `This information is withheld in accordance with 10 CFR 2.390.?` / `]]SRI` (any split or glued form) → one `raw_md` callout element; strip `[[` from glued captions.
- Tests (`tests/test_structure.py`) with synthetic Docs: glued heading `- 3.7.4.1.2 Radiological Consequences Fuel cladding…` splits into heading + para; page-break pair (`…are documented in` / item `Chapter 5 and their…`) merges; withheld triple collapses; TOC element with dot leaders is dropped.

### Task 5: `tables.py` — table model and rendering

**Interfaces:** `from_odl(node) -> Table`, `fill_spans(t)`, `detect_header(t)`, `merge_sheets(doc, aux)` (step), `render_md(t) -> str`, `render_records(t, spec) -> str`.

Rules:
- Grid from ODL cells using row/column number and spans; spanned positions copy the text with `filled=True` (fill-down/right) — rows stay self-contained.
- Header rows = leading rows whose non-empty cells are all bold (ODL font contains `Bold`); multi-row headers flatten to `Parent: Child` (empty parents inherit leftwards).
- Sheet merge: consecutive table elements (possibly separated only by `hdr`, page anchors, notes) with the same caption base (caption minus `(Sheet n of m)`/`(continued)`) or identical header rows → one table; repeated header rows dropped; a first-column group label with `(continued)` → label without it.
- Group-label rows (single non-empty cell spanning all columns) → kept as a `Group` column value on the following rows when the profile requests it, else rendered as a bold row.
- Cell text: `\n` → ` ` except before enumerators `^\(?\d+[.)]|^[A-Z]\.\d+|^[a-z]\)` → `; `; pipes escaped `\|`.
- Caption: nearest preceding `hdr`/`heading`/`caption` whose text starts with `Table `; the caption element is consumed.
- Tests: 3×3 table with a rowspan-2 cell renders the value in both rows; two sheets with identical header merge into one with a single header; `a\nb` cell renders `a b`; `(1) x\n(2) y` renders `(1) x; (2) y`.

### Task 6: `figures.py` — figures

**Interfaces:** `figures_step(doc, aux)`; `render_png(pdf, FigureRef, out_path, dpi=200)`.

Rules:
- For each `FigureRef` (non-withheld): render PNG to `references/figures/<doc_key>/Fig_<num>.png`; replace the caption element (or insert at the figure page start) with `heading` (PSAR: level = owning section level + 1) + `raw_md` `![Figure <num> <caption>](figures/<doc_key>/Fig_<num>.png)`.
- Debris: on a figure page, drop elements (para/item/table/image/hdr) whose bbox lies inside the figure box, except the caption. Decorative images (cover logos, fill rectangles) are dropped everywhere.
- Withheld figure: heading + withheld callout, no PNG.
- Test: ch7 figure 7.2.3-1 → PNG exists, width > 1000 px; no element with text `NGA` remains on page 131.

### Task 7: `emit.py` + CLI + PSAR ch4 end-to-end

**Interfaces:** `render(doc, profile) -> str`; `scripts/clean_references.py`.

Rules: frontmatter keys `doc_id, title, doc_type, issuer, revision, date, source_pdf, raw_md, pdf_pages, page_labels (compact ranges), converter, cleaned, tables, figures, withheld, tags, aliases`; page anchor before first element of each page; headings `#`×level; items `- ` with 2-space nesting; tables via `render_md`; collapse ≥ 2 blank lines; file ends with one newline.

- [ ] ch4 end-to-end: output contains `## 4.1 Overall Plant Risk Performance Summary`, `### 4.2.1 Plant Capability Summary`, Table 4.2-2 with header `Mean Dose Margin[d]` and values `3.79 … 15.0`, no `. . . .`, no `SUBJECT TO DOE`, `5E-07` present and `5×10-7` absent.

### Task 8: `verify.py`

**Interfaces:** `verify(doc_key) -> dict` and `--verify` CLI flag writing `references/raw/_verify/<doc_key>.json` (raw dir is excluded from git and Obsidian).

Checks: (1) per-page bag-of-words PDF − output after removing header/footer/TOC tokens: report pages with > 3 missing tokens; (2) residue: dot leaders, `&amp;`/`&lt;`/`&gt;`, `[[`, lone `Kemmerer Unit 1 PSAR`, `(Sheet n of m)` headings, `SUBJECT TO DOE`; (3) heading coverage: every `HeadingRef` emitted exactly once; (4) doc-specific spot checks from each review (ch4 Table 4.2-2 [d] 11 values; ch6 522 non-empty load factors; ch3 one table per announced LBE kind; RG 178 criteria each with non-empty text; ch5 62 PSF IDs each with SRDC).

### Task 9: PSAR profile + chapter hooks (parallelisable per chapter after Tasks 1–8)

Common PSAR steps (in `profiles/psar.py`): drop_cover → drop_toc → withheld_callouts → figures_step → promote_headings → insert_subheads → fix_false_items → join_page_breaks → merge_sheets → normalise_text → chapter hooks → caption/References levels (`References` → `References (<section>)` at owning level + 1; `Table x.y-n` captions at level of section x.y + 1).

Chapter hooks — spec = the chapter review §5; acceptance = Task 8 checks green plus:
- **9a ch1:** Table 1.4-1 (26 sheets) → one table, `Conformance Status`/`Comments` split for the 26 glued rows; Figure 1.2-1 legend (31 entries) as a two-column table under the figure; ch1 bold status terms (`**Full Conformance**` etc.); 7 hyphen restorations from the PDF map only.
- **9b ch3:** relocate LBE mini-tables: the i-th "… are listed below." sentence of kind k (freq/dose/DBA dose) receives the i-th table of kind k (88 total); fill-down Tables 3.1-2/3.1-3/3.5-4; Table 3.5-4 LPZ header present; §3.14 equations replaced by the answer block in review_ch3 §5-4 (patch file); initial-conditions table moved under 3.3.4.2 (patch); LBE title split lines joined.
- **9c ch5:** PSF tables 5.2-1–5.2-4 → records `#### DL3-RR2 — <function description>` with fields (Safety classification, SRDC, Associated LBE(s), SSCs, Notes); fill-down PSF ID across 93 continuation rows; `Implementation Summary` / `Relevant PSAR Chapters and Sections` subheads under each PDC.
- **9d ch6:** load-combination tables 6.4-5/-6/-7/-8/-11/-12 verified against pdfplumber (522 non-empty factors); 3-level headers flattened; table notes kept with their table; IBC combinations one per line; source defects annotated only.
- **9e ch7:** rebuild borderless DL-function / Functional Support tables (27 tables, 167 rows) from PyMuPDF word positions (prototype `ch7c_dltab.py` in the review scratchpad) with expected-ID QA lists (review_ch7c §5.1); `- Consistent with PDC` markers removed; nested NIC bullets restored.
- **9f ch11:** Table 11.5-1 row 5.0 rebuilt from pdfplumber cell text; operating-mode definitions (Mode-1…4) as paragraphs checked against PDF p65–66.
- **9g ch4:** Tables 4.2-3/4.2-4 two-row header flattened; notes as a list under each table.

### Task 10: RG 1.232 profile

Spec: review_rg §5.1–§5.5. Steps: headings from font hierarchy with the two order swaps fixed; footnotes (14, explicit list) → `[^n]`; hyphen map (identifiers `SFR-DC`, `MHTGR-DC`, `SECY-15-0002`, …); Table 1 crosswalk as one table with columns `Section | Criterion | GDC title | ARDC title | ARDC status | SFR-DC title | SFR-DC status | MHTGR-DC title | MHTGR-DC status` using `~~…~~` + `<ins>…</ins>` (insertions from blue `#1f497c` spans); Appendices A–C as records `#### SFR-DC 4 — Environmental and dynamic effects design bases` + `Status`, `Criterion text`, `NRC rationale`, `(none in source)` when empty; acronyms two-column table; references numbered list; GDC-19 emphasis italics.

### Task 11: NEI 18-04 profile

Spec: review_nei §5.1–§5.5. Steps: headings from outline (depth 0/1/2 → H2/H3/H4) + BoldItalic subheads (parent + 1); tables 3-1, 3-2, 4-1, 5-1, 5-3–5-10, acronyms, glossary transplanted from a struct-tree conversion (`use_struct_tree=True`, generated into `references/raw/_aux/`) with the listed fixes (RISC-2 shift, rowspan shift for 5-3/5-5/5-7/5-8, Table 5-2 manual); Table 3-2 formulas and R_j equation from the patch file (transcribed from the rendered page); the 3 sign-lost exponents fixed by patch; footnotes `[^pNN]`; hyphen map; nested lists restored.

### Task 12: Patch files and manual items

`scripts/refclean/patches/<doc_key>.json`: list of `{ "find": "<exact text in cleaned output>", "replace": "...", "page": N, "evidence": "<why>" }`, applied after all steps; unmatched patches fail the run. Contents: review §6 C items (NEI formulas, ch3 §3.14 block, ch6 λ block, alt texts).

### Task 13: Full run, verification report, docs

- [ ] `python scripts/clean_references.py --verify` for all 9; all Task 8 checks green or listed as accepted residuals with reasons.
- [ ] Update `AGENTS.md` §3 step 3 to name `scripts/clean_references.py`; append `log.md`.
- [ ] Report to the user: files produced, residual issues, figure count and size.
