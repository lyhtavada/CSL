# Bot Corrections — Ivy (Chatty)

**Tuần:** 10/09/2026 → 11/09/2026  ·  **Tổng correction:** 5

> Đây là các câu bot trả bị CS sửa trong tuần. Dùng để update KB/training data cho bot.

## 📌 Tóm tắt theo topic

### khác — 4 câu
- and info@ayafinejewelry.com remove this
- Fehlerhafte, automatische Übersetzungen der FAQ sind schon länger bekannt und von uns dem Team mitgeteilt worden. Aber leider sind sie noch…
- How do I edit/remove these?
- … +1 câu khác (xem chi tiết bên dưới)

### chat/inbox — 1 câu
- Hi - you fixed an issue for me with the proactive chat box when a customers adds something to the cart. But the chat message is persistent,…

**Người sửa:** Jade (3), Hazel (2)

---

## 📋 Chi tiết từng correction

### 1. [khác] — Jade · 10/09 16:47

**Q:** and info@ayafinejewelry.com remove this

**Bot trả (sai/thiếu):**

```
No problem if you'd rather not decide each one — I can have the team go with sensible defaults: your assistant greets customers as your store assistant, stays available around the clock, and sends anything about orders or refunds straight to you. Just say "sounds good" and I'll note those as your choices and pass it on. Would you like the team to use those defaults for Order lookup / order handoff decision?
```

**CS sửa thành:**

```
Let me forward your request to the internal team for further support
```

**Context:** Submitted via TS Elite by phuongnt01@avadagroup.com · ref=crisp:session_0895a9a8-b98a-4fe9-8392-7c252d09cc87

_session: `session_0895a9a8-b98a-4fe9-8392-7c252d09cc87`_

### 2. [chat/inbox] — Hazel · 10/09 18:45

**Q:** Hi - you fixed an issue for me with the proactive chat box when a customers adds something to the cart. But the chat message is persistent, and doesn't disappear after x seconds / be dismissed with a cross. Can you help?

**Bot trả (sai/thiếu):**

```
Thanks for the details! The auto-dismiss timing is controlled by the Display duration setting in that campaign.
```

**CS sửa thành:**

```
đây là lỗi không có x button để tắt pop-up trên store, thường phải add css > nên hỏi xin screenshot hoặc đưa CS check luôn
```

**Context:** Submitted via TS Elite by hienpt@avadagroup.com · ref=crisp:session_17a534ad-9782-45fb-90af-722453f8703a

_session: `session_17a534ad-9782-45fb-90af-722453f8703a`_

### 3. [khác] — Hazel · 10/09 19:46

**Q:** Fehlerhafte, automatische Übersetzungen der FAQ sind schon länger bekannt und von uns dem Team mitgeteilt worden. Aber leider sind sie noch immer nicht vollständig behoben worden.

**Bot trả (sai/thiếu):**

```
Das lässt sich direkt beheben: Gehe zu AI agent → Instructions → Custom Instructions und füge dort folgenden Satz hinzu:

"Always reply in the same language the customer is writing in. If the customer writes in English, respond fully in English, do not carry over German words or sentences even if the underlying FAQ source is in German. Apply the same rule for Spanish, Italian, Polish, Dutch, and any other language."
```

**CS sửa thành:**

```
KH dang nói về issue translate trên FAQs page không liên quan tới AI agent
```

**Context:** Submitted via TS Elite by hienpt@avadagroup.com · ref=crisp:session_9f483cc7-4a93-4c00-9b18-cd07e33e33c8

_session: `session_9f483cc7-4a93-4c00-9b18-cd07e33e33c8`_

### 4. [khác] — Jade · 11/09 09:06

**Q:** How do I edit/remove these?

**Bot trả (sai/thiếu):**

```
They're not visible to your actual customers on the live store. If you want different samples, just click "Regenerate questions" to get a new set.
```

**CS sửa thành:**

```
They're not visible to your actual customers on the live store.
```

**Context:** Submitted via TS Elite by phuongnt01@avadagroup.com · ref=crisp:session_b34b7b79-5eeb-439c-9a7c-4944c2541ab2

_session: `session_b34b7b79-5eeb-439c-9a7c-4944c2541ab2`_

### 5. [khác] — Jade · 11/09 09:19

**Q:** Thank you

**Bot trả (sai/thiếu):**

```
Just head to AI agent → Settings and turn on the "AI Assistant" toggle, then save. That should fix it right away.
```

**CS sửa thành:**

```
Just head to AI agent → Activate the feature then save. That should fix it right away.
```

**Context:** Submitted via TS Elite by phuongnt01@avadagroup.com · ref=crisp:session_b34b7b79-5eeb-439c-9a7c-4944c2541ab2

_session: `session_b34b7b79-5eeb-439c-9a7c-4944c2541ab2`_
