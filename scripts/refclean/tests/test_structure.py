import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from refclean import structure as S  # noqa: E402
from refclean.doc import Doc, El  # noqa: E402
from refclean.pdfaux import Aux, HeadingRef, SubRef  # noqa: E402


def _doc(els):
    return Doc("T", "t", "", "", 3, {}, els)


def test_glued_heading_is_split():
    d = _doc([El("item", "3.7.4.1.2 Radiological Consequences Fuel cladding integrity is maintained.", 5)])
    S.promote_headings(d, Aux(), refs=[HeadingRef("3.7.4.1.2", "Radiological Consequences", 5, 5)])
    assert [e.kind for e in d.els] == ["heading", "para"]
    assert d.els[0].text == "3.7.4.1.2 Radiological Consequences" and d.els[0].level == 5
    assert d.els[1].text == "Fuel cladding integrity is maintained."


def test_heading_glued_after_body_text():
    d = _doc([El("para", "summarized in Table 3.2-5. 3.7.4.2.3 Radiological Consequences", 7)])
    S.promote_headings(d, Aux(), refs=[HeadingRef("3.7.4.2.3", "Radiological Consequences", 7, 5)])
    assert [(e.kind, e.text) for e in d.els] == [("para", "summarized in Table 3.2-5."),
                                                  ("heading", "3.7.4.2.3 Radiological Consequences")]


def test_page_break_join():
    d = _doc([El("para", "The SSCs that are categorized as NSRST are documented in", 6),
              El("item", "Chapter 5 and their performance criteria are documented in Chapters 6 and 7.", 7)])
    S.join_breaks(d)
    assert len(d.els) == 1 and d.els[0].text.endswith("documented in Chapter 5 and their performance criteria are documented in Chapters 6 and 7.")


def test_bulleted_lowercase_item_is_not_joined():
    d = _doc([El("item", "● for systems with single supports, and", 6),
              El("item", "● for systems with multiple supports", 6)])
    S.join_breaks(d)
    assert len(d.els) == 2


def test_list_item_followed_by_capitalised_paragraph_is_not_joined():
    d = _doc([El("item", "● Evaluation of Prevention-Mitigation Balance", 6),
              El("para", "Section 4.2.2 presents the programmatic DID.", 6)])
    S.join_breaks(d)
    assert len(d.els) == 2


def test_withheld_triple_collapses():
    d = _doc([El("para", "[[", 3), El("para", "This information is withheld in accordance with 10 CFR 2.390", 3),
              El("para", "]]SRI", 3)])
    S.withheld_callouts(d)
    assert [e.kind for e in d.els] == ["raw_md"]
    assert d.els[0].text == "> [!withheld] SRI — This information is withheld in accordance with 10 CFR 2.390"


def test_subheading_split_from_glued_paragraph():
    d = _doc([El("para", "Text ends here. Regulatory Criteria The design conforms to PDC 1.", 9)])
    S.insert_subheads(d, Aux(), subs=[SubRef("Regulatory Criteria", 9, 100.0)])
    assert [(e.kind, e.text) for e in d.els] == [("para", "Text ends here."), ("heading", "Regulatory Criteria"),
                                                  ("para", "The design conforms to PDC 1.")]
