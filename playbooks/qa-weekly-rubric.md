# QA Weekly Rubric — Chấm chat hàng tuần

**Mục đích:** Chấm chất lượng chat của từng CS mỗi tuần để **coaching**, không phải để phạt.
Khác với QA tháng (`qa-policy.md` — penalty, kỷ luật, CEO duyệt), rubric tuần này:

- Chỉ chấm những gì **quan sát được từ transcript chat**
- Cho điểm theo **% chất lượng trên mẫu**, không trừ điểm kiểu kỷ luật
- Có cả **điểm dương** (để khen) lẫn điểm cần cải thiện
- Output là **DM gửi riêng cho CS**, giọng phát triển — không phải bảng phạt

> QA tháng vẫn giữ nguyên là nguồn chính thức cho penalty & kỷ luật. Rubric tuần là công cụ coaching, chạy nhanh, nhẹ.

---

## 0. Phạm vi & giới hạn (đọc trước)

QA tuần này **chỉ nhìn thấy nội dung chat với khách hàng**. Nó **KHÔNG** đánh giá
được — và điểm tuần KHÔNG phản ánh — những phần sau:

- Phối hợp với **TS/dev**: tạo ticket, chất lượng ticket, follow-up đúng hạn
- **Bàn giao ca**, assign chat/card, cập nhật status nội bộ
- Việc **xử lý sau khi đóng chat** (card pending, update KH khi dev trả kết quả)
- **Xin review** thật sự, rating của KH, checkin/workshift
- Thái độ & teamwork ngoài kênh chat

→ Vì vậy điểm QA tuần là **một lát cắt coaching về kỹ năng chat**, không phải
đánh giá năng lực toàn diện. Một CS điểm chat cao vẫn có thể yếu ở ticket/handoff
và ngược lại. **Đánh giá toàn diện thuộc về QA tháng** (`qa-policy.md`, có đủ
data Trello/ticket/rating). Disclaimer này phải xuất hiện trong mọi DM gửi CS.

---

## 1. Sampling

- **30 session/CS/tuần** (Thứ 2 → Chủ Nhật)
- Nếu CS có >30 chat: random 30
- Nếu <30: lấy hết, ghi rõ số thực tế trong report
- Nguồn session: public CRM API (log chat theo ca) → group theo CS
- Transcript đầy đủ: BigQuery `crispchat_history` theo `session_id`

---

## 2. Tiêu chí chấm (chỉ những gì thấy được từ chat)

Mỗi chat được soi qua 2 nhóm: **lỗi cần cải thiện** (map về code QA tháng để nhất quán) và **điểm sáng** (để khen).

### A. Lỗi quan sát-được-từ-chat

Chỉ dùng các code mà transcript đủ bằng chứng. Bỏ qua mọi lỗi cần data ngoài chat
(workshift, checkin, Trello/ticket, review-system, rating, lưu data) — để QA tháng xử lý.

| Code | Lỗi | Mức | Soi cái gì trong chat |
|------|-----|-----|----------------------|
| QT5 | Thiếu thông tin cơ bản (URL, email, store) trước khi xử lý | Low | CS xử lý mà chưa thu thập đủ định danh shop |
| QT6 | Xin quyền không giải thích / không liệt kê đủ | Low | Lúc xin permission, có nói rõ xin gì + để làm gì không |
| QT7 | Xin quyền admin khi không cần | Moderate | Xin quyền rộng hơn mức vấn đề cần |
| QT8 | First response chậm (>2 phút) | Moderate | Khoảng cách timestamp tin đầu KH → tin đầu CS *(chỉ ghi nhận, xem mục 4)* |
| QT9 | Hỏi vòng vo, kéo dài hội thoại | Moderate | Hỏi thừa, không đi thẳng vấn đề |
| QT10 | Không theo flow xử lý của app (confirm URL, refund, downgrade…) | Moderate | So với flow trong `kb/cs-process/` |
| QT11 | Bỏ tin nhắn KH trong ca (không phản hồi) | Critical | KH nhắn, không có phản hồi nào của CS |
| QT12 | Thiếu minh bạch — không giải thích quá trình/nguyên nhân | Critical | Báo "đã xong" mà không nói làm gì/vì sao |
| QT18 | Kết thúc mà không báo KH bước tiếp theo | Moderate | Chat đóng lửng, KH không biết chờ gì |
| QT22 | Bỏ sót câu hỏi của KH | High | KH hỏi 2 ý, CS chỉ trả lời 1 |
| QT25 | Hẹn kiểm tra rồi im luôn | High | "Để em check rồi báo lại" → không quay lại |
| KT1 | Sai thông tin tính năng / giá / chính sách | Critical | **Đối chiếu KB agent** (xem mục Knowledge bên dưới) — claim của CS có khớp KB không |
| KT2 | Có FAQ/guide đầy đủ mà không dùng, support lòng vòng | Critical | Vấn đề đã có sẵn trong KB agent mà CS mò lại từ đầu / trả lời thiếu |
| KN1 | Sai ngữ pháp/chính tả, tin nhắn thiếu chuyên nghiệp | Low | Lỗi viết rõ rệt, ảnh hưởng hình ảnh |
| KN2 | Hỏi lại thứ KH đã cung cấp trong cùng chat | Moderate | CS hỏi cái KH nói rồi |
| KN3 | Hướng dẫn chưa rõ, KH khó hiểu | Moderate | KH phải hỏi lại "ý anh là sao" |
| KN5 | Hiểu sai vấn đề → tư vấn sai hướng | High | Giải pháp lệch với điều KH thật sự cần |
| KN6 | Chưa đủ thông tin đã kết luận | Moderate | Chốt vấn đề khi chưa hỏi đủ |
| KN7 | Trả lời chung chung, không giải quyết trực tiếp | Moderate | Câu trả lời mơ hồ, không có bước cụ thể |
| KN8 | Câu mất lịch sự, gây phản ứng tiêu cực | Urgent | Tone vô lễ/cộc lốc, KH phản ứng |

> KN8 / QT11 / KT1 nếu xuất hiện → **flag riêng cho Liz xem trước khi DM**, không tự gửi.

#### Kiểm tra kiến thức (KT1/KT2) — BẮT BUỘC đối chiếu KB agent

Khi chấm 2 lỗi kiến thức, **không dựa vào hiểu biết chung** — phải mở KB thật
mà con AI agent dùng để verify từng claim CS nói (giá, tính năng, giới hạn,
chính sách refund…):

- **Chatty KB:** `/Users/avada/claw-weebhook-crisp-chat/agents/chatty-agent/knowledge/`
- **Joy KB:** `/Users/avada/claw-weebhook-crisp-chat/agents/joy-loyalty-agent/knowledge/`
- **Index để tra nhanh file nào:** `skills/qa-weekly/references/kb-index.md`
  (mỗi file kèm "applies_when" → biết mở đúng file)

Cách làm: với mỗi chat, xác định app (Joy/Chatty theo segment) → nếu CS có
claim về kiến thức/giá/chính sách → tra index → **Read đúng 1–3 file KB liên
quan** → so claim với KB:
- Claim **trái** KB (sai giá, sai giới hạn, sai tính năng) → **KT1 (Critical)**, quote cả câu CS nói + dòng KB đúng.
- KB có sẵn câu trả lời rõ mà CS **lòng vòng / trả lời thiếu / bảo "không làm được"** trong khi KB nói được → **KT2 (Critical)**.
- Chỉ mở file KB khi chat có claim cần verify — **không đọc cả KB** (giữ nhẹ).
- Không tìm thấy file KB phù hợp / không chắc → **bỏ qua, không suy diễn**.

### B. Điểm sáng (để khen có cơ sở)

| Code | Điểm tốt | Nhận diện trong chat |
|------|----------|---------------------|
| P1 | Empathy tốt | KH bực/lo, CS giữ tone ấm, trấn an đúng lúc |
| P2 | Chủ động (proactive) | Đề xuất giải pháp/cảnh báo KH chưa kịp hỏi |
| P3 | Giải thích rõ ràng, có bước | Hướng dẫn từng bước, KH làm theo được ngay |
| P4 | Xử lý gọn, đúng flow | Đi thẳng vấn đề, đúng quy trình, không vòng vo |
| P5 | Đọc kỹ context | Nắm vấn đề từ đầu, không bắt KH lặp lại |

---

## 3. Cách tính điểm tuần (theo mẫu, không phải penalty)

Mỗi chat trong mẫu được xếp 1 trong 6 nhãn. **Mốc chuẩn của một chat xử lý
"đúng và đủ" là 90, KHÔNG phải 100.** Điểm 100 chỉ dành cho chat thật sự nổi
bật (có điểm sáng P1–P5 rõ rệt). Đã quote được lỗi thì chat đó không thể đạt
mốc chuẩn — phải tụt theo mức lỗi nặng nhất.

| Nhãn | Nghĩa | Điểm chat |
|------|-------|-----------|
| 🌟 **Xuất sắc** | Sạch lỗi **+ có điểm sáng P1–P5 rõ rệt** (empathy/proactive/giải thích xuất sắc) | 100 |
| ✅ **Đạt chuẩn** | Sạch lỗi, xử lý đúng & đủ nhưng không có gì nổi bật | 90 |
| 🟡 **Minor-Low** | Có lỗi **Low** (vd KN1, QT5/6) | 80 |
| 🟠 **Minor-Mod** | Có lỗi **Moderate** (vd KN2/3/6/7, QT18, QT9) | 70 |
| 🔴 **Major** | Có lỗi **High** (vd KN4/5, QT22/25) | 55 |
| ⛔ **Critical** | Có lỗi **Critical/Urgent** (vd QT11, KT1, KN8) | 30 |

> Một chat lấy điểm theo **lỗi nặng nhất** của nó. Nhiều lỗi cùng mức không trừ
> chồng (rubric tuần là coaching, không cộng dồn penalty như QA tháng).

**Điểm tuần = trung bình điểm các chat trong mẫu** (làm tròn). Chat không có
message nào của CS đang xét → loại khỏi mẫu, không tính.

> Tính trên % chất lượng của mẫu → so tuần-qua-tuần công bằng, không bị một chat
> tệ kéo cả tuần về 0 như cách trừ penalty.

**Phân loại tổng (đã siết — Xuất sắc thật sự khó đạt):**
- **95–100: Xuất sắc** 🌟
- **85–94: Tốt** 👍
- **75–84: Đạt** — cần cải thiện vài điểm
- **<75: Cần coaching 1-1** 🤝

---

## 4. Lưu ý khi chấm tự động

- **QT8 (FRT >2p):** chỉ **ghi nhận**, không tính vào điểm tuần — vì policy ghi "trừ point toàn bộ agent trong ca", khó gán cho 1 CS từ transcript. Để Liz tham khảo.
- **Cần bằng chứng mới ghi lỗi:** mỗi lỗi phải **quote được câu chat** làm dẫn chứng. Không suy diễn.
- **Không chắc thì bỏ qua**, không đoán — thà sót còn hơn ghi oan, vì report này gửi thẳng cho CS.
- **Lỗi cần data ngoài chat** (follow-up Trello, review, checkin…): KHÔNG chấm ở tuần. Nếu nghi ngờ, ghi 1 dòng "cần check thêm ngoài chat" cho Liz, không tính điểm.

---

## 5. Format report gửi CS (qua Slack DM)

**Tiêu đề bắt buộc ở đầu mỗi tin** — dòng đầu luôn là banner cố định để CS
nhận ra ngay và search lại được (search "QA TUẦN" trong Slack ra hết):

```
📋 *QA TUẦN — BÁO CÁO CỦA [Tên CS]*
🗓️ Tuần [W##] · [dd/mm – dd/mm]
━━━━━━━━━━━━━━━━━━━━━━━━━━━

📊 *Điểm tuần:* 86/100 — Tốt  (▲ +4 so với tuần trước)
🔍 Đã QA: 30 chat

✅ *Điểm tốt tuần này*
• Empathy tốt — giữ bình tĩnh khi KH bực về charge (chat #3, #17)
• Giải thích rõ ràng, có bước — KH làm theo được ngay (chat #8)

🔧 *Cần cải thiện*
• [KN5] Hiểu sai vấn đề ở chat #12 — KH hỏi về reward points, mình tư vấn nhầm sang membership
   → Lần sau confirm lại vấn đề trước khi tư vấn
• [QT18] 3 chat kết thúc mà chưa báo KH bước tiếp theo (#5, #14, #22)
   → Luôn chốt: "Em sẽ báo lại trong [x]" trước khi đóng

📈 *So với tuần trước*
• Điểm tăng từ 82 → 86 👏
• KN5 (tư vấn sai) giảm từ 4 → 1 chat — tiến bộ rõ
• QT18 (chốt bước tiếp theo) vẫn lặp lại — tuần này focus điểm này nhé

🔗 *Chat đã QA (24):*
<crisp_url|#1 Cuura Malaysia> · <crisp_url|#2 Nicholas Davies> · …

_📌 Lưu ý: Đánh giá này chỉ dựa trên *nội dung chat với khách*. Chưa bao gồm việc phối hợp với TS/dev, tạo & follow-up ticket, bàn giao ca, hay xin review — những phần đó nằm ngoài phạm vi chat. Đây là feedback để cải thiện, không phải đánh giá toàn diện._

_Tin tự động từ hệ thống QA của team CS 2. Có gì thắc mắc cứ nhắn lại Liz nhé 💬_
```

**Chat đã QA — bắt buộc hyperlink:** mỗi chat hiện **tên customer** (lấy
`customerNickname` từ BigQuery, fallback email → "Khách") và link thẳng vào
Crisp inbox theo cú pháp Slack `<url|text>`:
- URL: `https://app.crisp.chat/website/{website_id}/inbox/{session_id}`
- Số `#N` khớp số chat trong transcript (chat #N trong report = #N trong link)
- Nguồn data: file `*_index.json` do `fetch_transcripts.py` xuất ra

**Câu chốt cuối (cố định):**
`_Tin tự động từ hệ thống QA của team CS 2. Có gì thắc mắc cứ nhắn lại Liz nhé 💬_`

**Giọng điệu:** khích lệ, cụ thể, mỗi điểm cần cải thiện luôn kèm **1 gợi ý hành động**.
Khen trước, góp ý sau. Không dùng từ "phạt", "trừ điểm", "vi phạm".

---

## 6. So sánh tuần trước

- Đọc report tuần trước: `reports/qa-weekly/qa-weekly-[CS]-[YYYY-W##].md`
- So 3 thứ:
  1. **Delta điểm tổng** (tăng/giảm)
  2. **Lỗi lặp lại** — code nào xuất hiện cả 2 tuần → nhấn mạnh để CS focus
  3. **Lỗi đã khắc phục** — code tuần trước có, tuần này hết → khen
- Tuần đầu chưa có baseline → ghi "Tuần đầu, chưa có dữ liệu so sánh".

---

## 7. Lưu trữ

Mỗi tuần một folder riêng:

```
reports/qa-weekly/
└── qa-weekly-[YYYY-W##]/          ← vd qa-weekly-2026-W22/
    ├── qa-weekly-summary-[YYYY-W##].md   ← tổng hợp team (Liz duyệt)
    ├── qa-weekly-[CS]-[YYYY-W##].md      ← mỗi CS 1 file
    └── …
```

- Tên file giữ dạng dài (đủ nghĩa kể cả khi tách khỏi folder).
- So sánh tuần trước: đọc folder `qa-weekly-[YYYY-W(##-1)]/`.

---

## Khác biệt với QA tháng

| | QA tuần (rubric này) | QA tháng (`qa-policy.md`) |
|---|---|---|
| Mục đích | Coaching, phát triển | Đánh giá chính thức, penalty |
| Mẫu | 30 chat/tuần | 20 chat/tháng |
| Tiêu chí | Subset quan sát-được + điểm dương | Toàn bộ QT/BM/KT/KN |
| Điểm | % chất lượng theo mẫu | 100 trừ penalty |
| Nguồn | Chat log | Chat + Trello + checkin + rating |
| Người nhận | CS (DM riêng) | Hồ sơ QA, CEO duyệt |
| Hệ quả | Gợi ý cải thiện | Có thể kỷ luật |
