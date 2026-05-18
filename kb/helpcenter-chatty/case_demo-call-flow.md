# Demo Call Request Flow

<!-- CHUNK: demo-call-eligibility -->
```yaml
chunk_id: "case__demo-call-eligibility"
doc_id: "cs-case-demo-call-flow"
title: "Demo Call — Eligibility Criteria and Who Qualifies"
category: "cs-process"
subcategory: "demo-call"
tags: ["demo call", "eligibility", "high potential", "AI training", "paid plan", "consultant"]
applies_when: "Merchant asks for a demo call or product walkthrough call"
priority: "high"
```

## Overview

Demo calls for Chatty are only available to eligible merchants.

## Eligibility Criteria (must meet ONE)

- **High potential merchant** — large GMV, high-value customer
- **Needs AI training guidance** — wants help with AI scripts, auto-reply, or chat scenarios
- **Considering a paid plan** — actively evaluating or comparing Chatty paid plans

---

<!-- CHUNK: demo-call-flow -->
```yaml
chunk_id: "case__demo-call-flow"
doc_id: "cs-case-demo-call-flow"
title: "Demo Call — Step-by-Step Handling Flow"
category: "cs-process"
subcategory: "demo-call"
tags: ["demo call", "flow", "booking link", "eligible", "not eligible", "redirect", "live chat", "insists"]
applies_when: "CS is handling a demo call request and needs to decide how to respond"
priority: "high"
```

## Resolution Steps

### Step 1 — Check eligibility

Does the merchant meet any eligibility criteria? (High GMV, needs AI training guidance, or considering paid plan)

### Step 2 — If eligible → send demo booking link

Send: https://cal.com/drake-q-fonihl/chatty-consultant

The sales/consultant team handles scheduling and conducting the demo. After the call, CS continues supporting the merchant if they have follow-up questions.

### Step 3 — If NOT eligible → redirect to live chat

> Thanks for your request. For troubleshooting or app setup, our support team will assist you directly via live chat so you can get step-by-step help in real time.

### Step 4 — If merchant insists on a call despite not being eligible

Send the booking link: https://calendly.com/lyht-avada/30min

If merchant is frustrated and insists, send this link and notify Liz in **#cs-group-2** for follow-up.

---

<!-- CHUNK: demo-call-after-call -->
```yaml
chunk_id: "case__demo-call-after-call"
doc_id: "cs-case-demo-call-flow"
title: "Demo Call — What CS Does After the Call Completes"
category: "cs-process"
subcategory: "demo-call"
tags: ["after demo", "post-call", "follow up", "sales team", "CS role"]
applies_when: "A demo call has been completed and CS needs to know what to do next"
priority: "low"
```

## After the Demo Call

- The **sales team** handles the call itself (scheduling, conducting the demo).
- **CS continues** to support the merchant if they have follow-up questions about usage, setup, or optimization.

No special action needed from CS unless the merchant reaches out again.
