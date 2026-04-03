import os
import joblib
import shap
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.metrics import (
    confusion_matrix,
    roc_auc_score,
    classification_report
)


FEATURE_DIR = "src/features"
MODEL_DIR = "src/models"
EVAL_DIR = "src/evaluation"

os.makedirs(EVAL_DIR, exist_ok=True)



print("Loading the data")

X_test = pd.read_csv(os.path.join(FEATURE_DIR, "X_test.csv"))
y_test = pd.read_csv(os.path.join(FEATURE_DIR, "y_test.csv")).values.ravel()




y_test = pd.Series(y_test).astype(str)


y_test = y_test.map({
    "No": 0,
    "Yes": 1,
    "0": 0,
    "1": 1
})


y_test = y_test.astype(int).values


model = joblib.load(os.path.join(MODEL_DIR, "tuned_model.pkl"))


print("Generating SHAP values")

explainer = shap.TreeExplainer(model)
shap_values = explainer.shap_values(X_test)

plt.figure()
shap.summary_plot(shap_values, X_test, show=False)
plt.tight_layout()
plt.savefig(os.path.join(EVAL_DIR, "shap_summary.png"))
plt.close()

print("SHAP summary plot saved.")


importance = model.feature_importances_

feature_importance = pd.Series(
    importance,
    index=X_test.columns
).sort_values(ascending=False)

plt.figure(figsize=(10, 6))
feature_importance.head(20).plot(kind="barh")
plt.title("Top 20 Feature Importance")
plt.tight_layout()
plt.savefig(os.path.join(EVAL_DIR, "feature_importance.png"))
plt.close()

print("Feature importance plot saved.")


y_pred = model.predict(X_test)
y_proba = model.predict_proba(X_test)[:, 1]

y_pred = pd.Series(y_pred).astype(int).values

roc_auc = roc_auc_score(y_test, y_proba)

cm = confusion_matrix(y_test, y_pred)

plt.figure(figsize=(6, 5))
sns.heatmap(cm, annot=True, fmt="d", cmap="Blues")
plt.title("Confusion Matrix Heatmap")
plt.ylabel("Actual")
plt.xlabel("Predicted")
plt.tight_layout()
plt.savefig(os.path.join(EVAL_DIR, "error_heatmap.png"))
plt.close()

print("Error heatmap saved.")


report = classification_report(y_test, y_pred)

with open(os.path.join(EVAL_DIR, "classification_report.txt"), "w") as f:
    f.write(report)

print("Classification report saved.")


print("Test ROC-AUC:", roc_auc)
