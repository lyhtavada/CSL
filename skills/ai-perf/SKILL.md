---
name: ai-perf
description: Use this skill when Liz provides a list of Crisp session IDs (for Joy and/or Chatty) and asks for an AI agent performance report. Fetches full transcripts from BigQuery crispchat_history, classifies each session, and fills in the daily report file.
version: 1.0.0
---

# AI Agent Performance Skill

When Liz provides a list of session IDs (Joy and/or Chatty), automatically fetch transcripts from BigQuery, classify each session, and generate or update the daily report.

## Trigger

Liz sends a list of Crisp session IDs — typically in the form `session_xxxxxxxx-...` or just the short 8-char prefix — for one or both apps (Joy/Chatty).

## Data Source

**BigQuery table:** `avada-crm.crm.crispchat_history`
**Service account:** `churn-prediction@avada-crm.iam.gserviceaccount.com`
**Private key:** loaded from `/Users/avada/CSL/.env` — but since BQ keys are removed from .env, use the key passed inline in session or ask Liz to paste the SA JSON.

**Key fields:**
- `website_id` — `72a663b0-4cda-4e3b-8878-426bdd79364c` for both Joy and Chatty (retention website)
- `conversationInfo` — JSON with `session_id`
- `event` — `message:send`
- `data` — JSON with `content`, `origin`, `type`
- `agentEmail` — email of operator who sent the message
- `timestamp` — milliseconds

## Steps

### 1. Auth — Get BQ access token

Build a JWT and exchange for a Google OAuth2 token:
- `iss`: `churn-prediction@avada-crm.iam.gserviceaccount.com`
- `scope`: `https://www.googleapis.com/auth/bigquery.readonly`
- `aud`: `https://oauth2.googleapis.com/token`

Sign with RS256 using the private key from the SA JSON Liz provides.

### 2. Fetch transcripts from BigQuery

For each session ID, run:

```sql
SELECT
  timestamp,
  event,
  JSON_VALUE(data, '$.origin') as origin,
  JSON_VALUE(data, '$.content') as content,
  JSON_VALUE(data, '$.type') as msg_type,
  agentEmail
FROM `avada-crm.crm.crispchat_history`
WHERE website_id = '72a663b0-4cda-4e3b-8878-426bdd79364c'
  AND JSON_VALUE(conversationInfo, '$.session_id') = '{full_session_id}'
ORDER BY timestamp ASC
```

Batch sessions in one query using `IN (...)` when possible to reduce round trips.

### 3. Classify each session

**Determine agent (Joyce vs Chattie):**
- Look for messages where `content` contains `"I'm Joyce"` or `"I'm your AI agent from Joy"` → **joy-agent**
- Look for messages where `content` contains `"I'm Chattie"` or `"AI agent from Chatty"` → **chatty-agent**
- If neither found → skip or mark as "no bot participation"

**Determine bucket:**
- **Bucket A (Escalated):** Find a message where `content` contains `"🚨"` and `"Escalation Alert"` or `content` contains `"<escalate_human>"` → `Escalated = ✅`
- **Bucket B (Human step-in):** Bot sent messages, then a human operator (non-Joyce/Chattie agentEmail) replied — but NO escalation alert found → `Human step-in = ✅`
- **Bucket C (Resolved):** Bot handled all messages, no escalation alert, no human follow-up → `Resolved = ✅`

**Determine escalation/step-in reason:**
- Extract the escalation handoff summary from the 🚨 alert message (usually contains `📋 *HANDOFF SUMMARY*`)
- For human step-in: summarize what the human did (assigned to whom, what action)

**Determine merchant name:**
- Look for operator messages greeting the merchant by name, or check the first user message

### 4. Extract Joyce/Chattie message content for QA notes

For each session:
- Collect all bot messages (where `content` includes bot's name or sent by Daisy agent)
- Note: accuracy, tone, whether it escalated at the right time
- Leave `QA score` as `—` unless there's a clear issue

### 5. Generate report

**Report date:** Ask Liz if unclear, or use today's date.
**Report file:** `reports/ai-agent-performance/YYYY-MM-DD.md`

Fill in using the TEMPLATE at `reports/ai-agent-performance/TEMPLATE.md`:
- Count sessions per agent
- Calculate resolved/escalated/step-in percentages
- Fill Session Log table with Crisp links: `[short_id](https://app.crisp.chat/website/72a663b0-4cda-4e3b-8878-426bdd79364c/inbox/{full_session_id})`
- Note any training data gaps observed

**Leave for Liz:**
- `**AI active:**` time range (ask Liz if not known)
- `**Overall:**` narrative summary (draft one, Liz edits)
- `QA score` column (leave `—` unless gap is obvious)

## Output

After generating the report file, print a short summary:
- Total sessions per agent
- Resolved / Escalated / Human step-in counts
- List of any notable gaps found
- Path to the report file

## Notes

- Sessions where bot sent 0 messages → mark as "Joyce/Chattie không tham gia" in Notes, count as human-handled (don't add to bot Handled count)
- If a session appears in both Joy and Chatty lists → de-duplicate, assign to whichever bot actually participated
- Crisp API is limited to 40 messages — **always use BigQuery** for full transcripts
