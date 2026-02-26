# Tin nhắn từ Meta ko show trong Chatty

Category: Channels

### Problem/ Request

Merchant báo rằng một số tin nhắn từ Meta (Facebook/Instagram) không hiển thị trong Chatty, khiến việc theo dõi hội thoại bị gián đoạn.

---

### Flow

**Bước 1: Xác nhận thông tin lỗi**

- Yêu cầu merchant gửi:
    - Link của **1–2 hội thoại** gặp lỗi.
    - **Ảnh chụp màn hình** từ phía Meta thể hiện các tin nhắn bị thiếu (missing messages).
    - Thời gian hoặc người gửi của tin nhắn bị thiếu (nếu có thể).

---

**Bước 2: Xác định nguồn của tin nhắn bị thiếu**

- Nếu **tin nhắn bị thiếu là từ phía merchant gửi đi**:
    
    → Hỏi lại merchant xem những tin đó được gửi từ **Chatty** hay **trực tiếp từ Meta (Messenger/Instagram)**.
    
    - Nếu **gửi từ Meta**:
        
        → Giải thích rằng các tin này **sẽ không được đồng bộ về Chatty** do Meta **không cung cấp webhook cho loại tin nhắn đó** (ví dụ: reply từ Meta app hoặc một số loại reaction, attachment).
        
        → Đây là **giới hạn từ phía Meta**, không phải lỗi của Chatty.
        
        ```jsx
        Meta does not provide webhooks for certain types of messages (for example, messages 
        sent directly from the Messenger or Instagram apps). As a result, those messages will 
        not appear in Chatty.
        
        Messages sent and received through Chatty are fully synced. Therefore, we recommend 
        that you send and reply to all messages using only one channel – Chatty – to ensure 
        proper synchronization and easier conversation management.
        ```
        
    - Nếu **gửi từ Chatty** nhưng vẫn không hiển thị:
        
        → Ghi nhận chi tiết (thời gian, nội dung, người gửi) và **chuyển issue cho TS** kiểm tra thêm.
        
- **Nếu tin nhắn bị thiếu là từ phía customer gửi đi:**
    - CS **thử gửi tin nhắn test** để kiểm tra việc nhận tin từ Chatty.
    - **Forward issue cho TS** kèm theo:
        - Link hội thoại.
        - Screenshot từ Meta.
        - Thời điểm xảy ra lỗi.
        - Kết quả test của CS.

---