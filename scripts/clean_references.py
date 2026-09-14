"""Build cleaned, RAG-ready Markdown in references/ from the raw opendataloader output in references/raw/.

Usage:
  python scripts/clean_references.py                 # all documents
  python scripts/clean_references.py --only PSAR_ch04
  python scripts/clean_references.py --no-figures    # skip PNG rendering (faster)
  python scripts/clean_references.py --verify        # also write references/raw/_verify/<key>.json
  python scripts/clean_references.py --verify --max-missing-pct 1.0   # stricter PDF-coverage gate
  python scripts/clean_references.py --root internal   # read/write internal/references instead

With --verify the run exits non-zero when a document's `missing_pct` (PDF tokens absent from the output) exceeds
--max-missing-pct (default 2.0). The current accepted residuals are 0.00-1.66 % and are pinned token-exactly in
scripts/refclean/tests/test_psar_*.py / test_rg1232.py / test_nei1804.py; see refclean/verify.py for what the
metric cannot see.
"""
import argparse
import datetime
import importlib
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

from refclean import VERSION  # noqa: E402
from refclean.doc import load_doc  # noqa: E402
from refclean.emit import page_label_ranges, render  # noqa: E402
from refclean.pdfaux import build_aux  # noqa: E402
from refclean.profiles import DOCS  # noqa: E402
from refclean.tables import overlap_warnings  # noqa: E402

VAULT = os.path.dirname(HERE)
PATCH_DIR = os.path.join(HERE, "refclean", "patches")

RAW = OUT = None


def set_root(root=None):
    """Point RAW/OUT at <vault>/references[/raw] or <vault>/<root>/references[/raw]."""
    global RAW, OUT
    base = VAULT if not root else os.path.join(VAULT, root)
    RAW = os.path.join(base, "references", "raw")
    OUT = os.path.join(base, "references")


set_root(None)

PATH_FIELDS = ("source_pdf", "raw_json", "raw_md", "raw_json_tables")


def relocate_paths(meta, raw_dir):
    """Profiles write frontmatter paths as 'references/raw/<file>'; make them true for the actual raw_dir."""
    for k in PATH_FIELDS:
        v = meta.get(k)
        if isinstance(v, str) and v:
            meta[k] = os.path.relpath(os.path.join(raw_dir, os.path.basename(v)), VAULT).replace(os.sep, "/")
    return meta


def table_regions(doc):
    """{page: [visible rects]} of the tables opendataloader detected (kept out of heading/subheading search)."""
    import fitz
    from refclean.figures import odl_to_visible
    pdf = fitz.open(doc.pdf_path)
    regions = {}
    for e in doc.els:
        if e.kind == "table" and e.bbox and 0 < e.page <= len(pdf):
            r = odl_to_visible(e.bbox, pdf[e.page - 1])
            regions.setdefault(e.page, []).append(tuple(r))
    pdf.close()
    return regions


def apply_patches(key, text):
    path = os.path.join(PATCH_DIR, f"{key}.json")
    if not os.path.exists(path):
        return text, []
    with open(path, encoding="utf-8") as f:
        patches = json.load(f)
    failed = []
    for p in patches:
        n = text.count(p["find"])
        if n == 0 or (p.get("count") and n != p["count"]):
            failed.append(p["find"][:80])
            continue
        text = text.replace(p["find"], p["replace"])
    return text, failed


def build(key, render_figures=True, verify=False):
    stem, prof_name, chapter = DOCS[key]
    prof = importlib.import_module(f"refclean.profiles.{prof_name}")
    doc = load_doc(key, stem, RAW, OUT)
    aux = build_aux(doc.pdf_path, chapter=chapter, exclude=table_regions(doc))
    aux.meta["render_figures"] = render_figures
    for step in (prof.steps(chapter) if chapter is not None else prof.steps()):
        step(doc, aux)
    overlap_warnings(doc)          # cells lost to overlapping ODL spans in tables that reached the output
    meta = prof.metadata(doc, chapter, aux) if chapter is not None else prof.metadata(doc, aux)
    relocate_paths(meta, RAW)
    conv = {}
    cpath = os.path.join(RAW, "_conversion.json")
    if os.path.exists(cpath):
        conv = json.load(open(cpath, encoding="utf-8")).get(stem + ".pdf", {})
    meta["page_labels"] = page_label_ranges(doc.page_labels)
    opts = conv.get("options", {})
    meta["converter"] = (conv.get("converter", "opendataloader-pdf") + " (" +
                         ", ".join(f"{k}={v}" for k, v in opts.items() if k not in ("format", "quiet")) + ")")
    meta["cleaned"] = f"scripts/clean_references.py (refclean {VERSION}) {datetime.date.today().isoformat()}"
    text = render(doc, meta)
    text, failed = apply_patches(key, text)
    out_path = os.path.join(OUT, stem + ".md")
    with open(out_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)
    report = {
        "key": key,
        "output": os.path.relpath(out_path, VAULT),
        "unmatched_headings": doc.meta.get("unmatched_headings", []),
        "unmatched_subheads": doc.meta.get("unmatched_subheads", []),
        "orphan_captions": doc.meta.get("orphan_captions", []),
        "figures_without_caption_element": doc.meta.get("figures_without_caption_element", []),
        "failed_patches": failed,
        "warnings": [w for k, v in doc.meta.items() if k.endswith("_warnings") for w in v],
        "qa": {k: v for k, v in doc.meta.items() if k.endswith("_qa")},
    }
    if verify:
        from refclean.verify import verify as run_verify
        report["verify"] = run_verify(doc, aux, text)
        vdir = os.path.join(RAW, "_verify")
        os.makedirs(vdir, exist_ok=True)
        with open(os.path.join(vdir, f"{key}.json"), "w", encoding="utf-8") as f:
            json.dump(report, f, ensure_ascii=False, indent=1)
    return report


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--only", default="")
    ap.add_argument("--no-figures", action="store_true")
    ap.add_argument("--verify", action="store_true")
    ap.add_argument("--max-missing-pct", type=float, default=2.0,
                    help="with --verify: exit non-zero when a document's verify missing_pct exceeds this (default 2.0)")
    ap.add_argument("--root", default=None, help="sub-vault, e.g. internal")
    args = ap.parse_args()
    set_root(args.root)
    sys.stdout.reconfigure(encoding="utf-8")
    over = []
    for key in DOCS:
        if args.only and args.only not in key:
            continue
        try:
            prof = DOCS[key][1]
            importlib.import_module(f"refclean.profiles.{prof}")
        except ModuleNotFoundError:
            print(f"skip {key}: profile '{prof}' not implemented yet")
            continue
        rep = build(key, render_figures=not args.no_figures, verify=args.verify)
        print(json.dumps({k: (v if not isinstance(v, list) else v[:8] + ([f'... +{len(v) - 8}'] if len(v) > 8 else []))
                          for k, v in rep.items() if k != "verify"}, ensure_ascii=False))
        if "verify" in rep:
            summary = rep["verify"].get("summary", {})
            print("  verify:", json.dumps(summary, ensure_ascii=False))
            if summary.get("missing_pct", 0.0) > args.max_missing_pct:
                over.append(f"{key}: missing_pct {summary['missing_pct']} > {args.max_missing_pct}")
    if over:
        print("FAIL (PDF coverage): " + "; ".join(over))
        sys.exit(1)


if __name__ == "__main__":
    main()
