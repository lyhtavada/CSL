# Tư vấn tính năng/ plan phù hợp cho MC Joy

Category: General

## 1. Nguyên tắc chung

- Joy có **team Sales** chuyên phụ trách tư vấn gói và giá.
    - Sales Manager: @Nghĩa Đặng (Toby)
    - Sales executive: @Bùi Công Minh @Nguyễn Ngọc Minh
- CS **không tự ý tư vấn plan hoặc giá** cho merchant, vì:
    - Có thể chưa hiểu hết business case & nhu cầu thực sự của MC.
    - Dễ đưa ra gợi ý sai → merchant cảm thấy bị lừa dối → mất trust.

---

## 2. Flow xử lý

### Bước 1: Khi MC có nhu cầu tư vấn plan/giá

- CS gửi link để MC book call với team Sales.
- Nếu MC đã book → Sales sẽ take care trong call.
- CS tiếp tục hỗ trợ các câu hỏi khác (usage, setup, bug).

### Bước 2: Nếu MC không muốn book call

- CS forward case lên **#sales-cs-success** và tag PM @Nghĩa Đặng (Toby)
- Sales team sẽ follow-up trực tiếp với merchant.

### Bước 3: Trường hợp Merchant cần gấp

- Nếu MC hỏi rõ ràng về một tính năng cụ thể → CS chỉ cần confirm **tính năng đó thuộc plan nào**.
- CS **tuyệt đối không đoán hay nói sai** → tránh merchant cảm giác bị misleading.
- Nếu chưa chắc → escalate ngay lên Sales/PM để confirm.

---

## 3. Template hỗ trợ (English)

**a. Khuyến khích book call:**

```
Thank you for your interest in exploring the best plan for your business.

To make sure you get the most accurate advice tailored to your needs, our Sales team is 
available for a quick call.

You can book a time here: !joy-demo-call

Meanwhile, I’m happy to help with any product questions you may have.

```

**b. Merchant không muốn call:**

```
I understand if you prefer not to schedule a call right now.
In that case, I’ll forward your request to our specialized team so they can follow up with 
you directly.

```

**c. Merchant hỏi gấp về một tính năng cụ thể:**

```
That feature is available on the [Advanced/Enterprise] plan.
If you’d like, I can connect you with our specialized team for more details on pricing and the best setup for

```