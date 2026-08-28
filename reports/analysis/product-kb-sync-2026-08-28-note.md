# Product KB Sync — 2026-08-28 (diff-only, review-gate)

## Chatty
- Slack: 2 release posts (20/08, 26/08) fetched via shared channel (chatty's own fetch_slack.py hit Slack 429; used Joy's fetch of the same shared channel instead — content identical).
- GitLab (`avada-helpcenter-faqs`): 428 commits since last sync, **zero** changes under configured B1/B2 paths — no code-side signal.
- Classified 2 GAP + 2 OUTDATED (all from Slack, bug-fix-only items skipped). Payload: `product-kb-sync-chatty-2026-08-28-payloads.json` (3 files).
  1. **GAP** `kb/faq/ai-training-setup.md` — new "Bulk edit status" CSV feature (AI agent → Training data → Products → More actions), not in KB at all.
  2. **OUTDATED** `kb/faq/ai-training-setup.md` ("AI Capabilities & Limits") — AI can now build a real cart + checkout link on Messenger/WhatsApp/Instagram/email (24/08), not just the website widget.
  3. **GAP** `kb/case/ai-wrong-responses.md` — new case section explaining the 20/08 AI-engine migration (ai-vm) so CS doesn't over-escalate "AI sounds different" reports.
  4. **OUTDATED** `kb/faq/channels.md` — added a cross-reference note for the same cross-channel checkout capability as #2.
- **⚠️ Flag for Liz:** items #2/#4 (cross-channel AI checkout) come from a Slack note saying the merchant-facing help center release note for this is still a draft, not yet published. Patching CS's KB now means Ivy could tell merchants about it before the official announcement. Decide whether to push as-is, hold #2/#4 back, or push once the release note is public.

## Joy
- Slack: shared channel had 2 posts in this window, both entirely `:chatty:`-tagged — zero Joy-specific release content this run.
- GitLab (`starlink-team/joy`): 350 commits since last sync. B1 diffs found were internal engineering docs (implementation plans not yet confirmed shipped: tier-activities-tab, milestone-claimable-badge, SMS-subscribe-phone-bonus, referral-export-fix; plus an internal ShopifyQL field-rename reference and an internal AI-image-generation config default) — none merchant-facing or confirmed live, so none patched. B2 diffs (locale JSON + translation widget JS) came back with empty diff bodies from GitLab's compare API (likely size-truncated) — not practically reviewable this run.
- **Result: nothing to patch for Joy this run.** No payload file generated.

State (`state/last_sync.json`) intentionally NOT advanced for either app — advances only after Liz reviews, per skill's step 7.
