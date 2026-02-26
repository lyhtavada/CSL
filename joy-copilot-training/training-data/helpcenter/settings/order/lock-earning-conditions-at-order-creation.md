---
category: Settings
subcategory: Order
topic: Lock Earning Conditions At Order Creation
source: helpcenter
---

Q: What is Lock Earning Conditions At Order Creation in Joy Loyalty?
Q: How do I set up Lock Earning Conditions At Order Creation?
Q: Where can I find Lock Earning Conditions At Order Creation settings?
A: ### Overview

By default, Joy calculates loyalty points when an order is **fulfilled**. However, if reward rules change between the time a customer places an order and the time it's fulfilled, the actual points awarded may differ from what the customer expected.

To prevent this, enable **“Lock earning conditions at order creation”**. This ensures customers always receive the points based on the reward conditions at the **moment they placed the order**, not when it's fulfilled.

### Example scenario

Let’s say you create a rule:
&#xNAN;**“Earn +10,000 points for purchasing from Collection A.”**

1. A customer places an order containing a product from Collection A.
2. At checkout, Joy estimates they’ll earn +10,000 points.
3. Before the order is fulfilled, you remove the product from Collection A.

- **Without this setting**: When you fulfill the order, the product no longer qualifies. The customer doesn’t get the 10,000 bonus points.
- **With this setting enabled**: Joy locks the reward conditions at checkout, so the customer still receives the 10,000 bonus points.

### How to enable

1. Go to your **Joy app → Settings → Order**
2. Set order status to **Fulfilled** (required for this setting to appear)
3. Enable the toggle: **“Lock earning conditions at order creation”**
4. Click **Save** to apply the changes

> ⚠️ Note: This setting only appears when "Reward after order is fulfilled" is selected.

### Key behavior when this is enabled

- Points calculation is based on **order creation time**, not fulfillment.
- Earning conditions (e.g. bonus collections, product rules) are **captured at the time the order is placed** and stored with the order.
- Changes to reward rules **after the order is placed** will not affect that order.

### FAQs

**Q: Will old orders be affected when I enable this setting?**
A: No. This only applies to orders placed **after** the setting is enabled.

**Q: What if I disable the setting later?**
A: Orders placed while the setting was ON will still use locked conditions. New orders will follow the updated behavior.

---

Q: Will old orders be affected when I enable this setting?
A: No. This only applies to orders placed **after** the setting is enabled.

Q: What if I disable the setting later?
A: Orders placed while the setting was ON will still use locked conditions. New orders will follow the updated behavior.

[PreviousDisplay awaiting points](/settings/order/display-awaiting-points)[NextAdd tags for orders and customers](/settings/order/add-tags-for-orders-and-customers)

Last updated 19 days ago

Was this helpful?
