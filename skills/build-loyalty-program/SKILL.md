---
name: build-loyalty-program
description: Design or optimize a Joy Loyalty program for an EXISTING account (upsell/expansion angle) — new tier, added referral mechanic, higher-plan proposal. Outputs a live Google Sheet (Liz's standard template — Setup / Earning / Redemption / VIP / Referral / Launch & Bootstrap tabs) Liz can share or co-edit with the account. Use when Liz says "/build-loyalty-program", "thiết kế lại chương trình loyalty cho [account]", "đề xuất nâng cấp plan cho [account]", "optimize loyalty program cho [account]". Adapted from a sales prospecting skill (build-program) — this version assumes the account is ALREADY a Joy customer, not a cold prospect.
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

Write the real numbers from Steps 3-4 into a JSON file with flat keys matching `default_data()` in `scripts/generate_program_sheet.py` (e.g. `program_name`, `point_value`, `base_earn_rate`, `earn_purchase`, `tier1_condition`, `referrer_gets`, `public_launch_date`... — every key maps to one Value cell; leave a key out to keep that cell blank), then:

```bash
.venv-crisp/bin/python skills/build-loyalty-program/scripts/generate_program_sheet.py \
  --account "<account name>" \
  --data /tmp/<account>-program-data.json
```

This creates a **new Google Sheet** (not an edit to an existing file) titled `{Account} — Joy Loyalty Program`, using Liz's standard build template — 7 tabs, dark/red header formatting with pink "Value" cells to fill, a **Status** column on every table (dropdown: Not started / In progress / Live / Skipped, defaults to "Not started", light-blue cells) for tracking rollout progress after the proposal is approved, auto-sized columns — and prints the sheet's URL. It's owned by the authed account (`lyht@avada.io`) and shows up in that Drive automatically — no separate save step needed.

Tabs (Liz's standard template — same as the manually-built sheets she works from):
1. **Setup** — store info, program config (name, point currency/value, earn rate, expiry), app integrations, migration/import
2. **Earning** — how customers earn points (purchase, sign-up, review, social...) + birthday reward by tier
3. **Redemption** — min points to redeem, discount rewards (amount/%), free gift, free shipping
4. **VIP** — tier config (calculated by, evaluation window, multiplier) + tiers (condition, multiplier, entry reward, perks)
5. **Referral** — referrer/referee reward, condition, tier-based referral bonus
6. **Milestone** — individual achievement rewards (first order, loyal customer / order count, big spender / total spend, anniversary / account age)
7. **Launch & Bootstrap** — pre-launch checklist, bootstrap/seeding, public launch, post-launch monitoring (30/60/90 days)

Every table row across all 7 tabs also gets a **Status** column (dropdown, defaults "Not started") — use it after the proposal is approved to track which pieces are configured/live vs still pending, instead of a separate tracker doc.

If the numbers aren't final yet, run without `--data` to scaffold the blank template, then edit cells directly (or re-run with `--data` — note this creates a **new** sheet each run, it does not update an existing one).

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
- **Launch plan:** [soft launch group + date, or "unchanged"]

**Sheet:** [URL printed by the script]
```

## Step 7: Follow-up (optional)

Ask if Liz wants a follow-up email drafted — hand off to `/draft-upsell-email` with type `warm-advanced` (if proposing a plan upgrade) or reference this proposal directly.
