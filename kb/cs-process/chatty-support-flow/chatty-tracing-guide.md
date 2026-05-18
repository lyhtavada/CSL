# Chatty Tracing — Hướng dẫn dành cho CS/TS

## Tool này dùng để làm gì?

Chatty Tracing cho phép bạn xem lại toàn bộ quá trình xử lý của AI bot — khách hỏi gì, bot trả lời gì, có lỗi không, xử lý mất bao lâu.

**Dùng khi:**
- Khách báo bot trả lời sai hoặc không trả lời
- Khách báo bot chậm
- Khách báo không nhận được email từ hệ thống
- Cần lấy thông tin để báo dev

---

## 1. Đăng nhập

1. Truy cập ứng dụng → click **"Sign in with Google"**
2. Dùng tài khoản Google công ty
3. Sau khi đăng nhập, kiểm tra **dropdown môi trường** ở góc trái header

> **Quan trọng:** Luôn chọn **production** khi hỗ trợ khách hàng thực. Chọn nhầm **staging** sẽ không thấy dữ liệu thật.

---

## 2. Các tình huống thường gặp

### Tình huống 1: Khách báo bot trả lời sai

1. Vào **Conversations**
2. Tìm theo **shop domain** hoặc **Conversation ID** (nếu khách cung cấp)
3. Click vào cuộc hội thoại
4. Đọc lại từng reply:
   - Hộp **xanh dương** = tin nhắn của khách
   - Hộp **xanh lá** = trả lời của bot
   - Phần **Tool calls** (nếu có) = các bước bot xử lý trước khi trả lời
5. Nếu cần báo dev: xem [Quy trình báo lỗi](#5-quy-trình-báo-lỗi-cho-dev)

### Tình huống 2: Khách báo bot trả lời chậm

1. Vào **Conversations**, tìm cuộc hội thoại
2. Xem cột **Duration** — so sánh với các cuộc hội thoại cùng thời điểm
3. Click vào cuộc hội thoại, tìm reply chậm
4. Click vào **số span** (VD: "12 spans >") để mở waterfall
5. Thanh ngang càng dài = bước đó xử lý càng lâu
6. Click vào span dài nhất để xem chi tiết → báo dev

### Tình huống 3: Khách báo không nhận được email

1. Vào **Emails**
2. Tìm theo email người nhận hoặc tên website
3. Kiểm tra cột **Result**:
   - **Xanh** = email đã gửi thành công → vấn đề có thể ở phía khách (spam folder, sai địa chỉ)
   - **Đỏ** = email gửi thất bại → cần báo dev
4. Click vào dòng để xem nội dung email đầy đủ

### Tình huống 4: Bot bị lỗi

1. Vào **Conversations**
2. Tick **"Errors only"** để lọc chỉ cuộc hội thoại có lỗi
3. Click vào cuộc hội thoại có **badge đỏ**
4. Tìm reply có hộp đỏ — đó là nơi xảy ra lỗi
5. Mở waterfall, click vào span màu đỏ để xem thông báo lỗi chi tiết
6. Báo dev theo quy trình bên dưới

### Tình huống 5: Kiểm tra tình trạng hệ thống

1. Vào **Analytics**
2. Kiểm tra các chỉ số:
   - **Error Rate > 5%** → bất thường, cần báo dev
   - **Avg Latency** tăng đột ngột → cần báo dev
3. Xem biểu đồ **Trace Volume**: cột đỏ tăng đột ngột = đang có sự cố

---

## 3. Xem chi tiết cuộc hội thoại

### Tìm kiếm

Từ trang **Conversations**, bạn có thể tìm theo:
- Shop domain
- Shop ID
- Conversation ID

Lọc nhanh theo thời gian: **7d / 30d / 90d** hoặc chọn khoảng ngày tùy chỉnh.

### Đọc chi tiết một cuộc hội thoại

Sau khi click vào một cuộc hội thoại:

| Phần | Ý nghĩa |
|------|---------|
| Header | Thời gian xử lý tổng, số reply, Conversation ID, Shop ID |
| Hộp xanh dương | Tin nhắn của khách |
| Tool calls | Các bước bot xử lý (nếu có viền đỏ = lỗi ở bước này) |
| Hộp xanh lá | Trả lời của bot, kèm tên model AI và số token |
| Waterfall | Sơ đồ thời gian xử lý — click vào span để xem chi tiết |

**Nút copy reply context** (góc phải mỗi reply): sao chép toàn bộ nội dung hội thoại để dán vào ticket hoặc gửi dev.

---

## 4. Theo dõi email

Trang **Emails** hiển thị tất cả email hệ thống đã gửi.

| Cột | Ý nghĩa |
|-----|---------|
| Time | Thời điểm gửi |
| From / To | Email gửi / nhận |
| Subject | Tiêu đề |
| Result | Xanh = thành công, Đỏ = thất bại |

Lọc theo kết quả: All / Success / Failed / Error.

---

## 5. Quy trình báo lỗi cho dev

Mỗi khi báo lỗi, cần cung cấp đủ các thông tin sau:

- [ ] **Conversation ID** — copy từ header trang chi tiết
- [ ] **Reply thứ mấy** có vấn đề (VD: reply 2/3)
- [ ] **Thông báo lỗi** — copy từ panel chi tiết span (nút "Show raw JSON" nếu cần)
- [ ] **Môi trường** — production hay staging
- [ ] **Thời gian** xảy ra

---

## 6. FAQ

**Q: Không thấy cuộc hội thoại của khách?**
Kiểm tra đã chọn **production** chưa. Thử mở rộng khoảng thời gian (30d hoặc 90d). Kiểm tra lại shop domain hoặc Conversation ID.

**Q: Badge đỏ trên cột Errors nghĩa là gì?**
Số trên badge là số lỗi xảy ra trong cuộc hội thoại đó. Click vào để xem chi tiết.

**Q: Token là gì?**
Đơn vị đo lường văn bản AI xử lý. Nhiều token = chi phí cao hơn và thường chậm hơn. CS không cần quan tâm nhiều, chỉ cần biết để đọc báo cáo.

**Q: Dữ liệu có tự cập nhật không?**
Không tự động. Dùng nút **refresh** trên trang Conversations để tải dữ liệu mới nhất.

---

*Cập nhật lần cuối: 07/04/2026*
