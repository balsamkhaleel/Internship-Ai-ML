## Day 5 — EDA Part 2: Correlation \& Data Storytelling

## Summary



Explored bivariate analysis, correlation, and data storytelling, and learned how these concepts are applied in Machine Learning. Practiced scatter plots, grouped box plots, correlation heatmaps, and pairplots on the Titanic dataset, then assembled a complete, narrated EDA notebook.



## Key Concepts

*Bivariate analysis: scatter plots and grouped box plots

*Correlation as a measure of how strongly two numeric variables move together (-1 to +1)

*The correlation heatmap for scanning all pairwise relationships at once

*Correlation is not causation

*The pairplot for scanning every variable relationship in a single grid

*Data storytelling: turning analysis into a clear narrative

*Assembling a complete EDA notebook: statistics, univariate, outliers, bivariate, correlation

## Tasks

*Loaded the Titanic test dataset (tested.csv) and reviewed its shape, structure, descriptive statistics, and missing values.

*Produced a scatter plot of Age vs Fare and a grouped box plot of Fare by Pclass to examine key variable relationships.

*Computed the correlation matrix for all numeric columns and visualized it as an annotated heatmap.

-Identified the strongest relationships in the data (Pclass↔Fare, Fare↔Survived, SibSp↔Parch) and interpreted what each might mean for a future model.

-Used a pairplot colored by Survived to scan every numeric relationship at once.

-Assembled the full EDA — statistics, univariate distributions, outliers, bivariate relationships, and correlation — into one narrated notebook.

-Documented the final commit step for pushing the finished EDA notebook to GitHub.

##Key Takeaway



Bivariate analysis and correlation are where genuine insight starts to appear, because ML is fundamentally about relationships between features and a target. A correlation heatmap and pairplot make it fast to scan an entire dataset for relationships worth investigating further, but correlation only identifies patterns — it never proves cause. The real deliverable of EDA is not the charts themselves but a clear narrative: what the data contains, what patterns and problems were found, and what they imply for modeling. This complete, narrated notebook is the template for the EDA stage of every project going forward, through to the Phase 3 capstone.



##Files



day5.ipynb — bivariate EDA on the Titanic dataset, including scatter plots, grouped box plots, a correlation heatmap, a pairplot, and a full narrated EDA summary.

