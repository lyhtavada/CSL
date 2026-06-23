# QA Tuần 2026-W25 — Phoebe (Chatty)
**Tuần 15/06 – 21/06/2026** · coaching, không phải penalty

## 📊 Điểm tuần: 81/100 — Tốt  (▲ +2 so với W24: 79)
🔍 Đã QA: 19 chat

**Breakdown 3 trục:** 🧠 Mindset 26.6/34 · 📚 Kiến thức 27.8/33 · 🛠️ Xử lý 26.4/33  →  trục yếu nhất: **skill**

## 📝 Nhận xét chung
Phoebe duy trì phong độ ổn trong tuần này với điểm 81 — tăng nhẹ 2 điểm so với tuần trước. Bạn thể hiện rõ điểm mạnh là xử lý nhiều vấn đề song song, proactive check setup (App Embed, notifications, FAQ chưa enable), và deliver update sau khi TS xong — tất cả đều được làm đúng. Điểm cần tiếp tục cải thiện: khi tiếp nhận chat từ CS khác, xác nhận lại ngôn ngữ khách đang dùng trước khi reply, tránh lặp lại lỗi KN3 lần thứ hai.

## ✅ Điểm tốt
- [P1] Chủ động check toàn bộ setup khi tiếp nhận merchant mới, không chỉ trả lời câu hỏi được hỏi — phát hiện thêm những thứ merchant chưa nhận ra (App Embed chưa bật, notification chưa bật, FAQ chưa enable cho AI). (#11 #16 #1)
- [P2] Xử lý case kỹ thuật phức tạp (market pricing bug, behavior instruction bug) với cấu trúc rõ ràng: nêu root cause, nêu action đã làm, link screenshot. Merchant hiểu ngay mà không cần hỏi lại. (#17 #12)
- [P3] Không còn lặp tin nhắn (duplicate send) như W24 — cải thiện rõ rệt. (#1 #3 #8)

## 🔧 Cần cải thiện
- [KN3] (Moderate) Chuyển sang tiếng Anh và tiếng Tây Ban Nha trong khi khách đang viết tiếng Bồ Đào Nha — khách phải tự xử lý ngôn ngữ, ảnh hưởng trải nghiệm. (#2)
   • Dẫn chứng: [15:34:13] CS (Phoebe): 'Is the wishlist from MINIMOG currently working with this application?' — và [15:35:46] CS (Phoebe): '¿La lista de deseos de MINIMOG funciona actualmente con esta aplicación?' — trong khi khách (Dental Access) liên tục viết tiếng Bồ Đào Nha suốt chat #2.
   → Trước khi gửi tin, kiểm tra ngôn ngữ khách đang dùng. Nếu cần hỏi nhanh bằng tiếng Anh để clarify, hãy dịch luôn câu đó sang ngôn ngữ của khách (Crisp có live translate hỗ trợ). Lỗi này đã xảy ra ở W24 (chat tiếng Pháp) — đây là lần thứ hai, cần ưu tiên sửa.
- [KN5] (Low) Hỏi 'Could you please let me know what's wrong with this answer?' sau khi khách đã giải thích rõ vấn đề (AI vẫn nhắc stock dù đã disable) — thể hiện chưa đọc kỹ context trước khi phản hồi. (#4)
   • Dẫn chứng: [13:32:32] CS (Phoebe): 'Could you please let me know what's wrong with this answer?' — trong khi [13:33:43] Customer (Dodom) đã giải thích trước đó: '4) Stock is secondary: Do NOT include stock status in normal answers...' và share screenshot rõ ràng.
   → Khi tiếp nhận một chat đang diễn ra, đọc hết context ít nhất 5-10 tin nhắn gần nhất trước khi gửi câu hỏi. Tránh hỏi lại điều khách đã giải thích.

## 🌟 Xin review (chỉ ghi nhận, KHÔNG tính điểm)
- Đã xin 1/2 chat phù hợp. Đã xin review 1/2 chat phù hợp. Chat #14 (Orycea) xin đúng lúc — ngay sau khi khách nói 'It turned out perfect and exactly as I wanted', tự nhiên và hiệu quả. Bỏ lỡ chat #3 (ADHDblox): khách nói 'ok perfect' và 'tysm have a nice day' — đây là thời điểm vàng nhưng không xin. Lưu ý: chat #7 (ĐÃ CÓ review) đã được loại khỏi đếm đúng quy định; Phoebe có xin Trustpilot trong chat này — không phải lỗi vì là platform khác, nhưng không cần thiết vì đã có review Shopify rồi.

## 📈 So với tuần trước
Điểm tăng từ 79 (W24) lên 81 (W25) — tiến bộ nhẹ nhưng ổn định. Tích cực: KN1 (duplicate message) đã hết hoàn toàn — cải thiện rõ. KN3 (lệch ngôn ngữ) vẫn lặp lại lần thứ hai (W24: tiếng Pháp, W25: tiếng Bồ Đào Nha → Anh/Tây Ban Nha) — đây là điểm cần focus tuần tới. QT22 (không escalate rõ ràng) không còn lặp lại — tốt.

## 🔗 Chat đã QA
<https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_7e837253-25a1-44e7-97ff-c51443b2f00c|#1 AutoLux Pro> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_fa5af7b5-d884-4745-ab93-eaa2a07452e5|#2 Dental Access> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_04112ece-931e-4124-a2f5-516a1c46daec|#3 ADHDblox> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_49460c2d-d44f-4471-be0d-29eb19843779|#4 Dodom> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_53807806-75a5-4506-bc81-9e60571e7088|#5 Lege Capsules> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_a45e1cdf-e24d-457d-b0ce-450a67e5d733|#6 Dessclusive> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_af158d95-e4a2-4538-b04b-7c70d50af7ba|#7 The Pack Stock EU> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_4a7964ad-eb92-467e-a9dc-05fbb7dbeeaf|#8 AEMYR> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_0cac466b-17c3-47f7-a613-627ee7fde12a|#9 PrettyBirds> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_1cccb5a9-07fc-4bda-8714-233b687422f3|#10 A|LOUD> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_dd0d8a1b-dfb1-469d-b0c0-a7644e07adbb|#11 Sarabdd78> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_ee53c126-ff9c-486e-9f25-c40d3f446cff|#12 Vincent Daimon> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_ca22955f-5be8-4118-a617-cdaea078565e|#13 Peter's abiti da lavoro S.R.L.S> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_ec7b7215-4a2b-46e4-a858-a663b64bff07|#14 Orycea> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_149d1999-4c6a-4ad8-a546-db703cf18b2b|#15 Madoise> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_ec856b0b-7af1-423a-b5ff-214945c4e373|#16 Loja Vidac> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_92b73127-8b90-4f05-8dc0-4ed83261452d|#17 Novapanel> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_022a32fc-4f0d-4a5f-857c-c54e2e86fd50|#18 Ecuagenera Orquídeas del Ecuador > · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_1e19f8a2-5df2-42de-bb33-4747b0f04d64|#19 laptopokolcson.hu>
