# Template report — store Chatty

Giữ **đúng thứ tự và đúng tên** các section dưới đây — cùng bộ section với `joy.md` để
các store so sánh được với nhau. Section không có data thì vẫn để heading và ghi một dòng
lý do (`Không lấy được: ...`), **không xoá section**.

> ⚠️ **Phân biệt hai loại chat, đừng trộn** — đây là lỗi dễ mắc nhất khi research store Chatty:
> - **Chat của Chatty** = shopper của merchant ↔ chatbox/bot Ivy trên store họ. Đây là
>   *sản phẩm* → đọc từ `merchant_profile` (`enduser_usage_30d`, `entity_counts`) và
>   dashboard cs2.
> - **Chat Crisp** = merchant ↔ CS team Avada. Đây là *quan hệ hỗ trợ* → đọc từ BigQuery
>   `avada_cs.crisp_chats` (`fetch_store.py` lấy sẵn).
>
> Số của loại này không được dùng để nói về loại kia.

---

## TL;DR
3-5 gạch đầu dòng. Câu đầu **luôn** là: call ngày nào, với ai, mục đích gì, Liz cần đạt
được gì. Sau đó là 2-3 phát hiện đắt nhất — ưu tiên thứ có con số.

## Account
Bảng 2 cột: Shop domain · Contact (tên, email, chức danh) · Ngành · Shopify plan ·
App plan + MRR · Ngày install · Doanh thu lifetime · Billing health · Nguồn
(organic / referral / sale) · Stack app khác — **đặc biệt là helpdesk/live-chat khác đang
cài** (Gorgias, Tidio, Zendesk, Re:amaze): đó là đối thủ trực tiếp trên chính store này.

## Bối cảnh merchant
Ngành hàng, USP, đối tượng khách, khoảng giá, quy mô SKU.
**Cách họ đang làm CS hiện tại** — có team support không, kênh nào (email, FB, IG, WhatsApp),
có trang FAQ/help center riêng không, có policy trả hàng/vận chuyển rõ ràng không.
Store bán hàng cần tư vấn nhiều (size, tương thích, tuỳ chỉnh) thì AI + FAQ có giá trị
khác hẳn store mua nhanh — nói rõ store này thuộc nhóm nào.
Prospect thì thêm: vì sao họ đi tìm live chat (lấy từ form book demo / Crisp).

## Timeline
Bảng: Ngày | Chuyện gì | Ai. Gộp Crisp + ticket + call đã diễn ra + thao tác merchant tự
làm trong app (`merchant_usage_30d`: `settings_events`, `staff_events`, `channel_settings_events`,
`widget_settings_events`, `campaign_events`, `integration_connected`).
Kết bằng một dòng **"ai đang chờ ai"**.

## Trạng thái sản phẩm thật
Nguồn: `merchant_profile` (`entity_counts`, `merchant_usage_30d`, `enduser_usage_30d`,
các field `chatty_*_30d`) + dấu vết widget trên storefront (`fetch_store.py`) +
dashboard cs2 nếu cần. Ghi rõ số nào từ đâu.

- **Setup & kênh** — `setup_done`, `active_staffs`, `active_services`, `active_rules`,
  `email_channel_connected`, `facebook_messenger_connected`, `active_integrations`,
  `active_translations`. Cài rồi mà chưa nối kênh nào là gap lớn nhất và hay bị bỏ qua.
- **Volume & engagement** — `total_conversations`, `conversation_sessions`,
  `chatbox_engaged_sessions`, `open_conversations`, `impressions`, `widget_settings_seen`.
  Chat = 0 nhưng impressions cao → widget hiện mà không ai bấm: vấn đề vị trí/lời mời chào,
  không phải vấn đề bot.
- **AI** — `ai_answers`, `ai_found_answers`, `ai_not_found_answers`,
  `ai_positive_ratings`, `ai_negative_ratings`. Tính **tỉ lệ trả lời được**
  (`found / (found + not_found)`) và tỉ lệ rating âm. `not_found` cao = **thiếu training
  data / KB**, đây là việc CS làm được ngay và là lý do rất tốt để đề xuất DFY.
- **Bán hàng qua chat** — `sales_related_conversations`, `chat_to_sales_rate`, `purchase`.
  Đây là con số thuyết phục nhất với merchant, dùng được thì dùng.
- **Tự phục vụ** — `faq_uses`, `order_tracking_uses`, `email_submissions`.
  `order_tracking_uses` cao = khách toàn hỏi "đơn tôi đâu" → gợi ý tự động hoá.
- **Proactive & campaign** — `active_campaigns`, `campaign_events`, `gift_campaigns`,
  `active_gift_campaigns`, `generated_gift_orders`, `gift_revenue_usd`.
- **Widget/branding** — vị trí nút, ẩn trên mobile, ngôn ngữ, giờ làm việc.
- Field trả 0 kèm `has_behavior_data: false` là **thiếu tracking**, không phải "không ai
  dùng". **Không trích các số 0 này lên call.**

## Gap & cơ hội
Đánh số. Mỗi gap: **hiện trạng (số cụ thể) → rủi ro/chi phí → đề xuất**.
Đề xuất không có số đỡ lưng thì ghi rõ là giả định.

Checklist quét đủ, theo thứ tự ưu tiên hay gặp ở Chatty:
1. **Cài xong nhưng chưa nối kênh** (email/FB chưa connect, chưa thêm staff) — chat vào
   không ai thấy. Nặng nhất, sửa nhanh nhất.
2. **AI `not_found` cao / rating âm** — thiếu KB, thiếu training data. Cửa vào DFY.
3. **Impressions cao mà engaged thấp** — vị trí widget, lời chào, ẩn nhầm trên mobile.
4. **Chat nhiều mà `chat_to_sales_rate` thấp** — chưa map sản phẩm vào câu trả lời,
   chưa có proactive lúc khách phân vân.
5. **`order_tracking_uses` / câu hỏi lặp cao** — tự động hoá được, giảm tải người thật.
6. **Chưa dùng proactive / campaign / gift** — feature đã trả tiền mà chưa dùng.
7. **Đang cài helpdesk khác song song** — làm rõ ranh giới, hoặc là cơ hội thay thế.
8. **Giờ làm việc & fallback** — ngoài giờ khách nhắn thì chuyện gì xảy ra.

## Kịch bản call
1. **Mở đầu** — 1 câu hỏi mở để họ tự nói ra vấn đề thật. Nếu họ vừa tự cấu hình gì đó
   thì ghi nhận việc đó trong câu mở, đừng dạy lại từ đầu.
2. **Đào sâu** — 2-3 nhánh follow-up, chỉ dùng nhánh khớp câu trả lời của họ.
3. **Demo mapping** — feature ↔ đúng vấn đề họ vừa nêu, kèm câu nói mẫu **tiếng Anh**.
   Cụm hay dùng cho Chatty: AI trả lời từ chính KB của họ · FAQ tự phục vụ ·
   order tracking trong chat · proactive lúc khách chần chừ · gộp email/FB/IG về một hộp thư ·
   chuyển người thật khi AI bí · đa ngôn ngữ.
4. **Need-payoff** — câu để họ tự phát biểu KPI 90 ngày (giảm ticket lặp / tăng chuyển đổi
   qua chat / trả lời nhanh hơn ngoài giờ). Ghi lại làm mốc follow-up.
5. **Objection** — objection dự đoán + cách trả lời.
   Hay gặp: *"AI trả lời sai thì sao"* (→ nói thẳng cơ chế fallback sang người thật và
   việc AI chỉ đọc KB của chính họ) · *"team tôi nhỏ, không trực chat nổi"* ·
   *"tôi đang dùng [helpdesk khác] rồi"*.
6. **Đóng call** — chốt bước tiếp theo + timeline.

Câu nói với merchant viết **tiếng Anh** (`_identity/tone-and-voice.md`).
Ghi chú cho Liz viết tiếng Việt.

## Câu hỏi cần hỏi
Chỉ những câu **không tra được** bằng data. Với Chatty gần như luôn có:
**ai đang trực chat và bao nhiêu giờ/ngày**, **câu hỏi nào lặp nhiều nhất**, và
**nguồn nội dung để train AI** (help center? policy page? file?).
Thứ nào research ra rồi thì đừng hỏi lại merchant — mất uy tín.

## Việc cần làm
- [ ] Trước call
- [ ] Sau call

## Nguồn & khoảng trống
Đã pull từ đâu; phần nào **không lấy được và vì sao**. Với Chatty nói rõ luôn: số nào là
chat của shopper (sản phẩm), số nào là chat Crisp với CS Avada.
