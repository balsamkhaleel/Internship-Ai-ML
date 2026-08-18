# ❤️ Cardiac Patient Monitoring System

## 📌 Project Overview

The **Cardiac Patient Monitoring System** is a machine learning project that analyzes cardiovascular health data to identify patterns associated with cardiovascular disease.

The project follows a complete supervised machine learning workflow, including **data cleaning, exploratory data analysis, statistical analysis, model comparison, cross-validation, hyperparameter tuning, threshold optimization, and model evaluation**.

The main objective is to build and evaluate machine learning models that can classify whether a patient is likely to have cardiovascular disease based on demographic, clinical, and lifestyle features.

> **Note:** This project is developed for educational and analytical purposes and is not intended to replace professional medical diagnosis.

---

## 🎯 Objectives

* Clean and prepare cardiovascular patient data.
* Perform exploratory data analysis (EDA).
* Analyze relationships between patient characteristics and cardiovascular disease.
* Build and compare multiple supervised learning models.
* Apply stratified cross-validation.
* Perform hyperparameter tuning using GridSearchCV.
* Optimize the classification threshold to improve disease detection.
* Evaluate the final model using multiple classification metrics.
* Analyze feature importance.
* Select a suitable model for cardiovascular disease classification.

---

## 📊 Dataset

The project uses a cardiovascular disease dataset containing **70,000 patient records**.

### Features

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

## 🧹 Data Cleaning

Several data-quality checks and cleaning operations were performed before model training.

### Blood Pressure

Extreme and implausible blood pressure values were identified and removed.

The following ranges were used:

* Systolic blood pressure: **40–300 mmHg**
* Diastolic blood pressure: **40–300 mmHg**

### Age

The original `age` feature was stored in days.

It was converted into years using:

```python
age_years = age / 365.25
```

The original `age` column was then removed because `age_years` provides the same information in a more interpretable format.

### Height

Values outside the range of **100–200 cm** were removed as clearly implausible observations.

### Weight

Values outside the range of **30–200 kg** were removed.

### Final Dataset

After cleaning:

* **68,741 observations**
* **13 columns**
* No missing values
* No duplicate rows
* No duplicate patient IDs
* Invalid blood pressure values removed
* Implausible height and weight values removed

The cleaned dataset was then used for exploratory analysis and machine learning.

---

## 🔎 Exploratory Data Analysis

The EDA stage was performed to understand the distribution of patient characteristics and investigate their relationships with cardiovascular disease.

The analysis included:

* Cardiovascular disease distribution
* Age distribution
* Gender distribution
* Height
* Weight
* Systolic blood pressure
* Diastolic blood pressure
* Cholesterol
* Glucose
* Smoking
* Alcohol consumption
* Physical activity
* Correlation analysis

### Key Findings

Several features showed noticeable differences between patients with and without cardiovascular disease.

### Age

Patients with cardiovascular disease had a higher average age than patients without cardiovascular disease.

* No disease: approximately **51.69 years**
* Disease: approximately **54.93 years**

### Weight

* No disease: approximately **71.58 kg**
* Disease: approximately **76.72 kg**

Patients with cardiovascular disease had a higher average weight.

### Systolic Blood Pressure

* No disease: approximately **119.56 mmHg**
* Disease: approximately **133.82 mmHg**

Systolic blood pressure showed one of the largest differences between the two target classes.

### Diastolic Blood Pressure

* No disease: approximately **78.17 mmHg**
* Disease: approximately **84.66 mmHg**

Patients with cardiovascular disease also showed a higher average diastolic blood pressure.

### Cholesterol

The proportion of patients with cardiovascular disease increased as cholesterol level increased.

### Glucose

Higher glucose categories showed a higher proportion of cardiovascular disease compared with the normal glucose category.

### Physical Activity

Inactive patients showed a higher proportion of cardiovascular disease compared with active patients.

### Smoking and Alcohol

The differences in cardiovascular disease proportions between smokers and non-smokers, as well as between alcohol consumers and non-consumers, were relatively small in this dataset.

---

## 📈 Correlation Analysis

Correlation analysis was performed on the main numerical features to examine their linear relationships with the target variable.

The strongest positive correlations with `cardio` were:

| Feature     | Correlation with `cardio` |
| ----------- | ------------------------: |
| `ap_hi`     |                     0.425 |
| `ap_lo`     |                     0.335 |
| `age_years` |                     0.240 |
| `weight`    |                     0.180 |
| `height`    |                    -0.012 |

The strongest relationship between the numerical features was observed between systolic and diastolic blood pressure, with a correlation of approximately **0.698**.

Overall, blood pressure showed the strongest linear relationship with cardiovascular disease among the analyzed numerical features.

---

## 🤖 Supervised Learning

The project evaluated four classification algorithms:

1. **Logistic Regression**
2. **Random Forest**
3. **Decision Tree**
4. **K-Nearest Neighbors (KNN)**

These models were selected to compare different machine learning approaches, including:

* A linear model
* A tree-based model
* An ensemble model
* A distance-based model

### Train/Test Split

The dataset was divided using a stratified train/test split:

* **80% Training**
* **20% Testing**

Stratification was used to preserve the distribution of the target classes in both sets.

The `id` column was removed before model training because it is an identifier and does not provide meaningful predictive information.

---

## 🔄 Cross-Validation

A **5-fold Stratified Cross-Validation** strategy was used during model evaluation and hyperparameter tuning.

```python
StratifiedKFold(
    n_splits=5,
    shuffle=True,
    random_state=42
)
```

Stratification ensures that each fold maintains a similar proportion of patients with and without cardiovascular disease.

Cross-validation provides a more reliable estimate of model performance and reduces dependence on a single validation split.

---

## ⚙️ Hyperparameter Tuning

`GridSearchCV` was used to search for better hyperparameter configurations for the supervised models.

### Logistic Regression

The following parameters were evaluated:

* `C`
* `class_weight`

### Random Forest

The following parameters were optimized:

* `n_estimators`
* `max_depth`
* `min_samples_split`

### Decision Tree

The following parameters were evaluated:

* `max_depth`
* `min_samples_split`
* `min_samples_leaf`

The optimization process used **F1-score** as the scoring metric during cross-validation.

---

## 🎯 Threshold Optimization

For cardiovascular disease detection, **Recall** is particularly important because missing a positive case can be more concerning than incorrectly classifying a negative case as positive.

By default, binary classification commonly uses a probability threshold of **0.50**.

Instead of relying only on this default threshold, several thresholds were evaluated:

```text
0.30
0.35
0.40
0.45
0.50
0.55
0.60
```

A threshold of **0.35** was selected based on the Precision-Recall trade-off.

Lowering the threshold makes the model more likely to classify a patient as positive, which increases the number of detected positive cases and improves Recall, while also increasing the number of false positives.

---

## 🌲 Final Random Forest Model

After hyperparameter tuning and threshold optimization, **Random Forest** was selected as the final model.

The final model used the best hyperparameters identified through `GridSearchCV`.

The final classification threshold was set to:

```text
0.35
```

### Final Results

| Metric    |      Score |
| --------- | ---------: |
| Accuracy  | **70.66%** |
| Precision | **66.29%** |
| Recall    | **82.87%** |
| F1-Score  | **73.65%** |

The final model achieved a Recall of **82.87%**, meaning that it correctly identified a large proportion of the patients belonging to the cardiovascular disease class.

The threshold adjustment prioritized Recall while maintaining a reasonable balance with Precision.

---

## 📊 Model Evaluation

The final model was evaluated using several metrics:

* **Accuracy**
* **Precision**
* **Recall**
* **F1-Score**
* **Confusion Matrix**
* **Classification Report**

### Confusion Matrix

The confusion matrix was used to examine:

* **True Negatives (TN):** Correctly predicted patients without cardiovascular disease.
* **False Positives (FP):** Patients without cardiovascular disease incorrectly classified as positive.
* **False Negatives (FN):** Patients with cardiovascular disease incorrectly classified as negative.
* **True Positives (TP):** Correctly identified cardiovascular disease cases.

This evaluation provides a more detailed view of the model's classification behavior than accuracy alone.

---

## 🔍 Feature Importance

Feature importance was extracted from the final Random Forest model.

This analysis helps identify which features contributed most to the model's predictions.

Feature importance provides an additional level of model interpretation and helps understand which patient characteristics were most useful for classification.

---

## 🛠️ Technologies & Libraries

### Programming Language

* Python

### Data Analysis

* Pandas
* NumPy

### Visualization

* Matplotlib

### Machine Learning

* Scikit-learn

### Main Techniques

* Data Cleaning
* Exploratory Data Analysis
* Statistical Analysis
* Correlation Analysis
* Train/Test Split
* Stratified Cross-Validation
* Logistic Regression
* Decision Tree
* KNN
* Random Forest
* GridSearchCV
* Hyperparameter Tuning
* Classification Threshold Optimization
* Confusion Matrix
* Feature Importance
* Model Evaluation

---

## 📁 Project Structure

```text
Cardiac-Patient-Monitoring-System/
│
├── cardio.csv
├── Cardiac_Patient_Monitoring_System.ipynb
└── README.md
```

---

## 📝 Conclusion

The project demonstrates a complete supervised machine learning workflow for cardiovascular disease classification, starting from data quality analysis and preprocessing and progressing through exploratory data analysis, model comparison, cross-validation, hyperparameter tuning, and final model evaluation.

Four classification algorithms were evaluated: **Logistic Regression, Decision Tree, KNN, and Random Forest**.

Based on the experiments, **Random Forest** was selected as the final model. Because cardiovascular disease detection places particular importance on identifying positive cases, the classification threshold was adjusted from **0.50 to 0.35** to improve Recall.

The final model achieved:

* **70.66% Accuracy**
* **66.29% Precision**
* **82.87% Recall**
* **73.65% F1-Score**

The results demonstrate the potential of machine learning to identify patterns associated with cardiovascular disease in the analyzed dataset.

However, the model should be considered an **educational machine learning model rather than a clinical diagnostic system**, and further validation on independent and clinically representative datasets would be required before any real-world medical application.
