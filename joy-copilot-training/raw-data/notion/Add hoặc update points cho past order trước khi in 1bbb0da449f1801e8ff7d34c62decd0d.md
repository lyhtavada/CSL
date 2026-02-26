# Add hoặc update points cho past order trước khi install app hoặc do thay đổi rule của Place order (trong khoảng thời gian nào đó)

Category: Reward programs

### Problem/ Request

MC muốn cộng điểm cho các order trước khi cài app (trong khoảng thời gian nào đó)

---

### Possible causes

- App chỉ tính điểm cho các order placed từ thời điểm cài app
- MC muốn tính cả cho các order trc khi cài app để existing customer có sẵn điểm luôn

<aside>
💡

**Bởi vì việc update lại điểm cho đơn hàng cũ khá tốn resource và mất thời gian xử lý kỹ thuật**, nhưng hiệu quả mang lại không thực sự cao hoặc rõ ràng (việc cộng lại điểm theo đơn cũ không đảm bảo rằng khách cũ sẽ quay lại hay engage), nên CS có thể đề xuất những cách tiếp cận khác, đơn giản và tối ưu hơn.

</aside>

### Support flow

- **CS dùng shortcut `!reason-for-points-update`** để hỏi lý do MC muốn update points cho old orders:

### **Tùy vào câu trả lời của MC**, chia làm **2 hướng xử lý**:
🔷 **TH1: MC chỉ muốn cộng điểm cho khách cũ (trước khi install app) để khuyến khích họ quay lại**

- **CS có thể đề xuất gợi ý đơn giản, không cần thao tác kỹ thuật, CS dùng shortcut `!fixed-points-for-old-customers` .** Đây chỉ là 1 trong những approach, CS cần lựa theo lý do update point của MC để đưa ra solution phù hợp (có thể tham khảo GPT hoặc CSL nếu cần thiết).
    - Tặng mỗi người một lượng điểm cố định (VD: 100–200 điểm) bằng CSV adjustment
    - Gợi ý MC gửi 1 newsletter tới customer cũ về loyalty program
    
    → Nếu MC đồng ý với phương pháp add 1 số lượng point cho old customer, CS chủ động xin list customer đó và giúp MC adjust point bằng CSV import. Dưới đây là [1 convo để tham khảo](https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/session_aabcc1fa-84a0-4559-967e-06a51234960d/): 
    
    ![image.png](Add%20ho%E1%BA%B7c%20update%20points%20cho%20past%20order%20tr%C6%B0%E1%BB%9Bc%20khi%20in/image.png)
    
- Ngoài việc xử lý yêu cầu điểm, **CS có thể chủ động review lại chương trình Reward hiện tại của MC**, từ đó đưa ra các đề xuất để:
    - Tăng tính hấp dẫn cho chương trình
    - Giúp MC **thu hút & giữ chân khách hàng** một cách chủ động hơn
    - Tạo nhiều **điểm chạm tương tác (engagement touchpoints)** trong hành trình khách hàng

**✅ CS có thể gợi ý một số cách earn points đơn giản nhưng hiệu quả như:**

| Program | Gợi ý mô tả |
| --- | --- |
| **Create account** | Thưởng 100–200 điểm khi khách tạo tài khoản lần đầu |
| **Place an order** | Mỗi 10k chi tiêu = 1 điểm (hoặc tuỳ conversion rate của store) |
| **Follow social media** | Tặng điểm khi follow Instagram, Facebook… |
| **Birthday gift** | Tặng điểm hoặc mã giảm giá vào dịp sinh nhật khách |
| **Review a product** | Tặng điểm khi viết review (kết hợp với Air Product Reviews nếu có) |
| **Referral program** | Referrer nhận điểm, referee nhận discount 10% khi đặt đơn đầu tiên |
| **Visit website** | Gợi ý chỉ áp dụng cho những brand muốn tăng lượt truy cập cụ thể |

### **🔹 Trường hợp 2: MC vẫn muốn update điểm dựa theo order thật (có thể do mới đổi rule của place order hoặc do MC quên chưa chuyển program qua Live mode)**

1. CS hỏi rõ các thông tin sau, dùng shortcut **`!points-update-info` :**
    - Khoảng thời gian các đơn cần cộng điểm
    - Có cần update lại VIP tier không (nếu MC đang enable VIP tier)
2. **Thao tác trong hệ thống**:
- CS/TS vào **Dev_zone > Dev tool > Update points for past orders**.
    
    ![image.png](Add%20ho%E1%BA%B7c%20update%20points%20cho%20past%20order%20tr%C6%B0%E1%BB%9Bc%20khi%20in/image%201.png)
    
- Nhập khoảng thời gian (**Start date** và **End date**).
    
    ⚠️ **Start date** của **Place order** và **Start date** của **VIP Tier program** (nếu MC đang chạy VIP) **phải trùng** với **start date** của **date range** mà MC muốn cập nhật điểm để hệ thống có thể process được.
    
    Nếu không trùng, CS **được phép chủ động** cập nhật start date của Place order và VIP Tier cho đúng.
    
    VD: 
    
    - MC muốn cập nhật điểm cho các đơn hàng trong khoảng: **01/05/2025 – 01/09/2025**.
    - Hiện tại, **Start date của Place order = 01/09/2025**.
    
    ⇒ CS chủ động chỉnh **Start date của Place order về 01/05/2025**. Nếu MC có bật **VIP Tier program**, cũng cần chỉnh **Start date của VIP Tier về 01/05/2025** để đồng bộ.
    
- Sau đó, nhấn **Update Points** và chờ hệ thống xử lý.

<aside>
💡

Tính năng này sẽ tự động cộng lại điểm và cập nhật VIP tier cho các order trong khoảng thời gian được chọn, dựa theo rule hiện tại của Place order và Start date của VIP tier. Hệ thống cũng sẽ lưu lại activity như Place order thông thường.

</aside>

**Lưu ý:** Trong trường hợp MC muốn update points của All-time orders thì CS chỉ cần dùng tính năng Sync point for past order ở Settings.

![image.png](Add%20ho%E1%BA%B7c%20update%20points%20cho%20past%20order%20tr%C6%B0%E1%BB%9Bc%20khi%20in/image%202.png)

1. **Hoàn tất**:
- Sau khi hệ thống chạy xong, CS thông báo lại để merchant kiểm tra.
- CS chủ động nhắc merchant double-check kết quả.