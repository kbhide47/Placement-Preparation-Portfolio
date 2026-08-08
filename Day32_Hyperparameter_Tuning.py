# ==========================================================
# DAY 32 - HYPERPARAMETER TUNING & CROSS VALIDATION
# ==========================================================

import pandas as pd
import numpy as np

from sklearn.model_selection import (
    train_test_split,
    cross_val_score,
    KFold,
    GridSearchCV,
    RandomizedSearchCV
)

from sklearn.ensemble import (
    RandomForestClassifier,
    GradientBoostingClassifier
)

from sklearn.linear_model import LogisticRegression

from sklearn.metrics import (
    accuracy_score,
    classification_report
)


# ==========================================================
# Q1. Load Dataset
# ==========================================================

df = pd.read_csv("titanic.csv")

print(df.head())


# ==========================================================
# Q2. Handle Missing Values
# ==========================================================

df["Age"] = df["Age"].fillna(
    df["Age"].median()
)

df["Embarked"] = df["Embarked"].fillna(
    df["Embarked"].mode()[0]
)


# ==========================================================
# Q3. Encode Categorical Variables
# ==========================================================

df["Sex"] = df["Sex"].map({
    "male": 0,
    "female": 1
})

df["Embarked"] = df["Embarked"].map({
    "S": 0,
    "C": 1,
    "Q": 2
})


# ==========================================================
# Q4. Select Features
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
# Q5. Train-Test Split
# ==========================================================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)


# ==========================================================
# Q6. Train Basic Random Forest
# ==========================================================

model = RandomForestClassifier(
    random_state=42
)

model.fit(
    X_train,
    y_train
)

prediction = model.predict(
    X_test
)

print(
    "Basic Random Forest Accuracy:",
    accuracy_score(
        y_test,
        prediction
    )
)


# ==========================================================
# Q7. Perform K-Fold Cross Validation
# ==========================================================

kfold = KFold(
    n_splits=5,
    shuffle=True,
    random_state=42
)

scores = cross_val_score(
    model,
    X,
    y,
    cv=kfold,
    scoring="accuracy"
)

print("Cross Validation Scores:", scores)

print(
    "Average CV Score:",
    scores.mean()
)


# ==========================================================
# Q8. Compare Multiple Models
# ==========================================================

models = {

    "Logistic Regression":
        LogisticRegression(max_iter=1000),

    "Random Forest":
        RandomForestClassifier(
            random_state=42
        ),

    "Gradient Boosting":
        GradientBoostingClassifier(
            random_state=42
        )
}


for name, model in models.items():

    scores = cross_val_score(
        model,
        X,
        y,
        cv=5,
        scoring="accuracy"
    )

    print(
        name,
        "Average Accuracy:",
        scores.mean()
    )


# ==========================================================
# Q9. Create Hyperparameter Grid
# ==========================================================

param_grid = {

    "n_estimators": [
        50,
        100,
        200
    ],

    "max_depth": [
        None,
        5,
        10,
        15
    ],

    "min_samples_split": [
        2,
        5,
        10
    ],

    "min_samples_leaf": [
        1,
        2,
        4
    ]

}


# ==========================================================
# Q10. Perform GridSearchCV
# ==========================================================

rf = RandomForestClassifier(
    random_state=42
)

grid_search = GridSearchCV(

    estimator=rf,

    param_grid=param_grid,

    cv=5,

    scoring="accuracy",

    n_jobs=-1

)

grid_search.fit(
    X_train,
    y_train
)


# ==========================================================
# Q11. Display Best Parameters
# ==========================================================

print(
    "Best Parameters:"
)

print(
    grid_search.best_params_
)


# ==========================================================
# Q12. Display Best Cross Validation Score
# ==========================================================

print(
    "Best CV Score:",
    grid_search.best_score_
)


# ==========================================================
# Q13. Evaluate Best Model on Test Data
# ==========================================================

best_model = grid_search.best_estimator_

best_prediction = best_model.predict(
    X_test
)

print(
    "Test Accuracy:",
    accuracy_score(
        y_test,
        best_prediction
    )
)


# ==========================================================
# Q14. Classification Report
# ==========================================================

print(
    classification_report(
        y_test,
        best_prediction
    )
)


# ==========================================================
# Q15. Feature Importance
# ==========================================================

importance = pd.DataFrame({

    "Feature": features,

    "Importance":
        best_model.feature_importances_

})

importance = importance.sort_values(
    by="Importance",
    ascending=False
)

print(
    importance
)


# ==========================================================
# Q16. RandomizedSearchCV
# ==========================================================

random_grid = {

    "n_estimators":
        np.arange(50, 301, 50),

    "max_depth":
        [None, 5, 10, 15, 20],

    "min_samples_split":
        [2, 5, 10],

    "min_samples_leaf":
        [1, 2, 4]

}


random_search = RandomizedSearchCV(

    estimator=RandomForestClassifier(
        random_state=42
    ),

    param_distributions=random_grid,

    n_iter=10,

    cv=5,

    scoring="accuracy",

    random_state=42,

    n_jobs=-1

)

random_search.fit(
    X_train,
    y_train
)


# ==========================================================
# Q17. Display RandomizedSearchCV Results
# ==========================================================

print(
    "Random Search Best Parameters:"
)

print(
    random_search.best_params_
)

print(
    "Random Search Best Score:",
    random_search.best_score_
)


# ==========================================================
# Q18. Compare GridSearch and RandomSearch
# ==========================================================

print(
    "GridSearch Best Score:",
    grid_search.best_score_
)

print(
    "RandomSearch Best Score:",
    random_search.best_score_
)


# ==========================================================
# Q19. Find Most Important Feature
# ==========================================================

most_important_feature = importance.iloc[0]

print(
    "Most Important Feature:"
)

print(
    most_important_feature
)


# ==========================================================
# Q20. Final Model
# ==========================================================

final_model = grid_search.best_estimator_

print(
    "Final Model:"
)

print(
    final_model
)


# ==========================================================
# END OF DAY 32
# ==========================================================
