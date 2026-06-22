# QA Tuần 2026-W25 — Linda (Joy + Chatty)
**Tuần 15/06 – 21/06/2026** · coaching, không phải penalty

## 📊 Điểm tuần: 83/100 — Tốt  (= 0 so với W24: 83)
🔍 Đã QA: 30 chat

**Breakdown 3 trục:** 🧠 Mindset 26.9/34 · 📚 Kiến thức 28.8/33 · 🛠️ Xử lý 27.0/33  →  trục yếu nhất: **mindset**

## 📝 Nhận xét chung
Linda hoàn thành W25 với 30 chats, giữ nguyên mức Tốt (83) so với W24 (83). Điểm mạnh rõ nhất là knowledge — tư vấn đúng về plan, features, và escalation. Mindset nhìn chung ổn, chủ động DFY setup nhiều chats, nhưng vẫn có vài lần xin review hơi sớm khi vấn đề chưa confirm xong. Lỗi cần focus nhất tuần này: KN1 (typo lặp lại) và KN5 (đọc nhầm thông tin khách, chat #4) — cả hai xuất hiện ở nhiều chats, cần chủ động kiểm tra trước khi gửi.

## ✅ Điểm tốt
- [P1] DFY setup chắc tay và chủ động — không chỉ làm theo yêu cầu mà còn enable thêm AI Re-engage, Follow-up Messages, Custom Knowledge, support email mà không cần được hỏi. (#2 #3 #14 #19 #30)
- [P2] Ownership cao trong các case bug phức tạp — theo dõi xuyên suốt nhiều ngày, update khách chủ động, viết email follow-up rõ ràng và đầy đủ context. (#23 #24 #28)
- [P3] Xin review đúng thời điểm ở hầu hết các chat phù hợp — sau khi khách confirm hài lòng hoặc nói 'thank you / it works', không ép. (#6 #9 #22 #24)
- [P4] Tư vấn plan chính xác — chat #10: 'On the Basic plan at $19.99/month, you can have up to 5 team members' đúng theo bảng giá Chatty Basic. (#10)

## 🔧 Cần cải thiện
- [KN1] (Moderate) Typo lặp lại ở nhiều chats — pattern này đã xuất hiện từ W24 và chưa được khắc phục. Các lỗi đều ở câu ngắn, routine, cho thấy bạn chưa proofread trước khi send. (#4 #16 #25)
   • Dẫn chứng: Chat #4: 'I can better undestand your request' | Chat #25: 'could you help me double-chẹc it on your end?' | Chat #16: 'Goos news, I wanted to let you know...'
   → Tạo text shortcut cho các câu hay dùng ('better understand', 'double-check', 'Good news') để tránh typo tái diễn. Trước khi gửi bất kỳ câu nào, đọc lại 1 lần.
- [KN5] (Low) Đọc nhầm thông tin khách dẫn đến tư vấn lạc hướng — khách nói rõ ý nhưng bạn hiểu sai, phải sửa lại. (#4)
   • Dẫn chứng: Chat #4: Khách nói 'only 10kb' để mô tả kích thước email, Linda reply: 'I see that you mentioned it includes a 10KB video' — khách phải đính chính 'the 10kb refers to that message'.
   → Với các thông tin kỹ thuật (file size, error code, order number), quote lại câu khách nói trước khi kết luận để tránh hiểu nhầm.
- [KN3] (Low) Lệch ngôn ngữ — khách gửi tiếng Pháp nhưng Linda reply bằng tiếng Anh, khiến khách phải tự dịch. (#15)
   • Dẫn chứng: Chat #15: Khách Nina Moretti nhắn 'quand je mets le bloc faq j'ai pas le rendu que j'ai fait sur l'application avec les bonnes couleurs et tout' (tiếng Pháp), Linda trả lời bằng tiếng Anh hoàn toàn trong các tin tiếp theo.
   → Khi khách dùng một ngôn ngữ khác tiếng Anh, reply bằng ngôn ngữ đó hoặc ít nhất acknowledge bằng ngôn ngữ đó. Crisp hỗ trợ translate nhưng bạn nên chủ động match ngôn ngữ khách.
- [QT9] (Low) Xin review khi vấn đề chưa được confirm xong — khách chưa verify kết quả mà đã được hỏi review, tạo cảm giác thiếu chuyên nghiệp. (#17 #18)
   • Dẫn chứng: Chat #17: Linda gửi 'May I ask for a small favour?' và link review sau khi escalate lên TS nhưng trước khi TS fix xong và khách confirm. | Chat #18: Review ask gửi ngay sau khi set up notifications nhưng trước khi khách verify notifications hoạt động.
   → Chỉ xin review sau khi nhận được tín hiệu hài lòng từ khách (confirm 'it works', 'thank you', 'all good'). Nếu vấn đề đang pending với TS, đợi đến khi close ticket.

## 🌟 Xin review (chỉ ghi nhận, KHÔNG tính điểm)
- Đã xin 5/5 chat phù hợp. 4 chats excluded vì ĐÃ CÓ review (Shopify): #1, #21, #25, #27. Trong 26 chats còn lại, 5 chats có khách confirm hài lòng rõ ràng — Linda xin đủ 5/5, đúng lúc ở cả 5. Thêm 2 lần xin ở trạng thái pending/chưa confirm (#17, #18) — mistimed. Tuần này xin review tốt hơn W24, timing cải thiện rõ.

## 📈 So với tuần trước
Điểm giữ nguyên W24→W25: 83→83. KN1 (typo) lặp lại từ W24 — đây là lỗi cần ưu tiên fix nhất vì đã 2 tuần liên tiếp. QT25/QT9 (xin review sai thời điểm) giảm từ 2 lần xuống còn 2 lần nhưng pattern khác hơn — tiến bộ nhẹ. Mindset tăng nhẹ (24.0→26.9), Skill ổn định. Knowledge vững (29.0→28.8). Điểm kéo dài ở 83 cho thấy Linda đang ở mức plateau — cần break qua bằng cách xử lý dứt điểm KN1.

## 🔗 Chat đã QA
<https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_dad0823c-fa8e-4985-ac43-751a2fcdc0a0|#1 vivoonlinestore> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_ef0f5078-cc2e-4dc7-b78c-c596ea73b59b|#2 Jaipuri Craft> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_b34265e0-13f9-4e7f-bb84-39c3b1eec5b1|#3 Cervly> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_56d67564-ce2a-4720-8da9-1966d8d6af1d|#4 1byone Audio> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_e0808926-6ced-4439-b2f5-91782b9e017b|#5 holosport> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_2e25a714-21f2-43c5-a163-66a399193ecf|#6 Keskine> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_5da47018-9194-40b2-8bb1-7c72517a8ce0|#7 Early Learning Centre> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_ee53c126-ff9c-486e-9f25-c40d3f446cff|#8 Vincent Daimon> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_a23c7267-f7fa-4a69-bb38-9ee0ed494e66|#9 Viherpeukalot.fi> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_9cef3480-1d23-403d-b837-236e09e9f321|#10 Pebble & Co> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_0af0e7e4-9a2c-4201-8951-1f75e41fc319|#11 Xtra Store> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_ba50da7f-69d1-4afd-9224-3f6f72d0b469|#12 VTOP Gaming>