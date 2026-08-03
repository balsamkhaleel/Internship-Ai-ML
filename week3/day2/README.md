Day 2 — Linear Regression #

Summary ##



Explored linear regression and learned how to train, interpret, and evaluate a regression model. Practiced fitting a LinearRegression model on the California housing dataset, interpreting its coefficients, and evaluating it with MAE, RMSE, and R² against a baseline.



Key Concepts

Linear regression: fitting the best line (or hyperplane) through the data

Training and predicting with Scikit-learn's LinearRegression

Interpreting coefficients and the intercept

Regression metrics: MAE, RMSE, R²

Comparing a model against a baseline to confirm it adds value

Tasks

Loaded the housing dataset, handled missing values in total\_bedrooms, and one-hot encoded the categorical ocean\_proximity column.

Separated the data into features X and target y (median\_house\_value), then performed an 80/20 train/test split.

Trained a LinearRegression model and generated predictions on the test set.

Reported the model's coefficients and identified median\_income as the strongest well-supported predictor, while flagging ocean\_proximity\_ISLAND's large coefficient as based on very little data.

Evaluated the model with MAE (\~$50,702), RMSE (\~$70,031), and R² (\~0.626).

Compared the model's RMSE against a baseline that predicts the mean house value for every row, and confirmed the model reduces error by roughly 39%.

Documented the interpretation of the results in Markdown.

Key Takeaway



A linear regression model's prediction is just a weighted sum of the features plus a bias, which makes its coefficients directly interpretable — each one shows how much the prediction changes per unit increase in that feature, holding others constant. Evaluating a regression model always requires comparing it against a simple baseline: a model that cannot beat predicting the mean for every row has learned nothing useful. Here, the model clearly beat the baseline, but the gap between MAE and RMSE, along with a moderate R², showed it still struggles with a subset of harder-to-predict, high-value homes — a reminder that even a "successful" model has clear limits worth stating honestly.



Files



day2.ipynb — linear regression on the California housing dataset, including data preparation, model training, coefficient interpretation, evaluation metrics, and baseline comparison.

