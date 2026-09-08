# Day 3 — Computer Vision Preprocessing with OpenCV

## Overview

Day 3 focused on image preprocessing techniques used in computer vision and deep learning.

The session covered how raw images are prepared before being passed to a machine learning or deep learning model. The practical work included image resizing, color conversion, normalization, data augmentation, and preprocessing for transfer learning models.

---

## Learning Objectives

By the end of this session, I was able to:

* Preprocess images using OpenCV.
* Resize images to a fixed size.
* Understand the difference between BGR and RGB color formats.
* Normalize pixel values.
* Build a reusable image preprocessing pipeline.
* Apply data augmentation to training images.
* Match image preprocessing with the requirements of a pretrained model.

---

## Dataset

The practical work was performed using the **Flowers Multiclass Image Classification** dataset.

The dataset contains five flower classes:

* Daisy
* Dandelion
* Roses
* Sunflowers
* Tulips

**Dataset Source:** [Flowers Multiclass Image Classification — Kaggle](https://www.kaggle.com/datasets/sujaykapadnis/flowers-image-classification)

The dataset is organized into:

* Training set
* Validation set
* Test set

---

## Dataset Exploration

The dataset was explored to understand its structure, classes, and image distribution.

The training set contains different numbers of images for each flower class, while the validation and test sets are balanced across all classes.

Original images were also inspected to examine their dimensions, data types, and pixel value ranges.

---

## Image Preprocessing with OpenCV

The main preprocessing steps included:

### Image Reading

Images were loaded and inspected using OpenCV.

### Image Resizing

Images were resized to a fixed size of **224 × 224 pixels** to provide consistent input dimensions.

### BGR to RGB Conversion

Since OpenCV reads images in BGR format while most visualization and deep learning workflows use RGB, images were converted to the correct color format.

### Pixel Normalization

Pixel values were scaled from the original range of **0–255** to **0–1**.

---

## Reusable Preprocessing Pipeline

A reusable preprocessing pipeline was created to combine the main preprocessing steps:

**Read Image → Resize → BGR to RGB → Normalize**

The final output produced images with:

* Shape: **(224, 224, 3)**
* Data type: **float32**
* Pixel range: **0–1**

---

## Data Augmentation

A data augmentation pipeline was created to generate different variations of training images.

The applied transformations included:

* Rotation
* Zoom
* Horizontal flipping
* Brightness adjustment

Augmentation helps increase the diversity of the training data and can improve model generalization while reducing overfitting.

---

## Transfer Learning Preprocessing

The session also focused on matching preprocessing techniques with the requirements of pretrained models.

**MobileNetV2** was used as an example to demonstrate model-specific preprocessing.

Unlike standard normalization, MobileNetV2 expects pixel values to be transformed to approximately:

**-1 to 1**

A complete preprocessing pipeline was created to prepare images in the correct format for MobileNetV2.

---

## Key Takeaways

* Raw images need preprocessing before being used in deep learning models.
* Images should have consistent dimensions before being used as model input.
* OpenCV uses BGR format, while many other tools use RGB.
* Normalization helps scale pixel values to an appropriate range.
* Data augmentation creates additional variations of training images.
* Pretrained models may require specific preprocessing methods.
* Matching preprocessing with the selected model is essential for successful transfer learning.

---

## Tools Used

* OpenCV
* TensorFlow/Keras
* NumPy
* Matplotlib
* Google Colab
* Google Drive

---

## Conclusion

Day 3 provided practical experience with the main image preprocessing techniques used in computer vision.

A complete workflow was implemented, covering image exploration, resizing, color conversion, normalization, augmentation, and transfer learning preprocessing.

The final preprocessing pipeline successfully prepared images for use with a pretrained **MobileNetV2** model.
