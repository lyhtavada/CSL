# AI ko trả về đúng link sản phẩm theo từng variant

Category: AI Assistant

- **Vấn đề:** AI hiện chỉ gửi được link sản phẩm chung, không phân biệt theo variant (màu, size…), khiến KH khó tìm đúng sản phẩm họ quan tâm
- **Mục đích**
    - Giúp AI trả lời chính xác hơn theo nhu cầu cụ thể của khách
    - Tăng khả năng tư vấn đúng và khả năng convert
- **Mô tả tính năng**
    - Lưu ẩn link các variant của sản phẩm để sử dụng cho AI trả lời
    - Các tình huống liên quan:
        - Hỏi variant cụ thể: *“Do you have this in blue, size L?”*
        - Kiểm tra tồn kho/giá của variant cụ thể
- **Note:** do vấn đề chi phí nên tạm thời chỉ bật ở dev zone để test. Sau khi bật xong, CS đợi app sync lại, sau đó test và báo kết quả với MC.

![image.png](AI%20ko%20tr%E1%BA%A3%20v%E1%BB%81%20%C4%91%C3%BAng%20link%20s%E1%BA%A3n%20ph%E1%BA%A9m%20theo%20t%E1%BB%ABng%20variant/image.png)