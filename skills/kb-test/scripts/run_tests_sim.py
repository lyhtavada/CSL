#!/usr/bin/env python3
"""
run_tests_sim.py — batch-run kb-test questions through the REAL bridge
pipeline via the local sim-crisp process, instead of the /api/chat shortcut
used by run_tests.py. Catches things /api/chat can't: multi-turn context,
the human_active gate, greeting behavior.

Usage:
    python3 run_tests_sim.py <app> <questions.json> [output.json]

<questions.json> = JSON array of items, each either:
  - a string                         -> single-turn question
  - {"id","question"}                -> single-turn question
  - {"id","turns":[...]}             -> multi-turn: turns sent in order in
                                        the same session; only the LAST
                                        turn's reply is judged as "the
                                        answer", earlier replies are kept
                                        for context in the output
  - any item may add "profile": {...} to override the default dummy
    merchant profile (see sim_client.DEFAULT_PROFILES) for that question,
    e.g. to test a specific plan/segment.

No pass/fail logic here — judging is a reading task, done after this script
returns (same philosophy as run_tests.py).
"""
import json
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "kb-sync", "scripts"))
from kb_api import agent_id  # noqa: E402

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import sim_client as sc  # noqa: E402


def normalize(raw):
    items = []
    for i, item in enumerate(raw, 1):
        if isinstance(item, str):
            items.append({"id": f"Q{i}", "turns": [item]})
        elif "turns" in item:
            items.append({"id": item.get("id", f"Q{i}"), "turns": item["turns"], "profile": item.get("profile")})
        else:
            items.append({"id": item.get("id", f"Q{i}"), "turns": [item["question"]], "profile": item.get("profile")})
    return items


def run_one(base, token, app, agent, item):
    session_id = sc.new_session_id(app)
    profile = {**sc.DEFAULT_PROFILES.get(agent, {"agentId": agent}), **(item.get("profile") or {})}
    turn_results = []
    try:
        sc.create_session(base, token, session_id, profile)
        for turn_text in item["turns"]:
            result = sc.send_message(base, token, session_id, turn_text)
            turn_results.append({
                "question": turn_text,
                "reply": sc.last_reply_text(result),
                "status": result.get("status"),
                "suppress_reason": result.get("suppressReason"),
                "timed_out": result.get("timedOut"),
            })
        return {
            "id": item["id"],
            "turns": turn_results,
            "final_reply": turn_results[-1]["reply"] if turn_results else "",
            "error": None,
        }
    except Exception as e:
        return {"id": item["id"], "turns": turn_results, "final_reply": None, "error": str(e)}
    finally:
        sc.delete_session(base, token, session_id)


def main():
    if len(sys.argv) < 3:
        sys.exit("usage: run_tests_sim.py <app> <questions.json> [output.json]")

    app = sys.argv[1]
    questions_path = sys.argv[2]
    output_path = sys.argv[3] if len(sys.argv) > 3 else None

    with open(questions_path) as f:
        raw = json.load(f)
    items = normalize(raw)

    base, token = sc.load_sim_creds()
    sc.ensure_sim_up(base)
    agent = agent_id(app)

    results = []
    for item in items:
        results.append(run_one(base, token, app, agent, item))
        print(f"  [{item['id']}] done", file=sys.stderr)

    out = {"app": app, "agent": agent, "mode": "sim", "results": results}
    text = json.dumps(out, ensure_ascii=False, indent=2)

    if output_path:
        with open(output_path, "w") as f:
            f.write(text)
        print(f"Wrote {len(results)} result(s) to {output_path}", file=sys.stderr)
    else:
        print(text)


if __name__ == "__main__":
    main()
