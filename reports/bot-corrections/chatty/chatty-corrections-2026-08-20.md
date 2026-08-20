# Bot Corrections — Ivy (Chatty)

**Tuần:** 19/08/2026 → 20/08/2026  ·  **Tổng correction:** 4

> Đây là các câu bot trả bị CS sửa trong tuần. Dùng để update KB/training data cho bot.

## 📌 Tóm tắt theo topic

### chat/inbox — 2 câu
- chat di chatty itu disimpan dimana ya?
- [Image: https://storage.crisp.chat/users/upload-1/session/-/d/0/8/7/d087f1e68f1e7000/image_1loe5y2.png]

### points/earning — 1 câu
- Can the AI agent actually use Shopify customer tags when generating responses? For example, if a customer is tagged as “VIP” or “Wholesale,…

### khác — 1 câu
- 最多添加几个

**Người sửa:** Jade (4)

---

## 📋 Chi tiết từng correction

### 1. [chat/inbox] — Jade · 19/08 15:02

**Q:** chat di chatty itu disimpan dimana ya?

**Bot trả (sai/thiếu):**

```
Percakapan chat bisa kamu lihat langsung di dalam Chatty, di menu Inbox. Kalau ada gambar atau file yang dikirim pelanggan saat chat, itu tersimpan di Shopify Files (Shopify Admin → Content → Files) karena store kamu masih di plan Free.
```

**CS sửa thành:**

```
You can view your chat conversations directly inside Chatty, in the Inbox menu.
```

**Context:** Submitted via TS Elite by phuongnt01@avadagroup.com · ref=crisp:session_461178aa-1392-4655-964d-1ec9f5666b05

_session: `session_461178aa-1392-4655-964d-1ec9f5666b05`_

### 2. [points/earning] — Jade · 19/08 19:53

**Q:** Can the AI agent actually use Shopify customer tags when generating responses? For example, if a customer is tagged as “VIP” or “Wholesale,” can it recognize the tag and adjust its response accordingly?

**Bot trả (sai/thiếu):**

```
That's a great question, tag-based personalization isn't something the AI agent currently reads automatically. Its data sources are focused on products, discounts, markets, FAQs, and policies, not individual customer tags like "VIP" or "Wholesale".
```

**CS sửa thành:**

```
Yes, when a customer is logged in to your store, the AI agent automatically picks up their Shopify customer tags as part of its system context. So you can absolutely set up rules for this using General Instructions or Custom Scenarios under AI agent → Instructions → Manage.

For example, you could add an instruction like: "If the customer has the tag VIP, then [respond/offer accordingly]" and the AI will follow that logic whenever it detects the tag on a logged-in customer.
```

**Context:** Submitted via TS Elite by phuongnt01@avadagroup.com · ref=crisp:session_04ea6970-0c29-402e-bfc0-71e642009fd5

_session: `session_04ea6970-0c29-402e-bfc0-71e642009fd5`_

### 3. [chat/inbox] — Jade · 20/08 12:33

**Q:** [Image: https://storage.crisp.chat/users/upload-1/session/-/d/0/8/7/d087f1e68f1e7000/image_1loe5y2.png]

**Bot trả (sai/thiếu):**

```
这三个类型的具体判定标准目前手头的资料没有明确说明，我需要跟团队确认一下再给您准确的解释。
```

**CS sửa thành:**

```
These are the contact types in Chatty's Contacts list.  

Customer: A visitor who has a Shopify account or has purchased from your store before. Chatty can match them to your Shopify customer records.

Lead: A visitor who shared their email (such as through the pre-chat form) but hasn't made a purchase or created a Shopify account yet.

Anonymous: A visitor who hasn't shared any information via the live chat. Chatty assigns them a random name.
```

**Context:** Submitted via TS Elite by phuongnt01@avadagroup.com · ref=crisp:session_8f74094c-ae64-472a-b34c-be93ceadf178

_session: `session_8f74094c-ae64-472a-b34c-be93ceadf178`_

### 4. [khác] — Jade · 20/08 13:19

**Q:** 最多添加几个

**Bot trả (sai/thiếu):**

```
Chatty本身只能连接1个转发邮箱哦
```

**CS sửa thành:**

```
You can connect multiple emails to Chatty on the Basic plan
```

**Context:** Submitted via TS Elite by phuongnt01@avadagroup.com · ref=crisp:session_e6718968-69b2-4f87-8d9d-cf440f22f442

_session: `session_e6718968-69b2-4f87-8d9d-cf440f22f442`_
