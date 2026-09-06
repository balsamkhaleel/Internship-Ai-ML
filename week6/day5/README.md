# Day 5 — Neural Network

## Overview

Built and evaluated a neural network for cardiovascular disease classification using the TensorFlow/Keras Sequential API, using the original features with no hyperparameter tuning and no feature engineering.

## Objectives

* Load the cleaned dataset and split it into train / validation / test sets.
* Scale the features.
* Build and train a simple neural network.
* Use EarlyStopping to prevent unnecessary training and overfitting.
* Plot training and validation loss/accuracy curves.
* Evaluate the model on the validation and test sets using Accuracy, Precision, Recall, and F1-score.
* Visualize the results with a confusion matrix.

## Dataset

The experiment uses the cleaned cardiovascular disease dataset.

* **Samples:** 68,741
* **Original Features:** 11
* **Target:** `cardio`
* **Task:** Binary Classification

The `id` column was removed because it is only an identifier.

## Data Preparation

The dataset was split using stratified sampling into:

* 64% Training
* 16% Validation
* 20% Test

StandardScaler was applied to the features, fitted only on the training data to prevent data leakage.

## Model Architecture

A simple Sequential neural network was built with the original (non-engineered) features:

* Dense(32, activation="relu")
* Dense(16, activation="relu")
* Dense(1, activation="sigmoid")

Compiled with the Adam optimizer (learning rate = 0.001) and binary cross-entropy loss. No hyperparameter tuning was performed.

## Callbacks

**EarlyStopping** was used to stop training when validation loss stopped improving and restore the best model weights.

## Results

The neural network achieved the following performance:

| **Metric** | **Validation** |   **Test** |
| ---------- | --------------: | ---------: |
| Accuracy   |      **73.25%** | **73.27%** |
| Precision  |      **74.48%** | **74.40%** |
| Recall     |      **69.91%** | **70.12%** |
| F1-Score   |      **72.12%** | **72.20%** |

## Key Findings

* A simple neural network with no tuning and no feature engineering achieved a **72.12% F1-score** on validation and **72.20% F1-score** on the unseen test set.
* Validation and test performance were very close across all metrics, indicating the model generalized consistently.
* Training and validation loss/accuracy curves were plotted to check for overfitting.
* A confusion matrix was used to visualize correct and incorrect predictions.

## Tools & Technologies

* Python
* TensorFlow / Keras
* Scikit-learn
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Git & GitHub
* Google Colab / Jupyter Notebook