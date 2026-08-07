# ==========================================================
# DAY 31 - END TO END MACHINE LEARNING PROJECT
# ==========================================================

# Import Libraries

import pandas as pd
import joblib

from sklearn.model_selection import train_test_split

from sklearn.impute import SimpleImputer

from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler

from sklearn.ensemble import RandomForestClassifier

from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report

# ==========================================================
# Q1. Load Dataset
# ==========================================================

df = pd.read_csv("titanic.csv")

print(df.head())

# ==========================================================
# Q2. Display Dataset Information
# ==========================================================

print(df.info())

print(df.isnull().sum())

# ==========================================================
# Q3. Handle Missing Values
# ==========================================================

age_imputer = SimpleImputer(strategy="median")
df["Age"] = age_imputer.fit_transform(df[["Age"]])

embarked_imputer = SimpleImputer(strategy="most_frequent")
df["Embarked"] = embarked_imputer.fit_transform(df[["Embarked"]]).ravel()

# ==========================================================
# Q4. Remove Duplicate Rows
# ==========================================================

df = df.drop_duplicates()

# ==========================================================
# Q5. Encode Categorical Features
# ==========================================================

label_encoder = LabelEncoder()

df["Sex"] = label_encoder.fit_transform(df["Sex"])
df["Embarked"] = label_encoder.fit_transform(df["Embarked"])

# ==========================================================
# Q6. Select Required Features
# ==========================================================

features = [

    "Pclass",
    "Sex",
    "Age",
    "SibSp",
    "Parch",
    "Fare",
    "Embarked"

]

X = df[features]

y = df["Survived"]

# ==========================================================
# Q7. Feature Scaling
# ==========================================================

scaler = StandardScaler()

X = scaler.fit_transform(X)

# ==========================================================
# Q8. Train Test Split
# ==========================================================

X_train, X_test, y_train, y_test = train_test_split(

    X,
    y,

    test_size=0.20,

    random_state=42

)

# ==========================================================
# Q9. Train Random Forest Model
# ==========================================================

model = RandomForestClassifier(

    n_estimators=100,

    random_state=42

)

model.fit(

    X_train,

    y_train

)

# ==========================================================
# Q10. Prediction
# ==========================================================

prediction = model.predict(

    X_test

)

# ==========================================================
# Q11. Accuracy
# ==========================================================

accuracy = accuracy_score(

    y_test,

    prediction

)

print("Accuracy :", accuracy)

# ==========================================================
# Q12. Confusion Matrix
# ==========================================================

print(

    confusion_matrix(

        y_test,

        prediction

    )

)

# ==========================================================
# Q13. Classification Report
# ==========================================================

print(

    classification_report(

        y_test,

        prediction

    )

)

# ==========================================================
# Q14. Save Model and Scaler
# ==========================================================

joblib.dump(

    model,

    "random_forest_model.pkl"

)

joblib.dump(

    scaler,

    "standard_scaler.pkl"

)

print("Model Saved Successfully")

# ==========================================================
# Q15. Test Saved Model
# ==========================================================

loaded_model = joblib.load(

    "random_forest_model.pkl"

)

sample_prediction = loaded_model.predict(

    X_test[:5]

)

print(sample_prediction)

# ==========================================================
# END OF DAY 31
# ==========================================================
