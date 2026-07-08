# Joy Support Flow — FAQ tra cứu theo domain

**Owner:** Liz (CS Leader) · **Updated:** 2026-07-08

> **File này là gì.** Sổ tra cứu khi merchant **báo một lỗi/hiện tượng cụ thể** — tìm theo domain, tự chẩn đoán, xử lý hoặc escalate đúng chỗ. Onboarding một khách mới (từ intake → launch) → xem [`joy-onboarding-flow.md`](../../playbooks/joy-onboarding-flow.md). Decision guides sâu (Migration / VIP / Guest-Member / Widget V4) cũng ở file đó (Phần 2).
>
> **Nền tảng:** phân tích 3 tháng ticket Joy (`docs/joy-ticket-analysis-q2-2026.md`). **51% ticket đã escalate lên dev KHÔNG phải bug Joy** — mà config sai, đúng-thiết-kế bị hiểu nhầm, lỗi 3rd-party, hoặc data-fix một lần. → Luôn chạy hết lăng kính triage trước khi kêu dev.

---

## Cách đọc mỗi FAQ & lăng kính triage

Mỗi case theo format: **Dấu hiệu** (khách mô tả gì) → **Tự chẩn đoán** (CS/AI check state nào) → **Cách xử lý** → **Khi nào escalate**.

**Lăng kính bắt buộc — Lỗi Joy vs Config vs 3rd-party.** Trước khi hứa "để dev fix", phân loại:

- 🟢 **Config/User-error:** sai setting, sandbox, plan-gating, chưa bật embed… → tự sửa/hướng dẫn, KHÔNG cần dev.
- 🔵 **Expected behavior:** đúng-thiết-kế nhưng khách hiểu nhầm → giải thích.
- 🟠 **3rd-party:** lỗi Shopify/Fera/Judge.me/Recharge/POS… → chỉ ra đúng thủ phạm, không nhận là bug Joy.
- 🔴 **Bug Joy thật:** đã loại 3 nhóm trên → escalate **kèm bằng chứng** (state đã check).

> 💡 Câu hỏi chẩn đoán (guest hay member, order này vì sao không earn, coupon điều kiện thật là gì) → **hỏi Joy AI agent trước** — nó đọc được state, nhanh hơn mò tay hoặc đẩy dev.

---

## A. Points / Earning

**A1. Khách mua nhưng không cộng điểm.**
→ *Chẩn:* khách **guest hay member**? `type`/`verifiedEmail` có rỗng không? (Guest = cộng 0đ âm thầm.)
→ *Xử lý:* guest → hướng dẫn đăng ký/verify; kiểm tra enrollment. 🟢 thường config/data.
→ *Escalate:* member, verified, Live mà vẫn 0đ → 🔴 kèm order id + customer.

**A2. Cả store không cộng điểm (từ một mốc thời gian).**
→ *Chẩn:* shop đang **Sandbox hay Live**? Program có bật lúc order tạo không?
→ *Xử lý:* Sandbox → hướng dẫn launch sang Live. 🟢 rất hay gặp.
→ *Escalate:* Live mà vẫn không cộng toàn store → 🔴.

**A3. Order lẻ không cộng điểm (khách khác thì có).**
→ *Chẩn:* order thỏa điều kiện earn không (min-order, exclude tax, sản phẩm loại trừ)? có snapshot lúc fulfillment? `source_name` match (đơn subscription/Recharge)?
→ *Xử lý:* do điều kiện/tax → giải thích (🔵). Shopify đổi `source_name` phá earn Recharge → 🟠/🔴 tùy.
→ *Escalate:* đủ điều kiện mà vẫn trượt → 🔴 kèm order id.

**A4. Điểm bị cộng đôi cho cùng một đơn.**
→ *Chẩn:* có race webhook↔admin / import trùng / migrate nhiều lần không?
→ *Xử lý:* xác định nguồn double; do import/migrate lặp → sửa data + dặn không migrate lại.
→ *Escalate:* nghi race engine → 🔴 (bug thật đã gặp).

**A5. Đơn thứ 2 vẫn cộng dù đáng lẽ 1 lần (sign-up/once-in-lifetime).**
→ *Chẩn:* limit/once-in-lifetime của program có enforce không?
→ *Escalate:* 🔴 nếu anti-cheat/limit không chặn.

**A6. Điểm về chậm.**
→ *Chẩn:* có backlog xử lý (PubSub) không? mới có traffic lớn/bulk?
→ *Xử lý:* thường chỉ là delay → trấn an, chờ. 🔵/🟢.
→ *Escalate:* chậm bất thường kéo dài → 🔴.

**A7. Điểm bị mất/hết hạn vô lý.**
→ *Chẩn:* có phải **FIFO expiration** tính nhầm (bỏ qua điểm đã redeem)? lô legacy 2024 thiếu field?
→ *Escalate:* con số hết hạn không khớp logic → 🔴 (đã có bug expiration).

## B. Coupon / Redeem

**B1. Mã redeem báo invalid / không apply.**
→ *Chẩn:* đọc **điều kiện thật của mã động**: min-purchase, exclude-collection, country, **channel (online-only?)**, cap, start/end.
→ *Xử lý:* phần lớn điều kiện không thỏa (vd mã online-only dùng trên POS) → giải thích (🔵/🟢).
→ *Escalate:* điều kiện thỏa mà vẫn invalid → 🔴.

**B2. Coupon Joy không được đánh "used".**
→ *Chẩn:* có discount/app khác **non-combinable** đang thắng trên cart không?
→ *Xử lý:* giải thích xung đột combinability, chỉnh combinesWith nếu cần. Thường 🟢/🔵.

**B3. Redeem trên POS không được.**
→ *Chẩn:* mã có phải **online-only**? có khách + có sản phẩm trong cart chưa (UI redeem chỉ hiện khi đủ điều kiện)?
→ *Xử lý:* giải thích điều kiện hiển thị redeem trên POS (🔵). "Failed to load" trên POS thường là **lỗi Shopify** (🟠).

**B4. Cap giảm sai (vd hiện 6% dù cap khác).**
→ *Chẩn:* giá trị cap có lưu đúng kiểu/không rỗng không?
→ *Escalate:* 🔴 nếu cap lưu sai.

**B5. Prefix mã sai (JOY- thay vì Birthday-...).**
→ *Chẩn:* program có bật dùng prefix riêng không (`isUsePrefixDiscountCode`)?
→ *Xử lý:* bật/đặt prefix trong setting (🟢). Nhắc setup prefix coupon từ đầu (branding).

**B6. Free gift hết hàng vẫn redeem được → lỗi checkout.**
→ *Chẩn:* stock thật của variant vs "inventory-not-tracked" (âm)?
→ *Escalate:* 🔴 nếu redeem được khi hết hàng.

## C. Metafield / Perk sync ⭐ gốc của nhiều "widget chết" & "perk không apply"

**C1. Perk/tier discount không apply.**
→ *Chẩn:* **tier tag + metafield mà discount function đọc đã sync chưa**? merchant **import raw hay launch/migrate**?
→ *Xử lý:* import raw → chạy resync metafield+tag hoặc dùng launch/migrate flow. 🟢/🔴 tùy.

**C2. Loyalty Hub / widget trắng, 404.**
→ *Chẩn:* `joy_loyalty` metafield có null / sai kiểu (single_line_text thay vì json)? shopId rỗng → HMAC hash lỗi?
→ *Escalate:* 🔴 (metafield corruption → widget chết), kèm shop domain.

**C3. Điểm hiển thị 0 / 1000 placeholder dù backend có điểm.**
→ *Chẩn:* email hoa/thường lệch khi build HMAC (backend lowercase)?
→ *Escalate:* 🔴 nếu hash mismatch.

**C4. Report tier có cột "None".**
→ *Chẩn:* khách có `tierName` metafield **chưa sync** (không phải "tier thứ 4").
→ *Xử lý:* resync metafield cho nhóm khách đó.

## D. Widget / V4 — nhóm category #1

**D1. Widget không hiện trên store.**
→ *Chẩn:* **app embed đã bật chưa**? metafield/hash ok? (xem C2). currency symbol có undefined không?
→ *Xử lý:* bật app embed / app block đúng chỗ (🟢 rất hay gặp).

**D2. Loyalty page blank sau khi deploy.**
→ *Chẩn:* có phải **ChunkLoadError** (min.js cache cũ đòi chunk đã purge)?
→ *Xử lý:* hard refresh/clear cache; diện rộng → 🔴 (deploy staleness).

**D3. Sau lên V4 mất config / lệch so với V3.**
→ *Chẩn:* field nào **không migrate** V3→V4 (collection-page, custom login link, Submit Receipt, survey points, birthday field, per-tier rate, page-restriction)?
→ *Xử lý:* set lại field bị rơi trong V4. **Nguồn bug #1** — nếu là gap parity thật → 🔴.

**D4. Đổi CSS ngoài không ăn.**
→ *Chẩn:* Widget V4 dùng **Shadow DOM** → CSS ngoài không xuyên vào được.
→ *Xử lý:* sửa style **trong in-app editor**, không sửa CSS theme ngoài. 🔵 (đúng-thiết-kế) — giải thích, không cần dev.

**D5. Widget crash/trắng ở một số store nhất định.**
→ *Chẩn:* currency symbol lạ (SGD/SEK/Kč/TWD) throw JS? i18n ghép chuỗi vỡ (zh/FR/DE)?
→ *Escalate:* 🔴 (currency/i18n rendering).

**D6. Muốn account icon (đăng nhập) mở widget Joy thay vì account Shopify.**
→ *Chẩn:* theme dùng header.liquid thường hay dùng web component `<shopify-account>` (theme mới)?
→ *Xử lý:* dùng **deep link `#joy-open`**. Theme đơn giản → sửa thẻ `<a>` trong `header.liquid` về `#joy-open` (app tự remove khi tắt). Theme mới `<shopify-account>` → chèn JS chặn click (capture phase) rồi set `window.location.hash='joy-open'`. ⚠️ **Không recommend thay account Shopify — chỉ làm khi KH yêu cầu.** Doc "How to make Account icon opening Joy". 🟢/🔵.
→ *Bonus:* "Login xong có quay về trang cũ không?" → **Có, out-of-the-box** (`AVADA_JOY.login_url`); đổi **custom login link** sẽ override.

**D7. Khách chưa lên được V4 / convert V4 bị lỗi.**
→ *Chẩn:* KH đang ở version nào (v1 phải qua v2→v3→v4)? convert qua UI hay dev zone?
→ *Xử lý:* ưu tiên convert qua UI (Switch to Unified); KH không tự làm được → dev-zone fallback (bật hết field version, config nhanh tránh downtime); lỗi không khôi phục → **Reset to factory**. Xem [`joy-onboarding-flow.md` §2.5](../../playbooks/joy-onboarding-flow.md). Ảnh chậm do Firebase → chuyển upload lên Shopify.

## E. VIP tier

**E1. Khách ở sai tier.**
→ *Chẩn:* amount-spent thực tế? tier hiện tại tính theo nguồn nào (auto/manual/exclusive)? startDate dùng để tính?
→ *Xử lý:* đối chiếu công thức; do định nghĩa tier → giải thích (🔵).

**E2. Khách bị downgrade tier sau khi mua/đổi setting.**
→ *Chẩn:* **có ai bấm recalc thủ công** không? có đổi công thức tier không?
→ *Escalate:* silent-demote do đổi công thức → 🔴 (không được để tụt hạng âm thầm).

**E3. Recalc chạy dở/không xong (nhiều khách bị un-tier).**
→ *Chẩn:* có ai **save setting giữa lúc recalc** không?
→ *Escalate:* 🔴 (save phá recalc job).

**E4. Perk/auto-discount của tier không apply.**
→ *Chẩn:* → về **C1** (tag/metafield tier chưa sync); import raw hay launch/migrate?

**E5. Widget hiện sai ngưỡng/điểm tier (vd guest thấy earning rate của tier cao nhất).**
→ *Chẩn:* guest có đang hiển thị theo tier cao nhất không? ngưỡng backend vs widget lệch?
→ *Escalate:* 🔴 nếu widget hiển thị sai so với backend.

**E6. Import tier rồi mà entry reward/tag chưa đúng.**
→ *Chẩn:* re-import tier có sync tag + grant entry reward đúng không?
→ *Xử lý:* dùng launch/migrate flow thay vì import raw; resync.

## F. Migration / Import

**F1. "Migrate hộ tôi từ app X."**
→ *Xử lý:* KHÔNG làm ngay — chạy 3 câu hỏi ([`joy-onboarding-flow.md` §2.1](../../playbooks/joy-onboarding-flow.md)): từ đâu / point vs amount / file vs sync. Xác nhận khách đã có trên Shopify.

**F2. Migrate từ Smile.io có issue.**
→ *Chẩn:* mang gì sang (thường chỉ balance)? tier có kèm tag/metafield không? có migrate nhiều lần không?
→ *Xử lý:* thường data one-off cần rà; phức tạp → hẹn **call**. Phần lớn 🟢/data-fix.

**F3. Import xong khách có điểm nhưng là guest.**
→ *Chẩn:* → [§2.3 Guest vs Member](../../playbooks/joy-onboarding-flow.md); `type`/`verifiedEmail` sau import.
→ *Xử lý:* nói rõ cho merchant trạng thái guest, hướng xử lý; đừng im lặng.

**F4. Import nhiều lần → điểm cộng đôi.**
→ *Xử lý:* rà và sửa; dặn **migrate/import một lần**. Xem A4.

## G. Integration

**G1. Klaviyo/Omnisend không sync / nút Sync bị grey-out.**
→ *Chẩn:* connection status? có stale error-flag (vd MISSING_EVENTS_WRITE_SCOPE)? đang trong lúc launch tier (app tạm tắt sync)?
→ *Xử lý:* reconnect/cấp scope; do đang launch tier → chờ xong. 🟢/🔴 tùy.

**G2. Recharge ngừng sync discount.**
→ *Chẩn:* Recharge API key còn không (có bị xóa field)? key hợp lệ? `source_name` đổi?
→ *Escalate:* xóa nhầm field key → 🔴; key sai → 🟢.

**G3. Review app không cộng điểm (Judge.me/Loox/Yotpo/Fera).**
→ *Chẩn:* **lỗi Joy hay 3rd-party**? Fera webhook có bị tắt? Judge.me chỉ gửi status 'not-yet'? Loox free plan thiếu Flow?
→ *Xử lý:* phần lớn **3rd-party** (🟠) — chỉ ra đúng thủ phạm, hướng dẫn bật webhook/Flow; đừng nhận bug Joy.

**G4. App hiện "Not Connected" nhưng thực ra vẫn chạy (hoặc ngược lại).**
→ *Chẩn:* trạng thái hiển thị vs thực tế last-sync.
→ *Escalate:* 🔴 nếu status hiển thị sai (false "Not Connected").

## H. Shop config / plan / mode

**H1. "Feature X tôi không thấy đâu."**
→ *Chẩn:* có bị **plan-gating** không (Advanced/Ultimate/Plus/Enterprise)? (vd checkout Quick Redeem chỉ Enterprise; checkout extension chỉ Plus.)
→ *Xử lý:* giải thích plan cần thiết. 🔵/🟢.

**H2. "Program tôi setup rồi mà không chạy."**
→ *Chẩn:* đang **test-mode/Sandbox**? test-email đã add? điều kiện country/phone?
→ *Xử lý:* hướng dẫn launch/điều kiện. 🟢.

**H3. "Widget/loyalty page ngôn ngữ sai / chưa dịch."**
→ *Chẩn:* translation đã update chưa (mặc định English)? tương thích Shopify Translate & Adapt? field nào không đi qua i18n?
→ *Xử lý:* update translation từng field; chữ **vỡ do ghép chuỗi** (zh/FR/DE) → 🔴 (i18n bug).

---

*Nguồn: `docs/joy-ticket-analysis-q2-2026.md` (1.164 ticket semantic + 379 thread dev), `docs/joy-agent-diagnostic-tool-map.md`. Onboarding flow → [`joy-onboarding-flow.md`](../../playbooks/joy-onboarding-flow.md). Cập nhật: 2026-07-08.*
