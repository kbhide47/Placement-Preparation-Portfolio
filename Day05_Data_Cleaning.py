# ==========================================
# DAY 5 - DATA CLEANING
# Topics:
# 1. Create DataFrame
# 2. Check Missing Values
# 3. Fill Missing Values
# 4. Drop Missing Values
# 5. Find Duplicates
# 6. Remove Duplicates
# 7. Check Data Types
# 8. Convert Data Types
# 9. Rename Columns
# 10. Replace Values
# 11. String Cleaning
# 12. Outlier Detection
# ==========================================

import pandas as pd
import numpy as np

print("="*60)
print("Question 1 : Create DataFrame")
print("="*60)

data = {
    "Name":[" Amit ","Priya","Rahul",None,"Sneha","Rahul"],
    "Age":[20,21,np.nan,22,20,21],
    "Marks":[85,np.nan,78,92,88,78],
    "City":["Pune","Mumbai","Pune","Delhi",None,"Pune"]
}

df = pd.DataFrame(data)

print(df)

# --------------------------------------------------

print("\nQuestion 2 : Check Missing Values")

print(df.isnull())

# --------------------------------------------------

print("\nQuestion 3 : Count Missing Values")

print(df.isnull().sum())

# --------------------------------------------------

print("\nQuestion 4 : Fill Missing Values")

df["Age"] = df["Age"].fillna(df["Age"].mean())
df["Marks"] = df["Marks"].fillna(df["Marks"].mean())
df["City"] = df["City"].fillna("Unknown")

print(df)

# --------------------------------------------------

print("\nQuestion 5 : Drop Missing Name")

df = df.dropna(subset=["Name"])

print(df)

# --------------------------------------------------

print("\nQuestion 6 : Check Duplicate Rows")

print(df.duplicated())

# --------------------------------------------------

print("\nQuestion 7 : Remove Duplicates")

df = df.drop_duplicates()

print(df)

# --------------------------------------------------

print("\nQuestion 8 : Check Data Types")

print(df.dtypes)

# --------------------------------------------------

print("\nQuestion 9 : Convert Data Type")

df["Age"] = df["Age"].astype(int)

print(df.dtypes)

# --------------------------------------------------

print("\nQuestion 10 : Rename Columns")

df.rename(columns={"Marks":"Score"}, inplace=True)

print(df.columns)

# --------------------------------------------------

print("\nQuestion 11 : Replace Values")

df["City"] = df["City"].replace({
    "Pune":"PUNE",
    "Mumbai":"MUMBAI"
})

print(df)

# --------------------------------------------------

print("\nQuestion 12 : Remove Extra Spaces")

df["Name"] = df["Name"].str.strip()

print(df)

# --------------------------------------------------

print("\nQuestion 13 : Convert to Uppercase")

df["Name"] = df["Name"].str.upper()

print(df)

# --------------------------------------------------

print("\nQuestion 14 : Convert to Lowercase")

df["City"] = df["City"].str.lower()

print(df)

# --------------------------------------------------

print("\nQuestion 15 : Detect Outliers")

Q1 = df["Score"].quantile(0.25)
Q3 = df["Score"].quantile(0.75)

IQR = Q3 - Q1

lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR

outliers = df[(df["Score"] < lower) | (df["Score"] > upper)]

print(outliers)

# --------------------------------------------------

print("\nQuestion 16 : Final Clean Dataset")

print(df)

# --------------------------------------------------

print("\nQuestion 17 : Dataset Information")

print(df.info())

# --------------------------------------------------

print("\nQuestion 18 : Statistical Summary")

print(df.describe())

# --------------------------------------------------

print("\nQuestion 19 : Save Clean Dataset")

df.to_csv("cleaned_students.csv", index=False)

print("Dataset Saved Successfully!")

# --------------------------------------------------

print("\nQuestion 20 : Final Analysis")

print("Average Score :", df["Score"].mean())
print("Highest Score :", df["Score"].max())
print("Lowest Score :", df["Score"].min())

print("\nDay 5 Completed Successfully!")
