# Obsidian KnowledgeBase Skill

A Claude Code skill that saves, searches, and manages content in an Obsidian vault.

## Overview

This skill turns your AI assistant into a knowledge management partner. It can save notes, clip articles, journal, queue content for later, and search your entire vault — all through natural language.

## Architecture

```
KnowledgeBase/
├── SKILL.md              # Skill entry point & workflow routing
└── Workflows/
    ├── Save.md           # Save notes, ideas, learnings, resources
    ├── Search.md         # Find existing vault content
    ├── DailyJournal.md   # Journal entries & weekly review
    ├── DailyNote.md      # Daily aggregation of all saved content
    ├── WatchLater.md     # URL queue for future processing
    ├── Lint.md           # Vault health audit (orphans, stale content, gaps)
    └── Synthesize.md     # Generate concept pages across multiple notes
```

See **[WORKFLOW.md](./WORKFLOW.md)** for the end-to-end pipeline — how Save / WatchLater / DailyJournal / Lint / Synthesize / Search fit together.

## Quick Start

1. Copy `CONFIG.example.md` and set your vault path
2. Place the skill files in your Claude Code skills directory
3. Say "save this note about..." or "search my vault for..."

## Configuration

See [CONFIG.example.md](./CONFIG.example.md) for all configurable values.

## Workflows

| Workflow | Triggers | What It Does |
|----------|----------|-------------|
| **Save** | "save this", "clip this", "note this down" | Routes content to the right vault folder with tags and metadata |
| **Search** | "search vault", "find notes about..." | Full-text, tag, title, date, or type search |
| **DailyJournal** | "journal entry", "weekly review" | Timestamped journal entries, one file per day |
| **DailyNote** | "what did I save today" | Auto-aggregated index of everything saved on a given day |
| **WatchLater** | "watch later", "read later", "show queue" | URL queue with type hints, processing tracking |
| **Lint** | "lint vault", "audit vault", "KB health" | 5-check health audit: orphans, stale content, missing cross-refs, Telos coverage, topical index rebuild |
| **Synthesize** | "synthesize notes on...", "concept page for...", "what do I know about..." | Reads multiple related notes and generates a concept page with patterns, core ideas, contradictions, and open questions |

## Vault Structure

```
VAULT_PATH/
├── 1. Inbox/                  ← Quick captures, watch-later queue
├── 2. Notes/
│   ├── Reference/             ← Factual notes
│   ├── Learning/              ← Lessons, TIL
│   ├── Ideas/                 ← Brainstorms
│   ├── Conversations/         ← Meeting notes
│   └── Synthesis/             ← Auto-generated concept pages
├── 3. Projects/               ← Project-specific notes
├── 4. Journal/                ← Daily journal entries
├── 5. Resources/
│   ├── Clippings/             ← Web clippings
│   └── Templates/             ← Weekly review, etc.
└── 7. Daily Notes/            ← Auto-generated daily aggregation
```

## File Format

Every saved note uses Obsidian-compatible markdown with YAML frontmatter:

```markdown
---
title: "Note Title"
date: 2026-03-12
type: learning
tags:
  - tag1
  - tag2
source: "conversation"
connections:
  related: ["[[2026-03-10-related-note]]"]
  status: connected
---

# Note Title

Content body in clean markdown.

## Connections

**Related:** [[2026-03-10-related-note]]
```

## Features

- **Auto content-type routing** — detects note type from your intent
- **Smart tagging** — generates 2-5 relevant tags automatically
- **Vault connections** — discovers and links to related existing notes via wikilinks
- **Daily note updates** — every save is logged in the daily note
- **Watch Later integration** — queued URLs auto-link when processed
- **Sources Index** — chronological index of all consumed content
- **Duplicate detection** — warns if URL already saved
- **Vault health audit** — periodic lint finds orphans, stale content, missing cross-references, thin Telos coverage
- **Concept synthesis** — generate second-order notes that analyze patterns across multiple vault notes
- **Optional Telos integration** — map notes to life-goals for purposeful knowledge tracking

## Guides

- [Workflow](./WORKFLOW.md) — Full end-to-end pipeline: input → aggregation → audit → synthesis → retrieval
- [Use Cases](./USE-CASES.md) — Common scenarios and examples
- [Usage Guide / Hướng dẫn sử dụng](./USAGE-GUIDE.md) — Detailed guide (Vietnamese)
