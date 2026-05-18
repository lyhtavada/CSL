#!/usr/bin/env python3
"""
Fetch tickets từ Avada Ticket API cho tuần vừa rồi và fill vào weekly report.

Usage: python3 scan-weekly-issues.py [--week YYYY-MM-DD] [--dry-run]
  --week: any date in the target week (defaults to last week Mon-Sun)
"""

import argparse
import datetime
import os
import re
import sys
from collections import defaultdict
from pathlib import Path

import requests
from dotenv import load_dotenv

load_dotenv(Path(__file__).parent.parent.parent / ".env")

# ── Config ─────────────────────────────────────────────────────────────────
API_KEY = os.environ["AVD_TICKET_API_KEY"]
BASE_URL = "https://avada-ts-a9cb0.web.app/api/external"
HEADERS = {"X-API-Key": API_KEY}
APPS = ["Chatty", "JOY Loyalty"]
TZ7 = datetime.timezone(datetime.timedelta(hours=7))
REPORTS_DIR = Path(__file__).parent.parent / "weekly"


# ── Date helpers ────────────────────────────────────────────────────────────
def get_week_range(ref_date: datetime.date):
    monday = ref_date - datetime.timedelta(days=ref_date.weekday())
    sunday = monday + datetime.timedelta(days=6)
    return monday, sunday


# ── Ticket fetcher ──────────────────────────────────────────────────────────
def fetch_tickets(start_date: datetime.date, end_date: datetime.date, app_name: str) -> list:
    params = {
        "startDate": start_date.isoformat(),
        "endDate": end_date.isoformat(),
        "appName": app_name,
    }
    r = requests.get(f"{BASE_URL}/tickets/by-date", headers=HEADERS, params=params)
    data = r.json()
    if not data.get("success"):
        print(f"  API error ({app_name}): {data.get('error', {}).get('message')}", file=sys.stderr)
        return []
    tickets = data.get("data", {}).get("tickets", [])
    return tickets


# ── Classifier ──────────────────────────────────────────────────────────────
def classify_category(subject: str, description: str, ts_status: str) -> str:
    t = (subject + " " + description[:300]).lower()
    if any(w in t for w in ["ai ", "bot ", "trả lời", "response", "reply", "knowledge", "source", "accuracy", "duplicate", "ngôn ngữ", "language", "ai response", "ai không", "ai not"]):
        return "AI accuracy/quality"
    if any(w in t for w in ["sync", "product sync", "pending", "training data", "train", "data source"]):
        return "Sync / training data"
    if any(w in t for w in ["proactive", "campaign", "pop-up", "popup", "widget", "display", "hiển thị", "không hiện", "ko hiện", "not show", "invisible", "không hiển thị", "v4", "storefront"]):
        return "Widget / display issue"
    if any(w in t for w in ["point", "điểm", "earn", "reward", "redeem", "tier", "vip", "membership", "cộng điểm", "trừ điểm", "loyalty"]):
        return "Points / rewards / tier"
    if any(w in t for w in ["billing", "plan", "refund", "charge", "payment", "usage fee", "invoice", "trial", "upgrade", "downgrade"]):
        return "Billing / plan"
    if any(w in t for w in ["integrat", "connect", "recharge", "klaviyo", "shopify flow", "flow", "webhook", "api key", "invalid api"]):
        return "Integration / automation"
    if any(w in t for w in ["feature", "request", "custom", "css", "design", "layout", "block", "muốn có", "muốn thêm"]):
        return "Feature request / customization"
    if any(w in t for w in ["email", "smtp", "forward", "mail", "dmarc", "spf", "dkim", "notification"]):
        return "Email / notification"
    if any(w in t for w in ["404", "error", "bug", "lỗi", "crash", "broken", "not work", "ko load", "không load", "bị lỗi"]) or ts_status == "dev_fixing":
        return "Bug / error"
    return "Other"


# ── Analyzer ────────────────────────────────────────────────────────────────
EXCLUDE_STATUSES = {"sale_request", "billing", "feature_request"}

def analyze(tickets: list) -> list:
    groups = defaultdict(list)
    for t in tickets:
        ts_status = t.get("tsStatus", "")
        if ts_status in EXCLUDE_STATUSES:
            continue
        subject = t.get("subject", "")
        description = t.get("description") or ""
        ticket_id = t.get("ticketId", "")
        cat = classify_category(subject, description, ts_status)
        groups[cat].append({"subject": subject, "ticketId": ticket_id, "tsStatus": ts_status})

    result = []
    for cat, items in groups.items():
        overdue = sum(1 for i in items if i["tsStatus"] in ("dev_fixing", "waiting_customer", "sale_request", "feature_request"))
        result.append({
            "category": cat,
            "count": len(items),
            "overdue": overdue,
            "examples": [i["ticketId"] for i in items[:3]],
        })
    result.sort(key=lambda x: (x["category"] == "Other", -x["count"]))
    return result


# ── Formatter ───────────────────────────────────────────────────────────────
# Tên tính năng liên quan của từng category
CATEGORY_FEATURE = {
    "AI accuracy/quality":             "AI Agent / Knowledge base",
    "Sync / training data":            "AI Training / Product sync",
    "Widget / display issue":          "Widget / Storefront display",
    "Points / rewards / tier":         "Points & Rewards / VIP Tier",
    "Bug / error":                     "App core",
    "Integration / automation":        "Integrations / Shopify Flow",
    "Billing / plan":                  "Billing / Plan management",
    "Feature request / customization": "Customization / Theme",
    "Email / notification":            "Email / Notifications",
    "Other":                           "",
}

def format_top_issues(issues: list, app: str, total: int) -> str:
    lines = [f"**{app}** ({total} tickets)"]
    if not issues:
        lines.append("_(Không có issues được report tuần này)_")
        return "\n".join(lines)

    for i, issue in enumerate(issues[:3], 1):
        cat = issue["category"]
        count = issue["count"]
        feature = CATEGORY_FEATURE.get(cat, "")
        line = f"{i}. **{cat}** — {count} cases"
        if feature:
            line += f" _({feature})_"
        lines.append(line)

    return "\n".join(lines)


# ── Report filler ────────────────────────────────────────────────────────────
def fill_report(report_path: Path, chatty_md: str, joy_md: str):
    content = report_path.read_text()
    block = f"\n{chatty_md}\n\n{joy_md}\n"
    pattern = r"(## Top Issues tuần này\n)(.*?)(---\n## Bad Reviews)"
    replacement = rf"\1{block}\n---\n## Bad Reviews"
    new_content = re.sub(pattern, replacement, content, flags=re.DOTALL)
    if new_content == content:
        new_content = content.replace(
            "## Top Issues tuần này\n",
            f"## Top Issues tuần này\n\n{block}\n"
        )
    report_path.write_text(new_content)
    print(f"Filled: {report_path}")


# ── Main ─────────────────────────────────────────────────────────────────────
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--week", help="Any date in target week (YYYY-MM-DD). Default: last week.")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    if args.week:
        ref = datetime.date.fromisoformat(args.week)
    else:
        ref = datetime.date.today() - datetime.timedelta(days=7)

    monday, sunday = get_week_range(ref)
    print(f"Fetching tickets: {monday} → {sunday}")

    results = {}
    totals = {}
    for app in APPS:
        print(f"  {app}...")
        tickets = fetch_tickets(monday, sunday, app)
        filtered = [t for t in tickets if t.get("tsStatus") not in EXCLUDE_STATUSES]
        print(f"    {len(tickets)} tickets fetched, {len(filtered)} after filter")
        totals[app] = len(filtered)
        results[app] = analyze(tickets)

    chatty_md = format_top_issues(results["Chatty"], "Chatty", totals["Chatty"])
    joy_md    = format_top_issues(results["JOY Loyalty"], "Joy", totals["JOY Loyalty"])

    week_label = f"{monday.strftime('%d/%m')}–{sunday.strftime('%d/%m/%Y')}"
    print(f"\n{'='*60}")
    print(f"Top Issues — {week_label}")
    print('='*60)
    print(chatty_md)
    print()
    print(joy_md)

    if not args.dry_run:
        reports = sorted(REPORTS_DIR.glob("weekly-CSL-report-*.md"), reverse=True)
        if reports:
            fill_report(reports[0], chatty_md, joy_md)
        else:
            print("No report file found. Run gen-weekly-report.sh first.", file=sys.stderr)
    else:
        print("\n[dry-run] Not writing to file.")


if __name__ == "__main__":
    main()
