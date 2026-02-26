# Xử lý yêu cầu tạo Place Order Program cho First Order only

Category: General
PIC: Đỗ Minh Quân

<aside>
📌

**Lưu ý**: guide dưới đây được viết cho trường hợp customer ****sử dụng Rule engine và có thể tạo nhiều program với điều kiện phức tạp (liên quan đến customer tag)

</aside>

Khách hàng đang sử dụng Joy Loyalty (gói Advanced trở lên) và có nhu cầu tạo một chương trình “Place Order” riêng chỉ áp dụng cho đơn hàng đầu tiên của khách.

Mục tiêu là để thiết lập logic reward khác biệt cho first order, tách biệt hoàn toàn với các reward “Place Order” khác đang có trong chương trình loyalty hiện tại.

## I. Câu hỏi đầu tiên: “First order” được tính theo Shopify hay theo App?

Câu hỏi này phải được hỏi trước, vì nó quyết định toàn bộ hướng setup.

Có 2 trường hợp:

1. Theo Shopify order history
2. Theo logic riêng của App

Chỉ sau khi xác định rõ trường hợp này mới tiếp tục các bước sau.

## II. Trường hợp 1: First Order theo Shopify

Áp dụng khi:

- First order là đơn hàng thật sự đầu tiên trên Shopify
- Dựa vào số lượng order thực tế của customer

### 1. Câu hỏi thêm

- **Program này có stack với các program khác không?**
    
    ![image.png](X%E1%BB%AD%20l%C3%BD%20y%C3%AAu%20c%E1%BA%A7u%20t%E1%BA%A1o%20Place%20Order%20Program%20cho%20First%20Or/image.png)
    
    - Có stack (MC muốn customer place order lần đầu tiên có thể nhận >1 lần reward)
        
        → chỉ cần tạo 01 First Order Program, với setting allow stacking (không tick vào option “Stop giving rewards after this program”)
        
    - Không stack → có hai trường hợp:
        - Cần tạo riêng program cho subsequent orders (program áp dụng cho các order sau đó)
            - First order: để priority cao nhất + không allow stacking
            - Subsequent orders: priority thấp hơn + có thể allow stacking hoặc không
        - Không cần tạo riêng program cho subsequent orders: tạo 01 First order program với priority cao nhất và không allow stacking
- **Xử lý customer cũ thế nào?**
    
    Cần giải thích rõ cho MC:
    
    > Customer đã từng mua (có nhiều hơn 01 order) sẽ không được tính first order nữa.
    > 
    
    Hỏi xem MC có nhu cầu adjust point cho những customer này không?
    

### 2. Cách setup chuẩn

**Bước 1: Tạo Segment**

Sử dụng segment có sẵn của Shopify:

> Customers who have purchased at least once
> 

Segment sẽ tự động update khi customer có ≥1 order.

![image.png](X%E1%BB%AD%20l%C3%BD%20y%C3%AAu%20c%E1%BA%A7u%20t%E1%BA%A1o%20Place%20Order%20Program%20cho%20First%20Or/image%201.png)

**Bước 2: Shopify Flow - Tạo flow để add Tag**

Trigger:

> Customer joined segment (Customers who have purchased at least once)
> 

Action:

> Add customer tags (ví dụ: `ordered_before`)
> 

Mục đích:

- Đánh dấu customer đã từng mua
- Làm điều kiện cho program phía sau

Lưu ý:

- Customer cũ trong segment sẽ không được auto tag
- Cần bulk edit thủ công nếu cần

![image.png](X%E1%BB%AD%20l%C3%BD%20y%C3%AAu%20c%E1%BA%A7u%20t%E1%BA%A1o%20Place%20Order%20Program%20cho%20First%20Or/image%202.png)

**Bước 3: Setup Programs**

Tuỳ từng trường hợp, có thể cần tạo đến 02 program:

1. **First Order Program**
    - Priority: cao nhất (1)
    - Stop giving rewards after this program: ON
    - Condition: Customer không có tag
2. **Subsequent Orders Program**
    - Priority: thấp hơn
    - Stop giving rewards after this program: ON/OFF (không bắt buộc)
    - Condition: Customer có tag

### 3. Logic hoạt động

Luồng thực tế:

1. Customer đặt order đầu tiên (chưa có tag)
2. App ghi nhận và reward theo First order program
3. Flow add tag sau khi customer vào segment
4. Các order sau sẽ bị nhận diện là subsequent, do lúc này customer đã có tag

⇒ Dùng điều kiện “at least once” là hợp lý vì tag sẽ được add ngay sau order đầu tiên. Còn nếu sử dụng segment “more than once” thì đến khi place order thứ 2 thì customer mới được add tag.

### 4. Lưu ý quan trọng

- Setup này áp dụng ngay cho toàn bộ store
- Customer đã từng mua trước đó sẽ không được tính first order
- Bắt buộc phải confirm với MC về việc adjust point

## IV. Trường hợp 2: First Order = Theo App (Logic riêng)

Áp dụng khi:

- Không dựa vào Shopify order history
- Theo order đầu tiên được app ghi nhận

### 1. Định hướng xử lý

Sử dụng Shopify Flow để xử lý và tính reward cho “first order”; các order khác có thể sử dụng program trong app như bình thường.

### 2. Setup cơ bản bằng Shopify Flow

Trigger:

> Order created
> 

Condition

> Customer does NOT have tag `ordered_before`
> 

Actions:

- Không có tag:
    1. Adjust point hoặc adjust credit (action của app)
    2. Add customer tag `ordered_before`
- Có tag: kết thúc flow, không có action tiếp theo

Mục đích:

- Reward first order bằng Flow
- Đảm bảo chỉ chạy và trigger reward bởi app 1 lần
- Không phụ thuộc Shopify history

![image.png](X%E1%BB%AD%20l%C3%BD%20y%C3%AAu%20c%E1%BA%A7u%20t%E1%BA%A1o%20Place%20Order%20Program%20cho%20First%20Or/image%203.png)

![image.png](X%E1%BB%AD%20l%C3%BD%20y%C3%AAu%20c%E1%BA%A7u%20t%E1%BA%A1o%20Place%20Order%20Program%20cho%20First%20Or/image%204.png)

### 3. Điều chỉnh trong App Programs

Sẽ có hai trường hợp:

- Program không quan tâm đến first order hay không: setup như bình thường
- Chỉ áp dụng cho subsequent orders: bắt buộc phải thêm điều kiện để chỉ áp dụng cho customer có tag `ordered_before`

## V. Checklist cho CS khi xử lý request

Khi gặp yêu cầu “First Order Program”, luôn check theo thứ tự:

### 1. Xác định nguồn “First Order”

Shopify hay App?

### 2. Xác định stack

Stack hay không stack?

### 3. Xác định customer cũ

Có cần adjust không?

### 4. Chọn hướng setup

- Shopify
- App

### 5. Confirm với MC trước khi triển khai

- Logic áp dụng
- Impact
- Cách xử lý data cũ

## VI. Template câu hỏi gửi Merchant

CS có thể dùng mẫu sau:

1. “First order” sẽ được tính theo Shopify order history hay theo logic riêng của app?
2. Reward first order có được stack với các program khác không?
3. Với các customer đã mua trước đây, có cần điều chỉnh lại point không?
4. Sau first order, các order tiếp theo sẽ áp dụng rule nào?