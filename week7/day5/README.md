# Day 5 — Tuning, Evaluation & Sprint Review

## Project: Cardio Patient Monitoring

### 1. Objective

The goal of Day 5 was to advance the baseline Neural Network model by selecting a suitable architecture, tuning its hyperparameters, optimizing the classification threshold, evaluating the final model, and honestly comparing it against the baseline on the unseen test set.

Because the Cardio dataset is tabular, a Dense Neural Network was selected as the core model.

The primary evaluation metric was **F1-score**, while **Recall** was also considered important, since identifying positive cardiac cases is a key objective.

---

## 2. Baseline Model

The baseline Neural Network used:

* Architecture: `32 → 16 → 1`
* Learning Rate: `0.001`
* Batch Size: `32`
* Dropout: `0`
* Threshold: `0.50`
* Optimizer: Adam
* Loss: Binary Crossentropy

### Baseline Test Results

| Metric    |      Score |
| --------- | ---------: |
| Accuracy  |     0.7326 |
| Precision |     0.7487 |
| Recall    |     0.6918 |
| F1-score  | **0.7192** |

---

## 3. Hyperparameter Tuning

Experiments were conducted one variable at a time, using **validation F1-score** as the selection metric, on data that had inconsistent blood-pressure records removed and BMI / Pulse Pressure / Mean Arterial Pressure features added.

### Learning Rate Tuning

Tested learning rates:

* `0.001` → val F1 = `0.7231`
* `0.0005` → val F1 = `0.7234`
* `0.0001` → val F1 = `0.7254`

Best learning rate: **0.0001**

---

### Architecture Tuning

Tested architectures (with the best learning rate):

* `32 → 16` → val F1 = `0.7233`
* `64 → 32 → 16` → val F1 = `0.7244`
* `64 → 32` → val F1 = `0.7237`

Best architecture: **64 → 32 → 16**

---

### Dropout Tuning

Tested dropout rates:

* `0.0` → val F1 = `0.7249`
* `0.2` → val F1 = `0.7213`

Best dropout: **0.0**

---

### Batch Size Tuning

Tested batch sizes:

* `32` → val F1 = `0.7236`
* `64` → val F1 = `0.7211`

Best batch size: **32**

At this point (default 0.50 threshold), the tuned architecture reached a validation F1-score of **0.7236** — close to, but not clearly better than, the baseline.

---

### Threshold Tuning

The default 0.50 classification threshold is not necessarily optimal for F1-score. Thresholds from 0.30 to 0.70 were swept on the **validation set only**.

Best threshold: **0.36**

Validation results at the best threshold:

| Metric    |      Score |
| --------- | ---------: |
| Precision |     0.6722 |
| Recall    |     0.8226 |
| F1-score  | **0.7398** |

This is the step that produced the real improvement over the baseline — moving the threshold traded precision for a large gain in recall.

---

## 4. Final Tuned Model

The final model used:

| Parameter      | Value               |
| -------------- | ------------------- |
| Architecture   | `64 → 32 → 16 → 1`  |
| Learning Rate  | `0.0001`            |
| Dropout        | `0.0`               |
| Batch Size     | `32`                |
| Threshold      | `0.36`              |
| Optimizer      | Adam                |
| Loss           | Binary Crossentropy |
| Early Stopping | Enabled             |

---

## 5. Final Test Evaluation

The final tuned model was evaluated once on the held-out test set, at both the default and the validation-selected threshold, and compared against the baseline.

| Metric    | Baseline | Tuned (threshold = 0.50) | Final Tuned (threshold = 0.36) |
| --------- | -------: | ------------------------: | ------------------------------: |
| Accuracy  |   0.7326 |                     0.7271 |                           0.7134 |
| Precision |   0.7487 |                     0.7395 |                       **0.6713** |
| Recall    |   0.6918 |                     0.6923 |                       **0.8244** |
| F1-score  |   0.7192 |                     0.7151 |                       **0.7400** |

### Improvement (Baseline → Final Tuned)

* F1-score: **+0.0208** (0.7192 → 0.7400)
* Recall: **+0.1326** (0.6918 → 0.8244)
* Precision: **−0.0774** (0.7487 → 0.6713)

### Honest note on where the improvement came from

Tuning the architecture, learning rate, dropout, and batch size alone — still evaluated at the default 0.50 threshold — actually scored *slightly below* the baseline (0.7151 vs. 0.7192 F1). The improvement in the final model comes almost entirely from **optimizing the decision threshold** on the validation set. This was verified by selecting the threshold using only validation data and then applying it, unchanged, to the test set, so the gain is real and not test-set leakage — but it should be reported as a threshold effect, not an architecture effect.

---

## 6. Training Analysis

Training and validation loss curves were plotted for the baseline model to monitor learning behavior. No significant gap between training and validation curves was observed, indicating no severe overfitting.

EarlyStopping (`monitor="val_loss"`, `patience=5`, `restore_best_weights=True`) was used throughout to prevent unnecessary training and restore the best-performing weights.

---

## Conclusion

The final tuned model reached:

**F1-score = 0.7400**

compared with:

**Baseline F1-score = 0.7192**

Recall also improved substantially:

**69.18% → 82.44%**

The results show that, for this dataset, hyperparameter tuning alone did not clearly beat the baseline — the meaningful gain came from optimizing the classification threshold, which shifted the precision/recall balance strongly toward recall while raising the overall F1-score.

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