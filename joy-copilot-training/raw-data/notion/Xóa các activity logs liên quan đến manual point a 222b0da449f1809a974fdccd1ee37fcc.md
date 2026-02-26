# Xóa các activity logs liên quan đến manual point adjustments

Category: General, Onsite content

## **Problem/Request**

MC không muốn hiển thị các hoạt động điều chỉnh điểm thủ công (manual point adjustments) trong mục **Activity logs** mà khách hàng (end-customer) có thể nhìn thấy trên widget hoặc trang tài khoản.

---

## **Causes**

- Một số cửa hàng cần thực hiện điều chỉnh điểm thủ công cho khách (cộng/trừ điểm) vì các lý do như giải quyết khiếu nại, tặng điểm bù, điều chỉnh sai sót.
- Việc để các hoạt động điều chỉnh điểm này hiển thị cho end-customer có thể gây nhầm lẫn hoặc làm phát sinh câu hỏi không cần thiết.
- Hiện tại, hệ thống Joy Loyalty không có tuỳ chọn ẩn riêng biệt cho các logs này, nên cần xử lý qua backend.

---

## **Flow**

1️⃣ MC gửi yêu cầu cần xóa các activity logs liên quan đến điều chỉnh điểm thủ công.

- Trong trường hợp merchant chỉ muốn xoá activity logs ở frontend (widget hoặc loyalty page)
CS có thể suggest merchant giải pháp ẩn các activity đó thay vì xoá hoàn toàn, vì:
    - Hoạt động vẫn được lưu trong admin để đảm bảo lịch sử rõ ràng, dễ quản lý về sau.
    - Tránh trường hợp bị thiếu dữ liệu khi cần đối soát hoặc hỗ trợ khách hàng sau này.
    
    Nếu merchant đồng ý, CS làm theo hướng dẫn trong bài sau để hỗ trợ nhanh:
    

[Xóa các activity logs liên quan đến manual point adjustments](X%C3%B3a%20c%C3%A1c%20activity%20logs%20li%C3%AAn%20quan%20%C4%91%E1%BA%BFn%20manual%20point%20a%20222b0da449f1809a974fdccd1ee37fcc.md)

2️⃣ Nếu MC vẫn muốn xóa, CS cần collect các thông tin:

- Store name
- Cụ thể khoảng thời gian hoặc hoạt động nào cần ẩn

3️⃣ CS tạo Trello card, báo dev team thực hiện xoá các log này khỏi giao diện khách hàng (frontend).

4️⃣ Sau khi dev confirm đã xử lý xong, CS cần:

- Gửi email cập nhật cho merchant.
- Đề nghị họ double-check từ phía customer account.
- Follow-up để đảm bảo logs đã ẩn đúng như yêu cầu.

5️⃣ Nếu merchant phản hồi vẫn còn hiển thị hoặc có lỗi khác phát sinh, escalate lại dev để kiểm tra thêm.