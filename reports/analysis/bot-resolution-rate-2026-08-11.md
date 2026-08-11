# Bot resolution rate — audit & đổi cách đo (11/08/2026)

> **Kết luận**: công thức cũ `(total − human_active)/total` thổi phồng ~15 điểm và đang
> đi ngược chiều với thực tế. Từ tuần này report **2 chỉ số song song**: `AI resolved`
> (chất lượng bot) và `CS không phải đụng tay` (tải nhân sự).

## 1. Sai ở đâu

Công thức cũ đếm mọi session mà human không nhảy vào chat là "bot tự xử". Bóc tử số ra
(tuần 03–09/08, dữ liệu mức session từ `/api/obs/sessions`):

| | Bị đếm là "bot tự xử" | — đã escalated | — `no_ai` | — bot không reply | Thật sự sạch |
|---|---|---|---|---|---|
| Ivy | 262 | **57** | 6 | 1 | 203 |
| Joyce | 49 | **17** | 0 | 0 | 32 |
| Wendy | 1 | **1** | 1 | 0 | 0 |

**Lỗi 1 — session escalated vẫn tính là resolve.** Bot đã bàn giao, chỉ là CS xử qua
ticket/email nên `human_active` vẫn false. Chiếm 1/3 tử số của Joyce.

**Lỗi 2 — mẫu số lệch dashboard.** Công thức cũ chia cho `total`, API chia cho
`ai_replied` → lệch cả tử lẫn mẫu, không ai đối chiếu được với cs2.

**Lỗi 3 — "human không vào" ≠ "merchant được giúp".** Trong 203 session sạch của Ivy:
100% bot nói câu cuối, **54%** kết thúc bằng câu bỏ ngỏ kiểu *"Still there? Happy to walk
through whenever you're ready 😊"* mà merchant không trả lời, **48%** merchant chỉ nhắn
≤2 tin. Đây là merchant bỏ đi, không phải vấn đề được giải quyết.

## 2. Bằng chứng mạnh nhất: số cũ đi ngược chiều thực tế

| Ivy (Chatty) | AI resolved | CS ko đụng tay | ~~Số cũ~~ | Escalation | Human takeover |
|---|---|---|---|---|---|
| 29/06–05/07 | 47.1% | 57.2% | ~~63.4%~~ | 38.5% | 36.6% |
| 06/07–12/07 | 49.6% | 58.3% | ~~65.5%~~ | 36.4% | 34.5% |
| 13/07–19/07 | 47.5% | 53.9% | ~~62.1%~~ | 40.7% | 37.9% |
| 20/07–26/07 | 41.8% | 49.8% | ~~64.0%~~ | 44.1% | 36.0% |
| 27/07–02/08 | 43.9% | 51.0% | ~~66.1%~~ | 45.2% | 33.9% |
| 03/08–09/08 | 46.3% | 54.3% | ~~68.1%~~ | 35.8% | 31.9% |

Số cũ **tăng đều 63% → 68%** trong khi AI resolved **giảm rồi mới hồi** (47% → 42% → 46%).
Lý do: số cũ tăng chỉ vì human takeover giảm (36.6% → 31.9%) — tức là **CS vào chat ít đi**,
không phải bot giỏi lên. Escalation cùng kỳ vẫn 36–45%. Nếu giữ số cũ, tuần 20–26/07 sẽ
báo cáo "bot tốt lên (64%)" trong khi thực tế escalation vọt lên 44% và AI resolved rơi
xuống đáy 41.8%.

| Joyce (Joy) | AI resolved | CS ko đụng tay | ~~Số cũ~~ | Escalation | Human takeover |
|---|---|---|---|---|---|
| 29/06–05/07 | 10.4% | 16.4% | ~~27.9%~~ | 77.6% | 72.1% |
| 06/07–12/07 | 9.5% | 19.0% | ~~28.7%~~ | 77.4% | 71.3% |
| 13/07–19/07 | 9.6% | 20.5% | ~~32.6%~~ | 68.7% | 67.4% |
| 20/07–26/07 | 11.8% | 18.8% | ~~26.7%~~ | 75.3% | 73.3% |
| 27/07–02/08 | 13.6% | 20.0% | ~~28.2%~~ | 77.3% | 71.8% |
| 03/08–09/08 | 13.3% | 23.7% | ~~34.5%~~ | 71.1% | 65.5% |

**Joyce escalate 68–78% suốt 6 tuần** — đây mới là vấn đề thật, và con số cũ (~30%) đã che mất.

**Wendy (Wishlist)**: 0–12 session/tuần, không đủ mẫu để report %. Chỉ theo dõi số tuyệt đối
cho tới khi volume ổn định.

## 3. Hai chỉ số mới

| | Công thức | Trả lời câu hỏi | Dùng cho |
|---|---|---|---|
| **AI resolved** | `kpi.aiResolvedPct` = `ai_resolved/ai_replied` | Bot xử xong được bao nhiêu? | Chất lượng bot, báo cáo lên trên (khớp dashboard cs2) |
| **CS không phải đụng tay** | (không `human_active`, không `escalated`, không `no_ai`, bot có reply) / `ai_replied` | CS phải nhúng tay bao nhiêu? | Tải nhân sự, quyết định headcount |

Cùng mẫu số `ai_replied` để so trực tiếp. Phần chênh giữa 2 số (Ivy 8.0đ · Joyce 10.4đ) là
**vùng merchant im lặng, không rõ có được giúp không** — khoảng này phình ra nghĩa là bot
nói nhiều mà không chốt được vấn đề. Đáng theo dõi riêng.

⚠️ `CS không phải đụng tay` là **cận trên**, không phải ước lượng đúng: nó vẫn tính session
merchant bỏ đi. Không có metric nào hiện đo được "merchant thật sự hài lòng".

## 4. Chỗ chưa chắc

Mẫu số của `aiResolvedPct` verify được bằng số học (khớp chính xác cả 3 bot), nhưng **quy tắc
đánh dấu một session là `ai_resolved` thì không truy được** — cs2 không có endpoint mô tả
metric, filter param bị server bỏ qua. Bucket tự tính là 203, API ra 173, lệch 30 session
chưa rõ vì sao. Cần hỏi team dev cs2: *"ai_resolved được set khi nào?"*

Lưu ý thêm: số trên dashboard **thay đổi sau khi report chạy** do session backfill (Ivy tuần
03–09/08 lúc đầu 384 session, fetch lại ra 383). Nên chốt snapshot lúc chạy thay vì fetch lại.

## 5. Đã sửa những file nào

- `skills/cs-weekly/scripts/fetch_bot_qa.py` — bỏ `resolveRatePct`, thêm `aiResolvedPct` +
  `takeOnlyPct` + `unclearGapPct`; thêm agent `wishlist`; `get()` có retry vì
  `/api/obs/sessions` phải phân trang
- `skills/cs-weekly/scripts/notify_slack.py` — Slack block hiển thị 2 số + gap, thêm tên Wendy
- `reports/scripts/gen-ceo-weekly.py` — `resolve_rate()` → `bot_rates()`, cập nhật TL;DR
- `skills/cs-weekly/cron/prompt.txt` — **quan trọng**: prompt cron T2 9AM vẫn đang mô tả
  key `resolveRatePct` cũ (đã xoá khỏi script) → nếu không sửa thì cron tuần này gãy
- `skills/cs-weekly/SKILL.md`, `reports/weekly-cs/TEMPLATE.md`,
  `templates/ceo-weekly-template.md`, `CLAUDE.md`, `_identity/responsibilities.md`
- `reports/scripts/gen-ceo-weekly.sh`, `reports/scripts/cron/run-weekly.sh` — docstring
- `playbooks/cs-transformation/{chatty,joy}-transformation.md` +
  `cs-transformation-plan.md` — **trigger Phase 3/4 nói rõ đo bằng `aiResolvedPct`**.
  Với số cũ Ivy 68% trông như đã vượt mốc ≥60% để scale down remote outsource; số đúng
  là 46.3% → **chưa đạt**. Joyce 13.3%, còn rất xa.
- Reports cũ trong `reports/weekly/ceo-weekly-*.md` **giữ nguyên** — là bản ghi lịch sử
  của những gì đã báo cáo, không sửa lại.

**Khi report tuần đầu tiên**: nói rõ một câu là đổi cách đo, kèm số cũ để đối chiếu — tránh
bị đọc thành "bot rớt". Bảng backfill ở §2 dùng luôn cho việc này.
