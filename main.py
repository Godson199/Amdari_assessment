import joblib
import pandas as pd
from fastapi import FastAPI
from schemas import Transaction

# Load the trained pipeline
model = joblib.load("rf_fraud_detection_pipeline.pkl")

app = FastAPI(title="Fraud Detection API")

@app.post("/predict")
async def predict_transaction(data: Transaction):

    # Convert Pydantic model → DataFrame
    df = pd.DataFrame([data.dict()])

    # Make prediction
    prediction = model.predict(df)[0]
    probability = model.predict_proba(df)[0][1]

    return {
        "is_fraud": int(prediction),
        "fraud_probability": float(probability)
    }
