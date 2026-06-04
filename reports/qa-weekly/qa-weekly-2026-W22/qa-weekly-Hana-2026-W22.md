# QA Tuần 2026-W22 — Hana
**Giai đoạn:** 26/05 – 01/06  
**Điểm:** 84/100 — Đạt  
**Đã QA:** 24 chat  
**Phân bố:** 🌟2 ✅20 🟡0 🟠2 🔴0 ⛔0

## 📝 Nhận xét chung
Em hỗ trợ tận tâm và chắc về kiến thức sản phẩm. Tuần này có vài chat hiểu chưa đúng ý khách dẫn đến tư vấn hơi lệch. Hướng tập trung: confirm lại đúng nhu cầu khách trước khi đưa giải pháp — em vốn trả lời tốt, chỉ cần nắm đúng vấn đề từ đầu.

## ✅ Điểm tốt
- **[P2]** Chủ động đưa workaround khi chưa được hỏi — vụ Cookiebot/GDPR, ngoài việc xác nhận thẳng thắn Joy chưa tích hợp CMP, mình còn gợi ý whitelist fonts.bunny.net dưới mục Necessary để KH dùng tạm trong lúc chờ dev. Rất đáng khen vì biến một limitation thành lời khuyên hữu ích. (chat #3)
- **[P3]** Giải thích rõ ràng, có bước + ví dụ cụ thể — hướng dẫn biến số email ({{earning_discount}}, {{discount_code}}) kèm luôn một câu mẫu KH copy dùng được ngay, lại còn ghi rõ biến chỉ chạy trong notification của app. KH làm theo được liền. (chat #8)
- **[P5]** Đọc kỹ context, không tư vấn sai hướng — KH báo 'Joy review block hiện 2 lần', mình kiểm tra và nhận ra block đó là của Judge.me chứ không phải Joy, lịch sự hướng KH sang đúng team thay vì mò sửa app mình. (chat #16)
- **[P1]** Tôn trọng & đồng cảm với KH — vụ coupon revoke lỗi, KH nói không muốn làm phiền customer đang bực để quay video, mình không ép, vẫn nhận log issue lại cho có record. Giữ tone ấm, không cứng nhắc theo quy trình. (chat #18)

## 🔧 Cần cải thiện
- **[KN3 · Moderate]** Hai tin nhắn liền nhau mâu thuẫn nhau về cách tính milestone, dễ làm KH bối rối — một tin nói chi tiêu cũ vẫn được tính, tin sau lại nói chỉ tính từ ngày bắt đầu 1/6.
  - *Dẫn chứng:* Chat #23, Hana 09:29: "Any customer who has already spent 60,000 THB or more will qualify for the new milestone reward... The thresholds are independent, not additive." Ngay sau đó 09:31: "Joy will co
  - → Trước khi gửi, đọc lại xem 2 tin có khớp logic không. Ở case này yếu tố quyết định là start date — nên chốt 1 câu rõ ràng: 'Vì milestone có start date 1/6 nên chỉ tính chi tiêu TỪ 1/6; nếu muốn tính cả lịch sử thì bỏ start date đi'. Tránh đưa 2 hướng rồi để KH tự hỏi lại.
- **[QT9 · Moderate]** Xử lý export hơi vòng — hỏi 'vì sao muốn export' tạo chút friction, rồi export thiếu field phải làm lại 2 lần (lần 1 thiếu lifetime points, lần 2 thiếu các cột KH cần) thay vì confirm danh sách cột ngay từ đầu.
  - *Dẫn chứng:* Chat #22, Hana: "To proceed further, may I know why you want to export the customer data please?" → KH: "cause i need it... just send the file please". Sau đó export 3 lần mới đủ; KH phải tự liệt kê: 
  - → Với yêu cầu export, hỏi gọn ngay từ đầu 'Anh/chị muốn file gồm những cột nào ạ?' rồi export 1 lần đủ. Câu hỏi 'vì sao cần export' nên bỏ hoặc làm mềm hơn để không khiến KH thấy bị gác cửa.

## 📈 So tuần trước
Tuần đầu, chưa có dữ liệu so sánh. (Lưu ý phạm vi: điểm tuần chỉ dựa trên nội dung chat với khách — chưa gồm phối hợp TS/dev, tạo & follow-up ticket, bàn giao ca hay xin review; không phải đánh giá năng lực toàn diện.)