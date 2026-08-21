# Day 4 — t-SNE \& Anomaly Detection



## Overview



Applied t-SNE and Isolation Forest on the Breast Cancer Wisconsin dataset to explore high-dimensional data and detect unusual observations using unsupervised learning.



## Topics Covered



- t-SNE for local-structure visualization

- PCA vs. t-SNE

- Anomaly detection

- Isolation Forest

- Contamination parameter

- Interpretation of detected anomalies



## Dataset



- 569 samples

- 30 numerical features

- 357 Benign

- 212 Malignant

- No missing values

- No duplicate rows



## Results



### PCA



- First 2 components explained **63.24%** of the variance.

- First 5 components explained **84.73%** of the variance.



### t-SNE



Reduced the 30-dimensional feature space to 2D and revealed clearer local structure between the observations.



### Isolation Forest



- Contamination: **5%**

- Normal samples: **540**

- Anomalies: **29**

- Anomaly rate: **5.10%**



Among the detected anomalies:



- **22 Malignant**

- **7 Benign**



The target labels were not used by Isolation Forest and were only used afterward for interpretation.



## Key Takeaways



- PCA is useful for understanding global variance.

- t-SNE is useful for exploring local structure.

- Isolation Forest can detect unusual observations without labeled anomaly data.

- Anomaly detection and classification are different tasks.



## Tools



- Python

- Pandas

- Scikit-learn

- Matplotlib

- Jupyter Notebook

