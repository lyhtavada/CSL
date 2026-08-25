# Codex trên Zed — Training Plan cho CS Team

**Đối tượng:** Toàn bộ CS team (Chatty + Joy + Wishlist)
**Mục tiêu:** CS hiểu được Codex là gì, vì sao nên dùng, và tự tin dùng được trong công việc hàng ngày (không cần biết code)
**Hình thức:** **Codex chạy trong Zed** (IDE chính thức của khoá training) — ai muốn cũng dùng được qua terminal thuần, nhưng training và bài thực hành đều làm trên Zed
**Status:** Draft — chờ Liz duyệt trước khi chạy
**Last updated:** 2026-08-25

> **Lưu ý:** Đây là công cụ nội bộ, không dùng để trả lời trực tiếp merchant. Mục đích: tăng tốc công việc CS (báo cáo, phân tích data, xử lý file, soạn nội dung, tự động hoá việc lặp).

---

## 1. Mục tiêu training

Sau khoá này, CS có thể:
- [ ] Giải thích được Codex khác gì so với ChatGPT/chatbot thường
- [ ] Cài đặt Zed + Codex và mở được lên máy mình
- [ ] Tự đặt yêu cầu (prompt) rõ ràng và đọc hiểu Codex đang làm gì
- [ ] Dùng Codex để xử lý 1 việc thực tế: đọc file, phân tích data, viết báo cáo, tra cứu
- [ ] Biết ranh giới an toàn: khi nào nên tự làm, khi nào phải hỏi lại/xác nhận trước khi để Codex hành động

---

## 2. Codex là gì?

**Định nghĩa ngắn:** Codex (của OpenAI) là **AI agent chạy trong IDE (ở đây dùng Zed) hoặc terminal**, khác với ChatGPT bản web ở chỗ nó **không chỉ trả lời chữ — nó tự đọc file, tự sửa file, tự chạy lệnh** ngay trên máy của mình, theo yêu cầu mình đặt ra.

| | ChatGPT (web) | Codex (trên Zed) |
|---|---|---|
| Chạy ở đâu | Trình duyệt | Ngay trong Zed, trên máy mình |
| Truy cập gì | Chỉ nội dung mình paste vào | Đọc/ghi được file thật trong thư mục đang mở, chạy lệnh, gọi API |
| Kiểu tương tác | Hỏi — đáp | Ra lệnh — nó **tự hành động nhiều bước** để hoàn thành việc |
| Ví dụ | "Tóm tắt đoạn text này" | "Đọc file báo cáo tuần trước, so sánh với data mới, xuất file Excel" |

Codex ban đầu sinh ra cho lập trình viên (nên hay gọi là "coding agent") nhưng dùng được cho **bất kỳ việc gì liên quan đến file, data, văn bản** — không chỉ code. CS không cần biết lập trình để dùng.

---

## 3. Tại sao CS cần học công cụ này?

Đây không phải "học code" — đây là học một cách làm việc mới, nhanh hơn nhiều so với làm tay từng bước trên Excel/Google Sheet/Notion.

**Việc CS đang làm mà Codex làm nhanh hơn:**
- Đọc và tóm tắt hàng loạt file/data (chat log, ticket, review) → thay vì đọc tay từng dòng
- Lọc, gộp, so sánh data từ nhiều nguồn (CSV, Sheet, API) → ra báo cáo có số liệu, không cần công thức Excel phức tạp
- Soạn nội dung theo template có sẵn (FAQ, email, training data) → nhanh và nhất quán hơn viết tay
- Tự động hoá việc lặp lại theo lịch (báo cáo tuần, check dữ liệu) — cùng nguyên lý với cách Betty đang vận hành cho Liz (`/cs-weekly`, `/dfy-tracker`, `/kb-sync`...), chỉ khác công cụ nền
- Tìm nhanh thông tin trong khối lượng tài liệu lớn (playbook, KB, transcript) thay vì Ctrl+F từng file

**Giá trị cụ thể:** việc trước đây mất 1–2 tiếng làm tay (đọc data, gộp báo cáo, rà soát KB) có thể rút xuống 10–15 phút nếu biết ra yêu cầu đúng cách.

**Ví dụ pattern lặp lại có thể áp dụng:** chuyển đổi tài liệu support sang format bot đọc được, kiểm tra lại câu trả lời bot sau khi sửa KB, đồng bộ KB khi sản phẩm có thay đổi — đây đều là các quy trình có sẵn Betty đang chạy cho Liz (`/kb-sync`, `/kb-test`, `/product-kb-sync`, `/bot-corrections`), CS hoàn toàn áp dụng được pattern tương tự cho việc của mình bằng Codex.

---

## 4. Ví dụ thực tế: cùng nguyên lý Liz đang dùng hàng ngày

> Liz đang dùng **Claude Code** (một agent "anh em" của Codex — cùng khái niệm, chạy trong workspace CSL). CS team dùng **Codex trên Zed**. Công cụ khác nhau nhưng **nguyên lý vận hành giống hệt nhau** — xem ví dụ dưới đây để hiểu cách áp dụng Codex vào việc hàng ngày của mình.

- **Paste 1 link là xong, không cần hỏi lại:** Liz paste link chat Crisp hoặc link Slack thread vào → agent **tự động** đọc data, tóm tắt nội dung + đề xuất bước tiếp theo, không cần ra lệnh từng bước. CS có thể áp dụng y hệt với Codex: paste link ticket/thread dài → nhờ tóm tắt nhanh trước khi xử lý.
- **Báo cáo tổng hợp từ nhiều nguồn cùng lúc:** báo cáo CS tuần của Liz (`/cs-weekly`) tự kéo data từ ticket, chat log, DFY tracker, App Store review... rồi gộp thành 1 báo cáo, đẩy lên Notion + gửi Slack — việc mà làm tay sẽ mất rất nhiều thời gian mở từng nguồn.
- **"File quy tắc cố định" — không phải nhắc lại context mỗi lần:** Liz lưu sẵn 1 file quy tắc (`CLAUDE.md`) ghi rõ: ai là ai trong team, tone giọng văn, nguồn data nào dùng cho việc gì, quy trình nào áp dụng khi nào. Agent tự đọc file này mỗi lần làm việc → Liz không phải giải thích lại từ đầu mỗi lần hỏi. **Codex dùng đúng cơ chế này qua file `AGENTS.md`** (thư mục mẫu ở Mục 6 đã có sẵn) — CS lưu quy trình/thông tin mình hay dùng lặp lại vào đó, Codex tự đọc mỗi khi cần.
- **Agent tự nhớ điều đã học qua các lần làm việc trước:** khi Liz sửa cách làm 1 lần ("đừng làm X, làm Y thay vào đó"), agent tự ghi nhớ để lần sau áp dụng luôn — không cần lặp lại hướng dẫn.
- **AI làm nháp, người duyệt final:** dù agent tự soạn nội dung/báo cáo/sửa dữ liệu, **mọi việc có tác động ra ngoài** (gửi merchant, đẩy vào hệ thống live, gắn tag hàng loạt) đều dừng lại **chờ người duyệt** trước khi thực thi thật. Đây là nguyên tắc cốt lõi CS cần áp dụng khi dùng Codex (xem thêm Mục 9).

---

## 5. Khái niệm nền tảng: AI Agent & 5 tầng kiến trúc

Nắm được phần này sẽ hiểu bản chất Codex ở Mục 4 vừa thấy đang làm gì, không "sợ" nó hoặc dùng sai cách — không cần nhớ thuật ngữ, chỉ cần hiểu ý.

### AI Agent là gì?
- **Chatbot thường** = hỏi 1 câu, trả lời 1 câu, không tự làm gì thêm.
- **AI Agent** = AI được cấp "tay chân" (tools) và **quyền hạn** để **tự lên kế hoạch nhiều bước và hành động** cho tới khi xong việc — đọc file này, phân tích, viết file kia, tự kiểm tra lại kết quả, báo cáo lại cho mình.
- Ví dụ thực tế: Betty (trợ lý của Liz, chạy trên Claude Code) chính là 1 AI agent — khi Liz nhờ "tổng hợp báo cáo CS tuần này", Betty tự query data, tự phân tích, tự viết file, tự gửi Slack. **Codex hoạt động theo đúng nguyên lý này** — chỉ là "bộ não" và nơi chạy khác nhau.

### 5 tầng bên trong 1 AI Agent
Một agent như Codex vận hành qua 5 tầng, từ cơ bản đến nâng cao — 3 tầng đầu là thứ CS dùng hàng ngày, 2 tầng sau chỉ cần biết là có tồn tại:

| Tầng | Là gì | Ví dụ |
|---|---|---|
| **1. Prompt** | Yêu cầu mình đưa ra — rõ nhất khi có đủ 3 phần: **nguồn** + **việc cần làm** + **kết quả mong muốn** (xem Mục 7.2) | "Đọc `chat-log.csv`, đếm chat theo ngày, xuất bảng" |
| **2. Context** | "Kiến thức" Codex nhìn thấy khi làm việc — file trong thư mục đang mở, nội dung `AGENTS.md`, data mình đưa vào. Context càng đúng, kết quả càng chuẩn, càng ít phải sửa lại | Codex đọc đúng `AGENTS.md` + file trong `data/` trước khi trả lời |
| **3. Harness** | Bộ công cụ + quyền hạn Codex có: đọc file, sửa file, chạy lệnh, tìm kiếm web — kèm **cơ chế xin phép** trước việc rủi ro (xoá, ghi đè, chạy lệnh nguy hiểm). Khi chạy trong Zed, Zed là nơi hiển thị các bước này và cho mình xác nhận/từ chối | Zed hỏi xác nhận trước khi Codex ghi đè 1 file |
| **4. Tự kiểm tra lại (nâng cao)** | Agent tự làm xong rồi tự soi lại kết quả, phát hiện sai thì tự sửa tiếp — không cần mình nhắc | Codex tự phát hiện số liệu lệch, tự đối chiếu lại nguồn trước khi trả kết quả cuối |
| **5. Nhiều agent phối hợp (nâng cao)** | Chia 1 việc lớn cho nhiều agent làm song song rồi gộp lại — chỉ cần cho việc phức tạp, khối lượng lớn | Xem Mục 10 (Nâng cao) |

**Hiểu đơn giản:** **Agent = bộ não ra quyết định** (Tầng 1–2 là mình đưa input cho nó), **Harness = luật chơi + công cụ trong tay nó** (Tầng 3). Cùng 1 kiểu "bộ não" agent, nhưng đặt trong harness khác nhau (Zed, terminal thuần, Slack bot...) sẽ có khả năng và giới hạn khác nhau.

CS không cần chỉnh harness hay tự dựng Tầng 4–5 — chỉ cần biết: **mọi hành động rủi ro (xoá, ghi đè, gửi email thật...) đều sẽ được Zed hỏi xác nhận trước**, trừ khi mình đã tự ý bật chế độ tự động.

---

## 6. Cài đặt & bắt đầu

### 6.1 Cài đặt Zed + Codex
- Cài **Zed**: tải tại [zed.dev](https://zed.dev), cài như app bình thường
- Cài **Codex** trong Zed: mở Zed → vào phần Extensions → tìm và cài extension Codex (hoặc theo hướng dẫn chính thức của OpenAI nếu Zed yêu cầu cấu hình thêm) → mở panel Codex ngay trong Zed
- Đăng nhập bằng tài khoản được cấp (không dùng tài khoản cá nhân cho việc công ty)
- Ai muốn dùng qua terminal thuần (không qua Zed) vẫn được — cài `codex` CLI theo hướng dẫn chính thức của OpenAI, gõ `codex` để mở — nhưng training/bài thực hành mặc định làm trên Zed

### 6.2 Thư mục mẫu để bắt đầu — "bộ não thứ hai" của Codex
Không cần tự tạo cấu trúc từ đầu — dùng thư mục mẫu `codex-starter-kit/` (cùng cấp với file này). Thư mục này chính là **Context** (Tầng 2 ở Mục 5) — hay còn gọi là **"second brain"**: nơi lưu sẵn quy tắc + data để Codex tự đọc mỗi lần làm việc, không phải giải thích lại từ đầu mỗi phiên:

```
codex-starter-kit/
├── AGENTS.md            ← file quy tắc chuẩn của Codex — điền tên/app/quy trình của mình vào đây
├── data/                ← bỏ file cần Codex đọc vào đây (đã có 1 file chat log mẫu)
├── templates/           ← mẫu báo cáo + mẫu FAQ, nhờ Codex điền theo
└── reports/             ← nơi Codex xuất kết quả ra
```

**Cách bắt đầu:** copy cả thư mục này ra vị trí riêng của mỗi người (không làm việc trực tiếp trong repo CSL của Liz) → mở bằng **Zed** → điền `AGENTS.md` → làm thử bài thực hành ở Mục 8. Chi tiết xem `codex-starter-kit/README.md`.

---

## 7. Cách sử dụng cơ bản

### 7.1 Vòng lặp làm việc cơ bản
1. **Mở Zed tại đúng thư mục** chứa file mình cần làm việc cùng
2. **Ra yêu cầu bằng ngôn ngữ tự nhiên** trong panel Codex — càng cụ thể càng tốt (xem 7.2)
3. Codex **đọc, phân tích, và đề xuất hành động** — nếu việc rủi ro (sửa/xoá file, chạy lệnh) nó sẽ **hỏi xác nhận** ngay trong Zed trước khi làm
4. Mình **duyệt hoặc chỉnh lại yêu cầu** → Codex tiếp tục
5. Kiểm tra kết quả cuối — **luôn đọc lại trước khi dùng/gửi đi**, Codex có thể sai

### 7.2 Cách ra yêu cầu (prompt) hiệu quả — 3 phần bắt buộc
Đây chính là **Tầng 1 (Prompt)** ở Mục 5 — 1 yêu cầu tốt luôn có đủ 3 phần: **nguồn** (file/link nào) + **việc cần làm** + **kết quả mong muốn** (bảng? file mới? tóm tắt ngắn?).

| Yêu cầu mơ hồ | Yêu cầu rõ ràng, hiệu quả (đủ 3 phần) |
|---|---|
| "phân tích file này" | "Đọc file `chat-log.csv`, đếm số chat theo từng ngày, xuất bảng tổng hợp" |
| "viết báo cáo" | "Viết báo cáo tuần theo format ở file `report-template.md`, dùng data trong file `data.csv`" |
| "sửa file" | "Trong file `faq.md`, tìm câu trả lời về refund policy và cập nhật theo nội dung tôi paste bên dưới" |

### 7.3 Chế độ cấp quyền (permission)
- Mặc định: Codex sẽ **hỏi trước** mỗi khi định sửa file, chạy lệnh, hoặc gọi ra ngoài (gửi email, post Slack...) — hộp thoại xác nhận hiện ngay trong Zed
- Có thể chọn "auto-accept" cho việc lặp lại nhiều lần trong 1 phiên làm việc — nhưng **không bật auto cho việc gửi đi bên ngoài** (email merchant, Slack channel chung) khi chưa quen công cụ

---

## 8. Thực hành theo tình huống CS thực tế

Chọn 3–4 bài theo đúng công việc hàng ngày của CS, làm trực tiếp trên Zed trong buổi training (dùng luôn thư mục `codex-starter-kit/` ở Mục 6.2):

1. **Đọc & tóm tắt:** đưa 1 file chat log hoặc ticket dài (`data/sample-chat-log.csv`) → yêu cầu tóm tắt request chính + đề xuất hướng xử lý
2. **Lọc & so sánh data:** đưa 2 file CSV (data tuần này vs tuần trước) → yêu cầu so sánh, chỉ ra thay đổi đáng chú ý
3. **Soạn nội dung theo template:** dùng `templates/report-template.md` hoặc `templates/faq-entry-template.md` → yêu cầu điền/viết thêm 5 câu hỏi mới theo đúng format
4. **Tra cứu nhanh:** hỏi Codex tìm trong 1 thư mục tài liệu (playbook/KB) xem quy trình xử lý 1 case cụ thể ở đâu

---

## 9. Nguyên tắc an toàn khi dùng

- **"AI làm nháp, người duyệt final"** — nguyên tắc cốt lõi: Codex chuẩn bị/soạn/phân tích, nhưng **mọi việc có tác động ra ngoài** (gửi merchant, đăng Slack, đẩy dữ liệu vào hệ thống live) đều phải qua **mắt người trước khi thực thi thật** — cùng nguyên lý Liz đang vận hành Betty (xem Mục 4), không có ngoại lệ
- **Luôn đọc lại kết quả** trước khi gửi cho merchant, đăng lên Slack, hoặc commit vào hệ thống — Codex có thể hiểu sai ý hoặc bịa thông tin (hallucination)
- **Không paste data nhạy cảm bừa bãi** (mật khẩu, token, thông tin thanh toán merchant) vào prompt nếu không cần thiết
- **Việc khó hoàn tác** (xoá file, ghi đè dữ liệu, gửi email/Slack thật) → luôn để Codex hỏi xác nhận trong Zed, không bật chế độ tự động cho các việc này
- **Khi Codex báo không chắc / cần thông tin** → cung cấp thêm context, đừng ép nó đoán
- Công cụ là **trợ lý xử lý việc nội bộ**, không thay thế judgment của CS trong các case nhạy cảm (refund, escalation, VIP)

---

## 10. Nâng cao (tuỳ chọn): đóng gói việc lặp lại thành lệnh riêng

Phần này không bắt buộc trong training cơ bản — dành cho ai muốn đi xa hơn sau khi đã quen dùng hàng ngày (Mục 6–9).

- **Lệnh riêng (custom command) là gì:** 1 quy trình nhiều bước lặp đi lặp lại được đóng gói thành **1 lệnh ngắn gõ ra là chạy hết**, không phải giải thích lại từ đầu mỗi lần. Ví dụ: thay vì mỗi tuần phải tự nhắc "vào lấy data ticket, lấy data chat, so sánh tuần trước, viết báo cáo, đẩy Notion, gửi Slack" — Liz chỉ cần gõ `/cs-weekly` (trên Claude Code) và toàn bộ các bước đó tự chạy.
- **CS có thể tự làm tương tự trên Codex** cho việc lặp lại của riêng mình — ví dụ: 1 lệnh tự tổng hợp số liệu ca trực, 1 lệnh tự soạn nháp trả lời theo loại case hay gặp.
- **Tự động hoá theo lịch (nâng cao hơn nữa):** một số báo cáo của Liz tự chạy đúng giờ mỗi ngày/tuần mà không cần bấm tay (giống hẹn giờ) — chỉ nên làm khi đã dùng thành thạo, có thể nhờ Liz hoặc Betty hỗ trợ setup.

---

## 11. Lộ trình training đề xuất

| Buổi | Nội dung | Thời lượng |
|---|---|---|
| Buổi 1 | Mục 2–4: Codex là gì, vì sao cần học, ví dụ thực tế Liz đang dùng hàng ngày — demo trực tiếp trên Zed | 45 phút |
| Buổi 2 | Mục 5: Khái niệm nền tảng (AI Agent, Harness) — hiểu bản chất công cụ vừa xem demo | 30 phút |
| Buổi 3 | Mục 6–7: Cài Zed + Codex trên máy từng người + thư mục mẫu + ra lệnh cơ bản | 45 phút |
| Buổi 4 | Mục 8: Thực hành theo tình huống CS thật, mỗi người tự làm 1 bài | 60 phút |
| Buổi 5 | Mục 9 + Q&A: nguyên tắc an toàn, review case mỗi người đã thử, gỡ vướng | 45 phút |
| Buổi 6 (tuỳ chọn) | Mục 10: Nâng cao — đóng gói lệnh riêng cho ai muốn đi xa hơn | 30 phút |

**Sau training:** mỗi người áp dụng vào 1 việc thật trong tuần (ví dụ: tự tóm tắt data tuần của mình) → chia sẻ lại kết quả trong buổi Coaching để nhân rộng cách dùng hay.

---

## 12. Đánh giá sau training (self-check)

- [ ] Giải thích được sự khác nhau giữa chatbot thường và AI agent
- [ ] Nêu được 3 tầng cơ bản (Prompt — Context — Harness) và ví dụ của mỗi tầng
- [ ] Giải thích được vì sao thư mục `AGENTS.md` được gọi là "second brain"
- [ ] Nêu được ít nhất 1 ví dụ Liz đang dùng công cụ tương tự hàng ngày và áp dụng được cho Codex
- [ ] Tự mở được Zed + Codex và ra được 1 yêu cầu rõ ràng, đúng format
- [ ] Tự làm được 1 việc thực tế (đọc file, so sánh data, hoặc soạn nội dung) không cần hỗ trợ
- [ ] Biết khi nào cần dừng lại xác nhận trước khi để Codex hành động
- [ ] Giải thích được nguyên tắc "AI làm nháp, người duyệt final" bằng ví dụ của riêng mình
