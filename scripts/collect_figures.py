"""Copy rendered figures from references/figures/<KEY>/<name>.png to figures/<KEY>_<name>.png.

Withheld figures have no PNG in references/figures, so they are never copied.
Prints a manifest; dry run unless --apply.
"""
import os
import shutil
import sys

VAULT = r"C:\Obsidian\ripb"
SRC = os.path.join(VAULT, "references", "figures")
DST = os.path.join(VAULT, "figures")
apply = "--apply" in sys.argv
rows = []
for key in sorted(os.listdir(SRC)):
    d = os.path.join(SRC, key)
    if not os.path.isdir(d):
        continue
    for fn in sorted(os.listdir(d)):
        if not fn.lower().endswith(".png"):
            continue
        target = f"{key}_{fn}"
        rows.append((key, fn, target))
        if apply:
            os.makedirs(DST, exist_ok=True)
            shutil.copy2(os.path.join(d, fn), os.path.join(DST, target))
names = [r[2] for r in rows]
assert len(names) == len(set(names)), "name collision"
for k, fn, t in rows:
    print(f"{k}\t{fn}\t{t}")
print(f"{len(rows)} figures", "copied" if apply else "(dry-run)")
