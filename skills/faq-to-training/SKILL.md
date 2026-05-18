---
name: faq-to-training
description: Convert a CS FAQ (written in the Notion FAQ template format) into AI training data. Use when the user shares a FAQ doc and asks to "convert", "chuyển thành training data", "thêm vào training", "viết training data cho cái này", or pastes a FAQ and asks to add it to common-issues. Handles all 4 FAQ types: troubleshooting, how-to, process, knowledge. Output goes to chatty-copilot-training/training-data/common-issues/ or joy-copilot-training/training-data/common-issues/.
version: 1.0.0
---

# FAQ → Training Data Converter

Convert a FAQ written in the Notion CS template into Q&A training data format for the Chatty or Joy AI Copilot.

## Step 1: Identify app and FAQ type

**App** — determine from context:
- Mentions "Chatty", "live chat", "chatbox", "FAQ block", "inbox", "AI assistant" → **Chatty**
- Mentions "Joy", "loyalty", "points", "rewards", "VIP tier", "referral", "redemption" → **Joy**
- If unclear → ask Liz: "File này cho Chatty hay Joy?"

**FAQ type** — detect from the template structure used:
- Has "Triệu chứng / Symptom" + "Root Cause" + "Solution" → `troubleshooting`
- Has "Câu hỏi khách thường đặt" + "Hướng dẫn chi tiết" → `how-to`
- Has "Khi nào áp dụng" + multi-party steps (CS / TS / Dev) → `process`
- Has "Giải thích / Explanation" + concept breakdown → `knowledge`

## Step 2: Extract customer-facing content only

**Include:**
- Symptom / problem description (customer-visible)
- Root cause explanation (if explainable to customer)
- Solution steps
- Customer question variants
- Short answer / detailed steps
- Important notes / edge cases
- Sample responses to customers
- Escalation conditions (when and to whom — phrased from CS perspective)

**Exclude completely:**
- Anything under "Note nội bộ (Internal Only)"
- Dev zone steps, internal URLs, internal tool names
- Growth hack names
- Passwords, API keys, internal credentials
- Info that reveals internal tooling to customers

## Step 3: Generate Q variants

For each issue or how-to, write 2–4 Q: lines covering:
- How a merchant would describe the problem ("X doesn't work", "I can't do Y")
- How a CS agent would phrase it for lookup ("merchant reports...", "error when...")
- Common paraphrases or alternate phrasings

For troubleshooting: include symptom-based questions ("Why is X not working?", "Getting error message Y")
For how-to: include task-based questions ("How do I...", "Where can I find...", "Can I...")
For knowledge: include concept questions ("What is...", "How does X work", "Difference between...")

## Step 4: Write the answer

- Merge "Root Cause" + "Solution" into one clear answer
- Keep step-by-step structure where helpful (numbered lists)
- Include escalation guidance at the end if present: "If X persists → escalate to [Dev/TS] via [channel]"
- If "Mẫu trả lời khách (Sample Response)" is present → include it at the end of the answer under a `**Sample response:**` label. This helps the AI learn the right tone and phrasing when replying to merchants.
- Language: English only

## Step 5: Output format

```
---
category: Common Issues
topic: [Topic name — concise, title case]
source: notion/[app] FAQs
---

Q: [variant 1]
Q: [variant 2]
Q: [variant 3 if useful]
A: [Full answer]

[Escalation note if applicable]

---

Q: [Next issue variant 1]
Q: [Next issue variant 2]
A: [Answer]

---
```

Rules:
- One `---` separator between Q&A blocks (not between Q lines and A)
- 2+ Q variants per block
- No bold headers inside A unless the answer is long and multi-part
- No "Note nội bộ" content anywhere in the output

## Step 6: Determine output file path

File naming: `kebab-case-topic-name.md`
- Use the topic name, lowercase, hyphens only
- Match naming style of existing files (e.g. `ai-wrong-responses.md`, `points-not-earned-after-order.md`)

Output path:
- Chatty → `/Users/avada/CSL/chatty-copilot-training/training-data/common-issues/[filename].md`
- Joy → `/Users/avada/CSL/joy-copilot-training/training-data/common-issues/[filename].md`

Check if file already exists. If yes → ask Liz: "File `[filename].md` đã tồn tại — append vào hay overwrite?"

## Step 7: Write the file

Use the Write tool to create the file (or Edit to append if confirmed).

Then confirm to Liz:
```
Done. Wrote [N] Q&A blocks to:
[app]-copilot-training/training-data/common-issues/[filename].md

Topic: [topic]
Type: [troubleshooting/how-to/process/knowledge]
Blocks: [N]
Excluded: Note nội bộ section ✓
```

## Edge cases

- **Multiple issues in one FAQ** → each issue becomes its own Q&A block in the same file, separated by `---`
- **Process type with multiple parties** → simplify to CS-facing steps only; don't expose TS/Dev internal steps
- **FAQ is incomplete / missing sections** → write what's available, note to Liz what was missing
- **App can't be determined** → ask before writing
- **FAQ has no sample response** → that's fine, skip it; the answer itself is enough
