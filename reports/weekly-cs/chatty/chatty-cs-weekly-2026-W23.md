# Chatty CS Weekly — 2026-W23
**Period:** 01/06 – 07/06/2026 (Thứ 2 → Chủ nhật tuần trước) · **Prepared by:** Betty (review: Liz)

> _Bản tin tuần cho team CS Chatty. Đọc 2 phút để nắm tình hình + cập nhật cần biết khi support merchant._

---

## ⚡ TL;DR
Tuần này Chatty nhận **261 chats** và **91 tickets** — volume ổn định. Điểm nóng nhất vẫn là **merchant cần hỗ trợ setup AI agent** (chiếm phần lớn chat). Có **1 bug đáng chú ý: phản hồi/note bị gán nhầm conversation** — nhiều merchant report, cần nắm để trấn an + báo dev. Release mới: **AI Human Handover redesign** (đã có auto-trigger). App Store: **11 review, 4.9★** — rất tốt, có 1 review 4★ ngày 02/06 nên check xem merchant góp ý gì.

---

## 📊 Tình hình support tuần qua

| Chỉ số | Tuần này | Tuần trước | |
|---|---|---|---|
| Tickets created (API) | 91 | _(điền)_ | — |
| Chats (BigQuery) | 261 | _(điền)_ | — |
| DFY created | 0 | 0 | — |
| Reviews (App Store) | 11 (4.9★) | _(điền)_ | — |

_Nguồn: Ticket API · `avada_cs.crisp_chats` (segments app_chatty + app_faqs) · Shopify App Store reviews. Period 01–07/06. Tuần đầu chạy nên chưa có baseline tuần trước — từ tuần sau sẽ auto so sánh ▲▼._

---

## 🔥 Top issues tuần này

_Chủ đề merchant hỏi/than nhiều nhất — đọc để trả lời nhanh & đúng._

1. **Setup AI agent** — nhiều nhất trong tuần
   → _Cách xử lý:_ Dẫn merchant qua flow AI agent → Instruction → train data. Link helpcenter AI setup. Nếu cần extend limit → quy trình `handle-extend-limit`.

2. **Customization widget** (màu/icon/vị trí, ẩn trên trang nhất định, mở tab mới)
   → _Cách xử lý:_ Hướng dẫn trong Appearance settings; ẩn theo URL → page targeting. Đa số self-serve được.

3. **AI trả lời sai / không như ý** (gợi ý sai, để giá sai, không nên offer help với order)
   → _Cách xử lý:_ Check training data + instruction của shop. Hướng dẫn dùng intent rules / brand voice để chỉnh tone & phạm vi trả lời.

4. **Bug: phản hồi & note gán nhầm conversation** ⚠️
   → _Cách xử lý:_ Nhiều merchant report "manually responding goes to wrong conversation" + note/star nhảy sai chat. Trấn an, thu thập screenshot + shop domain, escalate dev ngay (xem mục Known bugs).

5. **Integration** (TikTok shop, WhatsApp sync đổi số, email assign vào account đã xóa)
   → _Cách xử lý:_ Confirm scope tích hợp hiện có; WhatsApp/email lỗi → thu info escalate dev.

---

## 🆕 Cập nhật sản phẩm & policy

_Release trong tuần (quét #product-release)._

- **[Improvement] AI Assistant – Human Handover redesign** (04/06) — Tách rõ "khi nào transfer" và "transfer đi đâu"; **thêm auto-trigger**: AI tự chuyển human khi khách bực, yêu cầu, hoặc AI không trả lời được. Vị trí: AI agent → Instruction → Assistant skill → Human handover.
  → Khi merchant hỏi "sao AI không tự chuyển cho người thật" → giờ đã có, hướng dẫn bật auto-trigger.
  → [Chi tiết release](https://avadaio.slack.com/archives/C07RNAY9ZC6/p1780567231031189?thread_ts=1780567231.031189&cid=C07RNAY9ZC6)

**🐞 Known bugs đang mở:**
- **Phản hồi/note gán nhầm conversation** — nhiều merchant report tuần này. Workaround tạm: refresh inbox, double-check đúng chat trước khi gửi. Trạng thái: _cần Liz xác nhận đã báo dev chưa._

---

## 💡 Coaching & lưu ý tuần này
_(Liz review/bổ sung)_

- **Lỗi hay gặp:** _(Liz điền từ QA tuần này)_
- **Reminder quy trình:** Khi merchant report bug đồng loạt (như bug gán nhầm conversation) → đừng xử lý lẻ tẻ, gom screenshot + domain, escalate 1 lần, báo team để trả lời nhất quán.

---

## 🌟 Ghi nhận & tinh thần

- 🙌 **Shoutout:** _(Liz điền — CS xử lý tốt / CSAT cao tuần này)_
- ✅ **Win tuần này:** App Store 11 review mới, 4.9★ (10 cái 5 sao, 1 cái 4 sao).
- 🎯 **Focus tuần tới:** _(Liz điền)_

---
_Generated 10/06/2026 · bản mẫu đầu tiên · góp ý gửi Liz._
