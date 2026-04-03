import os
import json
import joblib
import time
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import StratifiedKFold, cross_validate
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    roc_auc_score,
    confusion_matrix,
    ConfusionMatrixDisplay,
)

from xgboost import XGBClassifier


total_start_time = time.time()


FEATURE_DIR = "src/features"
MODEL_DIR = "src/models"
EVAL_DIR = "src/evaluation"

os.makedirs(MODEL_DIR, exist_ok=True)
os.makedirs(EVAL_DIR, exist_ok=True)


print("Loading feature datasets...")

X_train = pd.read_csv(os.path.join(FEATURE_DIR, "X_train.csv"))
X_test = pd.read_csv(os.path.join(FEATURE_DIR, "X_test.csv"))

y_train = pd.read_csv(os.path.join(FEATURE_DIR, "y_train.csv")).values.ravel()
y_test = pd.read_csv(os.path.join(FEATURE_DIR, "y_test.csv")).values.ravel()



if y_train.dtype == object or isinstance(y_train[0], str):
    y_train = pd.Series(y_train).map({"No": 0, "Yes": 1}).values

if y_test.dtype == object or isinstance(y_test[0], str):
    y_test = pd.Series(y_test).map({"No": 0, "Yes": 1}).values

print("Unique labels after encoding:", np.unique(y_train))


models = {
    "Logistic Regression": LogisticRegression(
        max_iter=1000,
        C=1.0,
        solver="lbfgs",
        random_state=42
    ),
    "Random Forest": RandomForestClassifier(
        n_estimators=200,
        random_state=42
    ),
    "Neural Network": MLPClassifier(
        hidden_layer_sizes=(128, 64),
        max_iter=500,
        random_state=42
    ),
    "XGBoost": XGBClassifier(
        eval_metric="logloss",
        random_state=42
    )
}


cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)

scoring = {
    "accuracy": "accuracy",
    "precision": "precision",
    "recall": "recall",
    "f1": "f1",
    "roc_auc": "roc_auc",
}

results = {}
best_model_name = None
best_score = 0

for name, model in models.items():
    print(f"\nTraining: {name}")

    start_time = time.time()

    cv_results = cross_validate(
        model,
        X_train,
        y_train,
        cv=cv,
        scoring=scoring,
        return_train_score=False
    )

    end_time = time.time()
    training_time = end_time - start_time

    mean_scores = {
        metric: np.mean(cv_results[f"test_{metric}"])
        for metric in scoring.keys()
    }

    mean_scores["cv_training_time_seconds"] = round(training_time, 4)

    results[name] = mean_scores

    print(f"CV ROC-AUC: {mean_scores['roc_auc']:.4f}")
    print(f"Training Time: {training_time:.2f} seconds")

    if mean_scores["roc_auc"] > best_score:
        best_score = mean_scores["roc_auc"]
        best_model_name = name


print("\nBest Model based on ROC-AUC:", best_model_name)

best_model = models[best_model_name]

fit_start = time.time()
best_model.fit(X_train, y_train)
fit_end = time.time()

final_training_time = fit_end - fit_start

joblib.dump(best_model, os.path.join(MODEL_DIR, "best_model.pkl"))

y_pred = best_model.predict(X_test)
y_proba = best_model.predict_proba(X_test)[:, 1]

test_metrics = {
    "accuracy": accuracy_score(y_test, y_pred),
    "precision": precision_score(y_test, y_pred),
    "recall": recall_score(y_test, y_pred),
    "f1": f1_score(y_test, y_pred),
    "roc_auc": roc_auc_score(y_test, y_proba),
    "final_training_time_seconds": round(final_training_time, 4)
}

results["Best_Model_Test_Performance"] = test_metrics


total_end_time = time.time()
total_runtime = total_end_time - total_start_time

results["Total_Runtime_Seconds"] = round(total_runtime, 4)

with open(os.path.join(EVAL_DIR, "metrics.json"), "w") as f:
    json.dump(results, f, indent=4)


cm = confusion_matrix(y_test, y_pred)
disp = ConfusionMatrixDisplay(confusion_matrix=cm)
disp.plot()
plt.title(f"Confusion Matrix - {best_model_name}")
plt.savefig(os.path.join(EVAL_DIR, "confusion_matrix.png"))
plt.close()


print("\nSuccessfully Model Trained")
print(f"Total Runtime: {total_runtime:.2f} seconds")
