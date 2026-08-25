Day 3 — Backpropagation, Gradient Descent \& Optimizers

Overview



Explored the fundamental training process of neural networks using the cleaned cardiovascular disease dataset (cardio\_cleaned).



The notebook focused on understanding how a neural network learns through forward propagation, loss calculation, backpropagation, and weight updates.



Topics Covered

Neural network training loop

Forward pass and loss calculation

Gradient Descent

Learning Rate

Backpropagation

Chain Rule

Adam and SGD optimizers

Epochs and batches

Learning rate comparison

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

Key Takeaways

Gradient Descent updates model weights in the direction that reduces the loss.

The learning rate controls the size of weight updates.

Backpropagation calculates gradients using the Chain Rule.

Adam provides adaptive weight updates and is a strong default optimizer.

The choice of learning rate has a significant effect on training speed and stability.

Tools

Python

NumPy

Pandas

TensorFlow

Scikit-learn

Matplotlib

Google Colab

Git \& GitHub

