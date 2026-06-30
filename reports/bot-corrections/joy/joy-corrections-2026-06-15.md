# Bot Corrections — Joyce (Joy)

**Tuần:** 15/06/2026 → 21/06/2026  ·  **Tổng correction:** 6

> Đây là các câu bot trả bị CS sửa trong tuần. Dùng để update KB/training data cho bot.

## 📌 Tóm tắt theo topic

### khác — 3 câu
- Sonny*
- eg/ 1000 yen coupon if the customer spent 12000 yen in their order
- yes

### integration — 1 câu
- I cannot integrate with BOLD Subscriptions

### points/earning — 1 câu
- Hello, I can no longer find how to validate the Google reviews that customers have left in order to unlock their points. Thank you. [Image:…

### setup/config — 1 câu
- About the unified widget: Do I have to translate all this inside the widget setup? I already translated everything in the classic widget

**Người sửa:** Sonny (3), Liz (1), Alyssa (1), Jade (1)

---

## 📋 Chi tiết từng correction

### 1. [khác] — Sonny · 16/06 15:54

**Q:** Sonny*

**Bot trả (sai/thiếu):**

```
Hi there! I'm Joyce, your AI assistant from Joy. 😊

To set up a "RM 1 spent = 10 points" earning rule, here's how:

Go to Joy Dashboard → Earning programs
Click on Money spent (or create a new one if it doesn't exist)
Set the rule to: for every 1 currency unit spent, customers earn 10 points
Save the changes

Once saved, customers will automatically earn 10 points for every RM 1 they spend at checkout.

Would you like to confirm if you can see the Money spent program in your dashboard?
```

**CS sửa thành:**

```
You can go to the Reward programs section > Open the Place Order rule to adjust the point earning rate there
```

**Context:** Submitted via TS Elite by huytc@avadagroup.com · ref=crisp:session_9e89a914-ba39-4da8-b769-60254f306d0b

_session: `session_9e89a914-ba39-4da8-b769-60254f306d0b`_

### 2. [integration] — Liz · 17/06 09:03

**Q:** I cannot integrate with BOLD Subscriptions

**Bot trả (sai/thiếu):**

```
Hi! I'm Joyce, your AI assistant! How can I help? 😊

Thanks for reaching out about BOLD Subscriptions. Unfortunately, Joy currently works with subscription apps that use Shopify's Selling Plans + Contracts standard, and BOLD Subscriptions uses its own proprietary system rather than that standard.

This means BOLD Subscriptions is not compatible with Joy's integration at this time.

If you'd like, I can connect you with our team to confirm this or explore any possible workarounds?
```

**CS sửa thành:**

```
sai, có work with bold subscription
```

**Context:** Submitted via TS Elite by lyht@avada.io · ref=crisp:session_4ce72cfe-7bbd-4d4c-ac03-7ceea7b058b4

_session: `session_4ce72cfe-7bbd-4d4c-ac03-7ceea7b058b4`_

### 3. [khác] — Alyssa · 17/06 10:12

**Q:** eg/ 1000 yen coupon if the customer spent 12000 yen in their order

**Bot trả (sai/thiếu):**

```
Yes, that's possible! You can set this up as a redeeming program in Joy.

Here's how it would work:

Go to Joy Admin → Reward programs → Redeeming programs
Create a new Discount program (amount off)
Set the reward as a 1000 yen coupon
Set the points required to match your earning rate — so if customers earn points per amount spent, they'd need enough points equivalent to 12,000 yen in purchases to redeem

When a customer hits that points threshold, Joy generates a unique one-time coupon code they can apply.

Would you like help calculating the exact points threshold based on your current earning rate?
```

**CS sửa thành:**

```
Thanks for the clarification!

Just to confirm, you wanted to give customers a discount as a reward when they reach a milestone of spending, right?
```

**Context:** Submitted via TS Elite by lypk@avadagroup.com · ref=crisp:session_ae72b2ca-af12-4451-9239-14d6fcb24254

_session: `session_ae72b2ca-af12-4451-9239-14d6fcb24254`_

### 4. [points/earning] — Sonny · 17/06 13:36

**Q:** Hello, I can no longer find how to validate the Google reviews that customers have left in order to unlock their points. Thank you.
[Image: /images/components/base/BaseFlag/fr.png]

**Bot trả (sai/thiếu):**

```
To validate Google reviews and unlock points, you can do this directly from the client page in Shopify.

Go to Shopify Admin → Clients, open the profile of the relevant client, and in the Joy panel on the right, you will find the "Google review submissions" section where you can approve or reject pending reviews.

Are you able to locate this section on your end?
```

**CS sửa thành:**

```
To validate Google reviews and unlock points, you can do this directly from the client page in Shopify.

Go to Shopify Admin → Customers, open the profile of the relevant client, and in the Joy panel on the right, you will find the "Activities" button then  "Google review submissions" section where you can approve or reject pending reviews.

Are you able to locate this section on your end?
```

**Context:** Submitted via TS Elite by huytc@avadagroup.com · ref=crisp:session_d47f3bc9-2655-418d-b808-e6eee8bd0fb8

_session: `session_d47f3bc9-2655-418d-b808-e6eee8bd0fb8`_

### 5. [khác] — Sonny · 17/06 22:52

**Q:** yes

**Bot trả (sai/thiếu):**

```
Great! Since the integration is connected, you can use Joy's Klaviyo properties in your email templates.

For points balance, use the property loyalty_lion_points_balance and for VIP tier, use loyalty_lion_tier_name in your Klaviyo email blocks.

To add these as a footer in Klaviyo, go to your email template and insert a text or dynamic block using those profile properties.

Could you let me know if you'd like a step-by-step guide on setting up the dynamic block in Klaviyo, or are you more looking for help on the Joy side to make sure the right data is being synced?
```

**CS sửa thành:**

```
Great! Since the integration is connected, you can use Joy's Klaviyo properties in your email templates.

For points balance, use the property {{ person|lookup:'Joy Loyalty Points'|default:'' }} and for VIP tier, use {{ person|lookup:'Joy Vip tier'|default:'' }} in your Klaviyo email blocks.

To add these as a footer in Klaviyo, go to your email template and insert a text or dynamic block using those profile properties.

Could you let me know if you'd like a step-by-step guide on setting up the dynamic block in Klaviyo, or are you more looking for help on the Joy side to make sure the right data is being synced?
```

**Context:** Submitted via TS Elite by huytc@avadagroup.com · ref=crisp:session_f67892bb-e278-4571-a032-364572874593

_session: `session_f67892bb-e278-4571-a032-364572874593`_

### 6. [setup/config] — Jade · 18/06 19:19

**Q:** About the unified widget:
Do I have to translate all this inside the widget setup? I already translated everything in the classic widget

**Bot trả (sai/thiếu):**

```
The translations you've already set up in the Classic widget won't carry over automatically to the Unified widget, so you would need to go through the translation fields again in the new version.

That said, the Unified widget has a full sidebar editor with a live preview, so you can see exactly how everything looks as you translate. It's a bit more work upfront, but the result is much more flexible.

Would you like to go ahead with the switch, or would you prefer to wait until you have time to redo the translations?
```

**CS sửa thành:**

```
The translations you've already configured in the Classic widget will be carried over automatically to the Unified widget. This means you do not need to set up the translation fields again after switching to the new version.

That said, the Unified widget has a full sidebar editor with a live preview, so you can see exactly how everything looks as you translate. It's a bit more work upfront, but the result is much more flexible.

Would you like to go ahead with the switch, or would you prefer to wait until you have time to redo the translations?
```

**Context:** Submitted via TS Elite by phuongnt01@avadagroup.com · ref=crisp:session_6e677956-c60d-46e4-a487-bdeda2191f89

_session: `session_6e677956-c60d-46e4-a487-bdeda2191f89`_
