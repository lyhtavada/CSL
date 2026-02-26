# Logic hiển thị Last activity trong Inbox

Category: Inbox
PIC: Nguyễn Thị Phượng

### **Problem / Request:**

Khách hàng thắc mắc về hiển thị Last activity của conversations trong Inbox

---

### Logic:

App sẽ tính **Last activity** dựa trên thời điểm hoạt động cuối cùng (last message, reply, hoặc event) trong conversation, sau đó hiển thị thời gian theo quy tắc sau:

| Khoảng thời gian từ Last activity | Cách hiển thị | Ví dụ minh họa |
| --- | --- | --- |
| **0 – 24 giờ** | Hiển thị **số giờ** kể từ khi xảy ra activity  | [https://prnt.sc/RbUs1ZDBuq_j](https://prnt.sc/RbUs1ZDBuq_j) |
| **24 – 48 giờ** | Hiển thị **“Yesterday”** | [https://prnt.sc/o1msQW6HymNu](https://prnt.sc/o1msQW6HymNu) |
| **> 48 giờ** | Hiển thị **số ngày** kể từ last activity | [https://prnt.sc/Kywdd0UJQ0I2](https://prnt.sc/Kywdd0UJQ0I2) |

### Ví dụ minh họa:

- **Conversation Start:** 10/08/2025 00:34
- **MC reply:** 10/08/2025 00:53
- **Resolve:** 10/08/2025 00:53
- **Reopen conversation:** 10/08/2025 20:27
- **MC truy cập lại conversation:** 10/10/2025 14:04

Khoảng thời gian từ **Reopen (10/08 20:27)** đến khi MC try cập lại conversation để phản hồi customers **(10/10 14:04)** là **1 ngày 17 giờ 37 phút**. Vì thời gian này vẫn nằm trong khoảng 24–48 giờ, nên app sẽ hiển thị trạng thái là “Yesterday” ([https://prnt.sc/iGvGUw5Zmt-s](https://prnt.sc/iGvGUw5Zmt-s))