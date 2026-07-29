#!/usr/bin/env python3
"""
Build the Notion markdown body for a monthly DFY report from fetch_dfy.py JSON.

Usage:
  python3 build_report.py --in /tmp/dfy.json --out /tmp/dfy.md

The body starts at `## Overview` (NO H1) — push_notion.py uses the --title as the
page title, so an H1 would duplicate it. Section order:
  Overview → 💡 Insight & đề xuất → 🔵 Inbound table → 🟢 Proactive table → Note
"""
import json, argparse

MONTH_VI = {
    "01": "1", "02": "2", "03": "3", "04": "4", "05": "5", "06": "6",
    "07": "7", "08": "8", "09": "9", "10": "10", "11": "11", "12": "12",
}


def ticket_table(tickets):
    out = ["| Date | Ticket | Store | CS | Tasks | Tags |",
           "|------|--------|-------|----|-------|------|"]
    for t in tickets:
        tags = ", ".join(t["tags"])
        out.append(f"| {t['date']} | [{t['ticket_id']}]({t['url']}) | {t['store']} | "
                   f"{t['cs_display']} | {t['tasks_done']}/{t['tasks_total']} | {tags} |")
    return "\n".join(out)


def insight_section(d):
    ins = d["insights"]
    v = ins["video"]
    ai = ins["ai"]
    cb = ins["chatbox"]
    tm = ins["timing"]
    # per-CS quality line: best adopt vs highest volume
    per = d["per_cs"]
    top_vol = max(per, key=lambda c: c["count"]) if per else None
    best = max((c for c in per if c["count"] >= 3), key=lambda c: c["adopt_pct"], default=None)

    L = ["## 💡 Insight & đề xuất\n"]
    L.append(f"**1. Video là đòn bẩy adopt mạnh nhất.** Ticket có quay video kết quả "
             f"adopt **{v['yes_adopt_pct']}%** ({v['yes_n']} ticket) vs không video chỉ "
             f"**{v['no_adopt_pct']}%** ({v['no_n']} ticket) — chênh +{v['delta']} điểm. "
             f"→ **Đề xuất:** đưa quay video kết quả thành bước bắt buộc trong DFY flow.\n")
    L.append(f"**2. Làm kỹ AI Agent → adopt cao.** AI Agent hoàn thành 100% adopt "
             f"**{ai['full_adopt_pct']}%**; hoàn thành 0% adopt **{ai['zero_adopt_pct']}%**. "
             f"Xác nhận DFY làm đến nơi thì giữ được widget.\n")
    L.append(f"**3. Khối Chatbox gần như bị bỏ trống.** Chỉ **{cb['task_pct']}%** task Chatbox "
             f"hoàn thành, **{cb['zero_ticket']}/{cb['total_ticket']} ticket không làm task "
             f"Chatbox nào**. DFY hiện gần như chỉ setup AI Agent. → **Cần xác định:** Chatbox "
             f"có nằm trong scope DFY Chatty không.\n")
    L.append(f"**4. DFY dồn cuối tháng.** {tm['peak_n']}/{d['total']} ticket tạo trong tuần "
             f"{tm['peak_week']} của tháng; đầu tháng gần như trống. → Ticket cuối tháng chưa "
             f"đủ thời gian follow-up adopt; nên rải đều hơn để theo dõi kết quả sát.\n")
    if ins["review_yes"]:
        L.append(f"**5. DFY sinh review 5★.** {ins['review_yes']} ticket convert được review "
                 f"từ flow DFY — giá trị phụ ngoài việc giữ widget.\n")
    if top_vol and best:
        L.append(f"**6. Chất lượng ≠ volume.** {best['display']} adopt {best['adopt_pct']}% "
                 f"(làm {best['count']} ticket) — kỹ nhất. {top_vol['display']} volume cao nhất "
                 f"({top_vol['count']} ticket) nhưng adopt {top_vol['adopt_pct']}%.\n")
    return "\n".join(L)


def build(d):
    mm = d["month"].split("-")[1]
    inb = d["inbound"]
    pro = d["proactive"]

    rv = d["insights"]["review"]
    dpi = d["insights"]["dfy_per_install"]

    L = []
    L.append("## Overview\n")
    L.append(f"- **Tổng ticket DFY:** {d['total']} · **Adopted:** {d['adopted']} ({d['adopt_pct']}%)")
    L.append(f"- 🔵 **Inbound** (DFY theo yêu cầu KH): {inb['count']} ticket · adopted "
             f"{inb['adopted']} (**{inb['adopt_pct']}%**)")
    L.append(f"- 🟢 **Proactive** (DFY chủ động reach out): {pro['count']} ticket · adopted "
             f"{pro['adopted']} (**{pro['adopt_pct']}%**)")
    L.append(f"- ⭐ **Review xin được / ticket DFY:** {rv['count']}/{rv['total']} "
             f"(**{rv['pct']}%**)")
    L.append(f"- 📈 **Case DFY / install app trong tháng:** {dpi['dfy_tickets']}/{dpi['installs']} "
             f"(**{dpi['pct']}%**)")
    L.append(f"- **Note:** Số liệu tháng {MONTH_VI.get(mm, mm)}/{d['month'].split('-')[0]} "
             f"(open tickets).\n")

    L.append(insight_section(d))
    L.append("")
    L.append(f"## 🔵 Inbound — DFY theo yêu cầu ({inb['count']} tickets · "
             f"{inb['adopted']} adopted / {inb['adopt_pct']}%)\n")
    L.append(ticket_table(inb["tickets"]))
    L.append("")
    L.append(f"## 🟢 Proactive — DFY chủ động ({pro['count']} tickets · "
             f"{pro['adopted']} adopted / {pro['adopt_pct']}%)\n")
    L.append(ticket_table(pro["tickets"]))
    L.append("")
    L.append("---\n")
    L.append("## Note\n")
    L.append("_(Liz điền — feedback / coaching khi review với team)_")
    return "\n".join(L)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--in", dest="inp", required=True, help="fetch_dfy.py JSON")
    ap.add_argument("--out", required=True, help="Output markdown path")
    a = ap.parse_args()
    d = json.load(open(a.inp))
    open(a.out, "w").write(build(d))
    print(f"Wrote {a.out}")


if __name__ == "__main__":
    main()
