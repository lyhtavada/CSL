# Setup API access — BigQuery (Crisp chat) & Avada Ticket API

Bài này chỉ làm **sau khi** đã xong Buổi 1-4 (cài Zed/Codex, quen `AGENTS.md`,
làm thử bài thực hành cơ bản). Mục đích: cho Codex đọc được data thật —
lịch sử chat Crisp (qua BigQuery, không qua Crisp API) và ticket (qua Avada
Ticket API) — để luyện tập trên case thật thay vì data mẫu.

## Quy tắc số 1 — bắt buộc đọc trước khi làm

**Không bao giờ gõ hoặc paste key/credential trực tiếp vào ô chat với Codex.**
Nếu paste vào đó, nó sẽ nằm trong lịch sử chat — rất khó thu hồi lại. Key
**chỉ** được đặt trong file `.env`, Codex tự đọc file này khi cần mà không
cần bạn gõ giá trị ra.

## Bước 1 — nhận credential của bạn

Liz sẽ gửi 1 link qua **secret.avada.net** (không dán thẳng vào Slack).
Mở link, đăng nhập email Avada, copy nội dung — gồm:
- 3 dòng BigQuery service account (`BQ_SA_CLIENT_EMAIL`, `BQ_SA_PRIVATE_KEY_ID`,
  `BQ_SA_PRIVATE_KEY`)
- 1 dòng `AVD_TICKET_API_KEY`

Link chỉ xem được vài lần rồi hết hạn — copy hết ngay, đừng để dành.

## Bước 2 — tạo file `.env`

1. Trong thư mục `codex-starter-kit` (bản bạn đã copy ra chỗ riêng), copy
   file `.env.example` thành file mới tên `.env` (bỏ chữ `.example`) — nằm
   cùng cấp với `AGENTS.md`.
2. Điền các giá trị vừa nhận vào đúng dòng tương ứng. Riêng
   `BQ_SA_PRIVATE_KEY` là 1 chuỗi dài có `\n` bên trong — copy nguyên văn cả
   dấu ngoặc kép, đừng tự xuống dòng.
3. `AVD_API_BASE` và `CRISP_WEBSITE_RETENTION` đã điền sẵn trong
   `.env.example` — không phải bí mật, giữ nguyên.
4. Lưu file lại.

## Bước 3 — kiểm tra không bị lộ ra ngoài

- `.gitignore` trong thư mục này đã tự chặn `.env` khỏi git — nhưng **luôn
  kiểm tra lại** trước khi push lên `git.avada.net`: chạy `git status`, nếu
  thấy `.env` (không phải `.env.example`) nằm trong danh sách sẽ commit thì
  **dừng lại, đừng commit**, hỏi Liz hoặc Betty ngay.
- Không copy nội dung `.env` dán vào đâu khác (Slack, note, doc chia sẻ).

## Bước 4 — dùng thử với Codex

- "Query BigQuery bảng `avada-crm.avada_cs.crisp_chats`, lọc `website_id`
  = giá trị trong `CRISP_WEBSITE_RETENTION`, lấy đoạn chat gần nhất của
  session `<session_id>`, tóm tắt yêu cầu chính" — chạy qua Python +
  `google-cloud-bigquery` (dùng scope `bigquery` + `cloud-platform`, không
  dùng `bigquery.readonly`).
- "Gọi Avada Ticket API (`GET $AVD_API_BASE/tickets`, header
  `Authorization: Bearer $AVD_TICKET_API_KEY`), lấy 5 ticket mới nhất của
  tôi, tóm tắt nội dung chính."

Codex tự đọc `.env` để lấy credential khi cần — bạn không cần nhắc lại mỗi
lần hỏi.

## Nếu nghi ngờ credential bị lộ

Báo Liz ngay để rotate lại (BQ service account key / Avada Ticket API key) —
key dùng chung cho cả team nên lộ 1 chỗ là ảnh hưởng tất cả, đừng đợi "chắc
chắn" mới báo.
