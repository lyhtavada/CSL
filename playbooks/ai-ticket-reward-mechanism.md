# Cơ chế Reward Point — Ticket AI Agent

> CS dùng AI agent để investigate issue và tạo ticket → được reward point. Point gắn với **giá trị/độ khó issue**, không thưởng cho việc chỉ tạo ticket. 1 point = 1.000đ.

## 1. Mục tiêu

Khuyến khích CS dùng AI agent investigate & tạo ticket, thưởng theo **giá trị/outcome thật của issue** — không thưởng cho ticket rác hay ticket chỉ đúng format. Trần **1.000p/CS/tháng** để kiểm soát chi phí.

## 2. Nhận diện ticket được reward (gate cứng — auto)

Ticket phải thỏa **CẢ 2** điều kiện, đọc trực tiếp từ field ticket:

- Creator là **CS thật**: `members[isCreate:true].authUid` **≠** `ai-agent-*`
- CS đã **dùng AI agent**: tồn tại `members[].authUid` bắt đầu bằng `ai-agent-`

→ CS nhận point = `members[isCreate:true].displayName` → map sang nickname KPI (bảng có sẵn trong /dfy-tracker). Merge trùng tên (`Alyssa` = `alyssa_avada`).

**Loại ngay (không tính point):**

- AI agent tự tạo ticket (creator là `ai-agent-*`, không có CS) → không có CS để thưởng
- Ticket thường không có AI agent tham gia → không thuộc chương trình

## 3. Gate chất lượng (qua mới xét point)

- `chatLink` không rỗng (có link Crisp session)
- `store[0].domain` có (shop + app)
- `description` đủ cấu trúc: "Vấn đề" + "Cửa hàng" + "Link hội thoại"
- Không dedup — trùng domain + nội dung trong 7 ngày → loại

**Không đạt gate = 0p** (không phạt).

## 4. Bảng LEVEL & point

Level suy từ **outcome thật của ticket** (`tsStatus`) — outcome phản ánh đúng độ khó/giá trị và auto 100%, CS không tự khai được nên chống farm tốt.

| Level | Ý nghĩa | Điều kiện auto (tsStatus) | Point |
|-------|---------|---------------------------|-------|
| L1 — Basic | Issue xử lý được, khách OK | done / waiting_customer / resolved | 20 |
| L2 — Dev-confirmed | Issue là bug thật, dev tiếp nhận | dev_fixing / dev_done / pending_dev | 35 |
| L3 — High-impact | Bug fixed, ảnh hưởng nhiều shop / feed cải thiện AI-KB | done + dev fix, hoặc tag recurring/kb-improve (Liz gắn) | 50 |
| Feature request | Ra được feature request hợp lệ | feature_request | 15 |

> Lý do map theo `tsStatus`: ticket đẩy được tới dev (dev_fixing/dev_done) = CS đã investigate ra bug thật, giá trị cao hơn ticket đóng nhanh.

## 5. Chống farm (auto)

- `ticketStatus` = invalid / duplicate, hoặc dedup trùng → **0p**
- Tỷ lệ (invalid + dup)/CS **> 30%/tuần** → tuần đó chỉ tính L1 (không cho L2/L3)
- **Trần 1.000p/CS/tháng** — chạm trần thì dừng cộng, Liz duyệt nếu vượt

## 6. Ước chi phí trên data thật (01–15/07)

25 ticket AI agent CS-tạo trong nửa tháng → ~50/tháng cả 2 app.

| App | Ticket | Ước point (theo tsStatus thật) |
|-----|--------|-------------------------------|
| JOY | 7 | ~210p |
| Chatty | 18 | ~410p |
| Tổng nửa tháng | 25 | ~620p → ~1.2tr/tháng cả 2 app |

Per-CS cao nhất hiện tại (Linda ~12 Chatty ticket) → ~500p/tháng — dưới trần 1.000p thoải mái. Ngân sách thật ~**1–1.5tr/tháng cho cả team** — kiểm soát được.

## 7. Vận hành

- Skill mới `/ai-ticket-reward` — tái dùng code fetch + bảng nickname của /dfy-tracker
- Fetch → lọc gate cứng → gate chất lượng → map tsStatus → level → point → gom per-CS → report tuần/tháng
- Cron tuần (monitor) + tháng (chốt point) → Notion + DM Liz duyệt L3/high-value

## 8. Ví dụ chấm trên ticket thật

- **JOY-260715-M6azs5** (Alyssa tạo, có ai-agent-2, tsStatus: pending): qua 2 gate → L1/L2 tùy khi dev tiếp nhận → 20–35p
- **JOY-260715-6ucCLC** (ai-agent-2 tự tạo, không có CS creator): loại ngay, không tính point
