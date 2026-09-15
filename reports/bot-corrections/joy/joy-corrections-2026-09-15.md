# Bot Corrections — Joyce (Joy)

**Tuần:** 14/09/2026 → 15/09/2026  ·  **Tổng correction:** 2

> Đây là các câu bot trả bị CS sửa trong tuần. Dùng để update KB/training data cho bot.

## 📌 Tóm tắt theo topic

### khác — 1 câu
- hello i will find it that was a few weeks ago

### chat/inbox — 1 câu
- [Image: https://storage.crisp.chat/users/upload-1/session/-/6/7/8/c/678c854a3e6c5800/image_13frsu2.png]

**Người sửa:** Jade (1), Liz (1)

---

## 📋 Chi tiết từng correction

### 1. [khác] — Jade · 15/09 05:52

**Q:** hello i will find it that was a few weeks ago

**Bot trả (sai/thiếu):**

```
Hi! I'm Joyce, your AI assistant! How can I help?
```

**CS sửa thành:**

```
Hi! I'm Joyce, your AI assistant! 

Thank you for your cooperation, and feel free to share the link with us once you find it.
```

**Context:** Submitted via TS Elite by phuongnt01@avadagroup.com · ref=crisp:session_c077d7ce-a47f-4f67-be1f-1d1482e010c7

_session: `session_c077d7ce-a47f-4f67-be1f-1d1482e010c7`_

### 2. [chat/inbox] — Liz · 15/09 08:51

**Q:** [Image: https://storage.crisp.chat/users/upload-1/session/-/6/7/8/c/678c854a3e6c5800/image_13frsu2.png]

**Bot trả (sai/thiếu):**

```
Thanks for flagging this! Once a reward is redeemed, the code generated becomes a standard Shopify discount code, so it can be applied at checkout regardless of whether the customer is logged in, the same as any other coupon code.
```

**CS sửa thành:**

```
Your reward settings actually have two restrictions in place: "Who can use discount" is set to only the customer who redeemed, so the code is meant to work only for the account that spent the points on it, and "Limit number of times each code can be used in total" is set to 1, so once it's used it stops working entirely.

As for why the code still applied while you were logged out: Shopify only checks who the customer is once an email is entered or they log in at checkout. Before that point, the discount can still show on the order summary, which is what you saw in your screenshot. Once a checkout email is entered that doesn't match the customer who redeemed the code, Shopify removes the discount and the order can't go through with it, so a shared code won't actually work for someone else.
```

**Context:** Submitted via TS Elite by lyht@avada.io · ref=crisp:session_0c84871d-0b0c-4e52-83ba-0175da1845fc

_session: `session_0c84871d-0b0c-4e52-83ba-0175da1845fc`_
