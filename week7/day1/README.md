# Day 1 — Sprint 2 Planning & Convolutional Neural Networks

## Overview

Introduced Sprint 2 planning and the fundamental concepts of Convolutional Neural Networks (CNNs). The session focused on understanding why Dense Neural Networks are not efficient for image data and how convolutional filters detect visual patterns and generate feature maps.

A hands-on convolution experiment was performed using a small sample of the **Melanoma Skin Cancer Dataset — Benign vs Malignant**.

## Sprint 2 Planning

### Sprint 2 Goal

The goal of Sprint 2 is to improve the cardiovascular disease prediction model by engineering relevant features, tuning the neural network hyperparameters, and optimizing the decision threshold to improve the model's overall performance, with a focus on the F1-score and the balance between Precision and Recall.

### Sprint 2 Backlog

| Task                            | Description                                                                                                                                                                      |
| ------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Feature Engineering             | Create and evaluate additional meaningful features from the existing cardiovascular dataset to improve the model's ability to capture relevant patterns.                         |
| Hyperparameter Tuning           | Experiment with different neural network architectures, dropout rates, and batch sizes to identify a suitable model configuration.                                               |
| Decision Threshold Optimization | Evaluate different classification thresholds using the validation set to find a threshold that provides a better balance between Precision and Recall and improves the F1-score. |
| Final Model Evaluation          | Evaluate the final model configuration using the selected evaluation metrics and compare its performance with the baseline model.                                                |
| Model Documentation             | Document the experiments, results, decisions, and limitations of the final model.                                                                                                |

### Sprint 1 Retrospective Improvement

The main improvement carried forward from Sprint 1 is to focus on improving the model through systematic experimentation rather than relying only on the baseline configuration.

In Sprint 2, the model will be improved through feature engineering and hyperparameter tuning, followed by decision threshold optimization using the validation set to achieve a better balance between Precision and Recall and improve the F1-score.

### Core Model

The core model for the cardiovascular disease prediction task is a **Dense Neural Network (MLP)** because the dataset consists of structured tabular data.

The Sprint 2 work will build on the Dense Neural Network developed during Week 6. The model will be further improved through feature engineering, hyperparameter tuning, and decision threshold optimization rather than starting the modeling process from scratch.

---

## CNN Hands-On

### Dataset

The hands-on experiment uses the **Melanoma Skin Cancer Dataset — Benign vs Malignant**.

The dataset contains two image classes:

* **Benign**

* **Malignant**

For the convolution experiment, a small balanced sample of **10 images** was selected:

* 5 Benign images

* 5 Malignant images

The sample was used for demonstration and visualization rather than model training.

## Why Dense Networks Fail on Images

Images contain spatial relationships between neighboring pixels. Flattening an image and feeding it directly into a Dense Network removes much of this spatial structure and can result in a very large number of parameters.

For example, a 200 × 200 RGB image contains:

**200 × 200 × 3 = 120,000 pixel values.**

If these 120,000 inputs are connected to 1,000 neurons in a Dense layer, the layer would require approximately:

**120,000 × 1,000 = 120,000,000 weights.**

This demonstrates why Dense Networks can become computationally expensive when working directly with image data.

## Image Inspection

The selected images were loaded and inspected before applying convolution.

All sample images had the same resolution:

The images had a resolution of **224 × 224 pixels**.

Each image was originally represented as an RGB image with three color channels:

**224 × 224 × 3**

A sample image was then converted to grayscale for the convolution experiment, resulting in a single-channel image with dimensions **224 × 224 pixels**.

## Convolution Filter

A hand-defined 3 × 3 edge-detection filter was used:

```text
[-1  0  1]

[-1  0  1]

[-1  0  1]
```

This filter is designed to highlight vertical edges by detecting changes in pixel intensity from left to right.

## Convolution and Feature Map

The filter was applied to the grayscale image using a convolution operation.

The filter slides across the image and performs a weighted sum of local pixel values at each position.

The result is a **feature map** that highlights areas where the detected pattern occurs.

The resulting feature map maintained the same spatial dimensions of **224 × 224 pixels** because `SAME` padding was used with a stride of 1.

## Parameter Sharing

CNNs use the same convolutional filter across different regions of an image. Therefore, the same learnable weights are reused at every spatial location.

**For a 3 × 3 filter:**

A 3 × 3 filter contains **9 weights**, plus a bias if used.

In comparison, a Dense Network requires a separate weight for every connection between the input and neurons.

Parameter sharing significantly reduces the number of parameters and allows the same visual pattern to be detected at different locations.

## Translation Invariance

Because convolutional filters move across the entire image, the same visual pattern can be detected at different spatial locations.

For example, an edge or texture can be recognized whether it appears on the left, right, top, or bottom of an image.

## Feature Hierarchy

CNNs learn visual features progressively through different layers.

```text
Edges

 ↓

Textures

 ↓

Shapes

 ↓

Complex Features

 ↓

Objects / Structures
```

Early layers learn simple patterns such as edges and lines. Middle layers combine these patterns into shapes and textures, while deeper layers learn more complex representations.

## Conclusion

The hands-on experiment demonstrated the basic operation of convolution using real Melanoma skin lesion images.

A manually defined edge-detection filter was applied to grayscale images to generate feature maps. The experiment demonstrated how CNNs use local connectivity, parameter sharing, and convolution to efficiently detect visual patterns in image data.
