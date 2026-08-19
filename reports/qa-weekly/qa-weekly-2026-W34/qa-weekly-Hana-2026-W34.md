📋 *QA TUẦN — BÁO CÁO CỦA Hana*
🗓️ Tuần W34 · 12/08 – 18/08/2026
━━━━━━━━━━━━━━━━━━━━━━━━━━━

📊 *Điểm tuần:* 74/100 — Đạt  (▼ -1 so với tuần trước (75→74))
🔍 Đã QA: 18 chat
Breakdown: 🧠 Mindset 24.4/34 · 📚 Kiến thức 25/33 · 🛠️ Xử lý 24.3/33

📝 *Nhận xét chung*
Tuần này bạn xử lý khối lượng case khá lớn, nhiều case kỹ thuật phức tạp (migration điểm cho 92k khách ở case #3, setup loyalty program dài hơi nhiều ngày ở case #8/#13) — điểm mạnh rõ nhất là sự kiên trì theo case tới cùng và luôn confirm kỹ từng bước trước khi thực thi thay đổi lớn trên hệ thống khách. Nhưng có 2 vấn đề cần nói thẳng: (1) ở case #6 bạn lỡ tay uninstall app Flits ngay trên store thật của khách vì nhầm với store test — dù xin lỗi rất chân thành, đây là lỗi thao tác trên live store, cần Liz review riêng; (2) ở những chat khách nói rõ họ đang bực (case #13, #16), bạn thường nhảy thẳng vào giải pháp kỹ thuật mà bỏ qua một câu ghi nhận/xin lỗi ngắn trước — khiến khách cảm thấy không được lắng nghe và dễ bực thêm, kéo dài chat không cần thiết. Tuần tới tập trung 2 điểm: chậm lại một nhịp để trấn an khách trước khi đưa giải pháp kỹ thuật, và luôn double-check đang ở store nào trước khi thao tác bất kỳ thay đổi nào trên admin của khách.

✅ *Điểm tốt tuần này*
• Nhận lỗi và xin lỗi chân thành ngay sau sự cố tự gây ra (uninstall nhầm app Flits trên store khách), không né tránh hay đổ lỗi: "I want to sincerely apologize—while reviewing the issue with the Joy app and adjusting settings, I accidentally uninstalled the Flits app... I am so sorry for the mistake." (chat #6)
• Xử lý ca migration điểm phức tạp, rủi ro cao (92,428 khách hàng) rất cẩn trọng — luôn confirm rõ từng bước (công thức tính điểm, ngày bắt đầu, tắt sandbox) trước khi thực thi để tránh sự cố production: "Could you please confirm that you want to proceed with importing points..." (chat #3)
• Hướng dẫn từng bước rõ ràng kèm video/screenshot để khách tự làm theo được ngay, ngay cả với case setup phức tạp nhiều điều kiện (opt-in, tier, redeem). (chat #1, #8, #13)
• Giữ được sự chuyên nghiệp, theo sát case dài hơi hàng chục lượt tin nhắn trải nhiều ngày mà không bỏ dở giữa chừng. (chat #13, #14)

🔧 *Cần cải thiện*
• [LiveStoreError] Thao tác nhầm gây hậu quả trên store thật của khách (uninstall app của bên thứ 3) (chat #6)
   → Dẫn chứng: "I want to sincerely apologize—while reviewing the issue with the Joy app and adjusting settings, I accidentally uninstalled the Flits app. I mistakenly thought I was configuring my test store and didn't notice I was the collaborator store."
   → Luôn kiểm tra kỹ tên/URL store đang thao tác (tab trình duyệt, tên store hiển thị) trước khi bấm bất kỳ nút cài đặt/gỡ app hay thay đổi cấu hình nào trên admin khách, đặc biệt khi đang mở song song nhiều store (test + khách).
• [Mindset-empathy] Bỏ qua câu ghi nhận/xin lỗi khi khách nói rõ họ đang bực, đi thẳng vào giải pháp kỹ thuật (chat #13)
   → Dẫn chứng: Khách: "sorry I am getting a bit frustrated, i feel i am repeating myself" (14:59) → Hana trả lời ngay: "As I have proposed before, for the customer who have signed before the program is configured, we suggest to sync points for these accounts" — không có câu trấn an nào.
   → Khi khách nói rõ họ đang frustrated/lặp lại, mở đầu phản hồi bằng 1 câu ghi nhận/xin lỗi ngắn ("Mình hiểu điều này khá mất thời gian, xin lỗi vì sự bất tiện") trước khi quay lại giải pháp kỹ thuật — tránh khách cảm thấy bị phớt lờ và leo thang thêm.
• [Mindset-empathy] Không trấn an khi khách bức xúc vì mất dữ liệu sau AI onboarding (chat #16)
   → Dẫn chứng: Khách: "no because its all gone? what was the point of the onboarding if i have to do it all manually anyway" → Hana trả lời ngay bằng câu hỏi nghiệp vụ: "Can you share with me the programs setting that you have did via AI onboarding?" thay vì trấn an trước.
   → Thêm 1 câu đồng cảm ngắn ("Mình hiểu sự cố này thật khó chịu, để mình kiểm tra ngay giúp bạn") trước khi hỏi thông tin kỹ thuật.

🌟 *Xin review (chỉ ghi nhận, không tính điểm)*
• Đã xin review đúng lúc ở 2/4 chat khách hài lòng phù hợp.
   Đã xin đúng lúc 2/4 chat khách vừa hài lòng (case #8, #18) — kèm luôn câu "mention Hana in the review" rất khéo. Tuy nhiên bỏ lỡ 2 chat vàng khác (khách vừa nói "perfect thank you"/"thank you so much" ngay sau khi Hana xử lý xong ở case #11, #14) mà không xin review — lần sau nên tranh thủ ngay khoảnh khắc khách vừa cảm ơn. Ở case #5 (đã có review sẵn) vẫn xin lại là hơi thừa, không cần thiết.

📈 *So với tuần trước*
• ▼ -1 so với tuần trước (75→74)
• Đã khắc phục so với tuần trước: QT9 👏

🔗 *Chat đã QA (18):*
<https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_bf06874f-46be-4971-b77b-91187f14fb7d|#1 ANDY MOORE> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_9ac8b97b-0295-47bc-977f-10c85cfe0f08|#2 Noriko Mirza> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_e0452a22-50ef-49de-8af7-1c2dc3d1db4e|#3 David Pavel> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_d4b0159a-f697-4655-98b4-7e3e06411ed7|#4 Çiğdem Karslıoğlu> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_743a0785-d3c6-4e1e-b39c-34a9d0a550be|#5 Karl Johannesson> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_f0773b2c-8957-4ff6-a74a-4b845c0a4c39|#6 Samata Das> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_ead65c47-b7a9-40d6-96a2-271472d9c6cf|#7 Joachim Kaeser> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_c6aad2fe-efa8-480d-877a-ffdb41c800c1|#8 Dylan Ong> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_8fc5b8ab-6737-4998-805a-f7496c7f346a|#9 Jazz> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_919419ae-6749-4545-8038-c0da796cd749|#10 Samuel Chan> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_a094ea56-6ba2-4135-91de-95ce0ffe6ded|#11 Veronica Rodriguez> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_106968d4-f92f-4eaa-9247-27a0474bfca3|#12 Beadedbyamyx> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_4c3a5a1f-6e04-4670-a88d-dd033abc84b3|#13 BLAEK Coffee> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_91eb2723-2206-496e-900b-88167f0a0fc2|#14 Garderobe Pre-Owned Goods> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_cd8c2e28-d944-4994-86a0-91e5d0b75814|#15 Kevin Köpcke> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_3aeb37ab-d092-4278-b0b8-1b359c5b6c0d|#16 Healthylifehappymind6> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_aa31471e-9719-44ba-a70c-0836437fb4c1|#17 Oussama Saoudi Hassani> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_d56a79b1-e680-480f-9b02-bf9a89f07dc0|#18 Andzej Pulkovskij>

_Tin tự động từ hệ thống QA của team CS 2. Có gì thắc mắc cứ nhắn lại Liz nhé 💬_