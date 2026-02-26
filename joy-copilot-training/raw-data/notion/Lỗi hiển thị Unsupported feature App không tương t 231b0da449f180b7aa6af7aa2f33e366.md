# Lỗi hiển thị Unsupported feature: App không tương thích với Markets (Fixed)

Category: General
PIC: Nguyễn Thị Phượng

## Vấn đề

Khi merchant (MC) cài đặt App **Joy Loyalty**, có thể sẽ thấy cảnh báo [**Unsupported features](https://prnt.sc/MKzLrb9BXv7-):** This app is not compatible with **Markets**, which may affect how some features work and lead to incorrect behavior. 

MC sẽ quan ngại rằng App sẽ không hoạt động đúng trên các thị trường (Markets) họ đã thiết lập trong Shopify Admin.

![image.png](L%E1%BB%97i%20hi%E1%BB%83n%20th%E1%BB%8B%20Unsupported%20feature%20App%20kh%C3%B4ng%20t%C6%B0%C6%A1ng%20t/image.png)

## Nguyên nhân

Cảnh báo trên xuất hiện do App chưa cập nhật lên phiên bản Markets and Catalogs API mới nhất **(2025-04)**

Shopify đã bắt đầu triển khai phiên bản Markets mới cho một số store, đặc biệt là các merchant dùng Shopify Plus có thể thử nghiệm qua tính năng Test Drive.

Khi Shopify nâng cấp Markets, các App tương tác với Markets hoặc Catalogs thông qua API cũ **(2025-01 hoặc thấp hơn)** có thể gặp lỗi không mong muốn hoặc không tương thích.

***Bài viết tham khảo:*** [https://community.shopify.dev/t/update-release-of-the-new-shopify-markets-and-related-apis/17549](https://community.shopify.dev/t/update-release-of-the-new-shopify-markets-and-related-apis/17549) 

## **Cách xử lý**

Do cảnh báo hiển thị là mặc định từ hệ thống Shopify với các App chưa cập nhật API mới nhất, nhưng không ảnh hưởng đến chức năng thực tế của App hiện tại. CS nhắn khách tiếp tục cài đặt và sử dụng app như bình thường. Nếu có vấn đề gì phát sinh trong quá trình sử dụng App, liên hệ Support team hỗ trợ để được kiểm tra và xử lý kịp thời. 

**📌 Notes**

- App hiện vẫn hoạt động bình thường, chưa ghi nhận trường hợp nào conflict với Markets.
- Cần cân nhắc cập nhật Markets & Catalogs APIs bản 2025-04 để đảm bảo tương thích hoàn toàn và gỡ cảnh báo từ Shopify. Sau cập nhật, banner cảnh báo sẽ tự động biến mất sau 7 ngày.