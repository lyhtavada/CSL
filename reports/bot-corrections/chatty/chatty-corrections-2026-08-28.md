# Bot Corrections — Ivy (Chatty)

**Tuần:** 27/08/2026 → 28/08/2026  ·  **Tổng correction:** 2

> Đây là các câu bot trả bị CS sửa trong tuần. Dùng để update KB/training data cho bot.

## 📌 Tóm tắt theo topic

### khác — 1 câu
- 我想设置 AI回复客户消息，优先询问客户邮箱 要怎么做

### chat/inbox — 1 câu
- [AI Feedback] Bot message: Nuestro equipo está en línea en este momento y te atenderá de inmediato. ¿Quieres conectarte con el soporte huma…

**Người sửa:** Jade (2)

---

## 📋 Chi tiết từng correction

### 1. [khác] — Jade · 28/08 11:18

**Q:** 我想设置 AI回复客户消息，优先询问客户邮箱 要怎么做

**Bot trả (sai/thiếu):**

```
可以到 AI agent → Instructions → Manage → General instructions → Behaviours 这里添加一条自定义指令
```

**CS sửa thành:**

```
You will configure the Pre-chat form under the Chatbox > Chat page to require an email from customers before they start the chat
```

**Context:** Submitted via TS Elite by phuongnt01@avadagroup.com · ref=crisp:session_e6718968-69b2-4f87-8d9d-cf440f22f442

_session: `session_e6718968-69b2-4f87-8d9d-cf440f22f442`_

### 2. [chat/inbox] — Jade · 28/08 11:42

**Q:** [AI Feedback]
Bot message: Nuestro equipo está en línea en este momento y te atenderá de inmediato. ¿Quieres conectarte con el soporte humano?
Feedback: No hay equipo humano disponible, cuando el cliente solicite hablar con un agente, la ia debe de remitir al cliente a la pagina de contacto
ConvoId: ai-test-XOoGc7ye
MessageId: aivm-20784cc118d70d7c1dade23c

**Bot trả (sai/thiếu):**

```
Thanks for your patience on this.
```

**CS sửa thành:**

```
Trả lời sai ngôn ngữ khách
```

**Context:** Submitted via TS Elite by phuongnt01@avadagroup.com · ref=crisp:session_c13c2fb0-b8f6-4727-acd0-a05eb2bd5618

_session: `session_c13c2fb0-b8f6-4727-acd0-a05eb2bd5618`_
