---
name: cs-daily
description: Daily CS performance report — how CS Team G2 performed on Crisp chats in the last 24h (9:00 yesterday → 9:00 today VN). Covers checkin/checkout, top issues, paid follow-ups, review asks, and per-CS quality. Posts to Liz via Slack DM.
---

# /cs-daily — Daily CS Performance Report

Generate the daily CS report for **Team G2** over the last 24h window (9:00 hôm qua → 9:00 hôm nay, giờ VN) and post it to Liz via Slack DM.

## Data sources
- **Crisp transcripts** → BigQuery `avada-crm.avada_cs.crisp_chats` (message-level). Joy = segment `app_joy`; Chatty = `app_chatty` OR `app_faqs`.
- **Shift / checkin / checkout** → Admin API `/shifts` + `/shifts/:id/checks` (`$AVD_TOKEN`, base `$AVD_API_BASE`). Filter `groupLabel` contains `G2`. Match CS by **email** (display names like `HangHM1` are the same person).
- **Plan tier** → Admin API `/shops/search?searchString=<domain>&searchAll=true` → `plan` field (only queried for follow-up shops).
- **Roster** → `_identity/team-g2.md` (mirrored in `lib/common.py`: `EMAIL2NICK`, `NICK2NAME`).
- **Output** → Slack DM to Liz (`U02GT4PC6RH`) via `SLACK_BOT_TOKEN_AVADA`.

All scripts live in `skills/cs-daily/lib/` and read `~/CSL/.env`. Working dir for intermediate files: `/tmp/csdaily/`.

## Pipeline (run from `~/CSL/skills/cs-daily/lib`)

### Step 1 — Fetch transcripts
```bash
cd ~/CSL/skills/cs-daily/lib && python3 fetch.py
```
(Optional: `python3 fetch.py 2026-06-03` to run for a specific end-date.)
Writes `/tmp/csdaily/cls_batch_0..6.json`, `sessions_raw.json`, `window.json`. Note `n_batch` (=7).

### Step 2 — Classify issues + quality (Workflow, fan-out per batch)
Run a Workflow with one agent per `cls_batch_{i}.json`. Each agent reads its batch and returns, for every session, a JSON object with:
`id, app, domain, cust, issue, topic (VN one-liner), cs_nick, quality (excellent|good|needs_improve|unanswered), quality_note (short EN), needs_followup (bool)`.

- Map agent **email → nickname** via the roster (see `lib/common.py` `EMAIL2NICK`). Agents not in the map → use their email prefix.
- `issue` categories: "Loyalty Program Setup", "AI Bot Training", "Live Chat Setup", "Billing/Plan", "Integration", "Bug", "Feature Request", "General".
- `quality_note` style mirror: "handled well" / "gave thorough response but could add more resources" / "provided detailed explanation with proper documentation/examples" / "Merchant question left unanswered".

Collect all sessions and **write the merged array to `/tmp/csdaily/classified.json`**.

### Step 3 — Enrich (plan tier + filter + review batches)
```bash
cd ~/CSL/skills/cs-daily/lib && python3 enrich.py
```
Filters spam/bot-only, queries plan for follow-up shops, writes `enriched.json` + `rv_batch_0..5.json`. Note `n_rv_batch` (=6).

### Step 4 — Detect review asks (Workflow, fan-out per batch)
Run a Workflow with one agent per `rv_batch_{i}.json`. Each agent reads the transcript and returns, per session:
`id, asked (bool — did the CS explicitly ask for a review / send a review link IN this transcript), outcome (got|declined|no_response|na), note (short)`.
- `got` = merchant clearly agreed / confirmed they left or will leave a review.
- `no_response` = CS asked but merchant gave no clear positive reply / chat ended.
- `declined` = merchant declined or deflected. `na` = CS did not ask.
- Be strict: generic "let me know if you need anything" is NOT a review ask.

Collect all and **write merged array to `/tmp/csdaily/reviews.json`**.

### Step 5 — Render + post Slack
```bash
cd ~/CSL/skills/cs-daily/lib && python3 render.py            # render + post DM to Liz
cd ~/CSL/skills/cs-daily/lib && python3 render.py --print    # preview without posting
```
Renders `report.txt` and posts to Liz's Slack DM (auto-chunked for Slack length limits).

## Report sections (in order)
1. **TỔNG QUAN** — total + Joy/Chatty split
2. **⏰ CHECKIN/CHECKOUT** — late (>5 min) / miss checkin / miss checkout
3. **TOP ISSUES** — Joy + Chatty, top 3 issue categories each (with case count, no shop detail)
4. **⚠️ PAID PLANS — TOP 3** — highest-value paid shops needing follow-up + count of the rest
5. **⭐ XIN REVIEW** — stats (asks/got/no-response/declined) + CS ranking (most asks) + no-response list cần follow-up
6. **👥 CS PERFORMANCE** — count cases handled well + "Cần cải thiện" list
7. **💡 INSIGHT** — 2 dòng: setup+bug counts, paid follow-up count

## Notes
- Default to running the full pipeline end-to-end. Show Liz the rendered report; only post to Slack after the render step succeeds.
- If Liz asks for a specific day, pass the date to `fetch.py` (it's the END day at 09:00).
- The 2 Workflow steps each take ~30–75s. Prefer running them in the background and continuing when notified.
