# Joy Copilot Training Data

This repo contains training content for the Joy Loyalty AI Copilot — a CS support bot for Joy Loyalty (Shopify loyalty & rewards app).

## Project Structure

```
raw-data/           → Source documents (Notion exports, helpcenter crawls)
  helpcenter/       → Crawled from help.joy.so
  notion/           → Exported from Notion
  cs-process/       → CS team process docs (Notion exports, zips)

training-data/      → Processed Q&A training files (this is what the bot uses)
  helpcenter/       → Feature docs converted to Q&A
  common-issues/    → Troubleshooting scenarios
  cs-process/       → CS workflows, escalation, billing, sensitive situations

instructions/       → Bot configuration
  system-prompt.md  → Bot persona, tone, response structure
  knowledge-base.md → Product knowledge summary

scripts/            → Python scripts for crawling/generating training data
```

## Training Data Format

All files in `training-data/` follow this format:

```markdown
---
category: [Category Name]
topic: [Topic Name]
source: [source folder/file reference]
---

Q: [Question variant 1]
Q: [Question variant 2]
A: [Detailed answer with steps, examples, and escalation guidance]
```

Rules:
- Each Q&A block should have 2+ question variants for better matching.
- Answers should include step-by-step instructions with specific navigation paths.
- Include escalation guidance (when to escalate, to whom, via what channel).
- Keep language in English (even if source docs are in Vietnamese).
- Use markdown formatting (bold, lists, code blocks) for readability.

## Workflow: Adding New Training Data

1. Put raw source docs in `raw-data/` under the appropriate subfolder.
2. Create corresponding Q&A file(s) in `training-data/` following the format above.
3. Commit and push to main.

## Key Context

- **Product**: Joy Loyalty — Shopify loyalty & rewards app
- **Users**: Shopify merchants (store owners, marketing managers)
- **CS tools**: Live chat, Trello cards for escalation, Slack channels
- **Shortcuts**: CS agents use text shortcuts like `!cancel-reason`, `!billing-details`, `!refund-process`
- **Escalation hierarchy**: CS Agent → CS Leader → PM/Tech Lead
- **Priority levels**: P0 (Critical) → P1 (High) → P2 (Medium) → P3 (Low)
