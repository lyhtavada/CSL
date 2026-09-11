# So sánh: Ivy (CS support cho merchant) vs Chatty AI Agent (bot trả lời buyer) + Niche Knowledge Pack

**Mục đích:** giúp Anthony (BA) phân biệt rõ 2 hệ thống dễ bị nhầm vì cùng tên "Chatty AI agent", và định vị đúng chỗ niche knowledge pack pipeline (train KB theo ngành hàng, pilot furniture) cắm vào hệ thống nào.

**Nguồn:** kinh nghiệm vận hành Ivy thực tế của CS team (kb-sync, mine-chat-faqs, bot-corrections) + plan niche knowledge pack (furniture pilot) do team BA/data gửi review 2026-09-11.

---

## 0. Phân biệt 2 hệ thống — điểm quan trọng nhất

| | **Ivy** | **Chatty AI Agent** (đối tượng của Anthony) |
|---|---|---|
| **Trả lời ai** | **Merchant (MC)** — người đang dùng app Chatty, hỏi về cách setup/dùng tính năng, plan, billing | **Buyer** — khách mua hàng thật trên storefront của merchant, hỏi về sản phẩm/chính sách/đơn hàng của **store đó** |
| **Nội dung KB** | Kiến thức về **bản thân app Chatty** (feature, plan, ICP, FAQ về app) | Kiến thức về **sản phẩm/policy của từng merchant** (giá, ship, đổi trả, đặc điểm sản phẩm theo ngành hàng họ bán) |
| **Ai sở hữu/train** | CS team (Liz + Betty) — qua `kb-sync`, `mine-chat-faqs`, `bot-corrections` | Team BA/data (Anthony) — qua niche knowledge pack pipeline |
| **Đây là widget hay công cụ nội bộ** | Bot support nội bộ, sống trên `cs2.avada.net` | Sản phẩm cốt lõi của Chatty — widget chat/FAQ nhúng trực tiếp lên storefront merchant |

**Đây là 2 hệ thống khác nhau, khác audience, khác domain kiến thức, khác owner.** Bài phân tích trước bị gộp nhầm — bản này sửa lại: **Chatty AI Agent (buyer-facing)**, không phải Ivy, mới là hệ thống niche pack đang tác động vào. Phần dưới so sánh **kiến trúc hiện tại của Chatty AI Agent** với **niche knowledge pack**, và dùng kinh nghiệm vận hành Ivy chỉ như bài học tham khảo (vì cùng là RAG chatbot, một số rủi ro vận hành giống nhau dù khác audience).

---

## 1. Kiến trúc Chatty AI Agent (buyer-facing) hiện tại — TRƯỚC khi có niche pack

| Layer | Mô tả |
|---|---|
| **Instruction chung** | Behavior/tone chung cho mọi store — cách trả lời lịch sự, cách xử lý khi thiếu thông tin, khi nào chuyển cho merchant xử lý tay. Áp dụng như nhau cho mọi ngành hàng. |
| **KB (Knowledge Base)** | Hoàn toàn **per-store** — mỗi merchant tự nhập FAQ/URL/file riêng của store mình qua Agent API. Baseline hiện tại: **trung bình 5 FAQ/store** — rất mỏng. Không có kiến thức nền theo ngành hàng nào cả. |
| **Vấn đề đang tồn tại** | Vì mỗi store bắt đầu gần như từ số 0, bot dễ "không có data" khi buyer hỏi theo đặc thù ngành mà merchant chưa kịp tự dạy (VD: "sofa da này bảo quản sao", "giường gỗ này chịu tải bao nhiêu kg") — dẫn tới 45% hội thoại kết thúc sau 1 lượt, 34% câu trả lời thiếu thông tin. |

**Điểm mấu chốt:** hiện tại chỉ có 2 tầng — **instruction chung** (hành vi, không chứa fact) và **KB per-store** (fact, do từng merchant tự nhập) — **không có tầng ở giữa theo ngành hàng**. Đây chính là khoảng trống niche pack đang lấp vào.

---

## 2. Niche Knowledge Pack pipeline (đề xuất, pilot furniture)

| Layer | Mô tả |
|---|---|
| **Mục tiêu** | Thêm 1 tầng KB **mới** vào Chatty AI Agent: shared knowledge theo **ngành hàng** (furniture, apparel...), nằm giữa instruction chung và KB riêng từng store. |
| **Nguồn** | Baseline Agent API hiện tại (2,435 entries/94 store) + conversation buyer↔bot thật 180 ngày (furniture: 49,405 conv/94 store; apparel: 492,487 conv/2,393 store). |
| **Xử lý** | Pipeline ML 6 bước: clean (PII removal, dedupe) → mine pattern bằng embedding + clustering (bge-small + HDBSCAN, 198 pattern cho furniture) → LLM (GPT-5.5) đặt tên pattern + tính failure rate → generate pack (LLM) → test bằng LLM judge (Claude Opus) trên câu hỏi thật, có held-out set → deploy vào merchant review queue. |
| **Cách đảm bảo an toàn** | Field giá/policy đánh dấu `merchant_fill` (không hard-code fact riêng của store nào vào pack dùng chung nhiều store) + lint tự động (8 pack rules + 5 scenario rules). |
| **Review** | Cluster-level (~100 item/ngành) — không review từng dòng. |
| **Deploy** | Đẩy pack vào **merchant review queue** qua Agent API mutation — merchant tự approve, pack trở thành tầng kiến thức nền cho bot của store đó. |

---

## 3. Bảng so sánh trực tiếp — Chatty AI Agent trước và sau niche pack

| Tiêu chí | Chatty AI Agent hiện tại (chỉ per-store) | + Niche Knowledge Pack |
|---|---|---|
| Phạm vi knowledge | Chỉ KB riêng từng store (rất mỏng, ~5 FAQ) | Thêm 1 tầng KB chung **theo ngành hàng**, áp cho nhiều store cùng ngành |
| Nguồn dữ liệu | Merchant tự nhập tay | Conversation buyer↔bot thật quy mô lớn (BigQuery) + baseline Agent API |
| Kiểu vấn đề giải quyết | Merchant phải tự dạy hết, cold-start chậm | **Proactive** — lấp khoảng trống ngay từ đầu, trước khi buyer kịp hỏi và gặp bot trống |
| Công cụ xử lý | Không có xử lý tự động, merchant tự viết | Embedding + clustering (HDBSCAN) + LLM judge, pipeline ML đầy đủ |
| Review trước deploy | Không có review tập trung (merchant tự chịu trách nhiệm nội dung mình nhập) | Review theo cluster (~100 item/ngành) + held-out test + win-rate threshold (≥60% vs baseline) |
| Ai duyệt trước khi live | — (merchant tự nhập là live luôn) | Merchant tự approve trong review queue trước khi pack áp dụng cho store đó |
| Bảo vệ khỏi leak data riêng store | Không cần — mỗi store tự quản data của mình | Cần cơ chế riêng (`merchant_fill` placeholder + lint) vì pack dùng chung nhiều store |
| KPI đo | — | Giảm "bot lacks data" response, giảm thumbs-down, giảm escalation |

---

## 4. Vì sao Chatty AI Agent chưa từng có tầng "shared theo ngành", dù đã có instruction chung?

Đây là câu hỏi cốt lõi Anthony cần hiểu — thực ra là 2 bài toán khác nhau về bản chất, không phải team bỏ sót:

1. **Instruction chung (đã có) ≠ Content-knowledge chung (chưa có).**
   Instruction trả lời "bot nên cư xử thế nào với buyer" — không chứa fact, đúng cho mọi store dù bán ngành gì, nên share tự nhiên, rủi ro gần bằng 0.
   Content-knowledge (giá, policy, đặc điểm sản phẩm) là **fact cụ thể của từng store**, nên mặc định trước giờ luôn giả định "phải khác nhau theo store, không share được". Niche pack pipeline lần đầu dùng **data thật** (conversation cross-store) để chứng minh: dưới lớp fact khác nhau, có 1 lớp **pattern-câu-hỏi + cấu-trúc-câu-trả-lời** giống nhau trong cùng ngành (VD: cách buyer hỏi "vệ sinh sofa da vs sofa vải" giống nhau dù mỗi store giá khác nhau). Đây là insight mới phát hiện được nhờ có đủ data cross-store, không phải thứ bị bỏ qua từ trước.

2. **Rủi ro kỹ thuật khi share content cao hơn hẳn share instruction.**
   Share instruction sai nhiều lắm bot hơi lệch tone. Share content sai (leak giá/policy store A sang trả lời cho buyer của store B) là sai fact trực tiếp với khách hàng thật — nặng hơn nhiều, có thể gây tranh chấp thương mại thật. Vì vậy pipeline mới phải xây thêm cơ chế `merchant_fill` + lint riêng — hạ tầng này không cần thiết ở tầng instruction, nên tầng content-shared ra đời muộn hơn, phức tạp hơn để làm đúng.

3. **Trước giờ chưa ai đứng ra sở hữu bài toán "cold-start theo ngành".**
   KB per-store hiện tại để merchant tự quản — không ai trong Avada chủ động tối ưu tốc độ cold-start theo ngành hàng, vì đây vốn được coi là trách nhiệm của merchant (họ tự dạy bot của họ). Niche pack là lần đầu Avada chủ động nhận trách nhiệm này thay merchant, dựa trên insight rằng cùng ngành thì cùng pattern câu hỏi — đây là bài toán/KPI mới (coverage cho merchant mới), khác hẳn KPI vận hành Ivy (correctness/safety, đo bằng correction rate).

**Tóm lại:** không phải thiếu sót kiến trúc, mà là (a) giả định cũ "fact luôn khác theo store, merchant tự lo" chưa từng bị data thách thức, (b) làm an toàn tầng content khó hơn hẳn tầng instruction, và (c) đây là bài toán mới (cold-start theo ngành) chưa ai từng chủ động sở hữu.

---

## 5. Rủi ro cần lưu ý khi build pipeline mới (từ kinh nghiệm vận hành Ivy — cùng là RAG chatbot nên nhiều bài học áp dụng được dù khác audience)

| # | Rủi ro | Vì sao biết (kinh nghiệm CS team với Ivy) | Áp dụng vào niche pack (Chatty AI Agent) |
|---|---|---|---|
| 1 | `merchant_fill` pass lint không đảm bảo substitute đúng lúc runtime | — | Test 2 store khác nhau cùng 1 pattern, xem bot có lẫn giá/policy giữa 2 store khi trả lời buyer không |
| 2 | Viết fix cho "pattern lỗi" theo hướng liệt kê cái sai (negative example) | Ivy từng bị bot copy nguyên câu "đừng nói X" ra trả lời khách (hallucinate ngược) | Prompt cho LLM sinh pack phải luôn generate theo hướng "câu trả lời ĐÚNG", không liệt kê điều cấm |
| 3 | Scenario directive (transfer to human, request order ID) rủi ro cao hơn FAQ text | Hành động sai (trigger nhầm) nặng hơn nhiều so với trả lời sai chữ, đặc biệt khi đối tượng là buyer thật đang muốn mua hàng | Cần vòng test riêng cho false-positive trigger, không chỉ test true-positive |
| 4 | Entry trong pack phải tự đủ nghĩa khi bị RAG kéo ra lẻ, không phụ thuộc context cluster | Bot bốc nhầm đoạn thiếu ngữ cảnh → trả lời vô nghĩa với buyer | Check mỗi FAQ/directive đứng độc lập được, không tham chiếu "như trên" |
| 5 | Offline win-rate cao không đảm bảo production ổn — nhiều lỗi thực ra do stale index, không phải content sai | Nhiều correction ở Ivy từng bị quy nhầm là "KB thiếu" trong khi là quên reindex | Sau khi merchant approve pack, cần bước reindex + smoke test bằng câu hỏi buyer thật trước khi tính pilot đã live |
| 6 | Pattern chỉ xuất hiện ở đúng ngưỡng tối thiểu (2 store) dễ bị generalize nhầm | — | Với furniture (94 store, mẫu nhỏ), soát tay các pattern biên giới (chỉ 2-3 store) trước khi đưa vào pack chính thức |

---

## 6. Mô hình 3 tầng cho Chatty AI Agent (để niche pack không xung đột với KB per-store hiện tại)

```
Layer 1: Instruction chung (đã có — behavior/tone cho mọi store)
         ↓
Layer 2: Industry knowledge pack (MỚI — niche pack pipeline, theo ngành hàng)
         ↓
Layer 3: Store-specific KB (đã có — merchant tự nhập FAQ/URL/file riêng)
```

Layer 2 không thay thế Layer 1 hay 3 — nó lấp khoảng trống ở giữa: khi merchant mới chưa kịp tự dạy bot (Layer 3 mỏng), bot vẫn có kiến thức nền theo ngành để trả lời buyer thay vì hoàn toàn trống. Khi merchant tự nhập fact riêng (giá, policy cụ thể của store họ), Layer 3 vẫn override Layer 2 nhờ cơ chế `merchant_fill` đã thiết kế.

**Lưu ý cho Anthony:** hệ thống này (Layer 1-3 của Chatty AI Agent, buyer-facing) hoàn toàn tách biệt với KB của Ivy (`cs2.avada.net`, support merchant dùng app Chatty). Hai hệ thống không dùng chung KB, không dùng chung dữ liệu — chỉ giống nhau về loại kiến trúc (RAG chatbot) nên một số bài học vận hành (mục 5) dùng chéo được.
