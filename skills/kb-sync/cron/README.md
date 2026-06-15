# kb-sync cron

Weekly **diff-only** run of `/kb-sync` — never auto-pushes to v2.

| | |
|---|---|
| Label | `com.avada.kb-sync` |
| Schedule | Tuesday 10:00 local (day after `/mine-chat-faqs` Mon 16:00) |
| Script | `run-weekly.sh` → Claude headless, `--dangerously-skip-permissions` |
| Auth | Claude subscription OAuth (no API bill); reads `CS2_API_TOKEN` from `~/CSL/.env` |
| Log | `/tmp/kb-sync-weekly.log` |
| Does | prep → diff both apps → build payloads → DM Liz to review |
| Does NOT | push to v2, reindex (review-gate — Liz runs `push_kb.py` after approving) |

## Install (run in a normal Terminal, not via Claude)
```
bash ~/CSL/skills/kb-sync/cron/install.sh
```
The permission classifier blocks Claude from loading launchd jobs headless, so Liz
installs it herself.

## Test now
```
launchctl start com.avada.kb-sync
# or directly:
bash ~/CSL/skills/kb-sync/cron/run-weekly.sh
```

## Remove
```
bash ~/CSL/skills/kb-sync/cron/install.sh --remove
```

## After the diff arrives
Review the Slack DM + payloads, then push the approved set:
```
python3 ~/CSL/skills/kb-sync/scripts/push_kb.py <payloads.json>
```
