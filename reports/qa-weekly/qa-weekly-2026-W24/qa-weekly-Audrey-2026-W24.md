# QA Tuần 2026-W24 — Audrey
**App:** Joy · **Kỳ:** 08/06 – 14/06/2026

## 📊 Điểm tuần: 87/100 — Tốt  (▲ +4 so với W23: 83)
- 🧠 Mindset 28.3/34 · 📚 Kiến thức 29.6/33 · 🛠️ Xử lý 28.8/33
- 🔍 Đã QA: 19 chat (loại 1)
- Trục yếu nhất: **Mindset**

## 📝 Nhận xét chung
Audrey có một tuần ổn định — ownership tốt, biết theo đuổi vấn đề tới cùng và handoff rõ ràng. Kiến thức sản phẩm chắc, đặc biệt với các câu hỏi về Klaviyo segment, exclusive deal vs Perks, và customer merge. Điểm cần cải thiện: một lần nói 'all set' trước khi thật sự xác nhận fix xong (chat #4), và một lần chuyển sang tiếng Anh khi khách hàng đang dùng tiếng Pháp (chat #11).

## ✅ Điểm tốt
- Ownership tốt — theo dõi vấn đề phức tạp đến khi xong. Ví dụ chat #7: tự mình migrate điểm từ Smile, double-check kết quả, giải thích rõ lý do hiển thị chưa cập nhật, và follow-up ngay khi dev team sync lại data. (#7 #15)
- Giải thích kỹ thuật rõ ràng, có cơ sở. Ví dụ chat #15: 'The issue happens when a customer places an order before logging in (guest checkout). Joy creates a "guest" record linked to their email. Later, when the customer creates an official Shopify account, Joy generates a brand new "member" record' — đúng và giúp khách hàng hiểu nguyên nhân gốc rễ. (#13 #15)
- Proactive upsell tự nhiên — không bị gượng. Chat #5: vừa xử lý bug first name lại chủ động offer customized widget, chat #7: đề xuất G2 review đúng lúc sau khi migration thành công và khách hài lòng. (#5 #7 #14)

## 🔧 Cần cải thiện
- **[QT25] · Moderate** Báo 'all set' khi vấn đề chưa thật sự được giải quyết xong. Khách test lại và vẫn bị lỗi redirect. (#4)
   > CS (Audrey): 'You're very welcome! Actually it's all set now! Could you please help me reload the page and check it again on your end?' — nhưng ngay sau đó [14:51:20] Customer: 'Hi Audrey, I've refreshed the page and tried a new coupon, it is still taking me to the page'
   → Trước khi báo khách 'all set', tự test hoặc xác nhận với dev team rằng fix đã apply thật sự. Nếu chưa chắc, dùng: 'The team is applying the fix now, could you check in about 5–10 minutes and let me know?'
- **[KN3] · Low** Lệch ngôn ngữ — khách đang chat bằng tiếng Pháp nhưng Audrey kết thúc bằng tiếng Anh, khiến khách phải đọc ngôn ngữ khác. (#11)
   > Customer (Chloé Cartier): 'c'est parfait merci!' — CS (Audrey): 'Is there anything else I can help you with today?' (tiếng Anh). Toàn bộ conversation trước đó Audrey đang dùng tiếng Pháp.
   → Duy trì ngôn ngữ nhất quán với khách trong suốt conversation. Nếu Crisp đang live-translate, chỉ cần nhập tiếng Việt/Anh và để máy dịch — không tự switch sang tiếng Anh giữa chừng.
- **[KN1] · Low** Typo nhỏ trong câu trả lời. (#5)
   > CS (Audrey): 'You're vert welcome!' (thay vì 'very')
   → Đọc lại tin nhắn trước khi gửi, đặc biệt là câu chốt kết thúc — đây là ấn tượng cuối cùng của khách về cuộc trò chuyện.

## 🌟 Xin review (chỉ ghi nhận, KHÔNG tính điểm)
- Đã xin 3/3 chat phù hợp (đúng lúc 3, chưa đúng lúc 0).
- Audrey xin review đúng lúc ở cả 3 chat phù hợp — đều sau khi vấn đề được giải quyết xong và khách tỏ ra hài lòng. Chat #14 ('dạ uki mình hiểu rồi, mình cảm ơn ạ') và chat #15 ('All good thank you!') là thời điểm vàng và Audrey không bỏ lỡ. Lưu ý nhỏ: chat #15 Audrey có nhờ nhắc tên 'Audrey and William' trong review — về tinh thần ổn, nhưng nên để tự nhiên hơn, không nhất thiết phải gọi tên cụ thể.

## 📈 So với tuần trước (W23)
- Điểm 83 → 87 (▲ +4)
