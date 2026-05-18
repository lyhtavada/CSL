# Test and Optimize AI

<!-- CHUNK: test-and-optimize-test-zone -->
```yaml
chunk_id: "faq__test-and-optimize-test-zone"
doc_id: "chatty-test-and-optimize-ai"
title: "How to use the AI test zone to verify responses before going live"
category: "faq"
subcategory: "ai-assistant"
tags: ["test AI", "AI test zone", "test chatbot", "simulate customer", "test before activate", "AI preview"]
applies_when: "When a merchant asks how to test the AI assistant before turning it on for customers"
priority: "high"
```

## AI Test Zone

You can test your AI assistant without enabling it for customers. The test zone simulates customer interactions so you can verify responses before going live.

**Before testing, make sure you've:**
- Added data sources (FAQs, product info, etc.)
- Added custom instructions (tone, voice, response length)
- Set up other settings (bot name, avatar)

**To access the test zone:**
Go to **AI assistant** → **Test**

**How to test:**
1. In the chatbox, ask questions as if you were a customer
2. Use the provided question examples (click **Regenerate questions** for more)
3. Check each response carefully

**What to check:**
- Is the information correct?
- Is the tone friendly but professional?
- Are product details accurate?
- Are prices and availability correct?
- Is the response length appropriate (not too long or too short)?

**Testing tips:**
- Test one topic at a time
- Ask the same question in different ways
- Try edge cases and unusual phrasings

You can also review which data sources the AI used to answer each question.

---

<!-- CHUNK: test-and-optimize-unresolved -->
```yaml
chunk_id: "faq__test-and-optimize-unresolved"
doc_id: "chatty-test-and-optimize-ai"
title: "How to fix AI responses using unresolved questions and response review"
category: "faq"
subcategory: "ai-assistant"
tags: ["unresolved questions", "AI wrong answers", "AI incomplete answers", "fix AI", "improve AI", "add answer", "AI review sources"]
applies_when: "When a merchant asks how to fix incorrect AI responses or improve the AI using unresolved questions"
priority: "high"
```

## Unresolved Questions

Unresolved questions are customer inquiries the AI couldn't answer effectively. They appear when customers click "Talk to a person" (or equivalent reply button).

Only questions from the past 30 days are shown.

**How to optimize unresolved questions:**

1. Go to **AI assistant** → **Unresolved questions**
2. Look for patterns — group similar questions to identify gaps in training data
3. For each question, click **Add answer** → Enter your answer
4. Answers are added to your data sources (in the Questions list)
5. Go back to **Test zone** and ask the same question to confirm AI can now handle it

For spam or duplicate questions, click **Ignore** to remove from the list.

## AI Response Review

Each AI response in the test zone includes a **Review sources** button showing what data was used.

Use this to:
- Add missing product information
- Correct inaccurate policy details
- Expand on partial answers
- Add question variations that weren't understood

**What to do when you spot a problem:**
1. Click **Add relevant data** in the response
2. You'll be redirected to data sources to add the right information
3. Watch for patterns — if you're repeatedly adding the same type of info, create comprehensive entries on that topic
