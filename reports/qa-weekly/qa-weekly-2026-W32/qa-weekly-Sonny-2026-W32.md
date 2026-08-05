# 📋 QA TUẦN — BÁO CÁO CỦA Sonny
🗓️ Tuần 2026-W32 · 29/07 – 04/08/2026
━━━━━━━━━━━━━━━━━━━━━━━━━━━

📊 **Điểm tuần:** 81/100 — Tốt  (▼ -5 so với tuần trước)
🔍 Đã QA: 30 chat
🧠 Mindset: 27.6/34 · 📚 Kiến thức: 26.8/33 · 🛠️ Xử lý: 26.7/33

📝 **Nhận xét chung**
Bạn xử lý được rất nhiều case kỹ thuật khó của Joy (tính điểm VIP tier, point expiration logic, currency format, custom CSS di chuyển widget, tích hợp LINE) một cách bài bản, kiên trì theo tới cùng và không né việc — đây là điểm mạnh rõ rệt nhất, thể hiện đặc biệt tốt ở các case khách khó tính, hỏi dồn dập (chat #3, #16, #25). Tuy nhiên có vài lỗ hổng cần sửa ngay: 2 lần gửi nhầm tin nhắn không chuyên nghiệp thẳng vào chat với khách (tiếng Việt informal ở chat #1, tin nhắn rác "儿子" ở chat #29) — nếu khách để ý sẽ mất điểm chuyên nghiệp ngay lập tức; và ở chat #23 bạn chẩn đoán sai vấn đề deliverability dựa trên nhầm screenshot của khách khác, khiến khách phải tự sửa lại cho bạn — cần chậm lại xác nhận đúng dữ liệu trước khi kết luận, tránh làm khách mất thời gian sửa lỗi hộ mình.

✅ **Điểm tốt tuần này**
- [P1] Xử lý sâu, đúng kỹ thuật các case Joy phức tạp (point expiration logic, VIP tier calculation, currency format, custom CSS) — theo tới cùng, có video/screenshot chứng minh, không bỏ cuộc dù vấn đề khó (chat #10, #15, #18, #25) (#10, #15, #18, #25)
- [P2] Kiên nhẫn và giữ chuyên nghiệp với khách khó tính, hỏi dồn dập hoặc phản ứng gay gắt — vẫn quay video test nhiều lần để chứng minh, không nổi nóng (chat #3 khách TQ về widget position, chat #16 khách giục liên tục) (#3, #16)
- [P3] Chủ động đề xuất giải pháp thêm cho khách chưa kịp hỏi — gợi ý demo store, unified widget, cách test scenario khác nhau (chat #1, #2, #26) (#1, #2, #26)
- [P4] Giải thích có bước, kèm ảnh/video rõ ràng giúp khách tự làm theo được ngay (chat #7 LINE integration, #14 loyalty hub access) (#7, #14)

🔧 **Cần cải thiện**
- **[KN1] Moderate** — Gửi tin nhắn tiếng Việt thông tục (như đang nói chuyện nội bộ với đồng nghiệp) thẳng vào khung chat khách nước ngoài — thiếu chuyên nghiệp, khách không hiểu và có thể nghi ngờ chất lượng support (#1)
  - Dẫn chứng: [07:21:10] CS (Sonny Truong): nó bị thế đấy, trên store oke :v
  - → Luôn nhắn nội bộ qua kênh riêng (Slack/note), không gõ nhầm vào ô chat khách. Kiểm tra lại trước khi gửi nếu đang chat song song nhiều nơi.
- **[KN1] Low** — Gửi 1 tin nhắn rác/lỗi "儿子" (nghĩa 'con trai', không liên quan) vào chat với khách trước khi trả lời thật — trông như thao tác nhầm hoặc gõ tắt chưa xong (#29)
  - Dẫn chứng: [07:51:29] CS (Sonny): 儿子
  - → Kiểm tra nội dung trước khi gửi, đặc biệt khi dùng gõ tắt/AI hỗ trợ soạn tin
- **[KN5] Moderate** — Chẩn đoán sai nguyên nhân email vào spam (nói khách dùng @outlook.com làm sender) dựa trên ảnh chụp không phải của khách, khiến khách phải tự đính chính lại (#23)
  - Dẫn chứng: [00:57:03] Customer (Prapti Priya): Hi I don't think above screesnhot is mine.  please see the correct screenshot as attached / I do have a brand domain
  - → Xác nhận lại đúng screenshot/dữ liệu của đúng khách trước khi đưa ra kết luận kỹ thuật, tránh gây hiểu lầm và mất thời gian khách phải sửa lại giúp mình
- **[KT2] Low** — Báo khách gói Pro Chatty có ưu đãi "$1 cho tháng đầu" — con số này không xuất hiện trong bảng giá KB hiện tại (Pro = $68.99/mo, $58.99/mo annual), cần Liz xác nhận đây có phải promo hợp lệ đang chạy hay không trước khi CS tiếp tục dùng câu này (#6)
  - Dẫn chứng: [04:37:18] CS (Sonny): Yes it will be $1 for the first month.
  - → Verify với Liz/team sale xem promo "$1 tháng đầu" cho Pro plan có đang active không, tránh hứa nhầm giá cho khách khác

🌟 **Xin review (chỉ ghi nhận, không tính điểm)**
- Đã xin review ở **3/6** chat phù hợp (đúng lúc: 3, sai lúc: 1)
- Đã xin review đúng lúc ở 3/6 chat phù hợp (khách vừa cảm ơn/hài lòng) — chat #2, #4, #13. Có 1 lần xin dư thừa ở chat #10 dù header đã ghi 'ĐÃ CÓ review' (không cần xin lại, dễ làm phiền khách). Nhìn chung hành vi xin review ổn, chỉ cần double-check header trước khi mời.

📈 **So với tuần trước**
- Điểm 86 → 81 (▼ -5)
- Trục: Mindset 28.5→27.6, Kiến thức 29.7→26.8, Kỹ năng 27.5→26.7
- Lỗi lặp lại từ tuần trước: KN1
- Lỗi tuần trước đã hết: KN3, QT9 👏
- Lỗi mới tuần này: KN5, KT2

🔗 **Chat đã QA (30):**
<https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_894f5998-cde6-47bf-b4d6-840bc8bd1deb|#1 Orsolya Lele> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_087721ad-7b8c-4502-bc0a-ecd3711c2a64|#2 eugene galang> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_c1c89aef-886b-43bd-a2ac-51994769fcbc|#3 Sparkace LAUNCH> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_c3167910-59ed-41c6-9c44-8b51f52502f9|#4 Jovilyn Arciaga> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_cd81ac62-b4ee-4256-bc43-62aa3059b5e1|#5 Nissoplus> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_cefa0af9-d403-4582-894f-4bbe543bf790|#6 Enveseur> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_193b8bef-9be7-4360-a323-33576213b38a|#7 wilson wu> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_67706346-c712-4655-9117-738429a672d9|#8 ZU SHAN> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_4bbe326a-a174-4b64-9992-6e2a29e897cf|#9 My Store Admin> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_11a7563a-a459-4766-9cc1-aa81a71c99c9|#10 Francisco Tormo> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_7cd52d5c-7475-465d-bbd7-c264e566359e|#11 Solomon Ficklin> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_083a6b9b-9d7c-4a95-b5b2-ef9efd4d494d|#12 יפה שרעבי> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_7897647a-350c-4ad5-81bd-d19030353f7f|#13 Ahmed AlMahmoud> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_25affd5c-5103-4ff0-ab0e-499e43dd759c|#14 Edward Brotherton> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_96e6c671-d4b2-4286-bd27-b39abacebc7f|#15 Nicholas Davies> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_03ac002a-cd59-4c72-9259-de2d7c2fed50|#16 奕群 黄> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_d3627ec4-a3e5-4a9f-ada9-f4b9d654b68c|#17 Jonathan Tang> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_b401eaec-0e89-4606-aa12-e7c14c155201|#18 shi tao wang> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_4596fcf3-5b13-4714-af3f-fdad45dd23c5|#19 My Store Admin> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_2092b149-8bbe-447f-8ef7-1a6095d8ba6b|#20 Nicola> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_1b69c3c0-4a56-4098-9884-bcb2b4fcb3f2|#21 Ali Haider> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_de604a1c-b4a0-491f-8e59-03a067fcbc12|#22 Oluwafemi Oyenekan> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_ce825edc-1e14-4f6d-85fb-46b8150843db|#23 Prapti Priya> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_347e2400-ef11-4725-b8b5-7db91fd1e877|#24 Justin Wong> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_73b1b5e1-3806-4447-a9d6-a6145285b892|#25 Direct Wines ECL> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_2191463d-57c4-4ba1-a765-ad1c6949b696|#26 Kuo-Hung Liang> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_abafd80a-c5be-497a-8347-bea67facd4ae|#27 Ahmed AlMahmoud> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_03f885cc-0a96-4260-aae9-fd44f444dea9|#28 IKJUN JANG> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_bf4dca27-5033-4ae9-9f9d-b2e6ff553d77|#29 Chan Henry Ling Yan> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_7a1f0a3e-a5dd-4e91-882c-8ac04c842b14|#30 laurie Stephens>

_Tin tự động từ hệ thống QA của team CS 2. Có gì thắc mắc cứ nhắn lại Liz nhé 💬_