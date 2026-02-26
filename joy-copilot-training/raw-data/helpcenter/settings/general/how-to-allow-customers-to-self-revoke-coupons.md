Sometimes customers redeem a reward by mistake or change their mind before using the code. Instead of contacting support, you can allow them to revoke the coupon themselves. This refunds their points immediately and disables the unused coupon code, creating a more flexible and positive user experience.

### [hashtag](#enable-the-feature-in-settings) Enable the Feature in Settings

To turn on this feature, go to Settings > General and scroll down to the Enable Customer Self-Revoke Coupon section.

Steps to configure:

1. Toggle On: Switch the button to Enable.
2. Set Limits (Optional but Recommended): To prevent abuse, you can configure the following restrictions:

   - Limit revokes per timeframe: Check this box to define how many times a specific customer can revoke coupons within a certain period (e.g., 3 times per week).
   - Revoke time limit: Check this box to set a window of time allowing revocation after redemption. (e.g., Customers can only revoke within 30 minutes of redeeming the reward).

> Note: By default, the system only allows revoking coupons that have not been used in any order yet.

---

### [hashtag](#how-it-works-for-customers) How it works for Customers

Once enabled, customers will see a "Revoke" button on their reward details.

- Location: Customers can find this in the Loyalty Widget > My Rewards (or in the Rewards Block on the storefront).
- Action: When they click "Revoke", the coupon is disabled, and their points are instantly returned to their balance.
- Status:

  - Revoke: The coupon is available to be cancelled.
  - Revoked: The action is complete; the coupon is invalid.
  - Disabled (Tooltip): If the button is grayed out (disabled), hovering over it will show a tooltip explaining why (e.g., "Time limit exceeded" or "Usage limit reached").

---

### [hashtag](#automation-with-shopify-flow) Automation with Shopify Flow

For advanced workflows, Joy Loyalty now supports a Revoke Coupon action in Shopify Flow. This allows you to automate the revocation process based on specific triggers.

- Action Name: Revoke coupon
- Required Inputs:

  - `Coupon code`

Đây là phần Frequently Asked Questions (FAQ) bổ sung để bài guide đầy đủ hơn, tập trung vào việc xử lý điểm, giới hạn và trạng thái coupon như trong requirement bạn mô tả.

Bạn có thể đặt phần này ở cuối bài viết, sau mục Shopify Flow.

---

### [hashtag](#frequently-asked-questions-faq) Frequently Asked Questions (FAQ)

**Q: Can customers revoke a coupon that has already been used in an order?**
A: No. The system automatically checks the coupon status with Shopify. If the code has already been used at checkout, the Revoke button will be disabled or hidden.

**Q: Will the points be refunded immediately?**
A: Yes. As soon as the customer confirms the revocation, the coupon code becomes invalid, and the points are instantly returned to their loyalty point balance.

**Q: How can I track revoked coupons?**
A: All revocation activities are recorded. You can check the customer's Activity Log in the Joy Loyalty admin to see when a coupon was revoked and the points refunded.

[PreviousHow to Set Up Points Exchange Ratechevron-left](/settings/general/how-to-set-up-points-exchange-rate)[NextColorchevron-right](/settings/color)

Last updated 19 days ago

Was this helpful?