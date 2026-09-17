\## Deployment



The Streamlit application was successfully deployed on Render using the free Web Service plan.



\*\*Live Application:\*\*

https://cardiac-patient-monitoring.onrender.com/



\### Deployment Configuration



\* \*\*Platform:\*\* Render

\* \*\*Framework:\*\* Streamlit

\* \*\*Python Version:\*\* 3.12.10

\* \*\*TensorFlow:\*\* 2.20.0

\* \*\*Streamlit:\*\* 1.64.0

\* \*\*Deployment:\*\* Automatic deployment from GitHub



\### Live Testing



The deployed application was tested using the same patient inputs used in the local application.



| Metric                |                   Local |                Deployed |

| --------------------- | ----------------------: | ----------------------: |

| Prediction            | No Cardio Risk Detected | No Cardio Risk Detected |

| Estimated Probability |                  12.31% |                  12.31% |

| BMI                   |                   24.22 |                   24.22 |

| Pulse Pressure        |                    40.0 |                    40.0 |

| MAP                   |                    93.3 |                    93.3 |



The deployed application produced the same prediction and calculated health indicators as the local application, confirming that the model, scaler, and preprocessing pipeline were successfully deployed.



