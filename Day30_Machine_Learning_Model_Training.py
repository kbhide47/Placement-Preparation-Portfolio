# ==========================================================
# DAY 30 - MACHINE LEARNING MODEL TRAINING
# ==========================================================


# Import Libraries

import pandas as pd

from sklearn.model_selection import train_test_split

from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix,
    classification_report
)

import joblib


# ==========================================================
# Q1. Load Preprocessed Dataset
# ==========================================================

df = pd.read_csv("titanic_preprocessed.csv")


print(df.head())



# ==========================================================
# Q2. Separate Features and Target
# ==========================================================

X = df.drop(
    "Survived",
    axis=1
)


y = df["Survived"]



# ==========================================================
# Q3. Split Data into Training and Testing
# ==========================================================

X_train, X_test, y_train, y_test = train_test_split(

    X,
    y,

    test_size=0.2,

    random_state=42

)


print(X_train.shape)
print(X_test.shape)



# ==========================================================
# Q4. Train Logistic Regression Model
# ==========================================================

logistic_model = LogisticRegression(
    max_iter=1000
)


logistic_model.fit(
    X_train,
    y_train
)



# ==========================================================
# Q5. Make Predictions
# ==========================================================

logistic_prediction = logistic_model.predict(
    X_test
)


print(logistic_prediction)



# ==========================================================
# Q6. Evaluate Logistic Regression
# ==========================================================


print(
    "Accuracy:",
    accuracy_score(
        y_test,
        logistic_prediction
    )
)


print(
    "Precision:",
    precision_score(
        y_test,
        logistic_prediction
    )
)


print(
    "Recall:",
    recall_score(
        y_test,
        logistic_prediction
    )
)


print(
    "F1 Score:",
    f1_score(
        y_test,
        logistic_prediction
    )
)



# ==========================================================
# Q7. Confusion Matrix
# ==========================================================

print(
    confusion_matrix(
        y_test,
        logistic_prediction
    )
)



# ==========================================================
# Q8. Classification Report
# ==========================================================

print(
    classification_report(
        y_test,
        logistic_prediction
    )
)



# ==========================================================
# Q9. Train Decision Tree Model
# ==========================================================


decision_tree = DecisionTreeClassifier(
    random_state=42
)


decision_tree.fit(
    X_train,
    y_train
)


dt_prediction = decision_tree.predict(
    X_test
)


print(
    "Decision Tree Accuracy:",
    accuracy_score(
        y_test,
        dt_prediction
    )
)



# ==========================================================
# Q10. Train Random Forest Model
# ==========================================================


random_forest = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)


random_forest.fit(
    X_train,
    y_train
)


rf_prediction = random_forest.predict(
    X_test
)



print(
    "Random Forest Accuracy:",
    accuracy_score(
        y_test,
        rf_prediction
    )
)



# ==========================================================
# Q11. Compare Models
# ==========================================================


models = {

    "Logistic Regression":
    accuracy_score(
        y_test,
        logistic_prediction
    ),


    "Decision Tree":
    accuracy_score(
        y_test,
        dt_prediction
    ),


    "Random Forest":
    accuracy_score(
        y_test,
        rf_prediction
    )

}


print(models)



# ==========================================================
# Q12. Select Best Model
# ==========================================================


best_model = random_forest



# ==========================================================
# Q13. Save Model using Joblib
# ==========================================================


joblib.dump(
    best_model,
    "best_model.pkl"
)


print(
    "Model Saved Successfully"
)



# ==========================================================
# Q14. Load Saved Model
# ==========================================================


loaded_model = joblib.load(
    "best_model.pkl"
)



# ==========================================================
# Q15. Test Prediction Using Saved Model
# ==========================================================


prediction = loaded_model.predict(
    X_test.iloc[:5]
)


print(
    prediction
)



# ==========================================================
# END OF DAY 30
# ==========================================================
