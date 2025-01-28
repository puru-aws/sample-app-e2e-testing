from fastapi import FastAPI
from pydantic import BaseModel
from app.sentiment import analyze_sentiment

app = FastAPI()

# Define the input data model
class TextRequest(BaseModel):
    text: str

# Define an endpoint for sentiment analysis
@app.post("/analyze")
async def analyze(request: TextRequest):
    sentiment, score = analyze_sentiment(request.text)
    return {"sentiment": sentiment, "score": score}