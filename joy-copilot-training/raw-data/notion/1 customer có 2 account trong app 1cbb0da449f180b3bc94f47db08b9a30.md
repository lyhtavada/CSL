# 1 customer có 2 account trong app

Category: Customers

### 🎯 **Scenario**

Một customer xuất hiện dưới hai tài khoản khác nhau trong app – một tài khoản cho mua hàng online, một tài khoản cho mua hàng offline qua POS.

---

### ⁉️ **Possible Causes**

- Shopify tạo **2 customer IDs** riêng biệt cho cùng một người, thường xảy ra khi:
    - Khách mua online sử dụng email/ phone number
    - Khách mua offline qua POS mà không dùng đúng thông tin email/sđt đã có trước đó
- Do sự khác biệt trong thông tin nhận diện (email, số điện thoại), hệ thống ghi nhận là 2 người dùng khác nhau.

---

### ➡️ **Support Flow**

### 1. **Xác nhận danh tính của 2 accounts**

CS cần kiểm tra với MC:

- Email hoặc thông tin liên quan của 2 account bị trùng lặp
- Khách có thật sự là cùng một người không?

### 2. **Giải thích nguyên nhân cho MC**

Giải thích với MC rằng:

> ***Shopify will generate two separate customer IDs if the customer information doesn’t fully match — for example, if they make an in-store purchase without providing the same email or phone number used online. As a result, Joy recognizes them as two different users.***
> 

### 3. **Đề xuất hướng xử lý**

- CS  có thể đề xuất với MC về việc merge 2 account này với nhau, nếu MC đồng ý, CS chuyển thông tin cho dev team để tiến hành merge

   → Sau khi hợp nhất, Joy sẽ tự đồng bộ lại thông tin và thống nhất điểm/tier cho 1 account duy nhất.

---

### 📌 Lưu ý cho CS

- Không can thiệp trực tiếp vào việc gộp account trong Joy (phụ thuộc vào Shopify)
- Cần giải thích rõ để MC hiểu cách hoạt động của Shopify và Joy trong việc nhận diện khách hàng
- Hướng dẫn MC theo từng bước cụ thể nếu họ cần hợp nhất customer.