# Playbook: cs-remind-bot

## Mục đích
Tự động remind CS chưa acknowledge thông báo `@channel` của Liz trong channel cs-group-2, sau 24h kể từ lúc thông báo được gửi.

**Acknowledged** = đã react bằng bất kỳ emoji nào, HOẶC đã reply vào thread.

## Flow

```
Liz gửi message có @channel vào cs-group-2
        ↓
Bot poll mỗi 1 giờ
        ↓
Message đủ 24h tuổi?
  ├── Chưa → skip, chờ poll sau
  └── Rồi → fetch thread replies
              ↓
        Bot đã reply trong thread?
          ├── Rồi → đã xử lý, skip
          └── Chưa → check reactions + replies của CS
                        ↓
                acknowledged = đã react ∪ đã reply (trừ Liz & bot)
                        ↓
                CS nào chưa acknowledged?
                  ├── Tất cả đã acknowledged → log, skip (không post gì)
                  └── Còn CS chưa acknowledged → tag vào thread (1 lần)
```

## Trigger conditions
- Message gửi bởi Liz (`LEADER_USER_ID` trong `.env`)
- Message chứa `@channel` (Slack format: `<!channel>`)
- Message đã đủ `delayHours` (mặc định 24h)

## Behavior
- **Acknowledged** khi CS: react bất kỳ emoji nào, HOẶC reply vào thread
- **1 lần duy nhất:** Bot tag 1 lần rồi thôi, không remind lần 2
- **Tracking:** Bot dùng reply của chính nó trong thread để biết đã xử lý — restart bot không bị tag lại
- **Liz excluded:** Reply của Liz trong thread không tính là CS acknowledge
- **TODO Slack IDs:** CS chưa có Slack ID trong config.json sẽ bị skip (không tag được)

## Config (`config.json`)

| Field | Default | Ý nghĩa |
|---|---|---|
| `pollIntervalMinutes` | 60 | Tần suất poll channel |
| `delayHours` | 24 | Thời gian chờ trước khi check |
| `bufferHours` | 2 | Cửa sổ xử lý sau khi đủ delay (24h–26h) |
| `message` | _(string)_ | Nội dung tag vào thread |
| `g2CS` | _(object)_ | Map nickname → Slack ID của toàn bộ CS G2 |

## Setup

### 1. Slack App permissions
Bot cần các OAuth scopes:
- `groups:history` — đọc messages và thread replies (private channel)
- `reactions:read` — đọc reactions
- `chat:write` — post vào thread

Bot phải được **invite vào cs-group-2**.

### 2. Environment variables
Copy `.env.example` → `.env` và điền:
```
SLACK_BOT_TOKEN=xoxb-...
ANNOUNCE_CHANNEL_ID=C...   # ID của cs-group-2
LEADER_USER_ID=U02GT4PC6RH # Slack ID của Liz
```

### 3. Điền Slack IDs còn thiếu
Mở `config.json`, tìm các entry `"TODO"` và điền Slack ID thực. Hiện còn thiếu:
- `NganDT` (Abby)
- `LinhTLK` (Linda)

### 4. Chạy bot
```bash
cd bots/cs-remind-bot
npm install
npm start
```

## Maintenance

**Thêm CS mới:** Thêm entry vào `g2CS` trong `config.json` — không cần restart.

**CS nghỉ/off:** Xóa entry hoặc để `"TODO"` → bot sẽ skip người đó.

**Đổi delay:** Sửa `delayHours` trong `config.json`.
