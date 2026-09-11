# Trả lời Anthony: kinh nghiệm training KB — áp dụng cho niche domain pack (furniture)

**Câu hỏi gốc của Anthony:** "Phần CS training data cho CS Agent và TS Agent có phải chị training KB không? Em đang làm tương tự cho niche domain pack (furniture) dựa trên FAQ/link/PDF merchant setup + conversation thực tế — chị review/feedback rủi ro hoặc bài học fail giúp em được không?"

---

## 1. Trả lời thẳng: ai train gì

- **CS Agent = Ivy** (bot support **merchant** dùng app Chatty, KB về bản thân app Chatty — feature/plan/FAQ) → **đúng, chị + Betty trực tiếp train** qua quy trình `kb-sync`/`mine-chat-faqs`/`bot-corrections`: mine câu hỏi thật từ chat → diff với KB live → viết patch → chị duyệt → push + reindex → test lại bằng câu hỏi mẫu.

- **TS Agent (TS Elite / TS AI Agent)** → **khác hẳn, không phải "training KB" theo nghĩa FAQ.** Đây là agent nội bộ để CS/CSL **investigate case** (đọc trace/log/settings), kiến trúc mới của nó là **playbook-driven** (dạy quy trình chẩn đoán, không phải dạy kiến thức trả lời khách). Chị không trực tiếp train KB kiểu FAQ cho cái này.

- **Cái em đang làm (niche pack cho furniture)** → thực ra là training cho **Chatty AI Agent** — widget chat nhúng lên storefront merchant, trả lời **buyer** (khách mua hàng thật) về sản phẩm/chính sách của từng store. Đây là **hệ thứ 3**, khác cả Ivy (audience là merchant, không phải buyer) lẫn TS Agent (không phải KB training). Không dùng chung KB/data với 2 cái kia.

→ Vì khác hệ thống, chị không có kinh nghiệm trực tiếp trên đúng data/audience của em, nhưng cùng là **RAG chatbot training** nên nhiều bài học vận hành dùng chéo được — dưới đây là review theo đúng plan em mô tả (FAQ/link/PDF + conversation).

---

## 2. Review theo từng loại nguồn em định dùng

### a) FAQ / link / PDF merchant setup (tài liệu tĩnh)

- **Rủi ro lớn nhất: tài liệu tĩnh viết theo hướng "feature có gì", không theo hướng khách thực sự hỏi gì.** PDF setup thường liệt kê tính năng theo logic sản phẩm, còn buyer hỏi theo tình huống thật (hỏi lệch từ ngữ, hỏi combo nhiều ý 1 lúc, hỏi thứ tài liệu không cover). Nếu train chủ yếu từ tài liệu tĩnh, dễ ra 1 bộ KB "đúng nhưng lệch pha" với câu hỏi thật.
  - **Cách chị làm ngược lại:** luôn mine FAQ từ conversation thật trước, rồi mới đối chiếu với tài liệu tĩnh để tìm GAP — không làm chiều ngược lại (đọc tài liệu rồi tự đoán khách sẽ hỏi gì).
- **Mỗi đoạn/heading trong file phải tự đủ nghĩa.** RAG chỉ kéo ra 1 mảnh nhỏ lúc trả lời, không có ngữ cảnh xung quanh. Nếu PDF gốc viết kiểu "bước 3: làm như bước 2" thì khi convert sang KB entry, bot bốc trúng đoạn đó sẽ trả lời vô nghĩa cho buyer.
- **Ngôn ngữ nhất quán** — nếu PDF/setup doc của các merchant khác ngôn ngữ nhau, cần chuẩn hoá về 1 ngôn ngữ khi đưa vào pack chung, tránh bot trộn ngôn ngữ khi trả lời buyer.

### b) Conversation thực tế (mining từ chat)

- **Đây là nguồn quý nhất — ưu tiên nó hơn tài liệu tĩnh**, vì phản ánh đúng cách buyer hỏi thật, kể cả những câu tài liệu setup không bao giờ nhắc tới.
- **Correction/complaint không đồng nghĩa "KB thiếu".** Nhiều lần chị thấy bot trả sai, sửa KB ngay, nhưng hoá ra do **index bị stale** (patch xong quên reindex, hoặc reindex nhưng cache chưa refresh) chứ nội dung KB không sai. Quy trình chuẩn: patch → reindex → **test lại bằng câu hỏi thật qua đúng pipeline live** trước khi kết luận là thiếu data.
- **Đừng viết "cái sai" vào KB, chỉ viết "cái đúng".** Bài học đau nhất chị từng gặp: sửa KB để chặn bot nói sai bằng cách viết kiểu "đừng recommend hãng X" — bot đọc raw content, thấy tên "X" xuất hiện, rồi bê nguyên ra trả lời khách (hallucinate ngược lại). Fix đúng là bổ sung đủ data ĐÚNG để bot tự nhiên không rơi vào nhánh sai.
- **Test bằng cách đọc từng câu trả lời thật, không tự động hoá bằng keyword-match** — dễ false pass. Chị luôn chạy câu hỏi mẫu qua pipeline thật rồi tự đọc so với KB gốc.

### c) Chung cho cả 2 nguồn

- **Phân biệt "trả lời thông tin" vs "hành động hệ thống".** Nội dung dạng FAQ (trả lời câu hỏi) thì an toàn, nhưng nếu trong pack có phần chỉ đạo hành động (transfer to human, request order ID...) thì rủi ro cao hơn hẳn — bot trigger sai hành động nặng hơn nhiều so với trả lời sai chữ. Cần test riêng cho trường hợp **trigger nhầm** (false positive), không chỉ test trigger đúng lúc.

---

## 3. Review kỹ thêm phần plan chi tiết em gửi (pipeline embedding/clustering/pack generation)

| # | Rủi ro | Gợi ý |
|---|---|---|
| 1 | `merchant_fill` placeholder pass lint không đảm bảo substitute đúng lúc runtime | Test 2 store khác nhau cùng 1 pattern, xem bot có lẫn giá/policy giữa 2 store khi trả lời buyer không |
| 2 | LLM sinh pack cho "pattern lỗi" theo hướng liệt kê điều cấm (negative example) | Luôn generate theo hướng "câu trả lời ĐÚNG", không liệt kê "đừng nói X" |
| 3 | Scenario directive (transfer to human, request order ID) rủi ro cao hơn FAQ text | Vòng test riêng cho false-positive trigger |
| 4 | Entry trong pack không tự đủ nghĩa khi bị RAG kéo ra lẻ | Check mỗi FAQ/directive đứng độc lập, không phụ thuộc context cluster |
| 5 | Offline win-rate cao không đảm bảo production ổn (nhiều lỗi thực ra do stale index) | Sau khi merchant approve pack, cần bước reindex + smoke test bằng câu hỏi thật trước khi tính pilot đã live |
| 6 | Pattern chỉ xuất hiện ở đúng ngưỡng tối thiểu (2 store) dễ generalize nhầm | Với furniture (94 store, mẫu nhỏ), soát tay các pattern biên giới (chỉ 2-3 store) trước khi đưa vào pack chính thức |

---

## 4. Bối cảnh kiến trúc (để hiểu tại sao tầng "shared theo ngành" chưa từng tồn tại)

Chatty AI Agent (buyer-facing) hiện tại chỉ có 2 tầng: **instruction chung** (hành vi, không chứa fact) + **KB per-store** (fact, merchant tự nhập, rất mỏng — trung bình 5 FAQ/store) — **không có tầng ở giữa theo ngành hàng**. Đây chính là khoảng trống niche pack đang lấp vào (mô hình 3 tầng: Instruction chung → Industry pack MỚI → Store-specific KB).

Lý do tầng này chưa từng tồn tại: (a) giả định cũ "fact luôn khác theo store, merchant tự lo" chưa từng bị data thách thức — niche pack lần đầu dùng conversation cross-store để chứng minh vẫn có pattern chung trong cùng ngành; (b) share content rủi ro cao hơn share instruction (leak fact giữa các store), cần cơ chế `merchant_fill` riêng mới làm an toàn; (c) đây là bài toán mới (cold-start theo ngành cho merchant mới) mà trước giờ không ai chủ động sở hữu — khác KPI với Ivy (correctness/safety, đo bằng correction rate).

---

Mai gặp trực tiếp bàn kỹ hơn nhé Anthony, mang theo vài ví dụ pattern biên giới (chỉ 2-3 store) để soi cùng luôn — chị rảnh [khung giờ].
