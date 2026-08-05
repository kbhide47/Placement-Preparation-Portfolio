# ==========================================================
# DAY 29 - FEATURE ENGINEERING & DATA PREPROCESSING
# ==========================================================

import pandas as pd

from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import MinMaxScaler

from sklearn.model_selection import train_test_split

# ----------------------------------------------------------
# Load Dataset
# ----------------------------------------------------------

df = pd.read_csv("titanic.csv")

# ----------------------------------------------------------
# Q1. Display first 5 rows.
# ----------------------------------------------------------

print(df.head())

# ----------------------------------------------------------
# Q2. Display dataset information.
# ----------------------------------------------------------

print(df.info())

# ----------------------------------------------------------
# Q3. Check missing values.
# ----------------------------------------------------------

print(df.isnull().sum())

# ----------------------------------------------------------
# Q4. Fill missing Age with median.
# ----------------------------------------------------------

df["Age"] = df["Age"].fillna(df["Age"].median())

# ----------------------------------------------------------
# Q5. Fill missing Embarked with mode.
# ----------------------------------------------------------

df["Embarked"] = df["Embarked"].fillna(df["Embarked"].mode()[0])

# ----------------------------------------------------------
# Q6. Remove duplicate rows.
# ----------------------------------------------------------

df = df.drop_duplicates()

# ----------------------------------------------------------
# Q7. Label Encode Sex column.
# Male = 1, Female = 0
# ----------------------------------------------------------

label_encoder = LabelEncoder()

df["Sex"] = label_encoder.fit_transform(df["Sex"])

print(df["Sex"].head())

# ----------------------------------------------------------
# Q8. One Hot Encode Embarked column.
# ----------------------------------------------------------

encoder = OneHotEncoder(sparse_output=False)

encoded = encoder.fit_transform(df[["Embarked"]])

encoded_df = pd.DataFrame(
    encoded,
    columns=encoder.get_feature_names_out(["Embarked"])
)

df = pd.concat(
    [df.reset_index(drop=True), encoded_df],
    axis=1
)

df.drop("Embarked", axis=1, inplace=True)

# ----------------------------------------------------------
# Q9. Standard Scaling Age and Fare.
# ----------------------------------------------------------

standard_scaler = StandardScaler()

df[["Age", "Fare"]] = standard_scaler.fit_transform(
    df[["Age", "Fare"]]
)

# ----------------------------------------------------------
# Q10. Display scaled Age and Fare.
# ----------------------------------------------------------

print(df[["Age", "Fare"]].head())

# ----------------------------------------------------------
# Q11. Min-Max Scaling SibSp and Parch.
# ----------------------------------------------------------

minmax_scaler = MinMaxScaler()

df[["SibSp", "Parch"]] = minmax_scaler.fit_transform(
    df[["SibSp", "Parch"]]
)

# ----------------------------------------------------------
# Q12. Select Features (X)
# ----------------------------------------------------------

X = df.drop("Survived", axis=1)

# ----------------------------------------------------------
# Q13. Select Target (y)
# ----------------------------------------------------------

y = df["Survived"]

# ----------------------------------------------------------
# Q14. Train-Test Split
# ----------------------------------------------------------

X_train, X_test, y_train, y_test = train_test_split(

    X,
    y,

    test_size=0.20,

    random_state=42

)

print("Training Shape :", X_train.shape)
print("Testing Shape  :", X_test.shape)

# ----------------------------------------------------------
# Q15. Save Processed Dataset
# ----------------------------------------------------------

df.to_csv(
    "titanic_preprocessed.csv",
    index=False
)

print("Feature Engineering Completed Successfully!")

# ==========================================================
# END OF DAY 29
# ==========================================================
