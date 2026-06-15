# QA Tuần 2026-W24 — Sonny
**App:** Joy · **Kỳ:** 08/06 – 14/06/2026

## 📊 Điểm tuần: 84/100 — Tốt  (▼ -7 so với W23: 91)
- 🧠 Mindset 29.2/34 · 📚 Kiến thức 28.1/33 · 🛠️ Xử lý 26.8/33
- 🔍 Đã QA: 30 chat
- Trục yếu nhất: **Xử lý**

## 🚨 Severe flag — Liz xem kỹ trước khi gửi
- Chat #9 [live_store_mistake]: Re-sync database để tìm 1 khách hàng khiến 2496 members bị convert thành guest. Sonny xử lý recovery nhưng thiệt hại đã xảy ra.
- Chat #27 [live_store_mistake]: Switch widget sang live mà không có explicit approval từ khách sau khi không nhận được reply.

## 📝 Nhận xét chung
Sonny kiến thức Joy rất chắc và DFY pitch đúng lúc, nhưng điểm tụt mạnh từ 91 xuống 84 vì các lỗi thao tác live store lặp lại tuần thứ 3 liên tiếp: chat #9 re-sync database làm 2496 member bị chuyển thành guest, chat #27 tự switch widget sang live khi khách chưa đồng ý. Ngoài ra gửi nhầm URL store của khách khác (chat #5, #17) và lệch ngôn ngữ (chat #7 Ý→Tây Ban Nha). Ưu tiên tuyệt đối: mọi thao tác ảnh hưởng live store PHẢI có xác nhận của khách trước khi thực hiện.

## ✅ Điểm tốt
- Ownership đến cùng
   > Chat #2 (pepperfield): Xử lý referral block nhiều ngày, tạo ticket, gửi follow-up email xác nhận. · Chat #11 (e5c08e): Giải thích chính xác sandbox mode, theo dõi đến khi khách hiểu hoàn toàn. · Chat #27 (south-metro): Chủ động follow-up widget + loyalty page design nhiều ngày liên tiếp.
- DFY pitch tốt và đúng thời điểm
   > Chat #27 (south-metro): 'I see that you would like to create a loyalty page that matches your theme, we're actually offering a free setup service...' [15:39:18] — sau khi khách nói overwhelmed, Sonny pitch DFY rất tự nhiên. · Chat #19 (r4xr1e): Sau khi giải quyết xong popup issue, offer widget upgrade + loyalty page DFY đúng thời điểm.
- Knowledge Joy chắc, giải thích technical rõ
   > Chat #10 (toycycle): Giải thích migration CSV format, xử lý extra columns, deletion flow — chính xác và rõ ràng. · Chat #28 (sy0nev): Giải thích đúng limitation về historical point balance ('we can only export the current data instead of the point/tier at the time') [07:08:58]. · Chat #27 (south-metro): Trả lời chính xác free gift perk limitation, tier downgrade, subscription tier trên Joy POS [15:11:06].

## 🔧 Cần cải thiện
- **[Live-store · Urgent] · severe** Thao tác live store mà không xin phép — lặp lại lần 3 (#9 #27)
   > #9: Customer [16:32:12]: 'una conversion masiva hace 53 minutos me aparece' / 'y solo tengo 2 miembros ahora / y 2496 guest' | #27: CS (Sonny) [12:05:10]: 'Since we haven't received a response from you yet, we went ahead and switched your store over to the new widget version.'
   → Bất kỳ thao tác nào ảnh hưởng đến live store — re-sync, switch widget, chỉnh nội dung — phải xác nhận rõ với khách trước khi thực hiện. Không được tự ý làm vì 'chưa reply'. Đây là lần thứ 3 lỗi này xảy ra (W22, W23, W24).
- **[KN3 · Moderate] · moderate** Language mismatch — dùng tiếng Tây Ban Nha với khách Ý — lặp lại từ W23 (#7)
   > #7: CS (Sonny) [13:42:55]: 'Aquí lo tienes' — Customer [13:52:10]: 'grazie, hai lo spagnolo attivo comunque' — Customer [13:55:21]: 'hai lo spagnolo attivo, puoi parlare in italiano?'
   → Kiểm tra ngôn ngữ khách đang dùng trước khi reply, đặc biệt khi có tool live-translate đang hoạt động. Nếu tool translate sang ngôn ngữ sai — tắt tool và reply đúng ngôn ngữ khách.
- **[KT1 · Low] · low** Gửi sai store URL cho khách — 2 lần trong tuần (#5 #17)
   > #5: CS (Sonny): 'https://www.veloraglowshop.com.my/#joy-loyalty' — đây không phải store của khách singularu. | #17: CS (Sonny): 'https://shop.cigar-kingdom.com/#joy-loyalty' — đây không phải store của khách x9z0g3.
   → Khi gửi preview link DFY, luôn kiểm tra URL có đúng store của khách đang chat không. Copypaste từ chat khác là nguồn gốc lỗi này.
- **[KN1 · Low] · low** Typo — lặp lại pattern từ W22/W23 (#12)
   > #12: CS (Sonny) [13:54:28]: 'I láo hope you can share a screenshot of it once done'
   → Đọc lại tin nhắn trước khi gửi, đặc biệt các câu kết thúc chat. Pattern typo đã xuất hiện nhiều tuần liên tiếp.
- **[Review ask · Low] · low** Review ask gửi trước khi xử lý xong issue (#22)
   > #22: CS (Sonny) [14:00:37]: 'Can you please share your experience here instead: https://www.trustpilot.com/review' — gửi ngay sau khi nhận code [13:57:13], trước khi access store và investigate.
   → Review ask chỉ gửi sau khi issue đã được giải quyết và khách confirm satisfied.

## 🌟 Xin review (chỉ ghi nhận, KHÔNG tính điểm)
- Đã xin 10/19 chat phù hợp (đúng lúc 9, chưa đúng lúc 1).
- Chat #22 (lacava): review ask gửi trước khi investigate issue. Chats #3, #4, #8, #11, #12, #14, #16, #20, #25 = 9 well-timed.

## 📈 So với tuần trước (W23)
- Điểm 91 → 84 (▼ -7)
