# Vấn đề liên quan đến connect Chatty với WhatsApp

Category: Channels

### Problem/ Request

MC đã click “Connect with WhatsApp” trong Chatty nhưng hiển thị “Pending”

![image.png](V%E1%BA%A5n%20%C4%91%E1%BB%81%20li%C3%AAn%20quan%20%C4%91%E1%BA%BFn%20connect%20Chatty%20v%E1%BB%9Bi%20WhatsApp/image.png)

---

### Possible causes

- **MC chưa có tài khoản Facebook Business liên kết với tài khoản WhatsApp Business**
- Business account chưa được xác minh
- Phone number chưa được duyệt.
- **MC chưa hoàn tất đầy đủ các bước kết nối trong pop-up** (vd: chưa chọn đúng tài khoản, chưa cấp quyền).

Dưới đây là video và hình ảnh setup đúng khi MC đã có FB Business Account:

[https://somup.com/cT1XnxLI3v](https://somup.com/cT1XnxLI3v)

<aside>
💡

Check thêm chi tiết tại [**Checklist: Merchant cần có gì để kết nối WhatsApp vào Chatty?**](Checklist%20Merchant%20c%E1%BA%A7n%20c%C3%B3%20g%C3%AC%20%C4%91%E1%BB%83%20k%E1%BA%BFt%20n%E1%BB%91i%20WhatsApp%20v%202bdb0da449f1804f8627e5b2a4968f81.md) 

</aside>

---

### Flow xử lý

1️⃣ **Xác nhận thông tin ban đầu với MC**

CS hỏi MC, dùng shortcut **`!ws_check_1`**

- Bạn đã tạo **WhatsApp Business Account** chưa?
- Tài khoản **Facebook Business** liên kết đã được **verified** chưa?
- Số điện thoại muốn kết nối đã được **approved** chưa?

2️⃣ **Xử lý theo từng trường hợp:**

**Trường hợp 1: MC chưa tạo WhatsApp Business**

→ Gửi shortcut **`!wsb_create`** kèm link hướng dẫn tạo tài khoản và đăng ký WhatsApp Business.

→ Giải thích rằng cần đợi Meta duyệt xong mới có thể kết nối.

*Since you haven't had a WhatsApp Business account yet. Please follow this guide to create your WhatsApp Business account and link it with your Facebook Business account: [Create a WhatsApp Business account on the WhatsApp Business platform](https://www.facebook.com/business/help/2087193751603668?id=2129163877102343). Once Meta approves your account, you can come back to connect it with Chatty.*

**Trường hợp 2: Đã tạo WhatsApp Business nhưng Business chưa được verified**

→ Thông báo MC rằng cần hoàn tất **Business Verification** trên Meta.

→ Chỉ khi được verified mới có thể connect thành công.

**Shortcut:** **`!wsb_verify`**

*"It seems your Facebook Business account is not yet verified. Please complete the Business Verification process in your Meta Business Manager. Once your account is verified, you will be able to connect it with Chatty."*

**Trường hợp 3: Number chưa được approved (MC đã connect nhưng hiển thị “Pending” trong app)**

Có nhiều lý do khiến number chưa được approved: CS xử lý theo những nguyên nhân sau:

- Do MC chưa thiết lập **Two-Factor Authentication (2FA)** cho số điện thoại WhatsApp Business.
    
    → Yêu cầu MC thiết lập **Two-Factor Authentication (2FA)** cho số điện thoại WhatsApp Business.
    
    **Shortcut đề xuất:** **`!wsb_2fa`**
    
    *"Your WhatsApp Business number is currently showing as 'Pending'. Please enable [Two-Factor Authentication (2FA)](https://prnt.sc/TQn0e_cVQtxH) in your WhatsApp Business settings, then reconnect to Chatty.*
    
    *Once 2FA is enabled, please wait for Meta to approve it — after approval, the connection should be completed.”*
    
    Sau đó MC cần đợi để phone number được approved rồi connect lại với Chatty.
    
- Do Display name của number chưa hợp lệ.
    
    → MC cần đặt lại Display name theo đúng guideline sau:
    
    - Tên phải rõ ràng, liên quan đến doanh nghiệp/nhãn hiệu.
    - Không được chứa các ký tự đặc biệt, từ ngữ cấm hoặc quá chung chung.
    - Tránh sử dụng từ khóa nhạy cảm hoặc mang tính chất quảng cáo quá mức.

Sau khi chỉnh sửa Display name đúng chuẩn, MC cần đợi Meta phê duyệt lại số điện thoại, sau đó kết nối lại với Chatty.

**Shortcut đề xuất: `!wsb_name`**

*"Your WhatsApp Business number is still pending because the Display name does not meet Meta's guidelines. Please update your Display name according to [these guidelines](https://www.facebook.com/business/help/757569725593362) to ensure it reflects your business properly.*

*After updating, please wait for Meta to approve the number and then reconnect to Chatty.”*

<aside>
💡

CS nên chủ động hỏi MC để xác định trạng thái hiện tại của số điện thoại:

- MC đã bật Two-Factor Authentication (2FA) chưa?
Nếu chưa, hướng dẫn MC bật 2FA theo shortcut **`!wsb_2fa`**.
- Display name hiện tại của số điện thoại là gì? 
CS kiểm tra xem tên này có phù hợp với [guidelines của Meta](https://www.facebook.com/business/help/757569725593362) hay không. Nếu chưa phù hợp, hướng dẫn MC chỉnh sửa theo shortcut **`!wsb_name`.**
</aside>

3️⃣ **Nếu MC đã hoàn tất các bước trên mà vẫn lỗi:**

→ CS thu thập thông tin chi tiết và báo lại dev team để kiểm tra thêm.

4️⃣ **CS tiếp tục theo dõi và cập nhật tiến độ cho MC.**

<aside>
✅

- Phía trên chỉ là 1 vài TH hay gặp để tham khảo, không phải tất cả, dựa vào từng thông tin MC cung cấp, CS sẽ xác định nguyên nhân và lựa chọn flow xử lý phù hợp (gửi guide tạo WBA, hướng dẫn verify, yêu cầu bật 2FA, hướng dẫn cấp quyền, hoặc kiểm tra số điện thoại).
- **CS cần linh hoạt, không áp dụng cứng nhắc mà hỏi kỹ từng bước để tránh bỏ sót điều kiện quan trọng dẫn đến lỗi kết nối.**
</aside>

---

### Screenshot tham khảo:

Business verification đã được verified:

![image.png](V%E1%BA%A5n%20%C4%91%E1%BB%81%20li%C3%AAn%20quan%20%C4%91%E1%BA%BFn%20connect%20Chatty%20v%E1%BB%9Bi%20WhatsApp/image%201.png)

1. Phone number của account WS đó đã được connected + approved.

![image.png](V%E1%BA%A5n%20%C4%91%E1%BB%81%20li%C3%AAn%20quan%20%C4%91%E1%BA%BFn%20connect%20Chatty%20v%E1%BB%9Bi%20WhatsApp/image%202.png)

Step 1: Chọn Business portpolio (edited)

![image.png](V%E1%BA%A5n%20%C4%91%E1%BB%81%20li%C3%AAn%20quan%20%C4%91%E1%BA%BFn%20connect%20Chatty%20v%E1%BB%9Bi%20WhatsApp/image%203.png)

Step 2: chọn Whatsapp account > Click Continue

![image.png](V%E1%BA%A5n%20%C4%91%E1%BB%81%20li%C3%AAn%20quan%20%C4%91%E1%BA%BFn%20connect%20Chatty%20v%E1%BB%9Bi%20WhatsApp/image%204.png)

Step 3: Save

![image.png](V%E1%BA%A5n%20%C4%91%E1%BB%81%20li%C3%AAn%20quan%20%C4%91%E1%BA%BFn%20connect%20Chatty%20v%E1%BB%9Bi%20WhatsApp/image%205.png)

---