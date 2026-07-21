# Dev Join Support — Quy trình kéo ticket (Chatty)

## Bối cảnh

Từ tuần này, **Dev join hỗ trợ CS như 1 TS** — tự kéo ticket kỹ thuật (bug) từ Avada Ticket để xử lý, thay vì chỉ nhận qua escalate thủ công. Doc này mô tả các status ticket trên Avada Ticket (`avada-ts-a9cb0.web.app`) và cách dev xác định ticket nào cần kéo, đang làm, đã xong.

Data lấy live qua Avada Ticket API (`GET /api/external/tickets/by-date`, app `Chatty`) — 2 field status quan trọng: **`ticketStatus`** (mở/đóng) và **`tsStatus`** (đang ở bước nào trong flow xử lý).

## 1. `ticketStatus` — trạng thái tổng

| Giá trị | Ý nghĩa |
|---|---|
| `open` | Ticket còn mở, đang cần xử lý (ở bất kỳ bước nào) |
| `closed` | Ticket đã đóng — xong hoặc đã huỷ |

## 2. `tsStatus` — trạng thái xử lý chi tiết

| `tsStatus` | Ý nghĩa | Ai đang giữ bóng |
|---|---|---|
| `pending` | Ticket mới, **chưa triage** — CS/TS cần đọc, xác định hướng xử lý (tự xử lý được hay cần escalate cho dev) | CS/TS |
| `waiting_customer` | Đang chờ merchant phản hồi thêm thông tin | Merchant |
| `waiting_permission` | Đang chờ merchant cấp quyền truy cập store/admin | Merchant |
| `doing` | CS/TS đang xử lý trực tiếp (không cần dev) | CS/TS |
| `dev_fixing` | **Dev đang sửa** — đây là ticket "working" của dev | Dev |
| `dev_done` | **Dev đã sửa xong**, đẩy lại cho CS verify với merchant rồi đóng ticket | CS/TS (verify) |
| `customization` | Yêu cầu custom riêng cho merchant (không phải bug) | Dev/TS |
| `feature_request` | Đề xuất tính năng mới, không xử lý ngay — chuyển PM | PM |
| `billing` | Vấn đề liên quan billing/subscription | CS Leader |
| `sale_request` | Yêu cầu liên quan sales (discount, upsell...) | Sales/PM |
| `done_for_you` | Ticket thuộc chương trình **DFY** (xem mục 4, flow riêng) | CS phụ trách DFY |
| `done` | Đã xử lý xong (không qua dev), chờ đóng hoặc đã đóng | — |

> Lưu ý: `pending` không có nghĩa là "chờ dev" — nó là ticket **chưa được ai nhận**, có thể là bug, billing, refund, cancel request... CS/TS phải đọc và phân loại trước khi biết có cần đẩy cho dev hay không.

## 3. Cách dev kéo ticket

**Ticket cần dev pull (bug kỹ thuật):**
1. Lọc subject có tiền tố `[bug]` (hoặc mô tả rõ lỗi kỹ thuật, không phải hỏi cách dùng)
2. `ticketStatus = open` **và** `tsStatus = pending` → đây là bug **đã report nhưng chưa ai claim** — dev đọc, nếu xác nhận là bug kỹ thuật thật (không phải setup sai) thì tự chuyển `tsStatus → dev_fixing` để claim
3. Ticket đã có `tsStatus = dev_fixing` mà chưa phải của mình → đã có dev khác claim, không pull trùng

**Trong lúc làm:**
- Giữ `tsStatus = dev_fixing` cho tới khi fix xong
- Nếu cần thêm thông tin từ merchant → chuyển `waiting_customer`, note rõ đang chờ gì
- Nếu cần quyền truy cập → chuyển `waiting_permission`

**Khi fix xong:**
- Chuyển `tsStatus → dev_done`
- Ghi rõ trong ticket: đã sửa gì, cách merchant có thể verify (VD: "đã fix, MC thử lại action X xem có ra kết quả Y không")
- CS/TS sẽ verify với merchant rồi đóng ticket (`ticketStatus = closed`)

## 4. DFY tickets — KHÔNG thuộc flow dev pull ở trên

Ticket subject `[DFY]` có `tsStatus = done_for_you` xuyên suốt cho tới khi xong — đây là chương trình CS chủ động setup hộ merchant (checklist AI Agent/Chatbox/Video), **không phải bug**, không cần dev pull theo flow trên. Chi tiết xem `playbooks/chatty-dfy-flow.md` và skill `/dfy-tracker`.

## 5. Phân loại issue theo tiền tố subject

Dựa trên data thực tế 21 ngày gần nhất (409 ticket), các tiền tố hay gặp:

| Tiền tố subject | Loại issue | Xử lý |
|---|---|---|
| `[bug]` | Lỗi kỹ thuật (UI sai, tính năng không hoạt động, crash...) | → Dev (mục 3) |
| `[DFY]` | Setup hộ merchant theo chương trình DFY | → CS phụ trách DFY, không qua dev |
| `[Customize]` / `[Custom]` | Yêu cầu tuỳ chỉnh riêng cho merchant (không phải lỗi) | → Dev, nhưng khác nature với bug — cần confirm phạm vi trước khi làm |
| `[Refund]` | Yêu cầu hoàn tiền | → CS Leader (billing flow), không liên quan dev |
| `[Request]` | Yêu cầu tính năng/hỗ trợ chung, chưa rõ loại | → Triage lại, xác định có phải bug không |
| (không tiền tố) | Đa số là câu hỏi cách dùng, hoặc bug được viết tự do (không gắn `[bug]`) — **CS/TS vẫn phải đọc kỹ**, đừng chỉ lọc theo tiền tố `[bug]` vì có bug report không gắn tag | → Triage theo nội dung |

> Không phải mọi bug đều có tiền tố `[bug]` chuẩn — ví dụ ticket "Cart counter không update tức thì" hay "Missing automated AI response for 'View Similar'" đang ở `dev_fixing` nhưng subject không có `[bug]`. Vì vậy bước triage (đọc nội dung, không chỉ lọc tiền tố) vẫn là bắt buộc trước khi kết luận không phải việc của dev.

## 6. Tham chiếu nhanh — API

```
GET https://avada-ts-a9cb0.web.app/api/external/tickets/by-date
Headers: X-API-Key: {AVD_TICKET_API_KEY}
Params: startDate, endDate, appName="Chatty"
```
Field quan trọng: `ticketStatus`, `tsStatus`, `subject`, `priority`, `tagIds`, `members[].isCreate` (người tạo), `shortUrl` (link ticket, prepend domain trên).
