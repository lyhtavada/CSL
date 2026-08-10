# KB Diff — Chatty (mined FAQ 2026-07-27 → 2026-08-02) — DIFF-ONLY, not pushed

Source: `reports/weekly-faqs/chatty/chatty_2026-07-27_2026-08-02.md` (23 FAQs) vs live KB cached from `cs2.avada.net` (`chatty-agent`, 88 files).

## Summary

| Verdict | Count |
|---|---|
| COVERED | 18 |
| GAP | 3 |
| PARTIAL | 3 |
| OUTDATED | 0 |

No stale/contradicting facts found this week — pricing, plan limits, discount-sync rules all verified accurate against the mined FAQ.

## GAP / PARTIAL items → patched in payload

1. **AI keeps wrong brand persona after multi-market/agency handover** (recurring 2+ weeks, unresolved) → `kb/case/ai-wrong-responses.md`
2. **Auto-assignment of conversations broken / "All" tab bug** (new, confirmed dev bug) → `kb/faq/inbox.md`
3. **AI-quoted promo/shipping-threshold text goes stale** → `kb/case/ai-wrong-responses.md`
4. PARTIAL — AI fabricating product specs/variant names never in catalog → `kb/case/ai-wrong-responses.md`
5. PARTIAL — anonymous nicknames "off entirely" option → `kb/faq/inbox.md`
6. PARTIAL — member-role scope + ownership transfer → `kb/faq/team.md`

## Payload
`reports/analysis/kb-sync-chatty-2026-08-02-payloads.json` — 3 files (`kb/case/ai-wrong-responses.md`, `kb/faq/inbox.md`, `kb/faq/team.md`), full new content, gitignored.

## Push command (after Liz approves)
```
python3 ~/CSL/skills/kb-sync/scripts/push_kb.py reports/analysis/kb-sync-chatty-2026-08-02-payloads.json
```
