\# Day 2 — FastAPI Prediction API



\## Completed Tasks



\* Built a FastAPI application for the cardiovascular disease prediction model.

\* Loaded the serialized neural network model (`final\_neural\_network.keras`).

\* Loaded the saved preprocessing scaler (`standard\_scaler.joblib`).

\* Defined a Pydantic input schema containing the 14 model features.

\* Created a `POST /predict` endpoint.

\* Applied the saved scaler before model inference.

\* Used the optimized classification threshold of `0.42`.

\* Tested the API through FastAPI Swagger documentation (`/docs`).

\* Tested multiple valid patient inputs successfully.

\* Tested invalid input and confirmed that Pydantic rejects it with HTTP `422`.



\## Prediction Flow



Request → Pydantic Validation → Saved Scaler → Neural Network → Probability → Threshold → Prediction



\## Test Results



| Test Case     | HTTP Status | Probability | Threshold | Prediction |

| ------------- | ----------- | ----------- | --------- | ---------- |

| Test 1        | 200         | 0.8202      | 0.42      | 1          |

| Test 2        | 200         | 0.4115      | 0.42      | 0          |

| Test 3        | 200         | 0.0470      | 0.42      | 0          |

| Invalid Input | 422         | —           | —         | Rejected   |



\## Conclusion



The FastAPI prediction service was successfully implemented and tested.



The API correctly validates patient inputs, applies the saved preprocessing pipeline, generates predictions using the serialized neural network, and returns the prediction probability and classification threshold as a JSON response.



