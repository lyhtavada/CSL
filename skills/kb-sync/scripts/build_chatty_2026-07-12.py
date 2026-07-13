#!/usr/bin/env python3
"""build_chatty_2026-07-12.py — payloads for the Jul 06-12 2026 kb-sync run (Chatty).
Review-gate: writes payloads JSON only. No push, no reindex.
Starts from the CACHED live files so we patch exactly what's on v2 now.
"""
import json, os

APP, AGENT, DATE = "chatty", "chatty-agent", "2026-07-12"
SRC = f"/tmp/kb-sync/{APP}"
OUT = os.path.expanduser(f"~/CSL/reports/analysis/kb-sync-{APP}-{DATE}-payloads.json")


def rd(flat):
    return open(os.path.join(SRC, flat)).read()


def _find(lines, anchor):
    idx = [i for i, l in enumerate(lines) if l.strip() == anchor]
    assert len(idx) == 1, f"anchor {anchor!r}: found {len(idx)}x (need 1)"
    return idx[0]


def before(content, anchor, block):
    lines = content.split("\n")
    i = _find(lines, anchor)
    return "\n".join(lines[:i] + block.strip("\n").split("\n") + [""] + lines[i:])


def after(content, anchor, block):
    lines = content.split("\n")
    i = _find(lines, anchor)
    return "\n".join(lines[:i + 1] + [""] + block.strip("\n").split("\n") + lines[i + 1:])


def repl(content, old, new, n):
    assert content.count(old) == n, f"{old!r}: {content.count(old)} occ (need {n})"
    return content.replace(old, new)


results = {}

# ---- OUTDATED: Basic AI-product limit 1,500 -> 500 (pricing.md + fresh chats both say 500) ----
results["kb/faq/ai-training-setup.md"] = repl(rd("kb__faq__ai-training-setup.md"), "1,500", "500", 2)
results["kb/case/ai-product-sync.md"] = repl(rd("kb__case__ai-product-sync.md"), "1,500", "500", 1)
results["kb/case/ai-sync-issues.md"] = repl(rd("kb__case__ai-sync-issues.md"), "1,500", "500", 2)

# ---- OUTDATED: knowledge-base.md — Basic products, Basic chat history, email domain ----
kb = rd("kb__faq__knowledge-base.md")
kb = repl(kb, "1,500", "500", 1)
kb = repl(kb,
          "| Chat history | 90 days | Unlimited | Unlimited | Unlimited |",
          "| Chat history | 90 days | 12 months | Unlimited | Unlimited |", 1)
kb = repl(kb, "noreply@chattyemail.com", "noreply@chatty.email", 1)
results["kb/faq/knowledge-base.md"] = kb

# ---- GAP Q24: microphone / voice input permission ----
MIC = """## Microphone / Voice Input Blocked ("no permission")

## Symptom

A merchant or customer tries to use voice/microphone input in chat and the browser reports "no permission" or the mic is blocked.

## Cause

This is a **browser-level microphone permission**, not a Chatty setting. Chatty cannot grant mic access — the browser must allow it for the site.

## Resolution — by browser

**Chrome / Edge:**
1. Click the lock icon in the address bar → set **Microphone** to **Allow** → refresh the page.
2. Edge alternative: **... → Cookies and site permissions → Microphone** → allow the site.

**Safari:**
1. **Safari → Settings for This Website → Microphone → Allow** → refresh.

If it is still blocked after allowing, ask the merchant to record a short clip of the permission prompt so support can check the specific browser/OS."""
results["kb/case/access-login-issues.md"] = before(rd("kb__case__access-login-issues.md"), "## Related", MIC)

# ---- GAP Q27: WhatsApp profile photo ----
WAP = """## WhatsApp Profile Photo (Show / Change)

Customers always see **your WhatsApp profile photo** (the one set on your WhatsApp Business account), on their side. When you open the WhatsApp thread **inside the Chatty inbox**, it displays the Chatty avatar — but that only affects your internal view; the customer still sees your WhatsApp avatar.

WhatsApp profile photos are controlled entirely by **WhatsApp / Meta** and **cannot be changed inside Chatty**. To change it, update it in **Meta Business Manager / WhatsApp Manager**, not in Chatty."""
results["kb/case/whatsapp-messenger-issues.md"] = before(rd("kb__case__whatsapp-messenger-issues.md"), "## Outbound WhatsApp Messages", WAP)

# ---- GAP Q43 + Q44: others.md ----
FOOTER = """## Chatty Cannot Edit Your Shopify Theme (Footer Links / Footer Icons)

The Shopify **theme editor is not managed by Chatty**, so theme content — including footer links and the footer social icons (e.g. a footer Instagram icon pointing to the wrong handle) — must be fixed in the **theme editor → Footer → Instagram icon** (or the relevant footer section). Chatty cannot change theme content on the merchant's behalf.

- **In-widget links** (FAQ quick-replies, contact-us links, deep links): the team can help configure these inside Chatty.
- **Theme elements** (footer, header, menus): direct the merchant to their Shopify theme editor or theme developer."""
INBOX = """## Removing the Shopify Inbox Popup (Competing Chat Widget)

If a second chat popup appears alongside Chatty, it is usually **Shopify Inbox**, a separate Shopify app — not part of Chatty. To remove it:

1. Go to **Shopify Admin → Settings → Apps and sales channels**.
2. Find **Shopify Inbox** and disable or remove it there.

Tip: any Q&A pairs the merchant already built in Shopify Inbox can be reused as Chatty AI training data (add them under **AI agent → Training data → Custom knowledge / FAQs**)."""
others = rd("kb__faq__others.md")
others = before(others, "## Chatty on Headless Shopify", FOOTER)
others = before(others, "## App Not Loading / 404 Error", INBOX)
results["kb/faq/others.md"] = others

# ---- PARTIAL Q20: WhatsApp launcher alignment ----
ALIGN = """### Matching the Chatbox Bubble to a Separate WhatsApp Icon

Some merchants run a standalone WhatsApp launcher icon beside the Chatty bubble and want the two to look the same size and line up. The Chatty bubble size/position is set in **Chatbox → Appearance → Chatbox button** (Button size + Position offsets). For a precise size/alignment match to a separate WhatsApp icon, collect a **screenshot** showing both icons and the device, and forward to TS — the team can fine-tune the bubble size and reposition it to align with the WhatsApp icon (done successfully via manual resize + reposition)."""
results["kb/case/chatbox-widget-issues.md"] = after(rd("kb__case__chatbox-widget-issues.md"), "## Widget Overlapping / Blocking Another Element", ALIGN)

ops = [{"agent": AGENT, "path": p, "content": c} for p, c in results.items()]
json.dump(ops, open(OUT, "w"), ensure_ascii=False, indent=2)
print(f"wrote {len(ops)} payloads -> {OUT}")
for o in ops:
    print(f"  {o['path']}: {len(o['content'])} bytes")
