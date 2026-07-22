# kb-sync cron — DISABLED (2026-07-22)

**This launchd job is currently uninstalled.** Since 2026-07-22, `/mine-chat-faqs`'s
own weekly cron (Tuesday 11:00) already chains straight into this same diff+patch
logic right after mining, so a separate weekly kb-sync run became redundant —
it was re-diffing last week's mined file a day after the fresher one had already
been diffed. Disabled instead of left running.

`/kb-sync` itself is untouched and still fully usable as a **manual, on-demand**
skill — e.g. to re-diff mid-week if the live KB changed outside this flow, or to
diff/patch a specific mined-FAQ file by hand. Just run the skill normally
(`/kb-sync` or ask Betty); nothing below is required for that.

| | |
|---|---|
| Label | `com.avada.kb-sync` |
| Schedule (when installed) | Monday 16:30 local |
| Script | `run-weekly.sh` → Claude headless, `--dangerously-skip-permissions` |
| Auth | Claude subscription OAuth (no API bill); reads `CS2_API_TOKEN` from `~/CSL/.env` |
| Log | `/tmp/kb-sync-weekly.log` |
| Does | prep → diff both apps → build payloads → DM Liz to review |
| Does NOT | push to v2, reindex (review-gate — Liz runs `push_kb.py` after approving) |

## Re-enable

```
bash ~/CSL/skills/kb-sync/cron/install.sh
```

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
