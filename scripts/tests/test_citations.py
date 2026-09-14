import citations as C

CLEANED = """---
pdf_pages: 12
---

<!-- page 1 -->

# Cover

<!-- page 2 | 1 -->

## 3.2 Frequency

The **F-C Target** is not a boundary between “acceptable” and unacceptable.[^1] ^fc-target

| Event | Frequency<sup>1</sup> |
|---|---|
| AOO | 1E-02/plant-year |

<!-- page 3 | 2 -->

> [!withheld] SRI — This information is withheld in accordance with 10 CFR 2.390.

> [!figure] Figure 3-1 text
> Licensing basis events include AOOs, DBEs, and BDBEs.

<!-- page 5-7 | 4..6 -->

| Table 5-1 | Value |
|---|---|
| Range row | 5E-07 |

<!-- page 9 | 8 -->

Criterion text on nine\\* continues.

<!-- page 8 | 7 -->

Back on eight: sodium leakage shall be considered.

<!-- page 9 | 8 -->

<!-- source: note supplied by the build -->
Tail of nine.
"""


def test_parse_citation_forms():
    c = C.parse_citation("NEI_18-04 §3.2.1 p.16-17")
    assert (c.key, c.locator, c.p1, c.p2) == ("NEI_18-04", "§3.2.1", 16, 17)
    c = C.parse_citation("RG_1.232 SFR-DC 4 p.64")
    assert (c.key, c.locator, c.p1, c.p2) == ("RG_1.232", "SFR-DC 4", 64, 64)
    c = C.parse_citation("PSAR_ch05 Table 5.2-1 p.12")
    assert (c.locator, c.p1) == ("Table 5.2-1", 12)
    c = C.parse_citation("MTG_2026-01-02 §반응도 절")
    assert (c.key, c.locator, c.p1, c.p2) == ("MTG_2026-01-02", "§반응도 절", None, None)
    assert C.parse_citation("^1") is None and C.parse_citation("!abstract") is None


def test_split_trailing():
    text, cites = C.split_trailing('"A [sic] b." [DOC_A §1 p.2] [DOC_B Table 1 p.3]  ')
    assert text == '"A [sic] b."' and [c.key for c in cites] == ["DOC_A", "DOC_B"]
    assert C.split_trailing("see [[Other_Note]]") == ("see [[Other_Note]]", [])
    assert C.split_trailing("footnote[^1]") == ("footnote[^1]", [])


def test_page_map_ranges_and_non_monotonic_anchors():
    pages = C.page_map(CLEANED)
    assert "Cover" in pages[1] and "pdf_pages" not in "".join(pages.values())
    assert all("Range row" in pages[p] for p in (5, 6, 7))
    assert "Criterion text on nine" in pages[9] and "Tail of nine" in pages[9]
    assert "sodium leakage" in pages[8] and 4 not in pages
    assert C.has_pages(CLEANED) and not C.has_pages("# no anchors\n")


def test_page_map_matches_refclean_verify():
    from refclean.verify import md_pages
    ours, theirs = C.page_map(CLEANED), md_pages(CLEANED)
    assert set(ours) == set(theirs)
    assert all(C.normalize(ours[p]) == C.normalize(theirs[p]) for p in ours)


def test_normalize_removes_editorial_markup():
    pages = {p: C.normalize(t) for p, t in C.page_map(CLEANED).items()}
    assert 'The F-C Target is not a boundary between "acceptable" and unacceptable.' in pages[2]
    assert "fc-target" not in pages[2] and "[^1]" not in pages[2]
    assert "Event Frequency AOO 1E-02/plant-year" in pages[2]
    assert "withheld" not in pages[3] and "Figure 3-1 text" not in pages[3]
    assert "Licensing basis events include AOOs, DBEs, and BDBEs." in pages[3]
    assert "Criterion text on nine* continues." in pages[9]
    assert "supplied by the build" not in pages[9]


def test_quotes_and_fragments():
    item = '"Licensing basis events ... include AOOs, DBEs, and BDBEs." and "second one here"'
    assert C.quotes(item) == ["Licensing basis events ... include AOOs, DBEs, and BDBEs.", "second one here"]
    assert C.fragments(C.quotes(item)[0]) == ["Licensing basis events", "include AOOs, DBEs, and BDBEs."]
    assert C.fragments("a…b c d") == ["a", "b c d"]


def test_numbers_ignore_locators_citations_and_markers():
    text = ("빈도 5E-07/plant-year와 1,000개, 3.40 값. §3.7.3.1과 Table 3-1, p.16, DL3-RC1, "
            "[NEI_18-04 §3.2.1 p.16] LBE%%t:LBE%%, [[Note_2]]")
    assert C.numbers(text) == {"5E-7", "1000", "3.40"}
    assert C.numbers("5E-07") == C.numbers("5E-7")
