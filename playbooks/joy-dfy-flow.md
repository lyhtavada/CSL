# Joy DFY — CS Flow & Checklist

**Owner:** Liz (CS Leader)
**Created:** 2026-05-18
**Updated:** 2026-05-25

> Xem mục đích & tinh thần DFY: [`joy-dfy-intro.md`](./joy-dfy-intro.md)

---

## 1. Scope — Khi nào áp dụng DFY

**Eligibility (đồng thời thỏa cả 2):**
1. MC đang dùng app và ở Widget V4 (unified widget).
2. MC thuộc ít nhất một trong các nhóm store sau:
   - **New install** — cài app trong vòng 30 ngày, chưa kịp setup hoàn chỉnh
   - **Installed but not launched** — cài lâu nhưng loyalty program chưa live (widget ẩn, page chưa accessible, hoặc không có earning program nào active)
   - **Launched but not on-brand** — đã live nhưng widget chưa match theme store (màu, font, wording, icon lạc tông)
3. Message Crisp inbound có intent liên quan **setup / customize / hiển thị** widget hoặc loyalty page — hoặc CS chủ động phát hiện store thuộc nhóm trên khi xử lý case khác

> CS đánh giá Crisp message → nếu match intent + plan trả phí → tự tạo ticket trong section "Done for You". Keyword list có thể mở rộng dựa trên data thực tế.

**KHÔNG tạo ticket DFY trong các trường hợp:**
- MC đã có ticket DFY active (status ≠ Adopted/No Adoption) → CS update ticket cũ thay vì tạo mới

---

## 3. CS audit — Nhìn toàn diện store trước khi vào flow

Trước khi bắt đầu, CS cần có cái nhìn tổng thể về store — không chỉ widget.

**Widget** — CS guide/setup trực tiếp trong chat (focus chính của checklist §7)

**Loyalty page:**
- Chưa có → recommend MC tạo — đây là điểm chạm quan trọng cho customer, thiếu page là thiếu một kênh convert
- Có rồi nhưng chưa on-brand → offer customize, đặc biệt với MC Advanced trở lên → forward TS xử lý, CS loop lại để verify kết quả

**Các element khác** (popup, launcher, account page…) — mention nếu thấy lạc tông hoặc chưa setup, nhưng không cần đi sâu trong DFY flow

---

## 4. CS Flow — Cách làm việc với MC

CS chủ động offer free white-glove service cho MC, dùng shortcut `!v4-rcm` hoặc `!dfy-offer`.

**Bước thực hiện:**

1. CS nhận chat của MC đang online → đánh giá store eligible → tạo ticket DFY bằng cách click button **[DFY]** embed trong Crisp chat hoặc prompt TS agent qua extension → ticket tự tạo kèm đầy đủ checklist, set label `DFY-new`
2. CS audit store → update label `DFY-in-progress` → chủ động setup widget theo checklist (Required trước, Recommended nếu phù hợp)
3. Sau khi có kết quả, CS dùng button **Preview on store** → **quay video ngắn kết quả** (highly recommended — MC dễ follow hơn nhiều so với email dài kèm ảnh) → gửi qua Crisp
4. Done → nếu convert được review từ flow DFY: gắn thêm `review-yes` → chụp ảnh hoặc quay video post vào phần comment để phục vụ tính point → **không close ticket ngay**, để mở chờ follow-up
5. **Follow-up sau 2–5 ngày** → CS check lại store xem MC có đang dùng/giữ customization không:
   - **Có adopt** (widget vẫn match, MC hài lòng) → gắn label `DFY-adopted` → close ticket
   - **Chưa thấy update / MC không phản hồi** → gửi reminder email (template `!dfy-remind`) → gắn label `DFY-no-adopt` → close ticket

> SLA: Bắt buộc phải có kết quả hoàn thiện và báo KH trong vòng **48H** sau khi tạo ticket. Nếu ticket quá 48H không có update → escalate Liz.

> **Lưu ý tính point:** Follow-up đúng hạn + gắn đủ tag (`DFY-adopted` hoặc `DFY-no-adopt`, `review-yes` nếu có) là điều kiện bắt buộc để ticket được tính vào points.

**Lưu ý:**
- Nếu là MC cũ (đang dùng widget cũ) → **tuyệt đối không ấn Switch to unified widget** nếu chưa được sự đồng ý của MC
- CS có thể show kết quả sơ bộ với MC trước để tăng khả năng xin review — sau đó hẹn MC gửi kết quả hoàn thiện sau
- CS được khuyến khích tự do sáng tạo và custom thêm cho phù hợp với store — miễn là Required items đã hoàn thành

---

## 5. Default checklist (CS audit)

Ticket auto-generate kèm checklist này. CS tick + viết note cho từng item.

Mục tiêu của DFY không phải là tick hết checklist — mà là làm cho widget **trông như một phần tự nhiên của store đó**. Mỗi store có thương hiệu, màu sắc, phong cách riêng (tối giản hay sặc sỡ, cao cấp hay gần gũi…), CS cần chủ động đọc store trước rồi mới bắt tay vào setup.

Checklist chia 2 phần: **Required** (bắt buộc mọi store) và **Recommended** (CS tự đánh giá — thêm nếu phù hợp, skip nếu không, ghi note lý do).

### Required

- [ ] Primary color + button color + text color phù hợp với brand, độ tương phản tốt
- [ ] Logo ở widget header (nếu thấy phù hợp)
- [ ] Point icon đã custom hợp lý
- [ ] Loyalty program name
- [ ] Point label phù hợp brand
- [ ] Header background image (nếu thấy phù hợp)
- [ ] Login with Shop đã bật nếu store có Login with shop option
- [ ] Drawer type
- [ ] Button shape giống với button shape ở store
- [ ] Content từng block đã viết lại onbrand (đặc biệt welcome messages)
- [ ] Referral banner image nếu store có chạy referral program
- [ ] Membership card images — Guest view
- [ ] Membership card images — Member view
- [ ] Ảnh của member profile sau khi login
- [ ] Các block không cần thiết đã ẩn
- [ ] Footer menu match với store
- [ ] Program order đã sort hợp lý

### Recommended

- [ ] My coupon images
- [ ] Ways to earn / redeem images
- [ ] Tier icon custom theo từng tier
- [ ] Tier banner custom theo store

### Bonus

- [ ] Video walkthrough / explain


---




