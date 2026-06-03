# Bots

Tổng hợp các bot automation của CS team. Mỗi bot có folder riêng chứa code, config, và .env.

---

## chatty-feedback-bot

**Mục đích:** Tự động tag CS Chatty đang trực khi merchant gửi feedback về AI reply.

**Flow:**
1. Poll channel feedback mỗi 15 phút, lookback 120 phút
2. Có feedback mới → check workshift → tag Chatty CS đang trực vào thread
3. 60 phút sau nếu CS chưa reply → nhắc 1 lần
4. CS reply hoặc đã nhắc → xong

**Config:** Sửa `chatty-feedback-bot/config.json` (message, CS list, timing) — không cần restart bot.

**Spec chi tiết:** [playbooks/chatty-feedback-bot.md](../playbooks/chatty-feedback-bot.md)

**Run:** `cd chatty-feedback-bot && npm start`

---

## cs-remind-bot

**Mục đích:** Sau 24h, tự động tag CS chưa acknowledge thông báo `@channel` của Liz trong cs-group-2.

**Flow:**
1. Poll cs-group-2 mỗi 1 giờ
2. Tìm messages của Liz có `@channel`, đã đủ 24h tuổi
3. Check reactions + thread replies — CS nào chưa react VÀ chưa reply → tag vào thread
4. Bot đã reply trong thread → skip (không nhắc lại)

**Config:** Sửa `cs-remind-bot/config.json` (CS list, message, timing) — không cần restart bot.

**Spec chi tiết:** [playbooks/cs-remind-bot.md](../playbooks/cs-remind-bot.md)

**Run:** `cd cs-remind-bot && npm install && npm start`
