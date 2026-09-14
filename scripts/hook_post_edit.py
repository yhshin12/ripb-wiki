"""hook_post_edit.py — Claude PostToolUse hook for Edit/Write/MultiEdit (spec §8.2).

Reads the hook JSON on stdin. For wiki/*.md and internal/wiki/*.md it runs the per-file lint and the quote check.
Errors: stdout JSON {"decision": "block", "reason": …} so Claude sees them (the edit itself already happened).
Warnings only: stdout JSON with hookSpecificOutput.additionalContext. Clean or not a note: no output.
Always exits 0; an internal failure is written to stderr only.
"""
import json
import os
import re
import sys

import notes as N

SCRIPTS = os.path.dirname(os.path.abspath(__file__))
VAULT = os.path.dirname(SCRIPTS)
NOTE = re.compile(r"^(internal/)?wiki/[^/]+\.md$")
MAX = 30


def target(payload, vault):
    path = (payload.get("tool_input") or {}).get("file_path")
    if not path:
        return None
    if not os.path.isabs(path):
        path = os.path.join(payload.get("cwd") or vault, path)
    path = os.path.normpath(path)
    rel = os.path.relpath(path, vault).replace(os.sep, "/")
    return path if NOTE.match(rel) else None


def respond(findings):
    if not findings:
        return ""
    lines = "\n".join(str(f) for f in findings[:MAX])
    more = f"\n… {len(findings) - MAX} more" if len(findings) > MAX else ""
    if any(f.level == "error" for f in findings):
        return json.dumps({"decision": "block",
                           "reason": "lint_wiki/verify_quotes found problems in the edited note; fix them:\n"
                                     + lines + more}, ensure_ascii=False)
    return json.dumps({"hookSpecificOutput": {"hookEventName": "PostToolUse",
                                              "additionalContext": "lint_wiki warnings:\n" + lines + more}},
                      ensure_ascii=False)


def main(stdin=None):
    sys.stdout.reconfigure(encoding="utf-8")
    try:
        payload = json.load(stdin or sys.stdin)
        path = target(payload, VAULT)
        if not path or not os.path.isfile(path):
            return 0
        import lint_wiki as LW
        import verify_quotes as VQ
        ctx = LW.Context(VAULT)
        findings = LW.lint_file(ctx, path)
        try:
            findings += VQ.verify_note(VAULT, path, VQ.Sources(VAULT, ctx.cards))
        except (N.NoteError, UnicodeDecodeError):
            pass                                  # L02 already reports it
        out = respond(findings)
        if out:
            print(out)
    except Exception as exc:
        print(f"hook_post_edit: {type(exc).__name__}: {exc}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
