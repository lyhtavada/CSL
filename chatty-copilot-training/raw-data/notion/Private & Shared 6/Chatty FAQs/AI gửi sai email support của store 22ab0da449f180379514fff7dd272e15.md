# AI gửi sai email support của store

Category: AI Assistant

### **Problem/ Request**

AI trả lời sai địa chỉ email khi share contact email của store cho khách.

https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_c7ed328d-1d65-45a9-8bfd-afccc58aecad/

![image.png](AI%20g%E1%BB%ADi%20sai%20email%20support%20c%E1%BB%A7a%20store/image.png)

---

### Causes

Hiện tại AI assistant đang lấy Support email ở phần **Transfer (AI Settings)** > **Contact Support Email:**

![image.png](AI%20g%E1%BB%ADi%20sai%20email%20support%20c%E1%BB%A7a%20store/image%201.png)

---

### **Flow**

1. CS cần kiểm tra email mà AI đã gửi cho khách
2. **Vào Chatty > AI Assistant > Transfer**, kiểm tra mục **Contact Support Email**:
    - Nếu merchant để sai email → CS cần **gửi hướng dẫn để họ cập nhật lại**.
3. Gợi ý merchant điền email đúng theo format họ muốn khách liên hệ (ví dụ: support@storename.com).
4. Sau khi merchant cập nhật, AI sẽ tự động lấy thông tin mới cho các chat sau đó.