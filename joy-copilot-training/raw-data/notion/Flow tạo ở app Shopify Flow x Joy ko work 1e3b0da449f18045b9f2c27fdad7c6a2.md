# Flow tạo ở app Shopify Flow x Joy ko work

Category: Integrations

**Problem:**

Flow được tạo trong Shopify Flow kết hợp với Joy Loyalty app không hoạt động như mong muốn.

**Cause:**

- Flow chưa được setup đúng.
- Chưa enable **Shopify Flow Integration** trong Joy app.
- Lỗi tích hợp giữa Joy và Shopify Flow.

**Flow:**

1. CS hỏi MC về **luồng hoạt động mong muốn** của Flow đó (khi nào chạy, mục đích gì...).
2. Kiểm tra xem MC đã **enable Shopify Flow Integration** trong app Joy hay chưa:
    - Vào Joy > Integration > Shopify Flow.

![image.png](Flow%20t%E1%BA%A1o%20%E1%BB%9F%20app%20Shopify%20Flow%20x%20Joy%20ko%20work/image.png)

1. Yêu cầu MC gửi **ảnh chụp cấu hình Flow** trong Shopify Flow app.
2. Nếu cần thiết, xin MC cấp quyền để truy cập vào Flow app nhằm điều tra kỹ hơn.
3. Xử lý theo hai hướng:
    - Nếu phát hiện Flow **chưa setup đúng**, hướng dẫn MC chỉnh lại cho đúng.
    - Nếu Flow đã setup đúng nhưng vẫn không hoạt động, **chuyển cho dev điều tra lỗi**.
4. CS tiếp tục theo dõi và cập nhật tiến độ cho MC.