Day 3 — Backpropagation, Gradient Descent \& Optimizers

Overview



Explored the fundamental training process of neural networks using the cleaned cardiovascular disease dataset (cardio\_cleaned).



The notebook focused on understanding how a neural network learns through forward propagation, loss calculation, backpropagation, and weight updates.



Learning Objectives

Understand the neural network training loop.

Explain Gradient Descent and Learning Rate.

Understand Backpropagation and the Chain Rule.

Identify common optimizers such as Adam and SGD.

Understand epochs and batches.

Compare different learning rates using loss curves.

Practical Work

Prepared the cardio\_cleaned dataset for neural network training.

Built a small feed-forward neural network for binary classification.

Trained the model using the Adam optimizer.

Compared three learning rates:

0.1

0.001

0.00001

Visualized training and validation loss curves.

Evaluated the final model using Accuracy, Precision, Recall, F1 Score, and Confusion Matrix.

Key Concepts

Training Loop



Forward Pass → Loss → Backpropagation → Weight Update



Gradient Descent



Gradient Descent updates the model weights in the direction that reduces the loss.



Learning Rate



The Learning Rate controls the size of each weight update and affects training speed and stability.



Backpropagation



Backpropagation calculates the gradients of the loss with respect to the model's weights using the Chain Rule.



Optimizers



Adam was used as the main optimizer, while SGD was discussed as a basic alternative.



Key Takeaways

Gradient Descent minimizes the loss by updating model weights.

The Learning Rate controls the size of weight updates.

Backpropagation calculates gradients using the Chain Rule.

Adam provides adaptive weight updates and is a strong default optimizer.

Learning Rate selection affects training speed and stability.

Tools

Python

NumPy

Pandas

TensorFlow

Scikit-learn

Matplotlib

Google Colab

Git \& GitHub

