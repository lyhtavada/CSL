---
name: reply-reviews
description: Đọc review app mobile Chatty trên Apple App Store (iOS) + Google Play (Android), soạn reply cho review chưa được trả lời, Liz duyệt rồi mới post. Cron T3 + T6 17:00 gửi draft qua Telegram. Dùng khi Liz nói "/reply-reviews", "check review app store", "reply review CH Play", "post 1,2", "skip 3", "sửa reply 1".
---

# /reply-reviews — Reply review App Store + CH Play

Review của **app mobile Chatty** (không phải Shopify App Store listing — cái đó xem `/count-reviews`).
Luồng: **fetch review chưa reply → Betty soạn draft → Liz duyệt → post**. KHÔNG bao giờ post khi Liz chưa duyệt.

## Kết nối (setup 2026-09-14)

| Store | Auth | Client |
|---|---|---|
| iOS — App Store Connect | Individual API Key của Liz (role Customer Support), `.secrets/ApiKey_XP8I9FYCXB1L.p8` | `tools/appstore/asc.py` |
| Android — Google Play | Service account `betty-play-reviews@lizs-502610.iam.gserviceaccount.com` (GCP project "Liz's agent", PM Tùng mời vào Play Console với quyền View app info + Reply to reviews), `.secrets/play-service-account.json` | `tools/appstore/play.py` |

App ids + danh sách reviewer bỏ qua (review nội bộ) ở `config.json` — Liz sửa trực tiếp.
Thêm app mới: thêm 1 entry vào `apps` (cần key có quyền trên app đó).

**Giới hạn:**
- Google Play API chỉ trả review có nội dung **trong 7 ngày gần nhất** → cron T3+T6 để không sót. Review cũ hơn phải reply tay trên Play Console.
- Reply Google Play **tối đa 350 ký tự** (script tự chặn). Apple ~5970.
- Reply Apple vào trạng thái `PENDING_PUBLISH`, vài tiếng–1 ngày mới hiện public.

## Lệnh

Luôn chạy bằng `.venv-crisp/bin/python -W ignore skills/reply-reviews/scripts/reviews.py ...`

| Lệnh | Việc |
|---|---|
| `fetch [--out f.json]` | Review chưa reply, chưa có draft, không nằm trong ignore list. In `TOTAL_NEW=n` |
| `save drafts.json` | Lưu draft `[{review_id, store, app, reply, flag?}]` → gán id ngắn (1, 2, 3...) |
| `list` | Draft đang chờ duyệt |
| `edit <id> "<text>"` | Sửa nội dung draft |
| `post <id,id> --live` | Post (thiếu `--live` = dry-run) |
| `skip <id,id>` | Đánh dấu không reply |

State ở `state/drafts.json` (commit vào repo): mỗi draft có `status` pending/posted/skipped — review đã có trong đây sẽ không bị draft lại.

## Soạn reply

Theo `_identity/tone-and-voice.md` — friendly, ngắn, như 1 teammate. Thêm luật riêng cho review public:
- **Ngôn ngữ:** trả lời bằng ngôn ngữ review được viết (không theo territory/`language` của máy — review tiếng Anh từ VN vẫn trả tiếng Anh).
- **Mở đầu cá nhân hoá** 1 chi tiết cụ thể trong review, không dùng câu cảm ơn chung chung.
- **5⭐:** cảm ơn + nhắc 1 điểm họ khen + (nếu hợp) mời chat trong app nếu cần hỗ trợ. 2–3 câu.
- **1–3⭐ / báo bug:** 1 lời xin lỗi thật lòng → ghi nhận đúng vấn đề họ mô tả → mời liên hệ **live chat trong app** để team hỗ trợ. **Không** hứa đã fix / timeline nếu chưa được xác nhận — gắn `flag` để Liz check với team Tesla (anh Tùng/anh Đạt) trước khi post; nếu đã fix thì sửa thành "đã fix, cập nhật bản mới nhất và thử lại".
- Không nhắc tên nhân viên, không xin đổi rating, không copy-paste cùng 1 câu cho nhiều review.
- **Flag** (không tự skip — để Liz quyết) khi: review có vẻ không nói về app mình (vd nhầm app trùng tên), văn giống seeding/AI viết, reviewer có thể là người nội bộ, review có thông tin nhạy cảm, hoặc cần xác nhận trạng thái bug.

## Chạy tay

1. `fetch` → đọc từng review → soạn draft theo luật trên → ghi file tạm trong scratchpad → `save`.
2. Show Liz bảng: `#id · store · ⭐ · tên · tóm tắt review · draft · flag`.
3. Liz nói "post 1,2" → `post 1,2 --live`; "skip 3" → `skip 3`; "sửa 1: ..." → `edit 1 "..."` rồi show lại.
4. Commit `skills/reply-reviews/state/drafts.json` sau khi post/skip.

## Cron (T3 + T6 17:00)

`cron/run.sh` (launchd `com.avada.reply-reviews`, cài bằng `bash cron/install.sh`):
fetch → nếu `TOTAL_NEW=0` thì im lặng (chỉ nhắc nếu còn draft pending cũ) → Claude headless soạn draft theo `cron/prompt.txt` → `save` → Telegram digest cho Liz. **Cron không bao giờ post.**
Liz duyệt bằng cách nhắn thẳng bot Telegram (telegram-control chạy Claude có Bash): "post review 1,2", "skip 3", "sửa reply 1: ...". Log: `/tmp/reply-reviews.log`.
