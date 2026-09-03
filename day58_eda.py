# ============================================================
# DAY 58 - EXPLORATORY DATA ANALYSIS (EDA)
# ============================================================

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# ============================================================
# STEP 1: CREATE SAMPLE SALES DATASET
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

    "Age": [
        24, 28, 31, 26, 35,
        29, 40, 23, 32, 27,
        24, 31, 29, 23, 35
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
# STEP 2: CREATE REVENUE COLUMN
# ============================================================

df["Revenue"] = df["Quantity"] * df["Price"]


# ============================================================
# STEP 3: FIRST LOOK AT DATA
# ============================================================

print("\n========== FIRST 5 ROWS ==========")
print(df.head())

print("\n========== LAST 5 ROWS ==========")
print(df.tail())

print("\n========== DATA SHAPE ==========")
print(df.shape)

print("\n========== COLUMN NAMES ==========")
print(df.columns)


# ============================================================
# STEP 4: DATA INFORMATION
# ============================================================

print("\n========== DATA INFO ==========")
df.info()

print("\n========== DATA TYPES ==========")
print(df.dtypes)


# ============================================================
# STEP 5: STATISTICAL SUMMARY
# ============================================================

print("\n========== STATISTICAL SUMMARY ==========")
print(df.describe())


# ============================================================
# STEP 6: CHECK MISSING VALUES
# ============================================================

print("\n========== MISSING VALUES ==========")
print(df.isnull().sum())


# ============================================================
# STEP 7: CHECK DUPLICATES
# ============================================================

print("\n========== DUPLICATE ROWS ==========")
print(df.duplicated().sum())


# ============================================================
# STEP 8: UNIQUE VALUES
# ============================================================

print("\n========== UNIQUE VALUES ==========")

for column in df.columns:

    print(
        column,
        ":",
        df[column].nunique()
    )


# ============================================================
# STEP 9: NUMERICAL DISTRIBUTION
# ============================================================

print("\n========== NUMERICAL COLUMNS ==========")

print(
    df.select_dtypes(
        include=np.number
    ).columns
)


# ============================================================
# STEP 10: AGE DISTRIBUTION
# ============================================================

plt.figure(figsize=(8, 5))

plt.hist(
    df["Age"],
    bins=5
)

plt.title("Age Distribution")

plt.xlabel("Age")

plt.ylabel("Frequency")

plt.show()


# ============================================================
# STEP 11: REVENUE DISTRIBUTION
# ============================================================

plt.figure(figsize=(8, 5))

plt.hist(
    df["Revenue"],
    bins=5
)

plt.title("Revenue Distribution")

plt.xlabel("Revenue")

plt.ylabel("Frequency")

plt.show()


# ============================================================
# STEP 12: CATEGORY DISTRIBUTION
# ============================================================

category_count = df["Category"].value_counts()

print("\n========== CATEGORY COUNT ==========")
print(category_count)


plt.figure(figsize=(8, 5))

category_count.plot(
    kind="bar"
)

plt.title("Number of Orders by Category")

plt.xlabel("Category")

plt.ylabel("Number of Orders")

plt.show()


# ============================================================
# STEP 13: CITY DISTRIBUTION
# ============================================================

city_count = df["City"].value_counts()

print("\n========== CITY COUNT ==========")
print(city_count)


plt.figure(figsize=(8, 5))

city_count.plot(
    kind="bar"
)

plt.title("Orders by City")

plt.xlabel("City")

plt.ylabel("Number of Orders")

plt.show()


# ============================================================
# STEP 14: REVENUE BY CATEGORY
# ============================================================

category_revenue = (
    df.groupby("Category")["Revenue"]
    .sum()
    .sort_values(ascending=False)
)

print("\n========== REVENUE BY CATEGORY ==========")
print(category_revenue)


plt.figure(figsize=(8, 5))

category_revenue.plot(
    kind="bar"
)

plt.title("Revenue by Category")

plt.xlabel("Category")

plt.ylabel("Revenue")

plt.show()


# ============================================================
# STEP 15: REVENUE BY CITY
# ============================================================

city_revenue = (
    df.groupby("City")["Revenue"]
    .sum()
    .sort_values(ascending=False)
)

print("\n========== REVENUE BY CITY ==========")
print(city_revenue)


plt.figure(figsize=(8, 5))

city_revenue.plot(
    kind="bar"
)

plt.title("Revenue by City")

plt.xlabel("City")

plt.ylabel("Revenue")

plt.show()


# ============================================================
# STEP 16: OUTLIER DETECTION USING IQR
# ============================================================

Q1 = df["Revenue"].quantile(0.25)

Q3 = df["Revenue"].quantile(0.75)

IQR = Q3 - Q1


lower_limit = Q1 - 1.5 * IQR

upper_limit = Q3 + 1.5 * IQR


print("\n========== OUTLIER LIMITS ==========")

print("Lower Limit:", lower_limit)

print("Upper Limit:", upper_limit)


outliers = df[
    (df["Revenue"] < lower_limit) |
    (df["Revenue"] > upper_limit)
]


print("\n========== OUTLIERS ==========")

print(outliers)


# ============================================================
# STEP 17: BOX PLOT FOR OUTLIERS
# ============================================================

plt.figure(figsize=(8, 5))

plt.boxplot(
    df["Revenue"]
)

plt.title("Revenue Outlier Detection")

plt.ylabel("Revenue")

plt.show()


# ============================================================
# STEP 18: CORRELATION ANALYSIS
# ============================================================

numerical_data = df.select_dtypes(
    include=np.number
)

correlation = numerical_data.corr()


print("\n========== CORRELATION MATRIX ==========")

print(correlation)


# ============================================================
# STEP 19: CORRELATION VISUALIZATION
# ============================================================

plt.figure(figsize=(8, 6))

plt.imshow(
    correlation,
    aspect="auto"
)

plt.colorbar()

plt.xticks(
    range(len(correlation.columns)),
    correlation.columns,
    rotation=45
)

plt.yticks(
    range(len(correlation.columns)),
    correlation.columns
)

plt.title("Correlation Matrix")

plt.show()


# ============================================================
# STEP 20: TOP CUSTOMERS
# ============================================================

customer_revenue = (
    df.groupby("Customer")["Revenue"]
    .sum()
    .sort_values(ascending=False)
)


print("\n========== TOP CUSTOMERS ==========")

print(customer_revenue)


# ============================================================
# STEP 21: BUSINESS INSIGHTS
# ============================================================

print("\n========== BUSINESS INSIGHTS ==========")

print(
    "Highest Revenue Category:",
    category_revenue.idxmax()
)

print(
    "Highest Revenue City:",
    city_revenue.idxmax()
)

print(
    "Top Customer:",
    customer_revenue.idxmax()
)

print(
    "Average Customer Age:",
    df["Age"].mean()
)

print(
    "Average Order Revenue:",
    df["Revenue"].mean()
)


# ============================================================
# END OF DAY 58
# ============================================================
