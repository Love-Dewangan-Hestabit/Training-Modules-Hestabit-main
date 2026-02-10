import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from scipy.stats import zscore
import os

RAW_PATH = "src/data/raw/WA_Fn-UseC_-HR-Employee-Attrition.csv"
PROCESSED_PATH = "src/data/processed/final.csv"

print("Loading data...")
df = pd.read_csv(RAW_PATH)
print("Initial shape:", df.shape)


# Handle missing values (SAFE)
print("Handling missing values...")
for col in df.columns:
    if df[col].dtype in ["int64", "float64"]:
        df[col] = df[col].fillna(df[col].median())
    else:
        df[col] = df[col].fillna(df[col].mode()[0])


# Remove duplicates
print("Removing duplicates...")
df = df.drop_duplicates()


# Outlier removal (ONLY continuous columns)
print("Removing outliers (continuous features only)...")

continuous_cols = [
    "Age",
    "MonthlyIncome",
    "DistanceFromHome",
    "TotalWorkingYears",
    "YearsAtCompany",
    "YearsInCurrentRole",
    "YearsSinceLastPromotion",
    "YearsWithCurrManager"
]

existing_cols = [col for col in continuous_cols if col in df.columns]

z_scores = np.abs(zscore(df[existing_cols]))
df = df[(z_scores < 3).all(axis=1)]

print("Shape after outlier removal:", df.shape)


# Scaling numerical features
print("⚖ Scaling numerical features...")

numeric_cols = df.select_dtypes(include=["int64", "float64"]).columns

if df.shape[0] == 0:
    raise ValueError("Dataset became empty after cleaning. Check outlier logic.")

scaler = StandardScaler()
df[numeric_cols] = scaler.fit_transform(df[numeric_cols])


# Save cleaned data
os.makedirs("src/data/processed", exist_ok=True)
df.to_csv(PROCESSED_PATH, index=False)

print("Day 1 pipeline completed successfully")
print("Final shape:", df.shape)
