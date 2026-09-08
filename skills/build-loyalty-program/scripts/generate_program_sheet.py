#!/usr/bin/env python3
"""
generate_program_sheet.py — create a Google Sheet loyalty program proposal
using Liz's standard build template (6 tabs: Setup, Earning, Redemption,
VIP, Referral, Launch & Bootstrap).

Usage:
  .venv-crisp/bin/python skills/build-loyalty-program/scripts/generate_program_sheet.py \
      --account "Acme Skincare" [--data path/to/data.json] [--share someone@avada.io]

Prints the spreadsheet URL on success. Pass --data with a JSON file matching
the flat key schema in `default_data()` to pre-fill the Value cells with real
numbers — otherwise the sheet is created blank (Value cells empty, pink) for
Liz to fill in directly or hand to the account.

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

DARK = {"red": 0.10980392, "green": 0.05490196, "blue": 0.07058824}
RED = {"red": 0.8980392, "green": 0.22352941, "blue": 0.20784314}
WHITE = {"red": 1, "green": 1, "blue": 1}
PINK = {"red": 0.9882353, "green": 0.88235295, "blue": 0.87058824}
STATUS_COLOR = {"red": 0.85, "green": 0.92, "blue": 0.98}

STATUS_OPTIONS = ["Not started", "In progress", "Live", "Skipped"]
STATUS_DEFAULT = "Not started"

TAB_SETUP = "Setup"
TAB_EARNING = "Earning"
TAB_REDEMPTION = "Redemption"
TAB_VIP = "VIP"
TAB_REFERRAL = "Referral"
TAB_MILESTONE = "Milestone"
TAB_LAUNCH = "Launch & Bootstrap"
TABS = [TAB_SETUP, TAB_EARNING, TAB_REDEMPTION, TAB_VIP, TAB_REFERRAL, TAB_MILESTONE, TAB_LAUNCH]

FILL_NOTE = "Fill in the Value column (red cells). Suggested / Preset are defaults — adjust as needed."
PLUS_ROW = "➕  Add your own — fill in the blank rows below"


def default_data():
    """Flat key -> value. Every key here maps to one editable Value cell.
    Leave a key out (or empty string) to keep that cell blank in the sheet."""
    return {
        # Setup
        "store_domain": "", "app_plan": "Advanced/ Ultimate", "industry": "",
        "program_goal": "", "desired_cashback_rate": "", "aov": "",
        "target_launch_date": "", "used_loyalty_before": "", "migrating": "",
        "program_name": "", "point_currency_name": "", "point_value": "",
        "base_earn_rate": "", "point_expiry": "", "coupon_expiry": "",
        "integ_email_sms": "", "integ_reviews": "", "integ_pos": "",
        "integ_flow": "", "integ_subscriptions": "",
        "migration_data": "", "migration_date": "",
        # Earning
        "earn_purchase": "", "earn_welcome": "", "earn_newsletter": "",
        "earn_birthday": "", "earn_review": "", "earn_review_media": "",
        "earn_google_review": "", "earn_ig": "", "earn_tiktok": "",
        "earn_social_share": "",
        "earn_birthday_tier1": "", "earn_birthday_tier2": "", "earn_birthday_tier3": "",
        # Redemption
        "redeem_min_points": "", "redeem_coupon_expiry": "",
        "discount_fixed1_cost": "", "discount_fixed1_min": "", "discount_fixed1_combo": "",
        "discount_fixed2_cost": "", "discount_fixed2_min": "", "discount_fixed2_combo": "",
        "discount_pct_cost": "", "discount_pct_min": "", "discount_pct_combo": "",
        "gift_product": "", "gift_cost": "", "gift_min": "", "gift_combo": "",
        "shipping_cost": "", "shipping_min": "", "shipping_combo": "",
        # VIP
        "vip_calc_by": "", "vip_eval_window": "", "vip_multiplier_applies": "",
        "vip_reeval_cycle": "",
        "tier1_condition": "", "tier1_multiplier": "", "tier1_entry": "",
        "tier1_entry_combo": "", "tier1_perk": "", "tier1_perk_combo": "",
        "tier2_condition": "", "tier2_multiplier": "", "tier2_entry": "",
        "tier2_entry_combo": "", "tier2_perk": "", "tier2_perk_combo": "",
        "tier3_condition": "", "tier3_multiplier": "", "tier3_entry": "",
        "tier3_entry_combo": "", "tier3_perk": "", "tier3_perk_combo": "",
        # Referral
        "referrer_gets": "", "referred_gets": "", "referral_condition": "",
        "referral_by_tier": "", "referral_banner": "",
        "referral_tier1": "", "referral_tier2": "", "referral_tier3": "",
        # Milestone
        "milestone_first_order_target": "", "milestone_first_order_reward": "",
        "milestone_loyal_target": "", "milestone_loyal_reward": "",
        "milestone_big_spender_target": "", "milestone_big_spender_reward": "",
        "milestone_anniversary_target": "", "milestone_anniversary_reward": "",
        # Launch & Bootstrap
        "launch_widget": "", "launch_terms_page": "", "launch_email_templates": "",
        "launch_staff_training": "", "launch_faq_doc": "",
        "bootstrap_soft_launch_group": "", "bootstrap_signup_bonus": "",
        "bootstrap_retroactive_points": "", "bootstrap_migration": "", "bootstrap_promo": "",
        "public_launch_date": "", "public_announcement_channels": "", "public_launch_owner": "",
        "monitor_redemption_target": "", "monitor_liability_checkin": "", "monitor_winback_email": "",
    }


class TabBuilder:
    """Accumulates rows + tracks which row/col indices need which format,
    so formatting stays in sync with content without hardcoded row numbers."""

    def __init__(self, status_default=True):
        self.rows = []
        self.title_idx = None
        self.note_idxs = []
        self.section_idxs = []
        self.colheader_idxs = {}  # row_idx -> ncols
        self.editable = []  # (row_idx, col_idx)
        self.status_cells = []  # (row_idx, col_idx)
        self.max_cols = 1
        self.status_default = status_default
        self._content_width = 0  # column count of the current section, excluding Status

    def title(self, text):
        self.title_idx = len(self.rows)
        self.rows.append([text])
        self.max_cols = max(self.max_cols, 1)

    def note(self, text):
        self.note_idxs.append(len(self.rows))
        self.rows.append([text])

    def blank(self):
        self.rows.append([])

    def section(self, text):
        self.section_idxs.append(len(self.rows))
        self.rows.append([text])

    def colheader(self, cols, status=None):
        show_status = self.status_default if status is None else status
        self._content_width = len(cols)
        full_cols = list(cols) + (["Status"] if show_status else [])
        self.colheader_idxs[len(self.rows)] = len(full_cols)
        self.rows.append(full_cols)
        self.max_cols = max(self.max_cols, len(full_cols))

    def data(self, row_values, editable_cols=(), status=None):
        show_status = self.status_default if status is None else status
        values = list(row_values)
        idx = len(self.rows)
        if show_status:
            # pad to the current section's content width so Status always
            # lands in its own column, even when trailing reference cells
            # (Suggested/Note) are omitted for this row
            while len(values) < self._content_width:
                values.append("")
            self.status_cells.append((idx, len(values)))
            values.append(STATUS_DEFAULT)
        self.rows.append(values)
        for c in editable_cols:
            self.editable.append((idx, c))
        self.max_cols = max(self.max_cols, len(values))

    def plus(self):
        self.rows.append([PLUS_ROW])


def build_setup(d):
    t = TabBuilder(status_default=False)
    t.title("Program Setup")
    t.note(FILL_NOTE)
    t.blank()
    t.section("STORE INFO")
    t.colheader(["Item", "Value", "Notes"])
    t.data(["Store / domain", d.get("store_domain", "")], [1])
    t.data(["App plan", d.get("app_plan", "")], [1])
    t.data(["Industry", d.get("industry", "")], [1])
    t.data(["Program goal", d.get("program_goal", ""), "e.g. retention/ higher AOV/ repeat purchase"], [1])
    t.data(["Desired cashback rate", d.get("desired_cashback_rate", ""), "e.g. ~5% (point value x earn rate)"], [1])
    t.data(["AOV (avg order value)", d.get("aov", "")], [1])
    t.data(["Target launch date", d.get("target_launch_date", "")], [1])
    t.data(["Used a loyalty app before?", d.get("used_loyalty_before", ""), "app name / no"], [1])
    t.data(["Migrating?", d.get("migrating", ""), "yes → old app / no"], [1])
    t.blank()
    t.section("PROGRAM CONFIG")
    t.colheader(["Item", "Value", "Suggested / Preset", "Notes"])
    t.data(["Program name", d.get("program_name", ""), "\"[Brand] Club\" / \"[Brand] Rewards\""], [1])
    t.data(["Point currency name", d.get("point_currency_name", ""), "\"[Brand] Points\" (e.g. Koko Points)", "branded currency = feels owned"], [1])
    t.data(["Point value", d.get("point_value", ""), "1 pt = $0.01", "~5% rebate rate"], [1])
    t.data(["Base earn rate", d.get("base_earn_rate", ""), "1 pt / $1 spent", "tier multipliers added in VIP tab"], [1])
    t.data(["Point expiry", d.get("point_expiry", ""), "12 months inactivity", "win-back email before expiry"], [1])
    t.data(["Coupon expiry", d.get("coupon_expiry", ""), "45 days from issue", "gives customers time to use"], [1])
    t.blank()
    t.section("APP INTEGRATIONS")
    t.colheader(["Item", "Value", "Suggested / Preset", "Notes"])
    t.data(["Email / SMS", d.get("integ_email_sms", ""), "Klaviyo / Omnisend — sync points & tier", "reward + win-back emails"], [1])
    t.data(["Reviews", d.get("integ_reviews", ""), "Judge.me / Loox / Yotpo — points for reviews", "links to Earning tab"], [1])
    t.data(["Shopify POS", d.get("integ_pos", ""), "earn & redeem in-store", "omnichannel"], [1])
    t.data(["Shopify Flow", d.get("integ_flow", ""), "custom triggers (e.g. social share)", "used in Earning tab"], [1])
    t.data(["Subscriptions", d.get("integ_subscriptions", ""), "Recharge / Loop / Appstle — earn on recurring orders", "reward subscribers"], [1])
    t.plus()
    t.blank()
    t.blank()
    t.blank()
    t.blank()
    t.section("MIGRATION / IMPORT  (migrating only)")
    t.colheader(["Item", "Value", "Suggested / Preset", "Notes"])
    t.data(["Data to import", d.get("migration_data", ""), "points balance + tier + expiry", "export CSV from old app"], [1])
    t.data(["Import date", d.get("migration_date", ""), "before launch", "freeze old app after export"], [1])
    return t


def build_earning(d):
    t = TabBuilder()
    t.title("Earning (how customers earn points)")
    t.blank()
    t.colheader(["Rule", "Action (Joy)", "Points Earned", "Suggested / Preset", "Note"])
    t.data(["Purchase Reward", "Place Order", d.get("earn_purchase", ""), "1 pt / $1"], [2])
    t.data(["Welcome Bonus", "Sign-Up", d.get("earn_welcome", ""), "200 pts"], [2])
    t.data(["Newsletter Sign-Up", "Newsletter Sign-Up", d.get("earn_newsletter", ""), "50 pts"], [2])
    t.data(["Birthday Gift", "Birthday Reward", d.get("earn_birthday", ""), "200–300 pts"], [2])
    t.data(["Product Review", "Write Review", d.get("earn_review", ""), "50 pts"], [2])
    t.data(["Photo/Video Review", "Write Review (media)", d.get("earn_review_media", ""), "150 pts"], [2])
    t.data(["Google Review", "Google Reviews", d.get("earn_google_review", ""), "150 pts (limit 1/customer)"], [2])
    t.data(["Follow Instagram", "Social Activity", d.get("earn_ig", ""), "30 pts"], [2])
    t.data(["Follow TikTok", "Social Activity", d.get("earn_tiktok", ""), "30 pts"], [2])
    t.data(["Social Share", "Custom (Shopify Flow)", d.get("earn_social_share", ""), "100 pts"], [2])
    t.plus()
    t.blank()
    t.blank()
    t.blank()
    t.blank()
    t.section("BIRTHDAY REWARD (BY TIER - OPTIONAL)")
    t.colheader(["Tier", "Reward", "Value", "Suggested / Preset", "Note"])
    t.data(["Tier 1 (base)", "Points", d.get("earn_birthday_tier1", ""), "200 pts"], [2])
    t.data(["Tier 2", "Points + gift", d.get("earn_birthday_tier2", ""), "300 pts + birthday gift"], [2])
    t.data(["Tier 3", "Points + gift + perk", d.get("earn_birthday_tier3", ""), "300 pts + gift + free shipping"], [2])
    t.plus()
    return t


def build_redemption(d):
    t = TabBuilder()
    t.title("Redemption (how customers redeem points)")
    t.blank()
    t.section("GENERAL RULE")
    t.colheader(["General Rule", "Value", "Suggested"])
    t.data(["Min points to redeem", d.get("redeem_min_points", ""), "100 pts"], [1])
    t.data(["Coupon expiration", d.get("redeem_coupon_expiry", ""), "45 days from issue"], [1])
    t.blank()
    t.section("REWARDS — DISCOUNT (AMOUNT / PERCENTAGE)")
    t.colheader(["Reward", "Type", "Cost (Points)", "Min purchase amount", "Discount combination", "Suggested / Preset", "Note"])
    t.data(["Fixed amount off", "Amount off", d.get("discount_fixed1_cost", ""), d.get("discount_fixed1_min", ""), d.get("discount_fixed1_combo", ""), "100 pts = $5 off"], [2, 3, 4])
    t.data(["Fixed amount off", "Amount off", d.get("discount_fixed2_cost", ""), d.get("discount_fixed2_min", ""), d.get("discount_fixed2_combo", ""), "500 pts = $30 off"], [2, 3, 4])
    t.data(["Percentage off", "% off", d.get("discount_pct_cost", ""), d.get("discount_pct_min", ""), d.get("discount_pct_combo", ""), "500 pts = 10% off"], [2, 3, 4])
    t.plus()
    t.blank()
    t.blank()
    t.blank()
    t.blank()
    t.section("REWARDS — FREE GIFT")
    t.colheader(["Reward", "Product (names or links)", "Cost (Points)", "Min purchase amount", "Discount combination", "Suggested / Preset", "Note"])
    t.data(["Free product", d.get("gift_product", ""), d.get("gift_cost", ""), d.get("gift_min", ""), d.get("gift_combo", ""), "(store dependent)"], [1, 2, 3, 4])
    t.plus()
    t.blank()
    t.blank()
    t.blank()
    t.blank()
    t.section("REWARDS — FREE SHIPPING")
    t.colheader(["Reward", "Type", "Cost (Points)", "Min purchase amount", "Discount combination", "Suggested / Preset", "Note"])
    t.data(["Free shipping", "Free ship", d.get("shipping_cost", ""), d.get("shipping_min", ""), d.get("shipping_combo", ""), "300 pts"], [2, 3, 4])
    t.plus()
    return t


def build_vip(d):
    t = TabBuilder()
    t.title("VIP Membership (if tiers used)")
    t.blank()
    t.note("Skip if the program is simple. Example (Maison Koko): Sipper → Steeper → Master.")
    t.blank()
    t.section("TIER CONFIG")
    t.colheader(["Tier Config", "Value", "Suggested"])
    t.data(["Tier calculated by", d.get("vip_calc_by", ""), "Amount spent OR points earned — pick one"], [1])
    t.data(["Evaluation window", d.get("vip_eval_window", ""), "over 12 months"], [1])
    t.data(["Point earn multiplied by tier?", d.get("vip_multiplier_applies", ""), "Yes — applies to Purchase Reward points only (e.g. 1x / 1.5x / 2x)"], [1])
    t.data(["Re-evaluation cycle", d.get("vip_reeval_cycle", ""), "12 months"], [1])
    t.blank()
    t.section("TIERS")
    t.colheader(["Tier", "Condition to Reach", "Earn Multiplier (purchase only - optional) ", "Entry rewards", "Entry reward combo", "Perk", "Perk combo", "Suggested / Preset"])
    t.data(["Tier 1 (e.g. Silver / Sipper)", d.get("tier1_condition", ""), d.get("tier1_multiplier", ""), d.get("tier1_entry", ""), d.get("tier1_entry_combo", ""), d.get("tier1_perk", ""), d.get("tier1_perk_combo", ""), "1x — base earn"], [1, 2, 3, 4, 5, 6])
    t.data(["Tier 2 (e.g. Gold / Steeper)", d.get("tier2_condition", ""), d.get("tier2_multiplier", ""), d.get("tier2_entry", ""), d.get("tier2_entry_combo", ""), d.get("tier2_perk", ""), d.get("tier2_perk_combo", ""), "1.5x — +earn, birthday gift"], [1, 2, 3, 4, 5, 6])
    t.data(["Tier 3 (e.g. Platinum / Master)", d.get("tier3_condition", ""), d.get("tier3_multiplier", ""), d.get("tier3_entry", ""), d.get("tier3_entry_combo", ""), d.get("tier3_perk", ""), d.get("tier3_perk_combo", ""), "2x — early access, free shipping"], [1, 2, 3, 4, 5, 6])
    t.plus()
    return t


def build_referral(d):
    t = TabBuilder()
    t.title("Referral")
    t.blank()
    t.colheader(["Item", "Value", "Suggested / Preset"])
    t.data(["Referrer gets", d.get("referrer_gets", ""), "+200 pts after friend's first order"], [1])
    t.data(["Referred friend gets", d.get("referred_gets", ""), "$10 off first order"], [1])
    t.data(["Condition", d.get("referral_condition", ""), "min order $X"], [1])
    t.data(["Referral points multiplied by tier?", d.get("referral_by_tier", ""), "Yes / No — higher tiers get bigger reward"], [1])
    t.data(["Referral banner (widget)", d.get("referral_banner", ""), "on-brand image"], [1])
    t.plus()
    t.blank()
    t.blank()
    t.blank()
    t.blank()
    t.section("REFERRAL REWARD BY TIER (OPTIONAL)")
    t.colheader(["Tier", "Referrer gets", "Suggested"])
    t.data(["Tier 1 (base)", d.get("referral_tier1", ""), "+200 pts"], [1])
    t.data(["Tier 2", d.get("referral_tier2", ""), "+250 pts"], [1])
    t.data(["Tier 3", d.get("referral_tier3", ""), "+300 pts"], [1])
    return t


def build_milestone(d):
    t = TabBuilder()
    t.title("Milestone (individual achievement rewards)")
    t.blank()
    t.colheader(["Milestone", "Type", "Target", "Reward", "Suggested / Preset", "Note"])
    t.data(["First order", "Order count", d.get("milestone_first_order_target", ""), d.get("milestone_first_order_reward", ""), "1 order → welcome badge + bonus pts"], [2, 3])
    t.data(["Loyal customer", "Order count", d.get("milestone_loyal_target", ""), d.get("milestone_loyal_reward", ""), "5 orders → 200 pts + badge"], [2, 3])
    t.data(["Big spender", "Total spend", d.get("milestone_big_spender_target", ""), d.get("milestone_big_spender_reward", ""), "$500 lifetime → 300 pts"], [2, 3])
    t.data(["Anniversary", "Account age", d.get("milestone_anniversary_target", ""), d.get("milestone_anniversary_reward", ""), "1 year → 100 pts + gift"], [2, 3])
    t.plus()
    return t


def build_launch(d):
    t = TabBuilder()
    t.title("Launch & Bootstrap")
    t.note(FILL_NOTE)
    t.blank()
    t.section("PRE-LAUNCH CHECKLIST")
    t.colheader(["Item", "Value", "Suggested / Preset", "Notes"])
    t.data(["Widget installed & on-brand", d.get("launch_widget", ""), "colors/logo match store", "check on desktop + mobile"], [1])
    t.data(["Program name & T&C page live", d.get("launch_terms_page", ""), "", "link in footer"], [1])
    t.data(["Email/SMS templates connected", d.get("launch_email_templates", ""), "welcome, points earned, birthday, expiry, redeem", "via Klaviyo/Omnisend"], [1])
    t.data(["Staff/POS trained", d.get("launch_staff_training", ""), "", "skip if online-only"], [1])
    t.data(["Terms & FAQ help doc published", d.get("launch_faq_doc", ""), "", "reduces CS tickets at launch"], [1])
    t.plus()
    t.blank()
    t.blank()
    t.section("BOOTSTRAP / SEEDING")
    t.colheader(["Item", "Value", "Suggested / Preset", "Notes"])
    t.data(["Soft launch group", d.get("bootstrap_soft_launch_group", ""), "VIPs / repeat customers first, 1-2 weeks", "test before public launch"], [1])
    t.data(["Sign-up bonus for existing customers", d.get("bootstrap_signup_bonus", ""), "200-300 pts (match Welcome Bonus)", "rewards signing up during bootstrap window"], [1])
    t.data(["Retroactive points for past purchases", d.get("bootstrap_retroactive_points", ""), "e.g. 1 pt/$1 on last 90 days orders", "optional, boosts perceived value at day 1"], [1])
    t.data(["Migration import (if migrating)", d.get("bootstrap_migration", ""), "points balance + tier + expiry", "see Setup tab → Migration/Import"], [1])
    t.data(["Launch promo", d.get("bootstrap_promo", ""), "double points week / referral boost", "drives first-week engagement"], [1])
    t.plus()
    t.blank()
    t.blank()
    t.section("PUBLIC LAUNCH")
    t.colheader(["Item", "Value", "Suggested / Preset", "Notes"])
    t.data(["Public launch date", d.get("public_launch_date", ""), "", ""], [1])
    t.data(["Announcement channels", d.get("public_announcement_channels", ""), "email blast + on-site banner + social", ""], [1])
    t.data(["Launch day monitoring owner", d.get("public_launch_owner", ""), "", "who watches for issues"], [1])
    t.plus()
    t.blank()
    t.blank()
    t.section("POST-LAUNCH MONITORING (30/60/90 DAYS)")
    t.colheader(["Item", "Value", "Suggested / Preset", "Notes"])
    t.data(["Redemption rate target", d.get("monitor_redemption_target", ""), ">20% of earned points redeemed", "too low = low perceived value"], [1])
    t.data(["Point liability check-in", d.get("monitor_liability_checkin", ""), "30/60/90 days after launch", "catch runaway earn rate early"], [1])
    t.data(["Follow-up win-back email", d.get("monitor_winback_email", ""), "to non-redeemers at 60 days", ""], [1])
    t.plus()
    return t


BUILDERS = {
    TAB_SETUP: build_setup,
    TAB_EARNING: build_earning,
    TAB_REDEMPTION: build_redemption,
    TAB_VIP: build_vip,
    TAB_REFERRAL: build_referral,
    TAB_MILESTONE: build_milestone,
    TAB_LAUNCH: build_launch,
}


def sheet_id_map(spreadsheet):
    return {s["properties"]["title"]: s["properties"]["sheetId"] for s in spreadsheet["sheets"]}


def format_requests_for(sheet_id, builder):
    reqs = []

    def repeat(row_idx, ncols, bg, fg, size, bold=False, italic=False):
        tf = {"foregroundColor": fg, "fontFamily": "Calibri", "fontSize": size}
        if bold:
            tf["bold"] = True
        if italic:
            tf["italic"] = True
        reqs.append({
            "repeatCell": {
                "range": {
                    "sheetId": sheet_id,
                    "startRowIndex": row_idx,
                    "endRowIndex": row_idx + 1,
                    "startColumnIndex": 0,
                    "endColumnIndex": ncols,
                },
                "cell": {"userEnteredFormat": {"backgroundColor": bg, "textFormat": tf}},
                "fields": "userEnteredFormat(backgroundColor,textFormat)",
            }
        })

    ncols = builder.max_cols
    if builder.title_idx is not None:
        repeat(builder.title_idx, ncols, DARK, WHITE, 15, bold=True)
    for idx in builder.note_idxs:
        repeat(idx, ncols, RED, WHITE, 10, italic=True)
    for idx in builder.section_idxs:
        repeat(idx, ncols, RED, WHITE, 11, bold=True)
    for idx, hcols in builder.colheader_idxs.items():
        repeat(idx, hcols, DARK, WHITE, 10, bold=True)
    for row_idx, col_idx in builder.editable:
        reqs.append({
            "repeatCell": {
                "range": {
                    "sheetId": sheet_id,
                    "startRowIndex": row_idx,
                    "endRowIndex": row_idx + 1,
                    "startColumnIndex": col_idx,
                    "endColumnIndex": col_idx + 1,
                },
                "cell": {"userEnteredFormat": {"backgroundColor": PINK}},
                "fields": "userEnteredFormat(backgroundColor)",
            }
        })

    # Status column: group contiguous same-column cells into ranges so each
    # block gets one background fill + one dropdown validation, not one per cell.
    cells = sorted(builder.status_cells, key=lambda rc: (rc[1], rc[0]))
    blocks = []
    i = 0
    while i < len(cells):
        row0, col0 = cells[i]
        row1 = row0
        j = i + 1
        while j < len(cells) and cells[j][1] == col0 and cells[j][0] == row1 + 1:
            row1 = cells[j][0]
            j += 1
        blocks.append((row0, row1, col0))
        i = j
    for row0, row1, col0 in blocks:
        rng = {
            "sheetId": sheet_id,
            "startRowIndex": row0,
            "endRowIndex": row1 + 1,
            "startColumnIndex": col0,
            "endColumnIndex": col0 + 1,
        }
        reqs.append({
            "repeatCell": {
                "range": rng,
                "cell": {"userEnteredFormat": {"backgroundColor": STATUS_COLOR}},
                "fields": "userEnteredFormat(backgroundColor)",
            }
        })
        reqs.append({
            "setDataValidation": {
                "range": rng,
                "rule": {
                    "condition": {
                        "type": "ONE_OF_LIST",
                        "values": [{"userEnteredValue": v} for v in STATUS_OPTIONS],
                    },
                    "showCustomUi": True,
                    "strict": False,
                },
            }
        })

    reqs.append({
        "autoResizeDimensions": {
            "dimensions": {"sheetId": sheet_id, "dimension": "COLUMNS", "startIndex": 0, "endIndex": ncols}
        }
    })
    reqs.append({
        "updateSheetProperties": {
            "properties": {"sheetId": sheet_id, "gridProperties": {"hideGridlines": True}},
            "fields": "gridProperties.hideGridlines",
        }
    })
    return reqs


def build(account, data, share_email):
    svc = gsheets()

    spreadsheet = (
        svc.spreadsheets()
        .create(
            body={
                "properties": {"title": f"{account} — Joy Loyalty Program"},
                "sheets": [{"properties": {"title": t}} for t in TABS],
            }
        )
        .execute()
    )
    spreadsheet_id = spreadsheet["spreadsheetId"]
    sheet_ids = sheet_id_map(spreadsheet)

    builders = {tab: BUILDERS[tab](data) for tab in TABS}

    value_updates = [
        {"range": f"'{tab}'!A1", "values": builders[tab].rows} for tab in TABS
    ]
    svc.spreadsheets().values().batchUpdate(
        spreadsheetId=spreadsheet_id,
        body={"valueInputOption": "RAW", "data": value_updates},
    ).execute()

    format_requests = []
    for tab in TABS:
        format_requests.extend(format_requests_for(sheet_ids[tab], builders[tab]))

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
    ap.add_argument("--data", help="path to JSON matching the flat key schema in default_data() (optional; blank template otherwise)")
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
