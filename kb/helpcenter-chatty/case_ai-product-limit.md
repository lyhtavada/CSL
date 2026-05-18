# Extend AI Training Data Limits (Products / Custom Answers / URL & File)

<!-- CHUNK: extend-ai-training-limits-overview -->
```yaml
chunk_id: "case__extend-ai-training-limits-overview"
doc_id: "cs-case-extend-ai-training-limits"
title: "Extend AI Training Data Limits — Overview & Who Handles What"
category: "cs-process"
subcategory: "limit-extension"
tags: ["limit", "extend", "products", "custom_answers", "url_file", "ai_training", "devzone", "plan"]
applies_when: "Merchant hits their Products, Custom Answers, or URL & File limit for AI training and asks CS to increase it"
priority: "high"
```

## Overview

CS can self-extend 3 types of AI training data limits — no escalation needed:
- **Products for AI training**
- **Custom Answers for AI training**
- **URL & File for AI training**

CS does **NOT** extend AI Conversations or AI Scenarios — those require PM approval via #sale-cs-success.

## Plan Limits Reference

| Feature | Free | Basic ($19.99) | Pro ($68.99) | Plus ($199) |
| --- | --- | --- | --- | --- |
| Products for AI training | 100 | 500 | 8,000 | 20,000 |
| Custom Answers | 100 | 1,000 | Unlimited | Unlimited |
| URL & File | 20 | 50 | 500 | 700 |

---

<!-- CHUNK: extend-ai-training-limits-flow -->
```yaml
chunk_id: "case__extend-ai-training-limits-flow"
doc_id: "cs-case-extend-ai-training-limits"
title: "Extend AI Training Data Limits — Step-by-Step Flow"
category: "cs-process"
subcategory: "limit-extension"
tags: ["extend", "devzone", "extended-limit", "tag", "flow", "products", "custom_answers", "url_file"]
applies_when: "CS needs to extend a merchant's Products, Custom Answers, or URL & File limit"
priority: "high"
```

## Resolution Steps

### Step 1 — Confirm the merchant's situation

Verify:
- What plan are they on? (Free / Basic / Pro / Plus)
- Which limit did they hit? (Products / Custom Answers / URL & File)
- How much do they need?

### Step 2 — Decide how much to extend

Extend up to the next plan's limit — **1 tier only, no more**.

| Merchant's plan | Products → extend to | Custom Answers → extend to | URL & File → extend to |
| --- | --- | --- | --- |
| Free | 500 (= Basic) | 1,000 (= Basic) | 50 (= Basic) |
| Basic | 8,000 (= Pro) | Unlimited (= Pro) | 500 (= Pro) |
| Pro | 20,000 (= Plus) | Already Unlimited | 700 (= Plus) |
| Plus | Max reached → escalate PM | Already Unlimited | Max reached → escalate PM |

### Step 3 — Apply the extension in DevZone

1. Go to DevZone
2. Adjust the relevant limit (Products / Custom Answers / URL & File)
3. Confirm the change is applied

### Step 4 — Tag the conversation

Add tag **`extended-limit`** to the conversation in Crisp. Mandatory — do not skip.

### Step 5 — Confirm with merchant

> Great news! I've extended your [Products/Custom Answers/URL & File] limit so you can continue setting up your AI assistant. You should now be able to [sync more products / add more custom answers / upload more files].
>
> Just so you know, if you need even more capacity in the future, upgrading to [next plan] would give you [limit of next plan] and also unlock [key feature of that plan]. Let me know if you need any help with that!

---

<!-- CHUNK: extend-ai-training-limits-edge-cases -->
```yaml
chunk_id: "case__extend-ai-training-limits-edge-cases"
doc_id: "cs-case-extend-ai-training-limits"
title: "Extend AI Training Data Limits — Edge Cases & Decision Points"
category: "cs-process"
subcategory: "limit-extension"
tags: ["extend", "repeat_request", "free_plan", "plus_plan", "multiple_limits", "escalate", "upgrade"]
applies_when: "Non-standard situations when handling a limit extension request"
priority: "medium"
```

## Edge Cases

### Merchant requests multiple limits at once
Extend each limit type separately, all following the 1-tier rule. Apply all changes in DevZone, tag `extended-limit` once, confirm everything in a single message.

### Merchant has been extended before and comes back asking for more
This is a strong signal the merchant needs to upgrade. Push the upgrade clearly. If merchant still refuses → escalate to CSL. Do not extend again without CSL input.

### Merchant is on Free plan
Still extend up to Basic limits (same 1-tier rule). Make the extension but highlight the benefits of upgrading — the goal is to help them see Chatty's value and convert, not give unlimited free access.

### Merchant is on Plus and needs more than Plus limit
CS cannot self-extend beyond Plus limits. Escalate to PM via #sale-cs-success with: store URL, current plan, which limit is hit, and how much the merchant needs.

## Notes

- **Purpose of extending:** let the merchant experience enough value to upgrade on their own — not a permanent free pass.
- **Always tag `extended-limit`** after every extension — no exceptions.
- **Never extend AI Conversations or AI Scenarios** — those affect billing and product strategy, require PM approval.

---

## Related
- case_ai-product-sync (sync issues affecting product count)
- case_ai-conversation-limit (conversation limit extension)
- case_ai-scenario-limit (scenario limit extension)
- faq_pricing (plan limits reference)
