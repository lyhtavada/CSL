# Bot Corrections — Ivy (Chatty)

**Tuần:** 11/09/2026 → 14/09/2026  ·  **Tổng correction:** 6

> Đây là các câu bot trả bị CS sửa trong tuần. Dùng để update KB/training data cho bot.

## 📌 Tóm tắt theo topic

### khác — 3 câu
- Next question, where can I edit the text a customer sees if they ask/select to talk to a Human?
- when time conv is finish. how is it calculate
- yo crero que es porque recien estoy configurando

### integration — 1 câu
- Hi, we're trying to set something up like the following: In any situation where the agent suggests the customer reach out to info@greytowng…

### chat/inbox — 1 câu
- HOW TO CHANGE BRANDING COLORS IN CHATBOX

### pricing/plan — 1 câu
- i have upgraded plan, please sync my all products

**Người sửa:** Jade (3), Linda (1), Phoebe (1), Hazel (1)

---

## 📋 Chi tiết từng correction

### 1. [khác] — Linda · 11/09 22:50

**Q:** Next question, where can I edit the text a customer sees if they ask/select to talk to a Human?

**Bot trả (sai/thiếu):**

```
You'll find that under AI agent → Scenarios → Human handover → Edit, in the "Where does the customer go?" section, there's a separate field for the staff-transfer message text.
```

**CS sửa thành:**

```
You'll find that under AI agent → Skills → Human agent transfer → Edit
```

**Context:** Submitted via TS Elite by linhtlk@avadagroup.com · ref=crisp:session_65b822d3-9869-4b76-981f-535c76f53e5e

_session: `session_65b822d3-9869-4b76-981f-535c76f53e5e`_

### 2. [khác] — Jade · 11/09 23:01

**Q:** when time conv is finish. how is it calculate

**Bot trả (sai/thiếu):**

```
A conversation ends when a team member manually resolves it, when it auto-resolves after 60 minutes of no team reply, or when the customer's session expires after 5 days of inactivity.
```

**CS sửa thành:**

```
A conversation ends when a team member manually resolves it, when it auto-resolves after a period of time with no team reply (set under the Automatic resolution setting), or when the customer's session expires after 5 days of inactivity.
```

**Context:** Submitted via TS Elite by phuongnt01@avadagroup.com · ref=crisp:session_b79b0d3f-aa6a-41cc-9745-987aceb424dc

_session: `session_b79b0d3f-aa6a-41cc-9745-987aceb424dc`_

### 3. [integration] — Phoebe · 11/09 23:43

**Q:** Hi, we're trying to set something up like the following:
In any situation where the agent suggests the customer reach out to info@greytowngin.com, suggests the customer fills in a contact form, or suggests to pass a customer's details along to the team, the agent should also automatically send the conversation transcript to adam@greytowngin.com

We have it set-up as an agent procedure but it isn'…

**Bot trả (sai/thiếu):**

```
Thanks for the detail on what you're trying to achieve!

That specific automation (transcript auto-sent whenever the AI mentions the email, a form, or passing details along) isn't something an agent procedure can trigger on its own, so that explains why it's not working, it's not a setup mistake on your end.

The closest built-in option is the Human handover scenario: go to AI agent → Scenarios → Human handover and set the destination to Collect info & follow up by email. When that handover actually triggers, it sends a summary (not the full chat transcript) to your team email, which you can edit in the AI settings.
```

**CS sửa thành:**

```
Human handover nằm trong AI agent > Skills, không phải trong Scenarios
```

**Context:** Submitted via TS Elite by phuongttm.ctv@avadagroup.com · ref=crisp:session_3a688bb6-c21f-4288-bbb6-acf2e6248dc1

_session: `session_3a688bb6-c21f-4288-bbb6-acf2e6248dc1`_

### 4. [chat/inbox] — Jade · 12/09 12:19

**Q:** HOW TO CHANGE BRANDING COLORS IN CHATBOX

**Bot trả (sai/thiếu):**

```
There you'll find Brand colors, where you can pick a preset, use "Surprise me" to randomize, or auto-detect your store's brand color.
```

**CS sửa thành:**

```
There you'll find Brand colors, where you can pick a preset, use "Surprise me" to randomize, or customize your store's brand color.
```

**Context:** Submitted via TS Elite by phuongnt01@avadagroup.com · ref=crisp:session_f4f49175-f955-4541-b615-b017f69a8902

_session: `session_f4f49175-f955-4541-b615-b017f69a8902`_

### 5. [pricing/plan] — Hazel · 12/09 15:57

**Q:** i have upgraded plan, please sync my all products

**Bot trả (sai/thiếu):**

```
To trigger a fresh sync right away, go to AI agent → Training data → Products and click Sync products.
```

**CS sửa thành:**

```
để sync all the remaining products sau khi upgrade, vào Products > Inactive tab > click all > select all matching products > enable
```

**Context:** Submitted via TS Elite by hienpt@avadagroup.com · ref=crisp:session_d53e2f60-e477-4361-8d1b-eb497670a604

_session: `session_d53e2f60-e477-4361-8d1b-eb497670a604`_

### 6. [khác] — Jade · 14/09 12:38

**Q:** yo crero que es porque recien estoy configurando

**Bot trả (sai/thiếu):**

```
Tienes razón, si aún no agregaste información sobre métodos de pago, el AI no tiene de dónde responder 😊
```

**CS sửa thành:**

```
You're right, if you haven't added information about payment methods yet, the AI has nothing to draw from to answer 

Moreover, please make sure that your AI has been activated
```

**Context:** Submitted via TS Elite by phuongnt01@avadagroup.com · ref=crisp:session_1441d581-b532-459c-86b2-706c2a04182b

_session: `session_1441d581-b532-459c-86b2-706c2a04182b`_
