\# Day 3 — RNNs \& LSTMs for Sequential Data



\## Overview



Day 3 focused on applying recurrent neural networks to sequential ECG heartbeat data.



The main objective was to understand why sequential data requires order-aware architectures and to compare a standard Recurrent Neural Network (RNN) with a Long Short-Term Memory (LSTM) network.



The experiment used the \*\*ECG Heartbeat Categorization Dataset\*\*, which contains preprocessed ECG heartbeat signals for five-class heartbeat classification.



\---



\## Learning Objectives



\* Understand why the order of observations matters in sequential data.

\* Understand how an RNN uses a hidden state to carry information across time steps.

\* Understand the vanishing-gradient problem in plain RNNs.

\* Understand how LSTM gated memory helps preserve relevant information.

\* Apply RNN and LSTM models to real sequential ECG data.

\* Compare the performance of RNN and LSTM models using appropriate classification metrics.



\---



\## Dataset



\*\*ECG Heartbeat Categorization Dataset\*\*



The dataset contains ECG heartbeat signals represented as sequences of 187 signal measurements.



\### Heartbeat Classes



| Label | Class            |

| ----: | ---------------- |

|     0 | Normal           |

|     1 | Supraventricular |

|     2 | Ventricular      |

|     3 | Fusion           |

|     4 | Unknown          |



The dataset is highly imbalanced, with the Normal class representing the majority of the samples.



\### Dataset Split



| Dataset    | Samples | Shape             |

| ---------- | ------: | ----------------- |

| Training   |  70,043 | `(70043, 187, 1)` |

| Validation |  17,511 | `(17511, 187, 1)` |

| Test       |  21,892 | `(21892, 187, 1)` |



\---



\## Data Preprocessing



The following steps were performed before model training:



1\. Loaded the ECG training and test datasets.

2\. Checked the dataset dimensions.

3\. Checked for missing values.

4\. Checked for duplicate rows.

5\. Separated the ECG signals from their class labels.

6\. Examined the class distribution.

7\. Visualized representative ECG signals from each class.

8\. Reshaped the signals for recurrent neural networks.



The final input format was:



```text

(samples, 187, 1)

```



where:



\* `samples` represents the number of heartbeat signals.

\* `187` represents the time steps in each ECG sequence.

\* `1` represents the signal feature at each time step.



\---



\## Models



\### 1. Simple RNN



A Simple RNN was implemented as the baseline sequential model.



```text

ECG Sequence

&#x20;    ↓

Simple RNN (64 units)

&#x20;    ↓

Dense (5 units)

&#x20;    ↓

Softmax

&#x20;    ↓

Heartbeat Class

```



The RNN processes the ECG signal sequentially while maintaining a hidden state containing information from previous time steps.



\### 2. LSTM



An LSTM was implemented to address the limitations of a plain RNN when learning long-term dependencies.



```text

ECG Sequence

&#x20;    ↓

LSTM (64 units)

&#x20;    ↓

Dense (5 units)

&#x20;    ↓

Softmax

&#x20;    ↓

Heartbeat Class

```



The LSTM uses gated memory to control which information should be retained, forgotten, and passed forward.



\---



\## Evaluation Metrics



Because the dataset is highly imbalanced, accuracy alone was not considered sufficient.



The models were evaluated using:



\* Accuracy

\* Macro Precision

\* Macro Recall

\* Macro F1-score

\* Classification Report

\* Confusion Matrix



Macro F1-score was especially important because it gives equal importance to all five heartbeat classes.



\---



\## Results



\### RNN vs LSTM



| Model      |   Accuracy | Macro Precision | Macro Recall |   Macro F1 |

| ---------- | ---------: | --------------: | -----------: | ---------: |

| Simple RNN |     82.80% |          29.00% |       20.18% |     18.49% |

| \*\*LSTM\*\*   | \*\*94.79%\*\* |      \*\*80.41%\*\* |   \*\*63.81%\*\* | \*\*68.47%\*\* |



The LSTM significantly outperformed the Simple RNN across all major evaluation metrics.



\---



\## RNN Performance



The Simple RNN achieved:



\* Accuracy: \*\*82.80%\*\*

\* Macro Precision: \*\*29.00%\*\*

\* Macro Recall: \*\*20.18%\*\*

\* Macro F1: \*\*18.49%\*\*



Although the accuracy appeared relatively high, the model performed poorly on minority heartbeat classes.



This demonstrates the effect of class imbalance: because the Normal class represents approximately 82.77% of the training data, a model can achieve high accuracy while still failing to recognize minority classes effectively.



\---



\## LSTM Performance



The LSTM achieved:



\* Accuracy: \*\*94.79%\*\*

\* Macro Precision: \*\*80.41%\*\*

\* Macro Recall: \*\*63.81%\*\*

\* Macro F1: \*\*68.47%\*\*



The LSTM demonstrated much stronger recognition of minority heartbeat categories compared with the Simple RNN.



\---



\## Key Findings



\* ECG signals are sequential time-series data, so temporal order is important.

\* A plain RNN can struggle to preserve information across many time steps because of the vanishing-gradient problem.

\* The Simple RNN strongly favored the majority Normal class.

\* Accuracy alone can be misleading on highly imbalanced datasets.

\* The LSTM achieved substantially better macro-averaged performance.

\* LSTM's gated memory helped the model learn more useful temporal patterns.

\* The large improvement in Macro F1 demonstrates that the LSTM was considerably better at handling the different heartbeat categories.



\---



\## Conclusion



The experiment demonstrated the importance of sequence-aware architectures for ECG heartbeat classification.



The Simple RNN achieved \*\*82.80% accuracy\*\* but only \*\*18.49% Macro F1\*\*, showing poor recognition of minority classes.



In comparison, the LSTM achieved \*\*94.79% accuracy\*\* and \*\*68.47% Macro F1\*\*. This substantial improvement demonstrates the advantage of LSTM's gated memory mechanism for learning temporal patterns in sequential ECG signals.



Overall, the results support the use of LSTM networks for sequential ECG classification and demonstrate why gated recurrent architectures can outperform plain RNNs when meaningful information exists across multiple time steps.



\---



\## Tools \& Technologies



\* Python

\* NumPy

\* Pandas

\* Matplotlib

\* Seaborn

\* Scikit-learn

\* TensorFlow / Keras

\* Jupyter Notebook / Google Colab

\* Git

\* GitHub



\---



\## Day 3 Outcome



\*\*Best Model: LSTM\*\*



\*\*Test Accuracy:\*\* 94.79%



\*\*Macro F1-score:\*\* 68.47%



The LSTM provided a clear improvement over the Simple RNN and demonstrated the value of order-aware architectures for sequential ECG data.




