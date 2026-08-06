# Bot Corrections — Ivy (Chatty)

**Tuần:** 30/07/2026 → 05/08/2026  ·  **Tổng correction:** 17

> Đây là các câu bot trả bị CS sửa trong tuần. Dùng để update KB/training data cho bot.

## 📌 Tóm tắt theo topic

### chat/inbox — 5 câu
- [Image: https://storage.crisp.chat/users/upload-1/session/-/c/9/6/d/c96d3f87f94d4000/image_ret6dw.png]
- [Image: https://storage.crisp.chat/users/upload-1/session/-/b/3/b/5/b3b57af74ec58000/screenshot-199_1t8jldk.png]
- I don't want a message to appear so that the client sees the chatbot on my site. [Image: /images/components/base/BaseFlag/fr.png]
- … +2 câu khác (xem chi tiết bên dưới)

### integration — 4 câu
- da dove hai preso questa risposta non è correta
- Is it possible for button to be add to cart instead of view product?
- we dont want chatty to send me an email every time the customer replies, i just want a transcript at the end of the conversation, how do we…
- … +1 câu khác (xem chi tiết bên dưới)

### khác — 4 câu
- 2-3 giorni lavorativi
- Hi Harry,
- Eso puede salir antes de que el cliente escriba en el sitio web. Cuando llega el cliente a WhatsApp algo diferente:  Bienvenid@ , soy Tatia…
- … +1 câu khác (xem chi tiết bên dưới)

### pricing/plan — 2 câu
- ele a nao me deixa adicionar outro idioma no plano free, porem para mim nao é interessante pagar $19,90 agora, nao tem outra alternativa in…
- besides，$6999 is our deposit-only price, not MSRP. the answer of chatty ai is also wrong

### setup/config — 1 câu
- Hi Chatty Support Team,  I noticed an issue where Chatty AI is generating inaccurate information when answering customer queries on our sto…

### referral — 1 câu
- I would prefer Order lookup

**Người sửa:** Phoebe (9), Andy (4), Hazel (1), Alicia (1), Cody (1), Jade (1)

---

## 📋 Chi tiết từng correction

### 1. [pricing/plan] — Hazel · 30/07 22:17

**Q:** ele a nao me deixa adicionar outro idioma no plano free, porem para mim nao é interessante pagar $19,90 agora, nao tem outra alternativa inicial para testar?

**Bot trả (sai/thiếu):**

```
Basta ir em AI agent → Instructions → Manage → General instructions → Behaviours e adicionar a instrução: "Always respond in the same language as the customer."
```

**CS sửa thành:**

```
AI trả lời trên ngôn ngũe của KH viết đè instructions không work được
```

**Context:** Submitted via TS Elite by hienpt@avadagroup.com · ref=crisp:session_71a70ad3-a111-494c-bd1b-3109eeca20ff

_session: `session_71a70ad3-a111-494c-bd1b-3109eeca20ff`_

### 2. [integration] — Phoebe · 30/07 22:56

**Q:** da dove hai preso questa risposta non è correta

**Bot trả (sai/thiếu):**

```
Puoi modificarla da AI agent → Training data → Custom knowledge → FAQ: cerca la domanda "How long will it take to receive my order?" e aggiorna la risposta con i tempi di spedizione corretti.
```

**CS sửa thành:**

```
This is FAQ page -> should also recommend FAQ section > Manage FAQ > Search for " How long will it take to receive my order?"
```

**Context:** Submitted via TS Elite by phuongttm.ctv@avadagroup.com · ref=crisp:session_f04b3fb2-38b9-4eff-9d34-39b824099a69

_session: `session_f04b3fb2-38b9-4eff-9d34-39b824099a69`_

### 3. [chat/inbox] — Phoebe · 30/07 22:57

**Q:** [Image: https://storage.crisp.chat/users/upload-1/session/-/c/9/6/d/c96d3f87f94d4000/image_ret6dw.png]

**Bot trả (sai/thiếu):**

```
Perfetto, ora ho la domanda esatta e la risposta sbagliata dell'AI.
```

**CS sửa thành:**

```
This is content of Conversation Starter > Suggest go to Chatbox > Chat Page > Conversation Starter
```

**Context:** Submitted via TS Elite by phuongttm.ctv@avadagroup.com · ref=crisp:session_f04b3fb2-38b9-4eff-9d34-39b824099a69

_session: `session_f04b3fb2-38b9-4eff-9d34-39b824099a69`_

### 4. [khác] — Phoebe · 30/07 23:00

**Q:** 2-3 giorni lavorativi

**Bot trả (sai/thiếu):**

```
Per risolverlo:
• Vai su AI agent → Training data → Manage e assicurati che il toggle FAQs sia attivo
• Crea una nuova QnA: Domanda: "Quanto tempo ci vuole per la consegna?" → Risposta: "2-3 giorni lavorativi"
```

**CS sửa thành:**

```
Another way is to look for (1) FAQ section > Manage FAQ and (2) Chatbox > Chat Page > Conversation Starters
```

**Context:** Submitted via TS Elite by phuongttm.ctv@avadagroup.com · ref=crisp:session_f04b3fb2-38b9-4eff-9d34-39b824099a69

_session: `session_f04b3fb2-38b9-4eff-9d34-39b824099a69`_

### 5. [khác] — Andy · 31/07 06:03

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

### 6. [integration] — Alicia · 01/08 01:45

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

### 7. [chat/inbox] — Phoebe · 02/08 21:05

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

### 8. [chat/inbox] — Cody · 03/08 07:44

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

### 9. [setup/config] — Phoebe · 03/08 20:25

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

### 10. [pricing/plan] — Phoebe · 03/08 20:33

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

### 11. [integration] — Phoebe · 03/08 22:17

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

### 12. [integration] — Phoebe · 03/08 22:18

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

### 13. [chat/inbox] — Phoebe · 03/08 22:19

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

### 14. [chat/inbox] — Jade · 04/08 04:10

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

### 15. [referral] — Andy · 04/08 11:30

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

### 16. [khác] — Andy · 04/08 20:34

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

### 17. [khác] — Andy · 05/08 14:03

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
