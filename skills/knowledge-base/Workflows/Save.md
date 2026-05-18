# Save Workflow

Save content to your Obsidian vault with proper formatting and location routing.

## Configuration

```
VAULT_PATH: {{YOUR_VAULT_PATH}}
```

All paths below are relative to `VAULT_PATH`.

## Content Type Detection

Determine the content type from user intent or explicit instruction:

| Type | Vault Location | Signals |
|------|---------------|---------|
| `note` | `2. Notes/Reference/` | General note, reference, factual content |
| `learning` | `2. Notes/Learning/` | Lesson learned, tutorial, how-to, TIL |
| `idea` | `2. Notes/Ideas/` | Brainstorm, concept, hypothesis, "what if" |
| `conversation` | `2. Notes/Conversations/` | Chat summary, meeting notes, discussion recap |
| `journal` | `4. Journal/` | Personal reflection, daily log (prefer DailyJournal workflow) |
| `project` | `3. Projects/` | Project-specific note, task context |
| `resource` | `5. Resources/Clippings/` | Web clipping, article save, external content |
| `inbox` | `1. Inbox/` | Default fallback, unsorted, quick capture |

**Default:** If type cannot be determined, use `inbox`.

## Filename Format

```
YYYY-MM-DD-{slug}.md
```

- `slug`: Lowercase, hyphens for spaces, strip special characters, max 60 characters
- Example: `2026-02-18-typescript-generics-cheatsheet.md`

## File Format

Every saved file uses this Obsidian-compatible markdown format:

```markdown
---
title: "{Title}"
date: {YYYY-MM-DD}
type: {content_type}
tags:
  - {tag1}
  - {tag2}
source: "{source_url_or_context}"
telos:
  problems: [P1]
  goals: [G1]
  projects: [PR0]
connections:
  related: ["[[2026-02-18-some-related-note]]"]
  status: connected | orphan
---

# {Title}

{Content body in clean markdown}

## Connections

**Related:** [[2026-02-18-some-related-note]] · [[2026-01-15-another-note]]

{Or if no connections found:}
*No connections found yet.*
```

## Procedure

1. **Receive content** from user (text, URL summary, conversation excerpt, etc.)
2. **Determine content type** using the detection table above. Ask user if ambiguous.
3. **Generate metadata:**
   - `title`: Clear, descriptive title
   - `date`: Today's date (YYYY-MM-DD)
   - `tags`: 2-5 relevant tags (lowercase, no hash prefix)
   - `source`: URL if from web, "conversation" if from chat, or relevant context
3.1. **Extract referenced URLs from conversation context:**
   - Scan the current conversation for any URLs mentioned by the user or discussed in the session
   - This includes: article links, YouTube URLs, blog posts, documentation, tweets, any `https://` references
   - Add all found URLs to a `references:` field in the YAML frontmatter:
     ```yaml
     references:
       - "https://example.com/article-discussed"
       - "https://youtube.com/watch?v=abc123"
     ```
   - Also add a `## References` section at the bottom of the note body (before `## Connections`):
     ```markdown
     ## References

     - [Article Title](https://example.com/article-discussed)
     - [Video Title](https://youtube.com/watch?v=abc123)
     ```
   - If the `source:` field is already a URL, still include it in `references:` for completeness
   - If no URLs found in the conversation, omit the `references:` field and `## References` section
   - This ensures conversations about articles always capture the original source links
3.5. **Infer Telos connections:**
   - Read `{{YOUR_TELOS_PATH}}/PROBLEMS.md`, `GOALS.md`, and `PROJECTS.md`
   - Based on the note's title, tags, and content, determine which Telos elements relate
   - Add a `telos:` field to the YAML frontmatter:
     ```yaml
     telos:
       problems: [P1]
       goals: [G1, G3]
       projects: [PR0]
     ```
   - If no Telos connection is apparent, add:
     ```yaml
     telos:
       relevance: none
     ```
   - Be conservative: only map when the connection is clear
   - Only read 3 files (Problems, Goals, Projects) — not all Telos files
3.6. **Discover vault connections (three-tier hierarchy):**

   **Speed constraint:** Max 2-3 Grep calls. No agent spawning. Must complete in <5 seconds.

   **Tier 1 — Telos metadata** (from step 3.5 results):
   - Telos IDs stay in the `telos:` frontmatter field ONLY (e.g., `goals: [G1, G3]`)
   - Do NOT generate wikilinks to Telos hub files (`[[Goals]]`, `[[Projects]]`, `[[Problems]]`, `[[Strategies]]`, etc.)
   - This prevents every note from backlinking to the same few Telos pages in Obsidian's graph

   **Tier 2 — Related vault notes** (search existing notes):
   - Take the note's 2-3 strongest tags and 1-2 title keywords
   - Grep `VAULT_PATH` for those terms in existing `.md` files (search frontmatter tags + titles)
   - For each match, extract the filename (without extension) as a `[[wikilink]]` target
   - **Cap: max 5 related note links.**
   - **One-directional only:** Link FROM this new note TO existing notes. NEVER edit existing notes to add backlinks.

   **Tier 3 — Orphan:**
   - If Tier 2 found no related notes → mark as orphan
   - Set `connections.status: orphan` in frontmatter
   - Add `*No connections found yet.*` in the Connections section
   - Orphan is fine — not every note needs to be connected

   **Build the `connections` frontmatter and `## Connections` body section from Tier 2 results.**

3.7. **Telos activity tracking (explicit request only):**
   - ONLY if the user explicitly says "track this", "this counts as G7", "log this to telos", or similar
   - Do NOT auto-track every save — this step is opt-in only
   - If triggered, call TelosLog.ts with the appropriate goal and metric:
     ```bash
     bun ~/.claude/skills/Telos/Tools/TelosLog.ts --text "{note title}" --goalId {G} --metricIndex {N} --delta 1
     ```
   - Common mapping: learning notes → G7 metricIndex 0 (learning hours)
   - If goal is ambiguous, ask which goal before logging

4. **Format content** as clean Obsidian markdown with YAML frontmatter
5. **Generate filename** using the date-slug format
6. **Resolve full path:** `VAULT_PATH / {vault_location} / {filename}`
7. **Write the file** using the Write tool
8. **Update daily note:** Follow `Workflows/DailyNote.md` procedure — create or update today's daily note at `{VAULT_PATH}/7. Daily Notes/{YYYY-MM-DD}.md` with a wikilink to the saved note in the appropriate section (Notes, Resources, etc. based on content type)
9. **Check Watch Later queue:** Read `{VAULT_PATH}/1. Inbox/watch-later.md` and check if the saved note's `source:` URL matches any item in the `## Queue` table.
   - If match found: move the row from `## Queue` to `## Processed`, adding today's date and a wikilink to the new note:
     ```markdown
     | {original_added_date} | {today} | `{type}` | [{Title}]({URL}) | [[{saved-note-filename}]] |
     ```
   - Update the stats line (`X queued | Y processed`)
   - If no match or queue file doesn't exist, skip this step
10. **Update Sources Index:** Append a new entry to `{VAULT_PATH}/{SOURCES_INDEX}`
   - Find today's date section (e.g., `## 2026-02-28`). If it doesn't exist, create it after the stats line, before older dates.
   - Add a line in this format:
     - If URL source: `- [Title](URL) — \`type\` \`tag1, tag2\``
     - If conversation: `- **Title** — \`type\` _conversation_ \`tag1, tag2\``
   - Update the `**Total entries:**` count in the header
   - This keeps a running chronological index of all consumed content
11. **Confirm** to user with: file path, title, type, tags, telos IDs, connections (related notes, or "orphan")

## Examples

**User says:** "Save this — TypeScript generics are covariant by default for arrays"

→ Type: `learning`
→ Path: `{VAULT_PATH}/2. Notes/Learning/2026-02-18-typescript-generics-covariance.md`
→ Tags: typescript, generics, type-system
→ Telos: G7, PR2
→ Connections: Related: [[2026-02-10-typescript-utility-types]]

**User says:** "Clip this article about quantum computing breakthroughs"

→ Type: `resource`
→ Path: `{VAULT_PATH}/5. Resources/Clippings/2026-02-18-quantum-computing-breakthroughs.md`
→ Tags: quantum-computing, science, technology
→ Connections: Orphan (no Telos match, no related notes found)

**User says:** "Save my thoughts on why education needs to be personalized"

→ Type: `idea`
→ Path: `{VAULT_PATH}/2. Notes/Ideas/2026-02-18-personalized-education.md`
→ Tags: education, personalization, learning
→ Telos: P0, G1
→ Connections: Related: [[2026-02-05-self-directed-learning]]

## Edge Cases

- **Duplicate filename:** Append `-2`, `-3`, etc. if file already exists
- **Project notes:** If user specifies a project, create subdirectory under `3. Projects/` if needed
- **Long content:** No truncation. Save full content.
- **URLs:** If user provides a URL, use WebFetch to extract content first, then save the extracted content
