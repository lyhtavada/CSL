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
- **KB dir** — Joy: `agents/joy-loyalty-agent/knowledge/`; Chatty: `agents/chatty-agent/knowledge/`.

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
- Read the app's KB files (`kb_*.md`) so standard answers match documented behavior, exact admin paths, and plan availability.

### 3. Cluster into FAQ categories

Group every distinct merchant question/problem by **feature category** (e.g. Getting Started, Points — Earning, Redemption, Widget, VIP Tiers, Referral, Notifications, Pricing, Integrations, Edge Cases). Skip pure greetings and one-off chit-chat.

For each FAQ capture: the normalized question, approximate **frequency** (how many sessions touched it), and the real fix agents applied.

### 4. Write one standard answer per FAQ

Each answer must:
- Be **correct per the KB** — verify admin paths, plan gates, and feature names against `kb_*.md`. Do not invent UI paths.
- Reflect **how agents actually resolved it** in chat (the practical fix, not just theory).
- Note limitations / "this is logged as product feedback" where the chats show an unresolved issue.
- Be customer-facing in tone — no internal tool names, credentials, or growth-hack labels.

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

## Output layout

```
reports/weekly-faqs/
├── joy/
│   └── joy_2026-06-08_2026-06-14.md
└── chatty/
    └── chatty_2026-06-08_2026-06-14.md
```

One file per mining run, dropped into the per-app folder. These are reference/analysis files — they do NOT go into the agent KB or RAG index unless the user explicitly asks to deploy them.

## Notes

- If the user wants the result indexed into the bot, copy the file into the agent's `knowledge/` dir and run `/deploy-agent {agent}`. By default, keep it under `CSL/reports/weekly-faqs/` only.
- No Anthropic API key needed — do the clustering and answer-writing inline with your own analysis. (An earlier approach called the Claude API but the key was revoked; inline is the supported path.)

## Weekly automation

A launchd job runs this skill for both apps every **Monday 16:00**, mining the
**previous full Mon→Sun week** — see `cron/README.md`. Source of truth lives in
`cron/` (versioned in CSL); `cron/install.sh` symlinks the plist into
`~/Library/LaunchAgents`. Output goes to `CSL/reports/weekly-faqs/{app}/` for later
review; it does not touch the agent KB.
