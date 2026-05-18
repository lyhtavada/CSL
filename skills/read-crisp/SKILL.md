---
name: read-crisp
description: Use this skill when the user pastes a Crisp chat URL (app.crisp.chat/website/.../inbox/session_...). Automatically fetch the conversation via Crisp API and summarize the latest merchant request.
version: 1.0.0
---

# Read Crisp Skill

When Liz pastes a Crisp chat URL, automatically read the conversation and summarize what's happening — no need to ask.

## Trigger

Any message containing a URL matching:
`https://app.crisp.chat/website/{website_id}/inbox/{session_id}/`

## Steps

1. Extract `website_id` and `session_id` from the URL
2. Call Crisp API using credentials from `/Users/avada/CSL/.env`:
   - `CRISP_API_KEY` and `CRISP_API_SECRET` for Basic auth
   - Header: `X-Crisp-Tier: plugin`
3. Fetch conversation metadata:
   `GET https://api.crisp.chat/v1/website/{website_id}/conversation/{session_id}`
4. Fetch all messages:
   `GET https://api.crisp.chat/v1/website/{website_id}/conversation/{session_id}/messages`
5. Summarize and output (see Output Format below)

## Output Format

**Merchant:** [nickname] — [email] — [store URL if available]
**Plan:** [app + plan name + price if available]
**Assigned to:** [operator name]
**Status:** resolved / unresolved

---

**Tóm tắt diễn biến:**
- Bullet timeline of key events (merchant complaint → CS actions → current state)

**Latest request:**
- What the merchant is asking for right now, in 1-2 sentences

**Suggested next action:**
- What Liz likely needs to do (reply, approve refund, escalate, etc.)

---

Keep the summary tight — focus on what's actionable. Internal notes (type: "note") are included in the timeline when relevant.
