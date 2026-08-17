\# Day 1 — Unsupervised Learning \& K-Means



\## Summary



Learned the fundamentals of unsupervised learning and clustering by applying K-Means to the Mall Customers dataset. Explored customer data, selected numerical features, applied feature scaling, used the Elbow Method to identify a suitable number of clusters, and used the Silhouette Score to evaluate the selected clustering configuration.



\## Key Concepts



\* Supervised vs. unsupervised learning

\* What clustering does and how it discovers natural groups

\* K-Means clustering and the centroid-assignment process

\* Choosing the number of clusters using the Elbow Method

\* Evaluating cluster quality using the Silhouette Score

\* Why feature scaling is important for distance-based algorithms

\* Interpreting cluster characteristics

\* Visualizing clusters and centroids



\## Tasks



\* Loaded and inspected the Mall Customers dataset.

\* Explored the dataset structure, data types, and descriptive statistics.

\* Selected `Age`, `Annual Income (k$)`, and `Spending Score (1-100)` as clustering features.

\* Removed `CustomerID` because it is only an identifier.

\* Excluded `Gender` because the lab focuses on numerical features only.

\* Applied `StandardScaler` to standardize the selected features.

\* Ran K-Means for values of k from 1 to 10.

\* Calculated inertia values and visualized the Elbow Method.

\* Selected k=4 based on the Elbow Method.

\* Calculated the Silhouette Score for k=4.

\* Trained the final K-Means model using four clusters.

\* Added the resulting cluster labels to the dataset.

\* Calculated the average characteristics of each cluster.

\* Visualized the customer clusters using Annual Income and Spending Score.

\* Visualized the final cluster centroids.

\* Interpreted the characteristics of each customer segment.



\## Results



\### Elbow Method



K-Means was evaluated for values of k from 1 to 10. The inertia decreased as the number of clusters increased, with the curve showing an elbow around k=4.



Based on the Elbow Method, four clusters were selected for the final model.



\### Silhouette Score



The Silhouette Score for the selected k=4 was:



|     k | Silhouette Score |

| ----: | ---------------: |

| \*\*4\*\* |        \*\*0.404\*\* |



The score indicates reasonably separated and meaningful clusters for the selected configuration.



\### Final Cluster Profiles



| Cluster |       Age | Annual Income (k$) | Spending Score |

| ------- | --------: | -----------------: | -------------: |

| 0       |     53.98 |              47.71 |          39.97 |

| 1       |     32.88 |              86.10 |      \*\*81.53\*\* |

| 2       | \*\*25.44\*\* |              40.00 |          60.30 |

| 3       |     39.37 |          \*\*86.50\*\* |      \*\*19.58\*\* |



\### Cluster Interpretation



\* \*\*Cluster 0:\*\* Older customers with moderate income and moderate spending.

\* \*\*Cluster 1:\*\* Relatively young customers with high income and high spending, representing a high-value customer segment.

\* \*\*Cluster 2:\*\* Young customers with relatively low income but moderate-to-high spending.

\* \*\*Cluster 3:\*\* Customers with high income but low spending.



An interesting finding is that Clusters 1 and 3 have very similar high average incomes, but their spending scores are significantly different. This shows that higher income does not necessarily lead to higher spending behavior.



\## Key Takeaway



K-Means clustering can discover meaningful customer segments without requiring predefined labels. Feature scaling is essential because K-Means relies on distance calculations, while the Elbow Method and Silhouette Score provide useful tools for selecting and evaluating the number of clusters.



The final model with k=4 revealed four distinct customer segments with different age, income, and spending characteristics.



The overall workflow was:



\*\*Data Exploration → Feature Selection → StandardScaler → Elbow Method → Silhouette Score → K-Means → Visualization → Cluster Interpretation\*\*



\## Files



\* `day1.ipynb` — Complete Day 1 notebook containing data exploration, feature scaling, Elbow Method, Silhouette Score, final K-Means clustering, visualization, and cluster interpretation.

\* `Mall\_Customers.csv` — Dataset used for the clustering analysis.



