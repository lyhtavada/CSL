# Diff prompt — fan-out compare (optional, for large batches)

When the mined-FAQ file is large (30+ FAQs), spawn one Agent (general-purpose) to
do the read-heavy compare and return a structured verdict, then review it yourself.
Adapt this prompt:

---

You are comparing two knowledge sources for the **<APP>** Shopify app to find gaps
and outdated content in the live KB.

SOURCE A (fresher — real customer chats this week, what the correct current answer is):
`<FAQ_FILE_PATH>`  — N FAQs, each with a frequency + standard answer.

SOURCE B (the LIVE KB of the agent on v2, cached locally):
Directory `/tmp/kb-sync/<APP>/`. Filenames use `__` for `/` (e.g.
`kb__faq__channels.md` = `kb/faq/channels.md`). Structure: `kb__case__*`,
`kb__faq__*`, `kb__reference__*`, `persona__*`, `agent.yaml`.

TASK — for EACH mined FAQ:
1. grep the cache by topic/keyword to find the matching KB file(s); read them fully.
2. Classify into exactly one: COVERED / OUTDATED / GAP / PARTIAL.
   - OUTDATED: quote the stale line in KB vs the correct line from the mined FAQ.
   - GAP: name the KB file it SHOULD go into.
   - PARTIAL: name the file + the missing sub-point.
3. Verify every candidate discrepancy against the actual file — do NOT assume, and
   count ALL occurrences of a stale string (don't trust a partial count).

OUTPUT (markdown):
- Summary table: mined Q# | topic | KB file | verdict
- `## Cần sửa (OUTDATED)` — file, stale line, correct line, one-line fix
- `## Cần bổ sung (GAP/PARTIAL)` — which file + what to add
- `## Ưu tiên` — top items ranked by mined frequency (high-freq first)

Quote real text from the files. If a file lacks something, that's a GAP, not an
invention.
