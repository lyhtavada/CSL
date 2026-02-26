# MC ko muốn AI cung cấp email support trong chat

Category: AI Assistant
PIC: Ly Hoàng

### **Problem / Request**

Merchant không muốn AI hiển thị hoặc cung cấp địa chỉ email support trong phần chat cho khách hàng.

---

### **Cause**

- Mặc định, AI có thể lấy thông tin liên hệ (bao gồm email support) từ store settings để hiển thị cho khách.
- Một số Merchant muốn kiểm soát và chỉ định kênh liên hệ khác (ví dụ: live chat, form, phone), không muốn công khai email.

---

### **Flow / Solution**

1. Vào phần **AI instructions:**
2. Thêm dòng sau:
    
    ```
    Do not provide Store Support Email addresses to customers.
    ```
    
3. Lưu lại thay đổi.
4. **Test**: Giả lập một số tình huống chat có thể trigger AI đưa ra email support (ví dụ: “How can I contact support?”, “What’s your support email?”) để đảm bảo email không còn hiển thị.
5. Confirm với Merchant.

https://avadagroupcom.slack.com/archives/C07AZNGEVTM/p1757256268506559