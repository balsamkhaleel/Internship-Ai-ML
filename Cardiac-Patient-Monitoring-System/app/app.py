import streamlit as st
import pandas as pd
import joblib
from pathlib import Path
from tensorflow.keras.models import load_model


# =========================
# Project Paths
# =========================

BASE_DIR = Path(__file__).resolve().parent.parent

MODEL_PATH = BASE_DIR / "models" / "final_neural_network.keras"
SCALER_PATH = BASE_DIR / "models" / "standard_scaler.joblib"
THRESHOLD_PATH = BASE_DIR / "models" / "best_threshold.txt"


# =========================
# Page Configuration
# =========================

st.set_page_config(
    page_title="Cardiac Patient Monitoring",
    page_icon="❤️",
    layout="centered"
)


# =========================
# Load Model, Scaler, Threshold
# =========================

model = load_model(MODEL_PATH)
scaler = joblib.load(SCALER_PATH)

with open(THRESHOLD_PATH, "r") as f:
    best_threshold = float(f.read().strip())


# =========================
# Page Title
# =========================

st.title("Cardiac Patient Monitoring System")

st.write(
    "Enter the patient's information below to estimate "
    "the probability of cardiovascular disease."
)

st.info(
    "This tool is for demonstration purposes and does not "
    "provide a medical diagnosis."
)


# =========================
# Patient Information
# =========================

st.header("Patient Information")

col1, col2 = st.columns(2)

with col1:

    age_years = st.number_input(
        "Age (years)",
        min_value=1,
        max_value=120,
        value=30
    )

    height = st.number_input(
        "Height (cm)",
        min_value=100,
        max_value=220,
        value=170
    )

    weight = st.number_input(
        "Weight (kg)",
        min_value=30.0,
        max_value=200.0,
        value=70.0
    )

    ap_hi = st.number_input(
        "Systolic Blood Pressure",
        min_value=40,
        max_value=300,
        value=120
    )

    ap_lo = st.number_input(
        "Diastolic Blood Pressure",
        min_value=40,
        max_value=200,
        value=80
    )


with col2:

    gender = st.selectbox(
        "Gender",
        options=[1, 2],
        format_func=lambda x: "Female" if x == 1 else "Male"
    )

    cholesterol = st.selectbox(
        "Cholesterol Level",
        options=[1, 2, 3],
        format_func=lambda x: {
            1: "Normal",
            2: "Above Normal",
            3: "Well Above Normal"
        }[x]
    )

    gluc = st.selectbox(
        "Glucose Level",
        options=[1, 2, 3],
        format_func=lambda x: {
            1: "Normal",
            2: "Above Normal",
            3: "Well Above Normal"
        }[x]
    )

    smoke = st.selectbox(
        "Smoking",
        options=[0, 1],
        format_func=lambda x: "No" if x == 0 else "Yes"
    )

    alco = st.selectbox(
        "Alcohol Intake",
        options=[0, 1],
        format_func=lambda x: "No" if x == 0 else "Yes"
    )

    active = st.selectbox(
        "Physical Activity",
        options=[0, 1],
        format_func=lambda x: "No" if x == 0 else "Yes"
    )


# =========================
# Prediction
# =========================

if st.button("Predict", use_container_width=True):

    # Calculate derived features
    bmi = weight / ((height / 100) ** 2)
    pulse_pressure = ap_hi - ap_lo
    map_value = ap_lo + (pulse_pressure / 3)

    # Prepare model features
    features = [[
        gender,
        height,
        weight,
        ap_hi,
        ap_lo,
        cholesterol,
        gluc,
        smoke,
        alco,
        active,
        age_years,
        bmi,
        pulse_pressure,
        map_value
    ]]

    feature_names = [
        "gender",
        "height",
        "weight",
        "ap_hi",
        "ap_lo",
        "cholesterol",
        "gluc",
        "smoke",
        "alco",
        "active",
        "age_years",
        "bmi",
        "pulse_pressure",
        "map"
    ]

    # Convert to DataFrame
    input_df = pd.DataFrame(
        features,
        columns=feature_names
    )

    # Apply the same scaler used during training
    scaled_features = scaler.transform(input_df)

    # Generate prediction probability
    probability = float(
        model.predict(
            scaled_features,
            verbose=0
        )[0][0]
    )

    # Apply final tuned threshold
    prediction = 1 if probability >= best_threshold else 0


    # =========================
    # Prediction Result
    # =========================

    st.subheader("Prediction Result")

    if prediction == 1:
        st.error("Cardio Risk Detected")
    else:
        st.success("No Cardio Risk Detected")

    st.metric(
        label="Estimated Probability",
        value=f"{probability:.2%}"
    )

    st.progress(probability)


    # =========================
    # Supporting Information
    # =========================

    st.subheader("Calculated Health Indicators")

    indicator_col1, indicator_col2, indicator_col3 = st.columns(3)

    with indicator_col1:
        st.metric("BMI", f"{bmi:.2f}")

    with indicator_col2:
        st.metric(
            "Pulse Pressure",
            f"{pulse_pressure:.1f}"
        )

    with indicator_col3:
        st.metric(
            "MAP",
            f"{map_value:.1f}"
        )


    # =========================
    # Probability Visualization
    # =========================

    st.subheader("Prediction Probability")

    probability_df = pd.DataFrame({
        "Result": [
            "No Cardio",
            "Cardio"
        ],
        "Probability": [
            1 - probability,
            probability
        ]
    })

    st.bar_chart(
        probability_df.set_index("Result"),
        y="Probability"
    )


    # =========================
    # Model Information
    # =========================

    st.caption(
        f"Classification threshold used: {best_threshold:.2f}"
    )


    # =========================
    # Disclaimer
    # =========================

    st.caption(
        "The prediction is generated by a machine learning model "
        "and is intended for demonstration purposes only."
    )