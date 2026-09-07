\# Day 2 — Text Representation: TF-IDF \& Embeddings



\## Overview



This session focused on transforming cleaned text into numerical representations for sentiment classification using the \*\*IMDB Movie Reviews Dataset\*\*.



The main goal was to understand and compare \*\*TF-IDF\*\* and \*\*Word2Vec Embeddings\*\* and evaluate their effectiveness using the same Logistic Regression classifier.



\## 1. Data Preparation



The preprocessing pipeline from Day 1 was reused, including:



\- Lowercasing

\- Removing HTML tags

\- Tokenization

\- Removing punctuation and numbers

\- Removing stop words while preserving negations (`not`, `no`, `never`)

\- Lemmatization



The dataset was split using stratified sampling:



\- \*\*Training:\*\* 40,000 reviews

\- \*\*Testing:\*\* 10,000 reviews



\## 2. TF-IDF Representation



TF-IDF was applied with a maximum of \*\*5,000 features\*\*.



Training shape: `(40000, 5000)`  

Testing shape: `(10000, 5000)`



A Logistic Regression classifier was trained on the TF-IDF features.



\### Results



| Metric | Score |

|---|---:|

| Accuracy | 0.8900 |

| Precision | 0.8825 |

| Recall | 0.8998 |

| \*\*F1-score\*\* | \*\*0.8911\*\* |



\## 3. Word2Vec Embeddings



A pre-trained \*\*Word2Vec\*\* model was used to explore semantic relationships between words.



For example, words similar to `excellent` included:



`terrific`, `superb`, `exceptional`, `fantastic`, and `good`.



Each review was then converted into a \*\*300-dimensional embedding vector\*\* by averaging the vectors of its words.



Training shape: `(40000, 300)`  

Testing shape: `(10000, 300)`



The same Logistic Regression classifier was trained using the review embeddings.



\### Results



| Metric | Score |

|---|---:|

| Accuracy | 0.8569 |

| Precision | 0.8585 |

| Recall | 0.8546 |

| \*\*F1-score\*\* | \*\*0.8566\*\* |



\## 4. Comparison



| Representation | Accuracy | Precision | Recall | \*\*F1-score\*\* |

|---|---:|---:|---:|---:|

| \*\*TF-IDF\*\* | 0.8900 | 0.8825 | 0.8998 | \*\*0.8911\*\* |

| Word2Vec | 0.8569 | 0.8585 | 0.8546 | 0.8566 |



A visualization was created to compare the performance of both representations across Accuracy, Precision, Recall, and F1-score, with an additional F1-score comparison.



\## 5. Conclusion



TF-IDF achieved the best performance with an \*\*F1-score of 0.8911\*\*, outperforming Word2Vec by \*\*3.45 percentage points\*\*.



Therefore, \*\*TF-IDF was selected as the preferred representation\*\* for the current sentiment classification task.



Word2Vec successfully captured semantic relationships between words, but averaging word vectors into a single review representation can lose word order and contextual information.

