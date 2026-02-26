# Email từ Hotmail và Outlook ko được forward qua Chatty

Category: Channels
PIC: Ly Hoàng

### **Problem / Request**

Merchant báo email có đuôi @outlook.com hoặc @hotmail.com không được forward về Chatty, dẫn đến không nhận được tin nhắn trong app.

---

### **Cause**

Nguyên nhân là do **Cloudflare và hệ thống mail của Microsoft (Outlook/Hotmail) không tương thích hoàn toàn**, khiến forwarding bị chặn hoặc thất bại trong một số trường hợp. Đây là vấn đề ngắt quãng, không phải lúc nào cũng xảy ra.

---

### **Flow / Solution (Workaround)**

Shortcut **`!outlook-hotmail-fw`**

1. Xác nhận với merchant rằng đây là limitation kỹ thuật giữa Microsoft và Cloudflare, dev team đang theo dõi.
2. Đề xuất workaround:
    - **Tạo mailbox trung gian**: Dùng Gmail hoặc domain email khác để nhận mail từ Outlook/Hotmail, sau đó forward sang Chatty.
    - **Chuyển sang email hosting khác**: Nếu merchant bắt buộc phải dùng Hotmail/Outlook, nên cân nhắc chuyển domain mail sang dịch vụ như Google Workspace hoặc Zoho Mail rồi forward về Chatty.
    - **Bật thêm kênh notification**: Trong thời gian chờ, merchant có thể bật email notification qua Gmail hoặc cài đặt Chatty mobile app để đảm bảo không bỏ lỡ tin nhắn.
3. Hướng dẫn MC test lại sau khi thiết lập workaround.
4. Ghi nhận feedback để product/dev team ưu tiên xử lý lâu dài.