# QA Tuần 2026-W22 — Hazel
**Giai đoạn:** 26/05 – 01/06  
**Điểm:** 87/100 — Tốt  
**Đã QA:** 30 chat  
**Phân bố:** 🌟5 ✅24 🟡1 🟠0 🔴0 ⛔0

## 📝 Nhận xét chung
Tuần này bạn xử lý ổn định trên toàn bộ mẫu 30 chat, không có lỗi nghiêm trọng nào. Điểm mạnh rõ nhất là khả năng giải thích kỹ thuật có cấu trúc — đặc biệt ở những case phức tạp như metafields (chat #7), Firebase deferred loading (chat #22) hay hướng dẫn setup AI cho Timesaver Kitchen (chat #9). Bạn đọc context tốt, ít bắt khách giải thích lại, và nhìn chung xử lý đúng flow. Điểm cần tập trung: ngôn ngữ nhất quán trong suốt cuộc trò chuyện — ở chat #11 bạn chuyển sang tiếng Anh trong một cuộc chat đang chạy hoàn toàn bằng tiếng Tây Ban Nha, điều này làm khách phải đọc tin nhắn không khớp ngữ cảnh. Đây không phải lỗi lớn nhưng ảnh hưởng trực tiếp đến trải nghiệm người dùng — hãy kiểm tra lại ngôn ngữ của khách trước khi gửi tin trong ca bàn giao.

## ✅ Điểm tốt
- **[P3]** Giải thích kỹ thuật rõ ràng, có cấu trúc — đặc biệt nổi bật ở chat metafields (đúng loại Metaobject không hỗ trợ, workaround cụ thể) và chat Firebase deferred init (trả lời đầy đủ 3 câu hỏi kỹ thuật của Nils với cả gotcha và API entry point). (#7, #22, #9)
- **[P5]** Đọc context tốt khi tiếp nhận ca: ở chat #7 ngay lập tức xác định đúng loại metafield từ JSON data khách gửi; ở chat #22 nắm đúng yêu cầu deferred loading mà không yêu cầu khách giải thích lại. (#7, #22)
- **[P4]** Xử lý gọn, đúng flow ở những chat không cần nhiều bước — chat #20 (export chat history) và chat #8 (AI catalogue sync) được giải quyết nhanh, đúng trọng tâm, không hỏi thừa. (#20, #8, #24)
- **[P2]** Chủ động thêm giá trị ngoài yêu cầu: ở chat #9 chủ động enable Products trong Training Data và thêm instruction cho merchant; ở chat #18 chủ động khuyến nghị bật 'Automatic assignment in order' để tránh mất chat. (#9, #18)

## 🔧 Cần cải thiện
- **[KN1 · Low]** Chuyển ngôn ngữ không nhất quán giữa cuộc chat — gửi tin bằng tiếng Anh trong cuộc trò chuyện đang chạy hoàn toàn bằng tiếng Tây Ban Nha, làm khách phải đọc tin nhắn lạc ngôn ngữ.
  - *Dẫn chứng:* CS (Hazel): 'I saved it for you. Please help me reload the page and double-check it on your side' — gửi bằng tiếng Anh trong khi toàn bộ cuộc chat #11 (MUS) đang diễn ra bằng tiếng Tây Ban Nha.
  - → Trước khi gửi tin trong ca bàn giao, kiểm tra ngôn ngữ của tin nhắn gần nhất của khách. Nếu khách chat bằng tiếng Tây Ban Nha (hoặc bất kỳ ngôn ngữ nào), giữ nguyên ngôn ngữ đó trong toàn bộ ca trực của bạn.

## 📈 So tuần trước
Tuần đầu, chưa có dữ liệu so sánh