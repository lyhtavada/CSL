# Chatty product-KB-sync — 2026-08-18 (Slack-only run, GitLab = 0 hits)

Review-gate draft. No push/reindex performed. Payloads: `product-kb-sync-chatty-2026-08-18-payloads.json` (13 files).

## Classification table

| # | Item (date) | Class | KB file | Reason |
|---|---|---|---|---|
| 1 | View Cart proactive trigger (29/05) | PARTIAL | `kb/faq/proactive-chat.md` | Template table + priority-order (Cart Booster→Abandoned Cart→View Cart→...) + max 5/session cap were missing entirely. |
| 2 | Image search in chat (29/05) | COVERED | `kb/faq/ai-training-setup.md` | Already documents AI matching a customer's product photo to the catalog. |
| 3 | Shopify customer tags personalization (29/05) | GAP | `kb/faq/ai-agent-settings.md` | No mention anywhere that AI reads customer tags to personalize replies; added a short section. |
| 4 | Human Handover redesign (04/06) | COVERED | `kb/faq/human-handover.md` | Already fully reflects new auto-triggers, intent rules, destinations, custom messages — an earlier sync round clearly already patched this. |
| 5 | AI auto-follow-up on silence (17/06) | COVERED | `kb/faq/ai-agent-settings.md` | "Follow-up Messages" section already matches (wait-time dropdown, 5 min default). |
| 6 | Widget position drag-and-drop (17/06) | COVERED | `kb/faq/chatbox-settings.md` | Position control (drag dot / anchor / 0–45% offset) already documented. |
| 7 | Pre-chat form X=0 / doesn't block chat (17/06 + 06/08) | COVERED | `kb/faq/chatbox-settings.md` | "Pre-Chat Form" section already states form no longer blocks chatting. |
| 8 | Inbox unread badge counting bug (17/06) | SKIP | — | Pure internal bug fix, no merchant-facing behavior difference to explain. |
| 9 | Inbox assignee list hiding non-activated admins (17/06) | SKIP | — | Same — internal bug fix. |
| 10 | Memory & facts UI cleanup (17/06) | SKIP | — | Pure UI cleanup, nothing a merchant would ask "why did X change" about. |
| 11 | Plan limit increases incl. Plus→Unlimited (23/06) | **OUTDATED** | `kb/faq/pricing.md`, `kb/case/ai-product-limit.md`, `kb/case/ai-product-sync.md` | KB still showed Plus at 20,000 products / 700 URL&File — the actual 23/06 change (→ Unlimited) was **never applied to the KB**. Everything else (Free/Basic/Pro numbers, AI conversation limits) was already correct. |
| 12 | FAQ block display condition redesign (23/06) | COVERED | `kb/faq/faqs-block.md` | Already reflects the new "Product pages / Specific pages" two-group model, no more "All pages". |
| 13 | Chat-to-Sale report (01/07) | PARTIAL | `kb/faq/analytics.md` | Sales tab existed but didn't mention the Operations & Team sub-tab, its plan-gating (4 columns only), or the ~1-day batch delay. |
| 14 | Product Quiz (01/08) | PARTIAL | `kb/faq/product-quiz.md` | File existed but was 2 sentences — missing config location, question count (3/5/7, default 5), default 2 products, upgrade-button behavior on lower plans. |
| 15 | Chatty mobile app (17/07) | COVERED | `kb/faq/mobile-app.md` | Already documents native App Store/Google Play app, QR code, download locations. |
| 16 | Unified inbox across stores (23/07) | COVERED | `kb/faq/inbox.md` | Already documents Plus-only, 10-store cap, store switcher. |
| 17 | Per-member permissions (10/08) | COVERED | `kb/faq/team.md` | Already documents per-staff permission grants and the "6 hidden settings" behavior. |
| 18 | WhatsApp image/file sending (07/08) + fix (14/08) | PARTIAL | `kb/case/whatsapp-messenger-issues.md` | Feature itself was covered, but size/type/count limits (5MB image, 16MB video, 20MB doc, max 10 files) and the "previously all files were Meta-blocked, now fixed" note were missing. |
| 19 | WhatsApp PIN activation (17/07) | COVERED | `kb/case/whatsapp-messenger-issues.md` | Already documents the PIN-code activation step in the connection requirements. |
| 20 | Search by custom attribute (30/06) | COVERED | `kb/faq/inbox.md` | Already documents this + the 50-value limit. |
| 21 | Import FAQs into Conversation Starter (21/07) | COVERED | `kb/faq/chatbox-settings.md` | Already documents importing an FAQ as a starter (one-time copy caveat included). |
| 22 | Widget shows online only when staff on duty (07/07) | PARTIAL | `kb/faq/chatbox-settings.md` | The 3rd "Online status display" option existed in the doc implicitly but didn't state the key CS-relevant fact: AI keeps replying even when the storefront shows offline in this mode. |
| 23 | Chat revenue written to Shopify orders/customers (30/07) | GAP | `kb/faq/analytics.md` | Not documented anywhere; added new section incl. the order-write-permission caveat and early-cohort exclusion. |
| 24 | Custom handover/after-sale messages (14/07, 31/07, 06/08) | COVERED | `kb/faq/human-handover.md` | Already documents custom confirmation + staff-transfer messages (500-char limit) and after-sale form message customizability. |
| 25 | Order attribution 7-day window (06/08) | GAP | `kb/faq/analytics.md` | Not documented; merchants will ask why revenue dropped — added to new "Why Did My Revenue/Order Numbers Change?" section. |
| 26 | Refunded/cancelled orders excluded from revenue (31/07) | GAP | `kb/faq/analytics.md` | Same section — added with the median/top-10% impact numbers. |
| 27 | Funnel table now includes out-of-range-conversation orders (31/07) | GAP | `kb/faq/analytics.md` | Same section — order counts in the funnel can jump noticeably; merchants will ask why. |
| 28 | Product revenue nets out discounts (31/07) | GAP | `kb/faq/analytics.md` | Same section — flagged that pre-change orders keep old list-price numbers (period comparisons will look off). |
| 29 | Plan-tier locks enforced in exports (23/07) | GAP | `kb/faq/analytics.md` | Same section — lower-plan exports now missing columns they used to include. |
| 30 | Cross-sell block removed → Top Products chart (08/07) | GAP | `kb/faq/analytics.md` | Same section — direct "where did the Cross-sell block go" answer. |
| 31 | New chat widget UI (order card, coupon button, etc.) (04/07) | SKIP | — | Visual redesign already rolled out to everyone since 07/02; no behavior change or setting to document. |
| 32 | Pre-chat form no longer blocks questions (06/08) | COVERED | `kb/faq/chatbox-settings.md` | Duplicate of #7 — already covered. |
| 33 | Bulk-delete conversations (05/08) | COVERED | `kb/faq/inbox.md` | Already documents the feature with the destructive-delete-contacts warning. |
| 34 | Custom confirmation message after handover form (31/07) | COVERED | `kb/faq/human-handover.md` | Covered under Custom Confirmation & Staff-Transfer Messages. |
| 35 | Custom after-sale support form messages (06/08) | COVERED | `kb/faq/human-handover.md` | Covered under After-Sales Support Skill section. |
| 36 | Greeting/offline char limit 150→300 (15/07) | COVERED | `kb/faq/chatbox-settings.md` | Already states the 300-char limit. |
| 37 | AI reply links keep correct market domain (06/08) | **OUTDATED (critical)** | `kb/case/ai-wrong-responses.md` | KB had two "Known limitation — market/translated domain links NOT supported" sections that directly **contradict** the shipped fix. Rewrote both to reflect the 06/08 fix (basic tier vs. country-detection/Pro+ tier, per-market Manage overrides since 04/08) while preserving them as historical context for pre-fix chats. |
| 38 | Abandoned cart popup multi-language (07/08) | PARTIAL | `kb/faq/proactive-chat.md` | Added note to the template table + a dedicated chunk on the "already-running campaign doesn't auto-pick-up translation, must Save/Reset" caveat. |
| 39 | AI adapts tone/role to customer situation (13/08) | SKIP | — | Soft behavioral change, not a setting or fact CS would look up; nothing actionable to patch. |
| 40 | AI real actions — shipping address change + email subscription (13/08) | **GAP (major)** | `kb/case/ai-actions.md` (new file) | Completely new capability, no prior coverage at all. Wrote full guardrails (confirmation-required, order matching for guest vs. logged-in, shipped/cancelled exclusion, cancellation not supported). |
| 41 | AI no longer fabricates policy (13/08) | GAP | `kb/case/ai-wrong-responses.md` | No prior coverage of the old fabrication behavior or the fix; added as a new section right before "AI Reverts to Default Behavior," with guidance to check training data first if wrong-policy reports continue post-fix. |
| 42 | Spam flagged only, not auto-blocked (14/08) | **OUTDATED** | `kb/faq/general-settings.md` | KB said Smart spam protection "automatically classifies and blocks" — now flag-only by default with block as opt-in. Direct contradiction, fixed. |
| 43 | WhatsApp file sending Meta-block fix (14/08) | PARTIAL | `kb/case/whatsapp-messenger-issues.md` | Folded into #18's patch as a "known fixed bug" note. |
| 44 | AI reads Contact page (previously excluded if short) (17/08) | PARTIAL | `kb/faq/data-sources.md` | Auto-synced pages list already included "Contact us" but didn't flag the short-page exclusion bug/fix — merchants who previously got "I don't have contact info" may ask why it works now. |
| 45 | After-sale flow resumes after interrupting message (15/08) | SKIP | — | Internal robustness fix, no visible behavior change to document. |
| 46 | Messenger duplicate reply display bug (10/08) | SKIP | — | Agent-side display bug only, customers never affected; not merchant-facing. |
| 47 | Minor bug fixes (image-forgetting, Overview/Sales mismatch, handover-language, auto-close-reopen) | SKIP | — | All internal fixes with no new setting/behavior for CS to explain. |

## Counts

- **OUTDATED: 3** (plan limits, market-domain links, spam flag-vs-block) — #11, #37, #42
- **GAP: 8** (customer tags, revenue-to-Shopify, order-attribution-window, refund-exclusion, funnel-scope, product-revenue-discount, plan-tier-export-locks, cross-sell-removed, AI real actions, policy-fabrication-fix) — note: several of these were folded into one `analytics.md` patch (#23, #25–30) plus standalone `ai-actions.md` (#40) and small additions to `ai-agent-settings.md` (#3) and `ai-wrong-responses.md` (#41)
- **PARTIAL: 7** (View Cart trigger, Chat-to-Sale sub-tab, Product Quiz, WhatsApp limits, online-status-AI-still-replies, abandoned-cart-language, contact-page-fix) — #1, #13, #14, #18, #22, #38, #44
- **COVERED: 18** — items already accurately reflected in KB (a good sign that prior sync rounds, especially the 28/06–12/08 digest window, already got picked up well)
- **SKIP (pure internal/no merchant-facing behavior): 8**

Total patched files: **13** (12 edits to existing files + 1 new file `kb/case/ai-actions.md`).

## Notes for Liz

- The two most important OUTDATED fixes are **#37 (market domain links)** and **#42 (spam flag-vs-block)** — both had the KB stating the *opposite* of current behavior, which is a direct hallucination risk for the bot if a merchant asks about either.
- **#11 (Plan limits)** matters for billing conversations — a CS agent or bot quoting "Plus caps at 20,000 products" would be telling merchants a real cap exists when it no longer does.
- **#40 (AI real actions)** is the biggest net-new capability this cycle and had zero prior KB coverage — recommend testing this one first with `/kb-test` once pushed, since the guardrails (guest matching, shipped-order exclusion) are exactly the kind of detail a bot might get subtly wrong.
