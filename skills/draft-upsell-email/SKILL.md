---
name: draft-upsell-email
description: Draft an expansion/upsell email (+ optional LinkedIn/Slack DM) to an EXISTING Joy Loyalty account — nudge toward a higher plan, or make the cost of staying on the current plan concrete. Three types only — warm-free, warm-advanced, roi-calculation. Use when Liz says "/draft-upsell-email", "soạn email upsell cho [account]", "email nhắc [account] nâng plan", "roi email cho [account] đang cân nhắc downgrade/rời đi". Adapted from a cold-outreach sales skill (draft-email) — cold types (cold-no-loyalty, cold-competitor, switch-sidebar) are dropped, this is account-expansion only.
argument-hint: "[account-name] [email-type: warm-free | warm-advanced | roi-calculation]"
allowed-tools: Read, Write, Edit, Glob, Grep, Bash, WebFetch
---

# Draft Upsell / Expansion Email — AM version

Draft an email to a **current** Joy Loyalty account, not a cold prospect. Always produce one email; add a short DM version only if Liz asks for one (Slack, not LinkedIn — the account already has a relationship with Avada).

## Difference from the original sales version
Dropped: `cold-no-loyalty`, `cold-competitor`, `switch-sidebar` — those pitch installing Joy for the first time, irrelevant once the account is live. Dropped: the "Run /spin first" requirement — replace SPIN research with real account data.

## Step 1: Pull account context (replaces SPIN lookup)

Don't invent numbers. Pull real data:
1. **`mcp__avada-analytic__merchant_profile`** / **`shop_profile`** on the shop domain → current Joy plan, MRR, install date, order volume if available.
2. **`mcp__avada-analytic__merchant_cs_history`** → recent tickets. A ticket asking for a gated feature ("can I set up VIP tiers?") is the strongest hook — use it verbatim.
3. **`mcp__avada-analytic__cs_review_trend`** → any recent review mentioning loyalty, useful as a soft signal (not a testimonial substitute).
4. If a loyalty program proposal was already built (`/build-loyalty-program` output), read it — it has the exact new features and the plan tier needed.

## Step 2: Pick the type

| Type | When to use |
|---|---|
| `warm-free` | Account is on Joy Free/Standard and has clearly outgrown it (ticket asking for a gated feature, or `/build-loyalty-program` proposal needs a higher plan) |
| `warm-advanced` | Account is already on a paid plan; nudging toward Advanced/Enterprise for a specific new capability |
| `roi-calculation` | Account is stalled, considering downgrading, or has gone quiet after a proposal — make the cost of staying flat concrete |

If Liz's request doesn't specify, infer from Step 1 data and confirm before drafting.

## Step 3: Testimonial (optional, use sparingly)

For an existing account, a competitor case study reads as generic. Only include one if it's from the account's exact industry vertical and adds real proof — pull from https://joy.so/case-study/ if so. Otherwise skip it; the account's own usage data (their ticket, their AOV) is stronger proof than a stranger's metric.

## Step 4: Draft rules

Follow the tone in `_identity/tone-and-voice.md` (friendly, direct, concise — teammate not vendor) and the email-format convention already in use: opens **"Hi [First Name], this is Liz from Joy Loyalty..."**, no bold formatting, no em dashes, plain text.

Differences from the sales version:
- CTA is a **call OR a direct next step in-app** ("want me to turn this on for you?") — not always "book a call." The account already has a relationship; don't force a meeting for a two-line config change.
- Reference the account's own data (their ticket, their usage), never a generic value prop.
- Keep under 120 words for standard types. `roi-calculation` has no word limit (same as source skill) but still plain text, no hyphens/em dashes.

### Standard template (warm-free / warm-advanced)

```
Hi [First Name],

[One line referencing their specific situation — the ticket they raised, or the feature gap in their current plan.]

[One sentence on what unlocking it looks like and the plan it needs.]

[Optional: one sentence testimonial, only if genuinely relevant.]

Want me to walk you through it, or should I just turn it on so you can try it?

Best,
Liz
```

### ROI calculation template (stalled/downgrade-risk account)

Same structure as the source skill's ROI email — reuse verbatim, adjusted for tone:

```
Hi [First Name],
[1-2 sentence warm opener acknowledging their situation.]

One thing worth flagging before any changes to your plan.
Looking at your numbers: [X] orders/month, $[Y] AOV, [Z]% enrollment rate on your current program.

At current usage, staying on [current plan] means [specific limitation — e.g. no VIP tiers, capped referral volume] is capping what your loyalty program can drive. A [N]% uplift from [the gated feature] would be roughly $[amount]/month based on your volume.

The plan that unlocks it is $[plan price]/month — the gap is [X] purchases worth of the upgrade cost.

Happy to send the full breakdown, or hop on a quick call if useful.

Best,
Liz
```

**ROI math (reuse source skill's formula):**
- Monthly missed value = orders/month × AOV × gross margin × enrollment rate × uplift %
- Always label inputs as conservative estimates
- Pull real orders/month and AOV from Step 1's `merchant_profile`/`shop_profile`; never fabricate — if the data isn't available, say so and ask Liz for the number instead of guessing.
- Current Joy pricing: verify against **joy.so/pricing** before quoting any number — do not reuse cached figures, they drift (see `03-deal-analyses` corrections in the Sales Handover for what happens when this isn't checked).

## Step 5: Output format

```
EMAIL

Subject: [subject line]

[email body]
```

Then 2-3 bullets: best time to send, whether this needs a follow-up if no reply in 3-5 days, and whether this should go through Crisp (if there's an open chat) instead of email.

## Step 6: Log

If this is part of the Chatty Proactive Care tracking, note it should become an Avada ticket per that project's existing convention — don't create a separate log file for this skill.
