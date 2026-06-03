# Chatty DFY — CS Flow & Checklist

**Owner:** Liz (CS Leader)
**Created:** 2026-05-27

---

## 1. Scope — Khi nào áp dụng DFY

**Eligibility (thỏa ít nhất 1 trong các nhóm):**
- **New install** — cài app trong vòng 30 ngày, chưa setup gì
- **Installed but inactive** — cài lâu nhưng widget vẫn default (chưa đổi màu, chưa có FAQ, AI chưa train)
- **Active but not on-brand** — đang dùng nhưng widget chưa match theme store

**KHÔNG tạo ticket DFY nếu:**
- MC đã có ticket DFY active (chưa close) → update ticket cũ thay vì tạo mới

---

## 2. Modules

CS offer 3 module độc lập. MC có thể nhận 1, 2 hoặc cả 3 tùy nhu cầu.

| Module | Nội dung | Ai làm |
|--------|----------|--------|
| **M1 — Chatbox** | Widget branding + proactive chat (product recommendation) | CS setup → KH duyệt |
| **M2 — FAQ** | Add FAQ từ file sẵn + FAQ page | CS setup → KH duyệt |
| **M3 — AI** | AI brand settings + human handover + sync URLs | CS setup với input từ KH |

**Thứ tự ưu tiên nếu làm cả 3:** M1 → M2 → M3
> M1 cho KH thấy kết quả ngay. M3 cần input từ KH nhiều nhất nên để cuối.

---

## 3. CS Flow

CS chủ động offer khi phát hiện store eligible, dùng shortcut `!chatty-dfy-offer`.

**Bước thực hiện:**

1. CS phát hiện store eligible (qua inbound chat hoặc proactive check) → tạo ticket DFY → set label `DFY-new`
2. CS audit store — xem widget hiện tại, FAQ có chưa, AI đã train chưa → chọn module phù hợp

   **Template offer M1 (gửi KH):**
   > Hey, I took a look at your store and noticed your Chatty widget is still on the default setup, so I'd love to offer you something.
   >
   > We have a **chatbox customization service** (completely free) where I personally set it up to fit your store: your colors, your logo, your tone. It's built specifically around how your store looks and what your customers need, not a generic template.
   >
   > If you're interested? Please let me know and I'll get started. No setup needed on your end, and you can still adjust anything you want.
   
3. **M1 và M2:** CS tự setup → preview → quay video ngắn kết quả → gửi KH duyệt trước khi live
4. **M3:** CS gửi KH **pre-session checklist** (xem §4) để collect input → setup sau khi có đủ info
5. Sau khi KH duyệt → activate → update label `DFY-in-progress` → gửi KH confirm live
6. Done → gắn label module đã hoàn thành (`DFY-M1` / `DFY-M2` / `DFY-M3`) → nếu convert được review: gắn thêm `review-yes` → **không close ngay**, để mở chờ follow-up
7. **Follow-up sau 2–5 ngày** → check store:
   - **Có adopt** → gắn `DFY-adopted` → close ticket
   - **Không phản hồi / chưa adopt** → gửi reminder (template `!dfy-remind`) → gắn `DFY-no-adopt` → close ticket

> SLA: Có kết quả và báo KH trong vòng **48H** sau khi tạo ticket. Quá 48H không update → escalate Liz.

> **Tính point:** Follow-up đúng hạn + gắn đủ tag là điều kiện bắt buộc để ticket được tính.

---

## 4. Pre-session checklist — Module AI

Gửi KH trước khi setup M3 để tránh bị kẹt giữa session:

- Brand tone/voice muốn AI dùng (formal, friendly, v.v.)
- Sản phẩm chính của store (top 3–5 nếu có)
- URLs cố định muốn AI đọc (helpcenter, policy page, FAQ page…)
- Kịch bản handover: khi nào AI nên chuyển sang người (ví dụ: order issue, refund, complaint)
- Giờ làm việc của team (để AI thông báo đúng khi offline)

---

## 5. Checklist theo module

### M1 — Chatbox + Proactive Chat

*Chatbox*
- [ ] Background color match brand primary color
- [ ] Custom launcher icon (nếu brand có icon riêng)
- [ ] Logo đã upload
- [ ] Heading text viết lại theo brand tone
- [ ] Description text viết lại theo brand tone
- [ ] Order tracking bật/tắt phù hợp (chỉ bật nếu store dùng tracking)
- [ ] FAQs block — chọn featured questions phù hợp
- [ ] Contact info đúng
- [ ] Primary color match brand

*Proactive Chat — Product Recommendation*
- [ ] Message text viết lại theo brand tone
- [ ] Product logic phù hợp (default: Best sellers — hỏi KH nếu muốn khác)
- [ ] Trigger: All product pages (hỏi KH nếu muốn specific pages)
- [ ] Background color + text color match brand
- [ ] Campaign ở trạng thái **draft** — gửi KH duyệt trước khi activate

---

### M2 — FAQ

*(checklist bổ sung sau)*

---

### M3 — AI

*(checklist bổ sung sau)*

---
