# Day 3 — Logistic Regression \& Classification Metrics

## Summary



Explored logistic regression and learned how to evaluate a classifier beyond simple accuracy. Practiced training a LogisticRegression model on the Breast Cancer Wisconsin dataset, reading a confusion matrix, and computing precision, recall, F1, and AUC-ROC.



## Key Concepts

- Logistic regression: weighted sum + sigmoid → probability

- Why accuracy alone is misleading on imbalanced data

- The confusion matrix: TP, FP, FN, TN

- Precision, recall, F1, and the trade-off between them

- AUC-ROC as a threshold-independent measure of classifier quality

## Tasks

- Loaded the breast cancer dataset, checked for missing values (none found), and reviewed the class balance (357 benign vs 212 malignant cases).

- Mapped the diagnosis labels to numeric (0 = benign, 1 = malignant), separated features X and target y, and performed an 80/20 train/test split.

- Scaled the features with StandardScaler and trained a LogisticRegression model.

- Generated predictions and class probabilities, and computed accuracy (\~97.4%).

- Produced the confusion matrix (TN=70, FP=1, FN=2, TP=41) and computed precision, recall, and F1 for both classes with classification\_report.

- Decided that recall matters more than precision for this problem, since a false negative (missing a real malignant case) is far more dangerous than a false positive.

- Computed the AUC-ROC (\~0.997) and interpreted what it says about the model's ability to separate the two classes across every threshold.

## Key Takeaway



Accuracy alone can hide exactly the mistakes that matter most — here, a 97.4% accuracy still meant missing 2 real malignant cases (false negatives), which the confusion matrix and per-class recall made visible in a way accuracy never could. Which metric to optimize is a real decision that depends on the problem: for a cancer diagnosis, recall on the positive class matters most, since missing a real case is far costlier than a false alarm that gets corrected by further testing. AUC-ROC rounded this out by confirming the model's strong separation between classes holds across every possible decision threshold, not just the default 0.5 — meaning there's real room to trade some precision for higher recall if this were used clinically.



## Files



day3.ipynb — logistic regression classifier on the Breast Cancer Wisconsin dataset, including feature scaling, model training, confusion matrix, precision/recall/F1, a precision-vs-recall justification, and AUC-ROC evaluation.

