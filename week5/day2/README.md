# Day 2 — DBSCAN \& Hierarchical Clustering



## Summary



Explored alternative clustering methods to address some of the limitations of K-Means. Applied DBSCAN for density-based clustering and noise detection, then built a hierarchical clustering dendrogram to identify the underlying structure of the Mall Customers dataset. Finally, compared K-Means, DBSCAN, and Hierarchical Clustering results on the same dataset.



## Key Concepts



* Limitations of K-Means

* Density-based clustering with DBSCAN

* DBSCAN parameters: eps and min\_samples

* Noise and outlier detection

* Hierarchical clustering

* Dendrograms and linkage methods

* Choosing a cut height

* Comparing different clustering methods

* Selecting the appropriate clustering method based on data structure



## Tasks



* Used the Mall Customers dataset from Day 1 and selected Age, Annual Income (k$), and Spending Score (1-100) as clustering features.

* Standardized the selected features using StandardScaler.

* Applied DBSCAN with eps=0.5 and min\_samples=5.

* Calculated the number of clusters and noise points identified by DBSCAN.

* Found 6 DBSCAN clusters and 60 noise points.

* Visualized the DBSCAN clustering results.

* Built a hierarchical clustering model using Ward linkage.

* Generated and interpreted a dendrogram to examine the hierarchical structure of the data.

* Selected a cut height of approximately 12 based on the dendrogram.

* Obtained 4 hierarchical clusters.

* Applied K-Means with k=4 to provide a comparison with the other clustering methods.

* Visualized the K-Means, DBSCAN, and Hierarchical Clustering results.

* Compared the clustering methods based on their results and characteristics.

* Identified K-Means as the most suitable method for this dataset.



## Results



### DBSCAN



DBSCAN was applied using eps=0.5 and min\_samples=5.



* **Number of clusters:** 6

* **Number of noise points:** 60



DBSCAN classified 60 out of 200 customers as noise, while also producing several relatively small clusters.



### Hierarchical Clustering



A hierarchical clustering model was built using Ward linkage. The dendrogram showed a large increase in linkage distance near 20.



A cut height of approximately 12 was selected, resulting in:



* **Number of clusters:** 4



### Comparison



| Method       | Clusters | Noise Points |

| ------------ | -------: | -----------: |

| K-Means      |        4 |            0 |

| DBSCAN       |        6 |           60 |

| Hierarchical |        4 |            0 |



## Key Takeaway



Different clustering algorithms make different assumptions about the structure of the data. K-Means is suitable for relatively well-separated customer groups but requires the number of clusters to be specified in advance. DBSCAN can automatically discover clusters and detect noise, but its results are sensitive to eps and min\_samples. Hierarchical Clustering provides a useful view of the relationships between data points through a dendrogram and allows clusters to be selected using a cut height.



For this dataset, K-Means was the most suitable method because it produced clear and meaningful customer segments with four clusters. Hierarchical Clustering also produced four clusters and provided additional insight through the dendrogram, while DBSCAN classified a relatively large portion of the dataset as noise.



## Files



day2.ipynb — Complete Day 2 notebook containing DBSCAN clustering and noise detection, hierarchical clustering and dendrogram analysis, K-Means comparison, visualizations, and final method interpretation.



