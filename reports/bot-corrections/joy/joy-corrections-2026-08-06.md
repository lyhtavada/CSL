# Bot Corrections — Joyce (Joy)

**Tuần:** 06/08/2026 → 12/08/2026  ·  **Tổng correction:** 16

> Đây là các câu bot trả bị CS sửa trong tuần. Dùng để update KB/training data cho bot.

## 📌 Tóm tắt theo topic

### khác — 9 câu
- can I also hide everything to non-logged in users?
- it has a pop up that says "session token fetch failed"
- https://creaturelandstore.com/pages/joy-loyalty-page
- … +6 câu khác (xem chi tiết bên dưới)

### referral — 2 câu
- Hi there! When a customer enters their friend's email to refer them (on the "share your referral link" page), does Joy send that email to K…
- need to turn off joy referral tag

### integration — 1 câu
- Hi! I'm trying to lower my Shopify app spending limit for JOY Loyalty. Shopify currently shows my spending limit as $9,901 USD, with $0 spe…

### loyalty page/widget — 1 câu
- I would like users to be able to complete the actions themselves directly on the loyalty page.

### points/earning — 1 câu
- Can we setup the amount of points the different vip tiers earn? example: vip1= 1 point per $ spent. vip2:= 1.5 points per $ spent. VIP3= 2 …

### setup/config — 1 câu
- Bạn ơi, bên app mình đang không configure với Klaviyo, vậy mình đang gửi email qua nền tảng nào vậy ạ

### pricing/plan — 1 câu
- Hello Alyssa, I plan to subscribe to the AOV.ai cart drawer and AOV.ai Free Gift plans. I would like to ask you for a discount if I purchas…

**Người sửa:** Jade (7), Sonny (5), Alyssa (3), hieunm02@avadagroup.com (1)

---

## 📋 Chi tiết từng correction

### 1. [khác] — hieunm02@avadagroup.com · 06/08 11:45

**Q:** can I also hide everything to non-logged in users?

**Bot trả (sai/thiếu):**

```
There isn't a built-in toggle in Joy to hide the widget specifically from non-logged-in visitors. It's designed to show a "join" prompt to guests so they can sign up.
```

**CS sửa thành:**

```
Unified widget có option để chỉ hiện sau khi login: On-site content > Widget > Unified Widget > Settings > Display > Display after login > Turn on
```

**Context:** Submitted via TS Elite by hieunm02@avadagroup.com · ref=crisp:session_cb8a5872-4675-4ffd-850d-82a15f3213dc

_session: `session_cb8a5872-4675-4ffd-850d-82a15f3213dc`_

### 2. [khác] — Sonny · 07/08 04:53

**Q:** it has a pop up that says "session token fetch failed"

**Bot trả (sai/thiếu):**

```
Just following up - were you able to check if the POS staff account is using individual or role-based permissions?
```

**CS sửa thành:**

```
If you have tried to remove and re-add the Joy POS extension but still doesn't work, please try to follow our guidance here: https://help.joy.so/pos/add-joy-to-shopify-pos/#faqs
```

**Context:** Submitted via TS Elite by huytc@avadagroup.com · ref=crisp:session_86d7a98c-3220-483d-8973-893b1326c8ec

_session: `session_86d7a98c-3220-483d-8973-893b1326c8ec`_

### 3. [khác] — Sonny · 07/08 05:35

**Q:** https://creaturelandstore.com/pages/joy-loyalty-page

**Bot trả (sai/thiếu):**

```
Just go to Shopify Admin → Online Store → Themes → Customize, open the Joy Loyalty page template, then click on the Joy: Loyalty Program FAQs block to edit its content.
```

**CS sửa thành:**

```
Just go to On-site content > Loyalty Page > FAQ block and edit the FAQs there
```

**Context:** Submitted via TS Elite by huytc@avadagroup.com · ref=crisp:session_cf0dd5a6-e611-4b4d-8690-77063db4edd4

_session: `session_cf0dd5a6-e611-4b4d-8690-77063db4edd4`_

### 4. [khác] — Sonny · 07/08 05:52

**Q:** Yes, it that doable?

**Bot trả (sai/thiếu):**

```
Yes, it's doable! You'd just set up two separate Birthday reward programs.
```

**CS sửa thành:**

```
Yes, it's doable! However, it will require the Advanced plan to upgrade the logic  of the birthday program so that it can support multiple rewards
```

**Context:** Submitted via TS Elite by huytc@avadagroup.com · ref=crisp:session_e0042121-7db0-458c-b272-47cf0b3be435

_session: `session_e0042121-7db0-458c-b272-47cf0b3be435`_

### 5. [khác] — Jade · 07/08 08:09

**Q:** yes the question and answer

**Bot trả (sai/thiếu):**

```
I don't have exact documented steps for editing the FAQ question and answer text within that specific FAQ block, let me check with our team and get back to you here.
```

**CS sửa thành:**

```
Please go to the Onsite section > Loyalty page, then scroll down to find the Loyalty Program FAQs section. Here, you can update the questions and answers according to your preferences.
```

**Context:** Submitted via TS Elite by phuongnt01@avadagroup.com · ref=crisp:session_cf0dd5a6-e611-4b4d-8690-77063db4edd4

_session: `session_cf0dd5a6-e611-4b4d-8690-77063db4edd4`_

### 6. [khác] — Sonny · 07/08 16:20

**Q:** how to select auto gift with purchase

**Bot trả (sai/thiếu):**

```
You can set this up under Joy Dashboard → Reward programs → Redeem programs → create a new "Free product" reward, then choose the selection mode: "Free one product from selection" (customer picks one) or "Free all products in selection" (for bundles).
```

**CS sửa thành:**

```
Our loyalty program's free gift rewards are usually in the form of redeemed coupons or tier privilege so I am afraid that they don't really match your requirements.

I highly recommend checking out BXGY apps such as AOV Free Gifts
```

**Context:** Submitted via TS Elite by huytc@avadagroup.com · ref=crisp:session_de3b6181-e80c-42e8-bae2-38b58634c08b

_session: `session_de3b6181-e80c-42e8-bae2-38b58634c08b`_

### 7. [referral] — Jade · 07/08 21:20

**Q:** Hi there!
When a customer enters their friend's email to refer them (on the "share your referral link" page), does Joy send that email to Klaviyo as a trigger/event I can use?

I want to build a Klaviyo flow that emails the friend directly with their personal referral link instead of relying on the referrer to share it manually.
Is there an event I can hook into for this, and does it include the …

**Bot trả (sai/thiếu):**

```
When the referrer enters their friend's email, Joy automatically sends the invitation email to that friend, containing the referrer's name, the reward, and their personal referral link.
```

**CS sửa thành:**

```
When the referrer enters their friend's email, Joy automatically sends the invitation email to that friend, containing the referrer's name, the reward, and a referral link to start shopping.
```

**Context:** Submitted via TS Elite by phuongnt01@avadagroup.com · ref=crisp:session_e6a1c45f-05b7-42f7-ab20-a6207bd9e736

_session: `session_e6a1c45f-05b7-42f7-ab20-a6207bd9e736`_

### 8. [integration] — Jade · 08/08 12:11

**Q:** Hi! I'm trying to lower my Shopify app spending limit for JOY Loyalty. Shopify currently shows my spending limit as $9,901 USD, with $0 spent, but it won't allow me to reduce it to $200 or another lower amount.

Could you please reset/lower my Shopify app spending limit to $200 USD? Thank you!

**Bot trả (sai/thiếu):**

```
Since it's not adjustable from our app, you'd need to reach out to Shopify Support directly to get that limit lowered or reset.
```

**CS sửa thành:**

```
Since it's not adjustable from our app, you'd need to reach out to Shopify Support directly to get further support. 

For further details on the App spending limits, you can refer to this documentation: https://help.shopify.com/en/manual/your-account/manage-billing/billing-charges/types-of-charges/third-party-charges/app-charges#app-usage-charges
```

**Context:** Submitted via TS Elite by phuongnt01@avadagroup.com · ref=crisp:session_ff46c2f9-f9f0-4080-bb2d-9c5b99c54306

_session: `session_ff46c2f9-f9f0-4080-bb2d-9c5b99c54306`_

### 9. [khác] — Alyssa · 09/08 07:49

**Q:** 獲得されたポイントはお客様はどのように使えるのでしょうか。会員様は決済時にポイントをご確認いただけるのでしょうか。

**Bot trả (sai/thiếu):**

```
また「決済時にポイントを確認・利用」も可能です。各プログラムの「Redeem at checkout page」を有効にすると、ウィジェットを開かなくても決済画面で直接ポイントを割引に変換できます。
```

**CS sửa thành:**

```
Also, members can check and use their points right at checkout. If you enable "Redeem at checkout page" for each program, customers can convert their points into a discount directly on the checkout page without opening the widget.

Please be informed that this function is only available when you use Shopify Plus and the Ultilmate plan of our app.
```

**Context:** Submitted via TS Elite by lypk@avadagroup.com · ref=crisp:session_0da8b77e-cbee-4aeb-9ed7-aaf4926681e0

_session: `session_0da8b77e-cbee-4aeb-9ed7-aaf4926681e0`_

### 10. [referral] — Jade · 09/08 12:15

**Q:** need to turn off joy referral tag

**Bot trả (sai/thiếu):**

```
I don't see a direct toggle to turn off the referral order tag in what I have access to, let me check this with our team so I can give you the exact setting.
```

**CS sửa thành:**

```
You will go to the Reward programs > Referrals > Advanced settings > Shopify order tagging and attribution > Untick the "Order tags" option > Save
```

**Context:** Submitted via TS Elite by phuongnt01@avadagroup.com · ref=crisp:session_12d0459c-b42f-4bda-a106-c4de61b0c112

_session: `session_12d0459c-b42f-4bda-a106-c4de61b0c112`_

### 11. [loyalty page/widget] — Sonny · 10/08 09:42

**Q:** I would like users to be able to complete the actions themselves directly on the loyalty page.

**Bot trả (sai/thiếu):**

```
Go to Joy Admin → On-site content → Loyalty page, then add or enable the redeem rewards block, customers will be able to browse and redeem inline right there.
```

**CS sửa thành:**

```
Go to the theme editor > create a loyalty page template if you haven't had one > add the Ways to Redeem block
```

**Context:** Submitted via TS Elite by huytc@avadagroup.com · ref=crisp:session_45746736-f758-4466-8c3a-f5d4363db003

_session: `session_45746736-f758-4466-8c3a-f5d4363db003`_

### 12. [khác] — Alyssa · 10/08 13:22

**Q:** 评论应用不可用

**Bot trả (sai/thiếu):**

```
能具体说一下是哪里显示"评论应用不可用"吗？比如是在Joy后台的哪个设置页面，或者是评论积分没有正常生效？
```

**CS sửa thành:**

```
Do you mean that the review app you are using is unavailable in the setting list of the Write Reviews program? If so, could you tell me which app you are looking for?
```

**Context:** Submitted via TS Elite by lypk@avadagroup.com · ref=crisp:session_cb7f0b84-9274-4d06-8d75-8f539a19c1e8

_session: `session_cb7f0b84-9274-4d06-8d75-8f539a19c1e8`_

### 13. [points/earning] — Jade · 10/08 13:22

**Q:** Can we setup the amount of points the different vip tiers earn? example: vip1= 1 point per $ spent. vip2:= 1.5 points per $ spent. VIP3= 2 point per $ spent.

**Bot trả (sai/thiếu):**

```
Go to Joy Admin → Reward programs → Earning programs → Place an order, then under "Who to reward" select "Only customers in a VIP tier can earn points". You'll get one rate field per tier, so you can enter 1, 1.5, and 2 points per $ for VIP1, VIP2, VIP3.
```

**CS sửa thành:**

```
Go to Joy Admin → Reward programs → Earning programs → Place an order, then under "Who to reward" select "Only customers in a VIP tier can earn points". You'll get one rate field per tier, so you can enter 1, 1.5, and 2 points per $ for VIP1, VIP2, VIP3.

However, to set up decimal reward values, you need to upgrade the Reward program to the Rule Engine mechanism (available on the Advanced and Ultimate plans only)
```

**Context:** Submitted via TS Elite by phuongnt01@avadagroup.com · ref=crisp:session_c8512d52-8ba1-402c-988e-c66e00aa1200

_session: `session_c8512d52-8ba1-402c-988e-c66e00aa1200`_

### 14. [khác] — Jade · 11/08 04:28

**Q:** yes

**Bot trả (sai/thiếu):**

```
Great! Let's start with setting up VIP tiers tied to a subscription membership.
```

**CS sửa thành:**

```
May I ask if you would like to set up a program to grant a reward to subscription orders or a VIP tied to a subscription membership?
```

**Context:** Submitted via TS Elite by phuongnt01@avadagroup.com · ref=crisp:session_db3286db-9a88-480a-8ffa-6464aaed7798

_session: `session_db3286db-9a88-480a-8ffa-6464aaed7798`_

### 15. [setup/config] — Alyssa · 11/08 10:10

**Q:** Bạn ơi, bên app mình đang không configure với Klaviyo, vậy mình đang gửi email qua nền tảng nào vậy ạ

**Bot trả (sai/thiếu):**

```
Nếu Klaviyo chưa được kết nối, các email thông báo của chương trình loyalty (chào mừng, cộng điểm, đổi thưởng...) sẽ được gửi qua Joy default sender — hệ thống email tích hợp sẵn của Joy, không qua Klaviyo.

Bạn có thể kiểm tra và tùy chỉnh người gửi tại Joy Admin → Settings → Email nhé.
```

**CS sửa thành:**

```
Bọn mình có integrate với Klaviyo đó ạ. Bạn vào phần Integrations > Tìm Klaviyo là sẽ thấy phần connect với Klaviyo. Sau khi connect xong, bạn có thể sync Joy data sang Klaviyo và set up flow ở Klaviyo để gửi email bằng trigger từ Joy nữa ạ.
```

**Context:** Submitted via TS Elite by lypk@avadagroup.com · ref=crisp:session_ea121b06-cd1f-4fc9-8544-f5935132a78d

_session: `session_ea121b06-cd1f-4fc9-8544-f5935132a78d`_

### 16. [pricing/plan] — Jade · 11/08 21:44

**Q:** Hello Alyssa, I plan to subscribe to the AOV.ai cart drawer and AOV.ai Free Gift plans. I would like to ask you for a discount if I purchase both annual subscriptions. Best regards, Pierre
[Image: https://cdn.shopify.com/s/files/1/0728/8602/6462/files/aov-free-gift-and-buy-x-get-y__general__og-default.jpg?v=1785984781 /images/components/base/BaseFlag/fr.png]

**Bot trả (sai/thiếu):**

```
A request for a discount on annual subscriptions must be approved by our sales team. I am forwarding your request; they will get back to you shortly.
```

**CS sửa thành:**

```
Thank you so much for your consideration. However, for the request related to the AOV.ai cart drawer and AOV.ai Free Gift apps, we unfortunately cannot provide you with a confirmation here.

We would recommend contacting AOV's support team so they can help you with the discount offer.
```

**Context:** Submitted via TS Elite by phuongnt01@avadagroup.com · ref=crisp:session_d47f3bc9-2655-418d-b808-e6eee8bd0fb8
