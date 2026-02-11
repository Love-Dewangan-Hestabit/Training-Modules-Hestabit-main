import pandas as pd
import numpy as np
import os
import json

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline

from feature_selector import select_features


DATA_PATH = "src/data/processed/final.csv"
OUTPUT_DIR = "src/features"
os.makedirs(OUTPUT_DIR, exist_ok=True)

print("Loading processed dataset...")
df = pd.read_csv(DATA_PATH)


print("Generating new features...")

df["TenureRatio"] = df["YearsAtCompany"] / (df["TotalWorkingYears"] + 1)

df["PromotionWaitRatio"] = (
    df["YearsSinceLastPromotion"] / (df["YearsAtCompany"] + 1)
)

df["IncomePerYear"] = df["MonthlyIncome"] * 12

df["CareerProgressionRatio"] = (
    df["YearsInCurrentRole"] /
    (df["TotalWorkingYears"] + 1)
)

df["IncomeStability"] = df["MonthlyIncome"] / (df["Age"] + 1)

df["LongCommute"] = (
    df["DistanceFromHome"] > df["DistanceFromHome"].median()
).astype(int)

df["LowSatisfaction"] = (
    (df["JobSatisfaction"] <= 2) |
    (df["EnvironmentSatisfaction"] <= 2)
).astype(int)

df["LowWorkLifeBalance"] = (df["WorkLifeBalance"] <= 2).astype(int)

df["EarlyCareer"] = (df["TotalWorkingYears"] < 5).astype(int)

df["ManagerChangeRisk"] = (
    df["YearsWithCurrManager"] < 2
).astype(int)


X = df.drop("Attrition", axis=1)
y = df["Attrition"]

if y.dtype == "object":
    y = y.map({"Yes": 1, "No": 0})


X_train_raw, X_test_raw, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)



categorical_cols = X_train_raw.select_dtypes(include=["object", "string"]).columns
numerical_cols = X_train_raw.select_dtypes(include=["int64", "float64"]).columns



preprocessor = ColumnTransformer(
    transformers=[
        ("num", StandardScaler(), numerical_cols),
        ("cat", OneHotEncoder(handle_unknown="ignore"), categorical_cols),
    ]
)

pipeline = Pipeline(steps=[("preprocessor", preprocessor)])

print("Fitting preprocessing on TRAIN only...")

X_train_processed = pipeline.fit_transform(X_train_raw)
X_test_processed = pipeline.transform(X_test_raw)

cat_features = pipeline.named_steps["preprocessor"] \
    .named_transformers_["cat"] \
    .get_feature_names_out(categorical_cols)

all_features = list(numerical_cols) + list(cat_features)

X_train_df = pd.DataFrame(
    X_train_processed.toarray() if hasattr(X_train_processed, "toarray") else X_train_processed,
    columns=all_features
)

X_test_df = pd.DataFrame(
    X_test_processed.toarray() if hasattr(X_test_processed, "toarray") else X_test_processed,
    columns=all_features
)


print("Selecting features on TRAIN only...")
selected_features, _ = select_features(X_train_df, y_train)

X_train_selected = X_train_df[selected_features]
X_test_selected = X_test_df[selected_features]


with open(os.path.join(OUTPUT_DIR, "feature_list.json"), "w") as f:
    json.dump(selected_features, f, indent=4)



X_train_selected.to_csv(os.path.join(OUTPUT_DIR, "X_train.csv"), index=False)
X_test_selected.to_csv(os.path.join(OUTPUT_DIR, "X_test.csv"), index=False)
y_train.to_csv(os.path.join(OUTPUT_DIR, "y_train.csv"), index=False)
y_test.to_csv(os.path.join(OUTPUT_DIR, "y_test.csv"), index=False)

print("Leakage-free Day 2 pipeline completed successfully!")
print("Final selected feature count:", len(selected_features))
