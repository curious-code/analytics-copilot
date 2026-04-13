import pandas as pd
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from src.data_loader import load_all_tables

# convert string dates to actual dates
def clean_orders(orders):
    date_cols = ('order_purchase_timestamp', 'order_approved_at',
                 'order_delivered_carrier_date','order_delivered_customer_date',
                 'order_estimated_delivery_date')
    
    for date_col in date_cols:
        orders[date_col] = pd.to_datetime(orders[date_col])
    
    return orders

# build one master order table
def build_order_master(orders, customers, order_items, order_payments, order_reviews):

    # aggregate orders in order_items
    order_items_agg = order_items.groupby('order_id').agg(
        total_items=('order_item_id', 'count'),
        total_price=('price', 'sum'),
        total_freight=('freight_value','sum')
    ).reset_index()
    
    # aggregate payments in order_payments
    order_payments_agg = order_payments.groupby('order_id').agg(
        total_payments=('payment_value', 'sum')
    ).reset_index()
     
    # aggregate reviews in order_reviews
    order_reviews_agg = order_reviews.groupby('order_id').agg(
        avg_reviews=('review_score', 'mean')
    ).reset_index()
    
    # merge tables
    order_master = orders.merge(customers, on='customer_id', how='left')
    order_master = order_master.merge(order_items_agg, on='order_id', how='left')
    order_master = order_master.merge(order_payments_agg, on='order_id', how='left')
    order_master = order_master.merge(order_reviews_agg, on='order_id', how='left')

    return order_master

# build a seller summary table
def build_seller_summary(order_master, order_items):
    
    # extract useful columns from order_master
    seller_cols = order_master[['order_id', 'order_status', 'avg_reviews']]

    # merge tables
    seller_summary = order_items.merge(seller_cols, on='order_id', how='left')

    # summarize by seller
    seller_summary = seller_summary.groupby('seller_id').agg(
        total_orders=('order_id', 'nunique'),
        total_revenue=('price', 'sum'),
        avg_review_score=('avg_reviews','mean')
    ).reset_index()

    return seller_summary

# build a customer summary table
def build_customer_summary(order_master):
    
    # extract useful columns from order_master
    customer_cols = order_master[['order_id', 'customer_unique_id', 'total_payments', 'avg_reviews']]

    # summarize by seller
    customer_summary = customer_cols.groupby('customer_unique_id').agg(
        total_orders=('order_id', 'nunique'),
        total_spent=('total_payments', 'sum'),
        avg_review_score=('avg_reviews','mean')
    ).reset_index()

    return customer_summary

if __name__ == "__main__":
    tables = load_all_tables()

    orders = clean_orders(tables['orders'])
    customers = tables['customers']
    order_items = tables['order_items']
    order_payments = tables['order_payments']
    order_reviews = tables['order_reviews']

    order_master = build_order_master(orders, customers, order_items, order_payments, order_reviews)
    seller_summary = build_seller_summary(order_master, order_items)
    customer_summary = build_customer_summary(order_master)

    print("Order master:", order_master.shape)
    print("Seller summary:", seller_summary.shape)
    print("Customer summary:", customer_summary.shape)
    print(order_master.head(2))