# AI Scenario Limit Extension Request

<!-- CHUNK: ai-scenario-limit-overview -->
```yaml
chunk_id: "case__ai-scenario-limit-overview"
doc_id: "cs-case-ai-scenario-limit"
title: "AI Scenario Limit — Plan Limits & Escalation Requirement"
category: "cs-process"
subcategory: "limit-extension"
tags: ["AI scenario", "scenario limit", "extend", "escalate", "PM", "sale-cs-success", "plan limit"]
applies_when: "Merchant hits their AI scenario limit and asks CS to increase it"
priority: "high"
```

## Overview

AI scenario limits are set per plan. CS **cannot self-extend** scenario limits — escalation to PM or CSL is required.

## Plan Limits Reference

| Plan | AI Scenarios |
|------|-------------|
| Free | Up to 5 scenarios |
| Basic | Up to 5 scenarios |
| Pro | Up to 15 scenarios |
| Plus | — |

**Note:** Existing stores created before limits were introduced keep their existing scenario count (no retroactive limit applied). New stores follow the limits above.

---

<!-- CHUNK: ai-scenario-limit-flow -->
```yaml
chunk_id: "case__ai-scenario-limit-flow"
doc_id: "cs-case-ai-scenario-limit"
title: "AI Scenario Limit Extension — Step-by-Step Flow"
category: "cs-process"
subcategory: "limit-extension"
tags: ["extend", "escalate", "flow", "sale-cs-success", "PM", "use case", "scenarios"]
applies_when: "CS needs to handle a merchant's request for more AI scenarios"
priority: "high"
```

## Resolution Steps

### Step 1 — Understand what they need

Ask the merchant:
- How many additional scenarios they need and why
- What use cases or customer situations the new scenarios will cover (the more specific, the better — helps with approval)
- Their current plan

### Step 2 — Escalate for approval

Post in **#sale-cs-success** and tag PM or CSL with:
- Store URL + current plan
- Current number of scenarios in use
- Number of additional scenarios requested
- Use cases / situations the new scenarios will handle

Wait for approval before making any changes.

### Step 3 — Follow up with merchant

Once approved, confirm the limit has been updated and let the merchant know they can proceed.

**Sample response to merchant while waiting:**

> Thanks for getting in touch! To help with your request, could you share a bit more about what you'd like to use the additional scenarios for — for example, what types of customer questions or situations you're looking to cover?
>
> This helps us process your request faster. I'll follow up once I have an update from our team.

---

## Related
- case_ai-product-limit (product/URL/file limit extension)
- case_ai-conversation-limit (conversation limit extension)
