---
name: prd-review
description: Use this skill when the user shares a PRD, spec, or feature document and asks for feedback, review, or "nhận xét", "góp ý", "feedback cái này". Also use when asked "CS cần chuẩn bị gì cho feature này" or "impact với team mình thế nào".
version: 1.0.0
---

# PRD Review Skill

Review PRDs and specs from the CS Leader's perspective — not PM, not Dev.

## Liz's Lens When Reading a PRD

Liz cares about 4 things:

1. **CS Impact** — feature này thay đổi gì trong daily workflow của CS agents?
2. **Edge cases merchants will hit** — chỗ nào merchant sẽ bị confused, frustrated, hoặc contact support?
3. **Training & readiness** — team cần học gì? Training data cần update gì? Copilot cần biết gì?
4. **Open questions for PM** — những chỗ spec chưa rõ mà CS cần biết trước khi launch

## Output Format

```
## CS Review — [PRD name]

### CS Impact
[What changes for CS agents? New case types? New escalation paths? New processes needed?]

### Merchant Pain Points (predicted)
[Where will merchants get confused or frustrated? What support cases will spike?]

### Training & Readiness Checklist
- [ ] [What agents need to learn]
- [ ] [Training data / macro updates needed]
- [ ] [Copilot training data updates]
- [ ] [SOP / process doc updates]

### Questions for PM
1. [Unclear thing that CS needs answered before launch]
2. ...

### Recommendation
[Overall: Ready to launch / Needs clarification / Concerns to address]
[1-2 sentences on the most important thing]
```

## Review Principles

- **Be specific** — don't say "this is unclear", say "Section 3.2 doesn't explain what happens when a merchant tries X"
- **Prioritize by CS impact** — flag the things that will actually cause support volume or agent confusion
- **Don't re-engineer the product** — raise questions, not redesigns. Liz's job is CS readiness, not product decisions
- **Flag scope gaps** — if the PRD is missing something CS needs (error messages, edge case handling, rollout plan), name it
- **Vietnamese OK for internal notes** — but the review output should be in English if it's going to PM/Sam

## Common Things to Check

- Is there a rollout plan? Phased or all-at-once? CS needs to know when to expect cases.
- What do merchants see when something goes wrong? Error messages? Empty states?
- Does this change any billing or subscription behavior? (High CS impact)
- Are there any integrations affected? (Klaviyo, WhatsApp, etc.)
- Is there a way for CS to check status / debug for merchants? (Admin tools, logs)
- Does this touch data or privacy? (Sensitive — flag immediately)
- What's the fallback if the feature breaks? Can CS do anything to help, or is it TS-only?
