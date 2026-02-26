# Checklist: Merchant cần có gì để kết nối WhatsApp vào Chatty?

Category: Channels

## **1. Tài khoản Meta Business Manager (BBM)**

Merchant phải có:

- Một **Meta Business Manager** hợp lệ.
- Role: **Business Admin**.
    
    → Nếu chỉ có Employee hoặc không có quyền trên BM gốc, sẽ không connect được.
    

**Link kiểm tra**:

business.facebook.com/settings/people

- ***Meta Business Manager là gì?***
    
    **Meta Business Manager** là hệ thống quản lý doanh nghiệp của Meta (Facebook), dùng để tập trung quản lý:
    
    - Facebook Page
    - Instagram Account
    - Ads Account
    - WhatsApp Business Account
    - Quyền truy cập và vai trò của từng thành viên trong doanh nghiệp
    
    Nói đơn giản, đây là “trung tâm điều khiển” để Meta xác định:
    
    **Doanh nghiệp nào sở hữu số WhatsApp, ai có quyền quản lý, và ứng dụng nào được phép kết nối vào số đó.**
    
- ***Tại sao MC cần Meta Business Manager để kết nối WhatsApp vào Chatty?***
    
    Vì WhatsApp Cloud API được quản lý bởi Meta, nên để Chatty có thể gửi và nhận tin nhắn, MC phải:
    
    1. Chọn Business Manager của mình
    2. Chọn WhatsApp Business Account thuộc Business Manager đó
    3. Chọn số điện thoại muốn kết nối
    4. Cấp quyền cho “AVADA group company limited” quản lý số này
    
    => Tất cả thao tác này đều diễn ra trong Meta Business Manager.
    
- ***MC phải có role gì?***
    
    Để kết nối WhatsApp vào Chatty, MC **bắt buộc phải là Business Admin** trong Business Manager.
    
    Nếu chỉ là Employee → không bật được 2FA, không chọn số, và không thể approve kết nối.
    

---

## **2. WhatsApp số điện thoại hợp lệ**

Merchant cần chuẩn bị:

- Một **số điện thoại chưa được đăng ký WhatsApp**
    
    hoặc
    
- Một số WhatsApp Business cũ nhưng **đã đồng ý migrate** sang Cloud API.

Lưu ý:

- Không dùng số đang active trên WhatsApp app (cá nhân).
- Không được cấp mã OTP qua WhatsApp app, chỉ qua SMS hoặc cuộc gọi.

---

## **3. Thông tin doanh nghiệp hợp lệ**

Trong quá trình Meta onboarding, MC phải cung cấp:

- Tên doanh nghiệp
- Loại hình kinh doanh
- Địa chỉ hợp pháp
- Website domain (nếu có)

Nếu Meta yêu cầu Business Verification thì MC phải hoàn tất thì mới dùng full features.

---

## **4. Quyền chấp thuận kết nối với “Example Business Page”**

Khi popup OAuth xuất hiện (như screenshot), MC phải:

![image.png](Checklist%20Merchant%20c%E1%BA%A7n%20c%C3%B3%20g%C3%AC%20%C4%91%E1%BB%83%20k%E1%BA%BFt%20n%E1%BB%91i%20WhatsApp%20v/image.png)

- Chọn Business Manager
- Chọn WhatsApp Account
- Chọn số điện thoại
- Cho phép Example Business Page quyền quản lý số đó
    
    (Cần thiết để Chatty gửi & nhận message qua Cloud API)
    

---

## **5. Email + Facebook account phải đăng nhập đúng**

MC cần:

- Facebook account đã được add vào Business Manager
- Không dùng tài khoản cá nhân không có quyền
- Đảm bảo bật trình duyệt không chặn popup / third-party cookies

---

## **6. Không dùng provider thứ 3 khác (Twilio, 360dialog…)**

Nếu số WhatsApp đang dùng Cloud API của provider khác, MC phải:

- Khóa / release / migrate số đó
    
    Nếu không → Chatty không thể kết nối.
    

---