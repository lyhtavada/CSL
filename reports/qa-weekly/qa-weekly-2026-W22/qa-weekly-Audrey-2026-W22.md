# QA Tuần 2026-W22 — Audrey
**Giai đoạn:** 26/05 – 01/06  
**Điểm:** 84/100 — Đạt  
**Đã QA:** 30 chat  
**Phân bố:** 🌟3 ✅25 🟡0 🟠1 🔴1 ⛔0

## 📝 Nhận xét chung
Audrey có nền tảng kỹ năng chat chắc — tone ổn định, chủ động xử lý, và nhiều ca cho thấy khả năng đọc context tốt (tự phát hiện vấn đề, fix trước khi khách hỏi). Điểm mạnh rõ nhất là proactive: chat #3 và #15 là những ví dụ thực sự nổi bật. Điểm cần tập trung ngay: đọc kỹ thông tin khách đã cung cấp trước khi đưa ra giả định về store hoặc vấn đề — chat #1 cho thấy việc đoán sai URL khi context đã đầy đủ làm khách phải đính chính hai lần, mất thời gian và để lại ấn tượng xử lý ẩu. Chat #27 cũng cho thấy pattern tương tự: check store xong rồi nhận xét sai hướng, khách phải chỉnh lại. Hai trường hợp này không phải tai nạn ngẫu nhiên — chúng phản ánh thói quen bỏ qua bước đọc lại context trước khi hành động.

## ✅ Điểm tốt
- **[P2]** Chủ động phát hiện vấn đề khách chưa hỏi — chat #3: thấy loyalty button bị gift button che và tự đề xuất đổi vị trí ngay, không chờ khách report; chat #15: phát hiện setting 'display after login' là nguyên nhân widget không hiển thị và xử lý luôn. (#3, #15)
- **[P3]** Hướng dẫn kỹ thuật theo từng bước, rõ ràng và có thể làm theo ngay — chat #8: giải thích SPF record, chỉ rõ đúng bản ghi TXT nào cần sửa (tránh bản ghi Google Site Verification), test email delivery xong rồi mới đóng; khách confirm thành công. (#8)
- **[P5]** Đọc kỹ context trước khi trả lời — chat #3: nắm ngay vấn đề widget bị che, không bắt khách lặp lại; chat #15: vào store kiểm tra trước, xác định nguyên nhân chính xác ('only display after login') mà không hỏi vòng vòng. (#3, #15)
- **[P4]** Xử lý các ca multi-thread phức tạp (nhiều issue song song, nhiều ngày) gọn gàng và theo dõi đến nơi — chat #18 và #13: tổng hợp outstanding items, cập nhật khách đúng hạn, không để issue lọt giữa chừng. (#13, #18)

## 🔧 Cần cải thiện
- **[KN5 · High]** Xác định sai store khi context đã rõ, khiến khách phải đính chính hai lần
  - *Dẫn chứng:* CS (Audrey): 'Ah, asumo que te gustaría cambiar el enlace de inicio de sesión para este sitio web https://aguascalientes-travel.myshopify.com/password' — trong khi khách đã nói rõ nhiều lần muốn chỉnh link trên nekane.mx
  - → Trước khi đưa ra giả định về store/URL, scroll lên đọc lại toàn bộ những gì khách đã cung cấp trong chat. Nếu khách đã nêu URL cụ thể, dùng đúng URL đó — không đoán.
- **[KN7 · Moderate]** Câu hỏi của khách đã khá rõ nhưng vẫn hỏi lại 'I'm not sure I understood your question correctly', rồi khi check store lại tập trung vào trạng thái draft milestone hiện tại thay vì câu hỏi về behavior khi xóa/tạo lại — khách phải đính chính: 'My question has nothing to do with the current draft'
  - *Dẫn chứng:* CS (Audrey): 'I'm not sure I understood your question correctly. To better assist you, could you please elaborate a bit more?' sau câu hỏi: 'If it is deleted and recreated, will the purchase data collection be reset?' — 
  - → Khi khách hỏi về behavior/logic của app, ưu tiên trả lời từ kiến thức sản phẩm trước, chỉ check store khi cần data cụ thể. Đừng nhầm 'kiểm tra store' với 'trả lời câu hỏi'. Nếu thực sự không rõ, tóm tắt lại hiểu của mình trước khi hỏi thêm.

## 📈 So tuần trước
Tuần đầu, chưa có dữ liệu so sánh.