# Trả lời Anthony: kinh nghiệm training KB — áp dụng cho niche domain pack (furniture)

**Câu hỏi gốc của Anthony:** "Phần CS training data cho CS Agent và TS Agent có phải chị training KB không? Em đang làm tương tự cho niche domain pack (furniture) dựa trên FAQ/link/PDF merchant setup + conversation thực tế — chị review/feedback rủi ro hoặc bài học fail giúp em được không?"

---

## 1. Review kỹ phần plan chi tiết em gửi (pipeline embedding/clustering/pack generation)

| # | Rủi ro | Gợi ý |
|---|---|---|
| 1 | `merchant_fill` placeholder pass lint không đảm bảo substitute đúng lúc runtime | Test 2 store khác nhau cùng 1 pattern, xem bot có lẫn giá/policy giữa 2 store khi trả lời buyer không |
| 2 | LLM sinh pack cho "pattern lỗi" theo hướng liệt kê điều cấm (negative example) | Luôn generate theo hướng "câu trả lời ĐÚNG", không liệt kê "đừng nói X" |
| 3 | Scenario directive (transfer to human, request order ID) rủi ro cao hơn FAQ text | Vòng test riêng cho false-positive trigger |
| 4 | Entry trong pack không tự đủ nghĩa khi bị RAG kéo ra lẻ | Check mỗi FAQ/directive đứng độc lập, không phụ thuộc context cluster |
| 5 | Offline win-rate cao không đảm bảo production ổn (nhiều lỗi thực ra do stale index) | Sau khi merchant approve pack, cần bước reindex + smoke test bằng câu hỏi thật trước khi tính pilot đã live |
| 6 | Pattern chỉ xuất hiện ở đúng ngưỡng tối thiểu (2 store) dễ generalize nhầm | Với furniture (94 store, mẫu nhỏ), soát tay các pattern biên giới (chỉ 2-3 store) trước khi đưa vào pack chính thức |

---

## 2. Bối cảnh kiến trúc (để hiểu tại sao tầng "shared theo ngành" chưa từng tồn tại)

Chatty AI Agent (buyer-facing) hiện tại chỉ có 2 tầng: **instruction chung** (hành vi, không chứa fact) + **KB per-store** (fact, merchant tự nhập, rất mỏng — trung bình 5 FAQ/store) — **không có tầng ở giữa theo ngành hàng**. Đây chính là khoảng trống niche pack đang lấp vào (mô hình 3 tầng: Instruction chung → Industry pack MỚI → Store-specific KB).

Lý do tầng này chưa từng tồn tại: (a) giả định cũ "fact luôn khác theo store, merchant tự lo" chưa từng bị data thách thức — niche pack lần đầu dùng conversation cross-store để chứng minh vẫn có pattern chung trong cùng ngành; (b) share content rủi ro cao hơn share instruction (leak fact giữa các store), cần cơ chế `merchant_fill` riêng mới làm an toàn; (c) đây là bài toán mới (cold-start theo ngành cho merchant mới) mà trước giờ không ai chủ động sở hữu — khác KPI với Ivy (correctness/safety, đo bằng correction rate).

---

Mai gặp trực tiếp bàn kỹ hơn nhé Anthony, mang theo vài ví dụ pattern biên giới (chỉ 2-3 store) để soi cùng luôn — chị rảnh [khung giờ].
