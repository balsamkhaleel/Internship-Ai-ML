<<<<<<< HEAD
\# Day 3 — Backpropagation, Gradient Descent \& Optimizers
=======
# Day 3 — Backpropagation, Gradient Descent \& Optimizers

Overview
>>>>>>> 92eb668cdf50f4edc50b4995466abda0c4efa21b



\## Overview



Explored the fundamental training process of neural networks using the cleaned cardiovascular disease dataset (`cardio\_cleaned`).



<<<<<<< HEAD
The notebook focused on understanding how a neural network learns through forward propagation, loss calculation, backpropagation, gradient descent, and weight updates.
=======
## Learning Objectives

- Understand the neural network training loop.

- Explain Gradient Descent and Learning Rate.

- Understand Backpropagation and the Chain Rule.

- Identify common optimizers such as Adam and SGD.

- Understand epochs and batches.

- Compare different learning rates using loss curves.

## Practical Work

- Prepared the cardio\_cleaned dataset for neural network training.

- Built a small feed-forward neural network for binary classification.

- Trained the model using the Adam optimizer.

- Compared three learning rates:

   - 0.1

   - 0.001

   - 0.00001

- Visualized training and validation loss curves.

- Evaluated the final model using Accuracy, Precision, Recall, F1 Score, and Confusion Matrix.

## Key Concepts

### Training Loop
>>>>>>> 92eb668cdf50f4edc50b4995466abda0c4efa21b



The practical work also included learning rate experiments, optimizer comparison, model improvement, callbacks, and final model evaluation.



\## Learning Objectives



\* Understand the neural network training loop.

\* Explain Gradient Descent and Learning Rate.

\* Understand Backpropagation and the Chain Rule.

\* Understand how TensorFlow calculates gradients using `GradientTape`.

\* Identify and compare common optimizers such as Adam and SGD.

\* Understand epochs and batches.

\* Analyze the effect of different learning rates.

\* Build and improve a neural network using TensorFlow/Keras.

\* Evaluate a classification model using multiple metrics.



\## Practical Work



\* Prepared the `cardio\_cleaned` dataset for neural network training.

\* Standardized the input features using `StandardScaler`.

\* Built a baseline feed-forward neural network for binary classification.

\* Trained the baseline model using the Adam optimizer.

\* Compared three learning rates:



&#x20; \* `0.1`

&#x20; \* `0.001`

&#x20; \* `0.00001`

\* Visualized training and validation loss curves for the different learning rates.

\* Compared Adam and SGD optimizers.

\* Demonstrated Backpropagation using TensorFlow's `GradientTape`.

\* Built an improved neural network using Batch Normalization and Dropout.

\* Used EarlyStopping to prevent unnecessary training.

\* Used ModelCheckpoint to save the best model.

\* Evaluated the final model using Accuracy, Precision, Recall, F1 Score, and Confusion Matrix.



\## Key Concepts



\### Training Loop



The neural network training process follows four main steps:



```text

Forward Pass → Loss → Backpropagation → Weight Update

```


<<<<<<< HEAD

This process is repeated across batches and epochs to minimize the loss.



\### Gradient Descent
=======
### Gradient Descent
>>>>>>> 92eb668cdf50f4edc50b4995466abda0c4efa21b



Gradient Descent updates the model weights in the direction that reduces the loss.



<<<<<<< HEAD
The gradient indicates how the loss changes with respect to each model parameter.



\### Learning Rate
=======
### Learning Rate
>>>>>>> 92eb668cdf50f4edc50b4995466abda0c4efa21b



The Learning Rate controls the size of each weight update and affects training speed and stability.



<<<<<<< HEAD
Three learning rates were tested:



| Learning Rate | Behavior                              |

| ------------- | ------------------------------------- |

| `0.00001`     | Slow but stable convergence           |

| `0.001`       | Smooth and stable convergence         |

| `0.1`         | Unstable with noticeable fluctuations |



The learning rate `0.001` provided the most stable behavior among the tested values.



\### Backpropagation
=======
### Backpropagation
>>>>>>> 92eb668cdf50f4edc50b4995466abda0c4efa21b



Backpropagation calculates the gradients of the loss with respect to the model's weights using the Chain Rule.



<<<<<<< HEAD
TensorFlow's `GradientTape` was used to demonstrate this process.
=======
### Optimizers
>>>>>>> 92eb668cdf50f4edc50b4995466abda0c4efa21b



The calculated gradient shapes corresponded to all trainable parameters in the network.



<<<<<<< HEAD
\### Optimizers
=======
## Key Takeaways
>>>>>>> 92eb668cdf50f4edc50b4995466abda0c4efa21b



Adam and SGD were compared during training.



<<<<<<< HEAD
Adam showed a gradual decrease in validation loss, while SGD showed smaller improvement followed by relatively stable behavior with minor fluctuations.



The experiment demonstrated how optimizer choice can affect convergence and training behavior.



\### Batch Normalization and Dropout



The improved model used Batch Normalization to stabilize activations and Dropout to reduce the risk of overfitting.



The improved architecture was:



```text

Input

&#x20; ↓

Dense(32)

&#x20; ↓

BatchNormalization

&#x20; ↓

ReLU

&#x20; ↓

Dropout(0.3)

&#x20; ↓

Dense(16)

&#x20; ↓

BatchNormalization

&#x20; ↓

ReLU

&#x20; ↓

Dropout(0.2)

&#x20; ↓

Dense(1, Sigmoid)

```



\### EarlyStopping and ModelCheckpoint



EarlyStopping monitored validation loss and restored the best model weights.



The best validation performance occurred at:



```text

Best Epoch: 14

Best Validation Loss: 0.5411

Best Validation Accuracy: 73.85%

```



Training stopped at approximately epoch 19 because the validation loss stopped improving.



ModelCheckpoint was also used to save the best-performing model.



\## Final Results



The final model was evaluated on the unseen test set.



| Metric    |      Score |

| --------- | ---------: |

| Accuracy  | \*\*73.36%\*\* |

| Precision | \*\*74.89%\*\* |

| Recall    | \*\*69.46%\*\* |

| F1 Score  | \*\*72.07%\*\* |



The results show that the model achieved balanced performance across multiple evaluation metrics, with Precision higher than Recall.



\## Key Takeaways



\* Gradient Descent minimizes the loss by updating model weights.

\* The Learning Rate controls the size of weight updates.

\* A very high learning rate can cause unstable training.

\* A very low learning rate can result in slow convergence.

\* A learning rate of `0.001` provided the most stable behavior in the experiment.

\* Backpropagation calculates gradients using the Chain Rule.

\* TensorFlow's `GradientTape` can automatically calculate these gradients.

\* Adam showed more consistent optimization progress than SGD in the experiment.

\* Batch Normalization and Dropout were used to improve the network architecture.

\* EarlyStopping prevented unnecessary training when validation performance stopped improving.

\* Multiple evaluation metrics provide a more complete view of model performance than accuracy alone.



\## Tools



\* Python

\* NumPy

\* Pandas

\* TensorFlow / Keras

\* Scikit-learn

\* Matplotlib

\* Google Colab


=======
## Tools

 Python

- NumPy

- Pandas

- TensorFlow

- Scikit-learn

- Matplotlib

- Google Colab

- Git \& GitHub
>>>>>>> 92eb668cdf50f4edc50b4995466abda0c4efa21b

