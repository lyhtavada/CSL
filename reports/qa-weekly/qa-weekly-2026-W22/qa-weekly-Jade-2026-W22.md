# QA Tuần 2026-W22 — Jade
**Giai đoạn:** 26/05 – 01/06  
**Điểm:** 87/100 — Tốt  
**Đã QA:** 30 chat  
**3 trục:** 🧠 Mindset 30.1/34 · 📚 Kiến thức 29/33 · 🛠️ Xử lý 28.2/33

## 📝 Nhận xét chung
Tuần này Jade thể hiện phong cách làm việc có trách nhiệm và nhất quán: chủ động follow-up qua email sau khi chat kết thúc, xử lý nhiều ngôn ngữ (EN/FR/ES/ZH) không bị áp lực, và đặc biệt xuất sắc ở các case kỹ thuật phức tạp như POS permissions, AI training, DNS/domain setup. Điểm mạnh nổi bật nhất là ownership — Jade ít khi đóng chat lửng, thường chủ động hỏi tiếp và gửi email follow-up khi ca kết thúc. Cần tập trung cải thiện ở hai điểm: (1) câu văn đôi khi viết sai ngữ pháp hoặc bị lỗi rõ ("our all does not have", "Thank you very much for your helo") làm giảm tính chuyên nghiệp và có thể khiến khách không hiểu đúng; (2) một số thông tin về Joy Loyalty cần kiểm tra lại trước khi nói — ví dụ trong chat #4 Jade nói "250 commandes gratuites" nhưng theo KB đây là giới hạn transaction chứ không phải orders, dễ gây hiểu sai về cách tính phí.

## ⚠️ Cần Liz xem trước
- KT2 (borderline): Chat #4 — Jade nói '250 commandes gratuites' thay vì '250 transactions'. Hệ quả: khách có thể hiểu Starter cho 250 đơn hàng miễn phí, trong khi thực tế là 250 loyalty transactions. Liz review trước khi DM.

## ✅ Điểm tốt
- **[P1]** Ownership rõ ràng: Jade thường xuyên gửi email follow-up sau khi ca kết thúc để chốt kết quả, ví dụ chat #7 (FAQ page fix), #12 (proactive chat + AI return flow), #22 (widget CSS position). Khách không cần phải hỏi lại. (#7, #12, #22, #17)
- **[P2]** Xử lý kỹ thuật phức tạp tốt: POS permissions (chat #19 với hướng dẫn 2 tùy chọn rõ ràng theo từng loại account), cashback tiered program (chat #18 với Phase 1/Phase 2 logic mạch lạc), Joy DNS domain setup (chat #10). (#19, #18, #10, #13)
- **[P3]** Hỗ trợ đa ngôn ngữ (EN/FR/ES/ZH) ổn định — không từ chối, không bị phân tâm, duy trì chất lượng ngang nhau qua các ngôn ngữ. (#2, #4, #9, #15)
- **[P4]** Proactive upsell/DFY đúng lúc và tự nhiên: ở chat #8, #10, #16, Jade giới thiệu widget mới (DFY) sau khi đã giải quyết xong vấn đề chính — không gây cảm giác ép khách. (#8, #10, #16)

## 🔧 Cần cải thiện
- **[KN1 · Moderate]** Lỗi ngữ pháp và typo lặp lại trong chat làm giảm tính chuyên nghiệp.
  - *Dẫn chứng:* Chat #1: 'Thank you very much for your helo' — 'helo' thay vì 'help'. Chat #5: 'If it does it work, feel free to let me know' — sai cú pháp. Chat #11: 'Currently, our all does not have a separate sign up flow' — câu bị l
  - → Trước khi gửi tin, đọc lại câu một lần. Với các câu dài hoặc kỹ thuật, viết nháp rồi check lại. Đặc biệt chú ý khi copy-paste template có thể chứa lỗi.
- **[KT2 · Moderate]** Diễn đạt thiếu chính xác về Joy Starter plan limit — nói 'orders' thay vì 'transactions', có thể khiến khách hiểu sai về cách tính phí.
  - *Dẫn chứng:* Chat #4: [16:47:15] 'chaque mois vous aurez 250 commandes gratuites' — KB xác nhận giới hạn Starter là 250 transactions, không phải orders. 1 đơn hàng có thể tạo nhiều transactions.
  - → Khi tư vấn về plan limit của Joy, dùng chính xác từ 'transactions' và giải thích ngắn: '1 order có thể tạo nhiều transactions (earn + redeem)'. Kiểm tra lại KB kb_pricing.md trước khi giải thích billing.
- **[KN3 · Low]** Một số câu trả lời kỹ thuật hơi mơ hồ hoặc không trả lời thẳng câu hỏi của khách, khiến khách phải hỏi thêm.
  - *Dẫn chứng:* Chat #9 [11:46:16]: Khách hỏi cụ thể về migration từ Smile.io và cần chuyển đổi điểm không. Jade trả lời chung chung 'Vous pouvez accéder à la section Clients > Importer' mà không confirm rõ có cần chuyển đổi hay không —
  - → Khi khách hỏi yes/no (ví dụ 'có cần chuyển đổi không?'), trả lời thẳng yes/no trước, sau đó mới giải thích. Tránh chỉ nêu path mà bỏ qua câu hỏi gốc.
- **[QT18 · Low]** Ở một số chat ngắn, Jade kết thúc mà không chốt bước tiếp theo rõ ràng cho khách.
  - *Dẫn chứng:* Chat #28: Jade hỏi code collaborator, khách paste '[PYN6DK-KE1LK]' rồi Jade không phản hồi và ca kết thúc. Phoebe tiếp ca sau 45 phút mới pick up. Khách đã ra đi không rõ issue được giải quyết chưa.
  - → Cuối ca, nếu đang đợi thông tin từ khách, gửi thêm 1 tin chốt: 'Tôi sẽ bàn giao cho bạn đồng nghiệp tiếp tục theo dõi, họ sẽ liên hệ bạn ngay khi nhận được code.' Tránh để chat trống không.

## 📈 So tuần trước
Tuần đầu, chưa có dữ liệu so sánh.