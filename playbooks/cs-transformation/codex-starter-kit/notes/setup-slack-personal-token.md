# Lấy personal Slack token để kết nối với Codex

Token này cho Codex hành động **như chính tài khoản Slack của bạn** (đọc DM, đọc
thread, gửi tin nhắn) — khác với bot chung của team. Mỗi người có 1 token
riêng, không dùng chung với ai.

## Quy tắc số 1

**Không bao giờ paste token này vào chat với Codex hay dán vào Slack.** Chỉ
điền vào file `.env` của bạn (`SLACK_USER_TOKEN=...`), giống các key khác.

## Các bước lấy token

1. Vào [api.slack.com/apps](https://api.slack.com/apps), đăng nhập bằng tài
   khoản Slack Avada của bạn.
2. Nếu workspace đã có sẵn 1 app dùng chung cho việc này (hỏi Liz tên app nếu
   chưa biết) → bấm vào app đó. Nếu chưa có và bạn được phép tự tạo app mới →
   **Create New App** → **From scratch** → đặt tên, chọn workspace **Avada
   Group**.
   - Nếu Slack báo không đủ quyền tạo app (workspace giới hạn bởi admin) →
     báo Liz để xin tạo giúp hoặc xin quyền.
3. Vào **OAuth & Permissions** ở sidebar.
4. Kéo xuống **User Token Scopes** (không phải Bot Token Scopes) — thêm các
   scope cần dùng, ví dụ tối thiểu: `channels:history`, `channels:read`,
   `chat:write`, `search:read`, `users:read`. Hỏi Liz nếu không chắc cần scope
   nào.
5. Kéo lên đầu trang, bấm **Install to Workspace** (hoặc **Reinstall to
   Workspace** nếu app đã cài) → màn hình xin quyền hiện ra → bấm **Allow**
   (đăng nhập bằng chính tài khoản Slack của bạn, không phải tài khoản dùng
   chung).
6. Sau khi cài xong, quay lại **OAuth & Permissions**, phần **OAuth Tokens** —
   copy dòng bắt đầu bằng `xoxp-` (**User OAuth Token**, không phải
   `xoxb-` — đó là bot token, không dùng cho việc này).
7. Dán token vào file `.env` của bạn:
   ```
   SLACK_USER_TOKEN=xoxp-...
   ```

## Kiểm tra nhanh

Nhờ Codex: "đọc 5 tin nhắn mới nhất trong kênh #tên-kênh-bạn-có-quyền-xem" —
nếu trả lời được đúng nội dung thật là token đã hoạt động.

## Nếu nghi ngờ token bị lộ

Vào lại **OAuth & Permissions** → **Revoke Token** → tạo lại từ đầu (bước
5-6). Báo Liz để theo dõi.
