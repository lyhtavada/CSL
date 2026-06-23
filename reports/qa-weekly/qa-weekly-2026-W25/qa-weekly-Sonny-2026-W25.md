# QA Tuần 2026-W25 — Sonny (Joy)
**Tuần 15/06 – 21/06/2026** · coaching, không phải penalty

## 📊 Điểm tuần: 83/100 — Tốt  (▼ -1 so với W24: 84)
🔍 Đã QA: 29 chat

**Breakdown 3 trục:** 🧠 Mindset 28.5/34 · 📚 Kiến thức 28.0/33 · 🛠️ Xử lý 26.8/33  →  trục yếu nhất: **skill**

## 📝 Nhận xét chung


## ✅ Điểm tốt
- [P] Chat #25 (disc-golf-deals-usa): Phân tích kỹ payload 219.6KB vs 132ms TBT, phân biệt transfer size vs blocking time rõ ràng và chuyên nghiệp khi xử lý technical complaint phức tạp. ()
- [P] Chat #10 (e43nfe-m2): Phân tích discrepancy 893 member qua tag sync, giải thích joy_tag_member vs joy_member chính xác. Chat #22 (kurozu): birthday scan timing correct (1st + last day). Chat #28 (sy0nev-98): 'we can only export the current data instead of the point/tier at the time the activity was recorded' — honest limitation. ()
- [P] Chat #21 (8849tech), #22 (kurozu), #25 (disc-golf-deals-usa), #29 (drdoireann): Nhận ra cơ hội pitch widget V4 / loyalty page DFY sau khi giải quyết issue — natural và well-timed. ()
- [P] Chat #29 (drdoireann): Khi khách hỏi giảm birthday lead time về 0, Sonny giải thích rõ risk gian lận (clone accounts) và suggest 7 ngày thay vì 0 — đây là ownership thực sự. ()
- [P] Chat #26 (hguneh-za): AI đưa sai UI path, Sonny jump in kịp thời và sửa đúng. Chat #29 (drdoireann): AI đưa sai Klaviyo variable, Sonny cung cấp syntax chính xác. ()

## 🔧 Cần cải thiện
- [] (low) Misread customer message / tone-deaf reply ()
   • Dẫn chứng: [04:31:15] Customer: 'I've created the discount and am testing it, but it shows invalid.' → [04:32:06] CS (Sonny): '太好了！你反应真快'
   → Đọc kỹ nội dung message trước khi reply. Khi khách báo lỗi, không reply bằng lời khen không liên quan. Nếu có nhiều tab/conversation đang mở, double-check context trước khi send.
- [] (low) Xin review khi shop đã có review (lặp lại từ W24) ()
   • Dẫn chứng: Header: 'Review: ĐÃ CÓ review (không cần xin)' — Sonny vẫn gửi review ask link.
   → Trước khi xin review, check header chat xem shop có review chưa. Nếu ĐÃ CÓ review → không xin. Chỉ xin G2 review (khác App Store) khi shop chưa có review trên Shopify App Store.
- [] (low) Review ask trước khi issue được giải quyết hoàn toàn ()
   • Dẫn chứng: Chat #13: widget iteration còn đang xử lý, Sonny gửi link review ask.
   → Review ask chỉ gửi sau khi issue đã resolved và khách confirm satisfied — không gửi trong lúc đang xử lý.
- [] (low) Wrong message sent (likely copypaste from another chat) ()
   • Dẫn chứng: [04:32:06] CS (Sonny): '太好了！你反应真快' — không liên quan đến context
   → Khi reply nhiều chat cùng lúc, luôn verify đúng tab trước khi send. Giống lỗi gửi sai URL trong W24.

## 🌟 Xin review (chỉ ghi nhận, KHÔNG tính điểm)
- Đã xin 9/20 chat phù hợp. Chats #7 và #18 là lỗi rõ ràng — shop đã có review. Cần kiểm tra header trước khi xin.

## 📈 So với tuần trước


## 🔗 Chat đã QA
<https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_0fda1baa-f179-411d-b569-b41d00bd3978|#1 Susan Liao> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_4c2eff67-89c8-4646-843f-377fe86fbea1|#2 KUO WEI LAI> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_e0042121-7db0-458c-b272-47cf0b3be435|#3 Hoi Chew> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_381963a7-c79f-4a26-85db-5971626401bc|#4 YUBIN PU> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_d47f3bc9-2655-418d-b808-e6eee8bd0fb8|#5 pierre millet> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_9b629b0d-638b-45d0-942b-f411a7755d01|#6 Pala Petfoods> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_aa44e0fa-55fe-402f-b034-23eb27b2f8cb|#7 Sincerely Valentine> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_aa86bad1-ef87-4422-86da-dfc3ef2e7f91|#8 Mervi Komulainen> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_522b4310-3b91-4a1e-80f6-287a89967d37|#9 TexaKana Organics> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_f55d6b9d-3083-4960-b0a8-d61edc990a9c|#10 ANNARITA GAUDIO> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_903aeeef-ac08-42c3-9e13-a68db16f3d01|#11 Peter Virostko> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_e48402c1-9fc5-40c6-95a2-0bcdc37b7914|#12 梓菡 吴> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_c1c89aef-886b-43bd-a2ac-51994769fcbc|#13 Sparkace LAUNCH> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_d81a0746-5b2e-4071-8d8b-82dd82415f52|#14 David Pavel> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_1844ac3e-e6c1-421c-b65b-b3d797fb19e5|#15 Cristian Luca> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_0f5ed96d-0f5f-440c-8b5c-9699ce16686a|#16 Nella Monaco-Wells> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_56d67564-ce2a-4720-8da9-1966d8d6af1d|#17 1byone Audio> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_f8653b02-df0a-4b4e-a6fd-4e2410d19ee7|#18 Antonio Martin del Nogal> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_14bc8e63-e2d1-4f6b-8b6d-9f3dc823faa1|#19 ZHANHAO MAI> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_c9682e88-4544-478e-8d96-e7130c061d97|#20 US ACEMAGIC> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_ae72b2ca-af12-4451-9239-14d6fcb24254|#21 Ricky Clennar> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_d71360e6-c466-4fb4-9fdd-e46c676baf8a|#22 Su Amelia> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_919419ae-6749-4545-8038-c0da796cd749|#23 Samuel Chan> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_fb9d1ef3-f96b-4827-b964-a513ab70ee31|#24 Alex Paynter> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_f67892bb-e278-4571-a032-364572874593|#25 Doireann O'Leary> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_f481b6c4-77e1-423a-832c-16848e15f22e|#26 Captain Frapp> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_73b1b5e1-3806-4447-a9d6-a6145285b892|#27 Direct Wines ECL> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_58a474d1-7f4c-473f-806c-0a185f17afc7|#28 Aleksandr Krutik> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_eaa6286e-778d-4bd8-8306-095b870b2ea6|#29 Web Pôdevache> · <https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_db37715c-3715-4c5d-a4e7-fadc01f32076|#30 Stefan Josic>
