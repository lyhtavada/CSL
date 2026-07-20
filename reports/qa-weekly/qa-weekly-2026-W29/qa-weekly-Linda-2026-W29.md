# QA Weekly — Linda — 2026-W29 (13/07 – 19/07/2026)

**Điểm tuần:** 81/100 — Tốt  (▼ -7)  
**Đã QA:** 30 chat

| Trục | Điểm TB |
|---|---|
| 🧠 Mindset | 28/34 |
| 📚 Kiến thức | 27.1/33 |
| 🛠️ Xử lý | 26.1/33 |

## 📝 Nhận xét chung

Tuần này bạn xử lý khối lượng chat DFY setup rất lớn và đa ngôn ngữ (Tây Ban Nha, Đức, Hy Lạp, Nhật, Hà Lan, Bồ Đào Nha...), phong cách nhất quán: luôn recap lại yêu cầu trước khi thao tác và theo tới cùng những case kéo dài nhiều ngày (export data, billing dispute, feature request) mà không bỏ dở giữa chừng — đây là điểm mạnh rõ nhất. Nhưng có hai lỗi cần sửa ngay: ở chat billing (#17) bạn khẳng định sai nguồn gốc phí trước khi verify kỹ, khiến khách phải tự sửa lại thông tin cho bạn — hệ quả là mất uy tín trong 1 case liên quan tiền bạc; và có 2 lần bạn gửi nhầm sang tiếng Ý giữa cuộc chat tiếng Tây Ban Nha (#2, #21), làm khách bối rối phải hỏi lại. Ở case ANZA (#1), do chưa chốt rõ yêu cầu cuối cùng ngay từ đầu nên phải sửa đi sửa lại 3-4 lần, khách bực rõ ràng trong chat — tuần tới cần paraphrase lại đúng ý khách trước khi bắt tay thao tác để tránh làm lại nhiều lần.

## ✅ Điểm tốt tuần này

- Ownership rất tốt trên case dài ngày — nhớ chính xác lịch sử xử lý và grounding lại cho khách thay vì lặp lại từ đầu, ví dụ 'we already worked on this yesterday... we resolved that issue for you on July 2nd' (#30), và kiên nhẫn không né tránh khi khách liên tục hỏi dồn 'any update?' nhiều lần trong ngày (#18). (#18, #30)
- Chủ động đề xuất thêm giá trị dù khách chưa hỏi — liên tục gợi ý bật AI Re-engage/Follow-up, kiểm tra Custom Knowledge, đề xuất cải thiện welcome message... ở gần như mọi case DFY setup. (#4, #6, #8, #12)
- Giữ bình tĩnh, thấu cảm với khách khó tính/bực bội mà không phòng thủ hay đẩy việc, ví dụ khi khách nói thẳng 'you're not doing what I want' (#13) hay khách liên tục thúc giục cả tuần (#30). (#13, #30)
- Trình bày rõ ràng, có recap từng điểm trước khi thao tác thật (không đoán ý khách), giúp khách dễ confirm/correct trước khi bạn set up, ví dụ recap 8 mục cấu hình AI ở #15 và #28. (#15, #28)

## 🔧 Cần cải thiện

- **[KT1] High** — Khẳng định sai nguồn gốc phí billing trước khi verify kỹ, phải để khách tự sửa lại cho mình (#17)
  - Dẫn chứng: CS (Linda): "These charges are Transaction fees, which are charged by Shopify, not Chatty... Chatty only charges for fees related to the app itself" → Customer: "No, these are from chatty" → CS (Linda): "oh ok you're right"
  - → Với câu hỏi liên quan tiền bạc/billing, luôn mở screenshot chi tiết (arrow/breakdown) và verify kỹ trước khi kết luận nguồn phí — sai ở đây rất dễ mất niềm tin của khách.
- **[KN3] Moderate** — Gửi nhầm sang tiếng Ý giữa cuộc chat đang bằng tiếng Tây Ban Nha, lặp lại 2 lần trong tuần (#2, #21)
  - Dẫn chứng: CS (Linda): "Grazie mille. E quando un cliente chiede di parlare con un agente umano oppure ha una richiesta post-vendita... Preferiresti che l'IA..." (trong khi khách hỏi bằng tiếng Tây Ban Nha ở #2); tương tự "Grazie mille, sto controllando la conversazione e i dati dell'AI, al momento ti farò sapere a breve." ở #21
  - → Rà lại canned response/template trước khi gửi để tránh dính nhầm ngôn ngữ khác không phải ngôn ngữ khách đang dùng — làm khách phải dừng lại để hỏi lại, kéo dài chat không cần thiết.
- **[KN6] Moderate** — Chưa chốt rõ yêu cầu cuối cùng của khách trước khi thao tác, phải sửa lại nhiều lần khiến khách bực (#1)
  - Dẫn chứng: Customer: "why is it still showing when it's been edited theee times already this will make 4"
  - → Trước khi apply thay đổi (đặc biệt welcome message/flow phức tạp), paraphrase lại chính xác nội dung cuối cùng khách muốn và xin confirm 1 lần rõ ràng, thay vì set rồi sửa từng phần theo phản hồi rời rạc.

## 🌟 Xin review (chỉ ghi nhận, KHÔNG tính điểm)

- Đã xin review ở **7/10** chat phù hợp (đúng lúc: 7, sai lúc: 0)
- Đã xin review đúng lúc ở 7/10 chat khách hài lòng phù hợp (#6, #7, #14, #19, #20, #25, #26) — timing đều tốt, khách vừa cảm ơn/hài lòng là xin ngay, không có lần nào xin sai lúc. Bỏ lỡ vài chat vàng khách rất hài lòng (#9, #23, #27) mà không chủ động xin (để đồng nghiệp khác xin hoặc bỏ qua) — tuần tới nên tận dụng thêm những khoảnh khắc này.
- Chat KH đã có review thì không cần xin lại — đã loại khỏi đếm.

## 📈 So với tuần trước

- Điểm 88 → 81 (▼ -7)
- Lỗi lặp lại từ 2026-W28: KN3 — cần ưu tiên sửa
- Lỗi tuần trước đã hết: KN1, QT22 👏

## 🚨 Flag cho Liz

- Chat #17 — CS khẳng định sai nguồn phí billing (Shopify vs Chatty) trước khi verify, tự sửa lại khi khách phản bác — Liz nên xem qua để đánh giá mức độ nghiêm trọng với case liên quan billing.
