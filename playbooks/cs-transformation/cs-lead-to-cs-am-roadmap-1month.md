# Roadmap: CS Lead → Customer Success / Business Partner (1 tháng, AI-era)

> Tạo 2026-08-07. Mục tiêu: chuyển Liz + team từ "trả lời ticket" sang "Customer Success / Business Partner", chuẩn bị nền lên CSM/AM. 5-7h/tuần, áp dụng trực tiếp vào Joy/Chatty.

Format: 4 tuần, mỗi tuần 5-7h, mỗi chủ đề có 80/20 + tài liệu + bài tập gắn thẳng vào Joy/Chatty. Bỏ những thứ không cần thiết ngay bây giờ, ghi rõ vì sao.

---

## Nguyên tắc lọc nội dung

Trong 5 nhóm ban đầu (Business Thinking, Data Thinking, Customer Success, AI Collaboration, Leadership), gộp lại theo thứ tự ưu tiên thực dụng nhất:

- **Tuần 1: Business Thinking** — nền tảng bắt buộc, không có cái này thì Data/CS Skills sau vô nghĩa.
- **Tuần 2: Data Thinking** — công cụ để chứng minh business thinking bằng số, không phải cảm tính.
- **Tuần 3: Customer Success Core** (Health, Churn, RCA, Consultant mindset) — phần "khó bị AI thay thế" nhất.
- **Tuần 4: AI Collaboration + Leadership** — gộp chung vì cả hai đều là "áp dụng những gì học được vào vận hành team".

**Cắt bớt/hoãn:**
- SQL nâng cao (window functions, JOIN phức tạp) — hoãn tháng 2. Tháng này chỉ cần đọc-hiểu SQL cơ bản.
- Prompt engineering học thuật (chain-of-thought theory, RAG architecture) — không cần, chỉ cần *dùng* AI để làm SOP/RCA.
- Account Management formal training (quota, forecasting, sales skills) — quá sớm, chưa có role AM. Để lại roadmap tháng 3-6.

**Đọc song song cả tháng (15 phút/ngày):** [Lenny's Newsletter](https://www.lennysnewsletter.com/) — chỉ 1 nguồn, không dàn trải nhiều blog cùng lúc (đúng nguyên tắc "không học lan man"). Nội dung về SaaS/product/growth giúp củng cố business thinking xuyên suốt 4 tuần mà không tốn thêm block học riêng.

---

## TUẦN 1 — Business Thinking (Merchant Journey, Ecommerce, Metrics)

### 1.1 Merchant Journey & Customer Lifecycle (2h)
**Vì sao:** Xử lý ticket theo "vấn đề" thay vì theo giai đoạn merchant đang ở đâu. Merchant mới cài app khác hoàn toàn merchant Plus đã dùng 2 năm.
**Khi nào dùng:** Ngay khi đọc bất kỳ Crisp chat nào — hỏi "merchant này đang ở lifecycle stage nào?" trước khi trả lời.
**80/20:** 5 giai đoạn — Awareness → Onboarding → Adoption → Expansion → Renewal/Churn. Cùng 1 câu hỏi có ý nghĩa khác nhau tùy stage (VD: câu hỏi setup ở Onboarding = bình thường; ở tháng thứ 6 = red flag adoption thất bại).
**Tài liệu miễn phí tốt nhất:** [HubSpot — Customer Journey Map guide](https://blog.hubspot.com/service/customer-journey-map).
**YouTube:** kênh "SaaStr" — video về customer journey SaaS.
**Bài tập:** Chọn 5 ticket Joy/Chatty gần nhất → gắn mỗi ticket vào 1 giai đoạn lifecycle → viết 1 dòng "nếu biết stage này sớm hơn, đã trả lời khác thế nào".

### 1.2 Ecommerce Fundamentals cho Shopify apps (2h)
**Vì sao:** Chatty và Joy đều ăn theo hành vi mua hàng Shopify. Không hiểu AOV, conversion funnel, cart abandonment thì không tư vấn được merchant về giá trị app.
**80/20:** 5 con số merchant Shopify quan tâm nhất — Conversion Rate, AOV, Repeat Purchase Rate, CAC, LTV. Joy tác động Repeat Purchase Rate + LTV; Chatty tác động Conversion Rate qua tốc độ support.
**Tài liệu miễn phí:** [Shopify — Ecommerce Metrics guide](https://www.shopify.com/blog/ecommerce-metrics).
**Blog:** Shopify Plus blog, Baremetrics blog.
**Bài tập:** Lấy 1 merchant Joy đang dùng → ước lượng AOV và Repeat Purchase Rate trước/sau khi cài Joy (dùng `dash_merchant_360` hoặc analytics MCP).

### 1.3 Product Thinking cơ bản (1.5h)
**Vì sao:** Chuyển từ "trả lời câu hỏi" sang "hiểu tại sao merchant hỏi câu đó" — thường là feature gap hoặc UX confusing.
**80/20:** Framework Jobs to be Done — merchant không mua Joy vì "loyalty program", họ "thuê" Joy để "giữ khách quay lại mà không giảm giá mù quáng".
**Tài liệu miễn phí:** [Intercom — "Intercom on Jobs-to-be-Done"](https://www.intercom.com/books) (ebook free).
**Bài tập:** 3 feature request gần nhất từ ticket → viết lại theo JTBD: "Khi [tình huống], merchant muốn [job], để [outcome]".

### 1.4 Business Metrics tổng quan SaaS (1h)
**80/20:** MRR, Churn Rate, NRR — chỉ cần hiểu định nghĩa và đọc được, chưa cần tính tay.
**Tài liệu:** [ProfitWell/Paddle metrics glossary](https://www.paddle.com/resources).

### Bảng tài liệu Tuần 1

| Nguồn | Loại | Chi phí | Ưu tiên |
|---|---|---|---|
| HubSpot Customer Journey Map guide | Blog | Free | Đọc trước |
| Shopify Ecommerce Metrics guide | Blog | Free | Đọc trước |
| Intercom JTBD ebook | Ebook | Free | Nên đọc |
| ProfitWell metrics glossary | Reference | Free | Tra cứu khi cần |

**Mini project cuối tuần:** Viết 1 trang "Merchant Business Snapshot Template" — form Liz điền khi review 1 merchant lớn (lifecycle stage, AOV, repeat rate, top job-to-be-done). Dùng ngay cho Chatty Proactive Care.

---

## TUẦN 2 — Data Thinking (đọc dashboard, Excel, SQL cơ bản, phân tích bằng data)

### 2.1 Đọc Dashboard đúng cách (1.5h)
**80/20:** 3 câu hỏi khi nhìn bất kỳ dashboard nào — (1) Trend lên/xuống? (2) So với baseline nào? (3) Signal hay noise (đủ sample size chưa)? Đã có `/api/obs/metrics` và analytics MCP — vấn đề là chưa có thói quen hỏi 3 câu này.
**Bài tập:** Lấy dashboard bot performance (verify coverage/correction rate) tuần này → trả lời 3 câu hỏi bằng văn bản.

### 2.2 Excel/Sheet nâng cao — chỉ phần cần (1.5h)
**80/20:** Pivot Table + `COUNTIFS`/`SUMIFS` + Conditional formatting để tự làm mini-report thay vì chờ dev build dashboard.
**Tài liệu miễn phí:** [ExcelJet Pivot Table guide](https://exceljet.net/pivot-tables).
**Bài tập:** Dùng Google Sheets (quyền có sẵn qua `gapi`) pivot data ticket 1 tháng theo CS + theo tag → tìm 1 pattern chưa từng để ý.

### 2.3 SQL cơ bản — chỉ SELECT/WHERE/GROUP BY (2h)
**Vì sao chỉ mức này:** Không cần viết production query, chỉ cần tự tra cứu BigQuery `crisp_chats` mà không phải nhờ dev.
**80/20:** `SELECT ... FROM ... WHERE ... GROUP BY ... ORDER BY ... LIMIT`. Dừng ở đây, không JOIN, không subquery.
**Tài liệu miễn phí:** [Mode Analytics SQL Tutorial](https://mode.com/sql-tutorial/) — sandbox chạy thử trên trình duyệt.
**Bài tập:** Viết tay (không nhờ AI) 1 query đếm số chat theo segment trong 1 tuần → so với report `/cs-weekly` để tự kiểm tra đúng/sai.

### 2.4 Phân tích issue bằng data thay vì cảm tính (1.5h)
**80/20:** Trước khi kết luận "nhiều merchant complain về X" — hỏi: mẫu bao nhiêu ticket, % trên tổng volume, so tuần trước tăng thật không hay chỉ do recency bias.
**Bài tập:** Chọn 1 "cảm giác" gần đây (VD: "dạo này Joy hay bị escalate hơn") → verify bằng `/api/obs/metrics` hoặc DFY tracker → kết luận đúng hay sai.

### Bảng tài liệu Tuần 2

| Nguồn | Loại | Chi phí | Ưu tiên |
|---|---|---|---|
| Mode Analytics SQL Tutorial | Interactive | Free | Học trước — có sandbox |
| ExcelJet Pivot Tables | Reference | Free | Tra cứu khi làm bài tập |
| Google Sheets (đã có quyền) | Tool | Free | Dùng ngay |

**Mini project cuối tuần:** Báo cáo 1 trang "Data-backed vs Gut-feel" — chọn 2 giả định tin là đúng về team/merchant, verify bằng data thật, ghi kết quả thật (kể cả khi sai).

---

## TUẦN 3 — Customer Success Core (Health, Churn, RCA, Consultant Mindset)

Tuần quan trọng nhất — phần "khó bị AI thay thế".

### 3.1 Customer Health Score (2h)
**Vì sao:** AI trả lời được ticket, nhưng không tự quyết định "merchant này sắp churn, cần can thiệp trước khi họ hỏi". Đó là việc của Liz.
**80/20:** Health score = Usage (login/tương tác feature chính) + Engagement (support ticket sentiment) + Value realization (đạt outcome mong đợi chưa) + Relationship (phản hồi outreach không). 4 tín hiệu, mỗi cái Red/Yellow/Green.
**Tài liệu miễn phí:** [Gainsight "Customer Health Score" guide](https://www.gainsight.com/guides/the-essential-guide-to-customer-health-scores/).
**Bài tập:** Áp dụng 4 tín hiệu cho 5 merchant Plus/Pro trong Chatty Proactive Care — chấm Red/Yellow/Green tay.

### 3.2 Churn & Retention (1.5h)
**80/20:** Phân biệt Churn dự đoán được (usage giảm dần, có warning signal) vs Churn bất ngờ (bug/billing/support tệ). Support ảnh hưởng trực tiếp loại 2 — đòn bẩy lớn nhất.
**Tài liệu miễn phí:** [ProfitWell Churn Rate guide](https://www.profitwell.com/recur/all/what-is-churn-rate).
**Bài tập:** Rà 3 case churn/downgrade gần nhất → phân loại predictable vs sudden → với sudden, hỏi "support có ngăn được không".

### 3.3 Root Cause Analysis — làm sâu hơn (2h)
**Vì sao:** Đã có project `joy_bot_escalate_kb_fixes` — chính là RCA thực chiến, làm hệ thống hơn.
**80/20:** 5 Whys + phân loại root cause thành 4 nhóm: Product bug / Product gap / KB gap / Process gap. Phân đúng nhóm quan trọng hơn tìm ra nguyên nhân — quyết định ai fix. Dùng thêm **Fishbone Diagram** khi 1 issue có nhiều nguyên nhân đan xen cùng lúc (VD: escalate rate tăng — có thể vừa do KB gap, vừa do process, vừa do bug — 5 Whys một đường thẳng không đủ, Fishbone giúp nhìn được nhiều nhánh nguyên nhân song song trước khi chốt root cause chính).
**Tài liệu miễn phí:** [Atlassian "5 Whys" guide](https://www.atlassian.com/team-playbook/plays/5-whys), [Atlassian "Fishbone/Ishikawa" guide](https://www.atlassian.com/team-playbook/plays/fishbone-ishikawa-diagram).
**Bài tập:** 3 ticket escalate tuần này → chạy 5 Whys → phân vào 1 trong 4 nhóm → nếu KB gap, patch qua `/kb-sync`. Với 1 case phức tạp nhất (nhiều nguyên nhân), thử vẽ Fishbone để so sánh.

### 3.4 Consultant Mindset & Upsell tự nhiên (1.5h)
**Vì sao:** Bước chuyển từ "người trả lời câu hỏi" sang "người tư vấn giải pháp". Upsell không phải bán hàng — là nhận ra khi merchant đang dùng sai/thiếu công cụ.
**80/20:** "Merchant nói X (triệu chứng) → hỏi Y (mục tiêu thật) → đề xuất Z (giải pháp, không nhất thiết trả phí)". Không recommend nếu không đúng nhu cầu — tin cậy quan trọng hơn 1 lần upsell.
**Tài liệu miễn phí:** [Winning by Design — "Bowtie model"](https://winningbydesign.com/resources/).
**Book:** *The Mom Test* — Rob Fitzgerald (thực ra tác giả là Rob Fitzpatrick) — cách hỏi khách để lộ ra nhu cầu thật thay vì câu trả lời lịch sự vô nghĩa. Đọc nhanh (~2-3h), áp dụng trực tiếp vào câu hỏi Y ở trên.
**Bài tập:** Trong 5 chat gần nhất, tìm 1 case merchant hỏi A nhưng thực ra cần B → viết cách nên hỏi để lộ "goal thật".

### Bảng tài liệu Tuần 3

| Nguồn | Loại | Chi phí | Ưu tiên |
|---|---|---|---|
| Gainsight Health Score guide | Guide | Free | Đọc trước |
| Atlassian 5 Whys | Guide | Free | Áp dụng ngay |
| Atlassian Fishbone/Ishikawa guide | Guide | Free | Dùng cho case phức tạp |
| ProfitWell Churn guide | Blog | Free | Đọc bổ trợ |
| Winning by Design Bowtie model | Framework | Free | Nên đọc |
| Book: *The Mom Test* — Rob Fitzpatrick | Book | ~$15 | ⭐ Đáng đọc trong tháng này — ngắn, sát với 3.4 |
| Book: "Customer Success" — Nick Mehta, Dan Steinman, Lincoln Murphy | Book | ~$20-30 | Không bắt buộc tháng này — để tháng 2 |

**Mini project cuối tuần:** Health Score sheet cho 10 merchant Plus/Pro (Red/Yellow/Green, 4 tín hiệu) — dùng làm input cho Chatty Proactive Care.

---

## TUẦN 4 — AI Collaboration + Leadership (áp dụng vào vận hành team)

### 4.1 AI Workflow cho CS — thực chiến (2h)
**Vì sao:** Đã có hạ tầng AI mạnh (Betty, Joyce, Ivy, `/kb-sync`, `/qa-weekly`...) — tuần này hệ thống hóa tư duy "task nào giao AI, task nào giữ người".
**80/20:** AI làm tốt: summarize, classify, draft, tìm pattern trong data lớn. Người làm tốt: quyết định (judgment call), xây quan hệ, xử lý cảm xúc merchant giận dữ, đánh giá đúng-sai output AI.
**Bài tập:** Liệt kê 10 task team đang làm tay → đánh dấu cái nào giao được AI (draft reply, summarize ticket, RCA nháp) vs bắt buộc người (quyết định refund, VIP call).

### 4.2 SOP Generation & RCA Generation bằng AI (1.5h)
**80/20:** Không phải "AI viết SOP hộ" mà "outline người + AI mở rộng + người review". Pattern: 3-5 case thật → AI tìm pattern chung → verify → chốt SOP.
**Bài tập:** Lấy 5 case escalate cùng loại tuần này → yêu cầu Betty/Claude generate SOP nháp → sửa lại → publish vào `kb/cs-process/`.

### 4.3 Coaching CS theo hướng Customer Success (1.5h)
**Vì sao:** Coaching hiện tại (`/qa-weekly`) theo "trả lời đúng KB chưa" — thêm trục "có hiểu business context merchant không".
**80/20:** Thêm câu hỏi coaching thứ 4 bên cạnh Mindset/Knowledge/Skill: "CS này có nhận ra lifecycle stage / health signal của merchant trong ca này không?"
**Bài tập:** Áp dụng câu hỏi này vào 3 case QA tuần này (dùng `/qa-weekly` sẵn có).

### 4.4 Đo chất lượng AI vs Human + Đề xuất cải tiến sản phẩm từ ticket (2h)
**80/20:** Đã có `/api/obs/metrics` (verify/correction rate) — thiếu quy trình định kỳ tổng hợp "top 3 pattern lỗi AI" → chuyển thành feature request cho product, không chỉ patch KB. Đây là bước "Business Partner" thật — đóng góp roadmap, không chỉ support.
**Bài tập:** Từ data bot-corrections tuần gần nhất → chọn 1 pattern lặp nhiều nhất → viết 1 feature request ngắn (format JTBD Tuần 1) gửi PM.

**Book:** *The Trusted Advisor* — David H. Maister, Charles H. Green, Robert M. Galford. Sát nhất với toàn bộ mạch chuyển đổi roadmap: từ "support trả lời đúng" sang "được merchant tin tưởng như consultant". Đọc trong tuần 4 để tổng kết mindset, không cần đọc hết — tập trung phần "Trust Equation".

### Bảng tài liệu Tuần 4

| Nguồn | Loại | Chi phí | Ưu tiên |
|---|---|---|---|
| Hạ tầng sẵn có trong CSL (`/kb-sync`, `/qa-weekly`, `/api/obs/metrics`) | Tool | Đã có | Dùng trực tiếp |
| Book: *The Trusted Advisor* — Maister, Green, Galford | Book | ~$15-20 | ⭐ Đáng đọc — tổng kết mindset cả tháng |

**Mini project cuối tuần (= mini project tổng kết cả tháng):** "CS → Customer Success Transformation Brief" gửi anh Sam — gồm: Health Score framework đã build, 1 SOP mới từ AI-assisted RCA, 1 feature request rút ra từ correction data, đề xuất thêm trục coaching thứ 4.

---

## Tổng kết kết quả sau 1 tháng

| Mục tiêu ban đầu | Đạt được qua |
|---|---|
| Phân tích merchant dưới góc nhìn business | Tuần 1 (lifecycle, metrics) + Tuần 3 (Health Score) |
| Đọc/giải thích metric merchant | Tuần 1.4 + Tuần 2 |
| RCA tốt hơn | Tuần 3.3 (5 Whys + phân loại 4 nhóm + Fishbone cho case phức tạp), áp dụng trực tiếp vào `joy_bot_escalate_kb_fixes` |
| Thiết kế AI workflow cho team | Tuần 4.1-4.2 |
| Coaching theo Customer Success | Tuần 4.3, tích hợp vào `/qa-weekly` |
| Consultant mindset (hỏi đúng, được tin tưởng) | Tuần 3.4 (*The Mom Test*) + Tuần 4 (*The Trusted Advisor*) |
| Nền tảng CSM/AM | Toàn bộ — nhưng là *nền*, không phải đủ. Roadmap tháng 2 nên đào sâu SQL + đọc book "Customer Success" (Dan Steinman, gợi ý Tuần 3) |

**Đọc song song cả tháng:** Lenny's Newsletter, 15 phút/ngày.
