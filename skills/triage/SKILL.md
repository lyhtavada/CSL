---
name: triage
description: Use this skill when the user shares a merchant case, conversation, or support ticket and asks "how do I handle this", "what should I do", "should I refund", "should I escalate", "is this a bug or user error", "who do I escalate to", or similar triage/decision questions. Also use when an agent asks Liz for guidance on a specific case.
version: 1.0.0
---

# Triage Skill

Analyse a support case and provide a clear handling recommendation.

## Context

- Liz is CS Leader at Avada for two Shopify apps: **Chatty** (live chat, AI, FAQ) and **Joy Loyalty** (loyalty & rewards)
- Triage is done from Liz's perspective: deciding what the agent should do, or what Liz herself should do as escalation point
- Output should be a quick, actionable decision — not a long analysis

## Triage Output Format

Always structure output as:

**Case Type:** [classification]
**Priority:** [P0 / P1 / P2 / P3]
**Recommended Action:** [what to do next, 1-2 sentences]
**Escalate?** [Yes / No — and to whom if yes]
**Draft Reply:** [optional — short starter if helpful]
**Watch Out For:** [optional — any risk flag]

Keep it brief. Liz reads fast.

## Case Classification

| Type | Examples |
|------|----------|
| How-to | "How do I add a reward?", "Where is the widget?" |
| Bug / Issue | "Points not credited", "Widget not showing", "App blank screen" |
| Billing | "I was charged", "How do I upgrade/downgrade?" |
| Refund Request | "I want my money back", "Cancel subscription" |
| Complaint | "Your app is terrible", angry tone, threatening review |
| Feature Request | "Can you add X feature?" |
| Pre-sales | "Does your app do X?", "How much does it cost?" |
| Sensitive | Harassment, personal info requests, threats |
| Integration | "How to connect Klaviyo?", "Does it work with [app]?" |
| Discount Request | "Can I get a better price?" |

## Priority Matrix

- **P0** — Critical bug affecting multiple stores, data loss, security issue, or outage → Slack #urgent immediately
- **P1** — Bug affecting one real store with active impact, angry VIP merchant, legal threat → respond within 1 hour
- **P2** — Billing issue, refund request, repeated complaint → respond within 2 hours
- **P3** — How-to, feature request, pre-sales, general feedback → normal queue

## Escalation Rules (for CS agents escalating to Liz)

| Situation | Escalate To | How |
|-----------|-------------|-----|
| Refund request | CS Leader (Liz) | Trello card + Slack |
| Angry merchant after 2 attempts | CS Leader (Liz) | Slack with context |
| VIP merchant (any issue) | CS Leader (Liz) | Slack FYI |
| Technical bug (confirmed) | TS | Trello card |
| P0 critical bug | PM + TS Leader | Slack #urgent |
| Security / data concern | CS Leader + PM | Slack #urgent |
| Policy exception | CS Leader + PM | Slack with reasoning |
| Pricing negotiation | PM / Sales Manager | Slack |
| Legal threat | CS Leader immediately | Slack |

## Refund Decision Guide

**Can process (after Liz approval):**
- Charged after uninstalling (if within reasonable window)
- Trial ended before merchant noticed — case by case
- Clear billing error on our side

**Try to retain first:**
- App didn't meet expectations → understand why, offer to help
- Encountered a bug → fix the issue first, then evaluate

**Never approve without CS Leader sign-off:**
- Agents are NOT authorized to approve refunds independently
- All refund cases → create Trello card, assign to CS Leader

**Refund timeline:** 7–10 business days after Shopify processes it

## Sensitive Situation Rules

- **Harassment:** Warn twice → end chat. Real store → report to CS Leader before blocking.
- **Personal info requests:** Decline, redirect to app support. End chat if persistent.
- **Legal threats:** Do not engage further. Escalate to CS Leader immediately.
- **Bad review threats:** Escalate to CS Leader. Do not offer compensation without approval.

## Key Judgement Calls for Liz

When Liz is making the call herself (not just advising an agent):

- **Refund or not?** → Consider: usage history, issue validity, merchant size, precedent risk
- **Exception or hold firm?** → Ask: is this pressure or a genuine edge case? Consistency beats heroics.
- **Escalate to PM/TS?** → Ask: is this a pattern or one-off? Lead with impact and evidence, not symptoms.
- **Protect the agent?** → If merchant is abusive to an agent, step in — agents should never handle abuse alone.
