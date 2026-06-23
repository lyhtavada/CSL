# Chatty Proactive DFY — Pilot SOP (Andy)

**Mục đích:** Chuyển DFY từ **thụ động** (chờ KH vào từ email rồi offer) sang **chủ động** — Andy tự lấy danh sách KH mới cài Pro/Plus, chủ động offer DFY và follow-up qua các ca.

**Người chạy:** Andy (CS đang training sub-lead, 4 ca/tuần)
**Owner:** Liz (CSL) — escalation & review
**Trạng thái:** Pilot v1 (2026-06-23) — 3–4 tuần đầu để lấy số thật về sức làm proactive
**Flow gốc:** mọi bước *làm* DFY (M1/M2/M3, checklist, template) theo `chatty-dfy-flow.md`. SOP này chỉ mô tả phần **mới**: lấy tệp → audit → **viết email hoàn chỉnh gửi KH** → follow-up theo ca → tạo ticket.

---

## 1. Tệp KH của pilot

**Đối tượng:** store Chatty **mới cài ≤14 ngày + đang ở plan Pro/Plus** (gồm cả trial Pro).

Vì sao nhóm này:
- Vừa cài + vừa lên Pro/Plus → đang nghiêm túc, đúng khoảnh khắc cần setup tốt để khỏi rớt sau trial.
- Khối lượng vừa sức (~20 store/tuần) cho 4 ca → audit + chạm kỹ từng store, không chạm đại trà.
- KH mới đang hào hứng → an toàn để tập kỹ năng proactive.

**Nguồn list = bảng analytics (KHÔNG dùng Slack/Sheet):**
- Link public (mở thẳng, không cần login): **https://analytics.avada.net/public/views/sytCf8kfby3J5Yknohqa**
- Tên view: "Chatty Proactive DFY — New Pro/Plus"
- Bảng tự refresh mỗi 1h, đã lọc sẵn store test nội bộ.
- Đã lọc: `app=avadaFaq`, cài ≤14 ngày, plan Pro/Plus, bỏ domain `ag-ly-chatty-*` và `*-test-*`.

---

## 2. Đọc bảng + nhận store theo ca

Các cột trong bảng và cách dùng:

| Cột | Dùng để |
|-----|---------|
| `shop_domain` | Mở store |
| `days_since_install` | Ưu tiên store cài **lâu nhất** trước (sắp nguội) |
| `current_mrr` | $0 = chưa charge; >0 = đã trả tiền thật |
| `on_trial` | `true` = đang trial → **ưu tiên DFY trước khi hết trial** |
| `usage_segment` | `high_usage` / `inactive_30d` / `active_usage` |
| `primary_industry` | Ngành — để cá nhân hoá email |
| `ticket_link` | Có link = **store đã có người làm** → click xem; `-` = **chưa ai đụng, nhận được** |
| `ticket_status` / `ticket_count` | Tình trạng ticket |
| `installed_at` | Ngày cài |

**Đầu mỗi ca (4 ca/tuần):**
1. Mở bảng → lọc/nhìn các dòng `ticket_link = -` (chưa ai làm).
2. Chọn **3–5 store**, ưu tiên: `on_trial=true` + `days_since_install` cao (sắp hết trial mà chưa setup).
3. Bắt tay vào audit → **tạo ticket ngay** (Bước 3) → vài giờ sau ticket tự hiện link trong bảng = báo cho ca/người khác là store đã có người làm.

> **Tránh trùng ca = qua ticket, không cần claim thủ công.** Store nào `ticket_link` đã có link DFY → KHÔNG đụng (trừ khi cần phối hợp, đọc ticket trước). Bảng tự phản ánh ai đang làm gì.

---

## 3. Vòng làm việc 1 store (chủ động)

### Bước 1 — Audit store TRƯỚC khi chạm
Mở store + tool audit setting (Liz cung cấp) → ghi nhanh:
- Widget còn default hay đã custom?
- FAQ có chưa? AI đã train chưa? Plan có AI không?
- Đã có hoạt động (conversation) chưa, hay cài rồi bỏ đó?

→ Đây là nội dung để chạm đúng vấn đề, không chạm chung chung.

### Bước 2 — Viết EMAIL hoàn chỉnh gửi KH (không chỉ offer chờ "yes")
Sau audit, Andy viết **một email cá nhân hoá** cho store đó — nêu cụ thể cái thấy được từ audit + đề xuất setup, rồi gửi luôn. Đây là điểm khác DFY thụ động: chủ động đến tận nơi, không pop-up chờ KH bấm.

Cấu trúc email (theo `_identity/tone-and-voice.md` — mở đầu "Hi there, This is ... from Avada Support Team", không bold, không em dash):
1. **Chào + giới thiệu** — Avada Support Team, đang hỗ trợ store mới dùng Chatty.
2. **Cái thấy được từ audit (cá nhân hoá)** — "I had a look at your store and noticed [widget vẫn default / chưa có FAQ / AI chưa train / ...]". Nêu 1–2 điểm cụ thể, đúng store đó.
3. **Đề xuất giá trị** — done-for-you setup miễn phí: branded widget + FAQ + AI, làm khớp store, không phải template chung.
4. **CTA rõ một hành động** — reply để Andy bắt đầu, hoặc đề xuất khung giờ.
5. **Trấn an** — KH không phải tự làm gì, vẫn chỉnh được sau.

> Email phải dựa trên audit thật của store đó, KHÔNG gửi bản chung chung. Lưu draft/nội dung email vào ticket (Bước 3).

### Bước 3 — Tạo ticket NGAY khi gửi email
**Andy tự tạo DFY ticket cho store đó** (KHÔNG dùng Google Sheet). Mỗi store = 1 ticket. Tạo ngay khi gửi email (để track cả KH chưa reply), ghi nội dung email + kết quả audit vào ticket.
- `appName` = Chatty, `appPlan`, `domain` (store đang làm)
- Member = Andy
- Tag: `DFY-new` **+** `proactive` (tag phụ để pilot này tách riêng khỏi DFY thường khi đo)
- Subject: `[Proactive DFY] <domain>`
- → bắt đầu đếm SLA 48H (theo flow gốc).

### Bước 4 — Làm DFY theo flow gốc
Theo `chatty-dfy-flow.md`: audit → M1 Chatbox → M2 FAQ → M3 AI (thứ tự M1→M2→M3), dùng đúng checklist §5 và pre-session checklist AI §4. Cập nhật label theo tiến độ (`DFY-in-progress` → `DFY-M1/M2/M3`).

### Bước 5 — Follow-up qua ca (điểm mấu chốt của pilot)
DFY kéo dài qua nhiều ca. Vì **ticket gánh trí nhớ**, không phải người:
- Mỗi lần đụng store → **đọc ticket trước** (lần trước làm tới đâu, KH duyệt gì, đang chờ gì).
- Mỗi lần làm/nhận phản hồi → **ghi vào ticket** (đã làm gì, KH nói gì, bước tiếp theo).
- KH duyệt module → activate → gắn label module.
- Sau 2–5 ngày check adopt: có adopt → `DFY-adopted` → close; không phản hồi → `!dfy-remind` → `DFY-no-adopt` → close.

---

## 4. Note vào đâu — chỉ MỘT chỗ: DFY ticket

| Việc | Note ở đâu |
|------|-----------|
| Đã chạm gì, KH phản hồi | Comment trong ticket |
| Store thiếu setting gì (từ audit) | Comment trong ticket |
| Module nào xong | Label `DFY-M1/M2/M3` |
| Kết quả cuối | `DFY-adopted` / `DFY-no-adopt` rồi close |

**KHÔNG tạo Google Sheet.** Mọi thứ vào ticket → tự lên DFY tracker (`reports/dfy/chatty/`) và `/dfy-weekly` đo được.

---

## 5. Khi nào escalate Liz
- KH đòi giảm giá / refund / muốn downgrade
- KH bực, complaint vượt tầm CS
- Store Plus có dấu hiệu bỏ app
- DFY quá SLA 48H chưa update được

---

## 6. Đo pilot (Liz review sau 3–4 tuần)
Lọc ticket tag `proactive` trong `/dfy-weekly`:
- Bao nhiêu store được offer → bao nhiêu đồng ý DFY (tỉ lệ accept)
- Bao nhiêu adopt (`DFY-adopted` / tổng)
- Trung bình 1 ca Andy làm xong bao nhiêu store
- → số liệu để quyết: có nhân rộng vai trò proactive cho cả team không, 1 người full-time làm được bao nhiêu/tuần.

---

## 7. Việc còn chờ trước khi Andy chạy
| # | Việc | Ai |
|---|------|-----|
| 1 | Mô tả tool audit setting (tên, cách mở) | Liz |
| 2 | Tạo channel Slack chứa list store + cách claim | Liz |
| 3 | Query/đẩy list ~20 store mới cài Pro/Plus vào channel hàng tuần | Betty |
| 4 | Tạo tag `proactive` trong ticket system | Liz/Betty |
| 5 | Brief Andy: tệp = list trong channel, làm theo SOP này + flow gốc | Liz |

---

*Pilot này tái dùng toàn bộ `chatty-dfy-flow.md`, chỉ thêm cách lấy tệp chủ động + follow-up qua ca. Sau 3–4 tuần có số → Liz quyết nhân rộng.*
