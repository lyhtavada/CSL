#!/usr/bin/env python3
"""Build payload: add AI Availability FAQ section to chatty kb/faq/settings.md."""
import json, os, sys
sys.path.insert(0, os.path.dirname(__file__))
import kb_api

base, token = kb_api.load_creds()
agent = "chatty-agent"
path = "kb/faq/settings.md"
content = kb_api.get_file(base, token, agent, path)
assert content, "could not fetch settings.md"

# 1. add tags for availability discovery
anchor_tags = '    - "generate instructions"\n'
new_tags = anchor_tags + (
    '    - "AI availability"\n'
    '    - "when AI replies"\n'
    '    - "control AI replies"\n'
    '    - "AI reply timing"\n'
    '    - "stop AI replying"\n'
    '    - "AI reply rules"\n'
)
assert anchor_tags in content, "tags anchor not found"
content = content.replace(anchor_tags, new_tags, 1)

# 2. insert new section right after the Appearance section (before its --- divider)
anchor_section = (
    "**Welcome message:**\n"
    "The first message customers see when they click Contact us. "
    "Customize this to match your brand tone.\n\n"
    "---\n"
)
new_section = (
    "**Welcome message:**\n"
    "The first message customers see when they click Contact us. "
    "Customize this to match your brand tone.\n\n"
    "---\n\n"
    "## AI Availability — Control When AI Replies\n\n"
    "You can control when your AI agent replies to customers — for example, only "
    "during business hours, only when your team is offline, or always.\n\n"
    "**To set this up:**\n"
    "Go to **AI agent** → **Settings** → **AI availability** → **Choose when AI replies**.\n\n"
    "From there you can pick the rule that fits how you want the AI to work alongside "
    "your human team.\n\n"
    "---\n"
)
assert anchor_section in content, "section anchor not found"
content = content.replace(anchor_section, new_section, 1)

payload = [{"agent": agent, "path": path, "content": content}]
out = os.path.expanduser("~/CSL/reports/analysis/kb-sync-chatty-2026-06-16-payloads.json")
os.makedirs(os.path.dirname(out), exist_ok=True)
with open(out, "w") as f:
    json.dump(payload, f, indent=2, ensure_ascii=False)
print("wrote", out)
print("---- new section preview ----")
i = content.index("## AI Availability")
print(content[i:i+520])
