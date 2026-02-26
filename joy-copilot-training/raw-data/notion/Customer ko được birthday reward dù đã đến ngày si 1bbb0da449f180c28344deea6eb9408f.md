# Customer ko được birthday reward dù đã đến ngày sinh nhật

Category: Reward programs

### **Problem/ Request**

Customer không nhận được phần thưởng sinh nhật (birthday reward) vào ngày sinh nhật.

---

### **Causes**

Để tránh gian lận, khách hàng cần nhập ngày sinh trước ít nhất 30 ngày mới có thể nhận quà sinh nhật trong năm nay.

- Nếu họ nhập trễ hơn 30 ngày trước sinh nhật, họ sẽ không nhận được reward năm nay.
- Tuy nhiên, ngày sinh của họ sẽ được lưu lại, và họ sẽ nhận reward vào sinh nhật năm sau.

Trường hợp phổ biến nhất là do khách hàng điền ngày sinh **không đủ 30 ngày trước ngày sinh** nên hệ thống sẽ chuyển phần thưởng sang năm sau.

Tuy nhiên, nếu:

- Merchant đã bật birthday reward đúng cách trong chương trình
- Khách hàng đã điền ngày sinh ít nhất 30 ngày trước sinh nhật

→ Nhưng vẫn không nhận được quà → Đây có thể là **lỗi hệ thống**.

---

### Support flow

Sau khi MC contact, CS cần hỏi thêm các thông tin sau:

1. Customer email address
2. Kiểm tra:
- Merchant đã bật reward này trong program chưa?
- Khách hàng đã điền ngày sinh chính xác và thời điểm nhập có trước ít nhất 30 ngày? (Phần này CS chủ động hỏi MC, nếu họ ko nhớ hoặc ko biết thì có thể tạo card để TS check).
1. Ngày customer nhập birthday
- Nếu customer ko nhập birthday trc 30 ngày sinh nhật thì CS dùng shortcut ***!birthday-reward*** để giải thích lại cách hoạt động của program này.
- Nếu customer đã nhập birthday đúng theo logic và ko đc reward thì có thể là lỗi app, CS tạo card để TS check và báo dev.

###