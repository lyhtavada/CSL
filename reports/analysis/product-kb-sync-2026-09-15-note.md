# Product KB Sync — 2026-09-15 (diff-only, review-gate)

## Chatty
- Slack: releases 20/08, 26/08, 04/09 fetched (since_ts 1787212665.307569 → latest 1788506031.307929).
- GitLab (`avada-helpcenter-faqs`): no relevant B1/B2 changes (1226 commits scanned, all i18n/nav diffs empty/unrelated).
- Almost every merchant-facing item from the three Slack releases (bulk CSV enable/disable, ai-vm engine migration, order-code handling, human-handover destination fix, holiday/off-hours fix, campaign save fix, Product Quiz fix, plan-upgrade limit fix, cart-on-social-channels, inbox summarize fix) is **already documented** in the live KB — evidently already patched via the reactive `/mine-chat-faqs` → `/kb-sync` chain, which runs more frequently than this proactive skill.
- One real gap found: **04/09 unified Knowledge base tab** (merges FAQs + Custom knowledge, adds Draft/Live/Off per entry) — not yet in KB. Rollout scope (all merchants? all plans?) wasn't confirmed in the Slack post itself, so the patch is an additive, clearly-flagged callout in `kb/faq/ai-training-setup.md` rather than a rewrite of the many existing "Training data → FAQs / Custom knowledge" nav references elsewhere — those stay authoritative until GA is confirmed.
- Skipped: **02/09 AI Mode "shopping assistant"** — explicitly `dev_zone`-gated, not available to merchants yet (per the release note itself).
- Payload: `product-kb-sync-chatty-2026-09-15-payloads.json` (1 entry).

## Joy
- Slack: releases 28/08, 03/09 fetched (same shared channel/timestamp range).
- GitLab (`starlink-team/joy`): B1 feature docs + B2 label files, 1288 commits scanned.
- Every merchant-facing Slack item (Subscribe SMS marketing + phone bonus, phone-prefix auto-detect, Milestone claim badge/event, Referral activity in widget, Widget v4 on-brand/account-button/Account mode) is **already documented** in the live KB, in more implementation detail than the Slack post itself.
- GitLab B1 `coupon-qr-code.md` (shipped feature) — **already documented** in `kb/reference/widget.md` ("Coupon QR code (My Coupons)"), matching file-for-file.
- GitLab B1 `member-exclusive-deal-duplicate.md` — explicitly "Status: proposed — NOT product-approved" in the doc itself. Correctly skipped.
- Other B1 docs (`shopifyql-loyalty-fields.md`, `brand-identity-store.md`, `flexible-tier-reset-frequency.md`, `loyalty-widget-demo.md`) are internal/engineering-only (ShopifyQL field renames for the AI agent's own query-building, backend groundwork, internal helper rename, AI image-gen model config) — no merchant-facing KB impact.
- No payload produced — nothing survived classification as OUTDATED/GAP/PARTIAL this run.

## State
Per instructions, `state/last_sync.json` was **not** updated for either app — this was a review-gate run. Advance state for both apps after Liz reviews (Joy: nothing to advance past besides bumping the checkpoint since there's no pending patch; Chatty: bump only after the one payload above is pushed, per SKILL.md step 7).
