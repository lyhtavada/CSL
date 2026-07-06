# KB Sync Diff — Chatty (chatty-agent / Ivy)

**Run:** DIFF-ONLY review gate (no push)
**Mined-FAQ source:** `reports/weekly-faqs/chatty/chatty_2026-06-29_2026-07-05.md` (46 FAQs, week Jun 29 – Jul 5 2026)
**Live KB cache:** `/tmp/kb-sync/chatty/` (70 files)
**Date:** 2026-07-06

## Verdict counts

| Verdict | Count |
|---------|-------|
| COVERED | 35 |
| OUTDATED | 4 |
| GAP | 5 |
| PARTIAL | 2 |

**Files to change: 8** (some files carry more than one item; merged into one payload each).

## Summary table (all 46 FAQs)

| Q# | Topic | KB file | Verdict |
|----|-------|---------|---------|
| Q1 | AI first-time setup & training | flows/done_for_you.md, kb/faq/ai-training-setup.md | COVERED |
| Q2 | Done-for-you setup (free any plan) | flows/done_for_you.md | COVERED (already "free of charge") |
| Q3 | Custom Q&A / sale campaign / discount code | kb/faq/data-sources.md, kb/case/discount-sync.md | COVERED |
| Q4 | Custom scenario / stop asking order # | kb/faq/ai-training-setup.md | COVERED |
| Q5 | Upload files/CSV to train, indexing time | kb/faq/ai-training-setup.md, kb/faq/data-sources.md | COVERED |
| Q6 | Check AI quality / read past AI chats | kb/faq/analytics.md, kb/faq/inbox.md | COVERED |
| Q7 | AI "no access" for active/synced product | kb/case/ai-wrong-responses.md | COVERED |
| Q8 | AI made up a fact (hallucination) | kb/case/ai-wrong-responses.md | COVERED |
| Q9 | Multi-market: AI can't find product via translated-domain URL | kb/case/ai-wrong-responses.md | **GAP** |
| Q10 | AI shows on translated pages after OFF | kb/case/ai-wrong-responses.md, kb/faq/translation.md | COVERED |
| Q11 | Desktop sound/banner stopped (Chrome) | kb/case/notification-issues.md | **PARTIAL** |
| Q12 | Email notifications stopped (test works) | kb/case/notification-issues.md | **GAP** (sub-section) |
| Q13 | Notifications despite all toggles off | kb/case/notification-issues.md | **GAP** (sub-section) |
| Q14 | AI-only / humans-only live chat | kb/faq/human-handover.md, kb/faq/live-chat.md | COVERED |
| Q15 | Handover triggers + email on escalate | kb/faq/human-handover.md, kb/case/notification-issues.md | COVERED |
| Q16 | Human joined but AI still replies / assign to AI | kb/faq/inbox.md, kb/faq/human-handover.md | COVERED |
| Q17 | Chat icon in header nav | kb/faq/deep-links.md, kb/case/chatbox-widget-issues.md | COVERED |
| Q18 | Hide floating widget, open from own icon | kb/case/chatbox-widget-issues.md | COVERED |
| Q19 | Launch chat via URL/deep link | kb/faq/deep-links.md | COVERED |
| Q20 | Button not centered / mobile position | kb/case/chatbox-widget-issues.md | COVERED |
| Q21 | Change store/AI name, logo, header | kb/faq/chatbox-settings.md, kb/faq/general-settings.md | COVERED |
| Q22 | Remove branding / "Explore" popup / typing text | kb/case/chatbox-widget-issues.md | COVERED |
| Q23 | Widget not showing / can't type | kb/case/chatbox-widget-issues.md | COVERED |
| Q24 | Embedded chatbox, one page only | kb/faq/embedded-chatbox.md | COVERED |
| Q25 | 404 / inbox won't load / resolved reappear | kb/faq/others.md, kb/faq/inbox.md | COVERED |
| Q26 | Un-resolve/reopen, disable Resolve button, no delete | kb/faq/inbox.md | **GAP** |
| Q27 | Missing inbox messages / older convos / orders | kb/faq/inbox.md | COVERED |
| Q28 | Deleted products still in Chatty / force resync | kb/case/ai-product-sync.md, kb/case/ai-sync-issues.md | COVERED |
| Q29 | Verify assisted vs direct revenue | kb/faq/analytics.md | COVERED |
| Q30 | Email channel won't verify (alias/spam) | kb/case/email-channel-issues.md | COVERED |
| Q31 | Change admin/notification email | kb/case/email-channel-issues.md | COVERED |
| Q32 | Connect WhatsApp / "Pending" / error | kb/case/whatsapp-messenger-issues.md | COVERED |
| Q33 | Change/remove IG & FB auto messages | kb/case/whatsapp-messenger-issues.md, kb/faq/quick-replies.md | COVERED |
| Q34 | FAQ page/block setup & fixes | kb/faq/faqs-page.md, kb/faq/faqs-block.md, kb/case/chatbox-widget-issues.md | COVERED |
| Q35 | Pre-chat form (require name/email) | kb/faq/live-chat.md, kb/faq/chatbox-settings.md | COVERED |
| Q36 | AI points to generic contact page | kb/faq/powerful-contact-form.md, kb/case/ai-wrong-responses.md | COVERED |
| Q37 | Wrong language / language reverted | kb/faq/translation.md, kb/case/translation-issues.md | COVERED |
| Q38 | Change source FAQ language / plan languages | kb/faq/translation.md | COVERED |
| Q39 | Where's the app / no App Store / native app coming | kb/faq/mobile-app.md, kb/case/notification-issues.md | **OUTDATED** |
| Q40 | Banners but no sound on Mac | kb/case/notification-issues.md | **PARTIAL** (merged w/ Q11) |
| Q41 | Pricing, plan limits, conversation cap | kb/faq/pricing.md, kb/case/ai-product-limit.md, kb/faq/knowledge-base.md | **OUTDATED** |
| Q42 | "Out of AI conversations" after upgrade | kb/case/ai-conversation-limit.md | **GAP** |
| Q43 | Cancel/downgrade & refund | kb/faq/pricing.md, kb/case/billing-refund.md | COVERED |
| Q44 | Public API / webhooks, plan gate | kb/faq/knowledge-base.md | **GAP** (Pro/Plus gate) |
| Q45 | Export conversations / FAQs (date range) | kb/faq/inbox.md | COVERED |
| Q46 | Use OpenAI / swap AI model | kb/faq/ai-training-setup.md | COVERED |

---

## OUTDATED items

### Q41 — Plan limits (custom answers + Plus URL & File) → `kb/faq/pricing.md`

The mined file's Notes confirm Q41 carries the **EXACT verified chatty.net/pricing figures (2026-07-06)** and supersedes older per-plan numbers. AI-conversation caps (Free 50 / Basic 100 / Pro 500 / Plus 1,000) and products (Basic 500 / Pro 8,000 / Plus Unlimited) already match. Three per-plan facts were stale:

- **Basic custom answers** — stale: `**Basic:** ... custom answers 1,000, ...` → correct: `custom answers 100` (Q41: Basic = 100 custom answers).
- **Pro custom answers** — stale: `**Pro:** ... custom answers unlimited, ...` → correct: `custom answers 1,000` (Q41: Pro = 1,000 custom answers).
- **Plus URL & File** — stale: `**Plus:** ... URLs & files unlimited, ...` → correct: `URLs & files 700` (Q41: Plus = 700 URL & File).

### Q41 — Plan limits → `kb/case/ai-product-limit.md`

This file's Plan Limits Reference contradicted both Q41 **and** pricing.md (internal inconsistency). Fixed the reference table and the derived "extend to" table:

- Products row — stale: `| Products for AI training | 200 | 1,500 | 8,000 | Unlimited |` → correct: `... | 200 | 500 | 8,000 | Unlimited |` (Basic 1,500 → **500**).
- Custom Answers row — stale: `| Custom Answers | 100 | 1,000 | Unlimited | Unlimited |` → correct: `| Custom Answers | 100 | 100 | 1,000 | Unlimited |` (Basic 1,000 → 100, Pro Unlimited → 1,000).
- URL & File row — stale: `| URL & File | 20 | 50 | 500 | Unlimited |` → correct: `... | 500 | 700 |` (Plus Unlimited → 700).
- Extend-to table rows updated to match (Free products extend-to 1,500 → **500**; Free custom-answers extend-to 1,000 → 100; Basic custom-answers extend-to Unlimited → 1,000; Pro URL & File extend-to Unlimited → 700).

### Q41 — Basic products → `kb/faq/knowledge-base.md`

- Plans table — stale: `| Products for AI training | 200 | 1,500 | 8,000 | Unlimited |` → correct: `... | 200 | 500 | 8,000 | Unlimited |` (Basic 1,500 → **500**, per Q41). (This file also gets the Q44 GAP addition below.)

### Q39 — Native app now submitted → `kb/faq/mobile-app.md` + `kb/case/notification-issues.md`

Both files stated flatly that Chatty is "PWA only / no native app." Mined Q39 reports a **native iOS/macOS app has been submitted to Apple, ~2–4 weeks from approval** — a change from prior messaging.

- `mobile-app.md` stale line: `Chatty's mobile app is a Progressive Web App (PWA) ... nothing to search for in those stores.` → kept, plus a new "Native app update" note that a native app is submitted (~2–4 weeks). Also added the iOS-Safari-only install + blank-screen-reinstall detail (Q39/Q40).
- `notification-issues.md` stale lines: `there is no native app on the App Store or Google Play` and `there is no native iOS/Android app in the App Store` → reworded to "today a PWA; native iOS/macOS app now submitted, ~2–4 weeks from approval" (PWA install guidance kept intact).

---

## GAP items

### Q9 — Multi-market AI can't resolve product via translated-domain URL → `kb/case/ai-wrong-responses.md`

Existing sections cover market **pricing** and **domain in the AI's output links**, but not the **input-side retrieval failure**: pasting a translated-domain product URL returns "no information" even when the product is Active/synced on both stores. **Missing sub-point added** as a new section "AI Cannot Find Product via Translated-Domain URL (Multi-Market / Multi-Language)": recognizes products by primary-domain URL only; workaround = reference by name/SKU + confirm each market synced; escalate with both store URLs + SKU + failing question.

### Q26 — Un-resolve/reopen, disable Resolve button, no delete → `kb/faq/inbox.md`

No KB content on reopening/un-resolving. **Missing sub-point added** ("Un-resolving / Reopening a Conversation & Disabling the Resolve Button"): no Unresolve button by design; reopens only on a new customer message (new conversation after ~5 days); team can disable the Resolve button per-account on request; set a reminder to keep Open convos visible; no delete-conversation option.

### Q42 — "Out of AI conversations" after upgrading → `kb/case/ai-conversation-limit.md`

Not documented. **Missing sub-point added** ("Bot Says 'Out of AI Conversations' After Upgrading"): usually a usage-state that hasn't refreshed; confirm plan in Shopify + Subscription → View details; escalate with store URL so the team can reset the counter / re-enable AI; human agents can still reply meanwhile.

### Q44 — Public API / webhooks Pro/Plus gate → `kb/faq/knowledge-base.md`

KB mentions the Public API only as "does not support saving chat history." Missing that the API can list conversation messages and that **webhooks** (`customer_message`, `ai_response`) push chats to your server — and that **API key generation + webhooks are Pro/Plus only**. **Missing sub-point added** as a bullet in the Integrations section.

### Q12 / Q13 — Email notification backend/per-member root causes → `kb/case/notification-issues.md`

Email section only covered spam/settings toggles. **Missing sub-points added**: (Q12) a test email landing while real notifications don't for weeks points to either a **backend-unsubscribed email** or **per-member** notification config, both team-checkable via backend logs; (Q13) notifications arriving despite all toggles off = **per-member settings** (or a second connected email) — audit every member.

---

## PARTIAL items

### Q11 / Q40 — macOS + Chrome: banners work, no sound → `kb/case/notification-issues.md`

The Desktop Push section listed generic checks but **missed the confirmed root cause**: on **macOS + Chrome**, notification **sound** is a documented Chrome/macOS compatibility limitation (not a Chatty bug); Safari / installed PWA behave differently. **Missing sub-point added** ("Known issue — macOS + Chrome: banners work, no sound") with the System Settings sound-permission check and the escalate-anyway guidance (some cases fixed on Chatty's side).

---

## Priority list (ranked by mined Frequency, highest first)

| Rank | Q# | Topic | Verdict | Freq | Target file |
|------|----|-------|---------|------|-------------|
| 1 | Q41 | Pricing / plan limits (custom answers, Plus URL & File, Basic products) | OUTDATED | ~12 | pricing.md, ai-product-limit.md, knowledge-base.md |
| 2 | Q11 | Desktop sound stopped (macOS/Chrome compatibility) | PARTIAL | ~10 | notification-issues.md |
| 3 | Q39 | Native app now submitted (~2–4 wks) | OUTDATED | ~8 | mobile-app.md, notification-issues.md |
| 4 | Q12 | Email notifications stopped (backend unsubscribe / per-member) | GAP | ~6 | notification-issues.md |
| 5 | Q40 | Banners but no sound on Mac | PARTIAL (merged Q11) | ~5 | notification-issues.md |
| 6 | Q26 | Un-resolve / disable Resolve button / no delete | GAP | ~4 | inbox.md |
| 7 | Q42 | "Out of AI conversations" after upgrade | GAP | ~4 | ai-conversation-limit.md |
| 8 | Q9 | Multi-market translated-domain URL retrieval | GAP | ~3 | ai-wrong-responses.md |
| 9 | Q44 | Public API / webhooks Pro/Plus gate | GAP | ~3 | knowledge-base.md |
| 10 | Q13 | Notifications despite all toggles off | GAP | ~2 | notification-issues.md |

**Highest-impact single file:** `kb/case/notification-issues.md` — carries the week's #1 support-labor cluster (Q11/Q12/Q13/Q40) plus the Q39 native-app correction.
