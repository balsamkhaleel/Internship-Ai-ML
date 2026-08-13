# Day 5 — Scikit-learn Pipelines & Tuned Mini-Project

## Summary

Learned how pipelines prevent data leakage by chaining preprocessing and
modeling into a single, leak-free workflow. Built a Pipeline with a
ColumnTransformer for mixed numeric and categorical data on the Titanic
dataset, incorporated an engineered Title feature, and tuned the complete
workflow end-to-end using GridSearchCV.

## Key Concepts

- Why pipelines prevent data leakage
- Building a Pipeline with preprocessing and modeling in one object
- Using ColumnTransformer for mixed numeric and categorical data
- Handling missing values within the pipeline
- Scaling numeric features and encoding categorical features
- Tuning a complete pipeline with GridSearchCV
- Using the step__param syntax to tune model parameters
- Evaluating a final model on a held-out test set

## Tasks

- Loaded and inspected the Titanic dataset, including its structure,
  missing values, and descriptive statistics.
- Engineered a Title feature from each passenger's name and grouped rare
  titles into a single Rare category.
- Removed PassengerId, Cabin, Ticket, and the original Name column
  from the predictors.
- Built separate preprocessing pipelines for numeric and categorical
  features.
- Applied median imputation and standardization to numeric features.
- Applied most-frequent imputation and one-hot encoding to categorical
  features.
- Combined both preprocessing pipelines using a ColumnTransformer.
- Integrated the ColumnTransformer with a RandomForestClassifier inside
  a single leak-free Pipeline.
- Established an untuned baseline on the held-out test set.
- Tuned the complete pipeline using GridSearchCV with 5-fold
  cross-validation and F1-score as the scoring metric.
- Found the best hyperparameters:
  **max_depth=10 and n_estimators=100**.
- Evaluated the final tuned pipeline once on the held-out test set.
- Compared the final tuned model against the untuned baseline.

## Results

| Metric | Baseline | Final Tuned | Change |
|---|---:|---:|---:|
| Accuracy | 0.816 | **0.827** | +0.011 |
| Precision | 0.781 | **0.828** | +0.046 |
| Recall | **0.725** | 0.696 | -0.029 |
| F1 | 0.752 | **0.756** | +0.004 |

### Final Model Performance

- **Accuracy:** 0.827
- **Precision:** 0.828
- **Recall:** 0.696
- **F1-score:** 0.756

The final tuned pipeline improved the F1-score from **0.752 to 0.756**,
an improvement of approximately **0.40 percentage points**.

Accuracy increased from **0.816 to 0.827**, while precision increased from
**0.781 to 0.828**. Recall decreased from **0.725 to 0.696**, showing a
trade-off between precision and recall after tuning.

The improvement in F1-score was modest, indicating that the default
Random Forest configuration was already relatively strong for this dataset.

## Key Takeaway

A Pipeline combined with a `ColumnTransformer` provides a structured and
leak-free machine learning workflow. Preprocessing steps such as imputation,
scaling, and encoding are fitted only on the appropriate training data and
are automatically handled correctly inside each cross-validation fold.

Using `GridSearchCV` to tune the complete pipeline makes model selection more
reliable because preprocessing and model training are performed together
during cross-validation.

The final tuned pipeline achieved a slight improvement in F1-score from
**0.752 to 0.756** while increasing accuracy and precision. Although the
overall improvement was modest, the project demonstrates the correct
professional structure for an end-to-end machine learning workflow:

**Feature Engineering → Preprocessing → ColumnTransformer → Model →
GridSearchCV → Final Test Evaluation**

This leak-free pipeline structure can be reused for larger machine learning
projects and future capstone work.

## Files

- day5.ipynb — Complete Day 5 notebook containing the engineered Title
  feature, leak-free `Pipeline`, `ColumnTransformer`, missing-value
  imputation, and `GridSearchCV`-tuned `RandomForestClassifier` on the
  Titanic dataset.
