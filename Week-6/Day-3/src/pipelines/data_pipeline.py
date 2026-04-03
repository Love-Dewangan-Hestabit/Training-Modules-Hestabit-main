import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from scipy.stats import zscore
import os

RAW_PATH = "src/data/raw/Raw.csv"
PROCESSED_PATH = "src/data/processed/final.csv"

print("Loading data...")
df = pd.read_csv(RAW_PATH)
print("Initial shape:", df.shape)


print("Handling missing values...")
for col in df.columns:
    if df[col].dtype in ["int64", "float64"]:
        df[col] = df[col].fillna(df[col].median())
    else:
        df[col] = df[col].fillna(df[col].mode()[0])



print("Removing duplicates...")
df = df.drop_duplicates()



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


os.makedirs("src/data/processed", exist_ok=True)
df.to_csv(PROCESSED_PATH, index=False)

print("Day 1 pipeline completed successfully")
print("Final shape:", df.shape)
