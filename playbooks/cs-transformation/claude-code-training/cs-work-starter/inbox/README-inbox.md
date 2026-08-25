# Folder `inbox/` — quăng file thô vào đây

## Dùng thế nào

Bất cứ file nào bạn muốn Claude xử lý → **copy vào đây trước**.

Nhớ lại quy tắc số 1: **Claude chỉ thấy những gì trong folder `cs-work`.**
File ở Desktop hay Downloads → nó không thấy.

## Bỏ được những gì vào đây

| Loại | Ví dụ | Claude làm được gì |
|---|---|---|
| `.csv` / `.xlsx` | export chat, export ticket | Đếm, nhóm, tìm xu hướng, tìm bất thường |
| `.txt` / `.md` | transcript chat, note | Tóm tắt, rút ý chính, soạn reply |
| Ảnh `.png` / `.jpg` | screenshot lỗi merchant gửi | Đọc nội dung ảnh, mô tả lỗi, gợi ý nguyên nhân |
| `.pdf` | tài liệu, hóa đơn | Đọc, trích thông tin |

## Đặt tên file

✅ `chatty-chat-export-2026-08.csv`
✅ `ticket-refund-t8.xlsx`
❌ `Báo cáo tháng 8.csv` (có dấu + khoảng trắng)
❌ `export (1).csv` (không biết là cái gì)
❌ `new.csv`

## ⚠️ Trước khi bỏ file vào — kiểm 1 lượt

Xóa hoặc che những thứ này nếu có trong file:

- API key, access token, mật khẩu
- Thông tin thẻ thanh toán
- Danh sách email khách hàng của merchant
- Bất cứ thứ gì bạn sẽ ngại nếu nó bị lộ ra ngoài

Không chắc → hỏi Liz trước khi dùng.

## Dọn dẹp

Xử lý xong → chuyển file sang `done/`. Đừng để `inbox/` chất đống, nó sẽ chậm và bạn cũng khó tìm.
