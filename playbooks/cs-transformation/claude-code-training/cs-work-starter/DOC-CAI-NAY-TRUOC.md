# Đọc cái này trước — 5 phút

Chào bạn 👋 Đây là bộ khởi động để bắt đầu dùng **Claude Code / Codex** trong công việc CS.

---

## 1. Đặt folder này ở đâu?

Giải nén và để ở chỗ **dễ nhớ, dễ tìm**. Gợi ý:

```
Mac:      /Users/<tên-bạn>/cs-work
Windows:  C:\Users\<tên-bạn>\cs-work
```

Đừng để trong Downloads. Đừng để tên folder có dấu tiếng Việt hoặc khoảng trắng.

---

## 2. Mở Claude Code ở đúng chỗ

Đây là bước quan trọng nhất, và cũng là chỗ người mới hay sai.

**Cách dễ nhất trên Mac:**
1. Mở **Finder**, tìm đến folder `cs-work`
2. Click chuột phải vào folder → **Services** → **New Terminal at Folder**
3. Cửa sổ đen hiện ra → gõ `claude` → Enter

**Cách thủ công:**
1. Mở app **Terminal**
2. Gõ `cd ` (có dấu cách ở cuối), rồi **kéo thả folder `cs-work` vào cửa sổ terminal** → Enter
3. Gõ `claude` → Enter

**Kiểm tra bạn đang đúng chỗ:** gõ `ls` → phải thấy `CLAUDE.md`, `kb`, `inbox`, `drafts`.
Nếu không thấy → bạn đang ở sai folder.

---

## 3. Quy tắc số 1 phải nhớ

> ### Claude chỉ nhìn thấy những gì nằm TRONG folder bạn mở.

File để ở Desktop, ở Downloads → **nó không thấy**.
Muốn nó xử lý file nào → **copy file đó vào `inbox/` trước**.

Đây vừa là giới hạn, vừa là lớp bảo vệ: nó không thể lục lọi máy bạn ngoài phạm vi này.

---

## 4. Việc đầu tiên nên làm

Mở Claude Code lên, gõ đúng 3 câu này theo thứ tự:

**Câu 1 — để nó tự giới thiệu:**
```
Đọc CLAUDE.md và cho tôi biết bạn hiểu vai trò của mình ở đây là gì.
```

**Câu 2 — để thấy nó nhìn được folder:**
```
Trong folder inbox có file gì?
```

**Câu 3 — để thấy nó làm được việc thật:**
```
Đọc file inbox/chat-export-mau.csv, cho tôi 5 vấn đề merchant hỏi nhiều nhất
và số lượng mỗi loại.
```

Nếu 3 câu này chạy được → bạn đã sẵn sàng.

---

## 5. Sau đó: điền tên mình vào `CLAUDE.md`

Mở file `CLAUDE.md`, tìm chỗ có `[Điền tên bạn]` và `[Chatty / Joy Loyalty / Joy Wishlist]`, sửa lại cho đúng.

Sửa bằng cách nào cũng được — TextEdit, VS Code, hoặc nhờ luôn Claude:
```
Sửa CLAUDE.md: tên tôi là Ly, tôi phụ trách chính app Chatty.
```

---

## 6. Có gì trong folder này

| Folder | Để làm gì |
|---|---|
| `CLAUDE.md` | Bảng nội quy — Claude đọc đầu tiên mỗi lần mở |
| `kb/` | Tài liệu gốc để nó **tra cứu**. Chỉ đọc, không sửa |
| `inbox/` | Quăng file thô vào đây: CSV, Excel, ảnh, transcript |
| `drafts/` | Claude viết ra ở đây. Bạn đọc lại rồi mới dùng |
| `prompts/` | Thư viện câu lệnh hay — copy dùng lại, khỏi nghĩ |
| `done/` | Xong rồi thì cất vào đây cho gọn |

---

## 7. Ba điều KHÔNG được quên

| ❌ Không | Vì sao |
|---|---|
| Không paste API key, token, thông tin thẻ, email list merchant | Dữ liệu nhạy cảm |
| Không gửi thẳng output cho merchant khi chưa đọc lại | AI bịa số liệu và policy rất tự tin |
| Không tin con số / policy / giá nó nói mà chưa kiểm `kb/` | Sai policy với merchant = lỗi nặng |

**Nguyên tắc gốc: AI viết nháp, mình chịu trách nhiệm.**

---

## 8. Ba phím tắt sống còn

| Phím | Làm gì |
|---|---|
| `Esc` | Dừng nó lại giữa chừng khi thấy nó đi sai hướng |
| `/clear` | Xóa trí nhớ ngắn hạn, bắt đầu việc mới. **1 việc = 1 phiên** |
| `Ctrl + C` (2 lần) | Thoát hẳn |

---

## 9. Kẹt thì làm gì

1. Đọc lại `prompts/prompt-thuong-dung.md` — có thể việc bạn cần đã có sẵn mẫu
2. Hỏi ngay chính nó: `"Tôi muốn làm X nhưng không biết bắt đầu thế nào"`
3. Hỏi trong nhóm CS — và nhớ **paste luôn prompt bạn đã dùng**, để mọi người biết sửa chỗ nào
