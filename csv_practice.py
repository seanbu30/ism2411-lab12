

import csv
from datetime import datetime

SALES_FILE = "data/sales.csv"
CLEANED_FILE = "data/sales_cleaned.csv"
LOG_FILE = "data/sales_log.txt"

print("--- Exercise 1 ---")
with open(SALES_FILE, "r") as f:
    print(f"Opened (SALES_FILE).")

print("--- Exercise 2 ---")

with open(SALES_FILE, "r") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)

print("--- Exercise 3 ---")
with open(SALES_FILE, "r") as f:
    reader = csv.reader(f)
    header = next(reader)  # Skip the header row
    print(f"Header: {header}")
    for row in reader:
        print(row)

print("--- Exercise 4 ---")
total_revenue = 0
with open(SALES_FILE, "r") as f:
    reader = csv.reader(f)
    next(reader)  # Skip the header row
    for row in reader:
        product, price_str, qty_str = row
        price = float(price_str)
        quantity = int(qty_str)
        total = price * quantity
        total_revenue += total
        print(f"{product}: {quantity} units x ${price:.2f} = ${total:.2f}")

print(f"Total revenue: ${total_revenue:.2f}")

print("--- Exercise 5 ---")
high_value = []
rows_read = 0

with open(SALES_FILE, "r") as f:
    reader = csv.reader(f)
    next(reader)  # Skip the header row
    for row in reader:
        rows_read += 1
        product, price_str, qty_str = row
        price = float(price_str)
        quantity = int(qty_str)
        total = price * quantity
        if total > 100:
            high_value.append([product, f"{price:.2f}", quantity, f"{total:.2f}"])

with open(CLEANED_FILE, "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["product", "price", "quantity", "total"])
    for row in high_value:
        writer.writerow(row)





    print("--- Exercise 6 ---")

    dict_total = 0
    with open(SALES_FILE, "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            price = float(row["price"])
            quantity = int(row["quantity"])
            total = price * quantity
            dict_total += total
            print(f"{row['product']}: {quantity} units x ${price:.2f} = ${total:.2f}")

        print(f"Total revenue: ${dict_total:.2f}")

print("--- Exercise 7 ---")
summary = {}

with open(SALES_FILE, "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        product = row["product"]
        total = float(row["price"]) * int(row["quantity"])
        summary[product] = summary.get(product, 0) + total
for product in sorted(summary):
    print(f"{product}: ${summary[product]:.2f}")

print("--- Exercise 8 ---")
timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
with open(LOG_FILE, "a") as f:
    f.write(f"{timestamp} total revenue: ${total_revenue:.2f}\n")

entries = 0
with open(LOG_FILE, "r") as f:
    for line in f:
        entries += 1
        print(line.strip())

print(f"Log entries so far: {entries}")

# Reflection Questions

# 1. Doing this ETL task in Python compared to Excel:
# In Excel I could filter rows and multiply price by quantity pretty quickly
# by clicking around, but I would have to redo all those steps by hand every
# time the data changed. Python lets me write the steps once and rerun them on
# a new file in seconds, and it handles huge files and automation (like logging
# every run) much better than Excel. Excel is still easier when I just want to
# look at the data, make a quick chart, or do a one-time calculation without
# writing any code.

# 2. A business process that would benefit from an append-mode log:
# A store could run a script at the end of every day that adds a line with the
# date and that day's total sales to a running log file. Append mode is the
# right tool because each run adds a new entry to the bottom instead of
# erasing the old ones, so the file builds a full sales history over time.
# If the script used write mode instead, it would wipe out every previous day
# and leave only the most recent total.