# QA Weekly — Audrey — 2026-W29 (13/07 – 19/07/2026)

**Điểm tuần:** 87/100 — Tốt  (▲ +6)  
**Đã QA:** 29 chat

| Trục | Điểm TB |
|---|---|
| 🧠 Mindset | 31/34 |
| 📚 Kiến thức | 28/33 |
| 🛠️ Xử lý | 27/33 |

## 📝 Nhận xét chung

Tuần này bạn thể hiện rất rõ chất "ôm việc tới cùng" — nhiều case dài, phức tạp, phải bàn giao qua nhiều ca vẫn được bạn theo sát, không đóng lửng, kể cả với khách đang bực bội hoặc case đã kéo dài nhiều giờ trước khi tới tay bạn. Đây là điểm mạnh nổi bật nhất, giúp giữ được khách trong những tình huống dễ mất thiện cảm. Điểm cần cải thiện rõ nhất: đôi lúc phản hồi hơi nhanh mà chưa paraphrase lại đúng ý khách khiến phải tự sửa (chat #14), và bỏ lỡ vài thời điểm vàng để mời khách để lại review dù khách vừa cảm ơn xong — nên biến bước xin review thành thói quen chốt case mặc định thay vì chỉ làm ở một số chat. Không phát hiện lỗi kiến thức sai nghiêm trọng (KT1) hay thái độ thiếu chuyên nghiệp trong mẫu tuần này.

## ✅ Điểm tốt tuần này

- Ownership rất tốt — theo tới cùng những case dài, phức tạp, nhiều bước xử lý qua nhiều giờ/nhiều ngày mà không đóng lửng: chat #1 kiên trì gỡ lỗi web push notification qua nhiều trình duyệt tới đêm khuya, cuối cùng gửi hẳn 1 email hướng dẫn Edge browser chi tiết từng bước dù đã rất muộn; chat #22 theo sát case Loop Subscriptions phức tạp, giải thích kỹ nguyên nhân kỹ thuật thay vì bỏ cuộc. (#1, #22, #27)
- Chủ động xác nhận thông tin trước khi hành động và luôn thông báo bước tiếp theo rõ ràng — ví dụ chat #7 hỏi đúng email khách hàng cần kiểm tra, xác nhận store URL, rồi quay lại cập nhật kết quả cụ thể thay vì im lặng chờ. (#7, #3, #20)
- Giữ bình tĩnh, thấu cảm tốt khi tiếp nhận khách đang bực/mệt mỏi do CS trước xử lý lâu — chat #5 nhận bàn giao 1 khách đã mất 10 tiếng bực bội, Audrey vẫn kiên nhẫn rà soát lại toàn bộ setup và tiếp tục hỗ trợ mà không né tránh. (#5, #11)
- Trình bày có ảnh chụp màn hình kèm hướng dẫn từng bước, dễ theo dõi — khách làm theo được ngay ở nhiều case (đổi tier, sync điểm, export data). (#16, #23, #28)

## 🔧 Cần cải thiện

- **[KN5] Low** — Hiểu sai yêu cầu khách trước khi tư vấn, phải tự sửa lại ngay sau đó (#14)
  - Dẫn chứng: Khách hỏi "Where do I adjust the size of the text circled in green?" nhưng Audrey trả lời "I noticed that you'd like to edit the Guest view welcome message on your widget..." — sai trọng tâm, phải tự nhận "Ah, I see! Sorry for my confusion" ở tin nhắn kế tiếp.
  - → Paraphrase lại đúng ý khách (đặc biệt câu hỏi ngắn/mơ hồ) trước khi đưa hướng dẫn, tránh đoán nhầm làm khách phải giải thích lại.
- **[review-ask] Low** — Bỏ lỡ thời điểm vàng để xin review dù khách vừa cảm ơn/hài lòng và case chưa có review (#23, #26)
  - Dẫn chứng: Chat #23: khách nói "thank you", Audrey đáp "That's amazing! It's the least I could do" rồi hỏi tiếp có cần hỗ trợ gì không — không xin review. Chat #26: khách nói "ありがとうございました" (đã hài lòng, hết câu hỏi), Audrey chỉ đáp "どういたしまして！" mà không mời để lại review.
  - → Biến việc mời review thành bước chốt mặc định mỗi khi khách vừa cảm ơn và case chưa có review (đã làm tốt ở chat #1, #4, #7) — áp dụng nhất quán hơn.
- **[KN1] Low** — Gửi tin nhắn cụt/lỗi chính tả, có thể gây khó hiểu nhẹ cho khách (#1)
  - Dẫn chứng: Tin nhắn chỉ có 1 từ "You" gửi cho khách lúc 00:00:33 (chat #1), rõ ràng là gõ thiếu ("You're welcome" bị cắt) trước khi gửi.
  - → Đọc lại tin trước khi gửi, đặc biệt các tin ngắn dễ bị gửi nhầm/thiếu.

## 🌟 Xin review (chỉ ghi nhận, KHÔNG tính điểm)

- Đã xin review ở **3/5** chat phù hợp (đúng lúc: 3, sai lúc: 0)
- Đã xin review đúng lúc 3/5 chat phù hợp (#1, #4, #7) — đều xin ngay sau khi khách vừa cảm ơn/hài lòng, cách xin tự nhiên. Bỏ lỡ 2 chat khách rõ ràng hài lòng mà chưa xin (#23, #26) — nên tận dụng thêm những thời điểm này.
- Chat KH đã có review thì không cần xin lại — đã loại khỏi đếm.

## 📈 So với tuần trước

- Điểm 81 → 87 (▲ +6)
- Lỗi lặp lại từ 2026-W28: KN1 — cần ưu tiên sửa
- Lỗi tuần trước đã hết: KN2, KN3, QT25 👏
