#!/usr/bin/env bash
# Push 6 KB patches to the Chatty agent (Ivy) on v2, then reindex.
# Run from a normal Terminal:  bash ~/CSL/reports/analysis/push-chatty-kb-v2.sh
# Reads CS2_API_URL + CS2_API_TOKEN from ~/CSL/.env
set -euo pipefail

ENV_FILE="$HOME/CSL/.env"
PAYLOADS="$HOME/CSL/reports/analysis/chatty-kb-v2-payloads.json"
AGENT="chatty-agent"

# load creds
CS2_API_URL=$(grep -E '^CS2_API_URL=' "$ENV_FILE" | head -1 | cut -d= -f2-)
CS2_API_TOKEN=$(grep -E '^CS2_API_TOKEN=' "$ENV_FILE" | head -1 | cut -d= -f2-)
[ -n "$CS2_API_URL" ] && [ -n "$CS2_API_TOKEN" ] || { echo "Missing CS2_API_URL / CS2_API_TOKEN in $ENV_FILE"; exit 1; }

echo "Target: $CS2_API_URL  agent=$AGENT"
echo "Payloads: $PAYLOADS"
echo

# POST each file. payloads.json is an array of {agent,path,content}.
COUNT=$(python3 -c "import json;print(len(json.load(open('$PAYLOADS'))))")
echo "Writing $COUNT files..."
for i in $(seq 0 $((COUNT-1))); do
  python3 -c "import json;json.dump(json.load(open('$PAYLOADS'))[$i],open('/tmp/_kb_one.json','w'),ensure_ascii=False)"
  PATH_VAL=$(python3 -c "import json;print(json.load(open('/tmp/_kb_one.json'))['path'])")
  echo -n "  POST $PATH_VAL ... "
  RESP=$(curl -s -m 30 -X POST \
    -H "Authorization: Bearer $CS2_API_TOKEN" \
    -H "Content-Type: application/json" \
    --data-binary @/tmp/_kb_one.json \
    "$CS2_API_URL/api/kb/file")
  echo "$RESP"
done

echo
echo "Reindexing agent $AGENT ..."
curl -s -m 120 -X POST \
  -H "Authorization: Bearer $CS2_API_TOKEN" \
  -H "Content-Type: application/json" \
  -d "{\"agent\":\"$AGENT\"}" \
  "$CS2_API_URL/api/kb/reindex"
echo
echo "Done. Verify in admin KB UI or via GET /api/kb/file?agent=$AGENT&path=..."
rm -f /tmp/_kb_one.json
