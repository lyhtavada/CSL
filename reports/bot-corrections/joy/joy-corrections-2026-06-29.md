# Bot Corrections — Joyce (Joy)

**Tuần:** 29/06/2026 → 05/07/2026  ·  **Tổng correction:** 7

> Đây là các câu bot trả bị CS sửa trong tuần. Dùng để update KB/training data cho bot.

## 📌 Tóm tắt theo topic

### setup/config — 2 câu
- do I need to go to settings? [Image: /images/components/base/BaseFlag/it.png]
- it is alreday setup i think can help to check in my store

### khác — 2 câu
- how do i get there
- 网站的默认登录界面怎么跟Joy: Loyalty Program 绑定成为一个登录接口

### chat/inbox — 1 câu
- [Image: https://storage.crisp.chat/users/upload-1/session/-/a/d/8/6/ad868dd162614000/screenshot-2026-06-29-184406_gd6be.png]

### points/earning — 1 câu
- Hi i want to set up your VIP tier system based on total amount spent, but i want to calculate this expenditure based on past year (rolling)…

### pricing/plan — 1 câu
- Hi i want to ask, if for essential plan can i do a pop up at the front page where they can key in their birthdya and email then it will aut…

**Người sửa:** Alyssa (3), Sonny (2), Hana (1), Rosie (1)

---

## 📋 Chi tiết từng correction

### 1. [chat/inbox] — Alyssa · 29/06 15:55

**Q:** [Image: https://storage.crisp.chat/users/upload-1/session/-/a/d/8/6/ad868dd162614000/screenshot-2026-06-29-184406_gd6be.png]

**Bot trả (sai/thiếu):**

```
It looks like the discount wasn't applied before reaching the Shopify approval page. Please cancel that approval for now.

Then go to your Joy Admin → Subscription page and apply the code JOY-BFCM2025 there first. Once applied, it'll generate a new approval link with the 30% off already reflected.

Could you give that a try and let me know what you see?
```

**CS sửa thành:**

```
It looks like the discount wasn't applied before reaching the Shopify approval page. Please cancel that approval for now.

Let me forward your case to our team for further checking.
```

**Context:** Submitted via TS Elite by lypk@avadagroup.com · ref=crisp:session_e334958f-f0b4-42d7-b2e8-3545411123d3

_session: `session_e334958f-f0b4-42d7-b2e8-3545411123d3`_

### 2. [setup/config] — Alyssa · 29/06 23:12

**Q:** do I need to go to settings?
[Image: /images/components/base/BaseFlag/it.png]

**Bot trả (sai/thiếu):**

```
It depends on what you want to use:
- For the Loyalty page: no need to go into settings. Go to Joy Admin → On-site content → Loyalty page, copy the page link and share it wherever you want (menu, email, etc.).
- For Deep links: yes, you can find them in Joy Admin → Settings → General → Deep links.
Which of the two were you looking for?
```

**CS sửa thành:**

```
It depends on what you want to use:
- For the Loyalty page: no need to go into settings. Go to Joy Admin → On-site content → Loyalty page, copy the page link and share it wherever you want (menu, email, etc.).
- For Deep links: yes, you can find them in Joy Admin → Settings → Developers → Deep links.
Which of the two were you looking for?
```

**Context:** Submitted via TS Elite by lypk@avadagroup.com · ref=crisp:session_ea1f6b04-e347-4316-9a8f-6ede536f7330

_session: `session_ea1f6b04-e347-4316-9a8f-6ede536f7330`_

### 3. [points/earning] — Sonny · 30/06 15:54

**Q:** Hi i want to set up your VIP tier system based on total amount spent, but i want to calculate this expenditure based on past year (rolling). How do i do this?

**Bot trả (sai/thiếu):**

```
Hi there, I'm Joyce, your AI agent from Joy. 😊

Good news: Joy does support a rolling spend window for VIP tiers. Here's how to set it up:

First, make sure your tier calculation method is set to "Amount spent" (the Assessment settings below are only available with that method).

Then go to Joy Admin → Membership → VIP Tier → Assessment and configure these three values:

- Assessment Cycle: how often Joy reviews each customer's tier (e.g., every 12 months)
- Order Review Timeframe: set this to 12 to evaluate only orders from the past 12 months (this is your rolling window)
- Spending Threshold: the minimum spend within that 12-month window to retain the tier

One thing to flag: VIP Tiers are available on the Advanced and Ultimate plans. You're currently on the free plan, so you can fully configure everything now and it'll be saved, but it won't go live for customers until you upgrade to Advanced or higher.

Would you like help with anything else in the tier setup, like entry rewards or tier thresholds?
```

**CS sửa thành:**

```
Then go to Joy Admin → Membership → VIP Tier → Check the calculation method to Amount Spent →Select a start date in the past for the system to sync the data of old orders →Once the syncing is done, you can launch the program to assign the tier based on the calculated data previously
```

**Context:** Submitted via TS Elite by huytc@avadagroup.com · ref=crisp:session_852e24d1-05c6-4aef-94fb-c4ef4692d4bf

_session: `session_852e24d1-05c6-4aef-94fb-c4ef4692d4bf`_

### 4. [pricing/plan] — Sonny · 01/07 13:52

**Q:** Hi i want to ask, if for essential plan can i do a pop up at the front page where they can key in their birthdya and email then it will auto become membership

**Bot trả (sai/thiếu):**

```
Hi there, I'm Joyce, your AI agent from Joy. 😊

Quick note first: I can see your store is currently on the free plan, not Essential yet. Just want to make sure I'm giving you the right info based on your actual plan.

Now, for your question: Joy does have a visit website popup (under On-site content → Popups) that can nudge visitors to sign up, and the Joy widget has a "Join" button that auto-enrolls customers as members. However, a single popup that collects both email and birthday in one step isn't something I can confirm from what I have on hand.

Could I check with our team on the exact capability here? They'll be able to confirm whether that specific flow is supported and how to set it up.
```

**CS sửa thành:**

```
Hi there, I'm Joyce, your AI agent from Joy. 😊

Quick note first: I can see your store is currently on the free plan, not Essential yet. Just want to make sure I'm giving you the right info based on your actual plan.

Now, for your question: Our loyalty program is connected to Shopify Customer Account, so when customers sign up for an account on the store, they will become a member of the program as well. And in Essential plan, indeed, you will be able to add the loyalty blocks on a page for customers to enter birthday and do other interactions as well such as redeeming and copy referral link.

Could I check with our team on the exact capability here? They'll be able to confirm whether that specific flow is supported and how to set it up.
```

**Context:** Submitted via TS Elite by huytc@avadagroup.com · ref=crisp:session_facbc645-fcaa-43e6-a5a9-99f599a86792

_session: `session_facbc645-fcaa-43e6-a5a9-99f599a86792`_

### 5. [khác] — Hana · 02/07 22:47

**Q:** how do i get there

**Bot trả (sai/thiếu):**

```
Here's how to get there:

• Open your Joy Admin dashboard
• Click On-site content in the left menu
• Select Branding
• Click the Popups tab

From there you should see your reward reminder pop-up listed. Once you open it, let me know what options you see for the image and I'll guide you from there!
```

**CS sửa thành:**

```
Here's how to get there:

• Open your Joy Admin dashboard
• Click On-site content in the left menu
• Select Unified widget
• Click setup
```

**Context:** Submitted via TS Elite by hanghm@avadagroup.com · ref=crisp:session_43a054ad-6fa6-40ee-bd29-163677770a2f

_session: `session_43a054ad-6fa6-40ee-bd29-163677770a2f`_

### 6. [khác] — Alyssa · 03/07 13:58

**Q:** 网站的默认登录界面怎么跟Joy: Loyalty Program 绑定成为一个登录接口

**Bot trả (sai/thiếu):**

```
关于登录接口的绑定，Joy 支持以下几种方式让顾客通过统一入口登录并识别积分身份：

- Sign in with Shop App（所有套餐可用，开关即可启用）
- Email OTP / Google / Facebook 登录（需要 Shopify Plus + 旧版顾客账户）

你们目前的 Shopify 套餐不是 Plus，所以现阶段可以启用的是 Shop App 登录。

设置路径：Joy Admin → Settings → Additional Features → 开启 Sign in with Shop App

启用后，顾客在你的店铺登录时，Joy 会自动识别其账户并关联积分记录，不需要单独注册 Joy。

请问你们店铺目前用的是新版顾客账户还是旧版（Legacy）？这样我可以更准确地告诉你哪些登录方式适合你们。
```

**CS sửa thành:**

```
Regarding login interface binding, Joy supports the following methods to let customers sign in through a unified entry point and have their loyalty points identity recognized:
- Sign in with Shopify login and Shop App (available on all plans, the Shop app login can be enabled with a toggle)
Email OTP / Google / Facebook sign in (requires Shopify Plus + Legacy customer accounts)

Your current Shopify plan is not Plus, so at this stage the login method you can enable is Sign in with Shop App.

Setup path: Joy Admin → Settings → Additional Features → enable Sign in with Shop App

After enabling it, when customers sign in to your store, Joy will automatically recognize their account and link their loyalty points history, with no need for a separate Joy sign-up.

Which version of customer accounts are you currently using on your store, the new version or Legacy? That way I can tell you more accurately which sign-in methods are suitable for you.
```

**Context:** Submitted via TS Elite by lypk@avadagroup.com · ref=crisp:session_2bd4af08-014a-4cf9-b592-94bc44c8a623

_session: `session_2bd4af08-014a-4cf9-b592-94bc44c8a623`_

### 7. [setup/config] — Rosie · 03/07 18:23

**Q:** it is alreday setup i think can help to check in my store

**Bot trả (sai/thiếu):**

```
Sure! To take a look at your store setup, our team will need collaborator access. Could you share your collaborator request code? You can find it in Shopify Admin → Settings → Users → Security — it's a 4-digit number.
```

**CS sửa thành:**

```
Escalate cho CS để check app setting xem khách set up đúng chưa
```

**Context:** Submitted via TS Elite by thaoltt.ctv@avadagroup.com · ref=crisp:session_dad20868-db0d-440a-8fa0-09485bec2f9c

_session: `session_dad20868-db0d-440a-8fa0-09485bec2f9c`_
