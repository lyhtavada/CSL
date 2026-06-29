# KB-sync diff — Chatty (week Jun 22–28, 2026)

> Mined-FAQ source: `reports/weekly-faqs/chatty/chatty_2026-06-22_2026-06-28.md` (30 FAQs, 372 sessions)
> Live KB compared: `chatty-agent` on cs2.avada.net (70 files, cached to `/tmp/kb-sync/chatty/`)
> Run mode: **DIFF-ONLY / review-gate** — no push, no reindex.
> Payloads: `reports/analysis/kb-sync-chatty-2026-06-28-payloads.json`

## Verdict counts
- **OUTDATED:** the plan/pricing schema is stale across the KB (multiple files).
- **GAP:** 4 (Q7 404-defect, Q11 AI-talks-over-agent, Q12 myshopify product links, Q20 Suggest-reply Beta)
- **PARTIAL:** 6 (Q5 CSV "Failed" rows, Q7 cross-link, Q14 open-straight-into-chat, Q22 speed vs latency + refund, Q26 email-only CRM/seats, Q30 Public API + Mailchimp/Zoho)
- COVERED (no action): Q1, Q2, Q4, Q8, Q9, Q10, Q13, Q15–Q19, Q21, Q23, Q24, Q25, Q27, Q29

## OUTDATED — current correct facts
Free: **50 AI conv LIFETIME** (not monthly), **100 products**, 90-day history.
Basic $19.99: **50 conv/mo**, **500 products**, **5 seats**, 12-month history.
Pro $68.99: **300 conv/mo**, **8,000 products**, **10 seats**, unlimited history.
Plus **$199**: **700 conv/mo**, **20,000 products**, unlimited seats, unlimited history.
$0.40/extra conversation; 7-day trial.

Stale facts found (all occurrences patched):
1. Free conversations "50/month (resets monthly)" → 50 lifetime. (pricing, ai-conversations, ai-conversation-limit, ai-wrong-responses, knowledge-base)
2. ai-conversation-limit.md: "monthly quota that resets each month (including the Free plan)" → paid reset monthly, Free 50 is lifetime.
3. Products: Free 200→100, Basic 1,500→500, Plus Unlimited→20,000. (pricing, knowledge-base, ai-product-limit, ai-product-sync, ai-sync-issues, ai-training-setup)
4. AI conv counts: Basic 100→50, Pro 500→300, Plus 1,000→700. (pricing, ai-conversations, ai-conversation-limit, knowledge-base)
5. team.md seats: Basic 3→5 total, Pro 5→10 total (matched the file's own table).
6. knowledge-base.md Plus price $199.99 → $199.
7. knowledge-base.md Basic chat-history Unlimited → 12 months.
8. inbox.md web-app URL app.meetchatty.com → app.chatty.net.

## GAP
- **Q7 (freq ~25+) — 404 / inbox-crash / mis-routing defect** → new section in `kb/faq/inbox.md`. Top escalation of the week; no consolidated KB entry existed. Agent-facing handling: hard-refresh/incognito first; else collect session IDs / customer emails / Loom / store URL / timestamps → escalate P1; don't reinstall.
- **Q11 (freq ~8) — AI replies after a human Joined** → `kb/faq/live-chat.md` (sibling of "AI Not Resuming After Human Takeover"). Ensure Join/assign; if it still talks over the agent, collect convo ID + which agent joined + assigned? → escalate.
- **Q12 (freq ~5) — AI product links use `.myshopify.com`** → `kb/case/ai-wrong-responses.md`. Confirm primary domain → re-sync; if persists, escalate with convo ID + example link.
- **Q20 (freq ~3) — Suggest-reply Beta** → `kb/faq/ai-agent-settings.md`. AI drafts, human reviews + sends; formatting/accuracy limits; log opt-in interest.

## PARTIAL
- **Q5 (freq ~8)** CSV rows "Failed" = topic Published-but-not-Active → set Active, re-upload; support clears stuck rows. (`kb/faq/ai-training-setup.md`)
- **Q7 cross-link** — link existing "Conversations Mixing Between Threads" note to the new Q7 section. (`kb/faq/inbox.md`)
- **Q14 (freq ~6)** open straight into chat — trim conversation starters, turn off pre-chat form / allow anonymous, ensure Live-chat block on. (`kb/faq/live-chat.md`)
- **Q22 (freq ~6)** split AI latency (10–30s, escalate) vs storefront page-speed tied to refund — gather evidence, route refund. (`kb/case/chatbox-widget-issues.md`)
- **Q26 (freq ~4)** email-only CRM / seats without Shopify plan — connect email only, assign+label, app.chatty.net login, no Shopify seat. (`kb/faq/team.md`)
- **Q30 (freq ~3)** no API conversation-export endpoint (via support); Mailchimp/Zoho no native integration → CSV / Klaviyo; log feature requests. (`kb/faq/klaviyo.md`)

## Priority (by mined frequency)
1. Q7 — 404/inbox-crash defect (~25+) — GAP + cross-link
2. Q28/Q3 — pricing & product limits (12) — OUTDATED across ~10 files
3. Q6 — out-of-conversations (8) — OUTDATED (Free lifetime + conv counts)
4. Q11 — AI talks over agent (8) — GAP
5. Q5 — CSV Failed rows (8) — PARTIAL
6. Q14 — open straight into chat (6) — PARTIAL
7. Q22 — speed vs latency + refund (6) — PARTIAL
8. Q12 — myshopify product links (5) — GAP
9. Q26 — email-only CRM / seats (4) — OUTDATED + PARTIAL
10. Q20 — Suggest-reply Beta (3) — GAP
11. Q30 — Public API / Mailchimp / Zoho (3) — PARTIAL
