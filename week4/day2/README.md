# Day 2 — Cross-Validation



## Summary



Explored how k-fold cross-validation produces a more reliable performance estimate than a single train/test split. Practiced running 5-fold cross-validation with cross\_val\_score on a Logistic Regression pipeline, comparing it to a single train/test split, and confirming the role of stratified folds on the Breast Cancer Wisconsin dataset.



## Key Concepts



* Why cross-validation provides a more reliable estimate than a single validation split

* How k-fold works: rotating folds so every data point is used for validation exactly once

* cross\_val\_score: interpreting the mean and standard deviation across folds

* Stratified k-fold and why it matters for imbalanced classification

* Using a Pipeline to prevent preprocessing leakage during cross-validation



## Tasks



* Loaded the dataset, checked the class balance (357 benign vs 212 malignant), and prepared the features and target.

* Built a Pipeline combining StandardScaler and LogisticRegression, and computed a single-split baseline (Accuracy ≈ 96.5%, F1 ≈ 0.9512).

* Ran 5-fold cross-validation with cross\_val\_score, obtaining five F1 scores: 0.954, 0.986, 0.938, 0.971, and 0.957.

* Reported the mean and standard deviation of the fold scores (0.9608 ± 0.0162).

* Compared the cross-validated estimate with the single-split score and explained why evaluating across multiple splits provides a more reliable estimate.

* Explicitly built a StratifiedKFold and re-ran cross-validation (0.9640 ± 0.0207).

* Confirmed that cross\_val\_score uses stratified folds by default for classifiers when cv is specified as an integer, and explained that the difference in results came from enabling shuffling in the explicit StratifiedKFold.

* Assembled the single-split, 5-fold CV, and stratified 5-fold results into one comparison table.



## Key Takeaway



A single train/test split provides one performance estimate that can be influenced by the particular samples selected for the split. In contrast, k-fold cross-validation evaluates the model across multiple train/validation splits and averages the resulting scores, providing a more reliable estimate of general performance.



The mean represents the model's average performance across the folds, while the standard deviation indicates how consistent the performance is between folds. On this dataset, the cross-validation mean (0.9608) was reasonably close to the single-split F1 score (0.9512), while the relatively low standard deviation (0.0162) indicated consistent performance across the folds.



Stratified k-fold is particularly important for classification datasets with class imbalance. It preserves the class proportions in each fold, ensuring that each fold contains a representative distribution of benign and malignant cases and allowing the model to be evaluated more fairly.



## Files



day2.ipynb — 5-fold and stratified 5-fold cross-validation of a Logistic Regression pipeline on the Breast Cancer Wisconsin dataset, including a full comparison against a single train/test split baseline.



