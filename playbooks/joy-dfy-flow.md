# Joy DFY — CS Flow & Checklist

**Owner:** Liz (CS Leader)
**Created:** 2026-05-18
**Updated:** 2026-06-30

> Xem mục đích & tinh thần DFY: [`joy-dfy-intro.md`](./joy-dfy-intro.md)

---

## 0. Đổi gì ở bản này (2026-06-30)

DFY trước đây gần như chỉ xoay quanh **widget customization**. Nhưng widget đẹp mà store **chưa có earning/redeeming program active** thì khách vẫn không kiếm được điểm → program không thực sự launch được. Bản này mở rộng journey ra toàn bộ con đường để KH **go-live thật**, chia 3 giai đoạn theo đúng thứ tự ưu tiên:

```
Phase 1 — LAUNCH      → store đủ điều kiện go-live (earning + redeeming + widget visible)
Phase 2 — BRAND       → widget on-brand, trông như một phần tự nhiên của store
Phase 3 — OPTIMIZE    → conversion touchpoints (cart drawer redeem, point calculator…)
```

**Nguyên tắc vàng:** mục tiêu là **KH launch được sớm**. Phase 1 là bắt buộc để store LIVE — làm xong Phase 1 là KH đã có thể chạy program. Phase 2 & 3 nâng chất lượng và conversion, làm tiếp khi có thời gian / phù hợp store.

---

## 1. Scope — Khi nào áp dụng DFY

**Eligibility (đồng thời thỏa cả 2):**
1. MC đang dùng app và ở Widget V4 (unified widget).
2. MC thuộc ít nhất một trong các nhóm store sau:
   - **New install** — cài app trong vòng 30 ngày, chưa kịp setup hoàn chỉnh
   - **Installed but not launched** — cài lâu nhưng loyalty program chưa live (widget ẩn, page chưa accessible, **hoặc không có earning program nào active**)
   - **Launched but not on-brand** — đã live nhưng widget chưa match theme store (màu, font, wording, icon lạc tông)
3. Message Crisp inbound có intent liên quan **setup / customize / hiển thị / earning / redeem** widget hoặc loyalty program — hoặc CS chủ động phát hiện store thuộc nhóm trên khi xử lý case khác

> CS đánh giá Crisp message → nếu match intent + plan trả phí → tự tạo ticket trong section "Done for You". Keyword list có thể mở rộng dựa trên data thực tế.

**KHÔNG tạo ticket DFY trong các trường hợp:**
- MC đã có ticket DFY active (status ≠ Adopted/No Adoption) → CS update ticket cũ thay vì tạo mới

---

## 2. Phân mức theo plan — CS làm tới đâu với program

Earning/redeeming đụng vào **logic điểm & tiền** của KH, nên mức can thiệp khác nhau theo giá trị KH:

| Plan | Earning / Redeeming program | Widget & Touchpoints |
|------|------------------------------|----------------------|
| **Starter / Pro** | CS **review + đề xuất** rule nên bật (qua chat/email recommendation), KH tự enable. CS có thể bật giúp các rule preset an toàn (signup, place order) nếu KH đồng ý trong chat. | CS setup trực tiếp (nếu V4 chưa launch) |
| **Advanced trở lên** | CS **setup full thay KH** theo preset recommended, hoặc forward TS nếu cấu hình phức tạp (tiers, custom rules, expiration). CS loop lại verify. | CS setup trực tiếp / forward TS |

> Với mọi mức: **không bao giờ tự ý đổi giá trị điểm/tiền của rule đang chạy** (vd: store đang để 1$ = 5 points thì không tự đổi thành 1$ = 1 point) — chỉ đề xuất. Chỉ setup mới các rule còn trống.

---

## 3. CS audit — Nhìn toàn diện store trước khi vào flow

Trước khi bắt đầu, CS cần có cái nhìn tổng thể về store — không chỉ widget. Audit theo đúng thứ tự 3 phase:

**① Program (Phase 1 — quan trọng nhất):**
- Có **earning rule** nào active chưa? (signup, place order là tối thiểu để khách bắt đầu kiếm điểm)
- Có **redeeming option** nào chưa? (khách có điểm mà không có gì để đổi → program vô nghĩa)
- Program đã **publish / active** chưa, hay đang ở draft?

**② Widget (Phase 2):**
- Widget có **đang hiển thị trên store** không (visible, không bị ẩn)?
- Đã on-brand chưa (màu, font, wording, icon)?

**③ Loyalty page:**
- Chưa có → recommend MC tạo — điểm chạm quan trọng để convert, thiếu page là thiếu một kênh
- Có rồi nhưng chưa on-brand → offer customize, đặc biệt MC Advanced trở lên → forward TS xử lý, CS loop lại verify

**④ Conversion touchpoints (Phase 3):**
- Redeem in cart drawer đã bật chưa? Point calculator? Các điểm chạm này có match store không?

**Các element khác** (popup, launcher, account page…) — mention nếu thấy lạc tông hoặc chưa setup, nhưng không cần đi sâu trong DFY flow

---

## 4. CS Flow — Cách làm việc với MC

CS chủ động offer free white-glove service cho MC, dùng shortcut `!v4-rcm` hoặc `!dfy-offer`.

**Bước thực hiện:**

1. CS nhận chat của MC đang online → đánh giá store eligible → tạo ticket DFY bằng cách click button **[DFY]** embed trong Crisp chat hoặc prompt TS agent qua extension → ticket tự tạo kèm đầy đủ checklist 3 phase, set label `DFY-new`
2. CS audit store theo §3 → update label `DFY-in-progress` → làm theo thứ tự phase:
   - **Phase 1 trước hết** — đảm bảo earning + redeeming + widget visible để store đủ điều kiện LIVE (theo phân mức plan §2)
   - **Phase 2** — customize widget on-brand
   - **Phase 3** — bật conversion touchpoints phù hợp
3. Sau khi có kết quả, CS dùng button **Preview on store** → **quay video ngắn kết quả** (highly recommended — MC dễ follow hơn nhiều so với email dài kèm ảnh) → gửi qua Crisp
4. Done → nếu convert được review từ flow DFY: gắn thêm `review-yes` → chụp ảnh hoặc quay video post vào phần comment để phục vụ tính point → **không close ticket ngay**, để mở chờ follow-up
5. **Follow-up sau 2–5 ngày** → CS check lại store xem MC có đang dùng/giữ customization + program còn active không:
   - **Có adopt** (widget vẫn match, program vẫn chạy, MC hài lòng) → gắn label `DFY-adopted` → close ticket
   - **Chưa thấy update / MC không phản hồi** → gửi reminder email (template `!dfy-remind`) → gắn label `DFY-no-adopt` → close ticket

> SLA: Bắt buộc phải có kết quả hoàn thiện (tối thiểu **Phase 1 — store LIVE được**) và báo KH trong vòng **48H** sau khi tạo ticket. Nếu ticket quá 48H không có update → escalate Liz.

> **Lưu ý tính point:** Follow-up đúng hạn + gắn đủ tag (`DFY-adopted` hoặc `DFY-no-adopt`, `review-yes` nếu có) là điều kiện bắt buộc để ticket được tính vào points.

**Lưu ý:**
- Nếu là MC cũ (đang dùng widget cũ) → **tuyệt đối không ấn Switch to unified widget** nếu chưa được sự đồng ý của MC
- **Không tự đổi giá trị điểm/tiền** của rule đang chạy (xem §2) — chỉ đề xuất
- CS có thể show kết quả sơ bộ với MC trước để tăng khả năng xin review — sau đó hẹn MC gửi kết quả hoàn thiện sau
- CS được khuyến khích tự do sáng tạo và custom thêm cho phù hợp với store — miễn là Required items (Phase 1) đã hoàn thành

**Tips chung (xem chi tiết + ví dụ ở Notion "Joy DFY Best practices"):**
- **Đọc brand store trước khi setup:** đọc màu, font, phong cách (tối giản/sặc sỡ, cao cấp/gần gũi) rồi mới làm. Mục tiêu là on-brand, không phải tick cho hết checklist.
- **Content trên store đã launch:** store đã launch (V3, hoặc V4 đã live) → KHÔNG sửa content trực tiếp, viết đề xuất qua email recommendation. Chỉ V4 chưa launch mới chỉnh trực tiếp.
- **Lấy ảnh từ chính store của KH:** cần ảnh cho widget (header, banner, card, coupon) → ưu tiên ảnh sản phẩm/brand có sẵn trên store, không dùng ảnh stock lạc tông.

---

## 4b. Conversation flow với KH — Áp 3 phase vào chat thật

Checklist 3 phase là **góc nhìn nội bộ của CS để audit/tick**. Khi nói chuyện với KH thì KHÔNG bê 3 bảng đó ra. KH chỉ cần cảm nhận **1 mốc rõ ràng: "store của tôi đã chạy được"** — đó là sau Phase 1. Phase 2 & 3 là CS làm thêm (ngầm / async), KH không phải chờ.

> **Nguyên tắc đóng gói:** Với KH, journey chỉ có 2 nhịp — **"bật chạy được trước"** rồi **"làm đẹp + tối ưu sau"**. Đừng làm KH thấy phải đi qua "3 giai đoạn".

### Nhịp hội thoại chuẩn (trong 1 chat session)

**① Offer** — store eligible → CS offer free setup (`!dfy-offer`).
> *"Hi [name], mình thấy store mình đang dùng Joy. Bên mình có hỗ trợ setup miễn phí giúp chương trình loyalty chạy mượt + hợp với store, mình làm giúp mình luôn nha?"*

**② Quick audit + đặt kỳ vọng** — CS nói thẳng tình trạng + mục tiêu launch trước:
> *"Mình vừa xem qua, store đã có widget nhưng chưa có chương trình tích/đổi điểm nào đang chạy, nên khách chưa kiếm được điểm. Mình sẽ bật chương trình để store chạy được trước, rồi chỉnh widget cho khớp brand sau nha."*

**③ Phase 1 — bật cho chạy + báo mốc LIVE** 🎉 — đây là khoảnh khắc "win", cũng là lúc xin review tốt nhất:
> *"Xong rồi nè! Giờ khách đã có thể tích điểm khi đăng ký + mua hàng, và đổi điểm lấy mã giảm giá. Chương trình của mình đã chạy chính thức 🎉"*
>
> - **Starter/Pro:** rule điểm/tiền → đề xuất trong chat, KH gật rồi mới bật. *"Mình đề xuất: đăng ký +100đ, $1 = 1 điểm, 100 điểm = mã $5. Mình bật theo mức này nha?"*
> - **Advanced+:** CS bật full theo preset / forward TS, báo lại kết quả.

**④ Phase 2 & 3 — offer thêm, làm async** — không bắt KH chờ trong session:
> *"Mình sẽ chỉnh widget cho khớp màu + brand store mình, làm xong trong hôm nay mình gửi lại video kết quả nha. Mình cũng bật thêm vài điểm chạm như đổi điểm ngay trong giỏ hàng để khách dễ dùng hơn."*

**⑤ Gửi kết quả + Follow-up** — quay video kết quả (`Preview on store`) gửi qua Crisp → follow-up 2–5 ngày như §4.

### Lưu ý khi dẫn KH qua flow
- **Luôn báo mốc LIVE rõ ràng** sau Phase 1 — đó là giá trị KH cảm nhận được ngay, và là điểm xin review.
- **Không liệt kê việc CS sẽ làm theo phase** cho KH — chỉ nói kết quả KH nhận được ("chạy được", "hợp brand", "khách dễ đổi điểm").
- **Earning/redeeming điểm-tiền:** Starter/Pro luôn xin KH gật trước khi bật; Advanced+ CS chủ động bật theo preset. Không tự đổi rule đang chạy (xem §2).
- **1 session hay nhiều:** cố gắng xong **Phase 1 ngay trong chat** (KH online) để có mốc LIVE. Phase 2/3 làm async trong ngày, gửi video sau. SLA 48H tính theo mốc **Phase 1 hoàn thành + báo KH**.
- Nếu KH không online đủ lâu để chốt Phase 1 → bật earning/redeeming preset an toàn (nếu eligible), báo qua email, hẹn customize sau.

---

## 5. Checklist 3 phase (CS audit)

Ticket auto-generate kèm checklist này. CS tick + viết note cho từng item.

Mục tiêu của DFY không phải là tick hết checklist — mà là làm cho **program thực sự launch được** và widget **trông như một phần tự nhiên của store đó**. Làm theo thứ tự phase: Phase 1 đủ để go-live, Phase 2 & 3 nâng chất lượng.

> Chi tiết "nên làm gì" cho từng item + ví dụ store thật: xem Notion **"Joy DFY Best practices"**.

---

### 🚀 PHASE 1 — LAUNCH (Required — store phải đủ điều kiện go-live)

Đây là phần **bắt buộc để KH launch được**. Thiếu phần này thì widget có đẹp mấy program vẫn không chạy.

**Earning program**
- [ ] Có ít nhất 1 earning rule cho **acquisition**: Signup / Create account
- [ ] Có earning rule cho **core action**: Place an order
- [ ] (Tùy store) earning rule khuyến khích: Leave a review, Follow social, Birthday
- [ ] Point value của mỗi rule hợp lý (không để 0 hoặc giá trị mặc định vô nghĩa)
- [ ] Earning program đã **Active / Published** (không còn ở draft)

**Redeeming program**
- [ ] Có ít nhất 1 redeem option khách thực sự dùng được (vd: $ off / % off coupon)
- [ ] Tỉ lệ quy đổi điểm → reward hợp lý (khách đạt được trong thời gian hợp lý, không quá xa)
- [ ] Redeem option đã **Active / Published**

**Widget visible**
- [ ] Widget đang **bật và hiển thị** trên storefront (không bị ẩn / chưa publish)
- [ ] Loyalty page accessible (nếu store dùng page) hoặc launcher hiển thị đúng

> ✅ **Hoàn thành Phase 1 = store đã LIVE.** Đến đây KH đã có thể chạy program. Báo KH ngay nếu cần go-live gấp.

> ⚠ Với rule điểm/tiền: **Starter/Pro** → đề xuất, KH duyệt rồi mới bật. **Advanced+** → CS setup full theo preset hoặc forward TS (xem §2).

---

### 🎨 PHASE 2 — BRAND (Required khi có thời gian — widget on-brand)

Phần customize widget để on-brand. Đây là phần checklist cũ — giữ nguyên giá trị.

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

> ⚠ **Content/text trên store đã launch:** Point label + Content từng block chỉ đổi TRỰC TIẾP khi store ở V4 và CHƯA launch. Nếu store ở V3 hoặc V4 đã launch → KHÔNG đổi trực tiếp, viết đề xuất trong email recommendation cho KH.

**Brand — Recommended (CS tự đánh giá)**
- [ ] My coupon images
- [ ] Ways to earn / redeem images (cân nhắc — nhiều ảnh quá gây rối, đẩy program xuống dưới fold)
- [ ] Tier icon custom theo từng tier
- [ ] Tier banner custom theo store

---

### ⚡ PHASE 3 — OPTIMIZE (Conversion touchpoints — nâng conversion sau khi đã launch)

Các điểm chạm đưa loyalty vào đúng lúc khách đang mua → nâng conversion. CS tự đánh giá bật theo store, ghi note nếu skip.

- [ ] **Redeem in cart drawer** — cho khách áp điểm/đổi reward ngay trong cart drawer (đúng lúc quyết định mua)
- [ ] **Point calculator** — hiển thị "mua đơn này được X điểm" trên product/cart để kích thích mua thêm
- [ ] **Earning points on product page** — nhắc khách số điểm sẽ nhận ngay trên trang sản phẩm
- [ ] **Post-purchase / thank-you touchpoint** — nhắc điểm vừa tích được sau khi mua
- [ ] **Account page integration** — hiển thị điểm & rewards trong trang tài khoản khách
- [ ] Các touchpoint trên hiển thị **on-brand** và không phá layout store

> Touchpoint nào không phù hợp store (vd theme không hỗ trợ cart drawer) → skip + ghi note lý do.

---

### 🎁 Bonus
- [ ] Video walkthrough / explain gửi KH
