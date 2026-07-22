# QA Weekly — Hana — 2026-W29 (13/07 – 19/07/2026)

**Điểm tuần:** 78/100 — Đạt  (▼ -7)  
**Đã QA:** 30 chat

| Trục | Điểm TB |
|---|---|
| 🧠 Mindset | 26.5/34 |
| 📚 Kiến thức | 26.5/33 |
| 🛠️ Xử lý | 25.3/33 |

## 📝 Nhận xét chung

Tuần này bạn thể hiện sự kiên nhẫn và chăm chỉ rõ rệt — xử lý được cả những case khách rất khó tính, đi kèm thói quen tốt là verify với leader trước khi chốt thông tin nhạy cảm như giá cả thay vì đoán bừa. Điểm mạnh nhất là khả năng tổng hợp/giải thích có cấu trúc khi case phức tạp (checklist pre-launch, phân tích Member vs Guest). Tuy nhiên điểm số 78 bị kéo xuống bởi 2 case đáng chú ý: một lần bật nhầm tính năng ảnh hưởng TOÀN BỘ khách ghé site thay vì đúng phạm vi khách yêu cầu (case #15), và một lần dùng tài nguyên giới hạn của khách (quota dịch) mà chưa xin phép trước (case #8) — cả hai đều là kiểu lỗi "thao tác vội trên store thật" cần cẩn trọng hơn, vì hậu quả không chỉ dừng ở 1 khách mà lan rộng hoặc không hoàn tác được. Tuần tới nên tập trung: xác nhận rõ phạm vi/điều kiện trước khi bật bất kỳ setting ảnh hưởng diện rộng, và luôn xin phép trước khi đụng vào tài nguyên không revert được của khách.

## ✅ Điểm tốt tuần này

- Chủ động xây checklist pre-launch đầy đủ 7 bước cho khách sắp launch chương trình loyalty, không đợi khách hỏi mới trả lời — chuẩn bị kỹ trước cả các case KH có thể gặp lỗi khi go-live. Quote: "Here is your complete pre-launch checklist to make sure everything is set up correctly before you go live: Step 1 — Review your earning programs..." (#9)
- Trước khi trả lời câu hỏi về giá, chủ động check với Liz thay vì tự đoán, tránh báo sai giá cho khách cũ (grandfathered pricing) — đúng tinh thần verify trước khi nói. (#11)
- Giải thích rành mạch, có cấu trúc 1-2-3 rõ ràng khi làm rõ nguyên nhân KH không nhận điểm (Member vs Guest logic, mốc thời gian), khách hiểu ngay không phải hỏi lại nhiều. (#25)
- Chủ động phát hiện và fix lỗi UI (nút chatbox đè lên nút Add to cart) mà khách chưa kịp report, đi thêm một bước vì lợi ích KH. (#2)

## 🔧 Cần cải thiện

- **[KN5] High** — Bật tính năng 'Instant popup' khiến widget tự động bật lên với TẤT CẢ khách ghé site, trong khi khách chỉ yêu cầu widget mở sau khi login — gây ảnh hưởng diện rộng trên store thật, phải nhờ CS khác (Rosie) sửa lại. (#15)
  - Dẫn chứng: Hana: "I have enabled the Instant popup feature to ensure the widget working as requested" → khách phản hồi bực: "It seems our website homepage is now opening the rewards widget every time someone visits. That is not what we wanted... Can our homepage be reverted back asap?"
  - → Trước khi bật 1 setting ảnh hưởng TOÀN BỘ visitor (không chỉ 1 luồng cụ thể KH yêu cầu), phải confirm lại đúng phạm vi/điều kiện trigger và tự test lại kết quả trước khi báo done.
- **[KN1] Moderate** — Gõ nhầm/dán nhầm ghi chú nội bộ (tiếng Trung "收藏", và "rv") thẳng vào khung chat với khách, khiến khách hoang mang không hiểu ý. (#20)
  - Dẫn chứng: CS (Hana): "收藏" rồi "rv" gửi liền — khách phản hồi bối rối: "很快就好？的话那就 ..."
  - → Đọc lại tin nhắn trước khi gửi, không copy-paste note nội bộ/shorthand vào ô chat khách.
- **[QT_process] Moderate** — Dùng hết 1 trong 2 quota auto-translate giới hạn (không hoàn tác được) của Shopify Translate & Adapt trên store khách mà chưa xin phép trước, khiến khách bực vì đây là tài nguyên không thể revert. (#8)
  - Dẫn chứng: Khách: "But your team used one of the quota yesterday, can you revert it?... you should ask before doing something is not revertable" → Hana xin lỗi: "Please accept our apologies for not asking your permission first..."
  - → Với bất kỳ thao tác dùng tài nguyên giới hạn/không hoàn tác được trên store khách (quota, discount code, v.v.), luôn xin phép rõ ràng trước khi làm, kể cả khi đang muốn xử lý nhanh giúp khách.
- **[KN1] Low** — Gửi đoạn code HTML thiếu dấu "<" mở thẻ khi hướng dẫn khách thêm unsubscribe link, khiến khách vẫn gặp lỗi y hệt sau khi dán code. (#29)
  - Dẫn chứng: Hana: "You can try this HTML code : p><br>Don't like these emails? <a href=\"{{unsubscribe}}\">..." — khách: "i added but the same error"
  - → Kiểm tra/copy kỹ code trước khi gửi cho khách, nhất là HTML — thiếu 1 ký tự là hỏng cả block.
- **[QT9] Low** — Hỏi lại gần như y hệt 1 câu confirm hai lần liên tiếp mà không liên kết với câu trước, khiến chat có cảm giác lặp/không theo dõi kỹ. (#12)
  - Dẫn chứng: "May I know that the reward button is currently not showing after login correct?" rồi sau đó lại "May I confirm that you want to show the reward button here, correct?"
  - → Lướt lại 2-3 tin nhắn gần nhất trước khi hỏi lại một câu confirm để tránh hỏi trùng.

## 🌟 Xin review (chỉ ghi nhận, KHÔNG tính điểm)

- Đã xin review ở **9/10** chat phù hợp (đúng lúc: 9, sai lúc: 0)
- Xin review khá tự nhiên, đúng lúc khi KH vừa cảm ơn/hài lòng ở phần lớn các case (ví dụ #2, #4, #7, #17, #19, #26) — nhiều case KH đồng ý để lại review ngay tại chat. Một vài chat (#9, #11, #24) đã có review Shopify từ trước nên không cần xin lại, Hana có ghi nhận đúng và không xin thừa (dù vẫn mời riêng review G2 cho chương trình quà tặng $50 — không tính vào đây vì khác nền tảng Shopify).
- Chat KH đã có review thì không cần xin lại — đã loại khỏi đếm.

## 📈 So với tuần trước

- Điểm 85 → 78 (▼ -7)
- Lỗi lặp lại từ 2026-W28: KN1 — cần ưu tiên sửa
- Lỗi tuần trước đã hết: KN3, KT1 👏
