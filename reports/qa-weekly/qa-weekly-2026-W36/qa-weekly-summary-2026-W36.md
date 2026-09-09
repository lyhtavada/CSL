# QA Weekly Summary — 2026-W36 (02/09 – 08/09/2026)
**Team in-house (8/9 CS — Hana không có chat tuần này) · rubric 3 trục · coaching, không phải penalty**

> ⏳ CHỜ LIZ DUYỆT — chưa gửi DM cho CS.

| CS | Điểm | Δ tuần trước | 🧠 Mind | 📚 Know | 🛠️ Skill | Chat | Xin review | Trục yếu | Flag |
|---|---|---|---|---|---|---|---|---|---|
| Phoebe | 78 | ▼ -1 | 26.2 | 26.8 | 24.8 | 19 | 3/4 | skill |  |
| Andy | 79 | ▼ -4 | 26.9 | 26.4 | 25.8 | 28 | 0/3 | skill |  |
| Linda | 81 | ▲ +1 | 27.2 | 27.4 | 26.7 | 17 | 2/2 | skill |  |
| Sonny | 83 | ▬ 0 | 28 | 27 | 26 | 30 | 4/6 | skill |  |
| Hazel | 84 | ▲ +6 | 28 | 28 | 28 | 29 | 3/6 | mindset | ⚠️ severe |
| Audrey | 86 | ▲ +8 | 30 | 28 | 28 | 30 | 2/3 | knowledge | ⚠️ severe |
| Jade | 87 | ▲ +6 | 29 | 29 | 29 | 30 | 1/4 | mindset |  |
| Alyssa | 92 | ▲ +6 | 31 | 31 | 29 | 30 | 1/2 | skill |  |
| Hana | — | (0 chat tuần này) | — | — | — | 0 | — | — |  |

**TB team 2026-W36 (8 CS có chat):** 83.8/100 — so với tuần trước (80.7/100, 9 CS): ▲ +3.1

## 🚨 Severe flags — Liz xem kỹ trước khi duyệt DM

**Hazel** (score 84):
- Chat #25: thao tác cấu hình sai trên live store — khách (Phos & Gaia) chỉ yêu cầu tắt Proactive Chat **CHỈ ở trang cart**, Hazel hiểu thành tắt **toàn bộ** Proactive Chat trên store. Khách phải phản hồi gắt để Hazel sửa lại. Không phải KN8/QT11/KT1 nhưng có ảnh hưởng thực tế lên trải nghiệm khách trên store đang chạy thật — nên xem qua, có thể do thao tác vội chứ không phải chủ đích.

**Audrey** (score 86):
- Chat #20: Audrey chủ động xin khách chia sẻ **login information + mã xác thực điện thoại (OTP)** để "đăng nhập vào tài khoản khách" giúp dev debug nhanh hơn — khách đã gửi email + mã OTP (307126) ngay sau đó. Đây **không phải** storefront password (thường được phép) mà là mã 2FA cá nhân — xin chia sẻ mã này là rủi ro bảo mật nghiêm trọng bất kể mục đích/ý tốt. Liz nên coaching riêng gấp trước khi hành vi này lặp lại — có thể liên quan đến việc team hiện chưa có quy định rõ ràng/được nhắc lại về giới hạn "được hỏi gì, không được hỏi gì" khi cần debug tài khoản khách.

## Về các claim giá/limit trong tuần này
Không có KT1 (sai giá/limit hiện hành) được raise tuần này. Vài chỗ đáng chú ý nhưng **không phải lỗi CS**, đã được các grader tự loại trừ đúng theo hướng dẫn (không suy diễn khi có thể là legacy pricing/KB có thể lệch) — không cần Liz verify KB thêm lần này.

## Ghi chú khác
- Điểm cao nhất tuần: **Alyssa (92, Xuất sắc, ▲ +6)** — tuần chất lượng rất cao, kiến thức sản phẩm sâu (VIP Tier, Klaviyo/Recharge, POS, store credit), theo case dài ngày không bỏ rơi khách, trung thực nhận lỗi khi hiểu sai. Điểm cần siết: lỗi chính tả rải rác trong email dài gửi khách lớn, và mời review G2 ở ít nhất 5 chat đã có review từ trước (nên check trạng thái review trước khi mời).
- Điểm thấp nhất tuần: **Phoebe (78, Đạt, ▼ -1)** — vẫn ổn định ở case kỹ thuật khó (WhatsApp WABA, email forwarding), nhưng hướng dẫn ban đầu đôi khi chưa đúng chỗ khiến khách phải hỏi lại/phản đối, kéo dài chat.
- **Andy giảm mạnh nhất tuần (▼ -4, từ 83→79)** — điểm trừ chính là 1 lỗi KN5 khá nặng: đưa hướng xử lý sai hoàn toàn với vấn đề khách đang hỏi (case Arvellis) khi khách đã bực sẵn vì phải làm lại setup cũ, khiến khách bực hơn. Ngoài ra 0/3 chat xin review tuần này dù tuần trước làm tốt (3/8) — và có xu hướng nhắc đồng nghiệp (Linda) xin review giúp nhưng không tự áp dụng cho case của chính mình.
- Hazel, Audrey, Jade, Alyssa đều tăng mạnh (+6 đến +8) — nhưng 2 trong số đó (Hazel, Audrey) có severe flag cần Liz xem trước khi khen thưởng công khai (xem mục trên).
- Sonny giữ nguyên 83 điểm tuần thứ 2 liên tiếp — ổn định, điểm cần chú ý là lỗi KN5 (trả lời trước khi đọc kỹ lịch sử chat, phải đính chính giữa chừng ở case #10).
- Linda tăng nhẹ +1 nhưng có 1 lỗi KN5 đáng chú ý: báo sai số liệu sản phẩm sync (506 vs thực tế 615 active) với khách đang sốt ruột vì case đã trễ hẹn — nên xác nhận số liệu chắc chắn trước khi báo khách.
- **Hana không có chat nào tuần này** (0/0 theo BigQuery, ≥3 msg in-week) — không chấm được, cần xác nhận có phải nghỉ phép/nghỉ việc tuần này không.
