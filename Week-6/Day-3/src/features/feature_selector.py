import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.feature_selection import mutual_info_classif, RFE
from sklearn.linear_model import LogisticRegression


def correlation_filter(X, threshold=0.9):
    corr_matrix = X.corr().abs()
    upper = corr_matrix.where(
        np.triu(np.ones(corr_matrix.shape), k=1).astype(bool)
    )
    to_drop = [column for column in upper.columns if any(upper[column] > threshold)]
    return X.drop(columns=to_drop)


def select_features(X, y):
    print("Applying correlation threshold...")
    X_filtered = correlation_filter(X)

    print("Applying Mutual Information...")
    mi_scores = mutual_info_classif(X_filtered, y)
    mi_series = pd.Series(mi_scores, index=X_filtered.columns)

    top_mi_features = mi_series.sort_values(ascending=False).head(30).index

    print("Applying RFE...")
    model = LogisticRegression(max_iter=1000)
    rfe = RFE(model, n_features_to_select=20)
    rfe.fit(X_filtered[top_mi_features], y)

    selected_features = X_filtered[top_mi_features].columns[rfe.support_]

    
    plt.figure(figsize=(10, 6))
    mi_series[selected_features].sort_values().plot(kind="barh")
    plt.title("Selected Feature Importance (Mutual Information)")
    plt.tight_layout()
    plt.savefig("src/features/feature_importance.png")
    plt.close()

    return list(selected_features), mi_series[selected_features]
