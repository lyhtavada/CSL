# KB Update Summary — April 2026
**Source:** `chatty-common-issues-2026-04.md` (62 entries)
**Date:** 2026-04-03
**Author:** Betty (subagent)

---

## Overview

| | Count |
|---|---|
| Total source entries | 62 |
| New files created | 0 |
| Files merged/updated | 10 |
| New chunks added | 28 |
| Entries skipped (already covered) | 34 |

---

## Files Merged (10 files, 28 new chunks)

### 1. `case_ai-wrong-responses.md` — 3 chunks added
- **`ai-wrong__not-responding`** (Very High) — AI gives no response at all; covers AI toggle, training data, Live Chat block, and conversation limit check
- **`ai-wrong__hallucination-over-promising`** (High) — AI offers refunds/replacements; Scenario + Custom Instructions fix; known limitation note
- **`ai-wrong__reverts-to-default`** (Medium) — AI "forgets" training; covers save verification, data source check, keyword specificity, escalation path

### 2. `faq_ai-training-setup.md` — 6 chunks added
- **`ai-training__metafields`** (Medium) — Does AI read Shopify metafields; metaobject limitation note
- **`ai-training__file-upload-details`** (Medium) — File formats (PDF/CSV/TXT/JSON), 2MB limit, CSV recommendation
- **`ai-training__language-switching`** (Medium) — AI responding in wrong language mid-conversation; Translation settings + Custom Instructions fix; Pro+ real-time translation note
- **`ai-training__brand-voice`** (Medium) — Setting AI tone/persona via Custom Instructions; examples included
- **`ai-training__disable-product-recommendations`** (Medium) — Smart Recommendations toggle off; Custom Instruction option; plan note
- **`ai-training__bot-name-avatar`** (Medium) — Changing AI bot name, welcome message, and avatar; file format/size requirements

### 3. `faq_chatbox-widget-issues.md` — 3 chunks added + 1 enhanced
- **`chatbox-widget-position`** (enhanced, Very High) — Added CSS fix for ATC overlap, common conflicting elements, collaborator access path
- **`faq__chatbox-widget-blocking-other-apps`** (High) — Widget blocking BOGOS/ATC/scroll-top; CSS offset fix; collaborator access for TS
- **`faq__chatbox-hide-specific-pages`** (Medium) — Display Rules → Page Rules; URL patterns; URL-based exclusion
- **`faq__chatbox-faq-formatting-bullets`** (Low) — Known rich text rendering bug; TS ticket; plain text prevention tip

### 4. `faq_live-chat.md` — 4 chunks added
- **`faq__live-chat-human-handover-email`** (High) — Handover email config, "only online members" setting, email notifications for handover
- **`faq__live-chat-holiday-message-limitation`** (Medium) — Holiday offline message cannot be customized per period; feature limitation noted
- **`faq__live-chat-ai-not-resume`** (Medium) — Expected behavior after human takeover; Assign to AI step; proactive explanation tip
- **`faq__live-chat-customer-reset`** (Low) — Chatbox Style → "Allow users to reset conversation" setting

### 5. `faq_team.md` — 2 chunks added
- **`team__invitation-not-received`** (Medium) — Spam/junk folder check, Gmail Workspace, resend, alternative email
- **`team__multiple-simultaneous`** (Medium) — Yes multiple agents can work simultaneously; plan member limits table

### 6. `case_notification-issues.md` — 2 chunks added
- **`notification__mobile-pwa-setup`** (Medium) — PWA install instructions; iOS Safari requirement; no native App Store app
- **`notification__too-many-duplicates`** (Medium) — Notification trigger config; "notify only when unread"; multiple channel overlap diagnosis

### 7. `faq_whatsapp-messenger-issues.md` — 2 chunks added
- **`faq__instagram-24hr-window`** (Medium) — Instagram Send button greyed out = 24-hour messaging window expired; Meta platform restriction; workarounds
- **`faq__whatsapp-contact-button`** (Medium) — Adding WhatsApp shortcut button in chatbox; distinction from full WhatsApp channel connection

### 8. `faq_inbox.md` — 3 chunks added
- **`inbox__cannot-find-messages`** (Medium) — Check Resolved tab, channel filter; error code "9 Failed Pre-conditioning" → cache clear + escalate
- **`inbox__mark-all-resolved`** (Low) — No bulk resolve button yet; feature request logged; support can help with backend bulk resolve
- **`inbox__replies-back-to-chatty`** (Medium) — Expected behavior for email channel; Reply-To field workaround for merchants who prefer email client

### 9. `faq_translation-issues.md` — 2 chunks added
- **`faq__translation-save-and-publish`** (Medium, Very Common) — Two-step process: Save → Publish; additional checks for Shopify language activation
- **`faq__translation-faq-not-auto-updating`** (Low) — Translations don't auto-update on new FAQ content; manual re-translate + publish required

### 10. `case_email-channel-issues.md` — 1 chunk added
- **`email__corporate-it-restriction`** (High) — Corporate/IT-managed email blocks auto-forwarding; IT admin must whitelist Chatty; Gmail personal account workaround

---

## Entries Skipped — Already Covered (34 entries)

| Entry # | Issue | Already in file |
|---|---|---|
| 1 | AI giving wrong/inaccurate answers | `case_ai-wrong-responses.md` — comprehensive diagnostic flow |
| 3 | How to train AI (new merchant setup) | `faq_ai-training-setup.md` — setup-first-time chunk |
| 4 | Products not syncing | `case_ai-product-sync.md` |
| 5 | AI recommending wrong/competitor products | `case_ai-wrong-responses.md` — ai-wrong-foreign-products |
| 10 | Product limit per plan | `faq_ai-training-setup.md` + `faq_pricing.md` |
| 13 | AI links not clickable | `case_ai-wrong-responses.md` — ai-wrong-links-not-clickable |
| 14 | Disable follow-up questions | `faq_ai-training-setup.md` — ai-training-disable-followup |
| 16 | Disable Add to Cart button | `faq_ai-training-setup.md` — ai-training-suppress-atc |
| 17 | Widget not showing on store | `faq_chatbox-widget-issues.md` — chatbox-widget-not-showing |
| 19 | Move/reposition widget | `faq_chatbox-widget-issues.md` — chatbox-widget-position |
| 22 | Widget pop-up timing/delay | `faq_proactive-chat.md` |
| 23 | Change widget colors/icon | `faq_chatbox-settings.md` |
| 24 | Open widget via JavaScript | `faq_chatbox-widget-issues.md` — chatbox-javascript-control |
| 25 | FAQ page not showing | `faq_chatbox-widget-issues.md` — chatbox-faq-page-not-showing |
| 27 | FAQ page template conflicts | `faq_chatbox-widget-issues.md` — chatbox-faq-overwriting-templates |
| 29 | Help setting up live chat first time | `faq_live-chat.md` — live-chat-setup |
| 31 | AI provide support email instead of transfer | `case_ai-wrong-responses.md` — ai-wrong-email-instead-of-transfer |
| 32 | Set online hours / business hours | `faq_online-hours.md` — comprehensive coverage |
| 38 | Analytics for chat and AI performance | `faq_analytics.md` |
| 39 | Push notifications not working (mobile) | `case_notification-issues.md` — notification-mobile-not-working |
| 40 | Push notifications not working (desktop) | `case_notification-issues.md` — notification-desktop-not-working |
| 43 | WhatsApp number stuck in Pending | `faq_whatsapp-messenger-issues.md` — whatsapp-pending-status |
| 44 | WhatsApp connection failing | `faq_whatsapp-messenger-issues.md` — whatsapp-connection-requirements |
| 45 | WhatsApp AI without website widget | `faq_whatsapp-messenger-issues.md` — whatsapp-ai-no-widget |
| 47 | Email verification fails | `case_email-channel-issues.md` — email-forwarding-verification-fails |
| 48 | Instagram messages not appearing | `faq_whatsapp-messenger-issues.md` — instagram-messages-not-showing |
| 51 | Plan limits and what's included | `faq_pricing.md` — pricing-plans-overview + plan-comparison |
| 52 | AI conversation quota reset monthly | `faq_pricing.md` — pricing-ai-conversation-limits |
| 53 | Discount/promo code requests | `faq_billing-subscription.md` — billing-discount-request + billing-linkedin-discount |
| 54 | Cancel subscription / uninstall | `faq_pricing.md` — pricing-cancel-downgrade |
| 55 | Usage cap for overuse | `faq_pricing.md` — pricing-check-usage-spending-limit |
| 57 | Export conversation transcripts | `faq_inbox.md` — inbox-export-history |
| 61 | Languages supported per plan | `faq_translation.md` — translation-language-limits |

---

## Notes

- **No new files were created** — all 28 new entries fit cleanly into existing topic files
- **High-priority entries placed at top** of their respective chunks where relevant
- **Known limitations and escalation cases** are clearly marked in their chunks (e.g., metaobject support, per-holiday custom messages, bulk resolve)
- **No local containers were modified** — all changes are local file edits only
