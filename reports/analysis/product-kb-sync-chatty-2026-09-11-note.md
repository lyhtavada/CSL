# Product KB Sync — Chatty — 2026-09-11

Review-gate run. No push/reindex performed. Payloads staged at
`reports/analysis/product-kb-sync-chatty-2026-09-11-payloads.json` (14 files, agent `chatty-agent`).

## Sources reviewed
- **Slack (source A):** 5 messages in the shared product-release channel since last sync
  (baseline ts 1787212665.307569 → latest 1788506031.307929). Of these, 3 are Chatty releases
  (20/08, 26/08, 04/09); 2 are Joy Loyalty releases (28/08, 03/09) — skipped, out of scope for
  this app run.
- **GitLab (source B):** already confirmed empty for this window by Betty before this run
  (B1 `chatty-knowledge/entities/features` — 0 commits; B2 `AppFullLayout.js` — 4 commits, all
  non-copy refactor/analytics, discarded; `messages.json` — 0 commits). Not re-fetched.
- Live KB cached via `kb-sync/scripts/prep.py chatty` (68 files) into `/tmp/kb-sync/chatty/`.

## Outcome: KB is unusually well-maintained
Nearly every Chatty release item from 20/08–04/09 was **already accurately documented** in the
live KB, including exact "fixed on <date>" framing and guidance for CS on how to tell an old bug
report from a fresh one:
- CSV bulk-edit AI status → `kb/faq/ai-training-setup.md`
- ai-vm engine migration (100% rollout) → `kb/case/ai-wrong-responses.md`
- Order-code handling improvement → `kb/faq/order-tracking.md`
- AI cart completion on Messenger/WhatsApp/Instagram/email → `kb/faq/channels.md`
- Handoff respecting merchant's chosen method → `kb/faq/human-handover.md`
- Holiday/after-hours AI handling → `kb/faq/online-hours.md`
- Meta channel message-loss fix → `kb/case/whatsapp-messenger-issues.md`
- AI analytics-zero fix → `kb/faq/analytics.md`
- Product bulk-toggle Confirm-hang fix, plan-upgrade product-limit fix → `kb/faq/ai-training-setup.md`
- Product Quiz fix → `kb/faq/product-quiz.md`
- Real handoff test email → `kb/faq/human-handover.md`
- Inbox summarize-conversation stability fix → `kb/faq/inbox.md`

Skipped as not merchant-facing / not yet live: Campaign field-save fix (admin-only editor bug,
no case file exists for it); AI Mode shopping assistant (still `dev_zone`-gated, not public).

## OUTDATED (1 finding, wide blast radius — 13 files)
**Knowledge Base tab merge (04/09):** the AI training data UI merged the old **FAQs** and
**Custom knowledge** tabs into one **Knowledge base** tab (statuses: Set live / Move to draft /
Turn off; auto-synced content lands in Draft; duplicate-handling; synced FAQs don't count toward
the data-source limit; freshness banners at 90+ days). The live KB still described the **old
6-tab structure** (`Products, Collections, Discounts, Markets, FAQs, Custom knowledge`) and used
`Training data → FAQs` / `Training data → Custom knowledge` as navigation paths across many files —
per CLAUDE.md's config-change rule, updated **every** file that referenced the old tab names, not
just the primary doc:

- `kb/faq/data-sources.md` — rewritten: tab list (6→5 tabs) + new "Knowledge Base Tab (since 02/09)"
  section with the full behavior (statuses, draft-by-default sync, duplicate handling, limit
  exemption, freshness banners)
- `kb/faq/knowledge-base.md` (master overview) — Training data section updated to match
- `kb/faq/ai-training-setup.md` — 10 nav-path mentions renamed (setup steps, phone-number
  redirect, contact-URL fix, character-limit note, metafield workarounds, file upload path)
- `kb/case/ai-wrong-responses.md` — 7 nav-path mentions renamed (hallucination workaround,
  negative-fact Q&A, source-tab mapping table, external-URL check, link-format check, FAQ-mixup fix)
- `kb/faq/add-questions.md`, `kb/faq/faqs-page.md` (×2), `kb/faq/suggested-qna.md`,
  `kb/faq/test-and-optimize-ai.md` (×2), `kb/faq/inbox.md`, `kb/faq/online-hours.md` (×2, incl.
  heading), `kb/faq/faqs-block.md`, `kb/faq/klaviyo.md`, `flows/done_for_you.md` — 1 nav-path
  mention each renamed

**Caveat carried from the Slack note itself:** the release author flagged rollout scope as
unconfirmed ("chưa rõ đã mở cho toàn bộ merchant hay còn giới hạn nhóm thử... Gói áp dụng chưa
rõ, tạm hiểu là mọi gói"). This patch assumes it's live for all merchants/plans, matching the
master release-note framing (not `dev_zone`-gated like AI Mode). **Worth confirming with anh Tùng
before push** if Liz wants extra certainty — if it's still partial-rollout, the nav path becomes
wrong for stores not yet migrated.

## PARTIAL (1 finding)
**Stuck-message auto-recovery (02/09):** a new background safety net that auto-answers messages
dropped mid-pipeline — distinct from the 20/08 ai-vm engine fix (which already covered the older
"stuck AI" failure mode). Added a short note to `flows/ai_not_responding.md` (system-action flow,
matching `flow_vs_case_patch_rule`) so CS checks timing (pre/post 02/09) before treating a
"customer got no answer" report as active, without changing the collect→consult_ts→ticket steps.

## Next step
Liz reviews the diff, then runs:
`python3 ~/CSL/skills/kb-sync/scripts/push_kb.py reports/analysis/product-kb-sync-chatty-2026-09-11-payloads.json`

State (`state/last_sync.json`) was **not** advanced — Betty will handle that separately per the
skill's review-gate instructions.
