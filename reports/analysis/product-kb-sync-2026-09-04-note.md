# Product KB Sync — 2026-09-04 (diff-only, review gate)

Run for Chatty + Joy (Wishlist skipped, pre-launch). Signals: Slack #product-release
(shared channel, filtered per app) + GitLab diff on B1/B2 paths per app.

- Chatty: GitLab returned empty (no feature-doc/label changes in range) — Slack only.
  GAP=3, OUTDATED=2, PARTIAL=10, SKIPPED=7 (cosmetic/invisible). 11 files patched.
- Joy: GitLab had real content, surfaced 3 features Slack never mentioned (Coupon QR
  code, Tier Activities tab, Referral export Status column). GAP=9 (1 low-confidence,
  corrected by hand — see below), PARTIAL=1, COVERED=1, SKIP=5. 5 files patched.

Manual correction: subagent drafted the "open widget from theme account button" KB
section as a hedged/unverified note (claimed Slack text was unavailable due to a 429).
The actual Slack message (03/09 Joy release) had the exact location and mechanics —
rewrote that section using the real source before finalizing the payload.

Payloads:
- product-kb-sync-chatty-2026-09-04-payloads.json
- product-kb-sync-joy-2026-09-04-payloads.json

Not pushed, not reindexed, state/last_sync.json untouched — awaiting Liz's review.
