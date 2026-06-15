# QA Tuần 2026-W24 — Hazel
**App:** Chatty · **Kỳ:** 08/06 – 14/06/2026

## 📊 Điểm tuần: 84/100 — Tốt  (▲ +1 so với W23: 83)
- 🧠 Mindset 28.4/34 · 📚 Kiến thức 27.8/33 · 🛠️ Xử lý 27.3/33
- 🔍 Đã QA: 30 chat
- Trục yếu nhất: **Xử lý**

## 🚨 Severe flag — Liz xem kỹ trước khi gửi
- Chat #11 [CREDENTIAL_REQUEST]: Hazel explicitly requested merchant's plaintext email and password in Crisp chat. Customer complied, sharing credentials in plain text. This violates Avada security policy and must be addressed immediately.
- Chat #5 [2FA_PIN_RECEIVED]: Customer shared 2FA PIN '935141' in chat after Hazel's team requested access. Hazel forwarded it to dev team without warning merchant about the security risk of sharing OTPs.

## 📝 Nhận xét chung
Hazel tone ấm, ổn định và xử lý kỹ thuật tốt (WABA, metafield). Nhưng tuần này có 2 lỗi bảo mật nghiêm trọng: chat #11 bạn trực tiếp xin email + mật khẩu của khách (khách đã gửi plaintext), và chat #5 nhận mã 2FA rồi chuyển cho dev mà không cảnh báo khách. Đây là vi phạm chính sách bảo mật, phải dừng ngay. Về kỹ năng còn lệch ngôn ngữ (chat #1 Nhật→Anh) và 1 lần xin review chưa đúng lúc. Ưu tiên: tuyệt đối không xin/nhận credentials hay mã bảo mật trong chat.

## ✅ Điểm tốt
- Proactive troubleshooting and ownership
   > Chat #6: "Let me check the settings on our end right away — I want to make sure this is fully resolved before we close."
- Technical accuracy on plan limits and WABA setup
   > Chat #15: Clear step-by-step WABA connection walkthrough with correct account type verification
- Consistent warm, professional tone across 30 chats
   > Chat #9: "I completely understand your frustration — let me take this off your plate right now."

## 🔧 Cần cải thiện
- Never request or accept credentials in chat (CRITICAL)
   > Chat #11: "We need your email and password to log in and activate the Chatty web app. Don't worry, we won't access or modify anything unauthorized on your account." — This is a severe security violation.
- Do not receive/forward 2FA or security codes shared by merchant
   > Chat #5: Customer shared 2FA PIN '935141' and Hazel responded 'Thank you so much. Let me forward it to our dev team' — must immediately warn merchant and not pass along security codes.
- Language consistency (KN3): maintain customer's chosen language
   > Chat #1: Switched from Japanese to English mid-conversation without customer prompting the switch.
- Review-ask timing: only ask after confirmed resolution, not when customer has gone quiet
   > Chat #10: Added 'Is it possible?' review ask after customer stopped responding — creates pressure rather than genuine invitation.

## 🌟 Xin review (chỉ ghi nhận, KHÔNG tính điểm)
- Đã xin 10/12 chat phù hợp (đúng lúc 9, chưa đúng lúc 1).

## 📈 So với tuần trước (W23)
- Điểm 83 → 84 (▲ +1)
