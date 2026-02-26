# Merchant vẫn nhận được email báo lỗi “Fail to deliver” sau khi đã disable email forwarding vào Chatty

Category: Channels
PIC: Ly Hoàng

![image.png](Merchant%20v%E1%BA%ABn%20nh%E1%BA%ADn%20%C4%91%C6%B0%E1%BB%A3c%20email%20b%C3%A1o%20l%E1%BB%97i%20%E2%80%9CFail%20to%20deli/image.png)

### **Problem:**

Merchant báo đã disable email forwarding trong Chatty, nhưng vẫn nhận được email báo lỗi “Delivery Status Notification (Failure)” từ hệ thống email của họ.

---

### Flow

1. **Double-check trong Chatty**
    - Vào Chatty > Channels > Email
    - Xác nhận xem merchant đã thực sự disable Email channel chưa.
2. **Kiểm tra setting email forwarding từ phía merchant**
    - Hỏi merchant xem đã remove Chatty email khỏi phần email forwarding trong cài đặt email của họ chưa.
    - Nếu **chưa remove**:
        - Hướng dẫn họ remove Chatty email khỏi forwarding settings.
        
        VD ở Gmail:
        
        ![image.png](Merchant%20v%E1%BA%ABn%20nh%E1%BA%ADn%20%C4%91%C6%B0%E1%BB%A3c%20email%20b%C3%A1o%20l%E1%BB%97i%20%E2%80%9CFail%20to%20deli/image%201.png)
        
        - Test lại để xem còn gặp lỗi “Fail to deliver” hay không.
    - Nếu **đã remove** nhưng vẫn nhận lỗi:
        - CS escalate vấn đề sang TS hoặc Dev để check kỹ hơn.

<aside>

- Email “Delivery Status Notification (Failure)” này do hệ thống mail của merchant gửi, không phải do Chatty gửi.
- Quan trọng là phải xác nhận merchant đã remove forwarding hoàn toàn khỏi email provider của họ.
</aside>