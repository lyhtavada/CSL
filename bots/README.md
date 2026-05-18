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

## chatty-insight-bot

**Mục đích:** Tổng hợp weekly insights từ #chatty-cs-issues — top bugs, issues, feature requests — và draft FAQ cho recurring topics.

**Flow:**
1. Chạy mỗi thứ Hai 9:00 AM VN time
2. Đọc channel C07AZNGEVTM, lookback 7 ngày
3. Claude phân loại messages → gộp theo topic, đếm số lần xuất hiện
4. Post weekly digest vào channel
5. Topic xuất hiện ≥ 3 lần → Claude draft FAQ → reply vào thread digest

**Config:** Sửa `chatty-insight-bot/config.json` (runDay, runHour, lookbackDays, recurringThreshold) — không cần restart bot.

**Spec chi tiết:** [playbooks/chatty-insight-bot.md](../playbooks/chatty-insight-bot.md)

**Run:** `cd chatty-insight-bot && npm install && npm start`
**Test ngay:** `node index.js --now`

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

---

## call-followup

**Mục đích:** Web form để CS log thông tin sau mỗi quick call với merchant. Data lưu vào Supabase.

**Flow:**
1. CS mở link web form (bookmark sẵn)
2. Nhập password 1 lần (cookie giữ 30 ngày)
3. Điền thông tin call → bấm Save
4. Supabase Edge Function insert data vào table `call_followup`

**Khác biệt:** Chạy trên Supabase cloud (Edge Function) — không cần máy nào bật, không cần Slack app.

**Setup:** Xem `call-followup/README.md`

**Spec chi tiết:** [playbooks/quick-call-support.md](../playbooks/quick-call-support.md)
