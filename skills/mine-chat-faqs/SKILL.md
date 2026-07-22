---
name: mine-chat-faqs
description: Mine FAQ from real Crisp chats for a Joy or Chatty app. Use when the user asks to "mine FAQ", "tổng hợp FAQ từ chat", "build FAQ from chats", or wants to analyze recent merchant conversations and produce a standard-answer FAQ file. Fetches chats from BigQuery (avada_cs.crisp_chats) by segment + date window, clusters questions into feature categories, compares against the agent KB, and writes one standard answer per FAQ. Output goes to /Users/avada/CSL/reports/weekly-faqs/{app}/{app}_{start}_{end}.md
version: 1.0.0
---

# Mine Chat FAQs

Turn real Crisp support conversations into a clean FAQ file: cluster what merchants actually asked, cross-check the existing KB and how agents answered, then write one correct standard answer per question.

## When to use

User says things like: "mine FAQ cho Joy", "tổng hợp FAQ từ chat 7 ngày", "build FAQ from Chatty chats", "phân tích chat rồi viết FAQ".

## Inputs to confirm (only if ambiguous)

- **App / segment** — default to what the user names:
  - **Joy** → segment `app_joy`
  - **Chatty** → segments `app_chatty,app_faqs` (Chatty spans BOTH; always pass both, comma-separated — the script ORs them and dedups by session)
- **Window** — either a rolling look-back (`--days`, default 7) or an exact calendar window (`--start`/`--end`, inclusive `YYYY-MM-DD`). The weekly cron uses `--start`/`--end` for the previous full Mon→Sun week.
- **KB source** — the **live CS v2 KB** on `cs2.avada.net` (agent `joy-loyalty-agent` for Joy, `chatty-agent` for Chatty), NOT the old claw repo. Pull it the same way `/kb-sync` does: `skills/kb-sync/scripts/prep.py <app>` caches every KB file to `/tmp/kb-sync/<app>/`, then read from there. Cross-checking against the old `claw-weebhook-crisp-chat` repo is wrong — that KB is stale.

Bias toward action — don't over-ask. If the user already named the app and window, run.

## Data source

**BigQuery table:** `avada-crm.avada_cs.crisp_chats`
**Credentials:** `/Users/avada/CSL/.env` (`BQ_SA_CLIENT_EMAIL`, `BQ_SA_PRIVATE_KEY`, `BQ_SA_PRIVATE_KEY_ID`).

> The MCP BigQuery tool is app-scoped and CANNOT read `avada_cs.crisp_chats`. You MUST use the bundled Python script, which authenticates with the churn-prediction service account using the full `bigquery` scope.

Key columns: `session_id`, `segments`, `timestamp`, `type`, `fromType` (`user` = customer, else agent), `content`, `shopifyDomain`, `conversationState`.

## Steps

### 1. Fetch conversations

```bash
cd /Users/avada/CSL/skills/mine-chat-faqs
# Rolling 7-day window:
python3 scripts/fetch_chats.py --segment app_joy --days 7 --output /tmp/joy_convs.json
# Or an exact calendar week (what the weekly cron uses):
python3 scripts/fetch_chats.py --segment app_joy --start 2026-06-08 --end 2026-06-14 --output /tmp/joy_convs.json
# Chatty — pass BOTH segments:
python3 scripts/fetch_chats.py --segment app_chatty,app_faqs --days 7 --output /tmp/chatty_convs.json
```

Output is a JSON list of `{session_id, messages:[{role: Customer|Agent, text}]}`, newest first. The script prints session/message counts — note the session count for the file header.

Requires `python-dotenv` + `google-cloud-bigquery` (already installed in this environment).

### 2. Read the conversations and the KB

- Read the JSON. For large output, dump dialogs to a temp `.txt` (Customer/Agent interleaved) and read in passes.
- Cache the app's **live CS v2 KB** (`cd skills/kb-sync/scripts && python3 prep.py <app>` → files land in `/tmp/kb-sync/<app>/`) and read those so standard answers match documented behavior, exact admin paths, and plan availability. Do not read the old claw repo.

### 3. Cluster into FAQ categories

Group every distinct merchant question/problem by **feature category** (e.g. Getting Started, Points — Earning, Redemption, Widget, VIP Tiers, Referral, Notifications, Pricing, Integrations, Edge Cases). Skip pure greetings and one-off chit-chat.

For each FAQ capture: the normalized question, approximate **frequency** (how many sessions touched it), and the real fix agents applied.

### 4. Write one standard answer per FAQ

Each answer must:
- Be **correct per the KB** — verify admin paths, plan gates, and feature names against the KB. Do not invent UI paths.
- Reflect **how agents actually resolved it** in chat (the practical fix, not just theory).
- Note limitations / "this is logged as product feedback" where the chats show an unresolved issue.
- Be customer-facing in tone — no internal tool names, credentials, or growth-hack labels.

> ⚠️ **Never invent plan limits or pricing.** AI-conversation caps, product-sync limits, seat counts, history length, and prices are **facts**, not things to infer from chats. A merchant's chat is NOT a reliable source for the exact number. The source of truth is **chatty.net/pricing** (Chatty) — fetch it if you state any number, and copy the figure exactly. If you can't verify a limit, describe the behavior qualitatively ("limited by plan; check Subscription → View details") rather than writing a number. Past runs fabricated wrong caps (e.g. Free "50 lifetime", Basic "50/mo") that contradicted the live pricing page — do not repeat this.

### 4b. Dedup against previous runs

Before writing, check the app's folder (`reports/weekly-faqs/{app}/`) for earlier dated files. For each FAQ in the new run, decide:

- **Recurring** — same question already covered in a prior run. Keep it, but mark it `🔁 recurring` next to the frequency. A high recurring frequency = the KB/bot still isn't resolving it → worth flagging.
- **New** — not seen in any prior file. Mark it `🆕 new`.

This keeps each dated file self-contained (full FAQ list for that window) while making it obvious at a glance what's newly surfaced vs. chronic. Add a short **"What changed since last run"** summary block under the header listing the 🆕 new questions and any 🔁 recurring ones whose frequency rose sharply.

If there are no prior runs, skip the markers and the summary.

### 5. Write the output file

Path: `/Users/avada/CSL/reports/weekly-faqs/{app}/{app}_{YYYY-MM-DD}_{YYYY-MM-DD}.md`
(`{app}` = `joy` or `chatty`; dates = window start/end.)

Header block:
```markdown
# {App} — FAQ from Real Chats ({Mon DD} – {Mon DD}, YYYY)

> Compiled from {N} Crisp chat sessions of the `{segment}` segment over {days} days.
> Each FAQ contains: the common question, frequency, and a standard answer based on the KB + real agent responses.
```
Then numbered sections by category, each FAQ as `### Q{n}: ...` with `**Frequency:** ~N sessions` and `**Standard answer:**`.

Write in **English** unless the user asks otherwise.

### 6. Diff the fresh mined file against the live KB

Immediately continue into the **`/kb-sync` diff flow** (`skills/kb-sync/SKILL.md`,
steps 1–2) for the file just written — don't stop at step 5:

```
cd ~/CSL/skills/kb-sync/scripts
python3 prep.py <app>            # caches live KB, auto-picks the file just written
```

Classify every mined FAQ as **COVERED / OUTDATED / GAP / PARTIAL** against the
cached KB (verify each discrepancy against the real cached file — never assume).
For a large batch, fan out with the Agent tool per `kb-sync/references/diff-prompt.md`.

Save the diff summary as its own file:
`reports/weekly-faqs/{app}/{app}_{start}_{end}-kb-diff.md`
(table: mined Q# | topic | KB file | verdict, + OUTDATED detail + GAP/PARTIAL detail
+ a priority list by frequency — same shape as an interactive kb-sync diff).

### 7. Draft the patch (kb-sync steps 3)

For every OUTDATED/GAP/PARTIAL item, build the full new file content (start from
the cached KB file, edit/insert at a real anchor) per `kb-sync/SKILL.md` step 3.
Skip anything that has no verifiable official answer yet (e.g. an open legal/security
request with nothing published) — flag it in the diff report instead of inventing
content for it.

Write the payloads file at the path `/kb-sync` already expects, so its push script
needs no changes:
`reports/analysis/kb-sync-{app}-{YYYY-MM-DD}-payloads.json`

**Review gate — do not push.** Pushing to v2 (`push_kb.py`) and reindexing stay a
separate, explicit step that only happens after Liz reviews the diff + payloads
and says go — same as `/kb-sync` step 4–5. This holds whether the run is
interactive or the weekly cron.

## Output layout

```
reports/weekly-faqs/
├── joy/
│   ├── joy_2026-06-08_2026-06-14.md
│   └── joy_2026-06-08_2026-06-14-kb-diff.md
└── chatty/
    ├── chatty_2026-06-08_2026-06-14.md
    └── chatty_2026-06-08_2026-06-14-kb-diff.md

reports/analysis/
└── kb-sync-{app}-{date}-payloads.json     # built in step 7, consumed by push_kb.py
```

One mined-FAQ file + one diff report per run per app, plus a shared payloads file
per app if there's anything to patch. The mined-FAQ file and diff report are
reference/analysis files — nothing touches the agent KB or RAG index until the
payloads file is explicitly pushed (`kb-sync/scripts/push_kb.py`) after review.

## Notes

- If the user wants the mined-FAQ content indexed into the bot some other way (not
  via kb-sync), copy the file into the agent's `knowledge/` dir and run
  `/deploy-agent {agent}`. By default, everything stays under `CSL/reports/` until
  pushed through the kb-sync payloads flow above.
- `/kb-sync` remains a standalone skill — use it directly for an ad-hoc re-diff
  (e.g. the KB changed mid-week) without re-running the mining step.
- No Anthropic API key needed — do the clustering and answer-writing inline with your own analysis. (An earlier approach called the Claude API but the key was revoked; inline is the supported path.)

## Weekly automation

A launchd job runs this skill for both apps every **Tuesday 11:00**, mining the
**previous full Mon→Sun week**, then chaining into steps 6–7 (diff + draft patch)
and DMing Liz a review digest — see `cron/README.md`. Source of truth lives in
`cron/` (versioned in CSL); `cron/install.sh` symlinks the plist into
`~/Library/LaunchAgents`. The cron never pushes to v2 or reindexes — that stays a
manual step after Liz reviews (`kb-sync/scripts/push_kb.py`).

Note: the separate `/kb-sync` cron (Monday 16:30, diff-only) still runs on its own
original schedule and is unaffected by this change — it re-diffs whatever mined
file is newest at that time.
