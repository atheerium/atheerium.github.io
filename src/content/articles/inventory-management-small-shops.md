---
title: "Inventory Management for Small Shops (Without Expensive Software)"
description: "Most inventory systems cost too much for small Algerian businesses. Here's a paper-to-digital system that scales from 10 products to 500."
pubDate: 2026-07-21
tags: ["business", "ecommerce", "inventory", "operations", "algeria"]
---

Running out of stock on a popular product is lost revenue. Overstocking a product that doesn't sell is wasted capital. For a small business in Algeria, both mistakes can hurt for months.

But most inventory management software costs $50-200/month and is designed for businesses with warehouses and barcode scanners. A small shop with 50 products doesn't need that.

Here's the system I use, starting with paper and graduating to digital when volume requires it.

## The Problem: "We Still Have Some" Is Not Inventory Management

Before I had a system, inventory was in people's heads. "I think we still have some of those." "Did we order more?" "How many did we sell last week?"

At 10 orders/day, this works-ish. At 30 orders/day, it breaks:
- You accept an order for a product you already sold out of
- You have to call the customer and cancel
- They don't order again
- You lost a customer because you didn't know your stock level

## Stage 1: Paper System (0-20 Products)

Write each product on an index card. On the card:
- Product name and supplier
- Cost price and selling price
- Current stock (update with every sale or delivery)

Keep cards in a box, organized by category. Every morning, count the cash and check it against sales. If a product sells out, order more that day.

**When to upgrade:** When you have more than 20 products and can't find the right card fast enough.

## Stage 2: Spreadsheet System (20-100 Products)

Move to Google Sheets. Columns:
- Product name
- Category
- Supplier
- Cost price
- Selling price
- Current stock
- Minimum stock (reorder point)
- Supplier contact

When stock hits the minimum, order more. This is automated conditionally formatting: green = OK, yellow = reorder soon, red = reorder now.

**When to upgrade:** When you have more than 100 products or 3+ people entering data.

## Stage 3: Simple Software (100-500 Products)

At this volume, a spreadsheet becomes slow. But you don't need expensive software. A simple database with 5 tables handles it:

- Products (name, category, supplier, cost, price)
- Stock movements (date, product, quantity change, reason)
- Orders (customer, products, quantity, status, payment)
- Suppliers (name, contact, lead time)
- Inventory count (periodic physical count vs system count)

I built this for $0 using Supabase free tier (see [this guide](/articles/supabase-free-tier/)). It took 2 weekends.

## How You Can Do It Too

1. Start with paper if you have <20 products
2. Move to Google Sheets at 20 products
3. Add automated reorder alerts at 50 products
4. Build or buy simple software at 100+ products
5. Never buy expensive inventory software unless you have 1,000+ SKUs

## FAQs

### Q: How often should I count physical inventory?
A: Monthly for fast-moving products. Quarterly for slow-moving ones. Annual for everything.

### Q: What's the most common inventory mistake?
A: Not accounting for damaged or returned products. A product that comes back damaged is still "in stock" in your system but unsellable. Track returns separately.

### Q: How much safety stock should I keep?
A: 2 weeks of average sales for imported products (long lead time). 1 week for locally sourced products.

### Q: What's the minimum stock level rule?
A: When stock hits 2 weeks of average sales, reorder. This gives you time for delivery delays.

---

*Related: [The Real Cost of Running an E-commerce Business in Algeria](/articles/ecommerce-costs-algeria/) -- the full cost breakdown. [WhatsApp Order Chaos](/articles/whatsapp-order-chaos/) -- managing orders without a system.*
