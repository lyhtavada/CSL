# Module 6: DFU Onboarding Playbook & FAQ

> **Mục đích.** Đây KHÔNG phải module dạy lại product (kiến thức product ở Module 0–3). Đây là **sổ tay vận hành + tra cứu** để một bạn support/DFU tự xử được **hết các case cơ bản** khi onboard một merchant Joy Loyalty — từ lúc nhận khách đến lúc launch, và tra nhanh khi khách báo lỗi.

**Cách dùng.**
- Đang onboard 1 khách mới → đọc **Phần 1 (Quy trình chuẩn DFU)**, làm theo đúng thứ tự. Phần thao tác CS trên chat (offer/ticket/issue) → xem [`joy-onboarding-flow.md`](./joy-onboarding-flow.md).
- Khách hỏi "migrate sao", "VIP tier tính kiểu gì", "guest với member khác gì" → **Phần 2 (Decision guides)**.
- Khách báo một lỗi/hiện tượng cụ thể → **Phần 3 (FAQ tổng hợp)**, tìm theo domain.

**Nền tảng dữ liệu.** Nội dung được rút từ phân tích 3 tháng ticket Joy Loyalty (1.164 ticket phân loại theo nghĩa + 379 thread dev đọc thật, xem `docs/joy-ticket-analysis-q2-2026.md`). Con số quan trọng nhất cần nhớ: **51% ticket đã escalate lên dev hóa ra KHÔNG phải bug Joy** — mà là config sai, hành vi đúng-thiết-kế bị hiểu nhầm, lỗi bên thứ ba, hoặc sửa data một lần. → Nhiệm vụ của bạn là **tự chẩn đoán để lọc ra 51% đó**, không phải đẩy hết lên dev.

---

# 🧭 Phần 1 — Quy trình chuẩn DFU (7 bước)

## Nguyên tắc vàng

1. **Chuẩn hơn nhanh.** Giá trị của một lần onboard KHÔNG nằm ở "thấy widget nhanh", mà ở **Time-to-value SAU khi khách launch**. Setup vội để rồi khách launch xong không có gì chạy = thất bại, dù widget đẹp.
2. **Hỏi trước, làm sau.** Không bao giờ nhận một yêu cầu lẻ ("migrate hộ", "import hộ") rồi làm ngay mà chưa hiểu bức tranh tổng thể của khách. Yêu cầu lẻ luôn phải quy về plan tổng.
3. **1 khách = 1 kế hoạch, không phải nhiều ticket rời.** Một lần onboarding gom vào **một** kế hoạch có checklist, không xé thành 5 ticket lẻ mỗi người làm một mẩu.
4. **Nhận là own tới cùng.** (Xem rule Ownership & SLA cuối phần.)

## 7 bước — mỗi bước có exit-criteria (chỉ qua bước sau khi đạt)

### Bước 0 — Intake: hỏi plan Loyalty của khách TRƯỚC KHI làm bất cứ gì

Đây là bước hay bị bỏ nhất và là gốc của phần lớn rework. Trước khi động vào app, hỏi và ghi lại:

- **Mục tiêu:** khách muốn giữ chân (retention), tăng AOV, hay lấy referral? Ngành hàng gì (margin cao/thấp)?
- **Chương trình tính theo gì:** **points-based** hay **amount-spent**? (quyết định cách setup VIP tier — xem Phần 2.2).
- **Khách mới hay đang chuyển sang:** làm loyalty lần đầu, hay **migrate** từ app/platform khác? Nếu migrate → từ đâu (Smile.io, LoyaltyLion, platform ngoài Shopify…)?
- **Tài khoản khách:** đang dùng **Legacy** hay **New Customer Accounts**? (ảnh hưởng customize + guest/member — xem Phần 2.3).
- **Có tích hợp gì bắt buộc không:** Klaviyo/Omnisend? Review app (Judge.me/Loox/Yotpo)? Subscription (Recharge)? POS?

**Exit-criteria:** có một bản tóm tắt yêu cầu, **khách đã xác nhận** đúng ý.

### Bước 1 — Lập plan gộp cho khách (offer trước)

Từ intake, viết ra **một** checklist onboarding cho khách này (không tách ticket lẻ). Chủ động **offer trước** các việc sẽ làm — đặc biệt hai chỗ app hay "trigger" nhiều thao tác: **import** và **migrate**. Khách biết trước lộ trình → ít ticket phát sinh giữa chừng.

**Exit-criteria:** khách nắm được các bước và mốc thời gian.

### Bước 2 — Xin quyền (scopes)

Đề nghị khách **grant thêm scopes** cần thiết. Ngoài để app chạy đủ tính năng, extra scopes còn giúp **AI report/diagnostic đọc được nhiều state hơn** → chẩn đoán tốt hơn về sau.

**Exit-criteria:** scopes đã cấp đủ.

### Bước 3 — Setup (theo Module 3)

Thực hiện setup theo **Module 3: How to setup** (currency, earn/redeem, widget, loyalty page, tiers, integrations, notifications…). Module 6 không lặp lại — chỗ nào vướng thì tra Phần 2/Phần 3.

**Nhắc:** làm trên **theme test** (duplicate theme riêng cho rewards, sửa ở preview mode), và bật **Sandbox Mode** để test không đụng dữ liệu thật.

**Exit-criteria:** chương trình đã cấu hình xong trên Sandbox/theme test.

### Bước 4 — Test cho khách (đừng bỏ bước này)

Đây là bước **thường xuyên bị thiếu**. Trước khi launch, phải **test thật** trên Sandbox và cho khách thấy:

- Earn: đặt một đơn test → điểm vào đúng.
- Redeem: đổi điểm → coupon sinh ra và apply được.
- VIP tier (nếu có): khách rơi đúng tier, perk apply.
- Widget/loyalty page hiển thị đúng brand.

**Exit-criteria:** **khách đã xem và xác nhận** luồng chạy đúng.

### Bước 5 — Launch: Sandbox → Live

Bước cuối cùng để chương trình bắt đầu cộng điểm thật cho khách hàng. **Rất quan trọng, phải confirm rõ với merchant** rằng đây là lúc "bật thật". Merchant cần: tắt Sandbox → Live, và bật app trên theme chính (hoặc publish theme test lên chính) để widget hiện ra ngoài.

**Exit-criteria:** program ở **Live mode**, widget hiện trên storefront thật.

### Bước 6 — Report & handoff

Chỉ cho khách chỗ xem số liệu (**assisted revenue**, **redemption rate**), và bàn giao. Giải thích ngắn các chỉ số để khách tự theo dõi.

**Exit-criteria:** khách biết đọc report, đã handoff.

## ★ Rule Ownership & SLA (chat trực theo ca)

Chat trực theo ca dễ dẫn tới ticket bị bỏ dở hoặc đá qua người khác. Quy tắc:

- **Nhận là own tới cùng.** Bạn nhận case nào thì bạn chịu trách nhiệm case đó tới khi xong — kể cả khi phải kéo dài.
- **Hẹn rõ:** với việc cần thời gian (vd import), **hẹn khách ~1 ngày** và làm tới nơi.
- **Bàn giao ca liền mạch:** hết ca mà chưa xong → để lại note trạng thái đầy đủ để **ca sau nối tiếp**, không bắt khách kể lại từ đầu.
- **Không đá việc.** Không mặc định assign một bạn khác "import hộ" chỉ vì hết ca — trừ khi đã bàn giao trạng thái rõ ràng và có lý do chính đáng.

## Dùng AI chat nhiều hơn

Team đang dùng luồng AI chat hơi ít. Với các câu hỏi chẩn đoán trong Phần 3 (khách này có phải guest không, order này vì sao không earn, mã coupon điều kiện thật là gì…), **hỏi AI trước** — nó đọc được state và trả lời nhanh hơn là mò tay hoặc đẩy lên dev.

## 🤖 Kết hợp với Joy AI Agent — plan sống trên "canvas"

Checklist 7 bước ở trên không nên là giấy tĩnh — nó là thứ **Joy AI Agent vận hành được**, và mỗi merchant có một **plan sống trên canvas** (artifact hiển thị cùng chat, cả support lẫn merchant cùng thấy & cập nhật):

- **Agent chạy Intake:** hỏi plan KH + tự đọc state shop (plan, Sandbox/Live, account type, integrations đã cài, có phải migrate không) → điền sẵn phần lớn Bước 0.
- **Agent sinh plan gộp:** từ intake + state, tạo **đúng 1 kế hoạch onboarding** cho merchant đó (không ticket lẻ), đề xuất việc cần làm ở Bước 1.
- **Lưu trên canvas:** plan được ghi lên một canvas per-merchant — liệt kê 7 bước, exit-criteria, trạng thái done/pending. Đây là **nguồn sự thật chung**: hết ca, ca sau mở canvas là nối tiếp được (giải luôn bài toán bàn giao ở rule Ownership & SLA).
- **Agent tự theo dõi exit-criteria:** vì mỗi bước có tiêu chí máy đọc được (Sandbox hay Live? app embed bật chưa? đơn test đã earn? tier đã sync metafield?), agent tự tick từng bước và nhắc bước còn thiếu — thay vì phụ thuộc trí nhớ từng bạn.

> **House rule:** đúng tinh thần *"AI agent là substrate"* (mọi feature readable/writable/explainable bởi agent) + *"AI skill per feature"*. Đề xuất skill `joy-onboarding-plan` (chạy intake → sinh & duy trì canvas plan). **API:** `POST /agent/onboarding/plan`, `GET /agent/onboarding/plan?shop=`, `PATCH /agent/onboarding/plan/step` (tick exit-criteria).

---

# 🧩 Phần 2 — Decision guides ("hiểu tại sao")

Phần này dành cho các quyết định mà nếu "hỏi gì làm nấy" sẽ sai. Trọng tâm: **Migration** và **VIP tier** — hai chỗ gây nhiều ticket & rework nhất.

## 2.1 Migration & Import (đào sâu)

Đây là chỗ hay "làm đúng cái được hỏi mà không hỏi lại", dẫn tới migrate sai/lặp. **Trước khi migrate, luôn hỏi đủ 3 câu:**

### Câu hỏi 1 — Migrate TỪ ĐÂU?

- **Từ app loyalty khác trên Shopify** (Smile.io, LoyaltyLion, Rivo…): thường chỉ mang được **balance điểm**; **activities/lịch sử** thường ít hoặc không mang. VIP tier có thể mang nhưng phải xử lý đúng (xem dưới).
- **Từ một platform ngoài Shopify** (chuyển hẳn nền tảng) rồi launch loyalty lần đầu: khác — thường vừa migrate balance vừa launch chương trình mới.

> **Điều kiện bắt buộc:** khách được migrate **phải đã tồn tại trên Shopify**. Không có customer trên Shopify thì không gắn điểm/tier vào đâu được.

### Câu hỏi 2 — Tính theo POINT hay AMOUNT?

- **Points-based:** mang balance điểm sang.
- **Amount-spent:** thường đi kèm VIP tier theo chi tiêu. `amount-spent` **linh hoạt hơn** — chỉ cần khách có orders trên Shopify là tính được, nên khi khách đổi/relaunch chương trình vẫn giữ được tier dễ dàng.

### Câu hỏi 3 — Dùng FILE IMPORT hay SYNC ORDERS & LAUNCH? (hiểu pros/cons)

Đây là quyết định quan trọng nhất và hay bị bỏ qua:

|  | **File import (CSV)** | **Sync orders & launch** |
| --- | --- | --- |
| Cách làm | Khách gửi file điểm/tier, mình import raw | Bật earn theo lịch sử orders có sẵn trên Shopify rồi launch |
| Hợp khi | Chỉ có balance điểm rời từ app cũ, không map được ra orders | Chương trình tính theo **amount-spent**, dữ liệu order đã nằm trên Shopify |
| Ưu | Nhanh, mang đúng con số app cũ | Dữ liệu "thật" theo Shopify; tier/tag/metafield được sinh **đúng luồng** |
| Nhược | ⚠️ **Import raw dễ bỏ qua sync tag + metafield** mà discount function đọc → perk/tier không apply (đây là root cause của cả cụm bug tier). Import nhiều lần dễ cộng đôi. | Chỉ hợp khi logic là amount-spent |

> **Quy tắc:** nếu chương trình tính theo **amount-spent**, **ưu tiên sync orders & launch** thay vì import file — vì nó sinh tier/tag/metafield đúng luồng, tránh cụm lỗi "perk không apply do metafield chưa sync".

### Lưu ý bắt buộc khi migrate

- **Tránh migrate nhiều lần** → dễ cộng đôi/gây lỗi. Migrate một lần, kiểm tra kỹ.
- **Migrate cả VIP tier:** không import tier raw. Phải đảm bảo **tag + metafield** của tier được sync (discount function đọc metafield/tag để cấp perk — thiếu là perk không apply).
- **Sau migrate, khách có earn lại khi sign-up ở platform mới không?** → cần xác định trước để không cộng nhầm sign-up reward cho khách cũ.
- **Guest sau import:** khách import xong thường ở trạng thái **guest** (xem 2.3) — phải nói rõ cho merchant, không im lặng.

## 2.2 VIP tier (đào sâu)

### Tính theo Points vs Amount-spent

- **Theo points:** dành cho chương trình points-based.
- **Theo amount-spent:** dành cho ngành hàng có nhu cầu cao; **flexible** — cứ có orders trên Shopify là tính, dễ giữ tier khi relaunch/đổi chương trình.

### Recalc là thao tác NGUY HIỂM nhất — hiểu để không gây sự cố

Từ ticket thật, tier engine là cụm bug lớn (35 bug). Ba cạm bẫy:

1. **Save setting giữa lúc đang recalc** → có thể **giết job recalc âm thầm** và đánh dấu "completed" (đã có case ~58k member bị un-tier). → Đừng chỉnh setting khi recalc đang chạy.
2. **Over-promote rồi silent-demote:** đổi công thức tier làm khách đang ở tier cao **tụt hạng âm thầm** → khách bực, phải xin lỗi. → Khi đổi công thức, phải **grandfather/thông báo**, không để tụt hạng lặng lẽ.
3. **Import tier raw bỏ qua sync tag/metafield** → perk/discount đọc metafield không thấy → không apply. → Dùng **launch/migrate flow** thay vì import raw (xem 2.1).

### Perk & auto-discount

Hiểu các perk có thể setup cho tier: earn theo tier, birthday theo tier, auto-discount theo tier. Perk apply được là nhờ **tier metafield + tag** đã sync đúng — nếu perk "không apply", nghi ngờ đầu tiên là metafield/tag chưa sync (Phần 3 → Metafield).

## 2.3 Guest vs Member (rất hay nhầm)

- **Member:** khách đã có tài khoản/đăng ký, có `type = member`, đã verify email → **earn/redeem bình thường**.
- **Guest:** khách chưa đăng ký đầy đủ. Với **New Customer Accounts** khách có thể tồn tại chỉ với mỗi email (không điền tên) → khó phân biệt guest/member; với **Legacy** dễ phân biệt hơn.
- **Bẫy chí mạng:** khách tạo qua guest-checkout / NCA / POS có thể thiếu `type`/`verifiedEmail` → bị đẩy về **guest** → **cộng 0 điểm cho MỌI order mà không báo lỗi gì**. Sau import cũng hay rơi vào guest.
- **Legacy → New conversion:** khách legacy sau khi convert lên new account cần được xử lý đúng để không mất điểm/định danh.

> Khi khách nói "khách của tôi mua mà không có điểm", câu hỏi số 1: **"khách đó đang là guest hay member?"** (xem FAQ Points).

## 2.4 Expire vs Birthday

- **Point expiration (FIFO):** điểm hết hạn theo lô, tính theo thứ tự vào trước ra trước. Lỗi hay gặp: tính expiration theo **raw balance** mà bỏ qua điểm đã redeem trước đó → **hết hạn nhầm** hàng nghìn điểm. Khi khách kêu "mất điểm vô lý", nghi ngờ expiration.
- **Birthday reward:** có thể set theo tier. Hay gặp issue quanh việc field birthday không được thu thập (đặc biệt NCA không có chỗ nhập) hoặc trigger sai ngày.
- Cả hai nhóm này khách hỏi nhiều → nên có FAQ trong loyalty page + để AI giải thích.

## 2.5 Widget V4 — Unified Widget: convert & tối ưu ⭐

Widget là category ticket #1, và Widget V4 (Unified Widget) là nơi hay phát sinh sự cố nhất khi onboard. Nắm chắc phần này.

### Vì sao Unified Widget

Unified Widget không chỉ là widget đẹp hơn — đó là **chỗ kết nối & mở rộng**: wishlist, recommendation, trang orders, profile, currency icon, block tích hợp Joy Subscription/Survey… Chiến lược là **đánh vào đầu journey của khách** (facade/"Trojan horse") thay vì chỉ là một lớp transactional ở cuối. Đồng thời **nâng chuẩn aesthetic** so với thị trường loyalty (nơi app nào cũng na ná "smile-alternative"). → Khi tư vấn, hiểu đây là điểm khác biệt để **recommend khách lên V4 + bật extensions**.

### Convert v1/v2/v3 → V4

**Cách 1 (KHUYẾN NGHỊ) — qua UI trong app:**

- Preview V4 trước → sửa trong **editor** → preview ngoài store (cần đã bật app Joy trong **app embed**) → nếu ok, nhấn **Switch to Unified**.
- Có thể chuyển qua lại V3 ↔ V4, nhưng **tốt nhất lên V4 là thôi** (trừ khi có lỗi phát sinh). Có tương thích ngược nên lên V4 chỉnh một chút là tương đối ổn so với V3.
- Video quy trình: https://go.screenpal.com/watch/cOhY1pntg5r

**Cách 2 (FALLBACK) — qua dev zone, khi KH không tự lên V4 được:**

- Vào **dev zone → dev tools** → **bật hết các field** version nếu chưa bật. ⚠️ Nếu KH ở **v1 → phải lên v2, v3 rồi mới V4** (chỉ bật mỗi V4 sẽ không chạy đúng).
- Sau khi bật, vào editor nó **convert data V3→V4**. Giao diện V3 rất khác V4 → **màu hơi ngược** → chọn **1 preset** → chọn **primary đúng màu KH** → setup nốt.
- ⚠️ Cách dev zone **chuyển lên LUÔN** (không có bước preview) → phải **config nhanh kẻo có downtime**. Bù lại: khi cần reset data lúc lỗi, đây là cách khả thi.
- **2 nút Reset to factory** (V3/V4): reset design y như mới cài — dùng khi lỗi ngoài dự kiến không khôi phục được settings. Đổi lại phải config lại design từ đầu.

### Lưu ý bắt buộc khi convert (không nắm là gây sự cố cho KH đang chạy V3)

- **V3 & V4 dùng CHUNG design tiers + launcher.** Trước đây tier card design nằm trong VIP tier; lên V4 nó move vào editor → **sửa tier card image/icon ở V4 ảnh hưởng NGƯỢC cả V3**. V4 thiết kế giữ nguyên membership card bằng cách để ảnh **lên trên** point balance (thay vì overlay che) → nên khi lên V4 **gần như không cần thay ảnh/icon VIP tier**.
- **Preview KHÔNG cần live:** "View on Store" thêm `?preview_widget_unified=true` vào URL → thấy V4 trên store thật (có overlay báo "đang preview" như Shopify theme preview). Không exit thì còn thấy V4 trong ~10 phút tiếp theo.
- **Ảnh chậm (KH v1/đầu v2):** ảnh cũ lưu ở **Firebase** → load chậm. Fix: bật KH sang **upload lên Shopify** rồi upload lại → link về `cdn.shopify.com` (Shopify resize/compress qua CDN, rất tối ưu — vd ô nhỏ lấy đúng size ~400).

### Checklist tối ưu Unified Widget khi onboard

- **Màu:** chọn **preset + industry preset**; **primary phải match store** (app tự detect — mở store picker, chọn ở brand colors). Background/button/text ăn theo rule → **chỉnh primary trước**, tùy chỉnh sau.
- **Layout:** chọn **drawer vs widget** — **recommend drawer**. Dùng drawer thì nắm **deep links** để mở từ account/header/menu (xem FAQ D6).
- **Ảnh:** thay **Guest card / Member card** (nếu không có VIP tier); có VIP tier → thay **ảnh + icon từng tier**, mỗi tier một điểm nhấn (nên dùng **ChatGPT image** gen on-brand). Ảnh **header** (contrast lớn với chữ → dùng overlay opacity). **Currency icon** (emoji hoặc upload icon riêng để brand hóa). **Logo header** (rất nên thay — ảnh transparent, có thể bỏ chữ giữ logo). Ảnh section referral/subscription portal nên có. Hiệu ứng carousel: **hover đổi ảnh thứ 2**, **subtle zoom** — xem demo store để làm đúng.
- **Content:** dùng tính năng **onbrand** (đổi earn→gain, redeem→unlock, complete→hit… theo brand; ăn theo default/ngôn ngữ KH chọn; **review rồi mới apply** — giúp ~80%). **Program detailed description**: từ bản Unified, desc & detailed desc **khác nhau hết** (dễ quên) — có AI viết; detailed description là **fallback** khi điều kiện setup ở rule engine không hiện đủ ra ngoài.
- **Ẩn/hiện block:** mọi block config được (vd ẩn marketing block ở profile). Block chưa bật program (vd referral) **tự không hiện**.
- **Earning blocks:** `number of items to display` mặc định 5 (đừng show hết); sort program theo orders (2 options); sắp thứ tự program; **đổi icon program** (có thể để to như banner — không nhất thiết icon độ phân giải thấp).
- **Way to redeem:** có nhiều layout → chọn hợp lý.
- **Footer menu:** store clean → **label-only + underline**; phức tạp → có icon; nhìn theo style header.
- **Extensions:** recommend KH — đặc biệt **Wishlist** để hoàn thiện bộ suit (chú ý layout aesthetic của wishlist). Sắp tới có thêm reviews/subscription/AOV bundle.
- **Behaviors:** bật **Login with Shop** (recommended — login xong mở lại widget đúng trang). Nắm **deep link** để mở widget Joy / thay account icon.
- **Preview tips:** trong preview chỉnh **số point/hạng** để xem widget ở các tier & member status trông khác nhau ra sao.

---

# ❓ Phần 3 — FAQ tổng hợp (theo domain)

## Cách đọc mỗi FAQ & lăng kính triage

Mỗi case theo format: **Dấu hiệu** (khách mô tả gì) → **Tự chẩn đoán** (bạn/AI check state nào) → **Cách xử lý** → **Khi nào escalate**.

**Lăng kính bắt buộc — Lỗi Joy vs Config vs 3rd-party.** Trước khi hứa "để dev fix", phân loại:

- 🟢 **Config/User-error:** sai setting, sandbox, plan-gating, chưa bật embed… → tự sửa/hướng dẫn, KHÔNG cần dev.
- 🔵 **Expected behavior:** đúng-thiết-kế nhưng khách hiểu nhầm → giải thích.
- 🟠 **3rd-party:** lỗi của Shopify/Fera/Judge.me/Recharge/POS… → chỉ ra đúng thủ phạm, không nhận là bug Joy.
- 🔴 **Bug Joy thật:** đã loại 3 nhóm trên → escalate kèm bằng chứng (state đã check).

> Nhắc: 51% ticket từng escalate hóa ra thuộc 3 nhóm đầu. Luôn chạy hết lăng kính trước khi kêu dev.

---

## A. Points / Earning (7)

**A1. Khách mua nhưng không cộng điểm.**
→ *Tự chẩn:* khách đang **guest hay member**? `type`/`verifiedEmail` có rỗng không? (Guest = cộng 0đ âm thầm.)
→ *Xử lý:* nếu guest → hướng dẫn khách đăng ký/verify; kiểm tra enrollment. → 🟢 thường là config/data.
→ *Escalate:* nếu là member, verified, program đang Live mà vẫn 0đ → 🔴 kèm order id + customer.

**A2. Cả store không cộng điểm (từ một mốc thời gian).**
→ *Tự chẩn:* shop đang **Sandbox hay Live**? Program có bật lúc order tạo không?
→ *Xử lý:* Sandbox → hướng dẫn launch sang Live. → 🟢 rất hay gặp.
→ *Escalate:* Live mà vẫn không cộng toàn store → 🔴.

**A3. Order lẻ không cộng điểm (khách khác thì có).**
→ *Tự chẩn:* order có thỏa điều kiện earn không (min-order, exclude tax, sản phẩm loại trừ)? có snapshot lúc fulfillment? `source_name` có match (đơn subscription/Recharge)?
→ *Xử lý:* nếu do điều kiện/tax → giải thích (🔵). Nếu Shopify đổi `source_name` phá earn của Recharge → 🟠/🔴 tùy.
→ *Escalate:* đủ điều kiện mà vẫn trượt → 🔴 kèm order id.

**A4. Điểm bị cộng đôi cho cùng một đơn.**
→ *Tự chẩn:* có race webhook↔admin / import trùng / migrate nhiều lần không?
→ *Xử lý:* xác định nguồn double; nếu do import/migrate lặp → sửa data + dặn không migrate lại.
→ *Escalate:* nghi race engine → 🔴 (đây là bug thật đã gặp).

**A5. Đơn thứ 2 vẫn cộng dù đáng lẽ 1 lần (sign-up/once-in-lifetime).**
→ *Tự chẩn:* limit/once-in-lifetime của program có enforce không?
→ *Escalate:* 🔴 nếu anti-cheat/limit không chặn.

**A6. Điểm về chậm.**
→ *Tự chẩn:* có backlog xử lý (PubSub) không? mới có traffic lớn/bulk?
→ *Xử lý:* thường chỉ là delay → trấn an, chờ. 🔵/🟢.
→ *Escalate:* chậm bất thường kéo dài → 🔴.

**A7. Điểm bị mất/hết hạn vô lý.**
→ *Tự chẩn:* có phải **FIFO expiration** tính nhầm (bỏ qua điểm đã redeem)? lô legacy 2024 thiếu field?
→ *Escalate:* nếu con số hết hạn không khớp logic → 🔴 (đã có bug expiration).

## B. Coupon / Redeem (6)

**B1. Mã redeem báo invalid / không apply.**
→ *Tự chẩn:* đọc **điều kiện thật của mã động**: min-purchase, exclude-collection, country, **channel (online-only?)**, cap, start/end.
→ *Xử lý:* phần lớn là điều kiện không thỏa (vd mã online-only dùng trên POS) → giải thích (🔵/🟢).
→ *Escalate:* điều kiện thỏa mà vẫn invalid → 🔴.

**B2. Coupon Joy không được đánh "used".**
→ *Tự chẩn:* có discount/app khác **non-combinable** đang thắng trên cart không?
→ *Xử lý:* giải thích xung đột combinability, chỉnh combinesWith nếu cần. Thường 🟢/🔵.

**B3. Redeem trên POS không được.**
→ *Tự chẩn:* mã có phải **online-only**? có khách + có sản phẩm trong cart chưa (UI redeem chỉ hiện khi đủ điều kiện)?
→ *Xử lý:* giải thích điều kiện hiển thị redeem trên POS (🔵). "Failed to load" trên POS thường là **lỗi Shopify** (🟠).

**B4. Cap giảm sai (vd hiện 6% dù cap khác).**
→ *Tự chẩn:* giá trị cap có lưu đúng kiểu/không rỗng không?
→ *Escalate:* 🔴 nếu cap lưu sai.

**B5. Prefix mã sai (JOY- thay vì Birthday-...).**
→ *Tự chẩn:* program có bật dùng prefix riêng không (`isUsePrefixDiscountCode`)?
→ *Xử lý:* bật/đặt prefix trong setting (🟢). Nhắc setup prefix coupon từ đầu (branding).

**B6. Free gift hết hàng vẫn redeem được → lỗi checkout.**
→ *Tự chẩn:* stock thật của variant vs "inventory-not-tracked" (âm)?
→ *Escalate:* 🔴 nếu redeem được khi hết hàng.

## C. Metafield / Perk sync (4)  ⭐ gốc của nhiều "widget chết" & "perk không apply"

**C1. Perk/tier discount không apply.**
→ *Tự chẩn:* **tier tag + metafield mà discount function đọc đã sync chưa**? merchant **import raw hay launch/migrate**?
→ *Xử lý:* nếu import raw → chạy resync metafield+tag hoặc dùng launch/migrate flow. 🟢/🔴 tùy.

**C2. Loyalty Hub / widget trắng, 404.**
→ *Tự chẩn:* `joy_loyalty` metafield có null / sai kiểu (single_line_text thay vì json)? shopId rỗng → HMAC hash lỗi?
→ *Escalate:* 🔴 (metafield corruption → widget chết), kèm shop domain.

**C3. Điểm hiển thị 0 / 1000 placeholder dù backend có điểm.**
→ *Tự chẩn:* email hoa/thường lệch khi build HMAC (backend lowercase)?
→ *Escalate:* 🔴 nếu hash mismatch.

**C4. Report tier có cột "None".**
→ *Tự chẩn:* khách có `tierName` metafield **chưa sync** (không phải "tier thứ 4").
→ *Xử lý:* resync metafield cho nhóm khách đó.

## D. Widget / V4 (7)  — nhóm category #1

**D1. Widget không hiện trên store.**
→ *Tự chẩn:* **app embed đã bật chưa**? metafield/hash ok? (xem C2). currency symbol có undefined không?
→ *Xử lý:* bật app embed / app block đúng chỗ (🟢 rất hay gặp).

**D2. Loyalty page blank sau khi deploy.**
→ *Tự chẩn:* có phải **ChunkLoadError** (min.js cache cũ đòi chunk đã purge)?
→ *Xử lý:* hard refresh/clear cache; nếu diện rộng → 🔴 (deploy staleness).

**D3. Sau lên V4 mất config / lệch so với V3.**
→ *Tự chẩn:* field nào **không migrate** V3→V4 (collection-page, custom login link, Submit Receipt, survey points, birthday field, per-tier rate, page-restriction)?
→ *Xử lý:* set lại field bị rơi trong V4. Đây là **nguồn bug #1** — nếu là gap parity thật → 🔴.

**D4. Đổi CSS ngoài không ăn.**
→ *Tự chẩn:* Widget V4 dùng **Shadow DOM** → CSS ngoài không xuyên vào được.
→ *Xử lý:* sửa style **trong in-app editor**, không sửa CSS theme ngoài. 🔵 (đúng-thiết-kế) — giải thích, không cần dev.

**D5. Widget crash/trắng ở một số store nhất định.**
→ *Tự chẩn:* currency symbol lạ (SGD/SEK/Kč/TWD) throw JS? i18n ghép chuỗi vỡ (zh/FR/DE)?
→ *Escalate:* 🔴 (currency/i18n rendering).

**D6. Muốn account icon (đăng nhập) mở widget Joy thay vì account Shopify.**
→ *Tự chẩn:* theme dùng header.liquid thường hay dùng web component `<shopify-account>` (theme mới)?
→ *Xử lý:* dùng **deep link `#joy-open`**. Theme đơn giản → sửa thẻ `<a>` trong `header.liquid` về `#joy-open` (app tự remove `#joy-open` khi tắt để mở lại được). Theme mới bắt dùng `<shopify-account>` → chèn đoạn JS chặn click (capture phase) rồi set `window.location.hash='joy-open'`. ⚠️ **Không recommend thay account Shopify — chỉ làm khi KH yêu cầu.** Chi tiết: doc "How to make Account icon opening Joy". 🟢/🔵.
→ *Bonus:* "Login xong có quay về trang cũ không?" → **Có, out-of-the-box** (`AVADA_JOY.login_url`); nhưng đổi **custom login link** sẽ override cái này.

**D7. Khách chưa lên được V4 / convert V4 bị lỗi.**
→ *Tự chẩn:* KH đang ở version nào (v1 phải qua v2→v3→v4)? convert qua UI hay dev zone?
→ *Xử lý:* ưu tiên convert qua UI (Switch to Unified); nếu KH không tự làm được → dev-zone fallback (bật hết field version, config nhanh tránh downtime); lỗi không khôi phục được → **Reset to factory**. Xem **Phần 2.5**. Lưu ý ảnh chậm do Firebase → chuyển upload lên Shopify.

## E. VIP tier (6)

**E1. Khách ở sai tier.**
→ *Tự chẩn:* amount-spent thực tế? tier hiện tại tính theo nguồn nào (auto/manual/exclusive)? startDate dùng để tính?
→ *Xử lý:* đối chiếu công thức; nếu do định nghĩa tier → giải thích (🔵).

**E2. Khách bị downgrade tier sau khi mua/đổi setting.**
→ *Tự chẩn:* **có ai bấm recalc thủ công** không? có đổi công thức tier không?
→ *Escalate:* silent-demote do đổi công thức → 🔴 (không được để tụt hạng âm thầm).

**E3. Recalc chạy dở/không xong (nhiều khách bị un-tier).**
→ *Tự chẩn:* có ai **save setting giữa lúc recalc** không?
→ *Escalate:* 🔴 (save phá recalc job).

**E4. Perk/auto-discount của tier không apply.**
→ *Tự chẩn:* → về **C1** (tag/metafield tier chưa sync); import raw hay launch/migrate?

**E5. Widget hiện sai ngưỡng/điểm tier (vd guest thấy earning rate của tier cao nhất).**
→ *Tự chẩn:* guest có đang hiển thị theo tier cao nhất không? ngưỡng backend vs widget lệch?
→ *Escalate:* 🔴 nếu widget hiển thị sai so với backend.

**E6. Import tier rồi mà entry reward/tag chưa đúng.**
→ *Tự chẩn:* re-import tier có sync tag + grant entry reward đúng không?
→ *Xử lý:* dùng launch/migrate flow thay vì import raw; resync.

## F. Migration / Import (4)

**F1. "Migrate hộ tôi từ app X."**
→ *Xử lý:* KHÔNG làm ngay — chạy 3 câu hỏi ở **Phần 2.1** (từ đâu / point vs amount / file vs sync). Xác nhận khách đã có trên Shopify.

**F2. Migrate từ Smile.io có issue.**
→ *Tự chẩn:* mang gì sang (thường chỉ balance)? tier có kèm tag/metafield không? có migrate nhiều lần không?
→ *Xử lý:* thường là data one-off cần rà; nếu phức tạp, hẹn **call** với khách. Phần lớn 🟢/data-fix.

**F3. Import xong khách có điểm nhưng là guest.**
→ *Tự chẩn:* → **Phần 2.3**; `type`/`verifiedEmail` sau import.
→ *Xử lý:* nói rõ cho merchant trạng thái guest, hướng xử lý; đừng im lặng.

**F4. Import nhiều lần → điểm cộng đôi.**
→ *Xử lý:* rà và sửa; dặn **migrate/import một lần**. Xem A4.

## G. Integration (4)

**G1. Klaviyo/Omnisend không sync / nút Sync bị grey-out.**
→ *Tự chẩn:* connection status? có stale error-flag (vd MISSING_EVENTS_WRITE_SCOPE)? đang trong lúc launch tier (app tạm tắt sync)?
→ *Xử lý:* reconnect/cấp scope; nếu do đang launch tier → chờ xong. 🟢/🔴 tùy.

**G2. Recharge ngừng sync discount.**
→ *Tự chẩn:* Recharge API key còn không (có bị xóa field)? key hợp lệ? `source_name` đổi?
→ *Escalate:* xóa nhầm field key → 🔴; key sai → 🟢.

**G3. Review app không cộng điểm (Judge.me/Loox/Yotpo/Fera).**
→ *Tự chẩn:* **lỗi Joy hay 3rd-party**? Fera webhook có bị tắt? Judge.me chỉ gửi status 'not-yet'? Loox free plan thiếu Flow?
→ *Xử lý:* phần lớn là **3rd-party** (🟠) — chỉ ra đúng thủ phạm, hướng dẫn bật webhook/Flow; đừng nhận là bug Joy.

**G4. App hiện "Not Connected" nhưng thực ra vẫn chạy (hoặc ngược lại).**
→ *Tự chẩn:* trạng thái hiển thị vs thực tế last-sync.
→ *Escalate:* 🔴 nếu status hiển thị sai (false "Not Connected").

## H. Shop config / plan / mode (3)

**H1. "Feature X tôi không thấy đâu."**
→ *Tự chẩn:* có bị **plan-gating** không (Advanced/Ultimate/Plus/Enterprise)? (vd checkout Quick Redeem chỉ Enterprise; checkout extension chỉ Plus.)
→ *Xử lý:* giải thích plan cần thiết. 🔵/🟢.

**H2. "Program tôi setup rồi mà không chạy."**
→ *Tự chẩn:* đang **test-mode/Sandbox**? test-email đã add? điều kiện country/phone?
→ *Xử lý:* hướng dẫn launch/điều kiện. 🟢.

**H3. "Widget/loyalty page ngôn ngữ sai / chưa dịch."**
→ *Tự chẩn:* translation đã update chưa (mặc định English)? tương thích Shopify Translate & Adapt? có field nào không đi qua i18n?
→ *Xử lý:* update translation từng field; nếu chữ **vỡ do ghép chuỗi** (zh/FR/DE) → 🔴 (i18n bug).

---

## Phụ lục — Guardrails khi thao tác sửa data

Khi phải sửa/đồng bộ dữ liệu cho khách (adjust points, resync metafield, recalc tier):

- **Idempotent:** resync/retrigger/recalc không được cộng đôi.
- **Dry-run trước:** với recalc tier và mọi bulk write — xem diff trước khi apply.
- **Read-only mặc định:** chỉ action khi có xác nhận.
- **Không silent-demote** khách hiện hữu khi đổi công thức tier.
- **Phân biệt Joy vs 3rd-party** trước khi hứa fix.

---

*Nguồn: `docs/joy-ticket-analysis-q2-2026.md` (1.164 ticket phân loại semantic + 379 thread dev), `docs/joy-agent-diagnostic-tool-map.md` (question bank theo domain), Notion "Plan training DFU" (9 vấn đề vận hành), Notion "Support Docs" (Convert V4, Pull the most out of Unified Widget, Account icon opening Joy). Cập nhật: 2026-07-08.*
