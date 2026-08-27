# Joy Support Flow

> CS process specific to Joy Loyalty.

## Tra cứu khi khách báo lỗi

Khách **báo một lỗi/hiện tượng cụ thể** (không cộng điểm, coupon invalid, widget không hiện, perk không apply, sai tier, migrate lỗi…) → tra **FAQ tổng hợp theo domain** ở:

**→ [`playbooks/joy/joy-dfu-onboarding-playbook.md` — Phần 3](https://app.notion.com/p/avadagroup/Module-6-DFU-Onboarding-Playbook-FAQ-396b0da449f18167a149f4fa6474a92c)**

50 case theo 8 domain: **A** Points/Earning · **B** Coupon/Redeem · **C** Metafield/Perk · **D** Widget/V4 · **E** VIP tier · **F** Migration/Import · **G** Integration · **H** Config/plan.

Mỗi case: **Dấu hiệu → Tự chẩn đoán → Xử lý → Khi nào escalate**, kèm lăng kính triage 🟢 config · 🔵 đúng-thiết-kế · 🟠 3rd-party · 🔴 bug Joy. Nhớ: **51% ticket escalate hóa ra không phải bug Joy** → chạy hết lăng kính trước khi kêu dev.

## Onboarding một khách mới

Từ intake → launch (offer trên chat, tạo ticket, phân nhánh, xử lý issue) → **[`playbooks/joy/joy-onboarding-flow.md`](../../playbooks/joy/joy-onboarding-flow.md)**.
Kiến thức "làm thế nào / hiểu tại sao" (7 bước, migration, VIP, guest/member, Widget V4) → **[`playbooks/joy/joy-dfu-onboarding-playbook.md`](https://app.notion.com/p/avadagroup/Module-6-DFU-Onboarding-Playbook-FAQ-396b0da449f18167a149f4fa6474a92c)**.
