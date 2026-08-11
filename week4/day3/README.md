## Day 3 — Bias-Variance \& Diagnosing Model Fit

## Summary



Explored the bias-variance trade-off and learned how to diagnose a model's fit from the train-vs-test score gap. Practiced deliberately overfitting and underfitting a decision tree on the Breast Cancer Wisconsin dataset, then applied regularization (cost-complexity pruning) to fix the overfit model.



## Key Concepts

- Underfitting (high bias) vs. overfitting (high variance)

- The bias-variance trade-off

-Diagnosing fit from the train-vs-validation (test) gap

- Regularization: cost-complexity pruning for decision trees 

## Tasks

- Loaded the dataset, checked for missing values (none found), and reviewed the class balance (357 benign vs 212 malignant).

- Trained a deliberately overfit decision tree (max\_depth=2000) and confirmed the diagnosis: perfect training accuracy (1.000) but a much lower test accuracy (0.930), a gap of 0.070.

- Trained a deliberately underfit decision tree (max\_depth=1) and confirmed both scores were low relative to the other models (training 0.930, test 0.877).

- Trained a well-fit decision tree (max\_depth=2) for comparison, with the smallest gap of the three (0.033).

- Assembled all three models' scores into one comparison table and chart.

- Applied cost-complexity pruning (ccp\_alpha=0.01) to the overfit tree and showed the gap shrink from 0.070 to 0.046.

- Documented each diagnosis and fix with the score evidence in Markdown.

## Key Takeaway



The train-vs-test gap is the single most useful diagnostic in model tuning: a small gap with high scores means a good fit, a small gap with low scores means underfitting, and a large gap means overfitting — and the fix for each is the opposite of the other. Here, an unrestricted decision tree memorized the training data (a 0.070 gap), while a single-split tree was too simple to fit anything well (both scores low even with a modest 0.052 gap) — a reminder that gap size alone isn't the full picture, absolute performance matters too. Regularization (pruning) directly demonstrated the fix for overfitting: it traded a little training-set memorization for a smaller gap, without needing to hand-pick the "right" depth the way the explicit max\_depth=2 model did.



## Files



day3.ipynb — diagnosing overfitting, underfitting, and good fit on the Breast Cancer Wisconsin dataset using decision trees, including a train-vs-test gap comparison and a regularization (pruning) fix.

