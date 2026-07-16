# ==========================================================
# DAY 11 - REGRESSION
# Topics:
# 1. Load Dataset
# 2. Train-Test Split
# 3. Linear Regression
# 4. Decision Tree Regressor
# 5. Random Forest Regressor
# 6. KNN Regressor
# 7. Evaluation Metrics
# ==========================================================

import pandas as pd

from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split

from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.neighbors import KNeighborsRegressor

from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score
)

import numpy as np

# -------------------------------------------------------

print("="*60)
print("Question 1 : Load Dataset")
print("="*60)

housing = fetch_california_housing()

X = pd.DataFrame(housing.data, columns=housing.feature_names)

y = housing.target

print(X.head())

# -------------------------------------------------------

print("\nQuestion 2 : Dataset Shape")

print(X.shape)

# -------------------------------------------------------

print("\nQuestion 3 : Train-Test Split")

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

print("Training Samples :", X_train.shape[0])
print("Testing Samples :", X_test.shape[0])

# -------------------------------------------------------

print("\nQuestion 4 : Linear Regression")

linear = LinearRegression()

linear.fit(X_train, y_train)

linear_pred = linear.predict(X_test)

print("Prediction Completed")

# -------------------------------------------------------

print("\nQuestion 5 : Decision Tree Regressor")

tree = DecisionTreeRegressor(random_state=42)

tree.fit(X_train, y_train)

tree_pred = tree.predict(X_test)

print("Prediction Completed")

# -------------------------------------------------------

print("\nQuestion 6 : Random Forest Regressor")

forest = RandomForestRegressor(
    n_estimators=100,
    random_state=42
)

forest.fit(X_train, y_train)

forest_pred = forest.predict(X_test)

print("Prediction Completed")

# -------------------------------------------------------

print("\nQuestion 7 : KNN Regressor")

knn = KNeighborsRegressor()

knn.fit(X_train, y_train)

knn_pred = knn.predict(X_test)

print("Prediction Completed")

# -------------------------------------------------------

print("\nQuestion 8 : Linear Regression Metrics")

print("MAE :", mean_absolute_error(y_test, linear_pred))

print("MSE :", mean_squared_error(y_test, linear_pred))

print("RMSE :", np.sqrt(mean_squared_error(y_test, linear_pred)))

print("R2 Score :", r2_score(y_test, linear_pred))

# -------------------------------------------------------

print("\nQuestion 9 : Decision Tree Metrics")

print("MAE :", mean_absolute_error(y_test, tree_pred))

print("MSE :", mean_squared_error(y_test, tree_pred))

print("RMSE :", np.sqrt(mean_squared_error(y_test, tree_pred)))

print("R2 Score :", r2_score(y_test, tree_pred))

# -------------------------------------------------------

print("\nQuestion 10 : Random Forest Metrics")

print("MAE :", mean_absolute_error(y_test, forest_pred))

print("MSE :", mean_squared_error(y_test, forest_pred))

print("RMSE :", np.sqrt(mean_squared_error(y_test, forest_pred)))

print("R2 Score :", r2_score(y_test, forest_pred))

# -------------------------------------------------------

print("\nQuestion 11 : KNN Metrics")

print("MAE :", mean_absolute_error(y_test, knn_pred))

print("MSE :", mean_squared_error(y_test, knn_pred))

print("RMSE :", np.sqrt(mean_squared_error(y_test, knn_pred)))

print("R2 Score :", r2_score(y_test, knn_pred))

# -------------------------------------------------------

print("\nQuestion 12 : Compare First 10 Predictions")

comparison = pd.DataFrame({
    "Actual": y_test[:10],
    "Linear": linear_pred[:10],
    "DecisionTree": tree_pred[:10],
    "RandomForest": forest_pred[:10],
    "KNN": knn_pred[:10]
})

print(comparison)

# -------------------------------------------------------

print("\nQuestion 13 : Best Model")

scores = {
    "Linear Regression": r2_score(y_test, linear_pred),
    "Decision Tree": r2_score(y_test, tree_pred),
    "Random Forest": r2_score(y_test, forest_pred),
    "KNN": r2_score(y_test, knn_pred)
}

best_model = max(scores, key=scores.get)

print("Best Model :", best_model)
print("Best R2 Score :", scores[best_model])

# -------------------------------------------------------

print("\nQuestion 14 : Feature Names")

print(X.columns)

# -------------------------------------------------------

print("\nQuestion 15 : Dataset Summary")

print(X.describe())

# -------------------------------------------------------

print("\nDay 11 Completed Successfully!")
