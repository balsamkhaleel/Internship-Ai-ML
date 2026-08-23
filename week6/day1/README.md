# Day 1 — Sprint 1 Planning \& Baseline Model



## Overview



Completed Sprint 1 planning and established a baseline model for the Cardiovascular Disease project. Prepared and explored the dataset, then trained a Logistic Regression model using stratified 5-fold cross-validation and a held-out test set.



## Topics Covered



- Sprint 1 planning

- Baseline-first approach

- Data preparation and cleaning

- Exploratory Data Analysis (EDA)

- Feature distributions and relationships

- Correlation analysis

- 5-Fold Cross-Validation

- Model evaluation



## Dataset



- 68,742 samples

- 13 features

- No missing values

- No duplicate rows

- Binary target: `cardio`

- cardio = 0: No cardiovascular disease

- cardio = 1: Cardiovascular disease



## Data Preparation



- Converted age from days to years.

- Removed invalid height values.

- Removed invalid weight values.

- Removed invalid blood pressure values.

- Saved the cleaned dataset for the following notebooks.



## Exploratory Data Analysis



- Analyzed numerical feature distributions.

- Explored categorical feature distributions.

- Examined important features in relation to cardiovascular disease.

- Analyzed correlations between features using a correlation heatmap.

- Identified age, weight, and blood pressure as important features related to the target.



## Baseline Model



Logistic Regression was selected as the baseline classification model.



- Features were standardized using `StandardScaler`.

- Stratified 5-fold cross-validation was used on the training set.

- The held-out test set was used for final evaluation.



## Results



### 5-Fold Cross-Validation



- F1-score: **0.7077 ± 0.0061**



### Test Set



- Accuracy: **0.7270**

- Precision: **0.7524**

- Recall: **0.6685**

- F1-score: **0.7080**



## Key Takeaways



- Data preparation is an important step before modeling.

- EDA helped identify patterns and relationships within the cardiovascular disease dataset.

- Logistic Regression provides a baseline for comparing future models.

- 5-fold cross-validation provides a more reliable estimate of model performance.

- Future neural network models should aim to outperform the baseline F1-score of \*\*0.7077\*\*.



## Tools



- Python

- Pandas

- NumPy

- Scikit-learn

- Matplotlib

- Seaborn

- Jupyter Notebook

