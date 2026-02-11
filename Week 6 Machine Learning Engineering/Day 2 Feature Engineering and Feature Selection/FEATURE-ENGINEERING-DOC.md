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

## (1) IncomePerYear

MonthlyIncome \* 12 / (TotalWorkingYears + 1)

## (2) TenureRatio

YearsAtCompany / (TotalWorkingYears + 1)

## (3) PromotionGap

YearsAtCompany - YearsSinceLastPromotion

## (4) ExperienceLevel

Binary flag: 1 if TotalWorkingYears \> 10 else 0

## (5) IncomeStability

MonthlyIncome / (Age + 1)

## (6) RoleStability

YearsInCurrentRole / (YearsAtCompany + 1)

## (7) ManagerStability

YearsWithCurrManager / (YearsAtCompany + 1)

## (8) FarFromOffice

Binary flag: 1 if DistanceFromHome \> 20 else 0

## (9) WorkLifeInteraction

JobSatisfaction \* EnvironmentSatisfaction

## (10) LogDistanceFromHome

log1p(DistanceFromHome - min + 1)

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
