# tools/browser — Betty chụp màn hình trong Chrome của Liz

Ghép 2 thứ: **Playwright** (điều khiển Chrome) + **backend Flameshot của Avada**
(`capture-api.avada.io` → link `capture.avada.io`). Betty không cần user/pass:
nó attach vào Chrome mà Liz đang đăng nhập sẵn qua CDP.

## Bật 1 lần mỗi khi khởi động máy

```bash
# 1) Thoát hẳn Chrome: Cmd+Q  (bắt buộc, không chỉ đóng cửa sổ)
# 2) Mở lại ở chế độ debug:
open -a "Google Chrome" --args --remote-debugging-port=9222
```

Rồi đăng nhập Shopify / mở app Chatty như bình thường. Chrome vẫn dùng đúng
profile, bookmark, session cũ — chỉ khác là có mở cổng debug ở localhost.

## Dùng

```bash
cd ~/CSL/tools/browser

node shot.mjs --list                          # xem Betty thấy tab nào
node shot.mjs --tab 2 --out knowledge-base.png # chụp tab số 2
node shot.mjs --tab 2 --full                   # full page, cuộn hết
node shot.mjs --tab 2 --clip 0,0,1200,800      # chụp 1 vùng
node shot.mjs --url https://help.chatty.net/ai/chatty-lab/ --full
node shot.mjs --tab 2 --no-upload              # chỉ lưu file, không upload
```

### Bấm / gõ trước khi chụp

Lặp `--do` bao nhiêu lần cũng được, chạy đúng thứ tự viết trên dòng lệnh.
Selector dùng cú pháp Playwright: CSS, `text=...`, `role=...`, `:has-text(...)`.

| Bước | Ý nghĩa |
|------|---------|
| `--do 'click:text=Settings'` | bấm |
| `--do 'fill:#email=a@b.com'` | gõ vào ô input |
| `--do 'press:Enter'` | bấm phím (`press:#q=Enter` cho 1 ô cụ thể) |
| `--do 'select:#plan=pro'` | chọn dropdown |
| `--do 'hover:.menu'` | rê chuột (mở submenu) |
| `--do 'scrollto:h3:has-text("Pricing")'` | cuộn tới |
| `--do 'waitfor:.modal'` | chờ element hiện ra |
| `--do 'wait:2000'` | chờ 2 giây |
| `--do 'goto:https://...'` | sang trang khác |

Bước nào fail thì dừng luôn và in ra bước sai — không chụp ảnh sai rồi mới biết.

```bash
# mở accordion FAQ rồi chỉ chụp đúng khối đó
node shot.mjs --url https://help.chatty.net/ai/chatty-lab/ \
  --do 'click:summary:has-text("Do I have to accept every proposal?")' \
  --do 'wait:600' \
  --element 'details:has(summary:has-text("Do I have to accept every proposal?"))'
```

### Chụp gọn / che dữ liệu

```bash
--element '.pricing-table'     # chỉ chụp 1 element thay vì cả trang
--hide '.crisp-client'         # ẩn hẳn (widget chat, banner cookie) — lặp được
--mask '.customer-name'        # bôi hộp che dữ liệu merchant — lặp được
--viewport 1200x800            # đổi kích thước cửa sổ
```

In ra 2 link:
- `page:` — trang xem ảnh, gửi cho người khác (giống link Flameshot)
- `direct:` — link ảnh trực tiếp, dùng để nhúng vào Notion / markdown

Upload lẻ 1 file có sẵn: `python3 upload.py anh.png`

## Lưu ý

- **Chỉ chụp trên dev/test store.** Screenshot store thật sẽ dính tên sản phẩm,
  domain, data của merchant — doc nội bộ team đọc, không nên có.
- Token upload đọc thẳng từ `~/.config/flameshot/flameshot.ini` nên không lưu
  trùng secret. Override được bằng `CAPTURE_TOKEN` / `CAPTURE_URL` trong `~/CSL/.env`.
- `capture-api.avada.io` chặn User-Agent mặc định của urllib (403) → `upload.py`
  gửi UA giả `curl/8.7.1`.
- Ảnh upload lên là **public theo link** (không cần đăng nhập để xem).
- `--full` tự cuộn hết trang 1 lượt trước khi chụp để ảnh lazy-load kịp tải. Video
  / iframe nhúng vẫn có thể ra khoảng trắng — chỗ đó chụp tay.
- `--mask` là lưới an toàn khi buộc phải chụp màn hình có dữ liệu thật; ưu tiên
  vẫn là dùng dev/test store ngay từ đầu.
