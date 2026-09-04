#!/usr/bin/env python3
"""
run_tests.py — batch-run test questions against the live CS v2 bot (/api/chat)
and dump raw Q/A pairs for Betty to judge. No pass/fail logic here — keyword
matching is brittle (a correct answer can be phrased many ways, and a wrong
one can still contain the "right" keyword). Judging is a reading task, done
after this script returns.

Usage:
    python3 run_tests.py <app> <questions.json> [output.json] [--target sim|prod]

<questions.json> = JSON array of strings, or array of {"id": "...", "question": "..."}
<output.json>    = where to write results (default: stdout only)
--target          = which environment to hit (default: prod / cs2.avada.net).
                     Use --target sim to test against sim.avada.net BEFORE a
                     patch is pushed to prod (see kb-sync/scripts/push_kb.py
                     "Recommended safer flow").

Reuses ../../kb-sync/scripts/kb_api.py for creds + the /api/chat client.
"""
import json
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "kb-sync", "scripts"))
from kb_api import load_creds, agent_id, chat  # noqa: E402


def main():
    args = sys.argv[1:]
    target = "prod"
    if "--target" in args:
        i = args.index("--target")
        target = args[i + 1]
        del args[i:i + 2]

    if len(args) < 2:
        sys.exit("usage: run_tests.py <app> <questions.json> [output.json] [--target sim|prod]")

    app = args[0]
    questions_path = args[1]
    output_path = args[2] if len(args) > 2 else None

    with open(questions_path) as f:
        raw = json.load(f)

    questions = []
    for i, item in enumerate(raw, 1):
        if isinstance(item, str):
            questions.append({"id": f"Q{i}", "question": item})
        else:
            questions.append({"id": item.get("id", f"Q{i}"), "question": item["question"]})

    base, token = load_creds(target)
    agent = agent_id(app)

    results = []
    for q in questions:
        try:
            resp = chat(base, token, agent, q["question"])
            results.append({
                "id": q["id"],
                "question": q["question"],
                "reply": resp.get("reply", ""),
                "sources_count": resp.get("sources_count"),
                "duration_ms": resp.get("duration_ms"),
                "error": None,
            })
        except Exception as e:
            results.append({
                "id": q["id"],
                "question": q["question"],
                "reply": None,
                "sources_count": None,
                "duration_ms": None,
                "error": str(e),
            })
        print(f"  [{q['id']}] done", file=sys.stderr)

    out = {"app": app, "agent": agent, "target": target, "results": results}
    text = json.dumps(out, ensure_ascii=False, indent=2)

    if output_path:
        with open(output_path, "w") as f:
            f.write(text)
        print(f"Wrote {len(results)} result(s) to {output_path}", file=sys.stderr)
    else:
        print(text)


if __name__ == "__main__":
    main()
