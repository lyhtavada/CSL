# Bot Corrections — Ivy (Chatty)

**Tuần:** 13/07/2026 → 19/07/2026  ·  **Tổng correction:** 25

> Đây là các câu bot trả bị CS sửa trong tuần. Dùng để update KB/training data cho bot.

## 📌 Tóm tắt theo topic

### khác — 10 câu
- okay thanks!
- Hi, does the app support Hebrew?
- je voulais afficher seulement les questions
- … +7 câu khác (xem chi tiết bên dưới)

### chat/inbox — 9 câu
- [Image: https://storage.crisp.chat/users/upload-1/session/-/5/2/f/b/52fbfcfcd181bc00/image_to2vpf.png]
- [Image: https://storage.crisp.chat/users/upload-1/session/-/7/f/7/4/7f746567b1c71400/image_pguf34.png]
- [Image: https://storage.crisp.chat/users/upload-1/session/-/4/f/f/5/4ff5ae9df1520800/image_14clz5s.png]
- … +6 câu khác (xem chi tiết bên dưới)

### integration — 3 câu
- The images being sent to us are now being stored in my shopify files, is there a way we can stop this ? or is it necessary?
- yes, also I need to set support email to support@dougwestmusic.shop
- como obtengo la clave api para integración con 17 track?

### setup/config — 2 câu
- como indico eso para que se configure bien
- I need help on setup AI agent [Image: https://storage.crisp.chat/users/upload-1/session/-/d/1/4/e/d14e1ad0cc15a000/image_64sjvl.png https:/…

### loyalty page/widget — 1 câu
- hey actually we dont need ai agent we want each product to display its own FAQs

**Người sửa:** Phoebe (10), Andy (8), Jade (4), Cody (2), Hazel (1)

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

### 6. [integration] — Andy · 14/07 11:35

**Q:** The images being sent to us are now being stored in my shopify files, is there a way we can stop this ? or is it necessary?

**Bot trả (sai/thiếu):**

```
This is a new one for me, so let me check with the team on whether there's a way to stop chat images from being stored in your Shopify files. I'll get back to you here once I have an answer.
```

**CS sửa thành:**

```
hiện tại Free plan chỉ hỗ trợ store files/image ở Shopify files. Nếu khách muốn store ở external sources thì sẽ cần phải upgrade plan
```

**Context:** Submitted via TS Elite by anhbd@avadagroup.com · ref=crisp:session_fc5d1e30-224d-4a84-a6fd-342dd1a3e26c

_session: `session_fc5d1e30-224d-4a84-a6fd-342dd1a3e26c`_

### 7. [khác] — Jade · 14/07 20:32

**Q:** Hi, does the app support Hebrew?

**Bot trả (sai/thiếu):**

```
Hi there, I'm Ivy, your Chatty AI assistant 😊 Hebrew isn't in the list of 19 languages Chatty auto-translates.
```

**CS sửa thành:**

```
Hi there, I'm Ivy, your Chatty AI assistant 😊. Hebrew is supported in the Chatty translation list. 

You can go to the app Settings > Translations > Add Hebrew
```

**Context:** Submitted via TS Elite by phuongnt01@avadagroup.com · ref=crisp:session_4edc1d65-4315-4a76-9633-00dbb00abbf2

_session: `session_4edc1d65-4315-4a76-9633-00dbb00abbf2`_

### 8. [khác] — Jade · 14/07 22:10

**Q:** je voulais afficher seulement les questions

**Bot trả (sai/thiếu):**

```
Oui, c'est tout à fait possible ! Voici comment faire :
Dans FAQs → FAQs block, quand vous choisissez vos questions avec Browse, activez l'option "Don't categorize FAQs" : cela affiche toutes les questions sélectionnées dans une liste simple, sans les titres de catégories.
```

**CS sửa thành:**

```
I understand that you would like to show FAQs on the chatbox only, and you can go to the Chatbox section > General > Blocks > Deactivate the Categories option
```

**Context:** Submitted via TS Elite by phuongnt01@avadagroup.com · ref=crisp:session_b18b4c76-ea16-4dd9-ac22-7478b572d1fd

_session: `session_b18b4c76-ea16-4dd9-ac22-7478b572d1fd`_

### 9. [khác] — Jade · 15/07 19:45

**Q:** hello i need to add a response to a popular question the ai is answering wrong

**Bot trả (sai/thiếu):**

```
Easy fix! Head to AI agent → Training data → Manage, then add or edit the FAQ entry for that question with the correct answer.
```

**CS sửa thành:**

```
Easy fix! Head to AI agent → Training data → Custom Knowledge > Questions, then add or edit the FAQ entry for that question with the correct answer.
```

**Context:** Submitted via TS Elite by phuongnt01@avadagroup.com · ref=crisp:session_0cd2f877-ac11-44cf-ab9f-e15d1f75fa54

_session: `session_0cd2f877-ac11-44cf-ab9f-e15d1f75fa54`_

### 10. [khác] — Hazel · 16/07 15:22

**Q:** for that particular product

**Bot trả (sai/thiếu):**

```
Yes, exactly, once you click Manage FAQs on that specific product, the AI-generate option there will create Q&A just for that product only, not the whole store.
```

**CS sửa thành:**

```
Làm gì có AI gen FAQ cho từng Product
```

**Context:** Submitted via TS Elite by hienpt@avadagroup.com · ref=crisp:session_ef5cf0e8-d1e8-47c2-84c1-2adf881a9525

_session: `session_ef5cf0e8-d1e8-47c2-84c1-2adf881a9525`_

### 11. [khác] — Phoebe · 16/07 20:12

**Q:** お願いします

**Bot trả (sai/thiếu):**

```
• FAQの質問タイトル「How long does delivery take?」を日本語に変更してください。
• AI agent → Instructions → Manage → General instructions → Behaviours にある「Always respond in the same language as the customer.」の指示を削除してください。「日本語のみで回答する」という指示と矛盾してしまうため、こちらは不要です。
```

**CS sửa thành:**

```
In the first message AI detected correctly about the Conversation Starter, so AI should continue guiding how to translate content there by going to Chatbox > Chat page
```

**Context:** Submitted via TS Elite by phuongttm.ctv@avadagroup.com · ref=crisp:session_19bd5865-9b5e-4d09-8c0b-69263978f90c

_session: `session_19bd5865-9b5e-4d09-8c0b-69263978f90c`_

### 12. [khác] — Phoebe · 16/07 22:44

**Q:** Hello, could you please help me find or update the estimated response time for customer requests? It’s currently set to 24 hours, but we’d like to extend it to 72 hours since we don’t operate on weekends

**Bot trả (sai/thiếu):**

```
That's the Response time promise, set under offline behavior. Go to AI agent → Settings → Human handover (or wherever you've set "Transfer to human in Chatty inbox") → Offline behavior → "Leave a message" option, and update the Response time promise there to 72 hours.
```

**CS sửa thành:**

```
AI agent > Instructions > Assistant skills > Human handover
```

**Context:** Submitted via TS Elite by phuongttm.ctv@avadagroup.com · ref=crisp:session_ee42c67c-87b3-42e5-afff-04f7c6266490

_session: `session_ee42c67c-87b3-42e5-afff-04f7c6266490`_

### 13. [khác] — Phoebe · 16/07 23:07

**Q:** no, I don't

**Bot trả (sai/thiếu):**

```
Could you share your collaborator request code? You'll find it in Shopify Admin → Settings → Users → Security, it's a 4-digit number.
```

**CS sửa thành:**

```
For any questions or issue related to Chatty settings, there is no need to ask for collaborator access
```

**Context:** Submitted via TS Elite by phuongttm.ctv@avadagroup.com · ref=crisp:session_ee42c67c-87b3-42e5-afff-04f7c6266490

_session: `session_ee42c67c-87b3-42e5-afff-04f7c6266490`_

### 14. [integration] — Cody · 17/07 02:40

**Q:** yes, also I need to set support email to support@dougwestmusic.shop

**Bot trả (sai/thiếu):**

```
To set your support email to support@dougwestmusic.shop, head to AI agent → Instructions → Manage → General instructions and update the support email field there.
```

**CS sửa thành:**

```
To set your support email to support@dougwestmusic.shop, head to AI agent > Settings > Support email addresses
```

**Context:** Submitted via TS Elite by chauhm@avadagroup.com · ref=crisp:session_36604c32-b39c-4ab5-b08c-f2df9d94f361

_session: `session_36604c32-b39c-4ab5-b08c-f2df9d94f361`_

### 15. [chat/inbox] — Andy · 17/07 04:22

**Q:** [Image: https://storage.crisp.chat/users/upload-1/session/-/4/f/f/5/4ff5ae9df1520800/image_14clz5s.png]

**Bot trả (sai/thiếu):**

```
The Display pages setting controls where the chatbox shows on your store's regular pages. The screenshot you shared is Shopify's checkout page, which is separate from the storefront.

Let me check with our team whether the chatbox can be shown there for your store, and I'll get back to you with an update.
```

**CS sửa thành:**

```
Chatty có extension riêng cho checkout page và thank-you page. Tuy nhiên có điều kiện quan trọng: chỉ Shopify Plus mới có quyền chỉnh sửa layout checkout để thêm extension này. Non-Plus stores bị Shopify chặn ở bước đó
```

**Context:** Submitted via TS Elite by anhbd@avadagroup.com · ref=crisp:session_1d652e7a-f44d-46a2-b403-cb559fa03d8c

_session: `session_1d652e7a-f44d-46a2-b403-cb559fa03d8c`_

### 16. [integration] — Andy · 17/07 04:32

**Q:** como obtengo la clave api para integración con 17 track?

**Bot trả (sai/thiếu):**

```
Para 17TRACK no necesitas obtener ni ingresar una clave API por tu cuenta: solo debes seleccionar 17TRACK como método de tracking dentro de Chatty.

Ve a Settings → Integrations → en Order tracking, haz clic en Manage, y selecciona 17TRACK como tu método preferido. Luego guarda los cambios.
```

**CS sửa thành:**

```
Doc hướng dẫn lấy API 17track:
https://api.17track.net/en/doc?version=v2.4&anchor=get-security-key
```

**Context:** Submitted via TS Elite by anhbd@avadagroup.com · ref=crisp:session_cb1ae127-cdfc-415a-9d69-d9d7a0c64eb3

_session: `session_cb1ae127-cdfc-415a-9d69-d9d7a0c64eb3`_

### 17. [chat/inbox] — Phoebe · 17/07 17:16

**Q:** not chat directly?

**Bot trả (sai/thiếu):**

```
That's the current handover setting, it's set to collect info and follow up by email instead of transferring directly into live chat.
To change it: go to AI agent → Instructions → Manage → Assistant skills → Customer support skills → Human handover, then under "Where does the customer go?" select Transfer to human in Chatty inbox instead.
That way customers connect straight into your inbox rather than being asked to email.
```

**CS sửa thành:**

```
AI could not get the context here, the issue is related to the Live chat feature not enabled
```

**Context:** Submitted via TS Elite by phuongttm.ctv@avadagroup.com · ref=crisp:session_05f5844c-db03-401e-a7dc-0dd892e061cc

_session: `session_05f5844c-db03-401e-a7dc-0dd892e061cc`_

### 18. [khác] — Phoebe · 17/07 19:07

**Q:** Also, do i get notifications on my phone?

**Bot trả (sai/thiếu):**

```
Yes, you can reply to conversations right from your phone using the Chatty mobile app (a PWA you install via your browser, not from the App Store).
```

**CS sửa thành:**

```
Chatty has already released app on Google Play and App store. Go to Inbox or Settings > Notifications to download
```

**Context:** Submitted via TS Elite by phuongttm.ctv@avadagroup.com · ref=crisp:session_5541a3db-cbed-4a50-a39f-15f904d2fa56

_session: `session_5541a3db-cbed-4a50-a39f-15f904d2fa56`_

### 19. [khác] — Phoebe · 17/07 19:12

**Q:** Also, do i get notifications on my phone?

**Bot trả (sai/thiếu):**

```
And yes, once installed you'll get push notifications for new messages right on your phone.
```

**CS sửa thành:**

```
Click Enable to allow Chatty send push notification on mobile
```

**Context:** Submitted via TS Elite by phuongttm.ctv@avadagroup.com · ref=crisp:session_5541a3db-cbed-4a50-a39f-15f904d2fa56

_session: `session_5541a3db-cbed-4a50-a39f-15f904d2fa56`_

### 20. [chat/inbox] — Andy · 17/07 23:04

**Q:** [Image: https://storage.crisp.chat/users/upload-1/session/-/6/5/b/0/65b0eaac6ab99c00/image_1vnlo8p.jpg]

**Bot trả (sai/thiếu):**

```
That's exactly the FAQ editor. Click on the question text ("How long will it take to receive my order?") to open it for editing, then update the answer text and click Save at the top right.
```

**CS sửa thành:**

```
đây là FAQs hiển thị trên widget ở front store.
Phải hướng dẫn khách set up FAQs từ trong Chatty app chứ
```

**Context:** Submitted via TS Elite by anhbd@avadagroup.com · ref=crisp:session_417833bc-aea2-4dd6-85bf-41c0d2cb6ff6

_session: `session_417833bc-aea2-4dd6-85bf-41c0d2cb6ff6`_

### 21. [setup/config] — Andy · 18/07 00:02

**Q:** I need help on setup AI agent
[Image: https://storage.crisp.chat/users/upload-1/session/-/d/1/4/e/d14e1ad0cc15a000/image_64sjvl.png https://storage.crisp.chat/users/upload-1/session/-/d/1/4/e/d14e1ad0cc15a000/image_lraxbg.png]

**Bot trả (sai/thiếu):**

```
太好了，成功了就好！😊
退款那边我们团队还在处理中，一有进展我会第一时间同步给您。还有其他需要帮忙的吗？
```

**CS sửa thành:**

```
Khách confirm lại là ko có refund request nào rồi mà
```

**Context:** Submitted via TS Elite by anhbd@avadagroup.com · ref=crisp:session_05f5844c-db03-401e-a7dc-0dd892e061cc

_session: `session_05f5844c-db03-401e-a7dc-0dd892e061cc`_

### 22. [chat/inbox] — Cody · 18/07 04:07

**Q:** hi there. how can I start a complete new chat?

**Bot trả (sai/thiếu):**

```
Go to Chatbox → General → Chatbox Style and turn on "Allow users to reset conversation".
```

**CS sửa thành:**

```
Wrong answer, customer can start a new chat on their end by going to the 3-dot icon on the top right of the chat page > choose reset conversation
```

**Context:** Submitted via TS Elite by chauhm@avadagroup.com · ref=crisp:session_7edbf8b2-1e85-41c1-9b46-dca05024128b

_session: `session_7edbf8b2-1e85-41c1-9b46-dca05024128b`_

### 23. [chat/inbox] — Phoebe · 18/07 20:22

**Q:** [Image: https://storage.crisp.chat/users/upload-1/session/-/8/0/a/b/80ab56c30ba56000/screenshot-2026-07-18-151452_3jdszi.png]

**Bot trả (sai/thiếu):**

```
Ciao! Questo succede perché l'AI risponde in base alla lingua dei dati di addestramento, ma non ha ancora un'istruzione esplicita per rispondere sempre in italiano.
Puoi risolverlo così: vai su AI agent → Instructions → Manage → General instructions → Behaviours e aggiungi questa istruzione: "Rispondi sempre nella stessa lingua del cliente."
Dopo averla salvata, testala di nuovo in Test AI per verificare che risponda in italiano.
```

**CS sửa thành:**

```
the prebuit questions showing up there is to support merchants test AI quickly, these questions are not showing up on the live store
```

**Context:** Submitted via TS Elite by phuongttm.ctv@avadagroup.com · ref=crisp:session_dba3ea65-cb1f-4dc7-92d8-c67362cca180

_session: `session_dba3ea65-cb1f-4dc7-92d8-c67362cca180`_

### 24. [chat/inbox] — Phoebe · 19/07 23:38

**Q:** [Image: https://storage.crisp.chat/users/upload-1/session/-/4/9/b/c/49bc92583d02d400/screenshot20260719093320chrome_vkrbel.jpg]

**Bot trả (sai/thiếu):**

```
Thanks for the screenshot! That's the "..." menu, which only has Manage app, Get support, Pin, and Uninstall, no Inbox there.
```

**CS sửa thành:**

```
suggest clicking on the hamburger menu next to the search field on the header. Find Inbox under Chatty app
```

**Context:** Submitted via TS Elite by phuongttm.ctv@avadagroup.com · ref=crisp:session_259306fe-24b0-4244-aecb-1a764f42d936

_session: `session_259306fe-24b0-4244-aecb-1a764f42d936`_

### 25. [chat/inbox] — Phoebe · 19/07 23:39

**Q:** [Image: https://storage.crisp.chat/users/upload-1/session/-/4/9/b/c/49bc92583d02d400/screenshot20260719093320chrome_vkrbel.jpg]

**Bot trả (sai/thiếu):**

```
Try tapping "Manage app" instead, that should open the full Chatty dashboard where you'll find the Inbox tab in the side menu.
```

**CS sửa thành:**

```
suggest clicking on the hamburger menu on the mobile which next to the search field on the header. Find Inbox under Chatty app: https://capture.avada.io/i/1g5trvkYxuiB
```

**Context:** Submitted via TS Elite by phuongttm.ctv@avadagroup.com · ref=crisp:session_259306fe-24b0-4244-aecb-1a764f42d936

_session: `session_259306fe-24b0-4244-aecb-1a764f42d936`_
