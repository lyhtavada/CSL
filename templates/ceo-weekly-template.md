📊 CS Group 2 (Retention) — Weekly W{n} (dd/mm–dd/mm/yyyy)

**Date**: [DD/MM/YYYY] | **Meeting**: Thứ 2, 15:00 | **Prepared by**: Liz
**Gửi trước**: 13:00 cùng ngày (trước meeting 2 tiếng)
**Nguồn**: tổng hợp 2 bản CS Weekly (Chatty + Joy) trên Notion + dashboard `cs2.avada.net /api/obs/metrics`

> CEO Weekly = bản gửi anh Sam (gộp từ 2 bản CS Weekly team-facing). Khớp generator `reports/scripts/gen-ceo-weekly.py` (chạy qua `gen-ceo-weekly.sh`).
> Auto-fill: TL;DR (tóm tắt toàn bộ report bên dưới), Volume (tickets từ Notion, chats fetch live qua `fetch_chats_week.py` — CÙNG cách đếm `chat_count()` mà `/cs-weekly` dùng, không parse text Notion nữa), Bot performance (AI resolved + CS không phải đụng tay), DFY (ticket/adopt%/review%/install% — fetch live qua `fetch_dfy_week.py`, cùng tuần Mon-Sun với report), Top Issues.
> Liz điền tay: Response time, Crisis (nếu có bad review ≤3★), CEO decision.

---

## ⚡ TL;DR
Tóm tắt tuần:
- **Chatty**: X tickets (▲/▼Y%), Z chats, AI resolved X% (CS không đụng tay Z%), DFY adopt X%.
- **Joy**: X tickets (▲/▼Y%), Z chats, AI resolved X% (CS không đụng tay Z%), DFY adopt X%.
- Crisis: không có bad review (≤3★) tuần này ở cả 2 app.

---

## 📦 Volume
- **Chatty**: X tickets (▲/▼Y%), Z chats, N reviews (0 review xấu). Response time (avg): _(điền)_
- **Joy**: X tickets (▲/▼Y%), Z chats, N reviews (0 review xấu). Response time (avg): _(điền)_

---

## 🤖 Bot performance
- **Ivy (Chatty)**: AI resolved **X%** (tuần trước Y%) · CS không phải đụng tay **Z%** (tuần trước W%), N session.
- **Joyce (Joy)**: AI resolved **X%** (tuần trước Y%) · CS không phải đụng tay **Z%** (tuần trước W%), N session.

> AI resolved = bot xử xong (số khớp dashboard cs2) → chất lượng bot. CS không phải đụng tay = session bot chạy trọn, không escalate → tải nhân sự. Chênh giữa 2 số = merchant im lặng, chưa rõ kết quả.

---

## 🛠️ DFY (tuần dd/mm–dd/mm/yyyy)
- **Chatty**: N ticket, adopt **X%** (a/N), review **Y%**, DFY/install **Z%** (N/install tuần này).
- **Joy**: N ticket, adopt **X%** (a/N), review **Y%**, DFY/install **Z%** (N/install tuần này).

---

## 🔥 Top Issues tuần này
**Chatty**: [chủ đề 1] · [chủ đề 2] · [chủ đề 3] · …

**Joy**: [chủ đề 1] · [chủ đề 2] · [chủ đề 3] · …

---

## 🚨 Crisis (Bad Reviews)
Tuần này không có bad review (≤3★) ở cả 2 app.

<!-- Khi có bad review, thêm dòng:
- **[App]** X bad review (N★): "trích nội dung" → đã xử lý / đang follow up.
-->

---

## 🚀 Team Project đang triển khai
1. Tiếp tục chạy & review Chatty + Joy DFY.
2. Team member verify/correct bot replies → loop training (push verify coverage lên mục tiêu >50%).

---

## 🧠 CEO Cần Quyết Định *(tối đa 3, Liz điền nếu có)*

**1. [Câu hỏi]**
- Context: [1 câu]
- Default nếu không decide: [X]

**2. [Câu hỏi]** *(nếu có)*
- Context: ...
- Default: ...

**3. [Câu hỏi]** *(nếu có)*
- Context: ...
- Default: ...
