Day 4 — Trees, Forests, SVMs \& k-NN

Summary



Explored decision trees, random forests, SVMs, and k-NN, and learned how to compare multiple classifiers fairly. Practiced training all four models on the same Breast Cancer Wisconsin train/test split, evaluating them with the same metric, and interpreting a random forest's feature importances.



Key Concepts

Decision trees: rule-based, interpretable, prone to overfitting

Random forests: ensembles and feature importances

Support Vector Machines and the margin

k-Nearest Neighbors

Comparing models fairly on the same split and metric ("no free lunch")

Tasks

Reused the same dataset and 80/20 train/test split from Day 3 to keep the comparison fair.

Trained a Decision Tree (max\_depth=7), Random Forest (n\_estimators=100), SVM (RBF kernel), and k-NN (n\_neighbors=5) on identical training data.

Evaluated all four with classification\_report, comparing precision, recall, and F1 per class.

Reported the random forest's top feature importances — area\_worst, concave points\_worst, and concave points\_mean — and interpreted them as matching medical intuition (malignant tumors tend to be larger with more irregular, concave boundaries).

Compared all four models' weighted F1-scores in a bar chart and identified Random Forest as the best-performing model, explaining why in Markdown.

Key Takeaway



No single algorithm wins by default — the "no free lunch" principle held true here, with Decision Tree, Random Forest, SVM, and k-NN all landing in a fairly narrow performance range. But looking past the tied overall F1-scores, Random Forest gave the best balance of precision and recall specifically on the malignant class, the one that matters most clinically, while SVM and k-NN both leaned toward higher precision at the cost of missing more real malignant cases. The ensemble's averaging across 100 trees is what fixed the single decision tree's overfitting tendency, making Random Forest the most reliable choice for this particular, moderately imbalanced medical dataset — and its feature importances gave a bonus: an explainable, biologically sensible account of what the model actually relies on.



Files



day4.ipynb — comparing Decision Tree, Random Forest, SVM, and k-NN classifiers on the Breast Cancer Wisconsin dataset, including per-model evaluation, feature importances, and a fair model comparison with justification for the best performer.

