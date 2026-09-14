"""`refs` marker guard (spec D11: references/ is not in git).

- refs-marked tests are skipped when references/raw holds no PDF (fresh clone).
- an unmarked test that opens a file under references/ during setup or call fails, so new tests get marked.
  Blind spot: files opened from C code (PyMuPDF `fitz.open`) raise no audit event.
"""
import os
import sys

import pytest

VAULT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
REFS = os.path.normcase(os.path.join(VAULT, "references")) + os.sep
RAW = os.path.join(VAULT, "references", "raw")
REFS_PRESENT = os.path.isdir(RAW) and any(f.lower().endswith(".pdf") for f in os.listdir(RAW))
_state = {"on": False, "hits": []}


def _audit(event, args):
    if _state["on"] and event == "open" and args and isinstance(args[0], (str, bytes, os.PathLike)):
        p = os.path.normcase(os.path.abspath(os.fsdecode(args[0])))
        if p.startswith(REFS):
            _state["hits"].append(p)


sys.addaudithook(_audit)


def pytest_collection_modifyitems(config, items):
    if REFS_PRESENT:
        return
    skip = pytest.mark.skip(reason="references/raw has no PDF (local-only inputs, spec D11)")
    for item in items:
        if item.get_closest_marker("refs"):
            item.add_marker(skip)


def _guard(item):
    marked = item.get_closest_marker("refs") is not None
    _state.update(on=not marked, hits=[])
    try:
        result = yield
    finally:
        _state["on"] = False
    if _state["hits"]:
        raise AssertionError(f"unmarked test opened {_state['hits'][0]}; add @pytest.mark.refs")
    return result


@pytest.hookimpl(wrapper=True)
def pytest_runtest_setup(item):
    return (yield from _guard(item))


@pytest.hookimpl(wrapper=True)
def pytest_runtest_call(item):
    return (yield from _guard(item))
