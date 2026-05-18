# Watch Later Workflow

Quick-capture URLs and content to a "Watch Later" queue for future processing.

## Configuration

```
VAULT_PATH: {{YOUR_VAULT_PATH}}
QUEUE_FILE: 1. Inbox/watch-later.md
```

## Trigger Phrases

"watch later", "read later", "save for later", "bookmark this", "queue this", "add to queue", "I'll read this later", "remind me to watch", "save link", "check later", "show queue", "what's in my queue"

## Workflow Routing

| Intent | Action |
|--------|--------|
| Add URL/content to queue | → **Add to Queue** (below) |
| Show current queue | → **View Queue** (below) |
| Process/complete a queued item | → **Process Item** (below) |
| Clear completed items | → **Clean Queue** (below) |

---

## Add to Queue

### Procedure

1. **Extract the URL** from the user's message
   - If user provides a bare URL, use WebFetch to get the page title
   - If user provides URL + context, use their context as the description
   - If no URL (e.g., "watch later: that Sam Altman video"), ask for the link
2. **Determine content type hint** (used when processing later):
   - `article` — blog post, news article, essay, newsletter
   - `video` — YouTube, Vimeo, any video URL
   - `podcast` — audio content, podcast episode
   - `thread` — Twitter/X thread, Reddit thread, forum discussion
   - `paper` — academic paper, PDF, research
   - `tool` — product, app, GitHub repo to evaluate
   - `other` — anything else
3. **Read the queue file** at `{VAULT_PATH}/{QUEUE_FILE}`
   - If it doesn't exist, create it with the template below
4. **Append the new item** to the `## Queue` section, directly after the `| --- | --- | --- | --- |` header row:
   ```markdown
   | {YYYY-MM-DD} | `{type}` | [{Title}]({URL}) | {user's note or auto-generated context} |
   ```
5. **Confirm** to user: title, type, position in queue (count of items)

### Queue File Template

If the file doesn't exist, create it with:

```markdown
---
title: "Watch Later"
date: 2026-02-28
type: index
tags:
  - queue
  - watch-later
  - reading-list
source: "auto-managed by PAI KnowledgeBase skill"
---

# Watch Later

Content queued for future reading, watching, or processing. Items move to Processed when saved to the vault.

**Stats:** 0 queued | 0 processed

## Queue

| Added | Type | Link | Why |
| --- | --- | --- | --- |

## Processed

| Added | Processed | Type | Link | Saved As |
| --- | --- | --- | --- | --- |
```

---

## View Queue

### Procedure

1. **Read** `{VAULT_PATH}/{QUEUE_FILE}`
2. **Display** the Queue section contents to the user
3. **Show stats:** X items queued, Y processed
4. If queue is empty, say so

---

## Process Item

This happens automatically during the **Save workflow** (see Save.md step 9.5). But if the user explicitly says "process this from my queue" or "I read [title] from my queue":

### Procedure

1. **Read** `{VAULT_PATH}/{QUEUE_FILE}`
2. **Find the matching item** in the `## Queue` section by URL or title match
3. **Trigger the Save workflow** (`Workflows/Save.md`) with the URL — this does the full extraction, tagging, Telos mapping, connections, and Sources Index update
4. **Move the item** from `## Queue` to `## Processed`:
   - Remove the row from the Queue table
   - Add to the Processed table with:
     ```markdown
     | {original_added_date} | {today} | `{type}` | [{Title}]({URL}) | [[{saved-note-filename}]] |
     ```
5. **Update stats** in the header line
6. **Confirm** to user: what was processed, where it was saved, queue count remaining

---

## Clean Queue

### Procedure

1. **Read** `{VAULT_PATH}/{QUEUE_FILE}`
2. If user says "clean queue" or "clear completed":
   - Keep the Processed section but offer to archive items older than 30 days
3. If user says "clear all" — ask for confirmation first, then empty both sections
4. **Update stats**

---

## Edge Cases

- **Duplicate URL:** If the URL already exists in the queue, notify the user instead of adding a duplicate
- **URL already saved:** If the URL matches a `source:` field in an existing vault note, tell the user "You already saved this on {date}" and link to the existing note
- **Multiple URLs in one message:** Add all of them, confirm the batch
- **No URL provided:** Ask the user for the link. Don't guess.
