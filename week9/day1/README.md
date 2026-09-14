# Sprint 4 — Serialization & MLOps

## Overview

In Sprint 4, the final neural network model for the Cardiac Patient Monitoring System was prepared for deployment.

The sprint focused on saving the trained model and preprocessing objects, loading them back, verifying predictions, and applying basic reproducibility practices.

## Work Completed

* Saved the final neural network model using Keras.
* Saved the fitted `StandardScaler` using Joblib.
* Saved the optimized classification threshold.
* Loaded all serialized artifacts successfully.
* Verified predictions using the loaded model and scaler.
* Created a pinned `requirements.txt`.
* Fixed random seeds to `42`.
* Logged the model configuration and evaluation results using MLflow.

## Final Model

* Architecture: `64 → 32 → 1`
* Learning Rate: `0.0001`
* Dropout: `0.0`
* Batch Size: `64`
* Threshold: `0.42`

## Test Verification

The serialized pipeline was tested on **10,296 test samples**.

The model successfully loaded the saved artifacts and generated predictions using the saved threshold.

## Saved Files

* `final_neural_network.keras`
* `standard_scaler.joblib`
* `best_threshold.txt`
* `requirements.txt`

## Conclusion

Sprint 4 successfully prepared the final model and its preprocessing components for the next deployment stage. The saved artifacts were loaded and verified successfully, with reproducibility supported through fixed seeds, pinned dependencies, and MLflow tracking.
