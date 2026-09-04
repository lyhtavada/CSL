# Bot Corrections — Ivy (Chatty)

**Tuần:** 03/09/2026 → 04/09/2026  ·  **Tổng correction:** 6

> Đây là các câu bot trả bị CS sửa trong tuần. Dùng để update KB/training data cho bot.

## 📌 Tóm tắt theo topic

### khác — 4 câu
- when clicked
- bondteam@luxxecoast.com
- 想问下 我可能需要一个设置帮助 就是用户通过AI 客服提交了 售后信息 怎样让他发给我们的客服邮箱呢
- … +1 câu khác (xem chi tiết bên dưới)

### loyalty page/widget — 1 câu
- I want to display Chatty only on specific pages. How do I set that up?

### integration — 1 câu
- And how do I switch off the we are online bit on the chatbox? so people don't email in

**Người sửa:** Jade (3), Hazel (2), Andy (1)

---

## 📋 Chi tiết từng correction

### 1. [loyalty page/widget] — Jade · 03/09 17:11

**Q:** I want to display Chatty only on specific pages. How do I set that up?

**Bot trả (sai/thiếu):**

```
Sure! Head to Chatbox → Advanced → Display settings → Display pages, then choose "Hide on specific pages" and add the URLs you want to exclude.
```

**CS sửa thành:**

```
To set it up, you will go to the Chatbox section > Display rule > Show on specific pages and configure the pages
```

**Context:** Submitted via TS Elite by phuongnt01@avadagroup.com · ref=crisp:session_196b255e-31cd-472a-92d4-bdce29c23ad5

_session: `session_196b255e-31cd-472a-92d4-bdce29c23ad5`_

### 2. [khác] — Andy · 03/09 18:38

**Q:** when clicked

**Bot trả (sai/thiếu):**

```
You can turn off the Search button from your chatbox blocks. Go to Chatbox → General → Blocks, then toggle off the Search block so only the AI chat button shows.
```

**CS sửa thành:**

```
Không có block Search trên widget
```

**Context:** Submitted via TS Elite by anhbd@avadagroup.com · ref=crisp:session_4577e504-8a51-4136-8475-46427d535bff

_session: `session_4577e504-8a51-4136-8475-46427d535bff`_

### 3. [integration] — Hazel · 03/09 19:09

**Q:** And how do I switch off the we are online bit on the chatbox? so people don't email in

**Bot trả (sai/thiếu):**

```
To remove the "We are online" status line from the chatbox, go to Settings → Working hours and toggle Chat status off.
```

**CS sửa thành:**

```
Settings > chat availaibilty > working hours
```

**Context:** Submitted via TS Elite by hienpt@avadagroup.com · ref=crisp:session_7204d638-9de8-4785-b085-3d21ab304d43

_session: `session_7204d638-9de8-4785-b085-3d21ab304d43`_

### 4. [khác] — Hazel · 03/09 23:40

**Q:** bondteam@luxxecoast.com

**Bot trả (sai/thiếu):**

```
Go to Chatty → Channels → Email settings and add luxxecoast.com as your custom sender domain there.
```

**CS sửa thành:**

```
Chatty → Channels →Email sender
```

**Context:** Submitted via TS Elite by hienpt@avadagroup.com · ref=crisp:session_84efa84a-0bb4-473d-8ecf-a21e4c6a8bf3

_session: `session_84efa84a-0bb4-473d-8ecf-a21e4c6a8bf3`_

### 5. [khác] — Jade · 04/09 11:20

**Q:** 想问下 我可能需要一个设置帮助 就是用户通过AI 客服提交了 售后信息 怎样让他发给我们的客服邮箱呢

**Bot trả (sai/thiếu):**

```
这个可以在 AI agent → Scenarios → Human handover 里设置。
```

**CS sửa thành:**

```
You can set it up in Agent > Skills > After-sale support
```

**Context:** Submitted via TS Elite by phuongnt01@avadagroup.com · ref=crisp:session_e3ac0d6f-df0b-4e28-9603-9ef008456e3d

_session: `session_e3ac0d6f-df0b-4e28-9603-9ef008456e3d`_

### 6. [khác] — Jade · 04/09 11:36

**Q:** 人工又在哪里回答

**Bot trả (sai/thiếu):**

```
可以去 AI agent → Scenarios → Human handover，打开"AI cannot answer"这个自动触发条件
```

**CS sửa thành:**

```
You can go to AI agent → Skills → Human handover and enable the "AI cannot answer" automatic trigger condition.
```

**Context:** Submitted via TS Elite by phuongnt01@avadagroup.com · ref=crisp:session_c7092aa2-ba44-4cfb-ad3a-f4116a03ff88

_session: `session_c7092aa2-ba44-4cfb-ad3a-f4116a03ff88`_
