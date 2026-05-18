---
name: write-process
description: Use this skill when the user asks to "viết quy trình", "tạo SOP", "write a process", "làm flow xử lý", "thêm quy trình mới", or needs to create/update a CS support process for the team — either shared (applies to both apps) or app-specific (Chatty or Joy only).
version: 1.0.0
---

# Write Process Skill

Create or update a CS support process document for the Avada Support Team.

## Context

- Liz is CS Leader for two Shopify apps: **Chatty** and **Joy Loyalty**
- Processes are used by CS agents as reference when handling cases
- There are 3 levels of process docs:
  - **Shared** (`kb/cs-process/shared-cs-process/`) — applies to both apps (e.g., escalation, billing, first response)
  - **Chatty-specific** (`kb/cs-process/chatty-support-flow.md` or referenced sub-docs)
  - **Joy-specific** (`kb/cs-process/joy-support-flow.md` or referenced sub-docs)

## When to Use

- Liz wants to document a new support flow (e.g., "handle order tracking issues", "handle loyalty tier complaints")
- Liz wants to formalize something the team has been doing informally
- Liz wants to update or expand an existing process
- Liz says "viết quy trình cho...", "thêm process...", "cần SOP cho..."

## Step 1 — Clarify Scope

Before writing, ask (if not already clear from context):

1. **Which app?** Chatty, Joy, or shared (both)?
2. **What triggers this process?** (e.g., "merchant says points are missing", "customer asks about refund")
3. **Who executes?** CS Agent, CS Leader, or both?
4. **Any existing process to reference or replace?**

If Liz gives enough context upfront, skip the questions and draft directly.

## Step 2 — Draft the Process

Use this structure:

```markdown
# [Process Name]

## When to Use
[1-2 sentences: what situation triggers this process]

## Who
[CS Agent / CS Leader / Both — and when to hand off]

## Steps

### 1. [First action]
- What to do
- What to say (template if applicable)
- What to check

### 2. [Next action]
...

### 3. [Decision point — if applicable]
- **If [condition A]:** → [action]
- **If [condition B]:** → [action]
- **If unsure:** → escalate to [who]

## Escalation
[When to escalate, to whom, via what channel — reference escalation-matrix.md if standard]

## Templates
[Ready-to-use message templates, if applicable]

## Notes
[Edge cases, exceptions, things agents commonly get wrong]
```

## Writing Rules

- **Be specific** — include exact navigation paths, button names, field names where relevant
- **Decision trees over paragraphs** — agents scan, they don't read essays
- **Include templates** — if the process involves messaging the merchant, write the actual text
- **Name the tools** — Trello, Slack, which channel, what to put in the card
- **Reference existing docs** — don't duplicate. Link to `escalation-matrix.md`, `first-response.md`, etc. when applicable
- **Keep steps numbered and short** — max 3-4 bullet points per step

## Tone

- Written for CS agents, not merchants — can be direct and instructional
- Vietnamese is fine if Liz asks for it, but default to English
- No fluff. Agents need to find info fast during live chats.

## Step 3 — File Placement

After drafting, place the file correctly:

| Scope | Location |
|-------|----------|
| Shared (both apps) | `kb/cs-process/shared-cs-process/handle-[topic].md` |
| Chatty only | `kb/cs-process/chatty/[topic].md` |
| Joy only | `kb/cs-process/joy/[topic].md` |

Naming convention: `handle-[topic].md` for action-oriented processes (e.g., `handle-missing-points.md`, `handle-widget-not-showing.md`).

If updating an existing file, edit in place — don't create a duplicate.

## Step 4 — Cross-reference

After creating the process:
- Check if `kb/INDEX.md` needs an entry added
- Check if the app-specific flow file (`chatty-support-flow.md` or `joy-support-flow.md`) should reference the new process
- If this process involves escalation, verify it aligns with `escalation-matrix.md`

## Output

Present the draft to Liz for review before writing to file. Format:

> **File:** `kb/cs-process/shared-cs-process/handle-[topic].md`
> **Scope:** Shared / Chatty / Joy
>
> [full process content]
>
> Liz duyệt thì mình save nhé?
