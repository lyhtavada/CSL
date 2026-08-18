# Bot Corrections — Ivy (Chatty)

**Tuần:** 13/08/2026 → 18/08/2026  ·  **Tổng correction:** 8

> Đây là các câu bot trả bị CS sửa trong tuần. Dùng để update KB/training data cho bot.

## 📌 Tóm tắt theo topic

### khác — 6 câu
- Hoe kunnen we er voor zorgen dat als iemand aan de AI assistant vraagt om doorverbonden te worden met Tim, deze een whatsapp bericht ontvan…
- cannot find the setting
- they are but it says it cannot acces them when i test it
- … +3 câu khác (xem chi tiết bên dưới)

### pricing/plan — 1 câu
- Hello team, how can we regulate which discount codes it gives?  08/13/2026 8:23 PM Warm Wind υπαρχει καποιο εκπτωτικο κουπονι; 08/13/2026 8…

### setup/config — 1 câu
- I do NOT want the defaults you described. I choose ORDER LOOKUP. Please select ORDER LOOKUP and pass this choice to your setup team. Thank …

**Người sửa:** Cody (4), Hazel (2), Jade (2)

---

## 📋 Chi tiết từng correction

### 1. [khác] — Hazel · 13/08 18:20

**Q:** Hoe kunnen we er voor zorgen dat als iemand aan de AI assistant vraagt om doorverbonden te worden met Tim, deze een whatsapp bericht ontvangt?

**Bot trả (sai/thiếu):**

```
Daarnaast kun je onder Settings → Notifications → Email Notifications de melding "Unanswered by AI" of "Escalation" inschakelen met het gewenste e-mailadres.
```

**CS sửa thành:**

```
làm gì có "Unanswered by AI" of "Escalation" ở trong Notifications
```

**Context:** Submitted via TS Elite by hienpt@avadagroup.com · ref=crisp:session_e54d3b84-59ca-4207-9bf6-78b3245eccf9

_session: `session_e54d3b84-59ca-4207-9bf6-78b3245eccf9`_

### 2. [khác] — Cody · 14/08 02:37

**Q:** cannot find the setting

**Bot trả (sai/thiếu):**

```
Go to AI agent → Proactive chat → Discount list, you'll see all synced codes there and can manually turn off any you don't want the AI to use.
```

**CS sửa thành:**

```
AI Agent > Data training > Discounts
```

**Context:** Submitted via TS Elite by chauhm@avadagroup.com · ref=crisp:session_189c71d5-be72-456b-a44d-0016c47fd38c

_session: `session_189c71d5-be72-456b-a44d-0016c47fd38c`_

### 3. [pricing/plan] — Cody · 14/08 02:41

**Q:** Hello team, how can we regulate which discount codes it gives?

08/13/2026 8:23 PM Warm Wind
υπαρχει καποιο εκπτωτικο κουπονι;
08/13/2026 8:23 PM Φωτεινή | Βοηθός AI
Αυτή τη στιγμή μπορείτε να χρησιμοποιήσετε τον κωδικό STELLA για 15% έκπτωση σε όλη τη συλλογή μας, καθώς και τον κωδικό BESTPRICE10 για 10% έκπτωση σε αγορές άνω των 49€. Επίσης, διαθέτουμε τους κωδικούς WELCOME10, 10OFF και NEW20 π…

**Bot trả (sai/thiếu):**

```
If you want to limit which codes show up beyond that, go to Settings > AI Training / Proactive chat > Discount list, and manually disable any codes you don't want the AI to mention.
```

**CS sửa thành:**

```
AI agent > Training Data > Discounts
```

**Context:** Submitted via TS Elite by chauhm@avadagroup.com · ref=crisp:session_189c71d5-be72-456b-a44d-0016c47fd38c

_session: `session_189c71d5-be72-456b-a44d-0016c47fd38c`_

### 4. [setup/config] — Cody · 14/08 03:59

**Q:** I do NOT want the defaults you described. I choose ORDER LOOKUP. Please select ORDER LOOKUP and pass this choice to your setup team. Thank you.

**Bot trả (sai/thiếu):**

```
No problem if you'd rather not decide each one — I can have the team go with sensible defaults: your assistant greets customers as your store assistant, stays available around the clock, and sends anything about orders or refunds straight to you. Just say "sounds good" and I'll note those as your choices and pass it on.
```

**CS sửa thành:**

```
AI bị stuck in a loop. Câu trên khách đã confirm "choose ORDER LOOKUP" rồi.
```

**Context:** Submitted via TS Elite by chauhm@avadagroup.com · ref=crisp:session_2b072c08-939c-4fa4-8197-49c357116bc5

_session: `session_2b072c08-939c-4fa4-8197-49c357116bc5`_

### 5. [khác] — Jade · 14/08 11:11

**Q:** they are but it says it cannot acces them when i test it

**Bot trả (sai/thiếu):**

```
Go to AI agent → Training data → Products, and confirm the toggle "Enable your AI agent to answer customer questions about products" is switched ON.
```

**CS sửa thành:**

```
Go to AI agent → Training data → Products and confirm you activated this option
```

**Context:** Submitted via TS Elite by phuongnt01@avadagroup.com · ref=crisp:session_97c8727b-75eb-4120-9893-9cf780a3de01

_session: `session_97c8727b-75eb-4120-9893-9cf780a3de01`_

### 6. [khác] — Jade · 14/08 20:38

**Q:** Hi I wanted to check in if there's been any progress? thanks

**Bot trả (sai/thiếu):**

```
Our team is still working on this one, I don't have a confirmed update yet but I'll make sure to follow up with you here as soon as I hear back.
```

**CS sửa thành:**

```
As I can see, our team did provide you with an update regarding your previous question about Chatty's cart data and consent handling. 

Let me share further details with you if you missed this note; no worries.
```

**Context:** Submitted via TS Elite by phuongnt01@avadagroup.com · ref=crisp:session_9ee465af-d055-4143-8b53-63b72539cb5a

_session: `session_9ee465af-d055-4143-8b53-63b72539cb5a`_

### 7. [khác] — Cody · 16/08 00:54

**Q:** yes I am store owner

**Bot trả (sai/thiếu):**

```
In the Chatty app inside Shopify Admin, look for the "Web app activation" notice on the Dashboard, Settings → Team, or Chatbox → Live chat in Blocks. Tap Activate there, then set a password.
```

**CS sửa thành:**

```
Go to Settings > Team to activate the account
```

**Context:** Submitted via TS Elite by chauhm@avadagroup.com · ref=crisp:session_cd863687-3f5f-47ea-ac1b-21362a26951d

_session: `session_cd863687-3f5f-47ea-ac1b-21362a26951d`_

### 8. [khác] — Hazel · 16/08 05:16

**Q:** 我如何改在和客户聊天时我的名字

**Bot trả (sai/thiếu):**

```
To change the name customers see when you reply, go to Settings → Team → Manage, click your profile, then update the Name field and save.
```

**CS sửa thành:**

```
đổi tên hiển thị khi chat với KH nếu là admin thì đổi cả ở Settings > Store informations
```

**Context:** Submitted via TS Elite by hienpt@avadagroup.com · ref=crisp:session_d0ddbe0a-997b-4532-9177-e112a72aec85

_session: `session_d0ddbe0a-997b-4532-9177-e112a72aec85`_
