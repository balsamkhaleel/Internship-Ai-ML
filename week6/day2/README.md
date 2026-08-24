# Day 2 — Activations, Forward Propagation \& Loss



## Overview



Explored activation functions, forward propagation, and loss functions in neural networks. Visualized common activation functions, selected the appropriate output activation and loss function for the Cardiovascular Disease classification task, and implemented a small forward pass using NumPy.



## Topics Covered



* Why activation functions are important

* ReLU

* Sigmoid

* Tanh

* Softmax

* Activation function visualization

* Forward propagation

* Output activation selection

* Loss function selection

* Binary Cross-Entropy



## Dataset



* 68,742 samples

* 13 features

* Binary target: cardio

* cardio = 0: No cardiovascular disease

* cardio = 1: Cardiovascular disease



## Activation Functions



* Visualized ReLU, Sigmoid, and Tanh.

* ReLU outputs 0 for negative values and keeps positive values unchanged.

* Sigmoid maps values between 0 and 1.

* Tanh maps values between -1 and 1.

* Softmax is used for multi-class classification.



## Project Configuration



The Cardiovascular Disease task was identified as a binary classification problem.



* Hidden layer activation: **ReLU**

* Output activation: **Sigmoid**

* Loss function: **Binary Cross-Entropy**



## Forward Propagation



Implemented a small 2-layer neural network using NumPy.



* Input layer: 3 features

* Hidden layer: 2 neurons with ReLU

* Output layer: 1 neuron with Sigmoid

* Calculated weighted sums, activations, and final prediction.



## Results



* Predicted probability: **0.5681**

* Predicted class: **1**

* Binary Cross-Entropy loss: **0.5655**



## Key Takeaways



* Activation functions introduce non-linearity into neural networks.

* ReLU is commonly used in hidden layers.

* Sigmoid is suitable for binary classification output.

* Binary Cross-Entropy is appropriate for binary classification with Sigmoid.

* Forward propagation produces the model's prediction by passing data through the network.



## Tools



* Python

* NumPy

* Pandas

* Matplotlib

* Jupyter Notebook



