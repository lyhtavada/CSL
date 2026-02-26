# Email forwarding ko đc verify dù đã add forwarding email thành công và nhận đc verification email

Category: Channels

## **Problem/ Request**

Email forwarding không được verify dù đã MC đã **chọn đúng Provider** và add forwarding email thành công cùng với nhận được verification email từ Chatty.

---

## **Causes**

- Forwarding email đã được thêm nhưng hệ thống email gốc (ví dụ: Tencent Email) không thực sự forward email về địa chỉ đích.
- Có thể do cấu hình forwarding ở bên email gốc chưa đúng hoặc gặp lỗi.

---

## **Flow**

1. Kiểm tra lại **forwarding settings** ở hệ thống email gốc (A).
2. Thay đổi forwarding email (B - Chatty) sang một địa chỉ email khác (C) của merchant.
3. Merchant gửi test email từ email gốc (A) từ 1 address (D) để xem có forward thành công từ D > A sang email mới (C) không.
    - Nếu email mới (C) nhận được thì vấn đề nằm ở email đích ban đầu (B-Chatty) → cần báo dev xử lý tiếp. CS tiếp tục follow up và update tiến độ cho MC.
    - Nếu email mới (C) cũng không nhận được → forwarding bên hệ thống email gốc đang bị lỗi, cần merchant liên hệ nhà cung cấp email để kiểm tra.
4. Sau khi xác nhận forwarding hoạt động bình thường, thực hiện lại bước verify trong Chatty.

Ref: [https://avadagroupcom.slack.com/archives/C07AZNGEVTM/p1754899870846449](https://avadagroupcom.slack.com/archives/C07AZNGEVTM/p1754899870846449)