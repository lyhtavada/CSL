# Quick Call Support — Chatty Onboarding & AI Training

> **Owner:** Liz (CS Leader)
> **Participants:** Andy, Jade
> **Booking tool:** Cal.com
> **Call duration:** 15-20 phút (hard limit)
> **Status:** Draft

---

## Mục tiêu

Tập trung support nhóm khách ICP, tạo trải nghiệm tốt, giữ chân, lấy insights, đồng hành cùng khách hàng trong suốt hành trình sử dụng app — từ khi cài, live, đến tối ưu.

CS Chatty chuyển dịch từ support on demand sang **proactive support nhóm khách tiềm năng, chất lượng**. Mỗi CS là một AM — đồng hành thực sự, không chỉ giải quyết ticket. Team sản phẩm cũng sẽ join call, survey, và support nhóm khách này để lấy insights chính xác hơn.

Call này là **quick session** — không phải demo chi tiết hay troubleshooting.

---

## Ai được offer call?

Call này dành riêng cho nhóm KH tiềm năng, chất lượng — không offer đại trà. Mục tiêu là proactive support đúng người, đúng lúc.

### Offer khi match ít nhất 1 điều kiện

- KH thuộc ICP (score 7+ theo Chatty ICP trên KB LIVE `cs2.avada.net`, fetch qua `skills/qa-weekly/scripts/fetch_kb.py chatty kb/reference/...`) — bất kể plan nào
- Mới cài app — offer proactive, không cần đợi KH hỏi
- Đang setup hoặc training AI lần đầu
- Đang gặp friction rõ ràng (loay hoay, hỏi nhiều, chưa live được)
- KH ICP đã dùng một thời gian nhưng chưa tận dụng hết app

### Không offer

- Không thuộc ICP và chưa có signal rõ ràng
- Chỉ hỏi 1 câu đơn giản (quick reply là đủ)
- Đã offer call trước đó mà không book
- KH chỉ cần troubleshoot bug (xử lý qua chat + escalate TS)

---

## Phân loại call

| Loại | Khi nào | Mục tiêu |
|------|---------|-----------|
| Onboarding / Walkthrough | KH mới cài, chưa biết bắt đầu từ đâu | Setup được live chat hoặc FAQ cơ bản |
| AI issue | AI trả lời sai, không sync, không hoạt động | Xác định nguyên nhân, fix trong call hoặc escalate TS |
| AI training | KH đã dùng nhưng muốn tối ưu AI | Optimize product sync, custom answers, scenarios |

---

## Pre-call Form

**Gửi cho KH sau khi họ book** — tự động qua Cal.com hoặc CS gửi thủ công link.

Mục đích: CS nắm được KH cần gì trước khi vào call. Form ngắn, buộc KH tập trung vào 1-2 vấn đề cụ thể.

### Các câu hỏi trong form

1. **What's the main thing you want to get done in this call?** *(chọn 1)*
   - Get started / understand how the app works
   - Set up or improve the AI assistant
   - Fix a specific issue
   - Other (please describe)

2. **Briefly describe your issue or goal:** *(text, max 200 ký tự)*

3. **What's your store URL?** *(myshopify.com format)*

> Form chỉ 3 câu — không để KH viết essay. Mục tiêu: CS đọc form là biết luôn call này thuộc loại nào và cần chuẩn bị gì.

---

## Flow

```
CS nhận chat → KH match criteria → Offer call
                                         ↓
                          KH đồng ý: gửi Cal.com link
                          KH từ chối: tiếp tục qua chat
                                         ↓
                              KH nhận link pre-call form
                              (auto sau khi book, hoặc CS gửi thủ công)
                                         ↓
                    CS đọc form + check store trước call (5 phút)
                                         ↓
                              Call — 15-20 phút (hard limit)
                                         ↓
                    KH tự explore → gửi helpcenter link, kết thúc
                    KH cần follow-up → log vào call form
```

---

## Chi tiết từng bước

### 1. Offer call

Gợi ý tự nhiên trong chat:

> Would you like to hop on a quick 15-20 min call? I can walk you through [the setup / fixing this] directly — usually faster than chat.

Nếu KH đồng ý → gửi Cal.com link. Không push nếu KH từ chối.

### 2. Trước call — chuẩn bị 5 phút

Đọc form KH điền + check nhanh:

| Check | Cách xem |
|-------|----------|
| Store URL + plan | DevZone |
| AI setup status | Chatty app > AI Assistant |
| Chat/issue history | Crisp inbox |
| Pending issues | Trello / Crisp notes |

Mục đích: vào call là biết KH đang ở đâu, không hỏi lại những thứ đã có.

### 3. Trong call — 15-20 phút (hard limit)

**Mở đầu (1-2 phút):** Bật record trên tl;dv trước. Confirm mục tiêu — "We have 15 minutes, let's focus on [X]."

**Quick audit (2-3 phút):** Share screen, xem setup, identify điểm cần chỉnh.

**Hands-on (10-12 phút):** Làm 1-2 việc quan trọng nhất. Không cố cover hết.

**Wrap-up (2-3 phút):** Tóm tắt đã làm gì. Nếu cần follow-up → hẹn ngày.

### 4. Sau call

- **KH tự explore:** Gửi 1-2 link helpcenter phù hợp → kết thúc.
- **KH cần follow-up:** Mở [form log call](https://chatty-call-logs.lizavada.deno.net/) → điền ngay, không để qua ngày.

---

## Scheduling — Cal.com setup

### CS được assign call

Tất cả CS full-time đều có thể handle call. Scheduling qua Cal.com theo ca trực.

### Time slots

Mỗi ngày mở 2-3 slot cố định, chọn theo overlap giờ US/EU:

| Slot | Giờ VN (GMT+7) | US Eastern | US Pacific | EU (CET) |
|------|----------------|------------|------------|----------|
| Slot 1 | 20:00 | 9:00 AM | 6:00 AM | 2:00 PM |
| Slot 2 | 22:00 | 11:00 AM | 8:00 AM | 4:00 PM |
| Slot 3 | 00:00 (+1) | 1:00 PM | 10:00 AM | 6:00 PM |

> Liz confirm lại slots phù hợp với ca trực của Andy và Jade.

### Cal.com config

- **Event type:** "Quick Setup Call — Chatty" (15 phút, buffer 5 phút)
- **Team page:** Andy + Jade — round-robin hoặc collective (tùy Liz chọn)
- **Availability:** Chỉ show slots của CS được assign, theo ca trực
- **Buffer:** 5 phút giữa các call (thời gian ghi note)
- **Max bookings/ngày/agent:** 3 (tránh ảnh hưởng chat support)
- **Booking window:** KH chỉ book trước tối đa 5 ngày
- **Cancellation:** KH có thể cancel/reschedule trước 2 giờ

---

## Follow-up tracking — Web form + Supabase

Dùng cho KH cần hỗ trợ thêm sau call. Không dùng cho KH tự explore.

### Cách dùng

Ngay sau call, CS mở link form (bookmark sẵn) → điền thông tin → bấm Save. Data tự động lưu vào Supabase (table `call_followup`).

- **Link form:** https://chatty-call-logs.lizavada.deno.net/
- **Password:** `chatty2026` (nhập 1 lần, cookie giữ 30 ngày)

```
CS mở link form → nhập password (1 lần) → điền info → Save → Lưu vào Supabase
```

### Các field trong form

| Field | Bắt buộc | Ví dụ |
|-------|----------|-------|
| Call Date | ✅ | 2026-03-20 |
| Store URL | ✅ | example.myshopify.com |
| Store Name | | Example Store |
| Contact Email | | merchant@example.com |
| Current Plan | | Pro ($68.99) |
| Call Topic | ✅ | AI training — product sync + scenarios |
| What was done | | Synced 500 products, set up 3 scenarios |
| Next Steps | | Add custom answers for shipping policy |
| Follow-up Date | | 2026-03-25 |
| Status | ✅ | Need follow-up / Done / Upgraded / No response |
| Notes | | KH interested in upgrading to Plus |

CS Agent tự động lấy từ Slack account — không cần điền.

### Quy tắc follow-up

- Follow-up lần 1: đúng ngày đã hẹn
- Follow-up lần 2: 3-5 ngày sau nếu KH chưa phản hồi
- Sau 2 lần không phản hồi → update status "No response" (mở lại form hoặc báo CSL)
- Nếu KH upgrade → update status "Upgraded", báo CSL

### Technical details

- Data lưu trên Supabase table `call_followup` (cùng project với `cs_performance`)
- Edge Function chạy trên Supabase cloud — không cần máy nào bật
- Setup guide: `bots/call-followup/README.md`

---

## Giới hạn và lưu ý

### Call KHÔNG dùng để

- Demo chi tiết từng feature (gửi helpcenter link thay vì giải thích dài)
- Troubleshoot bug (note lại, escalate TS sau call)
- Thương lượng pricing/discount (refer CSL)
- Setup phức tạp cần > 20 phút (hẹn call riêng hoặc chia nhỏ)

### Lưu ý cho CS

- **Set timer 15 phút** khi bắt đầu call — khi còn 3 phút thì wrap-up
- **Không hứa feature/timeline** — chỉ hỗ trợ những gì đang available
- **Nói chậm, rõ** — KH không phải lúc nào cũng quen tiếng Anh
- **Share screen** khi hướng dẫn — show, đừng chỉ nói
- **Ghi note ngay sau call** — mở form log call, điền ngay, không để qua ngày hôm sau

### Khi nào escalate CSL

- KH là VIP hoặc high-revenue merchant
- KH yêu cầu discount/refund trong call
- KH angry hoặc threaten bad review
- Call cần kéo dài hơn 20 phút vì case phức tạp
- KH muốn setup cần involve TS/Dev

---

## Metrics (theo dõi hàng tháng)

| Metric | Mục đích |
|--------|----------|
| Số call/tháng | Đo workload |
| Conversion sau call (upgrade) | Đo hiệu quả |
| Follow-up close rate | KH cần follow-up → resolved hay drop? |
| Avg call duration | Có giữ được 15-20 phút không? |
| KH satisfaction (optional) | Cal.com có thể gắn survey ngắn sau call |

---

*Last updated: March 2026*
*Owner: Liz (CS Leader)*
