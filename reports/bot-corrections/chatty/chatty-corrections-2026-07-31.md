# Bot Corrections — Ivy (Chatty)

**Tuần:** 31/07/2026 → 06/08/2026  ·  **Tổng correction:** 17

> Đây là các câu bot trả bị CS sửa trong tuần. Dùng để update KB/training data cho bot.

## 📌 Tóm tắt theo topic

### chat/inbox — 6 câu
- [Image: https://storage.crisp.chat/users/upload-1/session/-/b/3/b/5/b3b57af74ec58000/screenshot-199_1t8jldk.png]
- I don't want a message to appear so that the client sees the chatbot on my site. [Image: /images/components/base/BaseFlag/fr.png]
- [Image: https://storage.crisp.chat/users/upload-1/session/-/5/7/0/d/570d5a0e0aec6800/image_4x7haf.png]
- … +3 câu khác (xem chi tiết bên dưới)

### khác — 4 câu
- Hi Harry,
- Eso puede salir antes de que el cliente escriba en el sitio web. Cuando llega el cliente a WhatsApp algo diferente:  Bienvenid@ , soy Tatia…
- Muchas gracias de verdad por haberme ayudado a configurar la IA
- … +1 câu khác (xem chi tiết bên dưới)

### integration — 3 câu
- Is it possible for button to be add to cart instead of view product?
- we dont want chatty to send me an email every time the customer replies, i just want a transcript at the end of the conversation, how do we…
- we dont want chatty to send me an email every time the customer replies, i just want a transcript at the end of the conversation, how do we…

### setup/config — 2 câu
- Hi Chatty Support Team,  I noticed an issue where Chatty AI is generating inaccurate information when answering customer queries on our sto…
- I need help on setup AI agent

### pricing/plan — 1 câu
- besides，$6999 is our deposit-only price, not MSRP. the answer of chatty ai is also wrong

### referral — 1 câu
- I would prefer Order lookup

**Người sửa:** Phoebe (8), Andy (6), Alicia (1), Cody (1), Jade (1)

---

## 📋 Chi tiết từng correction

### 1. [khác] — Andy · 31/07 06:03

**Q:** Hi Harry,

**Bot trả (sai/thiếu):**

```
Hi there! 😊 Just to update you, our team is still working on Isaac's setup, I'll let you know right here as soon as he's ready for you to test.
```

**CS sửa thành:**

```
Setup done rồi mà, Harry đã báo lại ở bên trên
```

**Context:** Submitted via TS Elite by anhbd@avadagroup.com · ref=crisp:session_8f0ec761-9a41-4c45-8a18-c8d5d89cca0c

_session: `session_8f0ec761-9a41-4c45-8a18-c8d5d89cca0c`_

### 2. [integration] — Alicia · 01/08 01:45

**Q:** Is it possible for button to be add to cart instead of view product?

**Bot trả (sai/thiếu):**

```
Yes, you can customize the CTA button label when setting up the Product recommendation campaign, so it can say "Add to Cart" instead of "View Product."

You'll find this under the Chat message section when editing the campaign.
```

**CS sửa thành:**

```
This CTA is not customizable
```

**Context:** Submitted via TS Elite by anhln.ctv@avadagroup.com · ref=crisp:session_2062bab3-1922-4101-b0bd-e5bd2bf20469

_session: `session_2062bab3-1922-4101-b0bd-e5bd2bf20469`_

### 3. [chat/inbox] — Phoebe · 02/08 21:05

**Q:** [Image: https://storage.crisp.chat/users/upload-1/session/-/b/3/b/5/b3b57af74ec58000/screenshot-199_1t8jldk.png]

**Bot trả (sai/thiếu):**

```
Go to AI agent → Settings → AI identity → Welcome message, then delete the "📌 Pre-order Information" block and save.
```

**CS sửa thành:**

```
click on "Review sources" button on the Inbox to see where the source is and go there to edit
```

**Context:** Submitted via TS Elite by phuongttm.ctv@avadagroup.com · ref=crisp:session_f375512c-ac0f-480a-8db9-4dbacd122b60

_session: `session_f375512c-ac0f-480a-8db9-4dbacd122b60`_

### 4. [chat/inbox] — Cody · 03/08 07:44

**Q:** I don't want a message to appear so that the client sees the chatbot on my site.
[Image: /images/components/base/BaseFlag/fr.png]

**Bot trả (sai/thiếu):**

```
No problem! To prevent an automatic message from appearing and only show the chat icon, go to Chatbox → Proactive Chat and disable the automatic message (toggle off).
```

**CS sửa thành:**

```
Go to Proactive chat and set them as Inactive
```

**Context:** Submitted via TS Elite by chauhm@avadagroup.com · ref=crisp:session_784ba580-8712-465e-8f44-0df2afefb730

_session: `session_784ba580-8712-465e-8f44-0df2afefb730`_

### 5. [setup/config] — Phoebe · 03/08 20:25

**Q:** Hi Chatty Support Team,

I noticed an issue where Chatty AI is generating inaccurate information when answering customer queries on our store.

As shown in the attached screenshot, the AI stated:

"Additionally, the Pro model includes exclusive AI-driven lens contamination detection and AI weld analysis, which are not available on the L1."

This statement is incorrect. These features are actually…

**Bot trả (sai/thiếu):**

```
On the page for the L1 Pro/L1, the rows "AI Lens Contamination Detect" and "AI Weld Analysis & Optimization" are shown as ✓ for L1 Pro but × for L1, so the AI just repeated what's on the page.
```

**CS sửa thành:**

```
AI đọc nhầm nội dung bảng trên trang, X là cho cột 500W Laser Welder https://capture.avada.io/i/EWDE8ky2r79e
```

**Context:** Submitted via TS Elite by phuongttm.ctv@avadagroup.com · ref=crisp:session_7ed75446-feb7-4629-bb11-bfefdb27e7b7

_session: `session_7ed75446-feb7-4629-bb11-bfefdb27e7b7`_

### 6. [pricing/plan] — Phoebe · 03/08 20:33

**Q:** besides，$6999 is our deposit-only price, not MSRP. the answer of chatty ai is also wrong

**Bot trả (sai/thiếu):**

```
Found it, that pricing mix-up comes from how the page content gets read: the section listing $6,999 lost its "Deposit-Only Price" label when pulled in, so the AI saw it next to the bundle total and assumed it was the full bundle price.
```

**CS sửa thành:**

```
AI hiểu sai context giá trên store: https://capture.avada.io/i/2yHbbAbI1lc6, trên store giá MSRP có strikethrough tag: https://capture.avada.io/i/tf2KMCrVnzWZ, vì không nhận diện được strikethrough nên mặc định hiểu là bao gồm MSRP
```

**Context:** Submitted via TS Elite by phuongttm.ctv@avadagroup.com · ref=crisp:session_7ed75446-feb7-4629-bb11-bfefdb27e7b7

_session: `session_7ed75446-feb7-4629-bb11-bfefdb27e7b7`_

### 7. [integration] — Phoebe · 03/08 22:17

**Q:** we dont want chatty to send me an email every time the customer replies, i just want a transcript at the end of the conversation, how do we change this?

**Bot trả (sai/thiếu):**

```
Got it, that's an easy switch. Head to Settings → Notifications → Email Notifications and turn off the notification that's emailing you on every reply (likely "Unanswered by AI" or a general escalation alert).
```

**CS sửa thành:**

```
Không có scenario nào cho tắt noti on every reply
```

**Context:** Submitted via TS Elite by phuongttm.ctv@avadagroup.com · ref=crisp:session_6af36054-cf1b-4fa5-bbb4-ddf9fc38f61d

_session: `session_6af36054-cf1b-4fa5-bbb4-ddf9fc38f61d`_

### 8. [integration] — Phoebe · 03/08 22:18

**Q:** we dont want chatty to send me an email every time the customer replies, i just want a transcript at the end of the conversation, how do we change this?

**Bot trả (sai/thiếu):**

```
Then go to Settings → Channels → Email channel → Preferences and turn on Conversation transcript email, adding your email under Forward to. That'll send you one transcript once the conversation wraps up instead of an email per reply.
```

**CS sửa thành:**

```
Không có Settings → Channels -> Email channel → Preferences
```

**Context:** Submitted via TS Elite by phuongttm.ctv@avadagroup.com · ref=crisp:session_6af36054-cf1b-4fa5-bbb4-ddf9fc38f61d

_session: `session_6af36054-cf1b-4fa5-bbb4-ddf9fc38f61d`_

### 9. [chat/inbox] — Phoebe · 03/08 22:19

**Q:** [Image: https://storage.crisp.chat/users/upload-1/session/-/5/7/0/d/570d5a0e0aec6800/image_4x7haf.png]

**Bot trả (sai/thiếu):**

```
Thanks for the screenshot! On this page, uncheck the Email box next to "Conversations assigned to AI assistant" (row 3), that's what's sending you an email on every AI reply.
```

**CS sửa thành:**

```
Scenario "Conversations assigned to AI assistant" chỉ thông báo khi AI join vào conversation, chứ không phải thông báo cho từng message AI gửi trong cùng 1 convo
```

**Context:** Submitted via TS Elite by phuongttm.ctv@avadagroup.com · ref=crisp:session_6af36054-cf1b-4fa5-bbb4-ddf9fc38f61d

_session: `session_6af36054-cf1b-4fa5-bbb4-ddf9fc38f61d`_

### 10. [chat/inbox] — Jade · 04/08 04:10

**Q:** where do i insert instructions for the ai chatbot

**Bot trả (sai/thiếu):**

```
From there you can write out the AI's tone, role, and response boundaries, or use the Generate with AI button to get a starting point based on your business type.
```

**CS sửa thành:**

```
From there, you can write out the AI's tone, role, behaviors, and response boundaries
```

**Context:** Submitted via TS Elite by phuongnt01@avadagroup.com · ref=crisp:session_71d4ffd3-f2a1-431d-b229-8278bb837cb0

_session: `session_71d4ffd3-f2a1-431d-b229-8278bb837cb0`_

### 11. [referral] — Andy · 04/08 11:30

**Q:** I would prefer Order lookup

**Bot trả (sai/thiếu):**

```
I just need to confirm one more setup detail before I can hand this to the team: Order lookup / order handoff decision. What would you prefer?
```

**CS sửa thành:**

```
khách đã trả lời là prefer order lookup rồi
```

**Context:** Submitted via TS Elite by anhbd@avadagroup.com · ref=crisp:session_0475f597-f02d-48d7-98de-fdc98c360f2c

_session: `session_0475f597-f02d-48d7-98de-fdc98c360f2c`_

### 12. [khác] — Andy · 04/08 20:34

**Q:** Eso puede salir antes de que el cliente escriba en el sitio web.
Cuando llega el cliente a WhatsApp algo diferente:

Bienvenid@ , soy Tatiana 😊
Cómo te puedo ayudar?

**Bot trả (sai/thiếu):**

```
Perfecto, anotado ese saludo diferente para WhatsApp 😊
```

**CS sửa thành:**

```
Không set greeting riêng cho từng channel được
```

**Context:** Submitted via TS Elite by anhbd@avadagroup.com · ref=crisp:session_e1f265d2-d054-4171-9fc3-fc4a6060eb24

_session: `session_e1f265d2-d054-4171-9fc3-fc4a6060eb24`_

### 13. [khác] — Andy · 05/08 14:03

**Q:** Muchas gracias de verdad por haberme ayudado a configurar la IA

**Bot trả (sai/thiếu):**

```
Hola,

Muchas gracias a ti por tu paciencia y por compartir toda la información necesaria para configurar tu agente de IA.

Nuestro equipo sigue trabajando en la configuración final basada en los detalles que nos diste, y te avisaré aquí mismo en cuanto esté lista para tu revisión.

Si tienes alguna otra pregunta mientras tanto, no dudes en escribirme.

Saludos,
Ivy
Chatty Support Team
```

**CS sửa thành:**

```
CS đã setup xong AI cho khách rồi
```

**Context:** Submitted via TS Elite by anhbd@avadagroup.com · ref=crisp:session_07c110c1-68ad-4949-b117-e0ff8f8e0138

_session: `session_07c110c1-68ad-4949-b117-e0ff8f8e0138`_

### 14. [chat/inbox] — Andy · 06/08 09:30

**Q:** [Image: https://storage.crisp.chat/users/upload-1/session/-/6/b/5/4/6b54351a3a906400/image_jpu84d.png]

**Bot trả (sai/thiếu):**

```
Just to confirm, are you asking about the highlighted "3-5 business days" line in the AI's reply, since that looks different from your official 15-20 business day delivery estimate?
```

**CS sửa thành:**

```
Khách đang hỏi về conversation starters
```

**Context:** Submitted via TS Elite by anhbd@avadagroup.com · ref=crisp:session_02d5d6c2-b6a0-459e-bfe2-ffb08a5916ed

_session: `session_02d5d6c2-b6a0-459e-bfe2-ffb08a5916ed`_

### 15. [setup/config] — Andy · 06/08 10:12

**Q:** I need help on setup AI agent

**Bot trả (sai/thiếu):**

```
To have the AI reply to emails directly, go to AI agent → Instructions → Manage → General instructions → AI channels, and turn on Email. Once enabled, the AI will handle email replies automatically (it auto-replies after 5 minutes if no agent responds first).
```

**CS sửa thành:**

```
To have the AI reply to emails directly, go to AI agent → Settings -> AI channels, and turn on Email
```

**Context:** Submitted via TS Elite by anhbd@avadagroup.com · ref=crisp:session_af930999-9d31-42e0-81c0-f3007cd8d9ae

_session: `session_af930999-9d31-42e0-81c0-f3007cd8d9ae`_

### 16. [chat/inbox] — Phoebe · 06/08 20:07

**Q:** I dont can i have it as part of the chat

**Bot trả (sai/thiếu):**

```
Go to FAQs → FAQs block → Add block, pick the questions you want to show, then save. It'll appear in your chatbox automatically once added.
```

**CS sửa thành:**

```
It should be Chatbox > General > Blocks > FAQs > turn on. And to show which question in front of the chatbox, go to FAQs > Manages FAQs > Featured. FAQs block is to show on specific page, not the chat
```

**Context:** Submitted via TS Elite by phuongttm.ctv@avadagroup.com · ref=crisp:session_e94bb8ae-c897-4a8b-b004-e187ebd51082

_session: `session_e94bb8ae-c897-4a8b-b004-e187ebd51082`_

### 17. [khác] — Phoebe · 06/08 20:09

**Q:** homepage

**Bot trả (sai/thiếu):**

```
Perfect, homepage it is. Under Specific pages, tick Homepage.
```

**CS sửa thành:**

```
Open Display condition, under Specific pages, tick Homepage. Specific pages is child element of Display condition and Display condition is collapsed by default
```

**Context:** Submitted via TS Elite by phuongttm.ctv@avadagroup.com · ref=crisp:session_e94bb8ae-c897-4a8b-b004-e187ebd51082

_session: `session_e94bb8ae-c897-4a8b-b004-e187ebd51082`_
