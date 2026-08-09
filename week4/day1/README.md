# Day 1 — Train / Validation / Test Splits

## Summary



Explored why a validation set is needed in addition to a test set, and learned how to build a correct three-way split. Practiced tuning a hyperparameter against a validation set only, then evaluating the final model on a held-out test set exactly once, on the Breast Cancer Wisconsin dataset.



## Key Concepts

- The problem with tuning against a single test set

- The three-way split: train, validation, test — each with one job

- Creating a three-way split in Scikit-learn with two train\_test\_split calls

- Why one validation set can still mislead (motivating cross-validation)

## Tasks

- Loaded the breast cancer dataset, mapped diagnosis to numeric, and separated features X and target y.

- Created a 60/20/20 train/validation/test split with a fixed random\_state, confirming the resulting shapes (341/114/114 rows).

- Scaled the features with StandardScaler, fitting only on the training set.

- Trained a logistic regression model and checked its accuracy on the validation set (\~97.4%).

- Tuned the C hyperparameter across five values by checking validation accuracy only, and selected C = 0.5 as the best-tied, most sensibly regularized choice.

- Trained the final model with the chosen C and evaluated it on the test set exactly once, reporting \~98.2% accuracy.

- Explained in Markdown what would go wrong if the test set had been used for tuning instead of the validation set.

## Key Takeaway



A single test set stops being an honest estimate of real-world performance the moment it's used to make decisions — even something as simple as comparing a few hyperparameter values. The three-way split solves this by giving each set exactly one job: the training set learns parameters, the validation set is checked repeatedly during tuning, and the test set is opened exactly once, after every decision is already final. Tuning against the test set instead would quietly bias the reported accuracy upward, because the "best" setting would have been chosen partly because it happened to fit that specific test data — not because it truly generalizes best.



## Files



day1.ipynb — three-way train/validation/test split on the Breast Cancer Wisconsin dataset, including hyperparameter tuning against the validation set, a one-time final test evaluation, and a Markdown explanation of test-set leakage.

