---
name: screenshot
description: Chụp màn hình bất kỳ trang web nào (kể cả trang cần đăng nhập — Shopify admin, app Chatty/Joy, Crisp, cs2, analytics) rồi trả về link ảnh public để nhúng Notion/doc/Slack. Dùng khi Liz nói "/screenshot", "chụp màn hình trang X", "lấy ảnh màn hình cho doc", "screenshot cái này", hoặc khi Betty đang viết doc/help-center mà cần ảnh minh hoạ.
version: 1.0.0
---

# /screenshot

Chụp màn hình qua Chrome + upload lên backend Flameshot của Avada
(`capture-api.avada.io` → link `capture.avada.io`), trả về link nhúng được.

Tool: `~/CSL/tools/browser/` — `shot.mjs` (chụp), `upload.py` (upload),
`start-chrome.sh` (bật Chrome debug). README ở đó là nguồn chi tiết nhất.

## Chọn chế độ TRƯỚC khi chạy

| Trang | Chế độ | Cần Liz làm gì |
|-------|--------|----------------|
| Public (help.chatty.net, joy.so, App Store, docs, web đối thủ) | `--launch` | không |
| Cần đăng nhập (Shopify admin, app Chatty/Joy, Crisp, cs2, analytics) | attach CDP | bật Chrome debug 1 lần/ngày |

## Flow

### 1. Trang public — chạy thẳng

```bash
cd ~/CSL/tools/browser
node shot.mjs --launch --url 'https://help.chatty.net/ai/chatty-lab/' --full --out ten-anh.png
```

### 2. Trang cần đăng nhập

```bash
~/CSL/tools/browser/start-chrome.sh     # tự báo nếu đã chạy sẵn
node shot.mjs --list                    # xem Betty thấy tab nào
node shot.mjs --tab 2 --out ten-anh.png
```

Nếu `--list` chỉ ra tab trống → Liz đang đăng nhập nhầm ở Chrome thường.
**Đừng bắt Liz tự tìm cửa sổ** — mở sẵn trang cần login trong Chrome của Betty
rồi `bringToFront()`, cửa sổ nào nhảy lên là cửa sổ đó:

```bash
node shot.mjs --url 'https://admin.shopify.com/' --no-upload --out probe.png
```

Bước 2FA thì để Liz tự nhập, Betty không đụng vào. Xong 1 lần là profile nhớ.

### 3. Bấm/gõ trước khi chụp

Lặp `--do` bao nhiêu lần cũng được, chạy đúng thứ tự. Selector nhận CSS,
`text=...`, `:has-text(...)` — nên tả theo chữ hiện trên màn hình là được.

```bash
node shot.mjs --tab 2 \
  --do 'click:text=Settings' --do 'waitfor:.modal' --do 'wait:800' \
  --element '.modal' --out setting-modal.png
```

`click` `fill:sel=val` `press:Enter` `select:sel=val` `hover` `scrollto`
`waitfor` `wait:ms` `goto:url`. Bước nào fail thì dừng và in đúng bước sai.

### 4. Làm ảnh sạch cho doc

- `--element '.pricing-table'` — chỉ chụp 1 khối, không chụp cả trang
- `--hide '.crisp-client'` — ẩn widget chat / banner cookie (lặp được)
- `--mask '.customer-name'` — bôi hộp che dữ liệu (lặp được)
- `--viewport 1200x800`, `--full`, `--clip x,y,w,h`, `--no-upload`

Output in ra 2 link: `page:` (gửi người khác) và `direct:` (nhúng Notion/markdown).

## Luật bắt buộc

1. **Chỉ chụp dev/test store.** Store thật sẽ lộ tên sản phẩm, domain, đơn hàng
   của merchant — doc nội bộ cả team đọc. Buộc phải chụp thì `--mask` chỗ nhạy cảm.
2. **Ảnh upload là public theo link.** Ai có link đều xem được, không cần đăng nhập.
   Cân nhắc trước khi chụp dashboard doanh thu / thông tin khách.
3. **Luôn tự xem lại ảnh bằng Read trước khi đưa link cho Liz.** Trang SPA nặng
   (Shopify admin, cs2) hay ra ảnh trắng hoặc lỗi 500 — đưa link mà không xem là
   đưa nhầm ảnh hỏng.

## Bẫy đã gặp (đừng đạp lại)

- **Chrome 136+ chặn `--remote-debugging-port` trên profile mặc định.** Lệnh cũ
  `open -a "Google Chrome" --args --remote-debugging-port=9222` mở lên nhưng cổng
  câm. Bắt buộc dùng profile riêng → đó là việc `start-chrome.sh` làm.
- **Không bao giờ `browser.close()` khi đang attach** — nó đóng sạch tab Liz đang
  mở. `shot.mjs` đã xử lý (hàm `finish()`), nhưng nếu viết script Playwright ad-hoc
  thì phải tự nhớ.
- **Trang SPA cần chờ lâu hơn** — mặc định `--wait 1500` không đủ cho Shopify
  admin, dùng `--wait 9000` hoặc `--do 'waitfor:<selector>'`.
- **Ảnh lazy-load** — `--full` đã tự cuộn hết trang trước khi chụp. Video/iframe
  nhúng vẫn có thể ra khoảng trắng, chỗ đó chụp tay.
- **Lỗi 500 của Shopify** không phải lỗi tool — thử lại hoặc đổi trang.
