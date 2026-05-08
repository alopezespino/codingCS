"""
Generate a large synthetic sales dataset for big data exercises.

Run this script to create data/sales_large.csv (100,000 rows).
This file is NOT committed to git — each person generates it locally.

Usage:
    python scripts/generate_large_data.py
"""

import csv
import random
import os
from datetime import date, timedelta

PRODUCTS = {
    "Electronics": ["Laptop", "Phone", "Tablet", "Headphones", "Monitor", "Keyboard", "Mouse", "Webcam"],
    "Clothing": ["T-Shirt", "Jeans", "Jacket", "Sneakers", "Hat", "Scarf", "Socks", "Dress"],
    "Groceries": ["Rice", "Pasta", "Bread", "Milk", "Eggs", "Chicken", "Apples", "Cheese"],
    "Books": ["Novel", "Textbook", "Cookbook", "Biography", "Comic", "Magazine", "Journal", "Guide"],
    "Home": ["Lamp", "Pillow", "Blanket", "Mug", "Plate", "Towel", "Candle", "Vase"],
}

REGIONS = ["Northeast", "Southeast", "Midwest", "Southwest", "West"]

PRICE_RANGES = {
    "Electronics": (29.99, 999.99),
    "Clothing": (9.99, 149.99),
    "Groceries": (0.99, 24.99),
    "Books": (4.99, 79.99),
    "Home": (5.99, 89.99),
}

NUM_ROWS = 100_000
START_DATE = date(2022, 1, 1)
END_DATE = date(2024, 12, 31)
DATE_RANGE = (END_DATE - START_DATE).days

random.seed(42)

output_path = os.path.join(os.path.dirname(__file__), "..", "data", "sales_large.csv")
output_path = os.path.abspath(output_path)

os.makedirs(os.path.dirname(output_path), exist_ok=True)

with open(output_path, "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["transaction_id", "date", "product", "category", "quantity", "unit_price", "region", "customer_id"])

    for i in range(1, NUM_ROWS + 1):
        category = random.choice(list(PRODUCTS.keys()))
        product = random.choice(PRODUCTS[category])
        low, high = PRICE_RANGES[category]
        price = round(random.uniform(low, high), 2)
        quantity = random.randint(1, 10)
        region = random.choice(REGIONS)
        tx_date = START_DATE + timedelta(days=random.randint(0, DATE_RANGE))
        customer_id = random.randint(1000, 9999)

        writer.writerow([i, tx_date.isoformat(), product, category, quantity, price, region, customer_id])

print(f"Generated {NUM_ROWS:,} rows -> {output_path}")
