# Day 5 — Tuning, Evaluation & Sprint Review


## Overview


Systematically developed, tuned, and evaluated a neural network for cardiovascular disease classification using the TensorFlow/Keras Sequential API.

The main focus was improving data quality, applying feature engineering and one-hot encoding, tuning the neural network one variable at a time, and evaluating the final model on unseen test data.

## Objectives


* Build and evaluate a baseline neural network.
* Identify and handle inconsistent blood pressure records.
* Apply feature engineering to create additional informative features.
* Apply one-hot encoding to categorical features.
* Tune learning rate, architecture, dropout, and batch size.
* Use Validation F1-score as the primary tuning metric.
* Apply EarlyStopping and ModelCheckpoint.
* Compare baseline and tuned model performance.
* Prepare evidence for Sprint Review and Retrospective.

## Dataset


The experiment uses the cleaned cardiovascular disease dataset.

* **Samples:** 68,741
* **Original Features:** 11
* **Target:** `cardio`
* **Task:** Binary Classification

The `id` column was removed because it is only an identifier.

## Data Preparation


The dataset was split using stratified sampling into:

* 64% Training
* 16% Validation
* 20% Test

StandardScaler was applied to numerical features, while categorical features were one-hot encoded.

The preprocessing was fitted only on the training data to prevent data leakage.

### Data Quality Check

During the analysis, **103 records (0.15%)** were identified where systolic blood pressure (`ap_hi`) was lower than or equal to diastolic blood pressure (`ap_lo`).

These inconsistent records were removed before applying feature engineering.

## Feature Engineering


Additional features were created from the existing clinical measurements:

* **BMI**
* **Pulse Pressure**
* **Mean Arterial Pressure**

Categorical variables were also transformed using **One-Hot Encoding**.

The baseline and feature-engineered models were compared to measure the impact of these changes.

## Hyperparameter Tuning


A one-variable-at-a-time strategy was used to evaluate:

* Learning Rate
* Network Architecture
* Dropout Rate
* Batch Size

Validation F1-score was used as the primary metric for selecting the best configuration.

### Best Configuration


| **Hyperparameter** |   **Best Value** |
| ------------------ | ---------------: |
| Learning Rate      |       **0.0005** |
| Architecture       | **(64, 32, 16)** |
| Dropout            |          **0.2** |
| Batch Size         |           **32** |

The best validation F1-score during the final tuning experiments was approximately **0.7289**.

## Callbacks


**EarlyStopping** was used to stop training when validation loss stopped improving and restore the best model weights.

**ModelCheckpoint** was used to save the best-performing final model.

## Results


The final tuned neural network achieved the following performance on the unseen test set:

| **Metric** |  **Score** |
| ---------- | ---------: |
| Accuracy   | **72.71%** |
| Precision  | **75.20%** |
| Recall     | **66.92%** |
| F1-Score   | **70.82%** |

The original baseline model achieved:

| **Metric** | **Baseline Test** |
| ---------- | ----------------: |
| Accuracy   |        **73.50%** |
| Precision  |        **75.32%** |
| Recall     |        **69.08%** |
| F1-Score   |        **72.07%** |

## Key Findings


* The baseline neural network achieved **72.07% F1-score** on the test set.
* Feature engineering and one-hot encoding produced only a small change in validation performance.
* The best tuned configuration achieved a validation F1-score of approximately **0.7289**.
* The final tuned model achieved **70.82% F1-score** on the unseen test set.
* The baseline model performed better than the final tuned model on the test set.
* EarlyStopping and ModelCheckpoint were used to improve training efficiency and preserve the best model.
* The results show that improvements on validation data do not always generalize to unseen test data.

## Sprint Review & Retrospective


The Sprint 1 work was documented using:

* Training and validation curves
* Hyperparameter comparison tables
* Baseline vs tuned model comparison
* Confusion matrices
* Final evaluation metrics

The main lesson from the experiments was the importance of evaluating the final model on unseen data rather than relying only on validation performance.

## Tools & Technologies


* Python
* TensorFlow / Keras
* Scikit-learn
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Git & GitHub
* Google Colab / Jupyter Notebo
