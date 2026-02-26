# Ko nhận được verification email từ sau khi add Custom email sender

Category: General

### Problem/ Request:

- Merchant báo: “I didn’t receive any verification email after adding my custom sender.”
- Trong Joy > Settings > Email, mục **Custom sender** hiển thị “Pending verification”.
- Email dùng để xác minh là **email doanh nghiệp hoặc cá nhân (Gmail, Outlook, v.v.)**.

---

### Possible causes

Về bản chất, email xác minh được gửi từ hệ thống Joy đến địa chỉ mà Merchant cung cấp.

Nếu Merchant không nhận được email, nguyên nhân thường do:

- Email bị lọc sang hộp **Spam / Promotions**; hoặc
- Domain/email bị cấu hình filter chặn email từ Avada; hoặc
- Địa chỉ email của Merchant không hợp lệ (invalid).

---

### Flow

**Bước 1. Xác minh lại thông tin cơ bản**

- Xác nhận lại với MC xem email nhập ở sender có valid hay không.
- Hướng dẫn kiểm tra hộp **Spam / Promotions / Updates**.
- Nếu không thấy, hướng dẫn họ chọn **Resend verification email** trong Joy.

<aside>

CS có thể dùng tool [https://www.zerobounce.net/](https://www.zerobounce.net/) để xác mình email của MC valid hay không.

![image.png](Ko%20nh%E1%BA%ADn%20%C4%91%C6%B0%E1%BB%A3c%20verification%20email%20t%E1%BB%AB%20sau%20khi%20add%20Cus/image.png)

</aside>

**Bước 2: Check DMARC ở [MXTools](https://mxtoolbox.com/SuperTool.aspx#) > DMARC lookups**

![image.png](Ko%20nh%E1%BA%ADn%20%C4%91%C6%B0%E1%BB%A3c%20verification%20email%20t%E1%BB%AB%20sau%20khi%20add%20Cus/image%201.png)

Hiện tại, app đã tự động hiển thị cảnh báo khi email domain của merchant có **DMARC policy = `p=reject`**.

Khi đó, CS **không cần kiểm tra thủ công bằng MXTools nữa**, mà chỉ cần giải thích lại và hướng dẫn merchant:

- Nếu muốn tiếp tục dùng địa chỉ email này, hãy **thiết lập Custom Sending Domain hoặc SMTP** để đảm bảo email được xác thực đúng cách.

![image.png](Ko%20nh%E1%BA%ADn%20%C4%91%C6%B0%E1%BB%A3c%20verification%20email%20t%E1%BB%AB%20sau%20khi%20add%20Cus/image%202.png)

- Hoặc merchant có thể **đổi sang một địa chỉ email khác** thuộc domain chưa bật DMARC ở mức `p=reject` hoặc `p=quarantine`.

> Tham khảo: [DMARC là gì?](https://www.notion.so/DMARC-l-g-2a8b0da449f18058ae1de28aab6da608?pvs=21)
> 

<aside>

**Cách check DMARC thủ công:**

1. Truy cập trang **MXTools > [DMARC Lookup](https://mxtoolbox.com/SuperTool.aspx#)**.
2. Dán **domain chính của website** (ví dụ: `example.com`) vào ô tìm kiếm và nhấn Enter để kiểm tra.
3. Xem phần kết quả:
    - Nếu **kết quả hiển thị “`p=reject`” hoặc “`p=quarantine`”**, điều đó nghĩa là domain này **đã bật DMARC**.
    - Khi đó, các email gửi đi **từ domain này thông qua hệ thống Avada (hoặc domain gửi chung của Avada)** sẽ **không được chấp nhận**, vì Avada không có quyền gửi thay mặt domain đã được bảo vệ bằng DMARC.
        
        ![image.png](Ko%20nh%E1%BA%ADn%20%C4%91%C6%B0%E1%BB%A3c%20verification%20email%20t%E1%BB%AB%20sau%20khi%20add%20Cus/image%203.png)
        
    
</aside>