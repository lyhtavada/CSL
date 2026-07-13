# QA Tuần 2026-W28 — Hana (Joy)
**Tuần 06/07 – 12/07/2026** · coaching, không phải penalty

## 📊 Điểm tuần: 85/100 — Tốt  (▼ -3 so với W27: 88)
🔍 Đã QA: 30 chat

**Breakdown 3 trục:** 🧠 Mindset 27.6/34 · 📚 Kiến thức 29.5/33 · 🛠️ Xử lý 27.7/33  →  trục yếu nhất: **mindset**

## 📝 Nhận xét chung
Bạn duy trì phong độ ổn định ở mức Tốt — DFY ownership rõ ràng, fix nhanh, tone ấm áp nhất quán trên cả các case kỹ thuật phức tạp lẫn case ngắn. Điểm yếu cốt lõi tuần này vẫn là lỗi KT1 tên plan 'PRO plan' tái diễn lần thứ 3 liên tiếp: đây không còn là sơ suất ngẫu nhiên mà là pattern đã định hình, và nó ảnh hưởng trực tiếp đến expectation của khách khi upgrade. Ngoài ra, lỗi báo sai giá Essential ($24.99 thay vì $29) ở chat #28 thêm một KT1 pricing nữa trong tuần — cả hai lỗi này cùng nhóm: thiếu verify thông tin plan/pricing trước khi gửi. Ưu tiên tuần tới: ghi nhớ bảng plan Joy (Starter / Essential $29 / Advanced $129 / Ultimate $499), không dùng 'Pro' hay 'PRO' trong bất kỳ chat nào, và verify giá trước khi mention.

## ✅ Điểm tốt
- [P1] DFY ownership nổi bật — chủ động fix widget, CSS, popup, app embed mà không cần khách nhắc lại; gửi preview/video capture để xác nhận trước khi publish. (#13 #14 #15 #16 #26)
- [P2] Empathy nhất quán — dùng tone ấm áp (':$', '<3'), xin lỗi vì thời gian chờ, cảm ơn khách, không để khách cảm thấy bị bỏ rơi trong các case dài hơi. (#2 #24 #16 #26)
- [P4] Kiến thức kỹ thuật đúng ở nhiều case khó: streak chỉ hỗ trợ 3/5/7 ngày (không phải 30 ngày như khách yêu cầu), usage fee tính trên tổng orders, birthday reward có thể chia per-tier qua 'Member by tier' — sửa đúng điều Joyce trả lời sai. (#16 #20 #28)
- [P3] Proactive upsell và DFY offer đúng thời điểm — sau khi resolve xong issue chính, chào đề nghị Unified Widget tự nhiên, không gượng ép. (#14 #26 #29)

## 🔧 Cần cải thiện
- [KT1] (Critical) Dùng sai tên plan Joy 'PRO plan' — lỗi này tái diễn tuần thứ 3 liên tiếp (W26 → W27 → W28). Joy không có plan nào tên Pro. Đây không còn là lỗi đơn lẻ mà là pattern cố định.  (#5)
   • Dẫn chứng: [11:40:27] CS (Hana): The option is currently not available on PRO plan yet
   → Trước khi mention plan trong bất kỳ chat nào, dừng lại kiểm tra: Joy có 4 plan là Starter / Essential ($29) / Advanced ($129) / Ultimate ($499). Không có 'Pro' hay 'PRO'. Ghi bảng này ra giấy dán cạnh màn hình. Lỗi lặp 3 tuần → coaching 1-1 có chủ đích.
- [KT1] (Moderate) Báo sai giá Essential plan — nói '$24.99/tháng' nhưng giá đúng theo KB là $29/tháng. Khách có thể bị nhầm lẫn khi quyết định upgrade.  (#28)
   • Dẫn chứng: [04:03:15] CS (Hana): Plan Essential bên mình sẽ hỗ trợ với số lượng khoảng 500 order một tháng với giá $24.99 ạ
   → Essential = $29/tháng (500 orders included, +$15 mỗi 100 orders thêm). Mỗi lần đề cập giá, verify lại trong app subscription page trước khi gửi cho khách.
- [KN1] (Low) Gửi tin nhắn trùng lặp — 'Thank you so much, you really made my day' gửi hai lần liên tiếp làm chat trông thiếu chuyên nghiệp.  (#18)
   • Dẫn chứng: [16:42:32] CS (Hana): Thank you so much, you really made my day <3
[16:42:34] CS (Hana): Thank you so much, you really made my day <3
   → Soạn tin nhắn hoàn chỉnh trước khi nhấn gửi. Nếu lỡ gửi trùng thì xin lỗi ngắn gọn, không im lặng để đó. Tuần trước W27 cũng có lỗi duplicate — pattern cần chú ý.
- [KN3] (Low) Chat #27: xin review nhưng yêu cầu khách mention 'Jade' thay vì 'Hana' — sai tên người. Khách có thể nhầm lẫn hoặc mất tin tưởng.  (#27 #29)
   • Dẫn chứng: [01:21:56] CS (Hana): Would you mind spending a few moments sharing your feedback... If possible, please mention "Jade" in the review
   → Khi copy template xin review, kiểm tra lại tên trước khi gửi. Lỗi nhỏ nhưng ảnh hưởng brand perception — khách để ý.

## 🌟 Xin review (chỉ ghi nhận, KHÔNG tính điểm)
- Đã xin 9/10 chat phù hợp (8 well-timed).
  Xin review đều đặn và tích cực — 9/10 chat phù hợp có ask, phần lớn đúng lúc sau khi issue đã resolve. Có 1 lần hơi lệch timing (chat #26 — khách đang trong quá trình chuyển nền tảng khỏi Shopify, xin review lúc này không còn nhiều ý nghĩa). Lưu ý nhỏ ở #27 và #29: copy template quên đổi tên từ 'Jade' sang 'Hana'. 3 chat đã có review sẵn (#16, #19, #30) nên loại khỏi eligible pool.

## 📈 So với tuần trước
W27: 88/100 (Tốt). W28: 85/100 (Tốt) — giảm 3 điểm. Trục Knowledge giảm nhẹ do có thêm KT1 giá ($24.99 vs $29) bên cạnh KT1 plan name 'PRO'. Lỗi KT1 tên plan tái diễn lần thứ 3 — coaching đã flag tuần trước nhưng chưa được khắc phục. Trục Mindset và Skill ổn định.

## 🚨 Severe flags
- KT1 tại #5: 'PRO plan' — Joy không có plan nào tên Pro (Starter/Essential/Advanced/Ultimate). Lỗi lặp lại từ W26→W27→W28, cần coaching có chủ đích.
- KT1 tại #28: báo giá Essential là '$24.99' trong khi KB ghi $29/tháng — cần verify lại.

## 🔗 Chat đã QA
<https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_d2187e2d-b3c4-49cd-adc2-0a96ffd64e5f|#1 SUMIT GUPTA> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_f55d6b9d-3083-4960-b0a8-d61edc990a9c|#2 ANNARITA GAUDIO> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_765b3b3e-93f0-4dc3-b728-96bcdfd14a78|#3 Dominik Zander> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_32bf5eff-2d92-486f-9cca-c0ea85ed8737|#4 Pradeep Gupta> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_aa44e0fa-55fe-402f-b034-23eb27b2f8cb|#5 Sincerely Valentine> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_e2a5cb14-5fc6-4cde-a015-0fc5b100800a|#6 Elena Privalova> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_2bd4af08-014a-4cf9-b592-94bc44c8a623|#7 Andy Liu> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_3ac3f2be-e312-478e-b3a2-4e0e3af540ce|#8 My Store Admin> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_9dfb3393-3b9f-4492-bd06-cf078a2abea9|#9 nicholas fitzwilliams> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_b11c6e02-1617-445b-8301-41de3cf86b54|#10 pankaja kasthuri> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_72f38c9b-18d0-4a4d-8416-85018d2f78fb|#11 Kaitlin Johnstone> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_7a1f0a3e-a5dd-4e91-882c-8ac04c842b14|#12 laurie Stephens> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_ee7e52fe-c915-47ab-bf2b-7f9a9d70ee44|#13 Xianghua Ye> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_a0fe5371-4386-49c9-9754-e6106e3d7e15|#14 Sina Nouravar> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_27dc5a12-3ef5-4596-97a7-aeeaf81207a8|#15 Younes Harichane> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_980074d7-f70d-4ab8-a1b3-db6e970480d7|#16 Cuura Malaysia> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_9ab48ba7-a192-46ea-b93f-0c1452d7d7f3|#17 Jinwei Han> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_23dc5689-84f8-418a-81da-3c1b19257e43|#18 Jamie Canterbury> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_68934b52-d28a-44cd-b9a5-9809f5fe34b7|#19 Emily Wang> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_28edb5fd-1ef7-4f91-aacd-ab1608fce3b8|#20 Official Kootion> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_a6cbc5b8-6e90-4678-8228-db248a5e9e7c|#21 JOCKEY MOHAMMED> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_1083ca8f-ee1c-4341-ad66-d6ceded9f158|#22 Monica Olavarria> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_0da8b77e-cbee-4aeb-9ed7-aaf4926681e0|#23 MOE KIDOGUCHI> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_e334958f-f0b4-42d7-b2e8-3545411123d3|#24 Matthew Youn> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_26a77636-9698-41bd-b55b-084b56c60c72|#25 Paul Wells> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_05535fc2-b967-44b3-a79f-879e1a1617e7|#26 Dub Charge> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_f5c986c2-08bc-49f5-acb8-f6b8824a3bc5|#27 Ann Marie Chua> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_abe75e35-5eae-422c-b772-f8697be3a319|#28 Tuan Anh Doan> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_2ff9a89a-dcb0-4204-9e31-42a4e2b27ec1|#29 Welblandmore> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_0f0fa547-1619-4c8e-b20a-7594b314780d|#30 Official GMKtec>

_Tin tự động từ hệ thống QA của team CS 2. Có gì thắc mắc cứ nhắn lại Liz nhé 💬_
