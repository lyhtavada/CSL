# FAQ page của app overwrite các default page template

Category: FAQs

### **Problem/ Request**

Trang FAQ của app Chatty ghi đè lên tất cả các trang "page" trong theme, gây lỗi hiển thị cho các trang nội dung khác (ví dụ: About Us, Contact...).

---

### **Causes**

App Chatty gán nội dung FAQ vào template mặc định, thay vì tạo một template riêng cho trang FAQ. Nếu merchant không cấu hình đúng template và URL, tất cả các trang "page" sẽ bị ảnh hưởng.

---

### **Flow**

CS dùng shortcut: **`!faq_overwrite_fix`**

1. CS giải thích cho MC: App đang dùng template mặc định để hiển thị nội dung FAQ. Vì vậy nếu MC không tạo và gán riêng template cho trang FAQ, tất cả các trang nội dung khác như About Us, Contact... cũng sẽ bị ảnh hưởng và hiển thị sai → Mình sẽ hướng dẫn chi tiết để xử lý.
2. Ở phần "Theme template", chọn hoặc tạo template mới (ví dụ: `chatty-faq`)
3. Vào admin Shopify > Online Store > Pages
4. Chọn FAQ page do app tạo ra, thường có tên là Frequently Asked Questions
5. Assign template này cho đúng trang FAQ vừa tạo
6. Gắn đúng URL của trang FAQ vào phần cấu hình trong app Chatty (ví dụ: `/pages/faq`)
7. Kiểm tra lại các trang nội dung khác để đảm bảo không bị ảnh hưởng

<aside>
⚠️

Nếu MC vẫn ko tự xử lý được, CS cần xin quyền **Themes, Pages và Navigation** để hỗ trợ MC show lại FAQ page (có thể tạo ticket cho TS xử lý).

</aside>