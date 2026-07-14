# Bot Corrections — Ivy (Chatty)

**Tuần:** 13/07/2026 → 14/07/2026  ·  **Tổng correction:** 5

> Đây là các câu bot trả bị CS sửa trong tuần. Dùng để update KB/training data cho bot.

## 📌 Tóm tắt theo topic

### chat/inbox — 2 câu
- [Image: https://storage.crisp.chat/users/upload-1/session/-/5/2/f/b/52fbfcfcd181bc00/image_to2vpf.png]
- [Image: https://storage.crisp.chat/users/upload-1/session/-/7/f/7/4/7f746567b1c71400/image_pguf34.png]

### setup/config — 1 câu
- como indico eso para que se configure bien

### khác — 1 câu
- okay thanks!

### loyalty page/widget — 1 câu
- hey actually we dont need ai agent we want each product to display its own FAQs

**Người sửa:** Andy (3), Phoebe (1), Jade (1)

---

## 📋 Chi tiết từng correction

### 1. [setup/config] — Phoebe · 13/07 22:34

**Q:** como indico eso para que se configure bien

**Bot trả (sai/thiếu):**

```
Entendido, quieres que el asistente se presente como BEBERSO y no revele que es una IA ni mencione a Chatty.
Voy a anotar esto para que el equipo lo incluya en las instrucciones del rol al configurar tu AI agent: que se presente únicamente como BEBERSO, sin mencionar que es IA ni el nombre Chatty.
Esto quedará configurado en AI agent → Instructions → Manage → General instructions → Role, junto con el resto de la configuración que ya está en proceso con el equipo.
```

**CS sửa thành:**

```
To change AI name go to AI agent -> Settings > Name
```

**Context:** Submitted via TS Elite by phuongttm.ctv@avadagroup.com · ref=crisp:session_add0b220-7cce-40e0-a168-5a85e02179d8

_session: `session_add0b220-7cce-40e0-a168-5a85e02179d8`_

### 2. [khác] — Andy · 13/07 23:52

**Q:** okay thanks!

**Bot trả (sai/thiếu):**

```
You're welcome! Our team is still looking into the order recall issue and will follow up with you here once there's an update.
```

**CS sửa thành:**

```
Báo khách xong rồi mà, làm gì còn still looking into the issue nữa
```

**Context:** Submitted via TS Elite by anhbd@avadagroup.com · ref=crisp:session_2cbfe5d4-2fcb-4734-a9f3-4fea44abd5c7

_session: `session_2cbfe5d4-2fcb-4734-a9f3-4fea44abd5c7`_

### 3. [chat/inbox] — Andy · 13/07 23:53

**Q:** [Image: https://storage.crisp.chat/users/upload-1/session/-/5/2/f/b/52fbfcfcd181bc00/image_to2vpf.png]

**Bot trả (sai/thiếu):**

```
Thanks for confirming, order SF#12292 should definitely be findable since it shows in Shopify, so this looks like a genuine lookup issue on the AI's end.
```

**CS sửa thành:**

```
Trong ảnh thì mới có Order ID thôi.
Track order thì cần car order ID lẫn email address/phone number
```

**Context:** Submitted via TS Elite by anhbd@avadagroup.com · ref=crisp:session_2cbfe5d4-2fcb-4734-a9f3-4fea44abd5c7

_session: `session_2cbfe5d4-2fcb-4734-a9f3-4fea44abd5c7`_

### 4. [loyalty page/widget] — Jade · 14/07 06:34

**Q:** hey actually we dont need ai agent we want each product to display its own FAQs

**Bot trả (sai/thiếu):**

```
For product-specific FAQs without the AI agent, you'd go to AI agent → Training data → Products, pick the product, and click Add FAQs or Manage FAQs to attach questions directly to that product.

That's the built-in way to give each product its own set of FAQs.
```

**CS sửa thành:**

```
In this case, you will create an FAQs block for each product (under FAQs → FAQs block), select the questions you want, then set the display condition to Product pages → By collection/tag so different products show different FAQ sets.
```

**Context:** Submitted via TS Elite by phuongnt01@avadagroup.com · ref=crisp:session_b4f6f9c0-e6e6-4427-8b3b-ccec74d920eb

_session: `session_b4f6f9c0-e6e6-4427-8b3b-ccec74d920eb`_

### 5. [chat/inbox] — Andy · 14/07 08:26

**Q:** [Image: https://storage.crisp.chat/users/upload-1/session/-/7/f/7/4/7f746567b1c71400/image_pguf34.png]

**Bot trả (sai/thiếu):**

```
可以的，去 AI agent → Instructions → Manage → General instructions → Role 里就能改助手的名字，最多250字符
如果想改欢迎语，也可以在同一页面的 Behaviours 里调整
```

**CS sửa thành:**

```
Name trong ảnh của khách là ở phần Team settings
```

**Context:** Submitted via TS Elite by anhbd@avadagroup.com · ref=crisp:session_fa6aecfa-baef-4c24-a5c9-de6d85b40d3b

_session: `session_fa6aecfa-baef-4c24-a5c9-de6d85b40d3b`_
