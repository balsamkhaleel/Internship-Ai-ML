# \# Day 5 — Tuning, Evaluation \& Sprint Review

# 

# \[svg](https://github.com/balsamkhaleel/Internship-Ai-ML/tree/main/week6/day5#day-5--tuning-evaluation--sprint-review)

# 

# \## Overview

# 

# 

# 

# Systematically tuned and evaluated a neural network for cardiovascular disease classification using the TensorFlow/Keras Sequential API.

# 

# The main focus was hyperparameter tuning, Early Stopping, Model Checkpointing, model evaluation, and preparing the Sprint 1 review evidence.

# 

# \## Objectives

# 

# 

# \* Tune a neural network one variable at a time.

# \* Evaluate learning rate, architecture, dropout, and batch size.

# \* Use Validation F1-score as the primary tuning metric.

# \* Apply Early Stopping and ModelCheckpoint.

# \* Analyze training and validation curves.

# \* Evaluate the final model on unseen test data.

# \* Prepare evidence for Sprint Review and Retrospective.

# 

# \## Dataset

# 

# 

# The experiment uses the cleaned cardiovascular disease dataset.

# 

# \* \*\*Samples:\*\* 68,741

# \* \*\*Features:\*\* 11

# \* \*\*Target:\*\* `cardio`

# \* \*\*Task:\*\* Binary Classification

# 

# The `id` column was removed because it is only an identifier.

# 

# \## Data Preparation

# 

# 

# 

# The dataset was split using stratified sampling into:

# 

# \* 64% Training

# \* 16% Validation

# \* 20% Test

# 

# `StandardScaler` was fitted only on the training data and then applied to the validation and test sets to prevent data leakage.

# 

# \## Hyperparameter Tuning

# 

# 

# A one-variable-at-a-time strategy was used to evaluate:

# 

# \* Learning Rate

# \* Network Architecture

# \* Dropout Rate

# \* Batch Size

# 

# Validation F1-score was used as the primary metric for selecting the best configuration.

# 

# \### Best Configuration

# 

# | Hyperparameter |   Best Value |

# | -------------- | -----------: |

# | Learning Rate  |   \*\*0.0005\*\* |

# | Architecture   | \*\*(32, 16)\*\* |

# | Dropout        |      \*\*0.0\*\* |

# | Batch Size     |       \*\*32\*\* |

# 

# The best validation F1-score observed during tuning was approximately \*\*0.7248\*\*.

# 

# \## Callbacks

# 

# 

# \*\*EarlyStopping\*\* was used to stop training when validation loss stopped improving and restore the best model weights.

# 

# \*\*ModelCheckpoint\*\* was used to save the best-performing model during final training.

# 

# \## Results

# 

# 

# 

# The final neural network was evaluated using:

# 

# \* Accuracy

# \* Precision

# \* Recall

# \* F1-Score

# \* Confusion Matrix

# 

# Training and validation loss and accuracy curves were also analyzed to understand model learning behavior.

# 

# \## Key Findings

# 

# 

# 

# \* A learning rate of \*\*0.0005\*\* achieved the highest validation F1-score among the tested learning rates.

# \* The \*\*(32, 16)\*\* architecture achieved the best validation F1-score.

# \* Dropout did not improve the validation performance for the tested configurations.

# \* Batch size \*\*32\*\* achieved the highest validation F1-score among the tested batch sizes.

# \* EarlyStopping helped prevent unnecessary training.

# \* ModelCheckpoint preserved the best-performing final model.

# 

# \## Sprint Review \& Retrospective

# 

# 

# 

# The Sprint 1 results were documented using training curves, metric tables, model configuration, and final evaluation results.

# 

# The tuning process and model evaluation were reviewed as part of the Sprint Review and Retrospective.

# 

# \## Tools \& Technologies

# 

# 

# 

# \* Python

# \* TensorFlow / Keras

# \* Scikit-learn

# \* Pandas

# \* NumPy

# \* Matplotlib

# \* Seaborn

# \* Git \& GitHub

# \* Google Colab / Jupyter Notebook



