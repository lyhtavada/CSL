# Full Workflow — How I Actually Use This Skill

This doc walks through the end-to-end lifecycle of a piece of knowledge as it moves through the vault: from the moment an idea, article, or conversation hits me, to the moment it becomes a structured concept page I can trust later.

Five stages:

```
1. INPUT        → 2. AGGREGATION → 3. AUDIT  → 4. SYNTHESIS → 5. RETRIEVAL
   Save                DailyNote     Lint        Synthesize      Search
   WatchLater          DailyJournal
```

Each stage has a dedicated workflow file under `Workflows/`. This doc ties them together.

---

## Stage 1 — INPUT

**Goal:** capture raw knowledge with zero friction, at the speed of thought.

Three entry points, depending on the shape of the input:

### 1a. `Save` — I know what this is and I want it in the vault now

Trigger: *"save this note..."*, *"save this learning..."*, *"save this idea..."*, *"clip this article..."*

What the skill does:

- Detects content type (`note`, `learning`, `idea`, `conversation`, `resource`, `project`, `inbox`) and routes to the right folder
- Generates filename: `YYYY-MM-DD-slug.md`
- Builds YAML frontmatter: title, date, type, tags (2–5), source, telos mapping, connections
- Runs a **three-tier connection discovery**:
  - Tier 1: Telos metadata only in frontmatter (never wikilinks to Telos hub pages — avoids graph pollution)
  - Tier 2: 2–3 grep calls against existing notes for shared tags/keywords → up to 5 `[[wikilinks]]`, one-directional
  - Tier 3: marks `status: orphan` if no related notes found (that's fine — orphans get reconnected later by Lint)
- Appends the note to today's **Daily Note** and to the **Sources Index**
- Scans today's conversation for URLs → adds them under `references:` frontmatter and a `## References` body section
- If the saved URL matches an item in the Watch Later queue, promotes it from Queue → Processed

→ Full spec: [`Workflows/Save.md`](./Workflows/Save.md)

### 1b. `WatchLater` — I'll deal with this later

Trigger: *"watch later: <url>"*, *"read later: <url>"*, *"bookmark this"*

What the skill does:

- Appends the URL to `1. Inbox/watch-later.md` with an auto-detected type (`article`, `video`, `podcast`, `thread`, `paper`, `tool`)
- Fetches the page title if the user gave a bare URL
- Rejects duplicates (URL already in queue OR URL already saved to vault)
- `"show my queue"` prints the table; `"process first item"` triggers Save on that URL and moves the row to `## Processed`

→ Full spec: [`Workflows/WatchLater.md`](./Workflows/WatchLater.md)

### 1c. `DailyJournal` — I want to log a thought, not a fact

Trigger: *"journal entry..."*, *"weekly review"*

What the skill does:

- Appends a timestamped section (`## HH:MM`) to `4. Journal/YYYY-MM-DD.md` — one file per day, many entries per day
- Preserves user voice verbatim; no AI editing
- Updates the Daily Note with a `## Journal` link
- `"weekly review"` generates the weekly template with live Telos goals/projects/strategies for me to fill in

→ Full spec: [`Workflows/DailyJournal.md`](./Workflows/DailyJournal.md)

---

## Stage 2 — AGGREGATION

**Goal:** every input from Stage 1 automatically lands on one page per day, so "what did I do / learn / save today" is a single read.

`DailyNote` is not invoked directly — it's a subroutine called by Save and DailyJournal. For every input, the relevant daily note at `7. Daily Notes/YYYY-MM-DD.md` gets updated with a wikilink under the right section (`## Notes`, `## Journal`, `## Resources`).

This means my vault has two parallel indexes:

- **Chronological** — daily notes: "what happened on day X"
- **Topical** — sources index + tag graph: "what do I have on topic Y"

Both are kept in sync automatically by every Save.

**Backfill:** `"backfill daily notes"` scans the whole vault and creates daily notes for any existing content that pre-dated this skill. Useful once, after installing.

→ Full spec: [`Workflows/DailyNote.md`](./Workflows/DailyNote.md)

---

## Stage 3 — AUDIT (`Lint`)

**Goal:** the vault is only as useful as its graph is healthy. Lint is the periodic garbage collection pass.

Trigger: *"lint vault"*, *"audit vault"*, *"vault health check"*, *"KB health"*

Runs 5 checks — the first 4 in parallel (read-only), the 5th serially (writes):

| # | Check | What it finds |
|---|-------|---------------|
| 1 | **Orphan reconnection** | Notes marked `status: orphan` that now share tags with newer notes → suggests wikilinks (report only, doesn't auto-edit) |
| 2 | **Stale content** | Notes older than 90 days that are linked to active Telos goals → might be outdated |
| 3 | **Missing cross-refs** | Clusters of 3+ notes sharing 3+ tags but not linked to each other → suggests the missing links |
| 4 | **Telos coverage** | For each Telos goal/project, how many notes cover it — surfaces thin goals (`G6: Health routine — 2 notes, thin`) |
| 5 | **Topical index rebuild** | Regenerates the `## By Topic` section in the Sources Index by clustering tags |

Speed budget: max 15 Grep/Glob calls, target <30s, no agent spawning. Output is a structured **Vault Health Report** with a summary at the top and per-check findings below.

Important: checks 1–4 are **read-only**. Only check 5 writes to the vault. I can run Lint as often as I want without worrying about mutations.

→ Full spec: [`Workflows/Lint.md`](./Workflows/Lint.md)

---

## Stage 4 — SYNTHESIS

**Goal:** turn scattered notes into understanding. A synthesis page is a second-order note — not a summary, but an analysis of what I *collectively* know on a topic.

Trigger: *"synthesize notes on X"*, *"concept page for X"*, *"what do I know about X"*, *"merge notes about X"*

What the skill does:

1. **Freshness check** — if a synthesis for this topic already exists, check whether new source notes have appeared since. If not, don't regenerate (avoids wasting effort).
2. **Source discovery** — parallel tag search + title search + content search, deduplicated by file path, excluding previous synthesis pages. Minimum 3 source notes required; capped at 15 most recent.
3. **Full read** — reads the *complete* content of every source note, not just summaries. The synthesis has to demonstrate understanding, not aggregation.
4. **Concept page generation** — writes to `2. Notes/Synthesis/YYYY-MM-DD-{topic}-synthesis.md` with these sections:
   - **Key Patterns** — recurring themes across notes
   - **Core Ideas** — most important ideas, grouped logically, each cited with `[[wikilink]]`
   - **Contradictions & Tensions** — conflicting claims (if any)
   - **Open Questions** — what the notes raise but don't answer → gaps to fill with future Save operations
   - **Sources** — full wikilink list with one-line descriptions
5. Updates today's Daily Note with a link to the new synthesis page.

Synthesis is the payoff of the whole system. Stage 1 captures, Stage 2 indexes, Stage 3 cleans, Stage 4 **thinks**.

→ Full spec: [`Workflows/Synthesize.md`](./Workflows/Synthesize.md)

---

## Stage 5 — RETRIEVAL

**Goal:** find anything, by any access pattern.

Trigger: *"search vault for..."*, *"find notes tagged..."*, *"find notes from {date}"*, *"find all learnings"*

Five search modes, auto-selected from query shape:

| Mode | Example |
|------|---------|
| Keyword (default) | "search vault for rate limiting" |
| Tag | "find notes tagged with devops" |
| Title / filename | "find note named docker" |
| Date / range | "find notes from 2026-03-10" |
| Type | "find all learning notes" |

Results show title, date, type, tags, content preview, full vault path. Capped at 10 with total count if >20.

→ Full spec: [`Workflows/Search.md`](./Workflows/Search.md)

---

## How the stages reinforce each other

```
Save          ─┐
WatchLater    ─┼─→ DailyNote  ─→  Sources Index  ─→  Lint  ─→  Synthesize  ─→  Search
DailyJournal  ─┘                                                                  ↑
                                                                                  │
                                                         (every stage feeds this ─┘)
```

- **Save** writes both a note AND updates DailyNote + Sources Index → Stage 2 is free, not a separate action.
- **Lint** reads across everything Save produced → cleans orphans, surfaces gaps → I know *what to save next* or *what synthesis is worth doing*.
- **Synthesize** reads Save's output, writes a new concept note that itself becomes a Save → self-reinforcing loop.
- **Search** is the reader-side interface to everything above.

The vault is not a filing cabinet. It's a feedback loop.

---

## My actual weekly cadence

| Day | Stage | What I do |
|-----|-------|-----------|
| Daily | 1 + 2 | Save / WatchLater / Journal as things happen — no batching |
| Daily end | 2 | Quick glance at daily note (*"what did I save today"*) |
| Weekly | 3 | `"lint vault"` — review orphans, stale notes, thin goals |
| Weekly | 4 | Pick 1–2 topics that have grown → `"synthesize notes on X"` |
| Weekly | 1 (review) | `"weekly review"` — fill in the template |
| Ad hoc | 5 | Search when I need something specific |

The skill doesn't enforce this cadence — it just makes each step fast enough that the cadence holds without discipline.

---

## Configuration

See [`CONFIG.example.md`](./CONFIG.example.md) for all variables. The only required one is `VAULT_PATH`. Telos integration is optional (Lint skips related checks if `TELOS_PATH` is not set).
