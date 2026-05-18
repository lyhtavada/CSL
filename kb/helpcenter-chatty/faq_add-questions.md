# Adding and Managing FAQ Questions

<!-- CHUNK: add-questions-overview -->
```yaml
chunk_id: "faq__add-questions-overview"
doc_id: "chatty-add-questions"
title: "How to add, edit, and manage FAQ questions in Chatty"
category: "faq"
subcategory: "build-faqs"
tags: ["add faq", "create faq", "faq questions", "edit faq", "delete faq", "reorder faq", "featured question"]
applies_when: "When a merchant asks how to add or manage individual FAQ questions"
priority: "medium"
```

## How to Add a New Question

After creating a category, you can add questions to it.

1. Go to **FAQs**
2. Click **Add new** → **Add FAQ**
3. Enter the question and answer
4. Configure settings:
   - **Status**: Published or Draft
   - **Category**: Select which category this question belongs to (required)
   - **Featured question**: If enabled, the question shows on the first page of the chatbox
5. Click **Save**

## How to Manage Questions

- **Edit a question**: Hover over it and click the edit icon
- **Delete a question**: Hover over it and click the delete icon
- **Reorder questions**: Drag and drop within a category
- **Feature/unfeature**: Star or unstar the question

---

<!-- CHUNK: add-questions-import-export -->
```yaml
chunk_id: "faq__add-questions-import-export"
doc_id: "chatty-add-questions"
title: "Import and export FAQ questions in bulk using CSV"
category: "faq"
subcategory: "build-faqs"
tags: ["import faq", "export faq", "bulk faq", "csv import", "faq csv", "bulk upload"]
applies_when: "When a merchant asks how to import or export FAQs in bulk"
priority: "medium"
```

## Import FAQs in Bulk

You can import many questions at once using a CSV file.

**Get the sample file:**
Go to **FAQs** → **More actions** → **Import FAQs** → Download the sample CSV

**Fill in the CSV file:**
The file has 5 required fields (keep headers):
- Question
- Answer
- Category (name of the category the question belongs to)
- Published question: TRUE = published, FALSE = unpublished
- Featured question: TRUE = featured, FALSE = not featured

This CSV file is for importing FAQ questions only (not AI training data) — max file size: 1MB.

**Upload the file:**
Click **Import FAQs** → Drop your CSV file → Choose options:
- Overwrite FAQs that have the same questions
- Publish all new categories

## Export FAQs

Go to **FAQs** → **More actions** → **Export FAQs** → Select which FAQs to export → Click **Export**

The export file contains 7 fields: Question, Answer, Category, Published question, Featured question, Published category, Featured category.
