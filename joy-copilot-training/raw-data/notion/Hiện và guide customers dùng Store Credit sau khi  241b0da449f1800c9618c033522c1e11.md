# Hiện và guide customers dùng Store Credit sau khi tạo flow

Category: Integrations, Reward programs
PIC: Trương Cảnh Huy

### **LƯU Ý:** 
Store Credit là tính năng native của Shopify, trigger action của Joy trong Shopify Flow chỉ hỗ trợ MC add tự động, tạo cảm giác được Cash Back cho customers chứ mình không interfere/customize được hơn.

Problem/ Request:

MC quan tâm flow store credit và đã set up xong trong Shopify Flow, tuy nhiên MC chưa rõ cách customers sẽ check và dùng store credit như thế nào.

---

### Support flow:

**Step 1:** Bật tính năng store credit trong Shopify Settings > Customer Account:

![image.png](Hi%E1%BB%87n%20v%C3%A0%20guide%20customers%20d%C3%B9ng%20Store%20Credit%20sau%20khi%20/image.png)

**Step 2:** Sau đó có thể bắt đầu check store credit như sau

- **Backend:** có thể check và điều chỉnh thủ công (nếu cần thiết) trong profile của Shopify Customers:

![image.png](Hi%E1%BB%87n%20v%C3%A0%20guide%20customers%20d%C3%B9ng%20Store%20Credit%20sau%20khi%20/48fe3e23-792e-460e-bc51-d4ca26ff5361.png)

- **Frontend:** Check trong profile page > payment methods:

![image.png](Hi%E1%BB%87n%20v%C3%A0%20guide%20customers%20d%C3%B9ng%20Store%20Credit%20sau%20khi%20/image%201.png)

- Checkout: store credit sẽ hoạt động như một phương thức thanh toán phụ trợ cho phương thức thanh toán chính (giống như xu của Shopee). Khi tick chọn sẽ dùng toàn bộ credit để trừ vào giá trị đơn hàng giống như được discount

![image.png](Hi%E1%BB%87n%20v%C3%A0%20guide%20customers%20d%C3%B9ng%20Store%20Credit%20sau%20khi%20/image%202.png)

Related docs: [https://help.joy.so/integrations/integrate-with-shopify-flow/shopify-flow-store-credit#store-credit-formula-cheat-sheet](https://help.joy.so/integrations/integrate-with-shopify-flow/shopify-flow-store-credit#store-credit-formula-cheat-sheet)