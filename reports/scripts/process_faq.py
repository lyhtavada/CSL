#!/usr/bin/env python3
"""
Process Joy Crisp transcripts -> FAQ CSV
Uses OpenAI API (gpt-4o-mini) to analyze each conversation
"""

import csv
import json
import os
import time
import warnings
warnings.filterwarnings('ignore')

import requests

OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY', '')
OPENAI_URL = "https://api.openai.com/v1/chat/completions"

# ── Read knowledge base ──────────────────────────────────────────────────────
def read_file(path):
    with open(path, 'r', encoding='utf-8') as f:
        return f.read()

KB = read_file('/Users/avada/CSL/kb/kb-joy.md')
HC_REWARD   = read_file('/Users/avada/CSL/kb/helpcenter-joy/reward-programs.md')
HC_MEMBER   = read_file('/Users/avada/CSL/kb/helpcenter-joy/membership.md')
HC_ONSITE   = read_file('/Users/avada/CSL/kb/helpcenter-joy/on-site-content.md')
HC_CUST     = read_file('/Users/avada/CSL/kb/helpcenter-joy/customers-and-activities.md')
HC_POS      = read_file('/Users/avada/CSL/kb/helpcenter-joy/pos-integrations-settings.md')

KNOWLEDGE_BASE = f"""
=== MAIN KB ===
{KB}

=== REWARD PROGRAMS ===
{HC_REWARD}

=== MEMBERSHIP & VIP ===
{HC_MEMBER}

=== ON-SITE CONTENT ===
{HC_ONSITE}

=== CUSTOMERS & ACTIVITIES ===
{HC_CUST}

=== POS, INTEGRATIONS, SETTINGS ===
{HC_POS}
"""

SYSTEM_PROMPT = """You are an expert at analyzing customer support conversations for Joy Loyalty (a Shopify loyalty app).

Given a support chat transcript between a merchant (User) and CS staff, your job is to:
1. Identify the main question(s) the merchant is asking
2. Find the best answer from what CS said, enhanced with knowledge base
3. Classify the category
4. Return structured JSON

Categories:
- points — earning points, point calculation, expiration, retroactive
- rewards — redemption, free gift, store credit, discount codes  
- vip — VIP tiers, tier entry rewards, perks
- referral — referral program, referral rewards
- birthday — birthday program, anniversary
- widget — widget display, customization, translation, visibility
- integration — Klaviyo, POS, Flow, review apps, API
- billing — plans, pricing, order limits, upgrade/downgrade
- bug — something not working as expected
- migration — migrating from another app
- other — anything else

Rules:
- Return SKIP if conversation has no clear question (only greetings, thank yous, small talk)
- If multiple distinct questions in one conversation, return ARRAY of FAQ entries
- Answer should be concise, clear, professional English, no greeting/sign-off
- Answer should combine CS reply + knowledge base for accuracy
- Question should be written as a clear, standalone question a merchant might search for

Return JSON format (array even for single item):
[
  {
    "category": "...",
    "question": "...",
    "answer": "..."
  }
]

Or just return: "SKIP" if no clear question.
"""

def call_openai(transcript, retries=3):
    """Call OpenAI API to analyze one transcript"""
    messages = [
        {"role": "system", "content": SYSTEM_PROMPT + "\n\nKNOWLEDGE BASE:\n" + KNOWLEDGE_BASE},
        {"role": "user", "content": f"Analyze this support conversation transcript:\n\n{transcript}"}
    ]
    
    for attempt in range(retries):
        try:
            resp = requests.post(
                OPENAI_URL,
                headers={
                    "Authorization": f"Bearer {OPENAI_API_KEY}",
                    "Content-Type": "application/json"
                },
                json={
                    "model": "gpt-4o-mini",
                    "messages": messages,
                    "temperature": 0.3,
                    "max_tokens": 1500
                },
                timeout=60
            )
            resp.raise_for_status()
            content = resp.json()['choices'][0]['message']['content'].strip()
            return content
        except requests.exceptions.HTTPError as e:
            if resp.status_code == 429:
                wait = 30 * (attempt + 1)
                print(f"  Rate limited, waiting {wait}s...")
                time.sleep(wait)
            else:
                print(f"  HTTP error {resp.status_code}: {e}")
                if attempt < retries - 1:
                    time.sleep(5)
                else:
                    raise
        except Exception as e:
            print(f"  Error: {e}")
            if attempt < retries - 1:
                time.sleep(5)
            else:
                raise
    return "SKIP"

def parse_response(content):
    """Parse OpenAI response into list of FAQ entries"""
    if content.strip() == "SKIP":
        return []
    
    # Try to extract JSON from markdown code blocks
    if "```json" in content:
        start = content.find("```json") + 7
        end = content.find("```", start)
        content = content[start:end].strip()
    elif "```" in content:
        start = content.find("```") + 3
        end = content.find("```", start)
        content = content[start:end].strip()
    
    try:
        data = json.loads(content)
        if isinstance(data, list):
            return data
        elif isinstance(data, dict):
            return [data]
    except json.JSONDecodeError:
        # Try to find JSON array in content
        start = content.find('[')
        end = content.rfind(']') + 1
        if start >= 0 and end > start:
            try:
                data = json.loads(content[start:end])
                return data if isinstance(data, list) else [data]
            except:
                pass
        # Try single object
        start = content.find('{')
        end = content.rfind('}') + 1
        if start >= 0 and end > start:
            try:
                data = json.loads(content[start:end])
                return [data]
            except:
                pass
    
    print(f"  Could not parse response: {content[:200]}")
    return []

def deduplicate(entries):
    """Simple deduplication by question similarity"""
    seen_questions = {}
    result = []
    
    for entry in entries:
        q = entry['question'].lower().strip()
        # Check if very similar question already exists
        is_dup = False
        for seen_q in seen_questions:
            # Simple overlap check
            words_new = set(q.split())
            words_seen = set(seen_q.split())
            if len(words_new) > 0 and len(words_seen) > 0:
                overlap = len(words_new & words_seen) / min(len(words_new), len(words_seen))
                if overlap > 0.75:
                    # Keep the one with longer/better answer
                    existing_idx = seen_questions[seen_q]
                    if len(entry['answer']) > len(result[existing_idx]['answer']):
                        result[existing_idx] = entry
                    is_dup = True
                    break
        
        if not is_dup:
            seen_questions[q] = len(result)
            result.append(entry)
    
    return result

def main():
    # Read transcripts
    with open('/Users/avada/CSL/reports/crisp-joy-transcripts.csv', 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        conversations = list(reader)
    
    print(f"Total conversations to process: {len(conversations)}")
    print("=" * 60)
    
    all_entries = []
    skipped = 0
    processed = 0
    
    for i, conv in enumerate(conversations):
        session_id = conv['Session ID']
        transcript = conv['Transcript']
        merchant = conv.get('Merchant Name', '')
        
        print(f"[{i+1:3d}/{len(conversations)}] {merchant[:30]:<30} ", end="", flush=True)
        
        # Quick pre-check: skip if transcript is very short or only greetings
        user_messages = [line for line in transcript.split('\n') if line.startswith('[User]')]
        if not user_messages:
            print("SKIP (no user messages)")
            skipped += 1
            continue
        
        # Check if user messages have substantive content
        all_user_text = ' '.join(user_messages).lower()
        skip_phrases = ['thank you', 'thanks', 'okay', 'ok', 'great', 'perfect', 'alright', 
                       'got it', 'understood', 'i see', 'okey', 'noted']
        is_only_small_talk = all(
            any(phrase in msg.lower() for phrase in skip_phrases) or len(msg) < 30
            for msg in user_messages
        )
        
        if is_only_small_talk and len(user_messages) <= 3:
            print("SKIP (only small talk)")
            skipped += 1
            continue
        
        try:
            response = call_openai(transcript)
            entries = parse_response(response)
            
            if entries:
                all_entries.extend(entries)
                print(f"OK ({len(entries)} FAQ{'s' if len(entries)>1 else ''})")
                processed += 1
            else:
                print("SKIP (no clear question)")
                skipped += 1
        except Exception as e:
            print(f"ERROR: {e}")
            skipped += 1
        
        # Small delay to respect rate limits
        time.sleep(0.3)
    
    print(f"\n{'='*60}")
    print(f"Processed: {processed}, Skipped: {skipped}")
    print(f"Raw FAQ entries: {len(all_entries)}")
    
    # Deduplicate
    deduped = deduplicate(all_entries)
    print(f"After deduplication: {len(deduped)}")
    
    # Category breakdown
    categories = {}
    for e in deduped:
        cat = e.get('category', 'other')
        categories[cat] = categories.get(cat, 0) + 1
    
    print("\nBreakdown by category:")
    for cat, count in sorted(categories.items(), key=lambda x: -x[1]):
        print(f"  {cat:<15} {count}")
    
    # Write output CSV
    output_path = '/Users/avada/CSL/reports/joy-faq-from-crisp.csv'
    with open(output_path, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL)
        writer.writerow(['Category', 'Reviewer', 'Question', 'Answer'])
        for entry in deduped:
            writer.writerow([
                entry.get('category', 'other'),
                '',  # Reviewer empty
                entry.get('question', ''),
                entry.get('answer', '')
            ])
    
    print(f"\n✅ Output saved to: {output_path}")
    print(f"Total rows: {len(deduped)}")
    
    return len(conversations), processed, skipped, len(deduped), categories

if __name__ == '__main__':
    main()
