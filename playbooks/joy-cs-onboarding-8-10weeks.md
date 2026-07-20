# Joy Loyalty — CS Onboarding Plan (8-10 tuần)

> **Phạm vi:** Training toàn diện CS mới cho Joy Loyalty — Shopify nền tảng, company/CS team, học app Joy, CS process, đọc chat thật, mock chat, đến go-live độc lập.
> **Thời lượng:** 9 tuần (chuẩn) — co giãn 8-10 tuần tùy tốc độ trainee. Gợi ý co/giãn ghi ở cuối mỗi tuần liên quan.
> **Cách dùng:** Mỗi tuần có To-do (task cụ thể) → Test cuối tuần → Checklist follow-up (Liz/mentor tick trực tiếp vào bảng).
> **Bắt buộc:** ngay dưới mỗi phần **Thực hành**/**To-do**, CS phải điền **kết quả** — link/screenshot/video demo hoặc câu trả lời trực tiếp — không để trống. Mentor dựa vào đây để duyệt, không chỉ dựa vào tick checkbox.

---

## TUẦN 1 — Shopify 101 + Company & CS team

**Mục tiêu:** hiểu Shopify vận hành thế nào (để hiểu app Joy ngồi ở đâu trong hệ sinh thái), biết mình đang làm cho ai, làm với ai, theo quy tắc nào.

**To-do:**
- [ ] Tạo dev store Shopify riêng (free trial), tự cài 1 theme, thêm 3-5 sản phẩm test
- [ ] Đọc Shopify Admin cơ bản: Products, Orders, Customers, Discounts, Apps, Theme editor
- [ ] Tìm hiểu khái niệm: Shopify Plan, Checkout, App Store, App embeds
- [ ] Đọc `_identity/who-we-are.md`, `values.md`, `tone-and-voice.md`
- [ ] Đọc `_identity/responsibilities.md`, `_identity/team-g2.md` — biết ai làm gì trong team
- [ ] Đọc quy trình CS team (doc Liz đính kèm)
- [ ] (Optional, đọc thêm nếu có thời gian) Notion **Module 0 — Basic eCommerce**: lịch sử thương mại, Shopify App Store vận hành ra sao, dropshipping — giúp hiểu bối cảnh business trước khi vào sản phẩm
- [ ] 1-1 giới thiệu với mentor/Liz — hỏi bất kỳ câu gì về công ty, sản phẩm, kỳ vọng vai trò

📎 **Kết quả/Proof:**

**Test cuối tuần (30 phút, mentor hỏi miệng):**
- Giải thích được Shopify Admin có gì, App hoạt động trong store merchant ra sao (không cần sâu, chỉ cần đúng khái niệm)
- Kể được cấu trúc team G2, ai là escalation point, quy trình báo cáo khi gặp vấn đề
- Nói được tone & voice công ty áp dụng khi chat với khách

**Checklist theo dõi:**

| Hạng mục | Hoàn thành | Ghi chú |
|---|---|---|
| Dev store Shopify sẵn sàng | | |
| Đọc xong _identity/* | | |
| Đọc xong quy trình CS team | | |
| Test cuối tuần pass | | |

---

## TUẦN 2-3 — Learn Joy (product, có test)

**Mục tiêu 2 tuần:** kết thúc tuần 3, CS phải **tự cài + vận hành được Joy Loyalty từ số 0 trên 1 store bất kỳ**, và trả lời được câu hỏi merchant thật mà không cần tra cứu lại — không chỉ hiểu lý thuyết tính năng.

> **Format:** mỗi mục bên dưới là 1 **Heading 2 dạng toggle** (khi đưa vào Notion, set từng heading này thành toggle heading 2 để gập/mở) — không chia theo ngày cụ thể, trainee tự sắp xếp tốc độ học trong 2 tuần.

**To-do tổng quan (bức tranh toàn 2 tuần — xem chi tiết từng mục ở các toggle bên dưới):**
- [ ] **Setup được toàn bộ launch path:** cài app → bật customer accounts → chọn program type → cấu hình earning/redeeming → dựng loyalty page/widget → bật onsite content
- [ ] **Setup được các block hiển thị trên website** (không chỉ đọc lý thuyết): loyalty page, widget, onsite content (product page/cart drawer/thank-you page), account page — xem checklist setup riêng bên dưới
- [ ] **Cấu hình được mọi chương trình earning:** place order (3 rate option), sign-up, social, review, birthday, custom
- [ ] **Cấu hình được mọi chương trình redeeming:** discount amount/%, BXGY, free gift, free shipping — hiểu giới hạn theo plan
- [ ] **Dựng được VIP tier, milestone, referral** — test end-to-end bằng customer thật (đăng ký → mua → lên tier → redeem)
- [ ] **Xử lý được dữ liệu khách/điểm:** adjust điểm thủ công, import/export CSV, hiểu flow migration từ app loyalty khác
- [ ] **Bật + tùy chỉnh được thông báo:** email notification, sender domain, dịch đa ngôn ngữ
- [ ] **Biết giới hạn tích hợp:** integrations (Klaviyo/review apps...), POS, Joy AI — cái nào cần Shopify Plus
- [ ] **Đọc hiểu Analytics dashboard** + biết xử lý điểm khi order refund/cancel
- [ ] **Thuộc bảng plan (Essential/Advanced/Ultimate):** feature nào thuộc plan nào, trial rules, "Pro" = tên cũ Essential
- [ ] Tra case thật qua TS Elite tương ứng mỗi chủ đề — đây là lỗi merchant hay gặp nhất, không phải lý thuyết suông

**Nguồn học:** [help.joy.so](https://help.joy.so/) (help center chính thức của Joy — Reward Programs, Membership, On-Site Content, Customers, Operations, Support/Migration, FAQs) + Notion **"Joy Loyalty program - Training courses"** Module 0-6 (course chính thức, có video + case study Vinamilk, so sánh đối thủ, hướng dẫn setup chi tiết).

**Case thật:** tra qua **TS Elite** (`agent.avada-ts.site`, docs `/api/docs`) — mentor/trainee pull case thật theo chủ đề mỗi ngày qua endpoint `crisp-chat` (đọc 1 chat cụ thể) hoặc `agent-activity`/`app-digest` (quét case gần đây theo domain), thay vì đọc file case tĩnh.

**Khung mỗi buổi học (~4h):** 1h đọc help.joy.so/Module + xem video → 2h thực hành tự setup trên dev store → 0.5h tra case thật qua TS Elite → 0.5h self-check checklist, ghi câu chưa chắc hỏi mentor buổi sau.

**Bắt buộc trước khi bắt đầu:** dev store riêng đã cài Joy (plan Advanced), bật Customer accounts, có sẵn 3 customer test + 5 product test + 1 collection.

**Quy tắc vàng:** không tick "xong" nếu chưa tự tay setup + tự test bằng mắt khách hàng trên storefront. Đọc hiểu ≠ biết làm.

## Bài toán Joy giải quyết + Tổng quan + Pricing

**Đọc:** Module 1 (Retention — Joy giải quyết bài toán gì: tối ưu chi phí phân phối/D2C, xây thương hiệu bền vững, mở rộng qua referral; case study Vinamilk), Module 2 (Joy vs đối thủ 2025)

**Thực hành:**
- Đi hết 5-step launch path: goal → chọn program type → cấu hình earning/redeeming → loyalty page → bật widget
- Đổi custom point label, xem nó đổi ở đâu trên storefront
- Vẽ sơ đồ cây menu Joy Admin ra giấy — không nhìn màn hình

📎 **Kết quả/Proof:**

**Case thật (TS Elite):** tra 2-3 case về billing/plan gần đây qua `agent-activity`

**Checklist hoàn thành:**
- [ ] Giải thích được bằng lời (không đọc slide) Joy giải quyết 3 bài toán gì: tối ưu chi phí bán hàng/margin, xây thương hiệu bền vững, mở rộng khách qua referral — không chỉ nói "app tích điểm"
- [ ] Kể được 1-2 điểm khác biệt Joy vs đối thủ chính trên thị trường
- [ ] Kể được 4 plan + base fee + free order quota + overage của từng plan
- [ ] Giải thích được **order ≠ transaction**
- [ ] Biết trial: 14 ngày Essential/Advanced, 30 ngày Ultimate, 1 lần/store, reinstall không cấp lại. "Pro" = tên cũ Essential

## Earning programs

**Đọc:** [help.joy.so/reward-programs](https://help.joy.so/reward-programs/) — mục Earning programs (orders, sign-ups, birthdays, reviews, surveys, social, custom)

**Thực hành:**
- Set up Place order với cả 3 rate option: per amount spent / per item / per order
- Thêm: sign-up, social, review, birthday, custom program
- Đặt 1 order thật → xem điểm vào đúng chưa
- Test points multiplier/rate khác nhau theo tier

**Case thật (TS Elite):** tra case earning/birthday qua `crisp-chat`/`agent-activity`

**Checklist hoàn thành:**
- [ ] Đọc thuộc path: Reward programs → Earning programs → Add rule
- [ ] "1$ = 10 points setup ở đâu?" → trả lời ngay: Place order → per amount spent
- [ ] Biết program nào giới hạn theo plan

## Redeeming programs

**Đọc:** [help.joy.so/reward-programs](https://help.joy.so/reward-programs/) — mục Redeeming programs (discounts, free gifts, shipping, checkout redemption, limits)

**Thực hành:**
- Tạo đủ: discount amount, discount %, BXGY, free gift, free shipping
- Đặt total + per-customer redemption limit → test khi chạm limit
- Redeem bằng customer test → soi coupon code sinh ra (one-time-use)

**Case thật (TS Elite):** tra case redeem/coupon qua `crisp-chat`/`agent-activity`

**Checklist hoàn thành:**
- [ ] Bảng plan availability: cái nào All, cái nào Essential+, cái nào Ultimate + Plus + Checkout Extensibility
- [ ] Test được vòng đời 1 coupon từ redeem → apply → hết hạn

## Loyalty page + Widget V4 + Onsite content + Account page

**Đọc:** Module 3 phần *Setup on test theme / Setup branding widget / Setup loyalty page / Setup my account page* + [help.joy.so/on-site-content](https://help.joy.so/on-site-content/) — Branding (unified widget, loyalty design), Loyalty Landing Page, Account Page, Product Page, Cart Drawer, Thank You page

**Thực hành — setup bắt buộc trên dev store (nhóm ticket nhiều nhất merchant hỏi):**

| Hạng mục setup | Hoàn thành | Link/screenshot dev store |
|---|---|---|
| Duplicate theme ra 1 bản riêng để setup thử (test theme), dùng preview mode | | |
| Loyalty page — build qua Theme Editor → Add section → Joy Loyalty (hero, how it works, ways to earn/redeem, VIP tiers, FAQ) | | |
| Widget V4 — chỉnh branding trong in-app editor: màu preset match store, layout drawer, ảnh guest/member card, currency icon, logo header | | |
| Widget — bật qua App embeds; tắt app embed rồi tự bật lại (hiểu nguyên nhân "widget mất") | | |
| Onsite content — product page, cart drawer, thank-you page | | |
| Account page — hiểu phân biệt **Legacy vs New Customer Accounts** (New: SSO link, không chạy JS, chỉ add app block; Legacy: dễ custom liquid hơn) | | |
| Custom point label + prefix coupon code | | |
| Manual opt-in (nếu KH launch club mới, cần commitment) — hiểu khi nào nên dùng | | |
| Sandbox mode — bật thử earn/redeem không ảnh hưởng data thật, hiểu khi nào dùng (setup mới, demo, thử rule mới) | | |

**Case thật (TS Elite):** tra case widget/loyalty page qua `crisp-chat`/`agent-activity`

**Checklist hoàn thành:**
- [ ] "Widget không hiện" → liệt kê ≥4 nguyên nhân theo thứ tự check
- [ ] Phân biệt loyalty page (section) vs widget (app embed)
- [ ] Phân biệt New vs Legacy Customer Accounts, biết Shopify đang force chuyển hết sang New
- [ ] Giải thích được vì sao nên setup trên test theme + sandbox mode trước khi launch thật

## VIP tiers + Milestone + Referral (troubleshoot sâu)

**Đọc:** Module 3 phần *VIP tiers* (đặc biệt "VIP tier hoạt động end-to-end" + "Troubleshooting VIP tier") + [help.joy.so/membership](https://help.joy.so/membership/) (VIP tiers), [help.joy.so/reward-programs/milestone](https://help.joy.so/reward-programs/milestone/), [help.joy.so/reward-programs/referrals](https://help.joy.so/reward-programs/referrals/)

**Thực hành:**
- Tạo 3 tier + entry condition + reward mỗi tier + earning rate khác nhau theo tier
- Nhấn Launch, quan sát banner "Calculating Customer Tiers" — hiểu 3 bước hệ thống chạy ngầm: (1) recalc tier trên Joy, (2) sync metafield sang Shopify, (3) sync tag sang Shopify
- Đẩy customer test lên tier 2 → check tag + metafield `avada_joy.vipTier` trên Shopify customer, không chỉ nhìn trong app
- Set 1 milestone
- Chạy full referral: lấy link → mở incognito → đăng ký → mua → check reward 2 đầu; đọc qua các anti-cheat (self-referral, cùng IP/email)

**Case thật (TS Elite):** tra case VIP tier/referral qua `crisp-chat`/`agent-activity` — ưu tiên tìm case "tier đúng nhưng không nhận perk" để đối chiếu với checklist bên dưới

**Checklist hoàn thành (đây là nhóm ticket #1 CS hay gặp — thuộc lòng thứ tự check này):**
- [ ] Giải thích được: **"tier đúng trong app" ≠ "perk chạy"** — perk chỉ chạy khi tier đã sync tag/metafield sang Shopify VÀ discount function đọc được
- [ ] Thuộc checklist troubleshoot theo đúng thứ tự khi merchant báo "tier/perk sai": (1) tier đúng trong app chưa? (2) đã sync tag+metafield sang Shopify chưa? (3) perk cấu hình đúng chưa? (4) có discount khác non-combinable đang thắng không? (5) ai save setting/bấm recalc giữa chừng gây downgrade âm thầm không? (6) hiển thị đúng ở widget/POS chưa?
- [ ] Biết: nhiều triệu chứng ("tier sai", "không nhận perk", "earn sai") sau 1 lần launch/migrate lỗi thường là **CÙNG MỘT gốc** → gộp 1 ticket, không tách 2-3 ticket rời báo dev
- [ ] Chỉ escalate dev khi đã qua hết 5/6 bước tự check ở trên mà vẫn sai, kèm bằng chứng (customer, tier, ảnh tag/metafield, coupon)
- [ ] Biết vì sao referral "không chạy" (self-referral, cùng IP/email, chưa đủ điều kiện order…)
- [ ] Phân biệt milestone vs VIP tier

**Test giữa chặng (30 phút, sau khi xong nhóm Pricing → VIP tiers):** mentor đưa 5 câu hỏi merchant thật → CS trả lời bằng lời + chỉ đúng path trong admin. Bắt buộc có 1 câu về troubleshoot VIP tier.

---

## Customers + Points management + Migration (dev zone)

**Đọc:** Module 3 phần *Migration and import* (đọc kỹ — nhiều cạm bẫy) + [help.joy.so/customers](https://help.joy.so/customers/), [help.joy.so](https://help.joy.so/) mục Support → Migration (từ Stamped, Smile, Rivo, Yotpo, others)

**Thực hành:**
- Adjust điểm thủ công 1 customer (cộng/trừ) → xem transaction history
- Vào **dev zone → Enable feature migration** — hiểu từng control: "shop đang migrate" (tránh side-effect bắn nhầm email/webhook), nút **Recalculate** (quét lại order Shopify tính amount-spent — dùng khi KH CÓ orders trên Shopify), **Has migrate tier points** (bật mới migrate được cột Tier points)
- Tự chạy thử 1 lần migrate: import balance điểm (cột Points balance) + migrate VIP tier theo tên + **thêm cột Tier points vào file rồi map ở bước Match** (không bị giới hạn theo file mẫu)
- Import điểm bằng CSV, export customer list

**Case thật (TS Elite):** tra case customers/migration/points qua `crisp-chat`/`agent-activity`

**Checklist hoàn thành:**
- [ ] Phân biệt được **Migration wizard** (dev zone, mang balance/tier/tier points) vs **Import → Update tier** (trang Customers, file `tier_*_sample.csv`) — hai tính năng khác nhau, đừng nhầm
- [ ] Biết: tier theo **POINTS** → migrate tier point bằng file là nên làm; tier theo **AMOUNT SPENT có orders trên Shopify** → ưu tiên **Recalculate**, không nhập tay (Recalc sẽ ghi đè số nhập tay)
- [ ] Biết sau import khách thường ở trạng thái **guest** — phải confirm guest/member với KH trước khi launch
- [ ] Biết data lệch/gõ sai tên hạng → khách bị dồn về Bronze; biết 2 chỗ Joy KHÔNG tự sửa số tier point lệch ngưỡng
- [ ] Biết "unlimited transactions" không phải chuyện pricing → lấy store URL rồi escalate team
- [ ] Tránh import/migrate nhiều lần (dễ cộng đôi điểm)

## Notifications + Email + Translations

**Đọc:** [help.joy.so](https://help.joy.so/) mục Operations → Notifications, Settings (email), [help.joy.so/translations](https://help.joy.so/translations/)

**Thực hành:**
- Bật + sửa nội dung 3 email notification, gửi test về mail mình
- Set sender email + domain authentication
- Dịch widget + loyalty page sang 1 ngôn ngữ thứ 2, test đổi ngôn ngữ trên storefront

**Case thật (TS Elite):** tra case notification/email/translation qua `crisp-chat`/`agent-activity`

**Checklist hoàn thành:**
- [ ] Liệt kê đủ loại notification Joy gửi + trigger từng loại (open rate ~40% — touch point quan trọng, không phải phụ)
- [ ] "Khách không nhận được email" → biết thứ tự check
- [ ] Biết cái gì dịch được, cái gì không

## Integrations + POS + Checkout extensions + Joy AI

**Đọc:** Module 3 phần *Integrations* + *Setup checkout, thank you page extensions* + *Setup POS* + [help.joy.so](https://help.joy.so/) mục Operations → Integrations, [help.joy.so/pos](https://help.joy.so/pos/), [help.joy.so/joy-ai](https://help.joy.so/joy-ai/)

**Thực hành:**
- Nối 1 integration thật (Klaviyo hoặc review app) → xem data chảy qua
- Đọc kỹ POS: điều kiện, giới hạn, plan nào có; biết auto-discount tier **không chạy ở POS**
- Đọc checkout extensions (chỉ Plus, 1 ngôn ngữ) — quick redeem, point calculator, coupon list, sign-up block
- Thử Joy AI, hiểu nó làm được gì

**Case thật (TS Elite):** tra case integrations/POS qua `crisp-chat`/`agent-activity`

**Checklist hoàn thành:**
- [ ] Kể được danh sách integration phổ biến (Klaviyo top-of-mind dù rating thấp, Omnisend, Judge.me/Loox/Yotpo, Shopify Flow, Gorgias, Chatty) + plan yêu cầu
- [ ] Nắm giới hạn POS (câu hỏi hay gặp) + checkout extensions chỉ dành Plus
- [ ] Biết integration nào cần Shopify Plus

## Settings nâng cao + Point calculator + Analytics + Launch live

**Đọc:** Module 3 phần *Point calculators* + *Launch from sandbox mode to live mode* + *Xem số liệu report* + [help.joy.so/analytics](https://help.joy.so/analytics/), [help.joy.so](https://help.joy.so/) mục Operations → Settings, mục Customers (wallet pass)

**Thực hành:**
- Set order settings (điểm khi refund/cancel — hay gây tranh cãi)
- Bật point calculator ở product page + cart drawer (bật app embed calculator, thêm snippet `<div class="joy-points-calculator__block"></div>` vào liquid nếu theme tự render lại cart bằng innerHTML thì gọi `avadaJoyRerenderAllCalculators()`)
- Đọc Analytics dashboard — hiểu **assisted revenue** và **redemption rate** nghĩa là gì, nói được merchant nên nhìn số nào
- Thực hành **Launch from sandbox → live mode** — hiểu đây là bước quan trọng cuối cùng để điểm bắt đầu ghi nhận thật
- Tạo wallet pass, thử xin collaborator access vào 1 store test

**Case thật (TS Elite):** tra case order/refund/analytics qua `crisp-chat`/`agent-activity`

**Checklist hoàn thành:**
- [ ] Biết điểm xử lý sao khi order bị refund/cancel
- [ ] Đọc được Analytics, giải thích được assisted revenue + redemption rate cho merchant
- [ ] Biết chỗ thêm point calculator vào cart drawer khi theme không tự nhận (snippet + hàm rerender)
- [ ] Thuộc flow chuyển từ sandbox mode sang live mode

## Tổng ôn + Final test

**Thực hành (3h) — build store hoàn chỉnh trên dev store mới, tính giờ:**
1. Cài Joy từ đầu, bật customer accounts, chọn Legacy hoặc New có chủ đích
2. Chương trình: earning (place order + sign-up + birthday + referral) + redeeming (discount + free shipping + free gift)
3. 3 VIP tier với earning rate khác nhau, launch và verify tag/metafield đã sync sang Shopify
4. Loyalty page + widget V4 (branding cơ bản) + onsite content ở product page & cart + point calculator ở cart drawer
5. Notification bật + branding + dịch 1 ngôn ngữ 2
6. Import 10 customer kèm điểm bằng CSV/migration wizard
7. Launch từ sandbox sang live, test end-to-end bằng customer thật: đăng ký → mua → lên tier → redeem → dùng coupon

**Final test (1h) — mentor chấm:**
- 10 câu hỏi merchant thật (mentor lấy từ chat Crisp tuần gần nhất) — CS trả lời + chỉ đúng path
- 3 ca troubleshoot: widget không hiện / điểm không cộng / **VIP tier đúng trong app nhưng perk không apply** (bắt buộc dùng đúng checklist 6 bước ở mục VIP tiers)
- **Pass = ≥8/10 câu đúng và cả 3 ca troubleshoot chỉ đúng thứ tự check**

**Checklist theo dõi (mentor điền):**

| Chủ đề | Checklist hoàn thành |
|---|---|
| Bài toán Joy giải quyết + Tổng quan + Pricing | |
| Earning | |
| Redeeming | |
| Loyalty page + Widget V4 + Account page | |
| VIP tier end-to-end + Milestone + Referral | |
| **Test giữa chặng** | |
| Customers + Migration (dev zone) | |
| Notifications + Email | |
| Integrations + POS + Checkout ext + AI | |
| Settings + Point calculator + Analytics + Launch live | |
| **Final test** | |

> Trainee đã có kinh nghiệm CS app loyalty khác → có thể đi nhanh hơn, gộp mục Customers+Migration với Settings+Analytics trong cùng 1 buổi.

**Tài nguyên tham khảo thêm (xem bất kỳ lúc nào trong 2 tuần, không bắt buộc theo ngày):**
- Notion **Module 4 — Guides videos**: kênh Screenpal video hướng dẫn setup từng phần
- Notion **Module 5 — Demo stores**: danh sách store demo để xem cách configure app tốt nhất, tính năng nào làm được gì

---

## TUẦN 4 — Joy CS process riêng

**Mục tiêu:** biết xử lý ticket/chat theo đúng quy trình công ty, không chỉ biết app.

**To-do:**
- [ ] Đọc `kb/cs-process/joy-support-flow.md` — flow tra cứu khi khách báo lỗi
- [ ] Đọc `playbooks/joy-onboarding-flow.md` — flow onboarding khách mới (offer → discovery → ticket → nhánh A/B/C)
- [ ] Đọc `playbooks/joy-dfu-onboarding-playbook.md` Phần 3 — lướt qua 50 case theo 8 domain (chưa cần thuộc, chỉ cần biết cấu trúc: Dấu hiệu → Tự chẩn đoán → Xử lý → Khi nào escalate)
- [ ] Đọc `shared-cs-process/escalation-matrix.md`, `case-classification.md`, `first-response.md`, `follow-up.md`
- [ ] Đọc `shared-cs-process/handle-billing-refund.md`, `handle-complaints.md`, `handle-sensitive-situations.md`
- [ ] Tự phân loại thử 10 case mẫu (mentor đưa) theo đúng case-classification + escalation matrix
- [ ] Viết thử 1 escalation note mẫu theo đúng format

**Test cuối tuần:**
- 10 case mẫu (tình huống mô tả, không phải chat thật) → trainee phân loại đúng mức độ + chỉ đúng bước xử lý/escalate theo matrix
- 1 case viết escalation note — mentor chấm đủ thông tin theo `escalation-note.md`

**Checklist theo dõi:**

| Hạng mục | Hoàn thành | Ghi chú |
|---|---|---|
| Đọc xong toàn bộ process docs | | |
| Phân loại 10 case mẫu (điểm/10) | | |
| Escalation note đạt chuẩn | | |
| Test cuối tuần pass | | |

---

## TUẦN 5 — Đọc Crisp + luyện case thật

**Mục tiêu:** đọc hiểu context 1 cuộc chat thật trên Crisp, tra đúng case trong 50 case FAQ.

**To-do:**
- [ ] Đọc `skills/read-crisp/SKILL.md` — cách đọc/tóm tắt 1 session Crisp
- [ ] Mentor gửi 10 link chat Crisp thật (đã xử lý xong) → trainee tự đọc, tóm tắt lại vấn đề + cách CS cũ xử lý, KHÔNG xem trước đáp án
- [ ] Với mỗi case, tự tra ngược trong 50 case (Phần 3 playbook) xem case đó rơi vào domain nào, đúng lăng kính 🟢🔵🟠🔴 nào
- [ ] Ghi lại 5 case mình thấy khó nhất → hỏi mentor

**Test cuối tuần:**
- Mentor đưa 5 link Crisp mới (trainee chưa từng xem) → trainee đọc, tóm tắt đúng vấn đề, xác định đúng domain + lăng kính, đề xuất hướng xử lý — chấm bằng lời với mentor

**Checklist theo dõi:**

| Hạng mục | Hoàn thành | Ghi chú |
|---|---|---|
| 10 case thật đã đọc + tóm tắt | | |
| Tra đúng domain/lăng kính (điểm/10) | | |
| Test cuối tuần (điểm/5) | | |

---

## TUẦN 6 — Mock chat

**Mục tiêu:** phản xạ trả lời real-time, chưa để khách thật rủi ro.

**To-do:**
- [ ] Mentor/CS senior đóng vai khách hàng, dựng lại 8-10 case thật (lấy từ Crisp tuần gần nhất, đa dạng độ khó) → trainee trả lời live qua chat/Slack giả lập
- [ ] Bắt buộc có ít nhất 3 ca troubleshoot khó: widget không hiện / điểm không cộng / referral không chạy
- [ ] Bắt buộc có 1 ca khách hàng gắt/complaint để luyện tone xử lý sensitive situation
- [ ] Bắt buộc có 1 ca cần escalate — trainee phải nhận ra và viết escalation note đúng lúc
- [ ] Sau mỗi ca, mentor feedback ngay (đúng/sai, thiếu gì, tone ổn không)

**Test cuối tuần:**
- 2 ca mock chat hoàn toàn mới (trainee không biết trước kịch bản), mentor chấm theo rubric: đúng vấn đề / đúng xử lý / đúng tone / đúng quyết định escalate hay không — **Pass = cả 2 ca đạt ≥ mức "đạt yêu cầu" trên rubric**

**Checklist theo dõi:**

| Hạng mục | Hoàn thành | Ghi chú |
|---|---|---|
| 8-10 ca mock đã chạy | | |
| Ca troubleshoot khó (3 ca) | | |
| Ca complaint/sensitive | | |
| Ca escalate đúng lúc | | |
| Test cuối tuần pass | | |

---

## TUẦN 7 — Shadow + supervised live chat

**Mục tiêu:** tiếp xúc chat thật, có người đỡ ngay bên cạnh.

**To-do:**
- [ ] 2 ngày đầu: ngồi shadow CS senior xử lý chat thật, ghi chú lại cách xử lý/cách hỏi khách
- [ ] 3 ngày sau: tự trả lời chat thật, nhưng **mentor duyệt nội dung trước khi gửi** cho khách
- [ ] Cuối mỗi ngày, mentor review nhanh 15 phút: hôm nay có gì làm tốt, có gì cần sửa

**Test cuối tuần:** không có bài test riêng — đánh giá bằng số lượng chat xử lý đúng/tổng số chat trong tuần (mentor track)

**Checklist theo dõi:**

| Ngày | Số chat xử lý | Số chat cần sửa trước gửi | Vấn đề lặp lại |
|---|---|---|---|
| 1-2 (shadow) | | | |
| 3 | | | |
| 4 | | | |
| 5 | | | |

---

## TUẦN 8 — Solo có giám sát

**Mục tiêu:** tự chạy độc lập, mentor review sau (không chặn trước) để đo phản xạ thật.

**To-do:**
- [ ] Tự xử lý chat/ticket thật cả tuần, không cần duyệt trước
- [ ] Mentor review lại toàn bộ chat trong ngày (sau giờ), chấm theo `playbooks/qa-weekly-rubric.md` (Mindset/Knowledge/Skill)
- [ ] Feedback 1-1 mỗi cuối ngày hoặc cách ngày, tùy khối lượng lỗi phát sinh

**Test cuối tuần:**
- Tổng hợp điểm QA rubric cả tuần — **Pass = điểm QA trung bình đạt mức chuẩn CS chính thức** (theo `qa-policy.md`)

**Checklist theo dõi:**

| Hạng mục | Hoàn thành | Điểm QA trung bình | Ghi chú |
|---|---|---|---|
| Số chat/ticket xử lý trong tuần | | | |
| Lỗi lặp lại cần train thêm | | | |
| Đạt chuẩn QA rubric | | | |

---

## TUẦN 9 — Final assessment + go-live

**Mục tiêu:** chốt go/no-go cho làm việc độc lập chính thức.

**To-do:**
- [ ] Ôn lại các điểm yếu đã note từ tuần 1-8
- [ ] Review lại 50 case FAQ (Phần 3) lần cuối — tập trung domain còn yếu

**Test cuối tuần (final, mentor + Liz cùng chấm):**
- Bài test tổng hợp: 10 câu hỏi product (như final test Learn Joy) + 5 case phân loại/escalate + 3 ca mock chat troubleshoot mới
- Review toàn bộ QA score 2 tuần live (tuần 7-8)
- **Pass = đạt đủ 3 điều kiện trên** → go-live độc lập chính thức. Không đạt → gia hạn thêm 1 tuần vào đúng module còn yếu (không lặp lại toàn bộ plan).

**Checklist theo dõi:**

| Hạng mục | Đạt | Ghi chú | Ký duyệt go-live (Liz) |
|---|---|---|---|
| Test product (điểm/10) | | | |
| Test process/escalate (điểm/5) | | | |
| Mock chat troubleshoot (3 ca) | | | |
| QA score tuần 7-8 đạt chuẩn | | | |
| **Quyết định go-live** | | | |

---

## Ghi chú co giãn 8-10 tuần

- **Rút còn 8 tuần:** gộp tuần 7+8 (shadow → solo giám sát trong cùng 1 tuần) nếu trainee đã có kinh nghiệm CS chat trước đó.
- **Giãn thành 10 tuần:** tách tuần 9 (final assessment) thành 2 tuần nếu QA tuần 8 chưa đạt chuẩn — thêm 1 tuần "solo có giám sát" nữa trước khi test final.
- Tiêu chí pass/fail mock chat (tuần 6) và final assessment (tuần 9) hiện dùng khung `qa-weekly-rubric.md` — nếu Liz muốn tiêu chí riêng cho onboarding (khác QA định kỳ), báo để mình tách riêng.
