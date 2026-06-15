# QA Tuần 2026-W24 — Phoebe
**App:** Chatty · **Kỳ:** 08/06 – 14/06/2026

## 📊 Điểm tuần: 79/100 — Đạt  (▼ -4 so với W23: 83)
- 🧠 Mindset 26.0/34 · 📚 Kiến thức 27.2/33 · 🛠️ Xử lý 26.0/33
- 🔍 Đã QA: 29 chat (loại 1)
- Trục yếu nhất: **Mindset**

## 📝 Nhận xét chung
Phoebe xử lý tốt các ca setup cơ bản — AI agent, live chat, chatbox — với thái độ chủ động, thường phát hiện thêm vấn đề mà merchant chưa hỏi (theme embed chưa bật, notification chưa cấu hình, conversation starter còn default). Điểm yếu rõ nhất tuần này là xử lý ca kỹ thuật phức tạp: khi không có đáp án chắc chắn, bạn có xu hướng dừng ở mức gửi link YouTube hoặc câu hỏi mở thay vì escalate rõ ràng. Lỗi nhỏ nhưng lặp lại là gửi tin nhắn trùng (duplicate send) và đôi khi trả lời sai ngôn ngữ khách. Đây là tuần đầu có báo cáo — chưa có baseline để so sánh.

## ✅ Điểm tốt
- Chủ động phát hiện vấn đề chưa được hỏi: thường xuyên check và báo merchant những thứ họ chưa để ý như theme App Embed chưa bật, conversation starters vẫn là default, AI lifetime limit cần dùng test mode thay vì live store. Ví dụ: 'our app has not been enabled in the Theme's App Embed yet. You are advised to click here to activate and save it' (chat #25); 'the Free plan includes 50 AI lifetime conversations. Testing on the live site will count toward these available slots. So you are advised to go to AI test mode instead' (chat #7). (#7 #9 #10 #23 #25)
- Giải thích analytics proactive chat rõ ràng và đúng kỹ thuật ở chat #11: phân biệt được lifetime revenue per campaign vs 7-day dashboard aggregation, breakdown từng campaign views khớp với tổng. Thể hiện nắm vững sản phẩm khi gặp ca phức tạp. (#11)

## 🔧 Cần cải thiện
- **[KN3] · Moderate** Gửi tin bằng tiếng Anh trong khi khách nhất quán viết tiếng Pháp — khách phải tự dịch, kéo dài ca support. (#5)
   > [16:05:14] CS (Phoebe): 'Could you please share with me further? As per checking, I can see the chatbox is now displaying on the live store:' — và [16:17:17] CS (Phoebe): 'Could you please try to check the app notification as suggested in this video? https://www.youtube.com/watch?v=_p4WPJQcTPM' — trong khi khách (E-VELO) liên tục viết tiếng Pháp suốt chat #5.
   → Khi khách viết tiếng Pháp (hoặc bất kỳ ngôn ngữ nào khác English), luôn trả lời bằng cùng ngôn ngữ đó — Crisp có live translate hỗ trợ bạn. Chỉ cần paste tiếng Việt/English vào và để Crisp translate, hoặc reply thẳng tiếng Pháp nếu bạn biết.
- **[QT22] · Low** Ca notification sound trên Samsung A05 (chat #5) — Phoebe không giải quyết được và chỉ gửi link YouTube generic, kết thúc bằng câu hỏi mở chứ không escalate rõ ràng cho tech team kiểm tra. (#5)
   > [16:44:58] CS (Phoebe): 'Je viens de chercher comment activer le son pour une application spécifique, et je suis tombé sur cette vidéo : https://www.youtube.com/watch?v=y2Ogm7iH-YM. Elle n'est pas spécifique à votre appareil ni à notre application' — tự thừa nhận video không đặc thù cho case này nhưng vẫn gửi.
   → Khi bạn không có đáp án kỹ thuật chắc chắn sau 2-3 lượt thử, hãy escalate rõ: 'Để tôi báo team kỹ thuật kiểm tra thêm về thiết bị Samsung A05 của bạn và cập nhật trong [thời gian cụ thể].' Đừng để ca lơ lửng với link video generic.
- **[KN1] · Low** Gửi trùng tin nhắn trong cùng giây ở nhiều chat — khách nhận 2 bản giống hệt nhau, trông thiếu chuyên nghiệp. (#3 #5 #17)
   > [15:26:24] CS (Phoebe): 'As per checking, I can see that the chatbox widget is displaying perfectly on your end now ^^ All necessary options have been turned on' — rồi [15:26:31] CS (Phoebe): cùng nội dung đó lần nữa (chat #17). Tương tự ở chat #3 (greeting gửi 2 lần 15:26:45-46) và chat #5 (16:05:14 gửi 2 lần).
   → Trước khi gửi, kiểm tra xem tin đã appear chưa. Nếu giao diện lag, chờ 5-10 giây trước khi nhấn Send lại. Duplicate message làm mất tin tưởng về tính chuyên nghiệp.

## 🌟 Xin review (chỉ ghi nhận, KHÔNG tính điểm)
- Đã xin 3/4 chat phù hợp (đúng lúc 3, chưa đúng lúc 0).
- Phoebe xin review đúng lúc ở 3/4 chat phù hợp (chats #6, #8, #15 — đều sau khi khách vui, issue đã xong). Bỏ lỡ 1 chat: chat #16 (Water Fountain) — khách nói 'Viele Dank' và đã tự giải quyết xong, đây là thời điểm vàng nhưng không có xin review. 3 chat có segment 'ĐÃ CÓ review' (#3, #5, #27) đã loại khỏi đếm đúng theo quy định.

## 📈 So với tuần trước (W23)
- Điểm 83 → 79 (▼ -4)
