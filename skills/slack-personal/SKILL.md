---
name: slack-personal
description: Act as Liz's own Slack account (user token, xoxp-) to read DMs/threads, search across the workspace, send messages, or react — for anything the shared bot tokens can't see or can't do as "Liz" herself. Use when Liz asks to check/search/reply/react on her personal Slack, or references a DM the bot wouldn't have access to.
version: 1.0.0
---

# Slack Personal Skill

Uses `SLACK_USER_TOKEN` (xoxp-, in `~/CSL/.env`) — a **user token**, not a bot token. Every action runs as Liz's real account (`lyht`, workspace **Avada Group**). This is different from the existing bot-token flows (`feedback_slack_link.md`, `send_dm.py`), which act as the Avada bot and can only see channels the bot is a member of.

## What this token can do

- Read message history in any channel/private channel/DM/group DM Liz is in (`*:history`)
- Search across the whole workspace (`search:read`) — bot tokens have no search scope
- Send messages **as Liz herself** into existing channels/DMs (`chat:write`)
- Upload files, react to messages, manage private channels, invite to channels
- Read/update Liz's own profile

## What it cannot do

- **Cannot open a new DM** with someone Liz has never messaged (no `im:write`) — only post into channels/DMs that already exist
- No delete, no archive, no admin-level workspace management
- No `files:read` (can't fetch attachment contents)

## When to use

- Liz asks to check a DM or private channel the shared bot isn't in
- Liz wants to search Slack for something ("has anyone mentioned X")
- Liz wants a reply sent that should visibly come from her, not the bot
- A Slack link Liz pastes turns out to be a DM/private channel the bot token can't read (fall back here instead of failing)

## Scripts (`scripts/`)

All load `SLACK_USER_TOKEN` from `/Users/avada/CSL/.env` via `_common.py`.

- `read_thread.py` — read a thread/channel/DM by link or `--channel [--ts]`
- `search.py "query"` — search messages workspace-wide (Slack search modifiers like `from:@x` work)
- `send_message.py` — post as Liz; **dry-run by default**, requires `--send` to actually post
- `react.py` — add an emoji reaction to a message
- `request_approval.py` / `check_approval.py` — approval flow for sends (see below)

## Approval flow before sending as Liz

Before any real send, post the draft to Liz's own Slack self-DM ("Saved Messages" / "Just for me", channel `D02GQ4DCFBP`) for her to review from her phone or desktop — not just as a terminal preview in this chat.

1. `request_approval.py --channel <real target> [--thread-ts ...] --text "..."` — posts the draft into Liz's self-DM with a ✅-to-approve prompt, prints `approval_ts`
2. Liz reacts `:white_check_mark:` on that message in Slack when she approves (edit and re-run step 1 if she wants changes instead)
3. `check_approval.py --ts <approval_ts>` — exits 0 and prints `APPROVED` once the reaction is there, exits 1 / `NOT YET APPROVED` otherwise
4. Only after approval, run `send_message.py --channel <real target> [--thread-ts ...] --text "..." --send`

Never skip straight to `send_message.py --send` for anything other than trivial, Liz-requested-verbatim, low-stakes sends — this account posts as Liz herself and a bad send is visible and hard to unsend.

`find_self_dm_channel()` in `_common.py` caches the self-DM id in `scripts/.self_dm_cache` after the first lookup (finding it requires paginating ~280 im channels).

## Example

```
python3 scripts/read_thread.py --link "https://avadaio.slack.com/archives/D0XXXXX/p1690000000000000"
python3 scripts/search.py "refund policy"

# approval flow
python3 scripts/request_approval.py --channel D0XXXXX --text "..."
# ... Liz reacts ✅ in Slack ...
python3 scripts/check_approval.py --ts <approval_ts>
python3 scripts/send_message.py --channel D0XXXXX --text "..." --send
```
