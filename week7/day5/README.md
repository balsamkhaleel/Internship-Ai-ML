\# Day 5 — Advancing the Core Model \& Sprint 2 Review



\## Project: Cardio Patient Monitoring



\### 1. Objective



The goal of Day 5 was to advance the baseline Neural Network model by selecting a suitable architecture, tuning its hyperparameters, evaluating the final model, and documenting the Sprint 2 results.



Because the Cardio dataset is tabular, a Dense Neural Network was selected as the core model.



The primary evaluation metric was \*\*F1-score\*\*, while \*\*Recall\*\* was also considered important because identifying positive cardiac cases is a key objective.



\---



\## 2. Baseline Model



The baseline Neural Network used:



\* Architecture: `16 → 8 → 1`

\* Learning Rate: `0.001`

\* Batch Size: `32`

\* Dropout: `0`

\* Threshold: `0.50`

\* Optimizer: Adam

\* Loss: Binary Crossentropy



\### Baseline Test Results



| Metric    |      Score |

| --------- | ---------: |

| Precision |     0.7458 |

| Recall    |     0.7008 |

| F1-score  | \*\*0.7226\*\* |



\---



\## 3. Hyperparameter Tuning



Several experiments were conducted using the validation set.



\### Learning Rate Tuning



Tested learning rates:



\* `0.01`

\* `0.001`

\* `0.0005`

\* `0.0001`



Best learning rate:



\*\*0.0005\*\*



Best validation F1-score:



\*\*0.7219\*\*



\---



\### Architecture Tuning



Tested architectures:



\* `16 → 8`

\* `32 → 16`

\* `64 → 32 → 16`



Best architecture:



\*\*64 → 32 → 16\*\*



Validation F1-score:



\*\*0.7245\*\*



\---



\### Dropout Tuning



Tested dropout rates:



\* `0.0`

\* `0.1`

\* `0.2`

\* `0.3`



Best dropout:



\*\*0.3\*\*



Validation F1-score:



\*\*0.7228\*\*



\---



\### Batch Size Tuning



Tested batch sizes:



\* `16`

\* `32`

\* `64`



Best batch size:



\*\*64\*\*



Validation F1-score:



\*\*0.7191\*\*



\---



\### Threshold Tuning



Different classification thresholds were tested to improve F1-score and Recall.



Best threshold:



\*\*0.35\*\*



Validation results:



| Metric    |      Score |

| --------- | ---------: |

| Precision |     0.6511 |

| Recall    |     0.8381 |

| F1-score  | \*\*0.7329\*\* |



\---



\## 4. Final Tuned Model



The final model used:



| Parameter      | Value               |

| -------------- | ------------------- |

| Architecture   | `64 → 32 → 16 → 1`  |

| Learning Rate  | `0.0005`            |

| Dropout        | `0.3`               |

| Batch Size     | `64`                |

| Threshold      | `0.35`              |

| Optimizer      | Adam                |

| Loss           | Binary Crossentropy |

| Early Stopping | Enabled             |



\---



\## 5. Final Test Evaluation



The final tuned model was evaluated once on the held-out test set.



| Metric    | Baseline | Final Tuned |

| --------- | -------: | ----------: |

| Precision |   0.7458 |      0.6413 |

| Recall    |   0.7008 |  \*\*0.8507\*\* |

| F1-score  |   0.7226 |  \*\*0.7313\*\* |



\### Improvement



\* F1-score: \*\*+0.0087\*\*

\* Recall: \*\*+0.1499\*\*

\* Precision: \*\*-0.1046\*\*



The final model improved the primary metric, F1-score, from \*\*0.7226 to 0.7313\*\*.



The most significant improvement was in Recall, which increased from \*\*0.7008 to 0.8507\*\*.



The decrease in Precision is expected after lowering the classification threshold to 0.35, as the model became more likely to classify samples as positive.



\---



\## 6. Training Analysis



Training and validation curves were analyzed to monitor the model's learning behavior.



No significant gap between training and validation curves was observed, indicating \*\*no clear severe overfitting\*\*.



Early Stopping was used to prevent unnecessary training and restore the best validation weights.



\---



\## 7. Experiment Tracking



MLflow was used to track the Sprint 2 experiments.



The following parameters and metrics were logged:



\### Parameters



\* Architecture

\* Learning Rate

\* Dropout

\* Batch Size

\* Classification Threshold



\### Metrics



\* Validation Precision

\* Validation Recall

\* Validation F1-score

\* Final Test Accuracy

\* Final Test Precision

\* Final Test Recall

\* Final Test F1-score



A dedicated MLflow experiment was created:



`Cardio\_Sprint\_2`



The final tuned model was also logged as a separate MLflow run.



\---



\# Sprint 2 Review



\## What Went Well?



\* A Dense Neural Network was selected appropriately for the tabular dataset.

\* Multiple hyperparameters were systematically evaluated.

\* F1-score was used as the primary model-selection metric.

\* Recall was significantly improved.

\* The final model achieved a higher F1-score than the baseline.

\* Training curves were analyzed for overfitting.

\* MLflow was used to track experiments and final results.



\## What Could Be Improved?



The experiments were performed sequentially, optimizing one hyperparameter at a time. This does not guarantee that the selected parameters represent the globally optimal combination.



More systematic hyperparameter search could be explored in future work.



\---



\# Sprint 2 Retrospective



\## What Went Well?



The model development process became more systematic compared with the baseline stage.



Experimenting with architecture, learning rate, dropout, batch size, and threshold helped identify how each parameter affected Precision, Recall, and F1-score.



The use of F1-score as the primary metric also aligned the model evaluation with the project's objective.



\## What Could Be Improved?



Experiment tracking was added after the experiments were completed. In future iterations, experiments should be logged automatically during training rather than recorded afterward.



\## Concrete Change for Sprint 3



For Sprint 3, MLflow will be integrated directly into the training and tuning loops so that every experiment is automatically logged with its parameters, metrics, and model information.



\---



\# Sprint 2 Conclusion



Sprint 2 successfully advanced the Cardio Neural Network beyond the baseline.



The final tuned model achieved:



\*\*F1-score = 0.7313\*\*



compared with:



\*\*Baseline F1-score = 0.7226\*\*



Recall also improved substantially:



\*\*70.08% → 85.07%\*\*



The results demonstrate that hyperparameter tuning and threshold optimization improved the model's ability to identify positive cardiac cases while achieving a modest improvement in the overall F1-score.






