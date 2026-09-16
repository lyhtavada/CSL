# QA Weekly Summary — 2026-W37 (09/09 – 15/09/2026)
**Team in-house (9/9 CS có chat tuần này, gồm Ethan tuần đầu) · rubric 3 trục · coaching, không phải penalty**

> ⏳ CHỜ LIZ DUYỆT — chưa gửi DM cho CS.

| CS | Điểm | Δ tuần trước | 🧠 Mind | 📚 Know | 🛠️ Skill | Chat | Xin review | Trục yếu | Flag |
|---|---|---|---|---|---|---|---|---|---|
| Alyssa | 77 | ▼ -15 (92) | 25.7 | 26.3 | 25.5 | 24 | 1/2 | skill |  |
| Ethan | 78 | (tuần đầu) | 25.5 | 27 | 26 | 30 | 0/2 | mindset |  |
| Hazel | 80 | ▼ -4 (84) | 26.7 | 27.1 | 26.5 | 29 | 5/7 | mindset |  |
| Jade | 80 | ▼ -7 (87) | 27.8 | 26.6 | 25.9 | 30 | 4/6 | skill |  |
| Linda | 80 | ▼ -1 (81) | 26.6 | 26.8 | 26.1 | 19 | 1/2 | skill |  |
| Phoebe | 80 | ▲ +2 (78) | 27.2 | 27.3 | 25.4 | 11 | 0/1 | skill |  |
| Sonny | 81 | ▼ -2 (83) | 28.1 | 26.4 | 26.1 | 30 | 5/7 | knowledge | ⚠️ severe |
| Andy | 82 | ▲ +3 (79) | 28.2 | 27.3 | 26.8 | 30 | 2/4 | skill | ⚠️ severe |
| Audrey | 84 | ▼ -2 (86) | 28 | 27 | 26 | 30 | 3/3 | knowledge | ⚠️ severe |

**TB team 2026-W37 (9 CS):** 80.2/100 — so với tuần trước (83.8/100, 8 CS): ▼ -3.6

## 🚨 Severe flags — Liz xem kỹ trước khi duyệt DM

Tuần này có **3 flag KT1** (sai kiến thức/giá) — nhiều hơn hẳn tuần trước (0 KT1). Cả 3 đều liên quan claim về **giá/plan/dependency giữa app** — đúng loại rủi ro rubric nhắc phải verify KB trước khi kết tội, vì KB có thể outdated hoặc 2 file KB không khớp nhau.

**Andy** (score 82):
- Chat #18: Andy khẳng định khách **KHÔNG cần** cài Joy Loyalty để kết nối Wishlist với Klaviyo. Đồng nghiệp (Rosie) quay lại đính chính: Joy Loyalty **là bắt buộc** (middleware). → **Liz nên verify trong KB Wishlist/Joy hiện tại xem dependency này ghi thế nào** — nếu KB không rõ ràng về điểm này, đây là gap KB cần vá trước khi coi là lỗi cá nhân của Andy.

**Audrey** (score 84):
- Chat #12: Audrey nói tính năng Claude integration thuộc plan **"Enterprise"** (Joy không có plan tên này) — đúng ra là **Ultimate**. Liz đã phát hiện và Audrey tự sửa lại ngay trong chat. Vì Audrey tự đính chính nhanh sau khi được nhắc, mức độ rủi ro thấp hơn 2 case còn lại, nhưng vẫn nên xem lại **tên plan trong KB Joy có nhất quán không** (Free/Advanced/Ultimate) — dễ nhầm nếu KB dùng tên plan khác ở nhiều chỗ.

**Sonny** (score 81):
- Chat #4: Sonny báo khách đang dùng **"giá cũ" (grandfathered)** nhưng lại đưa ra đúng con số của **giá mới hiện hành ($29)**, cao hơn giá grandfathered thật (theo bot đưa ra là ~$24.99). Sau đó khi được đính chính, Sonny nói đó là "AI gửi nhầm" thay vì tự sửa câu trả lời của chính mình cho khách. → **Đây là case cần Liz verify giá grandfathered thật của khách này trước** (dễ có 2 số khác nhau giữa CS nhớ và hệ thống), và **nên nói riêng với Sonny về việc không nên đổ cho "AI" khi mình đã là người trả lời sai** — đây là vấn đề thái độ nhận lỗi, tách biệt với đúng/sai KB.

## Về các claim giá/limit trong tuần này
Không giống tuần trước (0 KT1), tuần này có 3 case KT1 liên quan giá/plan/dependency — nhưng **cả 3 đều nên verify KB trước khi coi là lỗi CS thuần túy**, theo đúng nguyên tắc rubric (KB có thể outdated hoặc không nhất quán giữa các file). Đề xuất: sau khi Liz duyệt DM, dành thêm 1 vòng kiểm tra riêng 3 file KB liên quan (Wishlist-Klaviyo dependency, tên các plan Joy, giá grandfathered) độc lập với việc gửi DM coaching.

## Ghi chú khác
- **Điểm cao nhất tuần: Audrey (84, Tốt, ▼ -2)** — vẫn xử lý tốt các case dài/nhạy cảm (GDPR audit, migration 302K khách hàng) nhưng có KT1 (xem severe flag) và 1 case ownership yếu (chỉ report tình trạng thay vì hành động theo yêu cầu rõ ràng của khách).
- **Điểm thấp nhất tuần: Alyssa (77, Đạt, ▼ -15)** — giảm mạnh nhất trong tuần, từ 92 (Xuất sắc, cao nhất tuần trước) xuống 77. Vẫn giữ ownership tốt trên case kỹ thuật nặng và trung thực nhận lỗi khi sai, nhưng có 1 lỗi KN6 (trả lời trước khi đọc đủ lịch sử chat đã qua nhiều CS) khiến khách phải tự sửa lại — nên xem đây có phải case đột biến (1 tuần case khó hơn) hay xu hướng cần theo dõi tiếp tuần sau.
- **Ethan (78, Đạt)** — tuần đầu chính thức được QA (join fulltime 2026-09-01), chưa có baseline so sánh. Điểm mạnh là chủ động đề xuất trước khi khách hỏi và trung thực nhận lỗi; điểm cần chú ý là Mindset (25.5/34, thấp nhất nhóm) — với khách đang bực/mệt, phản hồi còn khá máy móc, thiếu 1 câu thấu cảm trước khi vào giải pháp kỹ thuật.
- **Jade giảm mạnh thứ 2 (▼ -7, từ 87→80)** — vẫn ownership tốt (theo case bug tag khách hàng, tự debug scenario Chatty) nhưng Skill là trục yếu nhất (25.9/33): có case báo kết quả test sai kênh khách đang hỏi, khách phải tự phát hiện.
- **Hazel giảm (▼ -4, từ 84→80)** — không còn severe flag như tuần trước (thao tác sai trên live store), nhưng lặp lại pattern hiểu sai ý khách rồi thao tác nhầm setting ở 1 case ngôn ngữ khác (Ả Rập).
- **Andy tăng (▲ +3, từ 79→82)** — nhưng có severe flag KT1 mới (xem trên) cần Liz xem trước khi khen thưởng công khai.
- **Linda ổn định (▼ -1, từ 81→80)** — pattern lặp lại rõ nhất trong nhóm: hiểu sai ý khách rồi trả lời/kết luận sai trước khi xác nhận lại, xảy ra ở ít nhất 3 chat khác nhau trong tuần (đa ngôn ngữ: Bồ Đào Nha, Đức, Nhật) — nên ưu tiên sửa vì lặp lại nhiều lần.
- **Phoebe tăng nhẹ (▲ +2, từ 78→80)** — mẫu nhỏ nhất tuần này (11 chat, do ít volume), Skill là trục yếu nhất (25.4/33) — có 1 lần gửi nhầm tin nhắn tiếng Trung cho khách chat tiếng Đức.
- **Sonny giảm nhẹ (▼ -2, từ 83→81)** — xem severe flag KT1 trên. Ngoài ra có 1 case giải thích sai cơ chế Shopify BxGy discount khiến merchant launch campaign theo hướng sai, và 1 case phản hồi chậm khi khách đòi người thật 2 lần liên tiếp.

## Xu hướng đáng chú ý
- **Điểm trung bình team giảm ▼ -3.6** so với tuần trước (83.8 → 80.2) — phần lớn do 3 case KT1 mới xuất hiện (tuần trước 0 KT1) và Alyssa giảm mạnh từ mức đỉnh 92. Cần xem đây là biến động 1 tuần hay bắt đầu 1 xu hướng — theo dõi tiếp tuần sau.
- **Trục Skill (Xử lý)** là trục yếu nhất ở 5/9 CS (Alyssa, Jade, Linda, Phoebe, Andy) — lỗi phổ biến nhất là **KN5/KN6: hiểu sai ý khách hoặc kết luận trước khi đọc đủ ngữ cảnh**, xuất hiện lặp lại ở nhiều CS khác nhau trong cùng tuần — có thể đáng để đưa vào 1 buổi coaching chung cho cả team (không riêng ai) về "confirm lại ý khách trước khi trả lời/thao tác".
