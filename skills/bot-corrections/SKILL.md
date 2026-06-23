---
name: bot-corrections
description: Weekly report các câu bot CS (Joyce/Ivy) bị human sửa (correction) để Liz update KB/training data cho bot. Period = Mon→Sun tuần trước.
---

# /bot-corrections — Weekly Bot Correction Report

Pull các **correction** (câu bot trả bị CS sửa) của Joyce (Joy) + Ivy (Chatty) trong
tuần trước (Mon→Sun), gom theo topic, ghi report markdown vào repo để Liz dùng
**update data cho bot**.

## Nguồn data

`GET /api/corrections?agent=<id>` trên CS v2 (`cs2.avada.net`) — xem [[cs2_obs_metrics_dashboard]].
- Agent ids: `joy-loyalty-agent` (Joyce), `chatty-agent` (Ivy)
- Auth: `CS2_API_TOKEN` (super_admin) từ `~/CSL/.env`, header `Authorization: Bearer` + `User-Agent` (thiếu UA bị 403)
- Mỗi row: `question`, `original_response` (bot trả), `corrected_response` (CS sửa), `context`, `tags`, `created_by`, `created_at`, `source_session_id`

## Chạy

```bash
# Mặc định: cả Joy + Chatty, tuần TRƯỚC trọn vẹn (Mon→Sun)
python3 skills/bot-corrections/scripts/fetch_corrections.py

# Chỉ 1 app
python3 skills/bot-corrections/scripts/fetch_corrections.py --apps joy

# Window tùy chọn
python3 skills/bot-corrections/scripts/fetch_corrections.py --start 2026-06-16 --end 2026-06-22
```

## Output

File markdown / app trong `reports/bot-corrections/`:
`{app}-corrections-{YYYY-MM-DD thứ-2-đầu-tuần}.md`

Mỗi report có **2 phần** (theo yêu cầu Liz):
1. **📌 Tóm tắt theo topic** — gom correction theo chủ đề (pricing, points/earning,
   setup, integration...), kèm vài ví dụ tiêu biểu + danh sách người sửa.
2. **📋 Chi tiết từng correction** — full `question` / bot trả / CS sửa thành /
   context / session id → đủ để copy thẳng vào KB.

Sau khi tạo, **commit** vào repo.

## Lưu ý xử lý data

- **Tag nguồn ≠ topic:** tags như `ts-elite`, `src:crisp-extension`, `crisp` là kênh
  submit, KHÔNG phải topic nội dung → script bỏ qua, gom topic bằng heuristic từ khóa.
- **Người sửa thật:** khi `created_by` là token (vd `token:Avada CS Team`, submit qua
  TS Elite), người sửa thật nằm trong `context` (`...by <email>`) → script tự parse +
  map email → tên hiển thị qua `_identity/team-g2.md`.

## Sau khi có report

Liz đọc report → cập nhật KB/training data cho bot. Có 2 đường:
- Sửa trực tiếp KB v2 qua `/kb-sync` (push `POST /api/kb/file` + reindex) — xem [[kb_sync_v2]]
- ⚠️ Khi viết KB từ correction: viết cái ĐÚNG, KHÔNG viết negative example kèm "đừng
  nói X" (bot copy ra cho khách) — xem [[feedback_kb_no_negative_examples]]

## Cron

`com.avada.bot-corrections` — **T2 11:00** hàng tuần (lệch cs-weekly 09:00 để không
chạy chồng). Tự chạy script → ghi file → commit. Source-of-truth: `cron/`.
Install: `bash skills/bot-corrections/cron/install.sh` (Liz tự chạy trong Terminal).
Log: `/tmp/bot-corrections.log`.
