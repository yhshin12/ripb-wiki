import os
import sys

import pytest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from refclean import normalize as N  # noqa: E402


@pytest.mark.parametrize("inp,out", [
    ("shall not exceed 5×10-7 per plant-year", "shall not exceed 5E-07 per plant-year"),
    ("3.40x10-5", "3.40E-05"),
    ("3.72 x10-4", "3.72E-04"),
    ("1 x 10-2/plant-year", "1E-02/plant-year"),
    ("below 1x10-2 per plant-year and 1x10-4", "below 1E-02 per plant-year and 1E-04"),
    ("10 CFR 50.34", "10 CFR 50.34"),
    ("NUREG-1855", "NUREG-1855"),
    ("SECY-16-0012", "SECY-16-0012"),
    ("Table 3.10-1", "Table 3.10-1"),
    ("DG-1330", "DG-1330"),
    ("Criteria 10-19", "Criteria 10-19"),
])
def test_exponents_default(inp, out):
    assert N.exponents(inp) == out


def test_exponents_with_evidence():
    assert N.exponents("between 10-4 to", sups=["-4"]) == "between 1E-04 to"
    assert N.exponents("Criteria 10-19", sups=[]) == "Criteria 10-19"
    assert N.exponents("3.98 x 1015 n/cm2-s", sups=["15"]) == "3.98E+15 n/cm2-s"
    assert N.exponents("3.98 x 1015 n/cm2-s", sups=["-4"]) == "3.98 x 1015 n/cm2-s"


def test_entities_bullets_hyphen_escape():
    assert N.decode_entities("I&amp;C &lt; USL &gt; 400 °F") == "I&C < USL > 400 °F"
    assert N.bullets("• item\n● item\no sub") == "- item\n- item\n  - sub"
    assert N.apply_hyphen_map("sodiumcooled fast", {"sodiumcooled": "sodium-cooled"}) == "sodium-cooled fast"
    assert N.apply_hyphen_map("pre-sodiumcooled", {"sodiumcooled": "sodium-cooled"}) == "pre-sodiumcooled"
    assert N.obsidian_escape("approximately $0.30.") == "approximately \\$0.30."
