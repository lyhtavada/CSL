# Product KB Sync — DIFF-ONLY review — 2026-09-18

Review-gate run only. No push, no reindex, no state update — state advances after Liz
reviews (see notes below on why Chatty's state especially needs a careful catch-up).

## Data-integrity note (read first)

`fetch_gitlab.py`'s `compare` call truncates GitLab's diff at 1000 files. Chatty's last
sync baseline was **1656 commits** old (last synced 2026-08-21), so the naive compare
result was empty/misleading (`diffs_truncated: true`). Re-ran via per-path `commits?path=`
queries instead (bounded, no truncation) to get a trustworthy diff. Joy's baseline was
only 33 commits old — compare was not truncated, trustworthy as-is. Flagging this because
`fetch_gitlab.py` itself doesn't check `diffs_truncated` — worth a follow-up fix so future
runs after another long gap don't silently miss signal again.

## Chatty

### Slack (3 release posts: 20/08, 26/08, 04/09) + GitLab (B1: 0 changes; B2: 1 real feature commit + 4 non-copy AppFullLayout.js refactors, discarded)

| Item | Verdict | Reason |
|---|---|---|
| CSV bulk enable/disable AI training (20/08) + Confirm-hang fix (21/08) | COVERED | Already documented in `kb/faq/ai-training-setup.md` § *Bulk Enable/Disable AI Training for Products via CSV Import* |
| AI completes cart on Messenger/WhatsApp/Instagram/email (24/08) | COVERED | Already documented in `kb/faq/channels.md` § *AI Building Real Carts on Messenger, WhatsApp, Instagram & Email* |
| Handoff respects merchant-configured destination (22/08 fix) | COVERED | Already documented in `kb/faq/human-handover.md` |
| **Pricing display rules — hide price / "Call for Price" label (shipped 11/09)** | **GAP** | Not documented anywhere. Verified via GitLab: fully wired into `routes/defaultAppRoutes.js` + `pwaRoutes.js`, no dev_zone gate — production feature, not experimental. Payload ready. |
| Knowledge base tab merge — FAQs + Custom knowledge → one "Knowledge base" tab w/ Draft/Live/Off (04/09) | **PARTIAL — held back** | `kb/faq/data-sources.md` still describes the old 6-tab structure and would need a real rewrite (tabs list, FAQs/Custom knowledge → Knowledge base, Draft/Live/Off states, Store pages section). **Not patched this run** — the release note itself says rollout scope is unconfirmed ("chưa rõ đã mở cho toàn bộ merchant hay còn giới hạn nhóm thử... cần xác nhận trước khi báo khách rộng"). Renaming "Custom knowledge"/"FAQs" would also touch several other files (`ai-training-setup.md` references "Custom knowledge" ~8 times). Recommend confirming rollout with Tùng/Đạt before patching broadly. |
| AI Mode chatbox → shopping assistant (02/09) | Skip | Explicitly dev_zone-gated, "chưa có chỗ bật cho merchant" — no toggle exists yet, not ready for KB. |
| All other bug fixes in the 3 releases (message-drop protection, Meta message loss, analytics zeros, campaign field save, Product Quiz restore, holiday hours, Inbox summary stability, misc small fixes) | Skip | Bug fixes restoring already-documented behavior, or too internal/non-configurable to need a KB entry. |
| Joy Slack items in the same channel (SMS subscribe reward, Milestone claim reminder, Referral widget stats, Widget v4 on-brand, REST API/MCP for Pro+Advanced) | N/A this run | `ts` ≤ Joy's `last_slack_ts` — already surfaced/handled in a prior run, out of scope here. |

**Payload:** `reports/analysis/product-kb-sync-chatty-2026-09-18-payloads.json` — 1 entry,
patches `kb/faq/ai-agent-settings.md` (appends new § *Pricing Display Rules*, adds tags).

## Joy

GitLab only (Slack: 0 new messages — Joy's `last_slack_ts` already at the channel's latest).

| Item | Verdict | Reason |
|---|---|---|
| Klaviyo integration page — new "partnerBanner" copy (Moonpie agency promo) | Skip | Promotional partner banner, not a merchant capability or support-relevant behavior change. No KB action. |

**Payload:** none — nothing to patch for Joy this run.

## Next steps (manual, after Liz reviews)

```
python3 ~/CSL/skills/kb-sync/scripts/push_kb.py reports/analysis/product-kb-sync-chatty-2026-09-18-payloads.json
```
Then run `/kb-test` against a few "call for price" / "hide price" phrasings to confirm
retrieval picks up the new section, then update `state/last_sync.json` for chatty
(`last_slack_ts` → latest fetched ts, `last_gitlab_commit` → to_sha) and for joy.
