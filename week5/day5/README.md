\# Day 5 — Unsupervised Learning \& Data Analysis



\## Overview



Completed Day 5 of the Cardiovascular Disease project by performing data cleaning, exploratory data analysis, and unsupervised learning. Applied K-Means and DBSCAN clustering to explore patient groups and identify hidden patterns within the dataset.



\## Topics Covered



\* Data preparation and cleaning

\* Exploratory Data Analysis (EDA)

\* Feature distributions and relationships

\* Correlation analysis

\* Feature scaling

\* K-Means clustering

\* Elbow Method

\* Silhouette Score

\* DBSCAN clustering

\* K-Distance analysis

\* Cluster profiling

\* Noise detection



\## Dataset



\* 68,741 samples

\* 13 features

\* No missing values

\* No duplicate rows

\* No duplicate patient IDs

\* Binary target: `cardio`

\* cardio = 0: No cardiovascular disease

\* cardio = 1: Cardiovascular disease



\## Data Preparation



\* Converted age from days to years.

\* Removed invalid height values.

\* Removed invalid weight values.

\* Removed invalid blood pressure values.

\* Checked for missing values and duplicates.

\* Prepared the cleaned dataset for analysis and clustering.



\## Exploratory Data Analysis



\* Analyzed numerical feature distributions.

\* Explored categorical feature distributions.

\* Examined patient characteristics in relation to cardiovascular disease.

\* Analyzed correlations between numerical features.

\* Identified age, weight, and blood pressure as important features related to the target.

\* Observed a strong correlation between systolic and diastolic blood pressure.



\## K-Means Clustering



K-Means clustering was applied after standardizing the selected features.



\* Evaluated the number of clusters using the Elbow Method.

\* Used Silhouette Score to evaluate clustering quality.

\* The final configuration used \*\*7 clusters\*\*.

\* Analyzed the characteristics of the resulting patient groups.



\## DBSCAN Clustering



DBSCAN was applied as a density-based clustering method.



\* Used a k-distance plot to help select the `eps` value.

\* `eps = 2.5`

\* `min\_samples = 10`

\* Identified dense patient groups.

\* Detected potential noise and unusual observations.



\## Key Takeaways



\* Data cleaning and EDA provided a better understanding of the patient population before clustering.

\* K-Means identified distinct patient groups based on their characteristics.

\* The Elbow Method and Silhouette Score helped evaluate the appropriate number of clusters.

\* DBSCAN provided a complementary clustering approach and allowed potential noise observations to be identified.

\* Unsupervised learning provided additional insights into the structure of the cardiovascular disease dataset without using the target variable during clustering.



\## Tools



\* Python

\* Pandas

\* NumPy

\* Scikit-learn

\* Matplotlib

\* Seaborn

\* Jupyter Notebook



