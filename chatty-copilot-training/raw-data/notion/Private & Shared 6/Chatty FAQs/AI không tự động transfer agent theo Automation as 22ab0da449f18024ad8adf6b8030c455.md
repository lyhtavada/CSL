# AI không tự động transfer agent theo Automation assigment setting

Category: AI Assistant
PIC: Nguyễn Thị Phượng

[https://avadaio.slack.com/archives/C07AZNGEVTM/p1751688547926129](https://avadaio.slack.com/archives/C07AZNGEVTM/p1751688547926129)

## **Vấn đề**

Khi AI phát hiện intent của cuộc hội thoại là **"talk to human"**, customer xác nhận và đồng ý transfer sang human support, nhưng AI không tự động assign cuộc hội thoại cho agent theo đúng Automation Settings mà merchant (MC) đã cài.

---

## **Nguyên nhân phổ biến**

- MC đang chọn Assignment method là Manual assignment, nhưng chưa assign agent nào cho cuộc hội thoại.

→ Khi đó, dù có agent/member nào trong team trả lời thì cuộc hội thoại vẫn giữ trạng thái **"Unassigned"**.

- Lỗi logic Automatic Assignment từ phía app

---

## Cách xử lý theo từng trường hợp Assignment Method:

1️⃣ **Trường hợp 1: MC cài đặt Assignment method là “Manual assignment”.** 

- Hệ thống không tự động assign agent, và cuộc hội thoại chỉ được assign khi MC hoặc thành viên team chủ động assign thủ công. Nếu cuộc hội thoại không được assign thủ công, conversation sẽ vẫn ở trạng thái **"Unassigned"**.

![image.png](AI%20kh%C3%B4ng%20t%E1%BB%B1%20%C4%91%E1%BB%99ng%20transfer%20agent%20theo%20Automation%20as/image.png)

- ***Lưu ý*:** Khi cuộc hội thoại đã được assign cho một agent, nếu member khác trả lời (trường hợp team có nhiều members) thì cuộc hội thoại vẫn giữ nguyên assignment, không chuyển sang người mới.

![image.png](AI%20kh%C3%B4ng%20t%E1%BB%B1%20%C4%91%E1%BB%99ng%20transfer%20agent%20theo%20Automation%20as/image%201.png)

➡️ **Cách CS xử lý**: Nhờ MC chủ động assign cuộc hội thoại cho một thành viên trong team để phản hồi khách hàng. 

<aside>
💡

Nếu MC không có quy trình rõ ràng để assign thủ công thì **nên dùng Automatic Assignment**

</aside>

2️⃣ **Trường hợp 2: MC cài đặt Assignment method là “Automatic assignment to each member in order”**

- Đây là chế độ assign tự động theo vòng lặp (round-robin). Mỗi khi có cuộc trò chuyện mới, hệ thống sẽ lần lượt gán cho từng member trong team, và cuộc hội thoại không rơi vào trạng thái **"Unassigned"**. Danh sách member được sắp xếp theo thứ tự đã lưu, và cứ hết danh sách thì quay lại từ đầu.
- Trong cài đặt Reassign conversations, khi chọn *Conversations stay with assigned member (or stay unassigned)* → Nếu member khác trả lời thì conversation vẫn giữ nguyên assignment, không chuyển người mới

![image.png](AI%20kh%C3%B4ng%20t%E1%BB%B1%20%C4%91%E1%BB%99ng%20transfer%20agent%20theo%20Automation%20as/image%202.png)

- Nếu không bật tùy chọn đó, hệ thống sẽ assign lại cho người trả lời đầu tiên nếu khác với người được auto-assign ban đầu.

➡️ **Cách CS xử lý**: Kiểm tra và đảm bảo MC đã cài đặt Automation Settings. Trong trường hợp MC đã cài đặt đúng nhưng vẫn có lỗi cuộc hội thoại hiện **"Unassigned",** CS cần xin thông tin conversation để forward lại cho TS và dev kiểm tra thêm.