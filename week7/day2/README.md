\# Day 2 — Building CNNs \& Transfer Learning



\## Overview



This session focused on building complete Convolutional Neural Networks (CNNs) for image classification and understanding how different approaches affect model performance.



The hands-on experiment used the \*\*Melanoma Skin Cancer Dataset — Benign vs Malignant\*\* to classify skin lesion images into two classes.



Three approaches were implemented and compared:



\* CNN trained from scratch

\* CNN with Data Augmentation

\* Transfer Learning using a pre-trained MobileNetV2 model



The main goal was to understand how pooling, full CNN architectures, data augmentation, and transfer learning can be applied to image classification tasks.



\---



\## Dataset



The hands-on experiment uses the \*\*Melanoma Skin Cancer Dataset — Benign vs Malignant\*\*.



The dataset contains two image classes:



\* \*\*Benign\*\*

\* \*\*Malignant\*\*



\### Dataset Distribution



| \*\*Dataset\*\* | \*\*Benign\*\* | \*\*Malignant\*\* | \*\*Total\*\* |

| ----------- | ---------: | ------------: | --------: |

| Train       |      6,289 |         5,590 |    11,879 |

| Test        |      1,000 |         1,000 |     2,000 |



The training dataset was divided into:



\* \*\*80% Training\*\*

\* \*\*20% Validation\*\*



The test dataset was kept separate and was used only for final evaluation.



\### Image Information



All images have the same characteristics:



\* \*\*Format:\*\* JPEG

\* \*\*Resolution:\*\* 224 × 224 pixels

\* \*\*Color Mode:\*\* RGB

\* \*\*Input Shape:\*\* 224 × 224 × 3

\* \*\*Number of Classes:\*\* 2



\---



\## Data Loading and Preprocessing



The dataset was loaded using TensorFlow/Keras image dataset utilities.



The images were automatically resized to \*\*224 × 224 pixels\*\* and converted to floating-point values.



Pixel values were normalized to the range:



```text

0.0 → 1.0

```



A batch inspection confirmed the following shapes:



```text

Image Shape: (32, 224, 224, 3)

Label Shape: (32, 1)

```



The binary labels correspond to the two classes:



```text

0 → Benign

1 → Malignant

```



\---



\# Full CNN Architecture



\## CNN From Scratch



A complete CNN was built from scratch using convolutional layers, max pooling, flattening, and dense layers.



The architecture consists of:



```text

Input Image

&#x20;    ↓

Conv2D (32 filters)

&#x20;    ↓

MaxPooling2D

&#x20;    ↓

Conv2D (64 filters)

&#x20;    ↓

MaxPooling2D

&#x20;    ↓

Flatten

&#x20;    ↓

Dense (64 neurons)

&#x20;    ↓

Sigmoid

&#x20;    ↓

Benign / Malignant

```



\### Convolutional Layers



The first convolutional layer uses:



\* \*\*32 filters\*\*

\* \*\*3 × 3 kernel\*\*

\* \*\*ReLU activation\*\*



The second convolutional layer uses:



\* \*\*64 filters\*\*

\* \*\*3 × 3 kernel\*\*

\* \*\*ReLU activation\*\*



The convolutional layers learn visual features from the skin lesion images.



\---



\## Pooling



Max Pooling was used after each convolutional layer.



A \*\*2 × 2 MaxPooling\*\* operation reduces the spatial dimensions of the feature maps while keeping the strongest activations.



The main benefits of pooling are:



\* Reduce computational cost

\* Reduce the spatial size of feature maps

\* Retain important visual information

\* Improve robustness to small changes in image position



The CNN therefore follows the pattern:



```text

Convolution

&#x20;    ↓

Pooling

&#x20;    ↓

Convolution

&#x20;    ↓

Pooling

```



\---



\## Flatten and Dense Layers



After the convolution and pooling operations, the resulting feature maps are flattened into a one-dimensional vector.



The flattened features are then passed to:



```text

Flatten

&#x20;  ↓

Dense(64, ReLU)

&#x20;  ↓

Dense(1, Sigmoid)

```



Because this is a binary classification problem, a single output neuron with a \*\*Sigmoid\*\* activation function is used.



The output represents the probability of belonging to one of the two classes.



\---



\# CNN Baseline Results



The CNN trained from scratch achieved the following results:



| \*\*Metric\*\*    |         \*\*Result\*\* |

| ------------- | -----------------: |

| Test Accuracy |         \*\*84.50%\*\* |

| Test Loss     |         \*\*0.3688\*\* |

| Training Time | \*\*215.54 seconds\*\* |



This baseline demonstrates that a CNN can learn useful visual features directly from the skin lesion dataset without using a pre-trained model.



\---



\# Data Augmentation



\## Purpose of Data Augmentation



Image datasets can contain limited variations of the same visual patterns, which may cause a CNN to overfit the training data.



Data augmentation increases the variety of training examples by applying random transformations to the images.



The following transformations were used:



\* Random Horizontal Flip

\* Random Rotation

\* Random Zoom



The augmentation process can be represented as:



```text

Original Image

&#x20;     ↓

Random Flip

&#x20;     ↓

Random Rotation

&#x20;     ↓

Random Zoom

&#x20;     ↓

Augmented Image

```



The transformations are applied during training, while the validation and test images remain unchanged.



\---



\## CNN with Data Augmentation



The same CNN architecture was used with the addition of the augmentation layers at the beginning of the model.



```text

Input Image

&#x20;    ↓

Data Augmentation

&#x20;    ↓

Conv2D (32 filters)

&#x20;    ↓

MaxPooling2D

&#x20;    ↓

Conv2D (64 filters)

&#x20;    ↓

MaxPooling2D

&#x20;    ↓

Flatten

&#x20;    ↓

Dense (64)

&#x20;    ↓

Sigmoid

&#x20;    ↓

Benign / Malignant

```



\---



\## Data Augmentation Results



The augmented CNN achieved:



| \*\*Metric\*\*    |         \*\*Result\*\* |

| ------------- | -----------------: |

| Test Accuracy |         \*\*86.10%\*\* |

| Test Loss     |         \*\*0.3296\*\* |

| Training Time | \*\*241.04 seconds\*\* |



Compared with the baseline CNN, the test accuracy improved from:



```text

84.50%

&#x20;  ↓

86.10%

```



This represents an improvement of \*\*1.60 percentage points\*\*.



The test loss also decreased from \*\*0.3688\*\* to \*\*0.3296\*\*.



The training time increased because additional image transformations were performed during training.



\---



\# Transfer Learning



\## MobileNetV2



Training a deep CNN completely from scratch can require a large amount of data and computational resources.



Transfer learning allows a model to reuse visual features learned from a large pre-trained dataset.



For this experiment, \*\*MobileNetV2\*\* with pre-trained \*\*ImageNet\*\* weights was used.



The original ImageNet classification head was removed and replaced with a new classification layer for the two skin lesion classes.



\---



\## Freezing the Pre-trained Model



Initially, the MobileNetV2 base model was frozen:



```text

base\_model.trainable = False

```



MobileNetV2 contains \*\*154 layers\*\*, which were kept frozen during the initial transfer learning stage.



The architecture was:



```text

Input Image

&#x20;     ↓

MobileNetV2

(Frozen Pre-trained Features)

&#x20;     ↓

Flatten

&#x20;     ↓

Dense(1, Sigmoid)

&#x20;     ↓

Benign / Malignant

```



The frozen MobileNetV2 acts as a feature extractor, while the new classification layer learns the specific Benign vs Malignant classification task.



\---



\## Transfer Learning Results



The frozen MobileNetV2 achieved:



| \*\*Metric\*\*    |         \*\*Result\*\* |

| ------------- | -----------------: |

| Test Accuracy |         \*\*91.75%\*\* |

| Test Loss     |         \*\*0.7682\*\* |

| Training Time | \*\*266.76 seconds\*\* |



This was the highest test accuracy among all approaches evaluated in this session.



\---



\# Model Comparison



The three approaches were compared using the same test dataset.



| \*\*Model\*\*                | \*\*Test Accuracy\*\* | \*\*Test Loss\*\* | \*\*Training Time\*\* |

| ------------------------ | ----------------: | ------------: | ----------------: |

| CNN From Scratch         |            84.50% |        0.3688 |          215.54 s |

| CNN + Data Augmentation  |            86.10% |        0.3296 |          241.04 s |

| \*\*MobileNetV2 (Frozen)\*\* |        \*\*91.75%\*\* |        0.7682 |          266.76 s |



\### Accuracy Progression



```text

CNN From Scratch

&#x20;      ↓

&#x20;   84.50%



&#x20;      ↓



CNN + Data Augmentation

&#x20;      ↓

&#x20;   86.10%



&#x20;      ↓



MobileNetV2 (Frozen)

&#x20;      ↓

&#x20;   91.75% 🏆

```



\---



\# Analysis



\## CNN From Scratch



The baseline CNN achieved \*\*84.50% test accuracy\*\*.



This demonstrates that the network was able to learn meaningful visual patterns directly from the training images.



However, the model had to learn all visual features from the beginning.



\---



\## Data Augmentation



Adding data augmentation increased the test accuracy to \*\*86.10%\*\*.



The improvement suggests that the additional variation introduced during training helped the model generalize better to unseen images.



However, augmentation also increased the training time from \*\*215.54 seconds\*\* to \*\*241.04 seconds\*\*.



\---



\## Transfer Learning



The frozen MobileNetV2 achieved the best test accuracy of \*\*91.75%\*\*.



The improvement demonstrates the advantage of reusing visual features learned from a large pre-trained image dataset.



Although the training time was higher than the CNN approaches, the model achieved significantly better classification performance.



\---



\# Final Model Selection



Based on the test results, \*\*MobileNetV2 with frozen pre-trained layers\*\* was selected as the best-performing approach.



The final model achieved:



```text

Test Accuracy: 91.75%

```



Compared with the baseline CNN:



```text

91.75% - 84.50% = 7.25 percentage points improvement

```



This shows that transfer learning was more effective than training the CNN from scratch for this dataset.



\---







\# Conclusion



The hands-on experiment demonstrated how different CNN-based approaches can be used for binary skin lesion classification.



A CNN trained from scratch achieved \*\*84.50% test accuracy\*\*. Adding data augmentation improved the performance to \*\*86.10%\*\* by introducing additional variation into the training data.



Transfer learning using a frozen \*\*MobileNetV2\*\* model achieved the best result with \*\*91.75% test accuracy\*\*.



Therefore, the experiment demonstrates that \*\*transfer learning can provide stronger performance than training a CNN from scratch\*\*, particularly when using a pre-trained model with useful visual features learned from a large image dataset.



