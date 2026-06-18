_(Title của Notion sub-page đã chứa app + tuần + date range → KHÔNG lặp lại H1/Period ở đầu body. Bắt đầu thẳng từ TL;DR.)_

## ⚡ TL;DR
{2-3 câu tóm tắt tuần: volume, điểm nóng nhất, 1 thứ cần lưu ý.}

---

## 🤖 Bot performance tuần này ({Ivy nếu Chatty / Joyce nếu Joy})

_Nguồn: dashboard chỉ số vận hành `cs2.avada.net` (`/api/obs/metrics`) + reviews/corrections, range = tuần report (Mon→Sun), compare tuần trước._

**Handle (vận hành)**

| Chỉ số | Tuần này | Tuần trước | |
|---|---|---|---|
| Bot resolve rate | {RESOLVE}% | {N-1}% | {▲▼} |
| AI reply coverage | {AICOV}% | {N-1}% | {▲▼} |
| Human takeover | {TAKEOVER}% | {N-1}% | {▲▼} |
| Escalation rate | {ESCAL}% | {N-1}% | {▲▼} |

_Resolve rate = % session bot tự xử, human KHÔNG nhảy vào = (total − human_active)/total. Volume: {INBOUND} tin vào · {REPLY} reply bot._

**QA (chất lượng — human CS verify / correct)**

| Chỉ số | Tuần này | Tuần trước | |
|---|---|---|---|
| Verify coverage | {COV}% ({V_WEEK}/{REPLY} reply) | {N-1}% | {▲▼} |
| Correction rate | {CORR}% ({C_WEEK}/{REPLY} reply) | {N-1}% | {▲▼} |

🏆 **Top verify tuần này:** {Tên (n) · Tên (n) · Tên (n)}
🔧 **Top correction tuần này:** {Tên (n) · Tên (n) · Tên (n)}

{Nếu verify coverage < 30% → thêm dòng: ⚠️ **Verify coverage thấp** — nhắc team vào verify reply bot nhiều hơn để keep track chất lượng.}
{Nếu tuần không có lượt verify nào → Top verify ghi _(chưa có lượt nào tuần này)_.}

---

## 📊 Tình hình support tuần qua

| Chỉ số | Tuần này | Tuần trước | |
|---|---|---|---|
| Tickets created (API) | {N} | {N-1} | {▲▼ %} |
| Chats (BigQuery) | {N} | {N-1} | {▲▼ %} |
| DFY created | {N} | {N-1} | {▲▼ %} |
| Reviews (App Store) | {N} ({avg}★) | {N-1} ({avg}★) | {▲▼} |

_Nguồn: Ticket API · `avada_cs.crisp_chats` · DFY ticket tags · Shopify App Store reviews (sort_by=newest). Period {START}–{END} vs tuần trước {PREV_START}–{PREV_END}._
{Nếu có review ≤3★ trong tuần → thêm dòng: ⚠️ **Review cần lưu ý:** {ngày} {rating}★ — nên đọc xem merchant góp ý gì. [Thread bad-review]({SLACK_PERMALINK G019ZF7GM7H}) — nếu không thấy trong feed thì ghi _(không thấy trong feed bad-review)_.}
{Chatty chưa có DFY program → DFY created = 0 là bình thường, không phải sụt.}

---

## 🔥 Top issues tuần này

_Chủ đề ticket nhiều nhất tuần qua (cluster từ **ticket** — Ticket API, đã loại [dfy]). Đọc để nắm bug nóng & trả lời nhanh. Sắp theo độ phổ biến._

1. **{Issue}** — {nhiều nhất / phổ biến / lác đác}
   → _Cách xử lý:_ {1 dòng / link KB}
2. **{Issue}** — {…}
   → _Cách xử lý:_ {1 dòng / link KB}
3. **{Issue}** — {…}
   → _Cách xử lý:_ {1 dòng / link KB}

_(Cluster theo độ phổ biến của ticket, đã loại [dfy] — không phải con số tuyệt đối. Prefix [bug] trong subject = bug report → flag nếu lặp lại.)_

---

## 🆕 Cập nhật sản phẩm & policy

_Release / thay đổi trong tuần (quét #product-release `C07RNAY9ZC6`). Đọc để không trả lời sai._

- **{Feature/Improvement}** — {1 dòng merchant-facing: là gì, ảnh hưởng support thế nào}
  → [Chi tiết release]({SLACK_PERMALINK})

**🐞 Known bugs đang mở:**
- **{Bug}** — workaround tạm: {…} · trạng thái: {đang fix / đã báo dev}

_(Không có release/bug mới → ẩn mục này)_

---

## 🛠 TS Elite usage tuần này (team G2)

_Agent investigate (`agent.avada-ts.site`) — team dùng để tra case. Mỗi chat = 1 lượt hỏi agent. Nguồn: `/api/v1/chats`, range = tuần report, compare tuần trước._

**{TOTAL} lượt hỏi · {ACTIVE}/{MEMBERS} CS dùng** ({▲▼ vs tuần trước {PREV_TOTAL}})

| CS | Lượt |
|---|---|
| {Tên (nick)} | {N} |
| {Tên (nick)} | {N} |
| {Tên (nick)} | {N} |
| {Tên (nick)} | {N} |
| {Tên (nick)} | {N} |

{Nếu có CS G2 chưa dùng lần nào → ⚠️ **Chưa dùng tuần này:** {tên, tên, …} — nhắc onboard tool.}

**💬 Hay được hỏi nhất:** (cluster từ câu mở đầu các chat)
1. {Chủ đề / dạng câu hỏi} — {nhiều / phổ biến}
2. {Chủ đề}
3. {Chủ đề}

_(Top 5 người dùng nhiều nhất. "Hay được hỏi" = gộp title chat thành chủ đề, bỏ URL trần. Nếu cả team chưa đụng tool → ẩn mục này.)_

---

## 💡 Coaching & lưu ý tuần này
_(Liz review/bổ sung)_

- **Lỗi hay gặp:** {1-2 lỗi từ QA/chat review} → cách làm đúng
- **Reminder quy trình:** {escalation / refund / extend-limit…}

---

## 🌟 Ghi nhận & tinh thần

- 🙌 **Shoutout:** {tên CS — vì sao}
- ✅ **Win tuần này:** {…}
- 🎯 **Focus tuần tới:** {1 câu}

---
_Generated {GEN_DATE} · `/cs-weekly` · góp ý gửi Liz._
