# product-kb-sync — 2026-08-14 (diff-only run)

Review-gate run for Chatty + Joy. No push/reindex/state update performed — waiting on Liz's review.

## Chatty
- Signals: Slack weekly posts 25/05–25/06 + rollup post 10/08 (28/06→12/08, 18 features/32 improvements/29 behavior changes). GitLab diff had no usable signal (44 commits, all touched files unrelated/noise).
- 8 files patched (OUTDATED/GAP/PARTIAL): pricing.md, knowledge-base.md, proactive-chat.md, human-handover.md, ai-training-setup.md, inbox.md, analytics.md, product-quiz.md.
- Payloads: `product-kb-sync-chatty-2026-08-14-payloads.json`

## Joy
- Signals: Slack had 2 new messages since last sync, both zero Joy Loyalty content (discarded). GitLab compare API truncated diffs on this large window — worked around by diffing raw file content at from/to SHA directly for B2 locale/widget files + reading 3 new B1 milestone docs.
- 8 files patched, all additive GAP/PARTIAL (no OUTDATED — nothing contradicted): settings-developers.md, analytics.md, milestone.md, customers.md, integrations-subscription.md, redeeming-programs.md, widget.md, translations.md.
- Payloads: `product-kb-sync-joy-2026-08-14-payloads.json`

## Next step (after Liz reviews)
```
python3 ~/CSL/skills/kb-sync/scripts/push_kb.py <payloads.json>
```
Then run `/kb-test` per SKILL.md step 6, then advance `state/last_sync.json` for both apps.
