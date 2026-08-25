# Bot Corrections — Joyce (Joy)

**Tuần:** 24/08/2026 → 25/08/2026  ·  **Tổng correction:** 3

> Đây là các câu bot trả bị CS sửa trong tuần. Dùng để update KB/training data cho bot.

## 📌 Tóm tắt theo topic

### points/earning — 3 câu
- Hi there, Eve here!  Just a quick question to double check. Redeeming points wont affect the rank of the customer, right?
- bulk assign VIP tier by CSV?
- bulk assign VIP tier by CSV?

**Người sửa:** hieunm02@avadagroup.com (3)

---

## 📋 Chi tiết từng correction

### 1. [points/earning] — hieunm02@avadagroup.com · 24/08 15:35

**Q:** Hi there,
Eve here!

Just a quick question to double check.
Redeeming points wont affect the rank of the customer, right?

**Bot trả (sai/thiếu):**

```
It depends on the tier rule you're using. If tiers are based on Points earned, redeeming lowers the active balance and can demote a customer. If tiers are based on Amount spent or Number of orders, redemption doesn't affect the rank since it's based on cumulative spend/orders, not the current point balance.
```

**CS sửa thành:**

```
Wrong answer - redeem point không ảnh hưởng đến tier.
```

**Context:** Submitted via TS Elite by hieunm02@avadagroup.com · ref=crisp:session_1083ca8f-ee1c-4341-ad66-d6ceded9f158

_session: `session_1083ca8f-ee1c-4341-ad66-d6ceded9f158`_

### 2. [points/earning] — hieunm02@avadagroup.com · 25/08 14:11

**Q:** bulk assign VIP tier by CSV?

**Bot trả (sai/thiếu):**

```
Right now VIP tier assignment is manual only, there's no CSV bulk-upload option for tiers.
```

**CS sửa thành:**

```
Sai thông tin - Có thể dùng Import trong Customers để update VIP tier
```

**Context:** Submitted via TS Elite by hieunm02@avadagroup.com · ref=crisp:session_6d771360-b741-4f69-a78a-3e59b343d88e

_session: `session_6d771360-b741-4f69-a78a-3e59b343d88e`_

### 3. [points/earning] — hieunm02@avadagroup.com · 25/08 14:12

**Q:** bulk assign VIP tier by CSV?

**Bot trả (sai/thiếu):**

```
You'd need to assign each customer's tier individually at Joy Admin → Membership → VIP Tiers.
```

**CS sửa thành:**

```
Có thể bulk import qua Customers > Import > Update tier for existing customers
```

**Context:** Submitted via TS Elite by hieunm02@avadagroup.com · ref=crisp:session_6d771360-b741-4f69-a78a-3e59b343d88e

_session: `session_6d771360-b741-4f69-a78a-3e59b343d88e`_
