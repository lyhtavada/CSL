#!/usr/bin/env python3
"""
generate_program_sheet.py — create a Google Sheet loyalty program proposal
(4 tabs: Points Program / VIP Membership / Referral Program / Milestones & Quest).

Usage:
  .venv-crisp/bin/python skills/build-loyalty-program/scripts/generate_program_sheet.py \
      --account "Acme Skincare" [--data path/to/data.json] [--share someone@avada.io]

Prints the spreadsheet URL on success. Data schema matches the placeholder
structure below — pass --data to fill real numbers, or edit the sheet
directly afterward (values().update / batchUpdate) with real figures.

Auth: uses gapi.client.sheets() (and drive() if --share is passed), authed
as lyht@avada.io per gapi/auth_setup.py. The created sheet is owned by that
account and shows up in its Drive automatically.
"""
import argparse
import json
import os
import sys

ROOT = os.path.expanduser("~/CSL")
sys.path.insert(0, ROOT)

from gapi.client import sheets as gsheets, drive as gdrive  # noqa: E402

BRAND_PURPLE = {"red": 0.424, "green": 0.361, "blue": 0.902}  # #6C5CE7
WHITE = {"red": 1, "green": 1, "blue": 1}

TAB_POINTS = "Points Program"
TAB_VIP = "VIP Membership"
TAB_REFERRAL = "Referral Program"
TAB_MILESTONES = "Milestones & Quest"
TABS = [TAB_POINTS, TAB_VIP, TAB_REFERRAL, TAB_MILESTONES]


def default_data():
    return {
        "point_valuation": {
            "point_value": "1 pt = $0.01",
            "earning_rate": "X pts per $1",
            "purchases_to_reward": "~2-3 orders",
            "liability_estimate": "TBD",
        },
        "earning_rules": [["Purchase", "$1 spent", "TBD", ""]],
        "redemption_rules": [["First reward", "% off", "TBD", "TBD", "TBD", ""]],
        "paid_membership": False,
        "tiers": [
            ["Tier 1", "0", "1x", "Welcome bonus", "TBD"],
            ["Tier 2", "3-5 purchases", "1.25x", "TBD", "TBD"],
            ["Tier 3", "8-12 purchases", "1.5x", "TBD", "TBD"],
            ["Tier 4 (VIP)", "15-20+ purchases", "2x", "TBD", "TBD"],
        ],
        "demotion_policy": "TBD",
        "referral": [
            ["Referrer Reward", "TBD (≈1 purchase worth of points)", ""],
            ["Referee Reward", "10-20% off or $10-15 off", ""],
            ["Min Purchase", "At or slightly above AOV", ""],
            ["Sharing Channels", "Email, SMS, social", ""],
            ["Anti-Cheat Settings", "TBD", ""],
            ["Referral Message Template", "TBD", ""],
        ],
        "milestones": [["First order", "Order count", "1", "TBD", "TBD"]],
        "quest": [[1, "TBD", "TBD", "TBD", "TBD"]],
    }


def sheet_id_map(spreadsheet):
    return {s["properties"]["title"]: s["properties"]["sheetId"] for s in spreadsheet["sheets"]}


def header_format_request(sheet_id, row_index, ncols):
    return {
        "repeatCell": {
            "range": {
                "sheetId": sheet_id,
                "startRowIndex": row_index,
                "endRowIndex": row_index + 1,
                "startColumnIndex": 0,
                "endColumnIndex": ncols,
            },
            "cell": {
                "userEnteredFormat": {
                    "backgroundColor": BRAND_PURPLE,
                    "textFormat": {"bold": True, "foregroundColor": WHITE},
                }
            },
            "fields": "userEnteredFormat(backgroundColor,textFormat)",
        }
    }


def autoresize_request(sheet_id, ncols):
    return {
        "autoResizeDimensions": {
            "dimensions": {
                "sheetId": sheet_id,
                "dimension": "COLUMNS",
                "startIndex": 0,
                "endIndex": ncols,
            }
        }
    }


def build(account, data, share_email):
    svc = gsheets()

    spreadsheet = (
        svc.spreadsheets()
        .create(
            body={
                "properties": {"title": f"{account} — Joy Loyalty Program Proposal"},
                "sheets": [{"properties": {"title": t}} for t in TABS],
            }
        )
        .execute()
    )
    spreadsheet_id = spreadsheet["spreadsheetId"]
    sheet_ids = sheet_id_map(spreadsheet)

    value_updates = []
    format_requests = []
    max_cols = {}

    # --- Tab 1: Points Program ---
    pv = data.get("point_valuation", {})
    rows = [
        ["Point Valuation"],
        ["Point value", pv.get("point_value", "")],
        ["Earning rate", pv.get("earning_rate", "")],
        ["Purchases to first reward", pv.get("purchases_to_reward", "")],
        ["Annual point liability estimate", pv.get("liability_estimate", "")],
        [],
        ["Earning Rules"],
    ]
    earning_header_row = len(rows)
    rows.append(["Rule Name", "Action", "Points Earned", "Notes/Details"])
    rows.extend(data.get("earning_rules", []))
    rows.append([])
    rows.append(["Redemption Rules"])
    redemption_header_row = len(rows)
    rows.append(["Reward Name", "Type", "Points Required", "Discount Value", "Min Order", "Notes"])
    rows.extend(data.get("redemption_rules", []))
    rows.append(["Designed by Joy Loyalty"])

    value_updates.append({"range": f"'{TAB_POINTS}'!A1", "values": rows})
    format_requests.append(header_format_request(sheet_ids[TAB_POINTS], earning_header_row, 4))
    format_requests.append(header_format_request(sheet_ids[TAB_POINTS], redemption_header_row, 6))
    max_cols[TAB_POINTS] = 6

    # --- Tab 2: VIP Membership ---
    is_paid = data.get("paid_membership", False)
    tier_header = (
        ["Tier Name", "Subscription Trigger", "Earning Multiplier", "Entry Reward", "Perks/Benefits"]
        if is_paid
        else ["Tier Name", "Threshold (pts/$/orders)", "Earning Multiplier", "Entry Reward", "Perks/Benefits"]
    )
    rows2 = [tier_header]
    rows2.extend(data.get("tiers", []))
    rows2.append([])
    rows2.append(["Demotion policy", data.get("demotion_policy", "")])
    rows2.append(["Designed by Joy Loyalty"])

    value_updates.append({"range": f"'{TAB_VIP}'!A1", "values": rows2})
    format_requests.append(header_format_request(sheet_ids[TAB_VIP], 0, 5))
    max_cols[TAB_VIP] = 5

    # --- Tab 3: Referral Program ---
    rows3 = [["Element", "Configuration", "Notes"]]
    rows3.extend(data.get("referral", []))
    rows3.append(["Designed by Joy Loyalty"])

    value_updates.append({"range": f"'{TAB_REFERRAL}'!A1", "values": rows3})
    format_requests.append(header_format_request(sheet_ids[TAB_REFERRAL], 0, 3))
    max_cols[TAB_REFERRAL] = 3

    # --- Tab 4: Milestones & Quest ---
    rows4 = [["Individual Milestones"]]
    milestone_header_row = len(rows4)
    rows4.append(["Milestone Name", "Type", "Target", "Reward", "Customer Message"])
    rows4.extend(data.get("milestones", []))
    rows4.append([])
    rows4.append(["Quest Journey"])
    quest_header_row = len(rows4)
    rows4.append(["Step #", "Action", "Target", "Reward", "Description"])
    rows4.extend(data.get("quest", []))
    rows4.append(["Designed by Joy Loyalty"])

    value_updates.append({"range": f"'{TAB_MILESTONES}'!A1", "values": rows4})
    format_requests.append(header_format_request(sheet_ids[TAB_MILESTONES], milestone_header_row, 5))
    format_requests.append(header_format_request(sheet_ids[TAB_MILESTONES], quest_header_row, 5))
    max_cols[TAB_MILESTONES] = 5

    svc.spreadsheets().values().batchUpdate(
        spreadsheetId=spreadsheet_id,
        body={"valueInputOption": "USER_ENTERED", "data": value_updates},
    ).execute()

    for tab, ncols in max_cols.items():
        format_requests.append(autoresize_request(sheet_ids[tab], ncols))

    svc.spreadsheets().batchUpdate(
        spreadsheetId=spreadsheet_id, body={"requests": format_requests}
    ).execute()

    if share_email:
        gdrive().permissions().create(
            fileId=spreadsheet_id,
            body={"type": "user", "role": "writer", "emailAddress": share_email},
            sendNotificationEmail=False,
        ).execute()

    return spreadsheet["spreadsheetUrl"]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--account", required=True)
    ap.add_argument("--data", help="path to JSON matching the schema (optional; placeholders used otherwise)")
    ap.add_argument("--share", help="optional email to share the sheet with (drive.file scope, writer role)")
    args = ap.parse_args()

    data = default_data()
    if args.data:
        with open(args.data) as f:
            data.update(json.load(f))

    url = build(args.account, data, args.share)
    print(f"Saved {url}")


if __name__ == "__main__":
    main()
