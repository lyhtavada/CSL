# Joy Loyalty — Program Setup Sheet (template điền cho từng KH)

**Dùng cho:** [Joy Onboarding Flow — Phase 1](./joy-onboarding-flow.md). CS clone thành 1 Google Sheet cho mỗi KH, **mỗi mảng = 1 tab riêng** → KH điền rule → paste link sheet vào field "Detail program" của ticket onboarding chính.

**Tabs:** `Store Info & Setup` · `Earning` · `Redemption` · `VIP Membership` · `Referral` · `Milestones & Quest`

- Cột **KH điền** = giá trị store này chọn.
- Cột **Gợi ý / Preset** = ví dụ mẫu (dựa AOV + ngành) để KH chưa biết thì theo. CS có thể để AI agent trong app đọc AOV/industry sinh gợi ý.
- **Status:** Existing / New / Upgraded / Skip — tick khi đã setup trong Joy admin.

---

## TAB 1 — Store Info & Setup (tiền đề)

### Store info
| Mục | KH điền |
|-----|---------|
| Store / domain | |
| Plan | Advanced |
| Ngành hàng (industry) | |
| AOV (giá trị đơn TB) | |
| **Launch date dự kiến** | |
| Đã dùng loyalty app nào trước đó? | (tên app / chưa) |
| Migrate sang? | (có → app cũ / không) |

### Program config
| Metric | KH điền | Gợi ý / Preset | Notes |
|--------|---------|----------------|-------|
| Tên program | | "[Brand] Club" / "[Brand] Rewards" | |
| Point currency name | | "[Brand] Points" (vd Koko Points) | tên riêng → khách thấy sở hữu |
| Point value | | 1 pt = $0.01 | ~5% rebate rate |
| Base earn rate | | 1 pt / $1 spent | tier multiplier cộng thêm ở tab VIP |
| Point expiry | | 12 tháng inactivity | win-back email trước khi hết hạn |
| Coupon expiry | | 45 ngày từ khi phát | cho khách thời gian dùng |
| BFCM / sự kiện policy | | pause earning trong event? | toggle Joy admin, báo khách trước |

### Migration / Import (chỉ nhánh migrate)
| Mục | KH điền | Notes CS |
|-----|---------|----------|
| App cũ | | |
| Data đã export chưa? | | point balance / member list / tier |
| Format file | | CSV? |
| **Point balance migrate tới đâu** | | ⚠️ chốt sớm, phức tạp → forward TS |
| Số lượng member | | |

---

## TAB 2 — Earning (cách khách kiếm điểm)

> Ít nhất bật **Place Order + Sign-up**.

| Rule | Action (Joy) | Points earned (KH điền) | $ Equiv | Gợi ý / Preset | Status |
|------|-------------|-------------------------|---------|----------------|--------|
| Purchase Reward | Place Order | | | 1 pt / $1 | |
| Welcome Bonus | Sign-Up | | | 200 pts (= $10) | |
| Newsletter Sign-Up | Newsletter Sign-Up | | | 50 pts | |
| Birthday Gift | Birthday Reward | | | 200–300 pts | |
| Product Review | Write Review | | | 50 pts | |
| Photo/Video Review | Write Review (media) | | | 150 pts | |
| Google Review | Google Reviews | | | 150 pts (limit 1/khách) | |
| Follow Instagram | Social Activity | | | 30 pts | |
| Follow TikTok | Social Activity | | | 30 pts | |
| Social Share | Custom (Shopify Flow) | | | 100 pts | |

---

## TAB 3 — Redemption (cách khách đổi điểm)

> Ít nhất bật **1 discount tier**.

| Reward | Type | Cost (pts) — KH điền | Value | Gợi ý / Preset | Status |
|--------|------|----------------------|-------|----------------|--------|
| Fixed discount | Amount off | | | 100 pts = $5 off | |
| Fixed discount | Amount off | | | 500 pts = $30 off | |
| Percentage discount | % off | | | 500 pts = 10% off | |
| Free shipping | Free ship | | | 300 pts | |
| Free product | Product | | | (tùy store) | |

| Rule chung | KH điền | Gợi ý |
|-----------|---------|-------|
| Min points để redeem | | 100 pts |
| Point expiration | | 12 tháng inactivity |

---

## TAB 4 — VIP Membership (nếu có tier)

> Bỏ qua nếu program đơn giản. Ví dụ Maison Koko: Sipper → Steeper → Master.

| Tier | Điều kiện đạt (KH điền) | Earn multiplier | Perk (KH điền) | Gợi ý / Preset |
|------|------------------------|-----------------|----------------|----------------|
| Tier 1 (vd Silver / Sipper) | | 1x | | 0+ — earn cơ bản |
| Tier 2 (vd Gold / Steeper) | | 1.5x | | $500/năm — +earn, quà sinh nhật |
| Tier 3 (vd Platinum / Master) | | 2x | | $2000/năm — early access, free ship |

| Cấu hình | KH điền | Gợi ý |
|----------|---------|-------|
| Tính tier theo? | | Total spent / points earned trong X tháng |
| Chu kỳ xét lại tier | | 12 tháng |
| Guest thấy gì? | | thấy program + ways to earn, login mới tích/đổi |
| Member thấy gì? | | điểm hiện có, lịch sử, tier, đổi thưởng |

---

## TAB 5 — Referral (giới thiệu bạn)

| Mục | KH điền | Gợi ý / Preset |
|-----|---------|----------------|
| Người giới thiệu nhận | | +200 pts sau khi bạn mua đơn đầu |
| Người được giới thiệu nhận | | $10 off đơn đầu |
| Điều kiện | | đơn tối thiểu $X |
| Referral banner (widget) | | on-brand image |

---

## TAB 6 — Milestones & Quest (nếu có)

> Chuỗi hành động / mốc để khách hoàn thành → thưởng thêm. Bỏ qua nếu không dùng.

| Milestone / Quest | Điều kiện (KH điền) | Reward (KH điền) | Gợi ý / Preset |
|-------------------|---------------------|------------------|----------------|
| Complete profile | | | +50 pts |
| First purchase | | | +100 pts |
| Reach X orders | | | bonus pts / unlock tier |
| Seasonal quest | | | (tùy campaign) |

---

## Go-live check (CS tick trước khi bật live — ghi trong ticket chính)

- [ ] Earning active
- [ ] Redemption active
- [ ] VIP tier (nếu có) đúng ngưỡng/perk
- [ ] Member/Guest hiển thị đúng
- [ ] Migration/import xong & verify (nếu có)
- [ ] Widget hiện trên store (ticket con riêng)
- [ ] **Test 1 vòng** (earn thử → redeem thử) OK
- [ ] Xin KH gật → **switch sandbox → live mode** 🚀

*(Liz chỉnh preset số điểm theo AOV/ngành thật của nhóm KH Advanced sau.)*
