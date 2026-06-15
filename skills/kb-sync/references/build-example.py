#!/usr/bin/env python3
"""
build-example.py — TEMPLATE for step 3 (draft patches → payloads).

Pattern proven on the first two Chatty sync runs. Copy + adapt per run.
Key rules:
  - Start from the CACHED live file (/tmp/kb-sync/<app>/<flattened>), so you patch
    exactly what's on v2 right now.
  - assert the anchor exists before replace — a moved/renamed heading should fail
    loudly, not silently produce an unchanged file.
  - For OUTDATED facts, count ALL occurrences and replace all (don't trust a
    hand-counted number — assert the count first so a miscount fails).
  - Emit full file content per entry; the API writes the whole file.
"""
import json
import os

APP = "chatty"
AGENT = "chatty-agent"
DATE = "2026-06-15"            # window/run date — pass in, never call date.now in a workflow
SRC = f"/tmp/kb-sync/{APP}"
OUT = os.path.expanduser(
    f"~/CSL/reports/analysis/kb-sync-{APP}-{DATE}-payloads.json")


def rd(flat_name):
    return open(os.path.join(SRC, flat_name)).read()


results = {}  # path -> new full content

# ---- OUTDATED: fix a stale fact everywhere it appears ----
f = rd("kb__case__email-channel-issues.md")
assert f.count("noreply@chattyemail.com") == 3        # count first, then replace
f = f.replace("noreply@chattyemail.com", "noreply@chatty.email")
results["kb/case/email-channel-issues.md"] = f

# ---- GAP: insert a new section before a real anchor heading ----
c = rd("kb__faq__channels.md")
anchor = "## Outlook Email Forwarding Blocked"
assert anchor in c
new_section = """## AI Auto-Reply by Channel & Plan

... full markdown matching KB voice ...

"""
c = c.replace(anchor, new_section + anchor, 1)
results["kb/faq/channels.md"] = c

# ---- write payloads ----
ops = [{"agent": AGENT, "path": p, "content": content}
       for p, content in results.items()]
json.dump(ops, open(OUT, "w"), ensure_ascii=False)
print(f"wrote {len(ops)} payloads -> {OUT}")
for o in ops:
    print(f"  {o['path']}: {len(o['content'])} bytes")
