📋 *QA TUẦN — BÁO CÁO CỦA Linda*
🗓️ Tuần W36 · 02/09 – 08/09/2026
━━━━━━━━━━━━━━━━━━━━━━━━━━━

📊 *Điểm tuần:* 81/100 — Tốt  (▲ +1 so với tuần trước (80→81))
🔍 Đã QA: 17 chat
Breakdown: 🧠 Mindset 27.2/34 · 📚 Kiến thức 27.4/33 · 🛠️ Xử lý 26.7/33

📝 *Nhận xét chung*
Tuần này bạn xử lý ổn định, đặc biệt mạnh ở việc theo tới cùng những case kỹ thuật dài hơi (chat #3 xác định đúng nguyên nhân chặn forward email do M365, chat #15 tự đặt reminder để duy trì gửi export hàng tuần đều đặn cho khách suốt nhiều ngày). Điểm cần thẳng thắn nhìn nhận: có chat bạn đưa ra số liệu chưa chính xác khi khách đang bực (chat #4, nói "506 sản phẩm đã sync" trong khi khách chứng minh Shopify có 615 sản phẩm active) — việc này làm khách nghi ngờ thêm và kéo dài case đã trễ hẹn từ thứ Sáu. Ngoài ra có 2 chat đã có review từ trước (header ghi rõ) mà bạn vẫn mời khách để lại review lần nữa — nên kiểm tra field Review trước khi hỏi, tránh làm phiền khách không cần thiết. Hướng tập trung tuần tới: xác nhận số liệu/dữ kiện chắc chắn trước khi báo cho khách, nhất là với case đã kéo dài và khách đang sốt ruột.

✅ *Điểm tốt tuần này*
• [P1] Ownership tốt với case dài hơi — chat #3 theo tới cùng vấn đề email forwarding bị M365 chặn, tự tra cứu và đưa ra fix chính xác (SPF/Outbound spam policy), khách xác nhận "Verified!" ngay sau đó. Chat #15 chủ động đặt reminder nội bộ để duy trì gửi export dữ liệu đều đặn mỗi tuần cho khách dù đây là việc lặp lại tốn công. (#3, #15)
• [P5] Kiến thức kỹ thuật chính xác và nhất quán — chat #11 giải thích đúng và nhất quán về cơ chế tên ẩn danh (feature request đang chờ, không bịa ra fix giả), chat #9 giải thích đúng chính sách gia hạn/downgrade khớp KB. (#11, #9)
• [P3] Chủ động thêm giá trị ngoài câu hỏi khách — chat #11 chủ động đề xuất sửa luôn welcome message sau khi giải thích nguyên nhân tên ẩn danh; chat #6 chủ động xác nhận thêm support email để AI handover đúng chỗ. (#11, #6)
• [P4] Xác nhận lại vấn đề bằng lời của mình trước khi xử lý, tránh hiểu lệch — chat #12 paraphrase chính xác cả 2 vấn đề khách gặp trước khi bắt tay làm, chat #10 hỏi lại rõ ràng trước khi trả lời. (#12, #10)

🔧 *Cần cải thiện*
• [KN5] Đưa ra số liệu không chính xác về sản phẩm active khi khách đang sốt ruột vì case đã trễ hẹn, khiến khách phải tự chứng minh lại và case kéo dài thêm. (#4)
   → Dẫn chứng: [12:32:42] CS (Linda): "As I just checked, all 506 of your products have been synced to Chatty. However, only 201 products are currently active in your store" — khách phản hồi ngay sau: "our Shopify store currently has 615 active products... Shopify currently shows 615 Active products, while Chatty is only showing 201 products available"
   → Trước khi khẳng định con số cụ thể với khách (nhất là case đã kéo dài, khách đang mất kiên nhẫn), nên xác nhận lại qua TS-inspect/backend hoặc nói "để mình xác nhận chính xác con số" thay vì đưa số chưa chắc chắn.
• [QT-review] Mời khách để lại review Shopify/G2 dù chat đã được đánh dấu "ĐÃ CÓ review" — làm phiền khách không cần thiết vì họ đã review rồi. (#1, #2)
   → Dẫn chứng: Chat #1 header "Review: ĐÃ CÓ review (không cần xin)" nhưng [16:21:20] CS (Linda): "...we're running a special program where merchants who leave a review on G2... Would you mind taking a few minutes..."; tương tự chat #2 [07:59:02] CS (Linda): "啊，你来了。我能请求你帮个小忙吗？😊 ...分享你对我们应用和支持的反馈"
   → Liếc qua header/segment review của chat trước khi mời review — nếu đã có review rồi thì bỏ qua bước này.
• [KN2] Thử đi thử lại nhiều lần một thao tác (bôi đậm text trong welcome message) trước mặt khách thay vì xác nhận sớm với team rằng tính năng không hỗ trợ, kéo dài chat không cần thiết. (#2)
   → Dẫn chứng: [10:35:58] CS (Linda): "我尝试过对文本和链接都使用加粗格式，但是一旦我在设置中保存，加粗格式就会消失" → [10:41:58] "我试过在这里调整它，也在其他几个应用中调整过..." → mãi đến [10:50:21] mới chốt "欢迎消息仅支持纯文本格式"
   → Khi không chắc tính năng có hỗ trợ hay không, kiểm tra với team/tài liệu trước 1 lượt rồi mới báo khách, tránh vừa thử vừa để khách chờ nhiều vòng.

🌟 *Xin review (chỉ ghi nhận, không tính điểm)*
• Đã xin review đúng lúc ở 2/2 chat khách hài lòng phù hợp.
   Xin đúng lúc ở cả 2/2 chat phù hợp (chat #6, #17), ngay sau khi khách cảm ơn/hoàn tất — tốt. Lưu ý riêng: có 2 chat (#1, #2) đã có review từ trước mà vẫn được mời lại (xem mục Cần cải thiện), không tính vào đếm này vì không thuộc diện "nên xin".

📈 *So với tuần trước*
• ▲ +1 so với tuần trước (80→81)

🔗 *Chat đã QA (17):*
<https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_4131d23e-711b-4e61-9755-a251b7e8fe76|#1 DHIntra> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_b7cbab74-f54d-4aa9-aa28-0524769e3f6a|#2 Lumiere Hair> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_767d0e07-b2de-4d6e-81b8-8a2409b9c48b|#3 Lenovra> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_e4015785-6363-4ce1-9a28-7da01c7fb91a|#4 visitor3673470> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_9d1d8db9-6b7d-4be0-aadb-582519fceb34|#5 Beautiful Blooms> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_334f9750-ae80-4171-9ee1-e08b93382b01|#6 TRU SKN> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_b4698881-bcb0-4e6b-8eb8-7e14b607eca9|#7 Multigenus> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_e8af7426-960c-417c-97a6-d57a74cc0530|#8 Piherk> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_c7ed328d-1d65-45a9-8bfd-afccc58aecad|#9 The Bad Peach US Official Store | Shop Adult Sex Toys and Lingerie> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_5b483105-4c3c-4b26-b42b-9b671e64cccc|#10 Fitz Fine Furniture> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_fc5d1e30-224d-4a84-a6fd-342dd1a3e26c|#11 Portia & Alexa Hair Extensions> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_c90638b7-80cb-4e7c-9f62-5f728e247284|#12 Kabelbinders.com> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_74f21536-af22-4c34-8aea-b9af62d3a305|#13 Freyza> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_0f3722b9-1f53-44a6-ab8c-9419d5a1a7d4|#14 MLOONG DIGITAL LIMITED> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_87038f28-0742-4af0-b3cf-e7faf524aa1a|#15 Rheidon Tech> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_73cf58ad-c7b5-47c2-b5ff-44467e83b2f8|#16 Baggbay> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_a1e82fec-93c4-4f16-a4a7-21960e72e608|#17 SOARDISTUSA>

_Tin tự động từ hệ thống QA của team CS 2. Có gì thắc mắc cứ nhắn lại Liz nhé 💬_