# Handle: Merchant không nhớ đã upgrade lên paid plan

**Áp dụng cho:** CS Chatty & Joy
**Trigger:** Merchant hỏi tại sao đang ở paid plan / bị charge, nói không nhớ hoặc không bao giờ upgrade

---

## Nguyên tắc

Không phủ nhận merchant, không nhận lỗi khi chưa có bằng chứng. Mục tiêu là giúp họ nhớ lại một cách tự nhiên, không có vẻ đang đổ lỗi ngược.

**Về bản chất:** phía app hoàn toàn không có quyền và không thể tự upgrade plan của merchant — mọi thay đổi plan đều yêu cầu admin của store xác nhận thủ công. Đây là điểm quan trọng cần làm rõ ngay trong chat để tránh merchant hiểu nhầm và leo thang không cần thiết.

---

## Bước 1 — Xác nhận và hứa check

> "Thank you for reaching out! I totally understand the confusion. Let me pull up your account details right now to see exactly what happened."

→ Check: upgrade từ lúc nào, qua account nào, có trial trước đó không.

---

## Bước 2 — Phản hồi sau khi có data

> "I can see the plan was upgraded on [date] from the account [email/admin account]. Upgrades on our end require manual confirmation from a store admin — it can't happen automatically or without someone approving it on your side.
>
> It's also possible you may have started a free trial earlier and forgotten to cancel before it ended — that would automatically switch the plan to paid. Could you check if that might be the case, or whether someone on your team may have approved the upgrade?"

---

## Bước 3 — Nếu merchant vẫn khăng khăng không ai làm

> "I completely understand. Just to clarify — our system only allows store admins to approve plan changes, so it wouldn't have been changed without action from your side. That said, I want to make sure everything is sorted for you.
>
> If you'd like to avoid any further charges, I'd recommend downgrading your plan first. I can help you do that right now — just let me know and I'll walk you through it."

---

## Bước 4 — Nếu merchant yêu cầu refund hoặc còn thắc mắc

> "I've noted down your concern and will raise a ticket to our billing team to look into this further. They'll review your account history and get back to you as soon as possible."

→ Tạo ticket cho billing team, ghi rõ: tên store, ngày upgrade, account thực hiện, nội dung merchant phản ánh.

---

## Những điều KHÔNG làm

- Không nói thẳng "bạn đã upgrade" ngay từ đầu — nghe như đang buộc tội
- Không nói "đây không phải lỗi của chúng tôi" — dễ leo thang
- Không refund ngay khi chưa clarify
- Không để case lửng không có next step

---

## Khi nào escalate lên CS Leader

- Merchant đã check với team, khẳng định không ai upgrade, yêu cầu refund
- Merchant angry hoặc dọa report/review
- Bị charge nhiều tháng, số tiền lớn

---

*Cập nhật: 2026-04-24*
*Liên quan: [handle-billing-refund.md](handle-billing-refund.md) · [escalation-matrix.md](escalation-matrix.md)*
