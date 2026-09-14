import os
import shutil
import sys

import pytest

SCRIPTS = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REAL_VAULT = os.path.dirname(SCRIPTS)
sys.path.insert(0, SCRIPTS)


@pytest.fixture
def vault(tmp_path, monkeypatch):
    """A throw-away vault with the real template and empty inbox/references/wiki (public and internal)."""
    import source
    for d in ("inbox", "inbox/internal", "references/raw", "wiki", "templates",
              "internal/references/raw", "internal/wiki"):
        os.makedirs(tmp_path / d)
    shutil.copy(os.path.join(REAL_VAULT, "templates", "source_card.md"), tmp_path / "templates" / "source_card.md")
    monkeypatch.setattr(source, "VAULT", str(tmp_path))
    monkeypatch.setattr(source, "load_docs", lambda: {"DOC_A": ("DOC_A_Some Title", "generic", None)})
    return tmp_path
