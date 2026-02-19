# Week 6 (Day 4) - MODEL DEPLOYMENT, MONITORING and MLOPS CONCEPTS Analysis

**Name: Love Dewangan**  
**Email: love.dewangan@hestabit.in**

## Task

To deploy model as an API

## Model Information

- Algorithm: XGBoost
- Tuning Method: Optuna
- Evaluation Metric: ROC-AUC
- Model File: `tuned_model.pkl`
- Metadata File: `model_metadata.json`

## API Details

### Endpoint

POST /predict

### Sample Request Body

{ "feature1": value, "feature2": value }

### Response Format

{ "request_id": "uuid", "prediction": 0 or 1, "probability": 0.85 }

## Input Validation

- JSON schema validation using Pydantic
- Feature alignment using stored metadata
- Automatic rejection of missing or extra features

## Logging

All predictions are logged into:

`prediction_logs.csv`

Each log entry includes: - Timestamp - Request ID - Input features -
Predicted label - Probability score

## Monitoring

### Data Drift

- I used Kolmogorov-Smirnov (KS) test
- Compares baseline training distribution vs production predictions
- Drift flagged if p-value \< 0.05

## Model Versioning

Model metadata stores: - Version number - Training timestamp - Feature
schema - Best CV score

Allows: - Safe model upgrades - Rollback capability - Schema validation
in production

## Containerization

Deployment includes:

- Dockerfile
- requirements.txt
- .env.example
- README.md

Container can be built using:

docker build -t attrition-model .

Run using:

docker run -p 8000:8000 attrition-model
