#!/usr/bin/env python3
"""
build_chatty_2026-07-19.py — build KB patch payloads for chatty-agent from the
mined FAQ file chatty_2026-07-13_2026-07-19.md.

Every operation asserts its anchor exists, so a moved heading fails loudly.
Output: reports/analysis/kb-sync-chatty-2026-07-19-payloads.json
"""
import json
import os

AGENT = "chatty-agent"
CACHE = "/tmp/kb-sync/chatty"
OUT = os.path.expanduser(
    "~/CSL/reports/analysis/kb-sync-chatty-2026-07-19-payloads.json")

files = {}


def load(path):
    if path not in files:
        flat = path.replace("/", "__")
        with open(os.path.join(CACHE, flat), encoding="utf-8") as fh:
            files[path] = fh.read()
    return files[path]


def sub(path, old, new, count=None):
    """Exact-string replace. Asserts old is present (and count if given)."""
    text = load(path)
    n = text.count(old)
    assert n > 0, f"ANCHOR MISSING in {path}: {old[:80]!r}"
    if count is not None:
        assert n == count, f"{path}: expected {count} of {old[:50]!r}, found {n}"
    files[path] = text.replace(old, new)


def insert_before(path, heading, block):
    """Insert block immediately before an existing '## heading' line."""
    text = load(path)
    assert heading in text, f"ANCHOR MISSING in {path}: {heading!r}"
    files[path] = text.replace(heading, block.rstrip() + "\n\n" + heading, 1)


def append(path, block):
    files[path] = load(path).rstrip() + "\n\n" + block.rstrip() + "\n"


# ---------------------------------------------------------------------------
# 1. OUTDATED — plan limits. Verified against chatty.net/pricing (2026-07-20):
#    Basic products 500 (KB said 1,500), Plus URLs & files 700 (KB said
#    unlimited), Basic chat history 12 months (KB said unlimited), Plus $199.
# ---------------------------------------------------------------------------
OLD_LIMITS = "(Free: 200, Basic: 1,500, Pro: 8,000, Plus: Unlimited)"
NEW_LIMITS = "(Free: 200, Basic: 500, Pro: 8,000, Plus: Unlimited)"

sub("kb/faq/ai-training-setup.md", "| Basic | 1,500 products |",
    "| Basic | 500 products |", count=1)
sub("kb/faq/ai-training-setup.md", OLD_LIMITS, NEW_LIMITS, count=1)
sub("kb/case/ai-product-sync.md", OLD_LIMITS, NEW_LIMITS, count=1)
sub("kb/case/ai-sync-issues.md", OLD_LIMITS, NEW_LIMITS, count=2)

PROD_ROW = "| Products for AI training | 200 | 1,500 | 8,000 | Unlimited |"
PROD_ROW_FIXED = "| Products for AI training | 200 | 500 | 8,000 | Unlimited |"
sub("kb/faq/knowledge-base.md", PROD_ROW, PROD_ROW_FIXED, count=1)
sub("kb/case/ai-product-limit.md", PROD_ROW, PROD_ROW_FIXED, count=1)

# Plus URLs & files: Unlimited -> 700
sub("kb/case/ai-product-limit.md",
    "| URL & File | 20 | 50 | 500 | Unlimited |",
    "| URL & File | 20 | 50 | 500 | 700 |", count=1)
sub("kb/faq/pricing.md",
    "URLs & files unlimited, team members unlimited",
    "URLs & files 700, team members unlimited", count=1)

# Extension baseline table must follow the corrected limits
sub("kb/case/ai-product-limit.md",
    "| Free | 1,500 (= Basic) | 1,000 (= Basic) | 50 (= Basic) |",
    "| Free | 500 (= Basic) | 1,000 (= Basic) | 50 (= Basic) |", count=1)
sub("kb/case/ai-product-limit.md",
    "| Pro | Unlimited (= Plus) | Already Unlimited | Unlimited (= Plus) |",
    "| Pro | Unlimited (= Plus) | Already Unlimited | 700 (= Plus) |", count=1)

# knowledge-base.md plan table: Plus price + Basic chat history + URLs row
sub("kb/faq/knowledge-base.md", "Plus ($199.99/mo)", "Plus ($199/mo)", count=1)
sub("kb/faq/knowledge-base.md",
    "| Chat history | 90 days | Unlimited | Unlimited | Unlimited |",
    "| Chat history | 90 days | 12 months | Unlimited | Unlimited |", count=1)
sub("kb/faq/knowledge-base.md", PROD_ROW_FIXED,
    PROD_ROW_FIXED + "\n| URLs & files for AI training | 20 | 50 | 500 | 700 |",
    count=1)

# ---------------------------------------------------------------------------
# 2. OUTDATED — stale web app domain (1 occurrence, verified)
# ---------------------------------------------------------------------------
sub("kb/faq/inbox.md", "app.meetchatty.com", "app.chatty.net", count=1)

# ---------------------------------------------------------------------------
# 3. OUTDATED — retention stated as a flat 90 days; it is per-plan
# ---------------------------------------------------------------------------
sub("kb/faq/ai-compliance.md",
    "- **How long is data stored?** Default retention is 90 days. "
    "You can adjust this in your settings.",
    "- **How long is chat history stored?** Retention depends on the plan: "
    "90 days on Free, 12 months on Basic, unlimited on Pro and Plus. "
    "Chat history retention is not adjustable in settings.", count=1)

# ---------------------------------------------------------------------------
# 4. OUTDATED — anonymous visitor names: workarounds exist today
# ---------------------------------------------------------------------------
sub("kb/faq/inbox.md",
    "This is a feature request currently under review. As a workaround, "
    "filter your inbox by segment to identify anonymous contacts.",
    "Anonymous visitors are given a random nickname (\"Grateful dream\", "
    "\"thunder flake\"). Two things can be done today:\n\n"
    "1. **Stop the name reaching the customer** — remove the "
    "`{{customer_name}}` variable from **AI agent → Settings → AI identity → "
    "Welcome message**. The nickname then only appears in your inbox.\n"
    "2. **Switch to a fixed label** — a fixed \"Anonymous-xxx\" format can be "
    "enabled on the account on request; contact support.\n\n"
    "To capture real names instead, enable the pre-chat form "
    "(**Chatbox → Chat page → Pre-chat Form**) with Name required.", count=1)

# ---------------------------------------------------------------------------
# 5. GAP / PARTIAL — new sections
# ---------------------------------------------------------------------------
insert_before("kb/faq/chatbox-settings.md", "## Adjusting Widget Position", """
## Which Welcome Message Am I Editing? (Three Places, One Wins)

Merchants very often edit the wrong field and conclude the change "didn't
save". There are three separate welcome messages, and they override each other
in this order:

1. **Settings → Translations → [language] → AI Agent / Live chat** — each
   published language keeps its own copy and **overrides both of the others**
   for visitors in that language. This is the most common reason an edit
   appears to do nothing.
2. **AI agent → Settings → AI identity → Welcome message** — used whenever the
   AI agent is on, and overrides the chatbox greeting.
3. **Chatbox → Chat page → Welcome message** — used only when the AI agent is
   off.

A **Proactive Chat** campaign can also show a separate pop-up teaser; that text
is edited in the Proactive chat section, not here.

**To fix:** change the value at the highest level that applies (Translations
first if any language is published), then reload the storefront in a private
window to confirm.
""")

insert_before("kb/case/ai-wrong-responses.md", "## AI Mixing Up Similar FAQs", """
## AI Still Gives the Old Answer After the FAQ Was Updated

The merchant edited a FAQ or Custom knowledge entry, but the AI keeps quoting
the previous answer. In most cases this week the edited entry was not the one
the AI was reading. Check in this order:

1. **Conversation starters** — each starter carries **its own answer**,
   independent of the FAQ list. A stale shipping time or policy usually lives
   here. Update the starter itself under **Chatbox → Chat page → Conversation
   starters**.
2. **Settings → Translations → [language]** — each published language stores
   its own copy of the text and overrides the main settings for visitors in
   that language.
3. **Other entries on the same topic** — a duplicate FAQ or Custom knowledge
   entry may still hold the old fact. Run **Review sources** on the failing
   question to see which entry the AI actually used.
4. **Reset the conversation and retest** — an open chat keeps the knowledge it
   loaded when it started and will not reflect a fresh edit.

If a freshly reset conversation still returns the old answer after the correct
source is fixed, collect the question, a screenshot and the Review sources
output, and escalate.
""")

insert_before("kb/faq/data-sources.md", "## Adding & Managing Data Sources", """
## FAQs vs Custom Knowledge vs Instructions vs Scenarios

Merchants regularly put the right content in the wrong place. The rule of
thumb: **facts go in Training data, behaviour goes in Instructions,
situation-specific handling goes in Scenarios.**

| Type | What it is | Customer-visible? |
|---|---|---|
| **FAQs** | Q&A pairs shown on the FAQs page and blocks, and used by the AI | Yes — browsable list |
| **Custom knowledge** | Q&A pairs, URLs and files the AI learns from | No — used in chat only |
| **Instructions** | The AI's role, tone, boundaries and what it must never discuss | No |
| **Custom scenarios** | Handling rules for specific situations (e.g. refund requests) | No |

Notes:
- Custom knowledge is never shown to customers as a list — use it for internal
  detail you want the AI to know but not publish.
- Custom scenarios are capped at 1,000 characters each.
- To make the AI answer something without publishing it on the storefront, add
  it under **Custom knowledge** only and leave it off the FAQ page and blocks.
""")

insert_before("kb/faq/analytics.md", "## Verifying Assisted Revenue & Order Attribution", """
## Why My Analytics Numbers Look Wrong (Metric Definitions)

Most disputes come from the metric definition rather than a counting error:

- **Handled Conversations** counts only replies made **within 24 hours** of the
  customer's message. Replying to an older backlog does not increment it, so
  the figure can look lower than the work actually done.
- **First Response Time** is a **median** across conversations that received a
  **human** reply. Automated replies and stale backlog replies are excluded.
- **Total conversations = 0** almost always means the **Live chat block is off**
  (**Chatbox → General → Blocks**) — with no way to start a chat, no
  conversations can be created.

If the numbers still don't reconcile, collect the store URL and the exact
period and escalate — collect a screenshot of the figure being disputed.
""")

append("kb/faq/mobile-app.md", """
## Inbox Crashes or Won't Load on Mobile

There are active reports on both Android and iOS of the inbox crashing or
lagging when opening a conversation. This is with the dev team.

**Collect before escalating:** device model, OS version, browser, whether the
app is the installed PWA or a browser tab, and a short screen recording.

**Workaround:** the desktop web app at **app.chatty.net** is unaffected. If the
installed app shortcut opens a blank screen, open app.chatty.net in the browser
and re-install from there — the installed session can go stale.
""")

insert_before("kb/faq/faqs-page.md", "## Set Up the Contact Us Section", """
## "The FAQs Page URL Has Already Been Taken"

The FAQ page won't activate because an existing Shopify page already uses that
handle — usually a leftover from a previous install, or a page that was deleted
and recreated.

1. Check **Shopify Admin → Online Store → Pages** for a page on the same
   handle (default `/pages/avada-faqs`).
2. Remove or rename the conflicting page.
3. Re-enable the FAQs page in Chatty.

If it persists, collect the store URL — the team can change the FAQ page URL
from the backend.
""")

insert_before("kb/case/whatsapp-messenger-issues.md", "## Instagram Story Reply Errors", """
## Can't Reply to a Messenger / Instagram Customer (Meta 24-Hour Window)

Meta enforces a **24-hour messaging window**. If the customer's last message is
more than 24 hours old, Meta blocks the reply — this is Meta platform policy
and cannot be extended from Chatty.

Advise the merchant to reply within the window, and to capture an email address
during the conversation as a second route for slower follow-ups.
""")

insert_before("kb/faq/ai-conversations.md", "## Session Mechanics", """
## Common Surprises in How Conversations Are Counted

- The allowance is **store-wide per month and shared across every channel**
  (website, Messenger, Instagram, WhatsApp) — it is not per customer.
- The **product-page AI assistant creates conversations that count** whenever
  the AI gives a valid response. Turning off suggested questions on product
  pages reduces this volume.
- **Resetting a conversation starts a new one**, which consumes allowance.
""")

insert_before("kb/faq/translation.md", "## Real-Time Conversation Translation", """
## A Published Translation Overrides Your Main Settings

Each published language keeps **its own copy** of the chatbox messages, AI
welcome message, conversation starters and FAQ text. A translated string that
was not refreshed will silently override a newer edit made in the main
settings.

This is the usual cause of "I edited the welcome message but the old one still
shows" and "the AI still quotes the old shipping time". After changing any
customer-facing text, re-check **Settings → Translations → [language]** for
every published language.

Note also that **Auto-translate is not available on every plan** — on lower
tiers each field must be translated manually.
""")

sub("kb/faq/faqs-block.md",
    "or a **Custom URL**",
    "or a **Custom URL** (enter the **path only**, e.g. `/pages/contact-us` — "
    "a full URL fails with \"Custom URL page is invalid\")")

sub("kb/case/chatbox-widget-issues.md",
    "- Exact URL → hide on one specific page",
    "- Exact URL → hide on one specific page. Enter the **path only** "
    "(e.g. `/pages/contact-us`), not the full URL — a full URL returns "
    "\"Custom URL page is invalid\".", count=1)

insert_before("kb/case/notification-issues.md", "## No Notification Sound (Banners Appear, Sound Doesn't Play)", """
## Web Push Subscription Is Per Browser and Per Device

A common cause of "notifications just stopped": the web push subscription is
tied to **one browser on one device**. Reinstalling the OS, switching browsers
or moving to a new machine requires subscribing again.

- Re-subscribe from **inside the app**, not from browser settings. If the
  permission popup never appears, allow notifications in the browser's site
  settings first, then subscribe in the app.
- Use **Send test** to confirm the subscription is live.
- An **unverified notification email address silently stops email
  notifications** — check its verification status.
- **Not available:** SMS notifications, and notifications for CSAT ratings.
  Both are logged as feature requests.

Keep email notifications on as a safety net while troubleshooting.
""")

append("persona/facts.md", """
## When the Person Chatting Is a Shopper, Not a Merchant

This inbox reaches **Chatty's support team**, not the merchant's store. Some
shoppers land here after using a Chatty-powered widget on a store.

- Do **not** attempt to answer "what's your bestseller", "where's my order", or
  any catalog, order or sales question — we have no access to the merchant's
  store data.
- If they are a **merchant testing their own AI agent**, redirect them to
  **AI agent → Test AI** in the app, or to their live storefront widget, which
  is connected to their training data and shows what customers actually see.
- If they are a genuine shopper, politely point them back to the store they
  were trying to reach.
""")

# ---------------------------------------------------------------------------
payloads = [{"agent": AGENT, "path": p, "content": c}
            for p, c in sorted(files.items())]
os.makedirs(os.path.dirname(OUT), exist_ok=True)
with open(OUT, "w", encoding="utf-8") as fh:
    json.dump(payloads, fh, ensure_ascii=False, indent=2)
print(f"Wrote {len(payloads)} file payload(s) -> {OUT}")
for p in sorted(files):
    print(f"  - {p}")
