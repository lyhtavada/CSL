# Chatty AI Agent/Playground — CSL Test Notes

**Feature:** AI Agent Playground
**How to access:** CRM → staging 1 → store `ag-loanpt-chatty-checkout-stg1` → dev_zone → Enable Agent Playground
**Tester:** Liz (CSL)
**Purpose:** Evaluate CS impact, merchant readiness, UX gaps before go live

## UI Layout (thực tế)

3-column layout:
- **Trái:** Chat history list (danh sách các session)
- **Giữa:** Chat window với AI agent + suggested prompts
- **Phải:** Proposals panel (Pending / Approved / Rejected / All)

Suggested prompts mặc định:
- "Audit my shop" — quick overview & top issues
- "Find missing FAQs" — gaps customers ask about
- "Review AI instructions" — tone, scope, fallbacks

Flow cốt lõi: **merchant chat → AI đề xuất (Proposals) → merchant Approve/Reject → AI cập nhật**

---

## Findings từ session test

### Proposals Panel

**Card interaction**
- Nút **"–" (dấu trừ)** trên card → thực ra là **collapse** chứ không phải remove/reject — UX misleading, merchant dễ nhầm → báo PM đổi icon hoặc thêm tooltip
- Hover/click vào proposal card → cần confirm có mở detail/edit view không, hay chỉ có Approve/Reject

**Content & readability**
- **Proposal title** hiện dạng `create faq_question` (technical action name) — merchant không hiểu → nên đổi thành "New FAQ" / "Update setting" → báo PM
- **categoryId** hiện raw ID (`DY0dN5nm5EyxNWFQL2U3`) thay vì category name — merchant không biết FAQ sẽ nằm ở category nào → báo PM
- FAQ proposal không hiển thị category sẽ được assign vào → merchant không biết FAQ đó sẽ nằm ở đâu

**Sort order**
- Proposals sort theo creation order (cũ lên đầu) — merchant vừa chat xong phải scroll xuống tìm proposal mới nhất → **nên sort newest first** → báo PM
- Proposal card chưa hiện **ngày/giờ tạo** — khó biết proposal nào mới, nhất là khi list dài → báo PM

**Scope — per-session vs global**
- Proposals panel chỉ show proposals của chat session đang mở — nếu merchant tạo chat mới → không thấy proposals từ session cũ
- Merchant chỉ có 1 chat window, proposals tích lũy dài theo thời gian → **Proposals nên là global (across all sessions)**, không phải per-session → báo PM

**Search**
- Không có search/filter trong Proposals panel — tab Approved sẽ ngày càng dài → **nên có search theo keyword** → báo PM

**Queue flow**
- Khi merchant ra lệnh (vd: "turn on AI assistant") → AI không làm ngay mà queue vào Proposals → merchant cần ra cột phải bấm Accept để apply
- AI có thông báo trong chat nhưng merchant đang nhìn vào chat, dễ bỏ sót bước Accept
- "Accept all" button — không có confirmation step → 1 click apply hết tất cả Pending → risky nếu có proposal sai lẫn vào

**Open questions cần clarify với PM**
- Reject nhầm → có undo không?
- Proposal có expire không? Bỏ đó không approve/reject thì tồn tại mãi hay mất?
- Sau khi approve → merchant có nhận confirmation "FAQ is now live" không hay phải tự vào FAQ page check?
- AI-generated answer có dựa trên shop data thật không? (risk: merchant Accept all mà không đọc kỹ → live với data sai/placeholder)

---

## Chat History (cột trái)

- Chưa có option **xóa chat history** — merchant không thể dọn danh sách session
- **Session title** = câu đầu tiên merchant gõ (không phải AI đặt) — hiện kèm msg count + timestamp (vd: "10 msgs · 4h")
- Chưa có option **đổi tên session title** — merchant không thể rename nếu câu đầu không mô tả tốt
- Chưa có **search box** để tìm lại session cũ — danh sách dài sẽ khó navigate → báo PM

---

## Bugs

| # | Bước | Vấn đề gặp | Severity |
|---|------|------------|----------|
| 1 | Gửi message bằng Enter | Sau khi gửi, từ cuối của prompt còn sót lại trong chatbox (không clear hết) | Major |

**Severity:** Blocker / Major / Minor

---

## Summary

| Area | Status | Notes |
|------|--------|-------|
| Proposals Panel | | |
| Bugs | | |

**Overall assessment:**
- Ready to go live? Yes / No / Conditional
- Blockers:
- PM action items:
