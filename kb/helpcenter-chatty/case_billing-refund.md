# Billing & Refund Playbook

<!-- CHUNK: billing-refund-case-types -->
```yaml
chunk_id: "case__billing-refund-case-types"
doc_id: "cs-case-billing-refund"
title: "Billing & Refund — Case Classification and Who Handles What"
category: "cs-process"
subcategory: "billing"
tags: ["billing", "refund", "cancel", "charge", "inquiry", "chargeback", "dispute", "subscription"]
applies_when: "Merchant contacts CS about billing, charges, cancellation, or refund"
priority: "high"
```

## Case Types

| Case Type | Who Handles |
|-----------|------------|
| General inquiry (plan comparison, how to upgrade) | CS handles directly |
| Charge confusion (why charged, unexpected amount) | CS explains + checks charge history |
| Cancellation request | CS handles + escalates if refund needed |
| Refund request | CS collects info → escalates to CS Leader |
| Dispute / Chargeback | Immediately escalate to CS Leader |

**⚠️ CS is NOT authorized to approve any refund without CS Leader approval.**

---

<!-- CHUNK: billing-refund-simple-cancellation -->
```yaml
chunk_id: "case__billing-refund-simple-cancellation"
doc_id: "cs-case-billing-refund"
title: "Billing — Simple Cancellation / Refund Request Flow"
category: "cs-process"
subcategory: "billing"
tags: ["refund", "cancel", "downgrade", "trello", "billing-details", "CS leader", "free plan"]
applies_when: "Merchant wants to cancel or requests a refund with no service complaint (subscribed by mistake or just doesn't want to continue)"
priority: "high"
```

## Resolution Steps — Simple Cancellation

**Step 1:** Guide merchant to downgrade to Free plan. Verify they've downgraded.

**Step 2:** Collect billing info using `!billing-details`:
- Screenshot of invoice showing: app name, billing cycle, amount
- Whether the invoice has been paid
- Where to find: **Shopify Admin → Settings → Billing**

**Step 3:** Create Trello card for CS Leader using `!refund-process`:
- Assign to CS Leader
- Include all details and refund reason

---

<!-- CHUNK: billing-refund-dissatisfaction -->
```yaml
chunk_id: "case__billing-refund-dissatisfaction"
doc_id: "cs-case-billing-refund"
title: "Billing — Refund Due to Dissatisfaction or Bug"
category: "cs-process"
subcategory: "billing"
tags: ["refund", "dissatisfied", "bug", "complaint", "cancel", "high-risk", "escalate", "CS leader"]
applies_when: "Merchant requests a refund because they're unhappy with the app or experienced a bug"
priority: "high"
```

## Resolution Steps — Dissatisfaction or Bug-Related Refund

**Step 1:** Understand their expectations — what were they trying to achieve?

**Step 2:** Proactively offer support:
- If setup/feature misunderstanding → guide them again
- If bug → help resolve it
- If resolved and merchant is satisfied → encourage continued use, consult CS Leader about next-month discount

**Step 3:** If merchant still wants to cancel:
- Apologize for the experience
- Collect billing info (`!billing-details`)
- Guide to downgrade to Free plan

**Step 4:** Create Trello card for CS Leader.

**High-risk cases:** If merchant doesn't accept your explanation after clear communication → do NOT argue. Escalate to CS Leader/CSM immediately.

---

<!-- CHUNK: billing-refund-common-questions -->
```yaml
chunk_id: "case__billing-refund-common-questions"
doc_id: "cs-case-billing-refund"
title: "Billing — Common Merchant Questions About Charges"
category: "cs-process"
subcategory: "billing"
tags: ["billing", "charged", "payment failed", "two bills", "refund timeline", "uninstall", "billing date"]
applies_when: "Merchant asks common questions about why they were charged, when they'll be charged, or why payment failed"
priority: "medium"
```

## Common Billing Questions

**How long does a refund take?**
7–10 business days. Depends on Shopify's refund process and the bank. If > 10 days, advise merchant to check with Shopify and their bank directly.

**Merchant was charged after uninstalling/downgrading. Why?**
If they uninstalled/downgraded after the billing cycle started, they'll receive a full invoice for that cycle but be refunded for unused days.

**Merchant shows Free plan but was charged. What happened?**
They may have uninstalled (auto-cancels subscription), then reinstalled (defaults to Free), but the final bill from the previous cycle was still pending.

**Two bills in the same month?**
Ask for charge breakdown screenshot. If different billing periods → explain. If same period → check with CS Leader. May be caused by exceeding billing threshold before regular billing date.

**When will the merchant be charged?**
On their regular Shopify billing date, together with Shopify subscription and other app charges.

**Where to see charges?**
Shopify Admin → Settings → Billing → Bills.

**Why did payment fail?**
Common reasons: expired card, no payment method, insufficient funds, card doesn't support recurring USD payments.

---

<!-- CHUNK: billing-refund-shortcuts -->
```yaml
chunk_id: "case__billing-refund-shortcuts"
doc_id: "cs-case-billing-refund"
title: "Billing — Key Shortcuts Reference"
category: "cs-process"
subcategory: "billing"
tags: ["shortcut", "billing-details", "refund-process", "cancel-reason", "crisp shortcut"]
applies_when: "CS needs to use billing-related message shortcuts in Crisp"
priority: "low"
```

## Key Shortcuts

| Shortcut | Purpose |
|----------|---------|
| `!cancel-reason` | Confirm cancellation reason with merchant |
| `!billing-details` | Request billing info (invoice screenshot, payment status) |
| `!refund-process` | Set expectations with merchant about refund timeline |
