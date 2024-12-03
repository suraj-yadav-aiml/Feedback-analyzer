from langchain_ollama import ChatOllama
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables.base import RunnableSequence

def build_sentiment_chain(llm: ChatOllama)->RunnableSequence:
    """Creates the sentiment classification chain."""
    sentiment_template = """Sentiment Classification Instructions:

    Review Analysis Criteria:
    - Determine overall sentiment of the review
    - Use ONLY the provided text
    - Classify strictly as 'Positive' or 'Negative'
    - Base decision on:
    * Emotional tone
    * Explicit sentiment indicators
    * Overall customer experience

    Review: {review}

    Output Requirements:
    - Single word response
    - Exact match: 'Positive' or 'Negative'
    - No additional explanation
    - No punctuation

    Classification:"""
    prompt = ChatPromptTemplate.from_template(template=sentiment_template)
    return prompt | llm | StrOutputParser()

def build_positive_chain(llm: ChatOllama)->RunnableSequence:
    """Creates the positive response generation chain."""
    positive_template = """Customer Appreciation Response Guidelines:

    Response Objectives:
    - Express genuine gratitude
    - Create emotional connection
    - Encourage social media sharing
    - Reinforce positive brand experience

    Response Components:
    1. Personalized acknowledgment
    2. Specific reference to review highlights
    3. Invitation to share experience
    4. Social media sharing encouragement

    Tone Requirements:
    - Warm and authentic
    - Enthusiastic
    - Professional
    - Conversational

    Key Sharing Platforms:
    - Instagram
    - Twitter/X
    - LinkedIn
    - Facebook

    Review: {review}
    """
    prompt = ChatPromptTemplate.from_template(template=positive_template)
    return prompt | llm | StrOutputParser()

def build_negative_chain(llm: ChatOllama)->RunnableSequence:
    """Creates the negative response generation chain."""
    negative_template = """Negative Review Response Protocol:

    Response Objectives:
    - Demonstrate genuine empathy
    - Take full accountability
    - Provide clear resolution pathway
    - Rebuild customer trust

    Response Framework:
    1. Sincere, personal apology
    2. Acknowledge specific concerns
    3. Offer concrete resolution steps
    4. Provide direct communication channel

    Tone Requirements:
    - Empathetic
    - Professional
    - Solution-oriented
    - Non-defensive

    Communication Guidelines:
    - Validate customer's experience
    - Avoid blame or justification
    - Show commitment to improvement
    - Offer private follow-up

    Customer Engagement:
    - Direct email for detailed discussion
    - Propose specific resolution
    - Request further details
    - Optional compensation/remedy

    Contact Information:
    Customer Care Email: abc.info@gmail.com

    Review: {review}
    """
    prompt = ChatPromptTemplate.from_template(template=negative_template)
    return prompt | llm | StrOutputParser()
