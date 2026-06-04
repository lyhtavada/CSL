# QA Weekly Rubric — Chấm chat hàng tuần

**Mục đích:** Chấm chất lượng chat của từng CS mỗi tuần để **coaching**, không phải để phạt.
Khác với QA tháng (`qa-policy.md` — penalty, kỷ luật, CEO duyệt), rubric tuần này:

- Chỉ chấm những gì **quan sát được từ transcript chat**
- Cho điểm theo **% chất lượng trên mẫu**, không trừ điểm kiểu kỷ luật
- Có cả **điểm dương** (để khen) lẫn điểm cần cải thiện
- Output là **DM gửi riêng cho CS**, giọng phát triển — không phải bảng phạt

> QA tháng vẫn giữ nguyên là nguồn chính thức cho penalty & kỷ luật. Rubric tuần là công cụ coaching, chạy nhanh, nhẹ.

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
| KT1 | Sai thông tin tính năng / giá / chính sách | Critical | Đối chiếu `kb/` + chatty.net/pricing |
| KT2 | Có FAQ/guide đầy đủ mà không dùng, support lòng vòng | Critical | Vấn đề đã có sẵn doc mà CS mò lại từ đầu |
| KN1 | Sai ngữ pháp/chính tả, tin nhắn thiếu chuyên nghiệp | Low | Lỗi viết rõ rệt, ảnh hưởng hình ảnh |
| KN2 | Hỏi lại thứ KH đã cung cấp trong cùng chat | Moderate | CS hỏi cái KH nói rồi |
| KN3 | Hướng dẫn chưa rõ, KH khó hiểu | Moderate | KH phải hỏi lại "ý anh là sao" |
| KN5 | Hiểu sai vấn đề → tư vấn sai hướng | High | Giải pháp lệch với điều KH thật sự cần |
| KN6 | Chưa đủ thông tin đã kết luận | Moderate | Chốt vấn đề khi chưa hỏi đủ |
| KN7 | Trả lời chung chung, không giải quyết trực tiếp | Moderate | Câu trả lời mơ hồ, không có bước cụ thể |
| KN8 | Câu mất lịch sự, gây phản ứng tiêu cực | Urgent | Tone vô lễ/cộc lốc, KH phản ứng |

> KN8 / QT11 / KT1 nếu xuất hiện → **flag riêng cho Liz xem trước khi DM**, không tự gửi.

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

Mỗi chat trong mẫu được xếp 1 trong 4 nhãn:

| Nhãn | Nghĩa | Điểm chat |
|------|-------|-----------|
| ✅ **Clean** | Không lỗi, xử lý ổn | 100 |
| 🟡 **Minor** | Chỉ lỗi Low/Moderate, không hại KH | 80 |
| 🟠 **Major** | Có lỗi High | 60 |
| 🔴 **Critical** | Có lỗi Critical/Urgent | 30 |

**Điểm tuần = trung bình điểm các chat trong mẫu.**

> Tính trên % chất lượng của mẫu → so tuần-qua-tuần công bằng, không bị một chat tệ kéo cả tuần về 0 như cách trừ penalty.

**Phân loại tổng:**
- 90–100: Xuất sắc
- 80–89: Tốt
- 70–79: Đạt, cần cải thiện vài điểm
- <70: Cần coaching 1-1

---

## 4. Lưu ý khi chấm tự động

- **QT8 (FRT >2p):** chỉ **ghi nhận**, không tính vào điểm tuần — vì policy ghi "trừ point toàn bộ agent trong ca", khó gán cho 1 CS từ transcript. Để Liz tham khảo.
- **Cần bằng chứng mới ghi lỗi:** mỗi lỗi phải **quote được câu chat** làm dẫn chứng. Không suy diễn.
- **Không chắc thì bỏ qua**, không đoán — thà sót còn hơn ghi oan, vì report này gửi thẳng cho CS.
- **Lỗi cần data ngoài chat** (follow-up Trello, review, checkin…): KHÔNG chấm ở tuần. Nếu nghi ngờ, ghi 1 dòng "cần check thêm ngoài chat" cho Liz, không tính điểm.

---

## 5. Format report gửi CS (qua Slack DM)

```
*QA Tuần [W##] — [Tên CS]*  📅 [dd/mm – dd/mm]

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

🔗 *Chat đã QA:* [link 1] · [link 2] · … (file đính kèm full list)
```

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

- Mỗi CS: `reports/qa-weekly/qa-weekly-[CS]-[YYYY-W##].md`
- Tổng hợp cả team: `reports/qa-weekly/qa-weekly-summary-[YYYY-W##].md` (cho Liz nhìn toàn cảnh trước khi duyệt)

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
