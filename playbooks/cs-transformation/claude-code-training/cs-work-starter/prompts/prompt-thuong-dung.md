# Thư viện prompt — copy về sửa rồi dùng

> Cách dùng: tìm việc bạn cần → copy cả khối → thay chỗ `<...>` → paste vào Claude.
>
> **Prompt nào bạn dùng thấy hay, thêm vào cuối file này.** Đây là vốn chung của team.

---

## Công thức gốc — nhớ 4 phần này là đủ

```
[BỐI CẢNH]   Ai, chuyện gì, đang ở tình trạng nào
[VIỆC CẦN]   Bạn muốn nó làm gì, cụ thể
[NGUỒN]      Dựa vào file nào / dữ liệu nào
[ĐỊNH DẠNG]  Ra cái gì: dài bao nhiêu, tiếng gì, kiểu gì
```

Thiếu phần nào cũng ra kết quả — nhưng thiếu **NGUỒN** thì nó bịa, thiếu **ĐỊNH DẠNG** thì bạn phải sửa tay.

---

## 1. Draft reply cho merchant

```
Merchant dùng <app>, gói <gói>, đang <mô tả tình huống + cảm xúc của họ>.
Họ hỏi/phàn nàn: "<paste nguyên câu của merchant>"

Draft cho tôi 1 reply.

Theo tone trong kb/tone-and-voice.md.
Tiếng Anh, dưới 150 từ, tối đa 3 đoạn.
Không dùng "Sorry for the inconvenience".
Kết bằng 1 bước tiếp theo rõ ràng.
```

---

## 2. Draft reply cho merchant đang rất bực

```
Merchant đang rất bực, đây là chat: <paste transcript>

Trước khi draft, cho tôi biết:
1. Họ bực vì cái gì — nguyên nhân gốc, không phải câu chữ bề mặt
2. Cái họ thật sự muốn là gì

Rồi mới draft reply. Theo kb/tone-and-voice.md.
Thừa nhận cảm xúc trước, giải pháp sau. Xin lỗi 1 lần thôi.
Không hứa timeline nếu tôi chưa nói với bạn timeline.
```

---

## 3. Tóm tắt 1 chat dài

```
Đọc transcript trong inbox/<tên file>.

Tóm tắt theo đúng 3 mục, mỗi mục 1-2 câu:
1. Vấn đề: merchant đang gặp gì
2. Đã thử: những gì đã làm rồi, kết quả ra sao
3. Đang chờ: merchant đang đợi gì từ mình

Cuối cùng thêm 1 dòng: mức độ gấp (thấp/vừa/cao) và vì sao.
Tiếng Việt.
```

---

## 4. Phân tích file export chat / ticket

```
Đọc inbox/<tên file>.

Cho tôi:
1. Tổng số hội thoại
2. Top 5 vấn đề merchant hỏi nhiều nhất, kèm số lượng và % 
3. Nhóm nào tăng bất thường so với phần còn lại
4. 3 câu hỏi lặp đi lặp lại mà đáng lẽ nên có trong FAQ

Trình bày dạng bảng. Tiếng Việt.
Nếu file thiếu cột cần thiết thì nói ra, đừng đoán.
```

---

## 5. Dịch & localize

```
Dịch đoạn sau sang <tiếng Việt / tiếng Anh>: <paste>

Yêu cầu:
- Giữ nguyên tên tính năng và đường dẫn menu, không dịch
- Giọng tự nhiên như người bản xứ viết, không dịch word-by-word
- <Nếu là nội bộ: ngắn gọn, không cần lịch sự quá>
```

---

## 6. Viết quy trình / SOP từ các case thật

```
Đây là <số> case tôi đã xử lý: <paste hoặc chỉ file trong inbox/>

Viết cho tôi 1 quy trình xử lý chuẩn cho loại case này:
- Các bước theo thứ tự
- Mỗi bước có điều kiện để biết khi nào xong, khi nào chuyển bước
- Trường hợp ngoại lệ nào cần escalate và escalate cho ai
- Câu mẫu để CS dùng ở từng bước

Lưu vào drafts/. Tiếng Việt. Đây là bản nháp, tôi sẽ duyệt lại.
```

---

## 7. Soạn báo cáo có insight

```
Số liệu tuần này: <paste hoặc chỉ file>

Viết báo cáo tuần. Yêu cầu quan trọng:
- KHÔNG liệt kê lại số. Tôi tự đọc số được.
- Chỉ ra cái gì thay đổi so với bình thường và ý nghĩa của nó
- 3 điều đáng chú ý nhất, mỗi điều 2-3 câu
- 1 việc nên làm tuần tới

Nếu dữ liệu không đủ để kết luận thì nói thẳng, đừng cố suy diễn.
```

---

## 8. Học sản phẩm / hỏi kiến thức

```
Giải thích tính năng <tên> cho một CS mới vào chưa biết gì.

- Nó dùng để làm gì, giải quyết vấn đề gì của merchant
- Merchant bật/dùng nó ở đâu (đường dẫn cụ thể)
- 3 câu merchant hay hỏi nhất về nó và cách trả lời
- 1 lỗi/hiểu lầm phổ biến

Dựa vào file trong kb/. Chỗ nào kb/ không có thì ghi rõ "kb/ chưa có mục này".
```

---

## 9. Kiểm tra lại bản nháp trước khi gửi

```
Đọc lại draft này trước khi tôi gửi merchant: <paste>

Soát giúp tôi:
1. Có con số / policy / timeline nào tôi chưa verify không? Liệt kê ra.
2. Có câu nào nghe như đang hứa hẹn quá không?
3. Tone có đúng kb/tone-and-voice.md không?
4. Có dài dòng chỗ nào cắt được không?

Chỉ ra vấn đề, đừng tự viết lại trừ khi tôi bảo.
```

> Prompt số 9 nên dùng thường xuyên. Nó là cái phanh.

---

## 10. Khi bạn không biết bắt đầu thế nào

```
Tôi cần làm <mô tả việc>. Tôi có <mô tả dữ liệu đang có>.

Đừng làm ngay. Trước hết hỏi tôi 3 câu để hiểu rõ yêu cầu,
rồi đề xuất cách làm, tôi duyệt xong bạn mới làm.
```

---

## Prompt do team đóng góp

<!-- Thêm vào đây. Ghi rõ tên người đóng góp và dùng cho việc gì. -->

### <Tên prompt> — <tên bạn>
Dùng khi: <trường hợp nào>
```
<prompt>
```
