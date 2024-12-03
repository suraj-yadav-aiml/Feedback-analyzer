from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from feedback_analyzer.analyzer import FeedbackAnalyzer

app = FastAPI(
    title="Feedback Analyzer API",
    description="API for processing customer feedback and generating responses.",
    version="1.0.0"
)

analyzer = FeedbackAnalyzer()


class FeedbackRequest(BaseModel):
    review: str

@app.get("/")
def root():
    """
    Health check endpoint for the API.
    """
    return {"message": "Feedback Analyzer API is running!"}

@app.post("/process-feedback/")
def process_feedback(feedback: FeedbackRequest):
    """
    Endpoint to process customer feedback and generate a response.

    Args:
        feedback (FeedbackRequest): Input review text.

    Returns:
        dict: Sentiment classification and response text.
    """
    try:
        response = analyzer.process_feedback(feedback.review)
        review_sentiment = analyzer.process_sentiment(feedback.review)
        return {"review": feedback.review, "sentiment":review_sentiment, "response": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# uvicorn api.main:app --reload