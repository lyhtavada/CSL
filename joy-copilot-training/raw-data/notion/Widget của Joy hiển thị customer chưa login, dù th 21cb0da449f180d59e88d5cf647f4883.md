# Widget của Joy hiển thị customer chưa login, dù thực tế họ đã login vào tài khoản

Category: Onsite content

## **Problem/Request**

Với store dùng Customer Accounts (New), đôi lúc xảy ra vấn đề widget của app hiển thị customer chưa đăng nhập, dù thực tế khách đã đăng nhập vào tài khoản.

---

## **Causes**

Đây là lỗi liên quan đến Shopify: với Shopify Customer Accounts, đôi khi xảy ra hiện tượng **Shopify không cập nhật chính xác trạng thái đăng nhập của khách hàng**. Điều này thường xảy ra khi khách đăng nhập xong nhưng quay lại trang trước, Shopify không đồng bộ trạng thái Single Sign-On (SSO) kịp thời → dẫn đến widget vẫn hiển thị khách chưa đăng nhập.

---

## **Flow**

CS dùng shortcut **`!sso` :**

- Hiện tại, để workaround, có thể hướng dẫn khách hàng sau khi login hãy nhấn nút **Join program** trên widget Joy Loyalty. Việc này sẽ kích hoạt xác thực lại login và widget sẽ hiển thị đúng trạng thái.
- Để giảm thiểu khả năng xảy ra lỗi, có thể thiết lập Shopify redirect khách về trang trước khi login thay vì account page, theo hướng dẫn:
    
    [How to redirect customers to the previous page instead of the account page with Shopify NCA](https://help.joy.so/how-to-redirect-customers-to-the-previous-page-instead-of-the-account-page-with-shopify-nca)
    
- Dev team của Joy Loyalty hiện đã ghi nhận và đang tìm giải pháp xử lý triệt để hơn.