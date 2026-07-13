# Bug report — Joy Loyalty page: earning program titles không dịch trên storefront (hiện tiếng Anh)

**App:** Joy Loyalty
**Surface:** Storefront Loyalty page (Widget V4) — theme page `/pages/...`
**Severity:** Medium–High (mọi store multi-language dùng loyalty page V4 có khả năng dính; số store dính > số store báo)
**Reported by merchant:** arlos.hk (`1d55gq-vj.myshopify.com`, shopId `98135081277`)
**Repro URL:** https://www.arlos.hk/zh-hant/pages/arlos-club

---

## Triệu chứng

Trên loyalty page tiếng Trung phồn thể, phần "獲得A Points 的方法" hiển thị đúng tiếng Trung (system string OK), **nhưng title các earning card vẫn là tiếng Anh gốc**: "Signup Bonus", "Order Reward", "5 Stars Google reviews", "Celebrate a birthday", "Follow on Facebook", "Follow on Instagram".

**Không phải merchant chưa dịch.** Merchant đã điền đủ bản dịch trong App translation. Data dịch có sẵn trong metafield của store:

```
Signup Bonus          → translateTitle: {"zh-TW":"註冊獎勵"}
Order Reward          → translateTitle: {"zh-TW":"訂單獎勵","zh-CN":"订单奖励"}
5 Stars Google reviews→ translateTitle: {"zh-CN":"5 星 Google 评论","zh-TW":"五星 Google ..."}
...
translateDescription  → {"zh-TW":"歡迎加入本計畫","zh-CN":"欢迎加入此计划"} (cũng có)
```

→ Đây là **bug render/resolve**, không phải thiếu data.

---

## Môi trường store (lấy từ live page)

| Field | Value |
|-------|-------|
| `Shopify.locale` | `zh-TW` (có chỗ trong payload là lowercase `zh-tw`) |
| URL path | `/zh-hant/` |
| `primaryLanguage` | `en` |
| `plan` | `advanced_2026` |
| `translation.detectMethod` | `optionalStorefrontLanguage` |

---

## Code path đã trace (branch master)

**File render title:** `packages/scripttag/v4-adapters/loyalty-page/LoyaltyPageAdapter.js`

Title earn card được resolve tại **dòng 2390** (và 2902):

```js
program?.translateTitle?.[this._getDetectLocale()] || program.title || ''
```

`_getDetectLocale()` (dòng 2779) → `joyInstance.detectLocale(detectMethod)` → `ApiManager.getLocale()`:

`packages/scripttag/src/managers/ApiManager.js` dòng ~324:
```js
getLocale = async (detectMethod) => {
  if (detectMethod === DETECT_LANGUAGE_BY_OPTIONAL_STOREFRONT_LANGUAGE) {
    return window.Shopify.locale || this.primary;   // → "zh-TW"
  }
  ...
}
```

Và gate ở `Joy.js` `getDetectLocale`:
```js
const canUseDetectedLanguage = isPremium(shop, PLAN_TIER_1) || shop?.allowDetectedLanguage;
if (!canUseDetectedLanguage) return '';
return apiManager.locale !== apiManager.primary ? apiManager.locale : '';
```

---

## Root cause (hai điểm nghi vấn, dev repro với store để chốt)

Điểm chung: **lookup title là exact-match, KHÔNG có normalize và KHÔNG có fallback `split('-')[0]`.**

So sánh: cùng file, **tier name** ở dòng 682 CÓ fallback base-language:
```js
r.translateTitle?.[locale] || r.translateTitle?.[locale.split('-')[0]];   // tier: có fallback
```
Nhưng **earn program title** ở dòng 2390/2902 thì KHÔNG:
```js
program?.translateTitle?.[this._getDetectLocale()] || program.title;      // earn: không fallback
```

→ Nếu `detectLocale` trả về value không khớp CHÍNH XÁC key `zh-TW`, title rơi thẳng về tiếng Anh.

**Nghi vấn 1 — casing.** Shopify serve `Shopify.locale` có lúc `zh-TW`, có lúc `zh-tw` (thấy cả 2 trong payload arlos.hk). Key metafield là `zh-TW`. `translateTitle["zh-tw"]` ≠ `translateTitle["zh-TW"]` → miss. Không có `.toLowerCase()`/normalize ở lookup.

**Nghi vấn 2 — script subtag `zh-hant`/`zh-hans`.** URL Shopify dùng `zh-hant` (BCP-47 script subtag) trong khi Joy lưu region subtag `zh-TW`/`zh-CN`. Nếu ở path nào đó `detectLocale` nhận `zh-hant`:
- `translateTitle["zh-hant"]` → miss
- không có fallback → miss (mà kể cả có `split('-')[0]` = `zh` cũng miss vì key là `zh-TW`, không phải `zh`)
- → tiếng Anh.

Grep toàn repo Joy: **không có** mapping `zh-hant → zh-TW` / `zh-hans → zh-CN` ở đâu cả.

---

## Đề xuất fix

1. **Chuẩn hoá earn title lookup giống tier** — thêm fallback `split('-')[0]` tại dòng 2390 & 2902:
   ```js
   const loc = this._getDetectLocale();
   program?.translateTitle?.[loc]
     || program?.translateTitle?.[loc.split('-')[0]]
     || program.title || ''
   ```
2. **Case-insensitive match** cho locale key (map key metafield về canonical, hoặc lowercase 2 đầu khi so).
3. **Map script subtag** `zh-hant ↔ zh-TW`, `zh-hans ↔ zh-CN` ở `getLocale()`/`detectLocale` (Shopify Markets storefront dùng `zh-hant`/`zh-hans`).

Fix (1) một mình đã cứu phần lớn case region-subtag; (2)(3) xử lý nốt casing + script-subtag.

---

## Cách repro nhanh cho dev

1. Mở https://www.arlos.hk/zh-hant/pages/arlos-club (guest).
2. Console: `window.Shopify.locale` → xem casing thực tế lúc widget đọc.
3. Console: kiểm `window.AVADA_JOY.program.earning[0].translateTitle` → thấy key `zh-TW` có data.
4. So value `_getDetectLocale()` trả ra với key đó → sẽ thấy mismatch (casing hoặc `zh-hant`).
