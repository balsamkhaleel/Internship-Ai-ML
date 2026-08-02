# Day 1 — Supervised Learning Concepts \& the Scikit-learn API



## Summary

Explored the fundamentals of supervised learning and learned how the Scikit-learn API is used consistently across models. Practiced separating a dataset into features and target, and performed a train/test split on a real weather dataset to set up an honest ML workflow.



## Key Concepts

- Supervised learning: training a model on labeled examples to predict on new data

- Regression vs. classification, distinguished by what the target looks like

- Features (X) and target (y)

- The consistent Scikit-learn API: instantiate, fit, predict, score

- The train/test split and why it matters

- Never evaluating a model on the data it was trained on



## Tasks

- Loaded the weather dataset and reviewed its shape, data types, and missing values.

- Visualized the relationship between `Dew Point Temp\_C` and `Temp\_C` with a scatter plot and confirmed a strong positive correlation (about 0.93).

- Separated the dataset into features `X` (all columns except `Temp\_C`) and target `y` (`Temp\_C`).

- Performed an 80/20 train/test split with a fixed `random\_state` for reproducibility.

- Confirmed the shapes of `X\_train`, `X\_test`, `y\_train`, and `y\_test` were consistent with the 80/20 split.

- Explained in Markdown why the model must never see the test set during training.



## Key Takeaway

Supervised learning is fundamentally about learning the relationship between features (X) and a target (y) from labeled examples, and Scikit-learn's consistent instantiate–fit–predict–score API makes every model in the library usable through the same four steps. The train/test split is the single most important rule in ML: a model can memorize its training data and look perfect, yet fail on new data, so evaluating only on a held-out test set the model has never seen is the only honest way to estimate real-world performance.



## Files

day1.ipynb — supervised learning setup on a weather dataset, including feature/target separation, correlation check, and an 80/20 train/test split.



