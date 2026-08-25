# [Tên của bạn] — Workspace

> `AGENTS.md` là "file quy tắc cố định" chuẩn của Codex — Codex tự đọc file này mỗi lần bạn mở
> Zed/terminal ở thư mục này, nên bạn không cần giải thích lại context mỗi lần hỏi. Điền thông tin
> thật của bạn vào các mục dưới đây.

## Bạn là ai

- Tên: **[điền tên]**
- Vai trò: CS Agent phụ trách **[Chatty / Joy Loyalty / Joy Wishlist — điền app bạn phụ trách]**
- Công việc chính: **[ví dụ: trực chat, xử lý ticket, DFY onboarding, QA...]**
- Ngôn ngữ: tiếng Việt cho ghi chú nội bộ; tiếng Anh khi soạn nội dung gửi merchant

## Cấu trúc thư mục này

- `data/` — nơi bỏ file bạn muốn Codex đọc (CSV, export chat log, export ticket...)
- `reports/` — nơi Codex xuất báo cáo/kết quả ra
- `templates/` — mẫu có sẵn, nhờ Codex điền theo đúng format thay vì tạo từ đầu
- `notes/` — ghi chú/tóm tắt nhanh

## Quy tắc làm việc

- Khi mình nhờ làm gì, **thực hiện luôn**, không hỏi lại trừ khi thật sự mơ hồ
- Khi tạo nội dung (báo cáo, FAQ, email), **làm trực tiếp trong session**, không cần viết script
- **Luôn để mình duyệt trước khi gửi bất cứ thứ gì ra ngoài** (merchant, Slack, hệ thống live) — đây là nguyên tắc bắt buộc, không có ngoại lệ
- Không paste/lưu data nhạy cảm của merchant (thanh toán, mật khẩu) vào workspace này nếu không thật sự cần

## Nguồn dữ liệu tôi hay dùng

> Điền nguồn thật của bạn — càng cụ thể, Codex càng đỡ đoán sai.

- Data ca trực / báo cáo: **[ví dụ: Google Sheet link, hoặc file export ở đâu]**
- Tra cứu KB / quy trình: **[ví dụ: link cs2.avada.net, hoặc thư mục kb/cs-process/ trong repo CSL]**
- Case cần tham khảo: **[ví dụ: Crisp, Avada Ticket]**

## Việc tôi thường nhờ Codex làm ở đây

> Ví dụ mẫu — sửa lại theo đúng công việc thật của bạn, càng cụ thể càng dễ tái sử dụng lần sau.

- Đọc file trong `data/`, tóm tắt nội dung chính + đề xuất hướng xử lý
- So sánh 2 file data (tuần này vs tuần trước), chỉ ra thay đổi đáng chú ý
- Điền báo cáo theo mẫu ở `templates/report-template.md`, dùng data mới nhất trong `data/`
- Soạn thêm câu hỏi FAQ theo mẫu ở `templates/faq-entry-template.md`
