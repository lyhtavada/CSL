# Weekly FAQ mining (launchd)

Runs the `mine-chat-faqs` skill every **Monday 16:00 local** for both Joy and
Chatty over the **previous full calendar week (Mon→Sun)**, writing dated files into
`CSL/reports/weekly-faqs/{app}/`. You review the output
afterward — nothing is pushed to the agent KB or RAG.

## Files (source of truth, versioned in CSL)

| File | Role |
|---|---|
| `run-weekly.sh` | Headless runner — calls `claude -p` with the mining prompt for both apps |
| `com.avada.mine-faqs.plist` | launchd schedule (Mon 16:00), symlinked into `~/Library/LaunchAgents` |
| `install.sh` | Symlinks + loads the job (or `--remove` to uninstall) |

## Install

```bash
bash install.sh
```

## Run now (don't wait for Tuesday)

```bash
launchctl start com.avada.mine-faqs
# or run the script directly (foreground, see output live):
bash run-weekly.sh
```

## Uninstall

```bash
bash install.sh --remove
```

## Logs

```bash
tail -f /tmp/mine-faqs-weekly.log
```

## Notes / caveats

- **Mac must be awake** at the scheduled time (or it runs on next wake). launchd
  does not wake the machine. If the Mac is regularly off Tuesday morning, prefer
  a remote routine instead.
- The runner uses `--dangerously-skip-permissions` (no interactive approval in
  headless mode). Auth is the Claude **subscription** (OAuth), so a run draws on
  subscription quota — not a paid API bill. The runner also `unset`s any
  `ANTHROPIC_API_KEY` a repo `.env` might inject, to avoid flipping into paid-API mode.
- BQ creds come from `/Users/avada/CSL/.env` via `scripts/fetch_chats.py`.
- Recurring launchd jobs do **not** expire (unlike CronCreate's 7-day limit).
