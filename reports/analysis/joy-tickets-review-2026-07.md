# Joy Loyalty — Review ticket tháng 7 → case train Joyce

> **Kỳ:** 01/07 → 15/07/2026 · **Nguồn:** Avada Ticket API (`fetch_tickets.py --app joy`) · **Tổng:** 241 ticket (217 open / 24 closed) · **KB đối chiếu:** cs2.avada.net agent `joy-loyalty-agent` (66 file)
>
> Mục đích: tìm issue LẶP LẠI mà bot Joyce trả lời được → đóng thành case → patch KB. Đã loại bỏ [ONB] và customize per-store (không train được).

---

## 1. Phân bố theo nhóm (volume)

| Nhóm | ~# ticket |
|---|---|
| Redeem / discount / coupon | 48 |
| VIP Tier (reset / perk / tag / threshold / migrate tier) | 41 |
| Integration (Klaviyo / Omnisend / Judge.me / pixel / sync) | 38 |
| Widget customize/position (per-store — phần lớn không train) | 28 |
| Points không cộng / cộng sai / adjust / expire | 25 |
| Loyalty page customize/design (per-store) | 18 |
| Widget **bug** (không show / overlap / launcher reset / label) | 17 |
| Translation / multi-language | 15 |
| Onboarding [ONB] (không train) | 14 |
| Migration (Smile.io → Joy) | 10 |

---

## 2. Case nên đóng để train Joyce (đã dedupe giữa các cluster)

### 🔴 Ưu tiên cao — GAP, lặp ≥3 ticket, KB chưa có

| # | Case | Nhóm | #tk | KB file | Tickets |
|---|---|---|---|---|---|
| G1 | **VIP tier reset hàng loạt về Bronze** sau khi merchant đổi threshold / re-launch (re-run assessment theo rule mới) | VIP | 4 | `kb/case/vip-tiers.md` | #261468 (URGENT), #261488, #261463, #261435 |
| G2 | **Re-launch tier tính lại toàn bộ lifetime**, bỏ qua start date → khách nhảy sai tier | VIP | 3 | `kb/case/vip-tiers.md` | #261435, #261540, #261549 |
| G3 | **Bulk import points + status + tier** — phải **sync Shopify customers TRƯỚC** + **không trigger entry reward** | VIP/Migration | 6 | `kb/reference/migration.md` | #261444, #261443, #261423, #261416, #261470, #261493 |
| G4 | **Launcher/widget tự reset vị trí** sau khi mở rồi close (CSS custom bị Unified widget ghi đè khi re-render) | Widget | 4-5 | `kb/case/widget.md` | #261605, #261604, #261561, #261429, #261421 |
| G5 | **App pixel Disconnected** trên Shopify Customer Events, nút Connect chỉ redirect ⚠️ *sẽ tăng volume do deadline Shopify 26/8* | Integration | 3 | integrations (mới) | #261544, #261414, #261396 |
| G6 | **Deactivate coupon KHÔNG refund points** (Revoke mặc định trả điểm — merchant hỏi cách ngược lại + bulk deactivate) | Redeem | 3 | `kb/reference/redeeming-programs.md` | #261584, #261536, #261614 |
| G7 | **Redeem trả màn trắng / mã không hiện / widget mất khi login** (app embed off / segment exclude) | Redeem | 3 | `kb/case/points-redeeming.md` | #261495, #261434, #261580 |
| G8 | **Program/redeem description không update** trên loyalty page dù đã set/dịch (cache / sai field / biến không render) | Redeem/Translation | 4 | `kb/reference/redeeming-programs.md` | #261585, #261584, #261574, #261384 |

### 🟡 Ưu tiên trung — PARTIAL, bổ sung nhánh vào case sẵn có

| # | Case | Nhóm | #tk | KB file |
|---|---|---|---|---|
| P1 | **Điểm không cộng do login qua Shop app** (không phải customer account web → widget/signup path không trigger) | Points | 3 | `kb/case/points-earning.md` |
| P2 | **VIP tier points ≠ point balance** — không auto-recalc sau adjust/reset (2 chỉ số tách biệt) | VIP/Points | 2+ | `kb/case/vip-tiers.md` |
| P3 | **Widget/text không dịch TRƯỚC khi login** (guest view; thường do Translate & Adapt meta override) | Widget/Translation | 3 | `kb/case/widget.md`, `kb/reference/translations.md` |
| P4 | **Redeem inline ở cart drawer 3rd-party** không attach (how-to lặp: xin theme access → team add CSS selector) | Redeem | 6 | `kb/reference/cart-drawer.md` |
| P5 | **Perk/tier discount không auto-apply** vào cart cho một số customer (điều kiện eligibility / combine / free-product không gen code) | VIP/Redeem | 3 | `kb/reference/redeeming-programs.md` |
| P6 | **Migrate từ Smile: logic tier-spending không khớp** → cần team replicate + book call | Migration | 2 | `kb/reference/migration.md` |
| P7 | **Klaviyo:** trigger thiếu → disconnect/reconnect re-stream; variable `n/a` do nhầm `person\|lookup` vs `event\|lookup` | Integration | 4 | `kb/reference/integrations-email.md` |
| P8 | **Adjust points không xuống âm** (chỉ về 0); **expire points** troubleshoot; **earn sai rate** do đổi rate sau khi đặt đơn (rate locked lúc order) | Points | 3+ | `kb/case/points-earning.md`, `kb/reference/points-advanced.md` |

### ⚪ Bỏ — bug 1-lần cần dev, KHÔNG train (~15 ticket)

#261458 (€270 duplicate coupon, cần bồi thường → escalate Liz), #261490/#261514 (variable dynamic không render), #261422 (POS 26pt vs app 23pt rounding), #261473 (birthday reward $0), #261564 (currency `$` lỗi tiếng Trung), #261350 (earning rate trống ở rule), #261439 (redeemed discount hiển thị sai), #261417 (Swym integration redirect), #261562 (membership status discrepancy), #261581 (search customer lỗi 500), #261607 (CSS logo tier + translation), #261559 (rename SMS label), #261548 (design tab preview lệch), #261507 (export thiếu field), #261449 (excluded customer vẫn thấy block).

---

## 3. Chi tiết Q-variants + answer chuẩn (dùng để soạn patch KB)

### G1 — VIP tier reset hàng loạt về Bronze
**Q:** "All my customers' tiers got reset to Bronze today" / "Sau khi import spend files thì mọi người tụt tier thấp nhất" / "Đổi threshold xong existing customer đều về Bronze."
**A:** Root cause: đổi threshold / đổi calculation rule / re-launch VIP Tier → hệ thống **re-run tier calculation** toàn bộ customer theo threshold MỚI. Threshold mới cao hơn giá trị hiện có → phần lớn tụt tier thấp nhất. Không mất data, chỉ là re-assessment.
Kiểm tra: (1) merchant vừa đổi threshold/rule/re-launch? lúc nào? (2) metric đang dùng (Points earned / Amount spent / Orders) — nếu Amount spent mà spend chưa sync đủ từ Shopify → tính thiếu. (3) có import file tier song song ghi đè không.
Escalate nếu threshold KHÔNG đổi mà vẫn reset, hoặc cần khôi phục tier cũ → gửi store URL, thời điểm, threshold cũ/mới, ảnh setting.

### G2 — Re-launch tier tính lại từ đầu, bỏ qua start date
**Q:** "Re-launched tiers với start date 1/7 nhưng order từ 30/6 vẫn tính vào tier points" / "Re-launch đẩy customer lên Gold thay vì Basic."
**A:** Kỳ vọng: sau reset, tier point tính từ **start date**. Nhưng khi chỉnh setting rồi re-launch, hệ thống hiện có xu hướng **recalculate toàn bộ lifetime** (cả order trước start date) → nhảy sai tier. Đây là known behavior/bug đang escalate.
Kiểm tra: Assessment cycle start date + thời điểm re-launch; order nào tính sai (email + ngày); calculation rule.
Escalate: cần TS/dev — gửi customer email ví dụ, start date, tier hiện tại vs đúng, ảnh setting. Merchant thường muốn reset tier point + downgrade đúng tier.

### G3 — Bulk import points + status + tier
**Q:** "Import file này để update points + set status member" / "Migrate points/tier từ file" / "Lọc guest có balance >0 → member, import tier, đừng trigger entry reward."
**A:** Bulk data op → luôn cần TS. Checklist trước khi escalate: (1) **Sync Shopify customers TRƯỚC** — nếu file >1k mà Joy chỉ hiện vài customer thì phải sync trước (vd #261423 chỉ hiện 6/1000+). (2) Scope rõ: import points / update status guest→member / import tier (amount spent = milestone từng tier). (3) Hỏi **có trigger entry reward khi assign tier không** (đa số muốn KHÔNG). (4) Import bổ sung lần sau không double-count.
Escalate: gửi file mới nhất + 3 scope + flag "no entry reward" + đã sync Shopify chưa.

### G4 — Launcher/widget tự reset vị trí sau close
**Q:** "Custom launcher position bằng CSS nhưng mở/đóng widget xong nó nhảy về default" / "Widget button đổi vị trí sau khi mở đóng trên mobile" / "Add CSS move widget up trên unified widget nhưng reset."
**A:** Root cause: custom vị trí bằng CSS ngoài (theme custom CSS / CSS Classic cũ) → Unified widget re-render launcher sau khi đóng và ghi đè về default. Hành vi của widget mới.
Xử lý: (1) confirm Widget v4/Unified. (2) Vị trí cơ bản → dùng built-in **Settings → Launcher → Alignment** (không bị reset). (3) CSS custom phải đặt trong **Advanced → Custom CSS** của widget editor (KHÔNG phải theme CSS ngoài). (4) Vẫn reset sau khi đặt đúng chỗ → escalate kèm loom + device + URL + đoạn CSS.

### G5 — App pixel Disconnected trên Customer Events
**Q:** "Joy app pixel Disconnected dưới Shopify Customer Events, bấm Connect chỉ redirect về Joy dashboard" / "Nút Connect ở App pixels không làm gì cả."
**A:** Root cause: Web Pixel của Joy hiển thị Disconnected; nút Connect không kích hoạt. Thường liên quan re-authorization (cấp lại scope) nhưng UI Shopify không có chỗ connect manual rõ → đa số cần team recreate pixel backend.
Xử lý: (1) confirm vị trí Checkout Settings → Tracking and analytics → App pixels. (2) thử re-authorize Joy app. (3) vẫn Disconnected → escalate recreate pixel, kèm store URL + screenshot + video nút Connect. ⚠️ *Ưu tiên viết sớm — deadline Shopify migration 26/8 sẽ tăng volume.*

### G6 — Deactivate coupon KHÔNG refund points
**Q:** "Vô hiệu hoá mã của 1 customer NHƯNG không hoàn điểm (Revoke thì tự trả điểm)" / "Remove hết coupons mà không refund, để khách redeem lại bằng program mới."
**A:** Root cause: **Revoke coupon** (Customers → [name] → Revoke) mặc định trả coupon chưa dùng về points — đúng thiết kế. Không có toggle "deactivate không trả điểm" hay bulk-deactivate.
Xử lý: để vô hiệu hoá mã mà không trả điểm → **deactivate trực tiếp trong Shopify → Discounts** (không dùng Revoke). Lưu ý trạng thái mã trong Joy có thể chưa tự update thành Expired. Bulk deactivate không refund → không có UI self-serve, escalate kèm danh sách/điều kiện.

### G7 — Redeem trả màn trắng / mã không hiện / widget mất khi login
**Q:** "Bấm Redeem points thì màn trắng, không hiện mã dù hệ thống đã tạo" / "Customer login thì widget/redeem biến mất, logout lại thấy" / "Widget blank không redeem được."
**A:** Root cause: (1) **app embed bị disable** (Joy Redeem inline / widget embed off → blank), (2) segment/member flag ẩn widget với customer đang login, (3) app bug render.
Xử lý: (1) check app embed đã bật trong Theme Editor (đặc biệt "Joy: Redeem in line"). (2) hỏi store URL + email, so logged-in vs logged-out. (3) check segment assignment. (4) embed đúng mà vẫn blank → escalate kèm session/loom.

### G8 — Description không update trên loyalty page
**Q:** "Set description với biến `{{earning_point_raw}}` nhưng loyalty page không update" / "Description không translate dù Translation đã dịch hết" / "Lỗi description khi tạo Discount amount redeem program."
**A:** Root cause: (1) loyalty page cache chưa refresh, (2) sai field (program-level vs Translation-level), (3) biến `{{...}}` không render trên published page.
Xử lý: (1) confirm lưu description đúng nơi (program setup vs Translation) + re-launch/clear cache + hard refresh. (2) đã set đúng field + reindex mà biến vẫn không render → app bug, escalate kèm program + loyalty page URL.

### P1 — Điểm không cộng do login qua Shop app
**A:** Signup bonus chỉ cấp qua 3 path: login customer account **web** + widget bật / join qua widget popup / POS khi guest được identify là member. **Login qua Shop app** (không phải account web) → widget storefront không detect session → không trigger. Nếu khách đã nhận place-order point mà thiếu signup point + login qua Shop app → xác nhận nguyên nhân này, cấp thủ công qua Customers → adjust points. Escalate nếu cần cấp cho toàn bộ khách cũ.

### P2 — VIP tier points ≠ point balance
**A:** **VIP tier points** và **point balance** là 2 chỉ số riêng — reset/adjust balance **không** tự recalc tier points. Sau reset balance qua CSV/adjust, tier points vẫn giữ giá trị lũy kế cũ. Không có toggle self-serve recalc → escalate với store URL + email + program + kỳ vọng.

### P3 — Widget không dịch trước khi login
**A:** Bản dịch apply theo language context của session. Guest (trước login) có thể không nhận đúng language nếu store dùng **Translate & Adapt** can thiệp meta/language; sau login Joy có context đúng nên hiển thị đúng. Xử lý: confirm đã điền dịch tại Settings → Translations → Storefront blocks/Widget; hỏi có dùng Translate & Adapt + meta override không; test guest vs sau login; đã dịch + không app thứ ba mà guest vẫn English → escalate kèm ảnh trước/sau login.

### P4 — Redeem inline ở cart drawer 3rd-party
**A:** Redeem-in-line là app embed riêng, bind vào **native cart drawer selectors** → không tự chạy với cart drawer app thứ 3 (qikify, PageFly, swatches-popup-cart) hay page builder. Native: On-site content → Product page → Redeem in Cart Drawer → Edit in Theme Editor → bật "Joy: Redeem in line". 3rd-party: xin theme access + app permission → escalate team add CSS selector khớp nút cart theme đó. Muốn redeem full balance: Dynamic discount + xoá Maximum points per redemption.

### P5 — Perk/tier discount không auto-apply
**A:** Privilege/perk auto-apply mỗi qualifying order khi customer ở tier (khác entry reward 1 lần). Không apply cho một số customer cùng tier → check: (1) customer logged-in đúng account + đúng tier; (2) eligibility conditions (min spend, product/collection eligible); (3) Free product perk cần product còn eligible/còn hàng; (4) plan Advanced+. Free-product không gen code / apply lệch giữa customer cùng tier → escalate kèm 2 email (work + không-work) + tier + product URL + ảnh setting.

### P6 — Migrate Smile: logic tier-spending không khớp
**A:** Joy map tier theo total spending / points earned khi migrate, nhưng công thức Smile có thể khác (lifetime spending, thời điểm reset). Sau import tier lệch nếu rule chưa khớp. Thu thập: Smile tính tier theo gì, ngưỡng từng tier, 1-2 customer sai để đối chiếu → escalate team replicate logic. Enterprise yêu cầu call → gom yêu cầu, đề xuất book call, không hứa giải quyết ngay trên chat.

### P7 — Klaviyo trigger thiếu / variable n/a
**A:** (a) Trigger thiếu → confirm Integrations → Klaviyo Connected; các event: Joy Earn Point, Redeem Points, Tier Achieved, Points Eligible Reward, Birthday, 7 Days Pre Point Expiration. Không thấy → disconnect + reconnect (API key mới) re-stream. (b) Variable `n/a`/sai giá trị → nhầm loại lookup: balance (profile) = `{{ person|lookup:'Joy Loyalty Points' }}`; điểm mang theo event = `{{ event|lookup:'Customer points' }}`. Dùng `event|lookup` không phải `person|lookup`. (c) coupon name / dedicated "Reward Expiring" event = feature request, chưa có.

### P8 — Adjust / expire / earn rate
**A:** (1) **Adjust không xuống âm** — chỉ về tối thiểu 0 (giới hạn thiết kế); adjust về 0 = xóa điểm khả dụng của riêng customer đó, không phải reset toàn shop. (2) **Expire**: check loại expiration (Full inactivity / Fixed date / FIFO); "trừ hết sớm" thường do setting đổi trước đó hoặc mốc inactivity tính từ lần earn cũ; ngày expire không khớp logic → escalate. (3) **Earn sai rate**: điểm locked theo rate lúc order được ghi nhận, không phải lúc fulfill — đơn đặt TRƯỚC khi đổi rate vẫn áp rate cũ (expected). Đơn đặt SAU khi đổi rate mà vẫn rate cũ → escalate kèm order + email + thời điểm đổi rate.

---

## 4. Bước tiếp theo (khi Liz duyệt)

1. Soạn patch vào KB file tương ứng trên cache `/tmp/kb-sync/joy/` (mỗi case = 1 chunk có Q-variants + answer + escalation guidance).
2. Liz duyệt diff.
3. Push qua `skills/kb-sync/scripts/push_kb.py` (auto git commit) + reindex `joy-loyalty-agent`.
4. Test lại vài case bằng chat test endpoint trước khi kết luận.

> Ưu tiên viết G5 (app pixel) sớm nhất vì deadline Shopify migration 26/8 sẽ đẩy volume nhóm này lên.
