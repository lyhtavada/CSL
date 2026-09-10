# Setup API access cho Crisp / Helpdesk — hướng dẫn tạo file `.env`

Bài này chỉ làm **sau khi** đã xong Buổi 1-4 (cài Zed/Codex, quen `AGENTS.md`,
làm thử bài thực hành cơ bản). Mục đích: cho Codex đọc/gọi được data thật từ
Crisp và Helpdesk (Avada Ticket) để bạn luyện tập trên case thật thay vì data
mẫu.

## Quy tắc số 1 — bắt buộc đọc trước khi làm

**Không bao giờ gõ hoặc paste API key trực tiếp vào ô chat với Codex.**
Nếu bạn paste key vào đó, key sẽ nằm trong lịch sử chat — rất khó thu hồi lại.
Key **chỉ** được đặt trong file `.env`, một file riêng nằm cạnh `AGENTS.md`,
Codex tự đọc file này khi cần mà không cần bạn gõ giá trị ra.

## Bước 1 — nhận key của bạn

Liz sẽ gửi bạn 1 link riêng qua **secret.avada.net** (không phải dán thẳng
key vào Slack). Mở link đó, đăng nhập bằng email Avada, bạn sẽ thấy key thật.
Copy lại — link chỉ xem được vài lần rồi hết hạn nên đừng để dành.

## Bước 2 — tạo file `.env`

1. Trong thư mục `codex-starter-kit` (bản bạn đã copy ra chỗ riêng), tìm file
   `.env.example`.
2. Copy file đó thành 1 file mới tên đúng là `.env` (bỏ chữ `.example`) —
   nằm cùng cấp với `AGENTS.md`.
   - Trên máy Mac: chuột phải → Duplicate → đổi tên thành `.env`.
   - Hoặc mở Zed, mở file `.env.example`, "Save As" → gõ tên `.env`.
3. Mở file `.env` vừa tạo, điền key thật vào sau dấu `=`, ví dụ:
   ```
   CRISP_API_KEY=bf3b704a-8496-...
   HELPDESK_API_KEY=avd_xxxxxx...
   ```
   Không có khoảng trắng quanh dấu `=`, không có dấu ngoặc kép trừ khi key
   gốc có ký tự đặc biệt.
4. Lưu file lại.

## Bước 3 — kiểm tra không bị lộ ra ngoài

- File `.gitignore` trong thư mục này đã tự chặn `.env` không bị đưa lên git —
  bạn không cần tự làm gì thêm, nhưng **nhớ kiểm tra lại** trước khi
  push/commit bất cứ gì lên git.avada.net: chạy `git status`, nếu thấy dòng
  nào có chữ `.env` (không phải `.env.example`) được liệt kê để commit thì
  **dừng lại, đừng commit**, hỏi Liz hoặc Betty ngay.
- Không copy nội dung `.env` dán vào đâu khác (Slack, note, doc chia sẻ).

## Bước 4 — dùng thử với Codex

Giờ có thể nhờ Codex việc cần data thật, ví dụ:
- "Đọc 5 ticket Helpdesk mới nhất của tôi, tóm tắt nội dung chính"
- "Lấy đoạn chat Crisp gần nhất của merchant X, tóm tắt yêu cầu"

Codex tự đọc `.env` để lấy key khi gọi API — bạn không cần nhắc lại key mỗi
lần hỏi.

## Nếu nghi ngờ key đã bị lộ

Báo Liz ngay để rotate lại key tại nguồn (Crisp dashboard / Avada Ticket
admin) — key cũ dùng tiếp là rủi ro, không đợi "chắc chắn" mới báo.
