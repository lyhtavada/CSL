# QA Tuần 2026-W22 — Sonny
**Giai đoạn:** 26/05 – 01/06  
**Điểm:** 84/100 — Đạt  
**Đã QA:** 19 chat  
**Phân bố:** 🌟1 ✅17 🟡0 🟠1 🔴0 ⛔0

## 📝 Nhận xét chung
Bạn ổn định, tone tốt. Điểm yếu rõ tuần này: một số chat trả lời chung chung, chưa đi thẳng vào điều khách cần — khách đọc xong vẫn chưa biết phải làm gì cụ thể. Cần sửa: thay vì nói nguyên tắc chung, đưa ra từng bước cụ thể khách làm theo được ngay.

## ✅ Điểm tốt
- **[P1]** Giữ tone bình tĩnh, ấm khi KH bực: KH nói widget revamp 'it's a disaster', Sonny không phòng thủ mà revert ngay text/images và đổi layout classic — KH chốt 'now it's ok, thank you' (chat #16)
- **[P2]** Chủ động phát hiện vấn đề KH chưa hỏi: tự nhận ra cột 'awaiting point' trong file import và hỏi có cộng vào available point không trước khi chạy; ở case captcha cũng chủ động gợi ý bật Spam protection của Shopify (chat #15, chat #2)
- **[P3]** Xử lý cẩn thận, có bước rõ khi import CSV: confirm chỉ import point balance, đề xuất loại bỏ KH 0 điểm & điểm âm để giảm tải, trấn an không động vào data Shopify — KH yên tâm 'rest assured' (chat #8, chat #13)
- **[P5]** Đọc kỹ context và test trước khi khẳng định: KH hỏi nếu cập nhật tên ở Shopify admin thì có sync sang Joy không, Sonny test rồi mới confirm 'Yes I confirm... That was clever of you to think of the idea!' (chat #3)

## 🔧 Cần cải thiện
- **[KN6 · Moderate]** Chốt/đề xuất giải pháp khi chưa xác minh phiên bản widget của shop — dẫn đến phải đính chính lại với KH
  - *Dẫn chứng:* Sonny nhắn '...In this new version, you will be able to set the detail description for each redeeming program on the widget' (06:22), nhưng Liz flag nội bộ 'kh này vẫn ở v3 mà @sonny' và Sonny thừa nh
  - → Trước khi offer v4/khẳng định tính năng theo phiên bản, check version widget của shop (referral block, dấu hiệu v3/v4) rồi mới nhắn — tránh phải retract trước mặt KH

## 📈 So tuần trước
Tuần đầu, chưa có dữ liệu so sánh. (Lưu ý: điểm tuần này chỉ phản ánh chất lượng nội dung chat với khách — chưa bao gồm phối hợp TS/dev, tạo & follow-up ticket, bàn giao ca hay xin review; đây là feedback coaching, không phải đánh giá năng lực toàn diện.)