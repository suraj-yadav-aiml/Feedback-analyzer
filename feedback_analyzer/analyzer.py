from langchain_openai import ChatOpenAI
from config import MODEL_NAME, TEMPERATURE
from chains import build_sentiment_chain, build_positive_chain, build_negative_chain
from routes import create_feedback_chain

from dotenv import load_dotenv
load_dotenv()

class FeedbackAnalyzer:
    """
    FeedbackAnalyzer processes customer reviews to classify sentiment
    and generate appropriate responses.
    """
    def __init__(self):
        self.llm = ChatOpenAI(model=MODEL_NAME,temperature=TEMPERATURE)
        self.sentiment_chain = build_sentiment_chain(self.llm)
        self.positive_chain = build_positive_chain(self.llm)
        self.negative_chain = build_negative_chain(self.llm)
        self.feedback_chain = create_feedback_chain(
            self.sentiment_chain, self.positive_chain, self.negative_chain
        )

    def process_feedback(self, review: str) -> str:
        """
        Processes a customer review and generates a response.

        Args:
            review (str): The customer review text.

        Returns:
            str: The generated response.
        """
        try:
            return self.feedback_chain.invoke(input={"review": review})
        except Exception as e:
            raise RuntimeError(f"Error processing feedback: {e}")
    
    def process_sentiment(self,review: str) -> str:
        try:
            return self.sentiment_chain.invoke(input={'review': review})
        except Exception as e:
            raise RuntimeError(f"Error processing review: {e}")

if __name__ == "__main__":
    try:
        analyzer = FeedbackAnalyzer()
        review = "Thank you so much for providing such a great platform for learning. I am really happy with the service."
        review_sentiment = analyzer.process_sentiment(review)
        feedback_reply = analyzer.process_feedback(review)
        print(review_sentiment)
        print(feedback_reply)
    except RuntimeError as e:
        print(f"An error occurred: {e}")
