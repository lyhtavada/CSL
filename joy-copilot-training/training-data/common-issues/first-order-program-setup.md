---
category: Reward programs
problem: Setting up a Place Order program for first order only
source: notion
---

Q: How do I create a loyalty program that only rewards points on a customer's first order?
Q: I want to set up a "first purchase" bonus in Joy. How do I configure that?
Q: Can I give extra points only for the first order a customer places? How do I set that up?
Q: I need a Place Order program that distinguishes between first-time and returning customers. What's the best approach?
Q: How do I reward first-time buyers differently from repeat customers using Joy?
A: Setting up a first-order-only program is a great way to incentivize new customers! This feature requires the **Advanced plan** with the **Rule Engine** enabled.

Before we start, there's an important question: **What counts as a "first order"?**

---

**Approach A - First Order based on Shopify order history:**

This uses Shopify's own data to determine if someone has ordered before.

1. **Create a Shopify segment** for customers who have purchased at least once (e.g., "Customers who have purchased at least once").
2. **Set up a Shopify Flow** automation that adds a tag like `ordered_before` to customers after they place an order.
3. **Create your First Order Program** in Joy:
   - Set it to **high priority**.
   - Add a condition: customer does **NOT** have the tag `ordered_before`.
4. **(Optional)** Create a separate **Subsequent Orders Program** with the condition: customer **HAS** the tag `ordered_before` (for different point values on repeat orders).

---

**Approach B - First Order based on app logic (using Shopify Flow):**

This approach handles everything through Shopify Flow without relying on Joy's program conditions.

1. **Create a Shopify Flow** with:
   - **Trigger:** "Order created"
   - **Condition:** Customer does NOT have the tag `ordered_before`
   - **Actions:** Adjust loyalty points (for the first-order bonus) AND add the tag `ordered_before`
2. Your regular Joy earning programs will handle all subsequent orders as normal.

---

**Key things to consider:**
- Which definition of "first order" works best for your store (Shopify history vs. app-tracked)?
- Should first-order rewards stack with other earning programs?
- How should existing customers (who ordered before you set this up) be handled?

Let me know which approach sounds right for your store and I'll walk you through the detailed setup!

Escalate khi: The merchant is not on the Advanced plan, or the Rule Engine setup requires custom configuration beyond the standard options.
