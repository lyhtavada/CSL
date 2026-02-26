# AI suggest sai giá sản phẩm không theo market

Category: AI Assistant
PIC: Ly Hoàng
Type: Dev fix

AI assistant khi suggest sản phẩm thì hiển thị **giá không khớp với market** mà khách đang truy cập. Ví dụ:

- Khách vào market France (`.fr`) currency là €, nhưng giá AI suggest lại lấy theo US domain (USD).
- Điều này khiến giá hiển thị khác so với Shopify Market, gây nhầm lẫn.

---

## Flow xử lý của CS

### 1. Hỏi thông tin từ Merchant

- **Shortcut:** **`!AI-WrongPrice-AskMarket`**
    
    > Could you please confirm if you have already added and set up the Market (e.g., France) in your **Shopify Admin** under [**Markets**](https://prnt.sc/kN_ctgC1ezMf)?
    > 
- **Shortcut:** **`!AI-WrongPrice-AskSync`**
    
    > Could you please confirm if you have enabled [Sync Markets](https://prnt.sc/MGFtDuiGMMwd) in the AI Assistant settings? This is required for the assistant to display product prices according to the correct Market.
    > 

### 2. CS reproduce issue

- Tự vào domain market mà MC báo.
- Hỏi AI với cùng câu hỏi → kiểm tra xem giá suggest có khớp market hay không.

> [Shopify Markets – Những điều CS/TS cần biết](https://www.notion.so/Shopify-Markets-Nh-ng-i-u-CS-TS-c-n-bi-t-265b0da449f180adb5ecd7579510451d?pvs=21)
> 

### 3. Xử lý theo tình huống

### TH1: Merchant chưa add và setup Market

- CS hướng dẫn MC setup Market + bật sync Market trong AI Assistant training.
- **Shortcut:**
    
    > To resolve this, please add and set up the Market (e.g., France) in Shopify Admin under Settings > Markets.
    > 
    > 
    > After that, go to your AI Assistant settings and enable “Sync Markets” so the assistant can fetch and display product prices correctly for that Market.
    > 
- CS có thể chủ động xin quyền để setup phần này giúp MC nếu họ gặp khó khăn.
- CS tiếp tục test lại với MC để đảm bảo AI trả lời đúng sau khi đã add Markets.

### TH2: Merchant đã add Market nhưng vẫn lỗi

- CS xin quyền để kiểm tra trực tiếp Market + Product trong Shopify Admin.
    - **Shortcut:**
        
        > Since you have already added the Market but the issue persists, could you grant us staff access to your **Markets** and Product settings in Shopify Admin? This will allow us to investigate the configuration directly.
        > 
- CS/TS report issue kèm đầy đủ:
    - Screenshot khách cung cấp.
    - Screenshot CS reproduce.
    - Thông tin Market config.
    - Thông tin Product pricing per Market.
- Follow up với Merchant
    - CS/TS giữ liên lạc, cập nhật khi dev đang xử lý / đã fix.