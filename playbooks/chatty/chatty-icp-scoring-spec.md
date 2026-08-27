# Chatty ICP Scoring — Spec (Data-Driven, thay thế 4-tier cũ)

**Owner:** Liz (CSL) — thiết kế & duyệt
**Trạng thái:** Draft v1 (2026-08-12) — cần dev team implement phần real-time (§4), phần on-demand đã có skill `/icp-score` dùng ngay
**Nguồn gốc:** Đề xuất ban đầu từ note Nexus (`notes.avada.net/yC1sRvaF6V.html`) — ICP classification → segment → routing → playbook, thay vì chỉ ICP Yes/No

---

## 0. Thay đổi so với hiện tại — ĐỌC TRƯỚC KHI IMPLEMENT

CSL hiện có **`kb/cs-process/chatty/handle-icp-qualification.md`** — SOP đang sống trên KB live, phân loại merchant bằng cách **hỏi trong chat** (email domain, GMV tự nhìn, 2-3 câu hỏi) thành 4 chân dung: **Solo Explorer / Growing Operator / Scaling CX Lead / Mid-Market Proof-Giver**, tag `icp-solo` / `icp-growing` / `icp-scaling` / `icp-midmarket`.

Spec này **thay thế hoàn toàn** taxonomy đó bằng: **score 0-100 tính từ data thật** (BigQuery `dash_merchant_360` + StoreLeads enrichment) → segment **`ICP-High` / `ICP-Medium` / `ICP-Low` / `ICP-Unknown`** + confidence %.

**Việc cần làm kèm theo (chưa làm trong spec này, cần Liz duyệt riêng trước khi push KB):**
- Patch `handle-icp-qualification.md`, `handle-icp-discovery-call.md`, `README.md` (trong `kb/cs-process/chatty/`) — đổi tag cũ → tag mới, giữ lại phần "hỏi trong chat" làm bước verify khi confidence thấp (không xóa hẳn, vì vẫn cần khi thiếu data)
- Đây là nội dung sống trên bot Ivy → phải qua flow `kb-sync`: patch → Liz duyệt → push + reindex, KHÔNG tự sửa trực tiếp

---

## 1. Nguồn data — 8 tiêu chí theo note Nexus, đã verify field thật 2026-08-12 (test trên `99bikescomau.myshopify.com`, Shopify Plus, $449 MRR)

Note Nexus liệt kê 8 tiêu chí. Test lại từng cái bằng `merchant_profile` / `shop_profile` / `merchant_cs_history` (MCP `avada-analytic`) — **tất cả field đều tồn tại thật**, không cái nào phải bỏ. Gộp cả 8 vào **1 công thức duy nhất** để ra score sơ bộ ngay từ đầu (không tách riêng context-only) — 2 tiêu chí cuối (lịch sử ticket, đối thủ đang dùng) vẫn cộng vào điểm, nhưng weight thấp hơn vì bản chất là tín hiệu "cách trả lời cho đúng" hơn là "KH lớn hay nhỏ".

| Tiêu chí | Field (đã verify) | Đọc thế nào |
|---|---|---|
| Shopify plan | `primary_plan` (từ `shop_profile`, giá trị chuẩn hoá `plus`/`advanced`/`grow`/`basic`) | `shopify_plan` thô có cả legacy code (`professional`/`unlimited`/`shopify_plus`) lẫn value mới — **dùng `primary_plan`**, không dùng field thô |
| Traffic của store | `storeleads_profile.estimated_visits` | Visit/tháng. Traffic lớn = nhu cầu thực, mọi lỗi đều ảnh hưởng doanh thu họ |
| Quy mô doanh nghiệp | `storeleads_profile.{employee_count, estimated_sales, monthly_app_spend}` | Chi cho app hằng tháng cao → có ngân sách, quen trả tiền cho công cụ tốt |
| Đang trả tiền hay chưa | `current_mrr`/`mrr`, `is_paying_now`, `trial_flag` | Có MRR → khách thật. Đang trial → xử lý sớm, đừng dồn người vào ngay |
| Đã dùng bao lâu | `days_since_install`, `installed_at` | Install <30 ngày mà plan cao → nhóm cần onboarding. Install lâu mà vẫn hỏi cơ bản → dấu hiệu chưa activate |
| Đang thực sự dùng không | `activation_status`, `usage_segment`, `chatty_conversations_30d` | Có usage → yêu cầu xuất phát từ vận hành thật, không phải hỏi thăm dò |
| Đã hỏi gì trước đây | `ticket_count`, `latest_subject` (từ `merchant_profile`) + full history qua `merchant_cs_history(shop_domain, app_id)` | Nhiều ticket cùng chủ đề chưa giải quyết → đừng trả lời như lần đầu. Có lịch sử tương tác (nhất là DFY) = mức đầu tư quan hệ cao hơn. `merchant_cs_history` trả `subject`, `description`, `ts_status`, `ticket_status`, `created_at` — đủ để so trùng chủ đề gần đây |
| Đang dùng đối thủ/tool nào | `storeleads_profile.{app_names, technology_names}` | Trả cả list app đang cài (vd `Gorgias`, `Zendesk`, `BetterDocs`) — biết mình đang đứng cạnh ai khi tư vấn/offer, đồng thời số lượng tool trả phí đang dùng là tín hiệu phụ về mức trưởng thành vận hành |

⚠️ `storeleads_profile` (dùng cho Traffic, Quy mô DN, và 2 tiêu chí cuối) có thể `null` nếu StoreLeads không match được domain — tính vào confidence %, không giả định luôn có data.

**Không có, đã bỏ khỏi công thức (không tự động hoá được):**
- Ads spend (~"$3K+/month Meta/Google" mà SOP cũ hỏi qua chat) — không có trong data warehouse, không có nguồn data-driven thay thế → giữ lại như câu hỏi verify thủ công khi confidence thấp (ICP-Unknown).

---

## 2. Công thức scoring (v1 — cần Liz duyệt trước khi dev implement)

| Tiêu chí | Weight | Cách tính điểm (0-100 từng tiêu chí) |
|---|---|---|
| Shopify plan (`primary_plan`) | 20% | plus=100, advanced=75, grow=50, basic=25, không rõ=0 |
| Traffic (`estimated_visits`) | 12% | ≥100k/tháng=100, 10k-100k=65, <10k=35, không có data=0 |
| Quy mô doanh nghiệp (`employee_count`, `estimated_sales`, `monthly_app_spend`) | 13% | employee ≥50 HOẶC monthly_app_spend cao=100; employee 10-49=65; employee <10=35; không có data=0 |
| Đang trả tiền (`current_mrr`, `is_paying_now`, `trial_flag`) | 20% | MRR ≥$100=100, $40-99=70, $1-39=40, trial/free=10 |
| Đã dùng bao lâu (`days_since_install`, `trial_flag`) | 8% | ≥90 ngày & không trial=100, 30-89 ngày=60, <30 ngày hoặc đang trial=30 |
| Đang thực sự dùng (`activation_status`, `usage_segment`, `chatty_conversations_30d`) | 15% | `usage_segment='high_usage'`=100, `active_usage`=60, `inactive_30d`=10 |
| Lịch sử ticket (`ticket_count`, `dfy_ticket_count`, có recurring unresolved không) | 6% | có DFY ticket=100, có ticket đã resolve bình thường=70, có ticket đang lặp lại chưa xong=40, chưa từng liên hệ=50 (trung tính, không đủ tín hiệu) |
| Đối thủ/tool stack (`app_names`/`technology_names` — đếm tool CS/marketing trả phí) | 6% | ≥2 tool trả phí (vd Gorgias/Zendesk/Klaviyo)=100, có 1=65, không thấy tool nào=35, không có `storeleads_profile`=0 |

**Score tổng** = Σ(điểm tiêu chí × weight) — cả 8 tiêu chí, không tách riêng nữa.

**Confidence %** = tỷ lệ tiêu chí có data thật / 8 (thiếu StoreLeads enrichment hoặc row `dash_merchant_360` không tồn tại → confidence thấp)

**Segment:**
- Confidence < 60% → **`ICP-Unknown`** (bất kể score bao nhiêu — thiếu data không được đoán liều)
- Score ≥ 80 → **`ICP-High`**
- Score 50-79 → **`ICP-Medium`**
- Score < 50 → **`ICP-Low`**

---

## 3. Routing / auto-action theo segment (Liz chọn: tự động hành động, không chỉ hiển thị signal)

| Segment | Auto-tag | Auto-action |
|---|---|---|
| **ICP-High** | `icp-high` | Ưu tiên SLA (route P1 nếu có issue), Slack ping CS senior/Liz nếu case phức tạp, bot gợi ý offer discovery call/DFY thay vì trả lời generic |
| **ICP-Medium** | `icp-medium` | Flow chuẩn, nhưng flag "watch for expansion" trên CRM Work để CS để ý upsell |
| **ICP-Low** | `icp-low` | Flow chuẩn, self-serve, không auto-escalate |
| **ICP-Unknown** | `icp-unknown` | Bot hỏi 2-3 câu verify (tái dùng bộ câu hỏi trong `handle-icp-qualification.md` Bước 2) trước khi finalize segment |

**Confidence hiển thị kèm segment** trên mọi nơi hiển thị (chat sidebar, CRM Work comment, ticket) — vd `ICP-High (92%)` — để CS biết mức tin cậy, không coi là tuyệt đối.

---

## 4. Chỗ cần dev implement (ngoài phạm vi CSL)

**Việc CSL/Betty làm được ngay** (không cần dev): skill `/icp-score` — CS tự ấn chấm 1 KH bất kỳ lúc nào, dùng MCP `avada-analytic` đã có sẵn. Xem `skills/icp-score/SKILL.md`.

**Việc cần dev team (bridge repo `avada/cs-team/avada-cs-ai-agent-crisp-chat`, file `process.ts`)** — để có auto real-time (chấm + gắn tag ngay khi chat mở, không cần CS bấm):

1. Bot Ivy hiện là **KB-only RAG với static profile inject trước chat** (đã verify — không tool-calling live tới data giữa chat). Muốn auto real-time, cần 1 trong 2 hướng:
   - **(a) Pre-compute tại webhook/session-start**: khi Crisp session mới mở, gọi 1 service tính ICP score (business logic ở §2) → inject kết quả vào static profile object cùng lúc với `shopDomain`/`appPlan` hiện tại → bot đọc được ngay từ đầu, không cần tool-call giữa chat.
   - **(b) Thêm 1 tool cho agent gọi giữa chat** (nếu muốn tái tính khi có thêm thông tin từ câu hỏi verify) — engineering nặng hơn (a), chỉ làm nếu (a) không đủ.
   - **Khuyến nghị: làm (a) trước** — đơn giản hơn, khớp với cách pipeline hiện tại đang hoạt động (static injection).
2. Auto-tag ngược lại: sau khi tính được segment, cần 1 call ghi tag vào hệ thống mà CS nhìn thấy (Crisp custom data và/hoặc Avada Ticket API `PUT /api/external/tickets/{id}` tagIds — endpoint này CSL đã dùng, xem memory `avada_ticket_write_tags_endpoint`).
3. Câu hỏi mở cần dev xác nhận: `shopDomain`/`appPlan` trong static profile hiện lấy từ đâu (cached Crisp custom field hay Shopify Admin API tại thời điểm webhook)? — quyết định chỗ nên chèn thêm bước tính ICP score vào đúng pipeline đó.

**Đề xuất next step:** Liz gửi §2 + §3 + §4 cho dev lead review tính khả thi của hướng (a), trước khi CSL viết prompt/copy cụ thể cho bot dùng khi biết ICP segment.

---

## 5. Rollout đề xuất (theo tinh thần note Nexus)

- **Phase 1 (đã làm):** skill `/icp-score` on-demand — CS tự chấm, tự thấy score+segment+lý do
- **Phase 2:** dev implement §4(a) — auto pre-compute + hiển thị segment ngay khi chat mở (chưa auto-action, chỉ hiển thị)
- **Phase 3:** auto-action theo §3 (auto-tag, auto-route, bot đổi flow theo segment)
- **Phase 4:** mở rộng — detect business opportunity (upsell/DFY/launch-critical) từ nội dung chat kết hợp segment, theo hướng "CS AI = support copilot có customer context" trong note gốc

---

*Draft v1 — 2026-08-12. Chờ Liz duyệt công thức §2 + gửi §4 cho dev trước khi implement phần real-time.*
