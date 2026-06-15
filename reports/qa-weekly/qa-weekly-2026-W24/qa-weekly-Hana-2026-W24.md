# QA Tuần 2026-W24 — Hana
**App:** Joy · **Kỳ:** 08/06 – 14/06/2026

## 📊 Điểm tuần: 84/100 — Tốt  (= 0 so với W23: 84)
- 🧠 Mindset 28.1/34 · 📚 Kiến thức 28.7/33 · 🛠️ Xử lý 27.2/33
- 🔍 Đã QA: 28 chat
- Trục yếu nhất: **Xử lý**

## 🚨 Severe flag — Liz xem kỹ trước khi gửi
- Chat #1 [live_store_access]: Hana asked for and received the live store admin password. [13:32:41] CS (Hana): 'Can you share with me the password to your live store please?' — customer provided password 'agha1122'. Shopify partner access request (4-digit code) is correct procedure; asking for the admin login password is not.

## 📝 Nhận xét chung
Hana giữ phong độ ổn định, ownership mạnh và kiến thức Joy vững (NCA/duplicate account, grandfathered pricing, Omnisend). Nhưng tuần này có một vấn đề NGHIÊM TRỌNG về bảo mật: bạn xin và nhận mật khẩu admin live store của khách (chat #1) — điều tuyệt đối không được làm, phải dùng Shopify collaborator request như chính bạn đã làm đúng ở chat #28. Ngoài ra còn lỗi gửi tin trùng (KN1, lặp từ W23) và lệch ngôn ngữ với khách Ý (KN3). Ưu tiên số 1 tuần tới: không bao giờ xin mật khẩu/thông tin đăng nhập của khách.

## ✅ Điểm tốt
- Strong ownership — proactive DFY and full issue resolution
   > Chat #5: Transaction limit fix clean from start to finish. Chat #6: Full referral setup end-to-end without prompting. Chat #10: CSS fix completed in ~5 minutes. Chat #25: Smooth DFY coordination.
- Solid product knowledge across complex scenarios
   > Chat #2: NCA/duplicate account explanation accurate and complete. Chat #3: Grandfathered pricing verified and confirmed correctly. Chat #17: Pre-launch sync resolution immediate and correct. Chat #27: Omnisend native integration explained with correct path and feature list.

## 🔧 Cần cải thiện
- **[LIVE_STORE] · severe** Requested and received merchant's live store admin password
   > Chat #1: [13:32:41] CS (Hana): 'Can you share with me the password to your live store please?' Customer replied with password 'agha1122'. Correct procedure is Shopify partner access request (4-digit code) — as Hana herself used in Chat #28.
- **[KN1] · low** Duplicate message sent
   > Chat #18: '[09:59:08] CS (Hana): Pending Points is a feature in Joy Loyalty that introduces a delay in making points available after a purchase.' → '[09:59:16] CS (Hana): Pending Points is a feature in Joy Loyalty that introduces a delay in making points available after a purchase.' Identical message 8 seconds apart. Pattern carried from W23.
- **[KN3] · low-moderate** Language mismatch — English message to Italian-speaking customer
   > Chat #26: Customer (osmesi.myshopify.com) communicated entirely in Italian throughout. [10:41:11] CS (Hana): 'I've sent you an access request which can be seen in your Shopify admin > Settings > [Users]...' — sent in English. Message should have been in Italian or relayed through Mirra/Rosie who were handling in Italian.
- **[QT22] · low** Review ask while still handling open issue
   > Chat #1: Asked for review while still in the middle of live store access work. Chat #6: Asked slightly early while referral program still being configured. Pattern from W23 QT22 partially persists.

## 🌟 Xin review (chỉ ghi nhận, KHÔNG tính điểm)
- Đã xin 9/23 chat phù hợp (đúng lúc 7, chưa đúng lúc 2).
- Observe only — NOT scored

## 📈 So với tuần trước (W23)
- Điểm 84 → 84 (= 0)
