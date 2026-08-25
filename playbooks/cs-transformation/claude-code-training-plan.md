# Claude Code / Codex — Training Plan cho CS Team

**Đối tượng:** Toàn bộ CS team (Chatty + Joy + Wishlist)
**Mục tiêu:** CS hiểu được Claude Code / Codex là gì, vì sao nên dùng, và tự tin dùng được trong công việc hàng ngày (không cần biết code)
**Hình thức:** Terminal hoặc IDE bất kỳ (VS Code, Cursor...) — training áp dụng chung cho cả 2 vì cách tư duy giống nhau
**Status:** Draft — chờ Liz duyệt trước khi chạy
**Last updated:** 2026-08-25

> **Lưu ý:** Đây là công cụ nội bộ, không dùng để trả lời trực tiếp merchant. Mục đích: tăng tốc công việc CS (báo cáo, phân tích data, xử lý file, soạn nội dung, tự động hoá việc lặp).

---

## 1. Mục tiêu training

Sau khoá này, CS có thể:
- [ ] Giải thích được Claude Code/Codex khác gì so với ChatGPT/chatbot thường
- [ ] Cài đặt và mở được công cụ trên máy mình (terminal hoặc IDE)
- [ ] Tự đặt yêu cầu (prompt) rõ ràng và đọc hiểu công cụ đang làm gì
- [ ] Dùng công cụ để xử lý 1 việc thực tế: đọc file, phân tích data, viết báo cáo, tra cứu
- [ ] Biết ranh giới an toàn: khi nào nên tự làm, khi nào phải hỏi lại/xác nhận trước khi để công cụ hành động

---

## 2. Claude Code / Codex là gì?

**Định nghĩa ngắn:** Đây là **AI agent chạy trong terminal (hoặc tích hợp vào IDE)**, khác với ChatGPT/Claude.ai bản web ở chỗ nó **không chỉ trả lời chữ — nó tự đọc file, tự sửa file, tự chạy lệnh** trên máy của mình, theo yêu cầu mình đặt ra.

| | ChatGPT / Claude.ai (web) | Claude Code / Codex (CLI/IDE) |
|---|---|---|
| Chạy ở đâu | Trình duyệt | Terminal / IDE, ngay trên máy mình |
| Truy cập gì | Chỉ nội dung mình paste vào | Đọc/ghi được file thật trên máy, chạy lệnh, gọi API |
| Kiểu tương tác | Hỏi — đáp | Ra lệnh — nó **tự hành động nhiều bước** để hoàn thành việc |
| Ví dụ | "Tóm tắt đoạn text này" | "Đọc file báo cáo tuần trước, so sánh với data mới, xuất file Excel" |

**Claude Code** (Anthropic) và **Codex** (OpenAI) là 2 sản phẩm cùng loại — cùng là "coding agent" chạy dòng lệnh, ban đầu sinh ra cho lập trình viên nhưng dùng được cho **bất kỳ việc gì liên quan đến file, data, văn bản** — không chỉ code. CS không cần biết lập trình để dùng.

---

## 3. Tại sao CS cần học công cụ này?

Đây không phải "học code" — đây là học một cách làm việc mới, nhanh hơn nhiều so với làm tay từng bước trên Excel/Google Sheet/Notion.

**Việc CS đang làm mà công cụ này làm nhanh hơn:**
- Đọc và tóm tắt hàng loạt file/data (chat log, ticket, review) → thay vì đọc tay từng dòng
- Lọc, gộp, so sánh data từ nhiều nguồn (CSV, Sheet, API) → ra báo cáo có số liệu, không cần công thức Excel phức tạp
- Soạn nội dung theo template có sẵn (FAQ, email, training data) → nhanh và nhất quán hơn viết tay
- Tự động hoá việc lặp lại theo lịch (báo cáo tuần, check dữ liệu) — chính là cách Betty đang vận hành cho Liz (`/cs-weekly`, `/dfy-tracker`, `/kb-sync`...)
- Tìm nhanh thông tin trong khối lượng tài liệu lớn (playbook, KB, transcript) thay vì Ctrl+F từng file

**Giá trị cụ thể:** việc trước đây mất 1–2 tiếng làm tay (đọc data, gộp báo cáo, rà soát KB) có thể rút xuống 10–15 phút nếu biết ra yêu cầu đúng cách.

---

## 4. Khái niệm nền tảng: AI Agent & Harness

Hai khái niệm này hay bị nhầm — nắm được sẽ hiểu bản chất công cụ đang làm gì, không "sợ" nó hoặc dùng sai cách.

### AI Agent là gì?
- **Chatbot thường** = hỏi 1 câu, trả lời 1 câu, không tự làm gì thêm.
- **AI Agent** = AI được cấp "tay chân" (tools) để **tự lên kế hoạch nhiều bước và hành động** cho tới khi xong việc — đọc file này, phân tích, viết file kia, kiểm tra lại kết quả, báo cáo lại cho mình.
- Ví dụ thực tế: Betty (trợ lý của Liz) chính là 1 AI agent — khi Liz nhờ "tổng hợp báo cáo CS tuần này", Betty tự query data, tự phân tích, tự viết file, tự gửi Slack — không phải hỏi lại từng bước.

### Harness là gì?
- **Harness** = "bộ khung vận hành" bao quanh agent — quy định agent được làm gì, không được làm gì, và cung cấp công cụ (tools) để nó hành động.
- Ví dụ cụ thể trong Claude Code: harness cấp cho agent các tool như *đọc file*, *sửa file*, *chạy lệnh terminal*, *tìm kiếm web* — và **cơ chế xin phép** trước khi làm việc rủi ro (xoá file, ghi đè, chạy lệnh nguy hiểm).
- Hiểu đơn giản: **Agent = bộ não ra quyết định, Harness = luật chơi + công cụ trong tay nó**. Cùng 1 "bộ não" AI, nhưng đặt trong harness khác nhau (terminal, IDE, Slack bot...) sẽ có khả năng và giới hạn khác nhau.
- CS không cần chỉnh harness — chỉ cần biết: **mọi hành động rủi ro (xoá, ghi đè, gửi email thật...) đều sẽ được hỏi xác nhận trước**, trừ khi mình đã tự ý bật chế độ tự động.

---

## 5. Cách sử dụng cơ bản

### 5.1 Cài đặt
- **Terminal:** cài qua npm (`npm install -g @anthropic-ai/claude-code` hoặc theo hướng dẫn chính thức) → gõ `claude` để mở
- **IDE (VS Code, Cursor...):** cài extension tương ứng từ Marketplace → mở panel chat ngay trong IDE
- Đăng nhập bằng tài khoản được cấp (không dùng tài khoản cá nhân cho việc công ty)

### 5.2 Vòng lặp làm việc cơ bản
1. **Mở terminal/IDE tại đúng thư mục** chứa file mình cần làm việc cùng
2. **Ra yêu cầu bằng ngôn ngữ tự nhiên** — càng cụ thể càng tốt (xem 5.3)
3. Agent **đọc, phân tích, và đề xuất hành động** — nếu việc rủi ro (sửa/xoá file, chạy lệnh) nó sẽ **hỏi xác nhận** trước khi làm
4. Mình **duyệt hoặc chỉnh lại yêu cầu** → agent tiếp tục
5. Kiểm tra kết quả cuối — **luôn đọc lại trước khi dùng/gửi đi**, agent có thể sai

### 5.3 Cách ra yêu cầu (prompt) hiệu quả
| Yêu cầu mơ hồ | Yêu cầu rõ ràng, hiệu quả |
|---|---|
| "phân tích file này" | "Đọc file `chat-log.csv`, đếm số chat theo từng ngày, xuất bảng tổng hợp" |
| "viết báo cáo" | "Viết báo cáo tuần theo format ở file `cs-weekly-template.md`, dùng data trong file `data.csv`" |
| "sửa file" | "Trong file `faq.md`, tìm câu trả lời về refund policy và cập nhật theo nội dung tôi paste bên dưới" |

**Mẹo:** nói rõ **nguồn** (file/link nào), **việc cần làm**, và **kết quả mong muốn** (bảng? file mới? tóm tắt ngắn?).

### 5.4 Chế độ cấp quyền (permission)
- Mặc định: agent sẽ **hỏi trước** mỗi khi định sửa file, chạy lệnh, hoặc gọi ra ngoài (gửi email, post Slack...)
- Có thể chọn "auto-accept" cho việc lặp lại nhiều lần trong 1 phiên làm việc — nhưng **không bật auto cho việc gửi đi bên ngoài** (email merchant, Slack channel chung) khi chưa quen công cụ

---

## 6. Thực hành theo tình huống CS thực tế

Chọn 3–4 bài theo đúng công việc hàng ngày của CS, làm trực tiếp trên máy trong buổi training:

1. **Đọc & tóm tắt:** đưa 1 file chat log hoặc ticket dài → yêu cầu tóm tắt request chính + đề xuất hướng xử lý
2. **Lọc & so sánh data:** đưa 2 file CSV (data tuần này vs tuần trước) → yêu cầu so sánh, chỉ ra thay đổi đáng chú ý
3. **Soạn nội dung theo template:** đưa 1 file FAQ mẫu → yêu cầu viết thêm 5 câu hỏi mới theo đúng format
4. **Tra cứu nhanh:** hỏi công cụ tìm trong 1 thư mục tài liệu (playbook/KB) xem quy trình xử lý 1 case cụ thể ở đâu

---

## 7. Nguyên tắc an toàn khi dùng

- **Luôn đọc lại kết quả** trước khi gửi cho merchant, đăng lên Slack, hoặc commit vào hệ thống — agent có thể hiểu sai ý hoặc bịa thông tin (hallucination)
- **Không paste data nhạy cảm bừa bãi** (mật khẩu, token, thông tin thanh toán merchant) vào prompt nếu không cần thiết
- **Việc khó hoàn tác** (xoá file, ghi đè dữ liệu, gửi email/Slack thật) → luôn để agent hỏi xác nhận, không bật chế độ tự động cho các việc này
- **Khi công cụ báo không chắc / cần thông tin** → cung cấp thêm context, đừng ép nó đoán
- Công cụ là **trợ lý xử lý việc nội bộ**, không thay thế judgment của CS trong các case nhạy cảm (refund, escalation, VIP)

---

## 8. Lộ trình training đề xuất

| Buổi | Nội dung | Thời lượng |
|---|---|---|
| Buổi 1 | Mục 2–4: Khái niệm (Agent, Harness), vì sao cần học, demo trực tiếp | 45 phút |
| Buổi 2 | Mục 5: Cài đặt trên máy từng người + làm quen giao diện, ra lệnh cơ bản | 45 phút |
| Buổi 3 | Mục 6: Thực hành theo tình huống CS thật, mỗi người tự làm 1 bài | 60 phút |
| Buổi 4 | Mục 7 + Q&A: nguyên tắc an toàn, review case mỗi người đã thử, gỡ vướng | 45 phút |

**Sau training:** mỗi người áp dụng vào 1 việc thật trong tuần (ví dụ: tự tóm tắt data tuần của mình) → chia sẻ lại kết quả trong buổi Coaching để nhân rộng cách dùng hay.

---

## 9. Đánh giá sau training (self-check)

- [ ] Giải thích được sự khác nhau giữa chatbot thường và AI agent
- [ ] Giải thích được Harness là gì bằng ví dụ của riêng mình
- [ ] Tự mở được công cụ và ra được 1 yêu cầu rõ ràng, đúng format
- [ ] Tự làm được 1 việc thực tế (đọc file, so sánh data, hoặc soạn nội dung) không cần hỗ trợ
- [ ] Biết khi nào cần dừng lại xác nhận trước khi để agent hành động
