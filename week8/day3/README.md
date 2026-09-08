\# Day 3 — Computer Vision Preprocessing with OpenCV



\## Overview



Day 3 focused on preparing image data for computer vision and deep learning models using OpenCV and TensorFlow/Keras.



The practical work was performed using the \*\*Flowers Multiclass Image Classification\*\* dataset, which contains five flower classes:



\* Daisy

\* Dandelion

\* Roses

\* Sunflowers

\* Tulips



The notebook covered the complete preprocessing workflow, from reading and inspecting raw images to preparing them for transfer learning with MobileNetV2.



\---



\## Learning Objectives



By the end of this session, I was able to:



\* Read and inspect images using OpenCV.

\* Resize images to a fixed input size.

\* Understand the difference between BGR and RGB.

\* Normalize pixel values.

\* Build a reusable image preprocessing function.

\* Apply image augmentation.

\* Visualize augmented images.

\* Apply model-specific preprocessing for transfer learning.

\* Prepare images for a pretrained MobileNetV2 model.



\---



\## Dataset



\### Flowers Multiclass Image Classification



The dataset contains five flower classes:



\* Daisy

\* Dandelion

\* Roses

\* Sunflowers

\* Tulips



\*\*Source:\*\* \[Flowers Multiclass Image Classification — Kaggle](https://www.kaggle.com/datasets/sujaykapadnis/flowers-image-classification)



The dataset is divided into:



\* Training

\* Validation

\* Test



\---



\## Dataset Exploration



The dataset contains:



\* \*\*Training:\*\* 3,540 images

\* \*\*Validation:\*\* 80 images

\* \*\*Test:\*\* 50 images



\### Training Distribution



| Class      | Images |

| ---------- | -----: |

| Daisy      |    607 |

| Dandelion  |    872 |

| Roses      |    615 |

| Sunflowers |    673 |

| Tulips     |    773 |



The training dataset is not perfectly balanced because the number of images differs between classes.



The validation and test sets are balanced, with 16 validation images and 10 test images per class.



\---



\## OpenCV Image Processing



\### 1. Reading Images



Images were loaded using OpenCV:



```python

image = cv2.imread(image\_path)

```



OpenCV reads images in \*\*BGR\*\* format by default.



\---



\### 2. Inspecting Image Properties



The original image was inspected to understand its dimensions, data type, and pixel range.



Example:



```text

Image shape: (263, 320, 3)

Data type: uint8

Minimum pixel value: 0

Maximum pixel value: 255

```



This shows that the image has:



\* Height: 263 pixels

\* Width: 320 pixels

\* 3 color channels

\* Pixel values between 0 and 255



\---



\### 3. Image Resizing



Images were resized to a fixed size of \*\*224 × 224 pixels\*\*:



```python

resized\_image = cv2.resize(image, (224, 224))

```



The resulting image shape was:



```text

(224, 224, 3)

```



A fixed image size is important because deep learning models require consistent input dimensions.



\---



\### 4. BGR to RGB Conversion



Since OpenCV uses BGR while visualization libraries such as Matplotlib use RGB, the images were converted using:



```python

image\_rgb = cv2.cvtColor(image, cv2.COLOR\_BGR2RGB)

```



This prevents incorrect color representation when displaying OpenCV images.



\---



\## Pixel Normalization



The original pixel values range from \*\*0 to 255\*\*.



Standard normalization was applied using:



```python

normalized\_image = image\_rgb / 255.0

```



This converts the pixel range to:



```text

0 → 1

```



The normalized image was converted to `float32` in the reusable preprocessing pipeline.



\---



\## Reusable Preprocessing Function



A preprocessing function was created to combine the main OpenCV operations:



```python

def preprocess\_image(image\_path, target\_size=(224, 224)):

&#x20;   image = cv2.imread(image\_path)

&#x20;   image = cv2.resize(image, target\_size)

&#x20;   image = cv2.cvtColor(image, cv2.COLOR\_BGR2RGB)

&#x20;   image = image.astype(np.float32) / 255.0



&#x20;   return image

```



The resulting image had:



```text

Shape: (224, 224, 3)

Data type: float32

Range: 0.0 to 1.0

```



\---



\## Data Augmentation



An augmentation pipeline was created using TensorFlow/Keras:



```python

augmentation = ImageDataGenerator(

&#x20;   rotation\_range=20,

&#x20;   zoom\_range=0.15,

&#x20;   horizontal\_flip=True,

&#x20;   brightness\_range=\[0.8, 1.2]

)

```



The applied transformations included:



\* Rotation

\* Zoom

\* Horizontal flipping

\* Brightness adjustment



Augmentation generates different variations of training images while preserving their main visual characteristics.



This can help improve model generalization and reduce overfitting.



Augmentation should be applied to training data rather than validation or test data.



\---



\## Transfer Learning Preprocessing



For transfer learning, preprocessing must match the requirements of the selected pretrained model.



For \*\*MobileNetV2\*\*, the model-specific `preprocess\_input()` function was used:



```python

from tensorflow.keras.applications.mobilenet\_v2 import preprocess\_input



image\_for\_model = processed\_image \* 255.0

mobilenet\_image = preprocess\_input(image\_for\_model)

```



Unlike standard normalization, which produces values between:



```text

0 → 1

```



MobileNetV2 preprocessing produces values approximately between:



```text

\-1 → 1

```



The final processed image had:



```text

Shape: (224, 224, 3)

Data type: float32

Minimum: -1.0

Maximum: 1.0

```



\---



\## Final Preprocessing Pipeline



A complete MobileNetV2 preprocessing function was created:



```python

def mobilenetv2\_preprocess(image\_path, target\_size=(224, 224)):

&#x20;   image = cv2.imread(image\_path)

&#x20;   image = cv2.resize(image, target\_size)

&#x20;   image = cv2.cvtColor(image, cv2.COLOR\_BGR2RGB)

&#x20;   image = image.astype(np.float32)

&#x20;   image = preprocess\_input(image)



&#x20;   return image

```



The final pipeline can be summarized as:



```text

Raw Image

&#x20;   ↓

Read with OpenCV

&#x20;   ↓

Resize to 224 × 224

&#x20;   ↓

BGR → RGB

&#x20;   ↓

Convert to float32

&#x20;   ↓

MobileNetV2 preprocess\_input()

&#x20;   ↓

Final Image

```



\### Final Output



```text

Shape: (224, 224, 3)

Data type: float32

Pixel range: -1.0 to 1.0

```



\---



\## Key Takeaways



\* Images need preprocessing before being used by deep learning models.

\* OpenCV reads images in BGR format.

\* Matplotlib expects RGB format.

\* Images can be resized to a fixed input size.

\* Pixel normalization scales values into a smaller range.

\* Data augmentation creates additional variations of training images.

\* Pretrained models may require specific preprocessing methods.

\* MobileNetV2 expects its inputs to be processed using `preprocess\_input()`.



\---



\## Conclusion



This session provided practical experience with the main image preprocessing techniques used in computer vision.



The complete pipeline was implemented using \*\*OpenCV and TensorFlow/Keras\*\*, including image reading, resizing, color conversion, normalization, augmentation, and model-specific preprocessing.



The final images were successfully prepared in the required format for a pretrained \*\*MobileNetV2\*\* model.



