# Chatty — CS Transformation Plan

**App:** Chatty (live chat, AI, FAQ)
**Status:** In Progress — Phase 1
**Last updated:** 2026-03-27

> **Current state:** Liz + Sam are building and testing training data. CS team is not yet involved — CS joins when AI is assessed ready to go live.

## Team

| Agent | New Role |
|-------|----------|
| **Hazel** | AI Monitor |
| **Phoebe** | AI Monitor |
| **Andy** | AM / Onboarding Call |
| **Jade** | AM / Onboarding Call |

---

## Phase 1 — Preparation (Before AI Go Live)

> CS joins Phase 1 only after Liz + Sam assess AI is ready to go live. Goal: get CS team ready to monitor and maintain AI from day one.

### Hazel + Phoebe (+ Liz) — AI Monitor Track

> AI Monitor is a new skill. Liz leads the onboarding, Hazel + Phoebe execute.

**Understand how AI works:**
- [ ] Liz walks through how Chatty AI works — data sources, how AI learns, what affects response quality
- [ ] Walk through existing training data structure together (`~/ai-copilot-training/chatty/`)
- [ ] Live demo: show a bad AI response → explain why → show how to fix via training data

**Learn training data format (to maintain, not build from scratch):**
- [ ] Learn training data format: Q&A pairs, variants, escalation guidance
- [ ] Practice: each writes 5–10 Q&A entries → Liz reviews and gives feedback
- [ ] Learn what makes good vs bad training data (specific vs vague, tone, edge cases)

**AI monitor skills:**
- [ ] Learn what "good AI response" looks like vs needs correction
- [ ] Define escalation criteria together: what types of cases should AI always transfer?
  - e.g. refund requests, billing disputes, angry merchants, bugs
- [ ] Practice: review 20 real Chatty AI conversations, rate each, discuss
- [ ] Learn to log errors systematically — not just "AI was wrong" but *why* and *what the correct answer is*

---

### Andy + Jade (+ Liz) — AM Track

> AM role is new for the whole team. Learn from Avada AM team before running solo.

**Learn from AM team first:**
- [ ] Liz arranges 1–2 knowledge transfer sessions with Avada AM team
- [ ] Andy + Jade shadow at least 2–3 real calls before running solo
- [ ] Document what AM team does differently — tone, objective, call flow

**Prepare Chatty AM playbook:**
- [ ] Define ICP for call support (add once Liz shares ICP doc)
- [ ] Map Chatty onboarding journey: new install → chatbox setup → AI setup → first conversation
- [ ] Draft call talk track — lightweight, not a rigid script
- [ ] Define call triggers: when to reach out proactively
  - e.g. paid plan but AI not set up after 7 days, ICP merchant on free plan, stuck in setup

**AM support scope:**
- Not limited to onboarding calls — AM owns the merchant relationship ongoing
- **Onboarding:** guide new ICP merchants through setup (chatbox, AI, first conversation)
- **Ongoing support:** continue supporting merchant post-onboarding via chat, email, or call as needed
- **Proactive check-ins:** 30/60/90 day follow-up to ensure merchant is getting value
- Not a sales call — goal is activation, retention, and success
- Async-first: chat/email is default, escalate to call only when needed or merchant requests

---

## Phase 2 — AI Pilot (First 1–3 Months After Go Live)

### Key metrics to establish baseline

| Metric | Target |
|--------|--------|
| AI self-resolve rate | Establish baseline |
| Escalation rate | Establish baseline |
| Escalation pickup time (FT hours) | ≤ 5 min |
| Escalation pickup time (overnight) | ≤ 15 min |
| Urgent escalation pickup time | ≤ 3 min |
| Time-to-resolve escalated cases | < 10 min |
| AI response accuracy (sampled weekly) | > 80% |
| Onboarding calls completed / month | Establish baseline |

### Hazel + Phoebe — AI Monitor duties
- Monitor AI conversations in real time during shift
- Flag and correct wrong AI responses
- Identify gaps → write new training data entries to fix recurring issues
- Log recurring errors weekly → feed back into training data
- Weekly: what topics is AI still failing at?

**Shift structure:**
- 4h = 2h active monitor + 2h training data / QA
- FT agents cover 8AM–12AM window (max 2 shifts/day weekday, 1 shift/day weekend)
- Overnight 12AM–8AM: remote/outsource as escalation buffer

### Andy + Jade — AM duties
- Reach out to new Chatty merchants matching ICP criteria
- Target: paid plan merchants who haven't set up AI yet
- Ongoing support for ICP merchants post-onboarding — via chat, email, or call
- Proactive check-ins at 30/60/90 days
- Track all interactions and outcomes in `call_followup` table (Supabase)

**Shift structure:**
- 4h = call prep + calls + follow-up notes
- FT agents cover 8AM–12AM window (max 2 shifts/day weekday, 1 shift/day weekend)

---

## Phase 3 — Scale Down (Month 3–6)
> Trigger: AI self-resolve rate ≥ 60%

- Hazel/Phoebe: shift from real-time monitor → async (respond to escalations within SLA)
- Andy/Jade: increase call volume, begin handling expansion/upsell conversations
- Reduce remote outsource if overnight escalation rate drops

---

## Phase 4 — Steady State (Month 6+)
> Trigger: AI self-resolve rate ≥ 75%, escalation rate stable

- Hazel/Phoebe fully async — no fixed shift for monitoring
- Andy/Jade fully in AM role
- KPIs fully switched (see below)

---

## New KPI Framework

### Hazel + Phoebe — AI Monitor
| KPI | Notes |
|-----|-------|
| AI accuracy score | % responses rated "good" (sampled weekly) |
| Escalation resolution rate | % escalated cases resolved without re-escalation |
| Training data output | # new QA entries / month |
| Escalation response time | Time from AI transfer to human pickup |

### Andy + Jade — AM
| KPI | Notes |
|-----|-------|
| Onboarding calls completed / month | Volume |
| Post-call activation rate | Did merchant set up the feature after call? |
| Call-to-review conversion | Did merchant leave a review after successful call? |
| Merchant check-in completion | 30/60/90 day follow-up done |
