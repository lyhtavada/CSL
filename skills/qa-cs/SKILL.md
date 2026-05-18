---
name: qa-cs
description: Monthly QA review of CS agent conversations from Crisp. Use when Liz asks to QA a specific agent (e.g. "QA chat của Jade tháng 3", "chấm điểm Andy"), generate a QA report, evaluate CS quality, or score agent performance against Avada QA policy.
---

# QA CS Skill

Perform monthly QA review of CS agent conversations and produce a scored report.

## QA Rules

Load `references/qa-rules.md` for the full error codes, severity levels, and penalty points.

## Process

### Step 1 — Fetch conversations

Run the fetch script to pull a random sample from Crisp:

```bash
python3 /Users/avada/CSL/skills/qa-cs/scripts/fetch_crisp_convs.py \
  --operator <name> \
  --month <YYYY-MM> \
  --count 20 \
  --output /tmp/qa_<name>_<YYYY-MM>.json
```

Operator names: `jade`, `andy`, `hazel`, `cody`, `mirra`, `phoebe`, `megan`

### Step 2 — Review each conversation

Read the JSON output. For each of the 20 conversations:

1. Read all messages carefully
2. Identify violations against the QA rules (QT / KT / KN / BM)
3. For each violation: note the error code, severity, and quote the specific message as evidence
4. If no violations: mark as "Pass"

Focus on what's observable from the chat log:
- **QT5–QT12, QT33**: visible in message content and flow
- **QT18, QT22, QT25**: look for unanswered questions, no handoff message
- **KT1, KT2**: check if advice is accurate against KB
- **KN1–KN7**: evaluate tone, grammar, completeness of answers
- **QT30, QT31, QT32**: check if/when review was requested

Cannot assess from chat alone (skip): QT1–QT4 (workshift), QT28 (absence), BM1 (data storage)

### Step 3 — Calculate score

Start from **100 points**.

For each violation:
- Deduct penalty points per the rules
- Urgent violations: flag separately (case by case)

**Tần suất miễn phạt:** Low (3/month), Moderate (2/month), High (1/month), Critical (0/month)
→ Only deduct when violations **exceed** the allowed frequency

Final score = 100 − total deductions

### Step 4 — Generate report

Create an Excel file at `/Users/avada/CSL/reports/qa_<operator>_<YYYY-MM>.xlsx` with:

**Sheet 1 — Summary**
| Field | Value |
|---|---|
| Agent | name |
| Month | YYYY-MM |
| Conversations reviewed | 20 |
| Final score | X/100 |
| Total violations | n |
| Urgent flags | n |

**Sheet 2 — Violations**
| # | Conv URL | Visitor | Error Code | Category | Severity | Penalty | Evidence (quote) |

**Sheet 3 — Conversations**
| # | URL | Visitor | Result | Notes |

## Output to Liz

After generating the file, send Liz:
1. File Excel
2. Brief summary: score, top 2-3 issues, recommendation

Example summary:
> **QA Jade — Tháng 3/2026**
> Score: 72/100
> 3 Critical, 2 High, 4 Moderate
> Vấn đề chính: QT11 (không phản hồi KH) + KN5 (tư vấn sai hướng)
> Đề xuất: coaching 1-1 về product knowledge + follow-up process
