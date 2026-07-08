# Joy Loyalty — Onboarding Flow & Decision Guide

**Owner:** Liz (CS Leader)
**Created:** 2026-07-07 · **Updated:** 2026-07-08
**Status:** v2 — gộp quy trình 7 bước (có exit-criteria) + decision guides. FAQ tra cứu tách sang [`joy-support-flow.md`](../kb/cs-process/joy-support-flow.md).

> **File này là gì.** Sổ tay vận hành onboarding một merchant Joy Loyalty — từ lúc nhận khách tới lúc launch. KHÔNG dạy lại product (kiến thức product ở KB LIVE `cs2.avada.net`). Khách **báo lỗi/hiện tượng cụ thể** → tra [`joy-support-flow.md`](../kb/cs-process/joy-support-flow.md) (FAQ 50 case theo domain).
>
> Khác gì với [`joy-dfy-flow.md`](./joy-dfy-flow.md)? DFY thiên về **làm hộ widget + đẩy go-live** cho store gần xong. **Onboarding flow này** dành cho KH **Advanced+** cần **build cả loyalty program từ đầu** (earning / redeeming / VIP / member-guest / migration / import) — có intake sâu, checklist chuẩn, 1 kế hoạch sống/KH xuyên suốt.

**Nền tảng dữ liệu.** Rút từ phân tích 3 tháng ticket Joy (1.164 ticket phân loại semantic + 379 thread dev — `docs/joy-ticket-analysis-q2-2026.md`). Con số phải nhớ: **51% ticket đã escalate lên dev hóa ra KHÔNG phải bug Joy** — mà là config sai, hành vi đúng-thiết-kế bị hiểu nhầm, lỗi 3rd-party, hoặc data-fix một lần. → Nhiệm vụ CS: **tự chẩn đoán để lọc 51% đó**, không đẩy hết lên dev.

---

## Nguyên tắc vàng (đọc trước)

1. **Chuẩn hơn nhanh.** Giá trị của onboard KHÔNG nằm ở "thấy widget nhanh" mà ở **Time-to-value SAU khi khách launch**. Setup vội để rồi launch xong không có gì chạy = thất bại, dù widget đẹp.
2. **Hỏi trước, làm sau.** Không nhận yêu cầu lẻ ("migrate hộ", "import hộ") rồi làm ngay mà chưa hiểu bức tranh tổng. Yêu cầu lẻ luôn quy về plan tổng.
3. **1 khách = 1 kế hoạch, không phải nhiều ticket rời.** Một lần onboard gom vào **một** ticket sống có checklist, không xé thành 5 ticket lẻ.
4. **Nhận là own tới cùng.** (Xem rule Ownership & SLA cuối Phần 1.)
5. **Dùng AI chat nhiều hơn.** Câu hỏi chẩn đoán (KH này guest hay member, order này vì sao không earn, coupon điều kiện thật là gì) → **hỏi Joy AI agent trước** — nó đọc được state, nhanh hơn mò tay hoặc đẩy dev.

---

# 🧭 Phần 1 — Quy trình chuẩn (7 bước, mỗi bước có exit-criteria)

> Chỉ qua bước sau khi đạt exit-criteria. Đây là bản nâng cấp của decision tree cũ — tree A/B/C nằm ở **Bước 1** (phân nhánh khi lập plan).

### Bước 0 — Intake: hỏi plan Loyalty của khách TRƯỚC KHI làm gì

Bước hay bị bỏ nhất, và là gốc của phần lớn rework. Trước khi động vào app, hỏi & ghi lại:

- **Mục tiêu:** giữ chân (retention), tăng AOV, hay referral? Ngành hàng gì (margin cao/thấp)?
- **Chương trình tính theo gì:** **points-based** hay **amount-spent**? (quyết định cách setup VIP tier — xem [§2.2](#22-vip-tier)).
- **Khách mới hay đang chuyển sang:** làm loyalty lần đầu, hay **migrate** từ app/platform khác? Nếu migrate → từ đâu (Smile.io, LoyaltyLion, platform ngoài Shopify…)?
- **Tài khoản khách:** đang dùng **Legacy** hay **New Customer Accounts (NCA)**? (ảnh hưởng customize + guest/member — xem [§2.3](#23-guest-vs-member)).
- **Tích hợp bắt buộc:** Klaviyo/Omnisend? Review app (Judge.me/Loox/Yotpo)? Subscription (Recharge)? POS?

**Câu offer mở đầu (trong chat):**
> *"Hi [name], I noticed you're on our Advanced plan — I'd love to help you get your loyalty program set up properly so it's ready to launch. Would you like me to walk through it with you and set things up together?"*

**Discovery 3 câu (đừng hỏi dồn 1 lúc):**
1. **Launch timeline:** *"When are you planning to launch your loyalty program?"*
2. **Kinh nghiệm trước đó:** *"Have you run a loyalty program before — either on another app or store?"*
3. **(Nếu có) Migration:** *"Are you moving over from another loyalty app? If so, do you already have your customer/points data exported?"*

**Exit-criteria:** có bản tóm tắt yêu cầu, **khách đã xác nhận** đúng ý.

### Bước 1 — Lập plan gộp cho khách (offer trước) + phân nhánh A/B/C

Từ intake, viết ra **một** checklist onboarding cho khách này (không tách ticket lẻ). Chủ động **offer trước** các việc sẽ làm — đặc biệt hai chỗ app hay "trigger" nhiều thao tác: **import** và **migrate**. Khách biết trước lộ trình → ít ticket phát sinh giữa chừng.

**Decision tree — phân nhánh theo tình huống KH:**
```
KH mới ở Advanced
        │
        ├── A. MIGRATE từ app loyalty khác sang
        │        ├── A1. Đã có detailed plan  → xin KH gửi plan → CS review + setup theo → test
        │        └── A2. Chưa có plan rõ       → gửi checklist Google Sheet → KH điền rule
        │                                          (KH chưa biết → hướng dẫn dùng AI agent trong app)
        │        + Luôn hỏi 3 câu migration (§2.1): từ đâu / point vs amount / file vs sync
        │
        ├── B. ĐÃ dùng loyalty trước (không migrate app / build lại từ đầu)
        │        ├── B1. Đã có plan/rule sẵn   → gửi CS → CS review + setup giúp → test
        │        └── B2. Chưa có plan rõ       → gửi checklist Google Sheet → KH điền
        │
        └── C. CHƯA từng dùng loyalty bao giờ
                 → CS gợi ý preset theo ngành/AOV
                 → hỗ trợ KH dùng AI agent trong app (đọc AOV, industry…) đề xuất rule
                 → chốt rule → CS setup → test
```
Checklist Google Sheet (KH điền rule) → template ở [`joy-onboarding-program-checklist.md`](./joy-onboarding-program-checklist.md). CS clone 1 sheet/KH → KH điền → paste link vào field "Detail program" của ticket chính.

**Exit-criteria:** khách nắm được các bước và mốc thời gian.

### Bước 2 — Xin quyền (scopes)

Đề nghị khách **grant thêm scopes** cần thiết. Ngoài để app chạy đủ tính năng, extra scopes còn giúp **AI report/diagnostic đọc được nhiều state hơn** → chẩn đoán tốt hơn về sau.

**Exit-criteria:** scopes đã cấp đủ.

### Bước 3 — Setup (theo Module 3 / KB LIVE)

Thực hiện setup: currency, earn/redeem, widget, loyalty page, tiers, integrations, notifications. Chỗ nào vướng → tra Phần 2 (guide) hoặc [`joy-support-flow.md`](../kb/cs-process/joy-support-flow.md) (FAQ).

**Nhắc:** làm trên **theme test** (duplicate theme riêng cho rewards, sửa ở preview mode) + bật **Sandbox Mode** để test không đụng data thật.

**Mức can thiệp theo plan** (đụng logic điểm & tiền của KH):

| Plan | Earning / Redeeming | Widget & Touchpoints |
|------|---------------------|----------------------|
| **Starter / Essential** | CS **review + đề xuất** rule, KH tự enable. Có thể bật giúp preset an toàn (signup, place order) nếu KH đồng ý trong chat. | CS setup trực tiếp |
| **Advanced trở lên** | CS **setup full thay KH** theo preset, hoặc forward TS nếu phức tạp (tiers, custom rules, expiration). CS loop verify. | CS setup trực tiếp / forward TS |

> **Luôn:** không tự đổi giá trị điểm/tiền của rule đang chạy — chỉ đề xuất. Chỉ setup mới rule còn trống.

**Exit-criteria:** chương trình đã cấu hình xong trên Sandbox/theme test.

### Bước 4 — Test cho khách (đừng bỏ bước này) ⭐

Bước **thường xuyên bị thiếu**. Trước khi launch, phải **test thật** trên Sandbox và cho khách thấy:
- Earn: đặt đơn test → điểm vào đúng.
- Redeem: đổi điểm → coupon sinh ra và apply được.
- VIP tier (nếu có): khách rơi đúng tier, perk apply.
- Widget/loyalty page hiển thị đúng brand.

**Exit-criteria:** **khách đã xem và xác nhận** luồng chạy đúng.

### Bước 5 — Launch: Sandbox → Live 🚀

Bước cuối để chương trình bắt đầu cộng điểm **thật**. **Rất quan trọng, phải confirm rõ với merchant** đây là lúc "bật thật". Merchant cần: tắt Sandbox → Live, và bật app trên theme chính (hoặc publish theme test lên chính) để widget hiện ra ngoài.

**Exit-criteria:** program ở **Live mode**, widget hiện trên storefront thật.

### Bước 6 — Report & handoff

Chỉ cho khách chỗ xem số liệu (**assisted revenue**, **redemption rate**) và bàn giao. Giải thích ngắn các chỉ số để khách tự theo dõi.

**Exit-criteria:** khách biết đọc report, đã handoff.

---

## ★ Rule Ownership & SLA (chat trực theo ca)

Chat trực theo ca dễ dẫn tới ticket bị bỏ dở hoặc đá qua người khác. Quy tắc:

- **Nhận là own tới cùng.** Nhận case nào chịu trách nhiệm case đó tới khi xong — kể cả phải kéo dài.
- **Hẹn rõ:** việc cần thời gian (vd import) → **hẹn khách ~1 ngày** và làm tới nơi.
- **Bàn giao ca liền mạch:** hết ca chưa xong → để lại note trạng thái đầy đủ để **ca sau nối tiếp**, không bắt khách kể lại từ đầu.
- **Không đá việc.** Không mặc định assign bạn khác "import hộ" chỉ vì hết ca — trừ khi đã bàn giao trạng thái rõ ràng và có lý do chính đáng.

---

## 🤖 Kết hợp Joy AI Agent — plan sống trên "canvas"

Checklist 7 bước không nên là giấy tĩnh — nó là thứ **Joy AI Agent vận hành được**, mỗi merchant có một **plan sống trên canvas** (artifact hiển thị cùng chat, cả CS lẫn merchant cùng thấy & cập nhật):

- **Agent chạy Intake:** hỏi plan KH + tự đọc state shop (plan, Sandbox/Live, account type, integrations đã cài, có migrate không) → điền sẵn phần lớn Bước 0.
- **Agent sinh plan gộp:** từ intake + state, tạo **đúng 1 kế hoạch** cho merchant (không ticket lẻ), đề xuất việc Bước 1.
- **Lưu trên canvas:** plan ghi lên canvas per-merchant — 7 bước, exit-criteria, trạng thái done/pending. Đây là **nguồn sự thật chung**: hết ca, ca sau mở canvas là nối tiếp (giải luôn bài toán bàn giao ở rule Ownership & SLA).
- **Agent tự theo dõi exit-criteria:** mỗi bước có tiêu chí máy đọc được (Sandbox hay Live? app embed bật chưa? đơn test đã earn? tier đã sync metafield?) → agent tự tick + nhắc bước còn thiếu, thay vì phụ thuộc trí nhớ từng bạn.

> **House rule:** đúng tinh thần *"AI agent là substrate"* (mọi feature readable/writable/explainable bởi agent) + *"AI skill per feature"*. Đề xuất skill `joy-onboarding-plan` (chạy intake → sinh & duy trì canvas plan). **API:** `POST /agent/onboarding/plan`, `GET /agent/onboarding/plan?shop=`, `PATCH /agent/onboarding/plan/step` (tick exit-criteria).

---

## Ticket structure — 1 ticket onboarding chính / KH

**Quy tắc vàng:** mỗi KH = **1 ticket onboarding sống**. Mọi issue liên quan onboarding (bug, câu hỏi, report tiến độ) → note thẳng vào **cùng thread ticket đó**. Ngoại lệ: **widget customize** → tạo ticket con riêng nhưng **insert link vào ticket chính**.

Checklist trong ticket chính:
- [ ] **Launch date**
- [ ] **Detail program** — *(paste link Google Sheet của KH)*
- [ ] **Earning / Redeeming rule** — đã chốt & setup?
- [ ] **VIP tier setup** (nếu có) — tag + metafield đã sync? ([§2.2](#22-vip-tier))
- [ ] **Migration hoặc Import** — data export chưa / import xong chưa ([§2.1](#21-migration--import))
- [ ] **Guest vs Member** — đã config phân quyền/hiển thị? ([§2.3](#23-guest-vs-member))
- [ ] **Widget customize** — *(ticket con riêng → insert link)* ([§2.5](#25-widget-v4--unified-widget))
- [ ] **Test one full loop** (earn → redeem) OK
- [ ] Get merchant OK → **switch sandbox → live** 🚀

---

# 🧩 Phần 2 — Decision guides ("hiểu tại sao")

Dành cho quyết định mà "hỏi gì làm nấy" sẽ sai. Trọng tâm: **Migration** và **VIP tier** — hai chỗ gây nhiều ticket & rework nhất.

## 2.1 Migration & Import

Chỗ hay "làm đúng cái được hỏi mà không hỏi lại" → migrate sai/lặp. **Trước khi migrate, luôn hỏi đủ 3 câu:**

**Câu 1 — Migrate TỪ ĐÂU?**
- **Từ app loyalty khác trên Shopify** (Smile.io, LoyaltyLion, Rivo…): thường chỉ mang được **balance điểm**; activities/lịch sử ít hoặc không mang. VIP tier có thể mang nhưng phải xử lý đúng.
- **Từ platform ngoài Shopify** rồi launch loyalty lần đầu: thường vừa migrate balance vừa launch chương trình mới.
- ⚠️ **Điều kiện bắt buộc:** khách được migrate **phải đã tồn tại trên Shopify**. Không có customer trên Shopify thì không gắn điểm/tier vào đâu.

**Câu 2 — Tính theo POINT hay AMOUNT?**
- **Points-based:** mang balance điểm sang.
- **Amount-spent:** thường đi kèm VIP tier theo chi tiêu. `amount-spent` **linh hoạt hơn** — chỉ cần khách có orders trên Shopify là tính được, đổi/relaunch chương trình vẫn giữ tier dễ.

**Câu 3 — FILE IMPORT hay SYNC ORDERS & LAUNCH?** (quyết định quan trọng nhất, hay bị bỏ qua)

|  | **File import (CSV)** | **Sync orders & launch** |
| --- | --- | --- |
| Cách làm | Khách gửi file điểm/tier, import raw | Bật earn theo lịch sử orders có sẵn trên Shopify rồi launch |
| Hợp khi | Chỉ có balance điểm rời từ app cũ, không map ra orders | Chương trình tính theo **amount-spent**, order đã nằm trên Shopify |
| Ưu | Nhanh, mang đúng con số app cũ | Data "thật" theo Shopify; tier/tag/metafield sinh **đúng luồng** |
| Nhược | ⚠️ **Import raw dễ bỏ qua sync tag + metafield** mà discount function đọc → perk/tier không apply (root cause cả cụm bug tier). Import nhiều lần dễ cộng đôi. | Chỉ hợp khi logic là amount-spent |

> **Quy tắc:** nếu chương trình tính theo **amount-spent**, **ưu tiên sync orders & launch** thay vì import file — vì sinh tier/tag/metafield đúng luồng, tránh cụm lỗi "perk không apply do metafield chưa sync".

**Lưu ý bắt buộc khi migrate:**
- **Tránh migrate nhiều lần** → dễ cộng đôi/gây lỗi. Migrate một lần, kiểm tra kỹ.
- **Migrate cả VIP tier:** không import tier raw. Phải đảm bảo **tag + metafield** của tier được sync (discount function đọc metafield/tag để cấp perk — thiếu là perk không apply).
- **Sau migrate, khách earn lại khi sign-up ở platform mới không?** → xác định trước để không cộng nhầm sign-up reward cho khách cũ.
- **Guest sau import:** khách import xong thường ở trạng thái **guest** ([§2.3](#23-guest-vs-member)) — phải nói rõ cho merchant, không im lặng.

## 2.2 VIP tier

**Points vs Amount-spent:** theo points cho chương trình points-based; theo amount-spent **flexible** — cứ có orders trên Shopify là tính, dễ giữ tier khi relaunch/đổi chương trình.

**Recalc là thao tác NGUY HIỂM nhất** (tier engine = cụm bug lớn, 35 bug). Ba cạm bẫy:
1. **Save setting giữa lúc đang recalc** → có thể **giết job recalc âm thầm** và đánh dấu "completed" (đã có case ~58k member bị un-tier). → Đừng chỉnh setting khi recalc đang chạy.
2. **Over-promote rồi silent-demote:** đổi công thức tier làm khách đang ở tier cao **tụt hạng âm thầm** → khách bực. → Khi đổi công thức, phải **grandfather/thông báo**, không để tụt hạng lặng lẽ.
3. **Import tier raw bỏ qua sync tag/metafield** → perk/discount đọc metafield không thấy → không apply. → Dùng **launch/migrate flow** thay vì import raw.

**Perk & auto-discount:** earn theo tier, birthday theo tier, auto-discount theo tier. Perk apply được nhờ **tier metafield + tag** sync đúng — nếu perk "không apply", nghi ngờ đầu tiên là metafield/tag chưa sync (FAQ → domain C Metafield).

## 2.3 Guest vs Member (rất hay nhầm)

- **Member:** khách có tài khoản/đăng ký, `type = member`, verify email → **earn/redeem bình thường**.
- **Guest:** chưa đăng ký đầy đủ. Với **NCA** khách có thể tồn tại chỉ với mỗi email (không tên) → khó phân biệt; **Legacy** dễ phân biệt hơn.
- **Bẫy chí mạng:** khách tạo qua guest-checkout / NCA / POS có thể thiếu `type`/`verifiedEmail` → bị đẩy về **guest** → **cộng 0 điểm cho MỌI order mà không báo lỗi gì**. Sau import cũng hay rơi vào guest.
- **Legacy → New conversion:** khách legacy sau convert lên new account cần xử lý đúng để không mất điểm/định danh.

> Khi khách nói "khách của tôi mua mà không có điểm", câu hỏi số 1: **"khách đó đang là guest hay member?"** (FAQ domain A).

## 2.4 Expire vs Birthday

- **Point expiration (FIFO):** điểm hết hạn theo lô, vào trước ra trước. Lỗi hay gặp: tính expiration theo **raw balance** mà bỏ qua điểm đã redeem → **hết hạn nhầm** hàng nghìn điểm. Khách kêu "mất điểm vô lý" → nghi expiration.
- **Birthday reward:** set theo tier. Hay gặp issue quanh field birthday không thu thập (NCA không có chỗ nhập) hoặc trigger sai ngày.
- Cả hai khách hỏi nhiều → nên có FAQ trong loyalty page + để AI giải thích.

## 2.5 Widget V4 — Unified Widget: convert & tối ưu ⭐

Widget là category ticket #1, và V4 (Unified Widget) là nơi hay phát sinh sự cố nhất khi onboard.

**Vì sao Unified Widget.** Không chỉ đẹp hơn — đó là **chỗ kết nối & mở rộng**: wishlist, recommendation, trang orders, profile, currency icon, block Joy Subscription/Survey… Chiến lược **đánh vào đầu journey khách** (facade/"Trojan horse") thay vì chỉ là lớp transactional ở cuối, đồng thời **nâng chuẩn aesthetic**. → Khi tư vấn, hiểu đây là điểm khác biệt để **recommend khách lên V4 + bật extensions**.

**Convert v1/v2/v3 → V4:**

*Cách 1 (KHUYẾN NGHỊ) — qua UI trong app:* Preview V4 trước → sửa trong **editor** → preview ngoài store (cần đã bật app Joy trong **app embed**) → nếu ok, nhấn **Switch to Unified**. Chuyển qua lại V3↔V4 được, nhưng **tốt nhất lên V4 là thôi**. Video: https://go.screenpal.com/watch/cOhY1pntg5r

*Cách 2 (FALLBACK) — qua dev zone, khi KH không tự lên được:* dev zone → dev tools → **bật hết các field version**. ⚠️ v1 → phải lên v2, v3 rồi mới V4 (chỉ bật mỗi V4 sẽ không chạy đúng). Sau khi bật, vào editor nó convert data V3→V4, giao diện V3 rất khác V4 → **màu hơi ngược** → chọn 1 preset → chọn **primary đúng màu KH** → setup nốt. ⚠️ Dev zone **chuyển lên LUÔN** (không preview) → **config nhanh kẻo downtime**. **2 nút Reset to factory** (V3/V4): reset design như mới cài — dùng khi lỗi không khôi phục được.

**Lưu ý bắt buộc khi convert:**
- **V3 & V4 dùng CHUNG design tiers + launcher.** Sửa tier card image/icon ở V4 **ảnh hưởng ngược cả V3**. V4 để ảnh **lên trên** point balance (không overlay che) → lên V4 **gần như không cần thay ảnh/icon VIP tier**.
- **Preview KHÔNG cần live:** "View on Store" thêm `?preview_widget_unified=true` vào URL → thấy V4 trên store thật (có overlay báo đang preview). Không exit thì còn thấy V4 ~10 phút.
- **Ảnh chậm (KH v1/đầu v2):** ảnh cũ lưu ở **Firebase** → load chậm. Fix: bật KH sang **upload lên Shopify** rồi upload lại → link về `cdn.shopify.com` (Shopify resize/compress qua CDN).

**Checklist tối ưu Unified Widget khi onboard:**
- **Màu:** chọn **preset + industry preset**; **primary phải match store** (app tự detect — brand colors). Chỉnh primary trước, tùy chỉnh sau.
- **Layout:** chọn **drawer vs widget** — **recommend drawer**. Dùng drawer thì nắm **deep links** để mở từ account/header/menu (FAQ D6).
- **Ảnh:** thay Guest card / Member card (không tier); có tier → thay ảnh + icon từng tier (dùng ChatGPT image gen on-brand). Ảnh header (overlay opacity). Currency icon. Logo header (rất nên thay). Section referral/subscription.
- **Content:** dùng **onbrand** (đổi earn→gain, redeem→unlock… theo brand; **review rồi mới apply** — giúp ~80%). **Program detailed description**: từ Unified desc & detailed desc **khác nhau hết** (dễ quên) — có AI viết; detailed desc là **fallback** khi điều kiện rule engine không hiện đủ ra ngoài.
- **Ẩn/hiện block:** block config được; block chưa bật program (vd referral) tự không hiện.
- **Earning blocks:** `number of items to display` mặc định 5; sort program theo orders; đổi icon program (để to như banner được).
- **Way to redeem / Footer menu:** chọn layout hợp lý; store clean → label-only + underline.
- **Extensions:** recommend **Wishlist** để hoàn thiện bộ suit. Sắp tới có reviews/subscription/AOV bundle.
- **Behaviors:** bật **Login with Shop** (recommended). Nắm **deep link** để mở widget Joy / thay account icon.
- **Preview tips:** chỉnh số point/hạng trong preview để xem widget ở các tier & member status.

---

## Guardrails khi thao tác sửa data

Khi phải sửa/đồng bộ data cho khách (adjust points, resync metafield, recalc tier):
- **Idempotent:** resync/retrigger/recalc không được cộng đôi.
- **Dry-run trước:** recalc tier và mọi bulk write — xem diff trước khi apply.
- **Read-only mặc định:** chỉ action khi có xác nhận.
- **Không silent-demote** khách hiện hữu khi đổi công thức tier.
- **Phân biệt Joy vs 3rd-party** trước khi hứa fix.

---

## TODO — Liz chốt sau

- [ ] Chốt **cột cuối** Google Sheet checklist + template dùng chung.
- [ ] Xác nhận **label/section ticket** (vd `onboarding-new` / `onboarding-in-progress`) đồng bộ DFY labels.
- [ ] Ngưỡng import data lớn: **CS tự làm** vs **forward TS**.
- [ ] Phase 2: trigger tự động trong app khi KH lên Advanced / mới install (điều kiện trigger, nội dung nudge) + skill `joy-onboarding-plan`.

---

*Nguồn: `docs/joy-ticket-analysis-q2-2026.md`, `docs/joy-agent-diagnostic-tool-map.md`, Notion "Plan training DFU", Notion "Support Docs" (Convert V4, Pull the most out of Unified Widget, Account icon opening Joy). FAQ tra cứu → [`joy-support-flow.md`](../kb/cs-process/joy-support-flow.md). Cập nhật: 2026-07-08.*
