import os
import pandas as pd
import numpy as np
from scipy.stats import ks_2samp

BASELINE_PATH = "src/features/X_train.csv"
LOG_PATH = "src/prediction_logs.csv"


baseline = pd.read_csv(BASELINE_PATH)


if not os.path.exists(LOG_PATH):
    print("No prediction logs found.")
    exit()


new_data = pd.read_csv(LOG_PATH)

print("Checking drift...\n")

for column in baseline.columns:
    if column in new_data.columns:

        
        base_col = baseline[column].dropna()
        new_col = new_data[column].dropna()

        if len(new_col) < 10:
            print(f"Not enough data for drift check in: {column}")
            continue

        stat, p_value = ks_2samp(base_col, new_col)

        if p_value < 0.05:
            print(f"⚠ Drift detected in: {column} (p-value={p_value:.4f})")
        else:
            print(f"✓ No drift in: {column} (p-value={p_value:.4f})")

print("\nDrift check completed.")
