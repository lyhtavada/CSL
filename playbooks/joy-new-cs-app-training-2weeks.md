# Joy Loyalty — Training plan CS mới (học app)

> **Phạm vi:** CHỈ học sản phẩm Joy Loyalty. Không bao gồm CS process (escalation, refund, tone, ticket) — phần đó học ở lộ trình riêng.
> **Thời lượng:** 2 tuần × 5 ngày × 4h/ngày = **40h**
> **Nguồn học duy nhất:** KB live trên `cs2.avada.net` (agent `joy-loyalty-agent`) — cùng nguồn bot Joyce dùng. Không đọc tài liệu cũ ở nơi khác.
> Lấy file: `.venv-crisp/bin/python skills/qa-weekly/scripts/fetch_kb.py joy <path>` — hoặc CS đọc trực tiếp trên cs2.

---

## Nguyên tắc học

**Khung 4h mỗi ngày (cố định):**

| Block | Thời lượng | Làm gì |
|---|---|---|
| 1. Đọc | 1h00 | Đọc KB reference của chủ đề trong ngày, gạch đầu dòng ra note riêng |
| 2. Thực hành | 2h00 | Set up đúng chủ đề đó trên dev store của mình, tự test bằng customer account |
| 3. Case | 0h30 | Đọc file `kb/case/*` tương ứng — đây là lỗi merchant hay gặp thật |
| 4. Self-check | 0h30 | Trả lời checklist cuối ngày, ghi lại câu chưa chắc → hỏi mentor sáng hôm sau |

**Bắt buộc trước ngày 1:**
- Dev store Shopify riêng, đã cài Joy Loyalty (plan Advanced để mở hết feature)
- Bật **Settings → Customer accounts** trong Shopify admin
- Tạo sẵn 3 customer test + 5 product test + 1 collection
- Quyền đọc KB trên `cs2.avada.net`

**Quy tắc vàng:** không feature nào được tick "xong" nếu chưa **tự tay setup + tự test bằng mắt khách hàng** trên storefront. Đọc hiểu ≠ biết làm.

---

## TUẦN 1 — Nền tảng + core loyalty

### Ngày 1 — Tổng quan Joy + Pricing
**Mục tiêu:** hiểu Joy giải quyết bài toán gì, cấu trúc admin, và trả lời được câu hỏi plan/giá.

- **Đọc:** `kb/reference/getting-started.md`, `kb/reference/pricing.md`, `kb/reference/settings-general.md`
- **Thực hành:**
  - Đi hết 5-step launch path: goal → chọn program type → cấu hình earning/redeeming → loyalty page → bật widget
  - Đổi custom point label (Settings → General) và xem nó đổi ở đâu trên storefront
  - Vẽ sơ đồ cây menu Joy Admin ra giấy — không nhìn màn hình
- **Case:** `kb/case/billing.md`
- **Checklist thoát ngày:**
  - [ ] Kể được 4 plan + base fee + free order quota + overage của từng plan
  - [ ] Giải thích được **order ≠ transaction** (1 transaction = 1 hoạt động loyalty)
  - [ ] Biết trial: 14 ngày Essential/Advanced, 30 ngày Ultimate, **1 lần/store**, reinstall không cấp lại
  - [ ] Biết "Pro" = tên cũ của **Essential**
  - [ ] Nói được vì sao Customer accounts là bắt buộc

### Ngày 2 — Earning programs
**Mục tiêu:** setup được mọi cách khách kiếm điểm.

- **Đọc:** `kb/reference/earning-programs.md`, `kb/reference/points-advanced.md`, `kb/reference/birthday.md`
- **Thực hành:**
  - Set up **Place order** với cả 3 rate option: per amount spent / per item / per order — hiểu khác nhau
  - Thêm: sign-up, social, review, birthday, custom program
  - Đặt 1 order thật trên dev store → xem điểm vào đúng chưa
  - Test points multiplier / rate khác nhau theo tier
- **Case:** `kb/case/points-earning.md`, `kb/case/birthday-reward.md`
- **Checklist thoát ngày:**
  - [ ] Đọc thuộc path: **Reward programs → Earning programs → Add rule**
  - [ ] Merchant hỏi "1$ = 10 points setup ở đâu?" → trả lời ngay: **Place order → per amount spent**
  - [ ] Biết program nào giới hạn theo plan
  - [ ] Giải thích được điểm store credit khác điểm thường thế nào

### Ngày 3 — Redeeming programs
**Mục tiêu:** setup được mọi cách khách tiêu điểm + hiểu giới hạn theo plan.

- **Đọc:** `kb/reference/redeeming-programs.md`, `kb/reference/checkout.md`
- **Thực hành:**
  - Tạo đủ: discount amount, discount %, BXGY, free gift, free shipping
  - Đặt total + per-customer redemption limit → test khi chạm limit
  - Redeem bằng customer test → soi coupon code sinh ra (one-time-use)
- **Case:** `kb/case/points-redeeming.md`
- **Checklist thoát ngày:**
  - [ ] Bảng plan availability: cái nào All, cái nào Essential+, cái nào **Ultimate + Shopify Plus + Checkout Extensibility**
  - [ ] Biết "Redeem at checkout page" — Advanced phải qua sales contact
  - [ ] Test được vòng đời 1 coupon từ redeem → apply → hết hạn

### Ngày 4 — Loyalty page + Widget + Onsite content
**Mục tiêu:** hiểu mọi điểm chạm khách hàng nhìn thấy — đây là nhóm ticket nhiều nhất.

- **Đọc:** `kb/reference/loyalty-page.md`, `kb/reference/widget.md`, `kb/reference/onsite-content.md`, `kb/reference/product-page.md`, `kb/reference/cart-drawer.md`, `kb/reference/thank-you-page.md`, `kb/reference/account-page.md`
- **Thực hành:**
  - Build loyalty page qua Theme Editor → Add section → Joy Loyalty
  - Bật widget qua App embeds → chỉnh vị trí, màu, trigger
  - Bật onsite content ở product page + cart drawer + thank-you page
  - **Tự phá rồi tự sửa:** tắt app embed → xem widget mất; bật lại
- **Case:** `kb/case/widget.md`, `kb/case/loyalty-page.md`, `kb/case/loyalty-page-buttons.md`, `kb/case/onsite-content.md`
- **Checklist thoát ngày:**
  - [ ] Merchant nói "widget không hiện" → liệt kê được ≥4 nguyên nhân theo thứ tự check
  - [ ] Phân biệt loyalty page (section) vs widget (app embed) — hai thứ khác nhau, bật riêng
  - [ ] Biết cái nào phụ thuộc theme / theme cũ vs OS 2.0

### Ngày 5 — VIP tiers + Milestone + Referral
**Mục tiêu:** ba program nâng cao merchant hay hỏi nhất.

- **Đọc:** `kb/reference/vip-tiers.md`, `kb/reference/milestone.md`, `kb/reference/referral.md`
- **Thực hành:**
  - Tạo 3 tier + entry condition + reward mỗi tier + earning rate khác nhau theo tier
  - Đẩy customer test lên tier 2 → xem tier update lúc nào, reset ra sao
  - Set 1 milestone
  - Chạy full referral: lấy link → mở incognito → đăng ký → mua → check reward 2 đầu
- **Case:** `kb/case/vip-tiers.md`, `kb/case/referral.md`
- **Checklist thoát ngày:**
  - [ ] Giải thích tier calculation + reset cycle
  - [ ] Biết vì sao referral "không chạy" (self-referral, cùng IP/email, chưa đủ điều kiện order…)
  - [ ] Phân biệt milestone vs VIP tier

**Cuối tuần 1 — mini test (30 phút, tách khỏi 4h):** mentor đưa 5 câu hỏi merchant thật → CS trả lời bằng lời + chỉ đúng path trong admin.

---

## TUẦN 2 — Data, kênh gửi, tích hợp, tổng ôn

### Ngày 6 — Customers + Points management + Migration
**Mục tiêu:** xử lý được dữ liệu khách và điểm — nhóm rủi ro cao nhất.

- **Đọc:** `kb/reference/customers.md`, `kb/reference/migration.md`, `kb/reference/rule-engine.md`
- **Thực hành:**
  - Adjust điểm thủ công 1 customer (cộng/trừ) → xem transaction history
  - Import điểm bằng CSV
  - Export customer list
  - Đọc rule engine, viết thử 1 rule đơn giản
- **Case:** `kb/case/customers.md`, `kb/case/unlimited-transactions.md`
- **Checklist thoát ngày:**
  - [ ] Nắm flow migration từ app loyalty khác + cần merchant gửi gì
  - [ ] Biết "unlimited transactions" **không phải** chuyện pricing → lấy store URL rồi escalate team
  - [ ] Biết điểm bị trừ/mất thì tra ở đâu

### Ngày 7 — Notifications + Email + Translations
**Mục tiêu:** mọi thứ Joy gửi cho khách.

- **Đọc:** `kb/reference/notifications.md`, `kb/reference/settings-email.md`, `kb/reference/translations.md`, `kb/reference/ask-for-review.md`
- **Thực hành:**
  - Bật + sửa nội dung 3 email notification, gửi test về mail mình
  - Set sender email + domain authentication
  - Dịch widget + loyalty page sang 1 ngôn ngữ thứ 2, test đổi ngôn ngữ trên storefront
- **Case:** `kb/case/notifications.md`, `kb/case/translations.md`, `kb/case/review-points.md`
- **Checklist thoát ngày:**
  - [ ] Liệt kê được đủ loại notification Joy gửi + trigger từng loại
  - [ ] Merchant "khách không nhận được email" → biết thứ tự check
  - [ ] Biết cái gì dịch được, cái gì không

### Ngày 8 — Integrations + POS + Joy AI
**Mục tiêu:** biết Joy nối với gì, và giới hạn ở đâu.

- **Đọc:** `kb/reference/integrations-email.md`, `integrations-reviews.md`, `integrations-subscription.md`, `integrations-mobile.md`, `integrations-shopify-flow.md`, `integrations-other.md`, `kb/reference/pos.md`, `kb/reference/joy-ai.md`
- **Thực hành:**
  - Nối 1 integration thật (Klaviyo hoặc review app) → xem data chảy qua
  - Đọc kỹ POS: điều kiện, giới hạn, plan nào có
  - Thử Joy AI, hiểu nó làm được gì
- **Case:** `kb/case/integrations.md`, `kb/case/pos.md`
- **Checklist thoát ngày:**
  - [ ] Kể được danh sách integration + plan yêu cầu
  - [ ] Nắm giới hạn POS (câu hỏi merchant hỏi nhiều)
  - [ ] Biết integration nào cần Shopify Plus

### Ngày 9 — Settings nâng cao + Analytics + Wallet pass
**Mục tiêu:** quét nốt phần còn lại, không để lỗ hổng.

- **Đọc:** `kb/reference/settings-order.md`, `settings-developers.md`, `settings-misc.md`, `kb/reference/analytics.md`, `kb/reference/wallet-pass.md`, `kb/reference/membership-b2b.md`, `kb/reference/membership-subscription.md`, `kb/reference/shopify-admin.md`, `kb/reference/collaborator-access.md`, `kb/reference/billing-refund.md`
- **Thực hành:**
  - Đọc hết Analytics dashboard, giải thích được từng metric
  - Set order settings (điểm khi refund/cancel — hay gây tranh cãi)
  - Tạo wallet pass, cài lên điện thoại
  - Tự xin collaborator access vào 1 store test → nhớ đúng flow
- **Case:** `kb/case/errors.md`
- **Checklist thoát ngày:**
  - [ ] Biết điểm xử lý sao khi order bị refund / cancel
  - [ ] Đọc được Analytics và nói merchant nên nhìn số nào
  - [ ] Thuộc flow xin collaborator access

### Ngày 10 — Tổng ôn + Final test
**Mục tiêu:** chứng minh tự làm được từ số 0.

- **Thực hành (3h) — Build store hoàn chỉnh trên dev store mới, tính giờ:**
  1. Cài Joy từ đầu, bật customer accounts
  2. Chương trình: earning (place order + sign-up + birthday + referral) + redeeming (discount + free shipping + free gift)
  3. 3 VIP tier với earning rate khác nhau
  4. Loyalty page + widget + onsite content ở product page & cart
  5. Notification bật + branding + dịch 1 ngôn ngữ 2
  6. Import 10 customer kèm điểm bằng CSV
  7. Test end-to-end bằng customer thật: đăng ký → mua → lên tier → redeem → dùng coupon
- **Final test (1h) — mentor chấm:**
  - 10 câu hỏi merchant thật (mentor lấy từ chat Crisp tuần gần nhất) — CS trả lời + chỉ đúng path
  - 3 ca troubleshoot: widget không hiện / điểm không cộng / referral không chạy
  - **Pass = ≥8/10 câu đúng và cả 3 ca troubleshoot chỉ được đúng thứ tự check**

---

## Bảng theo dõi (mentor điền)

| Ngày | Chủ đề | Thực hành xong | Checklist pass | Câu còn vướng | Mentor ký |
|---|---|---|---|---|---|
| 1 | Tổng quan + Pricing | | | | |
| 2 | Earning | | | | |
| 3 | Redeeming | | | | |
| 4 | Loyalty page + Widget | | | | |
| 5 | VIP + Milestone + Referral | | | | |
| — | **Mini test tuần 1** | | | | |
| 6 | Customers + Migration | | | | |
| 7 | Notifications + Email | | | | |
| 8 | Integrations + POS + AI | | | | |
| 9 | Settings + Analytics | | | | |
| 10 | **Final test** | | | | |

## Sau khi pass

CS đã biết app. Bước tiếp theo là CS process — không nằm trong plan này:
- `kb/cs-process/joy-support-flow.md`
- `playbooks/joy-dfu-onboarding-playbook.md` (FAQ 50 case — đọc ở giai đoạn sau, không nhồi vào 2 tuần này)
- `_identity/tone-and-voice.md`
