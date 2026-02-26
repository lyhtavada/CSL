# MC đã add custom email sender và verify email, tuy nhiên trong app vẫn hiển thị là Unverified

Category: General

### ✏️ Scenario

MC đã add custom email sender và verify email, tuy nhiên trong app vẫn hiển thị là [Unverified](https://prnt.sc/bUUaeUeo3iXP) 

### ⁉️Possible causes

- MC chưa thật sự click verify ở Verification email từ app gửi đến
- Lỗi app

### ➡️ Support flow

- CS validate email sender qua tool [ZeroBounce](https://www.zerobounce.net/members/dashboard) để đảm bảo là email đó valid.
- Nếu email valid, CS resend Verification email > nhờ MC thử check lại Inbox/ Spam > Click verify
    - CS check lại status của email.
    - CS có thể thử lại vài lần xem email có đc verified ko
- Trong TH email vẫn chưa được verify đc, CS forward issue cho dev kèm thông tin chi tiết.

### 🪞 References

### Tips & Tricks (optional)