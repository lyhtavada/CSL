# product-kb-sync — chatty — 2026-09-08 (diff-only, review gate)

## Sources used
- **Slack** (`C07RNAY9ZC6`, shared channel), since `last_slack_ts=1787212665.307569` → `latest_ts=1788506031.307929`. 3 Chatty release posts used (2 Joy Loyalty posts in the same window skipped — not Chatty):
  - Chatty release 20/08 (ts 1787285001)
  - Chatty release 26/08 (ts 1787711735)
  - Chatty release 04/09 (ts 1788506031)
- **GitLab** (`avada/avada-helpcenter-faqs`): empty diff, `from_sha 22743df…` → `to_sha c149b0d…`, 858 commits / 1000 skipped_unrelated_files. No signal this run.

## Items extracted (~24 across the 3 posts) and classification

| # | Item | Date | Verdict | Note |
|---|------|------|---------|------|
| 1 | CSV bulk enable/disable AI for products | 20/08 | COVERED | Already in `kb/faq/ai-training-setup.md` §"Bulk Enable/Disable AI Training for Products via CSV Import (20/08)" |
| 2 | New AI answer engine (ai-vm) rollout | 20/08 | COVERED | Internal engine swap, no merchant setting; referenced via `kb/case/ai-wrong-responses.md` "AI Answer Style Changed After 20/08" |
| 3 | AI order-code question more concise, drops wrong code | 20/08 | COVERED | `kb/faq/order-tracking.md` "How the AI asks for the order number (updated 20/08)" |
| 4 | Inbox summary button stability fix | 20/08 | COVERED | `kb/faq/inbox.md` "Conversation Summarize Button — Stability fixed 20/08" |
| 5 | AI completes real cart on Messenger/WhatsApp/Instagram/email | 24-26/08 | COVERED | `kb/faq/channels.md` "AI Building Real Carts on Messenger, WhatsApp, Instagram & Email (24/08)" |
| 6 | Handover respects merchant's configured destination | 21-22/08 | COVERED | `kb/faq/human-handover.md` "Destination now correctly respected (fixed 22/08)" |
| 7 | Holidays / after-hours chats now handled correctly | 24/08 | COVERED | `kb/faq/online-hours.md` "Holiday Hours and Chats Sent Outside Working Hours (fixed 24/08)" |
| 8 | Meta channels no longer drop messages/batches | 22/08 | COVERED | `kb/case/whatsapp-messenger-issues.md` "Meta Channels Dropping Messages... (fixed 22/08)" |
| 9 | Analytics AI numbers no longer show 0 | 24/08 | COVERED | `kb/faq/analytics.md` "AI metrics showing 0 (fixed 24/08)" |
| 10 | Bulk enable/disable Confirm no longer hangs | 21/08 | COVERED | `kb/faq/ai-training-setup.md` "Confirm button reliability (fixed 21/08)" |
| 11 | Campaign edits now save all 7 fields | 25/08 | COVERED | `kb/faq/proactive-chat.md` "Campaign Edits Not Saving All Fields (fixed 25/08)" |
| 12 | Product Quiz working again incl. new AI engine stores | 25/08 | COVERED | `kb/faq/product-quiz.md` "Not showing on stores using the new AI answer engine (fixed 25/08)" |
| 13 | Plan upgrade opens correct product sync limit immediately | 21/08 | COVERED | `kb/faq/ai-training-setup.md` "After a plan upgrade (fixed 21/08)" |
| 14-21 | "Thay đổi nhỏ khác" — product card clickable/variant, AI answers FAQ instead of refusing, no fabricated links, honest out-of-stock reply, widget language fix, widget preview real FAQ, real handover test email, better table parsing | 21-25/08 | COVERED / not KB-actionable | Micro bug-fixes restoring intended behavior; KB never documented the broken state as expected, so nothing to correct. Spot-checked: `ai-training-setup.md`, `human-handover.md` (Test AI real email), `ai-agent-settings.md` — none show stale claims. |
| 22 | **Knowledge base tab** — merges FAQs + Custom knowledge into one table with Live/Draft/Off status, background FAQ sync, dedup prompt, quality banner, synced FAQs excluded from data-source limit | 02/09 | **OUTDATED** | `kb/faq/data-sources.md` and `kb/faq/knowledge-base.md` still described the old 6-tab structure with separate FAQs / Custom knowledge tabs. Patched both. |
| 23 | AI Mode → shopping assistant chatbox (search/add-to-cart/checkout in chat) | 02/09 | SKIP (not merchant-facing yet) | Slack note: shipped behind `dev_zone`, no toggle for merchants, "chưa mở cho tất cả shop." Treated like a pre-launch feature — not actionable until it has a real merchant-facing entry point. Note: this may be easy to confuse with the *already-documented* Chatbox "AI Mode vs Legacy chatbox" picker (live since 26–27/08, `kb/faq/knowledge-base.md`) — those are two different things; flag to Liz to confirm with PM before next run. |
| 24 | AI auto-fills a backup reply when a customer message got dropped mid-conversation | 02/09 | SKIP | Internal reliability fix ("no place to turn off"), no documented merchant-facing behavior to correct. |

## Files patched (payloads, not yet pushed)
1. **`kb/faq/data-sources.md`** — rewrote "Adding & Managing Data Sources" (5 tabs, not 6) and added a new section **"Knowledge Base Tab — Unified FAQs + Custom Knowledge (02/09/2026)"** covering: merge of FAQs+Custom knowledge tabs, Live/Draft/Off states, synced FAQs start on Draft, background Sync FAQs button, duplicate-handling prompt (Create new/Merge/Replace), synced FAQs excluded from data-source limit, content-quality banner (too short/long/>90 days).
2. **`kb/faq/knowledge-base.md`** — updated the "Training data" bullet under **AI agent** to describe the new Knowledge base tab instead of the old Store data / Custom data split.

Both files are `type: reference` — patched with more `##`/prose headings, no `Q:`/`A:` injected, matches existing format. English only. Real `---` frontmatter preserved.

## Not patched (deliberately left alone)
- Other files that mention "Custom knowledge" in passing (e.g. `ai-training-setup.md`, `inbox.md`, `add-questions.md` references to `Custom knowledge → Add data → Files`) still work functionally — the underlying capability (add Q&A/URL/file) didn't change, only the tab it lives under was renamed/merged. Left as-is to avoid touching ~10 files for a label change; the two most-read reference docs (product overview + data-sources) now carry the correct current tab name and link to each other.

## Payloads file
`/Users/avada/CSL/reports/analysis/product-kb-sync-chatty-2026-09-08-payloads.json` — 2 entries, `agent: "chatty-agent"`.

**Not pushed. Not reindexed. `state/last_sync.json` not touched.** Waiting on Liz's approval before running `push_kb.py`.
