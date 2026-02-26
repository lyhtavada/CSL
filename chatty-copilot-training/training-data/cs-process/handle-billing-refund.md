---
category: CS Process
topic: Handling Billing and Refund Requests
source: cs-process/billing-refund
---

Q: A merchant wants to cancel their subscription or request a refund. What should I do?
Q: How do I handle a refund request from a merchant?
A: First, understand why the merchant wants to cancel or request a refund. Common reasons include:

- Charged unexpectedly (after uninstalling app or during trial)
- Subscription issues
- App didn't meet expectations
- Technical issues with the app (in this case, proactively help fix the issue first)

Use shortcut `!cancel-reason` to confirm the issue with the merchant.

**Important:** If a merchant claims they were charged without upgrading, clarify that the app does not auto-upgrade — all upgrades require approval from Shopify Admin. They may have started a trial and forgot to cancel before it ended, resulting in charges when the billing cycle began.

Q: A merchant simply doesn't want to continue using the app or subscribed by mistake. What is the refund process?
Q: What steps do I follow when a merchant requests a refund for a simple cancellation?
A: Follow these steps:

**Step 1: Guide the merchant to downgrade to Free plan**
- Use the available shortcut to guide them.
- Verify that the merchant has successfully downgraded to Free.

**Step 2: Collect billing information**
- Use shortcut `!billing-details` to request:
  - Screenshot of the invoice showing: app name, billing cycle, and amount.
  - Confirm whether the merchant has already paid the invoice.
  - Guide them to find the bill at: Shopify Admin > Settings > Billing.

**Step 3: Create a card for CS Leader**
- Use shortcut `!refund-process` to set expectations with the merchant.
- After collecting all information and confirming the app is on the Free plan, create a card, assign it to CS Leader, and note all details and refund reason.

**Critical:** CS is NOT authorized to approve any refund request without CS Leader approval. If you approve a refund without authorization, you will be personally responsible for the cost.

Q: A merchant wants a refund because the app didn't meet their expectations or they encountered a bug. What should I do?
Q: How do I handle a refund request when the reason is app dissatisfaction or a technical issue?
A: Do NOT process the refund immediately. Try to resolve the issue first:

**Step 1: Understand their expectations**
Ask what they were trying to achieve and what didn't work as expected.
Example: "Thanks for your feedback. I'm sorry to hear the app didn't meet your expectations. Could you please share more details about what you were looking to achieve or what didn't work as expected? I'd love to help clarify or find a solution that works for you."

**Step 2: Proactively offer support**
- If it's a setup or feature misunderstanding, guide them again.
- Collect info about the issue and help resolve it.
- If the issue is resolved and the merchant is satisfied, encourage them to continue using the app. Consult with CS Leader about offering a discount for the next month.

**Step 3: If the merchant still wants to cancel and refund**
- Apologize for the experience.
- Use shortcut `!billing-details` to collect invoice screenshot (app name, billing cycle, amount).
- Confirm whether the invoice has been paid.
- Guide them to downgrade to Free plan to avoid further charges.

**Step 4: Create a card**
- Use shortcut `!refund-process` and create a card for CS Leader with all details.

**Important:** For high-risk cases where the merchant doesn't accept your explanation after clear communication, do NOT continue arguing. Escalate to CS Leader/CSM on the group channel for the best resolution.

Q: How long does a refund take to process?
Q: A merchant is asking when they will receive their refund.
A: Refunds typically take 7–10 business days to appear in the merchant's bank account. This depends on both Shopify's refund process and the bank's processing time. The refund is returned to the original payment method used to pay for the app.

If more than 10 business days have passed and the merchant hasn't received the refund, advise them to check with Shopify and their bank directly. The transaction is processed by Shopify and we cannot check further on our end.

Q: A merchant was charged after uninstalling the app or downgrading to Free. Why?
Q: Why was the merchant still billed after they uninstalled or downgraded?
A: If the merchant uninstalled or downgraded after the billing cycle had already started, they will still receive a full invoice for that cycle. However, they will be refunded for any unused days within that cycle.

Q: A merchant says they were charged but the app shows the Free plan. What happened?
A: This can happen when the merchant previously uninstalled the app, which caused the subscription to be automatically canceled. When they reinstalled, the app defaults to the Free plan, but the final bill from the previous subscription cycle may still be pending.

Q: A merchant asks why they received two bills from Shopify in the same month.
Q: A merchant claims they were double-charged for the same billing cycle.
A: Ask the merchant to provide a screenshot of the charge breakdown.

- If the charges are for two different billing periods, explain: "You're not being double charged for the same app within one cycle. The two charges are for different subscription cycles. You can check the charge breakdown in your bill to see the details. Since Shopify manages how charges are added to your bill, if you'd like further clarification on why they appear in the same bill, I recommend contacting Shopify Support directly."
- If the charges appear to be for the same period, check with CS Leader.

Note: Merchants may receive two bills in one month if their charges exceeded their billing threshold before the regular billing date.

Q: When will the merchant be charged for their subscription?
A: The merchant will be charged on their regular Shopify billing date, together with their Shopify subscription and other charges (e.g., app charges). They can find more details at: https://help.shopify.com/en/manual/your-account/manage-billing/billing-charges/types-of-charges/third-party-charges/app-charges

Q: Where can a merchant see their app subscription charges?
A: They can view all charges in Shopify Admin > Settings > Billing > Bills. Each bill shows a breakdown of all charges including app subscriptions.

Q: Why might a merchant's payment fail?
A: Common reasons for payment failure include:
- The credit card on file has expired.
- No payment method is on file.
- Insufficient funds on the payment method.
- The credit card is not a valid Mastercard, Visa, or American Express.
- The credit card doesn't allow recurring payments in USD.

Direct the merchant to: https://help.shopify.com/en/manual/your-account/manage-billing/billing-charges/frozen-store
