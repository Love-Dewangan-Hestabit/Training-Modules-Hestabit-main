# Week 6 (Day 3) - Model Building and Advanced Training Pipeline

**Name: Love Dewangan**  
**Email: love.dewangan@hestabit.in**

## Task

To create a unified training pipeline that Trains 4 models (Logistic Regression, Random Forest, XG Boost, Neutral Network) also evaluate models on these metrics Accuracy, Precision, Recall, F1 Score, ROC-AUC

## Models Evaluated

- Logistic Regression
- Random Forest
- Neural Network (MLPClassifier)
- XGBoost

## Cross-Validation Results

```
_____________________________________________________________________
|                                                                   |
|  Model        Accuracy   Precision   Recall   F1 Score  ROC-AUC   |
|___________________________________________________________________|
|                                                                   |
|  Logistic     0.8629     0.6922      0.3008   0.4185    0.8165    |
|  Regression                                                       |
|                                                                   |
|  Random       0.8530     0.6977      0.2020   0.3121    0.7646    |
|  Forest                                                           |
|                                                                   |
|  Neural       0.8232     0.4462      0.3270   0.3761    0.7159    |
|  Network                                                          |
|                                                                   |
|  XGBoost      0.8332     0.4900      0.3000   0.3717    0.7522    |
|___________________________________________________________________|
```

## Best Model

### Logistic Regression

**Reason:**

- Highest Cross-Validation ROC-AUC (0.8165)
- Fastest training time
- Stable performance across folds

## Final Test Set Performance (Best Model)

### Metric Value

Accuracy: **0.8705**<br>
Precision: **0.7273**<br>
Recall: **0.3478**<br>
F1 Score: **0.4706**<br>
ROC-AUC: **0.8505**<br>

## Artifacts Generated

- `models/best_model.pkl`
- `evaluation/metrics.json`
- `evaluation/confusion_matrix.png`
