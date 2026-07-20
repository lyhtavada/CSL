# QA Weekly — Alyssa — 2026-W29 (13/07 – 19/07/2026)

**Điểm tuần:** 84/100 — Tốt  (▼ -6)  
**Đã QA:** 30 chat

| Trục | Điểm TB |
|---|---|
| 🧠 Mindset | 28.2/34 |
| 📚 Kiến thức | 28.2/33 |
| 🛠️ Xử lý | 27.7/33 |

## 📝 Nhận xét chung

Tuần này bạn xử lý một khối lượng chat rất nặng — nhiều case bị escalate từ AI, nhiều case shift-handoff phức tạp (migration Smile→Joy, khách VIP dài hơi như Hegen, Tokyolife, Maison Koko) — và giữ được chất lượng ổn định, không có ca nào xử lý hỏng. Điểm mạnh rõ nhất là ownership: bạn theo case tới cùng, tự phát hiện và sửa lỗi của chính mình (chat #3 vụ gift card, chat #26 tìm ra nguyên nhân gốc mà cả team bỏ sót cả tháng). Điểm cần đẩy lên: một số case bạn đưa ra hướng dẫn/cam kết trước khi verify kỹ 100%, dẫn tới phải đính chính lại và khách mất công làm lại (chat #3). Ngoài ra một vài chat khách đã hài lòng rõ ràng nhưng bạn bỏ lỡ thời điểm vàng để xin review — không tính điểm nhưng là cơ hội bị bỏ qua nhiều lần trong tuần, nên chủ động luyện thành phản xạ.

## ✅ Điểm tốt tuần này

- Ownership cao — tự nhận và sửa lỗi của chính mình ngay khi phát hiện thay vì im lặng, ví dụ tự phát hiện nhầm hướng dẫn về gift card và báo lại khách chủ động (chat #3), giữ uy tín với khách dù phải nhận sai. (#3)
- Đào sâu tìm root cause thay vì chấp nhận câu trả lời bề mặt — chat #26, sau cả tháng team chưa giải quyết được vụ khách bị tính điểm review sai, Alyssa tìm ra chính xác do 1 checkbox 'verified purchase' chưa bật trong Judge.me integration. (#26)
- Chủ động vì lợi ích khách — khi khách e ngại chia sẻ quyền truy cập theme, Alyssa không ép mà đề xuất quay video hướng dẫn thay thế để khách tự làm (chat #11). (#11)
- Kiên nhẫn xử lý case kỹ thuật khó, khách khó tính (AYAL Beauty - vấn đề CORS/domain migration, Hegen - nhiều lỗi liên tiếp) với giải thích rõ ràng, có bước, không né tránh dù không thể fix 100% từ phía Joy. (#16, #27)

## 🔧 Cần cải thiện

- **[KN5] Moderate** — Đưa hướng dẫn cho khách trước khi verify kỹ tính năng, khiến khách làm thừa việc (#3)
  - Dẫn chứng: [14:01:59] CS (Alyssa): Ah so you may need to create them first so we can select them when set up the free gift ... [14:32:40] CS (Alyssa): Ah I'm sorry. I've double-checked the logic and confirmed that the gift cards cannot be selected as a free gift reward.
  - → Với các câu hỏi về khả năng cấu hình tính năng (feature feasibility), nên test/verify trên hệ thống thật trước khi hướng dẫn khách thao tác, tránh để khách làm xong rồi mới biết không dùng được.
- **[QT18] Low** — Một vài case bàn giao ca khi vấn đề khách vẫn đang chờ xử lý mà chưa chốt rõ mốc thời gian tiếp theo cho khách nắm (#18)
  - Dẫn chứng: [09:04:59] CS (Alyssa): By the way, my shift has ended, so I'll be signing off now. I'll forward your question and issue to one of my teammates so they can continue to support you.
  - → Khi bàn giao ca giữa lúc case chưa xong, nên chốt thêm 1 câu về thời điểm khách có thể mong đợi cập nhật tiếp theo, để khách chủ động hơn thay vì chỉ biết 'sẽ có người khác tiếp'.

## 🌟 Xin review (chỉ ghi nhận, KHÔNG tính điểm)

- Đã xin review ở **3/6** chat phù hợp (đúng lúc: 3, sai lúc: 0)
- Đã xin đúng lúc 3/6 chat khách hài lòng (chat #2, #25, #29) — thời điểm xin đều tự nhiên, ngay sau khi khách cảm ơn. Tuy nhiên bỏ lỡ 3 chat vàng khác (#10, #11, #20) khi khách vừa hài lòng xong mà không mời xin review — nên tập luyện phản xạ này ở cuối mỗi case đã xong việc.
- Chat KH đã có review thì không cần xin lại — đã loại khỏi đếm.

## 📈 So với tuần trước

- Điểm 90 → 84 (▼ -6)
- Lỗi tuần trước đã hết: KN1, KN3, QT22 👏
