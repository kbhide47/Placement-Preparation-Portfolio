# ==========================================================
# DAY 34 - FASTAPI + REST API + ML MODEL API
# ==========================================================

# Install first:
#
# pip install fastapi uvicorn pandas scikit-learn joblib
#
# Run API:
#
# uvicorn day34_api:app --reload
#
# Then open:
#
# http://127.0.0.1:8000/docs


from fastapi import FastAPI
from pydantic import BaseModel
import joblib


# ==========================================================
# Q1. Create FastAPI Application
# ==========================================================

app = FastAPI(
    title="Titanic ML Prediction API",
    description="API for Titanic survival prediction",
    version="1.0"
)


# ==========================================================
# Q2. Create a Basic GET Endpoint
# ==========================================================

@app.get("/")
def home():

    return {
        "message": "Titanic ML API is running"
    }


# ==========================================================
# Q3. Create an API Health Check
# ==========================================================

@app.get("/health")
def health_check():

    return {
        "status": "healthy"
    }


# ==========================================================
# Q4. Create Pydantic Request Model
# ==========================================================

class Passenger(BaseModel):

    Pclass: int

    Sex: str

    Age: float

    SibSp: int

    Parch: int

    Fare: float

    Embarked: str


# ==========================================================
# Q5. Load Saved ML Pipeline
# ==========================================================

model = joblib.load(
    "titanic_ml_pipeline.pkl"
)


# ==========================================================
# Q6. Create POST Prediction Endpoint
# ==========================================================

@app.post("/predict")
def predict(passenger: Passenger):

    # Convert request data into DataFrame

    data = [[

        passenger.Pclass,

        passenger.Sex,

        passenger.Age,

        passenger.SibSp,

        passenger.Parch,

        passenger.Fare,

        passenger.Embarked

    ]]


    # Column names must match
    # the model's training features

    columns = [

        "Pclass",

        "Sex",

        "Age",

        "SibSp",

        "Parch",

        "Fare",

        "Embarked"

    ]


    import pandas as pd

    input_data = pd.DataFrame(
        data,
        columns=columns
    )


    # Make prediction

    prediction = model.predict(
        input_data
    )


    # Get probability

    probability = model.predict_proba(
        input_data
    )


    # Convert prediction to readable output

    if prediction[0] == 1:

        result = "Survived"

    else:

        result = "Did Not Survive"


    return {

        "prediction": int(prediction[0]),

        "result": result,

        "survival_probability":
            round(
                float(probability[0][1]),
                4
            )

    }


# ==========================================================
# Q7. Create Example GET Endpoint
# ==========================================================

@app.get("/model-info")
def model_info():

    return {

        "model": "Random Forest",

        "task": "Binary Classification",

        "target": "Survived",

        "features": [

            "Pclass",

            "Sex",

            "Age",

            "SibSp",

            "Parch",

            "Fare",

            "Embarked"

        ]

    }


# ==========================================================
# END OF DAY 34
# ==========================================================
