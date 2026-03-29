import pandas as pd
from pathlib import Path

# Define path to raw data
RAW_DATA_PATH = Path(__file__).resolve().parents[1] / "data" / "raw"

def load_all_tables():
    """Load all Olist CSV files into a dictionary of dataframes."""
    files = {
        "customers": "olist_customers_dataset.csv",
        "geolocation": "olist_geolocation_dataset.csv",
        "order_items": "olist_order_items_dataset.csv",
        "order_payments": "olist_order_payments_dataset.csv",
        "order_reviews": "olist_order_reviews_dataset.csv",
        "orders": "olist_orders_dataset.csv",
        "products": "olist_products_dataset.csv",
        "sellers": "olist_sellers_dataset.csv",
        "category_translation": "product_category_name_translation.csv",
    }

    tables = {}
    for name, filename in files.items():
        path = RAW_DATA_PATH / filename
        df = pd.read_csv(path)
        tables[name] = df
        print(f"\n--- {name} ---")
        print(f"Shape: {df.shape}")
        print(f"Columns: {list(df.columns)}")

    return tables


def audit_tables(tables):
    """Run basic null and duplicate counts on each table."""
    print("\n" + "="*50)
    print("DATA AUDIT SUMMARY")
    print("="*50)

    for name, df in tables.items():
        print(f"\n--- {name} ---")
        print(f"Rows: {df.shape[0]:,} | Columns: {df.shape[1]}")

        null_counts = df.isnull().sum()
        nulls = null_counts[null_counts > 0]
        if not nulls.empty:
            print("Nulls:")
            for col, count in nulls.items():
                pct = count / len(df) * 100
                print(f"  {col}: {count:,} ({pct:.1f}%)")
        else:
            print("Nulls: None")

        # Duplicate check on first column (usually an ID)
        id_col = df.columns[0]
        dupes = df[id_col].duplicated().sum()
        print(f"Duplicates on '{id_col}': {dupes:,}")


def print_join_map():
    """Print the join key relationships between all Olist tables."""
    print("\n" + "="*50)
    print("JOIN KEY MAP")
    print("="*50)

    join_map = [
        ("orders", "customers", "customer_id"),
        ("orders", "order_items", "order_id"),
        ("orders", "order_payments", "order_id"),
        ("orders", "order_reviews", "order_id"),
        ("order_items", "products", "product_id"),
        ("order_items", "sellers", "seller_id"),
        ("order_items", "order_payments", "order_id"),
        ("order_items", "order_reviews", "order_id"),
        ("order_payments", "order_reviews", "order_id"),
        ("products", "category_translation", "product_category_name"),
        ("customers", "geolocation", "customer_zip_code_prefix → geolocation_zip_code_prefix"),
        ("sellers", "geolocation", "seller_zip_code_prefix → geolocation_zip_code_prefix"),
    ]

    for left, right, key in join_map:
        print(f"  {left} ↔ {right} on [{key}]")

if __name__ == "__main__":
    tables = load_all_tables()
    audit_tables(tables)
    print_join_map()