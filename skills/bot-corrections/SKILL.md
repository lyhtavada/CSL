---
name: bot-corrections
description: Weekly report các câu bot CS (Joyce/Ivy) bị human sửa (correction) để Liz update KB/training data cho bot. Period = Thứ 5 tuần trước → Thứ 4 tuần này.
---

# /bot-corrections — Weekly Bot Correction Report

Pull các **correction** (câu bot trả bị CS sửa) của Joyce (Joy) + Ivy (Chatty) trong
tuần vừa qua (Thứ 5 tuần trước → Thứ 4 tuần này), gom theo topic, ghi report markdown vào repo để Liz dùng
**update data cho bot**.

## Nguồn data

`GET /api/corrections?agent=<id>` trên CS v2 (`cs2.avada.net`) — xem [[cs2_obs_metrics_dashboard]].
- Agent ids: `joy-loyalty-agent` (Joyce), `chatty-agent` (Ivy)
- Auth: `CS2_API_TOKEN` (super_admin) từ `~/CSL/.env`, header `Authorization: Bearer` + `User-Agent` (thiếu UA bị 403)
- Mỗi row: `question`, `original_response` (bot trả), `corrected_response` (CS sửa), `context`, `tags`, `created_by`, `created_at`, `source_session_id`

## Chạy

```bash
# Mặc định: cả Joy + Chatty, rolling 7 ngày kết thúc hôm qua (Thứ 5 → Thứ 4)
python3 skills/bot-corrections/scripts/fetch_corrections.py

# Chỉ 1 app
python3 skills/bot-corrections/scripts/fetch_corrections.py --apps joy

# Window tùy chọn
python3 skills/bot-corrections/scripts/fetch_corrections.py --start 2026-06-16 --end 2026-06-22
```

## Output

File markdown / app trong subfolder theo app `reports/bot-corrections/{app}/`:
`{app}/{app}-corrections-{YYYY-MM-DD thứ-2-đầu-tuần}.md`

Mỗi report có **2 phần** (theo yêu cầu Liz):
1. **📌 Tóm tắt theo topic** — gom correction theo chủ đề (pricing, points/earning,
   setup, integration...), kèm vài ví dụ tiêu biểu + danh sách người sửa.
2. **📋 Chi tiết từng correction** — full `question` / bot trả / CS sửa thành /
   context / session id → đủ để copy thẳng vào KB.

**Retention:** chỉ giữ **2 report gần nhất / app** trong repo — sau khi ghi report
mới, script tự xoá report cũ hơn (`--keep-weeks`, mặc định `2`, `0` = giữ hết).
Không lưu report qua nhiều tuần; lịch sử vẫn tra được qua `git log -- reports/bot-corrections/`
nếu cần.

Sau khi tạo, **commit** vào repo.

## Lưu ý xử lý data

- **Tag nguồn ≠ topic:** tags như `ts-elite`, `src:crisp-extension`, `crisp` là kênh
  submit, KHÔNG phải topic nội dung → script bỏ qua, gom topic bằng heuristic từ khóa.
- **Người sửa thật:** khi `created_by` là token (vd `token:Avada CS Team`, submit qua
  TS Elite), người sửa thật nằm trong `context` (`...by <email>`) → script tự parse +
  map email → tên hiển thị qua `_identity/team-g2.md`.

## Diff vs KB v2 → patch payload (review-gate)

Sau report, tự động so lại từng correction với **KB live trên `cs2.avada.net`** (2
app) rồi soạn sẵn patch để Liz duyệt — KHÔNG tự push.

```
cd ~/CSL/skills/bot-corrections/scripts
python3 prep_kb.py <app>            # cache KB + tìm report mới nhất của app
```
Đọc report → với mỗi correction, tìm file KB liên quan trong cache rồi phân loại:
- **COVERED** — KB đã đúng rồi → KHÔNG cần patch, coi là dấu hiệu **reindex stale**
  (correction không đồng nghĩa KB sai) — xem [[joy_reindex_stale_root_cause]].
- **OUTDATED** — KB có nội dung cũ/sai, mâu thuẫn với `corrected_response` → patch.
- **GAP** — KB chưa có nội dung này → thêm section mới.
- **PARTIAL** — KB có một phần, thiếu đúng điểm CS sửa → bổ sung.

Với mỗi OUTDATED/GAP/PARTIAL, soạn full nội dung file mới (giữ voice/frontmatter
hiện có, viết ĐÚNG 1 ví dụ — KHÔNG viết negative example "đừng nói X" vì bot có thể
copy ra cho khách, xem [[feedback_kb_no_negative_examples]]). Gộp nhiều correction
cùng 1 file KB thành 1 entry. Ghi payloads:
```
reports/analysis/bot-corrections-<app>-<YYYY-MM-DD thứ-2>-payloads.json   # {agent,path,content}[]
```
(gitignored, tạm thời — giống payload của `/kb-sync`).

**Review gate:** dừng lại đây, không tự POST `/api/kb/file` hay reindex. Cron báo
Liz qua Telegram: số COVERED/OUTDATED/GAP/PARTIAL mỗi app + top items + đường dẫn
payload.

Sau khi Liz duyệt, push (dùng lại script của `/kb-sync`, cùng format payload):
```
python3 ~/CSL/skills/kb-sync/scripts/push_kb.py <payloads.json>
```
Tự POST từng file (auto git commit bên v2) + reindex agent liên quan.

## Cron

`com.avada.bot-corrections` — **T2 11:00** hàng tuần (lệch cs-weekly 09:00 để không
chạy chồng). Chạy 2 bước:
1. Script thuần: fetch → ghi report → git commit (repo CSL).
2. Claude headless (`--dangerously-skip-permissions`, subscription OAuth): diff cả
   2 app vs KB v2 → soạn payload patch → DM Telegram Liz để duyệt. KHÔNG tự push.

Source-of-truth: `cron/` (`run-weekly.sh` + `prompt-diff.txt`).
Install: `bash skills/bot-corrections/cron/install.sh` (Liz tự chạy trong Terminal).
Log: `/tmp/bot-corrections.log`.
