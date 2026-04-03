import numpy as np
from sklearn.base import BaseEstimator, TransformerMixin


class OutlierCapper(BaseEstimator, TransformerMixin):

    def fit(self, X, y=None):
        X = np.asarray(X)
        self.upper_ = np.quantile(X, 0.99, axis=0)
        self.lower_ = np.quantile(X, 0.01, axis=0)
        return self

    def transform(self, X):
        X = np.asarray(X)
        return np.clip(X, self.lower_, self.upper_)


class FeatureEngineer(BaseEstimator, TransformerMixin):

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        X = X.copy()

        X["TenureRatio"] = X["YearsAtCompany"] / (X["TotalWorkingYears"] + 1)
        X["PromotionWaitRatio"] = X["YearsSinceLastPromotion"] / (X["YearsAtCompany"] + 1)
        X["IncomePerYear"] = X["MonthlyIncome"] * 12
        X["CareerProgressionRatio"] = X["YearsInCurrentRole"] / (X["TotalWorkingYears"] + 1)
        X["IncomeStability"] = X["MonthlyIncome"] / (X["Age"] + 1)
        X["LongCommute"] = (X["DistanceFromHome"] > X["DistanceFromHome"].median()).astype(int)
        X["EarlyCareer"] = (X["TotalWorkingYears"] < 5).astype(int)
        X["ManagerChangeRisk"] = (X["YearsWithCurrManager"] < 2).astype(int)

        return X
