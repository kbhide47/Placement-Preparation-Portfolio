# ==========================================================
# DAY 12 - CLASSIFICATION
# Topics:
# 1. Load Dataset
# 2. Train-Test Split
# 3. Logistic Regression
# 4. Decision Tree Classifier
# 5. Random Forest Classifier
# 6. KNN Classifier
# 7. Naive Bayes
# 8. Support Vector Machine (SVM)
# 9. Accuracy
# 10. Precision
# 11. Recall
# 12. F1 Score
# 13. Confusion Matrix
# ==========================================================

import pandas as pd

from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split

from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix
)

# -------------------------------------------------------

print("="*60)
print("Question 1 : Load Dataset")
print("="*60)

data = load_breast_cancer()

X = pd.DataFrame(data.data, columns=data.feature_names)
y = data.target

print(X.head())

# -------------------------------------------------------

print("\nQuestion 2 : Dataset Shape")

print(X.shape)

# -------------------------------------------------------

print("\nQuestion 3 : Train Test Split")

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

print("Training Samples :", X_train.shape[0])
print("Testing Samples :", X_test.shape[0])

# -------------------------------------------------------

print("\nQuestion 4 : Logistic Regression")

lr = LogisticRegression(max_iter=10000)

lr.fit(X_train, y_train)

lr_pred = lr.predict(X_test)

# -------------------------------------------------------

print("\nQuestion 5 : Decision Tree")

dt = DecisionTreeClassifier(random_state=42)

dt.fit(X_train, y_train)

dt_pred = dt.predict(X_test)

# -------------------------------------------------------

print("\nQuestion 6 : Random Forest")

rf = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

rf.fit(X_train, y_train)

rf_pred = rf.predict(X_test)

# -------------------------------------------------------

print("\nQuestion 7 : KNN")

knn = KNeighborsClassifier()

knn.fit(X_train, y_train)

knn_pred = knn.predict(X_test)

# -------------------------------------------------------

print("\nQuestion 8 : Naive Bayes")

nb = GaussianNB()

nb.fit(X_train, y_train)

nb_pred = nb.predict(X_test)

# -------------------------------------------------------

print("\nQuestion 9 : Support Vector Machine")

svm = SVC()

svm.fit(X_train, y_train)

svm_pred = svm.predict(X_test)

# -------------------------------------------------------

def evaluate(name, y_true, y_pred):

    print("\n" + "="*50)
    print(name)
    print("="*50)

    print("Accuracy :", accuracy_score(y_true, y_pred))

    print("Precision :", precision_score(y_true, y_pred))

    print("Recall :", recall_score(y_true, y_pred))

    print("F1 Score :", f1_score(y_true, y_pred))

    print("Confusion Matrix")

    print(confusion_matrix(y_true, y_pred))

# -------------------------------------------------------

print("\nQuestion 10 : Model Evaluation")

evaluate("Logistic Regression", y_test, lr_pred)

evaluate("Decision Tree", y_test, dt_pred)

evaluate("Random Forest", y_test, rf_pred)

evaluate("KNN", y_test, knn_pred)

evaluate("Naive Bayes", y_test, nb_pred)

evaluate("Support Vector Machine", y_test, svm_pred)

# -------------------------------------------------------

print("\nQuestion 11 : Compare First 10 Predictions")

comparison = pd.DataFrame({
    "Actual": y_test[:10],
    "Logistic": lr_pred[:10],
    "DecisionTree": dt_pred[:10],
    "RandomForest": rf_pred[:10],
    "KNN": knn_pred[:10],
    "NaiveBayes": nb_pred[:10],
    "SVM": svm_pred[:10]
})

print(comparison)

# -------------------------------------------------------

print("\nQuestion 12 : Best Model")

scores = {
    "Logistic Regression": accuracy_score(y_test, lr_pred),
    "Decision Tree": accuracy_score(y_test, dt_pred),
    "Random Forest": accuracy_score(y_test, rf_pred),
    "KNN": accuracy_score(y_test, knn_pred),
    "Naive Bayes": accuracy_score(y_test, nb_pred),
    "SVM": accuracy_score(y_test, svm_pred)
}

best_model = max(scores, key=scores.get)

print("Best Model :", best_model)

print("Best Accuracy :", scores[best_model])

# -------------------------------------------------------

print("\nQuestion 13 : Feature Names")

print(X.columns)

# -------------------------------------------------------

print("\nQuestion 14 : Dataset Summary")

print(X.describe())

# -------------------------------------------------------

print("\nQuestion 15 : Target Classes")

print(data.target_names)

# -------------------------------------------------------

print("\nDay 12 Completed Successfully!")
