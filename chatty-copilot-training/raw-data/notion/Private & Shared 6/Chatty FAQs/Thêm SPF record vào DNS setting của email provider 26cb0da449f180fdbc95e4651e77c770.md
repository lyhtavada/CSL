# Thêm SPF record vào DNS setting của email provider khi add Email channels

Category: Channels
PIC: Ly Hoàng

### **Problem / Request**

- Merchant đã verify email channel bằng Hostinger. Tencent hoặc các provider khác ngoài Google và Outlook. Email provider đã gửi email confirmation, nhưng app không nhận được email.
- Sau khi email được verify, nhưng vẫn nhận được thông báo **Delivery failure hoặc delay**

---

### **Cause**

Nguyên nhân là bản ghi SPF của domain chưa cho phép Amazon SES gửi email thay mặt cho domain đó. Vì thiếu `include:amazonses.com`, nên email bị chặn hoặc fail SPF check, dẫn đến app không nhận được.

---

### **Flow / Solution**

1. Giải thích cho merchant nguyên nhân là SPF record chưa đầy đủ.
2. Yêu cầu merchant vào phần quản lý DNS của domain trong email provider
3. Thêm SPF record để bao gồm Amazon SES.
    - Nếu domain đã có SPF record, bổ sung `include:amazonses.com`.
    - Ví dụ:
        
        ```
        v=spf1 include:amazonses.com ~all
        ```
        
4. Sau khi cập nhật DNS, cần chờ khoảng 24–48h để DNS propagation hoàn tất.
5. Test lại việc gửi và nhận email xác minh.

---

### **⇒ Hướng dẫn chi tiết: [Fix Email Delivery Issues with Amazon SES](https://help.meetchatty.com/live-chat/channels/email/fix-email-delivery-issues-with-amazon-ses)**