# AI Conversation Limit Extension Request

<!-- CHUNK: ai-conversation-limit-overview -->
```yaml
chunk_id: "case__ai-conversation-limit-overview"
doc_id: "cs-case-ai-conversation-limit"
title: "AI Conversation Limit Extension — Overview & Escalation Requirement"
category: "cs-process"
subcategory: "limit-extension"
tags: ["AI conversation", "limit", "extend", "monthly quota", "escalate", "PM", "sale-cs-success"]
applies_when: "Merchant hits their monthly AI conversation limit and asks CS to increase it"
priority: "high"
```

## Overview

AI conversation limits are a **monthly quota** that resets each month (including the Free plan). When a merchant hits their limit and needs more, CS **cannot self-extend** — escalation to PM is required before making any changes.

CS does **NOT** extend AI Conversations without PM approval — this affects billing and product strategy. Post in **#sale-cs-success** and tag PM.

## Plan Limits Reference

| Plan | AI Conversations |
|------|-----------------|
| Free | 50/month (resets monthly; AI pauses when reached, resumes next cycle) |
| Basic | 100/month + $0.40/extra |
| Pro | 500/month + $0.40/extra |
| Plus | 1,000/month + $0.40/extra |

---

<!-- CHUNK: ai-conversation-limit-flow -->
```yaml
chunk_id: "case__ai-conversation-limit-flow"
doc_id: "cs-case-ai-conversation-limit"
title: "AI Conversation Limit Extension — Step-by-Step Flow"
category: "cs-process"
subcategory: "limit-extension"
tags: ["extend", "escalate", "sale-cs-success", "PM", "upgrade", "flow", "AI conversation"]
applies_when: "CS needs to handle a merchant's request for more AI conversations"
priority: "high"
```

## Resolution Steps

### Step 1 — Gather information before escalating

Collect from the merchant or via their account:
- Store URL
- Current plan (Free / Basic / Pro / Plus)
- Average number of chats per month (ask merchant or check analytics)
- Which plan they're considering upgrading to (if any)
- Reason for needing more conversations

### Step 2 — Check if upgrade solves it first

If the merchant is on a lower plan and the next plan up covers their volume → recommend upgrading first. Manual limit extension is for cases where upgrading alone isn't sufficient or the merchant needs a temporary bridge.

### Step 3 — Escalate for approval

Post in **#sale-cs-success** and tag PM with:
- Store URL + current plan
- Monthly chat volume (estimated)
- Plan they're considering / reason they need more
- Requested extension amount (if merchant specified)

Wait for approval before making any changes.

### Step 4 — Follow up with merchant

Once approved, confirm the extension has been applied and advise on next steps (upgrade recommendation if applicable).

**Sample response to merchant while waiting:**

> Thank you for reaching out! To help you get more AI conversations, I'll need a little more information:
>
> - Approximately how many chats does your store handle per month?
> - Are you considering upgrading your plan, or are you looking for a temporary extension?
>
> Once I have these details, I'll check with our team and get back to you as soon as possible.

---

<!-- CHUNK: ai-conversation-limit-approval-timeline -->
```yaml
chunk_id: "case__ai-conversation-limit-approval-timeline"
doc_id: "cs-case-ai-conversation-limit"
title: "AI Conversation Limit Extension — Approval Timeline & Process"
category: "cs-process"
subcategory: "limit-extension"
tags: ["approval", "timeline", "escalate", "sale-cs-success", "PM", "wait"]
applies_when: "CS has escalated the request and the merchant is asking about timeline"
priority: "low"
```

## After Escalation

After CS posts in #sale-cs-success and tags PM with full details, the team will review and respond in the channel. CS should wait for explicit approval before applying any changes.

Timeline depends on team availability — if urgent, note that in the escalation message.

---

## Related
- case_ai-product-limit (product/URL/file limit extension)
- case_ai-scenario-limit (scenario limit extension)
