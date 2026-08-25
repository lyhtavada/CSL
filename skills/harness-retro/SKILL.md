---
name: harness-retro
description: Weekly self-improvement loop for Liz's Claude Code / Betty setup. Reads recent session transcripts, finds where things got stuck (tool errors, permission denials, retries, corrections, missing skills), proposes 1-3 concrete fixes (new skill / CLAUDE.md edit / allowlist permission). Use when Liz says "/harness-retro", "harness retro", "weekly retro", "sao Betty hay bị vướng". Role-agnostic — kept close to the original (harness-retro), only paths and identity changed.
---

# harness-retro — making Betty's setup smarter every week

Re-reads recent CSL sessions, finds friction (slow, repetitive, or failed interactions), and proposes specific upgrades to **this workspace's setup** — skills, `CLAUDE.md`, permissions, connected tools. Not about any single task's output; about the harness Liz runs her day through.

## Two-phase design (script first, AI second)

Same design as the source skill — a deterministic script filters the noisy raw transcripts before Claude reads anything, keeping the analysis cheap and accurate.

### Phase 1 — Deterministic preprocess (bun script)

```bash
bun skills/harness-retro/scripts/parse-transcripts.ts --days 7
```

Reads `~/.claude/projects/-Users-avada-CSL/*.jsonl` (this workspace's own session transcripts). Streams line-by-line, strips tool-output dumps/base64/system-reminders, **redacts anything that looks like a token/API key/Bearer/JWT**, and tags friction signals by rule (not AI):
- `tool_error`, `permission_denied`, `user_rejected_tool`
- `retry_loop` (same target failed 3+ times in a session)
- `user_correction` (pushback right after an action — "no", "sai rồi", "không phải vậy", "làm lại")
- `missing_capability` (Betty said she had no skill/tool/access for something)
- `context_compact`, high-churn sessions (120+ turns on one topic)

Writes a compact digest to `skills/harness-retro/.digest.json`.

### Phase 2 — Retro analysis (Claude reads the digest → report)

Claude reads only `.digest.json`, never raw JSONL.

## Steps

1. Run the parser (`--days 7`; retry with `--days 14` if too little signal, and say which window was used).
2. Read `skills/harness-retro/.digest.json` — look at `signalTally` and `sessions[].signals`.
3. Group repeated signals into friction points, rank by frequency × estimated time lost.
4. Write the report to `reports/harness-retro/YYYY-WW.md` (ISO year-week).
5. Summarize back to Liz in-chat + the report path (no external notification).

## Report template

```markdown
# Harness Retro — {YYYY-WW}

> Window: {from} → {to} ({N} days) · Sessions analyzed: {X} · Sessions with friction: {Y} · Total tool errors: {Z}

## Top friction points

### 1. {Friction name} — ~{turns} turns / ~{minutes} min lost
- **Signal:** {signal type} ×{count}, across {N} sessions
- **Quote:** "{one real quote from the digest}"
- **Root cause:** {1-2 sentences}

## Proposals (1-3 actionable fixes)

### Proposal 1 — {NEW SKILL | CLAUDE.md EDIT | ALLOWLIST PERMISSION}: {name}
- **Removes which friction:** {tie to a friction point above}
- **What it is:** {concrete, buildable spec — exact CLAUDE.md text, or exact allowlist line, or a full skill spec}
- **Estimated impact:** {how often, turns saved}

## What got smarter this week
{One paragraph: what the setup learned, which fix to do first, why it compounds.}
```

## Rules

- Every friction point and proposal ties to real data in the digest — never invent.
- Proposals must be immediately actionable (paste-ready CLAUDE.md text, copy-paste `.claude/settings.json` line, or a complete skill spec).
- Max 3 proposals — prioritize what compounds fastest.
- No emoji in the report.

## Weekly schedule (optional)

Use `/schedule` or a launchd cron the same way other CSL skills do (see `bot-corrections`, `qa-weekly` for the pattern) — not set up by default; ask Liz before adding a cron job.

## Dependencies

- `bun` (`/Users/avada/.bun/bin/bun`) — already available in this environment.
- `~/.claude/projects/-Users-avada-CSL/*.jsonl` — this workspace's own transcripts, automatic.
- Output dir `reports/harness-retro/` (auto-created).
