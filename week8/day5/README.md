# SHAP Explainability Analysis

## Overview

SHAP (SHapley Additive exPlanations) was used to interpret the trained cardiovascular risk prediction model and understand which features have the greatest influence on its predictions.

The analysis focused on explaining the model's behavior rather than treating it as a black-box system.

## SHAP Method

A `KernelExplainer` was used to calculate SHAP values for a sample of 200 test observations.

The resulting SHAP values were used to analyze:

- Global feature importance
- The direction of feature contributions
- Feature-level relationships with model predictions
- Possible interactions between important features

## Global Feature Importance

The mean absolute SHAP values identified the following features as the most influential:

| Rank | Feature | Mean \|SHAP\| |
|------|---------|---------------:|
| 1 | `ap_hi` | 0.055277 |
| 2 | `age_years` | 0.054667 |
| 3 | `pulse_pressure` | 0.054438 |
| 4 | `map` | 0.051557 |
| 5 | `cholesterol` | 0.043051 |
| 6 | `weight` | 0.031342 |
| 7 | `ap_lo` | 0.029242 |
| 8 | `active` | 0.013641 |
| 9 | `bmi` | 0.010007 |
| 10 | `gender` | 0.007034 |
| 11 | `height` | 0.006366 |
| 12 | `alco` | 0.004061 |
| 13 | `gluc` | 0.004039 |
| 14 | `smoke` | 0.003215 |

The results show that blood-pressure-related features and age have the greatest influence on the model's predictions.

## SHAP Dependence Analysis

Dependence plots were analyzed for the four most influential features.

### 1. Systolic Blood Pressure — `ap_hi`

The `ap_hi` dependence plot showed a strong positive relationship between the feature and its SHAP value.

Higher standardized `ap_hi` values generally produced positive SHAP values, pushing predictions toward `cardio = 1`, while lower values tended to push predictions toward `cardio = 0`.

### 2. Age — `age_years`

The `age_years` dependence plot also showed a clear positive relationship.

As standardized age increased, the SHAP value generally increased, indicating that higher age contributed toward higher predicted cardiovascular risk.

The plot showed more variation than `ap_hi`, suggesting that the contribution of age can be influenced by other patient features.

### 3. Pulse Pressure — `pulse_pressure`

`pulse_pressure` showed a strong positive relationship with its SHAP value.

Lower values generally contributed negatively to the prediction, while higher values contributed positively toward `cardio = 1`.

The color distribution based on `ap_lo` suggested a possible interaction between pulse pressure and diastolic blood pressure.

### 4. Mean Arterial Pressure — `map`

The `map` dependence plot showed another strong positive relationship.

Higher standardized `map` values generally produced higher SHAP values and pushed the model's prediction toward `cardio = 1`.

The color distribution based on age showed substantial overlap, suggesting that there was no strong visible interaction between `map` and `age_years` in this analysis.

## Key Findings

The SHAP analysis showed that:

- `ap_hi` was the most influential feature.
- `age_years` was the second most influential feature.
- `pulse_pressure` and `map` were also among the strongest contributors.
- Blood-pressure-related features had a major influence on the model's predictions.
- Higher values of the main blood pressure features generally pushed predictions toward the positive cardiovascular-risk class.
- Age showed a clear positive contribution to the model's predictions.
- Some possible feature interactions were observed, particularly among blood-pressure-related variables.

## Conclusion

SHAP improved the interpretability of the cardiovascular prediction model by showing which features contribute most to its decisions.

The analysis indicates that `ap_hi`, `age_years`, `pulse_pressure`, and `map` are the most influential features in the model. Their dependence plots showed that higher values generally contributed toward higher predicted cardiovascular risk.

Overall, SHAP provided an interpretable view of the model's behavior and helped explain the factors behind its predictions rather than relying only on overall evaluation metrics.

> **Note:** SHAP explains the behavior of the trained model and does not establish medical causation. The results should therefore be interpreted as model explanations rather than clinical conclusions.
