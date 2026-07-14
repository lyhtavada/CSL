#!/usr/bin/env python3
"""
build_chatty_2026-07-14.py — build KB payloads for Chatty/Ivy from the mined-FAQ
file chatty_2026-06-29_2026-07-05_new_only.md (12 new FAQs).

Covers: Q9 Q10 Q11 Q13 Q17 Q18 Q22 Q24 Q26 Q28 Q29 Q31 Q36 Q44 Q46
Plus 4 OUTDATED fixes:
  - kb/faq/knowledge-base.md      "powered by ChatGPT"       -> enterprise-grade LLM
  - kb/faq/inbox.md               "API does not support..."  -> API DOES support conversations/messages
  - kb/case/ai-product-sync.md    "AI agent -> Data Sources" -> AI agent -> Training data -> Manage -> Products
  - kb/case/email-channel-issues.md  admin email tied to Shopify owner -> team replaces it
Plus collaborator-code path update (Liz approved): Security -> Collaborator request code
  becomes the new Shopify Admin path (both forms listed).

Every replacement asserts its anchor exists — a moved heading fails loudly.
"""
import json
import os
import sys

CACHE = "/tmp/kb-sync/chatty"
AGENT = "chatty-agent"
OUT = os.path.expanduser(
    "~/CSL/reports/analysis/kb-sync-chatty-2026-07-14-payloads.json"
)

files = {}  # path -> content


def load(path):
    """Load a KB file into the working set (idempotent)."""
    if path not in files:
        flat = path.replace("/", "__")
        with open(os.path.join(CACHE, flat)) as f:
            files[path] = f.read()
    return files[path]


def sub(path, old, new, count=1):
    """Replace `old` with `new`, asserting `old` is present exactly `count` times."""
    c = load(path)
    n = c.count(old)
    if n != count:
        sys.exit(f"ANCHOR FAIL in {path}: expected {count}x, found {n}x:\n---\n{old[:160]}\n---")
    files[path] = c.replace(old, new, count)


def add_tags(path, new_tags):
    """Insert tags into the YAML `tags:` block (4-space indent, quoted)."""
    c = load(path)
    if "\ntags:\n" not in c:
        sys.exit(f"TAGS FAIL in {path}: no 'tags:' block")
    lines = c.split("\n")
    start = lines.index("tags:")
    i = start + 1
    while i < len(lines) and lines[i].startswith("    - "):
        i += 1
    existing = {l.strip().strip('- "') for l in lines[start + 1:i]}
    add = [f'    - "{t}"' for t in new_tags if t not in existing]
    files[path] = "\n".join(lines[:i] + add + lines[i:])


# ═══════════════════════════════════════════════════════════════════════════
# Q9 — AI can't find product from translated / market-domain URL
# GAP -> kb/case/ai-wrong-responses.md, after "AI Showing Main Domain..."
# ═══════════════════════════════════════════════════════════════════════════
P = "kb/case/ai-wrong-responses.md"
sub(P, """---

## AI Not Linking to Specific Variants""", """---

## AI Can't Find a Product from a Translated / Market Domain URL

**Symptom:** On a multi-market or multi-language store, the AI answers *"no information found"* for a product when the question contains a **translated or market-specific domain URL** (e.g. a `.pl` or `.fr` storefront link) — even though the product is Active and synced. Searching by **product name or SKU** in the same chat returns the product fine.

**Known limitation:** Chatty stores product data against the **main domain** only. A product URL from a translated/market domain doesn't resolve to the synced product, so lookup by that URL fails. This is the URL format failing — not a sync or training-data problem.

> Do NOT route this to the training-source/sync checks (see *AI Says "We Don't Have Information"*). If the merchant's failing question contained a market/translated-domain URL, the sync is fine and re-syncing will not help.

**Suggest workaround:**
- Reference products by **name or SKU** in customer conversations instead of pasting the translated-domain URL — this works today.

**Escalate to the team with:**
- Both store URLs (main domain + the translated/market domain)
- The product name and SKU
- An example of the failing question, exactly as asked

---

## AI Not Linking to Specific Variants""")

add_tags(P, ["translated domain", "multi-language store", "market URL",
             "product not found", "URL lookup", "SKU", "search by SKU"])

# Cross-link from the "We Don't Have Information" flow so the two don't collide
sub(P, '## AI Says "We Don\'t Have Information" Despite Data Being Added/Synced\n',
    '## AI Says "We Don\'t Have Information" Despite Data Being Added/Synced\n\n'
    '> **Check first:** if the failing question contained a **translated / market-domain product URL** '
    '(e.g. a `.pl` or `.fr` storefront link), stop here — see *AI Can\'t Find a Product from a Translated / '
    'Market Domain URL* below. The sync is fine; the URL format is what breaks the lookup.\n')

# ═══════════════════════════════════════════════════════════════════════════
# Q10 — AI still appears on translated pages after being turned off
# GAP -> kb/case/translation-issues.md, before "## AI Replies in the Wrong Language"
# ═══════════════════════════════════════════════════════════════════════════
P = "kb/case/translation-issues.md"
sub(P, """## AI Replies in the Wrong Language""", """---

## Symptom

The merchant deactivated the AI agent, but the AI still appears and replies on **translated (non-English) storefront pages**. On the default-language pages it is correctly off.

## Cause

Commonly caused by a third-party translation app overwriting Chatty's **metafields on the language variants** — the translated pages keep serving the old (AI-enabled) configuration.

## Resolution

1. Ask the merchant for the **URL(s) of the affected translated pages** and confirm which translation app they use.
2. Follow the collaborator access flow (`ref_collaborator-access.md`) — collect the collaborator code so the team can check the metafield configuration on those language variants.
3. Escalate to TS with: affected translated page URLs, translation app name, screenshot of the AI still showing, collaborator code (or note that the merchant declined and the team should send an access request directly).

> The merchant does not need to re-toggle the AI setting — flipping it again won't clear an overwritten metafield on the language variant.

---

## AI Replies in the Wrong Language""")

sub(P, 'applies_when: "Merchant reports FAQ page content doesn\'t change when customer switches language on the store"',
    'applies_when: "Merchant reports FAQ page content doesn\'t change when customer switches language on the store, '
    'or the AI still appears on translated pages after being turned off"')

add_tags(P, ["AI agent off", "AI still replying", "deactivated AI",
             "language variant", "metafields overwritten", "translated page",
             "AI on translated pages"])

# ═══════════════════════════════════════════════════════════════════════════
# Q11 — No notification SOUND (macOS + Chrome). Q13 — noti with all toggles off
# kb/case/notification-issues.md
# ═══════════════════════════════════════════════════════════════════════════
P = "kb/case/notification-issues.md"

# Q11 — insert after "Desktop Push Notifications Not Working" section
sub(P, """**Meanwhile:** Recommend email notifications or installing the Chatty mobile app as alternatives.

---

## Mobile App Notifications Not Working""", """**Meanwhile:** Recommend email notifications or installing the Chatty mobile app as alternatives.

---

## No Notification Sound (Banners Appear, Sound Doesn't Play)

Distinct from "no notifications at all" — here the **visual banner arrives but there is no sound**.

**Step 1: Check the sound settings in Chatty**
- **Settings → Notifications** → confirm the relevant triggers have **Web/desktop notifications on**, and click **Subscribe** if the label shows "Not subscribe"
- Under **Sound settings**, confirm the sound toggle is **on** and a sound option is selected (Only first message, or All messages)

**Step 2: Check the browser and OS**
- The browser **tab must not be muted** (right-click the tab → Unmute site)
- Do Not Disturb / Focus must be **off**
- The browser must be allowed to play notification sounds — on macOS: **System Settings → Notifications → [browser] → Allow notifications + Play sound for notifications**

**Step 3 — Known compatibility limitation (macOS + Chrome)**

On **macOS with Google Chrome (and other Chromium browsers)**, push-notification **sound** is a documented **Chrome/macOS compatibility problem — not a Chatty bug**. Visual banners work; the sound does not play.

**Recommend Safari** to resolve it — Chatty can be installed as a desktop app in Safari (**Share icon → Add to Dock**), and notification sound works there.

**If sound fails across multiple devices AND multiple browsers** after all of the above, escalate with: device model, OS version, browser + version, and confirmation of which steps were already checked.

---

## Mobile App Notifications Not Working""")

# Q13 — insert after "Too Many / Duplicate Notifications"
sub(P, """> Most cases of duplicate notifications are caused by having email, desktop push, and mobile push all enabled at once for the same trigger.

---

## AI Escalation Email Notifications""", """> Most cases of duplicate notifications are caused by having email, desktop push, and mobile push all enabled at once for the same trigger.

---

## Still Getting Notifications After Turning All Toggles Off

**Key fact:** notification settings in Chatty are **per member account, not global**. Turning everything off on the admin account only silences the admin account.

If the admin has every toggle off but the team still receives emails or push alerts, the alerts are coming from **another member's** notification settings — or from a second connected email account.

1. Ask how many team members the store has (**Settings → Team**)
2. Have **each member** log in and turn their own triggers off under **Settings → Notifications** — the admin cannot do this on their behalf
3. Check whether a **second email account is connected** under **Settings → Channels** (a connected inbox forwards its own notifications)

**If notifications still arrive** after every member account is set to off and no email account is connected, escalate with: a screenshot of the notification received, the **receiving email addresses**, and the list of member accounts already checked.

---

## AI Escalation Email Notifications""")

add_tags(P, ["no sound", "notification sound", "sound not playing", "no beep",
             "banner", "Chrome sound", "macOS", "muted tab", "Focus mode",
             "still receiving notifications", "turned off notifications",
             "per member notifications", "member account settings",
             "connected email"])

# ═══════════════════════════════════════════════════════════════════════════
# Q17 + Q19 — header nav icon / deep links
# kb/faq/deep-links.md — tighten path, add full example URL, add header section
# ═══════════════════════════════════════════════════════════════════════════
P = "kb/faq/deep-links.md"
sub(P, "1. Go to **Chatbox** → **Advanced**\n2. Copy the deep link",
    "1. Go to **Chatbox** → **Advanced** → **Deep links**\n2. Copy the deep link")

sub(P, '**Example:** Add a "Track my order" button in your store navigation that opens the chatbox directly to the Order tracking tab.',
    'Append the fragment to any store URL, or use it as the destination of a button or menu item.\n\n'
    '**Example:** a "Track my order" nav item pointing to `https://yourstore.com/pages/contact#chatty-tracking` '
    'opens the chatbox straight to the Order tracking tab.')

files[P] = load(P).rstrip() + """

---

## Chat Icon in the Header Nav (Instead of the Floating Bubble)

Merchants often ask to move the chat icon **into the theme header**, next to search/account.

**The built-in Position control cannot do this.** **Chatbox → Appearance → Chatbox button → Position** only anchors the *floating* button to a page corner with an offset — it cannot embed an icon into the theme's header.

**The supported way is a deep link:**
1. **Chatbox → Advanced → Deep links** → copy `#chatty-chat` (opens Live Chat) or `#chatty-home` (opens the chatbox home)
2. Add it to a **header menu item**: **Shopify Admin → Content → Menus** → select the header menu → **Add menu item** → paste the deep link URL → Save

**If the merchant wants a custom icon that matches their theme, placed precisely in the header** — that needs a small theme/CSS change:
- Ask for their **reference design** (which icon, where exactly)
- Follow the collaborator access flow (`ref_collaborator-access.md`) — collect the collaborator code
- Escalate to TS to implement it

**If they also want the floating bubble hidden** so the chat *only* opens from their header icon — see `case_chatbox-widget-issues` → *Hide the Floating Launcher but Keep the Chatbox Openable*. Do **not** tell them to turn off "Display chatbox on your store" — that disables the chatbox entirely and their header icon will stop working.
"""

add_tags(P, ["header icon", "header nav", "navigation icon", "custom chat icon",
             "chat icon in menu", "open chat from link", "icon in header",
             "move chat icon"])

# ═══════════════════════════════════════════════════════════════════════════
# Q18 — hide launcher but keep chatbox openable  (GAP, highest risk)
# Q22a — proactive-popup branding is NOT the DevZone chatbox branding
# kb/case/chatbox-widget-issues.md
# ═══════════════════════════════════════════════════════════════════════════
P = "kb/case/chatbox-widget-issues.md"

sub(P, """Add each exclusion URL and save.

---""", """Add each exclusion URL and save.

---

## Hide the Floating Launcher but Keep the Chatbox Openable

**Use case:** the merchant has their own trigger — a header icon, a button, a deep link — and wants the floating bubble gone from the corner, while the chatbox still opens from their trigger.

> **Do NOT turn off "Display chatbox on your store"** (Chatbox → General). That master toggle disables the chatbox completely — their own icon/deep link will stop working too. This is the most common wrong answer to this question.

**Correct handling:**
1. Keep **"Display chatbox on your store" enabled**
2. Collect the requirement (which trigger they're using, screenshot of the page)
3. Follow the collaborator access flow (`ref_collaborator-access.md`) — collect the collaborator code
4. Escalate to TS: the team applies a **targeted CSS snippet that hides the launcher only**, leaving the chatbox itself active and openable from a deep link or custom element

**Do NOT provide CSS code directly** — collect the requirement and forward to the team.

Related: `faq_deep-links` → *Chat Icon in the Header Nav*.

---""")

sub(P, """3. Communicate: "Normally, this option is only available for paid plans. However, we've helped remove the branding for you this time as a special support."

**Important:** Do NOT ask for a review immediately after removing branding""", """3. Communicate: "Normally, this option is only available for paid plans. However, we've helped remove the branding for you this time as a special support."

**Two different branding lines — don't confuse them:**
- **Chatbox branding** (bottom of the chat window) → the DevZone flow above.
- **Proactive-chat popup branding** (the line at the bottom of a proactive/teaser popup) → **there is no self-serve toggle** for this in Proactive chat. The team can hide it for the merchant — collect the request and escalate; don't tell them to look for a setting.

**Important:** Do NOT ask for a review immediately after removing branding""")

# fix the mislabelled Related cross-ref
sub(P, "- faq_embedded-chatbox (embedding chatbox on external sites)",
    "- faq_embedded-chatbox (adding the chatbox as a section on a store page)\n"
    "- faq_website (embedding the chatbox on an external / non-Shopify site)\n"
    "- faq_deep-links (opening the chatbox from a header icon, button, or URL)")

sub(P, 'applies_when: "Merchant wants to move the widget higher or lower, adjust its position on the page, fix overlapping with another element, or customize FAQ page appearance — anything related to widget position or CSS customization"',
    'applies_when: "Merchant wants to move the widget higher or lower, adjust its position on the page, fix overlapping '
    'with another element, hide the floating launcher while keeping the chatbox openable from a custom trigger, or '
    'customize FAQ page appearance — anything related to widget position or CSS customization"')

add_tags(P, ["hide launcher", "launcher", "hide floating button",
             "hide bubble", "open from my own icon", "custom trigger",
             "proactive popup branding"])

# ═══════════════════════════════════════════════════════════════════════════
# Q22c — remove the "typing…/query…" status text
# kb/faq/chatbox-settings.md, after "Disabling View Similar Button"
# ═══════════════════════════════════════════════════════════════════════════
P = "kb/faq/chatbox-settings.md"
sub(P, """## Disabling "View Similar" Button

Currently there is **no on/off toggle** for this button in settings.

Contact support — the team can hide it using custom CSS via **Chatbox** → **Advanced** → **Custom CSS**.

---""", """## Disabling "View Similar" Button

Currently there is **no on/off toggle** for this button in settings.

Contact support — the team can hide it using custom CSS via **Chatbox** → **Advanced** → **Custom CSS**.

---

## Removing the "Typing… / Query…" Status Text

While the AI is preparing an answer it shows a short status text (e.g. *"typing…"*, *"query…"*) above the three-dot indicator.

This can be removed with **custom CSS** via **Chatbox** → **Advanced** → **Custom CSS**.

If the merchant wants to keep the animated **three-dot indicator** but drop the wording, contact support — the team can add a small CSS snippet that hides only the status text.

---""")

add_tags(P, ["typing indicator", "typing status", "query text", "three dots",
             "remove status text", "hide typing"])

# ═══════════════════════════════════════════════════════════════════════════
# Q22b — "Explore this product" popup (proactive-chat.md — CHUNK format!)
# ═══════════════════════════════════════════════════════════════════════════
P = "kb/faq/proactive-chat.md"
files[P] = load(P).rstrip() + """

---

<!-- CHUNK: proactive-chat-disable-popup -->
```yaml
chunk_id: "faq__proactive-chat-disable-popup"
doc_id: "chatty-proactive-chat"
title: "Turn off a proactive chat popup — 'Explore this product' / product-recommendation popup"
category: "faq"
subcategory: "live-chat"
tags: ["explore this product", "explore product popup", "product recommendation popup", "disable popup", "turn off popup", "remove popup", "deactivate campaign", "stop proactive chat", "popup branding", "not our app", "another app popup"]
applies_when: "When a merchant wants to remove or turn off a popup on their store — especially an 'Explore this product' / product-recommendation popup — and asks whether it is Chatty"
priority: "high"
```

## Turning Off a Proactive Chat Popup ("Explore this product")

An **"Explore this product"** / product-recommendation popup on the storefront is a **Proactive Chat campaign** using the *Product recommendation* template.

**To turn it off:** go to **Proactive chat**, open the campaign, and **deactivate** it.

> **Confirm which app owns the popup first.** Some "explore products" / product-recommendation popups come from a **different app** on the store, not from Chatty. Ask the merchant for a screenshot and check whether a matching Proactive chat campaign is actually active — if there is no active Chatty campaign, the popup belongs to another app and deactivating things in Chatty will not remove it.

**Removing the branding line** at the bottom of a proactive popup is **not a self-serve toggle** — the team can hide it. Collect the request and escalate; don't send the merchant looking for a setting.
"""

# ═══════════════════════════════════════════════════════════════════════════
# Q24 — embedded chatbox on one page only
# ═══════════════════════════════════════════════════════════════════════════
P = "kb/faq/embedded-chatbox.md"
files[P] = load(P).rstrip() + """

**Prerequisites — both must be on, or the section renders empty:**
- The **Chatty (Core)** app embed must be **enabled** in the theme (**Online Store → Themes → Customize → App embeds**)
- **Chatbox → General → Blocks → Live chat** must be **on**

## Testing the Chat on One Page Only (No Floating Bubble Elsewhere)

To have the chat available on a **single page** without the floating bubble appearing site-wide:

1. Add the **Embedded chatbox** section to that one page template (steps above)
2. Turn **off** "Display chatbox on your store" in **Chatbox → General** — this removes the floating bubble
3. **Keep the Chatty (Core) app embed enabled** in the theme — the embedded section needs it to render

**If the section is added and all of the above is set but the chat still doesn't render**, escalate with: a screenshot of the page, the page URL, and the collaborator code (`ref_collaborator-access.md`).
"""

add_tags(P, ["test on one page", "one page only", "app embed", "Chatty Core",
             "embedded not showing", "no floating bubble", "single page chat"])

# ═══════════════════════════════════════════════════════════════════════════
# Q26 — reopen / un-resolve a conversation
# ═══════════════════════════════════════════════════════════════════════════
P = "kb/faq/others.md"
sub(P, """Customers can always reopen a conversation by sending a new message.

---

## Conversation Transcripts""", """Customers can always reopen a conversation by sending a new message.

---

## Reopening / Un-resolving a Conversation

**On the merchant side:** open the conversation from the **Resolved** tab — there is a **Reopen** button at the top of the conversation. Clicking it moves the conversation back to your **Open** list so you can continue from there.

**On the customer side:** by design there is **no "Unresolve" button** and the Resolve behaviour can't be turned off. Once a conversation is resolved it moves to the Resolved tab, and it reopens **only when the customer sends a new message**. After roughly **5 days of inactivity**, a new message starts a **brand-new conversation** rather than reopening the old one.

**If a merchant complains that older Open conversations disappear from view after they resolve one:** set a **reminder** on those conversations so they resurface in the unresolved view instead of getting lost.

> A **Reopen** button on a **Resolved** conversation is expected behaviour. Only treat it as the known inbox defect if the button appears on an **Open** conversation and refuses to close the chat (see *404 / Inbox-Crash & Cross-Contamination*).

---

## Conversation Transcripts""")

# disambiguate the defect bullet so a legit Reopen isn't escalated as the 404 defect
sub(P, '- the **Resolve** button showing "Reopen" and not closing the chat',
    '- on an **Open** conversation, the **Resolve** button showing "Reopen" and not closing the chat '
    '(a Reopen button on an already-**Resolved** conversation is normal — see *Reopening / Un-resolving a Conversation*)')

add_tags(P, ["reopen", "unresolve", "un-resolve", "undo resolve",
             "turn off resolve", "hide resolve button", "reminder",
             "resurface conversation"])

# Q29 — pointer from Total Sales in Analytics
sub(P, """Payments made outside Shopify or through non-tracked channels may not be counted.""",
    """Payments made outside Shopify or through non-tracked channels may not be counted.

Attributed orders are tagged in Shopify as **`chatty-assisted`** or **`chatty-direct`** — see `faq_analytics` → *Verifying Assisted Revenue & Order Attribution* for how to reconcile them.""")

# Q26 — merchant-side Reopen mirrored in Inbox
P = "kb/faq/inbox.md"
sub(P, """**For large volumes:** Contact support — the team may be able to help with a backend bulk resolve for your account.

---""", """**For large volumes:** Contact support — the team may be able to help with a backend bulk resolve for your account.

---

## Reopening a Resolved Conversation

Open the conversation from the **Resolved** tab — there is a **Reopen** button at the top. It moves the conversation back to the **Open** list.

Customers have no "Unresolve" control: a resolved conversation reopens on their side only when they send a new message, and after ~5 days of inactivity a new message starts a brand-new conversation instead.

See `faq_others` → *Reopening / Un-resolving a Conversation*.

---""")

add_tags(P, ["reopen", "unresolve", "un-resolve", "reopen conversation",
             "reminder", "webhook", "webhooks", "public API", "API key"])

# Q44 — OUTDATED: "API does not support chat history"
sub(P, """## Chat History via API

The Chatty Public API does not currently support saving chat history via API endpoint.

However, if you integrate with **Zendesk**, all Chatty conversations are automatically saved as Zendesk tickets when marked as resolved. The support team can also manually export transcripts.""",
    """## Chat History via API

The **Chatty Public API does support pulling conversations and messages** — you can list a conversation's messages via the API. There are also **webhooks** (e.g. `customer_message`, `ai_response`) that push chats to your own server in near real time.

**API key generation and webhooks are Pro/Plus only** — on Free/Basic the merchant must upgrade to generate a key. See `faq_klaviyo` → *Chatty Public API & Webhooks*.

What is **not** available via the API is a **bulk full-conversation / date-range export** — for that, route the merchant to support, or use the **Zendesk** integration (all Chatty conversations are automatically saved as Zendesk tickets when marked resolved). The support team can also manually export transcripts.""")

# ═══════════════════════════════════════════════════════════════════════════
# Q28 — deleted products / force resync + OUTDATED nav path
# ═══════════════════════════════════════════════════════════════════════════
P = "kb/case/ai-sync-issues.md"
sub(P, """1. Suggest the merchant trigger a manual resync in **AI agent → Training data → Manage → Products**
2. Advise the merchant not to sync repeatedly — either sync manually once or rely on the daily auto-sync at 12:00 AM PST

**If products still appear after resync**, escalate to support team with: store URL, product name(s) still showing, deletion date, screenshot.""",
    """1. Suggest the merchant trigger a manual resync in **AI agent → Training data → Products → Manage → Sync products**
2. Advise the merchant not to sync repeatedly — either sync manually once or rely on the daily auto-sync at 12:00 AM PST
3. They can also **deactivate** the stale products in the Training data list (toggle them Disabled) so the AI stops using them immediately, without waiting for the sync

**Deleted products reappearing after a manual resync is NOT expected behaviour.** If it keeps happening, escalate to the support team with: store URL, an **example product** that keeps coming back, product name(s) still showing, deletion date, screenshot. The team can reset the sync from their side.

> Reassure the merchant if they're worried about what "product training" does: it simply means Chatty **reads their product data** — title, description, price, variants — so the AI can answer about it. It doesn't change or publish anything in their store.""")

add_tags(P, ["force resync", "manual resync", "sync products", "product training",
             "what is product training", "deleted product reappearing"])

# OUTDATED nav paths in the near-duplicate file
P = "kb/case/ai-product-sync.md"
sub(P, "1. Go to **AI agent** → **Data Source** and check the timestamp of the most recent sync",
    "1. Go to **AI agent** → **Training data** → **Products** and check the timestamp of the most recent sync")
sub(P, """1. Suggest the merchant trigger a manual resync in **AI agent → Data Sources**
2. Advise the merchant not to sync repeatedly — either sync manually once or rely on the daily auto-sync at 12:00 AM PST

**If products still appear after resync**, escalate to dev team with: store URL, product name(s) still showing, deletion date, screenshot.""",
    """1. Suggest the merchant trigger a manual resync in **AI agent → Training data → Products → Manage → Sync products**
2. Advise the merchant not to sync repeatedly — either sync manually once or rely on the daily auto-sync at 12:00 AM PST
3. They can also **deactivate** the stale products in the Training data list (toggle them Disabled) so the AI stops using them immediately

**Deleted products reappearing after a manual resync is NOT expected behaviour.** If it keeps happening, escalate to the dev team with: store URL, an **example product** that keeps coming back, product name(s) still showing, deletion date, screenshot. The team can reset the sync from their side.""")

# Q28 — what "product training" means
P = "kb/faq/data-sources.md"
sub(P, """Product information updates daily at **12:00 AM PST**.""",
    """Product information updates daily at **12:00 AM PST**. To sync sooner, trigger a manual resync in **AI agent → Training data → Products → Manage → Sync products**.

**What "product training" actually does:** Chatty simply **reads** the product data — title, description, price, variants — so the AI can answer questions about it. It does not modify, publish, or unpublish anything in the merchant's store.""")

add_tags(P, ["what is product training", "product training", "force resync",
             "manual sync"])

# ═══════════════════════════════════════════════════════════════════════════
# Q29 — chatty-assisted / chatty-direct order tags  (GAP)
# ═══════════════════════════════════════════════════════════════════════════
P = "kb/faq/analytics.md"
files[P] = load(P).rstrip() + """

---

## Verifying Assisted Revenue & Order Attribution

Chatty tags attributed orders in **Shopify** with one of two order tags:
- **`chatty-assisted`** — the customer interacted with Chatty and then placed the order
- **`chatty-direct`** — the order came directly through the Chatty conversation

**To verify the revenue side:** open **Analytics → Overview** (assisted revenue / AOV, total sales share contributed by Chatty) and **Analytics → Sales** (total sales, orders, conversion rate). These are the numbers to reconcile against.

> **A tagged order will not always map 1:1 to a named contact in the Inbox.** Many attributed sessions are anonymous, so the buyer's email won't appear on the conversation. Reconcile via **Analytics**, not by searching the Inbox for the buyer's email — searching the Inbox by email is the most common wrong turn here.
"""

add_tags(P, ["chatty-assisted", "chatty-direct", "order tags", "attribution",
             "attributed orders", "verify revenue", "revenue attribution",
             "assisted vs direct"])

# ═══════════════════════════════════════════════════════════════════════════
# Q31 — admin email vs notification email  (OUTDATED)
# ═══════════════════════════════════════════════════════════════════════════
P = "kb/case/email-channel-issues.md"
sub(P, """## Changing Admin Email

The admin email is tied to the Shopify store owner account.

1. Go to Chatty app settings → check **Team settings** for the current admin email
2. If the merchant needs to change the primary admin, they may need to update their Shopify store owner email first, then re-access Chatty""",
    """## Changing Admin Email

**There are two different emails — clarify which one the merchant means before acting:**

| | What it is | How to change |
|---|---|---|
| **Admin account email** | The account that logs in and owns the Chatty workspace | **Our team changes it** — see below |
| **Notification email** | The address that receives chat/AI alerts | Merchant sets it in **Settings → Notifications** and **AI agent → Settings → Contact support email** |

**To change the admin account email** (e.g. from a personal address to `support@`):

1. Ask the merchant to **share the email address they want to use**
2. Escalate to the team to make the change — the merchant does **not** need to change their Shopify store-owner email
3. A **verification code is sent to the new address** to confirm the change

> **On Free / single-seat plans we can only *replace* the existing account, not add a second one** — the plan has 1 seat (admin only). If the merchant wants to keep both addresses active, they need to upgrade to a plan with more seats (see `faq_team`).""")

add_tags(P, ["change admin email", "admin account email", "notification email",
             "which email receives chats", "replace account", "verification code",
             "support@ email"])

P = "kb/faq/general-settings.md"
sub(P, """**Notification types:**
- **Email** — manage or send test
- **Web push** — browser notifications; manage or send test
- **Chatty mobile app** — download the app to receive notifications on mobile

---

## Translations""", """**Notification types:**
- **Email** — manage or send test
- **Web push** — browser notifications; manage or send test
- **Chatty mobile app** — download the app to receive notifications on mobile

> **Notification settings are per member account, not global.** Turning everything off on the admin account does not silence other team members — each member must turn their own triggers off.

---

## Which Email Receives Chats (and How to Change It)

Two different addresses — don't confuse them:

- **Admin account email** — the account that logs into Chatty. To switch it to a different address (e.g. `support@`), the merchant shares the address they want and **our team changes it**; a verification code is sent to the new address. On **Free / single-seat plans the existing account can only be replaced, not added to**. See `case_email-channel-issues` → *Changing Admin Email*.
- **Notification email** — where alerts are sent. Set in **Settings → Notifications**, and for AI/contact-form emails in **AI agent → Settings → Contact support email**.

---

## Translations""")

add_tags(P, ["change admin email", "admin email", "which email receives chats",
             "notification email address", "per member notifications"])

# ═══════════════════════════════════════════════════════════════════════════
# Q36 — AI points to generic contact page
# ═══════════════════════════════════════════════════════════════════════════
P = "kb/faq/ai-training-setup.md"
sub(P, """2. Create a **Custom Scenario** (**AI agent** → **Instructions** → **Manage** → **Assistant skills** → **Custom scenarios** → **+ Add scenario**) triggered when customers ask about contacting the team

---

## AI and Loyalty Points / Customer Account Data""", """2. Create a **Custom Scenario** (**AI agent** → **Instructions** → **Manage** → **Assistant skills** → **Custom scenarios** → **+ Add scenario**) triggered when customers ask about contacting the team

---

## AI Points to a Generic Contact Page / Wrong Contact URL

**Symptom:** the AI replies with a vague *"you can reach us via our contact page"* — with the wrong link, or no link at all.

**Fix:** add the merchant's **exact contact URL** to **AI agent → Instructions → Manage → General instructions** (or to Custom knowledge), so the AI references the right page instead of guessing. Re-test in **AI agent → Test AI**.

**If the merchant wants an on-store form rather than a link:**
- Chatty has a **built-in Contact form** section — it displays when a customer requests human/after-sales support. Submissions land in the **Inbox** and are also forwarded to the address set in **AI agent → Settings → Contact support email**.
- Chatty also integrates with **Powerful Contact Form** — set up in **Settings → Integrations** (see `faq_powerful-contact-form`). Each submission becomes a conversation in the inbox.

---

## AI and Loyalty Points / Customer Account Data""")

# ═══════════════════════════════════════════════════════════════════════════
# Q46 — can I use OpenAI / swap the model  (OUTDATED)
# ═══════════════════════════════════════════════════════════════════════════
sub(P, """## What AI Model Does Chatty Use

Chatty uses its own AI agent layer built on top of large language model technology. The specific underlying model is not publicly disclosed, but the AI is optimized for e-commerce support scenarios.""",
    """## What AI Model Does Chatty Use — Can I Use OpenAI / Switch the Model?

Chatty runs on a **secure, enterprise-grade large language model built for support**, upgraded regularly. The specific underlying model is not publicly disclosed, and the AI agent layer on top of it is optimized for e-commerce support scenarios.

**There is no option to plug in OpenAI or swap the underlying model** — not on any plan.

**If a merchant feels the replies are weak, the fix is almost always data/instruction quality, not the model:**
1. Set up **Assistant skills** — **AI agent → Instructions → Manage → Assistant skills**
2. Tighten the **General instructions** and add **Custom scenarios** for the cases they're unhappy with
3. Add **Custom knowledge** for anything the AI is missing
4. Re-test in **AI agent → Test AI → Test now** with the exact question that failed

Ask for the **specific example** that disappointed them — that is what makes the fix possible, and it's what the product team needs.

**Log the OpenAI / model-choice request as a feature request** with the merchant's use case and their example.""")

add_tags(P, ["OpenAI", "switch model", "custom model", "bring your own model",
             "stronger AI", "change AI model", "use my own AI",
             "contact page URL", "wrong contact link", "generic contact page"])

# OUTDATED: "powered by ChatGPT"
P = "kb/faq/knowledge-base.md"
sub(P, "automate customer support with an AI chatbot (powered by ChatGPT), and build self-serve FAQ help centers",
    "automate customer support with an AI chatbot (built on a secure, enterprise-grade large language model), "
    "and build self-serve FAQ help centers")

# ═══════════════════════════════════════════════════════════════════════════
# Q44 — Public API + webhooks + plan gating
# ═══════════════════════════════════════════════════════════════════════════
P = "kb/faq/klaviyo.md"
sub(P, """## Chatty Public API

Yes — the Chatty Public API provides access to your store's customer data (contacts, chat history timestamps, order counts, total spend). It's primarily for custom integrations: syncing contacts to a CRM, pulling data into spreadsheets, or building internal dashboards.

See: https://help.chatty.net/integrations/chatty-public-api""",
    """## Chatty Public API & Webhooks

Yes — the Chatty Public API supports:
- **Conversations and messages** — e.g. list the messages in a conversation
- **Customer data** — contacts, chat history timestamps, order counts, total spend
- **Webhooks** — events such as `customer_message` and `ai_response` that **push chats to the merchant's own server in near real time**

Typical uses: forwarding chats to their own backend, syncing contacts to a CRM, pulling data into spreadsheets, building internal dashboards.

> **API key generation and webhooks are Pro/Plus only.** On **Free and Basic**, the merchant must upgrade to **Pro or Plus** to generate an API key. Don't send a Free/Basic merchant to the API page expecting a key.

Point merchants to the official docs for the **base URL, auth headers, and endpoints**: https://help.chatty.net/integrations/chatty-public-api

**Not available via the API:** bulk full-conversation / date-range export. For contact and order data there is a self-serve **Contacts → Export** (CSV sent to their email) — see `faq_contacts`.""")

add_tags(P, ["webhook", "webhooks", "customer_message", "ai_response",
             "forward chats", "push to my server", "API key", "API plan",
             "Pro only API"])

P = "kb/faq/pricing.md"
sub(P, """**Plus:** AI conversations 1,000/month + $0.40/extra, products unlimited, custom answers unlimited, URLs & files unlimited, team members unlimited, chat history unlimited, dedicated AI consultant included.

---""", """**Plus:** AI conversations 1,000/month + $0.40/extra, products unlimited, custom answers unlimited, URLs & files unlimited, team members unlimited, chat history unlimited, dedicated AI consultant included.

**Public API & webhooks — Pro/Plus only:**

| Plan | API key generation | Webhooks |
|---|---|---|
| Free | ✗ | ✗ |
| Basic | ✗ | ✗ |
| Pro | ✓ | ✓ |
| Plus | ✓ | ✓ |

A merchant on Free/Basic who wants to pull conversations via the API or forward chats to their own server must upgrade to **Pro or Plus** (see `faq_klaviyo` → *Chatty Public API & Webhooks*).

---""")

add_tags(P, ["API", "API key", "webhook", "webhooks", "public API", "developer",
             "API plan"])

# ═══════════════════════════════════════════════════════════════════════════
# Collaborator code path — Liz approved updating to the new Shopify Admin UI
# ═══════════════════════════════════════════════════════════════════════════
P = "kb/reference/collaborator-access.md"
sub(P, """> *"Could you share your collaborator code? You'll find it in **Shopify Admin → Settings → Users and permissions → Security → Collaborator request code**."*""",
    """> *"Could you share your collaborator code? You'll find it in **Shopify Admin → Settings → Users and permissions → Collaborators → Get collaborator code**."*

(On older Shopify Admin versions the same code lives under **Settings → Users and permissions → Security → Collaborator request code**. If the merchant can't find it under Collaborators, point them there.)""")

# ═══════════════════════════════════════════════════════════════════════════
# Write payloads
# ═══════════════════════════════════════════════════════════════════════════
payloads = [{"agent": AGENT, "path": p, "content": c} for p, c in sorted(files.items())]
os.makedirs(os.path.dirname(OUT), exist_ok=True)
with open(OUT, "w") as f:
    json.dump(payloads, f, ensure_ascii=False, indent=2)

print(f"✅ {len(payloads)} files -> {OUT}\n")
for p in sorted(files):
    print(f"   {p}")
