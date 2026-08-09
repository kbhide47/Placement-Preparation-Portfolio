# ==========================================================
# DAY 33 - ML PIPELINE + COLUMN TRANSFORMER
# ==========================================================

import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer

from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder, StandardScaler

from sklearn.ensemble import RandomForestClassifier

from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix
)


# ==========================================================
# Q1. Load Dataset
# ==========================================================

df = pd.read_csv("titanic.csv")

print(df.head())


# ==========================================================
# Q2. Select Useful Columns
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
# Q3. Identify Numerical Columns
# ==========================================================

numeric_features = [
    "Age",
    "SibSp",
    "Parch",
    "Fare",
    "Pclass"
]


# ==========================================================
# Q4. Identify Categorical Columns
# ==========================================================

categorical_features = [
    "Sex",
    "Embarked"
]


# ==========================================================
# Q5. Create Numerical Preprocessing Pipeline
# ==========================================================

numeric_pipeline = Pipeline(
    steps=[
        (
            "imputer",
            SimpleImputer(strategy="median")
        ),
        (
            "scaler",
            StandardScaler()
        )
    ]
)


# ==========================================================
# Q6. Create Categorical Preprocessing Pipeline
# ==========================================================

categorical_pipeline = Pipeline(
    steps=[
        (
            "imputer",
            SimpleImputer(strategy="most_frequent")
        ),
        (
            "encoder",
            OneHotEncoder(
                handle_unknown="ignore"
            )
        )
    ]
)


# ==========================================================
# Q7. Combine Both Pipelines
# ==========================================================

preprocessor = ColumnTransformer(
    transformers=[
        (
            "numeric",
            numeric_pipeline,
            numeric_features
        ),
        (
            "categorical",
            categorical_pipeline,
            categorical_features
        )
    ]
)


# ==========================================================
# Q8. Create ML Model
# ==========================================================

model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)


# ==========================================================
# Q9. Create Complete ML Pipeline
# ==========================================================

ml_pipeline = Pipeline(
    steps=[
        (
            "preprocessing",
            preprocessor
        ),
        (
            "model",
            model
        )
    ]
)


# ==========================================================
# Q10. Split Data
# ==========================================================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)


# ==========================================================
# Q11. Train Complete Pipeline
# ==========================================================

ml_pipeline.fit(
    X_train,
    y_train
)


# ==========================================================
# Q12. Make Predictions
# ==========================================================

prediction = ml_pipeline.predict(
    X_test
)


# ==========================================================
# Q13. Calculate Accuracy
# ==========================================================

accuracy = accuracy_score(
    y_test,
    prediction
)

print(
    "Accuracy:",
    accuracy
)


# ==========================================================
# Q14. Display Confusion Matrix
# ==========================================================

print(
    "Confusion Matrix:"
)

print(
    confusion_matrix(
        y_test,
        prediction
    )
)


# ==========================================================
# Q15. Classification Report
# ==========================================================

print(
    classification_report(
        y_test,
        prediction
    )
)


# ==========================================================
# Q16. Predict a New Passenger
# ==========================================================

new_passenger = pd.DataFrame({

    "Pclass": [1],
    "Sex": ["female"],
    "Age": [25],
    "SibSp": [0],
    "Parch": [0],
    "Fare": [100],
    "Embarked": ["C"]

})


new_prediction = ml_pipeline.predict(
    new_passenger
)

print(
    "New Passenger Prediction:",
    new_prediction
)


# ==========================================================
# Q17. Predict Probability
# ==========================================================

probability = ml_pipeline.predict_proba(
    new_passenger
)

print(
    "Prediction Probability:",
    probability
)


# ==========================================================
# Q18. Save Complete Pipeline
# ==========================================================

joblib.dump(
    ml_pipeline,
    "titanic_ml_pipeline.pkl"
)

print(
    "Complete Pipeline Saved Successfully"
)


# ==========================================================
# Q19. Load Complete Pipeline
# ==========================================================

loaded_pipeline = joblib.load(
    "titanic_ml_pipeline.pkl"
)


# ==========================================================
# Q20. Test Loaded Pipeline
# ==========================================================

loaded_prediction = loaded_pipeline.predict(
    new_passenger
)

print(
    "Loaded Pipeline Prediction:",
    loaded_prediction
)


# ==========================================================
# END OF DAY 33
# ==========================================================
