---
title: "The Systems That Let Me Run a Business with a Team in a Small Town"
description: "Aflou has no co-working spaces, no reliable courier aggregation, and no tech talent pool. Here's how we built systems that work anyway."
pubDate: 2026-07-21
tags: ["business", "operations", "team", "algeria", "systems"]
---

I run my e-commerce business from Aflou, a town in Laghouat (wilaya 3). It's not a business hub. There are no co-working spaces, no delivery aggregators, and finding someone who knows how to use a spreadsheet is harder than finding a good domain.

But we built systems that work anyway. We have a team of friends processing 30+ orders a day, coordinating deliveries, and managing inventory. All from a town where most businesses still use paper notebooks.

Here's what makes it work.

## The Problem: Small Town Operations Don't Scale

When we started, everything was ad-hoc:

- Orders came through WhatsApp (personal messages to whoever was free)
- Someone would pack it, someone else would deliver it, no one tracked it
- Inventory was "what's in the room" -- we'd run out of stock without knowing
- Money was "give me the cash from yesterday" -- no separation of business and personal

It worked for 5 orders a day. At 20 orders, it broke. We had double-shipped orders, lost packages, and arguments about who was responsible.

## The Systems That Fixed It

We implemented three simple systems. Not software -- systems.

### 1. The Shared Order Log (Replaces Memory)

Every order goes into a shared Google Sheet. Columns:
- Date, customer name, phone, wilaya, address
- Product, quantity, price, delivery cost
- Status (new → confirmed → packed → shipped → delivered → returned)
- Who handled it

The rule: if it's not in the sheet, it doesn't exist. No exceptions. No one can say "I thought someone else was handling it."

This one rule eliminated 90% of our operational errors.

### 2. The Morning Huddle (Replaces Chaos)

Every morning at 9 AM, we have a 10-minute WhatsApp voice call:
- What's going out today (packing list)
- What came back yesterday (returns and COD failures)
- What's running low (inventory alerts)
- Who's doing what today (role assignment)

That's it. 10 minutes. Everyone knows their job for the day. No one asks "what should I do?" because we already decided.

### 3. Cash Separation (Replaces Confusion)

We have a cash box with an opening balance. Every sale goes in. Every expense comes out with a receipt. At the end of each day, we count the box and reconcile against the order log.

This sounds basic, but you'd be surprised how many small businesses in Algeria mix business and personal cash. We stopped having "where did the money go?" discussions entirely.

## Why Simple Systems Beat Fancy Software

I build software for a living. But for my own team, I chose Google Sheets and WhatsApp over a custom app.

Why:
- **Zero learning curve.** Everyone already knows WhatsApp. A custom app requires training.
- **Accessible from any phone.** Google Sheets works on $50 Android phones. No app installation needed.
- **Easy to change.** If a column is wrong, I edit it immediately. No developer needed.
- **Costs nothing.** No monthly subscription, no hosting fees.

The software comes later, when the system is proven and the volume justifies it.

## How You Can Do It Too

**For any team of 3-10 people in a non-tech environment:**

1. **Pick one operational problem** (orders, inventory, cash, or tasks). Fix it before moving to the next.

2. **Use tools they already have.** WhatsApp + Google Sheets + a physical notebook. Introduce one digital tool at a time.

3. **Write the rule down.** "Every order goes in the sheet before packing." Post it in the workspace. Repeat it daily.

4. **Reconcile daily.** 10 minutes at the end of each day to check: orders shipped vs cash collected. If they don't match, investigate immediately.

5. **Review weekly.** What broke this week? What needs to change? The system should evolve.

## When This Doesn't Work

If you have 50+ orders a day, Google Sheets becomes slow. You need a database-backed system at that volume. But the systems (the rules and processes) remain the same -- the tool just changes.

If your team doesn't read WhatsApp messages reliably, you need in-person communication or a different channel. WhatsApp only works if people check it.

*Related: [Daily Routine Three Businesses](/articles/daily-routine-three-businesses/)*

##s

### Q: What if my team doesn't use Google Sheets?
A: Start with a shared notebook (physical). Same system, different tool. Move to digital when they're ready.

### Q: How do I handle disagreements about who did what?
A: The order log is the source of truth. If it's not logged, it didn't happen. This removes the "I thought..." arguments.

### Q: Should I build a custom app for my team?
A: Not until the manual system is proven. If the manual system works, software will improve it. If the manual system is broken, software just automates the chaos.

### Q: What's the one system I should implement first?
A: The order log. Know what you sold, to whom, and where it is right now. Everything else builds on this.

---

*Related: [WhatsApp Order Chaos](/articles/whatsapp-order-chaos/) -- the problem before the system. [Delivery Costs Are Eating Your Margins](/articles/delivery-costs-margins/) -- the financial side of operations.*
