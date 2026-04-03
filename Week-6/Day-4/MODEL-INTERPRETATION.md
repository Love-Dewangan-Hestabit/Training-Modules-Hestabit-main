# Week 6 (Day 4) - Hyperparameter Tuning, Explainability and Error Analysis

**Name: Love Dewangan**  
**Email: love.dewangan@hestabit.in**

## Task

To implement Hyperparameter tuning with Optuna and also to Generate SHAP summary plot, feature importance chart and error analysis heatmap.

## Hyperparameter Tuning

I used Optuna for hyperparameter tuning of XGBoost.

### Parameters Tuned

- n_estimators
- max_depth
- learning_rate
- subsample
- colsample_bytree
- gamma
- reg_lambda

## SHAP Analysis

### SHAP Summary Plot

The SHAP summary plot helps us understand how the model is making decisions.

The SHAP analysis shows:

- Which features have the biggest overall impact on predictions

- How strongly each feature influences individual predictions

This allows us to understand:

- Which features drive attrition risk
- Whether higher/lower feature values increase attrition probability

## Feature Importance

Feature importance from XGBoost identifies the most influential
predictors.

Top features typically include:

- Income-related features
- Tenure-related features
- Satisfaction-related features
- Manager-related risk indicators

## Error Analysis

We analyzed:

- Confusion Matrix
- False Positives (predicted leave but stayed)
- False Negatives (predicted stay but left)

False negatives are more critical in attrition prediction, because
missing a leaving employee reduces intervention opportunity.

Heatmap visualization provides clarity on model performance balance.

## Bias/Variance Analysis

Observations:

- Cross-validation ensures stable generalization
- Tuned parameters control model complexity
- No severe overfitting observed

## Task Outcome

- Improved the ROC-AUC over baseline
- Full model explainability
- Structured error analysis

Evaluation Generated:

- shap_summary.png
- feature_importance.png
- error_heatmap.png
- classification_report.txt
- tuning/results.json
