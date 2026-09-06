---
name: store-research
description: Research đầy đủ 1 store để Liz chuẩn bị call (demo, onboarding, QBR, handover, save deal) — Betty pull hết dữ liệu có thể chạm được (analytic MCP, BigQuery Crisp, Google Calendar, storefront config thật, website merchant), viết thành 1 page nghiên cứu + kịch bản call, push thẳng lên Notion "Joy Stores" hoặc "Chatty Stores" và lưu bản markdown trong repo. Dùng khi Liz nói "/store-research", "research store X", "chuẩn bị call với X", "prep call [domain]", hoặc đưa 1 domain/email/tên brand kèm ý định gặp họ.
version: 1.0.0
---

# Store Research

Một store → một page Notion: **research + kịch bản call**, đủ để Liz mở ra là vào call được.

## Input Liz đưa

Bất kỳ thứ nào sau đây, không cần đủ: domain (`thekeeperscollective.com` hoặc
`x.myshopify.com`), email merchant, tên brand, link Crisp session, link deal analytics.
Tự resolve phần còn lại — đừng hỏi lại Liz những gì tra được.

Nếu chưa biết app: tra `merchant_search` rồi `shop_profile` → app nào đang cài.
Store cài **cả Joy và Chatty** → hỏi Liz call này về app nào; store **chưa cài gì**
(prospect) → hỏi Liz nhắm bán app nào.

## Bước 1 — Pull dữ liệu

### 1a. Chạy script (storefront + Crisp + Calendar)

```bash
.venv-crisp/bin/python skills/store-research/scripts/fetch_store.py \
  --shop <x.myshopify.com> [--site <domain-công-khai>] [--email <email>] [--days 180]
```

Trả về:
- **storefront**: app đang cài thật + config Joy render ra trang (earning/redeem/tier/referral,
  tự tính `money_per_point`, `cashback_pct`, `free_points_stackable` = điểm kiếm được
  mà không cần mua hàng). Đây là **nguồn đáng tin nhất về trạng thái app** — đúng cái
  khách đang thấy, không phải cái DB nói.
- **crisp.md**: toàn bộ transcript theo session (BigQuery, không giới hạn 40 msg như Crisp API)
- **calendar.json**: lịch call ±90 ngày khớp store (bắt cả lịch do sale đặt)

Phần nào lỗi thì script in traceback và chạy tiếp phần còn lại. **Phần lỗi phải ghi lên
page là "không lấy được + lý do", tuyệt đối không ghi thành "không có".**

### 1b. Gọi MCP analytic (Betty tự gọi, script không làm được)

Bắt buộc:
- `merchant_profile(shop_domain, app_id)` — plan, MRR, install date, revenue, billing health, ticket summary
- `merchant_cs_history(shop_domain, app_id)` — ticket đang mở, quá hạn, ai đang giữ
- `shop_profile(shop_domain)` — store này còn dùng app Avada nào khác

Khi liên quan:
- `sale_deals_list` / `sale_deal_get` + note trên deal — stage, probability, AM cũ, label
  (vd "Competitor Displacement"), lý do bàn giao
- `merchant_transactions` — nếu nghi vấn billing / churn risk
- `storeleads_merchant_stack` / `storeleads_app_profile` — stack đối thủ, quy mô store
  (hay bị từ chối quyền → ghi rõ là không truy cập được)
- `merchant_timeline` — hay vượt quota bytes; nếu lỗi thì bỏ, đừng cố

### 1c. Đọc website merchant

Fetch trang chủ + collections + trang rewards/loyalty nếu có. Cần rút ra: ngành hàng,
USP, đối tượng khách, khoảng giá, quy mô SKU, **retention đang có gì** (newsletter discount,
free gift threshold, subscription, bundle). Với prospect thì đây là phần nặng nhất —
là nguyên liệu duy nhất để dựng nhánh Problem.

## Bước 2 — Viết page

**Một cấu trúc chung cho mọi store.** Section nào không có data thì vẫn giữ heading và
ghi một dòng lý do (`Không lấy được: MCP storeleads từ chối quyền`), **không xoá section** —
để các store so sánh được với nhau về sau.

Độ dài co giãn theo lượng data thật, không độn chữ. Store mới cài 2 tuần thì phần
"Trạng thái sản phẩm" ngắn là đúng.

```markdown
## TL;DR
3-5 gạch đầu dòng. Câu đầu luôn là: call ngày nào, với ai, mục đích gì, và Liz cần
đạt được gì. Sau đó là 2-3 phát hiện đắt nhất.

## Account
Bảng: Shop domain | Contact (tên, email, chức danh) | Ngành | Shopify plan | App plan +
MRR | Ngày install | Doanh thu lifetime | Billing health | Nguồn (organic/referral/sale)
| Stack app khác

## Bối cảnh merchant
Ngành hàng, USP, đối tượng khách, quy mô, khoảng giá. Retention hiện có ngoài app mình.
Nếu là prospect: vì sao họ đi tìm giải pháp (lấy từ form book demo / Crisp).

## Timeline
Ngày → chuyện gì → ai. Gộp cả Crisp, ticket, call đã diễn ra, thao tác merchant tự làm
trong app. Nhìn vào phải thấy được "ai đang chờ ai".

## Trạng thái sản phẩm thật
Joy → earning rules / redeem rules / VIP tier (bật hay tắt) / referral / widget, kèm
%hoàn tính được và tổng điểm free không cần mua hàng.
Chatty → chatbox config, AI resolution, coverage, human takeover, volume chat.
Luôn ghi rõ số nào đọc từ storefront, số nào từ DB — hai nguồn có thể lệch.

## Gap & cơ hội
Đánh số. Mỗi gap: **hiện trạng (số cụ thể) → rủi ro/chi phí → đề xuất**. Mỗi đề xuất
phải có bằng chứng đi kèm; không có số thì ghi là giả định.

## Kịch bản call
1. Mở đầu — 1 câu hỏi mở để họ tự nói ra vấn đề thật (đừng đoán trước hộ họ)
2. Đào sâu — 2-3 nhánh follow-up, chỉ dùng nhánh khớp câu trả lời của họ
3. Demo mapping — feature nào giải quyết vấn đề nào họ vừa nêu, kèm câu nói mẫu (tiếng Anh)
4. Need-payoff — câu chốt để họ tự phát biểu KPI thành công 90 ngày
5. Objection — objection dự đoán được + cách trả lời
6. Đóng call — chốt bước tiếp theo + timeline

Câu nói với merchant viết **tiếng Anh** (xem `_identity/tone-and-voice.md`).
Ghi chú cho Liz viết tiếng Việt.

## Câu hỏi cần hỏi
Chỉ những câu **không tra được** bằng data. Thứ nào research ra rồi thì đừng hỏi lại
merchant — mất uy tín.

## Việc cần làm
- [ ] Trước call
- [ ] Sau call

## Nguồn & khoảng trống
Đã pull từ đâu, phần nào không lấy được và vì sao. Không có mục này thì người đọc
sau không biết chỗ nào đáng nghi.
```

**Nguyên tắc:** phần suy luận phải tách khỏi phần dữ kiện. Con số đọc từ hệ thống ghi
thẳng; suy đoán phải mở đầu bằng "đọc như là", "nhiều khả năng". Bloomable page đã làm
đúng chỗ này ("đọc như 'cài rồi để mặc định'") — giữ thói quen đó.

## Bước 3 — Push Notion + lưu repo

Lưu markdown:
```
reports/store-research/{joy|chatty}/{shop-slug}-{YYYY-MM-DD}.md
```

Push thẳng lên Notion (Liz đã chốt: không cần duyệt trước, chị sửa trên Notion):

```bash
cd /Users/avada/CSL && .venv-crisp/bin/python skills/dfy-weekly-chatty/scripts/push_notion.py \
  --parent <PARENT_ID> \
  --title "<Brand> — <domain>" \
  --md reports/store-research/<app>/<file>.md
```

| Parent | Page ID |
|---|---|
| Joy Stores | `38fb0da449f1808cbf1beb435fd6018c` |
| Chatty Stores | `3d3b0da449f1809abf8cea8e9f18d7d8` |

Title theo đúng nếp đang có: `Bloomable ZA — bloomablestore.myshopify.com`. Dùng domain
công khai nếu có, không thì myshopify domain.

Page mới tự nằm **trên cùng** (`position: page_start`). Xong thì báo Liz link Notion +
đường dẫn file local, kèm 3 phát hiện đắt nhất ngay trong chat — đừng bắt chị mở Notion
mới biết có gì.

**Store đã có page cũ:** đọc page cũ trước (`skills/grade-joy-trainee/scripts/notion_fetch.py`),
tạo page mới và thêm section "Thay đổi so với lần research trước" ở đầu. Không sửa đè
page cũ — lịch sử research của 1 account là thứ có giá trị.

## Ranh giới

- **Không** dùng skill này để chấm điểm ICP (đã có `/chatty-icp-score`) hay để tạo note
  trên deal timeline (đã có `/account-research-note`). Skill này ra 1 page Notion để đọc trước call.
- **Không** screenshot store thật (xem `tools/browser/README.md`).
- Dữ liệu merchant là dữ liệu thật của khách: page nằm trong workspace Notion nội bộ,
  không đưa ra ngoài, không đưa vào training data.
