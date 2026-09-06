#!/usr/bin/env python3
"""Upload 1 ảnh lên capture.avada.io (cùng endpoint Flameshot của Avada) và in link.

Token đọc từ config Flameshot (~/.config/flameshot/flameshot.ini) nên không phải
lưu trùng secret ở chỗ thứ hai. Override được bằng CAPTURE_TOKEN trong ~/CSL/.env.

In ra:
  page:   link viewer (gửi cho người khác)
  direct: link ảnh trực tiếp (nhúng vào Notion / markdown)
"""
import os, sys, json, uuid, mimetypes, urllib.request, configparser

INI = os.path.expanduser("~/.config/flameshot/flameshot.ini")
ENV = os.path.expanduser("~/CSL/.env")
CDN = "https://d2798l25hiaz3h.cloudfront.net/{}.webp"


def creds():
    tok = url = None
    for line in open(ENV, encoding="utf-8") if os.path.exists(ENV) else []:
        if line.startswith("CAPTURE_TOKEN="): tok = line.split("=", 1)[1].strip()
        if line.startswith("CAPTURE_URL="): url = line.split("=", 1)[1].strip()
    if not (tok and url):
        cp = configparser.ConfigParser(); cp.read(INI)
        g = cp["General"]
        tok = tok or g.get("customUploadToken")
        url = url or g.get("customUploadUrl")
    if not tok:
        sys.exit("Không tìm thấy upload token — cần Flameshot đã cấu hình, hoặc CAPTURE_TOKEN trong ~/CSL/.env")
    return tok, url


def upload(path):
    tok, url = creds()
    body, b = bytearray(), f"----betty{uuid.uuid4().hex}"
    ctype = mimetypes.guess_type(path)[0] or "image/png"
    body += f'--{b}\r\nContent-Disposition: form-data; name="image"; filename="{os.path.basename(path)}"\r\nContent-Type: {ctype}\r\n\r\n'.encode()
    body += open(path, "rb").read() + f"\r\n--{b}--\r\n".encode()
    req = urllib.request.Request(url, data=bytes(body), method="POST", headers={
        "Authorization": f"Bearer {tok}",
        "Content-Type": f"multipart/form-data; boundary={b}",
        # WAF của capture-api chặn User-Agent mặc định của urllib -> 403
        "User-Agent": "curl/8.7.1"})
    with urllib.request.urlopen(req, timeout=60) as r:
        return json.loads(r.read())


if __name__ == "__main__":
    if len(sys.argv) < 2: sys.exit("usage: upload.py <image> [<image> ...]")
    for p in sys.argv[1:]:
        d = upload(p)
        if not d.get("success"): sys.exit(f"upload lỗi: {d}")
        print(f"page:   {d['url']}")
        print(f"direct: {CDN.format(d['imageId'])}")
