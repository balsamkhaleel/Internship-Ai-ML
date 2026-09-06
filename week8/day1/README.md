\# Day 1 — Sprint 3 Planning \& NLP Preprocessing



\---



\# 1. Sprint 3 Planning



\*\*🚀 Sprint 3 Planning\*\*



\*\*🎯 Sprint Goal\*\*



The goal of Sprint 3 is to integrate the final machine learning model into a complete and reliable prediction pipeline, conduct comprehensive evaluation and error analysis, test the reliability of the system, and prepare the project for deployment in Sprint 4.



The \*\*Tuned Neural Network\*\* was selected as the final model based primarily on achieving the highest \*\*F1-score\*\*.



\---



\*\*📋 Sprint 3 Backlog\*\*



\* Finalize and document the final model.

\* Integrate preprocessing, feature engineering, scaling, and the trained model.

\* Perform comprehensive model evaluation.

\* Focus on \*\*F1-score, Precision, and Recall\*\*.

\* Create Confusion Matrix, ROC Curve, and Precision-Recall Curve.

\* Analyze False Positives and False Negatives.

\* Evaluate Decision Threshold optimization.

\* Test pipeline reliability and robustness.

\* Save the final model and preprocessing components.

\* Prepare the project for deployment in Sprint 4.



\---



\*\*🏆 Final Model\*\*



\*\*Tuned Neural Network with Threshold Optimization\*\*



Selected because it achieved the highest \*\*F1-score\*\*, providing a balance between Precision and Recall.



\---



\*\*🔄 Carrying Forward Improvements from Sprint 2\*\*



\* Focus on \*\*F1-score\*\*.

\* Use \*\*Threshold Optimization\*\*.

\* Avoid relying on Accuracy alone.

\* Apply preprocessing consistently.

\* Improve reproducibility and project organization.

\* Prepare all components for deployment.



\---



\*\*🛣️ Sprint 3 Roadmap\*\*



\*\*Model Integration → Evaluation → Error Analysis → Reliability Testing → Finalization → Deployment Preparation\*\*



\---



\# 2. NLP Preprocessing



\## 🎯 Learning Objectives



\* Apply text preprocessing.

\* Perform tokenization and cleaning.

\* Remove stop words.

\* Preserve negations.

\* Apply lemmatization.

\* Compare stemming and lemmatization.



\## 📊 Dataset



The \*\*IMDb Movie Reviews Dataset\*\* contains 50,000 balanced reviews.



| Sentiment |  Count |

| --------- | -----: |

| Positive  | 25,000 |

| Negative  | 25,000 |



No missing values were found.



\## 📚 Libraries



```python

import pandas as pd

import re

import string

import nltk



from nltk.tokenize import word\_tokenize

from nltk.corpus import stopwords

from nltk.stem import WordNetLemmatizer, PorterStemmer

```



```python

nltk.download('punkt')

nltk.download('punkt\_tab')

nltk.download('stopwords')

nltk.download('wordnet')

nltk.download('omw-1.4')

```



\## 📥 Load Dataset



```python

df = pd.read\_csv("IMDB Dataset.csv")



print(df.shape)

df.head()

```



\*\*Output:\*\* `(50000, 2)`



\## 🔤 Tokenization \& Cleaning



```python

text = df\['review'].iloc\[0]



text = text.lower()

text = re.sub(r'<.\*?>', ' ', text)



tokens = word\_tokenize(text)



tokens = \[

&#x20;   word for word in tokens

&#x20;   if word not in string.punctuation

&#x20;   and not word.isdigit()

]

```



\## 🚫 Stop-word Removal \& Negation Preservation



```python

stop\_words = set(stopwords.words('english'))

important\_negations = {"not", "no", "never"}



tokens = \[

&#x20;   word for word in tokens

&#x20;   if word not in stop\_words

&#x20;   or word in important\_negations

]

```



\## 🧠 Lemmatization



```python

lemmatizer = WordNetLemmatizer()



tokens = \[

&#x20;   lemmatizer.lemmatize(word)

&#x20;   for word in tokens

]

```



Lemmatization was selected because it produces more meaningful base forms than stemming.



\## 🔄 Complete Pipeline



```python

def preprocess\_text(text):



&#x20;   text = text.lower()

&#x20;   text = re.sub(r'<.\*?>', ' ', text)



&#x20;   tokens = word\_tokenize(text)



&#x20;   tokens = \[

&#x20;       word for word in tokens

&#x20;       if word not in string.punctuation

&#x20;       and not word.isdigit()

&#x20;   ]



&#x20;   negations = {"not", "no", "never"}



&#x20;   tokens = \[

&#x20;       word for word in tokens

&#x20;       if word not in stop\_words

&#x20;       or word in negations

&#x20;   ]



&#x20;   return \[

&#x20;       lemmatizer.lemmatize(word)

&#x20;       for word in tokens

&#x20;   ]

```



\## 📈 Before vs After



| Metric         | Result |

| -------------- | -----: |

| Tokens before  |    380 |

| Tokens after   |    178 |

| Tokens removed |    202 |

| Reduction      | 53.16% |



\## ❗ Negation Verification



```python

test = "I did not like this movie at all. I never recommend it."



print(preprocess\_text(test))

```



\*\*Output:\*\*



```text

\['not', 'like', 'movie', 'never', 'recommend']

```



Negations were successfully preserved.



\## 📝 Summary



\*\*Pipeline:\*\*



\*\*Lowercasing → HTML Removal → Tokenization → Punctuation/Number Removal → Stop-word Removal → Negation Preservation → Lemmatization\*\*



> Contractions such as `you'll` may require additional handling in a production pipeline.





