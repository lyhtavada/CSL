# Không nhận được Verification Email khi setup Email Channel

Category: Channels

### Problem

- KH add email forwarding vào Chatty
- Ở bước **Send verification email**, KH báo:
    - Không nhận được email xác thực
    - Hoặc inbox / spam đều không thấy

---

## Flow

### Step 1: Check Email Logs trong Chatty (qua CRM)

- CS login Chatty qua CRM
- Vào: **Email channel → Email logs (tính năng chỉ hiển thị khi login qua CRM, KH không truy cập được setting này).**

![image.png](Kh%C3%B4ng%20nh%E1%BA%ADn%20%C4%91%C6%B0%E1%BB%A3c%20Verification%20Email%20khi%20setup%20Email/image.png)

- Kiểm tra:
    - Có log email verification được gửi hay không
    - Click icon xem chi tiết để lấy **verification link**
    
    ![image.png](Kh%C3%B4ng%20nh%E1%BA%ADn%20%C4%91%C6%B0%E1%BB%A3c%20Verification%20Email%20khi%20setup%20Email/image%201.png)
    

### Step 2: Gửi lại verification link cho KH (nếu còn hạn)

- Nếu link **chưa expired**:
    - CS copy verification link từ Email logs
    - Gửi lại cho KH qua live chat/email
    - Hướng dẫn KH click link để verify

### Step 3: Trường hợp verification link đã hết hạn

- Verification link có **expiry time**
- Nếu link trong Email logs đã expired, CS nhờ KH quay lại trang setup email forwarding và click để send lại **verification email**
- Sau đó:
    - CS check lại Email logs
    - Lấy link mới và gửi lại cho KH nếu cần

---

## 3. Mẫu câu CS gửi cho KH:

### Trường hợp gửi lại link còn hạn

> I’ve checked our system and can see the verification email was sent. Sometimes it may not reach your inbox.
> 
> 
> Please use this verification link to complete the setup:
> 
> [verification link]
> 

---

### Trường hợp link đã hết hạn

> I checked the verification link and it looks like it has expired.
> 
> 
> Could you please click **Send verification email** again in your Email Forwarding setup? Once it’s sent, I’ll help you retrieve the new link right away.
> 

<aside>

Trong TH CS đã kiểm tra Email logs nhưng không thấy bất kỳ email verification nào được gửi

Sau khi đã loại trừ các nguyên nhân phổ biến:

- [Email alias](Add%20alias%20emails%20to%20channels%20286b0da449f180f48560e77d5ebea9ef.md)
- KH chưa thực hiện đúng các bước setup
- KH chưa click “Send verification email”

👉 CS chủ động báo dev team để kiểm tra thêm

</aside>