# Train AI

<!-- CHUNK: train-ai-planning -->
```yaml
chunk_id: "faq__train-ai-planning"
doc_id: "chatty-train-ai"
title: "How to plan and organize AI training content for best results"
category: "faq"
subcategory: "ai-assistant"
tags: ["train AI", "AI training", "training data", "AI data sources", "AI wrong answers", "improve AI accuracy", "AI best practices"]
applies_when: "When a merchant asks how to train their AI assistant effectively or why their AI gives wrong answers"
priority: "high"
```

## AI Training Overview

AI training is the process of teaching your AI assistant to understand your business and respond accurately to customer questions. High-quality, relevant data produces the best results.

## Step 1: Plan Your Training Content

Organize information into categories before you start adding data:

| Content category | What to include | How to add |
|---|---|---|
| Product information | Details, specs, variants, pricing | Sync products; add FAQs per product |
| Store information | Business hours, contact details, locations | Sync store data |
| Shipping & delivery | Methods, costs, delivery times | Sync FAQs or add custom Q&A |
| Returns & refunds | Policy details, steps, timeframes | Sync FAQs or add custom Q&A |
| Product-specific topics | Care instructions, warranties, compatibility | Add Q&A to custom data source or per product |
| Special scenarios | Holiday shipping, seasonal sales, event policies | Go to Instructions → Add custom scenarios |

## Step 2: Best Practices per Data Source

**Products:**
- Write detailed product descriptions with specifications
- Use consistent naming for variants
- Keep pricing updated
- For specific product recommendations, create Smart recommendations

If you sync Markets data, AI can answer region-specific questions about pricing and availability, and send product links with regional variations.

**Limitations to be aware of:**
- AI cannot identify bestsellers without Smart recommendations
- AI can only suggest complementary products if they're mentioned in product descriptions

---

<!-- CHUNK: train-ai-instructions -->
```yaml
chunk_id: "faq__train-ai-instructions"
doc_id: "chatty-train-ai"
title: "How to add custom instructions and scenario instructions to the AI"
category: "faq"
subcategory: "ai-assistant"
tags: ["custom instructions", "scenario instructions", "AI personality", "AI tone", "keyword triggers", "AI scenarios", "complaint handling"]
applies_when: "When a merchant asks how to add custom instructions or scenario-based instructions to control AI behavior"
priority: "high"
```

## Step 3: Add Custom Instructions

After adding data sources, customize how AI communicates:

- **Name & avatar**: How your bot appears to customers
- **Welcome message**: First message in chat
- **Custom instructions**: AI's personality, tone, role, and response boundaries
- **AI skills**: Shopping skills and customer support skills

## Step 4: Add Scenario Instructions

Scenario instructions train AI to handle specific situations when customers use certain keywords.

**How to add a scenario:**

1. Go to Instructions → Scenarios
2. **Name your scenario** — e.g., "Product return request", "Shipping delays"
3. **Set keywords** — words that trigger this scenario (include variations and synonyms): e.g., "refund", "return", "money back", "send back"
4. **Write instructions** — specific guidance for AI when this scenario triggers (max 1000 characters)
5. **Set status** — Active or Inactive

**Common scenarios to set up:**
- Product recommendations
- Order returns and refunds
- Shipping inquiries
- Complaint handling
- Promotional offers
- Technical support

**Example scenario — Customer expressing strong dissatisfaction:**

Instructions:
1. Acknowledge frustration: "I understand how disappointing this must be"
2. Apologize sincerely
3. Offer immediate solutions: refund, exchange, or store credit
4. Escalate to human: connect with a team member who can resolve this personally
5. Never argue — focus only on solutions

---

<!-- CHUNK: train-ai-custom-instructions-writing -->
```yaml
chunk_id: "faq__train-ai-custom-instructions-writing"
doc_id: "chatty-train-ai"
title: "How to write good custom instructions — structure and example"
category: "faq"
subcategory: "ai-assistant"
tags: ["write AI instructions", "custom instructions example", "AI role", "AI knowledge", "AI avoid", "AI instruction format", "generate with AI"]
applies_when: "When a merchant asks how to write good custom instructions or what format to use"
priority: "medium"
```

## How to Write Good Custom Instructions

Yes — custom instructions let you shape AI's personality, role, response style, and what it should or shouldn't say.

**Structure your instructions clearly, for example:**

```
ROLE:
- Act as a helpful customer support associate for [Store Name]
- Refer to yourself as "I" and the store as "we"

KNOWLEDGE:
- You know about our products, policies, and pricing
- If you don't know something, say so and suggest contacting our team

APPROACH:
- Keep responses conversational but professional
- Include product details (dimensions, materials, colors) when relevant
- Suggest complementary products when appropriate

AVOID:
- Don't make definitive claims about exact stock levels
- Don't promise specific delivery dates
- Don't make up product specifications
```

You can manually write instructions or use the **Generate with AI** button to create a starting point based on your business type.
