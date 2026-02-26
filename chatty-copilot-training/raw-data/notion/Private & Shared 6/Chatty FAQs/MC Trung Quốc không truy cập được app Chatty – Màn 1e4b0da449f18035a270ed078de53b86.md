# MC Trung Quốc không truy cập được app Chatty – Màn hình trắng, console báo lỗi

Category: Genaral

### Problem

Khách hàng (chủ yếu từ Trung Quốc) không thể mở được app Chatty. Khi truy cập, màn hình trắng và console hiển thị lỗi liên quan đến font. KH đã thử xoá cache, đổi trình duyệt nhưng vẫn không vào được.

---

### Causes

- KH ở Trung Quốc có thể **bị chặn do Chatty được host trên Google Cloud** – một dịch vụ thường bị Great Firewall của Trung Quốc block.
- Một số KH dùng VPN không ổn định hoặc không dùng VPN → dễ bị block.
- Lỗi này thường xảy ra **nếu KH không dùng VPN hoặc dùng mạng bị giới hạn**.

---

### **Flow**

1. **Xác nhận KH đang ở đâu** – hỏi xem họ có đang ở Trung Quốc không.
2. **Kiểm tra VPN**:
    - Nếu KH **không dùng VPN**: hướng dẫn dùng 1 VPN uy tín có thể hoạt động ở Trung Quốc.
    - Nếu **đang dùng VPN**: gợi ý thử VPN khác hoặc đổi kết nối mạng.
3. **Gửi link standalone**:
    
    👉 https://app.meetchatty.com
    
    Hướng dẫn KH mở thử link này bằng VPN.
    
4. **Nếu các app khác vẫn dùng bình thường**: giải thích rằng **Chatty host trên Google**, nên có thể bị block bởi Trung Quốc.
5. **Escalate cho dev** nếu KH đã dùng VPN, đã mở link trên mà vẫn không vào được.