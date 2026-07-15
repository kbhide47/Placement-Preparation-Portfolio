# ==========================================================
# DAY 10 - DATA PREPROCESSING
# Topics:
# 1. Load Dataset
# 2. Missing Values
# 3. Label Encoding
# 4. One-Hot Encoding
# 5. Feature Scaling (StandardScaler)
# 6. Feature Scaling (MinMaxScaler)
# 7. Train-Test Split
# ==========================================================

import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import MinMaxScaler

# -------------------------------------------------------

print("="*60)
print("Question 1 : Create Dataset")
print("="*60)

data = {
    "Age":[25,30,35,np.nan,28],
    "Gender":["Male","Female","Female","Male","Female"],
    "City":["Pune","Mumbai","Delhi","Pune","Mumbai"],
    "Salary":[30000,50000,45000,40000,np.nan],
    "Purchased":[0,1,1,0,1]
}

df = pd.DataFrame(data)

print(df)

# -------------------------------------------------------

print("\nQuestion 2 : Missing Values")

print(df.isnull().sum())

# -------------------------------------------------------

print("\nQuestion 3 : Fill Missing Values")

df["Age"] = df["Age"].fillna(df["Age"].mean())
df["Salary"] = df["Salary"].fillna(df["Salary"].mean())

print(df)

# -------------------------------------------------------

print("\nQuestion 4 : Label Encoding")

label = LabelEncoder()

df["Gender"] = label.fit_transform(df["Gender"])

print(df)

# -------------------------------------------------------

print("\nQuestion 5 : One-Hot Encoding")

encoded = pd.get_dummies(df["City"], prefix="City")

print(encoded)

# -------------------------------------------------------

print("\nQuestion 6 : Concatenate Encoded Columns")

df = pd.concat([df, encoded], axis=1)

df = df.drop("City", axis=1)

print(df)

# -------------------------------------------------------

print("\nQuestion 7 : Features and Target")

X = df.drop("Purchased", axis=1)

y = df["Purchased"]

print("Features")
print(X)

print("\nTarget")
print(y)

# -------------------------------------------------------

print("\nQuestion 8 : Train-Test Split")

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

print("X_train Shape :", X_train.shape)
print("X_test Shape :", X_test.shape)

# -------------------------------------------------------

print("\nQuestion 9 : Standard Scaling")

scaler = StandardScaler()

X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

print(X_train_scaled)

# -------------------------------------------------------

print("\nQuestion 10 : Min-Max Scaling")

minmax = MinMaxScaler()

X_train_min = minmax.fit_transform(X_train)
X_test_min = minmax.transform(X_test)

print(X_train_min)

# -------------------------------------------------------

print("\nQuestion 11 : Dataset Information")

print(df.info())

# -------------------------------------------------------

print("\nQuestion 12 : Statistical Summary")

print(df.describe())

# -------------------------------------------------------

print("\nQuestion 13 : Column Names")

print(df.columns)

# -------------------------------------------------------

print("\nQuestion 14 : Data Types")

print(df.dtypes)

# -------------------------------------------------------

print("\nQuestion 15 : Shape")

print(df.shape)

# -------------------------------------------------------

print("\nQuestion 16 : Features Used")

print(X.columns)

# -------------------------------------------------------

print("\nQuestion 17 : Target Values")

print(y.unique())

# -------------------------------------------------------

print("\nQuestion 18 : Check Null Values")

print(df.isnull().sum())

# -------------------------------------------------------

print("\nQuestion 19 : Save Processed Dataset")

df.to_csv("processed_dataset.csv", index=False)

print("Dataset Saved Successfully")

# -------------------------------------------------------

print("\nQuestion 20 : Completed")

print("Day 10 Completed Successfully!")
