# Có thể sync được birthday data từ Shopify hay ko?

Category: Integrations

## Problem/ Request

Có thể đồng bộ dữ liệu sinh nhật (birthday) từ Shopify sang app Joy hay không?

---

## Causes

Một số store đã thu thập ngày sinh của khách hàng và lưu dưới dạng Metafield trong Shopify, muốn sử dụng dữ liệu này để chạy các chương trình tích điểm hoặc gửi ưu đãi sinh nhật trong app Joy mà ko cần phải import thủ công ngày sinh nhật.

---

## Flow

Nếu birthday được lưu dưới dạng **Shopify Metafield** cho khách hàng, bạn có thể đồng bộ dữ liệu này với app Joy bằng cách:

![image.png](C%C3%B3%20th%E1%BB%83%20sync%20%C4%91%C6%B0%E1%BB%A3c%20birthday%20data%20t%E1%BB%AB%20Shopify%20hay%20ko/image.png)

1. Truy cập vào **Joy app > Settings**.
2. Bật tuỳ chọn **Sync Shopify metafield to Joy data**.
3. Nhập **tên Metafield** chứa ngày sinh (ví dụ: `custom.birthday`).

![image.png](C%C3%B3%20th%E1%BB%83%20sync%20%C4%91%C6%B0%E1%BB%A3c%20birthday%20data%20t%E1%BB%AB%20Shopify%20hay%20ko/image%201.png)

1. Lưu cài đặt.

App Joy sẽ tự động đọc giá trị Metafield và cập nhật vào trường sinh nhật trong hồ sơ khách hàng của app.