\# Day 5 — Scikit-learn Pipelines \& Tuned Mini-Project



\## Summary



Learned how pipelines prevent data leakage by chaining preprocessing and

modeling into a single, leak-free workflow. Built a `Pipeline` with a

`ColumnTransformer` for mixed numeric and categorical data on the Titanic

dataset, incorporated an engineered `Title` feature, and tuned the complete

pipeline end-to-end using `GridSearchCV`.



\## Key Concepts



\- Why pipelines prevent data leakage

\- Building a `Pipeline` with preprocessing and modeling in one object

\- Using `ColumnTransformer` for mixed numeric and categorical data

\- Handling missing values within the pipeline

\- Tuning a complete pipeline with `GridSearchCV`

\- Using the `step\_\_param` syntax to tune model parameters

\- Evaluating a final model on a held-out test set



\## Tasks



\- Engineered a `Title` feature from each passenger's name and grouped rare

&#x20; titles into a single `Rare` category.

\- Built separate preprocessing pipelines for numeric and categorical

&#x20; features, including median imputation and scaling for numeric features and

&#x20; most-frequent imputation and one-hot encoding for categorical features.

\- Combined the preprocessing steps using a `ColumnTransformer` and integrated

&#x20; them with a `RandomForestClassifier` inside a single `Pipeline`.

\- Established an untuned baseline on the held-out test set:

&#x20; \*\*F1 = 0.742\*\*.

\- Tuned the complete pipeline with `GridSearchCV` using 5-fold cross-validation

&#x20; and F1-score as the evaluation metric.

\- Found the best hyperparameters:

&#x20; \*\*`max\_depth=10` and `n\_estimators=100`\*\*.

\- Achieved a best cross-validation F1-score of \*\*0.750\*\*.

\- Evaluated the final tuned pipeline once on the held-out test set:

&#x20; \*\*Accuracy = 0.827, Precision = 0.817, Recall = 0.710, F1 = 0.760\*\*.

\- Compared the final tuned model against the untuned baseline and documented

&#x20; the results.



\## Results



| Metric | Baseline | Final Tuned |

|---|---:|---:|

| Accuracy | 0.810 | \*\*0.827\*\* |

| Precision | 0.778 | \*\*0.817\*\* |

| Recall | 0.710 | 0.710 |

| F1 | 0.742 | \*\*0.760\*\* |



The final pipeline improved the F1-score from \*\*0.742 to 0.760\*\*, an

improvement of approximately \*\*1.73 percentage points\*\*. Accuracy increased

from \*\*0.810 to 0.827\*\*, while precision increased from \*\*0.778 to 0.817\*\*.



\## Key Takeaway



A `Pipeline` combined with a `ColumnTransformer` provides a structured,

leak-free machine learning workflow. Preprocessing steps are fitted only on

the appropriate training data, including independently within each fold

during cross-validation.



Using `GridSearchCV` to tune the complete pipeline makes the model selection

process more reliable because preprocessing and model training are performed

together inside each cross-validation fold.



The final tuned pipeline improved the F1-score from \*\*0.742 to 0.760\*\*

compared with the untuned baseline, while also improving accuracy and

precision. The workflow combines feature engineering, mixed-data

preprocessing, model training, and hyperparameter tuning into one

reproducible pipeline — the same structure that can be applied to larger

machine learning projects and future capstone work.



\## Files



\- `day5.ipynb` — Complete Day 5 notebook containing the engineered `Title`

&#x20; feature, leak-free `Pipeline`, `ColumnTransformer`, and

&#x20; `GridSearchCV`-tuned `RandomForestClassifier` on the Titanic dataset.

