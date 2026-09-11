# So sánh: Chatty CS AI Agent (Ivy) hiện tại vs Niche Knowledge Pack pipeline

**Mục đích:** giúp Anthony (BA) hiểu rõ kiến trúc bot Chatty (Ivy) đang chạy khác gì với pipeline "niche knowledge pack" (train KB theo ngành hàng, pilot furniture) đang đề xuất, để định vị đúng chỗ pipeline mới sẽ cắm vào và tránh làm trùng/xung đột với hạ tầng hiện có.

**Nguồn:** kinh nghiệm vận hành KB thực tế của CS team (kb-sync, mine-chat-faqs, bot-corrections) + plan niche knowledge pack (furniture pilot) do team BA/data gửi review 2026-09-11.

---

## 1. Kiến trúc Ivy (Chatty CS AI Agent) hiện tại

| Layer | Mô tả |
|---|---|
| **Instruction chung** | Behavior/tone/escalation rule — áp dụng cho **mọi merchant** dùng Chatty, không đổi theo ngành hàng. Ví dụ: luôn lịch sự, luôn hỏi order ID trước khi xử lý refund, escalate khi nào. |
| **KB (Knowledge Base)** | 1 bộ KB **per-app** (`chatty-agent`), sống trên `cs2.avada.net`, cùng 1 nguồn cho tất cả merchant Chatty. Merchant tự nhập thêm FAQ/URL/file riêng qua Agent API (baseline hiện tại: trung bình **5 FAQ/store** — rất mỏng). |
| **Cách sửa KB** | Reactive: CS phát hiện bot trả sai/thiếu (qua correction, complaint) → Betty mine từ Crisp chat thật → diff với KB live → viết patch → **Liz duyệt từng patch** → push (`POST /api/kb/file`) + reindex → test lại bằng câu hỏi mẫu qua pipeline thật. |
| **Quy mô xử lý** | Thủ công/bán tự động, review **từng dòng**, vài entry mỗi lần chạy (daily/weekly). |
| **Vấn đề đang tồn tại** | Vì KB chỉ có baseline chung + vài FAQ mỏng manh của từng merchant, bot dễ rơi vào tình trạng "thiếu data" khi merchant hỏi sâu theo đặc thù ngành (furniture, apparel...) mà merchant chưa kịp tự dạy — dẫn tới 45% hội thoại kết thúc sau 1 lượt, 34% câu trả lời thiếu thông tin. |

**Điểm mấu chốt:** Ivy hiện tại có 2 tầng — **instruction chung** (hành vi, không chứa fact) và **KB per-store** (fact, do merchant tự nhập + baseline app-wide) — nhưng **không có tầng ở giữa** theo ngành hàng.

---

## 2. Niche Knowledge Pack pipeline (đề xuất, pilot furniture)

| Layer | Mô tả |
|---|---|
| **Mục tiêu** | Thêm 1 tầng KB **mới**: shared knowledge theo **ngành hàng** (furniture, apparel...), nằm giữa instruction chung và KB riêng từng store. |
| **Nguồn** | Baseline Agent API (2,435 entries/94 store) + conversation thật 180 ngày (furniture: 49,405 conv/94 store; apparel: 492,487 conv/2,393 store). |
| **Xử lý** | Pipeline ML 6 bước: clean (PII removal, dedupe) → mine pattern bằng embedding + clustering (bge-small + HDBSCAN, 198 pattern cho furniture) → LLM (GPT-5.5) đặt tên pattern + tính failure rate → generate pack (LLM) → test bằng LLM judge (Claude Opus) trên câu hỏi thật, có held-out set → deploy vào merchant review queue. |
| **Cách đảm bảo an toàn** | Field giá/policy đánh dấu `merchant_fill` (không hard-code fact riêng của store nào vào pack dùng chung) + lint tự động (8 pack rules + 5 scenario rules). |
| **Review** | Cluster-level (~100 item/ngành), không review từng dòng như Ivy hiện tại. |
| **Quy mô xử lý** | Tự động hoá cao, xử lý hàng chục nghìn đến gần nửa triệu conversation cùng lúc. |
| **Deploy** | Đẩy pack vào **merchant review queue** qua Agent API mutation — merchant tự approve, không qua Liz/CS duyệt nội dung trực tiếp. |

---

## 3. Bảng so sánh trực tiếp

| Tiêu chí | Ivy hiện tại (KB per-app) | Niche Knowledge Pack |
|---|---|---|
| Phạm vi knowledge | 1 KB chung cho toàn app + merchant tự thêm riêng | 1 pack chung cho **từng ngành hàng**, áp cho nhiều store cùng ngành |
| Nguồn dữ liệu | Chat thật (mine từ Crisp) + correction CS | Chat thật (BigQuery, quy mô lớn hơn nhiều) + baseline Agent API |
| Kiểu vấn đề giải quyết | **Reactive** — vá sau khi bot đã trả sai với merchant thật | **Proactive** — lấp khoảng trống TRƯỚC khi merchant kịp hỏi và gặp bot trống |
| Công cụ xử lý | Betty đọc/cluster bằng tay, LLM hỗ trợ đơn giản | Embedding + clustering (HDBSCAN) + LLM judge, pipeline ML đầy đủ |
| Review | Liz duyệt **từng patch** | Review theo **cluster** (~100 item), không soi từng dòng |
| Test trước deploy | `/kb-test` — chạy câu hỏi mẫu qua pipeline thật, Betty đọc từng câu | Held-out test set + win-rate threshold (≥60% vs baseline), tự động chấm |
| Ai duyệt trước khi live | Liz (CSL) | Merchant tự approve trong review queue |
| Bảo vệ khỏi leak data riêng store | Không cần — mỗi merchant có KB entry riêng của mình | Cần cơ chế riêng (`merchant_fill` placeholder + lint) vì pack dùng chung nhiều store |
| KPI đo | Correction rate, coverage/correction verify | Giảm "bot lacks data" response, giảm thumbs-down, giảm escalation |

---

## 4. Tại sao có tầng "shared theo ngành" ở pipeline mới mà Ivy hiện tại không có?

Đây là câu hỏi cốt lõi Anthony cần hiểu để không nghĩ nhầm là "team cũ bỏ sót" — thực ra là 2 bài toán khác nhau về bản chất:

1. **Instruction chung (đã có) ≠ Content-knowledge chung (chưa có).**
   Instruction trả lời "bot nên cư xử thế nào" — không chứa fact, nên đúng cho mọi merchant, share tự nhiên, rủi ro gần bằng 0.
   Content-knowledge (giá, policy, đặc điểm sản phẩm) là **fact cụ thể của từng store**, nên mặc định trước giờ luôn giả định "phải khác nhau theo store, không share được". Niche pack pipeline lần đầu dùng **data thật** (conversation cross-store) để chứng minh: dưới lớp fact khác nhau, có 1 lớp **pattern-câu-hỏi + cấu-trúc-câu-trả-lời** giống nhau trong cùng ngành (VD: cách hỏi "vệ sinh sofa da vs sofa vải" giống nhau dù mỗi store giá khác nhau). Đây là insight mới phát hiện được, không phải thứ bị bỏ qua trước đó.

2. **Rủi ro kỹ thuật khi share content cao hơn hẳn share instruction.**
   Share instruction sai nhiều lắm bot hơi lệch tone. Share content sai (leak giá/policy store A sang trả lời cho store B) là sai fact trực tiếp với khách — nặng hơn nhiều. Vì vậy pipeline mới phải xây thêm cơ chế `merchant_fill` + lint riêng — hạ tầng này **không cần thiết** ở tầng instruction, nên tầng content-shared ra đời muộn hơn, phức tạp hơn để làm đúng.

3. **Khác owner, khác KPI.**
   KB per-app hiện tại (Ivy) do dev team (Fennic) xây để tối ưu **correctness/safety** (đo bằng correction rate) — không phải bài toán "merchant mới cold-start thiếu data". Niche pack giải bài toán khác: **coverage cho merchant mới** (đo bằng % conversation "bot lacks data"). 2 KPI khác nhau, 2 nhóm sở hữu khác nhau → hạ tầng phát triển tách rời cho tới khi có người chủ động nối lại (chính là plan này).

**Tóm lại:** không phải thiếu sót kiến trúc, mà là (a) giả định cũ về "fact luôn khác theo store" chưa từng bị data thách thức, (b) làm an toàn tầng content khó hơn hẳn tầng instruction, và (c) đây là bài toán KPI mới (cold-start) chưa ai từng đứng ra sở hữu.

---

## 5. Rủi ro cần lưu ý khi build pipeline mới (từ kinh nghiệm vận hành Ivy thực tế)

| # | Rủi ro | Vì sao biết (kinh nghiệm CS team) | Áp dụng vào pipeline mới |
|---|---|---|---|
| 1 | `merchant_fill` pass lint không đảm bảo substitute đúng lúc runtime | — | Test 2 store khác nhau cùng 1 pattern, xem bot có lẫn giá/policy giữa 2 store không |
| 2 | Viết fix cho "pattern lỗi" theo hướng liệt kê cái sai (negative example) | Từng bị bot copy nguyên câu "đừng nói X" ra trả lời khách (hallucinate ngược) | Prompt cho LLM sinh pack phải luôn generate theo hướng "câu trả lời ĐÚNG", không liệt kê điều cấm |
| 3 | Scenario directive (transfer to human, request order ID) rủi ro cao hơn FAQ text | Hành động sai (trigger nhầm) nặng hơn nhiều so với trả lời sai chữ | Cần vòng test riêng cho false-positive trigger, không chỉ test true-positive |
| 4 | Entry trong pack phải tự đủ nghĩa khi bị RAG kéo ra lẻ, không phụ thuộc context cluster | Bot bốc nhầm đoạn thiếu ngữ cảnh → trả lời vô nghĩa | Check mỗi FAQ/directive đứng độc lập được, không tham chiếu "như trên" |
| 5 | Offline win-rate cao không đảm bảo production ổn — nhiều lỗi thực ra do stale index, không phải content sai | Nhiều correction từng bị quy nhầm là "KB thiếu" trong khi là quên reindex | Sau khi merchant approve pack, cần bước reindex + smoke test bằng câu hỏi thật trước khi tính pilot đã live |
| 6 | Pattern chỉ xuất hiện ở đúng ngưỡng tối thiểu (2 store) dễ bị generalize nhầm | — | Với furniture (94 store, mẫu nhỏ), soát tay các pattern biên giới (chỉ 2-3 store) trước khi đưa vào pack chính thức |

---

## 6. Đề xuất mô hình 3 tầng (để 2 kiến trúc không xung đột)

```
Layer 1: App-wide instruction & KB (hiện tại — Fennic/dev team sở hữu)
         ↓
Layer 2: Industry knowledge pack (MỚI — pipeline niche pack)
         ↓
Layer 3: Store-specific override (merchant tự nhập, giữ nguyên như hiện tại)
```

Layer 2 không thay thế Layer 1 hay 3 — nó lấp khoảng trống ở giữa: khi merchant mới chưa kịp tự dạy bot (Layer 3 mỏng), bot vẫn có kiến thức nền theo ngành thay vì hoàn toàn trống. Khi merchant tự nhập fact riêng (giá, policy cụ thể), Layer 3 vẫn override Layer 2 như cơ chế `merchant_fill` đã thiết kế.

Đây là điểm nên đưa vào roadmap thảo luận chung với Fennic/dev team, vì `/kb-sync` và `/product-kb-sync` hiện tại chưa có khái niệm "industry layer" — cần thống nhất trước khi 2 pipeline cùng ghi vào 1 nơi lưu trữ KB, tránh xung đột dữ liệu.
