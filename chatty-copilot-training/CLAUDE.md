# Chatty Copilot Training Data

This repo contains training content for the Chatty AI Copilot — a CS support bot for Chatty (Shopify live chat & AI assistant app).

## Project Structure

```
raw-data/           → Source documents (Notion exports, helpcenter crawls)
  helpcenter/       → Crawled from help.chatty.net
  notion/           → Exported from Notion
  chatty-cs-process/ → Chatty-specific CS process source docs

training-data/      → Processed Q&A training files (this is what the bot uses)
  helpcenter/       → Feature docs converted to Q&A
  common-issues/    → Troubleshooting scenarios
  chatty-cs-process/ → Chatty-specific CS workflows and processes

instructions/       → Bot configuration (system prompt, knowledge base)

scripts/            → Python scripts for crawling/generating training data
  crawl_helpcenter.py              → Crawl help.chatty.net sitemap → raw markdown
  generate_helpcenter_training.py  → Convert raw markdown → Q&A training format

../shared-cs-process/ → Shared content used by both Chatty and Joy copilots
  raw-data/
    cs-process/     → CS process source docs (Notion exports)
  training-data/
    cs-process/     → CS workflows, escalation, billing, sensitive situations
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
3. For helpcenter data: run `python3 scripts/crawl_helpcenter.py` then `python3 scripts/generate_helpcenter_training.py`.
4. Commit and push to main.

## Workflow: Re-crawling Helpcenter

When help.chatty.net is updated, re-crawl and regenerate:

```bash
python3 scripts/crawl_helpcenter.py
python3 scripts/generate_helpcenter_training.py
```

This will overwrite existing files. Review changes before committing.

## Key Context

- **Product**: Chatty — Shopify live chat, AI assistant & FAQ builder app
- **Users**: Shopify merchants (store owners, support teams)
- **Core features**: Live chat, AI assistant, chatbox, FAQ builder, order tracking, integrations
- **Helpcenter**: https://help.chatty.net/ (GitBook-based)
- **CS tools**: Live chat, Trello cards for escalation, Slack channels
- **Escalation hierarchy**: CS Agent → CS Leader → PM/Tech Lead
- **Priority levels**: P0 (Critical) → P1 (High) → P2 (Medium) → P3 (Low)

## Helpcenter Categories

| Category | Description |
|----------|-------------|
| Getting Started | Intro, quick start guide |
| Live Chat | Inbox, channels (email, Messenger, WhatsApp), contacts, team, quick replies |
| AI | AI assistant overview, data sources, training, skills, settings |
| Chatbox | Chatbox settings, contact button, deep links, embedded chatbox |
| Build FAQs | Categories, questions, FAQ page, FAQ block, analytics |
| Mobile and Web App | Mobile app, web app |
| Others | General settings, order tracking, translation, notifications, analytics, online hours |
| Integrations | Klaviyo, Zendesk, Joy, Air Reviews, Powerful Contact Form, Website |
| Product Roadmap | Changelog, pricing |
| FAQs | Common questions, uninstall guide |
| Privacy Policy | AI compliance, cookie policy |
