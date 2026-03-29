# KPI Definitions — Analytics Copilot

## Overview

These are the seven core KPIs the analytics copilot tracks, flags, and
summarizes. Every metric in the app and every generated narrative traces
back to one of these definitions.

---

## 1. Total Revenue

**Formula:** SUM(order_items.price) + SUM(order_items.freight_value)
**Source tables:** order_items
**Business intent:** Measures gross revenue generated across all delivered
orders. Includes product price and freight charges paid by customers.
**Expected range:** Varies by period. Monthly revenue in this dataset
ranges from ~R$50K to ~R$1.5M BRL.
**Segmentation:** By month, product category, seller, customer state.

---

## 2. Average Order Value (AOV)

**Formula:** SUM(payment_value) / COUNT(DISTINCT order_id)
**Source tables:** order_payments
**Business intent:** Tracks how much customers spend per transaction.
Rising AOV suggests upsell effectiveness or product mix shift.
Falling AOV may signal promotional discounting or basket shrinkage.
**Expected range:** R$100–R$200 BRL per order on average.
**Segmentation:** By category, payment type, customer state, time period.

---

## 3. Order Volume

**Formula:** COUNT(DISTINCT order_id) where order_status = 'delivered'
**Source tables:** orders
**Business intent:** Measures operational throughput. Used to track
growth trends, seasonality, and demand shifts.
**Expected range:** 500–8,000 delivered orders per month depending on period.
**Segmentation:** By day, week, month, customer state, product category.

---

## 4. Repeat Customer Proxy

**Formula:** COUNT(customer_unique_id) WHERE order_count > 1 /
COUNT(DISTINCT customer_unique_id)
**Source tables:** orders, customers
**Business intent:** Estimates the share of customers who placed more
than one order. True loyalty metric requires longer time windows.
**Note:** customer_id is not reused across orders — must use
customer_unique_id for repeat analysis.
**Expected range:** 1–5% repeat rate is typical for this dataset.
**Segmentation:** By customer state, first order category, acquisition period.

---

## 5. Fulfillment Latency

**Formula:** AVG(order_delivered_customer_date - order_purchase_timestamp)
**Source tables:** orders
**Business intent:** Measures end-to-end delivery time from purchase to
customer receipt. High latency drives poor reviews and cancellations.
**Expected range:** 10–20 days average across the dataset.
**Segmentation:** By seller, product category, customer state, carrier handoff date.

---

## 6. Seller Defect Proxy

**Formula:** COUNT(orders where review_score <= 2) /
COUNT(DISTINCT order_id) per seller
**Source tables:** orders, order_reviews, order_items
**Business intent:** Identifies sellers generating disproportionate
customer dissatisfaction. Used to flag sellers for intervention or review.
**Expected range:** Healthy sellers below 5% defect rate.
High-risk threshold: above 15%.
**Segmentation:** By seller_id, product category, time period.

---

## 7. Cancellation and Refund Proxy

**Formula:** COUNT(orders where order_status IN
('canceled', 'unavailable')) / COUNT(DISTINCT order_id)
**Source tables:** orders
**Business intent:** Tracks order failure rate. High cancellation rates
signal inventory issues, payment failures, or seller reliability problems.
**Expected range:** Below 5% is healthy. Spikes warrant investigation.
**Segmentation:** By seller, product category, payment type, time period.