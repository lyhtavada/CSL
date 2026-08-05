# 📋 QA TUẦN — BÁO CÁO CỦA Alyssa
🗓️ Tuần 2026-W32 · 29/07 – 04/08/2026
━━━━━━━━━━━━━━━━━━━━━━━━━━━

📊 **Điểm tuần:** 80/100 — Tốt  (▼ -5 so với tuần trước)
🔍 Đã QA: 30 chat
🧠 Mindset: 28/34 · 📚 Kiến thức: 26/33 · 🛠️ Xử lý: 26/33

📝 **Nhận xét chung**
Tuần này bạn xử lý ổn định trên khối lượng case lớn (nhiều case DFY/onboarding phức tạp kéo dài nhiều ngày), tinh thần chủ động theo tới cùng khá rõ — case nổi bật nhất là chat #29 (Harris Tihak): khách giận dữ vì bug lặp lại nhiều lần ("I'm losing money... WTF"), bạn vẫn giữ được sự bình tĩnh, điều tra kỹ và giải thích root-cause minh bạch thay vì né tránh. Điểm cần thẳng thắn nhìn nhận: có lúc bạn báo tin chưa chắc chắn cho khách rồi phải đính chính lại (chat #4: báo fix đã live rồi phải xin lỗi "tôi đọc nhầm tin nhắn"; chat #5: báo mã giảm giá 20% rồi sửa lại thành 35% ngay sau đó) — việc này làm khách phải đọc lại/hiểu nhầm dù chỉ là lỗi nhỏ, cần chốt thông tin chắc trước khi gửi khách thay vì gửi rồi sửa. Ở case khẩn cấp có ảnh hưởng tài chính trực tiếp (chat #11, khách đang mất tiền vì lỗi store credit), phản hồi của bạn hơi chung chung ("đang tìm giải pháp phù hợp") mà chưa đưa ra hướng xử lý tạm thời ngay lúc khách đang rất gấp — đây là điểm cần ưu tiên cải thiện: với case có tác động tiền bạc/khẩn cấp, cần hành động và cập nhật timeline cụ thể hơn thay vì trấn an chung chung.

✅ **Điểm tốt tuần này**
- [P1] Ownership tốt, theo tới cùng case phức tạp kể cả khi khách giận dữ — chat #29: điều tra kỹ nguyên nhân gốc (Joy discount bị deactivate từ 26/6), giải thích minh bạch từng phần, escalate đúng chỗ khi khách yêu cầu compensation thay vì tự hứa suông. (#29)
- [P3] Giải thích kỹ thuật rõ ràng, có bước cụ thể — ví dụ giải thích logic birthday reward 30-day rule, cơ chế discount combination của Shopify (chat #4, #29), khách hiểu ngay không phải hỏi lại nhiều. (#4, #29)
- [P4] Chủ động nhớ ngữ cảnh/preference của khách qua nhiều ngày làm việc (nhớ khách không thích widget nổi khắp trang, đề xuất lại đúng giải pháp cũ) — tạo cảm giác được quan tâm thực sự trong case DFY dài. (#1)
- [P1] Bám sát, không bỏ case dù phải chờ dev nhiều vòng — chat #3 (export lỗi cuối tuần) vẫn gửi email cập nhật kèm file đính kèm ngay khi có kết quả. (#3)

🔧 **Cần cải thiện**
- **[KN6] Moderate** — Kết luận sớm khi chưa chắc thông tin rồi phải đính chính lại với khách, gây rối và giảm độ tin cậy. (#4)
  - Dẫn chứng: "啊，抱歉，我的错！修复已经准备好了，但我们的团队正在测试环境中审查结果，所以正式发布还需要一些时间。我误读了消息，为此我为确认感到抱歉！" (chat #4)
  - → Trước khi báo 'đã fix xong/đã live', double-check trạng thái thật (đã deploy production hay còn ở test env) rồi mới thông báo, tránh phải rút lại.
- **[KT2] Moderate** — Báo con số chưa chốt (giá trị discount) cho khách rồi phải sửa lại ngay sau đó, dễ gây hiểu nhầm về ưu đãi thực tế. (#5)
  - Dẫn chứng: "Based on our discussion, the code should be 20% off for 3 first months. I'm checking again with our manager..." sau đó vài chục phút: "I would like to confirm that the code offers 35% off for the first 3 months." (chat #5)
  - → Chờ manager confirm số liệu chính xác trước khi gửi cho khách, tránh gửi số 'nháp' rồi phải sửa — nếu cần trấn an khách đang chờ, chỉ nên nói đang xác nhận, không đưa số cụ thể chưa chắc.
- **[QT25] Moderate** — Ở case khẩn cấp có ảnh hưởng tài chính trực tiếp cho khách, phản hồi chỉ trấn an chung chung mà không có hành động/mốc thời gian cụ thể, khiến khách phải tiếp tục gõ nhiều tin nhắn giục. (#11)
  - Dẫn chứng: Khách: "please! customers are using credit store / we are losing money / how to clear the credit store / !!!" — Alyssa: "As per your request, our team is still looking for a suitable solution. I'll push our developers to resolve it as soon as we can." (chat #11)
  - → Với case có tác động tiền bạc đang diễn ra, cần đưa giải pháp tạm thời ngay (vd tắt tính năng đang gây lỗi) + cam kết mốc thời gian cụ thể, không chỉ trấn an suông.
- **[KN1] Low** — Lỗi chính tả nhỏ trong câu trả lời khách. (#21)
  - Dẫn chứng: "Ah it's just the name of the progran" (chat #21)
  - → Đọc lại tin trước khi gửi để tránh lỗi chính tả, dù nhỏ vẫn ảnh hưởng tính chuyên nghiệp.

🌟 **Xin review (chỉ ghi nhận, không tính điểm)**
- Đã xin review ở **3/4** chat phù hợp (đúng lúc: 3, sai lúc: 0)
- Đã xin review đúng lúc ở 3/4 chat khách hài lòng phù hợp (chat #1, #15, #30) — thời điểm mời đều ngay sau khi khách vừa cảm ơn/hài lòng, tự nhiên. Bỏ lỡ 1 chat vàng ở #2 (khách vừa khen 'youve been a great help' nhưng không mời review).

📈 **So với tuần trước**
- Điểm 85 → 80 (▼ -5)
- Trục: Mindset 28.0→28, Kiến thức 28.5→26, Kỹ năng 27.5→26
- Lỗi lặp lại từ tuần trước: KN1
- Lỗi tuần trước đã hết: KN3 👏
- Lỗi mới tuần này: KN6, KT2, QT25

🔗 **Chat đã QA (30):**
<https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_894f5998-cde6-47bf-b4d6-840bc8bd1deb|#1 Orsolya Lele> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_1b03233c-28c5-4dab-bc50-119767bab305|#2 Leon Becker> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_9eaa3777-784a-40a6-bc40-a00027c8c1a5|#3 Derrick Trumbly> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_cd81ac62-b4ee-4256-bc43-62aa3059b5e1|#4 Nissoplus> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_03ac002a-cd59-4c72-9259-de2d7c2fed50|#5 奕群 黄> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_e5ab723f-ad1c-4f60-b014-72c9c015d556|#6 Hans Chan> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_abafd80a-c5be-497a-8347-bea67facd4ae|#7 Ahmed AlMahmoud> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_f238fb92-08ba-4fb7-8c61-24abae5f38ff|#8 Anua Team> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_c3167910-59ed-41c6-9c44-8b51f52502f9|#9 Jovilyn Arciaga> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_19b26ede-030e-4278-b8a1-f49d78465712|#10 My Store Admin> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_6107200a-a576-4447-bf02-96646b1023a1|#11 M B> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_14bc8e63-e2d1-4f6b-8b6d-9f3dc823faa1|#12 ZHANHAO MAI> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_bb140945-7f94-4132-9698-1de2c37b7edd|#13 My Store Admin> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_6ce63ae0-63c6-41f5-9570-9b316d2992a2|#14 yu chieh yang> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_536fae42-95f7-4f8a-89a4-f69062cea5c9|#15 Margarita Rankin> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_2d46036f-2b5e-416c-9364-1794428e714d|#16 Breanna Walter> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_2191463d-57c4-4ba1-a765-ad1c6949b696|#17 Kuo-Hung Liang> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_e3bb84e3-5044-448b-9146-832a565dff80|#18 TBOF middle east food trading llc Tapia> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_3802b634-e373-4c41-afc2-d4c6385f4270|#19 Motunrayo Adebo> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_b401eaec-0e89-4606-aa12-e7c14c155201|#20 shi tao wang> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_bf2f933e-147f-4943-9d5b-6ed900f20a91|#21 Gagandeep Singh Suri> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_53fb9763-581d-4d77-a8e2-d5e9bf51c8a8|#22 Pigeon Singapore> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_193b8bef-9be7-4360-a323-33576213b38a|#23 wilson wu> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_20a04803-a3d5-4a59-9308-0f57668271a5|#24 Damián López> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_67706346-c712-4655-9117-738429a672d9|#25 ZU SHAN> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_1b69c3c0-4a56-4098-9884-bcb2b4fcb3f2|#26 Ali Haider> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_c0f5f7ff-4699-4b8d-88a5-454fc25eea1f|#27 Saját üzletem Admin> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_bdd3b8c5-1006-4009-b5c3-91705df2da61|#28 BRAD PYATT> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_17990533-9de8-4fe9-81f7-92fea524870d|#29 Harris Tihak> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_b7817625-8001-408c-8501-3c7af481141d|#30 Shu Min Lee>

_Tin tự động từ hệ thống QA của team CS 2. Có gì thắc mắc cứ nhắn lại Liz nhé 💬_