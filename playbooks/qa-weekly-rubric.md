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

## 2. Ba trục đánh giá (mỗi chat chấm 3 trục, mỗi trục ~33 điểm)

Mỗi chat được chấm trên **3 trục độc lập**, mỗi trục tối đa ~33 điểm → tổng 100.
Trọng tâm là **chất lượng phục vụ khách hàng** (mindset + kiến thức), không chỉ
soi lỗi quy trình.

### Trục 1 — 🧠 MINDSET phục vụ KH (0–34đ)

CS có thật sự **đặt mình vào vị trí khách và muốn giải quyết tới cùng** không —
hay chỉ làm cho xong việc. Đây là "cái tâm" trong support.

| Khía cạnh | Tốt (cộng điểm) | Tệ (trừ điểm) |
|-----------|-----------------|----------------|
| **Ownership** | Theo đuổi vấn đề tới khi KH thật sự xong; không đẩy đi / đóng chat lửng | Đẩy việc, đóng chat khi KH chưa xong, "không phải việc của tôi" |
| **Thấu cảm** | Hiểu cảm xúc/tình huống KH, trấn an đúng lúc khi KH bực/lo | Máy móc, lạnh lùng, phớt lờ cảm xúc KH |
| **Chủ động vì KH** | Đề xuất thêm giải pháp/cảnh báo KH chưa kịp hỏi, nghĩ xa hơn yêu cầu | Chỉ làm đúng câu hỏi, không nghĩ thêm cho KH |
| **Nỗ lực làm KH hài lòng** | Đi thêm một bước để KH happy; kiên nhẫn với KH khó | Làm tối thiểu cho xong, bỏ cuộc khi KH khó |

- **~34đ:** mindset xuất sắc rõ rệt ở nhiều khía cạnh (KH cảm nhận được sự tận tâm).
- **~25đ:** ổn, phục vụ đàng hoàng nhưng không nổi bật.
- **~15đ:** máy móc, làm cho xong, thiếu sự quan tâm.
- **~5đ:** vô cảm/đẩy việc/bỏ mặc KH (kèm QT11 bỏ tin nhắn, KN8 mất lịch sự).

### Trục 2 — 📚 KIẾN THỨC (0–33đ) — BẮT BUỘC đối chiếu KB

Tư vấn có **đúng** không. Sai kiến thức là nguy hiểm nhất (KH tin rồi làm sai).
**Không dựa vào hiểu biết chung** — phải mở KB thật mà AI agent dùng để verify:

- **Chatty KB:** `/Users/avada/claw-weebhook-crisp-chat/agents/chatty-agent/knowledge/`
- **Joy KB:** `/Users/avada/claw-weebhook-crisp-chat/agents/joy-loyalty-agent/knowledge/`
- **Index tra nhanh:** `skills/qa-weekly/references/kb-index.md` (mỗi file kèm "applies_when")

Cách làm: chat có claim về giá/tính năng/giới hạn/chính sách → tra index → Read
1–3 file KB liên quan → so claim với KB.

- **~33đ:** mọi claim đúng KB, nắm vững sản phẩm, tư vấn chính xác.
- **~22đ:** đúng nhưng có chỗ chưa chắc / trả lời thiếu so với KB có sẵn.
- **~10đ:** dùng KB sẵn mà support lòng vòng (KT2), hoặc bảo "không làm được" khi KB nói được.
- **~0đ:** **sai thông tin** giá/tính năng/chính sách (KT1) — claim trái KB.

> KB có thể **outdated** → nếu claim CS trái KB nhưng nghi KB sai (vd app hiện số
> khác), **flag cho Liz verify**, đừng vội trừ điểm/kết tội CS.

### Trục 3 — 🛠️ KỸ NĂNG XỬ LÝ (0–33đ)

Cách trình bày & xử lý — rõ ràng, đúng flow, không lỗi giao tiếp.

| Tốt | Lỗi (trừ điểm) |
|-----|----------------|
| Giải thích có bước, KH làm theo được ngay | KN3 hướng dẫn khó hiểu · KN7 trả lời chung chung |
| Đi thẳng vấn đề, không vòng vo | QT9 hỏi vòng vo · KN2 hỏi lại thứ KH đã nói |
| Hiểu đúng vấn đề trước khi tư vấn | KN5 hiểu sai → tư vấn sai · KN6 kết luận khi chưa đủ thông tin |
| Báo rõ bước tiếp theo, không bỏ sót | QT18 đóng chat lửng · QT22 bỏ sót câu hỏi · QT25 hẹn rồi im |
| Viết chuyên nghiệp | KN1 sai ngữ pháp/chính tả |

- **~33đ:** xử lý gọn, rõ ràng, đúng flow, không lỗi.
- **~22đ:** ổn nhưng có 1 lỗi nhẹ (Low/Moderate).
- **~10đ:** có lỗi nặng (High: hiểu sai, bỏ sót câu hỏi).
- **~0đ:** xử lý hỏng (bỏ tin nhắn KH, gây hậu quả).

> **Ngôn ngữ:** Crisp có live translate sẵn → CS trả lời đúng tiếng KH **KHÔNG
> phải điểm cộng**, đừng khen "đa ngôn ngữ" (máy dịch hết). Ngược lại, **chỉ flag
> khi KH gửi 1 tiếng mà CS gửi tiếng khác** (lệch ngôn ngữ) → KH phải tự dịch →
> tính lỗi KN3, trừ điểm trục Skill. Cùng ngôn ngữ = bình thường, không nhận xét.

> **Flag riêng cho Liz** trước khi DM nếu có: KN8 (mất lịch sự), QT11 (bỏ KH),
> KT1 (sai kiến thức), hoặc thao tác gây hậu quả trên live store.

---

## 3. Cách tính điểm

**Điểm 1 chat = Mindset (0–34) + Kiến thức (0–33) + Xử lý (0–33) = 0–100.**

Chat không có message nào của CS đang xét → loại khỏi mẫu, không tính.

**Điểm tuần = trung bình điểm các chat trong mẫu** (làm tròn).

> Hệ quả của mô hình 3 trục: một CS **đúng kỹ thuật nhưng vô cảm/máy móc** sẽ mất
> ~⅓ điểm ở trục Mindset → không thể đạt cao. Một CS **tận tâm + đúng kiến thức**
> nhưng có vài typo nhỏ vẫn giữ điểm cao. Đây là chủ đích: đề cao phục vụ KH bằng
> cái tâm và sự chính xác, không chỉ đúng quy trình.

**Phân loại tổng:**
- **90–100: Xuất sắc** 🌟 — tận tâm, đúng kiến thức, xử lý mượt
- **80–89: Tốt** 👍
- **70–79: Đạt** — ổn nhưng thiếu một trục rõ rệt
- **<70: Cần coaching 1-1** 🤝

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

📝 *Nhận xét chung*
Tuần này bạn xử lý chắc tay, tone với khách rất ấm và chủ động. Điểm mạnh nhất là giải thích có bước, khách làm theo được ngay. Hướng tập trung tuần tới: confirm lại yêu cầu khách trước khi tư vấn để tránh hiểu lệch.

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

**Giọng điệu:** thẳng thắn, rõ ràng, cụ thể — **không vòng vo, không lấp liếm**.
Mục tiêu là để CS hiểu chính xác mình đang thiếu ở đâu và phải sửa gì, không phải
để dễ chịu. Mỗi điểm cần cải thiện luôn kèm **1 gợi ý hành động cụ thể**.

- **Gọi tên vấn đề thẳng:** "câu trả lời chưa đúng trọng tâm khách hỏi", không nói
  tránh thành "có thể rõ hơn một chút". Nêu rõ **hệ quả**: vấn đề này làm khách phải
  hỏi lại / kéo dài chat / hiểu sai.
- **Khen có cơ sở, không khen xã giao** — chỉ nêu điểm tốt khi thật sự nổi bật.
- Vẫn tôn trọng và mang tính xây dựng, nhưng **không hạ nhẹ mức độ** của lỗi. Lỗi
  lặp lại nhiều lần phải nói rõ là "lặp lại, cần ưu tiên sửa".
- Tránh từ "phạt", "trừ điểm", "vi phạm" (đây là coaching, không phải kỷ luật).

**Xưng hô:** gọi CS là **"bạn"** (trung lập), KHÔNG gọi "em". Tránh xưng "chị/mình"
trong nội dung nhận xét — chỉ dùng "bạn" để khách quan, đỡ tạo khoảng cách trên/dưới.

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
