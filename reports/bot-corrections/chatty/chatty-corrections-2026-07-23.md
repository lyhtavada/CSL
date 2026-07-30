# Bot Corrections — Ivy (Chatty)

**Tuần:** 23/07/2026 → 29/07/2026  ·  **Tổng correction:** 16

> Đây là các câu bot trả bị CS sửa trong tuần. Dùng để update KB/training data cho bot.

## 📌 Tóm tắt theo topic

### khác — 8 câu
- how long delivery take
- 怎么设置自动回复 不要求用户一开始提交邮箱？
- Hello I am trying to find a conversation I have had with a customer. But its really hard to find. Can you help me out?
- … +5 câu khác (xem chi tiết bên dưới)

### integration — 3 câu
- Alright! Is it possible to make these chats in the future be connected to the orders numbers or maybe a mail or something to verficate the …
- for order messages, it keeps asking for email address and order number, i want to get them to submit a contact us form. what do i do
- could you email me a transcript of our chat please?

### chat/inbox — 2 câu
- why is my AI agent not using the identity that i gave it
- [AI Feedback] Bot message: I'm sorry, but I do not have information on that topic. Feedback: our masturbator are available here: https://go…

### points/earning — 1 câu
- it says 200 of 920 products learned do I need to click anything to make it learn more?

### loyalty page/widget — 1 câu
- so when i test my chat in the theme, it has different responses to the test AI whyu

### pricing/plan — 1 câu
- with which plan i can add chatty to whats app

**Người sửa:** Andy (9), Phoebe (5), Cody (1), Alicia (1)

---

## 📋 Chi tiết từng correction

### 1. [integration] — Cody · 23/07 00:15

**Q:** Alright! Is it possible to make these chats in the future be connected to the orders numbers or maybe a mail or something to verficate the customer chatting?

**Bot trả (sai/thiếu):**

```
Yes, you can require email (and optionally name/phone) upfront by turning on the pre-chat form under Chatbox → General → Live chat → Edit.

That way every chat gets tied to a customer's email from the start, making it much easier to search and match to their orders later.
```

**CS sửa thành:**

```
Yes, you can require email (and optionally name/phone) upfront by turning on the pre-chat form under Chatbox > Chat page > Pre-chat form
```

**Context:** Submitted via TS Elite by chauhm@avadagroup.com · ref=crisp:session_04112ece-931e-4124-a2f5-516a1c46daec

_session: `session_04112ece-931e-4124-a2f5-516a1c46daec`_

### 2. [khác] — Andy · 23/07 08:17

**Q:** how long delivery take

**Bot trả (sai/thiếu):**

```
Just to recap, delivery time itself isn't something Chatty calculates, Order Tracking shows shipment status instead (Confirmed, On its way, Delivered), updated based on your carrier.

Anything specific about setting this up or how it appears for your customers that I can help with?
```

**CS sửa thành:**

```
Khách đang hỏi để kiểm tra xem AI agent trả lời như thế nào. Cần phải hỏi lại khách xem có phải khách muốn test AI agent không?
```

**Context:** Submitted via TS Elite by anhbd@avadagroup.com · ref=crisp:session_e2a33f9d-437b-4e43-a9e3-dad4e97f3168

_session: `session_e2a33f9d-437b-4e43-a9e3-dad4e97f3168`_

### 3. [khác] — Andy · 23/07 09:44

**Q:** 怎么设置自动回复 不要求用户一开始提交邮箱？

**Bot trả (sai/thiếu):**

```
可以通过开启 AI Product Page Assistant 或 Proactive Chat 来实现，这两个功能都可以让客户不用先填邮箱就直接和 AI 对话。
具体去 AI agent 里把 Product Page Assistant 嵌入到商品页，或者开启 Proactive Chat 功能即可～需要我教你哪个的具体开启步骤吗？
```

**CS sửa thành:**

```
Giới thiệu về pre-chat form và hướng dẫn khách chọn chat as anonymous
```

**Context:** Submitted via TS Elite by anhbd@avadagroup.com · ref=crisp:session_05f5844c-db03-401e-a7dc-0dd892e061cc

_session: `session_05f5844c-db03-401e-a7dc-0dd892e061cc`_

### 4. [integration] — Andy · 23/07 11:45

**Q:** for order messages, it keeps asking for email address and order number, i want to get them to submit a contact us form. what do i do

**Bot trả (sai/thiếu):**

```
To have order-related questions go to a contact form instead of the AI asking for email/order number, head to AI agent → Instructions → Manage → Assistant skills → Customer support skills → Human handover.

Under "Where does the customer go?", select Show contact methods - this way, instead of collecting info, the AI will show your configured contact options (including your contact form) for the customer to reach out through.
```

**CS sửa thành:**

```
Order-related questions thì phải hướng dẫn khách set up ở After-sales support chứ.
```

**Context:** Submitted via TS Elite by anhbd@avadagroup.com · ref=crisp:session_5f5e94d3-319b-4a7e-bd95-5b651292bc96

_session: `session_5f5e94d3-319b-4a7e-bd95-5b651292bc96`_

### 5. [khác] — Phoebe · 23/07 20:04

**Q:** Hello I am trying to find a conversation I have had with a customer. But its really hard to find. Can you help me out?

**Bot trả (sai/thiếu):**

```
Also make sure to check all the tabs (All, Unread, Resolved, Mine) and clear any filters, since it might just be sitting in Resolved.
```

**CS sửa thành:**

```
Mention the correct name of tabs: All, Your Inbox, Unassigned, Blocked
```

**Context:** Submitted via TS Elite by phuongttm.ctv@avadagroup.com · ref=crisp:session_04112ece-931e-4124-a2f5-516a1c46daec

_session: `session_04112ece-931e-4124-a2f5-516a1c46daec`_

### 6. [khác] — Phoebe · 23/07 21:08

**Q:** Bonjour, où puis-je mettre un statut vacances SVP?

**Bot trả (sai/thiếu):**

```
Bonjour ! Pour mettre un statut "vacances", vous pouvez utiliser la fonction Holiday dans les Online Hours.

Allez dans Settings → Online Hours → Holidays, puis ajoutez une plage de dates pour vos vacances.
```

**CS sửa thành:**

```
Settings -> Chat availability -> Manage -> Working hours > Holiday
```

**Context:** Submitted via TS Elite by phuongttm.ctv@avadagroup.com · ref=crisp:session_e3f852e7-9326-4cf2-baab-0b301a3f69b0

_session: `session_e3f852e7-9326-4cf2-baab-0b301a3f69b0`_

### 7. [points/earning] — Andy · 25/07 18:03

**Q:** it says
200 of 920 products learned
do I need to click anything to make it learn more?

**Bot trả (sai/thiếu):**

```
That count updates automatically as products sync, no need to click anything.

If it's been a while and it's still stuck at 200 of 920, go to AI agent → Training data → Products → Manage → Sync products to trigger a manual resync.
```

**CS sửa thành:**

```
Hướng dẫn khách active thêm products để AI học
```

**Context:** Submitted via TS Elite by anhbd@avadagroup.com · ref=crisp:session_cefa0af9-d403-4582-894f-4bbe543bf790

_session: `session_cefa0af9-d403-4582-894f-4bbe543bf790`_

### 8. [khác] — Andy · 25/07 18:09

**Q:** but that means we cannot test it until it's live to the public, I think

**Bot trả (sai/thiếu):**

```
That's a fair point, testing on the market domain would mean the widget is visible there too.

I don't have a workaround in my documentation for testing a market's language/currency without it being live. Let me check with our team on this and get back to you.
```

**CS sửa thành:**

```
Hướng dẫn khách test thử trên draft theme
```

**Context:** Submitted via TS Elite by anhbd@avadagroup.com · ref=crisp:session_cefa0af9-d403-4582-894f-4bbe543bf790

_session: `session_cefa0af9-d403-4582-894f-4bbe543bf790`_

### 9. [khác] — Phoebe · 25/07 21:01

**Q:** Where is the setting?

**Bot trả (sai/thiếu):**

```
That setting isn't something you can toggle yourself in the app - it's on our backend, so I'll need to pass this to our team to switch it to a fixed "Anonymous-xxx" format for you.
```

**CS sửa thành:**

```
Settings > Inbox Settings > Anonymous visitor names.
```

**Context:** Submitted via TS Elite by phuongttm.ctv@avadagroup.com · ref=crisp:session_74c6c964-2466-4f2e-b021-a7ebe1e68af4

_session: `session_74c6c964-2466-4f2e-b021-a7ebe1e68af4`_

### 10. [integration] — Andy · 26/07 11:32

**Q:** could you email me a transcript of our chat please?

**Bot trả (sai/thiếu):**

```
You can grab that yourself right from the chatbox, click the three dots menu at the top right and select Email transcript, it'll be sent straight to your email automatically.
```

**CS sửa thành:**

```
gửi transcript của conversation trên Crisp phải là do team tech gửi
```

**Context:** Submitted via TS Elite by anhbd@avadagroup.com · ref=crisp:session_cefa0af9-d403-4582-894f-4bbe543bf790

_session: `session_cefa0af9-d403-4582-894f-4bbe543bf790`_

### 11. [chat/inbox] — Phoebe · 26/07 23:02

**Q:** why is my AI agent not using the identity that i gave it

**Bot trả (sai/thiếu):**

```
Let's check a few things first.

Have you confirmed the Instructions were saved (clicked the save button after editing), and are your data sources still active under AI agent → Training data → Manage?
```

**CS sửa thành:**

```
When customer mentioned AI agent identity, it should be AI agents > Settings
```

**Context:** Submitted via TS Elite by phuongttm.ctv@avadagroup.com · ref=crisp:session_77a5cbd7-16dc-4965-9064-cb5405205a6a

_session: `session_77a5cbd7-16dc-4965-9064-cb5405205a6a`_

### 12. [loyalty page/widget] — Andy · 28/07 09:17

**Q:** so when i test my chat in the theme, it has different responses to the test AI whyu

**Bot trả (sai/thiếu):**

```
That usually happens because a live chat session keeps the knowledge it loaded when it started, so if you opened that chat before making changes, it'll keep answering from the old data.

Try clicking Reset the conversation on your storefront chat, then ask the same question again.

Let me know if it still differs from Test AI after resetting.
```

**CS sửa thành:**

```
hỏi xin thêm thông tin xem khách hỏi test bằng câu hỏi gì trước
```

**Context:** Submitted via TS Elite by anhbd@avadagroup.com · ref=crisp:session_5f5e94d3-319b-4a7e-bd95-5b651292bc96

_session: `session_5f5e94d3-319b-4a7e-bd95-5b651292bc96`_

### 13. [khác] — Phoebe · 28/07 16:28

**Q:** 可以设置客户留了邮箱之后才能发送消息吗

**Bot trả (sai/thiếu):**

```
这个功能目前在我们的资料里没有看到明确的设置项（比如强制客户必须先留邮箱才能发消息）。

方便的话我先跟团队确认一下这个是否可以设置，再回复您哈。
```

**CS sửa thành:**

```
Chatbox > Chat Page > scroll to Pre-chat form to select email required field before sending a message
```

**Context:** Submitted via TS Elite by phuongttm.ctv@avadagroup.com · ref=crisp:session_8c1964e5-bbec-4636-a7d2-91d2d0567a5b

_session: `session_8c1964e5-bbec-4636-a7d2-91d2d0567a5b`_

### 14. [pricing/plan] — Andy · 28/07 20:12

**Q:** with which plan i can add chatty to whats app

**Bot trả (sai/thiếu):**

```
Hi there! To connect Chatty to WhatsApp, you'll need the Pro plan or higher.
```

**CS sửa thành:**

```
Connect WhatsApp to Chatty available for Free plan and above
```

**Context:** Submitted via TS Elite by anhbd@avadagroup.com · ref=crisp:session_ecd4fbef-17e7-4f48-8013-13ac74956eb2

_session: `session_ecd4fbef-17e7-4f48-8013-13ac74956eb2`_

### 15. [khác] — Alicia · 29/07 02:53

**Q:** we use gmail

**Bot trả (sai/thiếu):**

```
Thanks for sharing that screenshot, the notification email settings look correctly set up (sales@racinghalloffamecollection.com verified, with CC to another address).
Since test emails work but real customer message notifications aren't coming through even after checking spam, this looks like it needs a closer look from our team. Let me get this escalated for you.
```

**CS sửa thành:**

```
Thanks for sharing that screenshot. As I see here, the notifications are automatically sent to sales@racinghalloffamecollection.com but you want to receive notification via info@racinghalloffamecollection.com. Would you like to change to the second email? If you want to change, you can simply replace the first email with the second one and complete the verification process. Otherwise, you can also add the second one in the CC under it.
```

**Context:** Submitted via TS Elite by anhln.ctv@avadagroup.com · ref=crisp:session_90ec4650-3c2e-4dc8-b64e-1d6710df7575

_session: `session_90ec4650-3c2e-4dc8-b64e-1d6710df7575`_

### 16. [chat/inbox] — Andy · 29/07 14:05

**Q:** [AI Feedback]
Bot message: I'm sorry, but I do not have information on that topic.
Feedback: our masturbator are available here: https://goliate.com/collections/masturbateurs
ConvoId: YeEkqrUvBynvvduKnxXk
MessageId: a41065a7-cb91-4bf3-9d36-5bfe4bf66ac0
[Image: http://goliate.com/cdn/shop/collections/masturbateur_vibrant_silicone_homme_mon_amour_2-min.webp?v=1770809496]

**Bot trả (sai/thiếu):**

```
To help the AI answer this correctly going forward, you can add that collection page as a training source: go to AI agent → Training data → Add data source, then paste in that URL so it gets crawled and included in the AI's knowledge.
```

**CS sửa thành:**

```
không cần phải add collection URL vào data source, hướng dẫn khách check xem collection data đã được sync và enable chưa?
```

**Context:** Submitted via TS Elite by anhbd@avadagroup.com · ref=crisp:session_2c9e9beb-1b2f-477a-a84c-10846081cc3a

_session: `session_2c9e9beb-1b2f-477a-a84c-10846081cc3a`_
