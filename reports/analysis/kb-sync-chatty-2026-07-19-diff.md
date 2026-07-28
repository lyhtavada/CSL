# KB Diff — Chatty (mined FAQ 2026-07-13→19 vs live KB)

75 mined FAQs reviewed. 64 COVERED, 2 OUTDATED, 3 GAP, 4 PARTIAL (verified item-by-item against cached KB files, not by frequency estimate).

## OUTDATED
1. **Mobile app description** (`kb/faq/mobile-app.md`, `kb/faq/quick-start.md`, `kb/faq/web-app.md`, `kb/case/notification-issues.md`) — all 4 files claim a native App Store/Google Play app "Chatty AI Sale Assistant" with an App Store URL. Mined FAQ (fresh, ~10 sessions) says the mobile app is a **PWA** installed via browser "Add to Home Screen", no App Store/Play listing. ⚠️ **Verify with product/dev before push** — this is a hard factual reversal across 4 files with a suspicious identical URL; patch assumes the mined (PWA) answer is correct.
2. **Plan comparison table** (`kb/faq/knowledge-base.md`) — Basic chat history listed as "Unlimited", should be **12 months** (matches `kb/faq/pricing.md`); Plus price listed as $199.99/mo, should be **$199/mo**.

## GAP
1. `kb/case/email-channel-issues.md` — own marketing emails landing in Chatty inbox
2. `kb/faq/channels.md` — can't forward chats to personal WhatsApp (feature request, not supported)
3. `kb/faq/others.md` — shopper messaging Chatty's own vendor support inbox by mistake

## PARTIAL
1. `kb/faq/data-sources.md` — added FAQs/Custom knowledge/Instructions/Scenarios rule-of-thumb
2. `kb/faq/ai-training-setup.md` — added "metafields limit reached, contact us to raise" note
3. `kb/case/ai-wrong-responses.md` — added conversation-starters as hidden root cause for stale answers
4. `kb/case/ai-wrong-responses.md` — added product-level vs variant/inventory recommendation limitation

11 files patched. Payloads: `reports/analysis/kb-sync-chatty-2026-07-19-payloads.json`
