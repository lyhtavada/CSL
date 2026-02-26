"""
Crawl all articles from https://help.joy.so/ and save as .md files.
Usage: python3 scripts/crawl_helpcenter.py
"""

import os
import re
import time
import xml.etree.ElementTree as ET

import requests
from bs4 import BeautifulSoup
from markdownify import markdownify as md

BASE_URL = "https://help.joy.so"
SITEMAP_URL = f"{BASE_URL}/sitemap-pages.xml"
OUTPUT_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "raw-data", "helpcenter")
DELAY = 0.5  # seconds between requests


def get_all_urls():
    """Fetch all page URLs from the sitemap."""
    resp = requests.get(SITEMAP_URL, timeout=30)
    resp.raise_for_status()
    root = ET.fromstring(resp.content)
    ns = {"s": "http://www.sitemaps.org/schemas/sitemap/0.9"}
    urls = [loc.text.strip() for loc in root.findall(".//s:loc", ns) if loc.text]
    # Filter out the homepage itself
    urls = [u for u in urls if u.rstrip("/") != BASE_URL.rstrip("/")]
    print(f"Found {len(urls)} pages in sitemap")
    return urls


def extract_content(html: str) -> tuple[str, str]:
    """Extract title and main content from a help center page."""
    soup = BeautifulSoup(html, "lxml")

    # Remove scripts, styles, nav, header, footer
    for tag in soup.find_all(["script", "style", "nav", "header", "footer", "noscript"]):
        tag.decompose()

    # Try to get the page title
    title = ""
    h1 = soup.find("h1")
    if h1:
        title = h1.get_text(strip=True)

    # Try GitBook-specific selectors first, then fall back to <main> or <article>
    content_el = (
        soup.find("div", {"data-testid": "page.contentEditor"})
        or soup.find("main")
        or soup.find("article")
        or soup.find("div", class_=re.compile(r"(content|page|docs|markdown)", re.I))
    )

    if not content_el:
        content_el = soup.body or soup

    # Convert to markdown
    markdown_content = md(
        str(content_el),
        heading_style="atx",
        bullets="-",
        strip=["img", "svg"],
    ).strip()

    # Clean up excessive blank lines
    markdown_content = re.sub(r"\n{3,}", "\n\n", markdown_content)

    return title, markdown_content


def url_to_filepath(url: str) -> str:
    """Convert a URL to a local file path under OUTPUT_DIR."""
    path = url.replace(BASE_URL, "").strip("/")
    if not path:
        return os.path.join(OUTPUT_DIR, "index.md")

    parts = path.split("/")
    # Last segment becomes the filename
    filename = parts[-1] + ".md"
    # Everything before is the directory (category)
    if len(parts) > 1:
        category_dir = os.path.join(OUTPUT_DIR, *parts[:-1])
    else:
        category_dir = OUTPUT_DIR

    return os.path.join(category_dir, filename)


def crawl_page(url: str) -> bool:
    """Crawl a single page and save it as markdown."""
    filepath = url_to_filepath(url)

    try:
        resp = requests.get(url, timeout=30)
        resp.raise_for_status()
    except requests.RequestException as e:
        print(f"  FAIL {url}: {e}")
        return False

    title, content = extract_content(resp.text)

    if not content or len(content) < 20:
        print(f"  SKIP {url}: no content extracted")
        return False

    # Prepend title as H1 if not already present
    if title and not content.startswith(f"# {title}"):
        content = f"# {title}\n\n{content}"

    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)

    return True


def main():
    urls = get_all_urls()
    success = 0
    fail = 0

    for i, url in enumerate(urls, 1):
        print(f"[{i}/{len(urls)}] {url}")
        if crawl_page(url):
            success += 1
        else:
            fail += 1
        time.sleep(DELAY)

    print(f"\nDone! {success} saved, {fail} failed")
    print(f"Output: {OUTPUT_DIR}")


if __name__ == "__main__":
    main()
