# urbanmart_analysis.py

import csv
import os
from datetime import datetime
import pandas as pd

# ------------------------------
# Part 1 – Basic Python & Data Loading
# ------------------------------

store_name = "UrbanMart"
print(f"Welcome to {store_name} Sales Analysis")

CSV_FILE = "urbanmart_sales.csv"


def load_data_with_csv_module(file_path):
    """Load data using built-in csv module and return a list of dicts."""
    data = []
    try:
        with open(file_path, mode="r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                data.append(row)
    except FileNotFoundError:
        print("Error: File not found while using csv module.")
    return data


def load_data_with_pandas(file_path):
    """Load data using pandas and return a DataFrame."""
    try:
        df = pd.read_csv(file_path)
        return df
    except FileNotFoundError:
        print("Error: CSV file not found. Please check the path.")
        return None


def basic_sanity_checks(df: pd.DataFrame):
    """Print basic sanity checks."""
    print("\n--- Basic Sanity Checks ---")
    # total number of rows
    print(f"Total rows: {len(df)}")

    # unique store IDs
    unique_stores = df["store_id"].unique()
    print(f"Unique store IDs: {list(unique_stores)}")

    # date range
    df["date"] = pd.to_datetime(df["date"])
    min_date = df["date"].min().date()
    max_date = df["date"].max().date()
    print(f"Date range: {min_date} to {max_date}")


def demonstrate_lists_tuples_dicts(data_list_of_dicts):
    """Use basic lists, tuples, dicts, and manual loops."""
    print("\n--- Lists, Tuples, Dictionaries Demo ---")

    # list of all product_categories (may contain duplicates)
    product_categories = [row["product_category"] for row in data_list_of_dicts]
    print(f"Sample product_categories (first 10): {product_categories[:10]}")

    # dictionary mapping store_id → store_location
    store_map = {}
    for row in data_list_of_dicts:
        store_id = row["store_id"]
        store_location = row["store_location"]
        store_map[store_id] = store_location
    print(f"Store map (store_id -> store_location): {store_map}")

    # count Online vs In-store manually (without pandas)
    online_count = 0
    instore_count = 0

    for row in data_list_of_dicts:
        channel = row["channel"]
        if channel == "Online":
            online_count += 1
        elif channel == "In-store":
            instore_count += 1

    print(f"Online transactions: {online_count}")
    print(f"In-store transactions: {instore_count}")

    # small example of a tuple (just for concept)
    example_tuple = ("S1", store_map.get("S1", "Unknown"))
    print(f"Example tuple (store_id, store_location): {example_tuple}")


# ------------------------------
# Part 2 – Functions & Simple KPIs
# ------------------------------

def compute_total_revenue(df: pd.DataFrame) -> float:
    """
    Returns total revenue = sum((quantity * unit_price) - discount_applied).
    Assumes quantity, unit_price, discount_applied exist and are numeric.
    """
    line_revenue = (df["quantity"] * df["unit_price"]) - df["discount_applied"]
    return float(line_revenue.sum())


def compute_revenue_by_store(df: pd.DataFrame) -> dict:
    """
    Returns a dictionary: store_id -> revenue.
    """
    line_revenue = (df["quantity"] * df["unit_price"]) - df["discount_applied"]
    df_temp = df.copy()
    df_temp["line_revenue"] = line_revenue
    grouped = df_temp.groupby("store_id")["line_revenue"].sum()
    return grouped.to_dict()


def compute_top_n_products(df: pd.DataFrame, n: int = 5):
    """
    Returns a DataFrame of top n products by revenue.
    """
    df_temp = df.copy()
    df_temp["line_revenue"] = (df_temp["quantity"] * df_temp["unit_price"]) - df_temp["discount_applied"]
    top_products = (
        df_temp.groupby(["product_id", "product_name"])["line_revenue"]
        .sum()
        .sort_values(ascending=False)
        .head(n)
        .reset_index()
    )
    return top_products


def cli_menu(df: pd.DataFrame):
    """Simple CLI menu using while loop and input()."""
    while True:
        print("\n--- UrbanMart CLI Menu ---")
        print("1. Show total revenue")
        print("2. Show revenue by store")
        print("3. Show top 5 products")
        print("4. Exit")

        try:
            choice = input("Enter your choice (1-4): ").strip()
            if choice == "1":
                total_rev = compute_total_revenue(df)
                print(f"Total Revenue: {total_rev:.2f}")

            elif choice == "2":
                store_rev = compute_revenue_by_store(df)
                print("Revenue by store_id:")
                for store_id, rev in store_rev.items():
                    print(f"  {store_id}: {rev:.2f}")

            elif choice == "3":
                top_products = compute_top_n_products(df, n=5)
                print("Top 5 products by revenue:")
                print(top_products.to_string(index=False))

            elif choice == "4":
                print("Exiting CLI. Goodbye!")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 4.")
        except Exception as e:
            print(f"An error occurred: {e}")


# ------------------------------
# Part 3 – Prepare Data for Dashboard
# ------------------------------

def prepare_dataframe_for_dashboard(df: pd.DataFrame) -> pd.DataFrame:
    """Add line_revenue and day_of_week, return updated DataFrame."""
    df = df.copy()
    df["date"] = pd.to_datetime(df["date"])
    df["line_revenue"] = (df["quantity"] * df["unit_price"]) - df["discount_applied"]
    df["day_of_week"] = df["date"].dt.day_name()
    return df


def revenue_by_category(df: pd.DataFrame) -> pd.DataFrame:
    """Return revenue by product_category."""
    return (
        df.groupby("product_category")["line_revenue"]
        .sum()
        .reset_index()
        .sort_values("line_revenue", ascending=False)
    )


def revenue_by_store_location(df: pd.DataFrame) -> pd.DataFrame:
    """Return revenue by store_location."""
    return (
        df.groupby("store_location")["line_revenue"]
        .sum()
        .reset_index()
        .sort_values("line_revenue", ascending=False)
    )


def revenue_by_channel(df: pd.DataFrame) -> pd.DataFrame:
    """Return revenue by channel."""
    return (
        df.groupby("channel")["line_revenue"]
        .sum()
        .reset_index()
        .sort_values("line_revenue", ascending=False)
    )


def top_customers_by_revenue(df: pd.DataFrame, n: int = 5) -> pd.DataFrame:
    """Return top n customers by total revenue."""
    return (
        df.groupby("customer_id")["line_revenue"]
        .sum()
        .sort_values(ascending=False)
        .head(n)
        .reset_index()
    )


def filter_data(df: pd.DataFrame, start_date=None, end_date=None, store=None, channel=None):
    """
    Filter data for date range, store, and channel.
    - start_date, end_date: datetime.date or string 'YYYY-MM-DD' or None
    - store: list of store_location or None
    - channel: 'Online', 'In-store', or None (for all)
    """
    filtered = df.copy()

    if start_date is not None:
        if isinstance(start_date, str):
            start_date = datetime.strptime(start_date, "%Y-%m-%d").date()
        filtered = filtered[filtered["date"].dt.date >= start_date]

    if end_date is not None:
        if isinstance(end_date, str):
            end_date = datetime.strptime(end_date, "%Y-%m-%d").date()
        filtered = filtered[filtered["date"].dt.date <= end_date]

    if store is not None and len(store) > 0:
        filtered = filtered[filtered["store_location"].isin(store)]

    if channel is not None and channel != "All":
        filtered = filtered[filtered["channel"] == channel]

    return filtered


# ------------------------------
# Main execution (for console)
# ------------------------------

def main():
    # Load with pandas (for analysis & dashboard prep)
    df = load_data_with_pandas(CSV_FILE)
    if df is None:
        return

    # Basic sanity checks
    basic_sanity_checks(df)

    # Also demonstrate list/dict using csv module
    data_list = load_data_with_csv_module(CSV_FILE)
    if data_list:
        demonstrate_lists_tuples_dicts(data_list)

    # Prepare df for KPIs & dashboard
    df_prepared = prepare_dataframe_for_dashboard(df)

    # Run CLI menu
    cli_menu(df_prepared)


if __name__ == "__main__":
    main()