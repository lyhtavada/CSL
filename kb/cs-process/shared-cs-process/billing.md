# Billing & Refund Playbook

## Case Types

### General Inquiry (plan comparison, how to upgrade)

CS handles directly. Explain plan features and guide the merchant through the upgrade process in Shopify Admin.

### Charge Confusion (why charged, unexpected amount)

CS explains the charge. Check the merchant's charge history, review plan usage, and provide invoice details.

### Cancellation Request

1. Understand why they want to cancel
2. If possible, address their concerns
3. If they proceed → guide them through cancellation/downgrade

### Refund Request

**CS is NOT authorized to approve any refund request without CS Leader approval.**

#### Simple cancellation (merchant doesn't want to continue / subscribed by mistake)

**Step 1:** Guide merchant to downgrade to Free plan. Verify they've downgraded.

**Step 2:** Collect billing info using `!billing-details`:
- Screenshot of invoice showing: app name, billing cycle, amount
- Whether the invoice has been paid
- Where to find: Shopify Admin > Settings > Billing

**Step 3:** Create Trello card for CS Leader using `!refund-process`:
- Assign to CS Leader
- Include all details and refund reason

#### Dissatisfaction or bug-related refund

**Step 1:** Understand their expectations — what they were trying to achieve

**Step 2:** Proactively offer support:
- If setup/feature misunderstanding → guide them again
- If bug → help resolve it
- If resolved and merchant is satisfied → encourage continued use, consult CS Leader about next-month discount

**Step 3:** If merchant still wants to cancel:
- Apologize for the experience
- Collect billing info (`!billing-details`)
- Guide to downgrade to Free plan

**Step 4:** Create Trello card for CS Leader

**High-risk cases:** If merchant doesn't accept your explanation after clear communication → do NOT argue. Escalate to CS Leader/CSM immediately.

### Dispute / Chargeback

Immediately escalate to CS Leader with full context.

---

## Common Billing Questions

**Q: How long does a refund take?**
7–10 business days. Depends on Shopify's refund process and the bank. If > 10 days, advise merchant to check with Shopify and their bank directly.

**Q: Merchant was charged after uninstalling/downgrading. Why?**
If they uninstalled/downgraded after the billing cycle started, they'll receive a full invoice for that cycle but be refunded for unused days.

**Q: Merchant shows Free plan but was charged. What happened?**
They may have uninstalled (auto-cancels subscription), then reinstalled (defaults to Free), but the final bill from the previous cycle was still pending.

**Q: Two bills in the same month?**
Ask for charge breakdown screenshot. If different billing periods → explain. If same period → check with CS Leader. May be caused by exceeding billing threshold before regular billing date.

**Q: When will the merchant be charged?**
On their regular Shopify billing date, together with Shopify subscription and other app charges.

**Q: Where to see charges?**
Shopify Admin > Settings > Billing > Bills.

**Q: Why did payment fail?**
Common reasons: expired card, no payment method, insufficient funds, card doesn't support recurring USD payments.

---

## Key Shortcuts

| Shortcut | Purpose |
|----------|---------|
| `!cancel-reason` | Confirm cancellation reason with merchant |
| `!billing-details` | Request billing info (invoice screenshot, payment status) |
| `!refund-process` | Set expectations with merchant about refund timeline |
