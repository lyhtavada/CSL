# Joyce Escalation Gap Analysis — 1 tháng (27/07 → 27/08/2026)

**Nguồn:** `/api/obs/sessions` + `/api/obs/session/{id}` (field `conversation.escalation_reason`) trên `cs2.avada.net`, agent `joy-loyalty-agent`. Toàn bộ 384 ca escalate trong kỳ (không sample) — phân loại theo `escalation_reason` do chính hệ thống gắn tag, đối chiếu với phân tích tuần 22–28/06 trong memory `joy_bot_escalate_kb_fixes`.

## Số tổng quan

- 523 session, 384 escalate = **73.4%** (tuần 22–28/06 là 77.7% — cùng bậc, không cải thiện rõ rệt trong 1 tháng).
- `aiResolvedPct` chỉ 11.1%, `humanTakeoverPct` 67.1% — bot vẫn cần người nhảy vào ở phần lớn session dù `aiReplyCoveragePct` 95% (bot có trả lời, nhưng không "chốt" được vấn đề).

## Breakdown theo trigger tag

| Tag | Số ca | Bản chất |
|---|---:|---|
| `[agent]` (catch-all) | 222 | Bug/feature request/billing/manual backend action — đa số LEGITIMATE |
| `[ticket-KHÔNG-NĂNG-LỰC→người nhận]` | 53 | Custom CSS/design/dev request ngoài năng lực bot — LEGITIMATE |
| `[answer-guard]` | 43 | Bot bịa (path/plan/fact/"đã làm xong") bị guard chặn trước khi gửi — **AVOIDABLE** |
| `[escalation-intent]` | 42 | Khách chủ động xin gặp người — LEGITIMATE |
| `[holistic-judge]` | 8 | LLM-judge tổng thể quyết định nên chuyển người | Chưa rõ, cần sample |
| `[kb-cannot-answer]` | 8 | Bot tự nhận KB không đủ tự tin — **AVOIDABLE** (gap KB) |
| `[envelope]` | 3 | Bug hệ thống: LLM sinh lại vẫn rỗng `<reply>` — **BUG, không phải KB** |
| khác (refund-cancel, wants-human, ticket-sync, consult_ts) | 4 | LEGITIMATE lẻ tẻ |

Trong nhóm `[agent]` (222 ca), tách được:
- 45 bug thật (Shopify/Joy data mismatch, discount code lỗi, POS lỗi...)
- 20 billing (refund, cancel plan)
- 28 manual backend action (bật tính năng, export, sửa tay điểm/coupon)
- 18 feature request
- **15 ca gõ thẳng "not covered in KB" / "no KB coverage"** — AVOIDABLE, liệt kê bên dưới
- 2 ca **handoff-promise bug**: bot hứa "I'll flag this to our team" nhưng KHÔNG phát escalate tag → rơi vào khoảng trống, không ai được noti. Đây là **bug flow**, không phải KB.
- còn lại là escalation-intent-like / theo dõi tiến độ ticket cũ (loop CS quay lại) — legitimate.

## AVOIDABLE — tổng ~76 ca (~20%) — đây là đòn bẩy để cải thiện

### 1. Answer-guard hallucination (43 ca) — vẫn là gốc lớn nhất, giống hệt tuần 06/2026
Phân nhóm nội dung bị guard chặn:
- **12 ca: bịa path/label UI** không có trong KB snippet (menu, tab, toggle tên sai).
- **8 ca: khẳng định sai plan/feature gating** (vd nói merchant đang ở Essential dù không có `joy_plan` trong context; nói block chỉ có ở Essential+ trong khi KB nói "all plans").
- **5 ca: khẳng định "đã làm xong"/"team sẽ bật sớm"** không có event thao tác thật đứng sau — rủi ro hứa suông với merchant.
- **4 ca: vi phạm persona** (thêm chữ ký bị cấm, chào lại giữa hội thoại).
- **13 ca khác:** bịa fact sản phẩm (vd đổi VIP tier "reset về ngày bắt đầu tier mới", bịa cơ chế `||` delimiter, bịa tồn tại T&C block có thể tắt...).

⚠️ **Phát hiện quan trọng — đúng như nghi vấn "B retrieval" trong memory cũ:** ít nhất 2 ca guard log rõ **KB đã có câu trả lời đúng nhưng bot vẫn bịa path khác**:
> "Path 'On-site content → Widget → Launcher' is invented; KB says Settings → Launcher → Alignment."
> "Path includes extra 'Widget design' segment; KB shows Setup → Launcher, not Widget design → Setup → Launcher."

→ Đây KHÔNG phải KB thiếu nội dung, mà là **bot không bám đúng KB đã retrieve được** (generation không grounded dù snippet có). Việc "B retrieval" trong memory `joy_bot_escalate_kb_fixes` (chưa fix) cần chuyển hướng: không chỉ là "bot không tìm ra KB" mà còn là "bot tìm ra rồi vẫn bịa thêm/sai lệch path".

### 2. KB gap rõ ràng, gọi thẳng tên (15 + 8 = 23 ca) — patch được ngay
Từ `[agent] ... not covered in KB` + `[kb-cannot-answer]`, các chủ đề cụ thể cần thêm vào KB:
1. Phân biệt template param `{{earned_points}}` vs `{{loyalty_point}}`
2. Nơi khách hàng nhập/xem ngày sinh nhật trên storefront (member-facing entry point)
3. Thu thập gender/age lúc signup — có hỗ trợ không
4. Member-exclusive deal (B2B membership) — ngày kích hoạt/hết hạn hoạt động thế nào
5. Free Gift reward: hiển thị khi sản phẩm unpublished/hết hàng (theme Aurora) — behavior thật
6. Tích hợp Froonze (customer accounts app) — có tương thích không
7. Tích hợp Appstle (subscription app) — có tương thích không
8. Data/coupon còn giữ lại gì sau khi uninstall Joy
9. Link/trang thu thập Instagram handle để track điểm — có sẵn không
10. Đường dẫn chỉnh translation cho Sign-Up Block (thank-you page text)
11. Nơi xem danh sách VIP tier perks trong unified launcher (từ góc nhìn member)
12. REST API v2 — server-side coupon/redemption generation cho native mobile integration
13. Wishlist: đổi shape nút wishlist trên product page — setting có sẵn hay cần CSS
14. Loại trừ earning điểm trên order đã dùng redeem discount — feasibility
15. Free shipping làm reward type cho Sign Up program — có hỗ trợ không

→ Đây là nhóm rẻ nhất để xử lý: chỉ cần verify qua source code Joy (`glab`, theo quy trình đã dùng lần trước) rồi patch `kb/reference/*.md` hoặc `kb/case/*.md`, không cần đổi flow.

### 3. Flow/system bug (không phải KB, cần báo Fennic) — 5 ca
- **2 ca handoff-promise**: bot nói "sẽ chuyển team" nhưng không bắn escalate tag → CS không biết mà xử lý. Cần fix ở tầng action-execution (đảm bảo mọi câu cam kết chuyển người phải kèm event thật).
- **3 ca envelope**: LLM sinh lại `<reply>` vẫn rỗng, phải để CS gõ tay. Bug pipeline generation, không liên quan nội dung KB.

### 4. Holistic-judge (8 ca) — chưa đủ dữ liệu để kết luận
Chỉ có nhãn "nên chuyển người", không có lý do chi tiết trong field. Cần đọc full transcript (`cs2_session.py`) từng ca nếu muốn biết đây là overcautious hay đúng — để dành, ưu tiên thấp (khối lượng nhỏ).

## Đối chiếu với 6 file KB đã patch (30/06)
Patch cũ (`widget.md` page-restriction, `pricing.md`, `persona/facts.md`, `migration.md`, `persona/soul.md`, `errors.md`) **không thấy tái phát y hệt** trong tháng này (không có case nào về page-restriction/migration/logo-placeholder lặp lại) — patch cũ có vẻ đứng vững. Vấn đề mới phát sinh là các case ở trên (Launcher path, template params, integration Q&A...), tức là mặt trận đã dịch sang chủ đề khác chứ chưa "hết việc".

## Đề xuất hành động (ưu tiên theo effort/impact)

1. **Patch 23 KB gap ở mục 2** — effort thấp, impact rõ, theo đúng quy trình verify-qua-source-code đã dùng lần trước. Đề xuất Betty làm patch nháp, Liz duyệt, rồi push+reindex.
2. **Báo Fennic 2 bug flow** (handoff-promise thiếu tag, envelope rỗng reply) — đây là bug code, ngoài phạm vi patch KB.
3. **Retrieval/grounding fix** cho answer-guard (43 ca, đặc biệt 2 ca Launcher lộ rõ retrieval có nhưng bot vẫn bịa) — cần Fennic xem lại vì đây là generation-layer, Liz/Betty không patch được bằng KB.
4. Sample đọc full transcript nhóm holistic-judge (8 ca) khi có thời gian — thấp ưu tiên.

## Update — rà lại KB live cho toàn bộ 23 ca (15 "not covered in KB" + 8 kb-cannot-answer), 2026-08-27

Đọc trực tiếp KB live trên `cs2.avada.net` (`kb_api.py get joy <path>`) cho từng chủ đề, không đoán.

### Xác nhận GAP thật — patch được ngay (8)
1. Phân biệt template `{{earned_points}}` vs `{{loyalty_point}}` — `kb/reference/notifications.md` không có dòng nào nhắc 2 param này.
2. Thu thập gender/age lúc signup — không có trong `earning-programs.md`/`account-page.md`.
3. Tích hợp Froonze (customer accounts app) — 0 nhắc tới trong toàn bộ KB.
4. Data/coupon còn giữ gì sau khi uninstall Joy — `billing-refund.md` chỉ nói về billing cycle khi uninstall, không nói về số phận data/coupon.
5. Translate text **Sign-Up Block ở Thank-you page** — `translations.md` liệt kê "Surfaces translated" (widget, loyalty page, account page, checkout, wallet) nhưng **thiếu hẳn Thank-you page** — đúng là gap, không phải bot không tìm ra.
6. Đường dẫn xem **VIP tier perks list** trong Unified widget (góc nhìn member) — `widget.md` có label "Tier perks" (chỉ để merchant sửa TEXT) nhưng không nói member xem ở đâu (tab nào trong footer/Rewards).
7. Free Gift/perk khi sản phẩm **thật sự unpublished/out-of-stock** (không phải case) — `kb/case/errors.md` chỉ có case "stale variant ID", chưa có case sản phẩm thật sự hết hàng/unpublish.
8. **Đổi shape nút Wishlist** trên product page — thuộc app **Joy Wishlist** (agent khác), không phải Joy Loyalty. Check `wishlist-design.md`: không có mục nào về shape/style nút. Cần patch bên KB Wishlist (agent `wishlist-agent`), không phải Joy.

### Partial — bổ sung nhỏ, không cần bài mới (3)
- Birthday storefront entry point: đã có 1 câu "customers add it in their Joy profile online" (`birthday.md`) nhưng chưa nói rõ đường dẫn cụ thể trong widget/account page — nên thêm 1 dòng path chính xác.
- Appstle: `integrations-subscription.md` đã gắn tag `appstle` nhưng thân bài chỉ nói chung "any other selling-plans-compliant app" — nên thêm 1 dòng gọi thẳng tên Appstle để bot tự tin trả lời thay vì escalate.
- Instagram handle collection: KB đã có flow "customer link IG username trong widget" nhưng câu hỏi merchant là muốn **link/trang riêng** để thu thập — nên làm rõ Joy không có trang riêng, chỉ qua widget.

### Không phải gap — KB đã có sẵn câu trả lời đúng (1)
- Member-exclusive deal (B2B) activation/validity date — `membership-b2b.md` mục "Active dates" đã trả lời đầy đủ (Static/Dynamic). Bot lẽ ra trả lời được, đây là ca lẻ (retrieval miss 1 lần), không cần patch.

### Không patch bằng KB được — giới hạn sản phẩm thật / feasibility (3)
- Free shipping làm reward type cho **Sign Up program**: earning program chỉ trả points/store credit, free shipping là loại reward của redemption/tier-perk — đây là feature request thật, không phải thiếu doc.
- Loại trừ earning điểm trên order đã dùng redeem discount: Rule Engine không có loại "Advanced condition" nào check được việc này (`rule-engine.md` không có) — feasibility thật, cần team xác nhận có làm được không trước khi viết KB.
- REST API v2 cho redemption/coupon qua mobile: KB đã nói chung là Ultimate có REST API v2 quản lý "point transactions, rewards..." + link `devdocs.joy.so` — đủ để trả lời không bịa, không cần thêm.

### 8 ca kb-cannot-answer — đọc lại tin nhắn gần lúc escalate
Không phải case sản phẩm cụ thể như tưởng — đa số là small talk/off-topic (hỏi giờ làm việc, chào hỏi, đổi email liên hệ...) khiến classifier không đủ tự tin trả lời (đúng hành vi, không phải KB thiếu). 2 ca đáng chú ý:
- 1 ca feature request thật (tăng mức tối thiểu đổi gift card lên hơn $10/lần) — không phải KB gap.
- 1 ca **có vẻ là bug**: merchant chọn giới hạn trang hiện popup nhưng checkbox không lưu khi rời trang — nên báo Fennic kèm, không phải patch KB.

## Giới hạn của phân tích này
Phân loại dựa trên field `escalation_reason` (tag tự động của hệ thống) trên toàn bộ 384 ca, KHÔNG đọc full transcript từng ca như lần phân tích tuần 06 (107 ca đọc tay). Field này đủ chi tiết để phân loại legitimate/avoidable và liệt kê KB gap cụ thể, nhưng 2 case Launcher retrieval-fail là phát hiện phụ (đọc kỹ nội dung reason), không phải audit đầy đủ tầng retrieval.
