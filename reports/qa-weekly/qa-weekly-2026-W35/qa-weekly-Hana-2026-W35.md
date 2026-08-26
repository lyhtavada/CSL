📋 *QA TUẦN — BÁO CÁO CỦA Hana*
🗓️ Tuần W35 · 19/08 – 25/08/2026
━━━━━━━━━━━━━━━━━━━━━━━━━━━

📊 *Điểm tuần:* 78/100 — Đạt  (▲ +4 so với tuần trước (74→78))
🔍 Đã QA: 4 chat
Breakdown: 🧠 Mindset 27.5/34 · 📚 Kiến thức 27.5/33 · 🛠️ Xử lý 23.25/33

📝 *Nhận xét chung*
Tuần này bạn xử lý case phức tạp khá chắc tay — điểm mạnh nhất là ownership: case migration kéo dài nhiều ngày (chat #3) bạn vẫn theo tới cùng, giải thích kỹ thuật rõ ràng, không đẩy việc. Nhưng có 2 lỗi cần nói thẳng: để tiếng Việt lọt vào tin nhắn gửi khách quốc tế (chat #4, 'missing email 3 cái') — nhìn cẩu thả và khách có thể không hiểu; và bỏ sót câu hỏi trực tiếp của khách (chat #3, khách hỏi tại sao không tự nhập được số thập phân) chỉ fix mà không trả lời, khách vẫn còn thắc mắc. Tuần tới ưu tiên: đọc lại tin nhắn trước khi gửi và trả lời đủ từng câu khách hỏi, đừng chỉ xử lý phần thao tác rồi bỏ qua câu hỏi kèm theo.

✅ *Điểm tốt tuần này*
• Ownership tốt với case phức tạp kéo dài nhiều ngày — chat #3 (migration Magento→Joy, VIP tier), Hana quay lại nhiều lần, forward đúng chỗ, không bỏ rơi khách dù case vượt phạm vi cá nhân: 'Thanks for sharing your requests. We will forward and consult the requests with our team' rồi sau đó gửi lại bản trả lời kỹ thuật chi tiết về Amount Spent rule. (#3)
• Hướng dẫn từng bước rõ, khách làm theo ngay không hỏi lại — chat #1 (setup earning rate theo tier) và chat #3 (đổi font/màu widget): 'From Joy admin > access to Reward program > select Place an order program' → khách phản hồi 'amazing thank you for your help and clairty on it'. (#1, #3)
• Xin review đúng lúc, tự nhiên ngay khi khách vừa hài lòng — 3/3 chat phù hợp đều xin đúng thời điểm (chat #1, #3, #4). (#1, #3, #4)

🔧 *Cần cải thiện*
• [KN1] Để lọt tiếng Việt vào tin nhắn gửi khách nói tiếng Anh — thiếu chuyên nghiệp, khách có thể không hiểu ý. (#4)
   → Dẫn chứng: [14:46:36] CS (Hana): We have imported the file successfully. There are 44 contacts with 3 contacts missing email 3 cái và 7 duplicated emails :$
   → Đọc lại tin nhắn trước khi gửi, đặc biệt khi vừa nghĩ bằng tiếng Việt vừa gõ tiếng Anh — tránh lẫn từ, nhất là với khách quốc tế.
• [QT22] Bỏ sót câu hỏi trực tiếp của khách — chỉ sửa lỗi kỹ thuật mà không trả lời câu 'tại sao' khách hỏi, khiến khách vẫn còn thắc mắc chưa được giải đáp. (#3)
   → Dẫn chứng: [09:38:52] Customer (Dylan Ong): how come i cannot input decimal places on my own?
[09:40:03] CS (Hana): [hình ảnh/file] I have updated it. Please help me refresh the app page to see if the decimal is working now
   → Khi khách hỏi kèm 'tại sao', trả lời thẳng nguyên nhân (vd giới hạn UI/cần refresh) trước khi chuyển sang bước fix, đừng chỉ đưa kết quả.
• [KN6] Bắt tay vào setup trước khi confirm rõ phạm vi yêu cầu khách muốn (per order hay per product), dẫn tới khách phải hỏi lại để làm rõ. (#2)
   → Dẫn chứng: Customer: 'i want to have $20 credit for each product bought.' → CS (Hana): 'I have setup the requested earning reward program which will reward $20 store credit for customers on each order that they purchase' → Customer sau đó: 'i checked this thing earlier but can we make it specific for products?'
   → Với yêu cầu có thể hiểu 2 cách (per order vs per product), hỏi confirm phạm vi cụ thể trước khi setup, tránh phải sửa lại và kéo dài chat.

🌟 *Xin review (chỉ ghi nhận, không tính điểm)*
• Đã xin review đúng lúc ở 3/3 chat khách hài lòng phù hợp.
   Xin review đủ 3/3 chat phù hợp, đúng lúc khách vừa hài lòng/cảm ơn (chat #1, #3, #4) — không có chat vàng nào bị bỏ lỡ tuần này. Riêng chat #4 xin review giúp đồng nghiệp (Alyssa) thay vì bản thân, vẫn tính là hành vi chủ động tốt.

📈 *So với tuần trước*
• ▲ +4 so với tuần trước (74→78)
• Không có lỗi trùng lặp mã cụ thể so với tuần trước.

🔗 *Chat đã QA (4):*
<https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_4f684a14-68ca-43c0-9673-fb2defcbb64f|#1 Jannes Schuiling> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_16a7a36d-fde9-47ae-bd76-99ca6536398e|#2 Thomas Smith> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_c6aad2fe-efa8-480d-877a-ffdb41c800c1|#3 Dylan Ong> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_3ae6c9c5-1901-44a7-a105-19b912b252b8|#4 Ralph Hwenjere>

_Tin tự động từ hệ thống QA của team CS 2. Có gì thắc mắc cứ nhắn lại Liz nhé 💬_