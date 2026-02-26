# Lỗi Response code 422 khi click vào generate Loyalty hero banner

Category: Onsite content

### **Problem/ Request**

Lỗi **Response code 422** khi merchant click vào nút **Generate Loyalty Hero Banner** trong app.

![image.png](L%E1%BB%97i%20Response%20code%20422%20khi%20click%20v%C3%A0o%20generate%20Loyal/image.png)

---

### **Causes**

- Khi merchant click vào nút “Edit in theme editor” để tùy chỉnh Loyalty Hero Banner, app sẽ tự động tạo một **loyalty page** trong mục **Online Store > Pages** trên Shopify.

![image.png](L%E1%BB%97i%20Response%20code%20422%20khi%20click%20v%C3%A0o%20generate%20Loyal/image%201.png)

- Nếu merchant đã từng click nút này trước đó và page đã được tạo, khi click lại, hệ thống sẽ không thể tạo thêm trang mới (do bị trùng), có thể dẫn đến lỗi **422 như trên**.

---

### **Flow**

1. **CS giải thích lỗi và hướng dẫn merchant kiểm tra page, dùng shortcut `!loyalty_hero_422_page_exists`** 

![image.png](L%E1%BB%97i%20Response%20code%20422%20khi%20click%20v%C3%A0o%20generate%20Loyal/image%202.png)

1. **CS follow-up để hỗ trợ merchant hoàn thiện loyalty page**

→ Sau khi merchant đã mở được loyalty page, CS cần chủ động follow-up để hỗ trợ chỉnh sửa, ví dụ:

- Điều chỉnh **màu sắc** của block cho phù hợp với thương hiệu
- Gợi ý **kích thước block hoặc text** nếu chưa hiển thị đẹp
- Gợi ý **ẩn/hiện các khối thông tin** nếu cần tối ưu UI/UX