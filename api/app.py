from fastapi import FastAPI
from pydantic import BaseModel

from src.inference import predict

app = FastAPI(title="Colombia Election Sentiment API")

# estructura de entrada
class TextInput(BaseModel):
    text: str

# endpoint principal
@app.get("/")
def home():
    return {"message": "Colombia Election Sentiment API is running 🚀"}

# endpoint de predicción
@app.post("/predict")
def predict_sentiment(data: TextInput):
    result = predict(data.text)
    return {
        "text": data.text,
        "sentiment": result
    }