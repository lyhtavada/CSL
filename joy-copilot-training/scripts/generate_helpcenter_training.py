"""
Convert raw helpcenter articles into Q&A training data for AI chatbot.
Reads raw-data/helpcenter/ and outputs to training-data/helpcenter/.

Each output file contains:
- Frontmatter (category, topic, source)
- Multiple Q: lines (question variations a merchant might ask)
- One A: block (structured answer derived from the article)

Usage: python3 scripts/generate_helpcenter_training.py
"""

from __future__ import annotations

import os
import re

RAW_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "raw-data", "helpcenter")
OUT_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "training-data", "helpcenter")


def clean_artifacts(text: str) -> str:
    """Remove GitBook artifacts from text."""
    # Remove [hashtag](#...) patterns
    text = re.sub(r"\[hashtag\]\(#[^)]*\)\s*", "", text)
    # Remove [user-content-...] patterns
    text = re.sub(r"\[hashtag\]\(#user-content-[^)]*\)\s*", "", text)
    # Remove arrow-up-right from link text
    text = re.sub(r"arrow-up-right", "", text)
    # Remove chevron artifacts in link text
    text = re.sub(r"chevron-(left|right)", "", text)
    # Remove icon artifacts on their own line
    text = re.sub(r"^(circle-info|circle-exclamation|circle-check|chevron-right|hashtag)\s*$", "", text, flags=re.MULTILINE)
    return text


def clean_markdown(text: str) -> str:
    """Clean raw markdown: remove nav links, artifacts, trailing noise."""
    text = clean_artifacts(text)
    # Remove navigation links [Previous...](...)  [Next...](...)
    text = re.sub(r"\[Previous[^\]]*\]\([^)]*\)\s*\[Next[^\]]*\]\([^)]*\)", "", text)
    # Remove "Last updated ... ago"
    text = re.sub(r"Last updated.*?ago\n?", "", text)
    # Remove "Was this helpful?"
    text = re.sub(r"Was this helpful\?", "", text)
    # Remove leading "# Title\n\n" if the raw file starts with an H1
    text = re.sub(r"^# .+\n+", "", text, count=1)
    # Collapse excessive blank lines
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


def extract_title_from_file(text: str, filename: str) -> str:
    """Extract a clean title. Prefer H1 from content, fallback to filename slug."""
    # Try H1 first
    m = re.search(r"^# (.+)$", text, re.MULTILINE)
    if m:
        title = m.group(1).strip()
        title = clean_artifacts(title).strip()
        # If title is meaningful (not just an anchor), use it
        if len(title) > 2 and not title.startswith("#"):
            return title

    # Fallback: use filename slug
    slug = filename.replace(".md", "")
    return slug_to_readable(slug)


def extract_faq_section(text: str) -> list[tuple[str, str]]:
    """Extract existing Q&A pairs from FAQ sections in the article."""
    pairs = []
    faq_pattern = re.compile(
        r"\*{0,2}Q:\s*(.+?)\*{0,2}\s*\n+\s*\*{0,2}A:\s*(.+?)(?=\n\*{0,2}Q:|\n###|\n##|\Z)",
        re.DOTALL | re.IGNORECASE
    )
    for m in faq_pattern.finditer(text):
        q = clean_artifacts(m.group(1).strip().rstrip("*"))
        a = clean_artifacts(m.group(2).strip().rstrip("*"))
        if len(q) > 10 and len(a) > 10:
            pairs.append((q, a))
    return pairs


def slug_to_readable(slug: str) -> str:
    """Convert URL slug to readable text: 'place-order' -> 'Place Order'."""
    # Handle special cases
    slug = slug.replace("joy-and-", "Joy and ")
    result = slug.replace("-", " ").replace(".", " ")
    # Title case but preserve known uppercase terms
    result = result.title()
    # Fix common terms
    for term, replacement in [
        ("Pos", "POS"), ("Vip", "VIP"), ("Sms", "SMS"),
        ("Api", "API"), ("Faq", "FAQ"), ("Csv", "CSV"),
        ("B2B", "B2B"), ("Ai", "AI"), ("Qr", "QR"),
    ]:
        result = result.replace(term, replacement)
    return result


def path_to_category(rel_path: str) -> str:
    """Convert relative file path to category string."""
    parts = rel_path.split(os.sep)
    if len(parts) > 1:
        return slug_to_readable(parts[0])
    return "General"


def path_to_subcategory(rel_path: str) -> str:
    """Get subcategory from path if exists."""
    parts = rel_path.split(os.sep)
    if len(parts) > 2:
        return slug_to_readable(parts[1])
    return ""


def generate_questions(title: str, category: str, subcategory: str, content: str) -> list[str]:
    """Generate likely merchant questions based on article title and content."""
    questions = []
    content_lower = content.lower()

    is_howto = bool(re.search(r"how to (set up|integrate|configure|use|enable|create)", content, re.I))
    is_integration = "integrat" in category.lower() or "integrat" in content_lower[:300]
    is_troubleshoot = bool(re.search(r"(troubleshoot|common (issue|reason|problem)|not (work|show|receiv))", content, re.I))

    # Base question
    questions.append(f"What is {title} in Joy Loyalty?")

    # How-to
    if is_howto or "set up" in content_lower[:500]:
        questions.append(f"How do I set up {title}?")
    else:
        questions.append(f"How does {title} work?")

    # Integration-specific
    if is_integration:
        questions.append(f"How do I connect {title} with Joy Loyalty?")

    # Troubleshooting
    if is_troubleshoot:
        questions.append(f"Why is {title} not working?")

    # Category-contextual
    cat_lower = category.lower()
    if "reward" in cat_lower:
        questions.append(f"How do customers earn rewards with {title}?")
    elif "membership" in cat_lower:
        questions.append(f"How does {title} work with VIP tiers?")
    elif "pos" in cat_lower:
        questions.append(f"How do I use {title} on Shopify POS?")
    elif "migration" in cat_lower:
        questions.append(f"How do I migrate to Joy from {title.replace('Migration From ', '').replace(' To Joy Loyalty', '')}?")
    elif "setting" in cat_lower:
        questions.append(f"Where can I find {title} settings?")
    elif "on site" in cat_lower:
        questions.append(f"How do I customize {title} on my store?")
    elif "notification" in cat_lower:
        questions.append(f"How do I set up {title}?")

    # Deduplicate
    seen = set()
    unique = []
    for q in questions:
        q_lower = q.lower()
        if q_lower not in seen:
            seen.add(q_lower)
            unique.append(q)
    return unique[:5]


def build_answer(content: str) -> str:
    """Build a clean answer from article content."""
    cleaned = clean_markdown(content)

    # Trim to reasonable length for training (max ~3000 chars)
    if len(cleaned) > 3000:
        lines = cleaned.split("\n")
        trimmed = []
        length = 0
        for line in lines:
            if length + len(line) > 2800:
                trimmed.append("\n(See the full help center article for more details.)")
                break
            trimmed.append(line)
            length += len(line) + 1
        cleaned = "\n".join(trimmed)

    return cleaned


def process_article(raw_path: str, rel_path: str) -> str | None:
    """Process one raw article into Q&A training content."""
    with open(raw_path, "r", encoding="utf-8") as f:
        content = f.read()

    if len(content.strip()) < 50:
        return None

    filename = os.path.basename(rel_path)
    title = extract_title_from_file(content, filename)
    category = path_to_category(rel_path)
    subcategory = path_to_subcategory(rel_path)
    questions = generate_questions(title, category, subcategory, content)
    answer = build_answer(content)
    existing_faq = extract_faq_section(content)

    lines = []
    lines.append("---")
    lines.append(f"category: {category}")
    if subcategory:
        lines.append(f"subcategory: {subcategory}")
    lines.append(f"topic: {title}")
    lines.append("source: helpcenter")
    lines.append("---")
    lines.append("")

    for q in questions:
        lines.append(f"Q: {q}")
    lines.append(f"A: {answer}")

    if existing_faq:
        lines.append("")
        lines.append("---")
        lines.append("")
        for q, a in existing_faq:
            lines.append(f"Q: {q}")
            lines.append(f"A: {a}")
            lines.append("")

    return "\n".join(lines)


def main():
    os.makedirs(OUT_DIR, exist_ok=True)

    count = 0
    skipped = 0

    for root, dirs, files in os.walk(RAW_DIR):
        for fname in sorted(files):
            if not fname.endswith(".md"):
                continue

            raw_path = os.path.join(root, fname)
            rel_path = os.path.relpath(raw_path, RAW_DIR)

            out_path = os.path.join(OUT_DIR, rel_path)
            os.makedirs(os.path.dirname(out_path), exist_ok=True)

            result = process_article(raw_path, rel_path)
            if result is None:
                skipped += 1
                continue

            with open(out_path, "w", encoding="utf-8") as f:
                f.write(result)
            count += 1

    print(f"Generated {count} training files, skipped {skipped}")
    print(f"Output: {OUT_DIR}")


if __name__ == "__main__":
    main()
