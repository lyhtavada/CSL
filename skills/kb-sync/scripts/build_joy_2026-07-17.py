#!/usr/bin/env python3
"""
build_joy_2026-07-17.py — KB patches cho Joyce từ bot-corrections tuần 06–12/07/2026
(report reports/bot-corrections/joy/joy-corrections-2026-07-06.md).

2 file, cả 2 đều là KB SAI THẬT (đã probe /api/chat: bot lặp lại đúng lỗi của KB):

1. kb/reference/birthday.md      — correction #6 (Alyssa 09/07)
   KB ghi "Joy Admin → Settings → Birthday field name in register form".
   Source: setting `birthdayFieldInRegisterForm` nằm trong packages/assets/src/pages/
   DevZone/DevZone.js — DevZone = trang nội bộ team (CsDeal/ImportManager/DevTestLog),
   merchant KHÔNG vào được. Field trong register form cũng phải merchant tự thêm vào
   theme, chỉ làm được với legacy customer accounts.

2. kb/reference/loyalty-page.md  — correction #3 (Audrey 07/07)
   KB ghi "Generate AI-styled icons cho Ways to earn/redeem — On-site content →
   [program] → Set up → AI icon". Sai cả feature lẫn path.
   Source: useGenerateIconAI dùng ở pages/Branding/SectionV2/Display.js, set
   `launcher.iconUrl` / `floatBtnIconUrl`, forcedCategory = GenerateAI.floatButtonWidget
   → AI icon CHỈ cho nút float của widget. Icon của program chọn bằng "Choose icon"
   trong widget section editor (locale WidgetSectionV2.json: chooseIcon).
   Path đúng lấy từ correction của Audrey.

Nguyên tắc: viết cái ĐÚNG, không viết negative example ("đừng nói X") — bot copy ra cho khách.
Mỗi replacement assert anchor tồn tại — heading dịch chuyển là fail to tiếng.
"""
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import kb_api

AGENT = "joy-loyalty-agent"
OUT = os.path.expanduser("~/CSL/reports/analysis/kb-joy-2026-07-17-payloads.json")

base, token = kb_api.load_creds()


def fetch(path):
    return kb_api.get_file(base, token, AGENT, path)


def replace(content, old, new, label):
    if old not in content:
        sys.exit(f"ANCHOR MISSING [{label}] — nội dung KB đã đổi, dừng lại:\n{old[:200]}")
    if content.count(old) != 1:
        sys.exit(f"ANCHOR NOT UNIQUE [{label}] — khớp {content.count(old)} chỗ")
    return content.replace(old, new)


payloads = []

# ---------------------------------------------------------------- 1. birthday.md
b = fetch("kb/reference/birthday.md")

OLD_METHOD1 = """## Method 1 — Registration form

1. **Joy Admin → Settings** → set **"Birthday field name in register form"** to `Birthday` (or your preferred name)
2. Edit theme `customers/register.liquid` and insert Joy's birthday field snippet (date picker)
3. On registration, value saves to Shopify customer notes → syncs to Joy via Shopify customer creation webhook"""

NEW_METHOD1 = """## Method 1 — Registration form (legacy customer accounts only)

Joy reads the birthday from the **Shopify customer note** that the store's registration
form writes. The note field name Joy looks for defaults to `Birthday`.

Adding a birthday field to the registration form is **theme work on the merchant's side** —
Joy does not inject the field into the form. It requires Shopify's **legacy (classic)
customer accounts**, the only mode where the registration template can be customized.

**Steps for the merchant:**
1. Confirm the store uses **legacy (classic) customer accounts**
2. Edit theme `customers/register.liquid` and add a birthday field (date picker) that saves
   to the customer note under the name `Birthday`
3. On registration, the value lands in the Shopify customer note → syncs to Joy via the
   Shopify customer-creation webhook

**If the form uses a different note field name:** the name Joy reads is configured by the
team, not by the merchant. Collect the exact field name the merchant's form writes, then
escalate to the team to set it for the shop — append `<escalate_human>` to the reply.

**On new customer accounts:** Shopify's new customer accounts do not allow editing the
registration template, so this method does not apply. Use **Method 2 — sync from
metafields** below, or have customers add their birthday in their Joy profile online."""

b = replace(b, OLD_METHOD1, NEW_METHOD1, "birthday: Method 1")

b = replace(
    b,
    "- kb_settings-general (birthday field name setting)",
    "- kb_settings-general (sync Shopify metafields to Joy)",
    "birthday: related pointer",
)
payloads.append({"agent": AGENT, "path": "kb/reference/birthday.md", "content": b})

# ----------------------------------------------------------- 2. loyalty-page.md
p = fetch("kb/reference/loyalty-page.md")

OLD_ICONS = """Available on **Essential and above** (the plans that have the loyalty page). Generate AI-styled icons matching your brand for **Ways to earn** and **Ways to redeem** programs.

**On-site content → [program] → Set up → AI icon** — enter prompt → regenerate until it matches your vision."""

NEW_ICONS = """## Program icons (Ways to earn / Ways to redeem)

Program icons are set **per surface** — the widget and the loyalty page each have their own
icon settings, so changing one does not change the other.

**Widget icons:** **On-site content → Loyalty widget → Set up the Widget → Section → Ways to
earn → Customize programs** — click a program to change its icon.

**Loyalty page icons:** **On-site content → Loyalty page → edit the "Ways to earn" block** —
click each program to upload a custom icon URL.

## AI icon generator

**Generate AI Icon** applies to the **widget float button icon**. Find it in the widget setup
under the float button's **Display** settings (**Button icon → Generate AI Icon**): enter a
prompt and regenerate until it matches the brand. Available on **Essential and above**.

Program icons in Ways to earn / Ways to redeem are set with the icon pickers above."""

p = replace(p, OLD_ICONS, NEW_ICONS, "loyalty-page: icons block")
payloads.append({"agent": AGENT, "path": "kb/reference/loyalty-page.md", "content": p})

os.makedirs(os.path.dirname(OUT), exist_ok=True)
with open(OUT, "w") as f:
    json.dump(payloads, f, indent=2, ensure_ascii=False)
print(f"OK — {len(payloads)} payload(s) → {OUT}")
for x in payloads:
    print(f"  - {x['path']}  ({len(x['content'])} chars)")
