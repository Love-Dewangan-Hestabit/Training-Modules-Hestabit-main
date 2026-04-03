import os
import uuid
import joblib
import pandas as pd
from datetime import datetime
from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional


PROJECT_ROOT = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "../../")
)

SRC_DIR = os.path.join(PROJECT_ROOT, "src")

MODEL_PATH = os.path.join(
    SRC_DIR, "models", "production_pipeline.pkl"
)

LOG_PATH = os.path.join(
    SRC_DIR, "prediction_logs.csv"
)


os.makedirs(SRC_DIR, exist_ok=True)

print("Model Path:", MODEL_PATH)
print("Log Path:", LOG_PATH)



if not os.path.exists(MODEL_PATH):
    raise FileNotFoundError(f"Model not found at {MODEL_PATH}")

artifact = joblib.load(MODEL_PATH)

pipeline = artifact["pipeline"]
expected_columns = artifact["expected_columns"]


app = FastAPI(title="Attrition Prediction API")



class PredictionInput(BaseModel):
    Age: Optional[int] = None
    MonthlyIncome: Optional[float] = None
    DistanceFromHome: Optional[float] = None
    TotalWorkingYears: Optional[float] = None
    YearsAtCompany: Optional[float] = None
    YearsInCurrentRole: Optional[float] = None
    YearsSinceLastPromotion: Optional[float] = None
    YearsWithCurrManager: Optional[float] = None
    JobSatisfaction: Optional[int] = None
    EnvironmentSatisfaction: Optional[int] = None
    WorkLifeBalance: Optional[int] = None
    Gender: Optional[str] = None
    MaritalStatus: Optional[str] = None
    BusinessTravel: Optional[str] = None



class PredictionOutput(BaseModel):
    request_id: str
    prediction: int
    probability: float
    timestamp: str



@app.get("/")
def health():
    return {"status": "API Running"}



@app.post("/predict", response_model=PredictionOutput)
async def predict(data: PredictionInput):

    request_id = str(uuid.uuid4())
    timestamp = datetime.utcnow().isoformat()

    try:

        user_input = data.model_dump(exclude_none=True)


        full_input = {col: None for col in expected_columns}


        for key, value in user_input.items():
            if key in full_input:
                full_input[key] = value

        input_df = pd.DataFrame([full_input])


        probability = pipeline.predict_proba(input_df)[0][1]
        prediction = int(probability >= 0.5)


        try:
            log_entry = {
                **full_input,
                "prediction": prediction,
                "probability": float(probability),
                "request_id": request_id,
                "timestamp": timestamp
            }

            log_df = pd.DataFrame([log_entry])

            log_df.to_csv(
                LOG_PATH,
                mode="a",
                header=not os.path.exists(LOG_PATH),
                index=False
            )

            print("Log written successfully.")

        except Exception as log_error:
            print("Logging failed:", log_error)

        return PredictionOutput(
            request_id=request_id,
            prediction=prediction,
            probability=round(probability, 4),
            timestamp=timestamp
        )

    except Exception as e:
        print("Prediction error:", e)

        return PredictionOutput(
            request_id=request_id,
            prediction=-1,
            probability=0.0,
            timestamp=timestamp
        )
