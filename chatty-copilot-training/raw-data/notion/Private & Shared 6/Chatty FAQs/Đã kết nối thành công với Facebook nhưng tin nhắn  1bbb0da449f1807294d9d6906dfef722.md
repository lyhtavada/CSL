# Đã kết nối thành công với Facebook nhưng tin nhắn mới không hiển thị trong Chatty

Category: Channels

⚠️ **Problem/ Request:**

Đã kết nối thành công với Facebook nhưng tin nhắn mới không hiển thị trong Chatty

🛠 Nguyên nhân phổ biến & cách khắc phục

- Cần đảm bảo là MC đã hoàn thành integrate Messenger với Chatty

![image.png](%C4%90%C3%A3%20k%E1%BA%BFt%20n%E1%BB%91i%20th%C3%A0nh%20c%C3%B4ng%20v%E1%BB%9Bi%20Facebook%20nh%C6%B0ng%20tin%20nh%E1%BA%AFn%20/image.png)

- Người thực hiện connect 2 channels với nhau chưa có đủ quyền truy cập tin nhắn ở FB page đó.

⇒ truy cập lại phần **Page Settings > Page Roles & Permissions** để đảm bảo bạn đã **cấp quyền “Manage and access Page messages”**.

- Đôi khi, khi kết nối, Facebook không đồng bộ hết quyền nếu bạn bỏ chọn 1 số mục trong popup cấp quyền.
- Customers gửi tin nhắn trước khi Chatty được kết nối

⇒ Chỉ những tin nhắn **được gửi sau khi Chatty kết nối thành công** mới được đồng bộ về inbox của Chatty.

- Với các tin cũ, bạn vẫn có thể trả lời từ Facebook Messenger.