# Joy Loyalty — CS Onboarding Plan (8-10 tuần)

> **Phạm vi:** Training toàn diện CS mới cho Joy Loyalty — Shopify nền tảng, company/CS team, học app Joy, CS process, đọc chat thật, mock chat, đến go-live độc lập.
> **Thời lượng:** 9 tuần (chuẩn) — co giãn 8-10 tuần tùy tốc độ trainee. Gợi ý co/giãn ghi ở cuối mỗi tuần liên quan.
> **Cách dùng:** Mỗi tuần có To-do (task cụ thể) → Test cuối tuần → Checklist follow-up (Liz/mentor tick trực tiếp vào bảng).

---

## TUẦN 1 — Shopify 101 + Company & CS team

**Mục tiêu:** hiểu Shopify vận hành thế nào (để hiểu app Joy ngồi ở đâu trong hệ sinh thái), biết mình đang làm cho ai, làm với ai, theo quy tắc nào.

**To-do:**
- [ ] Tạo dev store Shopify riêng (free trial), tự cài 1 theme, thêm 3-5 sản phẩm test
- [ ] Đọc Shopify Admin cơ bản: Products, Orders, Customers, Discounts, Apps, Theme editor
- [ ] Tìm hiểu khái niệm: Shopify Plan, Checkout, App Store, App embeds
- [ ] Đọc `_identity/who-we-are.md`, `values.md`, `tone-and-voice.md`
- [ ] Đọc `_identity/responsibilities.md`, `_identity/team-g2.md` — biết ai làm gì trong team
- [ ] Đọc quy trình CS team (doc Liz đính kèm)
- [ ] 1-1 giới thiệu với mentor/Liz — hỏi bất kỳ câu gì về công ty, sản phẩm, kỳ vọng vai trò

**Test cuối tuần (30 phút, mentor hỏi miệng):**
- Giải thích được Shopify Admin có gì, App hoạt động trong store merchant ra sao (không cần sâu, chỉ cần đúng khái niệm)
- Kể được cấu trúc team G2, ai là escalation point, quy trình báo cáo khi gặp vấn đề
- Nói được tone & voice công ty áp dụng khi chat với khách

**Checklist theo dõi:**

| Hạng mục | Hoàn thành | Ghi chú | Mentor ký |
|---|---|---|---|
| Dev store Shopify sẵn sàng | | | |
| Đọc xong _identity/* | | | |
| Đọc xong quy trình CS team | | | |
| Test cuối tuần pass | | | |

---

## TUẦN 2-3 — Learn Joy (product, có test)

**Dùng nguyên plan chi tiết đã có:** [`playbooks/joy-new-cs-app-training-2weeks.md`](joy-new-cs-app-training-2weeks.md) — 10 ngày × 4h, mỗi ngày có To-do (Đọc/Thực hành/Case) + Checklist thoát ngày sẵn. Không lặp lại nội dung ở đây, chỉ theo dõi tiến độ bằng bảng dưới.

**Test:**
- Mini test cuối ngày 5 (tuần 2): 5 câu hỏi merchant thật, trả lời bằng lời + chỉ đúng path trong admin
- Final test ngày 10 (tuần 3): build store hoàn chỉnh từ đầu (3h) + 10 câu hỏi + 3 ca troubleshoot — **Pass = ≥8/10 câu đúng + cả 3 ca troubleshoot đúng thứ tự check**

**Checklist theo dõi:**

| Ngày | Chủ đề | Checklist thoát ngày pass | Mentor ký |
|---|---|---|---|
| 1 | Tổng quan + Pricing | | |
| 2 | Earning | | |
| 3 | Redeeming | | |
| 4 | Loyalty page + Widget | | |
| 5 | VIP + Milestone + Referral | | |
| — | **Mini test tuần 2** | | |
| 6 | Customers + Migration | | |
| 7 | Notifications + Email | | |
| 8 | Integrations + POS + AI | | |
| 9 | Settings + Analytics | | |
| 10 | **Final test** | | |

> Nếu trainee đã có kinh nghiệm CS app loyalty khác → có thể rút xuống 8-9 ngày, gộp ngày 6+9.

**Checklist setup thực hành bắt buộc (Ngày 4 — không chỉ đọc lý thuyết, phải tự tay dựng trên dev store):**

Đây là nhóm ticket nhiều nhất merchant hỏi ("widget không hiện", "sao trang loyalty của em trống") — CS phải tự setup được, không chỉ giải thích được.

| Hạng mục setup | Hoàn thành | Link/screenshot dev store | Mentor ký |
|---|---|---|---|
| Loyalty page — build qua Theme Editor → Add section → Joy Loyalty | | | |
| Widget — bật qua App embeds, chỉnh vị trí/màu/trigger | | | |
| Widget — tắt app embed rồi tự bật lại (test hiểu nguyên nhân "widget mất") | | | |
| Onsite content — product page (hiển thị điểm/reward trên trang sản phẩm) | | | |
| Onsite content — cart drawer | | | |
| Onsite content — thank-you page | | | |
| Account page — hiển thị điểm/tier/lịch sử cho khách | | | |
| Custom point label (Settings → General) — đổi và xem đổi đúng chỗ trên storefront | | | |
| Phân biệt được: theme cũ (Asset/Additional scripts) vs theme OS 2.0 (App embeds) — setup có khác nhau | | | |

**Test riêng cho phần setup (gộp vào final test ngày 10):** trainee dựng lại toàn bộ loyalty page + widget + 4 loại onsite content trên dev store **mới, từ đầu, tính giờ** — không xem lại hướng dẫn cũ.

---

## TUẦN 4 — Joy CS process riêng

**Mục tiêu:** biết xử lý ticket/chat theo đúng quy trình công ty, không chỉ biết app.

**To-do:**
- [ ] Đọc `kb/cs-process/joy-support-flow.md` — flow tra cứu khi khách báo lỗi
- [ ] Đọc `playbooks/joy-onboarding-flow.md` — flow onboarding khách mới (offer → discovery → ticket → nhánh A/B/C)
- [ ] Đọc `playbooks/joy-dfu-onboarding-playbook.md` Phần 3 — lướt qua 50 case theo 8 domain (chưa cần thuộc, chỉ cần biết cấu trúc: Dấu hiệu → Tự chẩn đoán → Xử lý → Khi nào escalate)
- [ ] Đọc `shared-cs-process/escalation-matrix.md`, `case-classification.md`, `first-response.md`, `follow-up.md`
- [ ] Đọc `shared-cs-process/handle-billing-refund.md`, `handle-complaints.md`, `handle-sensitive-situations.md`
- [ ] Tự phân loại thử 10 case mẫu (mentor đưa) theo đúng case-classification + escalation matrix
- [ ] Viết thử 1 escalation note mẫu theo đúng format

**Test cuối tuần:**
- 10 case mẫu (tình huống mô tả, không phải chat thật) → trainee phân loại đúng mức độ + chỉ đúng bước xử lý/escalate theo matrix
- 1 case viết escalation note — mentor chấm đủ thông tin theo `escalation-note.md`

**Checklist theo dõi:**

| Hạng mục | Hoàn thành | Ghi chú | Mentor ký |
|---|---|---|---|
| Đọc xong toàn bộ process docs | | | |
| Phân loại 10 case mẫu (điểm/10) | | | |
| Escalation note đạt chuẩn | | | |
| Test cuối tuần pass | | | |

---

## TUẦN 5 — Đọc Crisp + luyện case thật

**Mục tiêu:** đọc hiểu context 1 cuộc chat thật trên Crisp, tra đúng case trong 50 case FAQ.

**To-do:**
- [ ] Đọc `skills/read-crisp/SKILL.md` — cách đọc/tóm tắt 1 session Crisp
- [ ] Mentor gửi 10 link chat Crisp thật (đã xử lý xong) → trainee tự đọc, tóm tắt lại vấn đề + cách CS cũ xử lý, KHÔNG xem trước đáp án
- [ ] Với mỗi case, tự tra ngược trong 50 case (Phần 3 playbook) xem case đó rơi vào domain nào, đúng lăng kính 🟢🔵🟠🔴 nào
- [ ] Ghi lại 5 case mình thấy khó nhất → hỏi mentor

**Test cuối tuần:**
- Mentor đưa 5 link Crisp mới (trainee chưa từng xem) → trainee đọc, tóm tắt đúng vấn đề, xác định đúng domain + lăng kính, đề xuất hướng xử lý — chấm bằng lời với mentor

**Checklist theo dõi:**

| Hạng mục | Hoàn thành | Ghi chú | Mentor ký |
|---|---|---|---|
| 10 case thật đã đọc + tóm tắt | | | |
| Tra đúng domain/lăng kính (điểm/10) | | | |
| Test cuối tuần (điểm/5) | | | |

---

## TUẦN 6 — Mock chat

**Mục tiêu:** phản xạ trả lời real-time, chưa để khách thật rủi ro.

**To-do:**
- [ ] Mentor/CS senior đóng vai khách hàng, dựng lại 8-10 case thật (lấy từ Crisp tuần gần nhất, đa dạng độ khó) → trainee trả lời live qua chat/Slack giả lập
- [ ] Bắt buộc có ít nhất 3 ca troubleshoot khó: widget không hiện / điểm không cộng / referral không chạy
- [ ] Bắt buộc có 1 ca khách hàng gắt/complaint để luyện tone xử lý sensitive situation
- [ ] Bắt buộc có 1 ca cần escalate — trainee phải nhận ra và viết escalation note đúng lúc
- [ ] Sau mỗi ca, mentor feedback ngay (đúng/sai, thiếu gì, tone ổn không)

**Test cuối tuần:**
- 2 ca mock chat hoàn toàn mới (trainee không biết trước kịch bản), mentor chấm theo rubric: đúng vấn đề / đúng xử lý / đúng tone / đúng quyết định escalate hay không — **Pass = cả 2 ca đạt ≥ mức "đạt yêu cầu" trên rubric**

**Checklist theo dõi:**

| Hạng mục | Hoàn thành | Ghi chú | Mentor ký |
|---|---|---|---|
| 8-10 ca mock đã chạy | | | |
| Ca troubleshoot khó (3 ca) | | | |
| Ca complaint/sensitive | | | |
| Ca escalate đúng lúc | | | |
| Test cuối tuần pass | | | |

---

## TUẦN 7 — Shadow + supervised live chat

**Mục tiêu:** tiếp xúc chat thật, có người đỡ ngay bên cạnh.

**To-do:**
- [ ] 2 ngày đầu: ngồi shadow CS senior xử lý chat thật, ghi chú lại cách xử lý/cách hỏi khách
- [ ] 3 ngày sau: tự trả lời chat thật, nhưng **mentor duyệt nội dung trước khi gửi** cho khách
- [ ] Cuối mỗi ngày, mentor review nhanh 15 phút: hôm nay có gì làm tốt, có gì cần sửa

**Test cuối tuần:** không có bài test riêng — đánh giá bằng số lượng chat xử lý đúng/tổng số chat trong tuần (mentor track)

**Checklist theo dõi:**

| Ngày | Số chat xử lý | Số chat cần sửa trước gửi | Vấn đề lặp lại | Mentor ký |
|---|---|---|---|---|
| 1-2 (shadow) | | | | |
| 3 | | | | |
| 4 | | | | |
| 5 | | | | |

---

## TUẦN 8 — Solo có giám sát

**Mục tiêu:** tự chạy độc lập, mentor review sau (không chặn trước) để đo phản xạ thật.

**To-do:**
- [ ] Tự xử lý chat/ticket thật cả tuần, không cần duyệt trước
- [ ] Mentor review lại toàn bộ chat trong ngày (sau giờ), chấm theo `playbooks/qa-weekly-rubric.md` (Mindset/Knowledge/Skill)
- [ ] Feedback 1-1 mỗi cuối ngày hoặc cách ngày, tùy khối lượng lỗi phát sinh

**Test cuối tuần:**
- Tổng hợp điểm QA rubric cả tuần — **Pass = điểm QA trung bình đạt mức chuẩn CS chính thức** (theo `qa-policy.md`)

**Checklist theo dõi:**

| Hạng mục | Hoàn thành | Điểm QA trung bình | Ghi chú | Mentor ký |
|---|---|---|---|---|
| Số chat/ticket xử lý trong tuần | | | | |
| Lỗi lặp lại cần train thêm | | | | |
| Đạt chuẩn QA rubric | | | | |

---

## TUẦN 9 — Final assessment + go-live

**Mục tiêu:** chốt go/no-go cho làm việc độc lập chính thức.

**To-do:**
- [ ] Ôn lại các điểm yếu đã note từ tuần 1-8
- [ ] Review lại 50 case FAQ (Phần 3) lần cuối — tập trung domain còn yếu

**Test cuối tuần (final, mentor + Liz cùng chấm):**
- Bài test tổng hợp: 10 câu hỏi product (như final test Learn Joy) + 5 case phân loại/escalate + 3 ca mock chat troubleshoot mới
- Review toàn bộ QA score 2 tuần live (tuần 7-8)
- **Pass = đạt đủ 3 điều kiện trên** → go-live độc lập chính thức. Không đạt → gia hạn thêm 1 tuần vào đúng module còn yếu (không lặp lại toàn bộ plan).

**Checklist theo dõi:**

| Hạng mục | Đạt | Ghi chú | Ký duyệt go-live (Liz) |
|---|---|---|---|
| Test product (điểm/10) | | | |
| Test process/escalate (điểm/5) | | | |
| Mock chat troubleshoot (3 ca) | | | |
| QA score tuần 7-8 đạt chuẩn | | | |
| **Quyết định go-live** | | | |

---

## Ghi chú co giãn 8-10 tuần

- **Rút còn 8 tuần:** gộp tuần 7+8 (shadow → solo giám sát trong cùng 1 tuần) nếu trainee đã có kinh nghiệm CS chat trước đó.
- **Giãn thành 10 tuần:** tách tuần 9 (final assessment) thành 2 tuần nếu QA tuần 8 chưa đạt chuẩn — thêm 1 tuần "solo có giám sát" nữa trước khi test final.
- Tiêu chí pass/fail mock chat (tuần 6) và final assessment (tuần 9) hiện dùng khung `qa-weekly-rubric.md` — nếu Liz muốn tiêu chí riêng cho onboarding (khác QA định kỳ), báo để mình tách riêng.
