# QA Tuần 2026-W25 — Jade (Chatty)
**Tuần 15/06 – 21/06/2026** · coaching, không phải penalty

## 📊 Điểm tuần: 84/100 — Tốt  (▲ +1 so với W24: 83)
🔍 Đã QA: 29 chat

**Breakdown 3 trục:** 🧠 Mindset 28.0/34 · 📚 Kiến thức 28.2/33 · 🛠️ Xử lý 27.4/33  →  trục yếu nhất: **skill**

## 📝 Nhận xét chung


## ✅ Điểm tốt
- [P] Best chat of the week. Correctly diagnosed that welcome message lives in AI Settings (not Chatbox). Gave honest store rating. Natural review ask led to review obtained. (#12)
- [P] Strong proactive follow-up pattern: Jade consistently sent email updates after dev fixes across multiple chats (#20 CSS, #23 wishlist, #29 loyalty page) without being asked. (#20 #23 #29)
- [P] Caught and corrected Joyce AI's wrong information about translations not carrying to unified widget. Proactively clarified for merchant. (#15)
- [P] Stayed 22 minutes past shift to fully resolve email integration issue. (#2)

## 🔧 Cần cải thiện
- [Live-store/Security] (High) Jade asked for store password twice this week in chats #3 and #27. (#3 #27)
   • Dẫn chứng: [01:57:07] CS (Jade): "can you kindly share with us the store password so our tech team can conduct a more thorough investigation?"
   → Cần nhắc ngay: không bao giờ xin store password. Xin collaborator access code (4 chữ số) từ Shopify Settings > Users > Security. Đây là lỗi lặp lại trong cùng 1 tuần.
- [KN2] (Low) In chat #22, Jade asked the same question twice after merchant already answered. (#22)
   • Dẫn chứng: [17:29:29] CS (Jade): "Darf ich in diesem Punkt fragen, ob Sie markus.hamburg@outlook.de aus Ihrer Kunden-Datenbank entfernt haben?" — then repeated same question at [17:31:02] despite merchant saying 'ich sagte doch bereits, dass ich die Daten aus dem System gelöscht habe!'
   → Đọc lại phản hồi của khách trước khi hỏi. Khi khách đã trả lời, acknowledge và chuyển tiếp, không hỏi lại.
- [QT22] (Low) Internal note accidentally sent to customer in chat #4. (#4)
   • Dẫn chứng: [10:29:02] CS (Jade): "ver 1.7.3 traduzione non funziona" — sent directly to customer chat instead of internal note channel.
   → Dùng đúng field internal note, không paste vào cửa sổ chat khách. Jade đã xin lỗi sau đó nhưng cần tránh trường hợp này xảy ra.
- [QT16] (Low) Missed review ask after clean, happy resolution. (#17)
   • Dẫn chứng: [21:56:16] Customer: "ok yes that must be it thank you!" then [21:56:49] CS (Jade): "You are welcome, and is there anything else I can help with today?" — no review ask.
   → Khi khách nói 'thank you' sau khi case resolved clean, đó là thời điểm vàng để mời review. Chỉ cần 1 câu ngắn.

## 🚨 Severe flags (Liz xem kỹ)
- {"chat": 3, "type": "live-store / security", "quote": "[01:57:07] CS (Jade): \"If you do not mind, can you kindly share with us the store password so our tech team can conduct a more thorough investigation?\"", "action_required": "Never ask for store password. Request collaborator access code instead (Shopify Settings > Users > Security)."}
- {"chat": 27, "type": "live-store / security (repeat)", "quote": "[07:37:00] CS (Jade): \"Can you kindly share the store password so I can take a look at the issue? Thank you for your help.\"", "action_required": "Second store password request this week. Same error as #3 — needs immediate coaching on correct access protocol."}

## 🌟 Xin review (chỉ ghi nhận, KHÔNG tính điểm)
- Đã xin 2/3 chat phù hợp. Xin review 2/3 chat eligible (đúng lúc 2, bỏ lỡ 1). Chat #17 sau khi khách nói 'ok yes that must be it thank you!' — đây là lúc phù hợp nhất nhưng không xin.

## 📈 So với tuần trước
W24 83 → W25 84 (+1)

## 🔗 Chat đã QA
<https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_742128c3-1b13-42f9-90cf-ec2f3f9e0846|#1 Jenny Thiel> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_8a113a0a-5665-4a91-934d-357e5f91ec38|#2 Now Pty Market> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_3552497c-2a64-4499-b50f-18dd52c429fa|#3 Celtic Peak> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_ca22955f-5be8-4118-a617-cdaea078565e|#4 Peter's abiti da lavoro S.R.L.S> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_79aa5a31-ac2c-46e4-b398-79fb97595da6|#5 ashwoodcollective> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_d8ce5aa4-f80d-4820-b4cb-d00ee93ba0ca|#6 My Store 2> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_8b7e60c6-0a9a-44b5-bb29-019f847dacb3|#7 Bliyt > · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_f366a449-1ee9-4718-801d-12f5ac343d8c|#8 Airway Eesti> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_b42f0e5f-00f1-412d-bd0b-24577888d86b|#9 A Modern Take> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_8f5b0ab6-8911-4e59-8933-22235229d108|#10 IN SU LEE> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_e0042121-7db0-458c-b272-47cf0b3be435|#11 Hoi Chew> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_dc9f03cc-94b1-4eb8-bc13-88586df470bb|#12 Loomi | The Sanctuary>