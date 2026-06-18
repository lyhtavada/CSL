_(Title của Notion sub-page đã chứa app + tuần + date range → KHÔNG lặp lại H1/Period ở đầu body. Bắt đầu thẳng từ TL;DR.)_

## ⚡ TL;DR
{2-3 câu tóm tắt tuần: volume, điểm nóng nhất, 1 thứ cần lưu ý.}

---

## 🤖 Bot QA tuần này ({Ivy nếu Chatty / Joyce nếu Joy})

_Tỉ lệ reply của bot được human CS vào verify / correct. Nguồn: dashboard chỉ số vận hành `cs2.avada.net` (`/api/obs/metrics`), range = tuần report (Mon→Sun)._

| Chỉ số | Tuần này | Tuần trước | |
|---|---|---|---|
| Verify coverage | {COV}% ({V_WEEK}/{REPLY} reply) | {N-1}% | {▲▼} |
| Correction rate | {CORR}% ({C_WEEK}/{REPLY} reply) | {N-1}% | {▲▼} |
| Verify đúng | {OK}% | {N-1}% | {▲▼} |

🏆 **Top verify tuần này:** {Tên (n) · Tên (n) · Tên (n)}
🔧 **Top correction tuần này:** {Tên (n) · Tên (n) · Tên (n)}

{Nếu verify coverage < 15% → thêm dòng: ⚠️ **Verify coverage thấp** — nhắc team vào verify reply bot nhiều hơn để keep track chất lượng.}
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
