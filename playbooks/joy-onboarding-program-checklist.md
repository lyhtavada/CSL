# Joy Loyalty — Program Setup Checklist (template điền cho từng KH)

**Dùng cho:** [Joy Onboarding Flow — Phase 1](./joy-onboarding-flow.md). CS clone bảng này thành 1 Google Sheet cho mỗi KH → KH điền rule (hoặc CS gợi ý / AI agent trong app sinh) → paste link vào field **Detail program** của ticket onboarding chính.

**Cách dùng:**
- Cột **"KH điền"** = giá trị store này chọn.
- Cột **"Gợi ý / Preset"** = ví dụ mẫu để KH chưa biết thì theo (dựa AOV + ngành). CS có thể để AI agent trong app đọc AOV/industry sinh gợi ý.
- KH chưa từng dùng loyalty (nhánh C) → CS điền cột gợi ý trước, KH gật/chỉnh.

---

## 0. Thông tin store

| Mục | KH điền |
|-----|---------|
| Store / domain | |
| Plan | Advanced |
| Ngành hàng (industry) | |
| AOV (giá trị đơn TB) | |
| **Launch date dự kiến** | |
| Đã dùng loyalty app nào trước đó? | (tên app / chưa) |
| Migrate sang? | (có → app cũ / không) |

---

## 1. Program basics

| Mục | KH điền | Gợi ý / Preset |
|-----|---------|----------------|
| Tên program | | "[Brand] Rewards" / "[Brand] Club" |
| Đơn vị điểm (point name) | | Points / Coins / Stars |
| Tỉ giá điểm ↔ tiền | | 1 point = $0.01 (100 pts = $1) |

---

## 2. Earning rules — cách khách kiếm điểm

> Chọn các cách khách earn + giá trị mỗi cách. Ít nhất bật **signup + place order**.

| Way to earn | Bật? | Giá trị KH điền | Gợi ý / Preset |
|-------------|------|-----------------|----------------|
| Sign up / tạo account | ☐ | | +100 points |
| Place an order | ☐ | | $1 spent = 1 point |
| Product review | ☐ | | +50 points |
| Photo/video review | ☐ | | +100 points |
| Birthday | ☐ | | +200 points |
| Follow / share social | ☐ | | +50 points / kênh |
| Newsletter subscribe | ☐ | | +50 points |
| Referral (giới thiệu bạn) | ☐ | | xem §5 |

---

## 3. Redeeming rules — cách khách đổi điểm

> Chọn khách đổi điểm ra gì. Ít nhất bật **1 discount tier**.

| Way to redeem | Bật? | Giá trị KH điền | Gợi ý / Preset |
|---------------|------|-----------------|----------------|
| Fixed amount discount | ☐ | | 100 pts = $5 off |
| Percentage discount | ☐ | | 500 pts = 10% off |
| Free shipping | ☐ | | 300 pts = free ship |
| Free product | ☐ | | (tùy store) |
| Point expiration | ☐ | | 12 tháng không hoạt động → hết hạn |
| Min points để redeem | ☐ | | 100 pts |

---

## 4. VIP Tier (nếu có)

> Chỉ dùng nếu KH muốn phân hạng. Bỏ qua nếu program đơn giản.

| Tier | Điều kiện đạt (KH điền) | Perk (KH điền) | Gợi ý / Preset |
|------|------------------------|----------------|----------------|
| Tier 1 (vd Silver) | | | 0+ điểm/chi tiêu — earn cơ bản |
| Tier 2 (vd Gold) | | | $500 chi tiêu/năm — +earn rate, quà sinh nhật |
| Tier 3 (vd Platinum) | | | $2000 chi tiêu/năm — early access, free ship |

| Mục | KH điền | Gợi ý |
|-----|---------|-------|
| Tính tier theo? | | Total spent / points earned trong X tháng |
| Chu kỳ xét lại tier | | 12 tháng |

---

## 5. Referral (nếu bật)

| Mục | KH điền | Gợi ý / Preset |
|-----|---------|----------------|
| Người giới thiệu nhận | | +200 points sau khi bạn mua đơn đầu |
| Người được giới thiệu nhận | | $10 off đơn đầu |
| Điều kiện | | đơn tối thiểu $X |

---

## 6. Member vs Guest — hiển thị & quyền

| Mục | KH điền | Gợi ý / Preset |
|-----|---------|----------------|
| Guest (chưa login) thấy gì? | | thấy program + ways to earn, phải login mới tích/đổi |
| Member (đã login) khác gì? | | thấy điểm hiện có, lịch sử, đổi thưởng |
| Bắt buộc tạo account để earn? | | Có (Login with Shop nếu store bật) |

---

## 7. Migration / Import (nhánh A — nếu migrate)

| Mục | KH điền | Ghi chú CS |
|-----|---------|-----------|
| App cũ | | |
| Data đã export chưa? | | point balance / member list / tier |
| Format file | | CSV? |
| **Point balance migrate tới đâu** | | ⚠️ chốt sớm — set kỳ vọng, phức tạp → forward TS |
| Số lượng member | | |

---

## 8. Widget (ticket con riêng — chỉ ghi link ở đây)

| Mục | KH điền |
|-----|---------|
| Link ticket con widget customize | |

> Widget on-brand làm theo checklist [`joy-dfy-flow.md §7`](./joy-dfy-flow.md) trong ticket con — không làm trong sheet này.

---

## 9. Go-live check (CS tick trước khi bật live)

- [ ] Earning active
- [ ] Redeeming active
- [ ] VIP tier (nếu có) đúng ngưỡng/perk
- [ ] Member/Guest hiển thị đúng
- [ ] Migration/import xong & verify (nếu có)
- [ ] Widget hiện trên store
- [ ] **Test 1 vòng** (earn thử → redeem thử) OK
- [ ] Xin KH gật → **switch sandbox → live mode** 🚀

---

*(Liz bổ sung / chỉnh cột hoặc preset sau — nhất là số điểm mẫu theo ngành thực tế của KH Advanced.)*
