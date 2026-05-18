# Outline — After Call Tracking Database (Notion)

> Tạo 1 Notion database. Mỗi discovery call = 1 record. CS điền sau mỗi call.

---

## Properties (cột trong database)

| Property | Type | Giá trị |
|----------|------|---------|
| Store Name | Title | Tên store |
| Store URL | URL | Link myshopify |
| Ngày call | Date | |
| CS phụ trách | Person | |
| Chân dung | Select | Growing Operator / Scaling CX Lead |
| Plan hiện tại | Select | Free / Basic / Pro / Plus |
| TLDV recording | URL | Link recording sau call |
| Follow up status | Select | Chưa làm / Đang làm / Done |
| Insight gửi PM | Checkbox | ☐ Đã gửi chưa |

---

## Body của mỗi record (viết tự do)

### Pain point nghe được
*Ghi đúng ngôn ngữ merchant nói — không paraphrase. Ví dụ: "Tôi mất sale mỗi tối vì không ai reply sau 5h."*

### Insight cho product
*Những gì merchant muốn mà Chatty chưa có hoặc chưa rõ là có. Đây là phần PM cần đọc.*

### Next step đã hứa
| Việc cần làm | Deadline | Done? |
|-------------|----------|-------|
| | | ☐ |
| | | ☐ |

### Ghi chú thêm
*Bất cứ điều gì không fit vào các mục trên.*

---

## Views nên tạo

| View | Filter | Dùng để |
|------|--------|---------|
| **All Calls** | Không filter | Xem toàn bộ |
| **Cần follow up** | Follow up status = Chưa làm | CS check hàng ngày |
| **Insight chưa gửi PM** | Insight gửi PM = ☐ | Liz hoặc CS review cuối tuần |
| **Theo chân dung** | Group by Chân dung | So sánh pattern giữa 2 nhóm |

---

## Quy trình CS điền sau call

1. Mở Notion database → New record
2. Điền properties (2 phút)
3. Điền body — pain point + insight + next step (5 phút)
4. Paste link TLDV recording vào property
5. Set Follow up status = "Chưa làm"
6. Làm xong next step → tick Done + đổi status = "Done"

---

*Outline này dùng để setup Notion. Sau khi tạo xong, paste link database vào [handle-icp-discovery-call.md](handle-icp-discovery-call.md) và [README.md](README.md).*
