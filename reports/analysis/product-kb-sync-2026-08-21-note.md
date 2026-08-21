# Product KB Sync — 2026-08-21 (diff-only, review-gate run)

Ran for chatty + joy. Wishlist skipped (pre-launch, low priority).

## Chatty
- Source: Slack `product-release` (19/08 post), GitLab `avada/avada-helpcenter-faqs` (edf29ee→22743df, 132 commits).
- Items classified: 4 from Slack.
  - PARTIAL → `kb/case/discount-sync.md` — AI can now proactively offer a discount code mid-chat (not just on request).
  - GAP → `kb/faq/klaviyo.md` — new SEA Post Purchase Survey integration.
  - HOLD (not drafted) → Inbox auto-reassign on member deletion — release note itself flagged as unconfirmed draft ("cần xác nhận... đang chờ duyệt"). Re-check next run once confirmed.
  - SKIP → Logout session fix — explicitly marked "not for public release note" (internal security fix, no merchant action).
- GitLab B2 diff (`AppFullLayout.js`) was a logic change (auth hook), not copy/nav — corroborates the logout item, filtered out per skill's noise rule.
- Payloads: `product-kb-sync-chatty-2026-08-21-payloads.json` (2 entries).

## Joy
- Source: Slack (no Joy-specific post in this window — only the Chatty release landed in the shared channel). GitLab `avada/starlink-team/joy` (c87877b→89782c5, 46 commits).
- B1 feature docs: `loyalty-widget-demo.md` (internal sales-demo AI image infra — not merchant-facing, skipped) and `perk-schedule.md` (Free Shipping perks joined Perk Schedule — CS-relevant).
  - OUTDATED/PARTIAL → `kb/reference/vip-tiers.md` — "Periodic (scheduled) perks" section didn't cover Free Shipping's dual mechanism, the refund-doesn't-restore-claim gap on Perk Schedule, or the "stuck hidden" flag-off edge case.
- B2 diff (`Modal.json`) — new locale strings for the above, corroborates the doc change, no separate action needed.
- Payloads: `product-kb-sync-joy-2026-08-21-payloads.json` (1 entry).

## Not done (by design, review-gate run)
No push, no reindex, no state advance. Liz reviews payloads → runs:
```
python3 ~/CSL/skills/kb-sync/scripts/push_kb.py <payloads.json>
```
State (`state/last_sync.json`) advances only after that, including for the held-back Chatty item once Liz decides how to handle it (patch after confirmation, or advance state to drop it).
