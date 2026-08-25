# Codex Starter Kit cho CS

Đây là **thư mục mẫu** để bắt đầu dùng **Codex trên Zed** — đi kèm với training plan ở
`../codex-training-plan.md`.

## Cách bắt đầu

1. **Copy cả thư mục này** ra vị trí riêng của bạn (ví dụ `~/codex-workspace/`), không làm việc trực tiếp trong repo CSL của Liz.
2. Mở **Zed** → mở thư mục vừa copy → mở panel Codex trong Zed (hoặc gõ `codex` trong terminal tích hợp của Zed).
3. Mở file `AGENTS.md` → điền thông tin của bạn (tên, app phụ trách, quy tắc làm việc riêng). File này Codex sẽ tự đọc mỗi lần bạn làm việc — không cần giải thích lại.
4. Thử luôn các bài tập ở Mục 8 trong training plan:
   - Bỏ 1 file chat log/ticket vào `data/` → nhờ Codex tóm tắt (`notes/`)
   - Bỏ 2 file CSV (tuần này/tuần trước) vào `data/` → nhờ so sánh
   - Mở `templates/report-template.md` → nhờ Codex điền báo cáo theo đúng format, dùng data trong `data/`
   - Mở `templates/faq-entry-template.md` → nhờ viết thêm câu hỏi mới theo đúng format

## Cấu trúc thư mục

```
codex-starter-kit/
├── AGENTS.md                      ← file quy tắc chuẩn của Codex — điền thông tin của bạn vào đây
├── data/                          ← bỏ file bạn muốn Codex đọc vào đây (CSV, chat log export, ticket export...)
├── reports/                       ← nơi Codex xuất báo cáo/kết quả ra
├── templates/                     ← mẫu có sẵn để Codex điền theo, không phải tạo từ đầu
│   ├── report-template.md
│   └── faq-entry-template.md
└── notes/                         ← ghi chú/tóm tắt nhanh trong lúc thực hành
```

## Lưu ý an toàn

- Đây là workspace luyện tập — **không bỏ data thật nhạy cảm của merchant** (thông tin thanh toán, mật khẩu) vào `data/` nếu chưa cần thiết.
- Mọi output ở đây là **nháp để luyện tập** — không gửi thẳng cho merchant hay đăng lên Slack team nếu chưa qua review.
- Xem đầy đủ nguyên tắc an toàn ở Mục 9 trong `../codex-training-plan.md`.
