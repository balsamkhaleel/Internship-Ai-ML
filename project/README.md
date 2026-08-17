\# ❤️ Cardiac Patient Monitoring System



\## 📌 Project Overview



The \*\*Cardiac Patient Monitoring System\*\* is a machine learning project that analyzes cardiovascular health data to identify patterns associated with cardiovascular disease.



The project combines \*\*data cleaning, exploratory data analysis, statistical analysis, supervised learning, hyperparameter tuning, threshold optimization, and unsupervised learning\*\* to gain insights into patient characteristics and build classification models for cardiovascular disease detection.



The main objective is to develop a reliable machine learning workflow that can classify whether a patient is likely to have cardiovascular disease based on demographic, clinical, and lifestyle features.



\---



\## 🎯 Objectives



\* Clean and prepare cardiovascular patient data.

\* Perform exploratory data analysis (EDA).

\* Analyze relationships between patient characteristics and cardiovascular disease.

\* Build and compare multiple supervised learning models.

\* Apply cross-validation and hyperparameter tuning.

\* Optimize the classification threshold to improve disease detection.

\* Evaluate the final model using multiple classification metrics.

\* Analyze feature importance.

\* Apply unsupervised learning to identify patient groups and hidden patterns.



\---



\## 📊 Dataset



The project uses a cardiovascular disease dataset containing \*\*70,000 patient records\*\*.



\### Features



| Feature       | Description                |

| ------------- | -------------------------- |

| `id`          | Patient identifier         |

| `age`         | Age in days                |

| `gender`      | Gender encoded as 1 or 2   |

| `height`      | Height in centimeters      |

| `weight`      | Weight in kilograms        |

| `ap\_hi`       | Systolic blood pressure    |

| `ap\_lo`       | Diastolic blood pressure   |

| `cholesterol` | Cholesterol level          |

| `gluc`        | Glucose level              |

| `smoke`       | Smoking status             |

| `alco`        | Alcohol consumption status |

| `active`      | Physical activity status   |

| `cardio`      | Target variable            |



\### Target Variable



\* `0` → No cardiovascular disease

\* `1` → Cardiovascular disease



\---



\## 🧹 Data Cleaning



Several data-quality checks and cleaning operations were performed before modeling.



\### Blood Pressure



Extreme and implausible blood pressure values were identified and removed.



The following ranges were used:



\* Systolic blood pressure: \*\*40–300 mmHg\*\*

\* Diastolic blood pressure: \*\*40–300 mmHg\*\*



\### Age



The original age feature was stored in days.



It was converted into years using:



```python

age\_years = age / 365.25

```



The original `age` column was then removed.



\### Height



Values outside the range of \*\*100–200 cm\*\* were removed as clearly implausible observations.



\### Weight



Values outside the range of \*\*30–200 kg\*\* were removed.



\### Final Dataset



After cleaning:



\* \*\*68,741 observations\*\*

\* \*\*13 columns\*\*

\* No missing values

\* No duplicate rows

\* No duplicate patient IDs



\---



\## 🔎 Exploratory Data Analysis



The EDA stage explored the distribution of patient characteristics and their relationship with cardiovascular disease.



The analysis included:



\* Cardiovascular disease distribution

\* Age distribution

\* Gender distribution

\* Height

\* Weight

\* Systolic blood pressure

\* Diastolic blood pressure

\* Cholesterol

\* Glucose

\* Smoking

\* Alcohol consumption

\* Physical activity

\* Correlation analysis



\### Key Findings



Some of the strongest differences between the cardiovascular disease classes were observed in:



\*\*Age\*\*



Patients with cardiovascular disease had a higher average age.



\*\*Weight\*\*



\* No disease: approximately \*\*71.58 kg\*\*

\* Disease: approximately \*\*76.72 kg\*\*



\*\*Systolic Blood Pressure\*\*



\* No disease: approximately \*\*119.56 mmHg\*\*

\* Disease: approximately \*\*133.82 mmHg\*\*



\*\*Diastolic Blood Pressure\*\*



\* No disease: approximately \*\*78.17 mmHg\*\*

\* Disease: approximately \*\*84.66 mmHg\*\*



\*\*Cholesterol\*\*



The proportion of patients with cardiovascular disease increased substantially as cholesterol level increased.



\*\*Physical Activity\*\*



Inactive patients showed a higher proportion of cardiovascular disease compared with active patients.



\---



\## 📈 Correlation Analysis



Correlation analysis was performed on the main numerical features.



The strongest positive correlations with the target were:



| Feature     | Correlation with `cardio` |

| ----------- | ------------------------: |

| `ap\_hi`     |                     0.425 |

| `ap\_lo`     |                     0.335 |

| `age\_years` |                     0.240 |

| `weight`    |                     0.180 |

| `height`    |                    -0.012 |



The strongest relationship was observed between systolic and diastolic blood pressure, with a correlation of approximately \*\*0.698\*\*.



\---



\## 🤖 Supervised Learning



The project evaluated four classification algorithms:



1\. \*\*Logistic Regression\*\*

2\. \*\*Random Forest\*\*

3\. \*\*Decision Tree\*\*

4\. \*\*K-Nearest Neighbors (KNN)\*\*



The dataset was divided using a stratified train/test split:



\* \*\*80% Training\*\*

\* \*\*20% Testing\*\*



Stratification was used to preserve the target class distribution.



\---



\## 🔄 Cross-Validation



A \*\*5-fold Stratified Cross-Validation\*\* strategy was used during model evaluation and hyperparameter tuning.



```python

StratifiedKFold(

&#x20;   n\_splits=5,

&#x20;   shuffle=True,

&#x20;   random\_state=42

)

```



This provides a more reliable estimate of model performance while maintaining the class distribution across folds.



\---



\## ⚙️ Hyperparameter Tuning



`GridSearchCV` was used to optimize the main supervised models.



\### Logistic Regression



Parameters such as:



\* `C`

\* `class\_weight`



were evaluated.



\### Random Forest



Parameters including:



\* `n\_estimators`

\* `max\_depth`

\* `min\_samples\_split`



were optimized.



\### Decision Tree



Parameters including:



\* `max\_depth`

\* `min\_samples\_split`

\* `min\_samples\_leaf`



were evaluated.



\---



\## 🎯 Threshold Optimization



Since cardiovascular disease detection is a classification problem where missing a positive patient can be important, \*\*Recall\*\* was given particular attention.



Instead of relying only on the default probability threshold of `0.50`, multiple thresholds were evaluated:



```text

0.30

0.35

0.40

0.45

0.50

0.55

0.60

```



A threshold of \*\*0.35\*\* was selected based on the Precision-Recall trade-off.



\### Final Random Forest Results



| Metric    |      Score |

| --------- | ---------: |

| Accuracy  | \*\*70.66%\*\* |

| Precision | \*\*66.29%\*\* |

| Recall    | \*\*82.87%\*\* |

| F1-Score  | \*\*73.65%\*\* |



The increased Recall allows the model to identify a larger proportion of patients with cardiovascular disease.



> \*\*Note:\*\* This project is intended for educational and analytical purposes and is not a clinical diagnostic system.



\---



\## 📊 Model Evaluation



The final model was evaluated using:



\* Accuracy

\* Precision

\* Recall

\* F1-Score

\* Confusion Matrix

\* Classification Report



A confusion matrix was also generated to examine the distribution of:



\* True Negatives

\* False Positives

\* False Negatives

\* True Positives



\---



\## 🌲 Feature Importance



Feature importance was extracted from the final Random Forest model to understand which patient characteristics contributed most to the predictions.



This provides an additional interpretation of the trained model and helps identify the features that were most useful for cardiovascular disease classification.



\---



\## 🔵 Unsupervised Learning



Unsupervised learning was used to explore the natural structure of the patient population without using the `cardio` target during clustering.



Two clustering approaches were explored:



\### K-Means



K-Means clustering was applied after standardizing the clustering features.



The number of clusters was evaluated using:



\* \*\*Elbow Method\*\*

\* \*\*Silhouette Score\*\*



The final configuration used:



```python

n\_clusters = 7

```



Cluster profiles were then analyzed using the average characteristics of each group.



\### DBSCAN



DBSCAN was also explored as a density-based clustering method.



The parameters were selected based on a k-distance plot:



```text

eps = 2.5

min\_samples = 10

```



DBSCAN was used to identify dense patient groups and potential noise observations.



\---



\## 🛠️ Technologies \& Libraries



\### Programming Language



\* Python



\### Data Analysis



\* Pandas

\* NumPy



\### Visualization



\* Matplotlib



\### Machine Learning



\* Scikit-learn



\### Main Techniques



\* Data Cleaning

\* Exploratory Data Analysis

\* Correlation Analysis

\* Feature Engineering

\* Train/Test Split

\* Cross-Validation

\* Logistic Regression

\* Decision Tree

\* KNN

\* Random Forest

\* Grid Search

\* Threshold Optimization

\* K-Means Clustering

\* DBSCAN

\* Model Evaluation



\---



\## 📁 Project Structure



```text

Cardiac-Patient-Monitoring-System/

│

├── cardio.csv

├── Cardiac\_Patient\_Monitoring\_System.ipynb

└── README.md



\---



\## 🚀 Workflow



```text

Raw Dataset

&#x20;    ↓

Data Understanding

&#x20;    ↓

Data Quality Analysis

&#x20;    ↓

Data Cleaning

&#x20;    ↓

Exploratory Data Analysis

&#x20;    ↓

Correlation Analysis

&#x20;    ↓

Train / Test Split

&#x20;    ↓

Cross-Validation

&#x20;    ↓

Baseline Model

&#x20;    ↓

Supervised Learning

&#x20;    ↓

Hyperparameter Tuning

&#x20;    ↓

Threshold Optimization

&#x20;    ↓

Final Model Evaluation

&#x20;    ↓

Feature Importance

&#x20;    ↓

Unsupervised Learning

&#x20;    ↓

K-Means + DBSCAN

&#x20;    ↓

Final Insights

```



\---



\## 📝 Conclusion



The project demonstrates a complete machine learning workflow for cardiovascular disease analysis.



The supervised learning experiments showed that \*\*Random Forest\*\* provided a useful solution for cardiovascular disease detection. By adjusting the classification threshold from the default value to \*\*0.35\*\*, the model achieved a \*\*Recall of 82.87%\*\*, allowing it to identify a larger proportion of positive cases.



The unsupervised learning experiments provided complementary insights into the underlying structure of the patient population through \*\*K-Means and DBSCAN clustering\*\*.



Overall, the project combines predictive modeling with exploratory and unsupervised analysis to provide a broader understanding of cardiovascular disease patterns within the dataset.





