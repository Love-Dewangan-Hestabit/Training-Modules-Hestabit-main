# Week 6 (Day 2) - Feature Engineering & Feature Selection Documentation

**Name: Love Dewangan**  
**Email: love.dewangan@hestabit.in**

## Task

To build a feature engineering pipeline that encodes categorical feature, Normalizes numerical features, generate new features and apply feature selection.

## Data Source

Input File:

```
   src/data/processed/final.csv
```

This dataset was generated in Day 1 after: - Handling missing values -
Removing duplicates - Removing outliers

No scaling or encoding was performed in Day 1 to avoid data leakage.

# Feature Engineering

The following new features were created:

## (1) TenureRatio

YearsAtCompany / (TotalWorkingYears + 1)

## (2) PromotionWaitRatio

YearsSinceLastPromotion / (YearsAtCompany + 1)

## (3) IncomePerYear

MonthlyIncome \* 12

## (4) CareerProgressionRatio

YearsInCurrentRole / (TotalWorkingYears + 1)

## (5) IncomeStability

MonthlyIncome / (Age + 1)

## (6) LongCommute

Binary flag: 1 if DistanceFromHome > median(DistanceFromHome) else 0

## (7) LowSatisfaction

Binary flag: 1 if JobSatisfaction ≤ 2 OR EnvironmentSatisfaction ≤ 2 else 0

## (8) LowWorkLifeBalance

Binary flag: 1 if WorkLifeBalance ≤ 2 else 0

## (9) EarlyCareer

Binary flag: 1 if TotalWorkingYears < 5 else 0

## (10) ManagerChangeRisk

Binary flag: 1 if YearsWithCurrManager < 2 else 0

## Train/Test Split

The dataset was split Before scaling and feature selection to prevent data leakage.

```
train_test_split(test_size=0.2, stratify=y)
```

This ensures:

- Test data remains completely unseen during training
- No leakage in preprocessing or feature selection

## Preprocessing Pipeline

I used sklearn Pipeline with ColumnTransformer.

### Numerical Features

- StandardScaler

### Categorical Features

- OneHotEncoder(handle_unknown="ignore")

Training data was only used for preprocessing

## Feature Selection

Feature selection was applied only on training data.

### Correlation Threshold

Removed highly correlated features (\> 0.9).

### Data Leakage Prevention

To prevent leakage:

- Scaling performed after train/test split
- Feature selection performed only on training data
- Test data never used during fitting

This ensures realistic model evaluation.
