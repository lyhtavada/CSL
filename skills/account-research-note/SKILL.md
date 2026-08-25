---
name: account-research-note
description: Research an existing Avada account (SPIN-style) for a QBR / account review / expansion conversation, and save the analysis as a pinned note on the account's deal timeline. Use when Liz says "/account-research-note", "chuẩn bị QBR cho [account]", "research account [account] để review", or gives a deal URL like https://analytics.avada.net/sale/pipeline?deal=xxxxxx and asks to save findings to it. Adapted from a cold-prospecting skill (avd-anal) — the avada-analytic MCP tools are already connected in this workspace (not Zed-restricted here), so this runs directly.
argument-hint: "[deal-url-or-account-name]"
---

# /account-research-note — account review research → pinned deal note

Given a deal/account (URL or name) in **$ARGUMENTS**, research the account's current state for a QBR or expansion conversation and save the analysis as a note pinned to the top of the deal's timeline.

## Difference from the original sales version
The source skill (`06-skills/avd-anal-SKILL.md`) framed this as cold-prospect research and required Zed (the `avada-analytics` MCP was terminal-restricted at the time it was written). In this workspace `mcp__avada-analytic__*` tools are already connected and callable directly — no Zed requirement. The research angle also flips: instead of "why should they buy," it's "what's their current health, and what's the expansion or renewal risk."

## Step 1 — Resolve the account
1. If given a deal URL (`https://analytics.avada.net/sale/pipeline?deal=xxxxxx`), call **`mcp__avada-analytic__sale_deal_get`** with the deal id (extract the `xxxxxx` after `?deal=` if the full URL errors).
2. If given only an account/brand name, use **`mcp__avada-analytic__merchant_search`** or **`shop_profile`** to resolve the shop domain first, then check if a deal exists via the pipeline tools.
3. Capture: brand/title, `shop_domain`, deal owner/AM, stage, amount, canonical `url`.

## Step 2 — Ground it in Avada's internal data (this is the core of the QBR version)

Pull as much of this as available — this is account-health research, not brand marketing research:
- **`merchant_profile`** / **`shop_profile`** → current Shopify plan, Joy plan, install date, revenue/MRR, which other Avada apps are active.
- **`merchant_cs_history`** → open/recent support tickets. Flag any unresolved or repeat issues — these are churn risk signals for a QBR.
- **`cs_review_trend`** → sentiment trend, not just a point-in-time score.
- **`app_events`** / **`app_state_summary`** if available → usage trend (is the account actually using what they pay for, or is the program dormant?). A dormant program is the single strongest churn predictor — call it out explicitly if found.
- **`sale_commission_overview`** or deal history → renewal date, any past downgrades/upgrades.

Skip external brand research (website scraping, competitor check) unless Liz specifically wants positioning context for an expansion pitch — for a QBR, internal data matters far more than public brand facts.

## Step 3 — Run the analysis

Produce the analysis using the same SPIN structure as the source `spin` skill, but reframed for an existing account:

- **Situation:** current plan, tenure, usage level, what's configured (tiers/referral/points) vs what's available but unused.
- **Problem:** open tickets, dormant features, sentiment dips, anything flagged in Step 2.
- **Implication:** churn/downgrade risk if nothing changes, or revenue left on the table if an available feature stays unused.
- **Need-Payoff:** the specific expansion or fix that addresses it — tie to a concrete plan tier or feature, not a generic pitch.

Output sections: Account Overview, Health Signal (🟢/🟡/🔴 — quick read for Liz before the QBR), Situation/Problem/Implication/Need-Payoff bullets, Recommended Talking Points for the QBR, Risks & Objections, Sources (which internal tools were queried).

## Step 4 — Compose the note

```
📌📌 PINNED RESEARCH — do not delete 📌📌
Joy Loyalty · Account Review · <YYYY-MM-DD>

<the full analysis from Step 3>

— saved by /account-research-note
```

## Step 5 — Confirm, then save
1. Show Liz a **compact preview**: deal title, health signal, section headings.
2. ⚠️ Notes can't be edited/deleted via the API (only in the Avada UI). Ask "Save this to **<deal title>**? (yes)" and wait, unless Liz has said to always save without asking.
3. On confirm, call **`mcp__avada-analytic__sale_deal_note_create`** with `deal_id` (preferred, fall back to `shop_domain`) and the composed note.
4. Report: ✔ saved, deal title, and the canonical deal `url`.

## What "pinned up top" means here
Same as the source skill — the note carries the 📌 marker and, being newest, sits at the top of the timeline. The Avada API has no true pin field. For a hard sticky pin, click **Pin** on the note inside the Avada pipeline UI — mention this once after saving.
