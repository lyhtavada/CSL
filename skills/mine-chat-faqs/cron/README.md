# Weekly FAQ mining + KB diff/patch (launchd)

Runs the `mine-chat-faqs` skill every **Tuesday 11:00 local** for Joy, Chatty, and
Wishlist over the **previous full calendar week (Mon→Sun)**, writing dated files into
`CSL/reports/weekly-faqs/{app}/`. It then chains straight into the kb-sync
diff+patch flow (classify each mined FAQ vs the live KB, draft full-file patches)
and DMs Liz a review digest on Telegram. **Nothing is pushed to v2 or reindexed** —
that stays a manual step after Liz reviews (`kb-sync/scripts/push_kb.py`).

The separate `/kb-sync` cron (previously Monday 16:30, diff-only) is now
**disabled** since this job replaced it — see `kb-sync/cron/README.md`.
`/kb-sync` remains a manual, on-demand skill.

## Files (source of truth, versioned in CSL)

| File | Role |
|---|---|
| `run-weekly.sh` | Headless runner — calls `claude -p` with the mining+diff+patch prompt for all three apps |
| `com.avada.mine-faqs.plist` | launchd schedule (Tue 11:00), symlinked into `~/Library/LaunchAgents` |
| `install.sh` | Symlinks + loads the job (or `--remove` to uninstall) |

## Install

```bash
bash install.sh
```

## Run now (don't wait for next Tuesday)

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

## After the Telegram digest arrives

Review the digest + the mined-FAQ file, the `-kb-diff.md` report, and the payloads
file per app, then push the approved set:

```bash
python3 ~/CSL/skills/kb-sync/scripts/push_kb.py <payloads.json>
```

## Notes / caveats

- **Mac must be awake** at the scheduled time (or it runs on next wake). launchd
  does not wake the machine. If the Mac is regularly off Tuesday morning, prefer
  a remote routine instead.
- The runner uses `--dangerously-skip-permissions` (no interactive approval in
  headless mode). Auth is the Claude **subscription** (OAuth), so a run draws on
  subscription quota — not a paid API bill. The runner also `unset`s any
  `ANTHROPIC_API_KEY` a repo `.env` might inject, to avoid flipping into paid-API mode.
- BQ creds come from `/Users/avada/CSL/.env` via `scripts/fetch_chats.py`. The KB
  diff/patch step reads `CS2_API_TOKEN`, and the Telegram digest step reads
  `TELEGRAM_BOT_TOKEN`/`TELEGRAM_OWNER_ID` (via `skills/_shared/notify_tele.py`) —
  all also in `/Users/avada/CSL/.env`.
- Recurring launchd jobs do **not** expire (unlike CronCreate's 7-day limit).
