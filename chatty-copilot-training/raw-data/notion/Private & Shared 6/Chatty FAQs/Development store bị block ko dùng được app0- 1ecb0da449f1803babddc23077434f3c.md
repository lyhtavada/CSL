# Development store bị block ko dùng được app0-

Category: Genaral

## **Vấn đề/Yêu cầu**

Không thể sử dụng app Joy trên development store – sau khi cài app, khi mở app sẽ hiện trang **Not Found**.

---

## **Nguyên nhân**

App hiện tại **không hỗ trợ truy cập trên một số development store**, đặc biệt là những store được sử dụng bởi bên thứ ba để test app hoặc dịch vụ.

Hệ thống sẽ tự động **chặn (block)** quyền truy cập app nếu email merchant thuộc danh sách không được hỗ trợ, bao gồm các domain sau:

- `@tidio.com`
- `@intercom.com`
- `@firegroup.io`
- `@flowio.app`
- `@beae.com`
- `@fireapps.vn`
- `@channelwill.cn`
- `@bsscommerce.com`
- `@amasty.com`
- `@secomus.com`
- `@appsfinal.com`
- `@omegatheme.com`
- `@loox.io`
- `@samita.io`

---

## **Quy trình xử lý**

1. Kiểm tra email đăng ký của merchant trên store.
2. Nếu email thuộc danh sách blacklist như trên, CS ko cần tiếp tục support, có thể resolve conversation.