---
title: "I Was Losing Money on Every Order Until I Fixed My Pricing"
description: "Most Algerian e-commerce businesses don't know their real margins. Here's a simple profit calculator that shows you exactly which products and destinations are profitable."
pubDate: 2026-07-21
tags: ["business", "ecommerce", "algeria", "pricing", "margins"]
---

For the first 6 months of running my e-commerce business, I priced products by feel. I'd look at what I paid wholesale, add a markup, and call it a day. Some orders made money. Some lost money. I couldn't tell which was which.

The problem was I wasn't accounting for all the hidden costs between wholesale price and customer payment.

## The Problem: Hidden Costs Are Eating Your Profit

Here's what actually happens to every order:

```
Wholesale price:           1,000 DZD
+ Delivery (to customer):    400 DZD   (varies by wilaya!)
+ Delivery (return if COD):  400 DZD   (you pay this if customer rejects)
+ COD fee (courier charge):   50 DZD   (percentage of order value)
+ Packaging:                   50 DZD
+ WhatsApp time/scrolling:    100 DZD  (your time)
= Total cost:              2,000 DZD
```

If you're selling at 2,500 DZD, that's only 500 DZD profit on paper. But if the customer rejects it and you eat the return shipping, you lose 500 DZD.

Now imagine this happens on 10% of your orders. That 500 DZD profit on successful orders has to cover the 2,000 DZD loss on failed ones. Suddenly your margins are negative and you don't know why.

## Why Spreadsheets Fail

Every e-commerce business starts with a spreadsheet. But most spreadsheets:

- Don't account for variable delivery costs by destination
- Use a flat "10% for fees" instead of actual numbers
- Don't track return rates by product or by customer
- Are updated irregularly or by different people with different assumptions

The result: you think you're making 20% margin, but the bank account says otherwise.

## How I Fixed It

I built a profit calculator into my order management system. Every time I enter an order, it shows me the real margin:

**Input:**
- Product cost (wholesale)
- Selling price
- Destination wilaya (auto-calculates delivery cost)
- Weight (affects delivery price)
- Customer history (high return risk?)

**Output:**
- Delivery cost (auto, from rate card)
- COD fee (auto, percentage of order value)
- Packaging cost (fixed estimate)
- Return risk cost (factoring in customer's history)
- Total cost
- Profit margin in DZD and percentage

The system flagged something immediately: we were losing money on every order to wilayas 11 (Tamanrasset) and 47 (Ghardaïa) because delivery costs exceeded the profit margin. We raised prices for those destinations or stopped offering free shipping.

## How You Can Do It Too

**The manual version (works immediately):**

1. List every product you sell and your wholesale cost
2. For each destination wilaya, calculate:
   - Delivery cost per kg (from your courier's rate card)
   - Return probability (start with 10% of delivery cost)
   - COD fee (usually 1-3% of order value)
3. Add packaging and handling (50-100 DZD)
4. Total cost = product + delivery + return risk + COD fee + packaging
5. Minimum selling price = total cost + your target margin

**The automated version:** If you process 20+ orders a day, build or buy a system that calculates this automatically. A 30-second manual calculation becomes 10 seconds per order.

**The key insight:** Different wilayas have different profitability. Don't average them. Price each destination independently.

## When This Doesn't Work

If you sell digital products or services with no delivery cost, this framework doesn't apply. Your costs are different (hosting, time, tools).

If you do local pickup only, delivery costs don't affect your pricing. But most e-commerce businesses in Algeria ship somewhere.

## FAQs

### Q: What's a healthy profit margin for Algerian e-commerce?
A: 20-30% after all costs. If you're below 15%, you're one bad month away from losing money.

### Q: How do I reduce return rates?
A: Confirm orders before dispatch. Call the customer to verify their address and willingness to pay. This cuts returns by 50%.

### Q: Should I raise prices or cut delivery costs?
A: Both. Higher prices on products, accurate delivery pricing, and negotiating better rates with your courier. Don't subsidize delivery with product margins.

### Q: What's the biggest mistake in e-commerce pricing?
A: Ignoring wilaya-based delivery costs and treating all orders as equal. A 2,000 DZD order to Algiers is profitable. The same order to Tamanrasset loses money.

---

*Related: [Delivery Costs Are Eating Your Margins](/articles/delivery-costs-margins/) -- how to calculate per-destination delivery costs. [WhatsApp Order Chaos](/articles/whatsapp-order-chaos/) -- the operational systems that make pricing work.*

*Related: [Cod Killing Margins](/articles/cod-killing-margins/)*
