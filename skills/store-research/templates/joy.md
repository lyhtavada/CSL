# Template report — store Joy Loyalty

Giữ **đúng thứ tự và đúng tên** các section dưới đây. Section không có data thì vẫn để
heading và ghi một dòng lý do (`Không lấy được: MCP storeleads từ chối quyền`) —
**không xoá section**, vì đó là thứ giữ cho các store so sánh được với nhau.

Độ dài co giãn theo lượng data thật. Store mới cài 2 tuần thì mục "Trạng thái sản phẩm"
ngắn là đúng, đừng độn chữ.

---

## TL;DR
3-5 gạch đầu dòng. Câu đầu **luôn** là: call ngày nào, với ai, mục đích gì, Liz cần đạt
được gì. Sau đó là 2-3 phát hiện đắt nhất — ưu tiên thứ có con số.

## Account
Bảng 2 cột: Shop domain · Contact (tên, email, chức danh) · Ngành · Shopify plan ·
App plan + MRR · Ngày install · Doanh thu lifetime · Billing health · Nguồn
(organic / referral / sale) · Stack app khác.

## Bối cảnh merchant
Ngành hàng, USP, đối tượng khách, khoảng giá, quy mô SKU.
**Retention đang có ngoài Joy** — newsletter discount, free gift threshold, subscription,
bundle, app affiliate/review đang cài. Đây là phần quyết định tier và referral nên
thiết kế thế nào.
Prospect thì thêm: vì sao họ đi tìm loyalty (lấy từ form book demo / Crisp).

## Timeline
Bảng: Ngày | Chuyện gì | Ai. Gộp Crisp + ticket + call đã diễn ra + **thao tác merchant
tự làm trong app** (đọc được từ `startDate`/`updatedAt` của từng rule).
Kết bằng một dòng **"ai đang chờ ai"** — đây là câu Liz cần nhất.

## Trạng thái sản phẩm thật
Đọc từ storefront (`fetch_store.py`) — tức đúng cái khách hàng của merchant đang thấy.
Luôn ghi rõ số nào từ storefront, số nào từ DB; hai nguồn lệch nhau được.

- **Earning** — bảng: Rule | Điểm | Bật từ. Ghi rule nào draft/tắt.
- **Redeeming** — bảng: Đổi | Nhận | Min order. Nêu rõ mốc nào **không có min order**.
- **Kinh tế chương trình** — `money_per_point`, `cashback_pct`, và
  `free_points_stackable` (tổng điểm kiếm được **không cần mua hàng**) quy ra tiền.
  Đây là 3 số đắt nhất của cả page.
- **VIP tier** — từng tier + ngưỡng + perk, và **bật hay tắt** (`enableTierProgram`).
  Ngưỡng `targetPoint` vs `targetPointUpdate` lệch nhau là chuyện thường gặp → ghi cả hai,
  đánh dấu cần verify trong admin.
- **Referral** — có program chưa. `useReferralV2: true` chỉ nghĩa là bản v2 được bật,
  **không** nghĩa là đã dựng program.
- **Usage thật** (member, điểm đã phát/đã đổi): các field usage trong `merchant_profile`
  hiện hay trả 0 kèm `has_behavior_data: false` → đó là **thiếu tracking**, không phải
  chương trình không ai dùng. **Không trích các số 0 này lên call.**

## Gap & cơ hội
Đánh số. Mỗi gap: **hiện trạng (số cụ thể) → rủi ro/chi phí → đề xuất**.
Đề xuất không có số đỡ lưng thì phải ghi rõ là giả định.

Checklist quét đủ, đúng thứ tự ưu tiên hay gặp ở Joy:
1. **Tỉ lệ hoàn quá cao** — benchmark beauty/skincare 2–5%. Trên 6% là phải nói.
2. **Điểm free chồng nhau** — cộng hết reward không cần mua hàng; đối chiếu với mốc đổi
   thấp nhất và với mốc nào không có min order.
3. **Tier dựng rồi mà chưa bật** — quick win kinh điển, gặp ở cả Bloomable lẫn Keepers.
4. **Referral chưa dựng** / chồng lấn app affiliate đang cài.
5. **Rule mới bật nhưng có thể không trigger** — điển hình: newsletter reward phụ thuộc
   Shopify marketing status, không phải popup Klaviyo/form.
6. **Migration từ app cũ** — luôn hỏi họ đã dùng loyalty app nào trước chưa. Nếu chưa thì
   **không tồn tại lịch sử điểm để migrate**, dù họ đang lo lắng vì data app khác
   (subscription/bundle) — gỡ nỗi lo này sớm.
7. **Điểm tiêu vào thứ không ăn margin** — environmental reward (GoodAPI), early access,
   free gift, trải nghiệm riêng của brand. Đây là lối thoát cho gap (1).
8. **Widget/branding** — watermark, font, vị trí nút, ẩn trên mobile.

## Kịch bản call
1. **Mở đầu** — 1 câu hỏi mở để họ tự nói ra vấn đề thật. Nếu họ vừa tự cấu hình gì đó
   thì ghi nhận việc đó trong câu mở, đừng dạy lại từ đầu.
2. **Đào sâu** — 2-3 nhánh follow-up, chỉ dùng nhánh khớp câu trả lời của họ.
3. **Demo mapping** — feature ↔ đúng vấn đề họ vừa nêu, kèm câu nói mẫu **tiếng Anh**.
   Cụm hay dùng cho Joy: tier theo spend · referral 2 chiều · điểm không hết hạn ·
   điểm cho review/UGC · environmental reward · early access.
4. **Need-payoff** — câu để họ tự phát biểu KPI 90 ngày. Ghi lại làm mốc follow-up.
5. **Objection** — objection dự đoán + cách trả lời.
   Hay gặp: *"tôi muốn chương trình hào phóng"* · *"tôi đã hứa mức thưởng này với khách rồi"* ·
   *"khách tôi mua theo mùa nên loyalty không hợp"*.
6. **Đóng call** — chốt bước tiếp theo + timeline.

Câu nói với merchant viết **tiếng Anh** (`_identity/tone-and-voice.md`).
Ghi chú cho Liz viết tiếng Việt.

## Câu hỏi cần hỏi
Chỉ những câu **không tra được** bằng data. Với Joy gần như luôn có:
**margin trung bình** (quyết định toàn bộ earn/redeem ratio) và **ngày muốn relaunch**.
Thứ nào research ra rồi thì đừng hỏi lại merchant — mất uy tín.

## Việc cần làm
- [ ] Trước call
- [ ] Sau call

## Nguồn & khoảng trống
Đã pull từ đâu; phần nào **không lấy được và vì sao**. Thiếu mục này thì người đọc sau
không biết chỗ nào đáng nghi.
