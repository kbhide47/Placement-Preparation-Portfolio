# ==========================================================
# DAY 13 - MODEL OPTIMIZATION
# Topics:
# 1. Overfitting
# 2. Underfitting
# 3. Bias Variance
# 4. Cross Validation
# 5. GridSearchCV
# 6. RandomizedSearchCV
# 7. Feature Importance
# 8. Pipeline
# 9. Model Comparison
# ==========================================================


import pandas as pd

from sklearn.datasets import load_breast_cancer

from sklearn.model_selection import (
    train_test_split,
    cross_val_score,
    GridSearchCV,
    RandomizedSearchCV
)

from sklearn.ensemble import RandomForestClassifier

from sklearn.pipeline import Pipeline

from sklearn.preprocessing import StandardScaler

from sklearn.metrics import accuracy_score


# ---------------------------------------------------------

print("="*60)
print("Question 1 : Load Dataset")
print("="*60)


data = load_breast_cancer()


X = pd.DataFrame(
    data.data,
    columns=data.feature_names
)


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


print(X_train.shape)
print(X_test.shape)



# ---------------------------------------------------------

print("\nQuestion 3 : Basic Random Forest Model")


model = RandomForestClassifier(
    random_state=42
)


model.fit(
    X_train,
    y_train
)


prediction = model.predict(X_test)


print(
    "Accuracy:",
    accuracy_score(y_test,prediction)
)



# ---------------------------------------------------------

print("\nQuestion 4 : Cross Validation")


scores = cross_val_score(
    model,
    X,
    y,
    cv=5
)


print("CV Scores:")
print(scores)


print(
    "Average CV Score:",
    scores.mean()
)



# ---------------------------------------------------------

print("\nQuestion 5 : Hyperparameters")


print(model.get_params())



# ---------------------------------------------------------

print("\nQuestion 6 : GridSearchCV")


parameters = {

    "n_estimators":[50,100,150],

    "max_depth":[5,10,15,None],

    "criterion":[
        "gini",
        "entropy"
    ]
}



grid = GridSearchCV(
    RandomForestClassifier(
        random_state=42
    ),
    parameters,
    cv=5
)


grid.fit(
    X_train,
    y_train
)


print(
    "Best Parameters:"
)

print(grid.best_params_)



print(
    "Best Score:"
)

print(grid.best_score_)



# ---------------------------------------------------------

print("\nQuestion 7 : Randomized Search")


random_search = RandomizedSearchCV(
    RandomForestClassifier(
        random_state=42
    ),
    parameters,
    cv=5,
    n_iter=5,
    random_state=42
)


random_search.fit(
    X_train,
    y_train
)


print(
    random_search.best_params_
)



# ---------------------------------------------------------

print("\nQuestion 8 : Feature Importance")


best_model = grid.best_estimator_


importance = pd.DataFrame({

    "Feature":
    X.columns,

    "Importance":
    best_model.feature_importances_

})


importance = importance.sort_values(
    by="Importance",
    ascending=False
)


print(importance.head(10))



# ---------------------------------------------------------

print("\nQuestion 9 : Pipeline")


pipeline = Pipeline([

    (
        "scaler",
        StandardScaler()
    ),

    (
        "model",
        RandomForestClassifier(
            random_state=42
        )
    )

])



pipeline.fit(
    X_train,
    y_train
)



pipe_prediction = pipeline.predict(
    X_test
)



print(
    "Pipeline Accuracy:",
    accuracy_score(
        y_test,
        pipe_prediction
    )
)



# ---------------------------------------------------------

print("\nQuestion 10 : Final Model Comparison")


models = {

    "Normal Random Forest":
    model,

    "Grid Search Model":
    grid.best_estimator_,

    "Pipeline Model":
    pipeline

}



for name,m in models.items():

    pred = m.predict(X_test)

    print(
        name,
        ":",
        accuracy_score(
            y_test,
            pred
        )
    )


# ---------------------------------------------------------

print("\nQuestion 11 : Overfitting Check")


train_score = model.score(
    X_train,
    y_train
)


test_score = model.score(
    X_test,
    y_test
)


print(
    "Training Accuracy:",
    train_score
)


print(
    "Testing Accuracy:",
    test_score
)



# ---------------------------------------------------------

print("\nDay 13 Completed Successfully!")
