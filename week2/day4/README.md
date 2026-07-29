# Day 4 — EDA Part 1: Distributions \& Outliers



## Summary



Performed univariate Exploratory Data Analysis (EDA) on the Diabetes dataset using Seaborn. Visualized the distributions of numerical variables using histograms and box plots, detected potential outliers using the IQR method, and analyzed the class distribution of the target variable Outcome.



## Key Concepts



* Exploratory Data Analysis (EDA) and why it comes before modeling

* Univariate analysis

* Histograms for understanding numerical distributions

* Box plots for visualizing quartiles and potential outliers

* Count plots for analyzing categorical class distributions

* KDE and distribution shapes

* Outlier detection using the IQR method

* Understanding skewed distributions

* Class imbalance and its impact on machine learning models

* Identifying potential missing values represented by 0



## Tasks



* Loaded the Diabetes dataset and inspected its shape, columns, data types, and missing values.

* Used .describe() to examine summary statistics and identify potential data quality issues.

* Created histograms for each numerical variable to analyze the shape and distribution of the data.

* Created box plots for key numerical variables (Glucose, Insulin, and DiabetesPedigreeFunction) to visually identify potential outliers.

* Applied the IQR method to the Insulin column and identified 34 potential outliers.

* Investigated the detected outliers and decided not to remove them automatically without further investigation or domain knowledge.

* Identified 0 values in some medical measurement columns as potential missing values that require further investigation.

* Created a count plot for the Outcome variable and identified an imbalance between the two target classes.

* Documented the findings and interpretations in Markdown cells throughout the notebook.



## Key Takeaway



EDA is an essential step before modeling because it helps uncover the structure, distribution, and quality of the data. Histograms and box plots can reveal skewness and potential outliers, while the IQR method provides a systematic way to flag extreme values. Outliers should not be removed automatically without understanding their meaning. EDA also revealed that some 0 values may represent missing medical measurements and that the target variable Outcome is imbalanced, both of which should be considered during data preprocessing and model development.



## Files



day4.ipynb — Univariate EDA of the Diabetes dataset, including distributions, box plots, IQR-based outlier detection, and class balance analysis.



