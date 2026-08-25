---
name: build-loyalty-program
description: Design or optimize a Joy Loyalty program for an EXISTING account (upsell/expansion angle) — new tier, added referral mechanic, higher-plan proposal. Outputs a live Google Sheet (Points / VIP / Referral / Milestones tabs) Liz can share or co-edit with the account. Use when Liz says "/build-loyalty-program", "thiết kế lại chương trình loyalty cho [account]", "đề xuất nâng cấp plan cho [account]", "optimize loyalty program cho [account]". Adapted from a sales prospecting skill (build-program) — this version assumes the account is ALREADY a Joy customer, not a cold prospect.
argument-hint: "[account-name-or-shop-domain]"
allowed-tools: "WebFetch, WebSearch, Bash, Read, Write, Edit, Glob, Grep, TodoWrite, AskUserQuestion"
---

# Build / Optimize Loyalty Program — AM version

Design an upgraded or new Joy Loyalty program for an account that is **already installed** (this is expansion/upsell work, not a cold pitch). Output: a multi-tab Excel proposal Liz can walk the merchant through.

## Difference from the original sales version
The source skill (`06-skills/build-program-SKILL.md` in the Sales Handover) assumed a fresh prospect and pulled brand facts from a SPIN analysis or a tl;dv demo call. Here the account is a live customer — pull real usage data from Avada's own systems first. Skip anything that reads like "convince them to install."

## Step 1: Gather account context

Ask which account (name or shop domain) if not given. Then pull real data, in this order:

1. **`mcp__avada-analytic__merchant_profile`** or **`shop_profile`** on the shop domain → current Shopify plan, current Joy plan, install date, MRR.
2. **`mcp__avada-analytic__merchant_cs_history`** and **`cs_review_trend`** → support tickets, sentiment, anything the merchant has already asked for (a feature request is a strong signal for what to design toward).
3. If a Crisp chat or Avada ticket mentions specific pain points (e.g. "can't set up VIP tiers", "want a referral program"), fold those in directly — don't guess.
4. Brand website (product lineup, AOV signal, industry vertical) — quick WebFetch/WebSearch pass, same as the original skill's Step 1.

If real usage data isn't available (new account, no history yet), fall back to the original skill's brand-URL-only research pass.

## Step 2: Determine program type and what's changing

Classify the brand (subscription vs standard VIP — same logic as the source skill) **and** state explicitly what's new vs what already exists:
- Is this a **net-new addition** (e.g. account has points only, proposing to add VIP tiers or referral)?
- Or a **full redesign** (thresholds/rates aren't working, review data shows low redemption)?
- Or a **plan upgrade unlock** (feature they want requires the next plan up)?

This framing matters for Step 5's summary — Liz needs to know if this is "add-on" or "replace."

## Step 3: Pull the current Joy feature catalog

Do NOT use a local reference file — the live KB is the source of truth and drifts constantly. Fetch what's needed:

```bash
.venv-crisp/bin/python skills/kb-sync/scripts/kb_api.py joy <path>
```
or list available files first:
```bash
.venv-crisp/bin/python -c "from skills.kb_sync.scripts.kb_api import *" # or use fetch_kb.py pattern from qa-weekly
```
In practice: use `skills/qa-weekly/scripts/fetch_kb.py joy <path>` to pull feature docs (agent id `joy-loyalty-agent`). Pull whichever feature pages are relevant to what you're designing (VIP tiers, referral, points, paid membership) rather than the whole KB.

## Step 4: Design the program

Same math as the original skill — reuse as-is, it's product-agnostic:

**Point valuation:** `earning_rate = target_reward_points / (AOV × purchases_to_reward)`. Target: first meaningful reward reachable in 2–3 purchases.

**Tier thresholds:** Tier 2 reachable at 3–5 purchases, Tier 3 at 8–12, Tier 4 (VIP/advocate) at 15–20+. Adjust to the account's actual AOV/order frequency from Step 1.

**Referral value:** Referee discount 10–20% off or $10–15 off (must be compelling to convert). Referrer reward ≈ 1 purchase worth of points. Min purchase for referee at or slightly above AOV.

If this is an **add-on to an existing program**, don't redesign what's already working — only spec the new piece, and note how it interacts with existing tiers/points so nothing conflicts.

## Step 5: Generate the Google Sheet

Write the real numbers from Steps 3-4 into a JSON file matching the schema in `scripts/generate_program_sheet.py` (`default_data()` shows the shape — point_valuation, earning_rules, redemption_rules, paid_membership, tiers, demotion_policy, referral, milestones, quest), then:

```bash
.venv-crisp/bin/python skills/build-loyalty-program/scripts/generate_program_sheet.py \
  --account "<account name>" \
  --data /tmp/<account>-program-data.json
```

This creates a **new Google Sheet** (not an edit to an existing file) titled `{Account} — Joy Loyalty Program Proposal`, with 4 tabs and header formatting (Joy purple `#6C5CE7`, bold white text, auto-sized columns), and prints the sheet's URL. It's owned by the authed account (`lyht@avada.io`) and shows up in that Drive automatically — no separate save step needed.

Tabs (same structure as the sales version, now live-editable):
1. **Points Program** — Earning Rules + Redemption Rules tables, valuation summary box at top
2. **VIP Membership** — Tier Name, Threshold, Earning Multiplier, Entry Reward, Perks
3. **Referral Program** — Referrer Reward, Referee Reward, Min Purchase, Sharing Channels, Anti-Cheat, Message Template
4. **Milestones & Quest** — Individual Milestones + Quest Journey (branded step sequence)

If the numbers aren't final yet, run without `--data` to scaffold the sheet with placeholders, then edit cells directly (or re-run with `--data` — note this creates a **new** sheet each run, it does not update an existing one).

To give the account or a teammate edit access directly, pass `--share <email>` (uses the `drive.file` scope — only works on sheets this script created).

## Step 6: Present summary

```
## {Account} Loyalty Program — {Add-on / Redesign / Upgrade Unlock}

**Current plan:** [Joy plan] | **Recommended plan:** [plan needed for the new features]
**Why now:** [the CS ticket / review signal / usage gap that triggered this]

### What's changing
- **Points:** [unchanged / new rate]
- **Tiers:** [new tier names + thresholds, or "unchanged"]
- **Referral:** [new mechanic, or "unchanged"]
- **Quest:** [if added]

**Sheet:** [URL printed by the script]
```

## Step 7: Follow-up (optional)

Ask if Liz wants a follow-up email drafted — hand off to `/draft-upsell-email` with type `warm-advanced` (if proposing a plan upgrade) or reference this proposal directly.
