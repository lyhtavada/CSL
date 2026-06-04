# QA Tuần 2026-W22 — Linda
**Giai đoạn:** 26/05 – 01/06  
**Điểm:** 80/100 — Đạt  
**Đã QA:** 22 chat  
**Phân bố:** 🌟1 ✅14 🟡5 🟠1 🔴1 ⛔0

## 📝 Nhận xét chung
Em rất linh hoạt đa ngôn ngữ và chủ động đề xuất cho khách — đó là điểm mạnh đáng quý. Tuần này điểm bị kéo xuống chủ yếu do lỗi chính tả/typo lặp lại và sót placeholder template. Đây là thứ dễ sửa nhất: đọc lại 1 lượt trước khi gửi, dùng shortcut chuẩn cho câu mở đầu. Sửa được phần này điểm em sẽ lên rõ.

## ✅ Điểm tốt
- **[P2]** Rất chủ động: ở chat #1 sau khi bật AI cho email channel, mình tự đề xuất thêm các setting hữu ích (auto re-assign, lọc spam để tiết kiệm AI conversation limit) mà KH chưa kịp hỏi — KH đồng ý 'Enable this!' (chat #1)
- **[P3]** Giải thích rõ ràng có bước: chat #13 tìm ra đúng nguyên nhân KH không downgrade được ('please select Continue to Downgrade instead of Keep Current Plan') khiến KH nhận ra mình nhầm; chat #4 giải thích mạch lạc xung đột Ciwi Translator dịch metafield avada_faq làm hỏng JSON khiến widget không hiện (chat #4, chat #13)
- **[P1]** Giữ tone ấm và bình tĩnh khi KH gấp/căng: chat #9 KH stress vì sắp vào giờ ra đơn ('ICON位置挡住这个问题非常致命'), mình vẫn trấn an, báo thời gian cụ thể và xử lý từng bước; chat #18 (HammerHouse) kiên nhẫn qua chuỗi feedback rất dài (chat #9, chat #18)
- **[P4]** Đa ngôn ngữ linh hoạt, đi thẳng vấn đề đúng ngôn ngữ KH: trả lời mượt bằng tiếng Trung (#2, #5, #7, #9), tiếng Thụy Điển (#1), tiếng Đức (#12, #16) đúng flow (chat #1, chat #2, chat #7, chat #12)

## 🔧 Cần cải thiện
- **[KN5 · High]** Hiểu sai yêu cầu KH rồi định escalate trước khi nắm rõ vấn đề. KH chỉ hỏi có setting nào để lazy-load app không, nhưng mình lại hiểu thành 'app làm chậm trang' và báo đang check với tech team — KH phải đính chính.
  - *Dẫn chứng:* KH: 'I just need to know if you have a way (through some settings) to lazy load the app... it slows down the loading of my page' → trước đó CS: 'we're currently checking with our technical team...' và
  - → Trước khi chốt hướng xử lý hay đẩy tech team, confirm lại đúng 1 câu yêu cầu của KH ('Ý anh là muốn tìm setting lazy-load đúng không ạ?'). Khi nắm rõ, mình đã trả lời rất tốt (app đã có lazy load) — chỉ cần confirm sớm hơn.
- **[KN7 · Moderate]** Trả lời chung chung, chưa giải quyết trực tiếp câu hỏi. KH hỏi 3 lần cách đơn giản nhất để có vài review cho sản phẩm, nhưng câu trả lời lại xoay sang gợi ý set scenario AI gửi review request — không đúng trọng tâm KH cần.
  - *Dẫn chứng:* KH: 'i just need a few reviews for my products, what is the easiest way to do this' → CS: 'I suggest setting up a scenario for the AI so that whenever customers receive or purchase a product, the AI c
  - → Khi KH lặp lại cùng câu hỏi, dừng lại confirm họ muốn gì (thêm review section/Air Reviews hay xin review thật?) rồi trả lời thẳng đúng nhu cầu thay vì đưa giải pháp gần đúng.
- **[KN1 · Low]** Một số tin có lỗi chính tả/đánh máy ảnh hưởng tính chuyên nghiệp — lặp lại ở vài chat. (Liz cũng đã nhắc sửa trực tiếp 1 câu trong chat #22.)
  - *Dẫn chứng:* 'Hey, I'm come back.' (chat #22, Liz nhắc 'sửa nhé em'); 'Sound amzing!' (chat #22); 'This is Lind afrom Avada Group' (chat #20); 'check the lòa page forr you' (chat #19); 'Secyurity' (chat #4)
  - → Đọc lại 1 lượt trước khi gửi, hoặc dùng text shortcut chuẩn cho các câu mở đầu/kết ('This is Linda from Avada Group', 'I'm back') để tránh typo lặp.
- **[KN1 · Low]** Sót placeholder template trong tin gửi KH — quên thay tên trước khi gửi (sau đó đã gửi lại bản đúng).
  - *Dẫn chứng:* chat #12: '...Please let me know if you'd like any further adjustments. Best regards, [Your Name]'
  - → Khi dùng template, soát 2 chỗ hay sót: tên ('[Your Name]') và link screenshot, trước khi nhấn gửi.

## 📈 So tuần trước
Tuần đầu, chưa có dữ liệu so sánh. (Lưu ý: điểm tuần này chỉ phản ánh chất lượng nội dung chat với khách — chưa bao gồm phối hợp TS/dev, tạo & follow-up ticket, bàn giao ca hay xin review; đó là phạm vi của QA tháng.)