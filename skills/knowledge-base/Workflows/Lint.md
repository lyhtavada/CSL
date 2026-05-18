# Lint Workflow

Audit the Obsidian vault for health issues: orphan notes, stale content, missing cross-references, Telos coverage gaps, and topical index freshness. Inspired by Karpathy's LLM Wiki lint operation.

## Configuration

```
VAULT_PATH: {{YOUR_VAULT_PATH}}
SOURCES_INDEX: 2. Notes/Reference/sources-index.md
TELOS_PATH: {{YOUR_TELOS_PATH}}  # optional, set to skip Telos checks
```

## Trigger Phrases

"lint vault", "audit vault", "vault health check", "check vault health", "vault lint", "knowledge base audit", "KB health"

## Speed Constraints

- Max 15 Grep/Glob calls total across all checks
- No agent spawning — all checks run inline
- Target completion: <30 seconds
- Cap results per check: max 20 items reported
- **Run checks 1-4 in parallel** — they are independent reads. Check 5 runs last (it writes).

---

## Checks

### 1. Orphan Reconnection

**Goal:** Find notes marked `status: orphan` and attempt to connect them to newer notes that didn't exist when they were saved.

**Procedure:**

1. Grep `VAULT_PATH` for `status: orphan` in frontmatter across `**/*.md`
2. Collect all orphan filenames (cap: 10 oldest first). Read their frontmatter to extract all tags.
3. Batch: grep vault once for the combined set of strongest tags across all orphans (single grep call with alternation pattern, e.g. `tag1|tag2|tag3`). Match results back to individual orphans.
4. For each orphan with matches → report as **reconnection candidate** with suggested wikilinks
5. Do NOT auto-edit orphan notes — report only
6. **Output:** List of orphans with suggested connections

### 2. Stale Content Detection

**Goal:** Surface notes older than 90 days that relate to active Telos goals — they may contain outdated information.

**Procedure:**

1. Read `{TELOS_PATH}/GOALS.md` to get active goal IDs and descriptions
2. Grep `VAULT_PATH` for notes with `telos:` frontmatter containing active goal IDs
3. Filter to notes with `date:` older than 90 days from today
4. **Output:** List of stale notes grouped by Telos goal, with date and title

### 3. Missing Cross-References

**Goal:** Find note clusters that share 3+ tags but don't link to each other.

**Procedure:**

1. Grep `VAULT_PATH` for all unique tags across frontmatter (sample up to 15 most common tags)
2. For each high-frequency tag, find notes that share it (cap: 9 notes per tag)
3. For clusters of 3+ notes sharing 3+ tags:
   - Check if they have `[[wikilinks]]` to each other in their `## Connections` section
   - If not → report as **missing cross-reference cluster**
4. **Output:** Clusters with suggested links (cap: 5 clusters reported)

### 4. Telos Gap Analysis

**Goal:** Show how well each Telos goal is covered by vault notes — surface goals with thin coverage.

**Procedure:**

1. Read `{TELOS_PATH}/GOALS.md` and `{TELOS_PATH}/PROJECTS.md`
2. For each goal/project ID (G1-G9, PR0-PR3):
   - Grep `VAULT_PATH` for the ID in `telos:` frontmatter
   - Count matching notes
3. **Output:** Table of goal/project → note count, sorted ascending (thinnest coverage first)
   ```
   | Telos ID | Description | Notes | Coverage |
   |----------|-------------|-------|----------|
   | G6       | Health routine | 2 | thin |
   | G8       | Family time | 4 | light |
   | G7       | Learn and read | 87 | strong |
   ```

### 5. Topical Index Rebuild (runs after checks 1-4)

**Goal:** Add or update a `## By Topic` section in the sources index, grouping entries by domain. This is the only check that **writes** to the vault — all other checks are read-only audits.

**Procedure:**

1. Read `{VAULT_PATH}/{SOURCES_INDEX}` (if >200 entries, process only the 100 most recent)
2. Collect all entries with their tags
3. Derive topic categories from tag frequency: count occurrences of each tag, group tags that co-occur frequently (e.g., `ai, agents, llm` → "AI & Machine Learning"). Use the top 8-10 tag clusters as categories. Tags appearing fewer than 3 times go under "Other."
4. Merge similar tags: `ai` + `artificial-intelligence`, `ts` + `typescript`, `dev` + `engineering` → same category
5. Group entries under topic headings
6. If a `## By Topic` section already exists, replace it. If not, append it after the chronological entries.
7. Write the updated sources index

---

## Output Format

Present results as a structured health report:

```markdown
# Vault Health Report — {YYYY-MM-DD}

## Summary
- **Total notes scanned:** {N}
- **Orphans found:** {N} ({N} reconnection candidates)
- **Stale notes:** {N} (older than 90 days, linked to active goals)
- **Missing cross-refs:** {N} clusters
- **Telos coverage:** {thinnest goal} has only {N} notes

## 1. Orphan Reconnection Candidates
{results or "All notes are connected."}

## 2. Stale Content
{results or "No stale content found."}

## 3. Missing Cross-References
{results or "Cross-references look healthy."}

## 4. Telos Coverage
{table}

## 5. Topical Index
{Updated/rebuilt — {N} topics, {N} entries}
```

## Edge Cases

- **Empty vault:** Report "Vault has fewer than 5 notes — lint is not useful yet."
- **No Telos files:** Skip checks 2 and 4, note in report: "Telos files not found — skipping goal-related checks."
- **Sources index missing:** Skip check 5, note in report: "Sources index not found — skipping topical index rebuild."
- **Very large vault (500+ notes):** Reduce orphan scan to 5, tag sampling to 10, and add a warning: "Large vault — running abbreviated lint. Consider running focused checks individually."
