# Case Handling Playbook

<!-- CHUNK: ref-case-handling-classification -->
```yaml
chunk_id: "ref__case-handling-classification"
doc_id: "cs-ref-case-handling"
title: "Case Classification — How to categorize incoming merchant requests"
category: "cs-process"
subcategory: "case-handling"
tags: ["case classification", "how-to", "bug", "feature request", "billing", "complaint", "pre-sales", "discount", "demo"]
applies_when: "CS receives a new merchant request and needs to classify it"
priority: "high"
```

## Case Classification

When a merchant reaches out, first determine: does the merchant have a **question** or a **problem**? Then classify:

| Case Type | Examples | Handler |
|-----------|----------|---------|
| **How-to Questions** | "How do I set up X?", "Where can I find Y?" | CS Agent |
| **Bug/Issue Reports** | "Feature X is broken", "Widget not showing" | CS → TS → Dev |
| **Feature Requests** | "Can you add X?", "Integration with Y?" | CS Agent → PM |
| **Billing & Subscription** | "Why was I charged?", "How do I upgrade?" | CS Agent (CS Leader for refunds) |
| **Complaints** | "Your app is terrible!", "I've been waiting for days" | CS Agent → CS Leader |
| **Pre-sales Questions** | "Does your app do X?", "How much does it cost?" | CS Agent |
| **Integration Questions** | "Can this work with X?", "How do I connect Y?" | CS (basic) → TS (complex) |
| **Discount Requests** | "Can I get a discount on the plan?" | CS Agent → CS Leader/Sales |
| **Demo Requests** | "Can you show me how this works?" | CS Agent (schedule) |

---

<!-- CHUNK: ref-case-handling-how-to -->
```yaml
chunk_id: "ref__case-handling-how-to"
doc_id: "cs-ref-case-handling"
title: "How to handle How-to Questions from merchants"
category: "cs-process"
subcategory: "case-handling"
tags: ["how-to", "knowledge base", "step-by-step", "helpcenter", "confirm"]
applies_when: "Merchant asks a how-to question (setup, navigation, feature usage)"
priority: "medium"
```

## How-to Questions

1. Check knowledge base for the answer
2. Provide step-by-step answer with navigation paths
3. Link to relevant helpcenter article
4. Follow up to confirm it worked

---

<!-- CHUNK: ref-case-handling-bugs -->
```yaml
chunk_id: "ref__case-handling-bugs"
doc_id: "cs-ref-case-handling"
title: "How to handle Bug and Issue Reports from merchants"
category: "cs-process"
subcategory: "case-handling"
tags: ["bug", "issue", "triage", "troubleshooting", "escalate", "TS", "Trello", "evidence", "reproduce"]
applies_when: "Merchant reports a bug or technical issue"
priority: "high"
```

## Bug/Issue Reports

1. **Triage** — is it a bug or a configuration issue?
2. **Basic troubleshooting** — check settings, clear cache, try another browser
3. **Gather evidence** — screenshots, steps to reproduce, store URL, plan
4. **If config issue** → guide the merchant to fix it
5. **If confirmed bug** → escalate to TS via Trello card

---

<!-- CHUNK: ref-case-handling-feature-requests -->
```yaml
chunk_id: "ref__case-handling-feature-requests"
doc_id: "cs-ref-case-handling"
title: "How to handle Feature Requests from merchants"
category: "cs-process"
subcategory: "case-handling"
tags: ["feature request", "PM", "product team", "no promise", "timeline", "forward"]
applies_when: "Merchant requests a new feature or integration"
priority: "medium"
```

## Feature Requests

1. Understand what the merchant is trying to achieve
2. Check if an existing feature already solves their need
3. If no existing solution → document the request and forward to PM
4. Don't promise features or timelines — say "I'll pass this to our product team"

---

<!-- CHUNK: ref-case-handling-complaints -->
```yaml
chunk_id: "ref__case-handling-complaints"
doc_id: "cs-ref-case-handling"
title: "How to handle Complaints — SLA, escalation triggers, and approach"
category: "cs-process"
subcategory: "case-handling"
tags: ["complaint", "SLA", "2 hours", "escalate", "CS Leader", "VIP", "legal threat", "negative review", "refund"]
applies_when: "Merchant is complaining, angry, or escalating an issue"
priority: "high"
```

## Complaints

**SLA: respond within 2 hours.**

1. Respond quickly — don't leave an angry merchant waiting
2. Stay professional — don't take it personally
3. Understand root cause — what actually went wrong?
4. Take ownership — apologize for their experience
5. Provide a solution — specific action plan with realistic timeline
6. Follow through — do what you promised, update proactively
7. Document and share with the team

**Escalate to CS Leader when:**
- After 2 attempts, merchant is still angry
- Merchant threatens legal action or public negative review
- Issue involves refund or compensation
- VIP merchant complaint

---

<!-- CHUNK: ref-case-handling-presales -->
```yaml
chunk_id: "ref__case-handling-presales"
doc_id: "cs-ref-case-handling"
title: "How to handle Pre-sales Questions — SLA and approach"
category: "cs-process"
subcategory: "case-handling"
tags: ["pre-sales", "SLA", "4 hours", "potential customer", "free trial", "honest", "capabilities"]
applies_when: "A potential merchant asks about Chatty features, pricing, or capabilities before installing"
priority: "medium"
```

## Pre-sales Questions

**SLA: respond within 4 hours.**

1. Respond fast — these are potential customers
2. Understand their needs
3. Be honest about capabilities — don't oversell
4. Guide them to free trial
5. Share relevant helpcenter links or demo

---

<!-- CHUNK: ref-case-handling-other -->
```yaml
chunk_id: "ref__case-handling-other"
doc_id: "cs-ref-case-handling"
title: "How to handle Integration Questions and Discount Requests"
category: "cs-process"
subcategory: "case-handling"
tags: ["integration", "native", "third-party", "custom", "TS", "discount", "CS Leader", "sales manager"]
applies_when: "Merchant asks about integrations or requests a discount"
priority: "medium"
```

## Integration Questions

1. Identify the integration type (native, third-party, custom)
2. For native integrations → provide setup guide
3. For complex/custom integrations → escalate to TS

## Discount Requests

1. Listen to the merchant's reasoning
2. Escalate to CS Leader or Sales Manager — CS agents do not have authority to approve discounts
