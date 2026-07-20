# QA Weekly — Jade — 2026-W29 (13/07 – 19/07/2026)

**Điểm tuần:** 87/100 — Tốt  (▼ -1)  
**Đã QA:** 29 chat (loại 1)

| Trục | Điểm TB |
|---|---|
| 🧠 Mindset | 28/34 |
| 📚 Kiến thức | 31.1/33 |
| 🛠️ Xử lý | 27.7/33 |

## 📝 Nhận xét chung

Tuần này bạn làm việc rất có tâm và bền bỉ — điểm mạnh nổi bật nhất là ownership: theo case tới cùng, chủ động follow-up khi khách offline, và không ngại nói thật khi tính năng không hỗ trợ thay vì hứa suông. Case Instagram ở chat #12 cho thấy bạn có khả năng chẩn đoán kỹ thuật sâu chứ không chỉ làm theo script. Điểm cần tập trung tuần tới: để ý ngôn ngữ khách đang dùng trước khi gõ (chat #13 bạn trả lời tiếng Tây Ban Nha cho khách tiếng Ý, khiến khách phải tự phát hiện và nhắc lại — nếu lặp lại sẽ ảnh hưởng trực tiếp đến điểm Kỹ năng); đồng thời đọc lại tin nhắn dài trước khi gửi để tránh lỗi copy-paste lặp đoạn như ở chat #12, tuy nhỏ nhưng làm chat trông thiếu chăm chút.

## ✅ Điểm tốt tuần này

- Ownership rất tốt — thường xuyên chủ động follow-up bằng email khi khách offline giữa chừng, không để case đứt đoạn. Ví dụ chat #9 với khách khó tính David Clifford: dù ticket bị trễ nhiều lần, Jade vẫn kiên trì theo tới cùng, cập nhật rõ ràng từng bước ('Let me contact the tech team again to push the checking progress, and we will update you as soon as possible'). Tương tự ở chat #16, khi khách cực kỳ bực ('This time, every step I took using your plugin resulted in problems'), Jade vẫn giữ thái độ xin lỗi chân thành và tiếp tục hỗ trợ tới khi xong. (#9, #16)
- Kỹ năng chẩn đoán kỹ thuật xuất sắc — không chỉ báo 'để check' mà tìm ra đúng root cause. Ở chat #12, Jade phát hiện chính xác nguyên nhân AI không trả lời đủ trên Instagram là do Instagram chặn tin nhắn chứa link, và đề xuất giải pháp kỹ thuật cụ thể (auto-retry bỏ link) — đây là mức độ hiểu sản phẩm sâu, không phải trả lời chung chung. (#12)
- Trung thực khi tính năng không hỗ trợ, không hứa suông. Chat #8: 'at the moment, I am sorry to say this is a limitation of Chatty's email reply feature... I'll forward this feedback to our development team.' Chat #3 (FMI health): từ chối khéo yêu cầu gợi ý collection tự động vì lý do kỹ thuật hợp lý, không né tránh. (#8, #3)
- Thấu cảm tốt với khách hàng bực bội/mệt mỏi — không phòng thủ, không đẩy việc. Chat #17, khi khách nói 'I give up again', Jade đáp: 'I completely understand that the connection process can sometimes take a while... No worries at all', giữ đúng tinh thần đồng hành thay vì chỉ đóng chat. (#17)

## 🔧 Cần cải thiện

- **[KN3] Moderate** — Lệch ngôn ngữ với khách — khách hỏi bằng tiếng Ý suốt cả chat nhưng Jade trả lời bằng tiếng Tây Ban Nha, khiến khách phải tự nhận ra và nhắc lại. (#13)
  - Dẫn chứng: Chat #13: khách viết 'come le attivo', 'ma non c'è un posto per digitare' (tiếng Ý) — Jade trả lời '¿Podrías compartir cómo no están funcionando las preguntas frecuentes...?' (tiếng Tây Ban Nha), khách phải gõ lại 'italiano' để chỉnh.
  - → Trước khi gõ trả lời, liếc lại ngôn ngữ khách vừa dùng ở tin gần nhất — đặc biệt sau khi mình vừa handle case tiếng khác trước đó, dễ bị quán tính gõ nhầm.
- **[KN1] Low** — Copy-paste sót, gửi tin nhắn bị lặp nguyên một đoạn — trông thiếu chuyên nghiệp và làm khách phải đọc dư. (#12)
  - Dẫn chứng: Chat #12: 'Puedes mejorar la respuesta de la IA agregando más datos de entrenamiento, como Preguntas/Instrucciones... Puedes mejorar la respuesta de IA añadiendo más datos de entrenamiento, como preguntas e instrucciones' — cùng một nội dung lặp lại 2 lần trong 1 tin.
  - → Đọc lại tin trước khi gửi khi soạn đoạn dài/giải thích nhiều bước, nhất là khi copy từ note cũ.
- **[KN2] Low** — Đôi lúc hỏi lại khách thay vì trả lời thẳng câu hỏi đơn giản, làm chat kéo dài thêm một vòng không cần thiết. (#1)
  - Dẫn chứng: Chat #1: khách hỏi 'does it have my websites infromation embedded into it', Jade đáp 'Can you kindly explain your request further so I can better support you?' thay vì trả lời trực tiếp là AI học được từ trang/URL đã thêm.
  - → Với câu hỏi rõ ràng, trả lời thẳng trước rồi mới hỏi thêm chi tiết nếu cần, thay vì hỏi ngược lại ngay.

## 🌟 Xin review (chỉ ghi nhận, KHÔNG tính điểm)

- Đã xin review ở **4/4** chat phù hợp (đúng lúc: 4, sai lúc: 0)
- Tuần này Jade xin review đúng lúc ở cả 4/4 chat khách rõ ràng hài lòng và Review: chưa có review (chat #1, #6, #7, #14) — đều xin ngay sau khi khách vừa cảm ơn/xác nhận xong việc, không có ca nào bị bỏ lỡ hay xin sai lúc trong mẫu quan sát được.
- Chat KH đã có review thì không cần xin lại — đã loại khỏi đếm.

## 📈 So với tuần trước

- Điểm 88 → 87 (▼ -1)
- Lỗi lặp lại từ 2026-W28: KN3 — cần ưu tiên sửa
- Lỗi tuần trước đã hết: QT18, QT9 👏
