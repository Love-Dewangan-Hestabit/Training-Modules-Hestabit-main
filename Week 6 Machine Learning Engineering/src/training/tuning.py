import os
import json
import joblib
import optuna
import numpy as np
import pandas as pd

from sklearn.model_selection import StratifiedKFold, cross_val_score
from sklearn.metrics import roc_auc_score
from xgboost import XGBClassifier

FEATURE_DIR = "src/features"
MODEL_DIR = "src/models"
TUNING_DIR = "src/tuning"

os.makedirs(TUNING_DIR, exist_ok=True)

print("Loading training data...")
X_train = pd.read_csv(os.path.join(FEATURE_DIR, "X_train.csv"))
y_train = pd.read_csv(os.path.join(FEATURE_DIR, "y_train.csv")).values.ravel()

if y_train.dtype == object:
    y_train = pd.Series(y_train).map({"No": 0, "Yes": 1}).values


cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)

def objective(trial):

    params = {
        "n_estimators": trial.suggest_int("n_estimators", 100, 500),
        "max_depth": trial.suggest_int("max_depth", 3, 10),
        "learning_rate": trial.suggest_float("learning_rate", 0.01, 0.3),
        "subsample": trial.suggest_float("subsample", 0.6, 1.0),
        "colsample_bytree": trial.suggest_float("colsample_bytree", 0.6, 1.0),
        "gamma": trial.suggest_float("gamma", 0, 5),
        "reg_lambda": trial.suggest_float("reg_lambda", 0, 10),
        "eval_metric": "logloss",
        "random_state": 42,
        "use_label_encoder": False
    }

    model = XGBClassifier(**params)

    scores = cross_val_score(
        model,
        X_train,
        y_train,
        cv=cv,
        scoring="roc_auc"
    )

    return scores.mean()

print("Starting Optuna tuning...")

study = optuna.create_study(direction="maximize")
study.optimize(objective, n_trials=30)

print("Best ROC-AUC:", study.best_value)
print("Best Parameters:", study.best_params)


best_model = XGBClassifier(
    **study.best_params,
    eval_metric="logloss",
    random_state=42
)

best_model.fit(X_train, y_train)

joblib.dump(best_model, os.path.join(MODEL_DIR, "tuned_model.pkl"))


results = {
    "best_score_cv_roc_auc": study.best_value,
    "best_parameters": study.best_params
}

with open(os.path.join(TUNING_DIR, "results.json"), "w") as f:
    json.dump(results, f, indent=4)

print("Tuning completed successfully!")
