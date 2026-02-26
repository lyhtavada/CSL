# MC edit email notification content nhưng thay đổi ko được lưu lại

Category: Notifications

### **Problem/ Request**

Merchant chỉnh sửa nội dung email notification nhưng sau khi nhấn “Save changes” thì thay đổi không được lưu. Khi reload trang, nội dung cũ vẫn hiển thị.

---

### **Causes**

- Đây là lỗi kỹ thuật thỉnh thoảng có thể xảy ra do hệ thống không ghi nhận đúng thao tác lưu của người dùng.
- Có thể do kết nối mạng tạm thời không ổn định hoặc thao tác lưu bị gián đoạn.

---

### **Flow**

1. Xác nhận lại với MC rằng họ đã nhấn nút **Save changes** sau khi chỉnh sửa nội dung.
2. Hướng dẫn MC **copy nội dung vừa chỉnh sửa ra file bên ngoài** (phòng trường hợp bị mất nội dung).
3. Yêu cầu MC, dùng shortcut **`!email_edit_not_saved`**:
    - **Logout khỏi app**, sau đó **login lại và thử chỉnh sửa lại một lần nữa**.
    - Sau khi chỉnh sửa, **đợi khoảng 3-5 giây** sau khi nhấn Save rồi mới reload trang để đảm bảo hệ thống xử lý xong.
4. Nếu sự cố vẫn xảy ra, báo dev team với thông tin:
    - Tên merchant + link store
    - Tên template email gặp lỗi
    - Thời gian gặp lỗi (timestamp gần nhất)