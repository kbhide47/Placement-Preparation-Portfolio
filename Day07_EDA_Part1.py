# =====================================================
# DAY 7 - EDA PART 1
# Topics:
# 1. Load Dataset
# 2. Shape
# 3. Columns
# 4. Data Types
# 5. Missing Values
# 6. Duplicate Rows
# 7. Descriptive Statistics
# 8. Unique Values
# 9. Correlation
# 10. Value Counts
# 11. Basic Insights
# =====================================================

import pandas as pd

# --------------------------------------------------

print("="*60)
print("Question 1 : Load Dataset")
print("="*60)

df = pd.read_csv("titanic.csv")

print(df.head())

# --------------------------------------------------

print("\nQuestion 2 : Shape")

print(df.shape)

# --------------------------------------------------

print("\nQuestion 3 : Columns")

print(df.columns)

# --------------------------------------------------

print("\nQuestion 4 : Data Types")

print(df.dtypes)

# --------------------------------------------------

print("\nQuestion 5 : Dataset Information")

print(df.info())

# --------------------------------------------------

print("\nQuestion 6 : Missing Values")

print(df.isnull().sum())

# --------------------------------------------------

print("\nQuestion 7 : Duplicate Rows")

print(df.duplicated().sum())

# --------------------------------------------------

print("\nQuestion 8 : Descriptive Statistics")

print(df.describe())

# --------------------------------------------------

print("\nQuestion 9 : Unique Values")

print(df.nunique())

# --------------------------------------------------

print("\nQuestion 10 : Value Counts")

print(df["Sex"].value_counts())

print(df["Pclass"].value_counts())

# --------------------------------------------------

print("\nQuestion 11 : Average Age")

print(df["Age"].mean())

# --------------------------------------------------

print("\nQuestion 12 : Median Fare")

print(df["Fare"].median())

# --------------------------------------------------

print("\nQuestion 13 : Highest Fare")

print(df["Fare"].max())

# --------------------------------------------------

print("\nQuestion 14 : Lowest Fare")

print(df["Fare"].min())

# --------------------------------------------------

print("\nQuestion 15 : Correlation")

print(df.corr(numeric_only=True))

# --------------------------------------------------

print("\nQuestion 16 : Survived Count")

print(df["Survived"].value_counts())

# --------------------------------------------------

print("\nQuestion 17 : Male vs Female")

print(df["Sex"].value_counts())

# --------------------------------------------------

print("\nQuestion 18 : Passenger Class Distribution")

print(df.groupby("Pclass")["PassengerId"].count())

# --------------------------------------------------

print("\nQuestion 19 : Survival Rate")

survival_rate = df["Survived"].mean() * 100

print(f"Survival Rate : {survival_rate:.2f}%")

# --------------------------------------------------

print("\nQuestion 20 : Basic Insights")

print("Total Passengers :", len(df))
print("Average Age :", df["Age"].mean())
print("Average Fare :", df["Fare"].mean())
print("Highest Fare :", df["Fare"].max())
print("Missing Values :")
print(df.isnull().sum())

print("\nDay 7 Completed Successfully!")
