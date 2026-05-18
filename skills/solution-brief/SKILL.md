---
name: solution-brief
description: Use this skill when the user describes a problem or requirement and asks to "think through this", "đề xuất solution", "có hướng nào không", "Sam yêu cầu X thì làm thế nào", "brainstorm", or needs to prepare a structured proposal or recommendation for leadership.
version: 1.0.0
---

# Solution Brief Skill

Structure a clear proposal when Liz needs to think through a problem or present a recommendation — to Sam, to the team, or to herself.

## When to Use

- Sam gives a vague or open-ended requirement and Liz needs to structure a response
- Liz needs to propose a new process, tool, or approach to the team
- There's a recurring problem that needs a systematic fix, not a one-off patch
- Liz needs to decide between options and wants to think it through clearly

## Output Format

```
## Solution Brief — [Topic]

### Problem
[1-3 sentences. What's actually broken or missing? Be specific — what's the symptom, and what's the root cause?]

### Context
[What's already been tried? What constraints exist? (team size, tools, timeline, budget)]

### Options

**Option A — [Name]**
- What: [brief description]
- Pros: [...]
- Cons: [...]
- Effort: [Low / Medium / High]

**Option B — [Name]**
- What: [brief description]
- Pros: [...]
- Cons: [...]
- Effort: [Low / Medium / High]

(add Option C if genuinely different)

### Recommendation
[Which option, and why. Be direct — Liz has an opinion, she doesn't hedge.]

### Next Steps
1. [Concrete action, owner, timeframe]
2. ...

### Open Questions
- [Anything that needs Sam's input or a decision from someone else]
```

## Thinking Principles

- **Lead with the problem, not the solution** — make sure the problem is framed correctly before jumping to answers
- **2-3 options max** — don't list every possibility, pick the real contenders
- **Have a recommendation** — Liz doesn't present options and walk away. She has a view.
- **Decide based on patterns, not pressure** — if the brief is being written because someone is pushing hard for something, flag that. Is this a real need or a squeaky wheel?
- **Effort vs impact** — a Medium-effort solution that actually gets adopted beats a High-effort perfect solution that doesn't
- **Protect the team** — if a proposed solution puts unrealistic load on CS agents, say so explicitly

## Tone When Presenting to Sam

- Concise — Sam reads fast. Lead with the recommendation, then the reasoning.
- Confident — Liz knows her domain. Don't over-qualify.
- Honest about tradeoffs — don't oversell. If Option A has a real downside, name it.
- Vietnamese is fine for internal discussion; use English if the brief will be shared more broadly.

## Common Problem Types in CSL Context

- **Process gaps** — something keeps falling through the cracks (escalations, follow-ups, QA)
- **Volume spikes** — a case type is growing and we need a playbook or automation
- **Team skill gaps** — agents are handling a case type badly; need training or a macro
- **Tool decisions** — choosing between approaches for a bot, script, or workflow
- **Cross-team coordination** — CS needs something from PM/TS/Dev and needs to make the ask clearly
