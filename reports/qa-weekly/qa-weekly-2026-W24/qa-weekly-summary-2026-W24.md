# QA Weekly Summary — 2026-W24 (08/06 – 14/06/2026)
**Team in-house (9 CS) · rubric 3 trục · coaching, không phải penalty**

> ⏳ CHỜ LIZ DUYỆT — chưa gửi DM cho CS. Liz review xong, ra lệnh thì mới gửi.

| CS | Điểm | Δ W23 | 🧠 Mind | 📚 Know | 🛠️ Skill | Chat | Xin review | Trục yếu | Flag |
|---|---|---|---|---|---|---|---|---|---|
| Alyssa | 87 (Tốt) | ▼ -1 | 28.8 | 29.3 | 28.6 | 30 | 5/16 | Mindset |  |
| Audrey | 87 (Tốt) | ▲ +4 | 28.3 | 29.6 | 28.8 | 19 | 3/3 | Mindset |  |
| Andy | 85 (Tốt) | ▲ +1 | 27.4 | 29.4 | 28.0 | 29 | 5/13 | Mindset |  |
| Sonny | 84 (Tốt) | ▼ -7 | 29.2 | 28.1 | 26.8 | 30 | 10/19 | Xử lý | 🚨 |
| Hana | 84 (Tốt) | = 0 | 28.1 | 28.7 | 27.2 | 28 | 9/23 | Xử lý | 🚨 |
| Hazel | 84 (Tốt) | ▲ +1 | 28.4 | 27.8 | 27.3 | 30 | 10/12 | Xử lý | 🚨 |
| Jade | 83 (Tốt) | ▲ +1 | 27.4 | 27.9 | 27.7 | 30 | 2/4 | Mindset |  |
| Linda | 83 (Tốt) | ▲ +3 | 24.0 | 29.0 | 27.0 | 30 | 8/24 | Mindset |  |
| Phoebe | 79 (Đạt) | ▼ -4 | 26.0 | 27.2 | 26.0 | 29 | 3/4 | Mindset |  |

**TB team W24:** 84.0/100  (W23: 84.2 → W24: 84.0)

## 🚨 Severe flags — Liz xem kỹ trước khi gửi CS
### Sonny
- Chat #9 [live_store_mistake]: Re-sync database để tìm 1 khách hàng khiến 2496 members bị convert thành guest. Sonny xử lý recovery nhưng thiệt hại đã xảy ra.
- Chat #27 [live_store_mistake]: Switch widget sang live mà không có explicit approval từ khách sau khi không nhận được reply.
### Hana
- Chat #1 [live_store_access]: Hana asked for and received the live store admin password. [13:32:41] CS (Hana): 'Can you share with me the password to your live store please?' — customer provided password 'agha1122'. Shopify partner access request (4-digit code) is correct procedure; asking for the admin login password is not.
### Hazel
- Chat #11 [CREDENTIAL_REQUEST]: Hazel explicitly requested merchant's plaintext email and password in Crisp chat. Customer complied, sharing credentials in plain text. This violates Avada security policy and must be addressed immediately.
- Chat #5 [2FA_PIN_RECEIVED]: Customer shared 2FA PIN '935141' in chat after Hazel's team requested access. Hazel forwarded it to dev team without warning merchant about the security risk of sharing OTPs.

## 🌟 Xin review — ai hay bỏ lỡ chat vàng
- **Alyssa**: chỉ xin 5/16 chat phù hợp
- **Linda**: chỉ xin 8/24 chat phù hợp
- **Andy**: chỉ xin 5/13 chat phù hợp
- **Hana**: chỉ xin 9/23 chat phù hợp

## 📝 Lưu ý KB-verify
- Không có CS nào bị KT1 trái pricing table (giá/limit đều khớp). Các severe flag tuần này là **vấn đề bảo mật/thao tác live store**, KHÔNG phải KB sai — nhưng Liz nên xác minh trực tiếp transcript trước khi nói chuyện với CS.
