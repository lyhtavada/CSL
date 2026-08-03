# KB Sync — Chatty (Ivy) — Diff Report

**Mined-FAQ window:** Jul 20–26, 2026 (`reports/weekly-faqs/chatty/chatty_2026-07-20_2026-07-26.md`, 469 sessions, 40 FAQs)
**KB cache:** `/tmp/kb-sync/chatty/` (88 files, cached 2026-07-28)
**Status:** DIFF ONLY — not pushed. Payloads staged at `reports/analysis/kb-sync-chatty-2026-07-26-payloads.json`. Awaiting Liz's approval before `push_kb.py` + reindex.

---

## Summary Table

| Q# | Topic | KB file(s) | Verdict |
|---|---|---|---|
| Q1 | AI agent first-time setup | `kb/faq/ai-training-setup.md`, `kb/faq/quick-start.md` | COVERED |
| Q2 | Done-for-you setup intake | `flows/done_for_you.md` | COVERED |
| Q3 | Chatbox/widget live | `kb/faq/quick-start.md`, `kb/faq/chatbox-settings.md` | COVERED |
| Q4 | FAQ setup (page vs Q&A) | `kb/faq/faqs-page.md`, `kb/faq/add-questions.md`, `kb/faq/data-sources.md` | COVERED |
| Q5 | Where AI gets its answers | `kb/faq/data-sources.md` | COVERED |
| Q6 | Discount code not suggested (3rd-party apps) | `kb/case/discount-sync.md` | COVERED |
| Q7 | Product sync stuck/timing (00:00 UTC vs 12:00 AM PST) | `kb/case/ai-sync-issues.md`, `kb/case/ai-product-sync.md`, `kb/faq/data-sources.md`, `kb/faq/knowledge-base.md` | **FLAGGED — not patched** (see note) |
| Q8 | Training file/URL not used | `kb/faq/data-sources.md`, `kb/faq/ai-training-setup.md` | COVERED |
| Q9 | AI gave wrong/outdated info | `kb/faq/test-and-optimize-ai.md`, `kb/case/ai-wrong-responses.md` | COVERED |
| Q10 | Chat button position / mobile caveat | `kb/faq/chatbox-settings.md`, `kb/case/chatbox-widget-issues.md` | COVERED |
| Q11 | Welcome message shows old text | `kb/faq/chatbox-settings.md` | **PARTIAL** |
| Q12 | AI recommends wrong/OOS products | `kb/faq/ai-training-setup.md` | COVERED |
| Q13 | AI shares exact stock quantity | `kb/faq/ai-training-setup.md` | **GAP** |
| Q14 | Custom Scenario overridden by built-in skill | `kb/faq/train-ai.md` | COVERED |
| Q15 | Product-page AI carries over previous product's context | `kb/faq/ai-training-setup.md` | **OUTDATED** |
| Q16 | Remove cart element from chatbox | `kb/faq/chatbox-settings.md` | COVERED |
| Q17 | Hide widget on certain pages | `kb/faq/chatbox-settings.md` | COVERED |
| Q18 | Delay widget appearing | `kb/faq/chatbox-settings.md` | **GAP** |
| Q19 | Proactive Chat popup wrong content | `kb/faq/proactive-chat.md` | COVERED |
| Q20 | Change name/avatar/colours | `kb/faq/ai-training-setup.md`, `kb/faq/chatbox-settings.md` | COVERED |
| Q21 | FAQ page URL "already taken" | `kb/faq/faqs-page.md` | COVERED |
| Q22 | Only some FAQs showing | `kb/faq/add-questions.md` | **PARTIAL** |
| Q23 | AI-generated FAQ exposed PII | `kb/faq/faqs-page.md`, `kb/faq/ai-training-setup.md` | COVERED |
| Q24 | Unread counter / resolved reappear as unread | `kb/faq/inbox.md`, `kb/faq/others.md` | COVERED |
| Q25 | Can't log in web/mobile app | `kb/case/access-login-issues.md` | COVERED |
| Q26 | Meta phone-number limit blocks WhatsApp | `kb/case/whatsapp-messenger-issues.md` | COVERED |
| Q27 | WhatsApp Pending / wrong number | `kb/case/whatsapp-messenger-issues.md` | COVERED |
| Q28 | AI on Instagram/Messenger | `kb/faq/channels.md` | COVERED |
| Q29 | Email channel won't verify (Outlook) | `kb/case/email-channel-issues.md` | COVERED |
| Q30 | Chatbox/FAQ language + plan limits | `kb/faq/translation.md` | COVERED |
| Q31 | AI replies in wrong language | `kb/case/translation-issues.md` | **PARTIAL** |
| Q32 | Get notified on new message | `kb/case/notification-issues.md` | COVERED |
| Q33 | No push notifications on phone | `kb/case/notification-issues.md` | COVERED |
| Q34 | Pricing table | `kb/faq/pricing.md` | **OUTDATED** |
| Q35 | Extend free trial | `kb/faq/pricing.md` | COVERED |
| Q36 | Extend plan data limits | `kb/faq/pricing.md`, `kb/case/ai-product-sync.md` | COVERED |
| Q37 | ADA/WCAG accessibility | `kb/faq/ai-compliance.md` | **GAP** |
| Q38 | GDPR cookie consent — Proactive Chat cart cookies | `kb/faq/cookie-policy.md` | **OUTDATED** |
| Q39 | Shopify Markets multi-domain link routing bug | `kb/case/ai-wrong-responses.md` | **PARTIAL** |
| Q40 | China / Google Cloud blocked | `kb/case/access-login-issues.md` | COVERED |

**Totals:** 27 COVERED · 3 OUTDATED · 3 GAP · 4 PARTIAL · 1 flagged-not-patched (Q7)

---

## OUTDATED (3)

### 1. Q34 — Pricing table (`kb/faq/pricing.md`) — HIGH PRIORITY
Verified against **chatty.net/pricing** live page source (fetched today, table extracted directly from the page's HTML — not paraphrased):
- Products for AI training: Free 200 / **Basic 500** / Pro 8,000 / Plus Unlimited
- Custom answers for AI training: Free 100 / **Basic 1,000** / Pro Unlimited / Plus Unlimited
- URL & File for AI training: Free 20 / Basic 50 / **Pro 500** / **Plus 700**

**Stale lines in KB (verbatim):**
- `"1,500 products"` (in the "Chatty Plans & Pricing" Basic bullet)
- `"products 1,500, custom answers 5,000, URLs & files 200"` (in "Plan Feature Comparison" Basic row)
- `"URLs & files 2,000"` (Pro row)
- `"URLs & files unlimited, team members unlimited"` (Plus row)

**Fix applied:** replaced with the live-verified figures above (Basic → 500 products / 1,000 custom answers / 50 URLs&files; Pro → 500 URLs&files; Plus → 700 URLs&files). Team members and chat history figures were already correct — untouched.

### 2. Q38 — GDPR cookie consent (`kb/faq/cookie-policy.md`)
**Stale line (verbatim):** "Chatty uses a single cookie called `avada-chatty/session`. This cookie is essential for the live chat service to function correctly." — presents this as the *only* cookie Chatty sets.

**Correct fact (mined Q38):** Some Proactive Chat cart features (Cart booster, Remove items from cart) set **additional cart-related cookies** beyond the session cookie, which may need consent under GDPR/ePrivacy. A consent gate is planned but not shipped; disabling the specific cart-related campaigns is the current workaround.

**Fix applied:** inserted a "Proactive Chat cart cookies" clarification paragraph immediately after the stale line.

### 3. Q15 — Product-page AI context carryover (`kb/faq/ai-training-setup.md`, "AI Page Context Detection")
**Stale line (verbatim):** "Yes — Chatty automatically detects the current page URL and product context. When a customer asks a question on a product page, the AI uses that product's information to answer." — presented as working cleanly, no caveat.

**Correct fact (mined Q15):** Known, **open, unresolved** dev issue — product card updates correctly but the AI's text answer can still reference the previously viewed product.

**Fix applied:** appended a "Known issue (open, unresolved)" paragraph with escalation guidance (collect product URLs + screen recording).

---

## GAP (3)

### 1. Q13 — AI shares exact stock quantity (`kb/faq/ai-training-setup.md`)
Existing "AI Product Inventory Sync" section only covers real-time sync limitations and out-of-stock handling — no mention of suppressing exact-quantity disclosure. **Added** a new "Preventing the AI From Disclosing Exact Stock Quantity" subsection: team can review Inventory-related AI settings and turn off exact-quantity disclosure on request. Flagged in the added text itself that no dedicated self-serve toggle is confirmed yet (per the mined report's own caveat — PM/dev confirmation still pending for a fuller self-serve answer).

### 2. Q37 — ADA/WCAG accessibility (`kb/faq/ai-compliance.md`)
No file in the KB addresses accessibility at all. **Added** a new "## Accessibility (ADA / WCAG)" section: no published accessibility statement/WCAG report yet; known gaps (ESC key dismissal, ARIA labels, focus management, heading hierarchy) under engineering review; guidance to flag urgency internally for compliance-deadline cases.

### 3. Q18 — Delay widget appearing (`kb/faq/chatbox-settings.md`)
No section covers a deliberate appearance delay (the existing "Chatbox Opening Automatically" section only covers *unwanted* auto-open causes). **Added** a new "## Delaying When the Widget Appears" section: no built-in delay setting; technical team can apply a custom script/CSS delay on request.

---

## PARTIAL (4)

### 1. Q11 — Welcome message shows old text (`kb/faq/chatbox-settings.md`, "Changing the Welcome Message")
Section already covers the 2 main locations (Chatbox → Chat page for AI-off; AI agent → Settings → AI identity for AI-on) but **missing**: (a) a 3rd override — **Settings → Translations → [language]**, which overrides both for that published language; (b) the clarification that **Proactive Chat's popup message is a separate, different setting**. **Added** both points immediately after the existing two-location explanation.

### 2. Q22 — Only some FAQs showing (`kb/faq/add-questions.md`, "Import FAQs in Bulk")
Section documents the CSV's "Published question"/"Featured question" fields but never states the practical consequence: **missing** the direct troubleshooting note that imported FAQs default to draft. **Added** a "Only some imported FAQs showing..." note right after the upload-options bullets.

### 3. Q31 — AI replies in wrong language (`kb/case/translation-issues.md`, "AI Replies in the Wrong Language")
Section covers the behaviour-instruction fix and chatbox auto-detection but is **missing** the specific diagnostic from this week's real cases: the trigger is often **untranslated Conversation Starters**, not the AI's language detection. **Added** as a new bullet at the end of the section.

### 4. Q39 — Shopify Markets multi-domain routing (`kb/case/ai-wrong-responses.md`, "AI Showing Main Domain Instead of Market Domain")
Section frames this as a general "known limitation" with a workaround. **Missing**: this week's case shows (a) it also affects **checkout links**, not just product links, for Shopify Plus/multi-market stores, and (b) it's now a **confirmed, internally tracked bug with a fix in progress** — a stronger status than "limitation," changing what CS should tell affected merchants. **Added** an "Update (Shopify Plus, multi-market stores)" paragraph right after the "Known limitation" line.

---

## Flagged, not patched

### Q7 — Product sync timing: 00:00 UTC (KB) vs 12:00 AM PST (mined answer)
5 occurrences of "00:00 UTC" across `kb/case/ai-sync-issues.md`, `kb/case/ai-product-sync.md`, `kb/faq/data-sources.md`, `kb/faq/knowledge-base.md`, all internally consistent with each other. The mined-FAQ's "12:00 AM PST" wasn't called out as a newly-verified fact in its own "what changed" section (unlike Q34's pricing figures, which were cross-checked against chatty.net/pricing directly). Rather than blind-patch 5 files off an unverified single data point, this is flagged for Liz/PM to confirm the actual sync time before a patch is drafted. **No file changed for this item.**

---

## Priority (ranked by mined frequency, patched items only)

| Rank | Q# | Freq | Type | Why |
|---|---|---|---|---|
| 1 | Q34 | ~12 sessions | OUTDATED | Pricing errors on Basic/Pro/Plus limits — verified live against chatty.net/pricing; directly affects billing conversations and trust. |
| 2 | Q11 | ~8 sessions | PARTIAL | Recurring welcome-message confusion; missing 3rd location (Translations) is a high-value, easy fix. |
| 3 | Q31 | ~3 sessions | PARTIAL | Useful diagnostic shortcut (Conversation Starters) missing from an otherwise solid section. |
| 4 | Q13 | ~1 session (new) | GAP | Real resolved case, but no self-serve settings path documented yet. |
| 5 | Q15 | ~1 session (new, open bug) | OUTDATED | KB currently claims clean page-context detection, contradicting an active unresolved dev issue. |
| 6 | Q37 | ~1 session (new, open) | GAP | Legal/compliance exposure (ADA lawsuit concern) — no accessibility content exists at all. |
| 7 | Q38 | ~1 session (new, unresolved) | OUTDATED | Incomplete "single cookie" claim — GDPR/compliance risk. |
| 8 | Q39 | ~1 session (new, enterprise/Plus) | PARTIAL | High-value merchant segment; status upgrade from "limitation" to "tracked bug + fix in progress" changes CS messaging. |
| 9 | Q22 | ~1 session (new) | PARTIAL | Minor, self-serve-fixable troubleshooting note. |
| 10 | Q18 | ~1 session (new) | GAP | Low frequency, low complexity documentation add. |

---

## Files touched (8), staged in payloads.json

1. `kb/faq/pricing.md`
2. `kb/faq/cookie-policy.md`
3. `kb/faq/ai-training-setup.md`
4. `kb/faq/ai-compliance.md`
5. `kb/faq/chatbox-settings.md`
6. `kb/faq/add-questions.md`
7. `kb/case/translation-issues.md`
8. `kb/case/ai-wrong-responses.md`

**Next step:** Liz reviews this diff + the payloads file, then approves push via `python3 ~/CSL/skills/kb-sync/scripts/push_kb.py ~/CSL/reports/analysis/kb-sync-chatty-2026-07-26-payloads.json`.
