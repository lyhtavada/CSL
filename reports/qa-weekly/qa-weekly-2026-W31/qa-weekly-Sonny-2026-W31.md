# 📋 QA TUẦN — BÁO CÁO CỦA Sonny
🗓️ Tuần 2026-W31 · 22/07 – 28/07/2026
━━━━━━━━━━━━━━━━━━━━━━━━━━━

📊 **Điểm tuần:** 86/100 — Tốt  (▲ +6 so với tuần trước)
🔍 Đã QA: 30 chat
🧠 Mindset: 28.5/34 · 📚 Kiến thức: 29.7/33 · 🛠️ Xử lý: 27.5/33

📝 **Nhận xét chung**
Tuần này bạn thể hiện rõ nhất ở việc theo đến cùng những case kỹ thuật khó — điển hình là case Marek (VIP tier tính sai do lỗi đổi tiền tệ khi import), bạn kiên trì test, xin bằng chứng cụ thể, không đóng chat hay đổ lỗi cho dev dù bug kéo dài nhiều ngày. Kiến thức sản phẩm và giá cả đều đúng theo KB, không có ca nào tư vấn sai gây hậu quả. Điểm cần sửa ngay: có ít nhất 2 lần trong tuần bạn trả lời nhầm tiếng Trung cho khách đang viết tiếng Anh (case Hans Chan, case Kiran K) — dù tự nhận ra và sửa lại, việc này vẫn buộc khách đọc/dịch nhầm trước khi hiểu đúng, và lặp lại 2 lần nghĩa là chưa phải sự cố ngẫu nhiên mà là thói quen cần chú ý khi dùng công cụ dịch nhanh. Ngoài ra có vài chỗ trả lời hơi vòng, khách phải hỏi lại mới rõ ý (case LINE integration). Tuần tới tập trung: đọc kỹ lại tin trước khi gửi để tránh lệch ngôn ngữ và trả lời đúng trọng tâm câu hỏi ngay lần đầu.

✅ **Điểm tốt tuần này**
- [P1] Ownership rất tốt với bug khó/kéo dài — case Marek (VIP tier tính sai tiền tệ), theo sát nhiều ngày, không đóng sớm dù dev sửa chưa triệt để, luôn thông báo rõ tiến độ và lựa chọn cho KH. (#29)
- [P3] Kiến thức + thái độ cẩn trọng — tự test trên demo store trước khi kết luận thay vì đoán, tránh trả lời sai cho khách. (#22)
- [P1] Minh bạch, xin phép rõ trước khi động vào code/CSS của khách, giải thích rõ tác động trước khi làm. (#10)
- [P2] Trung thực khi sản phẩm không hỗ trợ — đề xuất giải pháp thay thế (app BOGO ngoài) thay vì cố nói có thể làm được. (#9)

🔧 **Cần cải thiện**
- **[KN3] Moderate** — Trả lời lệch ngôn ngữ — khách viết tiếng Anh nhưng Sonny trả lời bằng tiếng Trung, xảy ra lặp lại 2 lần trong tuần (không phải ca lẻ). (#10, #16)
  - Dẫn chứng: [08:34:10] CS (Sonny): "我可以问一下,通常客户怎样输入电话号码呢?因为我在注册页面上看不到输入框" — trong khi khách Hans Chan hỏi bằng tiếng Anh ngay trước đó ở chat #10; lặp lại tương tự ở chat #16 với khách Kiran K ("[07:19:00] CS (Sonny): 哦，目前如果您已经连接到 Klaviyo...").
  - → Đọc lại ngôn ngữ khách vừa gửi trước khi bấm gửi tin, đặc biệt khi dùng tool dịch nhanh — nếu phát hiện gửi nhầm ngôn ngữ, sửa ngay lập tức thay vì để khách phải hỏi lại.
- **[QT9] Low** — Trả lời không thẳng vào câu hỏi khiến khách phải hỏi lại nhiều lần mới rõ ý (LINE console vs Joy). (#7)
  - Dẫn chứng: [06:36:44] Customer: "where is the LINE login tab? LINE consloe or Joy" — khách phải hỏi lại vì câu trả lời trước đó ("Please guide customers to log in on the LINE tab...") chưa trả lời trực tiếp câu hỏi.
  - → Đọc kỹ câu hỏi khách trước khi trả lời, xác nhận đúng trọng tâm (ở đâu — app nào) ngay từ câu đầu tiên.
- **[KN1] Low** — Gửi trùng 1 tin nhắn y hệt liên tiếp, gây rối luồng chat. (#1)
  - Dẫn chứng: [13:42:30] và [13:42:32] CS (Sonny) gửi 2 tin giống hệt nhau: "Understood! Glad I could adjust it for you. And about moving the widget..."
  - → Kiểm tra trạng thái gửi tin trước khi gửi lại, tránh double-send khi mạng chập chờn.

🌟 **Xin review (chỉ ghi nhận, không tính điểm)**
- Đã xin review ở **4/6** chat phù hợp (đúng lúc: 3, sai lúc: 1)
- Đã xin review đúng lúc ở 3/6 chat khách hài lòng (chat #1, #19, #25 — đều xin ngay sau khi khách cảm ơn/khen). 1 lần xin hơi sớm ở chat #2 khi việc setup chưa hoàn tất hẳn. Còn bỏ lỡ vài chat khách vui mà chưa ai xin (vd chat #8) — có thể chủ động hơn.

📈 **So với tuần trước**
- Điểm 80 → 86 (▲ +6)
- Trục: Mindset 26.7→28.5, Kiến thức 26.9→29.7, Kỹ năng 26.4→27.5
- Lỗi lặp lại: KN1 — cần ưu tiên sửa
- Lỗi tuần trước đã hết: KT1, QT18 👏

🔗 **Chat đã QA (30):**
<https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_57f4fe24-9f12-4922-ac02-41c6e3652218|#1 Alberto Nicolo’> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_fad1e3f7-383b-4a9f-bb55-f43938beff61|#2 Beate Dobler-Eberhard> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_e334958f-f0b4-42d7-b2e8-3545411123d3|#3 Matthew Youn> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_8011fa93-70f7-4a00-9c08-73f408662a93|#4 Love Rocks> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_894f5998-cde6-47bf-b4d6-840bc8bd1deb|#5 Orsolya Lele> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_4912a64b-9df1-4360-a54b-144265a6f9a3|#6 Olivier Gaudéchoux> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_193b8bef-9be7-4360-a323-33576213b38a|#7 wilson wu> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_15812650-f6de-4bc5-bd93-4bc8a82429a3|#8 Naak Bar> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_631fd237-1c43-456b-960e-db3279b6fdac|#9 Healez Beauty> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_e5ab723f-ad1c-4f60-b014-72c9c015d556|#10 Hans Chan> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_ee8b949f-11a2-43e7-8a10-46be73d28759|#11 ENHUI LIU> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_f9dd7051-616d-4a3c-a9e3-65cd318ce592|#12 Rooster's Brewing Co.> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_7621edf7-874f-442f-a069-aa0d794c522b|#13 Na balis> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_610d6703-0b1d-4ea0-b399-3397eef6879e|#14 Jacob Nørlem-Masters> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_930b922c-3852-441f-9e89-075db2d6c252|#15 Sam Fry> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_b2fd7d23-bcac-41ca-88ee-792fd2f4f418|#16 Kiran K> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_4e9e9af2-89e5-4058-bda0-9629c3ec86f3|#17 Jian He> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_852e24d1-05c6-4aef-94fb-c4ef4692d4bf|#18 Mark Yaocheng Tan> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_c5568d3d-f825-48ae-9f0e-0f794f3e6a01|#19 Jimin Kim> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_42bf2b93-ae7c-4279-a095-675a0f294b96|#20 Skye Baillie> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_1e684a18-e8f8-409b-b243-dfb8b83914d8|#21 Rafik Ali Ahmad> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_c615c7aa-9217-48db-8a68-a6d8fcd93a95|#22 visitor3640819> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_72915b76-c6f6-490f-a58d-cd8020ca9650|#23 Il mio negozio Admin> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_2e758c4c-f7e3-4be8-9612-d3e32e26a1b8|#24 Tian Zhao> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_3f658bb7-a32e-4d8f-8fc2-6e30124e748a|#25 visitor3621730> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_cd81ac62-b4ee-4256-bc43-62aa3059b5e1|#26 Nissoplus> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_2191463d-57c4-4ba1-a765-ad1c6949b696|#27 Kuo-Hung Liang> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_d4e5a165-acd6-4194-a195-d339a83e46ef|#28 Sean Curtis> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_18f3bbd3-1de6-4484-ab2c-a6d78952aeff|#29 Marek Michałowski> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_81a52e8b-1d7b-4d1a-858f-e4db8b7e226f|#30 Ali Kasi>

_Tin tự động từ hệ thống QA của team CS 2. Có gì thắc mắc cứ nhắn lại Liz nhé 💬_