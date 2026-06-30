# CS Training Plan — AI Monitor & AM Role

**Status:** Draft
**Last updated:** 2026-03-27

> Tài liệu này liệt kê những gì cần chuẩn bị để train CS team trước và sau khi AI go live.
> CS chỉ bắt đầu training khi Liz + Sam đã assess AI sẵn sàng go live.

---

## AI Monitor Track
**Áp dụng cho:** Hazel, Phoebe (Chatty) / Hana, Audrey (Joy)

### Tài liệu cần chuẩn bị

| Tài liệu | Nội dung | Người làm |
|----------|----------|-----------|
| AI Overview doc | AI hoạt động thế nào, data sources là gì, tại sao AI trả lời đúng/sai | Liz |
| Training data guide | Format Q&A, cách viết variants, khi nào thêm escalation note | Liz |
| Escalation criteria doc | Danh sách cụ thể: case nào AI nên transfer, case nào tự xử | Liz + CS |
| Error log template | Cách ghi nhận AI sai: topic, câu hỏi gốc, AI reply, correct answer, root cause | Liz |
| Sample conversations | 20–30 real conversations đã được Liz label "good / needs fix / escalate" | Liz |

### Lịch training

| Session | Nội dung |
|---------|----------|
| Session 1 | Liz walk through AI overview + demo live |
| Session 2 | CS tự review 10 conversations, rate → Liz review lại và debrief |
| Session 3 | CS tự viết Q&A entries → Liz feedback |
| Shadow | CS shadow Liz monitor 1–2 ca trước khi tự đứng ca |

---

## AM Track
**Áp dụng cho:** Andy, Jade (Chatty) / Sonny, Alyssa (Joy)

### Tài liệu cần chuẩn bị

| Tài liệu | Nội dung | Người làm |
|----------|----------|-----------|
| ICP doc | Ai là merchant đủ điều kiện nhận AM support | Liz |
| Onboarding journey map | Từng bước merchant cần đi qua để "activated" | Liz + CS |
| Call talk track | Flow + key questions + common objections (không phải script cứng) | Liz + CS |
| Call trigger list | Khi nào reach out, dựa vào signal gì (plan, setup status, ngày cài) | Liz |
| Follow-up template | Email/chat sau call, 30/60/90 day check-in | Liz + CS |

### Lịch training

| Session | Nội dung |
|---------|----------|
| Shadow 1–2 | Nghe Avada AM team chạy call thật |
| Debrief | Liz debrief sau mỗi shadow: họ làm gì khác, rút ra gì |
| Practice call | CS chạy thử 1 call có Liz nghe → feedback sau |

---

## Tài liệu dùng chung (đã có)

- KB LIVE trên `cs2.avada.net` — Chatty/Joy features, plans, common issues (nguồn Ivy/Joyce; fetch qua `skills/qa-weekly/scripts/fetch_kb.py <chatty|joy> <path>`)
- Escalation matrix — case nào CS tự xử, case nào leo lên Liz (`kb/cs-process/shared-cs-process/escalation-matrix.md`)

---

## Thứ tự ưu tiên

1. **AI Monitor track trước** — block trực tiếp việc go live
2. **AM track song song** — không block go live, nhưng nên bắt đầu sớm để kịp shadow Avada AM team
