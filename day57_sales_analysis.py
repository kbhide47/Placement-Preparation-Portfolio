# ============================================================
# DAY 57 - DATA ANALYST CASE STUDY
# E-COMMERCE SALES ANALYSIS
# ============================================================

import pandas as pd
import matplotlib.pyplot as plt


# ============================================================
# STEP 1: CREATE SAMPLE DATASET
# ============================================================

data = {
    "Order_ID": [
        101, 102, 103, 104, 105,
        106, 107, 108, 109, 110,
        111, 112, 113, 114, 115
    ],

    "Customer": [
        "Amit", "Riya", "Rahul", "Sneha", "Karan",
        "Priya", "Arjun", "Neha", "Vikas", "Ananya",
        "Amit", "Rahul", "Priya", "Neha", "Karan"
    ],

    "City": [
        "Pune", "Mumbai", "Pune", "Delhi", "Mumbai",
        "Pune", "Delhi", "Mumbai", "Pune", "Mumbai",
        "Pune", "Pune", "Pune", "Mumbai", "Delhi"
    ],

    "Category": [
        "Electronics", "Clothing", "Electronics",
        "Home", "Clothing",
        "Electronics", "Home", "Electronics",
        "Clothing", "Home",
        "Electronics", "Clothing", "Home",
        "Electronics", "Clothing"
    ],

    "Product": [
        "Laptop", "T-Shirt", "Headphones",
        "Chair", "Jeans",
        "Smartphone", "Table", "Laptop",
        "Shoes", "Lamp",
        "Laptop", "Shoes", "Chair",
        "Headphones", "T-Shirt"
    ],

    "Quantity": [
        1, 3, 2, 1, 2,
        1, 1, 1, 2, 3,
        1, 1, 2, 2, 4
    ],

    "Price": [
        50000, 1000, 3000, 8000, 2000,
        40000, 12000, 50000, 2500, 1500,
        50000, 2500, 8000, 3000, 1000
    ]
}


df = pd.DataFrame(data)


# ============================================================
# STEP 2: UNDERSTAND THE DATA
# ============================================================

print("\nFIRST 5 ROWS:")
print(df.head())

print("\nDATA INFORMATION:")
print(df.info())

print("\nDATA DESCRIPTION:")
print(df.describe())


# ============================================================
# STEP 3: DATA CLEANING
# ============================================================

print("\nMISSING VALUES:")
print(df.isnull().sum())

print("\nDUPLICATE ROWS:")
print(df.duplicated().sum())

# Remove duplicate rows if any
df = df.drop_duplicates()


# ============================================================
# STEP 4: CREATE REVENUE COLUMN
# ============================================================

df["Revenue"] = df["Quantity"] * df["Price"]

print("\nDATA WITH REVENUE:")
print(df.head())


# ============================================================
# STEP 5: KEY PERFORMANCE INDICATORS
# ============================================================

total_revenue = df["Revenue"].sum()

total_orders = df["Order_ID"].nunique()

total_quantity = df["Quantity"].sum()

average_order_value = total_revenue / total_orders


print("\n========== KPIs ==========")

print("Total Revenue:", total_revenue)

print("Total Orders:", total_orders)

print("Total Quantity Sold:", total_quantity)

print("Average Order Value:", average_order_value)


# ============================================================
# STEP 6: REVENUE BY CATEGORY
# ============================================================

category_revenue = (

    df.groupby("Category")["Revenue"]
    .sum()
    .sort_values(ascending=False)

)

print("\nREVENUE BY CATEGORY:")
print(category_revenue)


# ============================================================
# STEP 7: TOP PRODUCTS
# ============================================================

product_revenue = (

    df.groupby("Product")["Revenue"]
    .sum()
    .sort_values(ascending=False)

)

print("\nTOP PRODUCTS:")
print(product_revenue)


# ============================================================
# STEP 8: SALES BY CITY
# ============================================================

city_revenue = (

    df.groupby("City")["Revenue"]
    .sum()
    .sort_values(ascending=False)

)

print("\nSALES BY CITY:")
print(city_revenue)


# ============================================================
# STEP 9: TOP CUSTOMERS
# ============================================================

customer_revenue = (

    df.groupby("Customer")["Revenue"]
    .sum()
    .sort_values(ascending=False)

)

print("\nTOP CUSTOMERS:")
print(customer_revenue)


# ============================================================
# STEP 10: CATEGORY-WISE QUANTITY SOLD
# ============================================================

category_quantity = (

    df.groupby("Category")["Quantity"]
    .sum()
    .sort_values(ascending=False)

)

print("\nCATEGORY-WISE QUANTITY:")
print(category_quantity)


# ============================================================
# STEP 11: VISUALIZATION - CATEGORY REVENUE
# ============================================================

category_revenue.plot(
    kind="bar",
    title="Revenue by Category"
)

plt.xlabel("Category")

plt.ylabel("Revenue")

plt.show()


# ============================================================
# STEP 12: VISUALIZATION - TOP PRODUCTS
# ============================================================

product_revenue.plot(
    kind="bar",
    title="Revenue by Product"
)

plt.xlabel("Product")

plt.ylabel("Revenue")

plt.xticks(rotation=45)

plt.show()


# ============================================================
# STEP 13: VISUALIZATION - CITY-WISE REVENUE
# ============================================================

city_revenue.plot(
    kind="bar",
    title="Revenue by City"
)

plt.xlabel("City")

plt.ylabel("Revenue")

plt.show()


# ============================================================
# STEP 14: BUSINESS INSIGHTS
# ============================================================

print("\n========== BUSINESS INSIGHTS ==========")

print(
    "Highest Revenue Category:",
    category_revenue.idxmax()
)

print(
    "Top Product:",
    product_revenue.idxmax()
)

print(
    "Top Revenue City:",
    city_revenue.idxmax()
)

print(
    "Top Customer:",
    customer_revenue.idxmax()
)


# ============================================================
# STEP 15: RECOMMENDATIONS
# ============================================================

print("\n========== RECOMMENDATIONS ==========")

print(
    "1. Focus marketing efforts on the highest-performing category."
)

print(
    "2. Ensure sufficient stock for the highest-revenue products."
)

print(
    "3. Target high-performing cities with promotional campaigns."
)

print(
    "4. Introduce loyalty programs for top customers."
)


# ============================================================
# END OF DAY 57
# ============================================================
