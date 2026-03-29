# Data Dictionary — Olist Brazilian E-commerce Dataset

## Overview

The Olist dataset contains 9 linked tables covering orders, customers, sellers,
products, payments, reviews, and geolocation. The core unit of analysis is the
order, which connects customers, sellers, products, and logistics data.

---

## Tables

### 1. olist_orders_dataset
**Rows:** 99,441 | **Columns:** 8
**Description:** The central table. One row per order. Links to customers,
items, payments, and reviews.

| Field | Type | Description |
|-------|------|-------------|
| order_id | string | Unique order identifier (primary key) |
| customer_id | string | Links to customers table |
| order_status | string | Order state: created, approved, shipped, delivered, cancelled |
| order_purchase_timestamp | datetime | When the customer placed the order |
| order_approved_at | datetime | When payment was approved (160 nulls — unpaid/cancelled orders) |
| order_delivered_carrier_date | datetime | When seller handed to carrier (1,783 nulls) |
| order_delivered_customer_date | datetime | When customer received order (2,965 nulls) |
| order_estimated_delivery_date | datetime | Original estimated delivery date |

**Data quality notes:**
- Nulls on delivery dates are expected for cancelled or in-progress orders
- No duplicate order_ids — each row is a unique order

---

### 2. olist_customers_dataset
**Rows:** 99,441 | **Columns:** 5
**Description:** One row per order-customer pair. Note: the same physical
customer can appear multiple times with different customer_ids.

| Field | Type | Description |
|-------|------|-------------|
| customer_id | string | Links to orders table (primary key in this table) |
| customer_unique_id | string | True unique customer identifier across orders |
| customer_zip_code_prefix | string | Links to geolocation table |
| customer_city | string | Customer city |
| customer_state | string | Customer state (2-letter Brazilian state code) |

**Data quality notes:**
- No nulls, no duplicates on customer_id
- Use customer_unique_id for repeat customer analysis, not customer_id

---

### 3. olist_order_items_dataset
**Rows:** 112,650 | **Columns:** 7
**Description:** One row per item within an order. Orders with multiple
items appear multiple times.

| Field | Type | Description |
|-------|------|-------------|
| order_id | string | Links to orders table |
| order_item_id | integer | Item sequence number within the order |
| product_id | string | Links to products table |
| seller_id | string | Links to sellers table |
| shipping_limit_date | datetime | Deadline for seller to hand item to carrier |
| price | float | Item price in BRL |
| freight_value | float | Freight cost for this item in BRL |

**Data quality notes:**
- 13,984 duplicate order_ids — expected, reflects multi-item orders
- No nulls

---

### 4. olist_order_payments_dataset
**Rows:** 103,886 | **Columns:** 5
**Description:** One row per payment entry per order. Orders paid in
installments or with multiple methods appear multiple times.

| Field | Type | Description |
|-------|------|-------------|
| order_id | string | Links to orders table |
| payment_sequential | integer | Payment sequence number within the order |
| payment_type | string | Payment method: credit_card, boleto, voucher, debit_card |
| payment_installments | integer | Number of installments chosen |
| payment_value | float | Value of this payment entry in BRL |

**Data quality notes:**
- 4,446 duplicate order_ids — expected, reflects installment payments
- No nulls

---

### 5. olist_order_reviews_dataset
**Rows:** 99,224 | **Columns:** 7
**Description:** Customer satisfaction reviews linked to orders.

| Field | Type | Description |
|-------|------|-------------|
| review_id | string | Unique review identifier |
| order_id | string | Links to orders table |
| review_score | integer | Rating from 1 (worst) to 5 (best) |
| review_comment_title | string | Optional review title (87,656 nulls — 88.3%) |
| review_comment_message | string | Optional review body (58,247 nulls — 58.7%) |
| review_creation_date | datetime | When the review was created |
| review_answer_timestamp | datetime | When Olist responded |

**Data quality notes:**
- High null rate on comment fields is expected — most customers only leave a score
- 814 duplicate review_ids — flag for investigation during preprocessing

---

### 6. olist_products_dataset
**Rows:** 32,951 | **Columns:** 9
**Description:** Product catalog with category and dimension attributes.

| Field | Type | Description |
|-------|------|-------------|
| product_id | string | Unique product identifier (primary key) |
| product_category_name | string | Category in Portuguese (610 nulls — 1.9%) |
| product_name_lenght | integer | Character count of product name (note: typo in source data) |
| product_description_lenght | integer | Character count of description (note: typo in source data) |
| product_photos_qty | integer | Number of product photos |
| product_weight_g | float | Product weight in grams (2 nulls) |
| product_length_cm | float | Product length in cm (2 nulls) |
| product_height_cm | float | Product height in cm (2 nulls) |
| product_width_cm | float | Product width in cm (2 nulls) |

**Data quality notes:**
- Column names `product_name_lenght` and `product_description_lenght` contain
  a typo present in the original Olist data — preserve as-is for consistency
- 610 products missing category — assign to "unknown" during preprocessing

---

### 7. olist_sellers_dataset
**Rows:** 3,095 | **Columns:** 4
**Description:** Seller registry with location data.

| Field | Type | Description |
|-------|------|-------------|
| seller_id | string | Unique seller identifier (primary key) |
| seller_zip_code_prefix | string | Links to geolocation table |
| seller_city | string | Seller city |
| seller_state | string | Seller state (2-letter Brazilian state code) |

**Data quality notes:**
- No nulls, no duplicates
- Clean table, ready to join as-is

---

### 8. olist_geolocation_dataset
**Rows:** 1,000,163 | **Columns:** 5
**Description:** Latitude and longitude coordinates mapped to Brazilian
zip code prefixes.

| Field | Type | Description |
|-------|------|-------------|
| geolocation_zip_code_prefix | string | Brazilian zip code prefix (5 digits) |
| geolocation_lat | float | Latitude |
| geolocation_lng | float | Longitude |
| geolocation_city | string | City name |
| geolocation_state | string | State code |

**Data quality notes:**
- 981,148 duplicate zip code prefixes — expected, multiple coordinates per zip
- Use aggregation (mean lat/lng per zip) when joining to customers or sellers

---

### 9. product_category_name_translation
**Rows:** 71 | **Columns:** 2
**Description:** Maps Portuguese product category names to English equivalents.

| Field | Type | Description |
|-------|------|-------------|
| product_category_name | string | Category name in Portuguese |
| product_category_name_english | string | Category name in English |

**Data quality notes:**
- No nulls, no duplicates
- 71 categories covered — join to products on product_category_name

---

## Join Key Map

| Left Table | Right Table | Join Key |
|------------|-------------|----------|
| orders | customers | customer_id |
| orders | order_items | order_id |
| orders | order_payments | order_id |
| orders | order_reviews | order_id |
| order_items | products | product_id |
| order_items | sellers | seller_id |
| order_items | order_payments | order_id |
| order_items | order_reviews | order_id |
| order_payments | order_reviews | order_id |
| products | category_translation | product_category_name |
| customers | geolocation | customer_zip_code_prefix → geolocation_zip_code_prefix |
| sellers | geolocation | seller_zip_code_prefix → geolocation_zip_code_prefix |