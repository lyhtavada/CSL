# Không nhận được email gửi ra sau khi đã xác minh Custom Sender (Simple Custom Sender)

Category: Notifications

- Khi Merchant chọn **Simple Custom Sender**, hệ thống Joy sẽ gửi email **qua domain chia sẻ của Avada là `send.avada.io`**, chứ không trực tiếp từ domain của Merchant.
- Merchant có thể tùy chỉnh **tên hiển thị (display name)** và **địa chỉ email gửi (sender email)**, tuy nhiên **SPF alignment sẽ không đạt 100%** nếu domain của Merchant có chính sách **DMARC nghiêm ngặt (policy = reject)**.
- Để đảm bảo email gửi đi thành công, Merchant **phải thêm SPF record cho mailgun.org**.

> Tham khảo thêm: [**Simple custom sender setup**](https://help.joy.so/settings/email/configure-simple-custom-sender#simple-custom-sender-setup)
> 

---

### Problem

- Merchant báo đã thêm và xác minh thành công **Custom sender**, trạng thái hiển thị **Verified** trong Joy.
- Khi test (ví dụ gửi email thông báo earn/redeem points, reward, hoặc automation), **không thấy email gửi đến**.
- Merchant đang dùng loại **Simple Custom Sender** (không dùng SMTP).

---

### Khi Merchant báo lỗi “Không nhận được email sau khi test”

**CS cần kiểm tra:**

1. Xác minh sender email có “Verified” chưa.
2. Kiểm tra Merchant đã thêm **SPF record cho mailgun.org** chưa.
    
    **Ví dụ:**
    
    Hiện tại domain có SPF như sau:
    
    ```
    v=spf1 include:_spf.google.com include:_spf.protection.outlook.com include:secureserver.net ~all
    ```
    
    Cần chỉnh thành:
    
    ```
    v=spf1 include:mailgun.org include:_spf.google.com include:_spf.protection.outlook.com include:secureserver.net ~all
    ```
    
    **Lưu ý:**
    
    - Chỉ nên có **1 bản ghi SPF duy nhất**.
    - Có thể kiểm tra SPF record bằng công cụ [MX Toolbox SPF Check](https://mxtoolbox.com/spf.aspx).
    - Nếu domain có nhiều SPF records → gộp lại trong một dòng duy nhất.
3. Hỏi xem domain của họ có đang bật DMARC policy = reject không.
    - Nếu domain có DMARC policy = **reject**, email gửi qua `send.avada.io` có thể bị chặn.
    - Khuyên Merchant giữ DMARC ở **`none`** để đảm bảo khả năng gửi.
    - Không nên thay đổi DMARC sang “none” chỉ để workaround — chỉ nên làm nếu Merchant hiểu rõ ảnh hưởng.
4. Nếu có → giải thích rằng với Simple Custom Sender, email sẽ bị chặn do không khớp SPF alignment.
5. Đề xuất hướng xử lý:
    - Chuyển sang **Custom SMTP setup** để đảm bảo gửi 100% qua domain riêng (nếu MC ở Advanced hoặc Enterprise).
6. Gửi test email
    - Sau khi xác minh và thêm SPF record, Merchant có thể test bằng cách:
        - Vào **Email notification** trong Joy.
        - Chọn một mẫu (ví dụ: Points earned email).
        - Nhấn **Send test email**.
    
    **Kiểm tra kết quả:**
    
    - Nếu thấy email trong inbox → setup hoàn tất.
    - Nếu không thấy:
        - Kiểm tra thư mục **Spam / Promotions**.
        - Thử gửi đến **một địa chỉ email khác** (không trùng với sender email).
        - Dùng [https://www.mail-tester.com/](https://www.mail-tester.com/) để đánh giá khả năng gửi mail.