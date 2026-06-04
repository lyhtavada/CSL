# QA Tuần 2026-W22 — Phoebe
**Giai đoạn:** 26/05 – 01/06  
**Điểm:** 87/100 — Tốt  
**Đã QA:** 10 chat  
**Phân bố:** 🌟5 ✅3 🟡1 🟠0 🔴1 ⛔0

## 📝 Nhận xét chung
Phoebe có tuần làm việc khá ổn — xử lý đa dạng tình huống từ onboarding đơn giản đến case kỹ thuật phức tạp kéo dài nhiều ngày, và thường chủ động hơn mức yêu cầu (tự check knowledge base, resync URL, test lại sau khi fix). Điểm mạnh rõ nhất là khả năng tổng hợp và viết update có cấu trúc khi case phức tạp — khách hiểu được tình trạng mà không cần hỏi lại. Điểm cần tập trung: đọc kỹ thông tin khách đã cung cấp trước khi hỏi lại — ở chat #8, bạn hỏi confirm email sai (help@anderic.com thay vì tienyin@jumix.com.my đã được khách nêu rõ), buộc khách phải đính chính và tạo ấn tượng không chú ý lắng nghe. Lỗi này tuy nhỏ nhưng xảy ra trong bối cảnh case nhạy cảm (chuyển quyền admin) nên hệ quả nặng hơn bình thường.

## ✅ Điểm tốt
- **[P2]** Chủ động phát hiện và xử lý vấn đề trước khi khách hỏi: tự enable Products sync và resync URL bị stuck trong chat #4 và #6, tự resync Custom Knowledge pages bị In Progress trong chat #1 mà không cần được yêu cầu. (#1, #4, #6)
- **[P3]** Giải thích rõ ràng, có cấu trúc trong các case phức tạp. Đặc biệt ở chat #1, bản update 17:03:57 liệt kê 3 điểm rõ ràng (Custom Scenario vs Transfer to Human, Follow-up Questions, Conflicts with Built-in Skills) kèm screenshot và link kết quả test — khách không cần hỏi thêm. (#1, #7)
- **[P5]** Đọc context tốt khi bàn giao — chat #1 là case kỹ thuật phức tạp kéo dài nhiều ngày qua nhiều CS, Phoebe nắm tình huống nhanh và tiếp tục đúng điểm cần xử lý mà không bắt khách giải thích lại. (#1, #7)

## 🔧 Cần cải thiện
- **[KN5 · High]** Đọc nhầm thông tin khách đã cung cấp — xác nhận sai email cần thay đổi, buộc khách phải đính chính
  - *Dẫn chứng:* CS (Phoebe) [12:07:47]: "From help@anderic.com to mshepharma@mahsahospital.com, am I correct?" — trong khi Customer [12:08:15] đã nói rõ: "from tienyin@jumix.com.my to mshepharma@mahsahospital.com"
  - → Trước khi confirm thông tin, scroll lại chat để đọc đúng câu khách vừa nói. Trong case liên quan admin/email/quyền truy cập, sai một chữ có thể gây hậu quả nghiêm trọng — cần đặc biệt cẩn thận.
- **[KN1 · Low]** Câu thiếu tự nhiên, ngữ pháp lúng túng làm giảm tính chuyên nghiệp của tin nhắn
  - *Dẫn chứng:* CS (Phoebe) [15:07:26]: "Normally, users forgot to change the Conversation Starter default content here."
  - → Sửa thành "Most merchants forget to update the Conversation Starter content by default." Khi dùng tiếng Anh trong bối cảnh onboarding trang trọng, cần proofread trước khi gửi — câu sai ngữ pháp ảnh hưởng đến uy tín app.

## 📈 So tuần trước
Tuần đầu, chưa có dữ liệu so sánh.