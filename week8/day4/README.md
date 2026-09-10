# Day 4 — Model Integration & Error Analysis

## Overview

Day 4 focused on integrating the complete image classification workflow into an end-to-end pipeline and analyzing the model's classification errors.

The **Flower Photos** dataset was used with **MobileNetV2 Transfer Learning** to classify images into five flower categories: Daisy, Dandelion, Roses, Sunflowers, and Tulips.

## Data & Preprocessing

- Image size: `224 × 224 × 3`
- Classes: `5`
- Dataset split: Train, Validation, and Test
- MobileNetV2 preprocessing was applied to all images.
- Pixel values were transformed from `[0, 255]` to `[-1, 1]`.
- The same preprocessing was used during training, testing, and inference to avoid training/serving skew.

## Model

A pretrained **MobileNetV2** model with ImageNet weights was used as the feature extractor.

Architecture:

`MobileNetV2 → Global Average Pooling → Dropout (0.2) → Dense (5 classes)`

Training configuration:
- Optimizer: Adam
- Learning Rate: `0.0001`
- Epochs: `10`
- Batch Size: `32`

## Results

- **Test Accuracy:** `80%`
- **Macro F1-Score:** `0.80`
- **Correct Predictions:** `40/50`
- **Misclassified Images:** `10/50`

The strongest class was **Sunflowers** with an F1-score of `0.91`, while **Tulips** had the lowest F1-score at `0.67`.

## Error Analysis

The confusion matrix showed that the main source of error was the confusion between **Roses and Tulips**.

The most frequent misclassification was:

`Roses → Tulips: 3 cases`

Three misclassified images were analyzed in detail. Two were mainly related to data issues, such as unclear flower structure, unusual growth stages, poor lighting, or distracting backgrounds. One case was identified as a model weakness because the rose was clearly visible but was still classified as a tulip.

## End-to-End Prediction

An end-to-end `predict_image()` function was implemented to process a raw image automatically:

`Raw Image → Resize → Preprocessing → Model → Predicted Class + Confidence`

For one test image, the model predicted **Daisy** with a confidence of `39.03%`. The probabilities of Daisy and Dandelion were close (`39.03%` and `36.44%`), indicating uncertainty in the prediction.

A final consistency check confirmed that the test pipeline and the end-to-end prediction pipeline produced the same prediction.

## Conclusion

Day 4 successfully integrated the complete image classification workflow into an end-to-end pipeline. The error analysis provided a better understanding of the model's weaknesses, especially the confusion between **Roses and Tulips**. The final pipeline can now take a raw image, apply the required preprocessing, generate a prediction, and return the predicted class with its confidence score.
