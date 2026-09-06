#!/usr/bin/env bash
# Mở Chrome "của Betty" — profile riêng, có cổng debug để Betty attach vào.
# Chạy 1 lần mỗi khi khởi động máy. Chrome thường của Liz KHÔNG bị ảnh hưởng.
#
# Vì sao phải profile riêng: từ Chrome 136, Google chặn --remote-debugging-port
# trên profile mặc định (lỗ hổng cho phép web đọc cookie qua cổng debug).
set -euo pipefail
PORT="${1:-9222}"
DIR="$HOME/.betty-chrome"

if curl -s -m 2 "http://127.0.0.1:$PORT/json/version" >/dev/null 2>&1; then
  echo "✓ Chrome debug đã chạy sẵn ở cổng $PORT — không cần mở lại."
  exit 0
fi

mkdir -p "$DIR"
open -na "Google Chrome" --args \
  --remote-debugging-port="$PORT" \
  --user-data-dir="$DIR" \
  --no-first-run --no-default-browser-check

for i in $(seq 1 15); do
  sleep 1
  if curl -s -m 2 "http://127.0.0.1:$PORT/json/version" >/dev/null 2>&1; then
    echo "✓ Chrome debug sẵn sàng ở cổng $PORT (profile: $DIR)"
    echo "  Đăng nhập Shopify / Chatty / Crisp trong cửa sổ vừa mở — chỉ cần 1 lần,"
    echo "  lần sau vẫn còn đăng nhập."
    exit 0
  fi
done
echo "✗ Không thấy cổng $PORT mở sau 15s." >&2
exit 1
