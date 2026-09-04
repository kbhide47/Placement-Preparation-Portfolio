# ============================================================
# DAY 59 - DATA CLEANING PROJECT
# ============================================================

import pandas as pd
import numpy as np


# ============================================================
# STEP 1: CREATE A MESSY DATASET
# ============================================================

data = {
    "Order_ID": [
        101, 102, 103, 104, 105,
        106, 107, 108, 108, 110
    ],

    "Customer_Name": [
        "Amit", " riya", "RAHUL ", "Sneha", None,
        "Priya", "Arjun", "neha", "neha", "Karan"
    ],

    "City": [
        "Pune", "mumbai", "PUNE ", "Delhi", "Mumbai",
        "pune", "DELHI", "Mumbai", "Mumbai", None
    ],

    "Category": [
        "Electronics", "Clothing", "electronics",
        "Home", "Clothing", "ELECTRONICS",
        "Home", "Electronics", "Electronics", "Clothing"
    ],

    "Quantity": [
        1, 3, 2, None, 2,
        1, -1, 1, 1, 4
    ],

    "Price": [
        "50000", "1000", "3000", "8000", None,
        "40000", "12000", "50000", "50000", "1000"
    ],

    "Order_Date": [
        "2026-01-10",
        "2026/01/15",
        "15-01-2026",
        "2026-01-20",
        "2026-02-01",
        "2026/02/05",
        "05-02-2026",
        "2026-02-10",
        "2026-02-10",
        "invalid_date"
    ]
}


df = pd.DataFrame(data)


# ============================================================
# STEP 2: VIEW ORIGINAL DATA
# ============================================================

print("\n========== ORIGINAL DATA ==========")
print(df)


# ============================================================
# STEP 3: CHECK DATA INFORMATION
# ============================================================

print("\n========== DATA INFORMATION ==========")
df.info()


# ============================================================
# STEP 4: CHECK MISSING VALUES
# ============================================================

print("\n========== MISSING VALUES ==========")
print(df.isnull().sum())


# ============================================================
# STEP 5: CHECK DUPLICATES
# ============================================================

print("\n========== DUPLICATE ROWS ==========")
print(df.duplicated().sum())


# ============================================================
# STEP 6: REMOVE DUPLICATE ROWS
# ============================================================

df = df.drop_duplicates()


# ============================================================
# STEP 7: CLEAN CUSTOMER NAMES
# ============================================================

# Convert names to string format
df["Customer_Name"] = df["Customer_Name"].astype("string")

# Remove extra spaces
df["Customer_Name"] = df["Customer_Name"].str.strip()

# Convert names to title case
df["Customer_Name"] = df["Customer_Name"].str.title()


# ============================================================
# STEP 8: CLEAN CITY NAMES
# ============================================================

df["City"] = df["City"].astype("string")

df["City"] = df["City"].str.strip()

df["City"] = df["City"].str.title()


# ============================================================
# STEP 9: CLEAN CATEGORY NAMES
# ============================================================

df["Category"] = df["Category"].astype("string")

df["Category"] = df["Category"].str.strip()

df["Category"] = df["Category"].str.title()


# ============================================================
# STEP 10: HANDLE MISSING CUSTOMER NAMES
# ============================================================

df["Customer_Name"] = df["Customer_Name"].fillna(
    "Unknown"
)


# ============================================================
# STEP 11: HANDLE MISSING CITY VALUES
# ============================================================

df["City"] = df["City"].fillna(
    "Unknown"
)


# ============================================================
# STEP 12: FIX PRICE DATA TYPE
# ============================================================

df["Price"] = pd.to_numeric(
    df["Price"],
    errors="coerce"
)


# ============================================================
# STEP 13: HANDLE MISSING PRICE VALUES
# ============================================================

df["Price"] = df["Price"].fillna(
    df["Price"].median()
)


# ============================================================
# STEP 14: HANDLE MISSING QUANTITY
# ============================================================

df["Quantity"] = df["Quantity"].fillna(
    df["Quantity"].median()
)


# ============================================================
# STEP 15: REMOVE INVALID QUANTITY VALUES
# ============================================================

# Quantity cannot be zero or negative

df = df[
    df["Quantity"] > 0
]


# ============================================================
# STEP 16: FIX DATE FORMAT
# ============================================================

df["Order_Date"] = pd.to_datetime(
    df["Order_Date"],
    format="mixed",
    errors="coerce"
)


# ============================================================
# STEP 17: CHECK INVALID DATES
# ============================================================

print("\n========== INVALID DATES ==========")

print(
    df[df["Order_Date"].isnull()]
)


# Remove rows with invalid dates

df = df.dropna(
    subset=["Order_Date"]
)


# ============================================================
# STEP 18: CHECK DATA TYPES AGAIN
# ============================================================

print("\n========== CLEANED DATA TYPES ==========")

print(df.dtypes)


# ============================================================
# STEP 19: CHECK MISSING VALUES AGAIN
# ============================================================

print("\n========== MISSING VALUES AFTER CLEANING ==========")

print(df.isnull().sum())


# ============================================================
# STEP 20: CREATE REVENUE COLUMN
# ============================================================

df["Revenue"] = (
    df["Quantity"] * df["Price"]
)


# ============================================================
# STEP 21: RESET INDEX
# ============================================================

df = df.reset_index(
    drop=True
)


# ============================================================
# STEP 22: FINAL CLEAN DATA
# ============================================================

print("\n========== FINAL CLEAN DATA ==========")

print(df)


# ============================================================
# STEP 23: SAVE CLEANED DATASET
# ============================================================

df.to_csv(
    "cleaned_sales_data.csv",
    index=False
)


print(
    "\nCleaned dataset saved successfully!"
)


# ============================================================
# END OF DAY 59
# ============================================================
