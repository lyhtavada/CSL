#!/usr/bin/env python3
"""
build_chatty_2026-06-28.py — KB-patch payload builder for the Chatty CS-agent KB.

REVIEW-GATE run: builds the payloads JSON only. Does NOT push, does NOT call kb_api,
does NOT reindex.

Pattern (see references/build-example.py):
  - Start from the CACHED live file in /tmp/kb-sync/chatty/ (flattened name).
  - assert each anchor / occurrence-count BEFORE replacing, so a moved heading or a
    miscount fails loudly instead of silently emitting an unchanged file.
  - Emit FULL new file content per changed file; one payload entry per file.

Correct current plan facts (source of truth for this run):
  Free   $0       : 50 AI conv LIFETIME (does not reset), 100 products, 90-day history
  Basic  $19.99/mo: 50 AI conv/mo, 500 products, 5 team members total, 12-month history
  Pro    $68.99/mo: 300 AI conv/mo, 8,000 products, 10 team members total, unlimited history
  Plus   $199/mo  : 700 AI conv/mo, 20,000 products, unlimited team members, unlimited history
  $0.40 per extra conversation (paid plans); 7-day free trial.
"""
import json
import os

APP = "chatty"
AGENT = "chatty-agent"
DATE = "2026-06-28"
SRC = f"/tmp/kb-sync/{APP}"
OUT = os.path.expanduser(
    f"~/CSL/reports/analysis/kb-sync-{APP}-{DATE}-payloads.json")


def rd(flat):
    return open(os.path.join(SRC, flat)).read()


def rep(text, old, new, n):
    """Assert exactly n occurrences of `old`, then replace all of them."""
    c = text.count(old)
    assert c == n, f"expected {n}x {old!r}, found {c}"
    return text.replace(old, new)


results = {}  # real path -> new full content


# ============================================================
# kb/faq/pricing.md  — OUTDATED facts #1,#3,#4
# ============================================================
f = rd("kb__faq__pricing.md")

# Free: "50 AI conversations/month (resets monthly)" — L98 plan list (1x)
f = rep(f, "50 AI conversations/month (resets monthly)",
        "50 AI conversations lifetime (does not reset monthly)", 1)
# L108 comparison line uses a different word order
f = rep(f, "**Free:** AI conversations 50/month (resets monthly), products 200",
        "**Free:** AI conversations 50 lifetime (does not reset monthly), products 100", 1)
# Free AI Conversation Limits section line (L133)
f = rep(f, "**Free:** 50/month — resets monthly (no extra conversations available)",
        "**Free:** 50 lifetime — does not reset monthly (no extra conversations available)", 1)
# Free "limit reached" paragraph still implies monthly reset (L138)
f = rep(
    f,
    "**When Free plan limit is reached:** The AI agent pauses for the rest of the month and the quota resets to 50 at the start of the next month. Conversations can still be handled manually in Inbox in the meantime.",
    "**When Free plan limit is reached:** The Free 50 AI conversations are a lifetime allowance — they do not reset monthly. Once used up, the AI agent stops and the merchant must upgrade to a paid plan for more. Conversations can still be handled manually in Inbox in the meantime.",
    1)

# Products: Free 200 -> 100
f = rep(f, "200 products, 1 team member", "100 products, 1 team member", 1)  # L98 plan list
f = rep(f, "products 200, custom answers 100", "products 100, custom answers 100", 1)  # L108
# Basic products 1,500 -> 500
f = rep(f, "1,500 products, 5 team members", "500 products, 5 team members", 1)  # L99
f = rep(f, "products 1,500, custom answers 1,000", "products 500, custom answers 1,000", 1)  # L110
# Plus products Unlimited -> 20,000
f = rep(f, "unlimited products, unlimited team members", "20,000 products, unlimited team members", 1)  # L101
f = rep(f, "products unlimited, custom answers unlimited, URLs & files unlimited, team members unlimited",
        "products 20,000, custom answers unlimited, URLs & files unlimited, team members unlimited", 1)  # L114

# AI conv monthly counts: Basic 100->50, Pro 500->300, Plus 1,000->700
# L99 Basic plan list
f = rep(f, "100 AI conversations/month + $0.40/extra, 500 products",
        "50 AI conversations/month + $0.40/extra, 500 products", 1)
# L100 Pro plan list
f = rep(f, "500 AI conversations/month + $0.40/extra, 8,000 products",
        "300 AI conversations/month + $0.40/extra, 8,000 products", 1)
# L101 Plus plan list
f = rep(f, "1,000 AI conversations/month + $0.40/extra, 20,000 products",
        "700 AI conversations/month + $0.40/extra, 20,000 products", 1)
# L110 Basic comparison
f = rep(f, "AI conversations 100/month + $0.40/extra, products 500",
        "AI conversations 50/month + $0.40/extra, products 500", 1)
# L112 Pro comparison
f = rep(f, "AI conversations 500/month + $0.40/extra, products 8,000",
        "AI conversations 300/month + $0.40/extra, products 8,000", 1)
# L114 Plus comparison
f = rep(f, "AI conversations 1,000/month + $0.40/extra, products 20,000",
        "AI conversations 700/month + $0.40/extra, products 20,000", 1)
# AI Conversation Limits section (L134-136)
f = rep(f, "**Basic:** 100/month — extra at $0.40/conversation",
        "**Basic:** 50/month — extra at $0.40/conversation", 1)
f = rep(f, "**Pro:** 500/month — extra at $0.40/conversation",
        "**Pro:** 300/month — extra at $0.40/conversation", 1)
f = rep(f, "**Plus:** 1,000/month — extra at $0.40/conversation",
        "**Plus:** 700/month — extra at $0.40/conversation", 1)

results["kb/faq/pricing.md"] = f


# ============================================================
# kb/faq/ai-conversations.md — OUTDATED #1,#4
# ============================================================
f = rd("kb__faq__ai-conversations.md")

# Overage table rows
f = rep(f, "| Free | 50/month (resets monthly) | Not available |",
        "| Free | 50 lifetime (does not reset monthly) | Not available |", 1)
f = rep(f, "| Basic | 100/month | $0.40/each |",
        "| Basic | 50/month | $0.40/each |", 1)
f = rep(f, "| Pro | 500/month | $0.40/each |",
        "| Pro | 300/month | $0.40/each |", 1)
f = rep(f, "| Plus | 1,000/month | $0.40/each |",
        "| Plus | 700/month | $0.40/each |", 1)
results["kb/faq/ai-conversations.md"] = f


# ============================================================
# kb/case/ai-conversation-limit.md — OUTDATED #1,#2,#4
# ============================================================
f = rd("kb__case__ai-conversation-limit.md")

# #2 — reword the "monthly quota that resets each month (including Free)" overview line
f = rep(
    f,
    "AI conversation limits are a **monthly quota** that resets each month (including the Free plan).",
    "On paid plans, AI conversation limits are a **monthly quota** that resets each billing cycle. The Free plan's 50 AI conversations are a **lifetime** allowance that does **not** reset monthly.",
    1)
# Plan Limits Reference table — Free row + monthly counts
f = rep(
    f,
    "| Free | 50/month (resets monthly; AI pauses when reached, resumes next cycle) |",
    "| Free | 50 lifetime (does not reset; AI stops when reached — upgrade for more) |",
    1)
f = rep(f, "| Basic | 100/month + $0.40/extra |",
        "| Basic | 50/month + $0.40/extra |", 1)
f = rep(f, "| Pro | 500/month + $0.40/extra |",
        "| Pro | 300/month + $0.40/extra |", 1)
f = rep(f, "| Plus | 1,000/month + $0.40/extra |",
        "| Plus | 700/month + $0.40/extra |", 1)
results["kb/case/ai-conversation-limit.md"] = f


# ============================================================
# kb/case/ai-wrong-responses.md — OUTDATED #1 (L144) + GAP Q12
# ============================================================
f = rd("kb__case__ai-wrong-responses.md")

# #1 — Free plan 50/month line
f = rep(
    f,
    "   - Free plan = 50 conversations/month (resets monthly) — when hit, AI pauses until the next cycle",
    "   - Free plan = 50 AI conversations lifetime (does not reset monthly) — when used up, AI stops until the merchant upgrades to a paid plan",
    1)

# GAP Q12 — product links using .myshopify.com; insert before the Market-Domain section anchor
anchor_md = "## AI Showing Main Domain Instead of Market Domain"
assert anchor_md in f, "missing Market Domain anchor"
q12 = """## AI Product Links Use .myshopify.com Instead of the Primary Domain

Collection and page links use the store's primary domain correctly, but **product
links specifically** can sometimes fall back to the `vendor.myshopify.com` URL.

**First-line fix:**
1. Confirm the store's primary domain in **Shopify → Settings → Domains** (it should be
   the custom domain, set as primary — not the `.myshopify.com` address).
2. Trigger a product **re-sync** in **AI agent → Training data → Manage → Products**.

**If product links still show the `.myshopify.com` URL after re-sync**, this is a known
product-URL-handling issue. Escalate to the team with:
- Conversation ID (or customer name/email in that chat)
- An example product link the AI returned (the `.myshopify.com` one)
- The store's correct primary domain

"""
f = f.replace(anchor_md, q12 + anchor_md, 1)
results["kb/case/ai-wrong-responses.md"] = f


# ============================================================
# kb/faq/knowledge-base.md — OUTDATED #1,#3,#4,#6,#7
# ============================================================
f = rd("kb__faq__knowledge-base.md")

# #6 — Plus price $199.99/mo -> $199/mo (header table)
f = rep(f, "Plus ($199.99/mo)", "Plus ($199/mo)", 1)

# #4 + #1 — AI conversations table row: Basic 100->50, Pro 500->300, Plus 1,000->700, Free note lifetime
f = rep(
    f,
    "| AI conversations | 50/month | 100/month | 500/month | 1,000/month |",
    "| AI conversations | 50 lifetime | 50/month | 300/month | 700/month |",
    1)
# #3 — products row: Free 200->100, Basic 1,500->500, Plus Unlimited->20,000
f = rep(
    f,
    "| Products for AI training | 200 | 1,500 | 8,000 | Unlimited |",
    "| Products for AI training | 100 | 500 | 8,000 | 20,000 |",
    1)
# #7 — Chat history row: Basic column Unlimited -> 12 months
f = rep(
    f,
    "| Chat history | 90 days | Unlimited | Unlimited | Unlimited |",
    "| Chat history | 90 days | 12 months | Unlimited | Unlimited |",
    1)
results["kb/faq/knowledge-base.md"] = f


# ============================================================
# kb/case/ai-product-limit.md — OUTDATED #3
# ============================================================
f = rd("kb__case__ai-product-limit.md")

# Plan Limits Reference table: Products row Free 200->100, Basic 1,500->500, Plus Unlimited->20,000
f = rep(
    f,
    "| Products for AI training | 200 | 1,500 | 8,000 | Unlimited |",
    "| Products for AI training | 100 | 500 | 8,000 | 20,000 |",
    1)
# Step 2 extension table: Free -> Basic products "1,500 (= Basic)" ; Basic -> Pro "8,000 (= Pro)" unchanged;
# Pro -> Plus "Unlimited (= Plus)" -> "20,000 (= Plus)"
f = rep(f, "| Free | 1,500 (= Basic) |", "| Free | 500 (= Basic) |", 1)
f = rep(f, "Unlimited (= Plus) | Already Unlimited | Unlimited (= Plus) |",
        "20,000 (= Plus) | Already Unlimited | Unlimited (= Plus) |", 1)
results["kb/case/ai-product-limit.md"] = f


# ============================================================
# kb/case/ai-product-sync.md — OUTDATED #3
# ============================================================
f = rd("kb__case__ai-product-sync.md")
f = rep(f,
        "(Free: 200, Basic: 1,500, Pro: 8,000, Plus: Unlimited)",
        "(Free: 100, Basic: 500, Pro: 8,000, Plus: 20,000)", 1)
results["kb/case/ai-product-sync.md"] = f


# ============================================================
# kb/case/ai-sync-issues.md — OUTDATED #3 (recurring string x2)
# ============================================================
f = rd("kb__case__ai-sync-issues.md")
f = rep(f,
        "(Free: 200, Basic: 1,500, Pro: 8,000, Plus: Unlimited)",
        "(Free: 100, Basic: 500, Pro: 8,000, Plus: 20,000)", 2)
results["kb/case/ai-sync-issues.md"] = f


# ============================================================
# kb/faq/ai-training-setup.md — OUTDATED #3 + PARTIAL Q5
# ============================================================
f = rd("kb__faq__ai-training-setup.md")
# #3 — recurring product string (Plan Product Limit Too Low section, L415)
f = rep(f,
        "(Free: 200, Basic: 1,500, Pro: 8,000, Plus: Unlimited)",
        "(Free: 100, Basic: 500, Pro: 8,000, Plus: 20,000)", 1)

# PARTIAL Q5 — CSV "Failed" rows; insert before the Uploading Files anchor
anchor_up = "## Uploading Files for AI Training"
assert anchor_up in f, "missing Uploading Files anchor"
q5 = """## CSV Import Shows Questions as "Failed"

When a CSV import of FAQ/Q&A content shows rows as **"Failed,"** the usual cause is that
the **topic was set to Published but not Active**. The import targets an inactive topic,
so the rows can't be applied.

**Fix:**
1. Open the topic and set it to **Active** (not just Published).
2. Re-check the CSV file for the failed rows, correct any formatting issues.
3. **Re-upload** the file.

If the failed rows can't be deleted from within the app, contact support so the team can
clear them on the backend.

"""
f = f.replace(anchor_up, q5 + anchor_up, 1)
results["kb/faq/ai-training-setup.md"] = f


# ============================================================
# kb/faq/team.md — OUTDATED #5 + PARTIAL Q26
# ============================================================
f = rd("kb__faq__team.md")
# #5 — seat lines L54-55
f = rep(f, "- **Basic**: 2 additional members (3 total)",
        "- **Basic**: 5 members total", 1)
f = rep(f, "- **Pro**: 4 additional members (5 total)",
        "- **Pro**: 10 members total", 1)

# PARTIAL Q26 — email-only CRM / seats without a Shopify plan.
# Insert as a new section just before "## Multiple Team Members Using Chatty Simultaneously"
anchor_team = "## Multiple Team Members Using Chatty Simultaneously"
assert anchor_team in f, "missing Multiple Team Members anchor"
q26 = """## Using Chatty as an Email-Only Shared CRM (Seats Without Shopify Staff Accounts)

You don't have to use live chat to add a team. You can connect just the **email channel**
and skip live chat, using Chatty as a shared CRM for your support team:

- Assign conversations to specific members, and label/tag them to organize work.
- Set an auto-signature per member.
- Team members log in directly at **app.chatty.net** — they do **not** need a Shopify
  staff seat. This means you can add CS people without paying for Shopify's higher plan
  just to add staff accounts.

**Seats by plan:** Basic 5, Pro 10, Plus unlimited.

"""
f = f.replace(anchor_team, q26 + anchor_team, 1)
results["kb/faq/team.md"] = f


# ============================================================
# kb/faq/inbox.md — OUTDATED #8 + GAP Q7 (+ Q7 cross-link)
# ============================================================
f = rd("kb__faq__inbox.md")
# #8 — web-app URL
f = rep(f, "app.meetchatty.com", "app.chatty.net", 1)

# GAP Q7 — 404 / inbox-crash / mis-routing defect.
# Insert a new section near the existing Mixing/Lagging heading (before it).
anchor_mix = "## Conversations Mixing Between Threads / Inbox Lagging"
assert anchor_mix in f, "missing Mixing/Lagging anchor"
q7 = """## 404 / "Technical problem with Avada app" / Inbox Crash (system-side defect)

A recognized system-side defect. Symptoms (one or more may appear together):
- Opening a chat, or the **Resolved** or **Open** tab, throws **"404 / page not found /
  technical problem with Avada app"**.
- Old resolved chats reappear as **unread**.
- New chats land in the **Resolved** tab instead of Open.
- The **Resolve** button shows **"Reopen"** and won't close the conversation.
- The inbox **crashes mid-chat**.
- Two different customers' messages appear in one thread.

**First-line:**
1. Have the merchant **hard-refresh / reload** the page and try in an **incognito**
   window — this clears the transient 404 for some merchants.
2. If the 404 persists, or any of the other symptoms above appear, collect and escalate
   to **dev as P1**:
   - Conversation / session IDs
   - Affected customer emails
   - Screenshot or Loom of the behavior
   - Store URL and timestamps

Do **not** advise reinstalling — it won't fix this and risks losing the merchant's setup.

"""
f = f.replace(anchor_mix, q7 + anchor_mix, 1)

# Q7 cross-link — add a one-line pointer inside the existing Mixing/Lagging paragraph.
mix_para = "Cases where messages appear to **mix between different conversation threads** are treated as **high-priority and escalated to the dev team** for investigation. If a merchant experiences this, collect the affected **conversation IDs** and escalate so the team can investigate thoroughly."
assert mix_para in f, "missing Mixing paragraph text"
f = f.replace(
    mix_para,
    mix_para + "\n\n> This is likely the same root-cause defect as the 404 / inbox-crash issue above — see **404 / \"Technical problem with Avada app\" / Inbox Crash**.",
    1)
results["kb/faq/inbox.md"] = f


# ============================================================
# kb/faq/live-chat.md — GAP Q11 + PARTIAL Q14
# ============================================================
f = rd("kb__faq__live-chat.md")

# GAP Q11 — AI replying after a human agent Joined; sibling of "AI Not Resuming After Human Takeover"
anchor_resume = "## AI Not Resuming After Human Takeover"
assert anchor_resume in f, "missing AI Not Resuming anchor"
q11 = """## AI Keeps Replying After a Human Agent Joined (Talks Over the Agent)

When an agent clicks **Join** on a conversation, the AI is meant to step back and let the
human handle it. If the AI keeps posting over a joined agent:

**Workaround / checks:**
1. Make sure the agent actually uses **Join / assign** on the conversation (not just
   starts typing) — joining is what signals the AI to stop.
2. Check **AI availability** (AI agent → Settings → AI availability): if it's set to
   **Always**, the AI may reply even alongside an agent. Set it to **Only when agents
   are offline** if the team wants the AI to defer to humans.

If the AI still posts over a **joined / assigned** agent, this is a recognized defect.
Escalate with:
- Conversation ID
- Which agent joined
- Whether the chat was assigned to that agent

"""
f = f.replace(anchor_resume, q11 + anchor_resume, 1)

# PARTIAL Q14 — open straight into chat / skip the home screen.
# Insert before the "Customer Conversation Reset" section near the end.
anchor_reset = "## Customer Conversation Reset"
assert anchor_reset in f, "missing Customer Conversation Reset anchor"
q14 = """## Open Directly Into the AI Chat (Skip the Home Screen)

To make the chatbox open straight into the AI conversation instead of the home/menu
screen:
1. In **Chatbox**, trim or remove the **conversation starters** so there's no intro menu
   to land on.
2. Turn **off** the pre-chat form (or allow **"Chat with us as anonymous"**) so customers
   aren't stopped to enter details first.
3. Ensure the **Live chat / AI** block is enabled so the message box appears immediately.

"""
f = f.replace(anchor_reset, q14 + anchor_reset, 1)
results["kb/faq/live-chat.md"] = f


# ============================================================
# kb/faq/ai-agent-settings.md — GAP Q20 (Suggest Reply Beta)
# ============================================================
f = rd("kb__faq__ai-agent-settings.md")
# Insert before the Embed Product AI Agent section (a sibling top-level section).
anchor_embed = "## Embed Product AI Agent"
assert anchor_embed in f, "missing Embed Product AI Agent anchor"
q20 = """## Suggest Reply (Beta)

**Suggest reply** is a Beta capability that drafts a reply for the agent to review before
sending: the AI generates a suggested response, a human reviews (and edits) it, and the
human clicks **Send**. It's rolling out to select merchants.

**Current limitations (Beta):**
- Drafted-email formatting and spacing are still rough.
- Suggestions aren't always accurate — the agent must review before sending.

**Handling:** Log a merchant's interest so they can be opted in. Until it reaches GA,
guide merchants to keep the AI **off for the company email channel** (where every email
could otherwise auto-reply incorrectly) and use Suggest reply on **live chat**, where an
agent supervises each suggestion before it goes out.

"""
f = f.replace(anchor_embed, q20 + anchor_embed, 1)
results["kb/faq/ai-agent-settings.md"] = f


# ============================================================
# kb/case/chatbox-widget-issues.md — PARTIAL Q22
# ============================================================
f = rd("kb__case__chatbox-widget-issues.md")
anchor_slow = "## Chat Slow to Load on Mobile"
assert anchor_slow in f, "missing Chat Slow anchor"
q22 = """## AI Latency vs. Storefront/Page-Speed Slowdown (incl. Refund Requests)

Distinguish two different "slow" reports:

**(1) AI response latency.** On large catalogs the AI can take **10–30 seconds** to
respond. Capture the store URL, an example question, the browser used, and the timing,
then escalate to the team.

**(2) Storefront / page-speed slowdown blamed on the widget.** When a merchant says the
Chatty widget is slowing down their store — especially when it drives a **cancel or
refund request** — treat it seriously. Do not dismiss it:
- Gather evidence: Shopify performance data and/or a **Lighthouse** report, the affected
  pages, and any before/after comparison.
- Escalate to **TS** to assess the widget's actual impact on page speed.
- Route the **refund** through the standard refund process rather than refusing it.

"""
f = f.replace(anchor_slow, q22 + anchor_slow, 1)
results["kb/case/chatbox-widget-issues.md"] = f


# ============================================================
# kb/faq/klaviyo.md — PARTIAL Q30
# ============================================================
f = rd("kb__faq__klaviyo.md")
anchor_api = "## Chatty Public API"
assert anchor_api in f, "missing Chatty Public API anchor"
q30 = """## Public API Base URL, Bulk Export, Mailchimp & Zoho

- **Base URL / auth:** Provide these from the official Chatty API docs
  (https://help.chatty.net/integrations/chatty-public-api) — don't quote a base URL or
  auth scheme from memory.
- **Bulk / full-conversation export:** There is **no API endpoint** for this today — it's
  handled via support (give the date range and the team exports the data).
- **Mailchimp:** No native integration. Export **Leads / contacts as CSV** and import into
  Mailchimp, or use **Klaviyo** where supported. Log Mailchimp as a feature request.
- **Zoho Desk:** No native integration either. Same approach — CSV export/import or
  Klaviyo. Log Zoho Desk as a feature request.

"""
f = f.replace(anchor_api, q30 + anchor_api, 1)
results["kb/faq/klaviyo.md"] = f


# ============================================================
# write payloads
# ============================================================
ops = [{"agent": AGENT, "path": p, "content": content}
       for p, content in results.items()]
os.makedirs(os.path.dirname(OUT), exist_ok=True)
json.dump(ops, open(OUT, "w"), ensure_ascii=False, indent=None)
total_bytes = sum(len(o["content"]) for o in ops)
print(f"wrote {len(ops)} payloads -> {OUT}")
print(f"total content bytes: {total_bytes}")
for o in ops:
    print(f"  {o['path']}: {len(o['content'])} bytes")
