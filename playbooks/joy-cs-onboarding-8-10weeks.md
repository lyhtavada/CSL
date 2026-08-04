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

**Câu hỏi (điền câu trả lời vào bảng — nguồn: bộ test chính thức "CS Training: Joy Test"):**

| Question | Answer |
|---|---|
| What are the main benefits of Joy Loyalty app? | |
| What are the current supported plans and their price accordingly? | |
| What is Customer account in Shopify? How many types of customer accounts are there? | |
| How to enable Customer Accounts in Shopify? | |
| How does an Order differ from a Transaction? | |
| Name 1-2 key differences between Joy and its main competitors? | |
| Which plan is "Pro" the old name for? How many days is the trial for each plan, and how many times can it be applied per store? | |

## Earning programs

**Đọc:** [help.joy.so/reward-programs](https://help.joy.so/reward-programs/) — mục Earning programs (orders, sign-ups, birthdays, reviews, surveys, social, custom)

**Thực hành:**
- Set up Place order với cả 3 rate option: per amount spent / per item / per order
- Thêm: sign-up, social, review, birthday, custom program
- Đặt 1 order thật → xem điểm vào đúng chưa
- Test points multiplier/rate khác nhau theo tier

📎 **Kết quả/Proof:**

**Case thật (TS Elite):** tra case earning/birthday qua `crisp-chat`/`agent-activity`

**Câu hỏi (điền câu trả lời vào bảng — nguồn: bộ test chính thức):**

*Place Order:*

| Question | Answer |
|---|---|
| Can the names of programs be translated/changed? | |
| When are points for place order programs added? When are they deducted? | |
| How many free orders per month are there in the Free plan? | |
| Can we limit the number of times each customer can earn points by placing orders? | |
| How do the 'Earn points by amount spent' and 'Earn points by order placed' settings differ? | |
| Can we include products that can earn points by certain conditions? | |

*Sign Up:*

| Question | Answer |
|---|---|
| Differentiate between signing up and signing up for the newsletter. | |
| How to add points automatically for customers who signed up before the program's launch? | |

*Write Review:*

| Question | Answer |
|---|---|
| How many review apps are supported with the write reviews program? | |
| What are the conditions for a customer to receive points when leaving a review? | |
| 📹 Make a screen recording of a successful write review activity using Air Reviews | |

*Birthday Program:*

| Question | Answer |
|---|---|
| How are the birthdays collected? | |
| 📸 Insert a screenshot of the birthday reward from the widget | |
| When and how will customer receive the birthday reward? | |

*Social Programs:*

| Question | Answer |
|---|---|
| When do customers receive points for social programs? | |
| How many times can a customer earn points by following TikTok? | |

## Redeeming programs

**Đọc:** [help.joy.so/reward-programs](https://help.joy.so/reward-programs/) — mục Redeeming programs (discounts, free gifts, shipping, checkout redemption, limits)

**Thực hành:**
- Tạo đủ: discount amount, discount %, BXGY, free gift, free shipping
- Đặt total + per-customer redemption limit → test khi chạm limit
- Redeem bằng customer test → soi coupon code sinh ra (one-time-use)

📎 **Kết quả/Proof:**

**Case thật (TS Elite):** tra case redeem/coupon qua `crisp-chat`/`agent-activity`

**Câu hỏi (điền câu trả lời vào bảng — nguồn: bộ test chính thức):**

*Discount program:*

| Question | Answer |
|---|---|
| How does a Dynamic discount amount differ from a Fixed discount amount? | |
| Is it possible to set an expiration time for the discount? | |
| What happens when a customer redeems a reward? | |
| Can we create multiple redeem programs for the same type (percentage discount for example)? | |
| Which redeeming programs are available on All plans, which are Essential+, and which require Ultimate + Plus + Checkout Extensibility? | |
| Can the coupon generated from redeeming be reused? Why or why not? | |
| 📹 Make a screen recording of a successful redeeming activity | |

*Free shipping / Free product / Discount combination:*

| Question | Answer |
|---|---|
| What does "Exclude shipping rates over a certain amount" mean? | |
| How many products can you add to 1 Free product program? | |
| How many ways can the discounts be combined? List all of them. | |
| In order to use an order discount code in combination with a shipping discount code, what condition must be met? | |
| Can we combine Joy discount with other discounts in Shopify? | |
| Can discounts be combined for in-store purchases? | |

*Point Expiration:*

| Question | Answer |
|---|---|
| What is the purpose of setting a points expiration period? | |
| How is the expiration time for points calculated? | |
| What happens if customers don't earn or redeem points within the specified custom period? | |
| Is discount code's prefix customizable in Joy? | |

*Store Credit reward:*

| Question | Answer |
|---|---|
| How does a customer actually receive a Store Credit reward — do they get a discount code to enter at checkout? | |
| Which programs can trigger a Store Credit reward for a customer? | |
| What is the key difference between redeeming Store Credit and redeeming Points for a coupon? | |
| A merchant says a customer was told they received store credit, but nothing shows up in their Shopify account — what should you check first? | |
| A merchant needs to bulk-credit ~300 customers due to a system error — what's the fastest way to do this in Joy? | |

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

📎 **Kết quả/Proof:** (link/screenshot dev store đã điền ngay trong cột bảng trên)

**Case thật (TS Elite):** tra case widget/loyalty page qua `crisp-chat`/`agent-activity`

**Câu hỏi (điền câu trả lời vào bảng — nguồn: bộ test chính thức):**

*Widget Design (Branding):*

| Question | Answer |
|---|---|
| Is it possible to change the position of the content blocks in the widget? | |
| What is "Instant popup for widget" for? | |
| In what scenario is a custom login link used? | |
| What happens to the visibility of the loyalty widget if the "Display widget after login" feature is turned off? | |
| A merchant reports "the widget isn't showing" — list ≥4 causes in the correct troubleshooting order. | |
| How does New Customer Accounts differ from Legacy, and how does it affect the account page? | |

*Point Calculator / Signup Block / Visit website pop-up:*

| Question | Answer |
|---|---|
| Which plan supports the Point calculator? Can it be shown on the checkout page? | |
| 📸 Add the point calculator to your store and take a screenshot | |
| What is the Sign up block? 📸 Insert a screenshot of it | |
| What is the purpose of the visit website popup, and what message does it convey to customers? 📸 Share a screenshot of it | |

*Embedded Content / Loyalty page:*

| Question | Answer |
|---|---|
| What is the Embedded content feature for? | |
| Will customers be able to earn or redeem points via the loyalty page? | |
| What are the loyalty blocks supported on the Loyalty page? | |
| Can merchants insert a link to each loyalty block on the page? If yes, how? | |
| Is it possible to create a loyalty page including the Loyalty blocks if the theme is not standard 2.0? | |
| How does the loyalty page differ from the widget (section vs app embed)? | |
| 📹 Make a screen recording of creating and adding the loyalty page to your store | |

## VIP tiers + Milestone + Referral (troubleshoot sâu)

**Đọc:** Module 3 phần *VIP tiers* (đặc biệt "VIP tier hoạt động end-to-end" + "Troubleshooting VIP tier") + [help.joy.so/membership](https://help.joy.so/membership/) (VIP tiers), [help.joy.so/reward-programs/milestone](https://help.joy.so/reward-programs/milestone/), [help.joy.so/reward-programs/referrals](https://help.joy.so/reward-programs/referrals/)

**Thực hành:**
- Tạo 3 tier + entry condition + reward mỗi tier + earning rate khác nhau theo tier
- Nhấn Launch, quan sát banner "Calculating Customer Tiers" — hiểu 3 bước hệ thống chạy ngầm: (1) recalc tier trên Joy, (2) sync metafield sang Shopify, (3) sync tag sang Shopify
- Đẩy customer test lên tier 2 → check tag + metafield `avada_joy.vipTier` trên Shopify customer, không chỉ nhìn trong app
- Set 1 milestone
- Chạy full referral: lấy link → mở incognito → đăng ký → mua → check reward 2 đầu; đọc qua các anti-cheat (self-referral, cùng IP/email)

📎 **Kết quả/Proof:**

**Case thật (TS Elite):** tra case VIP tier/referral qua `crisp-chat`/`agent-activity` — ưu tiên tìm case "tier đúng nhưng không nhận perk" để đối chiếu

**Câu hỏi (điền câu trả lời vào bảng — nguồn: bộ test chính thức + Module 3):**

*VIP Tiers & Membership:*

| Question | Answer |
|---|---|
| What is the purpose of setting up a VIP Tier in a loyalty program? | |
| How are the tiers calculated? | |
| What is Entry reward? When does a customer receive an Entry reward, and how often can they receive the achieved reward? | |
| Is it possible to customize the VIP discount code prefix? How? | |
| How many ways can the VIP tiers be reset automatically? | |
| Can you give different amounts of points for different tiers for the same spent amount? | |
| What are privileges? How does it work? On which plans is the feature available? | |
| Which types of privileges are offered at the moment? | |
| Can you combine an Entry reward discount code with a Privilege discount code? | |
| What can you do to customers' tier if they have not made a purchase for a period of time? | |
| What is a Member exclusive deal (MED)? You've set up the MED, but it doesn't show on the store — what would you check? | |

*Milestone:*

| Question | Answer |
|---|---|
| What are milestone rewards in the Joy Rewards & Loyalty Program? | |
| How can I set up milestone rewards for my customers? | |
| Is it possible to set up multiple milestone rewards for different achievements? | |
| Can I customize the rewards given for each milestone? | |
| What happens if a customer reaches a milestone but then returns an item that contributed to that milestone? | |
| How does a milestone differ from a VIP tier? | |

*Referral:*

| Question | Answer |
|---|---|
| When is a referral considered successful? | |
| 📹 Make a screen recording of a successful referral | |
| How many referral links are there in the free plan? | |
| What is Shopify order tagging used for in referrals? | |
| If the discount text of the referral popup doesn't match the referral reward settings, where can you edit it? | |
| Why might a referral "not work"? Name the common causes. | |

*Troubleshoot VIP tier (this is the #1 ticket group CS runs into — memorize this order):*

| Question | Answer |
|---|---|
| Why doesn't "the tier being correct in the app" guarantee that "the perk works"? | |
| List, in the correct order, the 6 troubleshooting steps when a merchant reports "wrong tier/perk". | |
| Why should multiple symptoms ("wrong tier", "perk not received", "wrong earn") after one bad launch/migration be merged into a single ticket instead of split into 2-3 separate tickets? | |
| When should you actually escalate a tier/perk issue to dev, and what evidence should you attach? | |

**Test giữa chặng (30 phút, sau khi xong nhóm Pricing → VIP tiers):** mentor đưa 5 câu hỏi merchant thật → CS trả lời bằng lời + chỉ đúng path trong admin. Bắt buộc có 1 câu về troubleshoot VIP tier.

---

## Customers + Points management + Migration (dev zone)

**Đọc:** Module 3 phần *Migration and import* (đọc kỹ — nhiều cạm bẫy) + [help.joy.so/customers](https://help.joy.so/customers/), [help.joy.so](https://help.joy.so/) mục Support → Migration (từ Stamped, Smile, Rivo, Yotpo, others)

**Thực hành:**
- Adjust điểm thủ công 1 customer (cộng/trừ) → xem transaction history
- Vào **dev zone → Enable feature migration** — hiểu từng control: "shop đang migrate" (tránh side-effect bắn nhầm email/webhook), nút **Recalculate** (quét lại order Shopify tính amount-spent — dùng khi KH CÓ orders trên Shopify), **Has migrate tier points** (bật mới migrate được cột Tier points)
- Tự chạy thử 1 lần migrate: import balance điểm (cột Points balance) + migrate VIP tier theo tên + **thêm cột Tier points vào file rồi map ở bước Match** (không bị giới hạn theo file mẫu)
- Import điểm bằng CSV, export customer list

📎 **Kết quả/Proof:**

**Case thật (TS Elite):** tra case customers/migration/points qua `crisp-chat`/`agent-activity`

**Câu hỏi (điền câu trả lời vào bảng — nguồn: bộ test chính thức):**

*Customers:*

| Question | Answer |
|---|---|
| How can customers be imported into the app? | |
| What are the types of customers in Joy? | |
| What are the ways to manually add or deduct points? | |
| How many types of import actions are there? Explain the differences. | |
| How to find a customer in the app? | |
| How to exclude a member from the program from the merchant's (MC's) end? | |

*Migration:*

| Question | Answer |
|---|---|
| What types of customer data can Joy Loyalty migrate during the transition from another loyalty program? | |
| How does Joy Loyalty ensure that point balances and VIP tier statuses remain intact during data migration? | |
| Which loyalty apps have step-by-step migration guides available for transitioning to Joy Loyalty? | |
| Differentiate between the Migration wizard (dev zone) and Import → Update tier (Customers page)? | |
| For tiers based on POINTS, how should you migrate? For tiers based on AMOUNT SPENT with existing orders on Shopify, which method should you use? | |
| After import, what state are customers usually in? What should you confirm with the merchant before launching? | |
| If the tier name data is inconsistent/misspelled, which tier does the customer fall back to? | |

*Rule engine (Advanced plan and above):*

| Question | Answer |
|---|---|
| What is the main purpose of the Advanced rule engine? | |
| Explain the impact of the "Stop Further Rule Processing" feature on how rules are applied. How would you decide whether to enable or disable it for a store? | |
| Example: one rule gives 10 points per $50 spent, another gives 20 points during a holiday sale — how would you set priority/criteria so both work as intended? | |
| If you wanted to target customers in specific VIP tiers who live in certain cities, how would you configure the Rule Engine criteria? Give an example. | |
| How do Anti-Cheat features help maintain the integrity of a loyalty program? How would you set earning limits and handle canceled/refunded orders? | |
| Is "unlimited transactions" a pricing matter? How should you handle it? | |

## Notifications + Email + Translations

**Đọc:** [help.joy.so](https://help.joy.so/) mục Operations → Notifications, Settings (email), [help.joy.so/translations](https://help.joy.so/translations/)

**Thực hành:**
- Bật + sửa nội dung 3 email notification, gửi test về mail mình
- Set sender email + domain authentication
- Dịch widget + loyalty page sang 1 ngôn ngữ thứ 2, test đổi ngôn ngữ trên storefront

📎 **Kết quả/Proof:**

**Case thật (TS Elite):** tra case notification/email/translation qua `crisp-chat`/`agent-activity`

**Câu hỏi (điền câu trả lời vào bảng — nguồn: bộ test chính thức):**

| Question | Answer |
|---|---|
| Name all the types of notifications Joy sends + the trigger for each. | |
| Where to change the email sender of Joy notifications? | |
| A merchant reports "customers aren't receiving emails" — what order should you check things in? | |
| Can I translate all parts of the widget contents, including buttons and error messages? | |
| How do I change the default language for the widget contents? | |
| What happens if I do not translate some parts of the widget contents? | |
| Will the translated widget contents automatically update if I change the default language text? | |

## Integrations + POS + Checkout extensions + Joy AI

**Đọc:** Module 3 phần *Integrations* + *Setup checkout, thank you page extensions* + *Setup POS* + [help.joy.so](https://help.joy.so/) mục Operations → Integrations, [help.joy.so/pos](https://help.joy.so/pos/), [help.joy.so/joy-ai](https://help.joy.so/joy-ai/)

**Thực hành:**
- Nối 1 integration thật (Klaviyo hoặc review app) → xem data chảy qua
- Đọc kỹ POS: điều kiện, giới hạn, plan nào có; biết auto-discount tier **không chạy ở POS**
- Đọc checkout extensions (chỉ Plus, 1 ngôn ngữ) — quick redeem, point calculator, coupon list, sign-up block
- Thử Joy AI, hiểu nó làm được gì

📎 **Kết quả/Proof:**

**Case thật (TS Elite):** tra case integrations/POS qua `crisp-chat`/`agent-activity`

**Câu hỏi (điền câu trả lời vào bảng — nguồn: bộ test chính thức):**

| Question | Answer |
|---|---|
| What plan of Judge.me is required to integrate the Joy app with Judge.me? | |
| What is the purpose of integrating Joy with Klaviyo? | |
| What is the primary function of the Joy Shopify Flow Integration? | |
| Why might Shopify Flow not work with review apps? | |
| How to show customer points on "My account page"? | |
| What should you check if no program is available to redeem for a customer added in POS? | |
| 📹 Make a screen recording of a successful redeem activity in POS | |
| What is the POS limitation related to VIP tier auto-discount? | |
| Who are checkout extensions available for? | |
| Which integrations require Shopify Plus? | |

## Settings nâng cao + Point calculator + Analytics + Launch live

**Đọc:** Module 3 phần *Point calculators* + *Launch from sandbox mode to live mode* + *Xem số liệu report* + [help.joy.so/analytics](https://help.joy.so/analytics/), [help.joy.so](https://help.joy.so/) mục Operations → Settings, mục Customers (wallet pass)

**Thực hành:**
- Set order settings (điểm khi refund/cancel — hay gây tranh cãi)
- Bật point calculator ở product page + cart drawer (bật app embed calculator, thêm snippet `<div class="joy-points-calculator__block"></div>` vào liquid nếu theme tự render lại cart bằng innerHTML thì gọi `avadaJoyRerenderAllCalculators()`)
- Đọc Analytics dashboard — hiểu **assisted revenue** và **redemption rate** nghĩa là gì, nói được merchant nên nhìn số nào
- Thực hành **Launch from sandbox → live mode** — hiểu đây là bước quan trọng cuối cùng để điểm bắt đầu ghi nhận thật
- Tạo wallet pass, thử xin collaborator access vào 1 store test

📎 **Kết quả/Proof:**

**Case thật (TS Elite):** tra case order/refund/analytics qua `crisp-chat`/`agent-activity`

**Câu hỏi (điền câu trả lời vào bảng — nguồn: bộ test chính thức):**

| Question | Answer |
|---|---|
| What is the "Show metafields on Shopify admin" feature in Joy for? | |
| How are points handled when an order is refunded/canceled? | |
| What do "assisted revenue" and "redemption rate" mean, and which numbers should a merchant look at? | |
| If the point calculator doesn't automatically show in the cart drawer, how do you fix it (snippet + rerender function)? | |
| What does the flow of switching from sandbox mode to live mode involve? | |

## Tổng ôn + Final test

**Thực hành (3h) — build store hoàn chỉnh trên dev store mới, tính giờ:**
1. Cài Joy từ đầu, bật customer accounts, chọn Legacy hoặc New có chủ đích
2. Chương trình: earning (place order + sign-up + birthday + referral) + redeeming (discount + free shipping + free gift)
3. 3 VIP tier với earning rate khác nhau, launch và verify tag/metafield đã sync sang Shopify
4. Loyalty page + widget V4 (branding cơ bản) + onsite content ở product page & cart + point calculator ở cart drawer
5. Notification bật + branding + dịch 1 ngôn ngữ 2
6. Import 10 customer kèm điểm bằng CSV/migration wizard
7. Launch từ sandbox sang live, test end-to-end bằng customer thật: đăng ký → mua → lên tier → redeem → dùng coupon

📎 **Kết quả/Proof:** link dev store hoàn chỉnh + screenshot/video từng bước 1-7

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
- [ ] Đọc Notion **[Joy Loyalty — Khách hàng & ICP](https://app.notion.com/p/avadagroup/3b2b0da449f180ccb42ad4230ef21eb2)** — biết Joy bán cho ai, vì sao, và nhận ra một merchant có phải khách của mình không, TRƯỚC khi học quy trình xử lý ticket bên dưới
- [ ] Đọc toàn bộ process docs trong Notion **[Joy Process](https://www.notion.so/avadagroup/Joy-Process-280b0da449f1800098c4f194260f387f)** (nguồn chính thức, cập nhật liên tục — không copy vào repo vì dễ lỗi thời):
  - [1 số lưu ý về escalation ở Joy Loyalty](https://www.notion.so/280b0da449f1802b81a9e4427967d507)
  - [Joy live chat flow - Demo store](https://www.notion.so/294b0da449f18057b0b0df5d5efdfac6)
  - [Joy - CS Onboarding Flow](https://www.notion.so/397b0da449f18085b2aaf0b4c0e71e79)
  - [Joy DFY — Why We Do This](https://www.notion.so/366b0da449f1807fa17cd92df95b8d6f)
  - [Joy DFY — How We Do This](https://www.notion.so/366b0da449f180878b99d78c19ab9143)
  - [Joy DFY - Best practices](https://www.notion.so/37bb0da449f18074b03df9a48832e6d7)
- [ ] Tự phân loại thử 10 case mẫu (mentor đưa) theo đúng case-classification + escalation matrix
- [ ] Viết thử 1 escalation note mẫu theo đúng format

📎 **Kết quả/Proof:**

**Câu hỏi (điền câu trả lời vào bảng — verify CS đã nắm process, không chỉ đọc lướt):**

*Khách hàng & ICP:*

| Question | Answer |
|---|---|
| ICP chính của Joy là merchant quy mô bao nhiêu đơn/tháng? Kể 1-2 dấu hiệu merchant "khỏe" (dễ trả tiền, ở lại lâu)? | |
| "Plus Poster" là gì, khác ICP chính (mid-market) ở điểm nào — đo bằng gì? | |
| Kể 2-3 nhóm KHÔNG phải khách của Joy | |

*Escalation:*

| Question | Answer |
|---|---|
| Issue liên quan App Functionality escalate lên nhóm Slack nào, tag PIC chính là ai? | |
| Request về giá cả/demo call/discount/trial extend escalate lên nhóm nào, tag ai? | |
| CS có được tự tư vấn giá/plan/discount cho khách không? Vì sao? | |

*Joy live chat flow — Demo store:*

| Question | Answer |
|---|---|
| Chat từ demo website tự động gắn tag gì? | |
| Liệt kê 4 nhóm khách CS cần phân loại nhanh khi chat ở demo store. | |
| Với nhóm Potential Lead, CS cần verify điều gì trước khi mời demo call/gửi link install? | |
| Với nhóm Existing User vào demo test, mục tiêu hỗ trợ là gì, và bước cuối cần làm gì nếu phát hiện issue? | |

*Joy - CS Onboarding Flow (chat thao tác, không phải playbook lý thuyết):*

| Question | Answer |
|---|---|
| CS offer onboarding khi nào (2 điều kiện eligibility)? | |
| Nguyên tắc "1 ticket onboarding chính/KH" nghĩa là gì — ngoại lệ duy nhất là gì? | |
| Phân biệt nhanh 3 nhóm nhánh A (Migrate)/B (Rebuild)/C (First-time) dựa vào 3 câu discovery nào? | |
| Nhóm A (migrate) là "chỗ dễ vỡ nhất" — CS cần xác nhận điều gì trước khi import? | |
| Khi issue phát sinh lúc onboard (không cộng điểm, coupon invalid...), CS xử lý theo thứ tự nào — có tách ticket mới không? | |
| Nêu nguyên tắc ownership khi bàn giao ca (hết ca nhưng case chưa xong)? | |

*Joy DFY (Why/How/Best practices — white-glove widget service):*

| Question | Answer |
|---|---|
| Điều kiện eligibility để tạo ticket DFY (2 điều kiện đồng thời)? | |
| SLA bắt buộc từ lúc tạo ticket DFY đến khi có kết quả báo khách là bao lâu? | |
| Kể tên 3 level checklist DFY (Required/Recommended/Bonus) — ý nghĩa "level cao hơn bao gồm level dưới" là gì? | |
| Sau khi gửi kết quả, CS cần follow-up lại sau bao lâu, và gắn label gì tùy kết quả (adopt/no-adopt)? | |
| Nguyên tắc quan trọng nhất khi customize content: khi nào được sửa TRỰC TIẾP trên store KH, khi nào chỉ được đề xuất qua email? | |


---

## TUẦN 5 — Đọc Crisp + luyện case thật

**Mục tiêu:** đọc hiểu context 1 cuộc chat thật trên Crisp, tra đúng case trong 50 case FAQ.

**To-do:**
- [ ] Đọc `skills/read-crisp/SKILL.md` — cách đọc/tóm tắt 1 session Crisp
- [ ] Mentor gửi 10 link chat Crisp thật (đã xử lý xong) → trainee tự đọc, tóm tắt lại vấn đề + cách CS cũ xử lý, KHÔNG xem trước đáp án
- [ ] Với mỗi case, tự tra ngược trong 50 case (Phần 3 playbook) xem case đó rơi vào domain nào, đúng lăng kính 🟢🔵🟠🔴 nào
- [ ] Ghi lại 5 case mình thấy khó nhất → hỏi mentor

📎 **Kết quả/Proof:** (tóm tắt 10 case đã đọc)

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

📎 **Kết quả/Proof:** (transcript/ghi âm các ca mock + feedback mentor)

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

📎 **Kết quả/Proof:** (link ticket/chat đã xử lý mỗi ngày)

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

📎 **Kết quả/Proof:** (link chat/ticket + điểm QA từng ngày)

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

📎 **Kết quả/Proof:**

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
