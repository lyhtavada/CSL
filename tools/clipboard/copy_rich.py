#!/usr/bin/env python3
"""Copy a markdown-ish draft to the macOS clipboard as rich text (HTML) + plain text.

Why: text copied from the Claude Code terminal carries the terminal's soft wraps as
real newlines + leading indentation, so pasted emails break mid-sentence in Gmail.
Put drafts on the clipboard directly instead.

Usage:
  python3 tools/clipboard/copy_rich.py draft.md
  cat draft.md | python3 tools/clipboard/copy_rich.py

Supported syntax: blank-line paragraphs, **bold**, *italic*, [text](url),
"- " / "* " bullets, "1. " numbered lists. Single newlines inside a paragraph
become <br> (keeps signature lines intact).
"""
import html
import re
import subprocess
import sys


def inline(s: str) -> str:
    s = html.escape(s, quote=False)
    s = re.sub(r"\[([^\]]+)\]\((https?://[^)]+)\)", r'<a href="\2">\1</a>', s)
    s = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", s)
    s = re.sub(r"(?<!\*)\*(?!\s)(.+?)(?<!\s)\*(?!\*)", r"<i>\1</i>", s)
    return s


def strip_md(s: str) -> str:
    s = re.sub(r"\[([^\]]+)\]\((https?://[^)]+)\)", r"\1 (\2)", s)
    s = re.sub(r"\*\*(.+?)\*\*", r"\1", s)
    return re.sub(r"(?<!\*)\*(?!\s)(.+?)(?<!\s)\*(?!\*)", r"\1", s)


def to_html(text: str) -> str:
    out = []
    for block in re.split(r"\n\s*\n", text.strip()):
        lines = [l.strip() for l in block.strip().splitlines() if l.strip()]
        if all(re.match(r"[-*] ", l) for l in lines):
            out.append("<ul>" + "".join(f"<li>{inline(l[2:])}</li>" for l in lines) + "</ul>")
        elif all(re.match(r"\d+\. ", l) for l in lines):
            items = (inline(re.sub(r"^\d+\. ", "", l)) for l in lines)
            out.append("<ol>" + "".join(f"<li>{i}</li>" for i in items) + "</ol>")
        else:
            out.append("<p>" + "<br>".join(inline(l) for l in lines) + "</p>")
    return '<div style="font-family:Arial,sans-serif;font-size:14px">' + "".join(out) + "</div>"


def to_plain(text: str) -> str:
    blocks = re.split(r"\n\s*\n", text.strip())
    return "\n\n".join("\n".join(strip_md(l.strip()) for l in b.strip().splitlines()) for b in blocks) + "\n"


JXA = """
ObjC.import("AppKit");
function run(argv) {
  const pb = $.NSPasteboard.generalPasteboard;
  pb.clearContents;
  pb.setStringForType($(argv[0]), "public.html");
  pb.setStringForType($(argv[1]), "public.utf8-plain-text");
  return "ok";
}
"""


def main():
    text = open(sys.argv[1], encoding="utf-8").read() if len(sys.argv) > 1 else sys.stdin.read()
    subprocess.run(["osascript", "-l", "JavaScript", "-e", JXA, to_html(text), to_plain(text)],
                   check=True, capture_output=True)
    print("Copied to clipboard (rich text + plain text).")


if __name__ == "__main__":
    main()
