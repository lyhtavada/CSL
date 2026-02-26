# MC muốn transfer admin email sang email khác

Category: Genaral

### Problem

Merchant muốn chuyển quyền admin cho thành viên khác trên 1 store, nhưng gặp vấn đề:

- 1 Shopify account có thể có nhiều store.
- Khi đổi email admin ở 1 store, email ở các store khác cũng thay đổi theo.
- Merchant chỉ muốn thay đổi quyền admin cho từng store riêng lẻ.

---

### Cause

- Shopify quản lý tài khoản theo cấp **account**, không theo cấp **store**.
- Chức năng mặc định "Edit email" sẽ áp dụng trên toàn bộ store của account.
- Cần bật tính năng "Transfer admin" để chỉ thay đổi quyền admin trong từng store.

---

### Flow

1. **Xác định nhu cầu của merchant**
    - Hỏi rõ: Merchant muốn đổi email/admin cho **toàn bộ store** hay **chỉ một store**?
        
        → Nếu toàn bộ store → Dùng "Edit email".
        
        → Nếu chỉ một store → Dùng "Transfer admin".
        

1️⃣ Nếu MC đang ở Paid plans:

- **Bật tính năng Transfer admin**
    - Vào **Dev zone** > bật **Transfer admin** cho store merchant yêu cầu.
        
        ![image.png](MC%20mu%E1%BB%91n%20transfer%20admin%20email%20sang%20email%20kh%C3%A1c/image.png)
        
- **Hướng dẫn merchant chuyển admin**
    - Vào **Setting > Team**.
    - Edit profile của admin hiện tại > click **Transfer admin**.
        
        ![image.png](MC%20mu%E1%BB%91n%20transfer%20admin%20email%20sang%20email%20kh%C3%A1c/image%201.png)
        
    - Chọn thành viên muốn chuyển quyền admin > Xác nhận.
        
        ![image.png](MC%20mu%E1%BB%91n%20transfer%20admin%20email%20sang%20email%20kh%C3%A1c/image%202.png)
        

2️⃣ **Nếu MC đang ở Free plan**

- Mở thêm **số lượng seat** tại Dev zone.
- Hướng dẫn merchant:
    - **Invite** thành viên mới vào store.
    - **Activate** tài khoản thành viên.
- Sau khi thành viên activate thành công:
    - Bật **Transfer admin**.
    - Merchant chuyển quyền admin, sau đó **xoá admin cũ**.
- Cuối cùng: **Đóng lại limit seat** để tránh phát sinh seat thừa.

---

### Lưu ý thêm

- Không thể bật đồng thời 2 tính năng "Edit email" và "Transfer admin".
- Nếu cần đổi admin cho nhiều store cùng lúc, cần thực hiện từng store riêng biệt.