# Joy DFY — CS Flow & Checklist

**Owner:** Liz (CS Leader)
**Created:** 2026-05-18
**Updated:** 2026-07-03

> Xem mục đích & tinh thần DFY: [`joy-dfy-intro.md`](./joy-dfy-intro.md)

---

## 0. Đổi gì ở bản này (2026-07-03)

DFY trước đây gần như chỉ xoay quanh **widget customization**. Nhưng widget đẹp mà store **chưa có earning/redeeming active** hoặc **vẫn ở sandbox** thì khách vẫn không tích được điểm → program chưa launch thật. Bản này mở rộng DFY ra **toàn bộ con đường go-live**, và **bám đúng Quickstart checklist có sẵn trong app** (không tự chế phase riêng) để CS và KH nhìn cùng một thứ.

**Điểm neo quan trọng nhất: `launch = bật live mode (thoát sandbox)`.** App Joy chạy sandbox trước; store có thể setup xong hết earning/redeeming/widget mà **vẫn sandbox = khách thật chưa tích được điểm**. Công tắc launch thật là **"Switch from sandbox to live mode"** trong Quickstart → **Launch & Optimize**.

```
① Program      → earning + redeeming active
② Widget hiện  → brand color + setup widget (widget hiển thị trên store)
🚀 GO LIVE     → Switch sandbox → live mode   ← MỐC LAUNCH THẬT (luôn xin KH gật trước)
③ Touchpoints  → point calculator, visibility, account/thankyou page   (tối ưu sau LIVE)
④ Engagement   → referral, notifications, integrations   (tối ưu sau LIVE)
```

**Nguyên tắc vàng:** mục tiêu là **KH launch được sớm**. Đẩy tới GO LIVE trước; touchpoints & on-brand làm async sau. Và **không phải lúc nào cũng CS làm hộ** — nhiều KH muốn tự làm, mục tiêu là *thúc KH launch nhanh* dù ai bấm nút (xem §5).

---

## 1. Scope — Khi nào áp dụng DFY

**Eligibility (đồng thời thỏa cả 2):**
1. MC thuộc nhóm **Trial hoặc Paying Advanced trở lên**.
2. MC thuộc ít nhất một trong các nhóm store sau:
   - **New install** — cài app trong vòng 30 ngày, chưa kịp setup hoàn chỉnh
   - **Not launched** — loyalty program chưa live (**còn sandbox**, widget ẩn, page chưa accessible, hoặc không có earning program nào active)
   - **Launched but missing nhiều thứ** — đã live nhưng còn thiếu nhiều mảnh (chưa có redeeming, thiếu touchpoints, widget lạc tông / chưa on-brand, chưa có loyalty page…)
3. Message Crisp inbound có intent liên quan **setup / customize / hiển thị / earning / redeem / go-live** — hoặc CS chủ động phát hiện store thuộc nhóm trên khi xử lý case khác

> CS đánh giá Crisp message → nếu match intent + plan trả phí → tự tạo ticket trong section "Done for You". Keyword list có thể mở rộng dựa trên data thực tế.

**KHÔNG tạo ticket DFY:**
- MC đã có ticket DFY active (status ≠ Adopted/No Adoption) → CS update ticket cũ thay vì tạo mới

---

## 2. Phân mức theo plan — CS làm tới đâu với program

Earning/redeeming đụng vào **logic điểm & tiền** của KH, nên mức can thiệp khác nhau theo giá trị KH:

| Plan | Earning / Redeeming | Widget & Touchpoints |
|------|---------------------|----------------------|
| **Starter / Essential** | CS **review + đề xuất** rule nên bật (chat/email), KH tự enable. CS có thể bật giúp rule preset an toàn (signup, place order) nếu KH đồng ý trong chat. | CS setup trực tiếp (nếu chưa live) |
| **Advanced trở lên** | CS **setup full thay KH** theo preset recommended, hoặc forward TS nếu phức tạp (tiers, custom rules, expiration). CS loop lại verify. | CS setup trực tiếp / forward TS |

> **Luôn luôn:**
> - **Không tự đổi giá trị điểm/tiền của rule đang chạy** (vd store để 1$ = 5 points thì không tự đổi thành 1$ = 1 point) — chỉ đề xuất. Chỉ setup mới rule còn trống.
> - **Bật live mode = LUÔN xin KH gật trước**, mọi plan (xem §3 bước 4). Đây là công tắc launch thật, khách bắt đầu tích điểm thật.

---

## 3. Flow thao tác phía CS

Mạch CS cầm để làm — từ nhận chat tới đóng ticket.

### Bước 0 — Phát hiện & đánh giá eligible
CS nhận chat / rà store → check 2 điều kiện §1. Match + plan trả phí → vào flow.

### Bước 1 — Mở Quickstart của store + đọc trạng thái
CS mở **Quickstart trong app của store** (Basic/Advanced — để CS/KH tự chọn mode phù hợp) → đọc ngay 2 tín hiệu:
- Quickstart đang **x/8 (Basic)** hay **x/20 (Advanced)** → biết KH đứng đâu, còn thiếu bước nào
- **⭐ Store còn Sandbox hay đã Live mode?** — đây là công tắc launch. Widget đẹp + program active nhưng **còn sandbox = CHƯA LIVE thật**.
- Earning / Redeeming đã active chưa? Widget đã hiện chưa? Loyalty page có chưa?

> Đây thay cho "audit store" cũ. **Quickstart % + sandbox status** = 2 thứ CS đọc đầu tiên.

### Bước 2 — Đọc tín hiệu KH → chọn chế độ (xem §5)
| KH muốn | Chế độ |
|---------|--------|
| "làm hộ tôi luôn" | **DFY full** — CS thao tác |
| "tôi tự làm được" | **DFY-guided** — CS chỉ bước kẹt, KH tự bấm |
| chưa rõ / im | **Nudge** → chỉ store kẹt ở đâu, hỏi lại |

### Bước 3 — Tạo ticket + gắn label
Click button **[DFY]** trong Crisp (hoặc prompt TS agent qua extension) → ticket auto-gen kèm checklist §7.
- DFY full → label `DFY-new` → khi bắt tay làm đổi `DFY-in-progress`
- DFY-guided → label `DFY-guided`

### Bước 4 — Thực thi theo thứ tự → LIVE trước
Làm **đúng thứ tự này**, dừng báo KH ngay khi tới GO LIVE:

```
① Program Rules   → earning + redeeming active
                    (Starter/Essential: đề xuất, KH gật; Advanced+: CS bật/forward TS)
② Widget hiển thị → brand color + setup widget (widget hiện trên store) + loyalty page
🚀 GO LIVE        → Switch sandbox → live mode
                    ⚠ LUÔN xin KH gật trước khi bật → rồi báo "store LIVE 🎉" + xin review
─────────── mốc SLA 48H tính ở đây ───────────
③ Widget on-brand → checklist chi tiết §7 (màu/logo/font/card...) — async
④ Touchpoints     → point calculator (product/cart), visibility, account/thankyou — async
⑤ Engagement      → referral, notifications — nếu phù hợp
```

- Nếu **DFY-guided**: CS KHÔNG thao tác ①②🚀 — chỉ chỉ bước kẹt + đóng khung "còn X bước" để KH tự bấm (xem §5).
- **Không tự đổi rule điểm/tiền đang chạy** — chỉ setup rule trống.
- **Content trên store đã launch** (V3 hoặc V4 đã live): KHÔNG sửa content trực tiếp → viết đề xuất qua email recommendation. Chỉ store chưa live mới chỉnh trực tiếp.
- MC cũ đang dùng widget cũ → **tuyệt đối không ấn Switch to unified widget** nếu chưa được MC đồng ý.

### Bước 5 — Gửi kết quả
`Preview on store` → **quay video ngắn kết quả** (MC dễ follow hơn nhiều so với email dài kèm ảnh) → gửi Crisp. Convert được review → gắn `review-yes` + post ảnh/video vào comment ticket (để tính point). **Không close ticket ngay** — để mở chờ follow-up.

### Bước 6 — Follow-up sau 2–5 ngày
CS check lại store:
- **Đã Live + giữ customization** (DFY-guided: KH đã tự Go live) → `DFY-adopted` → close
- **Còn sandbox / không phản hồi** → reminder email (`!dfy-remind`) → `DFY-no-adopt` → close

### SLA & escalation
- SLA **48H** tính tới mốc **GO LIVE + báo KH** (không chờ xong widget on-brand). Quá 48H không update → escalate Liz.
- **Tính point:** follow-up đúng hạn + gắn đủ tag (`DFY-adopted`/`DFY-no-adopt`, `review-yes` nếu có) là điều kiện bắt buộc để ticket được tính point.

---

## 3b. [Ý tưởng — discuss với dev] Store Readiness Audit tool

> **Status: chưa build — spec để Liz discuss với dev.** Mục tiêu: tự động hóa **Bước 1** (đọc trạng thái store) thay vì CS mở app bấm tay từng store.

**Mục tiêu:** nhập shop domain → tool trả về trạng thái từng item launch-critical + Quickstart % + kết luận *"store còn thiếu X, Y để go-live"*. Giúp CS audit nhanh, nhất là khi làm DFY hàng loạt / proactive.

**Input:** shop domain (hoặc shop id).

**Output (đề xuất):**
```
Store: xxx.myshopify.com | Plan: Advanced | Quickstart: 6/8
─────────────────────────────────────────────
🚀 LAUNCH STATUS: SANDBOX  ← chưa go-live
① Program
   ✅ earning rules active (2)
   ❌ redeeming: chưa có option nào active
② Widget
   ✅ widget đang bật/hiển thị
   ✅ loyalty page: có
③ Touchpoints
   ❌ point calculator: off
   ⚠️ account page: off
─────────────────────────────────────────────
→ Kết luận: còn thiếu (1) redeeming option + (2) bật live mode để go-live.
```

**Tách rõ 2 loại item:**

| Auto audit được (query data) | Cần mắt người (tool không chấm thay) |
|------------------------------|--------------------------------------|
| Sandbox vs live mode | Widget có **on-brand** không (màu/font/wording hợp store) |
| Earning rule active (count) | Content từng block ổn chưa |
| Redeeming option active | Ảnh card/banner có lạc tông không |
| Widget bật/ẩn | |
| Loyalty page có/không | |
| VIP tier / referral / notifications on/off | |
| Touchpoints (point calculator, account/thankyou page) on/off | |
| Quickstart completion % | |

→ Tool lo phần trái (phần "cho chạy được" — đáng tự động nhất). Phần phải vẫn cần CS nhìn ở bước ③ widget on-brand.

**Câu hỏi cần chốt với dev:**
1. **Data source:** Joy có API / BigQuery / internal endpoint nào expose per-shop config không? (sandbox status, list active programs, widget enabled, touchpoints toggle…). Đây là điều kiện tiên quyết — không có data thì không build được.
2. Có thể **tái dùng logic Quickstart** (`checkList.js` + backend completion) để tool đọc thẳng completion state của từng item không, thay vì tự suy luận?
3. Output đẩy đi đâu: CLI cho CS / paste vào ticket / hiển thị ngay trong Crisp extension?
4. Có nên gắn với **proactive DFY** (batch audit nhiều store → lọc ra store eligible chưa launch → tạo ticket tự động) không?

---

## 4. Map DFY ↔ Quickstart app (tham chiếu)

Journey neo theo section của Quickstart trong app (source: `checkList.js`). CS dùng bảng này để biết item mình đang làm nằm ở đâu trong app KH nhìn thấy.

| Bước DFY | Section trong app | Items chính | Cần để LIVE? |
|----------|-------------------|-------------|--------------|
| **① Program** | Setup Program Rules | Enable customer accounts · **earning rules** · **redeeming rules** · custom point label · discount prefix · (VIP tier nếu store lớn) | ✅ |
| **② Widget** | Branding & Touchpoints (core) | brand color & logo · **setup widget** · create loyalty page | ✅ |
| **🚀 GO LIVE** | Launch & Optimize | **Switch sandbox → live mode** | ✅ **mốc launch** |
| **③ Touchpoints** | Branding & Touchpoints (nâng cao) | **point calculator (product/cart)** · improve visibility · account page · thankyou page | Sau LIVE |
| **④ Engagement / Advanced** | Engagement + Advanced | referral · email notifications · integrations · Shopify flow · checkout extensions | Sau LIVE |

> **Basic vs Advanced** = chỉ là view filter của cùng 1 checklist. Basic hiện các bước cốt lõi gom thành "Set up your program" + "Go live"; Advanced hiện tất cả. CS/KH tự chọn mode theo store.

---

## 5. DFY trong ca trực — Offer sao cho hợp thực tế

Trong ca trực CS xử nhiều chat song song, không thể dừng 30–40 phút setup full cho 1 KH. Quan trọng hơn: **không phải KH nào cũng muốn CS làm hộ — nhiều KH muốn tự setup.** Mục tiêu DFY trong ca không phải "làm hộ cho xong" mà là **thúc KH launch nhanh hơn**, dù họ tự làm hay CS làm.

Vì vậy offer trong ca mở hơn: **"để mình hỗ trợ mình launch"** (cho KH chọn tự làm / làm hộ), thay vì mặc định *"để mình làm hộ toàn bộ"*.

### 3 chế độ CS chọn theo ý muốn của KH

| KH muốn | Chế độ | CS làm trong ca | Track |
|---------|--------|-----------------|-------|
| "Làm hộ tôi luôn" | **DFY full** | Đẩy tới GO LIVE ngay trong chat → widget/touchpoint async | `DFY-*` thường |
| "Tôi tự làm được" | **DFY-guided** | KHÔNG làm hộ — chỉ bước kẹt + đóng khung gần xong + offer làm hộ dự phòng | `DFY-guided` |
| Chưa rõ / im | **Nudge** | Chỉ store đang kẹt Quickstart ở đâu → hỏi tự làm hay để CS hỗ trợ | — |

### Nhánh DFY-guided — thúc KH tự launch (hay gặp nhất, nhẹ nhất cho ca trực)

Ba đòn bẩy, dùng cùng lúc:

1. **Chỉ đúng bước kẹt trên Quickstart** — không bắt KH đọc cả journey, chỉ chỗ store đang thiếu + đường dẫn thao tác ngắn:
   > *"Quickstart của mình còn thiếu redeeming rule + chưa bật live mode. Vào **Programs → Redeem** thêm 1 option, rồi **Launch → Switch to live mode** là store chạy chính thức nha."*

2. **Đóng khung "gần xong"** — dùng chính % của Quickstart để tạo động lực:
   > *"Quickstart mình 6/8 rồi, chỉ còn 2 bước nữa là Go live được 💪"*

3. **Offer làm hộ như phương án dự phòng** — hạ rủi ro KH bỏ dở, không phải mặc định:
   > *"Nếu mình bận thì để mình bật giúp trong 2 phút cũng được nha, mình chỉ cần gật một tiếng thôi."*

### Track DFY-guided
- Vẫn tạo ticket, label `DFY-guided`, follow-up 2–5 ngày → KH đã Go live (thoát sandbox) chưa?
  - Đã → `DFY-adopted` → close
  - Chưa → nhắc lại bước kẹt + offer làm hộ lần nữa → vẫn không → `DFY-no-adopt` → close
- **Point cho DFY-guided: chưa chốt — Liz quyết sau.** Tạm thời cứ track adoption, chưa đưa vào cơ chế tính point.

### Nếu MC chọn "setup hết giúp em" (DFY full) — cần hỏi gì

Earning/redeeming là **quyết định kinh doanh của KH** (đổi ra tiền, ảnh hưởng margin) — CS không tự quyết hộ. Nhưng hỏi gọn để KH không ngại: **1 tin nhắn hỏi vài điều cốt lõi**, phần còn lại CS áp preset an toàn.

**Cần hỏi (đụng tiền / business decision):**
1. **Ngân sách reward / tỉ lệ đổi điểm** — bắt buộc. Hỏi đơn giản: *"How much of a reward would you like customers to unlock, and after roughly how much spend? (e.g. a $5 discount for every $50 spent)"*
2. **Reward muốn cho khách đổi** — % off / $ off / free shipping / free product? (mỗi loại ảnh hưởng margin khác nhau)
3. **Referral** — có muốn chạy chương trình giới thiệu bạn bè không (thưởng cả người giới thiệu + người được giới thiệu)?
4. **VIP tier** — muốn chia hạng thành viên (VIP tiers) hay chỉ 1 mức điểm phẳng?
5. **Chương trình đang chạy ở app cũ** (nếu migrate) — để không phá / trùng.

**KHÔNG cần hỏi — CS tự áp preset / lấy từ store:**
- Signup bonus, place-order rate (áp preset an toàn: +100đ signup, 1$ = 1 điểm)
- Màu / logo / brand (lấy từ store, chỉ confirm nếu cần)
- Cấu trúc block widget, wording mặc định

> Template hỏi gom 1 tin (English, tone Avada):
> *"Happy to set it all up for you! Just a few quick questions so it fits your store:*
> *1) What reward would you like customers to redeem — a % off, $ off, free shipping, or a free product? And roughly how much spend should earn it? (e.g. $5 off per $50 spent)*
> *2) Want a referral program (reward customers for referring friends)?*
> *3) Do you want VIP tiers (membership levels), or a single flat points program to start?*
> *I'll handle everything else with sensible defaults and match your store's branding."*

### CS chủ động offer — mức "chủ động + proactive outreach"

DFY **không chờ KH hỏi** — CS chủ động ở 2 kênh:

1. **Inbound (trong chat):** bất kỳ chat nào, CS thấy store eligible (§1) → chủ động offer (`!dfy-offer`), kể cả khi KH đang hỏi việc khác. Xử xong việc KH hỏi trước, rồi mới offer — không chèn ngang.
2. **Outbound (proactive outreach):** CS / tool §3b quét store eligible **chưa launch** (còn sandbox, thiếu program) → chủ động nhắn KH trước, offer setup giúp. Đây là hướng gắn với tool audit + Proactive Care.

> **Lưu ý outreach:** ưu tiên store **Trial sắp hết hạn** hoặc **Advanced mới cài chưa launch** — đúng nhóm cần đẩy go-live gấp nhất. Không spam store đã launch ổn.

---

## 6. Conversation flow với KH — nói gì trong chat

Checklist chi tiết là **góc nhìn nội bộ của CS**. Với KH journey chỉ có **2 nhịp**: **"bật cho LIVE trước"** → **"làm đẹp + tối ưu sau"**. Đừng làm KH thấy phải đi qua nhiều "giai đoạn".

> Template gửi KH = **tiếng Anh**, theo tone `_identity/tone-and-voice.md` (friendly, concise, teammate-not-robot). Dưới đây là mẫu CS copy thẳng cho merchant.

**① Offer** (`!dfy-offer` / `!v4-rcm`) — mở, cho KH chọn tự làm / làm hộ:
> *"Hi [name], I noticed you're using Joy on your store. We offer free setup help to get your loyalty program live and looking on-brand. Happy to help you launch — would you like to set it up yourself with a quick guide, or should I do it for you?"*

**② Quick audit + đặt kỳ vọng** — nói thẳng Quickstart còn thiếu gì + còn sandbox chưa:
> *"I took a quick look — your widget is set up, but there's no earning/redeeming program running yet and the app is still in sandbox mode, so customers can't earn real points yet. Let's get the program turned on and switch your store to live first, then I'll fine-tune the widget to match your brand."*

**③ Đẩy tới GO LIVE 🎉** — mốc "win", cũng là lúc xin review tốt nhất. **Xin KH gật trước khi bật live:**
> *"Your program is all set up. Shall I switch your store to live mode now so customers can start earning and redeeming real points? Once it's on, your loyalty program is officially running 🎉"*
>
> - **Starter/Essential:** rule điểm/tiền → đề xuất, KH gật rồi bật. *"Here's what I'd suggest: +100 points for signup, $1 = 1 point, 100 points = a $5 discount. Want me to set it up this way?"*
> - **Advanced+:** CS bật full theo preset / forward TS, báo lại kết quả.

**④ Touchpoints + widget on-brand — offer thêm, làm async:**
> *"I'll fine-tune the widget to match your store's colors and brand, and send you a short video once it's done today. I'll also enable a few extra touchpoints — like showing points right on your product and cart pages — to make it easier for customers to use."*

**⑤ Follow-up (reminder nếu KH chưa go live)** — email `!dfy-remind`:
> *"Hi [name], just checking in — your loyalty program is set up and ready. Whenever you're ready, switch it to live mode (Quickstart > Launch > Switch to live mode) and your customers can start earning points. Let me know if you'd like me to turn it on for you."*

**⑥ Gửi kết quả + Follow-up** — quay video (`Preview on store`) gửi Crisp → follow-up 2–5 ngày như §3.

### Lưu ý khi dẫn KH
- **Luôn báo mốc LIVE rõ ràng** sau khi bật live mode — đó là giá trị KH cảm nhận ngay + điểm xin review.
- **Không liệt kê việc CS làm theo phase** cho KH — chỉ nói kết quả KH nhận được ("chạy chính thức", "hợp brand", "khách dễ đổi điểm").
- **Cố gắng đẩy tới GO LIVE ngay trong chat** khi KH online. Widget on-brand + touchpoints làm async trong ngày, gửi video sau.
- Nếu KH không online đủ lâu để chốt GO LIVE → set sẵn program (nếu eligible) nhưng **để KH tự bật live hoặc hẹn xác nhận** (không tự bật live khi chưa có KH gật), báo qua email, hẹn customize sau.

---

## 7. Checklist widget on-brand (chi tiết — bước ③, treo dưới item "Setup widget")

Đây là phần chi tiết của item **"Setup widget"** trong app — CS dùng khi làm bước ③ widget on-brand (sau khi store đã LIVE, hoặc trực tiếp nếu store chưa live). Ticket auto-generate kèm checklist này.

Mục tiêu không phải tick hết — mà làm widget **trông như một phần tự nhiên của store**. Đọc brand store (màu, font, phong cách) trước rồi mới làm.

> Chi tiết "nên làm gì" từng item + ví dụ store thật: xem Notion **"Joy DFY Best practices"**.

### Required (on-brand core)
- [ ] Primary / button / text color phù hợp brand, độ tương phản tốt
- [ ] Logo ở widget header (nếu logo pro, phù hợp)
- [ ] Header background image (nếu phù hợp — ưu tiên ảnh từ store)
- [ ] Loyalty program name (Brand name + Rewards/Club)
- [ ] Point icon đã custom hợp lý
- [ ] Font inherit từ store font
- [ ] Card border (có/không tùy store — chỉnh weight + màu phù hợp)
- [ ] Point label phù hợp brand
- [ ] Login with Shop bật nếu store enable (chưa enable → recommend MC)
- [ ] Drawer type (drawer / floating drawer để fully display program)
- [ ] Button shape giống button ở store
- [ ] Content từng block viết lại on-brand (đặc biệt welcome message — có thể dùng AI onbrand)
- [ ] Referral banner image nếu store chạy referral
- [ ] Membership card image — Guest view
- [ ] Membership card image — Member view
- [ ] Ảnh member profile avatar sau khi login
- [ ] Footer menu match settings
- [ ] Recommended products — hover đổi ảnh (match behavior với store)
- [ ] Ẩn các block không cần thiết
- [ ] Program order sort hợp lý

> ⚠ **Content/text trên store đã launch:** Point label + Content từng block chỉ đổi TRỰC TIẾP khi store CHƯA live. Store đã live (V3 hoặc V4 đã live) → KHÔNG đổi trực tiếp, viết đề xuất trong email recommendation.

### Recommended (CS tự đánh giá)
- [ ] My coupon images
- [ ] Ways to earn / redeem images (cân nhắc — nhiều ảnh quá gây rối, đẩy program xuống dưới fold)
- [ ] Tier icon custom theo từng tier
- [ ] Tier banner custom theo store

### Touchpoints (bước ④ — Branding & Touchpoints nâng cao, làm sau LIVE)
- [ ] **Point calculator** — hiển thị "mua đơn này được X điểm" trên product/cart page (`Show point rewards on product and cart pages`)
- [ ] **Improve loyalty program visibility** — tăng độ hiển thị của program trên store
- [ ] **My Account page** — hiển thị điểm & rewards trong trang tài khoản khách
- [ ] **Thankyou page** — nhắc điểm vừa tích sau khi mua
- [ ] Các touchpoint hiển thị **on-brand**, không phá layout store → không phù hợp store thì skip + ghi note

### Bonus
- [ ] Video walkthrough / explain gửi KH
