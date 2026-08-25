# Claude Code Starter Kit cho CS

Đây là **thư mục mẫu** để bắt đầu dùng Claude Code (hoặc Codex) — đi kèm với training plan ở
`../claude-code-training-plan.md`.

## Cách bắt đầu

1. **Copy cả thư mục này** ra vị trí riêng của bạn (ví dụ `~/claude-workspace/`), không làm việc trực tiếp trong repo CSL của Liz.
2. Mở terminal tại thư mục vừa copy, gõ `claude` (hoặc mở thư mục này bằng IDE có extension Claude Code/Codex).
3. Mở file `CLAUDE.md` → điền thông tin của bạn (tên, app phụ trách, quy tắc làm việc riêng). File này agent sẽ tự đọc mỗi lần bạn làm việc — không cần giải thích lại.
4. Thử luôn các bài tập ở Mục 6 trong training plan:
   - Bỏ 1 file chat log/ticket vào `data/` → nhờ agent tóm tắt (`notes/`)
   - Bỏ 2 file CSV (tuần này/tuần trước) vào `data/` → nhờ so sánh
   - Mở `templates/report-template.md` → nhờ agent điền báo cáo theo đúng format, dùng data trong `data/`
   - Mở `templates/faq-entry-template.md` → nhờ viết thêm câu hỏi mới theo đúng format

## Cấu trúc thư mục

```
claude-code-starter-kit/
├── CLAUDE.md                      ← file quy tắc — điền thông tin của bạn vào đây
├── data/                          ← bỏ file bạn muốn agent đọc vào đây (CSV, chat log export, ticket export...)
├── reports/                       ← nơi agent xuất báo cáo/kết quả ra
├── templates/                     ← mẫu có sẵn để agent điền theo, không phải tạo từ đầu
│   ├── report-template.md
│   └── faq-entry-template.md
└── notes/                         ← ghi chú/tóm tắt nhanh trong lúc thực hành
```

## Lưu ý an toàn

- Đây là workspace luyện tập — **không bỏ data thật nhạy cảm của merchant** (thông tin thanh toán, mật khẩu) vào `data/` nếu chưa cần thiết.
- Mọi output ở đây là **nháp để luyện tập** — không gửi thẳng cho merchant hay đăng lên Slack team nếu chưa qua review.
- Xem đầy đủ nguyên tắc an toàn ở Mục 9 trong `../claude-code-training-plan.md`.
