#!/usr/bin/env python3
"""build_chatty_2026-07-30.py — patches from bot-corrections week 23/07-29/07.
Source: reports/bot-corrections/chatty/chatty-corrections-2026-07-23.md diff.
"""
import json
import os

APP = "chatty"
AGENT = "chatty-agent"
DATE = "2026-07-30"
SRC = f"/tmp/kb-sync/{APP}"
OUT = os.path.expanduser(
    f"~/CSL/reports/analysis/kb-sync-{APP}-{DATE}-payloads.json")


def rd(flat_name):
    return open(os.path.join(SRC, flat_name)).read()


results = {}

# ---- #1 OUTDATED + #6 OUTDATED: live-chat.md — pre-chat form path + Holiday path ----
f = rd("kb__faq__live-chat.md")
old_step3 = "3. Click **Edit** to configure the pre-chat form"
assert f.count(old_step3) == 1
f = f.replace(old_step3, "3. Go to **Chatbox → Chat page → Pre-chat form** to configure it")

old_holiday = "Go to **Settings → Online Hours → Holidays** → add a holiday date range."
assert f.count(old_holiday) == 1
f = f.replace(
    old_holiday,
    "Go to **Settings → Chat availability → Manage → Working hours → Holiday** → toggle on and add the date range."
)
results["kb/faq/live-chat.md"] = f

# ---- #5 OUTDATED + #9 OUTDATED: inbox.md — tab names + anonymous visitor names ----
f = rd("kb__faq__inbox.md")
old_tabs = "1. **Check all tabs** — inbox has: All / Unread / Resolved / Mine — conversations may be in the **Resolved** tab"
assert f.count(old_tabs) == 1
f = f.replace(
    old_tabs,
    "1. **Check all tabs** — inbox tabs are **All, Your Inbox, Unassigned, Blocked**; also check the **Status** filter (Open, Resolved, Starred, Blocked, Unread) — conversations may be sitting under Unassigned or Resolved"
)

old_anon = '1. **Switch to a fixed anonymous label** — the visitor shows as "Anonymous-xxx" instead of a random name. CS can change this setting for the merchant on request.'
assert f.count(old_anon) == 1
f = f.replace(
    old_anon,
    '1. **Switch to a fixed anonymous label** — the visitor shows as "Anonymous-xxx" instead of a random name. This is self-serve: **Settings → Inbox settings → Anonymous visitor names**.'
)
results["kb/faq/inbox.md"] = f

# ---- #9 GAP addition: general-settings.md — add Anonymous visitor names to Inbox settings tab row ----
f = rd("kb__faq__general-settings.md")
old_row = "| **Inbox settings** | Message preference (Enter key behavior), Quick replies |"
assert f.count(old_row) == 1
f = f.replace(
    old_row,
    "| **Inbox settings** | Message preference (Enter key behavior), Quick replies, Anonymous visitor names |"
)
results["kb/faq/general-settings.md"] = f

# ---- #14 OUTDATED + #11 PARTIAL: ai-agent-settings.md ----
f = rd("kb__faq__ai-agent-settings.md")
old_channels = """Enable the AI agent to respond to customers on selected channels: **Email**,
**Messenger**, **Instagram**, and **WhatsApp**. Click **Connect** on each channel
to set it up. Available on the **Pro** and **Plus** plans."""
assert f.count(old_channels) == 1
new_channels = """Enable the **AI agent to reply** on selected channels: **Email**, **Messenger**,
**Instagram**, and **WhatsApp**. Click **Connect** on each channel to set it up.

The **Pro/Plus** plan gate applies to **AI auto-reply on that channel** — not to
connecting the channel itself. Connecting WhatsApp, Messenger, Instagram, or Email
is available on **all plans, including Free**; only having the AI respond
automatically on WhatsApp, Messenger, or Instagram requires **Pro or Plus** (see
`case_whatsapp-messenger-issues` and `faq_channels`)."""
f = f.replace(old_channels, new_channels)

anchor_identity = "## Support Email Addresses"
assert f.count(anchor_identity) == 1
identity_addon = """### "AI Not Using the Identity I Gave It"

If a merchant reports the AI isn't using the identity they configured, start at
**AI agent → Settings** and verify Name/Avatar/Welcome message are saved, and check
**Instructions → General instructions → Role** for the persona text. Don't default
to the generic data-source/Instructions-saved troubleshooting used for wrong-answer
cases (see `case_ai-wrong-responses` → *AI Reverts to Default Behavior*) — that flow
is for factual answers, not identity/persona.

"""
f = f.replace(anchor_identity, identity_addon + anchor_identity, 1)
results["kb/faq/ai-agent-settings.md"] = f

# ---- #14 OUTDATED: whatsapp-messenger-issues.md — plan note ----
f = rd("kb__case__whatsapp-messenger-issues.md")
anchor_wa = "## WhatsApp Connection Requirements\n\nThe merchant needs all of the following:"
assert f.count(anchor_wa) == 1
new_wa = """## WhatsApp Connection Requirements

**Plan note:** Connecting WhatsApp itself is available on **all plans, including
Free**. Only **AI auto-reply on WhatsApp** requires the **Pro** or **Plus** plan
(see `faq_ai-agent-settings` → *AI Channels*) — connection and manual/human replies
work on any plan.

The merchant needs all of the following:"""
f = f.replace(anchor_wa, new_wa)
results["kb/case/whatsapp-messenger-issues.md"] = f

# ---- #14 GAP addition: pricing.md — connecting vs. AI auto-reply clarification ----
f = rd("kb__faq__pricing.md")
anchor_pricing = "## Free Trial & Refund Policy"
assert f.count(anchor_pricing) == 1
pricing_addon = """## Connecting Channels vs. AI Auto-Reply on Channels

Connecting a channel (Email, WhatsApp, Messenger, Instagram) to Chatty is available
on **all plans, including Free** — this only requires the channel Connect step under
**Settings → Channels**. What's plan-gated is **AI auto-reply** on WhatsApp,
Messenger, and Instagram, which requires **Pro or Plus** (see
`faq_ai-agent-settings` → *AI Channels*). A merchant asking "which plan do I need
for WhatsApp" usually means connecting it — that's free; only mention the Pro/Plus
requirement if they specifically want the AI answering on that channel.

---

"""
f = f.replace(anchor_pricing, pricing_addon + anchor_pricing, 1)
results["kb/faq/pricing.md"] = f

# ---- #4 GAP: human-handover.md — After-sales support skill ----
f = rd("kb__faq__human-handover.md")
anchor_hh = "## Related\n- faq_live-chat"
assert f.count(anchor_hh) == 1
hh_addon = """## After-Sales Support Skill (Order/Return/Refund Questions)

For merchants who want order-related questions (shipping status, returns, refunds,
"where's my order") to go to a **contact form** instead of the AI asking for
email/order number, the right setting is the **After-sales support** skill, not the
generic Human handover destination.

Configure it at: **AI agent → Instructions → Manage → Assistant skills → Customer
support skills → After-sales support**. It can run in parallel with a merchant's
own Custom Scenario on returns/refunds (see `faq_train-ai`).

Don't route this request through Human handover's "Show contact methods" — that
option is for general handover, not for gating order-related AI questions behind a
contact form.

---

"""
f = f.replace(anchor_hh, hh_addon + anchor_hh, 1)
results["kb/faq/human-handover.md"] = f

# ---- #8 GAP + #12 PARTIAL: ai-wrong-responses.md ----
f = rd("kb__case__ai-wrong-responses.md")

old_test_ai = """The most common cause: **a live chat session holds the knowledge it loaded when the conversation started.** If a customer opened the chat before the merchant's training-data change, that session keeps answering from the old data even after the fix.

1. Ask the merchant (or reproduce yourself) to **Reset the conversation** on the storefront, then ask the question again.
2. This resolves the vast majority of these reports."""
assert f.count(old_test_ai) == 1
new_test_ai = """The most common cause: **a live chat session holds the knowledge it loaded when the conversation started.** If a customer opened the chat before the merchant's training-data change, that session keeps answering from the old data even after the fix.

1. **Ask the merchant which exact question/message they used to test** — get the specific wording so the case can be reproduced before proposing a fix.
2. Ask the merchant (or reproduce yourself) to **Reset the conversation** on the storefront, then ask the same question again.
3. This resolves the vast majority of these reports."""
f = f.replace(old_test_ai, new_test_ai)

old_markets = """Yes — Chatty supports Shopify Markets. Enable **Sync Markets** in **AI agent** → **Training data → Manage → Markets** to sync market-specific pricing and domains. Without this setting, the AI may show main-domain prices instead of market-specific prices.

If the AI is already showing wrong prices or wrong domain links for a market, see the troubleshooting entries below."""
assert f.count(old_markets) == 1
new_markets = """Yes — Chatty supports Shopify Markets. Enable **Sync Markets** in **AI agent** → **Training data → Manage → Markets** to sync market-specific pricing and domains. Without this setting, the AI may show main-domain prices instead of market-specific prices.

**Testing a market before it's live:** merchants can preview a market's language/currency setup on a **draft (unpublished) theme** in the Shopify theme editor — it doesn't need to be published/live to test.

If the AI is already showing wrong prices or wrong domain links for a market, see the troubleshooting entries below."""
f = f.replace(old_markets, new_markets)
results["kb/case/ai-wrong-responses.md"] = f

# ---- #15 PARTIAL: email-channel-issues.md — change/CC notification email ----
f = rd("kb__case__email-channel-issues.md")
old_multi = """## Multiple Email Addresses

Chatty supports **one email per store** via forwarding. For additional email addresses, set up email forwarding from alias addresses to the connected Chatty email.

Contact support if you have specific needs around multiple email addresses or alias setups."""
assert f.count(old_multi) == 1
new_multi = """## Multiple Email Addresses

Chatty supports **one email per store** via forwarding. For additional email addresses, set up email forwarding from alias addresses to the connected Chatty email.

**Merchant wants notifications to go to a different/additional address** (e.g.
notifications go to `sales@...` but they want `info@...`): this is self-serve, not
an escalation —
1. Go to **Channels → Email → Email sender** settings
2. Either **replace** the verified sender with the new address (triggers
   re-verification), or **add the second address in CC** underneath it

Contact support if you have specific needs around multiple email addresses or alias setups beyond this."""
f = f.replace(old_multi, new_multi)
results["kb/case/email-channel-issues.md"] = f

# ---- write payloads ----
ops = [{"agent": AGENT, "path": p, "content": content}
       for p, content in results.items()]
json.dump(ops, open(OUT, "w"), ensure_ascii=False)
print(f"wrote {len(ops)} payloads -> {OUT}")
for o in ops:
    print(f"  {o['path']}: {len(o['content'])} bytes")
