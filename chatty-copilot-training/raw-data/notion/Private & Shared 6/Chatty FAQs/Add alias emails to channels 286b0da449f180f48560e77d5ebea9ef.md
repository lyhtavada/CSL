# Add alias emails to channels

Category: Channels

### Problem/ Request:

Merchant có nhiều email (ví dụ: support@, hiring@) và muốn thêm tất cả vào app. Tuy nhiên, khi add alias email (email phụ), hệ thống không gửi verification link về inbox nên không thể verify từng địa chỉ.

---

### Root causes

Alias emails (ví dụ hiring@, support@) thường được cấu hình forwarding rule trong cùng một tài khoản email chính.

Vì vậy, hệ thống chỉ nhận diện và gửi verification link đến **email gốc** (primary email), không gửi đến các alias.

---

### Flow

**Bước 1:**

Xác nhận với merchant xem các email muốn add có phải **alias của cùng một Gmail account** hay là **tài khoản email riêng biệt**.

**Bước 2: Nếu là alias (email phụ của cùng domain)**

→ Giải thích cho merchant:

- Chỉ cần **verify email gốc (primary)** một lần.
- Sau khi verify xong, add email alias vào Chatty, nhưng có thể skip đến bước cuối để Finish setup (ko cần verify nữa vì đã verify email gốc rồi) > Click to verify.
    
    ![image.png](Add%20alias%20emails%20to%20channels/image.png)
    
    - Email A là email chính (verified).
    - Email B là alias của A.

<aside>

Các email được gửi đến A hay B thì đều được forward đến Chatty inbox. Nếu MC muốn chỉ connect email alias (B) thì vẫn phải thực hiện các bước trên sau đó có thể xoá email chính (A) khỏi Channels.

</aside>

**Bước 3: Nếu là tài khoản riêng biệt (không phải alias)**

→ Merchant cần **verify từng email riêng** vì hệ thống xem đó là các tài khoản độc lập.

Nếu không nhận được verification link, CS kiểm tra:

- Merchant đã nhập đúng địa chỉ chưa.
- Email có chặn mail từ domain hệ thống không (ví dụ check spam, filter rule).
    
    → Nếu vẫn không nhận được link, forward issue cho Tech Support để kiểm tra log gửi mail.
    

---

<aside>

**Giải thích ngắn gọn cho merchant:**

If your emails (e.g. support@ and hiring@) are aliases of the same Gmail account, you only need to verify the **primary email address**.

Once it’s verified, add your alias email to Chatty. For the alias email, you don’t need to verify in your email inbox, just go to final step to finish your setup. 

If these are **separate email accounts**, each one needs to be verified individually.

</aside>