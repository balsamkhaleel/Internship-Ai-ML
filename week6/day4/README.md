\# Day 4 — Building \& Training a Neural Network with Keras



\## Overview



Built and trained a neural network using the TensorFlow/Keras Sequential API on the cleaned cardiovascular disease dataset.



The main focus was understanding the complete neural network training workflow, analyzing training behavior, and improving the baseline model using Batch Normalization and Dropout.



\## Objectives



\- Build a neural network using the Keras Sequential API.

\- Use Dense layers with appropriate activation functions.

\- Compile and train a binary classification model.

\- Analyze training and validation loss and accuracy.

\- Diagnose overfitting and model learning behavior.

\- Apply Batch Normalization and Dropout.

\- Evaluate the models on unseen test data.

\- Compare the baseline and improved models.



\## Dataset



The experiment uses the cleaned cardiovascular disease dataset.



\- \*\*Samples:\*\* 68,742

\- \*\*Features:\*\* 11

\- \*\*Target:\*\* `cardio`

\- \*\*Task:\*\* Binary Classification



The `id` column was removed because it is an identifier and does not provide useful predictive information.



\## Data Preparation



The following steps were performed before training:



\- Separated features (`X`) from the target (`y`).

\- Removed `id` and `cardio` from the input features.

\- Split the dataset into:

&#x20; - 70% Training

&#x20; - 15% Validation

&#x20; - 15% Test

\- Applied `StandardScaler` to standardize the input features.

\- The scaler was fitted only on the training data to prevent data leakage.



\## Baseline Model



The baseline neural network consists of:



\- Dense layer — 64 neurons, ReLU

\- Dense layer — 32 neurons, ReLU

\- Dense layer — 1 neuron, Sigmoid



The model was compiled using:



\- \*\*Optimizer:\*\* Adam

\- \*\*Loss:\*\* Binary Crossentropy

\- \*\*Metric:\*\* Accuracy



Early Stopping was used to stop training when validation loss stopped improving.



\## Improved Model



The baseline model was improved by adding:



\- Batch Normalization

\- Dropout with a rate of 0.3



These techniques were used to improve training stability and reduce overfitting.



\## Results



| Model | Test Loss | Test Accuracy |

|---|---:|---:|

| Baseline Neural Network | 0.5577 | 72.97% |

| Improved Neural Network | 0.5464 | 73.40% |



The improved model achieved a small improvement in test accuracy of approximately \*\*0.43 percentage points\*\* and a lower test loss.



\### Classification Performance



The improved model also showed a slight improvement in the F1-score for class `1`:



| Model | Class 1 F1-Score |

|---|---:|

| Baseline | 0.72 |

| Improved | 0.73 |



\## Key Findings



\- The baseline model showed limited improvement during training.

\- Training and validation curves did not show strong signs of overfitting.

\- Batch Normalization and Dropout produced a more stable training pattern.

\- The improved model slightly outperformed the baseline model on the test set.

\- The overall improvement was limited, indicating that additional model optimization may be needed for a significant performance increase.



\## Tools \& Technologies



\- Python

\- TensorFlow / Keras

\- Scikit-learn

\- Pandas

\- NumPy

\- Matplotlib

\- Google Colab / Jupyter Notebook

