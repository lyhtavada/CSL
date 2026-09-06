#!/usr/bin/env bash
# Mở Chrome "của Betty" — profile riêng, có cổng debug để Betty attach vào.
# Chạy 1 lần mỗi khi khởi động máy. Chrome thường của Liz KHÔNG bị ảnh hưởng.
#
# Vì sao phải profile riêng: từ Chrome 136, Google chặn --remote-debugging-port
# trên profile mặc định (lỗ hổng cho phép web đọc cookie qua cổng debug).
set -uo pipefail
PORT="${1:-9222}"
DIR="$HOME/.betty-chrome"
HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# ── Preflight: máy mới (mac mini, máy khác) thiếu gì thì báo ngay ở đây ──
fail=0
CHROME="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
[ -x "$CHROME" ] || { echo "✗ Chưa cài Google Chrome ($CHROME)"; fail=1; }

if command -v node >/dev/null 2>&1; then
  nv="$(node -p 'process.versions.node.split(".").slice(0,2).map(Number)' 2>/dev/null)"
  node -e 'const [a,b]=process.versions.node.split(".").map(Number); process.exit(a>20||(a===20&&b>=11)?0:1)'     || { echo "✗ Node $(node -v) quá cũ — cần >= 20.11 (dùng import.meta.dirname)"; fail=1; }
else
  echo "✗ Chưa có node"; fail=1
fi

[ -d "$HERE/node_modules/playwright-core" ] || {
  echo "✗ Thiếu playwright-core — chạy: cd $HERE && npm install"; fail=1; }

# Token upload: ưu tiên ~/CSL/.env, fallback config Flameshot của máy đó.
# .env KHÔNG sync qua git, flameshot.ini cũng theo máy → đây là thứ hay thiếu nhất
# khi chuyển sang máy mới.
if ! grep -q '^CAPTURE_TOKEN=' "$HOME/CSL/.env" 2>/dev/null    && ! grep -q 'customUploadToken' "$HOME/.config/flameshot/flameshot.ini" 2>/dev/null; then
  echo "✗ Không có upload token. Cách sửa (chọn 1):"
  echo "    a) Cài + đăng nhập Flameshot của Avada trên máy này"
  echo "    b) Copy 2 dòng customUploadToken/customUploadUrl từ máy cũ vào"
  echo "       ~/CSL/.env dưới tên CAPTURE_TOKEN= và CAPTURE_URL="
  echo "  (vẫn chụp được, chỉ không upload — thêm --no-upload)"
fi

[ "$fail" = 0 ] || { echo; echo "Thiếu thứ bắt buộc ở trên, dừng."; exit 1; }
set -e

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
