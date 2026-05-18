---
name: KnowledgeBase
description: Save content to your Obsidian vault. USE WHEN user says 'save to vault', 'knowledge base', 'save note', 'obsidian', 'remember this', 'save this', 'clip this', 'journal entry', 'daily journal', 'search vault', 'search notes', 'find in vault', 'save to obsidian', 'vault search', 'log this', 'note this down', 'add to knowledge base', 'watch later', 'read later', 'save for later', 'bookmark this', 'queue this', 'add to queue', 'show queue', 'what's in my queue', 'lint vault', 'audit vault', 'vault health', 'synthesize notes', 'concept page', 'merge notes', 'what do I know about'.
---

## Customization

**Before executing, check for user customizations at:**
`{{YOUR_SKILL_CUSTOMIZATIONS_PATH}}/`

If this directory exists, load and apply any PREFERENCES.md, configurations, or resources found there. These override default behavior. If the directory does not exist, proceed with skill defaults.

## MANDATORY: Voice Notification (REQUIRED BEFORE ANY ACTION)

```bash
curl -s -X POST http://localhost:8888/notify \
  -H "Content-Type: application/json" \
  -d '{"message": "Running the WORKFLOWNAME workflow in the KnowledgeBase skill to ACTION"}' \
  > /dev/null 2>&1 &
```

# KnowledgeBase Skill

Save, search, and manage content in the Obsidian vault.

## Workflow Routing

| Trigger | Workflow |
|---------|----------|
| Save content, note, idea, learning, reference, clip, resource | `Workflows/Save.md` |
| Search vault, find notes, search by tag/keyword | `Workflows/Search.md` |
| Journal entry, daily journal, log today | `Workflows/DailyJournal.md` |
| Daily note, what did I save today, browse by day, backfill daily notes | `Workflows/DailyNote.md` |
| Watch later, read later, save for later, bookmark, queue, show queue | `Workflows/WatchLater.md` |
| Lint vault, audit vault, vault health check, KB health | `Workflows/Lint.md` |
| Synthesize notes, concept page, merge notes, what do I know about | `Workflows/Synthesize.md` |

## Quick Reference

| Action | Default Location | Filename |
|--------|-----------------|----------|
| Save note | `2. Notes/Reference/` | `YYYY-MM-DD-slug.md` |
| Save idea | `2. Notes/Ideas/` | `YYYY-MM-DD-slug.md` |
| Save learning | `2. Notes/Learning/` | `YYYY-MM-DD-slug.md` |
| Journal entry | `4. Journal/` | `YYYY-MM-DD.md` |
| Clip resource | `5. Resources/Clippings/` | `YYYY-MM-DD-slug.md` |
| Quick capture | `1. Inbox/` | `YYYY-MM-DD-slug.md` |
| Watch later | `1. Inbox/` | `watch-later.md` |
| Daily note | `7. Daily Notes/` | `YYYY-MM-DD.md` |
| Lint report | Console output | — |
| Synthesis page | `2. Notes/Synthesis/` | `YYYY-MM-DD-{topic}-synthesis.md` |
