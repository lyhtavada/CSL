# Ẩn activity logs related to manual point adjustments phía Customer

Category: General, Onsite content

## **Problem/Request**

MC không muốn hiển thị các hoạt động điều chỉnh điểm thủ công (manual point adjustments) trong mục **Activity logs** mà customer (end-user) có thể nhìn thấy trên widget hoặc account page.

![image.png](%E1%BA%A8n%20activity%20logs%20related%20to%20manual%20point%20adjustmen/image.png)

---

## **Causes**

- Một số cửa hàng cần thực hiện điều chỉnh điểm thủ công cho khách (cộng/trừ điểm) vì các lý do như giải quyết khiếu nại, tặng điểm bù, điều chỉnh sai sót.
- Việc để các hoạt động điều chỉnh điểm này hiển thị cho end-customer có thể gây nhầm lẫn hoặc làm phát sinh câu hỏi không cần thiết.
- Hiện tại, hệ thống Joy Loyalty không có tuỳ chọn ẩn riêng biệt cho các logs này, nên cần xử lý qua backend.

---

## **Flow**

1. MC gửi yêu cầu cần ẩn các activity logs liên quan đến điều chỉnh điểm thủ công ở phía Customer.
2. CS vào dev_zone > Enable option: **Enable hide adjust point activity for customer**

![image.png](%E1%BA%A8n%20activity%20logs%20related%20to%20manual%20point%20adjustmen/image%201.png)

- Sau khi enable, tất cả các activity liên quan đến việc điều chỉnh point manually sẽ bị ẩn ở widget hoặc account/ loyalty page khi customer login.
1. CS update và nhờ MC check lại từ phía họ.
2. Follow-up để đảm bảo logs đã ẩn đúng như yêu cầu.
- Nếu merchant phản hồi vẫn còn hiển thị hoặc có lỗi khác phát sinh, escalate lại dev để kiểm tra thêm.

---

**Lưu ý:** Việc xoá/ẩn logs chỉ ảnh hưởng đến hiển thị của end-customer, không làm mất dữ liệu ghi nhận trong hệ thống admin (để đảm bảo audit trail nội bộ).