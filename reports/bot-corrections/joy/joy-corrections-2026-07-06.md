# Bot Corrections — Joyce (Joy)

**Tuần:** 06/07/2026 → 12/07/2026  ·  **Tổng correction:** 8

> Đây là các câu bot trả bị CS sửa trong tuần. Dùng để update KB/training data cho bot.

## 📌 Tóm tắt theo topic

### khác — 3 câu
- 没有找到，能提供截图吗
- hi, where can i locate the “Birthday field name in register form” setting?
- A customer reported it to me and I just confirmed it

### chat/inbox — 2 câu
- [Image: https://storage.crisp.chat/users/upload-1/session/-/1/f/f/d/1ffd30e532a0c800/screenshot-2026-07-07-at-15004_1jqnnp0.png]
- [Image: https://storage.crisp.chat/users/upload-1/session/-/3/5/0/8/350844b6e37bcc00/image_xr4kol.png]

### points/earning — 2 câu
- Can't I customize the little icons for the ways to earn points?
- Hey, on our product pages my coworker (on PC) have this link under the text that shows how many points you get when buying a product, I can…

### referral — 1 câu
- Hi! Could you help me look into the customer mandee.garciax3@gmail.com? She said she sent $30 but didn't get the $30 promotion. From her ac…

**Người sửa:** Sonny (2), Alyssa (2), Jade (1), Audrey (1), Liz (1), Cody (1)

---

## 📋 Chi tiết từng correction

### 1. [referral] — Jade · 07/07 08:15

**Q:** Hi! Could you help me look into the customer mandee.garciax3@gmail.com? She said she sent $30 but didn't get the $30 promotion. From her account it looks like her referral code hasn't been used yet. Would this be why she didn't receive her promotion?

**Bot trả (sai/thiếu):**

```
Yes, that's exactly why. Based on the referral flow, the referrer only gets their reward once the referee places an order using the referral link or code.
Since her referral code hasn't been used yet, the $30 reward hasn't been triggered. She'll receive it once her referred friend clicks her link, enters their email to claim the discount, and completes a purchase with that same email.
```

**CS sửa thành:**

```
Based on the current logic, the referrer will receive their reward only after the referred customer places an order using the same email address that was used to claim the referral reward.

Please note that using the promotion itself is optional. The referred customer does not have to apply the promotion code to qualify.

Additionally, referral rewards are issued based on your Order status setting. The reward is granted once the referred order reaches the required status, either Paid or Fulfilled, depending on your current configuration.

Could you please confirm whether the referred customer has already placed an order? If so, could you also let us know the current status of that order? This will help us investigate the issue further.
```

**Context:** Submitted via TS Elite by phuongnt01@avadagroup.com · ref=crisp:session_a7829a80-e854-4402-8c83-0cef98bf4835

_session: `session_a7829a80-e854-4402-8c83-0cef98bf4835`_

### 2. [chat/inbox] — Sonny · 07/07 13:06

**Q:** [Image: https://storage.crisp.chat/users/upload-1/session/-/1/f/f/d/1ffd30e532a0c800/screenshot-2026-07-07-at-15004_1jqnnp0.png]

**Bot trả (sai/thiếu):**

```
Hi there, I'm Joyce, your AI agent from Joy. 😊

From your screenshot, I can see the cart drawer is showing the points earning info and the redeem button. To turn this off, go to:

Joy Admin → On-site content → Cart drawer

From there you can disable the cart drawer feature entirely. Alternatively, if you only want to remove the redeem button specifically, you can go to your Theme Editor and disable the Joy: Redeem in line app embed.

Which part would you like to hide — the full cart drawer block, or just the redemption button?
```

**CS sửa thành:**

```
Hi there, I'm Joyce, your AI agent from Joy. 😊

From your screenshot, I can see the cart drawer is showing the points earning info and the redeem button. To turn this off, go to:

If you want to remove that redeem inline specifically, you can go to your Theme Editor and disable the Joy: Redeem in line app embed.
```

**Context:** Submitted via TS Elite by huytc@avadagroup.com · ref=crisp:session_0c252fe9-1f8d-4c3c-adf3-3d867119d882

_session: `session_0c252fe9-1f8d-4c3c-adf3-3d867119d882`_

### 3. [points/earning] — Audrey · 07/07 13:46

**Q:** Can't I customize the little icons for the ways to earn points?

**Bot trả (sai/thiếu):**

```
Yes, you can! Go to Joy Admin → Reward programs → [select an earning program] → Set up → AI icon, enter a prompt, and regenerate until you get an icon that matches your brand.

You can do this for each earning and redeeming program individually.
```

**CS sửa thành:**

```
To edit the icons for the widget: Go to Joy Admin > On-site Content > Loyalty widget > Set up the Widget > Choose "Section" > Ways to earn > Customize programs and change the icons.

To edit the icons on the loyalty page: Go to Joy Admin > On-site Content > Loyalty page > Edit "Ways to earn" block > Click on each program to upload the custom icon URLs
```

**Context:** Submitted via TS Elite by vanct@avadagroup.com · ref=crisp:session_ba861373-81a1-4801-9720-c3d14a09f722

_session: `session_ba861373-81a1-4801-9720-c3d14a09f722`_

### 4. [khác] — Liz · 08/07 12:02

**Q:** 没有找到，能提供截图吗

**Bot trả (sai/thiếu):**

```
你可以按这个路径找到：

Joy Admin → On-site content → Widget → Widget design → Unified widget → Setup → Content & Translations

展开 "Referral" 部分，里面有描述文字可以编辑，加上好友能获得的奖励信息就可以了。

这里有一张参考截图：https://avada-image.pages.dev/i/wGqV6gW6C

找到了吗？
```

**CS sửa thành:**

```
tự lấy và gửi sai link screenshot
```

**Context:** Submitted via TS Elite by lyht@avada.io · ref=crisp:session_2bd4af08-014a-4cf9-b592-94bc44c8a623

_session: `session_2bd4af08-014a-4cf9-b592-94bc44c8a623`_

### 5. [points/earning] — Alyssa · 08/07 19:59

**Q:** Hey, on our product pages my coworker (on PC) have this link under the text that shows how many points you get when buying a product, I can't see the text on mac. Is this a known issue, or how can we hide this?

**Bot trả (sai/thiếu):**

```
Thanks for the screenshots! That "Follow med oss för att ta emot" link under the point calculator text is the Product Referral widget - it's not a bug on Mac, it's likely just a display difference (font/CSS rendering or a visibility rule) between the two devices.
```

**CS sửa thành:**

```
Thanks for the screenshots! It is the point calculator of our app, which can show how many points customers can earn when they purchase the product.

It isn't restricted to show when you check it on different devices.
```

**Context:** Submitted via TS Elite by lypk@avadagroup.com · ref=crisp:session_aaa3dafb-968d-422e-8976-3d63d55a00c8

_session: `session_aaa3dafb-968d-422e-8976-3d63d55a00c8`_

### 6. [khác] — Alyssa · 09/07 09:13

**Q:** hi, where can i locate the “Birthday field name in register form” setting?

**Bot trả (sai/thiếu):**

```
You'll find it at Joy Admin → Settings → look for "Birthday field name in register form" — set it to Birthday or whatever field name you're using.
```

**CS sửa thành:**

```
I would like to clarify that the “Birthday field name in register form” setting isn't a built-in function of our app. It means you put a field in the account registration form to maximize the chance of getting customers' birthday information.

You can only set that up if you use the legacy customer account mode of Shopify, which allows users to customize their account registration form.
```

**Context:** Submitted via TS Elite by lypk@avadagroup.com · ref=crisp:session_2cad3a20-33fe-4b93-a76a-2718d54c6b4c

_session: `session_2cad3a20-33fe-4b93-a76a-2718d54c6b4c`_

### 7. [khác] — Cody · 10/07 01:51

**Q:** A customer reported it to me and I just confirmed it

**Bot trả (sai/thiếu):**

```
Thanks for confirming that with your customer. This is already with our team on ticket #7944, so no need to open a new one. I'll keep you posted here as soon as there's an update.
```

**CS sửa thành:**

```
AI báo đã có ticket rồi nhưng thật ra là chưa, issue khách báo là issue mới
```

**Context:** Submitted via TS Elite by chauhm@avadagroup.com · ref=crisp:session_31b98744-f6c7-4d10-9106-451de58e613f

_session: `session_31b98744-f6c7-4d10-9106-451de58e613f`_

### 8. [chat/inbox] — Sonny · 11/07 08:53

**Q:** [Image: https://storage.crisp.chat/users/upload-1/session/-/3/5/0/8/350844b6e37bcc00/image_xr4kol.png]

**Bot trả (sai/thiếu):**

```
These screenshots are really helpful, thank you.
The Design tab is showing the old widget layout (that's the mismatch you saw before), but the live preview on the right and your actual Unified widget both confirm Radiant's card style, icon, and colors are set correctly and match Signature's format. So the setup itself looks fine on your end.
I'll pass these along to our team so they can double check why the Design tab preview differs from the live one.
```

**CS sửa thành:**

```
These screenshots are really helpful, thank you.
The Design tab and the preview on the right are showing the old widget layout (that's the mismatch you saw before) while you are now using the new version of the Unified widget.

So please locate the membership card styling in the On-site content > Unified widget Set up instead.
```

**Context:** Submitted via TS Elite by huytc@avadagroup.com · ref=crisp:session_ba861373-81a1-4801-9720-c3d14a09f722

_session: `session_ba861373-81a1-4801-9720-c3d14a09f722`_
