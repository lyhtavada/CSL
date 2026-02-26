# Sử dụng function để trigger open, close widget

Category: Chatbox
PIC: Đỗ Minh Quân

Bên cạnh option sử dụng deeplink, app cũng cung cấp sẵn một số function để thực hiện thao tác đóng mở widget thông qua JavaScript function (cho những trường hợp không sửa trực tiếp ở link được, hoặc cần trigger ở vị trí không phải là một link)

## Function chung để đóng/mở

Sử dụng function `avadaFaqTrigger()` để thay đổi trạng thái đang đóng hoặc mở của widget, khi mở lên sẽ quay về trang cũ (Home, Message, Order Tracking hoặc Help).

## Function để đóng widget

Sử dụng function `ChattyJS.closeWidget()` để thay đổi trạng thái của widget thành đóng.

## Function để mở widget

Sử dụng function `ChattyJS.openWidget()` để thay đổi trạng thái của widget thành mở.

Lưu ý: sử dụng function trên sẽ mở widget ở trang cũ (Home, Message, Order Tracking hoặc Help), nếu cần mở cụ thể một trang có thể sử dụng các function sau:

1. `ChattyJS.openWidget('#chatty-home')`  để mở Home
2. `ChattyJS.openWidget('#chatty-chat')`  để mở Message
3. `ChattyJS.openWidget('#chatty-tracking')`  để mở Order Tracking
4. `ChattyJS.openWidget('#chatty-help')`  để mở Help (FAQ)