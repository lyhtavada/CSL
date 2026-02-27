# Case Handling Playbook

## Case Classification

When a merchant reaches out, classify their request:

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

First determine: does the merchant have a **question** or a **problem**? Then classify into the specific case type.

---

## How-to Questions

1. Check knowledge base for the answer
2. Provide step-by-step answer with navigation paths
3. Link to relevant helpcenter article
4. Follow up to confirm it worked

## Bug/Issue Reports

1. **Triage** — is it a bug or a configuration issue?
2. **Basic troubleshooting** — check settings, clear cache, try another browser
3. **Gather evidence** — screenshots, steps to reproduce, store URL, plan
4. **If config issue** → guide the merchant to fix it
5. **If confirmed bug** → escalate to TS via Trello card (see [escalation.md](escalation.md))

## Feature Requests

1. Understand what the merchant is trying to achieve
2. Check if an existing feature already solves their need
3. If no existing solution → document the request and forward to PM
4. Don't promise features or timelines — say "I'll pass this to our product team"

## Complaints

SLA: respond within **2 hours**.

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

## Pre-sales Questions

SLA: respond within **4 hours**.

1. Respond fast — these are potential customers
2. Understand their needs
3. Be honest about capabilities — don't oversell
4. Guide them to free trial
5. Share relevant helpcenter links or demo

## Integration Questions

1. Identify the integration type (native, third-party, custom)
2. For native integrations → provide setup guide
3. For complex/custom integrations → escalate to TS

## Discount Requests

1. Listen to the merchant's reasoning
2. Escalate to CS Leader or Sales Manager — CS agents do not have authority to approve discounts
