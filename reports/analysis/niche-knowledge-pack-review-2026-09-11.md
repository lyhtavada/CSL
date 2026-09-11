---
date: 2026-09-11
topic: Niche Knowledge Pack (Chatty AI Agent) — review đề xuất BA
source: https://notes.avada.net/VrifvsaToH.html?name=niche-knowledge-pack-2-nganh-de-xuat
proposed_by: Anthony (BA), Tùng (PM Team Tesla)
status: feedback đã soạn, chờ Liz gửi
---

# Niche Knowledge Pack — Review & Feedback

## Bối cảnh

BA team Chatty (Anthony/Tùng) đề xuất pipeline "niche knowledge pack" — 1 tầng KB dùng chung theo ngành hàng (pilot: **furniture**) cho **Chatty AI Agent** (bot chat widget nhúng trên storefront, trả lời **buyer thật** về sản phẩm/chính sách của từng store) — khác với Ivy/Joyce (trả lời **merchant** về sản phẩm Chatty/Joy).

Vấn đề gốc: median chỉ 5 FAQ/store → 45% conversation kết thúc sau 1 tin, 34% response thiếu data, 12.7% phải handoff người (baseline 180 ngày).

Pipeline: S1 acquisition (Agent API + BigQuery) → S2 sanitize (Presidio/spaCy PII, dedup, không LLM) → S3 pattern mining (BGE-small + HDBSCAN, GPT-5.5 gán tên, ≥2 store mới tính pattern) → S4 pack generation (3 variant A/B/C, tách `merchant_fill` khỏi shared KB) → S5 eval (Claude Opus judge trên 300 câu holdout, hard-gate chặn fabricate giá/PII) → S6 deploy (push Agent API, merchant approve, pilot 30 ngày ở 3 store furniture).

Timeline: demo 11/09, sample 1 (furniture) 15/09, sample 2 (apparel) 17/09, deploy pilot 18/09–30/09.

## Điểm mạnh của đề xuất

- Tách `merchant_fill` (giá/tồn kho/policy) khỏi shared knowledge — đúng nguyên tắc quan trọng nhất, tránh lẫn data store-specific vào KB chung.
- "Silence ≠ correct bot response" — đúng tinh thần QA (không coi im lặng là bot trả lời đúng).
- Hard-gate chặn fabricate giá/PII/hứa ngoài phạm vi — đúng trọng tâm rủi ro khi bot nói thẳng với buyer thật (sai = mất tiền/uy tín merchant ngay lập tức, khác Ivy/Joyce chỉ nói nội bộ với merchant).

## Rủi ro & feedback (dựa kinh nghiệm training Ivy/Joyce)

| # | Rủi ro | Vì sao biết (kinh nghiệm CS team với Ivy) | Cách áp dụng / mitigate |
|---|---|---|---|
| 1 | `merchant_fill` pass lint không đảm bảo substitute đúng lúc runtime | — | Test 2 store khác nhau cùng 1 pattern, xem bot có lẫn giá/policy giữa 2 store khi trả lời buyer không |
| 2 | Viết fix cho "pattern lỗi" theo hướng liệt kê cái sai (negative example) | Ivy từng bị bot copy nguyên câu "đừng nói X" ra trả lời khách (hallucinate ngược) | Prompt cho LLM sinh pack phải luôn generate theo hướng "câu trả lời ĐÚNG", không liệt kê điều cấm — xem [[feedback_kb_no_negative_examples]] |
| 3 | Scenario directive (transfer to human, request order ID) rủi ro cao hơn FAQ text | Hành động sai (trigger nhầm) nặng hơn nhiều so với trả lời sai chữ, đặc biệt khi đối tượng là buyer thật đang muốn mua hàng | Cần vòng test riêng cho false-positive trigger, không chỉ test true-positive |
| 4 | Entry trong pack phải tự đủ nghĩa khi bị RAG kéo ra lẻ, không phụ thuộc context cluster | Bot từng bốc nhầm đoạn thiếu ngữ cảnh → trả lời vô nghĩa với buyer | Check mỗi FAQ/directive đứng độc lập được, không tham chiếu "như trên" |
| 5 | Offline win-rate cao không đảm bảo production ổn — nhiều lỗi thực ra do stale index, không phải content sai | Nhiều correction ở Ivy từng bị quy nhầm là "KB thiếu" trong khi là quên reindex | Sau khi merchant approve pack, cần bước reindex + smoke test bằng câu hỏi buyer thật trước khi tính pilot đã live — xem [[joy_reindex_stale_root_cause]] |
| 6 | Pattern chỉ xuất hiện ở đúng ngưỡng tối thiểu (2 store) dễ bị generalize nhầm | — | Với furniture (94 store, mẫu nhỏ), soát tay các pattern biên giới (chỉ 2-3 store) trước khi đưa vào pack chính thức |

## Điểm bổ sung (Betty, ngoài bảng risk của Liz)

1. **Brand/tên store leakage** — S2 chỉ audit PII (0 leak/200 sample), không rõ có lọc tên thương hiệu/sản phẩm cụ thể không. Giữ nguyên phrasing gốc (đúng, để tránh over-summarization) thì dễ làm brand của store A lọt nguyên câu vào pack rồi bot đưa cho buyer store B.
2. **Đa ngôn ngữ** — bot nói thẳng với buyer cuối (khác Ivy/Joyce chủ yếu English với merchant). Furniture/Apparel buyer có thể nhiều thị trường/ngôn ngữ — đề xuất chưa nhắc tới.
3. **Review từ phía eng** — đây là thay đổi kiến trúc retrieval (thêm tầng KB chung cross-store), nên có review từ eng (kiểu Fennic — code owner retrieval/guard Chatty core, xem [[cs_ai_bot_code_owner_fennic]]) trước go-live, không chỉ BA tự chấm bằng Opus judge.

## Next step

- Feedback đã soạn thành message gửi Anthony (cc Tùng) qua `/draft-message` — nội dung ủng hộ hướng đi, không block, đề nghị đưa 6+3 điểm trên vào checklist trước khi push pilot 3 store thật (18/09).
- Theo dõi: nếu BA phản hồi/pilot chạy, cập nhật file này hoặc tạo follow-up note.
