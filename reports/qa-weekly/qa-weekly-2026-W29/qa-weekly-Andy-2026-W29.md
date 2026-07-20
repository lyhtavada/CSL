# QA Weekly — Andy — 2026-W29 (13/07 – 19/07/2026)

**Điểm tuần:** 85/100 — Tốt  (▼ -4)  
**Đã QA:** 29 chat (loại 1)

| Trục | Điểm TB |
|---|---|
| 🧠 Mindset | 29.5/34 |
| 📚 Kiến thức | 27/33 |
| 🛠️ Xử lý | 28.5/33 |

## 📝 Nhận xét chung

Andy là CS mạnh về mindset và kỹ năng xử lý — ownership rõ, kiên nhẫn với case dài/khó (compliance B2B ở #18, bug đa ngôn ngữ ở #23, #26), chủ động thêm giá trị và tạo được thiện cảm thật khiến khách tự nguyện để lại review. Điểm cần thẳng thắn nhìn nhận: ở chat #5 báo sai giới hạn ngôn ngữ của gói Basic/Pro ngay trong lúc tư vấn nâng cấp — đây là lỗi kiến thức nặng nhất tuần vì trực tiếp ảnh hưởng quyết định mua của khách, không phải lỗi vặt nên cần ưu tiên sửa: luôn tra KB trước khi chốt số liệu giới hạn/giá, đừng dựa vào trí nhớ. Ngoài ra vài lỗi chính tả nhỏ khi trả lời nhanh — không nghiêm trọng nhưng nên soát lại câu trước khi gửi.

## ✅ Điểm tốt tuần này

- Ownership rõ, nhận trách nhiệm thay cả đồng đội — chat #27, khi khách quay lại vì đồng nghiệp quên báo update: "It seems like my teammate forgot to share the updates with you 😭" rồi khắc phục ngay thay vì đổ lỗi. Cũng thấy rõ ở các case dài (ví dụ #5 truy investigation email-forwarding, #23 SKU tiếng Hungary) — theo tới cùng nhiều vòng lặp, không bỏ ngang. (#27, #5, #23)
- Trung thực với kiến thức, không bịa khi không chắc — case bảo mật B2B dài hơi #18: thay vì vẽ ra chứng nhận không có, Andy nói thẳng "Chatty does not currently hold formal security certifications such as SOC 2 or ISO 27001... we are still in the process of scaling" và giải thích rõ các biện pháp bảo mật thực tế đang có. Đây là cách xử lý đúng, giữ uy tín lâu dài với khách doanh nghiệp. (#18)
- Chủ động thêm giá trị ngoài yêu cầu — chat #20 tự phát hiện và khuyến nghị khách bổ sung Shipping/Return Policy còn thiếu trên site để AI trả lời chính xác hơn dù khách không hỏi; chat #1 chủ động gợi ý tính năng Subscribe pop-up phù hợp hơn cho site khách. (#20, #1)
- Tone ấm áp, tạo thiện cảm thật (không sáo rỗng) giúp khách chủ động để lại review 10/10 — chat #7 khách nói "I probably wouldnt even write a review if it wasnt for u"; chat #1 khách gọi Andy là "champion". (#7, #1)

## 🔧 Cần cải thiện

- **[KT1] Critical** — Báo sai giới hạn ngôn ngữ của các gói trả phí khi tư vấn nâng cấp — số liệu CAO HƠN KB thật (không phải giá legacy, mà limit ngược chiều làm khách kỳ vọng sai và có thể mua nhầm gói). (#5)
  - Dẫn chứng: Chat #5, Andy: "Please note that the Free plan only supports displaying 1 language and the Basic plan will support displaying 3 languages" và "If you want more than 3 languages, the Pro plan supports up to 10 languages" — KB thật (kb/faq/translation.md): Free=1, Basic=2, Pro=9 ngôn ngữ.
  - → Khi tư vấn giới hạn theo gói (đặc biệt lúc đang gợi ý nâng cấp), luôn tra lại KB/pricing trước khi báo số cho khách, tránh nhớ nhầm số liệu vì đây trực tiếp ảnh hưởng quyết định mua hàng của khách.
- **[KN1] Low** — Vài lỗi chính tả/ngữ pháp nhỏ lặp lại trong câu trả lời khách, làm câu đọc hơi vấp dù không ảnh hưởng nội dung chính. (#11, #19)
  - Dẫn chứng: Chat #11: "It mighe due to an cache issue on your current browser" (mighe→might, an→a); Chat #19 (Colorfulkoala): "I would need our tech team to check further to better understanding the issue" (better understanding→better understand).
  - → Đọc lại câu trước khi gửi với các case đang gõ nhanh/liên tục nhiều case cùng lúc, đặc biệt câu mở đầu xử lý case mới.

## 🌟 Xin review (chỉ ghi nhận, KHÔNG tính điểm)

- Đã xin review ở **6/9** chat phù hợp (đúng lúc: 5, sai lúc: 1)
- Đã xin review đúng lúc ở 5/9 chat phù hợp (chat #7, #13, #15, #16, #24 — đều lúc khách vừa hài lòng/cảm ơn, tỷ lệ chuyển đổi tốt vì tone tự nhiên). 1 lần xin hơi sớm ở chat #6 khi khách còn đang test, khách nói sẽ để review sau — không sai nhưng cần đọc tín hiệu khách kỹ hơn. Bỏ lỡ vài chat vàng (khách hài lòng nhưng chưa thấy Andy xin) ở #3, #12, #21.
- Chat KH đã có review thì không cần xin lại — đã loại khỏi đếm.

## 📈 So với tuần trước

- Điểm 89 → 85 (▼ -4)
- Lỗi tuần trước đã hết: KN3, KN6, QT22, QT25 👏

## 🚨 Flag cho Liz

- KT1 — Chat #5: báo sai giới hạn ngôn ngữ theo gói (Basic 3 thay vì 2, Pro 10 thay vì 9) lúc đang tư vấn nâng cấp — cần Liz review để coaching riêng và double-check khách #5 chưa bị ảnh hưởng quyết định mua
