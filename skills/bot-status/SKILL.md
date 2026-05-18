---
name: bot-status
description: Use this skill when Liz wants to check if bots are running, asks "bot có chạy không", "check bot", or "bot status". Checks all bots in the bots/ directory and reports which are running, which are down, and any quick fixes.
version: 1.0.0
---

# /bot-status — Check trạng thái các bots

Check tất cả bots xem cái nào đang chạy, cái nào down.

## Bots hiện có

| Bot | Folder | Chạy như thế nào |
|-----|--------|-----------------|
| chatty-feedback-bot | `bots/chatty-feedback-bot/` | `node index.js` (local process) |
| cs-remind-bot | `bots/cs-remind-bot/` | `node index.js` (local process) |
| chatty-insight-bot | `bots/chatty-insight-bot/` | `node index.js` (local process), test: `node index.js --now` |
| call-followup | Supabase Edge Function | Cloud — luôn chạy nếu Supabase up |

## Cách chạy

1. Chạy lệnh sau để check process nào đang running:
```bash
ps aux | grep "node index.js" | grep -v grep
```

2. Xem process ID và folder đang chạy

3. Check từng bot:
```bash
# chatty-feedback-bot
cd ~/CSL/bots/chatty-feedback-bot && node index.js --dry-run 2>&1 | head -5

# cs-remind-bot
cd ~/CSL/bots/cs-remind-bot && node index.js --dry-run 2>&1 | head -5
```

4. Đọc `bots/README.md` để xem danh sách đầy đủ và run commands

## Output Format

```
🤖 Bot Status — {ngày giờ}

**chatty-feedback-bot** — ✅ Running / ❌ Down / ⚠️ Unknown
**cs-remind-bot** — ✅ Running / ❌ Down / ⚠️ Unknown
**chatty-insight-bot** — ✅ Running / ❌ Down / ⚠️ Unknown
**call-followup** — ☁️ Supabase cloud (check supabase.com nếu cần)

---
[Bot nào down: hướng dẫn restart ngay]
```

## Quick restart

Nếu bot down, restart bằng:
```bash
cd ~/CSL/bots/[bot-name] && npm start
```

Nếu cần chạy background (không tắt khi đóng terminal):
```bash
cd ~/CSL/bots/[bot-name] && nohup npm start > bot.log 2>&1 &
```

Check log gần nhất:
```bash
tail -50 ~/CSL/bots/[bot-name]/bot.log
```

## Notes

- Các bot local chạy trên máy Liz → tắt máy là bot tắt theo
- Nếu muốn bot chạy liên tục 24/7 → cần deploy lên server hoặc dùng PM2
- `call-followup` là exception — chạy trên Supabase, không cần local
- Nếu Liz hỏi bot có chạy không mà không có terminal output → hỏi lại để chạy lệnh check
