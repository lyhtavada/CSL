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
