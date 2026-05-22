# Joy DFY — CS Flow & Checklist

**Owner:** Liz (CS Leader)
**Created:** 2026-05-18
**Updated:** 2026-05-20

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

1. CS nhận chat của MC đang online → đánh giá store eligible → tạo ticket DFY bằng cách click button **[DFY]** embed trong Crisp chat hoặc prompt TS agent qua extension → ticket tự tạo kèm đầy đủ checklist: **level 1 (basic branding), level 2 (full visual), level 3 (full onbrand)**, set label `DFY-new`
2. CS audit store → chọn level phù hợp → update label `DFY-in-progress` → chủ động setup widget theo checklist
3. Sau khi có kết quả, CS dùng button **Preview on store** → **quay video ngắn kết quả** (highly recommended — MC dễ follow hơn nhiều so với email dài kèm ảnh) → gửi qua Crisp
4. Done → gắn label level đạt được (`DFY-1` / `DFY-2` / `DFY-3`) → update label `DFY-adopted` → close ticket + chụp ảnh hoặc quay video post vào phần comment để phục vụ tính point

> SLA: Bắt buộc phải có kết quả hoàn thiện và báo KH trong vòng **48H** sau khi tạo ticket. Nếu ticket quá 48H không có update → escalate Liz.

**Lưu ý:**
- Nếu là MC cũ (đang dùng widget cũ) → **tuyệt đối không ấn Switch to unified widget** nếu chưa được sự đồng ý của MC
- CS có thể hoàn thành từng level và show kết quả sơ bộ với MC trước để tăng khả năng xin review — sau đó hẹn MC gửi kết quả hoàn thiện sau
- CS được khuyến khích tự do sáng tạo và custom thêm cho phù hợp với store, miễn là đã đảm bảo hoàn thành checklist của level đã chọn

---

## 5. Default checklist (CS audit)

Ticket auto-generate kèm checklist này. CS tick + viết note cho từng item.

CS chọn level cao nhất mình đạt được — level cao hơn bao gồm tất cả items của level dưới.

### Level 1 — Basic Branding

- [ ] Primary color + button color + text color
- [ ] Logo ở widget header
- [ ] Point icon đã custom
- [ ] Loyalty program name + point label phù hợp brand
- [ ] Header background image

### Level 2 — Full Visual *(Level 1 +)*

- [ ] Membership card images (guest + member)
- [ ] My coupon images
- [ ] Way to earn/redeem banner image
- [ ] Program order đã sort hợp lý

### Level 3 — Full Onbrand *(Level 1 + 2 +)*

- [ ] Tier banner (nếu có VIP tier)
- [ ] VIP icon đã thay theo từng tier
- [ ] Content từng block đã viết lại onbrand
- [ ] Các block không cần thiết đã ẩn
- [ ] Footer menu style match store
- [ ] Login with Shop đã bật

### Bonus

- [ ] Video walkthrough/ explain


---




