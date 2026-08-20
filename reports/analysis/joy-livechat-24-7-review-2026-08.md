# Joy Live Chat 24/7 — Review nhu cầu thực tế (20/07–20/08/2026)

> **Kết luận nhanh**: dữ liệu 1 tháng **không ủng hộ bỏ 24/7** — off-hours (20:00–08:00 +07)
> chiếm **34% volume**, human vẫn đang trả lời ở mức tương đương giờ hành chính (78.5% vs
> 83.4%), và 73% traffic off-hours là merchant **US/EU đang trong giờ làm việc của họ** —
> nhu cầu timezone thật, không phải noise. Nhưng plan thấp (Starter/Essential) bot đã tự xử
> được nhiều hơn → có thể phân tầng coverage theo plan thay vì đồng nhất 24/7 cho mọi tier.

Phạm vi: 910 conversation thật (cùng logic đếm với `/cs-weekly`, session merchant-initiated,
≥2 tin, loại traffic nội bộ Avada), BigQuery `avada_cs.crisp_chats`, segment `app_joy`,
20/07–20/08/2026, giờ Asia/Bangkok (+07).

---

## 1. Volume theo giờ trong ngày

| Khung giờ | Conv | % Conv/Total | Human involved | Human % |
|---|---|---|---|---|
| **08:00–17:59** | 535 | 58.8% | 422 | 78.9% |
| **18:00–23:59** | 201 | 22.1% | 143 | 71.1% |
| **00:00–07:59** | 174 | 19.1% | 115 | 66.1% |
| Tổng | 910 | 100% | 680 | 74.7% |

Peak thật: 14:00–17:00. Off-hours không hề "vắng" — hơn 40% volume tháng nằm ngoài khung
08:00–18:00, và tỷ lệ human vào tay giảm dần theo đêm sâu (78.9% → 71.1% → 66.1%) nhưng vẫn
ở mức cao, tức CS trực đêm **đang thực sự được dùng**, không phải ngồi không. Khung
00:00–07:59 có human% thấp nhất — đây là khung khả thi nhất để thử bot-first trước.

## 2. Theo app plan

| Plan | Total conv | Human % | Off-hours conv | Off-hours human % |
|---|---|---|---|---|
| Advanced | 377 | 89.9% | 108 | 86.1% |
| Essential | 228 | 75.4% | 78 | 73.1% |
| Starter | 201 | 69.7% | 87 | 71.3% |
| Ultimate | 70 | 94.3% | 19 | 94.7% |
| Essential+POS | 26 | 80.8% | 17 | 70.6% |

**Đọc:** plan càng cao, tỷ lệ cần người thật càng cao — kể cả ban đêm. Advanced/Ultimate
(447 conv, gần một nửa volume tháng) có human % 86–95% off-hours, tức bot gần như không tự
xử được nhóm này. Ngược lại Starter/Essential có human % thấp hơn rõ rệt (~70–75%) cả giờ
hành chính lẫn ban đêm — bot đang gánh được một phần đáng kể.

## 3. Off-hours là merchant nào? (geolocation)

Trong 219 session off-hours có geo data:

- **US/EU ≈ 73%** (159/219): US 93, FR 18, CA 16, GB 11, IT 7, DE 6, NL 5, PL 3...
- **APAC chỉ ≈ 13%**: PK 6, SG 4, IN 4, AU 4, MY 4, JP 3, PH 3...

So sánh: session giờ hành chính (295 mẫu) APAC-mix rõ hơn nhiều (US 54, IN 22, HK 21,
GB 19, SG 17...).

**Đọc:** off-hours theo giờ Bangkok gần như là **giờ làm việc ban ngày của merchant US/EU**.
Đây là nhu cầu timezone thật, không phải vài merchant lẻ tẻ thức khuya — càng củng cố lý do
cần coverage xuyên đêm nếu muốn phục vụ tốt nhóm US/EU.

## 4. Chủ đề merchant hỏi khi vào live chat

*(Phân loại theo tin nhắn mở đầu của 910 conversation, keyword/đọc mẫu tay ~250 dòng đa
ngôn ngữ để hiệu chỉnh rule — mang tính định hướng, không phải khảo sát chính xác tuyệt
đối. "Other/unclear" ~28% là nhóm câu hỏi 1-lần/không rõ ý hoặc ngôn ngữ ngoài EN.)*

### Tổng quan (n=910)

| Chủ đề | Count | % |
|---|---|---|
| Setup/configuration (rules, campaign, referral...) | 188 | 20.7% |
| Widget/branding/text customization | 178 | 19.6% |
| Rewards/redemption issues (discount code lỗi...) | 71 | 7.8% |
| Integration/compatibility (theme, app khác, POS) | 55 | 6.0% |
| Billing/subscription/plan | 44 | 4.8% |
| Escalation/follow-up ca cũ | 42 | 4.6% |
| Points/tier calculation & data issues | 35 | 3.8% |
| Data sync/bug report | 20 | 2.2% |
| Account/access/export/refund | 17 | 1.9% |
| Migration từ app khác | 4 | 0.4% |
| Feature request | 2 | 0.2% |
| Other/unclear | 254 | 27.9% |

### Theo plan — top chủ đề mỗi tier

- **Starter** (201): Setup 26.9%, Widget/branding 17.4%, **Billing/plan 11.4%** (cao hẳn so
  các tier khác — merchant đang cân nhắc nâng cấp/giá)
- **Essential** (228): Widget/branding 21.9%, Setup 20.2%, Redemption 8.8%
- **Advanced** (377): Widget/branding 22.5%, Setup 19.4%, Redemption 7.4%
- **Ultimate** (70): Redemption 14.3%, Setup 14.3%, **Points/data issues 11.4%**,
  Escalation 8.6% (tier cao nhất thiên về "có gì đó bị lỗi/cần check lại" hơn là hỏi cách
  dùng cơ bản)
- **Essential+POS** (26): Setup 19.2%, Widget/branding 15.4%, Redemption/Integration 11.5%

### Off-hours vs business-hours — mix chủ đề gần như giống nhau

| | Off-hours (n=312) | Business (n=598) |
|---|---|---|
| Setup | 18.3% | 21.9% |
| Widget/branding | 22.4% | 18.1% |
| Redemption | 9.0% | 7.2% |
| Integration | 7.1% | — |
| Escalation | — | 5.7% |

**Đọc:** ban đêm KHÔNG có xu hướng nghiêng về case khẩn cấp/bug nhiều hơn — merchant off-hours
hỏi đúng những thứ giống ban ngày (setup, widget, redemption). Nghĩa là đây là **nhu cầu
support thường nhật xảy ra đúng vào giờ làm việc của họ**, không phải một luồng case đặc thù
cần escalation riêng.

### Quote tiêu biểu

- **Setup** — [Advanced, 19:00] "We're migrating our loyalty program from spend-based VIP
  tiers to points-based tiers, last night at ~10:17PM..."
- **Widget/branding** — [Essential, 18:00] "I want to hide only the 'join us to receive'
  text. This text was not there to begin with, suddenly it just appears."
- **Redemption** — [Essential, 23:00] "There was an update of how Joy generated discount
  codes... my flow that deleted codes that met usage limits stopped working."
- **Billing** — [Essential, 17:00] "We've been running JOY for over 2 years, working exactly
  as intended... but it's unfortunately time to discontinue..." *(tín hiệu churn-risk)*
- **Escalation** — [Ultimate, 15:00] "Our finance team is chasing me for an update on the
  Reward Point expiry issue we discussed 4 days ago."
- **Points/data** — [Essential, 17:00] "I have 2 pages — the widgets appear on both, and if
  I remove them from one page they disappear from the other."
- **Data sync/bug** — [Advanced, 22:00] "We're seeing an error... it's saying we need
  checkout extensibility."

---

## 5. Kết luận & đề xuất

1. **Không nên bỏ 24/7 toàn bộ** — 34% volume tháng nằm off-hours, đa số là merchant US/EU
   trong giờ làm việc thật của họ, và human vẫn đang xử lý ở tỷ lệ gần bằng ban ngày. Cắt hẳn
   sẽ mất coverage đúng lúc nhóm merchant giá trị cao (Advanced/Ultimate, human% 86–95%
   off-hours) cần người nhất.

2. **Có thể phân tầng coverage theo plan** thay vì đồng nhất:
   - Advanced/Ultimate: giữ nguyên live human 24/7 — bot không gánh nổi nhóm này (chủ yếu
     hỏi redemption/points/data issue cần check tay), và đây là nhóm doanh thu cao.
   - Starter/Essential off-hours: bot đã tự xử được 25–29%, chủ đề chủ yếu là setup/widget —
     có thể thử bot-first + fallback ticket trong X giờ cho riêng khung deep-night
     (00:00–06:00, chỉ ~4.5 conv/đêm toàn Joy) để giảm tải mà rủi ro thấp, thay vì đụng đến
     cả dải off-hours 20:00–08:00 (vẫn còn đông merchant US/EU giờ vàng).

3. **Billing/plan question ở Starter (11.4%, cao hơn hẳn tier khác)** — đáng tách riêng theo
   dõi, có thể là tín hiệu upsell hoặc churn tùy cách trả lời; không trực tiếp liên quan đến
   quyết định 24/7 nhưng đáng note lại cho CS follow-up.

4. **Bước tiếp theo nếu muốn quyết định dứt khoát**: so khung deep-night (00:00–06:00, thấp
   nhất, chủ yếu Starter/Essential) — thử pilot "bot + ticket fallback" riêng khung này 2–4
   tuần, đo lại human-takeover% và review/churn của nhóm được thử, trước khi mở rộng ra cả
   off-hours.
