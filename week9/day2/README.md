# Sprint 4 — FastAPI Prediction API

## Overview

This sprint focuses on serving the serialized cardiovascular disease prediction model through a FastAPI REST API.

The API loads the trained neural network and the saved scaler, validates patient data, applies preprocessing, and returns a cardiovascular disease prediction.

## Objectives

* Load the serialized neural network model.
* Load the saved preprocessing scaler.
* Build a FastAPI application.
* Validate input data using Pydantic.
* Create a `POST /predict` endpoint.
* Apply the saved scaler before prediction.
* Use the optimized classification threshold of `0.42`.
* Test the API through FastAPI Swagger documentation.

## Model and Preprocessing

The API uses the following serialized files:

* `final_neural_network.keras` — trained neural network model.
* `standard_scaler.joblib` — fitted StandardScaler.

The model expects **14 input features** in the same order used during training:

```text
gender
height
weight
ap_hi
ap_lo
cholesterol
gluc
smoke
alco
active
age_years
bmi
pulse_pressure
map
```

## API Endpoint

### POST `/predict`

The endpoint receives patient information as a JSON request.

Example:

```json
{
  "gender": 1,
  "height": 180,
  "weight": 75,
  "ap_hi": 130,
  "ap_lo": 85,
  "cholesterol": 1,
  "gluc": 1,
  "smoke": 0,
  "alco": 0,
  "active": 1,
  "age_years": 35,
  "bmi": 23.15,
  "pulse_pressure": 45,
  "map": 100
}
```

Example response:

```json
{
  "prediction": 0,
  "probability": 0.4114757180213928,
  "threshold": 0.42
}
```

## Prediction Logic

The API follows this flow:

```text
Patient Data
     ↓
Pydantic Validation
     ↓
Feature Ordering
     ↓
Saved StandardScaler
     ↓
Neural Network
     ↓
Prediction Probability
     ↓
Threshold = 0.42
     ↓
Final Prediction
```

A probability greater than or equal to `0.42` is classified as:

```text
Prediction = 1
```

Otherwise:

```text
Prediction = 0
```

## Testing

The API was tested through the FastAPI interactive documentation:

```text
/docs
```

### Valid Test Cases

| Test Case | HTTP Status | Probability | Threshold | Prediction |
| --------- | ----------- | ----------- | --------- | ---------- |
| Test 1    | 200         | 0.8202      | 0.42      | 1          |
| Test 2    | 200         | 0.4115      | 0.42      | 0          |
| Test 3    | 200         | 0.0470      | 0.42      | 0          |

All valid requests returned HTTP `200 OK`.

### Invalid Input Test

An invalid value was provided for `age_years`.

The API returned:

```text
HTTP 422 Unprocessable Entity
```

This confirms that Pydantic validation correctly rejects invalid input before prediction.

## Technologies

* Python
* FastAPI
* Pydantic
* TensorFlow / Keras
* Joblib
* NumPy
* Uvicorn
* Google Colab

## Result

The FastAPI prediction service was successfully implemented and tested.

The serialized model and preprocessing scaler are correctly loaded, patient inputs are validated, preprocessing is applied, and predictions are returned through the `/predict` endpoint.
