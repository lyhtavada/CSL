# Claude Code / Codex — Training Plan cho CS Team

**Đối tượng:** Toàn bộ CS team (Chatty + Joy + Wishlist)
**Mục tiêu:** CS hiểu được Claude Code / Codex là gì, vì sao nên dùng, và tự tin dùng được trong công việc hàng ngày (không cần biết code)
**Hình thức:** Terminal (khuyến nghị chính) hoặc IDE **Zed** — training áp dụng chung cho cả 2 vì cách tư duy giống nhau, Zed chỉ thêm giao diện trực quan hơn
**Status:** Draft — chờ Liz duyệt trước khi chạy
**Last updated:** 2026-08-25

> **Lưu ý:** Đây là công cụ nội bộ, không dùng để trả lời trực tiếp merchant. Mục đích: tăng tốc công việc CS (báo cáo, phân tích data, xử lý file, soạn nội dung, tự động hoá việc lặp).

---

## 1. Mục tiêu training

Sau khoá này, CS có thể:
- [ ] Giải thích được Claude Code/Codex khác gì so với ChatGPT/chatbot thường
- [ ] Cài đặt và mở được công cụ trên máy mình (terminal hoặc Zed)
- [ ] Tự đặt yêu cầu (prompt) rõ ràng và đọc hiểu công cụ đang làm gì
- [ ] Dùng công cụ để xử lý 1 việc thực tế: đọc file, phân tích data, viết báo cáo, tra cứu
- [ ] Biết ranh giới an toàn: khi nào nên tự làm, khi nào phải hỏi lại/xác nhận trước khi để công cụ hành động

---

## 2. Claude Code / Codex là gì?

**Định nghĩa ngắn:** Đây là **AI agent chạy trong terminal (hoặc tích hợp vào IDE như Zed)**, khác với ChatGPT/Claude.ai bản web ở chỗ nó **không chỉ trả lời chữ — nó tự đọc file, tự sửa file, tự chạy lệnh** trên máy của mình, theo yêu cầu mình đặt ra.

| | ChatGPT / Claude.ai (web) | Claude Code / Codex (terminal/Zed) |
|---|---|---|
| Chạy ở đâu | Trình duyệt | Terminal / Zed, ngay trên máy mình |
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

## 4. Ví dụ thực tế: Liz đang dùng công cụ này hàng ngày

Để thấy công cụ này áp dụng được thật vào việc hàng ngày, không chỉ là lý thuyết — trước khi đi vào khái niệm ở Mục 5, xem qua vài ví dụ Liz đang dùng thật:

- **Paste 1 link là xong, không cần hỏi lại:** Liz paste link chat Crisp hoặc link Slack thread vào → agent **tự động** đọc data, tóm tắt nội dung + đề xuất bước tiếp theo, không cần ra lệnh từng bước. CS có thể áp dụng y hệt: paste link ticket/thread dài → nhờ tóm tắt nhanh trước khi xử lý.
- **Báo cáo tổng hợp từ nhiều nguồn cùng lúc:** báo cáo CS tuần của Liz (`/cs-weekly`) tự kéo data từ ticket, chat log, DFY tracker, App Store review... rồi gộp thành 1 báo cáo, đẩy lên Notion + gửi Slack — việc mà làm tay sẽ mất rất nhiều thời gian mở từng nguồn.
- **"File quy tắc cố định" — không phải nhắc lại context mỗi lần:** Liz lưu sẵn 1 file quy tắc (`CLAUDE.md`) ghi rõ: ai là ai trong team, tone giọng văn, nguồn data nào dùng cho việc gì, quy trình nào áp dụng khi nào. Agent tự đọc file này mỗi lần làm việc → Liz không phải giải thích lại từ đầu mỗi lần hỏi. **CS có thể áp dụng tương tự:** lưu 1 file ghi rõ quy trình/thông tin mình hay dùng lặp lại, rồi nhờ agent đọc file đó mỗi khi cần (thư mục mẫu ở Mục 6 đã có sẵn file này).
- **Agent tự nhớ điều đã học qua các lần làm việc trước:** khi Liz sửa cách làm 1 lần ("đừng làm X, làm Y thay vào đó"), agent tự ghi nhớ để lần sau áp dụng luôn — không cần lặp lại hướng dẫn.
- **AI làm nháp, người duyệt final:** dù agent tự soạn nội dung/báo cáo/sửa dữ liệu, **mọi việc có tác động ra ngoài** (gửi merchant, đẩy vào hệ thống live, gắn tag hàng loạt) đều dừng lại **chờ Liz duyệt** trước khi thực thi thật. Đây là nguyên tắc cốt lõi CS cần áp dụng theo (xem thêm Mục 9).

---

## 5. Khái niệm nền tảng: AI Agent & Harness

Hai khái niệm này hay bị nhầm — nắm được sẽ hiểu bản chất công cụ ở Mục 4 vừa thấy đang làm gì, không "sợ" nó hoặc dùng sai cách.

### AI Agent là gì?
- **Chatbot thường** = hỏi 1 câu, trả lời 1 câu, không tự làm gì thêm.
- **AI Agent** = AI được cấp "tay chân" (tools) để **tự lên kế hoạch nhiều bước và hành động** cho tới khi xong việc — đọc file này, phân tích, viết file kia, kiểm tra lại kết quả, báo cáo lại cho mình.
- Ví dụ thực tế: Betty (trợ lý của Liz) chính là 1 AI agent — khi Liz nhờ "tổng hợp báo cáo CS tuần này", Betty tự query data, tự phân tích, tự viết file, tự gửi Slack — đúng như ví dụ ở Mục 4, không phải hỏi lại từng bước.

### Harness là gì?
- **Harness** = "bộ khung vận hành" bao quanh agent — quy định agent được làm gì, không được làm gì, và cung cấp công cụ (tools) để nó hành động.
- Ví dụ cụ thể trong Claude Code: harness cấp cho agent các tool như *đọc file*, *sửa file*, *chạy lệnh terminal*, *tìm kiếm web* — và **cơ chế xin phép** trước khi làm việc rủi ro (xoá file, ghi đè, chạy lệnh nguy hiểm).
- Hiểu đơn giản: **Agent = bộ não ra quyết định, Harness = luật chơi + công cụ trong tay nó**. Cùng 1 "bộ não" AI, nhưng đặt trong harness khác nhau (terminal, Zed, Slack bot...) sẽ có khả năng và giới hạn khác nhau.
- CS không cần chỉnh harness — chỉ cần biết: **mọi hành động rủi ro (xoá, ghi đè, gửi email thật...) đều sẽ được hỏi xác nhận trước**, trừ khi mình đã tự ý bật chế độ tự động.

---

## 6. Cài đặt & bắt đầu

### 6.1 Cài đặt
- **Terminal (khuyến nghị chính):** cài Claude Code qua npm (`npm install -g @anthropic-ai/claude-code` hoặc theo hướng dẫn chính thức) → gõ `claude` để mở. Codex cài tương tự theo hướng dẫn chính thức của OpenAI.
- **IDE — dùng Zed:** cài Zed (zed.dev) → cài extension Claude Code/Codex trong Zed → mở panel chat ngay trong Zed, thao tác giống terminal nhưng có giao diện trực quan hơn (xem file đang mở, diff thay đổi rõ ràng)
- Đăng nhập bằng tài khoản được cấp (không dùng tài khoản cá nhân cho việc công ty)

### 6.2 Thư mục mẫu để bắt đầu
Không cần tự tạo cấu trúc từ đầu — dùng thư mục mẫu `claude-code-starter-kit/` (cùng cấp với file này):

```
claude-code-starter-kit/
├── CLAUDE.md            ← file quy tắc mẫu — điền tên/app/quy trình của mình vào đây
├── data/                ← bỏ file cần agent đọc vào đây (đã có 1 file chat log mẫu)
├── templates/           ← mẫu báo cáo + mẫu FAQ, nhờ agent điền theo
└── reports/             ← nơi agent xuất kết quả ra
```

**Cách bắt đầu:** copy cả thư mục này ra vị trí riêng của mỗi người (không làm việc trực tiếp trong repo CSL của Liz) → mở bằng terminal hoặc Zed → điền `CLAUDE.md` → làm thử bài thực hành ở Mục 8. Chi tiết xem `claude-code-starter-kit/README.md`.

---

## 7. Cách sử dụng cơ bản

### 7.1 Vòng lặp làm việc cơ bản
1. **Mở terminal/Zed tại đúng thư mục** chứa file mình cần làm việc cùng
2. **Ra yêu cầu bằng ngôn ngữ tự nhiên** — càng cụ thể càng tốt (xem 7.2)
3. Agent **đọc, phân tích, và đề xuất hành động** — nếu việc rủi ro (sửa/xoá file, chạy lệnh) nó sẽ **hỏi xác nhận** trước khi làm
4. Mình **duyệt hoặc chỉnh lại yêu cầu** → agent tiếp tục
5. Kiểm tra kết quả cuối — **luôn đọc lại trước khi dùng/gửi đi**, agent có thể sai

### 7.2 Cách ra yêu cầu (prompt) hiệu quả
| Yêu cầu mơ hồ | Yêu cầu rõ ràng, hiệu quả |
|---|---|
| "phân tích file này" | "Đọc file `chat-log.csv`, đếm số chat theo từng ngày, xuất bảng tổng hợp" |
| "viết báo cáo" | "Viết báo cáo tuần theo format ở file `report-template.md`, dùng data trong file `data.csv`" |
| "sửa file" | "Trong file `faq.md`, tìm câu trả lời về refund policy và cập nhật theo nội dung tôi paste bên dưới" |

**Mẹo:** nói rõ **nguồn** (file/link nào), **việc cần làm**, và **kết quả mong muốn** (bảng? file mới? tóm tắt ngắn?).

### 7.3 Chế độ cấp quyền (permission)
- Mặc định: agent sẽ **hỏi trước** mỗi khi định sửa file, chạy lệnh, hoặc gọi ra ngoài (gửi email, post Slack...)
- Có thể chọn "auto-accept" cho việc lặp lại nhiều lần trong 1 phiên làm việc — nhưng **không bật auto cho việc gửi đi bên ngoài** (email merchant, Slack channel chung) khi chưa quen công cụ

---

## 8. Thực hành theo tình huống CS thực tế

Chọn 3–4 bài theo đúng công việc hàng ngày của CS, làm trực tiếp trên máy trong buổi training (dùng luôn thư mục `claude-code-starter-kit/` ở Mục 6.2):

1. **Đọc & tóm tắt:** đưa 1 file chat log hoặc ticket dài (`data/sample-chat-log.csv`) → yêu cầu tóm tắt request chính + đề xuất hướng xử lý
2. **Lọc & so sánh data:** đưa 2 file CSV (data tuần này vs tuần trước) → yêu cầu so sánh, chỉ ra thay đổi đáng chú ý
3. **Soạn nội dung theo template:** dùng `templates/report-template.md` hoặc `templates/faq-entry-template.md` → yêu cầu điền/viết thêm 5 câu hỏi mới theo đúng format
4. **Tra cứu nhanh:** hỏi công cụ tìm trong 1 thư mục tài liệu (playbook/KB) xem quy trình xử lý 1 case cụ thể ở đâu

---

## 9. Nguyên tắc an toàn khi dùng

- **"AI làm nháp, người duyệt final"** — nguyên tắc cốt lõi: agent chuẩn bị/soạn/phân tích, nhưng **mọi việc có tác động ra ngoài** (gửi merchant, đăng Slack, đẩy dữ liệu vào hệ thống live) đều phải qua **mắt người trước khi thực thi thật** — đúng cách Liz đang vận hành Betty (xem Mục 4), không có ngoại lệ
- **Luôn đọc lại kết quả** trước khi gửi cho merchant, đăng lên Slack, hoặc commit vào hệ thống — agent có thể hiểu sai ý hoặc bịa thông tin (hallucination)
- **Không paste data nhạy cảm bừa bãi** (mật khẩu, token, thông tin thanh toán merchant) vào prompt nếu không cần thiết
- **Việc khó hoàn tác** (xoá file, ghi đè dữ liệu, gửi email/Slack thật) → luôn để agent hỏi xác nhận, không bật chế độ tự động cho các việc này
- **Khi công cụ báo không chắc / cần thông tin** → cung cấp thêm context, đừng ép nó đoán
- Công cụ là **trợ lý xử lý việc nội bộ**, không thay thế judgment của CS trong các case nhạy cảm (refund, escalation, VIP)

---

## 10. Nâng cao (tuỳ chọn): đóng gói việc lặp lại thành lệnh riêng

Phần này không bắt buộc trong training cơ bản — dành cho ai muốn đi xa hơn sau khi đã quen dùng hàng ngày (Mục 6–9).

- **Slash Command / Skill là gì:** 1 quy trình nhiều bước lặp đi lặp lại được đóng gói thành **1 lệnh ngắn gõ ra là chạy hết**, không phải giải thích lại từ đầu mỗi lần. Ví dụ: thay vì mỗi tuần phải tự nhắc "vào lấy data ticket, lấy data chat, so sánh tuần trước, viết báo cáo, đẩy Notion, gửi Slack" — Liz chỉ cần gõ `/cs-weekly` và toàn bộ các bước đó tự chạy.
- **CS có thể tự làm tương tự** cho việc lặp lại của riêng mình — ví dụ: 1 lệnh tự tổng hợp số liệu ca trực, 1 lệnh tự soạn nháp trả lời theo loại case hay gặp.
- **Tự động hoá theo lịch (nâng cao hơn nữa):** một số báo cáo của Liz tự chạy đúng giờ mỗi ngày/tuần mà không cần bấm tay (giống hẹn giờ) — chỉ nên làm khi đã dùng thành thạo, có thể nhờ Liz hoặc Betty hỗ trợ setup.

---

## 11. Lộ trình training đề xuất

| Buổi | Nội dung | Thời lượng |
|---|---|---|
| Buổi 1 | Mục 2–4: Công cụ là gì, vì sao cần học, ví dụ thực tế Liz đang dùng hàng ngày — demo trực tiếp | 45 phút |
| Buổi 2 | Mục 5: Khái niệm nền tảng (AI Agent, Harness) — hiểu bản chất công cụ vừa xem demo | 30 phút |
| Buổi 3 | Mục 6–7: Cài đặt trên máy từng người (terminal/Zed) + thư mục mẫu + ra lệnh cơ bản | 45 phút |
| Buổi 4 | Mục 8: Thực hành theo tình huống CS thật, mỗi người tự làm 1 bài | 60 phút |
| Buổi 5 | Mục 9 + Q&A: nguyên tắc an toàn, review case mỗi người đã thử, gỡ vướng | 45 phút |
| Buổi 6 (tuỳ chọn) | Mục 10: Nâng cao — đóng gói lệnh riêng cho ai muốn đi xa hơn | 30 phút |

**Sau training:** mỗi người áp dụng vào 1 việc thật trong tuần (ví dụ: tự tóm tắt data tuần của mình) → chia sẻ lại kết quả trong buổi Coaching để nhân rộng cách dùng hay.

---

## 12. Đánh giá sau training (self-check)

- [ ] Giải thích được sự khác nhau giữa chatbot thường và AI agent
- [ ] Giải thích được Harness là gì bằng ví dụ của riêng mình
- [ ] Nêu được ít nhất 1 ví dụ Liz đang dùng công cụ này hàng ngày và áp dụng tương tự cho việc của mình
- [ ] Tự mở được công cụ (terminal hoặc Zed) và ra được 1 yêu cầu rõ ràng, đúng format
- [ ] Tự làm được 1 việc thực tế (đọc file, so sánh data, hoặc soạn nội dung) không cần hỗ trợ
- [ ] Biết khi nào cần dừng lại xác nhận trước khi để agent hành động
- [ ] Giải thích được nguyên tắc "AI làm nháp, người duyệt final" bằng ví dụ của riêng mình
