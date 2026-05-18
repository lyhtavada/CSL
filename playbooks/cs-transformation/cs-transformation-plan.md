# CS Team Transformation Plan
## From Live Chat → AI Monitor + AM Role

**Status:** In Progress — Phase 1
**Owner:** Liz (CS Leader)
**Last updated:** 2026-03-27

> **Current state:** Liz + Sam are building and testing training data. CS team not yet involved. CS joins Phase 1 once AI is assessed ready to go live — then monitors, maintains training data, and handles escalations from day one.

---

## Context

Avada CS team is transitioning from 100% live chat to an AI-first support model:
- **AI** handles live chat (Chatty + Joy)
- **CS monitors** AI and takes over when AI wants to transfer
- **CS prepares** training data and trains AI
- **CS joins** onboarding calls as AM (Account Manager role)

Current setup: 4h shifts, max 2 shifts/day on weekdays (1 on weekends), 4 FT + 3 remote/outsource
- **FT agents**: cover 8AM–12AM (16h window)
- **Remote/outsource**: cover overnight 12AM–8AM (escalation buffer)

---

## Team Role Assignment

### Chatty
| Agent | New Role |
|-------|----------|
| **Hazel** | AI Monitor |
| **Phoebe** | AI Monitor |
| **Andy** | AM / Onboarding Call |
| **Jade** | AM / Onboarding Call |

### Joy Loyalty
| Agent | New Role |
|-------|----------|
| **Hana** | AI Monitor Lead |
| **Audrey** | AI Monitor |
| **Sonny** | AM / Onboarding Call |
| **Alyssa** | AM / Onboarding Call |

### Shared
| | |
|-|-|
| **3 Remote/outsource** | Cross-app escalation buffer — cover overnight (12AM–8AM), reduce gradually as AI stabilizes |

> **Coverage model:** FT agents are split by app (no cross-app). Remote/outsource agents cover both apps during overnight — volume is low enough that depth is not required.

---

## Transition Phases (Both Apps)

| Phase | Trigger | Focus |
|-------|---------|-------|
| **Phase 1 — Preparation** | After AI assessed ready | CS onboarding: learn AI, training data format, escalation criteria |
| **Phase 2 — AI Pilot** | AI go live | Measure AI, CS as safety net, full shifts |
| **Phase 3 — Scale Down** | AI self-resolve ≥ 60% | Reduce remote, shift to async monitor |
| **Phase 4 — Steady State** | AI self-resolve ≥ 75% | New roles fully operating, KPIs switched |

See app-specific plans for details:
- [chatty-transformation.md](chatty-transformation.md)
- [joy-transformation.md](joy-transformation.md)

---

## SLA — Escalation Response Time

| Scenario | SLA |
|----------|-----|
| AI transfer during FT hours (8AM–12AM) | ≤ 5 min |
| AI transfer overnight (12AM–8AM) | ≤ 15 min |
| Urgent escalation (angry merchant, billing dispute) | ≤ 3 min |

> CS does not need to pick up instantly — AI should send an automated message ("An agent will be with you shortly") when transferring so the merchant knows to expect a short wait.

---

## Shared Principles

- **Don't cut remote outsource early** — keep as buffer until AI self-resolve rate is confirmed stable
- **Call only when needed** — async-first (chat/email), escalate to call for ICP merchants or unresolved issues
- **AM role is new for everyone including Liz** — learn from Avada AM team before running solo
- **AI Monitor role is new for everyone** — Liz leads onboarding, agents execute
- **Review conversion rate benchmark needs recalibration** once AI handles majority of chat (escalated cases naturally score lower)

---

## Liz's Phase 1 Checklist

- [ ] Arrange knowledge transfer with Avada AM team (1–2 sessions) for Andy, Jade, Sonny, Alyssa
- [ ] Introduce AI Monitor team to training data structure (`~/ai-copilot-training/`)
- [ ] Define AI go-live criteria — what accuracy/metrics must AI hit before reducing CS involvement?
- [ ] Design new KPI framework for each role
- [ ] Align with Sam on headcount plan and remote outsource timeline
- [ ] Collect ICP definitions for Chatty and Joy → add to call trigger criteria
- [ ] Set up Supabase tracking for new metrics

---

## Open Questions

- [ ] Chatty AI vs Joy AI — same go-live timeline or staggered?
- [ ] Do remote agents get informed of role changes? Or quietly reduced over time?
- [ ] Will AM agents (Andy/Jade/Sonny/Alyssa) still cover escalations during shift or fully hands-off chat?
- [ ] Budget/tools for AM: call recording, scheduling, CRM?
- [ ] ICP definition for each app — who qualifies for onboarding call?
