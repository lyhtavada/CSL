# App không tính điểm cho order khi customer pay order bằng cả credit card và store credit

Category: Reward programs
PIC: Phạm Khánh Ly

### ✏️ Scenario

MC xác nhận có exclude phương thức thanh toán store credit khỏi Place Order program, nhưng nhận thấy có trường hợp customer chỉ trả 1 phần bằng store credit, còn lại trả bằng credit card thì customer ko nhận được điểm từ phần trả bằng credit card.

### ⁉️Possible causes

Với các plan free và Essential, thường MC sẽ chọn exclude bằng option này: [https://capture.avada.io/i/aIbUYPE3fz0j](https://capture.avada.io/i/aIbUYPE3fz0j). Khi đó, bất kể là customer pay full hay partially bằng store credit thì app cũng sẽ exlude hết cả order, không tính điểm.

### ➡️ Support flow

- Xác nhận xem MC ở plan nào. Nếu khách dùng Free hoặc Essential thì giải thích như trên cho khách là được.
- Nếu khách là Advanced hoặc Ultilmate thì check xem khách dùng Rule Engine chưa, nếu chưa thì khuyến khích họ dùng và tick option này trong Rule Engine: [https://capture.avada.io/i/K1oIyJrmxOpg](https://capture.avada.io/i/K1oIyJrmxOpg)

### 🪞 References

### Tips & Tricks (optional)