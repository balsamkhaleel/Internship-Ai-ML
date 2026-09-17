# ❤️ Cardiac Patient Monitoring System

## 📌 Project Overview

The **Cardiac Patient Monitoring System** is an end-to-end machine learning project for analyzing cardiovascular health data and estimating cardiovascular disease risk based on demographic, clinical, and lifestyle information.

The project covers the complete machine learning lifecycle:

**Data Preparation → EDA → Modeling → Optimization → Evaluation → Explainability → Serialization → Experiment Tracking → Application Development → Deployment**

Multiple traditional machine learning and deep learning approaches were explored throughout the project. The final production workflow uses a **Neural Network** integrated into an interactive **Streamlit** application and publicly deployed using **Render**.

> **Disclaimer:** This project is intended for educational and analytical purposes only. It is not a clinical diagnostic system and should not replace professional medical evaluation.

---

## 🌐 Live Application

The final Streamlit application is publicly available at:

**https://cardiac-patient-monitoring.onrender.com/**

The application allows users to enter patient health information and receive:

* Cardiovascular risk prediction
* Estimated prediction probability
* Calculated health indicators
* Structured prediction results

---

## 🎯 Project Objectives

The main objectives of the project are to:

* Clean and prepare cardiovascular patient data.
* Perform Exploratory Data Analysis (EDA).
* Analyze relationships between patient characteristics and cardiovascular disease.
* Engineer additional health-related features.
* Build and compare multiple machine learning models.
* Develop and tune a Neural Network.
* Optimize the classification threshold.
* Evaluate the model using Precision, Recall, F1-score, and Accuracy.
* Perform error analysis.
* Explain model behavior using SHAP.
* Serialize the final model and preprocessing artifacts.
* Track the final experiment using MLflow.
* Build an interactive Streamlit dashboard.
* Deploy the application publicly.
* Verify reproducibility and deployment consistency.

---

# 📊 Dataset

The project uses the **Cardiovascular Disease Dataset**, originally containing approximately **70,000 patient records**.

## Original Features

| Feature       | Description                |
| ------------- | -------------------------- |
| `id`          | Patient identifier         |
| `age`         | Age in days                |
| `gender`      | Gender encoded as 1 or 2   |
| `height`      | Height in centimeters      |
| `weight`      | Weight in kilograms        |
| `ap_hi`       | Systolic blood pressure    |
| `ap_lo`       | Diastolic blood pressure   |
| `cholesterol` | Cholesterol level          |
| `gluc`        | Glucose level              |
| `smoke`       | Smoking status             |
| `alco`        | Alcohol consumption status |
| `active`      | Physical activity status   |
| `cardio`      | Target variable            |

### Target Variable

* `0` → No cardiovascular disease
* `1` → Cardiovascular disease

---

# 🧹 Data Cleaning & Preparation

Several data-quality checks and preprocessing operations were performed before modeling.

## Blood Pressure

Extreme and implausible blood pressure observations were identified and removed during data preparation.

## Age

The original age feature was stored in days and converted into years:

```python
age_years = age / 365.25
```

## Height & Weight

Clearly implausible height and weight observations were removed during the cleaning stage.

## Final Cleaned Dataset

After cleaning, the main project dataset contained approximately:

* **68,741 observations**
* No missing values
* No duplicate rows
* No duplicate patient IDs

The cleaned dataset was then used throughout the modeling workflow.

---

# 🔎 Exploratory Data Analysis

EDA was performed to understand the dataset and investigate relationships between cardiovascular disease and patient characteristics.

The analysis included:

* Target distribution
* Age distribution
* Gender distribution
* Height and weight
* Systolic and diastolic blood pressure
* Cholesterol
* Glucose
* Smoking
* Alcohol consumption
* Physical activity
* Correlation analysis

## Key Findings

Important differences between cardiovascular disease classes were observed in several features, particularly:

* Age
* Weight
* Systolic blood pressure
* Diastolic blood pressure
* Cholesterol
* Physical activity

Blood-pressure-related variables showed particularly important relationships with cardiovascular risk.

---

# 🧪 Traditional Machine Learning Experiments

Several supervised classification algorithms were evaluated during the earlier modeling stages:

1. Logistic Regression
2. Random Forest
3. Decision Tree
4. K-Nearest Neighbors (KNN)

A stratified train/test strategy was used to preserve the target distribution.

---

## 🔄 Cross-Validation

A **5-fold Stratified Cross-Validation** strategy was used during traditional machine learning evaluation and tuning.

```python
StratifiedKFold(
    n_splits=5,
    shuffle=True,
    random_state=42
)
```

This provided a more reliable estimate of model performance while preserving class balance across folds.

---

# ⚙️ Hyperparameter Tuning

Traditional machine learning models were optimized using techniques such as `GridSearchCV`.

Parameters investigated included:

### Logistic Regression

* `C`
* `class_weight`

### Random Forest

* `n_estimators`
* `max_depth`
* `min_samples_split`

### Decision Tree

* `max_depth`
* `min_samples_split`
* `min_samples_leaf`

These experiments established useful traditional machine learning benchmarks before the later deep-learning workflow.

---

# 🎯 Earlier Random Forest Experiment

Threshold optimization was explored during the traditional machine learning stage because identifying positive cardiovascular-risk cases was an important consideration.

An earlier Random Forest experiment used a classification threshold of `0.35`.

| Metric    |  Score |
| --------- | -----: |
| Accuracy  | 70.66% |
| Precision | 66.29% |
| Recall    | 82.87% |
| F1-score  | 73.65% |

These results represent an **earlier traditional machine learning benchmark** and should not be confused with the final deployed Neural Network configuration.

---

# 🔵 Unsupervised Learning

Unsupervised learning was also used to investigate the natural structure of the patient population without using the target during clustering.

Two approaches were explored:

## K-Means

K-Means clustering was applied after feature standardization.

The number of clusters was investigated using:

* Elbow Method
* Silhouette Score

One explored configuration used:

```text
n_clusters = 7
```

Cluster profiles were then analyzed to investigate differences between patient groups.

## DBSCAN

DBSCAN was explored as a density-based clustering method.

One investigated configuration used:

```text
eps = 2.5
min_samples = 10
```

This analysis provided complementary insights into patient groups and potential noise observations.

---

# 🧠 Deep Learning Development

The project later introduced a deep learning approach using the **TensorFlow/Keras Sequential API**.

The Neural Network workflow included:

* Feature preprocessing
* Standardization using `StandardScaler`
* Neural Network development
* Hyperparameter tuning
* Early Stopping
* Threshold optimization
* Evaluation using classification metrics

Different values were explored for:

* Learning rate
* Network architecture
* Dropout
* Batch size

**F1-score** was used as an important metric during model development because it balances Precision and Recall.

Earlier Neural Network experiments used configurations such as `(32, 16)` before the final Sprint 4 production configuration was established.

---

# 🏆 Final Deployed Model

The final production workflow uses a **Neural Network**.

The final configuration tracked during Sprint 4 is:

| Hyperparameter           |    Final Value |
| ------------------------ | -------------: |
| Model                    | Neural Network |
| Architecture             |      `64-32-1` |
| Learning Rate            |       `0.0001` |
| Dropout                  |          `0.0` |
| Batch Size               |           `64` |
| Classification Threshold |         `0.42` |
| Random Seed              |           `42` |

This configuration represents the model used in the final serialization and deployment workflow.

---

# 📊 Final Model Evaluation

The final evaluation metrics tracked using MLflow are:

| Metric       |       Result |
| ------------ | -----------: |
| Precision    |     `0.6931` |
| Recall       |     `0.7744` |
| **F1-score** | **`0.7315`** |
| Accuracy     |     `0.7187` |

## Why F1-score?

The project does not rely on Accuracy alone.

The **F1-score** was treated as an important evaluation metric because it balances:

* Precision — how many predicted positive cases are actually positive.
* Recall — how many actual positive cases are identified.

Recall was also monitored because false-negative predictions are particularly relevant in a cardiovascular risk-screening context.

---

# 🔍 Error Analysis

Detailed error analysis was performed to understand the model beyond aggregate performance metrics.

The analysis included:

* True Negatives
* False Positives
* False Negatives
* True Positives
* False Negative Rate
* False Positive Rate

This helped identify where the model made mistakes and provided additional context for interpreting Precision, Recall, and F1-score.

---

# 🧠 Model Explainability with SHAP

SHAP was used to investigate how individual features influenced Neural Network predictions.

A **SHAP KernelExplainer** was used during the explainability analysis.

Important features investigated included:

* `ap_hi`
* `age_years`
* `pulse_pressure`
* `map`

The SHAP analysis provided additional insight into how patient characteristics contributed to the model output.

Explainability is particularly valuable in health-related machine learning because prediction behavior should be investigated rather than treating the model as a black box.

---

# 📦 Model Serialization

The final model and preprocessing objects were serialized for deployment.

Main production artifacts include:

```text
final_neural_network.keras
standard_scaler.joblib
best_threshold.txt
```

These artifacts preserve:

* The trained Neural Network
* The fitted preprocessing scaler
* The selected classification threshold

The serialized artifacts were loaded again and inference was verified before application deployment.

---

# 🔁 Reproducibility

Reproducibility practices were applied during Sprint 4.

## Fixed Random Seed

The project uses a fixed seed:

```text
42
```

Seeds were configured for:

* Python
* NumPy
* TensorFlow

## Dependency Management

Relevant `requirements.txt` files contain pinned versions of the required libraries.

Key technologies include:

* TensorFlow
* Scikit-learn
* Pandas
* NumPy
* Joblib
* MLflow
* Streamlit

## Reproducibility Verification

The Sprint 4 serialization notebook was executed from start to finish using the project environment to verify that the workflow could be reproduced successfully.

---

# 📈 Experiment Tracking with MLflow

MLflow was used during Sprint 4 to track the final production experiment.

Experiment:

```text
Cardiac_Patient_Monitoring_Sprint_4
```

The tracked parameters include:

```text
model_type    = Neural Network
architecture  = 64-32-1
learning_rate = 0.0001
dropout       = 0.0
batch_size    = 64
threshold     = 0.42
seed          = 42
```

Tracked evaluation metrics include:

```text
test_accuracy  = 0.7187
test_precision = 0.6931
test_recall    = 0.7744
test_f1        = 0.7315
```

Experiment tracking helps preserve the configuration associated with the final production model.

---

# 🖥️ Streamlit Application

An interactive Streamlit dashboard was developed to provide a user-friendly interface for the final model.

The application accepts patient information including:

* Age
* Height
* Weight
* Systolic blood pressure
* Diastolic blood pressure
* Gender
* Cholesterol level
* Glucose level
* Smoking status
* Alcohol intake
* Physical activity

The application then performs the required preprocessing and feature calculations before generating the prediction.

The result includes:

* Risk classification
* Estimated probability
* Calculated health indicators

---

# 🌐 Public Deployment

The Streamlit application was deployed using **Render**.

### Deployment Configuration

* Platform: Render
* Framework: Streamlit
* Python: 3.12.10
* TensorFlow: 2.20.0
* Streamlit: 1.64.0
* Deployment source: GitHub

### Live Application

**https://cardiac-patient-monitoring.onrender.com/**

---

# ✅ Deployment Verification

The application was tested both locally and after deployment.

The same patient information was submitted to both versions.

One verification example produced:

| Output                | Local                   | Deployed                |
| --------------------- | ----------------------- | ----------------------- |
| Prediction            | No Cardio Risk Detected | No Cardio Risk Detected |
| Estimated Probability | 12.31%                  | 12.31%                  |
| BMI                   | 24.22                   | 24.22                   |
| Pulse Pressure        | 40.0                    | 40.0                    |
| MAP                   | 93.3                    | 93.3                    |

The matching results confirmed that the deployed application reproduced the local inference workflow.

---

# 🛠️ Technologies & Tools

## Programming

* Python

## Data Analysis

* Pandas
* NumPy

## Visualization

* Matplotlib

## Machine Learning

* Scikit-learn

## Deep Learning

* TensorFlow
* Keras

## Explainability

* SHAP

## MLOps

* MLflow
* Joblib
* Model serialization
* Pinned dependencies
* Fixed random seeds

## Application

* Streamlit

## Deployment

* Render
* GitHub

---

# 📁 Project Organization

The repository preserves the complete learning and development history across the internship.

The main cardiac project area contains the core modeling notebooks and artifacts:

```text
project/
│
├── cardio.csv
├── cardio_cleaned.csv
│
├── Data_Preparation_01.ipynb
├── EDA_02.ipynb
├── Baseline_Model_03.ipynb
├── Supervised_Learning_04.ipynb
├── Unsupervised_learning_05.ipynb
├── Deep_learning_06.ipynb
├── NN_Tunning_07.ipynb
│
├── final_neural_network.keras
├── standard_scaler.joblib
├── best_threshold.txt
│
└── README.md
```

Sprint 4 deployment work is documented under Week 9:

```text
week9/
│
├── day1/
│   ├── day1.ipynb
│   ├── README.md
│   ├── cardio_cleaned.csv
│   ├── final_neural_network.keras
│   ├── standard_scaler.joblib
│   ├── best_threshold.txt
│   ├── mlflow.db
│   └── requirements.txt
│
├── day2/
│   ├── day2.ipynb
│   ├── README.md
│   ├── final_neural_network.keras
│   └── standard_scaler.joblib
│
├── day3/
│   ├── day3.ipynb
│   ├── app.py
│   ├── README.md
│   ├── final_neural_network.keras
│   └── standard_scaler.joblib
│
├── day4/
│   ├── app.py
│   ├── README.md
│   ├── requirements.txt
│   ├── final_neural_network.keras
│   └── standard_scaler.joblib
│
└── day5/
    └── day5.ipynb
```

---

# 🚀 Complete Project Workflow

```text
Raw Cardiovascular Dataset
          ↓
Data Cleaning & Preparation
          ↓
Exploratory Data Analysis
          ↓
Feature Engineering
          ↓
Baseline Models
          ↓
Supervised Learning
          ↓
Traditional ML Tuning
          ↓
Unsupervised Learning
          ↓
Neural Network Development
          ↓
Neural Network Tuning
          ↓
Threshold Optimization
          ↓
Model Evaluation
          ↓
Error Analysis
          ↓
SHAP Explainability
          ↓
Final Model Selection
          ↓
Model & Scaler Serialization
          ↓
Reproducibility Verification
          ↓
MLflow Experiment Tracking
          ↓
Streamlit Application
          ↓
Render Deployment
          ↓
Deployment Verification
```

---

# ⚙️ Running the Deployed Application Locally

The deployment application is located in:

```text
week9/day4/
```

Move to the deployment directory:

```bash
cd week9/day4
```

Create and activate a virtual environment if needed.

Install the required dependencies:

```bash
pip install -r requirements.txt
```

Run the Streamlit application:

```bash
streamlit run app.py
```

Streamlit will provide a local URL that can be opened in the browser.

---

# ⚠️ Limitations

The current project has several important limitations:

* The model was developed using a public cardiovascular dataset.
* The dataset may not represent every population or clinical environment.
* Predictions depend on the quality and accuracy of the input information.
* The model produces a statistical risk prediction rather than a medical diagnosis.
* External clinical validation has not been performed.
* Model performance may change when applied to data from different populations or collection processes.

Therefore, the application should be treated as an **educational machine learning demonstration**, not a clinical decision-making system.

---

# 🔮 Future Improvements

Potential future improvements include:

* External validation using additional cardiovascular datasets.
* Additional model optimization.
* Probability calibration.
* Automated inference tests.
* Continuous Integration and Continuous Deployment (CI/CD).
* Production monitoring.
* Data-drift and model-drift monitoring.
* Additional SHAP explanations inside the Streamlit interface.
* Improved separation between experimentation and production inference code.
* More extensive application validation.

---

# 📝 Conclusion

The Cardiac Patient Monitoring System demonstrates the development of a machine learning project across the complete lifecycle.

The work began with cardiovascular data cleaning and exploratory analysis, progressed through traditional machine learning, clustering, Neural Network development, hyperparameter tuning, threshold optimization, model evaluation, error analysis, and SHAP explainability.

The final Sprint 4 workflow extended the project beyond experimentation by introducing:

* Model serialization
* Preprocessing artifact management
* Reproducibility practices
* MLflow experiment tracking
* Streamlit application development
* Public deployment
* Deployment verification
* Repository polish and documentation

The final deployed Neural Network uses an architecture of `64-32-1` with a classification threshold of `0.42` and achieved an **F1-score of 0.7315**, with **Recall of 0.7744** and **Precision of 0.6931** in the tracked final evaluation.

Overall, the project demonstrates not only how to train a machine learning model, but how to evaluate, explain, package, reproduce, integrate, and deploy it as a complete machine learning application.

---

## ❤️ Live Demo

**Cardiac Patient Monitoring System**

https://cardiac-patient-monitoring.onrender.com/

> Educational project only — not intended for medical diagnosis.
