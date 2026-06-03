---
name: read-crisp
description: Use this skill when the user pastes a Crisp chat URL (app.crisp.chat/website/.../inbox/session_...). Automatically fetch the full conversation via BigQuery (crispchat_history) and summarize the latest merchant request.
version: 2.0.0
---

# Read Crisp Skill

When Liz pastes a Crisp chat URL, automatically read the full conversation and summarize what's happening — no need to ask.

## Trigger

Any message containing a URL matching:
`https://app.crisp.chat/website/{website_id}/inbox/{session_id}/`

## Data Source

**BigQuery table:** `avada-crm.avada_cs.crisp_chats`  
**Credentials:** load from `/Users/avada/CSL/.env`:
- `BQ_SA_CLIENT_EMAIL`
- `BQ_SA_PRIVATE_KEY`
- `BQ_SA_PRIVATE_KEY_ID`

**Why BQ instead of Crisp API:** Crisp API is limited to ~40 messages per call; BQ has the full transcript with no rate limit.

**Important:** MCP tool không có quyền query bảng này trực tiếp. Phải dùng **Python script** với `google-cloud-bigquery` library và scope `https://www.googleapis.com/auth/bigquery` (không dùng `bigquery.readonly`).

## Steps

### 1. Extract session info from URL

Parse `website_id` and full `session_id` UUID from the URL.  
Example: `https://app.crisp.chat/website/72a663b0-.../inbox/session_4afa0099-a070-4503-9a45-798f41568b93`

### 2. Run Python script to fetch transcript

```python
from dotenv import dotenv_values
from google.oauth2 import service_account
from google.cloud import bigquery

env = dotenv_values('/Users/avada/CSL/.env')

key_data = {
    "type": "service_account",
    "project_id": "avada-crm",
    "private_key_id": env["BQ_SA_PRIVATE_KEY_ID"],
    "private_key": env["BQ_SA_PRIVATE_KEY"].replace("\\n", "\n"),
    "client_email": env["BQ_SA_CLIENT_EMAIL"],
    "token_uri": "https://oauth2.googleapis.com/token"
}

credentials = service_account.Credentials.from_service_account_info(
    key_data,
    scopes=[
        "https://www.googleapis.com/auth/bigquery",
        "https://www.googleapis.com/auth/cloud-platform"
    ]
)
client = bigquery.Client(project="avada-crm", credentials=credentials)
```

### 3. Query transcript

```sql
SELECT
  timestamp,
  fromType,
  origin,
  content,
  type,
  agentEmail,
  customerEmail,
  customerNickname,
  conversationState
FROM `avada-crm.avada_cs.crisp_chats`
WHERE session_id = '{session_id}'
ORDER BY timestamp ASC
```

**Note:** `session_id` trong bảng là full string kể cả prefix `session_`, ví dụ: `session_13432525-b378-4b6a-91df-f0407c3e886a`

### 4. Parse and summarize

From the messages:
- **Merchant name:** look for CS greeting ("Hi [Name]") or first user message signature
- **Issue timeline:** bullet list of key events — merchant request → CS actions → current state
- **AI bot involvement:** note if Joyce/Chattie participated and what they did
- **Current status:** resolved / pending / escalated
- **Latest request:** what the merchant is asking right now

Internal notes (`origin = 'note'`) are included in timeline when relevant.

## Output Format

**Merchant:** [name] — [email if visible]  
**Assigned to:** [operator name]  
**Status:** resolved / pending / escalated

---

**Tóm tắt diễn biến:**
- Bullet timeline of key events (merchant complaint → CS actions → current state)

**Latest request:**
- What the merchant is asking for right now, in 1-2 sentences

**Suggested next action:**
- What Liz likely needs to do (reply, approve refund, escalate, etc.)

---

Keep the summary tight — focus on what's actionable.
