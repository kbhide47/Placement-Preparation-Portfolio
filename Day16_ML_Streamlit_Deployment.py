# ======================================================
# DAY 16 - MACHINE LEARNING DEPLOYMENT USING STREAMLIT
#
# Project:
# House Price Prediction App
#
# Concepts:
# 1. Import Streamlit
# 2. Load ML Model
# 3. User Input
# 4. Feature Processing
# 5. Prediction
# ======================================================


import streamlit as st

import pandas as pd

import joblib



# ---------------------------------------------------

# Load Model

model = joblib.load(
    "models/house_price_model.pkl"
)


scaler = joblib.load(
    "models/scaler.pkl"
)



# ---------------------------------------------------

# Page Configuration

st.set_page_config(
    page_title="House Price Predictor",
    page_icon="🏠"
)



# ---------------------------------------------------

st.title(
    "🏠 House Price Prediction System"
)


st.write(
    "Machine Learning Regression Application"
)



# ---------------------------------------------------

# User Inputs


area = st.number_input(
    "House Area (sq ft)",
    min_value=100
)


bedrooms = st.number_input(
    "Number of Bedrooms",
    min_value=1,
    max_value=10
)


bathrooms = st.number_input(
    "Number of Bathrooms",
    min_value=1,
    max_value=10
)


age = st.number_input(
    "House Age",
    min_value=0
)



location = st.selectbox(
    "Location",
    [
        "Pune",
        "Mumbai",
        "Delhi",
        "Bangalore"
    ]
)



parking = st.selectbox(
    "Parking Available",
    [
        0,
        1
    ]
)



# ---------------------------------------------------

# Prediction Button


if st.button(
    "Predict Price"
):


    input_data = pd.DataFrame({

        "Area":[area],

        "Bedrooms":[bedrooms],

        "Bathrooms":[bathrooms],

        "Age":[age],

        "Location":[location],

        "Parking":[parking]

    })



    # Encoding location

    location_mapping = {

        "Pune":0,

        "Mumbai":1,

        "Delhi":2,

        "Bangalore":3

    }


    input_data["Location"] = (
        input_data["Location"]
        .map(location_mapping)
    )



    # Scaling

    input_scaled = scaler.transform(
        input_data
    )



    # Prediction

    prediction = model.predict(
        input_scaled
    )



    st.success(
        f"Estimated House Price: ₹ {prediction[0]:,.2f}"
    )



# ---------------------------------------------------

st.sidebar.header(
    "About Project"
)


st.sidebar.write(
    """
    This application uses Machine Learning
    to predict house prices.
    
    Algorithms:
    
    - Linear Regression
    - Random Forest
    
    """
)
