# AI Agent Performance Report

Track AI agent quality khi live trên Crisp — Chatty & Joy.

## Cấu trúc folder

```
ai-agent-performance/
├── README.md              ← file này
├── TEMPLATE.md            ← template cho mỗi ngày
├── rubric.md              ← scoring rubric Betty dùng khi chấm
└── YYYY-MM-DD.md          ← 1 file per ngày review
```

## Report Format

```
# AI Agent Performance — YYYY-MM-DD
AI active: HH:MM – HH:MM

## Summary
- Handled
- Resolved (no human): N (%)
- Escalated: N (%)
- Human step-in: N (%)
- Avg QA score

Overall: [nhận xét text tổng quan]

## Agent Breakdown
| Agent | Handled | Resolved | Escalated | Human step-in | QA score |

## Session Log
| Session | Agent | Resolved | Escalated | Human step-in | Reason | QA score | Notes |

## Training Data Gaps
| # | Agent | Topic | Gap | Priority |
```

## Metrics

| Metric | Mô tả |
|--------|-------|
| **Handled** | Tổng conversations AI tham gia |
| **Resolved** | AI handle end-to-end, không cần human |
| **Escalated** | AI tự tag `<escalate_human>` |
| **Human step-in** | CS nhảy vào không có escalate tag |
| **Reason** | Lý do escalate hoặc human step-in |
| **QA score** | Betty chấm: Good / Needs Fix / Escalate Missed |

## Cách dùng

1. Paste Crisp session link vào chat với Betty
2. Betty fetch + chấm theo `rubric.md`
3. Betty fill vào Session Log, cộng count lên Summary
4. Liz thêm nhận xét vào **Overall**
