# Các yêu cầu liên quan đến Billing và Refund

Owner: Ly Hoàng
Created time: September 11, 2024 2:36 PM

> Understand [App charges](https://help.shopify.com/en/manual/your-account/manage-billing/your-invoice/apps)
> 

## **CS tìm hiểu lý do MC muốn cancel subscription hoặc refund:**

Trước khi nhận request, CS cần hiểu rõ lý do MC yêu cầu. Một số lý do phổ biến:

- **Bị tính phí ngoài ý muốn** (sau khi đã gỡ app hoặc trong thời gian trial)
- **Sự cố về subscription**
- **App không đáp ứng kỳ vọng**
- **Vấn đề kỹ thuật với app** (→ Trong trường hợp này, CS cần chủ động hỗ trợ khắc phục trước)

➡️ xác nhận vấn đề với MC, dùng shortcut **`!cancel-reason`** 

<aside>
💡

**Khi khách hàng phản ánh bị charge mà không upgrade,** CS nên **chủ động làm rõ** với khách hàng để xác định nguyên nhân trước khi xử lý yêu cầu.

- Làm rõ rằng app **không tự động nâng cấp**. Mọi nâng cấp đều cần **sự phê duyệt từ Shopify Admin**.
- Có thể khách hàng đã **đăng ký trial** nhưng **quên hủy trước khi kết thúc trial**, dẫn đến việc **tài khoản bị tính phí khi chu kỳ bắt đầu**.
</aside>

### Khi MC chỉ đơn giản không muốn tiếp tục dùng app hoặc subscribe nhầm (ko phải lý do liên quan đến app)

### 1. CS hướng dẫn KH downgrade app về free

- Hướng dẫn theo shortcut có sẵn
- CS kiểm tra lại plan 1 lần nữa để xác nhận KH đã downgrade về Free rồi

### 2. CS thu tập thông tin:

- Xin đầy đủ các thông tin sau, dùng shortcut **`!billing-details`** :
    - Ảnh chụp hóa đơn có đầy đủ: **tên app, chu kỳ bill, số tiền**
        
        → Đảm bảo đúng định dạng: 
        
        ![image.png](C%C3%A1c%20y%C3%AAu%20c%E1%BA%A7u%20li%C3%AAn%20quan%20%C4%91%E1%BA%BFn%20Billing%20v%C3%A0%20Refund/image.png)
        
        Hoặc
        
        ![image.png](C%C3%A1c%20y%C3%AAu%20c%E1%BA%A7u%20li%C3%AAn%20quan%20%C4%91%E1%BA%BFn%20Billing%20v%C3%A0%20Refund/image%201.png)
        
        Hoặc (Shopify đã thay đổi format hiển thị bill trong Shopify Admin cho một số store: Bill chỉ hiển thị **tên app và số tiền,** TH này **không yêu cầu** khách hàng phải tìm bill có billing cycle theo format cũ nữa)
        
        ![image.png](C%C3%A1c%20y%C3%AAu%20c%E1%BA%A7u%20li%C3%AAn%20quan%20%C4%91%E1%BA%BFn%20Billing%20v%C3%A0%20Refund/image%202.png)
        
    - CS có thể hướng dẫn KH tìm bill ở Shopify admin > Settings > Billing
        
        ![image.png](C%C3%A1c%20y%C3%AAu%20c%E1%BA%A7u%20li%C3%AAn%20quan%20%C4%91%E1%BA%BFn%20Billing%20v%C3%A0%20Refund/image%203.png)
        
    - Xác nhận xem MC **đã thanh toán** hóa đơn hay chưa

### 3. CS tạo card:

- CS hẹn KH, dùng shortcut **`!refund-process`**
- Sau khi đã có đủ thông tin và **app đã ở bản Free**, CS tạo card, assign CSL và note lại đầy đủ chi tiết yêu cầu, lý do refund.

### Xử lý khi App không đáp ứng kỳ vọng hoặc xảy ra lỗi trong quá trình sử dụng

**1. Ghi nhận vấn đề & xác định rõ kỳ vọng của MC**

Việc MC không hài lòng có thể đến từ:

- Tính năng không như mong đợi
- Giao diện khó dùng
- Setup khó hoặc MC không biết cách sử dụng

🎯 Mục tiêu: CS cần xác định rõ MC mong muốn app hỗ trợ như thế nào → đưa giải pháp/khắc phục phù hợp **trước khi xử lý refund**.

```jsx
Thanks for your feedback. I’m sorry to hear the app didn’t meet your expectations. Could you please share more details about what you were looking to achieve or what didn’t work as expected? I’d love to help clarify or find a solution that works for you.

```

---

**2. Chủ động đề xuất hỗ trợ & test lại tính năng**

Nếu lỗi thuộc về setup/feature, hoặc MC chưa biết dùng:

- Hướng dẫn lại
- Thu thập thông tin về issue và hỗ trợ MC xử lý issue đó
- Nếu MC đã nắm được tính năng, và các vấn đề đã được giải quyết, khuyến khích MC tiếp tục dùng app (có thể nhắn lên nhóm, tham khảo CSL xem có thể offer discount tháng tới cho MC hay ko).

<aside>
⚠️

Nếu lý do refund là do app không đáp ứng kỳ vọng hoặc gặp lỗi, CS phải chủ động follow-up để xử lý triệt để vấn đề cho merchant, tránh để họ uninstall hoặc cancel app khi vấn đề chưa được giải quyết.

</aside>

**3. Trong trường hợp MC vẫn muốn huỷ và refund**

- Gửi lời xin lỗi
- Xin đầy đủ các thông tin sau, dùng shortcut **`!billing-details`** :
    - Ảnh chụp hóa đơn có đầy đủ: **tên app, chu kỳ bill, số tiền**
        
        → Đảm bảo đúng định dạng: 
        
        ![image.png](C%C3%A1c%20y%C3%AAu%20c%E1%BA%A7u%20li%C3%AAn%20quan%20%C4%91%E1%BA%BFn%20Billing%20v%C3%A0%20Refund/image.png)
        
    - Xác nhận xem MC **đã thanh toán** hóa đơn hay chưa
    - Hướng dẫn MC **downgrade về gói Free** nếu chưa làm để tránh bị charge tiếp

**4. CS tạo card:**

- CS hẹn KH, dùng shortcut **`!refund-process`**
- Sau khi đã có đủ thông tin và **app đã ở bản Free**, CS tạo card, assign CSL và note lại đầy đủ chi tiết yêu cầu.

<aside>
⚠️

CS **KHÔNG được phép** tự ý đồng ý bất kỳ request refund hoặc hỗ trợ nào mà chưa có sự phê duyệt của CSL.
Nếu CS tự ý đồng ý, CS sẽ phải tự chịu trách nhiệm và chi trả cho khoản đó.

</aside>

<aside>

🚧 **Đối với các trường hợp rủi ro cao:**

Sau khi đã giải thích rõ ràng quy trình và chính sách cho khách hàng, nếu khách vẫn không hiểu hoặc không chấp nhận lời giải thích, **KHÔNG tiếp tục tranh luận hoặc trả lời qua lại nhiều lần**. Thay vào đó, hãy **chuyển tiếp request cho CSL/CSM** trên nhóm chung để đưa ra hướng xử lý tối ưu nhất.

</aside>

---

### **Frequently Asked Questions (FAQ)**

**Q: How long will it take to receive my refund (after the refund has been issued)?**

A: Refunds typically take 7-10 business days to appear in your bank account, but this may vary depending on your payment provider.

**Q: Am I eligible for a refund if I uninstalled the app but was still charged?**

A: You are eligible for a refund for the unused days.

**Q: What if I’ve been using the app but now want a refund due to dissatisfaction?**

A: Refund eligibility will depend on the specific circumstances, but we recommend discussing the issue with our support team. We may offer a partial refund or other compensation.

**Q: Can I cancel the refund request once it is submitted?**

A: Once a refund has been processed, it can’t be canceled. However, if you’d like to discuss alternatives (such as using the app for free for a limited time), please contact support.

**Q: Why were they charged after uninstalling the app or downgrading to the Free plan.** 

A: If they uninstalled or downgraded after the billing cycle had already started, they will still receive a full invoice for that cycle.

However, they will be refunded for any unused days within that cycle.

More details: [Handling Customer Questions on Charges After Uninstalling or Downgrading](https://www.notion.so/Handling-Customer-Questions-on-Charges-After-Uninstalling-or-Downgrading-d45544dcb56c4f84b2cf7e7078e125ac?pvs=21) 

**Q: Customer was charged/received an invoice but the app shows the Free plan**

A: It’s possible that the customer uninstalled the app previously, which caused the subscription to be automatically canceled.

More details: [Khách đã bị charge/nhận được invoice nhưng trong app hiện plan Free](https://www.notion.so/Kh-ch-b-charge-nh-n-c-invoice-nh-ng-trong-app-hi-n-plan-Free-febb27908b29497aa496d3ae6db2f756?pvs=21) 

**Q: Khách hàng báo không nhận được tiền refund/credit dù đã quá thời gian 5 ngày làm việc kể từ khi refund được issue**

A: Báo khách check với Shopify và ngân hàng. Giao dịch được thực hiện bởi Shopify, mình không thể check thêm gì nữa

It typically takes between 7 to 10 business days for a refund to be processed. This timeframe depends not only on Shopify’s refund process but also on the bank's processing time on the customer's side.

❌ Không cần đề cập rằng mình sẽ kiểm tra với Shopify nếu khách hàng phản hồi với thái độ bình thường, để tránh mất thời gian không cần thiết.

**Q: Where do I receive the refund?**

A: The refund will be processed through Shopify and returned to the original payment method you used to pay for the app. It typically takes 7–10 business days, depending on your bank or payment provider

**Q: When will I have to pay the subscription charge?**
A: You will be charged on your regular Shopify billing date, together with your Shopify subscription and any other charges (e.g. app charges). You can find more details at https://help.shopify.com/en/manual/your-account/manage-billing/billing-charges/types-of-charges/third-party-charges/app-charges

**Q: Where can I see the app subscription charges?**
A: You can view all charges, including app subscriptions, in your Shopify Admin under Settings > Billing > Bills. Each bill shows a breakdown of charges.

**Q: Why might a merchant receive two bills from Shopify in the same month?**

Because their charges (such as third-party transaction fees or app charges) exceeded their billing threshold before the regular billing date. More details are at https://help.shopify.com/en/manual/your-account/manage-billing/managing-your-bills/viewing-your-bills/billing-cycles-thresholds#about-billing-thresholds

**Q: Why am I being billed two times for the same 30-day billing cycle for the same app?**

- Ask the merchant to provide a screenshot of the charge breakdown
    - If the charges are for two different billing periods, explain:
        
        You’re not being double charged for the same app within one cycle. The two charges are for different subscription cycles. You can check the charge breakdown in your bill to see the details. Since Shopify manages how charges are added to your bill, if you’d like further clarification on why they appear in the same bill, I recommend contacting Shopify Support directly.
        
    - Others: check with CSL
    

**Q: Why does a payment fail?**

A: A payment might fail for some of the following reasons:

- The credit card that you have on file expired.
- Your account has no payment method on file.
- Your payment method has insufficient funds.
- You aren't using a valid credit card from Mastercard, Visa, or American Express to pay your Shopify bills.
- Your credit card doesn't allow for recurring payments in USD.

For more details: https://help.shopify.com/en/manual/your-account/manage-billing/billing-charges/frozen-store