# ==========================================================
# DAY 17 - ADVANCED MACHINE LEARNING
#
# Topics:
# 1. Feature Selection
# 2. Feature Importance
# 3. Handling Imbalanced Data (SMOTE)
# 4. ROC Curve
# 5. AUC Score
# 6. XGBoost Classifier
# ==========================================================

import pandas as pd
import matplotlib.pyplot as plt

from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (
    accuracy_score,
    roc_curve,
    roc_auc_score
)

from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2

from imblearn.over_sampling import SMOTE

from xgboost import XGBClassifier

# ---------------------------------------------------------

print("="*60)
print("Question 1 : Load Dataset")
print("="*60)

data = load_breast_cancer()

X = pd.DataFrame(data.data, columns=data.feature_names)

y = data.target

print(X.head())

# ---------------------------------------------------------

print("\nQuestion 2 : Train Test Split")

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# ---------------------------------------------------------

print("\nQuestion 3 : Feature Selection")

selector = SelectKBest(score_func=chi2, k=10)

X_train_selected = selector.fit_transform(X_train, y_train)

X_test_selected = selector.transform(X_test)

selected_features = X.columns[selector.get_support()]

print("Selected Features:")
print(selected_features)

# ---------------------------------------------------------

print("\nQuestion 4 : Random Forest")

rf = RandomForestClassifier(random_state=42)

rf.fit(X_train_selected, y_train)

rf_pred = rf.predict(X_test_selected)

print("Accuracy:",
      accuracy_score(y_test, rf_pred))

# ---------------------------------------------------------

print("\nQuestion 5 : Feature Importance")

importance = pd.DataFrame({
    "Feature": selected_features,
    "Importance": rf.feature_importances_
})

importance = importance.sort_values(
    by="Importance",
    ascending=False
)

print(importance)

# ---------------------------------------------------------

print("\nQuestion 6 : Handle Imbalanced Data")

smote = SMOTE(random_state=42)

X_resampled, y_resampled = smote.fit_resample(X_train, y_train)

print("Original Shape :", X_train.shape)
print("After SMOTE :", X_resampled.shape)

# ---------------------------------------------------------

print("\nQuestion 7 : Train XGBoost")

xgb = XGBClassifier(
    random_state=42,
    eval_metric="logloss"
)

xgb.fit(X_resampled, y_resampled)

xgb_pred = xgb.predict(X_test)

print("Accuracy:",
      accuracy_score(y_test, xgb_pred))

# ---------------------------------------------------------

print("\nQuestion 8 : ROC-AUC Score")

probability = xgb.predict_proba(X_test)[:,1]

auc = roc_auc_score(y_test, probability)

print("ROC AUC Score :", auc)

# ---------------------------------------------------------

print("\nQuestion 9 : ROC Curve")

fpr, tpr, threshold = roc_curve(
    y_test,
    probability
)

plt.figure(figsize=(8,5))

plt.plot(fpr, tpr)

plt.plot([0,1],[0,1],"--")

plt.title("ROC Curve")

plt.xlabel("False Positive Rate")

plt.ylabel("True Positive Rate")

plt.show()

# ---------------------------------------------------------

print("\nQuestion 10 : Compare Models")

print("Random Forest Accuracy:",
      accuracy_score(y_test, rf_pred))

print("XGBoost Accuracy:",
      accuracy_score(y_test, xgb_pred))

print("\nDay 17 Completed Successfully!")
