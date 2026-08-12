# 📋 QA TUẦN — BÁO CÁO CỦA Hana
🗓️ Tuần 2026-W33 · 05/08 – 11/08/2026
━━━━━━━━━━━━━━━━━━━━━━━━━━━

📊 **Điểm tuần:** 75/100 — Đạt  (▼ -7 so với tuần trước)
🔍 Đã QA: 19 chat
🧠 Mindset: 25.4/34 · 📚 Kiến thức: 25.2/33 · 🛠️ Xử lý: 24.8/33

📝 **Nhận xét chung**
Tuần này bạn xử lý được khối lượng case lớn và đa dạng (Joy + Chatty), kiến thức sản phẩm nhìn chung đúng — không có ca nào chấm KT1 (sai giá/tính năng). Điểm mạnh rõ nhất là khi có thời gian tổng hợp cẩn thận (ví dụ email tổng kết trạng thái từng issue cho case migration ở chat #18) và biết chủ động đề xuất thêm giải pháp thay vì chỉ trả lời đúng câu hỏi (chat #5). Nhưng điểm cần tập trung ngay là xử lý lúc khách đang căng thẳng/gấp: ở chat #17 bạn để khách làm lại một thao tác đã báo lỗi 6-7 lần thay vì chuyển thẳng qua specialist, khiến khách bực thêm ("you told me that yesterday...", "i feel like i am begging for basic service"); ở chat #18 (migration 100k khách, store down 10 tiếng) bạn vẫn lặp "let me check with our team" nhiều lần trước khi nối máy chuyên gia dù khách đã chủ động xin gọi. Ở chat #2 cũng có xu hướng hỏi xác nhận lặp lại một yêu cầu quá nhiều lần khiến khách nói thẳng "i feel i am repeating myself" — cần quyết đoán hành động hơn là hỏi lại nhiều vòng, đặc biệt khi khách đã báo hiệu mệt mỏi.

✅ **Điểm tốt tuần này**
- [P1] Tổng hợp & báo cáo tiến độ rất có tổ chức cho case phức tạp nhiều issue song song — email liệt kê Resolved / In Progress / Feature request rõ ràng giúp khách theo dõi dễ, giảm khách phải hỏi lại nhiều lần. (#18)
- [P2] Chủ động đề xuất thêm giải pháp ngoài câu hỏi gốc: khi thấy redemption rate thấp (0.52%), tự đề xuất bật tính năng Reward reminder và dịch luôn sang tiếng Hà Lan cho khách, không đợi khách yêu cầu. (#5)
- [P3] Giữ được thái độ thấu cảm đúng lúc dù khách rất bực ("I understand how frustrating this must be, and I'm truly sorry for the way it's made you feel") thay vì phòng thủ hay lờ đi cảm xúc khách. (#17)
- [P4] Trước khi escalate luôn có bước xác nhận lại yêu cầu ("May I confirm that...") giúp tránh tạo nhầm ticket, đặc biệt hữu ích với case nhiều yêu cầu dồn dập. (#2, #7)

🔧 **Cần cải thiện**
- **[KN6/QT9] High** — Xử lý khách rất gấp/bực bằng cách yêu cầu khách lặp lại đúng thao tác đã thất bại nhiều lần thay vì chuyển thẳng lên specialist (#17)
  - Dẫn chứng: Khách: "I have done this 7 times now..." / "you told me that yesterday check the screenshot and didnt get back to me... I am not using your product without a demo call" — trong khi Hana vẫn nói "Would you mind helping me schedule just one more time?"
  - → Khi khách báo đã thử cùng 1 cách >2 lần mà vẫn lỗi, đừng yêu cầu thử lại lần nữa — chuyển ngay lên specialist/manager kèm bằng chứng lỗi, tránh làm khách cảm thấy phải "năn nỉ".
- **[QT9/Mindset-ownership] High** — Trong ca khủng hoảng migration (100k khách, store down 10 tiếng), phản hồi chủ yếu là "let me check with our team" lặp lại nhiều lần thay vì chủ động đẩy nhanh escalate khi khách đã chủ động xin gọi điện (#18)
  - Dẫn chứng: Khách hỏi lúc 09:04: "Is there a possibility of getting into a call with someone?" — Hana trả lời "Let me check with our team on it" và mãi tới 09:27 mới forward yêu cầu qua Specialist, trong khi store vẫn đang down.
  - → Với case có mức độ nghiêm trọng cao (outage, downtime kinh doanh), ưu tiên escalate/gọi specialist ngay lập tức thay vì tiếp tục tự xử lý từng câu hỏi kỹ thuật nhỏ — tốc độ phản hồi lúc này quan trọng hơn sự đầy đủ.
- **[KN5/QT22] Moderate** — Bỏ sót một mối lo quan trọng của khách (hệ thống vô tình cộng điểm cho >1000 thành viên khi launch) mà không xác nhận/giải quyết, chuyển ngay sang câu hỏi khác (#6)
  - Dẫn chứng: Khách: "when i launched the system, it gave everyone bonus points that i did not want to happen" — Hana không quay lại xử lý/trấn an vấn đề này, tiếp tục hướng dẫn cách gán tier thủ công.
  - → Khi khách nêu một sự cố ngoài ý muốn trên live store (VD: cộng nhầm điểm hàng loạt), xác nhận rõ mức độ ảnh hưởng và đề xuất hướng khắc phục/rollback trước khi chuyển sang câu hỏi tiếp theo.
- **[QT9] Moderate** — Hỏi xác nhận lặp đi lặp lại cùng một yêu cầu (đồng bộ điểm sign-up cho khách cũ) khiến khách phải nhắc lại nhiều lần và bực bội (#2)
  - Dẫn chứng: Khách: "this has been the same request since yesterday!" và "sorry I am getting a bit frustrated, i feel i am repeating myself" sau nhiều vòng "May I confirm..." của Hana về cùng 1 yêu cầu.
  - → Sau 1-2 lần xác nhận không rõ, hãy tóm tắt lại hiểu biết của mình và hành động luôn thay vì hỏi lại thêm — nếu vẫn chưa chắc, nói rõ sẽ hành động theo hiểu biết hiện tại và điều chỉnh sau nếu sai.
- **[QT-process] Low** — Tạo trùng 2 ticket cho cùng một yêu cầu dịch thuật trong vòng vài phút (#2)
  - Dẫn chứng: "Đã tạo ticket: Nút 'Join program' trên Loyalty page chưa có trường dịch..." xuất hiện 2 lần liên tiếp lúc 13:42:24 và 13:46:51 với cùng nội dung.
  - → Kiểm tra nhanh danh sách ticket đang mở trước khi tạo mới để tránh trùng lặp, gây nhiễu cho team kỹ thuật.

🌟 **Xin review (chỉ ghi nhận, không tính điểm)**
- Đã xin review ở **2/4** chat phù hợp (đúng lúc: 1, sai lúc: 1)
- Xin review 2/4 chat phù hợp. Chat #5 xin đúng lúc (ngay sau khi khách nói "no thats all thanks"). Chat #3 xin hơi sớm khi khách mới cài app 1 tiếng và tự nói "too early to review" — nên đợi khách trải nghiệm thêm. Bỏ lỡ 2 chat vàng (#4, #8) khi khách vừa cảm ơn/xác nhận vấn đề đã fix xong mà không chủ động xin review (để bot làm sau).

📈 **So với tuần trước**
- Điểm 82 → 75 (▼ -7)
- Trục: Mindset 28→25.4, Kiến thức 27.5→25.2, Kỹ năng 26.8→24.8
- Lỗi lặp lại từ tuần trước: QT9
- Lỗi tuần trước đã hết: KN1, KN2 👏
- Lỗi mới tuần này: KN5/QT22, KN6/QT9, QT-process, QT9/Mindset-ownership

🔗 **Chat đã QA (19):**
<https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_894f5998-cde6-47bf-b4d6-840bc8bd1deb|#1 Orsolya Lele> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_4c3a5a1f-6e04-4670-a88d-dd033abc84b3|#2 BLAEK Coffee> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_cb8a5872-4675-4ffd-850d-82a15f3213dc|#3 Michele Varrasso> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_f0e69780-372b-4a19-bb3b-f0d0972869a8|#4 Selsdirect > · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_75c38a8a-c354-477b-94b7-15b83eaf81af|#5 Max Clasener> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_6c47015f-9d81-469f-92bd-6d9b080352e5|#6 John Henry's> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_de3b6181-e80c-42e8-bae2-38b58634c08b|#7 Hsiao Fan Chang> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_57c5cf46-2840-4c31-9dac-4fd1974b287d|#8 Stacks Warehouse> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_bb800977-b23b-4d88-bcc5-237994bff390|#9 David Kmecik> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_c403a918-d180-4472-9fcf-294aeafbfd8a|#10 thomas agarate> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_8c5dcd86-fb07-4b3d-9411-9fe718dd09a8|#11 Orbeluis Guasch> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_96e6c671-d4b2-4286-bd27-b39abacebc7f|#12 Nicholas Davies> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_0fb307bc-18e9-475c-a104-ffb60a4048a1|#13 visitor3656722> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_7e4e0022-4882-46b9-9976-23ace9f6433c|#14 Maria Josefa Gonzalez Garzon> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_46674ce7-189a-4ab2-b600-ddb5fd903b95|#15 Marco Belotti> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_1cdd9b10-6c72-4ddb-9a0f-af58520161ee|#16 Brice Lythgoe> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_12d0459c-b42f-4bda-a106-c4de61b0c112|#17 Shisha Distribution> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_4e9e9af2-89e5-4058-bda0-9629c3ec86f3|#18 Jian He> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_d5271998-6794-4417-9ace-6b11b9fe07b1|#19 Armada Shopify>

_Tin tự động từ hệ thống QA của team CS 2. Có gì thắc mắc cứ nhắn lại Liz nhé 💬_