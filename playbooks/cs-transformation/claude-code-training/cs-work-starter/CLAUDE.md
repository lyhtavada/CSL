# Nội quy folder này

> File này là **bảng nội quy** của folder `cs-work`.
> Mỗi lần bạn mở Claude Code / Codex trong folder này, nó đọc file này TRƯỚC KHI làm bất cứ việc gì.
> Viết ở đây 1 lần = khỏi phải nhắc lại mỗi lần chat.
>
> **Bạn được phép sửa file này.** Nó là văn bản thường, không phải code.
> Chỗ nào có `[...]` là chỗ bạn điền vào.

---

## Tôi là ai

Tôi tên là **[Điền tên bạn]**, CS của Avada Support Team.

Tôi support 3 app trên Shopify:
- **Chatty** — live chat, AI agent, FAQ
- **Joy Loyalty** — loyalty & rewards
- **Joy Wishlist** — wishlist / save-for-later

Khách hàng của tôi gọi là **merchant** — họ là chủ shop Shopify, không phải người mua hàng cuối.

App tôi phụ trách chính: **[Chatty / Joy Loyalty / Joy Wishlist]**

---

## Cách tôi muốn bạn làm việc

- Trả lời **thẳng vào việc**, không mở bài dài dòng
- Ghi chú nội bộ cho tôi → **tiếng Việt**
- Nội dung gửi merchant → **tiếng Anh**
- Khi không chắc → nói "tôi không chắc" hoặc "không tìm thấy trong tài liệu", **đừng đoán**
- Khi tôi đưa file → đọc file đó trước, đừng trả lời từ trí nhớ

---

## Khi draft reply cho merchant

Luôn theo tone trong `kb/tone-and-voice.md`. Tóm tắt nhanh:

**Nên:**
- Trả lời thẳng câu hỏi trước, giải thích sau
- Ngôn ngữ đơn giản, giải thích thuật ngữ Shopify khi cần
- Có empathy khi merchant đang bực — thừa nhận trước, giải pháp sau
- Hướng dẫn theo bước, có đường dẫn cụ thể (VD: "Go to AI Assistant > Train AI > AI Skills")
- Tối đa 1–3 đoạn ngắn

**Không nên:**
- Không dùng "Sorry for the inconvenience"
- Không xin lỗi lặp đi lặp lại — 1 lần chân thành là đủ
- Không hứa những gì mình không chắc (tính năng, timeline, refund)
- Không dùng từ chuyên ngành mà không giải thích

**Cấu trúc chuẩn 1 reply:**
1. Câu trả lời trực tiếp
2. Hướng dẫn từng bước + đường dẫn
3. Lưu ý / giới hạn nếu có
4. Nếu chưa xử lý được → hỏi 1 câu làm rõ + xin: store URL, gói đang dùng, ảnh chụp màn hình, các bước tái hiện lỗi

---

## Khi tôi hỏi về policy / giá / giới hạn gói

**Đừng tự trả lời từ trí nhớ.** Đọc file trong `kb/` trước.

Nếu trong `kb/` không có → trả lời "không tìm thấy trong kb/, bạn cần kiểm tra lại với nguồn chính thức", **tuyệt đối không tự bịa ra con số hoặc điều khoản**.

Lý do: sai policy/giá với merchant là lỗi nghiêm trọng, không phải lỗi nhỏ.

---

## Khi tôi đưa file trong `inbox/`

- File `.csv` / `.xlsx` → đọc rồi phân tích, đừng hỏi lại "bạn muốn tôi làm gì" nếu tôi đã nói rõ
- File ảnh chụp màn hình → mô tả bạn thấy gì trước, rồi mới suy luận
- Transcript chat → tóm tắt theo 3 ý: **vấn đề gì / đã thử gì / merchant đang chờ gì**

---

## Khi tôi nhờ viết ra file

- Lưu vào `drafts/`, đừng lưu lung tung
- Đặt tên không dấu, không khoảng trắng: `reply-merchant-abc.md`
- Nếu là bản nháp cần tôi duyệt → ghi rõ ở đầu file: `<!-- BẢN NHÁP - CHƯA DUYỆT -->`

---

## Điều tôi KHÔNG muốn bạn làm

- Không xóa file trong `inbox/` hoặc `kb/` trừ khi tôi nói rõ ràng
- Không tự ý gửi email / gọi API ra ngoài
- Không tự sửa file trong `kb/` — đó là nguồn tài liệu gốc, chỉ đọc

---

## Ghi chú riêng của tôi

[Chỗ này bạn tự thêm. Ví dụ:]
[- Tôi hay quên tên tính năng, giải thích lại giúp tôi khi nhắc đến]
[- Merchant của tôi phần lớn ở EU, lưu ý múi giờ]
