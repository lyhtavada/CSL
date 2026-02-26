# Exclude orders từ channel khác khỏi usage charge của Joy

Category: Subscription

## Problem

- Joy hiện **tính usage charge dựa trên tất cả Shopify orders** được sync vào store, không phân biệt channel.
- Một số MC có order từ: POS, Marketplace (Amazon, TikTok,…), ERP hoặc app bên thứ 3
- Các order này:
    - MC không muốn phục vụ cho loyalty program.
    - Nhưng vẫn bị tính vào usage charge, gây tăng chi phí.

---

## Possible causes

Về mặt hệ thống:

- Order đã vào Shopify thì Joy vẫn phải đọc và xử lý.
- Mặc định sẽ:
    - Tham gia loyalty program.
    - Bị tính vào usage charge.

<aside>

Thông thường, MC sẽ cảm thấy khó hiểu và thắc mắc tại sao lại tính cả những order này vào usage charge. CS nên chủ động giải thích khéo léo để MC ko thấy đây là lỗi:
*Currently, Joy calculates usage based on all orders synced into Shopify, regardless of the sales channel. That’s why orders from POS or third-party channels are still being counted.*

</aside>

---

## Flow

### Bước 1: Clarify nhu cầu của MC

CS cần confirm rõ với MC:

- Order đến từ channel nào?
- MC có đồng ý việc:
    - Sau khi exclude, order đó **sẽ không tham gia loyalty program** hay không?

> *Just to confirm, are you okay with these orders being completely excluded from the loyalty program so they won’t be counted toward usage anymore?*
> 

Nếu MC vẫn muốn order đó earn point thì **không thể exclude usage**.

---

### Bước 2: Giải thích impact trước khi làm

CS cần nói rõ:

- Exclude = loại order đó khỏi toàn bộ logic của Joy.
- Không chỉ là usage charge, mà cả program.

> *We can help exclude orders from a specific channel. However, please note that once excluded, those orders will not participate in the loyalty program at all. This means they won’t earn points or trigger any rewards.*
> 

---

### Bước 3: Yêu cầu MC setup order tag

CS cần hướng dẫn MC:

- Gắn **một tag cố định** cho tất cả order từ channel đó.
    - Ví dụ: `POS`, `marketplace`, `offline_order`
- Đảm bảo:
    - Tag được tự động gắn cho order mới.
    - Tag nhất quán, không thay đổi tên.

Giải thích rõ:

- System của Joy sẽ **dựa vào tag này để exclude order**.
- Nếu order không có tag, Joy **không thể nhận diện để exclude**.

> *Could you please help apply a consistent tag to all orders from that channel? This tag will be used to exclude those orders from the loyalty program and usage calculation.
Once excluded, orders with that tag will not participate in the loyalty program at all. They won’t earn points or trigger any rewards, and they also won’t be counted toward usage.*
> 

---

### Bước 4: Submit request cho dev team

Ticket cần có:

- Store URL
- Channel/source cần exclude
- Xác nhận: exclude khỏi loyalty program + usage charge
- Thời điểm áp dụng (ASAP)

---

### Bước 5: Follow up với MC

- Báo MC khi dev đã xử lý xong.
- Nhờ MC check các order mới từ channel đó để confirm:
    - Không earn point.
    - Không bị count usage.

> *We’ve excluded the orders from that channel as requested. Please help check newly created orders from this source to confirm they are no longer earning points or counted toward usage.*
>