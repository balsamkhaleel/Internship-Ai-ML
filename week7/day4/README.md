\# Day 4 — Attention \& Transformers



\## Arabic Sentiment Analysis with MARBERT



\## Overview



This day focused on Attention mechanisms and Transformer-based architectures for Natural Language Processing (NLP).



The main objective was to understand how Transformers overcome the limitations of recurrent neural networks and to apply a pre-trained Transformer model to an Arabic sentiment classification task.



For the practical implementation, the \*\*MARBERT\*\* pre-trained Transformer was fine-tuned on the \*\*Arabic Sentiment Twitter Corpus\*\* for binary sentiment classification.



The workflow included:



\* Dataset exploration and analysis

\* Detection and removal of duplicate tweets

\* Identification and removal of train-test data leakage

\* Arabic text preprocessing

\* Train-validation splitting

\* MARBERT tokenization

\* PyTorch Dataset and DataLoader creation

\* MARBERT fine-tuning

\* Validation-based best model selection

\* Test set evaluation

\* Classification report

\* Confusion matrix analysis

\* Discussion of LSTM and Transformer architectures

\* Core model selection



\---



\## Learning Objectives



By the end of this day, we aimed to:



\* Explain the limitations of RNNs and LSTMs.

\* Understand the attention mechanism and self-attention.

\* Explain why Transformers can process sequences in parallel.

\* Understand the role of positional encoding.

\* Use a pre-trained Transformer from Hugging Face.

\* Fine-tune MARBERT for Arabic text classification.

\* Evaluate a Transformer model using standard classification metrics.



\---



\## 1. RNN Limitations



Traditional RNNs process sequences step by step, where each hidden state depends on the previous state.



Although LSTMs improve the ability of RNNs to capture long-term dependencies, they still process sequences sequentially. This limits parallelization during training and can make learning long-range relationships more difficult.



Transformers overcome this limitation by removing recurrence and using \*\*self-attention\*\*, allowing tokens to directly interact with other tokens in the sequence.



\### Key Advantages of Transformers



| Concept                  | Description                                                         |

| ------------------------ | ------------------------------------------------------------------- |

| Self-Attention           | Each token can attend to other tokens based on their relevance.     |

| Parallel Processing      | Sequence positions can be processed simultaneously during training. |

| Long-Range Context       | Distant tokens can directly influence each other.                   |

| Contextual Understanding | The representation of a token depends on the surrounding context.   |



\---



\## 2. Attention Mechanism



Attention allows a model to determine which parts of an input sequence are most relevant when processing a particular token.



\### Self-Attention



In self-attention, every token can interact with the other tokens in the same sequence.



This allows the model to capture relationships between words that may be far apart.



For example, when interpreting a word in a sentence, self-attention allows the model to consider other relevant words in the sentence rather than relying only on a sequential hidden state.



\---



\## 3. Transformer Architecture



A Transformer is built around attention mechanisms and feed-forward neural network layers.



Unlike RNNs, Transformers do not inherently process tokens according to their sequential order. Therefore, positional information is added through \*\*positional encoding\*\* or positional representations.



The main conceptual components include:



\* Self-attention

\* Multi-head attention

\* Feed-forward layers

\* Positional information

\* Residual connections

\* Layer normalization



For this project, the Transformer architecture was used through a pre-trained model rather than being implemented from scratch.



\---



\## 4. Pre-trained Transformers



Pre-trained Transformer models can be reused for specific NLP tasks through transfer learning.



Examples include:



\* BERT

\* DistilBERT

\* GPT-2

\* MARBERT



For this task, \*\*MARBERT\*\* was selected because it is designed for Arabic language understanding and is suitable for Arabic text containing dialectal and naturally occurring language.



\---



\# 5. Dataset



\## Arabic Sentiment Twitter Corpus



The dataset used in this notebook is the \*\*Arabic Sentiment Twitter Corpus\*\* from Hugging Face.



The task is binary sentiment classification with two classes:



\* `0` — Negative

\* `1` — Positive



\### Original Dataset



| Split    | Samples |

| -------- | ------: |

| Training |  47,000 |

| Test     |  11,751 |

| Total    |  58,751 |



The original label distributions were:



\### Training



| Label    |  Count |

| -------- | -----: |

| Negative | 23,121 |

| Positive | 23,879 |



\### Test



| Label    | Count |

| -------- | ----: |

| Negative | 5,781 |

| Positive | 5,970 |



\---



\# 6. Data Quality Analysis



Before training, the dataset was inspected for missing values, duplicate tweets, and overlap between the training and test sets.



\## Missing Values



No missing values were found in either the training or test datasets.



\## Duplicate Tweets



The original data contained duplicated tweets:



\* Training duplicates: \*\*16,638\*\*

\* Test duplicates: \*\*2,786\*\*



Duplicate tweets were removed from the training data.



After removing duplicates:



\* Original training samples: \*\*47,000\*\*

\* Clean training samples: \*\*30,362\*\*



\---



\# 7. Train-Test Data Leakage



A comparison between unique training and test tweets revealed that some tweets appeared in both datasets.



The analysis found:



\* Unique training tweets: \*\*30,362\*\*

\* Unique test tweets: \*\*8,965\*\*

\* Tweets appearing in both sets: \*\*2,605\*\*



To prevent data leakage, tweets appearing in the training set were removed from the test set.



After leakage removal:



\* Original test samples: \*\*11,751\*\*

\* Clean test samples: \*\*6,497\*\*

\* Removed overlapping test samples: \*\*5,254\*\*



This provides a more reliable evaluation because identical tweets are not shared between the training and test sets.



\---



\# 8. Clean Dataset



After duplicate removal and leakage prevention, the sentiment distributions were:



\### Training Data



| Sentiment |    Samples |

| --------- | ---------: |

| Negative  |     15,437 |

| Positive  |     14,925 |

| \*\*Total\*\* | \*\*30,362\*\* |



\### Test Data



| Sentiment |   Samples |

| --------- | --------: |

| Negative  |     3,361 |

| Positive  |     3,136 |

| \*\*Total\*\* | \*\*6,497\*\* |



The classes remained reasonably balanced after cleaning.



\---



\# 9. Tweet Length Analysis



Tweet lengths were analyzed before training.



\### Training Tweets



\* Mean length: \*\*56.44 characters\*\*

\* Median length: \*\*47 characters\*\*

\* Minimum: \*\*5 characters\*\*

\* Maximum: \*\*140 characters\*\*



\### Test Tweets



\* Mean length: \*\*53.91 characters\*\*

\* Median length: \*\*44 characters\*\*

\* Minimum: \*\*6 characters\*\*

\* Maximum: \*\*139 characters\*\*



The distribution showed that most tweets were relatively short, making a maximum Transformer sequence length of 128 tokens practical for this task.



\---



\# 10. Arabic Text Preprocessing



Light preprocessing was applied to preserve the natural linguistic characteristics of Arabic tweets.



The preprocessing steps were:



1\. Remove URLs.

2\. Remove Twitter mentions.

3\. Normalize extra whitespace.



Aggressive Arabic normalization was intentionally avoided because MARBERT is designed to handle naturally occurring Arabic text.



After preprocessing:



\* No missing cleaned tweets were found.

\* No empty tweets were found.



\---



\# 11. Train-Validation Split



The cleaned training data was divided into training and validation sets using a stratified split.



A validation size of \*\*15%\*\* was used.



| Split      | Samples |

| ---------- | ------: |

| Training   |  25,807 |

| Validation |   4,555 |

| Test       |   6,497 |



Stratification was used to preserve the sentiment class distribution across the training and validation sets.



\---



\# 12. MARBERT Tokenization



The pre-trained tokenizer associated with:



`UBC-NLP/MARBERT`



was used to convert Arabic tweets into numerical representations.



The tokenizer produces:



\* `input\_ids`

\* `attention\_mask`



A maximum sequence length of:



```text

128 tokens

```



was used.



Sequences longer than the maximum length were truncated, while shorter sequences were padded.



\---



\# 13. PyTorch Dataset and DataLoader



A custom PyTorch `Dataset` was created to store:



\* Input IDs

\* Attention masks

\* Sentiment labels



The DataLoaders were configured with a batch size of \*\*16\*\*.



| Data       | Samples | Batches |

| ---------- | ------: | ------: |

| Training   |  25,807 |   1,613 |

| Validation |   4,555 |     285 |

| Test       |   6,497 |     407 |



Training batches were shuffled, while validation and test batches were kept in a fixed order.



\---



\# 14. MARBERT Model



The model was loaded using Hugging Face's `AutoModelForSequenceClassification`.



Configuration:



```text

Model: UBC-NLP/MARBERT

Task: Binary Classification

Number of Labels: 2

Device: CUDA

GPU: Tesla T4

```



MARBERT was fine-tuned directly for the sentiment classification task.



\---



\# 15. Training Configuration



The following hyperparameters were used:



| Hyperparameter          |  Value |

| ----------------------- | -----: |

| Learning Rate           | `2e-5` |

| Weight Decay            | `0.01` |

| Epochs                  |    `5` |

| Batch Size              |   `16` |

| Maximum Sequence Length |  `128` |

| Number of Labels        |    `2` |



AdamW was used as the optimizer.



\---



\# 16. Fine-Tuning Results



MARBERT was fine-tuned for five epochs.



| Epoch | Train Loss | Validation Loss | Validation Accuracy | Validation Macro F1 |

| ----- | ---------: | --------------: | ------------------: | ------------------: |

| 1     |     0.1948 |          0.1446 |              93.96% |              93.96% |

| 2     |     0.1306 |          0.1566 |          \*\*94.18%\*\* |          \*\*94.18%\*\* |

| 3     |     0.0705 |          0.2126 |              93.63% |              93.62% |

| 4     |     0.0322 |          0.2833 |              93.30% |              93.30% |

| 5     |     0.0186 |          0.2961 |              92.49% |              92.49% |



The best validation Macro F1 was achieved at \*\*Epoch 2\*\*:



```text

Best Validation Macro F1: 94.18%

```



After Epoch 2, training loss continued to decrease while validation loss increased and validation performance declined. This indicates that the model began to \*\*overfit\*\* the training data.



The best model weights were therefore selected based on the highest validation Macro F1.



\---



\# 17. Test Evaluation



The best-performing model from Epoch 2 was evaluated on the cleaned and leakage-free test set.



\### Final Test Results



| Metric    |      Score |

| --------- | ---------: |

| Accuracy  | \*\*94.00%\*\* |

| Precision | \*\*94.07%\*\* |

| Recall    | \*\*93.94%\*\* |

| Macro F1  | \*\*93.98%\*\* |



The model achieved a Macro F1 of \*\*93.98%\*\*, demonstrating strong and balanced performance across both sentiment classes.



\---



\# 18. Classification Report



| Class             | Precision |   Recall | F1-Score |   Support |

| ----------------- | --------: | -------: | -------: | --------: |

| Negative          |      0.93 |     0.96 |     0.94 |     3,361 |

| Positive          |      0.95 |     0.92 |     0.94 |     3,136 |

| \*\*Macro Average\*\* |  \*\*0.94\*\* | \*\*0.94\*\* | \*\*0.94\*\* | \*\*6,497\*\* |



The results show that MARBERT performs well on both negative and positive sentiment classes.



\---



\# 19. Confusion Matrix



A confusion matrix was used to visualize the model's classification performance.



The matrix provides information about:



\* True Negative predictions

\* False Positive predictions

\* False Negative predictions

\* True Positive predictions



The visualization was generated using a blue color map for easier interpretation.



\---



\# 20. LSTM vs. MARBERT



The LSTM model from Day 3 and the MARBERT Transformer from Day 4 were trained on different datasets and addressed different tasks.



The LSTM was applied to \*\*sequential ECG data\*\*, while MARBERT was applied to \*\*Arabic sentiment classification\*\*.



Therefore, their evaluation metrics should \*\*not be directly compared\*\*, because the datasets, input types, and classification tasks are different.



\### Day 3 — LSTM



| Metric        |  Score |

| ------------- | -----: |

| Test Accuracy | 94.79% |

| Macro F1      | 68.47% |



\### Day 4 — MARBERT



| Metric        |  Score |

| ------------- | -----: |

| Test Accuracy | 94.00% |

| Macro F1      | 93.98% |



The results demonstrate that different architectures are suitable for different types of sequential data.



LSTM is well suited for sequential signals such as ECG data, where temporal order is important. MARBERT is designed for natural language and uses self-attention to capture contextual relationships between words.



\---



\# 21. Core Model Selection



For the Arabic sentiment classification task, \*\*MARBERT\*\* was selected as the core model.



The main reasons are:



\* It is a Transformer-based architecture.

\* It is specifically designed for Arabic language understanding.

\* It can capture contextual relationships using self-attention.

\* It achieved strong performance on the Arabic sentiment test set.

\* It achieved a test Accuracy of \*\*94.00%\*\*.

\* It achieved a Macro F1-score of \*\*93.98%\*\*.



Therefore, MARBERT is the most appropriate core architecture for the Arabic text classification task explored in this day.



\---



\# 22. Conclusion



This day introduced Attention and Transformer architectures as alternatives to recurrent neural networks.



A pre-trained MARBERT model was fine-tuned for Arabic sentiment classification using Hugging Face Transformers and PyTorch.



The final model achieved:



```text

Test Accuracy: 94.00%

Test Precision: 94.07%

Test Recall: 93.94%

Test Macro F1: 93.98%

```



The best validation performance was achieved at \*\*Epoch 2\*\*, after which the model showed signs of overfitting.



Overall, the experiment demonstrated the effectiveness of Transformer-based architectures for Arabic NLP tasks and highlighted the advantages of self-attention in capturing contextual relationships within text.



MARBERT was therefore selected as the core model for the Arabic sentiment classification task.



