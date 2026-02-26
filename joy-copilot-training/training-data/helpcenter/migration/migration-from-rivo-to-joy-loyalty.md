---
category: Migration
topic: Migration From Rivo To Joy Loyalty
source: helpcenter
---

Q: What is Migration From Rivo To Joy Loyalty in Joy Loyalty?
Q: How does Migration From Rivo To Joy Loyalty work?
Q: How do I migrate to Joy from Rivo?
A: ### Which Customer Data Can Joy Migrate?

- **Customer Name:** Full name of the customer.
- **VIP Tier Name:** The customer’s rank tier in your loyalty program.
- **Birth Date:** The customer’s birthday.
- **Points Balance:** The current points balance the customer holds.
- **Email:** The customer’s email address.

### What do you need to prepare for the migration?

File format

You need to prepare a CSV file containing the list of your store's loyal customers

**Note**: If the customer list exported from the loyalty program managed by Rivo is missing the VIP tier field, you can contact the Rivo team for support in exporting the customer file with all necessary fields

### How to Migrate

1

Navigate to the `Customer`→ choose `Import` → `Migration`

2

Select `Migrate my loyalty program from: Rivo`

3

`Upload your loyalty customer data file`

4

Once uploaded, let's select the data to import

5

`Match your data` columns to Joy attributes

6

`Set up VIP Tier rules`

7

`Select migration method and start Migration`

8

Wait for the migration process to complete

9

Review your migrated customer loyalty data in the `Customer` section to ensure everything has transferred correctly.

**Last step:** Recheck your migration progress and fix Failed Import customers:

- **Successful Imports:** Number of customers successfully migrated.
- **Failed Imports:** Number of customers not migrated due to errors.

To resolve failed imports, download the **failed\_import** file, make corrections, and upload the file again for review.

**How to handle file errors and fix values for re-uploading**

After Joy Loyalty reads your file and reports the number of successful and failed customer imports, follow these steps to ensure no customers are missed:

1. Download the processed file from the **FailedImports** section.
2. Open the file (a spreadsheet) and apply a filter on the **Status** column to display only the failed customers.
3. Review the error messages and correct the failed values.
4. Re-upload the corrected file and review the data again to ensure all customers are successfully imported.

### Overall

Migrating from Rivo to Joy Loyalty is a simple process that retains essential data. Following these steps will help you complete the migration without disruption to your loyalty program.

If you encounter any issues during the migration process, don't hesitate to contact our support team.