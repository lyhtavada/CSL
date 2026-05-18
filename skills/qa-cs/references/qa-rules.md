# QA Rules Reference

Source: QA Policies (Avada CS Team)
Owner: Daisy Vo

## Violation Levels & Penalties

| Mức độ | Tần suất/tháng | Penalty |
|--------|----------------|---------|
| Urgent | 0 | Case by case (có thể THÔI VIỆC) |
| Critical | 0 | -50đ/lần |
| High | 1 | -40đ/lần |
| Moderate | 2 | -30đ/lần |
| Low | 3 | -20đ/lần |

---

## A. Quy trình (QT)

### Workshift
| Code | Nội dung | Mức độ | Penalty |
|------|----------|--------|---------|
| QT1 | Checkin trước khi có mặt và bắt đầu làm việc | Critical | -50 |
| QT2 | Ca 3/4 làm ở nhà không báo cáo + được phê duyệt | Critical | -50 |
| QT3 | Không active trong ca (last message ≥30p hoặc tổng chat <70% yêu cầu) | Urgent | Case by case |
| QT4 | Ảnh checkin/checkout không đúng quy định | Critical | -50 |
| QT28 | Bỏ ca | Urgent | Case by case |

### Live Chat
| Code | Nội dung | Mức độ | Penalty |
|------|----------|--------|---------|
| QT5 | Thiếu thông tin cơ bản (URL, email, store pw...) vào hội thoại | Low | -20 |
| QT6 | Thiếu giải thích khi xin quyền hoặc không liệt kê đủ quyền | Low | -20 |
| QT7 | Xin quyền Shopify admin không cần thiết | Moderate | -30 |
| QT8 | FRT >2 phút | Moderate | -30 |
| QT9 | Yêu cầu thông tin không cần thiết, kéo dài hội thoại | Moderate | -30 |
| QT10 | Không tuân thủ flow xử lý quy định | Moderate | -30 |
| QT11 | Không phản hồi tin nhắn KH trong ca trực | Critical | -50 |
| QT12 | Thiếu minh bạch khi support, không giải thích rõ | Critical | -50 |
| QT33 | Chat với KH trên điện thoại/Tablet | Critical | -50 |

### Follow-up
| Code | Nội dung | Mức độ | Penalty |
|------|----------|--------|---------|
| QT13 | Không confirm thông báo/update trong 24h | Low | -20 |
| QT14 | Tạo card trùng khi issue còn card pending | Low | -20 |
| QT15 | Update KH không đúng/đủ thông tin từ TS/dev | Moderate | -30 |
| QT16 | Hết ca không bàn giao đủ thông tin/assign chat/card | Moderate | -30 |
| QT17 | Không follow up TS/dev đúng hạn (24h issue, 48h bug) | Moderate | -30 |
| QT18 | Kết thúc ca không báo KH bước tiếp theo | Moderate | -30 |
| QT24 | Không kiểm tra lại kết quả/tính chính xác từ TS trước khi báo KH | Moderate | -30 |
| QT20 | Không cập nhật KH sau khi có update từ TS/dev (max 24h) | High | -40 |
| QT22 | Bỏ sót câu hỏi/yêu cầu của KH | High | -40 |
| QT23 | KH update/cho quyền nhưng không update card/thread | High | -40 |
| QT25 | Không phản hồi KH sau khi đã hẹn kiểm tra | High | -40 |
| QT26 | Quên tạo card/chuyển issue cho TS/dev | Critical | -50 |
| QT29 | Tạo ticket thiếu chi tiết (thiếu context, bước tái hiện...) | High | -40 |

### Review
| Code | Nội dung | Mức độ | Penalty |
|------|----------|--------|---------|
| QT27 | Xin review sai quy định | Urgent | Case by case |
| QT28b | Không chủ động xin review sau support thành công | Moderate | -30 |
| QT30 | Không chủ động xin/follow up lấy review sau hoàn tất hỗ trợ | Critical | -50 |
| QT31 | Support chưa đủ nhưng đã xin review | Moderate | -30 |
| QT32 | Xin review ngay sau khi enable feature | Critical | -50 |

---

## B. Bảo mật (BM)

| Code | Nội dung | Mức độ | Penalty |
|------|----------|--------|---------|
| BM1 | Lưu/chia sẻ dữ liệu KH cho mục đích cá nhân | Urgent | Case by case |
| BM2 | Xin quyền nhạy cảm (payment, approve charge...) không có lý do | Critical | -50 |

---

## C. Kiến thức (KT)

| Code | Nội dung | Mức độ | Penalty |
|------|----------|--------|---------|
| KT1 | Sai thông tin về tính năng, giá, chính sách | Critical | -50 |
| KT2 | Không nắm tính năng có FAQs đầy đủ, support không hiệu quả | Critical | -50 |

---

## D. Kỹ năng (KN)

### Giao tiếp
| Code | Nội dung | Mức độ | Penalty |
|------|----------|--------|---------|
| KN1 | Sai ngữ pháp, chính tả, cấu trúc không chuyên nghiệp | Low | -20 |
| KN2 | Hỏi lại thông tin KH đã cung cấp trong cùng hội thoại | Moderate | -30 |
| KN3 | Hướng dẫn chưa đầy đủ/rõ ràng, KH khó hiểu | Moderate | -30 |
| KN4 | Phản hồi chậm ≥10p trong khi đang xử lý | High | -40 |

### Xử lý tình huống
| Code | Nội dung | Mức độ | Penalty |
|------|----------|--------|---------|
| KN5 | Chưa hiểu đúng vấn đề → tư vấn sai/xử lý không phù hợp | High | -40 |
| KN6 | Chưa thu thập đủ thông tin → kết luận không chính xác | Moderate | -30 |
| KN7 | Trả lời chung chung, không giải quyết trực tiếp câu hỏi | Moderate | -30 |
| KN8 | Câu mất lịch sự, gây phản ứng tiêu cực từ KH | Urgent | Case by case |
| KN9 | KH rate 1–3 sao vì lý do từ phía agent | Urgent | Case by case |
