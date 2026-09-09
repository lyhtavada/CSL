# Bot Corrections — Ivy (Chatty)

**Tuần:** 08/09/2026 → 09/09/2026  ·  **Tổng correction:** 4

> Đây là các câu bot trả bị CS sửa trong tuần. Dùng để update KB/training data cho bot.

## 📌 Tóm tắt theo topic

### khác — 2 câu
- give me boundaries for the ai
- which is not exist

### pricing/plan — 1 câu
- Hi I will look into later. we have around over 2500+ products on our catalogue. What will be the best plan to train the AI agent for the be…

### chat/inbox — 1 câu
- https://help.chatty.net/live-chat/channels/whatsapp/ the steps should be like this right

**Người sửa:** Jade (2), Andy (2)

---

## 📋 Chi tiết từng correction

### 1. [pricing/plan] — Jade · 08/09 20:30

**Q:** Hi I will look into later. we have around over 2500+ products on our catalogue. What will be the best plan to train the AI agent for the better recommendation and customer service?

**Bot trả (sai/thiếu):**

```
Pro also unlocks Smart product recommendations, which is exactly what you need for better product discovery, plus CSAT surveys and Cart booster for stronger customer service.
```

**CS sửa thành:**

```
Pro also unlocks Custom recommendations (under the Smart product recommendations skill), which is exactly what you need for better product discovery, plus CSAT surveys and Cart booster for stronger customer service.
```

**Context:** Submitted via TS Elite by phuongnt01@avadagroup.com · ref=crisp:session_fc14315a-81a4-4fdb-97f7-f81cb4b41cbd

_session: `session_fc14315a-81a4-4fdb-97f7-f81cb4b41cbd`_

### 2. [khác] — Jade · 08/09 23:13

**Q:** give me boundaries for the ai

**Bot trả (sai/thiếu):**

```
You can set boundaries under AI agent → Instructions → General instructions → Behaviours — that's where you define what the AI should avoid discussing (like pricing exceptions or refunds) and how it should redirect those topics.
```

**CS sửa thành:**

```
You can set boundaries under AI agent → Instructions → General instructions → Boundaries  — that's where you define what the AI should avoid discussing (like pricing exceptions or refunds) and how it should redirect those topics.
```

**Context:** Submitted via TS Elite by phuongnt01@avadagroup.com · ref=crisp:session_bac593df-c16b-4a79-97cc-30ed06bfc14c

_session: `session_bac593df-c16b-4a79-97cc-30ed06bfc14c`_

### 3. [khác] — Andy · 09/09 08:30

**Q:** which is not exist

**Bot trả (sai/thiếu):**

```
Got it — since that address doesn't exist, we just need to swap it for the correct one.
```

**CS sửa thành:**

```
Khách không tự đổi được. Cần CS hỗ trợ đổi
```

**Context:** Submitted via TS Elite by anhbd@avadagroup.com · ref=crisp:session_ff4393cb-80a6-407f-99bf-4057af40e6b6

_session: `session_ff4393cb-80a6-407f-99bf-4057af40e6b6`_

### 4. [chat/inbox] — Andy · 09/09 09:04

**Q:** https://help.chatty.net/live-chat/channels/whatsapp/ the steps should be like this right

**Bot trả (sai/thiếu):**

```
I can't confirm that article reflects the current steps, the WhatsApp connection flow changed recently and the old walkthrough may not match anymore.
```

**CS sửa thành:**

```
Step 1: Backup & Preparation: before starting, remember that chat history does not migrate from the app to the API.

Export Chats: Manually export important conversations.
Meta Business Manager: Have your Meta Business Manager ready.
Payment Method: Link a Credit/Debit card in Meta for conversation billing.


Step 2: Delete the Mobile WhatsApp Account: the number must be completely "free" before it can join the API.

Open the WhatsApp Business App on your phone.
Go to Settings > Account > Delete My Account.
Note: You must delete the account, not just uninstall the app.

Step 3: Create a WhatsApp Business Account (WABA)

Go to Meta Business Suite > Business Settings.
Navigate to Accounts > WhatsApp Accounts.
Click Add > Create a new WhatsApp Business Account.
Fill in your Business Profile (Display Name, Category, and Website).


Step 4: Verify Your Phone Number (OTP)

Enter your phone number into the Meta setup.
Choose SMS or Voice Call to receive the code.
Enter the 6-digit OTP code to verify ownership of the number.


Step 5: Enable Two-Step Verification (2FA): Meta requires this extra layer of security for API accounts.

In Business Settings, go to WhatsApp Accounts and select y…
```

**Context:** Submitted via TS Elite by anhbd@avadagroup.com · ref=crisp:session_e9cc85b9-2220-4bb5-abbf-977cca2e4967

_session: `session_e9cc85b9-2220-4bb5-abbf-977cca2e4967`_
