 #PRD — v2.5 QA Agent (Shift-end Scoring)

**Status:** Draft  
**Author:** CEO Brain × Sam Ng  
**Created:** 2026-03-01  
**Version:** 0.1  

---

## 1. Overview

### Problem

Avada CS hiện có **67 CS agents** across 4 groups. QA review đang được thực hiện **thủ công** bởi group leaders (Esther, Liz, Lydia, Daisy) — đọc từng conversation, chấm điểm, ghi chú. Quy trình này:

- Tốn **3–5 giờ/tuần/leader** chỉ để sample và chấm
- **Inconsistent** — mỗi leader có cách chấm khác nhau, không có rubric chuẩn
- **Reactive** — phát hiện vấn đề chậm (tuần sau mới biết tuần trước có vấn đề)
- **Low coverage** — chỉ sample được 5–10% conversations thực tế

### Solution

Xây **QA Agent** — một AI agent tự động:
1. Pull conversations từ Crisp sau mỗi shift
2. Sample và score từng conversation theo rubric chuẩn
3. Aggregate thành report per agent, per group
4. Deliver report đến group leaders qua Slack + lưu vào Notion

### Goals

| Goal | Metric |
|---|---|
| Giảm thời gian QA thủ công | 3–5h/week/leader → <30 min review |
| Tăng coverage | 5–10% → 100% conversations sampled |
| Consistency | Rubric chuẩn, không phụ thuộc vào subjective của leader |
| Speed to insight | Biết vấn đề trong ngày, không phải tuần sau |

---

## 2. Scope

### In Scope (v2.5)

- Score conversations từ **human CS agents** (không score AI bot conversations)
- 4 groups: G1 SEO (Esther), G2 Retention (Liz), G3 AOV (Lydia), G4 Solar (Lydia)
- Delivery: Slack (mỗi group nhận riêng) + Notion (lưu history)
- Trigger: cron job cuối shift (17:30 VN) mỗi ngày làm việc

### Out of Scope (v2.5)

- Real-time scoring per conversation (v2.6+)
- Score AI bot conversations (khác biệt quá với human scoring)
- Two-way feedback (CS agent phản hồi lại QA score)
- Integration với HR/performance review system

---

## 3. User Stories

| # | As a... | I want to... | So that... |
|---|---|---|---|
| 1 | Group leader | Nhận QA report cuối ngày qua Slack | Tôi biết agent nào cần coaching hôm nay |
| 2 | Group leader | Xem flagged conversations với lý do cụ thể | Tôi có thể review và feedback trực tiếp |
| 3 | CS Manager (Daisy) | Xem overview tất cả 4 groups | Tôi biết tình trạng chất lượng toàn team |
| 4 | CS Agent | Nhận score của mình (optional) | Tôi tự cải thiện mà không cần chờ feedback |
| 5 | Sam (CEO) | Xem weekly aggregate trend | Chất lượng CS có đang cải thiện hay không |

---

## 4. Scoring Rubric (6 tiêu chí)

Mỗi tiêu chí chấm **1–5 điểm**. QA Agent (Claude Sonnet) đọc full conversation và chấm theo rubric sau:

### 4.1 Tone & Empathy (Thái độ)
| Score | Description |
|---|---|
| 5 | Thân thiện, empathetic, customer cảm thấy được lắng nghe |
| 4 | Lịch sự, professional, đôi khi hơi formal |
| 3 | Trung tính, không sai nhưng thiếu warmth |
| 2 | Hơi curt, thiếu patience với customer |
| 1 | Bất lịch sự, defensive, hoặc dismissive |

### 4.2 Accuracy (Độ chính xác)
| Score | Description |
|---|---|
| 5 | Thông tin hoàn toàn đúng, có dẫn chứng/link nếu cần |
| 4 | Đúng nhưng thiếu 1 số detail nhỏ |
| 3 | Đúng một phần, có chỗ cần clarify thêm |
| 2 | Sai một phần, có thể gây hiểu nhầm |
| 1 | Sai hoàn toàn hoặc misleading |

### 4.3 First Reply Quality (Chất lượng reply đầu tiên)
| Score | Description |
|---|---|
| 5 | Reply đầu giải quyết được vấn đề hoặc hỏi đúng câu cần thiết |
| 4 | Reply đầu tiếp cận đúng hướng, cần 1–2 bước nữa |
| 3 | Reply đầu generic, chưa hiểu rõ vấn đề |
| 2 | Reply đầu lạc đề hoặc hỏi câu không liên quan |
| 1 | Reply đầu hoàn toàn sai hướng |

### 4.4 Resolution Speed (Tốc độ giải quyết)
| Score | Description |
|---|---|
| 5 | Giải quyết trong ≤3 exchanges hoặc <5 phút |
| 4 | 4–5 exchanges hoặc 5–10 phút |
| 3 | 6–8 exchanges hoặc 10–20 phút |
| 2 | >8 exchanges hoặc 20–40 phút |
| 1 | Không giải quyết được hoặc >40 phút |

### 4.5 SOP Compliance (Đúng quy trình)
| Score | Description |
|---|---|
| 5 | Follow đúng SOP, template, escalation rules |
| 4 | Về cơ bản đúng, có 1 minor deviation |
| 3 | Bỏ qua 1–2 bước trong SOP |
| 2 | Bỏ qua nhiều bước hoặc xử lý sai flow |
| 1 | Không follow SOP, tự ý xử lý |

### 4.6 Escalation Handling (Xử lý leo thang)
| Score | Description |
|---|---|
| 5 | Escalate đúng lúc, đúng người, đầy đủ context |
| 4 | Escalate đúng nhưng thiếu 1 số context |
| 3 | Chậm escalate (đáng ra nên escalate sớm hơn) |
| 2 | Không escalate khi cần thiết |
| 1 | Escalate sai người hoặc không escalate nghiêm trọng |
| N/A | Conversation không cần escalation → bỏ qua tiêu chí này |

**Overall Score** = trung bình cộng 5–6 tiêu chí áp dụng (làm tròn 1 chữ số thập phân)

**Thresholds:**
- ≥ 4.5 → �� Excellent
- 4.0–4.4 → ✅ Good
- 3.5–3.9 → �� Average
- 3.0–3.4 → ⚠️ Below average
- < 3.0 → �� Critical — flag for immediate coaching

---

## 5. Technical Architecture

### 5.1 Data Flow

```
[Cron: 17:30 VN daily]
        ↓
[Fetch operators list — Crisp API]
  Map email → operator_id per group
        ↓
[Fetch conversations — Crisp API]
  Filter: closed conversations, last 8h, human replied ≥1 msg
  Exclude: assigned to "Avada AI" seat (bot-only conversations)
        ↓
[Sample N conversations per agent]
  N = min(5, total conversations)
        ↓
[QA Agent (Claude Sonnet) scores each conversation]
  Input: full message transcript
  Output: 6 scores + comments per criterion + flagged? + summary
        ↓
[Aggregate scores per agent, per group]
        ↓
[Deliver report]
  → Slack (per group leader)
  → Notion (append to QA log page)
        ↓
[Store raw scores → Firestore `qaScores` collection]
  For weekly trends + future dashboard
```

### 5.2 Crisp API Endpoints

| Action | Endpoint |
|---|---|
| List operators | `GET /website/{id}/operators/list` |
| List conversations | `GET /website/{id}/conversations/{page}` |
| Get full conversation | `GET /website/{id}/conversation/{session_id}` |
| Get messages | `GET /website/{id}/conversation/{session_id}/messages` |

**Filters khi fetch conversations:**
- `status=resolved` hoặc `status=unresolved` (lấy cả, filter sau)
- Date range: last 8h from trigger time
- `assigned_to` = operator_id của human agents (exclude Avada AI seat)

### 5.3 QA Agent Prompt (System)

```
You are a Customer Support QA reviewer for Avada — a Shopify app company.

Your task: Score a CS conversation on 6 criteria (1–5 scale each).

Context:
- CS agents support merchants using Shopify apps (SEO, Chatty, Joy Loyalty, etc.)
- Language: English (some Vietnamese is acceptable in internal notes)
- Standard: Professional, helpful, accurate, empathetic

Output format (JSON):
{
  "tone_empathy": { "score": X, "comment": "..." },
  "accuracy": { "score": X, "comment": "..." },
  "first_reply_quality": { "score": X, "comment": "..." },
  "resolution_speed": { "score": X, "comment": "..." },
  "sop_compliance": { "score": X, "comment": "..." },
  "escalation_handling": { "score": X, "comment": "..." | "na": true },
  "overall": X.X,
  "flagged": true/false,
  "flag_reason": "..." (if flagged),
  "summary": "1-2 sentence summary of this conversation quality"
}

Rules:
- Be objective and consistent
- Flag if overall < 3.0 OR any single criterion < 2
- Do NOT flag purely based on conversation length
- If escalation was not needed, set escalation_handling.na = true (exclude from average)
```

### 5.4 Sampling Strategy

```
Per agent per shift:
  - If total conversations ≤ 5 → score all
  - If total conversations > 5 → random sample 5
  - Priority: sample flagged conversations first (if any were auto-escalated)

Agent with 0 conversations:
  - Include in report with note "No conversations in this shift"
```

### 5.5 Storage Schema (Firestore)

```
Collection: qaScores
Document ID: {agentId}_{date}_{shiftId}

{
  agentId: "hienpt",           // Crisp operator user_id
  agentEmail: "hienpt@avadagroup.com",
  agentName: "Hazel",
  group: "G1_SEO",
  date: "2026-03-01",
  shiftId: "morning",          // morning / evening
  conversationsSampled: 5,
  conversationsTotal: 23,
  scores: {
    tone_empathy: 4.2,
    accuracy: 3.8,
    first_reply_quality: 4.0,
    resolution_speed: 3.6,
    sop_compliance: 4.4,
    escalation_handling: 4.0,
    overall: 4.0
  },
  flaggedConversations: [
    {
      sessionId: "abc123",
      overallScore: 2.8,
      flagReason: "Accuracy 2/5 — wrong pricing info given",
      crispLink: "https://app.crisp.chat/..."
    }
  ],
  createdAt: Timestamp
}
```

---

## 6. Report Format

### 6.1 Slack Report (per group)

```
📊 QA Report — G1 SEO | 01/03/2026 | Shift sáng
Trigger: 17:30 VN | Sampled: 40 conversations (8 agents × 5)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🏆 Top performers
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🌟 Nim (Nguyễn)    4.8/5   Tone:5 Acc:5 FRQ:5 Speed:4 SOP:5
✅ Riley Le         4.5/5   Tone:5 Acc:4 FRQ:4 Speed:5 SOP:4
✅ Hazel Pham       4.2/5   Tone:4 Acc:4 FRQ:4 Speed:4 SOP:5

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
⚠️  Needs attention
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🟡 Iris Nguyen      3.7/5   Tone:4 Acc:3 FRQ:3 Speed:4 SOP:4
⚠️  Arthur Avada    3.2/5   Tone:3 Acc:2 FRQ:4 Speed:3 SOP:4
🔴 Alicia Le        2.8/5   [FLAGGED] Tone:2 Acc:2 FRQ:3 Speed:3 SOP:4

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📌 Flagged conversations (need review)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🚨 Alicia Le | Score 2.8 | Wrong refund info + curt tone
   → https://app.crisp.chat/...

🚨 Arthur Avada | Score 2.9 | Accuracy 2/5 — incorrect SEO plan pricing
   → https://app.crisp.chat/...

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Group avg: 3.9/5 | Yesterday: 4.1 | Trend: 📉 -0.2
Full report: [Notion link]
```

### 6.2 Notion Page

Structure: `CS QA Log > {Year} > {Month} > {Date} — {Group}`

Content:
- Summary table (same as Slack)
- Per-agent detail section with conversation transcripts + inline comments
- Trend chart (manual in Notion, or embedded chart from Firestore data)

---

## 7. Implementation Plan

### Phase 1 — Core scoring (Week 1)
- [ ] Build `qa-agent.ts` — fetch conversations + score via Claude
- [ ] Implement sampling logic
- [ ] Test scoring quality with 10 real conversations
- [ ] Calibrate rubric (compare AI scores vs leader scores)

### Phase 2 — Report delivery (Week 2)
- [ ] Slack report formatter (per group)
- [ ] Notion page creator
- [ ] Cron job setup (17:30 VN, Mon–Sat)
- [ ] Manager overview (Daisy) — all 4 groups

### Phase 3 — Storage & trends (Week 3)
- [ ] Firestore `qaScores` write
- [ ] Weekly trend calculation
- [ ] Add trend arrow to Slack report (↑↓)
- [ ] Sam weekly summary (Mondays)

### Phase 4 — Calibration & feedback (Week 4+)
- [ ] Leader can "dispute" a score via Slack button
- [ ] Disputed scores → human review → update rubric
- [ ] Monthly rubric review with leaders

---

## 8. Cost Estimate

| Item | Estimate |
|---|---|
| Conversations/day | ~300 (all agents combined) |
| Sampled/day | ~100 (5/agent × 20 active agents) |
| Tokens/conversation | ~2K tokens (transcript + scoring) |
| Model | Claude Haiku 3.5 |
| Cost/conversation | ~$0.002 |
| **Daily cost** | **~$0.20/day** |
| **Monthly cost** | **~$4–5/month** |

> ✅ Extremely cost-effective — replaces 60–100 hours of manual QA/month

---

## 9. Risks & Mitigations

| Risk | Likelihood | Mitigation |
|---|---|---|
| AI scores inconsistent with human judgment | Medium | Calibration phase — compare 50 conversations with leader scores, tune prompt |
| Crisp API rate limits when fetching 100+ conversations | Low | Batch requests, add retry + backoff |
| CS agents feel surveilled/demotivated | Low | Frame as coaching tool, not punishment. Leaders communicate proactively |
| Conversations in Vietnamese affect scoring quality | Medium | Test with VN conversations, add Vietnamese context to QA Agent prompt |
| Leader doesn't read the report | Low | Keep Slack format short, flag only critical items |

---

## 10. Open Questions

| # | Question | Decision needed by |
|---|---|---|
| 1 | Có gửi score cho từng CS agent không, hay chỉ group leader? | Sam |
| 2 | Shift VN là 8AM–17PM. Có shift 2 không cần score? | Sam |
| 3 | SOP document ở đâu? QA Agent cần đọc để score SOP compliance | Daisy/Leaders |
| 4 | Notion page: tạo mới mỗi ngày hay append vào 1 page? | Sam |
| 5 | Có exempt conversation nào (e.g. billing, sensitive) khỏi QA? | Daisy |

---

## 11. Success Metrics

| Metric | Target |
|---|---|
| QA report delivery rate | 100% days có conversation |
| Manual QA time reduction | ≥70% (từ 3–5h xuống <1h) |
| Leader satisfaction score | ≥4/5 (survey sau 1 tháng) |
| AI vs human score alignment | ≥85% conversations có delta <0.5 |
| Coverage | 100% human agents sampled mỗi ngày |

---

*PRD v0.1 — Pending Sam review & open questions resolution*  
*Next step: Sam answer 5 open questions → start Phase 1 implementation*
Collapse




