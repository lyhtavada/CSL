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

## 1. Nguồn data — đã verify field thật (BigQuery `avada-crm.avada_product_dash.dash_merchant_360`, `app_id='avadaFaq'`)

| Field | Ý nghĩa | Dùng cho |
|---|---|---|
| `shopify_plan` | Basic / Shopify / Advanced / Plus | Quy mô business |
| `current_mrr`, `mrr`, `is_paying_now` | Đang trả Chatty bao nhiêu | Mức đầu tư vào Chatty |
| `days_since_install`, `trial_flag` | Cài bao lâu, còn trial không | Độ trưởng thành quan hệ |
| `chatty_conversations_30d`, `chatty_chat_to_sales_rate_30d`, `key_action_count_30d`, `usage_segment` | Mức dùng thật | Engagement |
| `ticket_count`, `has_contacted_cs`, `dfy_ticket_count` | Lịch sử tương tác CS | Mức đầu tư quan hệ |
| `gross_revenue_30d`, `net_revenue_30d`, `total_revenue` | Doanh thu Chatty tạo ra cho store (sales-attributed) | Giá trị Chatty đang tạo |

**Đã verify (test live 2026-08-12 trên `99bikescomau.myshopify.com`, Shopify Plus, $449 MRR):**
- `shop_profile(shop_domain, app_id)` trả về `storeleads_profile.{estimated_sales, estimated_sales_yearly, estimated_visits, estimated_page_views, employee_count, monthly_app_spend, rank}` — traffic/quy mô store thật, dùng được cho tiêu chí "Store scale" ở §2.
- `shop_profile` cũng trả `primary_plan` (giá trị chuẩn hoá: `plus`/`advanced`/`grow`/`basic`...) — sạch hơn field `shopify_plan` thô (có cả legacy value như `professional`/`unlimited`/`shopify_plus` lẫn value mới `Advanced`/`Grow`/`Plus`). **Dùng `primary_plan` làm nguồn chính cho tiêu chí Shopify plan tier**, không dùng `shopify_plan` thô.
- ⚠️ `storeleads_profile` có thể null nếu StoreLeads không match được domain (`match_source` cho biết độ tin — không có nghĩa là luôn có data) → tính vào confidence %, không giả định luôn có.

**Không có, đã bỏ khỏi công thức:**
- Ads spend (~"$3K+/month Meta/Google" mà SOP cũ hỏi qua chat) — không có trong data warehouse, không có nguồn data-driven thay thế → giữ lại như câu hỏi verify thủ công khi confidence thấp (ICP-Unknown), không đưa vào scoring tự động.

---

## 2. Công thức scoring (v1 — cần Liz duyệt trước khi dev implement)

| Tiêu chí | Weight | Cách tính điểm (0-100 từng tiêu chí) |
|---|---|---|
| Shopify plan tier (`primary_plan`, KHÔNG dùng `shopify_plan` thô) | 25% | plus=100, advanced=75, grow=50, basic=25, không rõ=0 |
| Mức đầu tư vào Chatty (`current_mrr`) | 20% | ≥$100=100, $40-99=70, $1-39=40, free/trial=10 |
| Store scale (`storeleads_profile.estimated_visits` + `employee_count`) | 20% | visits ≥100k HOẶC employee ≥50=100; visits 10k-100k HOẶC employee 10-49=65; visits <10k HOẶC employee <10=35; `storeleads_profile` null=0 (tính vào confidence, không đoán) |
| Engagement với Chatty (`chatty_conversations_30d`, `usage_segment`) | 15% | `usage_segment='high_usage'`=100, `active_usage`=60, `inactive_30d`=10 |
| Support relationship (`ticket_count`, `dfy_ticket_count`) | 10% | có DFY ticket=100, có ticket thường (≥1)=60, chưa từng liên hệ=30 |
| Business maturity (`days_since_install`, `trial_flag`) | 10% | ≥90 ngày & không trial=100, 30-89 ngày=60, <30 ngày hoặc đang trial=30 |

**Score tổng** = Σ(điểm tiêu chí × weight)

**Confidence %** = tỷ lệ field có data thật / tổng field cần (nếu thiếu StoreLeads enrichment hoặc row `dash_merchant_360` không tồn tại → confidence thấp)

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
