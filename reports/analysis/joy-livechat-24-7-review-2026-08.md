# Joy Live Chat 24/7 — Review nhu cầu thực tế (20/07–20/08/2026)

> **Kết luận nhanh**: dữ liệu 1 tháng **không ủng hộ bỏ 24/7** — ngoài khung 08:00–17:59
> (58.8% volume) còn **41.2% volume** nằm ở khung tối 18:00–23:59 (22.1%) và đêm sâu
> 00:00–07:59 (19.1%), và ~75% traffic ở 2 khung này là merchant **US/EU đang trong giờ làm
> việc của họ** (69.8% tối, 80.3% đêm sâu) — nhu cầu timezone thật, không phải noise. Human
> vẫn đang xử một tỷ lệ đáng kể dù giảm dần theo đêm (78.9% giờ hành chính → 71.1% tối → 66.1%
> đêm sâu), không phải bot đã gánh gần hết. Plan thấp bot tự xử được nhiều hơn, nhưng **khung
> giờ yếu nhất khác nhau theo từng plan** — Starter yếu nhất ở khung tối, Essential/
> Essential+POS yếu nhất ở đêm sâu → nên phân tầng coverage theo plan × khung cụ thể, không
> phải một khung "off-hours" chung cho mọi tier.

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

*(plan lấy từ `dash_merchant_360.current_plan` join theo shopifyDomain, map qua bảng
`getLabelPlan()` — free→Starter, pro*→Essential, pro_4_*→Essential+POS, advanced*→Advanced,
enterprise*→Ultimate. 29 conv (3.2%) không match được domain vào dash → Unknown.)*

### Starter (177 conv, 19.5% total)

| Khung giờ | Conv | % Conv/Total | Human involved | Human % |
|---|---|---|---|---|
| 08:00–17:59 | 86 | 9.5% | 52 | 60.5% |
| 18:00–23:59 | 41 | 4.5% | 19 | 46.3% |
| 00:00–07:59 | 50 | 5.5% | 32 | 64.0% |

### Essential (234 conv, 25.7% total)

| Khung giờ | Conv | % Conv/Total | Human involved | Human % |
|---|---|---|---|---|
| 08:00–17:59 | 144 | 15.8% | 105 | 72.9% |
| 18:00–23:59 | 47 | 5.2% | 31 | 66.0% |
| 00:00–07:59 | 43 | 4.7% | 21 | 48.8% |

### Essential+POS (24 conv, 2.6% total)

| Khung giờ | Conv | % Conv/Total | Human involved | Human % |
|---|---|---|---|---|
| 08:00–17:59 | 5 | 0.5% | 4 | 80.0% |
| 18:00–23:59 | 12 | 1.3% | 8 | 66.7% |
| 00:00–07:59 | 7 | 0.8% | 3 | 42.9% |

### Advanced (377 conv, 41.4% total)

| Khung giờ | Conv | % Conv/Total | Human involved | Human % |
|---|---|---|---|---|
| 08:00–17:59 | 238 | 26.2% | 209 | 87.8% |
| 18:00–23:59 | 80 | 8.8% | 67 | 83.8% |
| 00:00–07:59 | 59 | 6.5% | 46 | 78.0% |

### Ultimate (69 conv, 7.6% total)

| Khung giờ | Conv | % Conv/Total | Human involved | Human % |
|---|---|---|---|---|
| 08:00–17:59 | 44 | 4.8% | 41 | 93.2% |
| 18:00–23:59 | 15 | 1.6% | 12 | 80.0% |
| 00:00–07:59 | 10 | 1.1% | 8 | 80.0% |

### Summary — so sánh 5 plan theo khung giờ

| Plan | Total conv | % Total | % 08:00–17:59 | % 18:00–23:59 | % 00:00–07:59 |
|---|---|---|---|---|---|
| Starter | 177 | 19.5% | 48.6% | 23.2% | 28.2% |
| Essential | 234 | 25.7% | 61.5% | 20.1% | 18.4% |
| Essential+POS | 24 | 2.6% | 20.8% | 50.0% | 29.2% |
| Advanced | 377 | 41.4% | 63.1% | 21.2% | 15.6% |
| Ultimate | 69 | 7.6% | 63.8% | 21.7% | 14.5% |

**Đọc:** Advanced/Ultimate/Essential đều tập trung ~62–64% conv vào khung 08:00–17:59, phần
còn lại chia khá đều cho tối và đêm. Starter lệch khác — chỉ 48.6% rơi vào giờ hành chính,
tới 51.4% nằm ngoài 08:00–17:59 (tối 23.2% + đêm 28.2%), tỷ trọng off-hours cao nhất trong 5
plan. Essential+POS lệch mạnh nhất về khung tối (50.0% conv rơi vào 18:00–23:59) — khác hẳn
pattern của các plan còn lại, dù sample nhỏ (24 conv) nên chỉ mang tính tham khảo.

### Bảng tổng hợp — Conv thực tế theo Plan × Khung giờ (toàn bộ 910 conv)

| Plan | 08:00–17:59 | 18:00–23:59 | 00:00–07:59 | Tổng | % Tổng |
|---|---|---|---|---|---|
| Starter | 86 | 41 | 50 | 177 | 19.5% |
| Essential | 144 | 47 | 43 | 234 | 25.7% |
| Essential+POS | 5 | 12 | 7 | 24 | 2.6% |
| Advanced | 238 | 80 | 59 | 377 | 41.4% |
| Ultimate | 44 | 15 | 10 | 69 | 7.6% |
| Unknown/no-plan-data | 18 | 6 | 5 | 29 | 3.2% |
| **Tổng** | **535** | **201** | **174** | **910** | **100%** |

**Đọc nhanh:** khung 08:00–17:59 chiếm 58.8% tổng volume, và riêng Advanced đã chiếm
238/535 ≈ 44.5% conv của khung này — plan cao tập trung vào giờ hành chính nhiều nhất về số
tuyệt đối, dù không lệch nhất về tỷ trọng (xem bảng % ở trên, Starter mới là plan lệch tỷ
trọng off-hours cao nhất). Nói cách khác: **Advanced quyết định tổng khối lượng ban ngày**,
còn **Starter quyết định phần lớn "hình dạng" off-hours** dù volume tuyệt đối nhỏ hơn nhiều.

## 3. Merchant ở khung nào? (geolocation)

*(Geo lấy từ `rawConversation.meta.device.geolocation.country` trong Crisp, theo session đầu
mỗi conversation. 904/910 conv có geo data.)*

| Khung giờ | Conv có geo | US/EU | APAC | Other |
|---|---|---|---|---|
| 08:00–17:59 | 532 | 226 (42.5%) | 284 (53.4%) | 22 (4.1%) |
| 18:00–23:59 | 199 | 139 (69.8%) | 39 (19.6%) | 21 (10.6%) |
| 00:00–07:59 | 173 | 139 (80.3%) | 28 (16.2%) | 6 (3.5%) |

Top country mỗi khung:
- **08:00–17:59**: US 83, SG 49, HK 36, MY 36, DE 34, IN 34, TW 30, JP 30, FR 22, GB 21 — mix APAC rõ, đúng giờ hành chính chung của khu vực.
- **18:00–23:59**: US 40, FR 23, GB 15, DE 14, IT 11, CA 9, NL 9, IN 8, VN 7, MY 7.
- **00:00–07:59**: US 88, CA 14, HU 9, FR 6, SG 6, GB 5, PK 5, DE 4, PH 4, VN 3.

**Đọc:** càng về đêm theo giờ Bangkok, tỷ trọng US/EU càng tăng đều (42.5% → 69.8% → 80.3%),
và khung 00:00–07:59 gần như là **giờ làm việc ban ngày của merchant US** (US một mình chiếm
88/173 ≈ 51% conv có geo trong khung này). Khung 08:00–17:59 vẫn là khung đa dạng nhất
(APAC 53%, US/EU 42.5%) vì đây là giờ hành chính chung của cả khu vực lẫn phần đầu ngày làm
việc châu Âu. Nhu cầu đêm sâu không phải noise lẻ tẻ — nó là timezone thật của một nhóm
merchant cụ thể (US), càng về khuya càng rõ.

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

1. **Rào cản lớn nhất trước đây (Advanced/Ultimate) đã được gỡ bởi cấu trúc AM** — 2 tier
   này giữ human% 78–93% ở cả 3 khung giờ (49% volume tháng, chủ yếu hỏi redemption/points/
   data issue bot chưa xử được), nhưng vì đã có AM follow-up riêng nên không cần live-chat
   24/7 để đỡ nhóm này nữa. Điều kiện để bỏ hẳn 24/7 giờ phụ thuộc vào **Starter/Essential**
   (đội bot chính) chứ không còn phụ thuộc Advanced/Ultimate.

2. **Khung giờ yếu nhất khác nhau theo từng plan** — đây là phần bot sẽ phải gánh 100% khi bỏ
   hẳn human:
   - **Starter**: yếu nhất là khung **tối** 18:00–23:59 (human% 46.3%, thấp nhất toàn bộ dữ
     liệu) — không phải đêm sâu như giả định ban đầu.
   - **Essential / Essential+POS**: yếu nhất là khung **đêm sâu** 00:00–07:59 (human% 48.8% /
     42.9%).
   - → Nên cải thiện bot + thiết kế fallback riêng theo đúng khung yếu của từng plan (Starter
     ở khung tối, Essential ở khung đêm sâu) trước khi bỏ hẳn.

3. **2 việc cần chốt trước khi bỏ hẳn 24/7:**
   - **Fallback mechanism** cho chat Starter/Essential ngoài giờ mà bot không xử được — tạo
     ticket tự động + SLA trả lời ca sáng, có auto-reply set kỳ vọng cho merchant hay không.
   - **Escalation path cho case khẩn ban đêm** (VD case billing/finance-chasing như quote ở
     §4) — cần rule tách riêng khỏi ticket thường, route cho AM/CS xử lý sáng hôm sau thay vì
     nằm chờ như ticket thường.
   - Đồng thời xác nhận AM có đủ băng thông đón hết lượng phát sinh ngoài giờ của 446
     conv/tháng (Advanced/Ultimate) mà không làm chậm phản hồi so với live-chat hiện tại.

4. **Billing/plan question ở Starter (11.4%, cao hơn hẳn tier khác)** — đáng tách riêng theo
   dõi, có thể là tín hiệu upsell hoặc churn tùy cách trả lời; không trực tiếp liên quan đến
   quyết định coverage nhưng đáng note lại cho CS follow-up.

5. **Bước tiếp theo nếu muốn quyết định dứt khoát**: pilot "bot + ticket fallback" riêng cho
   Starter ở khung 18:00–23:59 và Essential ở khung 00:00–07:59 (2 khung yếu nhất của mỗi
   plan, 41 và 43 conv/tháng — rủi ro thấp vì volume nhỏ), đo lại human-takeover% và
   review/churn của nhóm được thử; song song theo dõi AM có kịp đỡ lượng Advanced/Ultimate
   ngoài giờ không, trước khi tuyên bố bỏ hẳn 24/7.
