---
name: chatty-test-grader
description: Grade Chatty AI Assistant knowledge test results from Google Form CSV exports. Use when Liz or the CS team needs to review and score test submissions for Chatty app knowledge assessment — includes MCQ review, open-ended grading with detailed feedback per question, and a summary report per candidate.
---

# Chatty Test Grader

Grade Chatty AI Assistant test submissions from Google Form CSV exports.

## Input

A CSV file exported from Google Forms with columns:
- `Timestamp`, `Username`, `Total score`
- Per question: `[Question]`, `[Question] [Score]`, `[Question] [Feedback]`
- MCQ questions: scores are auto-filled (1.00/1 or 0.00/1)
- Open-ended questions: scores show `-- / 1` (need manual grading)

## Workflow

1. **Parse** the CSV — identify each submission (by Username + Timestamp)
2. **Review MCQs** — note which auto-graded questions were wrong and why
3. **Grade open-ended** — score each `-- / 1` question using the answer key
4. **Write feedback** — one sentence per question: what was wrong/missing
5. **Summarize** — produce a report per candidate

## Answer Key

Read `references/answer-key.md` for correct answers and grading rubric for all 40 questions (Q1–Q19 MCQ, Q20–Q40 open-ended).

## Output Format

For each candidate, produce:

```
## [Name] ([email]) — [Date]

**MCQ: X/19** | **Open-ended: X/21** | **Total: X/40**

### MCQ Errors
| Q# | Question (short) | Their answer | Correct answer |
|---|---|---|---|
| Q4 | Why review Unresolved Q? | "To manually respond" | To identify content gaps |

### Open-ended Grading
| Q# | Score | Feedback |
|---|---|---|
| Q20 | 1/1 | Correct |
| Q28 | 0/1 | Sai — Chatty có sync ACTIVE discounts tự động... |

### Điểm yếu cần ôn lại
- [topic 1]
- [topic 2]
```

## Notes

- If a candidate has multiple submissions, grade the latest one (or best score if Liz specifies)
- Open-ended questions requiring video demo (Q33, Q34): if no video link provided, deduct 0.5pt
- Use Vietnamese for feedback when writing for internal team (CS team is Vietnamese)
- Write feedback concisely — 1 sentence per question is enough
- Common weak spots across team: Q16 (scenario trigger keywords), Q37 (metafields), Q28 (discount sync), Q35 (human handover steps)
