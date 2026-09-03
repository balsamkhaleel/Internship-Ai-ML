# Day 4 — Attention & Transformers

## Overview

This day focused on **Attention, Self-Attention, and Transformer architectures** as an alternative to traditional recurrent neural networks.

The practical task was **Arabic sentiment classification** using the pre-trained **MARBERT** model from Hugging Face.

---

## Learning Objectives

* Understand the limitations of RNNs.
* Understand the Attention and Self-Attention mechanisms.
* Learn how Transformers process sequences.
* Understand the role of Positional Encoding.
* Use a pre-trained Transformer model.
* Fine-tune MARBERT for Arabic sentiment classification.
* Evaluate and select the best-performing model.

---

## RNN Limitations

RNNs process sequences step by step, which makes training slower and limits parallelization. They can also struggle to preserve information over long sequences because of problems such as **vanishing gradients**.

Transformers overcome these limitations using **Self-Attention**, which allows the model to consider relationships between different words in a sequence at the same time.

---

## Attention & Self-Attention

The Attention mechanism allows the model to focus on the most relevant parts of the input when producing an output.

**Self-Attention** calculates relationships between tokens within the same sequence. This allows the model to understand which words are related to each other, even when they are far apart.

Unlike RNNs, Transformers can process the tokens in parallel, making training more efficient.

---

## Transformer Architecture

The main ideas covered were:

* **Self-Attention** — captures relationships between tokens.
* **Multi-Head Attention** — allows the model to learn different types of relationships.
* **Feed-Forward Network** — processes the representations produced by attention.
* **Positional Encoding** — provides information about the position of tokens.
* **Layer Normalization & Residual Connections** — improve training stability.

---

## Dataset

The project used the **Arabic Sentiment Twitter Corpus** from Hugging Face.

Original dataset:

* Training samples: **47,000**
* Test samples: **11,751**
* Classes: **Negative / Positive**

### Data Cleaning

The dataset was cleaned before training by:

* Removing duplicate tweets.
* Removing tweets that appeared in both training and test sets.
* Removing URLs and Twitter mentions.
* Normalizing whitespace.
* Checking for missing and empty texts.

After cleaning:

| Dataset  | Samples |
| -------- | ------: |
| Training |  30,362 |
| Test     |   6,497 |

The training data was further divided into:

* Training: **25,807**
* Validation: **4,555**
* Test: **6,497**

---

## Tokenization

The **MARBERT tokenizer** was used to convert Arabic tweets into token IDs.

Configuration:

* Maximum sequence length: **128**
* Padding: `max_length`
* Truncation: enabled

A custom PyTorch Dataset and DataLoader were used for model training.

---

## MARBERT Model

The pre-trained **UBC-NLP/MARBERT** model was fine-tuned for binary sentiment classification.

### Training Configuration

| Parameter     | Value           |
| ------------- | --------------- |
| Model         | MARBERT         |
| Learning Rate | `2e-5`          |
| Weight Decay  | `0.01`          |
| Batch Size    | `16`            |
| Epochs        | `5`             |
| Device        | CUDA — Tesla T4 |

The best model was selected based on **Validation Macro F1**.

---

## Training Results

| Epoch | Val Accuracy | Val Macro F1 |
| ----: | -----------: | -----------: |
|     1 |       93.96% |       93.96% |
| **2** |   **94.18%** |   **94.18%** |
|     3 |       93.63% |       93.62% |
|     4 |       93.30% |       93.30% |
|     5 |       92.49% |       92.49% |

The best performance was achieved at **Epoch 2**.

After Epoch 2, the training loss continued to decrease while validation performance declined. This indicates that the model started to **overfit** the training data.

---

## Test Evaluation

The best model was evaluated on the unseen test set.

| Metric    |      Score |
| --------- | ---------: |
| Accuracy  | **94.00%** |
| Precision | **94.07%** |
| Recall    | **93.94%** |
| Macro F1  | **93.98%** |

The classification report showed balanced performance between the negative and positive sentiment classes.

A **confusion matrix** was also used to visualize the model's correct and incorrect predictions.

---

## LSTM vs MARBERT

The LSTM model from **Day 3** and MARBERT from **Day 4** were applied to different datasets and tasks.

* LSTM → sequential ECG data.
* MARBERT → Arabic text sentiment classification.

Therefore, their performance metrics should **not be directly compared**. Each architecture was evaluated according to the requirements of its own task.

---

## Core Model Selection

For the Arabic sentiment classification task, **MARBERT** was selected as the core model.

It was chosen because it is designed for Arabic language understanding and achieved strong and balanced results:

**94.00% Accuracy**
**93.98% Macro F1**

Its Self-Attention mechanism also allows it to capture contextual relationships between words effectively.

---

## Conclusion

This day demonstrated how **Transformers and Self-Attention** can overcome important limitations of recurrent architectures.

A pre-trained MARBERT model was successfully fine-tuned for Arabic sentiment classification and achieved **94.00% test accuracy** and **93.98% Macro F1**.

The validation results also demonstrated the importance of monitoring model performance and selecting the best checkpoint to reduce the effect of overfitting.
