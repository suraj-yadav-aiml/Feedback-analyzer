
from langchain_core.runnables import RunnableLambda,RunnablePassthrough,RunnableSequence
from typing import Dict

def route_response(info: Dict[str, str], positive_chain:RunnableSequence, negative_chain:RunnableSequence)->RunnableSequence:
    """Routes the feedback chain based on sentiment."""
    sentiment = info["sentiment"].lower()
    if sentiment == "positive":
        return positive_chain
    return negative_chain

def create_feedback_chain(sentiment_chain:RunnableSequence,positive_chain:RunnableSequence, negative_chain:RunnableSequence)->RunnableSequence:
    """
    Creates the feedback routing chain.

    Args:
        sentiment_chain: Sentiment classification chain.
        positive_chain: Positive response chain.
        negative_chain: Negative response chain.

    Returns:
        RunnableLambda: Complete feedback routing chain.
    """
    return {
        "sentiment": sentiment_chain,
        "review": RunnablePassthrough()
    } | RunnableLambda(lambda info: route_response(info, positive_chain, negative_chain))
