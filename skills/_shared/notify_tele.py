#!/usr/bin/env python3
"""
notify_tele.py — gửi 1 tin Telegram cho Liz báo trạng thái 1 cron job.

Dùng chung cho mọi cron trong CSL. Gọi ở CUỐI mỗi run-*.sh:

    JOB="CS Weekly"
    ... chạy job, lưu rc ...
    python3 ~/CSL/skills/_shared/notify_tele.py \
        --job "$JOB" --status $([ $rc -eq 0 ] && echo ok || echo fail) \
        --summary "$(tail -3 /tmp/cs-weekly.log)"

Creds đọc từ ~/CSL/.env: TELEGRAM_BOT_TOKEN + TELEGRAM_OWNER_ID.
Không bao giờ raise lỗi ra ngoài (notify fail KHÔNG được làm hỏng job) — chỉ in cảnh báo.

Args:
  --job      tên job (bắt buộc)
  --status   ok | fail (mặc định ok)
  --summary  vài dòng tóm tắt / dòng lỗi (tùy chọn)
  --log      đường dẫn log; nếu có thì tự lấy tail vài dòng làm summary khi --summary trống
"""
import argparse
import datetime as dt
import json
import os
import sys
import urllib.request
from pathlib import Path

ENV_PATH = os.path.expanduser("~/CSL/.env")
VNT = dt.timezone(dt.timedelta(hours=7))


def load_creds():
    tok = chat = None
    try:
        for line in Path(ENV_PATH).read_text().splitlines():
            line = line.strip()
            if line.startswith("TELEGRAM_BOT_TOKEN="):
                tok = line.split("=", 1)[1].strip().strip('"').strip("'")
            elif line.startswith("TELEGRAM_OWNER_ID="):
                chat = line.split("=", 1)[1].strip().strip('"').strip("'")
    except FileNotFoundError:
        return None, None
    return tok, chat


def tail(path, n=4):
    try:
        lines = Path(path).read_text(errors="replace").splitlines()
        return "\n".join(lines[-n:])
    except Exception:
        return ""


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--job", required=True)
    ap.add_argument("--status", default="ok", choices=["ok", "fail"])
    ap.add_argument("--summary", default="")
    ap.add_argument("--log", default="")
    args = ap.parse_args()

    tok, chat = load_creds()
    if not tok or not chat:
        print("notify_tele: TELEGRAM_BOT_TOKEN/OWNER_ID missing — skip", file=sys.stderr)
        return

    icon = "✅" if args.status == "ok" else "❌"
    head = "xong" if args.status == "ok" else "FAIL"
    now = dt.datetime.now(VNT).strftime("%H:%M %d/%m")

    summary = args.summary.strip()
    if not summary and args.log:
        summary = tail(args.log)
    # Telegram giới hạn ~4096 ký tự; cắt cho gọn
    if len(summary) > 1500:
        summary = summary[:1500] + "…"

    text = f"{icon} <b>{args.job}</b> — {head}  ·  {now}"
    if summary:
        text += f"\n<pre>{summary}</pre>"

    url = f"https://api.telegram.org/bot{tok}/sendMessage"
    data = json.dumps({"chat_id": chat, "text": text, "parse_mode": "HTML"}).encode()
    req = urllib.request.Request(url, data=data, headers={"Content-Type": "application/json"})
    try:
        r = json.load(urllib.request.urlopen(req, timeout=20))
        if not r.get("ok"):
            print(f"notify_tele: telegram returned {r}", file=sys.stderr)
    except Exception as e:
        print(f"notify_tele: send failed: {e}", file=sys.stderr)


if __name__ == "__main__":
    main()
