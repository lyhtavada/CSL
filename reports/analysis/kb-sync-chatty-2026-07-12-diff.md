# KB-sync diff — Chatty (Ivy) · window Jul 06–12 2026

Mined FAQ: `reports/weekly-faqs/chatty/chatty_2026-07-06_2026-07-12.md` (44 FAQs, 414 sessions)
Live KB: agent `chatty-agent` on cs2.avada.net (cached `/tmp/kb-sync/chatty/`)
**Review-gate run — nothing pushed, nothing reindexed.**

## Tally
- COVERED: 34 · **OUTDATED: 2 facts (6 files)** · **GAP: 4** · **PARTIAL: 1**
- Payloads (8 files): `reports/analysis/kb-sync-chatty-2026-07-12-payloads.json`

## OUTDATED (fact drift — mined + canonical pricing.md both win)
1. **Basic AI-product limit `1,500` → `500`.** `kb/faq/pricing.md` (canonical) and this week's chats (Q9/Q37) both say **500**; six other files still say 1,500. Fixed in: `kb/faq/ai-training-setup.md` (×2), `kb/faq/knowledge-base.md` (×1), `kb/case/ai-product-sync.md` (×1), `kb/case/ai-sync-issues.md` (×2).
2. **Basic chat history `Unlimited` → `12 months`** and **`noreply@chattyemail.com` → `noreply@chatty.email`** in `kb/faq/knowledge-base.md` (both agree with pricing.md / email-channel case).

> ⚠️ **Left out on purpose — needs your call:** `kb/case/ai-product-limit.md` also holds `1,500` in **two** places, but one is the CS *extend-limit* logic row (`Free → 1,500 (= Basic)`). If Basic's real cap is 500, that extend target also shifts. I did **not** touch this file — decide the true extend target before editing it.

## GAP (new content, paste-ready)
- **Q24 mic/voice "no permission"** → `kb/case/access-login-issues.md` (new case, before `## Related`)
- **Q27 WhatsApp profile photo** → `kb/case/whatsapp-messenger-issues.md` (before `## Outbound WhatsApp Messages`)
- **Q43 Chatty can't edit theme footer/IG icon** → `kb/faq/others.md`
- **Q44 remove Shopify Inbox popup** → `kb/faq/others.md`

## PARTIAL
- **Q20 match WhatsApp launcher size/align to bubble** → `kb/case/chatbox-widget-issues.md` (sub-section under widget-overlap)

## Not actioned (agent-side noise, no merchant answer)
- Q41 shopper in support widget · Q42 marketing emails as tickets — internal triage only.

## After review
```
python3 ~/CSL/skills/kb-sync/scripts/push_kb.py reports/analysis/kb-sync-chatty-2026-07-12-payloads.json
```
