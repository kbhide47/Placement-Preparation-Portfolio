# ======================================================
# DAY 15 - END TO END MACHINE LEARNING PROJECT
#
# Project:
# House Price Prediction
#
# Steps:
# 1. Data Loading
# 2. Data Cleaning
# 3. EDA
# 4. Feature Engineering
# 5. Preprocessing
# 6. Model Training
# 7. Evaluation
# 8. Save Model
# ======================================================


# Import Libraries

import pandas as pd
import numpy as np


import matplotlib.pyplot as plt


from sklearn.model_selection import train_test_split


from sklearn.preprocessing import (
    LabelEncoder,
    StandardScaler
)


from sklearn.linear_model import LinearRegression


from sklearn.ensemble import RandomForestRegressor


from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score
)


import joblib



# ---------------------------------------------------

print("="*60)
print("STEP 1 : LOAD DATA")
print("="*60)


df = pd.read_csv(
    "house_prices.csv"
)


print(df.head())


# ---------------------------------------------------

print("\nSTEP 2 : DATA INFORMATION")


print(df.info())


print(df.describe())


# ---------------------------------------------------

print("\nSTEP 3 : CHECK MISSING VALUES")


print(
    df.isnull().sum()
)



# ---------------------------------------------------

print("\nSTEP 4 : DATA CLEANING")


# Fill numerical missing values

for col in df.select_dtypes(
    include="number"
):

    df[col] = df[col].fillna(
        df[col].mean()
    )


# Fill categorical values

for col in df.select_dtypes(
    include="object"
):

    df[col] = df[col].fillna(
        "Unknown"
    )


print(
    df.isnull().sum()
)



# ---------------------------------------------------

print("\nSTEP 5 : EDA")


print(
    df.corr(numeric_only=True)
)



plt.figure(figsize=(8,5))


plt.hist(
    df["Price"]
)


plt.title(
    "House Price Distribution"
)


plt.xlabel(
    "Price"
)


plt.ylabel(
    "Count"
)


plt.show()



# ---------------------------------------------------

print("\nSTEP 6 : FEATURE ENGINEERING")


# Create new feature

df["Price_per_area"] = (
    df["Price"] /
    df["Area"]
)


print(df.head())



# ---------------------------------------------------

print("\nSTEP 7 : ENCODING")


encoder = LabelEncoder()


df["Location"] = encoder.fit_transform(
    df["Location"]
)



# ---------------------------------------------------

print("\nSTEP 8 : SPLIT FEATURES")


X = df.drop(
    "Price",
    axis=1
)


y = df["Price"]



# ---------------------------------------------------

print("\nSTEP 9 : TRAIN TEST SPLIT")


X_train, X_test, y_train, y_test = train_test_split(

    X,
    y,
    test_size=0.2,
    random_state=42

)



# ---------------------------------------------------

print("\nSTEP 10 : FEATURE SCALING")


scaler = StandardScaler()


X_train = scaler.fit_transform(
    X_train
)


X_test = scaler.transform(
    X_test
)



# ---------------------------------------------------

print("\nSTEP 11 : TRAIN LINEAR REGRESSION")


lr = LinearRegression()


lr.fit(
    X_train,
    y_train
)


lr_prediction = lr.predict(
    X_test
)



# ---------------------------------------------------

print("\nSTEP 12 : RANDOM FOREST")


rf = RandomForestRegressor(
    n_estimators=100,
    random_state=42
)


rf.fit(
    X_train,
    y_train
)


rf_prediction = rf.predict(
    X_test
)



# ---------------------------------------------------

print("\nSTEP 13 : MODEL EVALUATION")


def evaluate(
    actual,
    prediction
):

    print(
        "MAE:",
        mean_absolute_error(
            actual,
            prediction
        )
    )


    print(
        "RMSE:",
        np.sqrt(
            mean_squared_error(
                actual,
                prediction
            )
        )
    )


    print(
        "R2 Score:",
        r2_score(
            actual,
            prediction
        )
    )



print("\nLinear Regression")

evaluate(
    y_test,
    lr_prediction
)



print("\nRandom Forest")

evaluate(
    y_test,
    rf_prediction
)



# ---------------------------------------------------

print("\nSTEP 14 : SAVE MODEL")


joblib.dump(
    rf,
    "models/house_price_model.pkl"
)


joblib.dump(
    scaler,
    "models/scaler.pkl"
)


print(
    "Model Saved Successfully"
)



print("\nDay 15 Completed Successfully!")
