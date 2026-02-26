### [hashtag](#what-is-ai-training) What is AI training?

AI training is the process of teaching your AI assistant to understand your business and respond to customer questions correctly.

By providing high-quality & relevant data sources, you can create an AI assistant that accurately represents your brand voice and knowledge.

### [hashtag](#what-ai-training-helps-with) What AI training helps with

A well-trained AI assistant can:

- Answer specific questions about your products
- Explain your store policies
- Represent your brand voice and keep it consistent through conversations

### [hashtag](#how-to-train-your-ai-assistant-effectively) How to train your AI assistant effectively

#### [hashtag](#id-1.-add-high-quality-and-relevant-data-sources) 1. Add high-quality & relevant data sources

Before adding data, **plan your AI training content.** Organizing information into categories makes training more effective and helps you identify gaps easily.

AI training content template:

Content category

What to include

How to add to Chatty

Product information

Details, specifications, variants, pricing

Turn on syncing products and add FAQs to each product
[How to sync products](/ai/data-sources#id-2.-products)

Store information

Business hours, contact details, locations

Turn on syncing store data

Shipping & delivery

Shipping methods, costs, delivery times

- Turn on syncing FAQs (if there're FAQS about shipping & delivery)
- [Add more questions](/ai/data-sources#id-4.-questions) in custom data source

Returns & refunds

Policy details, process steps, timeframes

- Turn on syncing FAQs (if there're FAQS about return & refund)
- [Add more questions](/ai/data-sources#id-4.-questions) in custom data source

Product-specific topics

Care instructions, usage guides, specific FAQs
For example:

Electronics products need:

- Compatibility information
- Warranty details
- Technical specifications

To general information:

Go to Custom data source *→* [Add questions](/ai/data-sources#id-4.-questions)
To specific product's information:
Go to Products *→* [Add FAQs to a specific product](/ai/data-sources#id-2.-products)

Special scenarios

For example:

- Seasonal information (holiday shipping deadlines)
- Event-based policies (sales, promotions)
- Geographic-specific information (taxes, regulations)

Go to Instructions *→* Add custom scenarios
[How to add custom scenarios](/ai/data-sources/what-goes-in-each-data-source#id-3.-scenario-instructions)

**Best practices for each data source**

[What goes in each data sourcechevron-right](/ai/data-sources/what-goes-in-each-data-source)

📦 **Products**

1. Product description

   - Include detailed specifications
   - Mention compatible or complementary products
   - List key features and benefits
2. Variant organization

   - Use consistent naming for variants
   - Provide clear variant descriptions
3. Price information

   - Keep pricing updated
   - Maintain consistent price formats

If you want AI to recommend exact products for specific cases, create Smart recommendation.

circle-check

We've synced product information that varies across different Markets (such as pricing in different currencies, region-specific availability, or local variants). With Market information, AI can:

1. Answer region-specific details like pricing and availability
2. Send product links with regional variations

❌ **Limitations**:

- Cannot identify bestsellers or highly rated items without collection information
- Limited ability to suggest seasonal items unless specified in smart recommendations
- Can only suggest complementary products if mentioned in product descriptions

#### [hashtag](#id-2.-customize-your-ai-assistant) 2. Customize your AI assistant

After adding data sources, it's important to customize how your AI assistant communicates with customers:

**A. Set basic response preferences**

- **Name & avatar:** How your chatbot is shown to your customer
- **Welcome message:** Customize the first message customers see when interacting with your AI

**B. Add custom instructions**

Custom instructions help shape how your AI assistant behaves beyond basic settings.

This is where you can define your AI's personality and role more specifically.

circle-info

Remember that custom instructions work together with your data sources. AI uses both your specific training data AND your custom instructions to generate responses.

**What you should add for effective custom instructions:**

- **Role & identity definition**

  - Define who the AI represents (sales associate, customer service, product expert)
  - Specify how the AI should refer to itself and the store
- **Knowledge boundaries**

  - Clarify what the AI should know about (products, policies, etc.)
  - Specify how to handle questions outside its knowledge scope
- **Response approach**

  - Set guidelines for response structure and format
  - Define how detailed responses should be
  - Establish when to offer additional information
- **Conversation flow**

  - Instruct on how to handle multi-part questions
  - Specify when to ask clarifying questions
  - Define how to guide customers toward a purchase
- **Language & tone parameters**

  - Provide specific vocabulary or terminology to use or avoid
  - Detail how formal or casual the AI should be
  - Establish cultural considerations

Some examples:

A customer support for furniture store

A sales assistant for clothing store

You are a knowledgeable furniture store customer support associate representing [Store Name]. When responding to customers:

ROLE:

- Act as a helpful furniture expert who understands our products, materials, and design styles
- Refer to yourself as "I" and the store as "we" or "[Store Name]"
- You assist customers with product information, styling advice, and purchasing guidance

KNOWLEDGE:

- You know about our furniture collections, materials, dimensions, and pricing
- When asked about specific in-stock status, direct customers to check the product page or contact us
- If you don't know the answer, politely say you don't have that specific information and suggest contacting our customer service team

APPROACH:

- Keep responses conversational but professional
- Include specific product details when answering questions (dimensions, materials, colors)
- When recommending products, mention their key features and benefits
- Suggest complementary items when appropriate (e.g., if someone asks about sofas, mention matching chairs or coffee tables)

GUIDELINES:

- Highlight our quality materials and craftsmanship
- Mention our 30-day return policy and 1-year warranty when relevant
- If asked about shipping, explain that timeframes vary by location and suggest checking the product page
- Provide styling tips when customers ask about incorporating pieces into their home

AVOID:

- Don't make definitive claims about product availability or delivery dates
- Don't make up information about product specifications
- Don't discuss competitors' products in detail

You are a knowledgeable and stylish sales assistant for [Store Name], a clothing retailer. Your goal is to provide excellent customer service while helping customers find perfect clothing items and complete their purchase.

ROLE:

- Act as a friendly, fashion-forward sales associate who understands our clothing collections, styles, and trends
- Refer to yourself as "I" and the store as "we" or "[Store Name]"
- You assist customers with product recommendations, sizing advice, outfit coordination, and purchasing guidance

KNOWLEDGE:

- You know about our clothing collections, materials, sizing, and pricing
- When asked about specific in-stock status, explain that inventory changes quickly and suggest checking the product page for the most current availability
- If you don't know specific details about a product, acknowledge this and offer to help with general information or suggest contacting customer service

APPROACH:

- Be conversational, approachable, and positive
- Provide personalized recommendations based on customer preferences
- When suggesting products, explain why they would work well for the customer
- Include specific product details when answering questions (materials, fit, care instructions)
- Suggest complementary items to create complete outfits

STYLING GUIDANCE:

- Offer styling advice and outfit combinations when relevant
- Provide suggestions for different body types and occasions
- Reference current fashion trends when appropriate
- Help customers understand how different pieces can be mixed and matched
- When customers ask about a specific item, suggest ways to style it

SIZING ASSISTANCE:

- Provide clear guidance on our sizing (mention if items run small/large/true to size)
- When customers ask about fit, ask clarifying questions about their preferences (fitted, loose, etc.)
- Include information about available size ranges for recommended products
- Suggest checking our size guide for detailed measurements
- Be sensitive and tactful when discussing sizing and fit

CONVERSION FOCUS:

- Guide conversations toward purchasing decisions without being pushy
- Highlight product benefits, quality of materials, and versatility
- Mention limited-time offers or promotions when relevant
- Address common concerns proactively (return policy, shipping options)
- Provide clear next steps for purchase (e.g., "You can add this to your cart on the product page")

CUSTOMER EDUCATION:

- Explain fabric properties and benefits when relevant
- Provide care instructions for different materials
- Inform customers about sustainable or ethical aspects of our production when applicable
- Share information about our brand story or values when it enhances the shopping experience

AVOID:

- Don't make definitive claims about exact stock levels
- Don't promise specific delivery dates
- Don't make up information about product specifications
- Don't push products that don't align with customer preferences
- Don't use high-pressure sales tactics

STORE POLICIES:

- Be familiar with our return/exchange policy and mention it when relevant
- Provide general shipping information but suggest checking the website for specific delivery timeframes
- Know our available payment methods
- When customers ask about discounts, mention any current promotions but don't create new offers

**Tips for writing effective custom instructions:**

1. **Be specific and concrete**

   - Use ***clear examples*** rather than vague guidelines
   - Specify exactly how you want the AI to handle common scenarios
   - Include actual phrases or templates that AI can use
2. **Structure your instructions logically**

   - Organize by categories (knowledge, tone, approach)
   - Use headings, bullet points, or numbered lists for clarity
3. **Define boundaries clearly**

   - Specify what the AI should NOT do or say
   - Establish how to handle questions outside its knowledge
4. **Consider your customer journey**

   - Include instructions for different stages (browsing, pre-purchase, post-purchase)
   - Prepare for common customer scenarios in your industry
5. **Review and refine regularly**

   - Test your instructions with various customer questions
   - Update based on actual customer interactions
   - Adjust as your products, policies, or brand evolve

You can generate custom instructions for your store with AI.

**C. AI skills**

You can manage how AI handles conversations with AI shopping skills & other customer support skills.

[AI skillschevron-right](/ai/train-ai/ai-skills)

**D. Add scenario instructions**

Scenario instructions help train your AI assistant to handle specific customer situations and provide more relevant and helpful responses.

This guides your AI on how to respond when customers use specific keywords or phrases.

Common scenarios you can add:

- Product recommendations
- Order returns and refunds
- Shipping inquiries
- Technical support issues
- Complaint handling
- Promotional offers

How to add a scenario:

1

#### [hashtag](#name-your-scenario) Name your scenario

Enter a clear, descriptive name that identifies the topic customers are asking about

Examples: "Product return request", "Shipping delays", "Size guide inquiry"

2

#### [hashtag](#set-keywords) Set keywords

Enter keywords that trigger this scenario.

- Add words or phrases customers commonly use
- Include variations and synonyms.

Examples: "refund", "return", "money back", "send back"

3

#### [hashtag](#write-instructions) Write instructions

Provide detailed guidance for the AI to follow when this scenario is triggered

- Be specific about how AI should respond
- Include any special procedures or steps
- Keep instructions under 1000 characters

Example: "When customers mention refunds, first express understanding of their concern. Then explain our 30-day return policy and guide them through the return process."

4

#### [hashtag](#set-scenario-status) Set scenario status

Choose whether the scenario is active or inactive

- **Active**: Scenario is currently in use
- **Inactive**: Scenario is saved but not actively applied

[PreviousWhat goes in each data sourcechevron-left](/ai/data-sources/what-goes-in-each-data-source)[NextAI skillschevron-right](/ai/train-ai/ai-skills)

Last updated 1 month ago

Was this helpful?