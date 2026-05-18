#!/usr/bin/env python3
"""
Fetch Crisp conversations với segment app_chatty/app_faqs trong N ngày qua,
lấy first user message của mỗi conversation, cluster thành FAQ patterns.

Usage:
  python3 fetch-chatty-faq.py              # 7 ngày mặc định
  python3 fetch-chatty-faq.py --days 14    # 14 ngày
  python3 fetch-chatty-faq.py --dry-run    # Chỉ count, không fetch messages
"""

import argparse
import datetime
import json
import time
import sys
from collections import Counter, defaultdict
from pathlib import Path

import requests

# ── Config ─────────────────────────────────────────────────────────────────
CRISP_API = "https://api.crisp.chat/v1"
WEBSITE_ID = "72a663b0-4cda-4e3b-8878-426bdd79364c"
API_KEY    = "60053ee7-54a7-4426-b0c7-66fc7eadee5a"
API_SECRET = "72f3cd4146cea1ac60ab5164f5e143fc35e3bd6280313fb961527067f92c5e31"
AUTH       = (API_KEY, API_SECRET)
HEADERS    = {"X-Crisp-Tier": "plugin"}
TARGET_SEGMENTS = {"app_chatty", "app_faqs"}
DELAY = 0.25  # seconds between requests

TZ7 = datetime.timezone(datetime.timedelta(hours=7))
REPORTS_DIR = Path(__file__).parent


# ── Crisp API helpers ────────────────────────────────────────────────────────
def get_conversations_page(page: int) -> list:
    r = requests.get(
        f"{CRISP_API}/website/{WEBSITE_ID}/conversations/{page}",
        auth=AUTH, headers=HEADERS
    )
    r.raise_for_status()
    return r.json().get("data", [])

def get_first_user_message(session_id: str):
    r = requests.get(
        f"{CRISP_API}/website/{WEBSITE_ID}/conversation/{session_id}/messages",
        auth=AUTH, headers=HEADERS
    )
    if r.status_code != 200:
        return None
    msgs = r.json().get("data", [])
    for m in msgs:
        if m.get("from") == "user" and m.get("type") == "text":
            content = m.get("content", "").strip()
            if len(content) > 3:  # skip "hi", "ok", etc.
                return content
    return None


# ── Clustering helpers ────────────────────────────────────────────────────────
# Simple keyword-based topic grouping
TOPICS = {
    "Billing / plan / pricing":   ["billing", "charge", "plan", "price", "refund", "invoice", "subscription", "payment", "upgrade", "downgrade", "cancel", "cost", "fee", "thanh toán", "hoàn tiền", "nâng cấp", "hủy"],
    "AI / chatbot not working":   ["ai ", "bot", "chatbot", "answer", "response", "wrong", "incorrect", "training", "knowledge", "faq", "trả lời", "sai", "không trả lời", "không phản hồi"],
    "Email / inbox issues":       ["email", "inbox", "forward", "smtp", "mail", "notification", "hộp thư", "chuyển tiếp"],
    "Widget / UI display":        ["widget", "display", "show", "hide", "button", "color", "style", "layout", "css", "appear", "hiển thị", "ẩn", "màu sắc", "nút"],
    "Setup / onboarding":         ["setup", "install", "config", "how to", "tutorial", "start", "begin", "cài đặt", "thiết lập", "hướng dẫn", "bắt đầu"],
    "Integration":                ["integration", "connect", "sync", "klaviyo", "shopify", "app", "webhook", "api", "tích hợp", "kết nối", "đồng bộ"],
    "Human handover / agent":     ["human", "agent", "handover", "live", "operator", "staff", "assign", "chuyển", "người thật", "nhân viên"],
    "Translation / language":     ["language", "translate", "translation", "multilingual", "ngôn ngữ", "dịch"],
    "Performance / bug":          ["slow", "lag", "bug", "error", "broken", "not working", "crash", "chậm", "lỗi", "không hoạt động"],
    "Feature request":            ["feature", "request", "wish", "can you", "possible", "yêu cầu", "tính năng", "có thể"],
}

def classify_message(text: str) -> str:
    text_lower = text.lower()
    for topic, keywords in TOPICS.items():
        if any(kw in text_lower for kw in keywords):
            return topic
    return "Other / General"


# ── Main ─────────────────────────────────────────────────────────────────────
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--days", type=int, default=7, help="Number of days to look back")
    parser.add_argument("--dry-run", action="store_true", help="Count only, skip message fetch")
    parser.add_argument("--output", help="Save results to JSON file")
    args = parser.parse_args()

    cutoff = datetime.datetime.now(tz=datetime.timezone.utc) - datetime.timedelta(days=args.days)
    print(f"Fetching Chatty conversations since {cutoff.astimezone(TZ7).strftime('%d/%m/%Y %H:%M')} GMT+7")
    print(f"Segments: {TARGET_SEGMENTS}\n")

    # ── Step 1: Paginate conversation list ────────────────────────────────
    target_sessions = []
    page = 1
    while True:
        print(f"  Page {page}...", end=" ", flush=True)
        convs = get_conversations_page(page)
        if not convs:
            print("empty — done")
            break

        in_range = 0
        matched = 0
        for c in convs:
            updated_ms = c.get("updated_at", 0)
            updated_dt = datetime.datetime.fromtimestamp(updated_ms / 1000, tz=datetime.timezone.utc)
            if updated_dt < cutoff:
                continue
            in_range += 1
            segments = set(c.get("meta", {}).get("segments", []))
            if segments & TARGET_SEGMENTS:
                matched += 1
                target_sessions.append({
                    "session_id": c["session_id"],
                    "updated_at": updated_dt.astimezone(TZ7).strftime("%Y-%m-%d %H:%M"),
                    "segments": list(segments),
                    "merchant": c.get("meta", {}).get("nickname", ""),
                    "email": c.get("meta", {}).get("email", ""),
                })

        print(f"{in_range} in range, {matched} matched segment")

        # If all convs on this page are older than cutoff, we're done
        oldest_ts = convs[-1].get("updated_at", 0)
        oldest_dt = datetime.datetime.fromtimestamp(oldest_ts / 1000, tz=datetime.timezone.utc)
        if oldest_dt < cutoff:
            print(f"  Reached cutoff at page {page} — stopping")
            break

        page += 1
        time.sleep(DELAY)

    print(f"\nTotal matched Chatty conversations: {len(target_sessions)}")

    if args.dry_run:
        print("[dry-run] Skipping message fetch.")
        return

    # ── Step 2: Fetch first user message ─────────────────────────────────
    print(f"\nFetching first messages ({len(target_sessions)} conversations)...")
    results = []
    for i, conv in enumerate(target_sessions, 1):
        sid = conv["session_id"]
        print(f"  [{i}/{len(target_sessions)}] {sid[:16]}...", end=" ", flush=True)
        msg = get_first_user_message(sid)
        if msg:
            topic = classify_message(msg)
            print(f"✓ [{topic[:20]}] {msg[:60]}")
        else:
            topic = "No message"
            print("(no user message)")
        results.append({**conv, "first_message": msg, "topic": topic})
        time.sleep(DELAY)

    # ── Step 3: Aggregate ─────────────────────────────────────────────────
    print("\n" + "="*60)
    week_label = f"{(datetime.datetime.now() - datetime.timedelta(days=args.days)).strftime('%d/%m')}–{datetime.datetime.now().strftime('%d/%m/%Y')}"
    print(f"FAQ Analysis — Chatty — {week_label}")
    print("="*60)

    topic_counter = Counter(r["topic"] for r in results if r.get("first_message"))
    print(f"\nTop Topics ({sum(topic_counter.values())} conversations analyzed):\n")
    for topic, count in topic_counter.most_common():
        pct = count / max(sum(topic_counter.values()), 1) * 100
        bar = "█" * int(pct / 5)
        print(f"  {count:3d}  {pct:5.1f}%  {bar:<20}  {topic}")

    # Top questions per topic
    print(f"\n--- Sample Questions by Topic ---")
    by_topic = defaultdict(list)
    for r in results:
        if r.get("first_message") and r["topic"] != "No message":
            by_topic[r["topic"]].append(r["first_message"])

    for topic, msgs in sorted(by_topic.items(), key=lambda x: -len(x[1])):
        print(f"\n[{topic}] — {len(msgs)} cases")
        for m in msgs[:3]:
            print(f"  • {m[:120]}")

    # ── Step 4: Save ──────────────────────────────────────────────────────
    out_path = args.output or str(REPORTS_DIR / f"chatty-faq-{datetime.date.today()}.json")
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump({
            "generated_at": datetime.datetime.now(TZ7).isoformat(),
            "days": args.days,
            "total_conversations": len(results),
            "topic_summary": dict(topic_counter.most_common()),
            "conversations": results,
        }, f, ensure_ascii=False, indent=2)
    print(f"\nSaved: {out_path}")


if __name__ == "__main__":
    main()
