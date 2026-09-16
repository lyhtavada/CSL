# QA Weekly — Alyssa — 2026-W37 (09/09 – 15/09/2026)

**Điểm tuần:** 77/100 — Đạt ➖ — ▼ -15 so với tuần trước (92)
**Đã QA:** 24 chat (loại 1 chat không tính)

## Breakdown 3 trục
- 🧠 Mindset: 25.7/34
- 📚 Kiến thức: 26.3/33
- 🛠️ Xử lý: 25.5/33
- Trục yếu nhất: **🧠 Mindset**

## 📝 Nhận xét chung
Tuần này Alyssa xử lý một lượng lớn case kỹ thuật nặng (migration Smile/Magento, billing, VIP tier, Klaviyo, API) và điểm mạnh rõ nhất là ownership — case nào cũng được theo tới cùng, tạo ticket đầy đủ, và bạn không ngại tự sửa khi trả lời sai (case #4). Đây là chất lượng đáng khen ở một CS xử lý case phức tạp thường xuyên. Tuy nhiên điểm cần tập trung ngay là thói quen trả lời trước khi đọc lại đủ ngữ cảnh — case #3 là ví dụ rõ: bạn kết luận sai hướng khiến khách phải tự sửa lại, dễ gây mất thời gian và giảm niềm tin khi lặp lại ở case đông CS xử lý. Ngoài ra, vài "chat vàng" (khách vừa cảm ơn, vấn đề vừa xong) đang bị bỏ lỡ cơ hội xin review — nên tập thói quen chốt review ngay khi khách vừa hài lòng.

## ✅ Điểm tốt
- [P1] Ownership rất tốt trên nhiều case kỹ thuật kéo dài nhiều ngày (chat #1 wishlist/point calculator, #4 enterprise Nhật, #6, #8 onboarding, #18 billing/translation issues, #24) — luôn tạo ticket, tự follow up, không bỏ case giữa đường dù case phức tạp. (#1, #4, #6, #8, #18, #24)
- [P3] Chủ động vì khách: ở chat #16 không escalate mù mà hỏi lại lý do khách muốn tính năng để tìm hướng phù hợp hơn; ở chat #24 tự đề xuất extend trial khi thấy khách lo deadline trước khi khách phải hỏi. (#16, #24)
- [P5] Trung thực, tự nhận sai và sửa nhanh khi trả lời nhầm (chat #4: '啊，抱歉，我的错！我误读了消息'), giữ uy tín thay vì lấp liếm. (#4)
- [P4] Kiến thức kỹ thuật vững ở các case phức tạp (billing breakdown chat #15, VIP Tier Assessment logic chat #13) — giải thích đúng, khách hiểu và không phải hỏi lại. (#13, #15)

## 🔧 Cần cải thiện
- **[KN6] (Moderate)** Trả lời/kết luận trước khi đọc lại đủ lịch sử chat (case đã qua nhiều CS xử lý), khiến khách phải tự sửa lại thông tin. (#3)
  - Evidence: Alyssa: "As I checked, your Place an Order program is still inactive. You will need to turn it on to allow customers to earn." → Customer: "we are usiing shopfy flow not his setting please check history"
  - Action: Trước khi trả lời case dài đã qua tay nhiều CS, lướt lại vài tin gần nhất (nhất là escalation note/ticket cũ) để tránh đưa ra hướng đã bị loại trừ trước đó.

## 🌟 Xin review (observe-only, không tính điểm)
- Đã xin review ở 1/2 chat phù hợp
- Xin đúng lúc ở 1/2 chat phù hợp tìm được (chat #7 — ngay sau khi khách cảm ơn xong việc sửa nút wishlist). Chat #23 (khách cảm ơn sau khi được restore Ultimate plan) là một 'chat vàng' khác nhưng không ai xin review, kể cả Alyssa — hơi tiếc vì đây đúng thời điểm khách hài lòng.

## 📈 So với tuần trước
- Điểm: 92 → 77

## 🔗 Chat đã QA (25)
<https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_ba861373-81a1-4801-9720-c3d14a09f722|#1 caiwu jigao> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_8eb1ca78-d185-4a16-ab93-31e08eeb0677|#2 Oasis HOULTE> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_97cca5c2-72d1-454c-adbb-0aa754118dd4|#3 Travel Likes Me> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_cd81ac62-b4ee-4256-bc43-62aa3059b5e1|#4 Nissoplus> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_cb7f0b84-9274-4d06-8d75-8f539a19c1e8|#5 Jay Man> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_a041e982-0086-446a-b9ad-7b226da8d0bf|#6 Fei f> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_d7a98380-9374-41b3-ba51-f2a6fd8de083|#7 汉桂 张> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_2191463d-57c4-4ba1-a765-ad1c6949b696|#8 Kuo-Hung Liang> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_c42e63bb-6dbc-4f97-8823-5aee76d49ea9|#9 Jonathan Yang> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_e8ae8dea-0614-4c83-9f80-444c3b5c446e|#10 Dominik Schörm> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_fa2f2ea0-5716-4567-b0b0-a56eba27c970|#11 Yiqun Huang> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_d54f5269-992b-4aa1-af9f-6470642dc3b9|#12 pongbot sports> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_e6c2f1a1-bfe8-41a8-aff4-4793ede91990|#13 大介 木口屋> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_631fd237-1c43-456b-960e-db3279b6fdac|#14 Healez Beauty> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_bcf1041c-e7db-432c-8187-7ba476d242a3|#15 Jianmin Yu> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_43a271d1-5872-421d-a1ab-9a1217e99c8b|#16 SUMA Gourmet> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_83d9b993-dc0e-469b-b8b3-f6b80eb9045c|#17 Paula Penna> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_b46cd734-920b-454a-98cb-ddbed261018a|#18 創造 富川> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_c6aad2fe-efa8-480d-877a-ffdb41c800c1|#19 Dylan Ong> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_96e6c671-d4b2-4286-bd27-b39abacebc7f|#20 Nicholas Davies> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_4e9e9af2-89e5-4058-bda0-9629c3ec86f3|#21 Jian He> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_a2107290-f310-4ab9-a6c5-1c5f7884e03e|#22 Ellen Chung> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_6f681598-f9da-4914-871b-c54d9645ae4a|#23 Andrew Tang> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_b0ffd55a-c71a-449b-91a2-d3bd4649bf53|#24 George scinider@gmail.com> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_03f885cc-0a96-4260-aae9-fd44f444dea9|#25 IKJUN JANG>
