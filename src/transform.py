import pandas as pd

def transform(data):
    print("Starting transformations...")

    # --- Orders ---
    orders = data["olist_orders_dataset"].copy()
    date_cols = [
        "order_purchase_timestamp",
        "order_approved_at",
        "order_delivered_carrier_date",
        "order_delivered_customer_date",
        "order_estimated_delivery_date"
    ]
    for col in date_cols:
        orders[col] = pd.to_datetime(orders[col], errors="coerce")
    print("Orders transformed.")

    # --- Customers ---
    customers = data["olist_customers_dataset"].copy()
    customers.drop_duplicates(subset="customer_id", inplace=True)
    print("Customers transformed.")

    # --- Products ---
    products = data["olist_products_dataset"].copy()
    translations = data["product_category_name_translation"].copy()
    products = products.merge(translations, on="product_category_name", how="left")
    products["product_category_name"] = products["product_category_name_english"].fillna(products["product_category_name"])
    products.drop(columns=["product_category_name_english"], inplace=True)
    print("Products transformed.")

    # --- Sellers ---
    sellers = data["olist_sellers_dataset"].copy()
    sellers.drop_duplicates(subset="seller_id", inplace=True)
    print("Sellers transformed.")

    # --- Order Items ---
    order_items = data["olist_order_items_dataset"].copy()
    order_items["shipping_limit_date"] = pd.to_datetime(order_items["shipping_limit_date"], errors="coerce")
    print("Order items transformed.")

    # --- Payments ---
    payments = data["olist_order_payments_dataset"].copy()
    print("Payments transformed.")

    # --- Reviews ---
    reviews = data["olist_order_reviews_dataset"].copy()
    reviews["review_creation_date"] = pd.to_datetime(reviews["review_creation_date"], errors="coerce")
    reviews["review_answer_timestamp"] = pd.to_datetime(reviews["review_answer_timestamp"], errors="coerce")
    print("Reviews transformed.")

    print("\nTransform complete.")

    return {
        "fact_orders": orders,
        "dim_customers": customers,
        "dim_products": products,
        "dim_sellers": sellers,
        "fact_order_items": order_items,
        "fact_payments": payments,
        "fact_reviews": reviews
    }

if __name__ == "__main__":
    from extract import extract
    data = extract()
    transformed = transform(data)
    for name, df in transformed.items():
        print(f"{name}: {df.shape[0]} rows, {df.shape[1]} columns")