# (Loyalty blocks) Translation cho store multi-language không work khi đổi language

Category: Translations
PIC: Trương Cảnh Huy

### Problem:

MC đã add đa ngôn ngữ trong setting Translation, khi thử chuyển đổi giữa các ngôn ngữ trên live store thì thấy ở một số ngôn ngữ, content của loyalty blocks trên site không được translate. Lý do có thể là MC đã đồng thời dùng các app translate bên ngoài để translate page của mình, ví dụ như Translate & Adapt, có thể ghi đè data meta content của page và gây lỗi.

---

### Solution:

Flow support tham khảo:

- Hỏi MC để xác nhận xem có đang dùng app nào để translate page không
- Nếu MC không rõ, cần xin quyền apps để có thể check hoặc chuyển cho TS kiểm tra kỹ hơn

Nếu là Translate & Adapt, là một app quen thuộc thì CS sau khi có quyền có thể check qua trước. Kiểm tra xem trong Meta content của ngôn ngữ mà bị lỗi > các row của Joy có đang bị ghi đè không.

Nếu loại bỏ content đang ghi đè mà vẫn lỗi thì nên tạo card check với TS để tìm cách recover cho đúng.

![image.png]((Loyalty%20blocks)%20Translation%20cho%20store%20multi-langu/image.png)

Thường các case này MC tưởng meta field của mình dịch được, nên paste vào các row đó text mà họ muốn dịch, khiến nó freeze luôn content trên widget của mình, khi app mình translate nó sẽ không work nữa.