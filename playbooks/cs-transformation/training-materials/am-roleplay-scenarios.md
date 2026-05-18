# AM Roleplay Scenarios — Chatty & Joy

> **Dùng cho:** Andy, Jade (Chatty) + Sonny, Alyssa (Joy)
> **Mục đích:** Luyện tập call trước khi gọi merchant thật
> **Người đóng merchant:** Liz (hoặc CS teammate)
> **Format:** Liz đọc scenario, agent chạy call. Debrief sau mỗi scenario.

---

## Cách dùng

1. **Liz chọn scenario** — không báo trước cho agent (để luyện phản ứng thật)
2. **Agent bắt đầu call** như thật — không được hỏi "tôi nên làm gì"
3. **Liz đóng merchant** theo tính cách trong scenario — cooperative hay khó tính tùy bài
4. **Sau call:** Liz debrief theo checklist bên dưới

### Debrief checklist sau mỗi scenario:

- [ ] Agent mở call tự nhiên chưa, hay nghe cứng / scripted?
- [ ] Agent discovery đủ chưa — hiểu được pain của merchant trước khi pitch?
- [ ] Agent có push back đúng lúc không, hay bị merchant dẫn dắt?
- [ ] Có bị stuck ở đâu không? Stuck ở đâu → đó là gap cần fill thêm kiến thức
- [ ] Tone có phù hợp không — quá formal / quá casual?
- [ ] Call có close được không? Next step có rõ ràng không?

---

## CHATTY — Scenarios

---

### Scenario C1: Paid plan, AI chưa setup (cooperative merchant)

**Tình huống:** Andy gọi cho merchant đã upgrade lên Basic 10 ngày trước nhưng AI chưa setup.

**Merchant profile:**
- Fashion accessories store, ~$1.2M revenue
- Team: owner + 1 CS người
- Pain: CS chỉ work giờ hành chính, miss nhiều messages buổi tối
- Cooperative, hơi busy nhưng sẵn sàng dành 20 min

**Liz đóng merchant với tính cách:** Friendly, bận, muốn setup xong nhanh. Không biết nhiều về AI — cần được hướng dẫn từng bước.

**Mục tiêu call:** Ra khỏi call với AI đang chạy + test 1 lần

**Bẫy Liz sẽ giăng:**
- Hỏi "AI có trả lời đúng sản phẩm của tôi không?" trước khi setup xong → agent phải biết cách demo
- "Tôi có 500 sản phẩm, AI có học hết không?" → Basic plan chỉ train 500 products

---

### Scenario C2: Free plan, nhiều traffic nhưng chưa thấy value

**Tình huống:** Jade gọi merchant đã cài Chatty 3 tuần, dùng free plan, có một ít conversations nhưng chưa thấy AI làm được gì.

**Merchant profile:**
- Home décor store, organic traffic chủ yếu
- Dùng Chatty free — 50 lifetime AI conversations gần hết
- Chưa add custom Q&A, chưa setup FAQ

**Liz đóng merchant với tính cách:** Skeptical nhẹ — "tôi thử rồi nhưng AI trả lời chung chung quá, không nói được về sản phẩm của tôi."

**Mục tiêu call:** Explain tại sao AI generic → walk through cách thêm Q&A + custom data → set expectation về free plan limit

**Bẫy:**
- "Nâng plan lên có đảm bảo AI tốt hơn không?" → không phải plan quyết định AI quality, là training data
- Nếu agent pitch upgrade sớm quá → merchant cảm thấy bị push

---

### Scenario C3: Merchant giận — AI trả lời sai cho khách

**Tình huống:** Andy nhận escalation: merchant nhắn tin trên chat complain AI đã recommend sản phẩm hết hàng cho khách. Khách complain. Merchant muốn tắt AI.

**Merchant profile:**
- Skincare brand, Pro plan
- AI đã chạy 2 tuần, phần lớn tốt nhưng 1 lần này sai

**Liz đóng merchant với tính cách:** Frustrated, muốn giải thích ngay lập tức. "Tôi không hiểu sao AI lại làm vậy, bây giờ tôi phải xin lỗi khách."

**Mục tiêu:** Không để merchant tắt AI — acknowledge lỗi, explain nguyên nhân, show cách fix + prevent

**Key info agent cần biết:**
- Products sync daily at 12AM PST — nếu sản phẩm out-of-stock trong ngày, AI vẫn có thể recommend đến midnight
- Fix: manual retrain hoặc exclude sản phẩm đó

**Bẫy:**
- Merchant hỏi "Avada sẽ bồi thường gì cho tôi không?" → không có compensation policy cho AI errors; agent cần handle expectation
- Merchant muốn AI chỉ recommend sản phẩm mà họ manually approve → có thể dùng Smart Recommendations collections thay vì full catalog

---

### Scenario C4: Merchant hỏi về upgrade, nhưng không rõ họ cần Pro không

**Tình huống:** Jade đang support call, merchant đang dùng Basic, hỏi "Pro có gì hơn không?"

**Merchant profile:**
- Pet supplies store, $800K revenue
- Basic plan: 50 AI conversations/mo — đang dùng hết nhanh
- Team 3 người

**Liz đóng merchant với tính cách:** Đang consider upgrade nhưng muốn justify cost. Không muốn bị oversell.

**Mục tiêu:** Qualify xem Pro có phù hợp không → recommend đúng, không push để bán

**Key differences Basic → Pro:**
- 300 vs 50 AI conversations/mo
- 8,000 vs 500 products trained
- Smart recommendations (Pro+)
- CSAT survey (Pro+)
- Cart booster (Pro+)

**Bẫy:**
- Nếu agent list hết features mà không hỏi merchant cần gì → merchant confused, không quyết được
- Merchant hỏi "tôi đang overpay không?" → honest answer quan trọng hơn upsell

---

### Scenario C5: Support call — Chatbox không hiện trên store (cold call in)

**Tình huống:** Merchant chat in hỏi "chatbox của tôi đột nhiên biến mất." Andy tiếp nhận và escalate thành call vì cần screen share để debug.

**Merchant profile:**
- Electronics accessories store
- Pro plan, đã dùng 2 tháng, trước giờ fine
- Hôm nay sau khi update theme thì chatbox biến mất

**Liz đóng merchant với tính cách:** Impatient — "khách đang vào store mà không thấy chat, tôi mất doanh thu từng phút."

**Mục tiêu:** Debug nhanh và chính xác, không để merchant chờ

**Checklist debug:**
1. App embed still on in Shopify theme editor?
2. Theme update có reset app embeds không? (Shopify behavior — update theme đôi khi tắt app embeds)
3. Display rules có accidentally exclude current page?
4. Chatbox toggle còn on?

**Bẫy:**
- Merchant đang stress → agent phải calm, methodical, không đoán mò
- Nếu agent không biết checklist → bị stuck, merchant càng frustrated

---

## JOY — Scenarios

---

### Scenario J1: Paid plan, loyalty program chưa launch (cooperative)

**Tình huống:** Sonny gọi cho merchant upgrade Professional 2 tuần trước nhưng program vẫn draft.

**Merchant profile:**
- Fitness apparel store, $1.5M revenue
- Muốn loyalty để tăng repeat purchase
- Biết về loyalty concept nhưng chưa biết Joy cụ thể

**Liz đóng merchant với tính cách:** Friendly, sẵn sàng học, có 20 min. Hơi lo về setup complexity.

**Mục tiêu call:** Launch program với Place Order earning rule + discount redemption rule trước khi kết thúc call.

**Bẫy:**
- "Tôi muốn setup VIP tiers luôn" → VIP cần Advanced plan, họ đang Professional → explain upgrade path
- "Điểm bao nhiêu là hợp lý?" → agent cần có gợi ý cụ thể (1 point/$1, 100 points = $5 off là starting point tốt)

---

### Scenario J2: Merchant migrate từ Smile, lo mất data khách

**Tình huống:** Alyssa gọi merchant đang dùng Professional plan, vừa quyết định migrate từ Smile.

**Merchant profile:**
- Beauty brand, 8,000 loyalty members trên Smile
- Đã có nhiều khách VIP — lo nhất là mất points history
- Professional plan: migration supported

**Liz đóng merchant với tính cách:** Careful, hỏi nhiều. "Tôi cần chắc chắn khách của tôi không mất điểm — nếu có 1 người complain về điểm bị mất thì tôi không dám migrate."

**Mục tiêu:** Build trust về migration process, walk through những gì Joy migrate được và không migrate được.

**Key info:**
- Joy migrate: name, email, points balance, VIP tier, birthday, status
- Không migrate: transaction history, custom fields ngoài những trường trên
- Process: export từ Smile → import CSV vào Joy
- Recommend: run parallel 1–2 ngày trước khi tắt Smile

**Bẫy:**
- "Joy có migrate transaction history không?" → không, chỉ current balance
- "Nếu có lỗi trong lúc migrate thì sao?" → Joy có support, nhưng agent không nên promise "không có lỗi gì hết"

---

### Scenario J3: Points không earn — merchant complain

**Tình huống:** Merchant chat in complain "3 khách vừa order nhưng không thấy điểm đâu." Sonny escalate thành call.

**Merchant profile:**
- Organic food store, Advanced plan
- Loyalty program live 1 tháng, phần lớn fine
- 3 orders hôm nay không earn points

**Liz đóng merchant với tính cách:** Frustrated nhẹ, lo khách complain. "Tôi không muốn phải manually adjust điểm cho từng người."

**Mục tiêu:** Debug nguyên nhân, fix, set expectation về manual adjustment nếu cần.

**Checklist debug:**
1. Earning rule đang on?
2. Ba customers đó có phải loyalty member không? (chưa join = không earn)
3. Orders có đủ điều kiện không? (minimum spend, specific products excluded?)
4. Pending points setting? (earn after fulfillment hay after payment?)
5. Orders bị tagged as B2B hoặc excluded customer segment?

**Bẫy:**
- "Tại sao app lại như vậy?" → đừng apologize thay app, explain logic cụ thể
- Merchant muốn "tự động add điểm cho tất cả orders luôn, kể cả guest checkout" → guest checkout không earn (customer phải có account)

---

### Scenario J4: Support call — VIP tier không tự update

**Tình huống:** Alyssa nhận case: merchant VIP tier của 1 khách không update lên Silver dù đủ điểm.

**Merchant profile:**
- Fashion brand, Advanced plan
- 3 VIP tiers: Bronze (0–500 pts), Silver (501–1500 pts), Gold (1500+ pts)
- 1 khách đã có 600 pts nhưng vẫn thấy Bronze

**Liz đóng merchant với tính cách:** Calm nhưng confused. "Khách đó complain với tôi — tôi phải giải thích cái gì đây?"

**Mục tiêu:** Debug + explain + xử lý cho case này + prevent cho tương lai.

**Key info:**
- Tier assessment không real-time — có schedule (daily / monthly / manually triggered)
- Check: tier assessment method là gì? (points earned / amount spent / number of orders?)
- Check: đang tính từ lúc nào? (all time hay rolling period?)
- Fix: manually trigger reassessment hoặc wait for next scheduled run

**Bẫy:**
- "Tại sao không real-time?" → explain design intent (performance), không phải lỗi
- Merchant muốn notify khách khi tier update → có notification setting, agent cần biết chỗ đó

---

### Scenario J5: Cold call — merchant free plan, loyalty program never launched

**Tình huống:** Sonny gọi cho merchant cài Joy 3 tuần, free plan, program chưa publish.

**Merchant profile:**
- Candle & home fragrance store
- ~$600K revenue, solo owner
- Không biết tại sao chưa publish — có thể overwhelmed

**Liz đóng merchant với tính cách:** Slightly hesitant. "Tôi chưa publish vì tôi không biết nên set points như thế nào, và tôi lo phức tạp quá."

**Mục tiêu:** Remove blocker (lo lắng về setup), giúp họ launch trong 15 min, không push upgrade.

**Bẫy:**
- Họ hỏi "free plan có đủ không?" → honest: free plan đủ để bắt đầu, nhưng nếu muốn VIP hay migration thì cần upgrade
- Agent không nên pitch Professional/Advanced nếu merchant chưa thấy value từ free

---

## Sau khi làm hết scenarios:

- **Round 1:** Scenarios báo trước → agent chuẩn bị
- **Round 2:** Scenarios ngẫu nhiên, không báo trước → test phản ứng thật
- **Round 3:** Mix + Liz thêm twist giữa chừng (VD: merchant đổi hướng, hỏi câu out of scope)
