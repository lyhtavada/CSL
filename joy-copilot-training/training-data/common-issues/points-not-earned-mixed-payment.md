---
category: Reward programs
problem: Points not earned when customer pays with both credit card and store credit (mixed payment)
source: notion
---

Q: My customer paid with a mix of credit card and store credit, but they didn't earn any loyalty points for the order. Why?
Q: Orders paid partially with store credit are not earning points. Is this a bug or expected behavior?
Q: A customer used store credit and a credit card for the same order, but Joy didn't give them any points. How do I fix this?
Q: Why are orders with mixed payment methods (credit card + store credit) not triggering point earnings in Joy?
Q: I've excluded store credit from earning points, but now orders that use store credit along with another payment method don't earn any points at all. What's going on?

A: This behavior depends on which Joy plan you're on.

**If you're on the Free or Essential plan:**
When you've set up a rule to exclude store credit payments from earning points, the system treats the **entire order** as excluded -- even if the customer also paid partially with a credit card. Unfortunately, on these plans, the app cannot split the order into separate payment portions. This means any order that includes store credit as a payment method will not earn points at all.

This is a known limitation on the Free and Essential plans.

**If you're on the Advanced or Ultimate plan:**
You have access to the **Rule Engine**, which can handle partial payment scenarios. With the Rule Engine, you can configure Joy to:
- Calculate points only on the non-store-credit portion of the payment.
- Apply more granular rules for mixed payment methods.

**What to do:**
1. Check which plan you're currently on by going to **Joy > Settings > Billing**.
2. If you're on **Free or Essential**, this is expected behavior. To handle mixed payments properly, consider upgrading to the **Advanced or Ultimate plan**.
3. If you're on **Advanced or Ultimate**, go to **Joy > Rule Engine** and set up a rule to handle partial payment calculations. If you need help configuring this, our support team can walk you through it.

Escalate khi: Merchant is on Advanced/Ultimate plan but the Rule Engine is not calculating partial payments correctly.
