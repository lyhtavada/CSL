# Joy DFY (Done-for-You) Support Flow — Spec

**Status:** Draft
**Owner:** Liz (G2 CS Leader)
**Created:** 2026-05-18
**Updated:** 2026-05-18

---

## 1. Mục đích

Joy MC trả phí cần setup widget + loyalty page nhanh để đạt time-to-value sớm. Hiện tại MC tự setup → mất nhiều ngày, dễ bỏ cuộc giữa chừng, churn cao trong 30 ngày đầu.

**DFY giải quyết:** CS chủ động audit store (tập trung vào widget và loyalty page để đảm bảo onbrand setup) + viết recommendation cụ thể cho MC → MC chỉ cần apply theo checklist → time-to-value rút ngắn còn vài ngày → giảm churn và tạo cơ hội xin review khi MC đã thấy giá trị.

**Mục tiêu đo lường:**
- Adoption rate ≥ 60% trong 14 ngày
- Avg time từ Crisp inbound → recommendation sent: ≤ 4 giờ
- Reduce 30-day churn của Joy MC trả phí
- Review conversion rate từ MC đã adopted

---

## 2. Scope — Khi nào áp dụng DFY

**Eligibility (đồng thời thỏa cả 2):**
1. MC đang dùng plan **trả phí** (Essential / Advanced / Ultimate của Joy)
2. MC thuộc ít nhất một trong các nhóm store sau:
   - **New install** — cài app trong vòng 30 ngày, chưa kịp setup hoàn chỉnh
   - **Installed but not launched** — cài lâu nhưng loyalty program chưa live (widget ẩn, page chưa accessible, hoặc không có earning program nào active)
   - **Launched but not on-brand** — đã live nhưng widget chưa match theme store (màu, font, wording, icon lạc tông)
3. Message Crisp inbound có intent liên quan **setup / customize / hiển thị** widget hoặc loyalty page — hoặc CS chủ động phát hiện store thuộc nhóm trên khi xử lý case khác

**Keyword reference (CS dùng để self-check intent của Crisp message):**

| Tiếng Anh | Tiếng Việt |
|---|---|
| setup, set up, install, configure | cài đặt, setup, cấu hình |
| widget, popup, launcher, button | widget, nút, popup |
| loyalty page, rewards page, landing page | trang loyalty, trang thưởng |
| customize, design, layout, theme, color | tùy chỉnh, thiết kế, màu, layout |
| not showing, not displayed, can't see, hidden | không hiện, không thấy, ẩn |
| how to, can you help me, guide me | làm sao, hướng dẫn, giúp với |

> CS đánh giá Crisp message → nếu match intent + plan trả phí → tự tạo ticket trong section "Done for You". Keyword list có thể mở rộng dựa trên data thực tế.

**KHÔNG tạo ticket DFY trong các trường hợp:**
- MC dùng Free plan → vào support flow thông thường
- Message chỉ hỏi billing, refund, technical bug → vào flow tương ứng
- MC đã có ticket DFY active (status ≠ Adopted/No Adoption) → CS update ticket cũ thay vì tạo mới

---

## 3. Ticket lifecycle

### 3.1 Status

| # | Status | Khi nào | Owner | SLA chuyển status |
|---|---|---|---|---|
| 1 | **New** | CS vừa tạo ticket (sau khi đánh giá store eligible) | CS tự tạo + assign | ≤ 30 phút từ lúc nhận Crisp |
| 2 | **Recommendation Sent** | Đã gửi rcm cho MC qua Crisp/email | CS | ≤ 4 giờ từ New |
| 3 | **Following Up** | Đã FU ít nhất 1 lần | CS | Theo FU schedule (§4) |
| 4 | **Adopted** ✅ | MC apply ≥ 80% recommendation | (close) | — |
| 5 | **Partially Adopted** 🔶 | MC apply 50–79% recommendation | (close, log lý do chưa đủ) | — |
| 6 | **No Adoption** ❌ | Hết FU window, MC không apply hoặc không response | (close, log lý do) | — |

### 3.2 Sub-tag (optional, dùng cho phân tích)

- `No Response` — MC không reply suốt FU window
- `Declined` — MC reply nhưng từ chối apply
- `Blocked` — MC muốn apply nhưng gặp issue (bug, plan limit, theme conflict,…)

### 3.3 Transition rules

```
New → Recommendation Sent     (CS audit xong + gửi rcm)
Recommendation Sent → Following Up   (sau FU1)
Following Up → Adopted             (MC apply ≥80%)
Following Up → Partially Adopted   (MC apply 50-79% sau FU window)
Following Up → No Adoption         (sau FU3 vẫn ko adopt)
Any → No Adoption                  (MC explicit decline)
```

---

## 4. Follow-up schedule

CS tự quản lý FU, không bot remind. Khuyến nghị CS dùng calendar/reminder trong ticket tool để track.

| FU | Timing (từ Recommendations Sent) | Mục đích | Action CS |
|---|---|---|---|
| **FU1** | Sau **48 giờ** | Check MC đã đọc + bắt đầu apply chưa | Hỏi: "Anh/chị đã thử áp dụng các gợi ý chưa? Có vướng gì không?" |
| **FU2** | Sau **5 ngày** (nếu FU1 ko response hoặc chưa adopt) | Hỗ trợ block | Hỏi cụ thể block là gì → offer screen share / call |
| **FU3 / Close** | Sau **10-14 ngày** | Quyết định close | Nếu adopted → close `Adopted`. Nếu không → close `No Adoption` + log lý do |

**Quy tắc bonus:**
- Nếu MC reply tích cực ở FU1 → CS có thể skip FU2 và đợi đến FU3 để check final
- Nếu MC adopt giữa chừng (vd ngày 3) → CS close `Adopted` ngay, không cần đợi đủ window
- Nếu MC explicit nói "không cần nữa" → close `No Adoption` ngay với sub-tag `Declined`

---

## 5. Default checklist (CS audit + recommendation)

Ticket auto-generate kèm checklist này. CS tick + viết note cho từng item.

### 5.1 Widget audit — Màu sắc & branding

- [ ] Màu primary đã match store chưa? (Joy tự detect — mở store picker, chọn từ brand colors)
- [ ] Background color match dark/light theme của store không? (chỉnh sau khi set primary)
- [ ] Button color + text color có ăn theo primary không, hay lệch tông?
- [ ] Logo trên widget header đã thay chưa? (dùng ảnh transparent, bỏ chữ nếu có logo)
- [ ] Ảnh header có contrast tốt với text không? (nếu không → bật overlay opacity)
- [ ] Currency icon đã custom chưa? (dùng emoji hoặc upload icon riêng để brand hóa)
- [ ] Guest card / Member card image đã thay chưa? (nếu có VIP tier: ảnh + icon từng tier)

### 5.2 Widget audit — Layout & content

- [ ] Layout chọn Drawer hay Widget popup? (recommend Drawer — rộng hơn, UX tốt hơn)
- [ ] Nếu dùng Drawer: deep link đã setup chưa? (mở widget từ account page / header / menu)
- [ ] On-brand language đã bật chưa? (đổi "earn/redeem/complete" → wording phù hợp brand voice)
- [ ] Program description + detailed description đã viết chưa? (dùng AI trong app để gen, rồi review + chỉnh)
- [ ] Footer menu style có match store không? (clean store → label only; phức tạp → có icon)
- [ ] Các block không cần thiết đã ẩn chưa? (referral, marketing opt-in, v.v.)
- [ ] Login with Shop đã bật chưa? (recommended — sau login tự mở lại đúng trang widget)

### 5.3 Widget audit — Earning & Redeem blocks

- [ ] Earning block: số programs hiển thị có hợp lý không? (default 5 — không nên show tất cả)
- [ ] Thứ tự programs đã sort hợp lý chưa? (program quan trọng nhất lên đầu)
- [ ] Icon của từng earning program đã custom chưa? (có thể dùng ảnh lớn làm banner khi click vào)
- [ ] Redeem block: layout đã chọn phù hợp với style store chưa?

### 5.4 Setup health

- [ ] Earning programs đang active ≥ 3 (Place order, Sign up, Birthday, Social share, Review,…)
- [ ] Redeeming options ≥ 2 và có ít nhất 1 option entry-level (vd 100 pts = $5)
- [ ] Email notifications đã enabled (welcome, points earned, reward redeemed)
- [ ] Integration phù hợp đã bật (Klaviyo / Chatty / POS / Judge.me) — nếu plan support
- [ ] Wishlist extension đã recommend cho MC chưa? (nếu plan support)

### 5.5 Output format — Recommendation message

CS dùng template (§6.2) để soạn message gửi MC. Mỗi recommendation cần:
- **What** — rcm cụ thể là gì (vd: "Đổi màu widget từ #FF0000 sang #4CAF50")
- **Why** — lý do (vd: "Để match brand color của theme và tăng visibility")
- **How** — hướng dẫn ngắn hoặc link helpcenter

---

## 6. Templates

> ⚠️ Tất cả merchant-facing message phải bằng **tiếng Anh**. CS không dùng tiếng Việt trong reply cho MC, kể cả khi MC nhắn tiếng Việt.

### 6.1 Initial recommendation message (after audit)

```
Hi [MC name],

Thanks for reaching out to Joy! I just took a look at your store 
[store-url] and have a few recommendations to make your loyalty 
program more effective:

**Widget:**
1. [Recommendation 1 — What + Why]
   → How: [Steps or helpcenter link]

2. [Recommendation 2]
   → How: [...]

**Loyalty page:**
3. [Recommendation 3]
   → How: [...]

**Setup:**
4. [Recommendation 4]
   → How: [...]

Feel free to give these a try — I'll check back in a day or two 
to see how it's going. If you run into anything, just reply here 
and I'll jump in to help right away!

Best,
[CS name]
```

### 6.2 FU1 (after 48h)

```
Hi [MC name],

Just checking back in after a couple of days — have you had a 
chance to try out the recommendations? Let me know if anything 
is unclear or if you hit any roadblocks, happy to help!
```

### 6.3 FU2 (after 5 days — if MC hasn't adopted)

```
Hi [MC name],

I noticed your store hasn't changed much since my last message — 
is there anything blocking you from applying the recommendations?

If it would help, I can set up a quick 15-minute call to walk 
you through it, or I can handle some of the setup for you 
directly. Just let me know which option works better for you!
```

### 6.4 Close — Adopted

```
Hi [MC name],

I checked your store again and noticed you've applied most of 
the recommendations — your loyalty program is looking great! 🎉

I'll close this case for now. If you'd like to fine-tune things 
further down the road, just ping the Joy team anytime and we'll 
be here to help!
```

### 6.5 Close — No Adoption

```
Hi [MC name],

I'm going to close this case for now since I haven't seen any 
changes over the past couple of weeks. If you decide to optimize 
your loyalty program later, just reply here or message the Joy 
team — I'd be happy to pick this back up anytime!
```

---

## 7. Quản lý ticket DFY

DFY tickets được quản lý trong **Avada Ticket** (tool nội bộ tự build), trong một **section riêng** tên **"Done for You"**. CS tự tạo ticket sau khi đánh giá Crisp message eligible — không có bot auto-tạo.

**Spec UI chi tiết (sidebar, status tabs, ticket card, detail panel, New Ticket form, dashboard, dependencies cho dev team) tách riêng trong:** [`joy-dfy-ticket-ui.md`](./joy-dfy-ticket-ui.md)

Tóm tắt:
- Section mới "Done for You" trong sidebar, đặt giữa "Tickets Management" và "Follow Up"
- 6 status tabs riêng (theo §3.1) thay cho status chung của Tickets view
- Detail panel có default checklist (§5), recommendation editor, FU history timeline, FU reminder date picker, close actions
- "+ New Ticket" form cần CS verify eligibility (checkbox required)

---

## 8. Metrics to track

| Metric | Target | Frequency |
|---|---|---|
| Tickets DFY created | (baseline tuần đầu) | Weekly |
| Avg time New → Recommendations Sent | ≤ 4 giờ | Weekly |
| Adoption rate (Adopted / Total closed) | ≥ 60% | Weekly |
| Partial adoption rate | (baseline) | Monthly |
| Top decline reasons | — | Monthly |
| 30-day churn của MC qua DFY vs không qua DFY | DFY churn < non-DFY | Monthly |

Tracking sources:
- Ticket tool — export hàng tuần
- Crisp conversation — link trong ticket
- Joy admin — check adoption (widget config, page content, programs active)

---

## 9. Roles & responsibilities

| Role | Responsibility |
|---|---|
| **CS (Joy team)** | Đánh giá Crisp message → tự tạo ticket DFY trong Avada Ticket nếu eligible. Audit store, viết rcm, gửi MC, FU, close ticket với đúng status + sub-tag |
| **Liz (CSL)** | Review weekly metrics, training CS team về eligibility check + checklist, update template, escalation cho case khó |
| **Dev team** | Build section "Done for You" trong Avada Ticket UI theo spec [`joy-dfy-ticket-ui.md`](./joy-dfy-ticket-ui.md), integrate Crisp link |

---

## 10. Cần làm tiếp

| # | Item | Owner |
|---|---|---|
| 1 | Brief dev team về spec UI section "Done for You" ([`joy-dfy-ticket-ui.md`](./joy-dfy-ticket-ui.md)) | Liz |
| 2 | Build section "Done for You" trong Avada Ticket (sidebar item, 6 status tabs, detail panel, New Ticket form) | Dev |
| 3 | Training Joy CS team về eligibility check + DFY flow + checklist + template | Liz |
| 4 | Tạo dashboard / KPI widget track metrics (§8) | Liz / Data team |
| 5 | Pilot 2 tuần với 1-2 CS → iterate trước khi rollout toàn team | Liz |
| 6 | Update Joy ICP doc (`kb/icp-joy.md`) sau khi có data DFY thực tế | Liz |
