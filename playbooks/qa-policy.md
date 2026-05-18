# QA Policies

**Owner:** Daisy Vo
**Created:** April 16, 2025

---

## I. Quy trình QA

### 1. Mục đích

Đảm bảo dịch vụ hỗ trợ khách hàng được cung cấp với chất lượng cao nhất, nâng cao sự hài lòng của khách hàng, giảm thiểu sai sót và cải thiện hiệu quả làm việc của đội ngũ CS.

### 2. Cách thực hiện

- **Thời gian:** Xuyên suốt mỗi tháng
- **Sampling:** Mỗi CS agent được CSL chọn ngẫu nhiên **20 cuộc chat** từ các app khác nhau
- **Đánh giá theo 3 tiêu chí:** Quy trình · Kiến thức · Kỹ năng

---

## II. Mức độ vi phạm & Penalty

> **Lưu ý:** Mức độ vi phạm dựa trên **tính chất, rủi ro tiềm ẩn** và **mức độ quan trọng** với trải nghiệm khách hàng và vận hành nội bộ — **không phụ thuộc vào việc khách hàng có than phiền hay không**. Mọi lỗi có nguy cơ ảnh hưởng đến chất lượng dịch vụ đều cần được ghi nhận.

| Mức độ | Tính chất | Tần suất cho phép/tháng | Penalty |
|---|---|---|---|
| **Urgent** | Đặc biệt nghiêm trọng — vi phạm bảo mật, tài chính, đạo đức, có rủi ro mất khách hoặc bad review công khai | 0 lần | Case by case (có thể THÔI VIỆC) |
| **Critical** | Nghiêm trọng cao — sai sót trong tư vấn/xử lý/quy trình, rủi ro cao về tài chính hoặc mất khách | 0 lần | -50đ/lần |
| **High** | Nghiêm trọng cao + Quan trọng vừa — ảnh hưởng chất lượng dịch vụ, giảm hiệu suất nội bộ đáng kể | 1 lần | -40đ/lần |
| **Moderate** | Nghiêm trọng vừa — lỗi nhỏ gây khó chịu cho KH, nếu lặp lại sẽ ảnh hưởng mục tiêu team | 2 lần | -30đ/lần |
| **Low** | Nghiêm trọng thấp — ít ảnh hưởng trực tiếp nhưng cần cải thiện để duy trì tính chuyên nghiệp | 3 lần | -20đ/lần |

---

## III. Chi tiết lỗi theo danh mục

### A. Quy trình (QT)

#### Workshift

| Code | Nội dung | Mức độ | Penalty |
|---|---|---|---|
| QT1 | Checkin trước khi có mặt tại công ty và bắt đầu làm việc | Critical | -50 |
| QT2 | Ca 3, ca 4 làm việc ở nhà mà không báo cáo lý do và được phê duyệt bởi manager | Critical | -50 |
| QT3 | Không active trong ca trực (last message ≥30p hoặc tổng chat không đạt 70% yêu cầu tối thiểu) | Urgent | Case by case |
| QT4 | Ảnh chụp màn hình checkin/checkout không đúng quy định | Critical | -50 |
| QT28 | Bỏ ca | Urgent | Case by case |
| — | Fake checkin | Urgent | THÔI VIỆC |

#### Live chat

| Code | Nội dung | Mức độ | Penalty |
|---|---|---|---|
| QT5 | Thiếu bổ sung thông tin cơ bản (URL, email, store pw, review…) vào hội thoại, gây khó khăn cho người tiếp nhận hoặc theo dõi sau | Low | -20 |
| QT6 | Thiếu giải thích rõ ràng khi xin quyền hoặc không liệt kê đầy đủ quyền cần xin | Low | -20 |
| QT7 | Xin quyền Shopify admin trong những tình huống không thực sự cần thiết | Moderate | -30 |
| QT8 | Thời gian trả lời tin nhắn đầu tiên của KH quá 2 phút (trừ point toàn bộ agent trong ca) | Moderate | -30 |
| QT9 | Yêu cầu thông tin không cần thiết khiến hội thoại kéo dài, không đi thẳng vào vấn đề | Moderate | -30 |
| QT10 | Không tuân thủ flow xử lý theo quy định cho từng app (confirm URL, refund, downgrade, nhận call…) | Moderate | -30 |
| QT11 | Không phản hồi tin nhắn của KH trong ca trực | Critical | -50 |
| QT12 | Thiếu minh bạch khi support KH, không giải thích rõ quá trình xử lý, nguyên nhân vấn đề | Critical | -50 |
| QT33 | Chat với KH trên điện thoại/Tablet | Critical | -50 |

#### Follow-up

| Code | Nội dung | Mức độ | Penalty |
|---|---|---|---|
| QT13 | Không confirm các thông báo, update về sản phẩm/quy trình trong vòng 24h | Low | -20 |
| QT14 | Tạo card trùng cho issue vẫn còn card pending trước đó | Low | -20 |
| QT15 | Update KH không đúng hoặc không đầy đủ thông tin như TS/dev đưa ra | Moderate | -30 |
| QT16 | Khi hết ca, không bàn giao đầy đủ thông tin/assign chat/card cho người nhận ca sau | Moderate | -30 |
| QT17 | Không follow up với TS/dev đúng thời hạn: trong 24h với issue, 48h với bug | Moderate | -30 |
| QT18 | Kết thúc ca mà không báo KH bước tiếp theo (bàn giao, chờ xử lý, thời gian phản hồi…) | Moderate | -30 |
| QT24 | Không kiểm tra lại kết quả/không kiểm chứng tính chính xác của thông tin từ TS trước khi báo KH | Moderate | -30 |
| QT29 | Khi tạo ticket, không ghi rõ chi tiết yêu cầu/lỗi (thiếu ngữ cảnh, bước tái hiện, dữ liệu liên quan…) khiến TS/dev phải hỏi lại nhiều lần hoặc xử lý sai hướng | High | -40 |
| QT20 | Không cập nhật KH sau khi có update từ TS/dev. Trong ca: phản hồi ngay; ngoài ca: phản hồi trong ca tiếp theo; tối đa 24h | High | -40 |
| QT22 | Bỏ sót câu hỏi/yêu cầu của KH, kể cả được bàn giao từ ca trước | High | -40 |
| QT23 | KH update thông tin/cho quyền nhưng không update nội dung và status card/thread | High | -40 |
| QT25 | CS không phản hồi lại KH sau khi đã hẹn kiểm tra trong ca trực | High | -40 |
| QT26 | CS quên tạo card/chuyển thiếu issue cho TS/dev | Critical | -50 |

#### Review

| Code | Nội dung | Mức độ | Penalty |
|---|---|---|---|
| QT27 | Xin review sai quy định | Urgent | Case by case |
| QT28 | Không chủ động xin review sau khi support KH thành công | Moderate | -30 |
| QT30 | Không chủ động xin hoặc follow up để lấy review sau khi hoàn tất hỗ trợ (bao gồm sau support thành công, enable feature, hoặc fix issue/hướng dẫn xong) | Critical | -50 |
| QT31 | Support thêm chưa đủ nhưng đã xin review | Moderate | -30 |
| QT32 | Xin review ngay sau khi enable feature | Critical | -50 |

---

### B. Bảo mật (BM)

| Code | Nội dung | Mức độ | Penalty |
|---|---|---|---|
| BM1 | Lưu trữ dữ liệu/thông tin KH phục vụ mục đích cá nhân. Chia sẻ thông tin kinh doanh (doanh thu, KH…) cho người không liên quan | Urgent | Case by case |
| BM2 | Xin các quyền nhạy cảm (edit payment, approve charge…) hoặc xin full quyền mà không có lý do hợp lý | Critical | -50 |

---

### C. Kiến thức (KT)

| Code | Nội dung | Mức độ | Penalty |
|---|---|---|---|
| KT1 | Cung cấp sai thông tin về tính năng, giá hoặc chính sách (khuyến mãi) | Critical | -50 |
| KT2 | Không nắm rõ tính năng/vấn đề có FAQs/user guide đầy đủ nhưng không làm theo, dẫn đến hỗ trợ không hiệu quả, kéo dài thời gian | Critical | -50 |

---

### D. Kỹ năng (KN)

#### Giao tiếp

| Code | Nội dung | Mức độ | Penalty |
|---|---|---|---|
| KN1 | Sử dụng sai ngữ pháp, chính tả, cấu trúc email hoặc tin nhắn không chuyên nghiệp | Low | -20 |
| KN2 | Hỏi lại thông tin KH đã cung cấp trong cùng hội thoại | Moderate | -30 |
| KN3 | Hướng dẫn/giải thích chưa đầy đủ hoặc chưa rõ ràng, khiến KH khó hiểu | Moderate | -30 |
| KN4 | Phản hồi chậm trễ (≥10p) trong khi đang xử lý hội thoại, làm gián đoạn trải nghiệm KH | High | -40 |

#### Xử lý tình huống

| Code | Nội dung | Mức độ | Penalty |
|---|---|---|---|
| KN5 | Chưa hiểu đúng vấn đề, dẫn đến tư vấn sai hoặc đưa ra hướng xử lý không phù hợp | High | -40 |
| KN6 | Chưa thu thập đủ thông tin từ KH dẫn đến kết luận không chính xác hoặc không phù hợp | Moderate | -30 |
| KN7 | Đưa ra câu trả lời chung chung, không trực tiếp giải quyết câu hỏi/tình huống của KH. Tư vấn hời hợt mà không giải thích rõ các bước tiếp theo | Moderate | -30 |
| KN8 | Sử dụng câu bị đánh giá là mất lịch sự hoặc không đúng hướng dẫn, dẫn đến phản ứng tiêu cực từ KH | Urgent | Case by case |
| KN9 | KH rate 1–3 sao vì lý do từ phía agent (có lý do rõ ràng, nằm trong quy định ở file quy trình Customer Success) | Urgent | Case by case |

---

## IV. Xử lý lỗi

### Phân quyền

- QA là quản lý trực tiếp của CS — mọi ý kiến của QA phải được tôn trọng
- QA có quyền monitor hội thoại và record lỗi độc lập
- CS có quyền khiếu nại cách xử lý của QA lên CSL và CSM
- **CEO là người xem xét cuối cùng**

### Lỗi lặp lại

Lỗi được coi là **lặp lại** khi:
1. Đã xuất hiện trong kết quả QA tháng trước
2. Tiếp tục xuất hiện trong tháng hiện tại với số lần vi phạm ≥ số lần của tháng trước
3. Tính theo từng lỗi cụ thể, không tính gộp các lỗi khác loại

Xử lý: Hệ thống **highlight màu đỏ** khi lỗi đã từng xảy ra tháng trước và vượt tần suất lặp lại cho phép.

> **Note:** Theo dõi kết quả sau 2–3 tháng để đưa ra quy chuẩn → sau đó đề xuất xử lý lỗi lặp lại chính thức.
