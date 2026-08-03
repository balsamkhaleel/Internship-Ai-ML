# Day 2 — Linear Regression 


## Summary 

Explored linear regression and learned how to train, interpret, and evaluate a regression model. Practiced preprocessing the California housing dataset, standardizing the features with StandardScaler, training a LinearRegression model, interpreting its coefficients, and evaluating it with MAE, RMSE, and R² against a baseline.



## Key Concepts

- Linear regression: fitting the best line (or hyperplane) through the data

- Training and predicting with Scikit-learn's LinearRegression

- Interpreting coefficients and the intercept

- Regression metrics: MAE, RMSE, R²

- Comparing a model against a baseline to confirm it adds value
  
- Feature scaling with StandardScaler for coefficient comparability.

## Tasks

- Loaded the housing dataset, handled missing values in total_bedrooms, one-hot encoded the categorical ocean_proximity column, and standardized the features using StandardScaler.

- Separated the data into features X and target y (median\_house\_value), then performed an 80/20 train/test split.

- TTrained a LinearRegression model on the standardized training features and generated predictions on the standardized test set.

- Reported the model's coefficients and identified median\_income as the strongest well-supported predictor, while flagging ocean\_proximity\_ISLAND's large coefficient as based on very little data.

- Evaluated the model with MAE (~50,702), RMSE (~70,031), and R² (~0.626).

- Compared the model's RMSE against a baseline that predicts the mean house value for every row, and confirmed the model reduces error by roughly 39%.

- Documented the interpretation of the results in Markdown.


## Key Takeaway



A Linear Regression model predicts a target as a weighted sum of the features plus an intercept. Standardizing the features with StandardScaler makes the coefficients directly comparable. The model clearly beat the baseline, showing it learned useful relationships from the data, although the gap between MAE and RMSE indicates it still struggles with some higher-value homes.



## Files



day2.ipynb — linear regression on the California housing dataset, including data preparation, model training, coefficient interpretation, evaluation metrics, and baseline comparison.

