# Trên POS ko hiển thị option để edit birthday

Category: POS extension

### **Problem/ Request**

Trên POS không hiển thị tuỳ chọn để chỉnh sửa ngày sinh nhật (birthday) của khách.

❌

![image.png](Tr%C3%AAn%20POS%20ko%20hi%E1%BB%83n%20th%E1%BB%8B%20option%20%C4%91%E1%BB%83%20edit%20birthday/image.png)

✅

![image.png](Tr%C3%AAn%20POS%20ko%20hi%E1%BB%83n%20th%E1%BB%8B%20option%20%C4%91%E1%BB%83%20edit%20birthday/image%201.png)

---

### **Causes**

Ngoài lỗi có thể xảy ra từ extension trên POS, một nguyên nhân khác là do hiện tại **giao diện POS chưa hỗ trợ đầy đủ các định dạng ngày sinh**.

Cụ thể, tuỳ chọn chỉnh sửa **chỉ hiển thị khi ngày sinh của khách được lưu theo định dạng có chứa năm (YYYY)** — ví dụ: `MM/DD/YYYY` hoặc `DD/MM/YYYY`.

→ Nếu ngày sinh chỉ có ngày và tháng (không có năm), POS sẽ không hiển thị nút chỉnh sửa.

→ **CS nên kiểm tra nguyên nhân này trước** nếu merchant đã thử **remove tile và add lại** mà vẫn không thấy hiển thị.

> Team sẽ cập nhật nếu có thay đổi từ phía Shopify trong tương lai.
> 

---

### **Flow**

1. Kiểm tra ngày sinh của khách đã lưu trong app.
2. Nếu chưa đúng định dạng (bao gồm cả YYYY), có thể chỉnh sửa lại trực tiếp trên trang customer detail. MC có thể thử lại trên POS extension sau khi đã sửa customer’s birthday.

![image.png](Tr%C3%AAn%20POS%20ko%20hi%E1%BB%83n%20th%E1%BB%8B%20option%20%C4%91%E1%BB%83%20edit%20birthday/image%202.png)

1. Sau đó, MC vào Birthday program, chọn lại **Date format** có chứa cả **YYYY để có thể collect được cả năm sinh của các customer mới.**

![image.png](Tr%C3%AAn%20POS%20ko%20hi%E1%BB%83n%20th%E1%BB%8B%20option%20%C4%91%E1%BB%83%20edit%20birthday/image%203.png)

1. Nếu thay đổi date format mà issue vẫn xảy ra thì CS xin thông tin thiết bị, POS version và xin quyền truy cập cho email của techlead để check sâu hơn.