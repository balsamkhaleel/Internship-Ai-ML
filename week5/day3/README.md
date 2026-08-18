# Day 3 — Dimensionality Reduction with PCA



## Summary



Learned the fundamentals of dimensionality reduction by applying Principal Component Analysis (PCA) to the Breast Cancer Wisconsin dataset. Inspected the dataset, selected the 30 numerical features, applied feature scaling, analyzed explained variance, selected the number of components needed to retain approximately 95% of the variance, and reduced the data to 2 components for visualization.



## Key Concepts



- The curse of dimensionality

- Dimensionality reduction and why it is useful

- Principal Component Analysis (PCA)

- Principal components and variance

- Explained variance ratio

- Cumulative explained variance

- Choosing the number of components using a 95% variance threshold

- Why feature scaling is required before PCA

- PCA for dimensionality reduction vs. visualization

- Trade-off between information preservation and interpretability



## Tasks



- Loaded and inspected the Breast Cancer Wisconsin dataset.

- Explored the dataset shape, data types, missing values, and duplicate rows.

- Identified and removed the id column because it is only an identifier.

- Removed the empty Unnamed: 32 column.

- Separated diagnosis as the target variable.

- Selected the 30 numerical measurements as PCA features.

- Applied StandardScaler to standardize all numerical features.

- Fitted PCA without limiting the number of components to analyze the explained variance.

- Calculated the explained variance ratio for each principal component.

- Calculated the cumulative explained variance.

- Plotted cumulative explained variance against the number of components.

- Selected 10 components because they retained approximately 95% of the total variance.

- Reduced the dataset from 30 original features to 10 principal components.

- Reduced the dataset to 2 principal components for visualization.

- Calculated the variance retained by the first two components.

- Created a 2D scatter plot using the diagnosis labels for visualization.

- Interpreted what PCA preserved and what was lost during dimensionality reduction.



## Results



### Explained Variance



PCA was first fitted using all 30 numerical features to analyze the contribution of each principal component.



The first components captured the largest amount of variance:



| Component | Explained Variance |

| --------- | -----------------: |

| PC1 | 44.27% |

| PC2 | 18.97% |

| PC3 | 9.39% |

| PC4 | 6.60% |

| PC5 | 5.50% |



The first two components together retained approximately **63.24%** of the total variance.



### Component Selection



The cumulative explained variance was analyzed to determine how many components should be retained.



The results showed:



- **2 components → 63.24% variance**

- **4 components → 79.24% variance**

- **9 components → 93.99% variance**

- **10 components → 95.16% variance**



Based on the commonly used 95% variance threshold, **10 principal components** were selected.



This reduced the feature space from **30 original features to 10 principal components**, while retaining approximately **95.16% of the total variance**.



### 2D PCA Visualization



A separate PCA model with two components was used to visualize the high-dimensional data in two dimensions.



The first two components retained approximately **63.24% of the total variance**.



The 2D scatter plot used the diagnosis labels only to color the observations:



- **B → Benign**

- **M → Malignant**



The visualization showed a visible separation between the benign and malignant groups, although some overlap remained.



### Information Preservation and Cost



Using 10 components preserved **95.16% of the total variance** while reducing the number of dimensions by **66.67%**.



However, PCA also introduced some trade-offs:



- Approximately **4.84% of the variance** was not retained.

- The original features were replaced by principal components.

- Each principal component is a combination of multiple original features, making the transformed features less directly interpretable.



For visualization, reducing the data to 2 components resulted in a larger information loss, retaining only **63.24% of the total variance**, but allowed the dataset to be represented in a 2D plot.



## Key Takeaway



PCA successfully reduced the dimensionality of the Breast Cancer Wisconsin dataset while preserving most of its variance. The first **10 principal components retained 95.16% of the total variance**, reducing the original feature space from 30 dimensions to 10.



A separate 2-component PCA representation retained **63.24% of the variance** and was used for visualization. The resulting plot showed a visible separation between benign and malignant cases.



The main benefit of PCA is reducing dimensionality and redundancy while preserving important variation in the data. The main trade-off is reduced interpretability because principal components are combinations of the original features rather than individual measurable features.



## Files



- day3.ipynb — Complete Day 3 notebook containing data inspection, feature scaling, PCA, explained variance analysis, component selection, 2D visualization, and interpretation.

- data.csv — Breast Cancer Wisconsin dataset used for the PCA analysis.

