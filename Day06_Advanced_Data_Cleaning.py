# ======================================================
# DAY 6 - ADVANCED DATA CLEANING & FEATURE ENGINEERING
# Topics:
# 1. Date Conversion
# 2. Extract Year, Month, Day
# 3. String Operations
# 4. Regex Cleaning
# 5. Split Columns
# 6. Replace Values
# 7. Remove Special Characters
# 8. Remove Leading & Trailing Spaces
# 9. Handling Invalid Values
# 10. Encoding
# 11. Feature Creation
# 12. Save Clean Dataset
# ======================================================

import pandas as pd
import numpy as np

print("="*60)
print("Question 1 : Create DataFrame")
print("="*60)

data = {
    "Name":[" Amit Kumar ","Priya Sharma","Rahul123","Sneha@Patil","Karan#Joshi"],
    "Gender":["Male","Female","Male","Female","Male"],
    "City":[" Pune ","Mumbai ","Delhi"," Pune","Nagpur"],
    "DOB":["12-05-2004","25-08-2003","10-01-2005","18-11-2002","15-07-2004"],
    "Salary":[25000,35000,-5000,42000,38000]
}

df = pd.DataFrame(data)

print(df)

# ----------------------------------------------------

print("\nQuestion 2 : Remove Leading & Trailing Spaces")

df["Name"] = df["Name"].str.strip()
df["City"] = df["City"].str.strip()

print(df)

# ----------------------------------------------------

print("\nQuestion 3 : Convert to Uppercase")

df["City"] = df["City"].str.upper()

print(df)

# ----------------------------------------------------

print("\nQuestion 4 : Remove Numbers From Name")

df["Name"] = df["Name"].str.replace(r"\d+", "", regex=True)

print(df)

# ----------------------------------------------------

print("\nQuestion 5 : Remove Special Characters")

df["Name"] = df["Name"].str.replace(r"[^a-zA-Z ]", "", regex=True)

print(df)

# ----------------------------------------------------

print("\nQuestion 6 : Split First and Last Name")

df[["First_Name","Last_Name"]] = df["Name"].str.split(" ", n=1, expand=True)

print(df)

# ----------------------------------------------------

print("\nQuestion 7 : Convert DOB to Datetime")

df["DOB"] = pd.to_datetime(df["DOB"], format="%d-%m-%Y")

print(df)

# ----------------------------------------------------

print("\nQuestion 8 : Extract Year, Month and Day")

df["Birth_Year"] = df["DOB"].dt.year
df["Birth_Month"] = df["DOB"].dt.month
df["Birth_Day"] = df["DOB"].dt.day

print(df)

# ----------------------------------------------------

print("\nQuestion 9 : Create Age Feature")

current_year = 2026

df["Age"] = current_year - df["Birth_Year"]

print(df)

# ----------------------------------------------------

print("\nQuestion 10 : Handle Invalid Salary")

df["Salary"] = df["Salary"].apply(lambda x: np.nan if x < 0 else x)

print(df)

# ----------------------------------------------------

print("\nQuestion 11 : Fill Missing Salary")

df["Salary"] = df["Salary"].fillna(df["Salary"].mean())

print(df)

# ----------------------------------------------------

print("\nQuestion 12 : Label Encoding")

gender = {
    "Male":0,
    "Female":1
}

df["Gender"] = df["Gender"].map(gender)

print(df)

# ----------------------------------------------------

print("\nQuestion 13 : One-Hot Encoding")

city_encoded = pd.get_dummies(df["City"], prefix="City")

print(city_encoded)

# ----------------------------------------------------

print("\nQuestion 14 : Combine Encoded Columns")

df = pd.concat([df, city_encoded], axis=1)

print(df)

# ----------------------------------------------------

print("\nQuestion 15 : Drop Unnecessary Columns")

df = df.drop(columns=["DOB"])

print(df)

# ----------------------------------------------------

print("\nQuestion 16 : Check Data Types")

print(df.dtypes)

# ----------------------------------------------------

print("\nQuestion 17 : Statistical Summary")

print(df.describe())

# ----------------------------------------------------

print("\nQuestion 18 : Save Clean Dataset")

df.to_csv("advanced_cleaned_data.csv", index=False)

print("Dataset Saved Successfully!")

# ----------------------------------------------------

print("\nQuestion 19 : Final Dataset")

print(df)

# ----------------------------------------------------

print("\nQuestion 20 : Dataset Info")

print(df.info())

print("\nDay 6 Completed Successfully!")
