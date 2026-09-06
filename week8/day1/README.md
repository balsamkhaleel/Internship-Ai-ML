# Day 1 — Sprint 3 Planning & NLP Preprocessing

---

# 1. Sprint 3 Planning

**🚀 Sprint 3 Planning**

**🎯 Sprint Goal**

The goal of Sprint 3 is to integrate the final machine learning model into a complete and reliable prediction pipeline, conduct comprehensive evaluation and error analysis, test the reliability of the system, and prepare the project for deployment in Sprint 4.

The **Tuned Neural Network** was selected as the final model based primarily on achieving the highest **F1-score**.

---

**📋 Sprint 3 Backlog**

* Finalize and document the final model.
* Integrate preprocessing, feature engineering, scaling, and the trained model.
* Perform comprehensive model evaluation.
* Focus on **F1-score, Precision, and Recall**.
* Create Confusion Matrix, ROC Curve, and Precision-Recall Curve.
* Analyze False Positives and False Negatives.
* Evaluate Decision Threshold optimization.
* Test pipeline reliability and robustness.
* Save the final model and preprocessing components.
* Prepare the project for deployment in Sprint 4.

---

**🏆 Final Model**

**Tuned Neural Network with Threshold Optimization**

Selected because it achieved the highest **F1-score**, providing a balance between Precision and Recall.

---

**🔄 Carrying Forward Improvements from Sprint 2**

* Focus on **F1-score**.
* Use **Threshold Optimization**.
* Avoid relying on Accuracy alone.
* Apply preprocessing consistently.
* Improve reproducibility and project organization.
* Prepare all components for deployment.

---

**🛣️ Sprint 3 Roadmap**

**Model Integration → Evaluation → Error Analysis → Reliability Testing → Finalization → Deployment Preparation**

---

# 2. NLP Preprocessing

## 🎯 Learning Objectives

* Apply text preprocessing.
* Perform tokenization and cleaning.
* Remove stop words.
* Preserve negations.
* Apply lemmatization.
* Compare stemming and lemmatization.

## 📊 Dataset

The **IMDb Movie Reviews Dataset** contains 50,000 balanced reviews.

| Sentiment |  Count |
| --------- | -----: |
| Positive  | 25,000 |
| Negative  | 25,000 |

No missing values were found.

## 📚 Libraries

```python
import pandas as pd
import re
import string
import nltk

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer, PorterStemmer
```

```python
nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('omw-1.4')
```

## 📥 Load Dataset

```python
df = pd.read_csv("IMDB Dataset.csv")

print(df.shape)
df.head()
```

**Output:** `(50000, 2)`

## 🔤 Tokenization & Cleaning

```python
text = df['review'].iloc[0]

text = text.lower()
text = re.sub(r'<.*?>', ' ', text)

tokens = word_tokenize(text)

tokens = [
    word for word in tokens
    if word not in string.punctuation
    and not word.isdigit()
]
```

## 🚫 Stop-word Removal & Negation Preservation

```python
stop_words = set(stopwords.words('english'))
important_negations = {"not", "no", "never"}

tokens = [
    word for word in tokens
    if word not in stop_words
    or word in important_negations
]
```

## 🧠 Lemmatization

```python
lemmatizer = WordNetLemmatizer()

tokens = [
    lemmatizer.lemmatize(word)
    for word in tokens
]
```

Lemmatization was selected because it produces more meaningful base forms than stemming.

## 🔄 Complete Pipeline

```python
def preprocess_text(text):

    text = text.lower()
    text = re.sub(r'<.*?>', ' ', text)

    tokens = word_tokenize(text)

    tokens = [
        word for word in tokens
        if word not in string.punctuation
        and not word.isdigit()
    ]

    negations = {"not", "no", "never"}

    tokens = [
        word for word in tokens
        if word not in stop_words
        or word in negations
    ]

    return [
        lemmatizer.lemmatize(word)
        for word in tokens
    ]
```

## 📈 Before vs After

| Metric         | Result |
| -------------- | -----: |
| Tokens before  |    380 |
| Tokens after   |    178 |
| Tokens removed |    202 |
| Reduction      | 53.16% |

## ❗ Negation Verification

```python
test = "I did not like this movie at all. I never recommend it."

print(preprocess_text(test))
```

**Output:**

```text
['not', 'like', 'movie', 'never', 'recommend']
```

Negations were successfully preserved.

## 📝 Summary

**Pipeline:**

**Lowercasing → HTML Removal → Tokenization → Punctuation/Number Removal → Stop-word Removal → Negation Preservation → Lemmatization**

> Contractions such as `you'll` may require additional handling in a production pipeline.

