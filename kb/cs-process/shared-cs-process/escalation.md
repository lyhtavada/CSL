# Escalation Playbook

## Priority Levels

| Priority | Definition | Examples | First Response | Resolution Target |
|----------|-----------|----------|---------------|-------------------|
| **P0 — Critical** | App down, data loss, security issue, affects all merchants | App won't load, all data deleted, payment broken | Immediate (< 1 hour) | 4–24 hours |
| **P1 — High** | Core feature broken, affects merchant business | Rewards can't be redeemed, AI not responding, chatbox down | 2–4 hours | 1–5 days |
| **P2 — Medium** | Minor feature issue, workaround available | Email delay, minor display issue | 4–24 hours | 1–2 weeks |
| **P3 — Low** | Cosmetic issue, enhancement request | Color alignment, text typo, minor UI inconsistency | 1–2 days | Backlog |

## SLA by Ticket Type

| Ticket Type | First Response | Resolution Target |
|-------------|---------------|-------------------|
| P0 Critical Bug | < 1 hour | 4–24 hours |
| P1 High Bug | < 4 hours | 2–5 days |
| Complaint | < 2 hours | Same day |
| Pre-sales | < 4 hours | Same day |
| How-to (VIP merchant) | < 2 hours | < 6 hours |
| How-to (Regular) | < 24 hours | < 48 hours |
| Billing (not refund) | < 4 hours | Same day |
| Refund Request | < 2 hours | < 24 hours |
| Feature Request | < 24 hours | No commitment |

## Escalation Matrix

| Situation | Escalate To | When | How |
|-----------|------------|------|-----|
| Technical bug (after CS troubleshooting) | TS | Immediately | Trello card |
| Cannot reproduce bug | TS | Immediately | Trello card |
| Critical bug (P0) | PM + TS Leader | Immediately | Slack + #urgent |
| Refund request | CS Leader | Immediately | Slack or Trello card |
| Angry merchant (after 2 attempts) | CS Leader | Immediately | Slack or Trello card |
| VIP merchant (any issue) | CS Leader | FYI immediately | Slack with context |
| Feature request (5+ merchants) | PM | Weekly batch | Slack with context |
| Design/UX confusion (multiple cases) | PM | Weekly batch | Slack with context |
| Complex custom integration | PM | After initial assessment | Slack with context |
| Security concern | CS Leader + PM | Immediately | Slack + #urgent |
| Data loss issue | CS Leader + PM | Immediately | Slack + #urgent |
| Policy exception | CS Leader + PM | Immediately | Slack with reasoning |
| Pricing negotiation | PM / Sales Manager | Immediately | Slack with details |

## Before Escalating a Bug

Make sure you have:

1. Confirmed it's **not** a merchant configuration issue
2. Clear **steps to reproduce**
3. Complete evidence — screenshots, video, store URL
4. **Priority assessment** (P0/P1/P2/P3)

## Information to Collect

- Store URL (mystore.myshopify.com)
- App plan (Free / Basic / Pro / Plus / Professional / Advanced / Enterprise)
- Steps to reproduce the issue
- Screenshots or screen recordings
- Browser and device info (if UI-related)
- Affected customer emails or order numbers (if applicable)
