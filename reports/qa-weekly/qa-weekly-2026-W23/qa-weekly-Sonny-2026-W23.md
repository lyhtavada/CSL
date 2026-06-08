# QA Tuần 2026-W23 — Sonny
**Giai đoạn:** 01/06 – 07/06  
**App:** Joy  
**Điểm:** 91/100 — Xuất sắc (▲ +5 so tuần trước)  
**Đã QA:** 30 chat
**3 trục:** 🧠 Mindset 31.4/34 · 📚 Kiến thức 30.2/33 · 🛠️ Xử lý 29.3/33

## 📝 Nhận xét chung
Tuần này Sonny đạt 91/100 — kết quả tốt và cải thiện so với W22. Điểm mạnh rõ nhất là sở hữu case đến cùng; knowledge Joy chắc. Tuy nhiên, hai lỗi từ W22 vẫn lặp lại: typo 'I am I could clarify' xuất hiện lần hai, và pattern gây tác động lên live store mà không báo trước tiếp tục xảy ra ở chat #6 — đây là loại lỗi ảnh hưởng trực tiếp đến trải nghiệm của merchant. Nếu bạn không sửa được 2 lỗi này sau 2 tuần liên tiếp, cần có cam kết cụ thể và rõ ràng hơn.

## ✅ Điểm tốt
- **[P1]** Ownership đến cùng — không đẩy case đi — Chat #4: Sonny chủ động theo dõi và xử lý POS tile setup cho Teresa đến khi hoàn tất. Chat #16: Nhận danh sách 7 khách bị thiếu điểm, xử lý và xác nhận trong cùng session. Chat #19: Phát hiện tier perks display bug, escalate tech team, theo dõi và gửi follow-up xác nhận fix hoàn tất. (#4 #16 #19)
- **[P3]** Chủ động đề xuất thêm giá trị — DFY widget, loyalty page, upsell chính xác — Chat #11: Đề xuất plan Advanced với giải thích tính năng chính xác khi khách đang dùng plan thấp hơn. Chat #26: Sau khi xử lý xong coupon issue cho Monica, chủ động offer V4 unified widget DFY setup. Chat #30: Escalate lên team Joy để cấp trial Ultimate cho khách khi bản thân không có thẩm quyền — đúng quy trình. (#11 #26 #30)
- **[P4]** Giải thích kỹ thuật Joy chính xác và rõ ràng với nhiều ngôn ngữ — Chat #22: Trả lời bằng tiếng Ý, giải thích đúng Advanced plan hỗ trợ VIP tier với spending-based calculation + tier assessment. Chat #23: Giải thích chính xác rằng direct checkout redemption chỉ có ở Ultimate + Shopify Plus với Checkout Extensibility. Chat #17 (wacoal-sg): Giải thích đúng cơ chế sandbox mode chặn external API point adjustments, chỉ whitelist Joy programs. (#22 #23 #17)

## 🔧 Cần cải thiện
- **[Live-store · Urgent]** Severe — Live-store mistake: thay đổi widget live mà không báo trước
  - *Dẫn chứng:* Chat #6 (ciindia): Sonny thực hiện thay đổi nội dung widget customization khiến text cập nhật lên live widget, không chỉ preview. Khách phàn nàn: 'But you said nothing will be updated in live. Then only I allowed you to make the changes.' Sonny xác nhận: 'Yes my apologies. I wasn't aware that the content is updated as well.' [09:25:42] (#6)
  - → Trước bất kỳ thao tác DFY nào trên widget, cần kiểm tra và xác nhận rõ với khách liệu thay đổi có ảnh hưởng đến live storefront hay không. Nếu có nguy cơ — báo trước, không để khách tự phát hiện. Đây là lỗi tạo ra hậu quả trực tiếp trên store đang hoạt động.
- **[KN3 · Moderate]** Language mismatch — trả lời sai ngôn ngữ khách
  - *Dẫn chứng:* Chat #7 (MUS): Khách giao tiếp hoàn toàn bằng tiếng Tây Ban Nha. Sonny trả lời bằng tiếng Anh: 'Thanks! Allow us some time to check it further' [04:46:37]. Khách lập tức phản hồi: 'podrias comunicarte en espanol siempfre en este chatty?' [04:47:34] Chat #20 (My Store 3 Admin): Giữa cuộc trò chuyện tiếng Tây Ban Nha, Sonny chuyển sang tiếng Anh: 'Thanks! Allow me a minute' / 'Please help me check in this section:' [08:13:00–08:15:25]. Review ask cuối chat cũng gửi bằng tiếng Anh [05:57:52] trong khi toàn bộ chat là tiếng Tây Ban Nha. (#7 #20)
  - → Live-translate không miễn trừ việc chủ động trả lời đúng ngôn ngữ khách. Khi khách bắt đầu bằng tiếng Tây Ban Nha, giữ toàn bộ hội thoại bằng tiếng Tây Ban Nha — kể cả review ask.
- **[KT1 · Low]** Sai thông tin — tự sửa nhanh nhưng vẫn cần ghi nhận
  - *Dẫn chứng:* Chat #12 (cigar-kingdom): Sonny ban đầu trả lời: 'Yes you totally can! Please go to your account page editor and add our loyalty pass block there' [07:13:36] khi khách hỏi về hiển thị Member QR code trong customer account page. Ngay sau đó tự sửa: 'Oh sorry for my misunderstanding. I am afraid that at the moment, only the floating widget can directly show the QR code.' [07:18:20] (#12)
  - → KT1 tự sửa nhanh là tốt và được tính điểm cao hơn không sửa. Tuy nhiên, cần kiểm tra kỹ trước khi xác nhận 'Yes you totally can' với tính năng kỹ thuật cụ thể như QR code display.
- **[KN1 · Moderate]** Typo lặp lại nhiều chat — gây ấn tượng không chuyên nghiệp
  - *Dẫn chứng:* Chat #21: 'Ah glad I am could clarify!' [15:00:14] Chat #25: 'Great! I am I could clarify' [14:11:49] — lặp lại cùng lỗi từ W22 Chat #28: 'if you have any other concerns or would like some advicesm please feel free...' [08:42:34] (#21 #25 #28)
  - → Lỗi 'I am I could clarify' xuất hiện lần thứ hai (đã có trong W22). Cần tập thói quen đọc lại trước khi gửi tin quan trọng, đặc biệt các câu kết thúc chat. Bật spellcheck trên trình duyệt.

## ⚠️ Flag cho Liz (xem kỹ trước khi gửi)
- Chat #6 (live_store_mistake): Thay đổi text/nội dung trên live widget của khách (ciindia) mà không báo trước, sau khi đã hứa 'nothing will be updated in live'. Khách phàn nàn trực tiếp và Sonny thừa nhận không biết content sẽ cập nhật live.

## 🌟 Xin review (chỉ ghi nhận, KHÔNG tính điểm)
- Đã xin review ở **7/18** chat phù hợp (7 đúng lúc, 1 chưa đúng lúc).

## 📈 So tuần trước
Điểm 86 → 91 (+5). Điểm tăng 5 điểm so với W22 — cải thiện rõ ở knowledge và mindset. Tuy nhiên, 2 pattern lỗi từ W22 chưa được fix: KN1 typo (đặc biệt 'I am I could clarify' xuất hiện lần 2) và live-store mistake (W22 là label 'TREATS' thay đổi live, W23 là text widget cập nhật live ở ciindia). Đây là dấu hiệu pattern hành vi chưa được sửa gốc rễ.
