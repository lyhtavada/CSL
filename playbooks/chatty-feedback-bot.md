# Chatty Feedback Bot — Spec

**Status:** Working (local)
**Owner:** Liz (G2 CS Leader)
**Created:** 2026-03-03
**Updated:** 2026-03-12

---

## 1. Mục đích

Merchant dùng Chatty có thể feedback trực tiếp cho từng AI reply trong conversation. Feedback này được sync tự động vào Slack channel. Hiện tại không có ai monitor channel này thường xuyên → feedback bị bỏ sót, merchant có thể không được followup.

**Bot giải quyết:** Khi có feedback mới → xác định ca đang trực → tự động tag CS Chatty trong ca đó → CS followup với merchant + ghi lại action đã thực hiện. Nếu CS chưa phản hồi sau 15 phút → nhắc lại 1 lần.

---

## 2. Flow

```
Merchant feedback → #chatty-notice channel (C08TSD3EET0)
        ↓
Bot poll mỗi 15 phút, lookback 12 giờ
        ↓
Phát hiện message mới (chưa có reply)
        ↓
Kiểm tra loại message:
  → "Customer Data Request" → skip (không cần CS action)
  → Feedback thường → tiếp tục
        ↓
Phát hiện feedback mới (chưa có reply)
        ↓
Xác định ca hiện tại dựa vào giờ VN (UTC+7)
        ↓
Đọc #workshift channel (C034NAWKMFA)
  → Parse "*check in*" / "*check out*" (Slack bold format)
  → Lọc từ đầu ca hiện tại đến hiện tại
  → Loại những ai đã check out
  → Filter chỉ lấy Chatty CS (theo config)
  → Match case-insensitive (Hienpt → HienPT)
        ↓
Tag CS Chatty đang trực vào thread (lần 1)
        ↓
Poll tiếp → 15 phút sau nếu chỉ có bot reply, CS chưa reply
  → Gửi reminder (lần 2, max)
        ↓
CS vào thread, comment:
  - Link conversation (nếu có)
  - Action đã thực hiện
```

### Reply logic

| reply_count | Hành động |
|---|---|
| 0 | Tag CS lần đầu |
| 1 (chỉ bot) | Gửi reminder |
| 1 (có CS reply) | Skip — đã xử lý |
| >= 2 | Skip |

---

## 3. Ca trực

Có 6 ca trong ngày (timezone: Asia/Ho_Chi_Minh — UTC+7):

| Ca | Bắt đầu | Kết thúc |
|---|---|---|
| Ca 1 | 00:00 | 04:10 |
| Ca 2 | 04:00 | 08:10 |
| Ca 3 | 08:00 | 12:10 |
| Ca 4 | 12:00 | 16:10 |
| Ca 5 | 16:00 | 20:10 |
| Ca 6 | 20:00 | 00:10 |

> Overlap 10 phút giữa các ca. Trong khoảng overlap, bot xét cả 2 ca, tag tất cả CS đang trực.

---

## 4. Workshift message format

Bot parse message trong #workshift theo regex (hỗ trợ Slack bold `*...*`):

```
[username] *check in* Shift-X - D/M/YYYY On time ...
[username] *check out* Shift-X - D/M/YYYY In time ...
```

Logic:
1. Xác định ca hiện tại theo giờ VN
2. Tìm check in/out trong #workshift từ shift_start đến hiện tại
3. Loại ai đã check out
4. Strip đuôi suffix (`.ctv`, `.cds`, v.v.) khỏi username trước khi match
5. Match case-insensitive với Chatty CS trong config
5. Trả về Slack IDs để tag

---

## 5. Chatty CS mapping

Cấu hình trong `config.json`, sửa không cần restart bot.

| Tên | Workshift username | Slack ID |
|---|---|---|
| Jade | PhuongNT | U07CGHSHNMB |
| Andy | AnhBD | U09DC212XN0 |
| Hazel | HienPT | U09FYACFH2T |
| Cody | ChauHM | U08TZM2LL74 |
| Mirra | MinhBT | U08GX75N5CZ |
| Phoebe | PhuongTTM | U0A84BE00FK |
| Megan | TrangNTH | U09FJ7F2G1Z |

---

## 6. Messages

**Lần 1 (tag):**
```
@CS1 @CS2 ace tìm hoặc tạo chat để fu với KH rồi log lại actions mình đã làm nha!
```

**Lần 2 (reminder — sau 15 phút nếu CS chưa reply):**
```
@CS1 @CS2 nhắc lại: ace chưa reply thread này nha! Tìm/tạo chat fu với KH rồi log actions vào đây.
```

Cả 2 message đều sửa được trong `config.json` không cần restart.

---

## 7. Edge cases

| Tình huống | Xử lý |
|---|---|
| Không có Chatty CS nào check in trong ca | Không tag, log, poll sau thử lại (trong 12 giờ lookback) |
| Workshift username chưa được map trong config | Bỏ qua agent đó |
| Username có đuôi suffix (`.ctv`, `.cds`, v.v.) | Strip suffix trước khi match — `Phuongttm.ctv` → match `PhuongTTM` |
| Overlap 10 phút giữa 2 ca | Xét cả 2 ca, tag tất cả CS đang trực |
| Bot restart | Dùng reply_count từ Slack API, không mất state |
| Message là "Customer Data Request" | Skip — không tag CS, không remind |
| Feedback đến ngoài lookback 12 giờ | Không xử lý |
| Người ngoài reply thread (không phải CS) | Coi là đã xử lý, skip |

---

## 8. Config

### Environment (.env)

| Key | Value |
|---|---|
| SLACK_BOT_TOKEN | `xoxb-...` |
| FEEDBACK_CHANNEL_ID | `C08TSD3EET0` (optional, có default) |
| WORKSHIFT_CHANNEL_ID | `C034NAWKMFA` (optional, có default) |

### config.json (hot-reload, không cần restart)

| Key | Mô tả |
|---|---|
| pollIntervalMinutes | Tần suất poll (hiện tại: 15) |
| message | Nội dung tag lần đầu |
| reminderMessage | Nội dung nhắc lại |
| chattyCS | Map username → Slack ID |

---

## 9. Tech stack

- **Runtime:** Node.js
- **Slack:** `@slack/web-api` (polling, không cần Socket Mode / App-Level Token)
- **Config:** `config.json` hot-reload (xóa require cache mỗi poll)
- **Code:** `bots/chatty-feedback-bot/`

---

## 10. Cần làm tiếp

| # | Item |
|---|---|
| 1 | Deploy lên server (hiện chạy local) — cần pm2 hoặc tương tự để auto-restart |
| 2 | Persistent logging (ghi file hoặc gửi về Slack channel riêng) |
| 3 | Cân nhắc escalation nếu sau reminder CS vẫn không reply (tag Liz / gửi #urgent) |
