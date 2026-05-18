# CS Team SLA

Tài liệu cam kết mức dịch vụ cho CS team. Dùng để set expectations cho team, track performance, và escalate khi cần.

---

## 1. First Response Time

| Loại ticket | First Response | Ghi chú |
|-------------|---------------|---------|
| P0 - Critical (app down, data loss, security) | < 1 giờ | Escalate ngay lên PM + TS Leader |
| P1 - High (core feature broken) | < 4 giờ | |
| Complaint / Angry merchant | < 2 giờ | Sau 2 lần thử → escalate CS Leader |
| Refund request | < 2 giờ | CS Leader quyết định, CS không tự approve |
| VIP merchant (any issue) | < 2 giờ | FYI CS Leader ngay |
| Pre-sales | < 4 giờ | |
| How-to (VIP) | < 2 giờ | |
| How-to (Regular) | < 24 giờ | |
| Billing (non-refund) | < 4 giờ | |
| Feature request | < 24 giờ | Không cam kết fix |

---

## 2. Resolution Time (CS tu xu ly duoc)

| Loai ticket | Target | Ghi chu |
|-------------|--------|---------|
| How-to (VIP) | < 6 gio | |
| How-to (Regular) | < 48 gio | |
| Complaint | Trong ngay | |
| Pre-sales | Trong ngay | |
| Billing (non-refund) | Trong ngay | |
| Refund | < 24 gio | CS Leader approve → 7-10 ngay refund ve bank |

---

## 3. Resolution Time (involve team khac)

Day la phan CS KHONG kiem soat duoc thoi gian fix, nhung CS van chiu trach nhiem:

### CS phai lam:

| Action | SLA | Ghi chu |
|--------|-----|---------|
| Xac nhan van de + tao card/ticket | < 4 gio | Sau khi troubleshoot xong |
| Bao khach "da chuyen team xu ly" | Ngay khi tao card | Dung template: "Our team is looking into this. I'll update you within [X]." |
| Follow-up update cho khach | Moi 24-48 gio | KHONG de khach phai hoi lai |
| Check trang thai card tren Trello | Moi ngay | |

### Team khac phai lam:

| Loai issue | Team | Target phan hoi | Escalation neu qua han |
|------------|------|-----------------|------------------------|
| P0 Critical bug | TS + Dev | < 4 gio phan hoi, < 24 gio fix | CS Leader → TS Leader → PM |
| P1 High bug | TS | < 24 gio phan hoi | CS Leader nhac tren Slack |
| P2 Medium bug | TS | < 48 gio phan hoi | CS Leader nhac tren Trello |
| P3 Low bug | TS | Backlog | Khong escalate |
| Feature request | PM | < 48 gio acknowledge | CS Leader batch weekly |

### Escalation ladder khi team khac cham:

```
Buoc 1: Nhac tren Trello/Slack (sau khi qua target)
Buoc 2: CS Leader nhac truc tiep TS/PM (+ 24 gio)
Buoc 3: CS Leader bao TS Leader/PM Lead (+ 48 gio)
Buoc 4: Bao anh Sam (chi khi P0/P1 va anh huong nhieu merchant)
```

---

## 4. Follow-up SLA (quan trong nhat)

Merchant khong quan tam ai dang xu ly -- ho chi muon biet co ai dang lo khong.

| Tinh huong | Follow-up | Message mau |
|------------|-----------|-------------|
| Dang cho TS/Dev fix | Moi 24-48 gio | "Hi there, just a quick update -- our team is still working on this. I'll keep you posted as soon as there's progress." |
| Co update tu TS/Dev | Trong ngay | "Good news -- our team has [update]. [Next step / ETA if available]." |
| Fix xong | Ngay lap tuc | "This has been resolved. [Huong dan cu the]. Let me know if you need anything else!" |
| Khong fix duoc / Won't fix | Ngay khi co quyet dinh | "After reviewing, [ly do]. Here's what we can do instead: [workaround/alternative]." |

---

## 5. SLA Tracking

### Metric theo doi hang thang (da co tren Supabase):

| Metric | Target (full-time) | Warning | Data source |
|--------|---------------------|---------|-------------|
| Avg Response Time | < 60s | > 90s | cs_performance |
| Review Conversion Rate | > 5% | < 3% | cs_performance |
| Conversations / shift | Tham khao | -- | cs_performance |

### Metric chua track (can bo sung):

| Metric | Target | Cach lay data |
|--------|--------|---------------|
| First Response Time (FRT) | Theo bang tren | Can pull tu Chatty/Joy inbox API |
| Resolution Time | Theo bang tren | Can pull tu Chatty/Joy inbox API |
| Follow-up compliance | 100% | Manual review hoac bot check |
| Escalation response time | Theo bang tren | Trello card timestamps |

---

## 6. Nguyen tac chung

1. **Khong bao gio im lang** -- khach cho ma khong biet tinh hinh la trai nghiem te nhat
2. **Khong cam ket thoi gian fix** cho bug -- chi cam ket "se cap nhat trong 24-48 gio"
3. **Cam ket nhung gi CS kiem soat duoc** -- response time, follow-up, chat do, thai do
4. **Track de cai thien** -- khong phai de phat. Data giup team biet dang o dau va can lam gi
