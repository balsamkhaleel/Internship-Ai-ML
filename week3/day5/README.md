Day 5 — Supervised-Learning Mini-Project

Summary



Assembled a complete end-to-end supervised-learning pipeline on the Titanic dataset — from EDA through preprocessing, model training, and evaluation against a baseline — and practiced choosing and justifying the right model and metric for the task.



Key Concepts

The full pipeline: EDA → preprocessing → split → model → evaluation

Basic preprocessing: one-hot encoding, feature scaling

Avoiding data leakage (fitting the scaler on train only)

Choosing the right model and metric for the task

Documenting and justifying the final result against a baseline

Tasks

Determined the task was classification, since the target (Survived) is a category, not a continuous number.

Performed brief EDA: reviewed shape, missing values, class balance, survival by sex, and a correlation heatmap.

Preprocessed the data: filled missing Age with the median, dropped 2 rows missing Embarked, dropped the mostly-empty Cabin column, dropped non-predictive columns (PassengerId, Name, Ticket), and encoded Sex/Embarked.

Split the data 80/20 and scaled Age/Fare with StandardScaler, fitting only on the training set to avoid data leakage.

Established a baseline (predicting the majority class) at 61.2% accuracy.

Trained and evaluated Logistic Regression (78.1%), Random Forest (77.5%), and SVM (82.0%) against that baseline.

Selected SVM as the best-performing model and justified the choice in Markdown.

Key Takeaway



A real ML pipeline is more than fitting a model — it's a sequence of deliberate decisions, each with a reason: which columns to drop or keep, how to fill missing values, how to encode categories, and critically, fitting any scaler on training data only to avoid leaking test-set information into training. Every model beat the 61.2% baseline by a wide margin, proving each had learned something real, but the differences between them (SVM's 82.0% versus Random Forest's 77.5%) showed that model choice still matters and depends on the specific dataset — here, a small, moderately-sized dataset with likely feature interactions favored an SVM's curved decision boundary over the other two. This pipeline shape — EDA, preprocessing, split, model, evaluation — .



Files



day5.ipynb — end-to-end Titanic survival pipeline, including EDA, leakage-free preprocessing, three trained classifiers evaluated against a baseline, and a justified final model selection.

