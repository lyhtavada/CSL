# QA Weekly — Hazel — 2026-W29 (13/07 – 19/07/2026)

**Điểm tuần:** 82/100 — Tốt  (▼ -4)  
**Đã QA:** 30 chat

| Trục | Điểm TB |
|---|---|
| 🧠 Mindset | 27.8/34 |
| 📚 Kiến thức | 28.3/33 |
| 🛠️ Xử lý | 25.8/33 |

## 📝 Nhận xét chung

Tuần này bạn xử lý một lượng chat setup/DFY và bug report rất lớn, nhiều case dài và phức tạp (SKYROVER chat #25 kéo dài nhiều ngày với hàng loạt lỗi kỹ thuật), và điểm mạnh rõ nhất là ownership — theo tới cùng, cập nhật khách đều đặn, không đóng chat lửng. Kiến thức sản phẩm khá vững, đối chiếu KB thì các claim về giá/limit (Free 200 sản phẩm, Pro 8.000, Plus unlimited) đều đúng. Điểm cần siết lại nằm ở trục Kỹ năng: có ít nhất 2 lần gửi nhầm ngôn ngữ cho khách (tiếng Serbia cho khách Hy Lạp ở chat #5, tiếng Hy Lạp cho khách tiếng Anh ở chat #1) khiến khách phải hỏi lại "sorry what does this mean" — đây là lỗi có thể tránh nếu đọc lại tin trước khi gửi. Ngoài ra một vài chat (ví dụ #8) khách phàn nàn ứng dụng "quá phức tạp" vì bạn xử lý vòng vo, cần confirm rõ yêu cầu trước khi đi vào chi tiết kỹ thuật.

## ✅ Điểm tốt tuần này

- Ownership mạnh — theo đuổi vấn đề tới cùng, chủ động follow-up không để khách chờ mà không có cập nhật, kể cả với case kéo dài nhiều ngày/nhiều lỗi kỹ thuật liên tiếp (chat #25 SKYROVER, #3 Cornerstone, #9 GOKUMIN, #30 ExBrite — tự tìm ra field 'Inventory status description' gây lỗi email sai và sửa tận gốc). (#25, #3, #9, #30)
- Trung thực về giới hạn sản phẩm, không thổi phồng — nói rõ khi tính năng chưa có (A/B test widget ở chat #16, AI không đọc được filter trang sản phẩm ở chat #11) thay vì hứa suông; đúng với KB pricing khi tư vấn nâng cấp plan (chat #5). (#16, #11, #5)
- Giữ bình tĩnh, không phản ứng lại khi khách bực/áp lực — ví dụ khách Đức dọa gỡ AI vì lỗi (chat #13), khách Pháp than app 'quá phức tạp' (chat #8) — vẫn xử lý ôn hòa, không đôi co. (#13, #8)
- Hướng dẫn có bước rõ ràng, dễ làm theo — ví dụ hướng dẫn quy trình review/update AI knowledge base 3 bước chi tiết ở chat #30, hướng dẫn phân biệt Conversation Starters vs FAQs ở chat #1. (#30, #1)

## 🔧 Cần cải thiện

- **[KN3] Moderate** — Gửi nhầm ngôn ngữ cho khách — chat tiếng Hy Lạp nhưng gửi câu tiếng Serbia, khiến khách phải hỏi lại/khó hiểu. (#5)
  - Dẫn chứng: [15:06:27] CS (Hazel): Evo što se dešava kada kupac pita o proizvodu koji AI nije naučio. U tom slučaju, AI neće imati nikakve informacije o proizvodu, pa neće moći dati odgovor.
  - → Đọc lại tin nhắn trước khi gửi, đặc biệt khi dùng công cụ dịch — nếu không chắc ngôn ngữ đúng thì kiểm tra lại 1 lần trước khi bấm gửi.
- **[KN3] Moderate** — Gửi từ tiếng Hy Lạp 'Ευχαριστώ' (nghĩa 'cảm ơn') cho khách nói tiếng Anh, khách không hiểu và phải hỏi lại, làm gián đoạn chat. (#1)
  - Dẫn chứng: [14:55:05] CS (Hazel): Ευχαριστώ ... [14:59:28] Customer (LASH GLO): sorry what does this mean Ευχαριστώ
  - → Trước khi gửi câu ngắn/lời cảm ơn, kiểm tra lại đúng ngôn ngữ khách đang dùng thay vì tin tưởng hoàn toàn vào tool dịch.
- **[QT9] Moderate** — Xử lý vòng vo khi khách hỏi vấn đề FAQ không hiện — khiến khách bực và nhận xét app 'trở nên phức tạp', phải hỏi lại nhiều lần 'vous avez compris mon besoin ou non?' trước khi Hazel escalate. (#8)
  - Dẫn chứng: [17:59:23] Customer: franchement la configuration de votre application est devenue compliquée. Il y a quelques années elle etait facile. ... [18:13:00] Customer: vous avez compris mon besoin ou non ?
  - → Khi khách mô tả vấn đề chưa rõ, confirm lại chính xác yêu cầu (paraphrase) ngay từ đầu thay vì thử nhiều hướng rồi mới hỏi lại, giúp tiết kiệm thời gian và tránh khách bực.
- **[KN1] Low** — Câu chào tạm biệt lặp lại lỗi ngữ pháp 'Wishing you enjoy the rest of the day!' (thiếu 'a'/'to') ở nhiều chat khác nhau. (#1, #3)
  - Dẫn chứng: [16:00:49] CS (Hazel): Got it. Wishing you enjoy the rest of the day!
  - → Sửa thành mẫu câu chuẩn 'Wishing you a great rest of the day!' và lưu làm quick-reply cố định để tránh lặp lỗi.
- **[KN1] Low** — Gửi sai domain của app khi trả lời khách (app.meetchatty.com thay vì app.chatty.net đúng theo KB). (#20)
  - Dẫn chứng: [05:19:12] CS (Hazel): ...bạn có thể chuyển đổi cửa hàng trong app.meetchatty.com...
  - → Double-check lại URL/domain chính xác trước khi gửi cho khách, nhất là thông tin liên quan tới đăng nhập.

## 🌟 Xin review (chỉ ghi nhận, KHÔNG tính điểm)

- Đã xin review ở **8/13** chat phù hợp (đúng lúc: 8, sai lúc: 0)
- Đã xin review đúng lúc ở 8/13 chat khách hài lòng (ngay sau lời cảm ơn) — làm tốt phần timing khi có xin. Tuy nhiên còn bỏ lỡ khoảng 5 chat vàng (khách rất hài lòng, ví dụ chat #4, #18) mà không chủ động xin — có thể tận dụng thêm.
- Chat KH đã có review thì không cần xin lại — đã loại khỏi đếm.

## 📈 So với tuần trước

- Điểm 86 → 82 (▼ -4)
- Lỗi lặp lại từ 2026-W28: KN1, KN3, QT9 — cần ưu tiên sửa
- Lỗi tuần trước đã hết: QT18 👏
