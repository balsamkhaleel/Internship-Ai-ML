# Day 4 — Feature Engineering \& Hyperparameter Tuning



## Summary



Explored feature engineering and systematic hyperparameter tuning using `GridSearchCV`. Worked with the Titanic dataset to engineer new features, establish a cross-validated Random Forest baseline, tune its hyperparameters, and evaluate whether the engineered features actually improved performance.



## Key Concepts



- Feature engineering and why useful features can improve model performance

- Feature creation, encoding, scaling, and other common transformation techniques

- Hyperparameters vs. learned model parameters

- GridSearchCV and cross-validation

- best\_params\_ and best\_score\_

- RandomizedSearchCV for larger search spaces



## Tasks



 - Created two engineered features:

 - FamilySize = SibSp + Parch + 1

 - IsAlone = 1 when FamilySize == 1, otherwise 0

 - Built a preprocessing pipeline using imputation, scaling, and one-hot encoding.

 - Established an untuned Random Forest baseline using 5-fold cross-validation:

 - **Mean CV F1 = 0.7255**

 - Tuned the Random Forest using GridSearchCV over:

 - n\_estimators

 - max\_depth

 - min\_samples\_split

 - Best hyperparameter combination:

 - n\_estimators = 300

 - max\_depth = None

 - min\_samples\_split = 5

 - **Best CV F1 = 0.7497**

- Evaluated the tuned model on the held-out test set:

 - **Accuracy = 0.810**

 - **F1 = 0.734**

- Performed feature ablation experiments to measure the individual and combined contribution of FamilySize and IsAlone.



## Key Takeaway



Hyperparameter tuning improved the mean cross-validated F1 score from **0.7255 to 0.7497**, showing that systematic hyperparameter search can provide a meaningful improvement over default model settings.



The feature ablation experiments showed that the engineered features did not improve the overall model performance in this experiment. The highest mean CV F1 (**0.7514**) was achieved without either engineered feature, while removing only IsAlone produced a very similar score (**0.7512**).



This highlights an important practical lesson: **feature engineering should be validated experimentally rather than assumed to improve performance.**



The best hyperparameter combination was selected by GridSearchCV; however, the experiments did not isolate the individual effect of each hyperparameter, so the improvement is attributed to the combination rather than to a single parameter.



## Files



- day4.ipynb — Feature engineering, Random Forest hyperparameter tuning, cross-validation, model evaluation, visualizations, and feature ablation analysis.

