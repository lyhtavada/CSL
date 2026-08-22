---
name: bot-corrections
description: Daily report các câu bot CS (Joyce/Ivy) bị human sửa (correction) để Liz update KB/training data cho bot. Window = kể từ lần chạy trước (T2-T6 15:00, T2 phủ cả cuối tuần).
---

# /bot-corrections — Daily Bot Correction Report

Pull các **correction** (câu bot trả bị CS sửa) của Joyce (Joy) + Ivy (Chatty) kể
từ lần chạy trước, gom theo topic, ghi report markdown vào repo để Liz dùng
**update data cho bot**. Chạy daily (T2-T6) để bắt lỗi bot sớm và fix nhanh hơn
so với trước (weekly); ngày nào không có correction mới thì im lặng, không noti.

## Nguồn data

`GET /api/corrections?agent=<id>` trên CS v2 (`cs2.avada.net`) — xem [[cs2_obs_metrics_dashboard]].
- Agent ids: `joy-loyalty-agent` (Joyce), `chatty-agent` (Ivy)
- Auth: `CS2_API_TOKEN` (super_admin) từ `~/CSL/.env`, header `Authorization: Bearer` + `User-Agent` (thiếu UA bị 403)
- Mỗi row: `question`, `original_response` (bot trả), `corrected_response` (CS sửa), `context`, `tags`, `created_by`, `created_at`, `source_session_id`

## Chạy

```bash
# Mặc định: cả Joy + Chatty, kể từ lần chạy trước tới giờ (T2 lùi về T6 tuần trước)
python3 skills/bot-corrections/scripts/fetch_corrections.py

# Chỉ 1 app
python3 skills/bot-corrections/scripts/fetch_corrections.py --apps joy

# Window tùy chọn
python3 skills/bot-corrections/scripts/fetch_corrections.py --start 2026-06-16 --end 2026-06-22
```

## Output

File markdown / app trong subfolder theo app `reports/bot-corrections/{app}/`:
`{app}/{app}-corrections-{YYYY-MM-DD ngày chạy}.md`. **App nào 0 correction mới
trong window thì KHÔNG ghi file** (tránh report rỗng mỗi ngày) — script in
`TOTAL_NEW=<n>` ở cuối để cron biết có cần chạy tiếp bước diff/notify hay không.

Mỗi report có **2 phần** (theo yêu cầu Liz):
1. **📌 Tóm tắt theo topic** — gom correction theo chủ đề (pricing, points/earning,
   setup, integration...), kèm vài ví dụ tiêu biểu + danh sách người sửa.
2. **📋 Chi tiết từng correction** — full `question` / bot trả / CS sửa thành /
   context / session id → đủ để copy thẳng vào KB.

**Retention:** chỉ giữ **10 report gần nhất / app** trong repo (~2 tuần daily) —
sau khi ghi report mới, script tự xoá report cũ hơn (`--keep-weeks`, mặc định `10`,
`0` = giữ hết). Lịch sử xa hơn vẫn tra được qua `git log -- reports/bot-corrections/`
nếu cần.

Sau khi tạo, **commit** vào repo (chỉ khi có report mới).

## Lưu ý xử lý data

- **Tag nguồn ≠ topic:** tags như `ts-elite`, `src:crisp-extension`, `crisp` là kênh
  submit, KHÔNG phải topic nội dung → script bỏ qua, gom topic bằng heuristic từ khóa.
- **Người sửa thật:** khi `created_by` là token (vd `token:Avada CS Team`, submit qua
  TS Elite), người sửa thật nằm trong `context` (`...by <email>`) → script tự parse +
  map email → tên hiển thị qua `_identity/team-g2.md`.

## Triage từng correction — root cause trước, patch/ticket/verify sau

(Đổi 2026-08-21, thay cho pass diff-only-vs-KB cũ.) Sau report, với **mỗi correction**
KHÔNG chỉ diff với KB nữa mà trace lại conversation gốc để tìm root cause thật, rồi
đi đúng 1 trong 3 nhánh — chứ không mặc định coi mọi correction là "KB thiếu".

### 1. Trace conversation gốc

```
python3 skills/bot-corrections/scripts/cs2_session.py <source_session_id>
```
Gọi `GET /api/obs/session/{session_id}` trên `cs2.avada.net` → full conversation +
per-message `trace`/`debug`/`escalation` (populated ở turn agent thật, null ở message
backfill). Đây là cách biết agent làm gì ngay trước khi trả lời sai: retrieve đúng/sai
doc, gọi tool nào, route sai intent, hứa hẹn (handoff) rồi không làm, hay hallucinate
ngoài mọi doc đã retrieve.

### 2. Phân loại — chọn ĐÚNG 1 nhánh

- **(a) Lỗi hệ thống** — KB đã đúng (hoặc câu hỏi không cần KB) nhưng agent vẫn sai:
  tool call lỗi, route sai intent, hứa chuyển việc nhưng không escalate, hallucinate.
  → Tạo ticket cho Fennic:
  ```
  python3 skills/bot-corrections/scripts/create_bug_ticket.py \
    --bug-key <slug ổn định theo root cause> --title "..." --summary "..." \
    --app chatty|joy [--priority normal|high|urgent]
  ```
  `appName` = **"Avada CS Ai"**, member = **Liz + Fennic**. **Dedup**: cùng
  `--bug-key` (đặt tên theo root cause, không theo correction id, để nhiều correction
  cùng nguyên nhân gộp về 1 ticket) → script tự check `state/system-bugs.json`, nếu
  ticket cũ còn mở thì **không tạo ticket mới**, thay vào đó POST comment vào ticket
  cũ (`POST /api/external/tickets/{internal_id}/comments`, endpoint đã confirm — xem
  [[avada_ticket_post_comment_endpoint]]) báo occurrence mới + tăng counter, **không
  tự đổi `tsStatus`** (Liz tự đổi status, xem [[feedback_ticket_progress_comments]]).
  Nếu ticket cũ đã đóng thì coi là regress → tạo ticket mới. Tag `ai-bot-bug` tự áp
  nếu tag đó đã tồn tại trong helpdesk (script không tự tạo tag).

- **(b) Thiếu/sai KB** — KB thiếu/sai đúng điểm CS sửa, đủ giải thích câu trả lời sai.
  → Soạn patch, **giữ nguyên cơ chế cũ** (xem chi tiết bên dưới): OUTDATED/GAP/PARTIAL,
  review-gate, Liz duyệt rồi tự `push_kb.py`.

- **(c) CS sửa sai** — trace ra bot vốn trả lời đúng (hoặc chấp nhận được), correction
  của CS không đúng hơn (hiểu nhầm, khác style, hoặc trái với KB đúng). → **Reject**
  correction đó (KHÔNG phải verify — verify là xác nhận 1 câu trả lời bot đúng, còn đây
  là đánh dấu chính cái correction là sai để nó không bị tính là lỗi bot / không lọt
  vào training data):
  ```
  python3 skills/bot-corrections/scripts/reject_correction.py --id <id> \
    --reason "..." --live
  ```
  ⚠️ Endpoint `PUT /api/corrections/{id}` **chưa confirm 100%** (suy từ field
  `status/verified_by/verified_at` thấy trên row, chưa test PUT thật — giá trị status
  `"rejected"` cũng là suy đoán) — lần chạy đầu Liz nên soi kỹ digest, coi kết quả
  live_ok/live_failed trước khi tin tưởng auto.

**Không chắc (a) hay (b)** → ưu tiên (b), patch KB an toàn hơn dù root cause thật là (a).

Cả (a) và (c) **chạy tự động thẳng, không cần Liz duyệt trước** (Liz chốt
2026-08-21) — digest Telegram cuối chỉ để báo đã làm gì, không phải xin duyệt. Riêng
(b) **vẫn giữ review-gate** như cũ.

### KB patch (nhánh b) — chi tiết không đổi

```
cd ~/CSL/skills/bot-corrections/scripts
python3 prep_kb.py <app>            # cache KB + tìm report mới nhất của app
```
Với mỗi correction rơi vào nhánh (b), tìm file KB liên quan trong cache rồi phân loại:
- **OUTDATED** — KB có nội dung cũ/sai, mâu thuẫn với `corrected_response` → patch.
- **GAP** — KB chưa có nội dung này → thêm section mới.
- **PARTIAL** — KB có một phần, thiếu đúng điểm CS sửa → bổ sung.

(**COVERED** — KB đã đúng rồi mà vẫn bị sửa — giờ không còn là nhánh riêng: trace ở
bước 1 sẽ tự lộ ra đây là (a) lỗi hệ thống hoặc (c) CS sửa sai, chứ không dừng ở
"có thể do reindex stale" như cách cũ nữa. Xem thêm [[joy_reindex_stale_root_cause]]
nếu trace vẫn không rõ nguyên nhân.)

Với mỗi OUTDATED/GAP/PARTIAL, soạn full nội dung file mới theo template chuẩn ở
`~/CSL/skills/kb-sync/SKILL.md` step 3 (case: symptom phrasings + scripted reply +
Step→WAIT + `<escalate reason="..."/>` thật + ❌ Do NOT; faq: Q/A thuần **CHỈ khi
file đang patch thật sự dùng format đó** — check `type:` trong frontmatter file
gốc trước, đa số `kb/faq/*.md` hiện tại (Chatty) thực chất là `type: reference`
viết theo `## Heading`, patch theo đúng format đó chứ đừng tự chèn Q:/A:; reference:
heading tự đủ nghĩa + scripted answer cho phần FAQ-style) — giữ voice/frontmatter
hiện có của file đang patch, viết ĐÚNG 1 ví dụ — KHÔNG viết negative example "đừng
nói X" vì bot có thể copy ra cho khách, xem [[feedback_kb_no_negative_examples]]).
Không dùng format cũ `<!-- CHUNK -->`/```yaml``` — không được parser đọc, chỉ
thành rác trong chunk. Không lặp lại 1 heading string (kể cả `###`) cho 2 tình
huống khác nhau trong cùng file. Gộp nhiều correction cùng 1 file KB thành 1 entry.

**Patch vào `flows/*.md` hay `kb/case`/`kb/faq`/`kb/reference`?** Mặc định case/faq/
reference (Chatty chỉ). Chỉ patch thêm vào `flows/` (Chatty) khi correction liên quan
tới **hành động hệ thống bot phải quyết định** (ticket/escalate/consult_ts) VÀ đã có
sẵn 1 flow khớp chủ đề — thêm vào causes list / "Never create a ticket when" của flow
đó, đừng tự tạo flow mới. Xem [[flow_vs_case_patch_rule]]. Ghi payloads:
```
reports/analysis/bot-corrections-<app>-<YYYY-MM-DD thứ-2>-payloads.json   # {agent,path,content}[]
```
(gitignored, tạm thời — giống payload của `/kb-sync`).

**Review gate:** dừng lại đây, không tự POST `/api/kb/file` hay reindex. Cron báo
Liz qua Telegram: số OUTDATED/GAP/PARTIAL mỗi app + top items + đường dẫn payload.

Sau khi Liz duyệt, push (dùng lại script của `/kb-sync`, cùng format payload):
```
python3 ~/CSL/skills/kb-sync/scripts/push_kb.py <payloads.json>
```
Tự POST từng file (auto git commit bên v2) + reindex agent liên quan.

## Cron

`com.avada.bot-corrections` — **T2-T6 15:00** hàng ngày (đổi từ T5 10:00/tuần
2026-08-18, để bắt lỗi bot sớm hơn và Liz fix KB nhanh hơn). Chạy 2 bước:
1. Script thuần: fetch (window = kể từ lần chạy trước) → ghi report cho app có
   correction mới → git commit (repo CSL). App nào 0 correction thì không ghi/commit.
2. Claude headless (`--dangerously-skip-permissions`, subscription OAuth) — **CHỈ
   chạy nếu bước 1 có ít nhất 1 correction mới**: diff app đó vs KB v2 → soạn payload
   patch → DM Telegram Liz để duyệt. KHÔNG tự push. Ngày không có correction mới:
   im lặng hoàn toàn, không DM.

Source-of-truth: `cron/` (`run-daily.sh` + `prompt-diff.txt`).
Install: `bash skills/bot-corrections/cron/install.sh` (Liz tự chạy trong Terminal).
Log: `/tmp/bot-corrections.log`.
