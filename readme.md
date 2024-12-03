# Feedback Analyzer: Customer Sentiment and Response Generator

![Feedback Analyzer Banner](https://via.placeholder.com/800x200.png?text=Feedback+Analyzer+%7C+Sentiment+Analysis+and+Response+Generation)

## 🌟 **Overview**
**Feedback Analyzer** is a robust application designed to classify customer feedback sentiment (Positive or Negative) and generate custom responses using the power of **LangChain** and **OpenAI LLMs**. The project integrates:
- **FastAPI**: For a production-ready REST API.
- **Streamlit**: For an interactive and engaging front-end application.
- **LangChain**: For advanced prompt-based large language model interaction.
- **Environment Variables**: Uses `.env` to manage sensitive API keys securely.


---

## 🚀 **Features**
1. **Sentiment Analysis**: Classifies feedback as Positive or Negative based on emotional tone, explicit indicators, and overall customer experience.
2. **Custom Responses**: 
   - Positive feedback: Generates warm and encouraging responses.
   - Negative feedback: Generates empathetic and solution-oriented responses.
3. **REST API**: A FastAPI-based API to integrate feedback analysis with other services.
4. **Interactive UI**: A Streamlit-based front-end for end-users to interact with the system seamlessly.
5. **Secure API Key Management**: API keys are securely stored in an `.env` file (ignored in `.gitignore`).

---

## 📂 **Project Structure**
```
feedback_analyzer/
    __init__.py
    config.py                 # Configuration file for LLM and app settings
    chains.py                 # LangChain prompt templates and response chains
    routes.py                 # Feedback routing logic
    analyzer.py               # FeedbackAnalyzer class for processing feedback
api/
    __init__.py
    main.py                   # FastAPI application
streamlit_app/
    app.py                    # Streamlit app
.env.example                  # Example environment variable file
README.md                     # Documentation file
requirements.txt              # Project dependencies
.gitignore                    # Git ignore file including .env
```

---

## 🛠️ **Technologies Used**
1. **Python 3.10+**
2. **FastAPI**
3. **Streamlit**
4. **LangChain**
5. **LangChain OpenAI**
6. **Requests**
7. **dotenv**: For environment variable management.

---

## 📦 **Setup Instructions**
### Prerequisites
- Python 3.10+
- `pip` (Python package manager)
- OpenAI API Key (sign up at [OpenAI](https://platform.openai.com/signup))

### Clone the Repository
```bash
git clone https://github.com/your-username/feedback-analyzer.git
cd feedback-analyzer
```

### Install Dependencies
Install all required packages:
```bash
pip install -r requirements.txt
```

---

## 📋 **Environment Variables**
1. Create a `.env` file in the project root (same level as `README.md`).
2. Add your OpenAI API key:
```plaintext
OPENAI_API_KEY=your-openai-api-key
```

### Example `.env`
For users, a sample `.env.example` is provided. Rename it to `.env` and add your OpenAI API key:
```plaintext
# .env.example
OPENAI_API_KEY=your-openai-api-key
```

---

## 🚀 **How to Run the Application**

### 1. Start the FastAPI Server
Navigate to the **API directory** and run the FastAPI server:
```bash
cd feedback_analyzer/api
uvicorn main:app --reload
```
- Access API documentation at [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs).
- Test the API health check at [http://127.0.0.1:8000/](http://127.0.0.1:8000/).

### 2. Run the Streamlit Front-End
In a new terminal, navigate to the **Streamlit app directory** and start the app:
```bash
cd streamlit_app
streamlit run app.py
```
- Access the UI at [http://localhost:8501](http://localhost:8501).

---

## 📖 **How to Use**
### Using the Streamlit App
1. Enter customer feedback into the text area.
2. Click on **Analyze Feedback 💡**.
3. View:
   - **Sentiment**: Positive or Negative.
   - **Generated Response**: Tailored to the feedback sentiment.

### Using the FastAPI API
#### 1. Analyze Feedback
- **Endpoint**: `POST /process-feedback/`
- **Request**:
    ```json
    {
        "review": "The service was excellent and exceeded expectations!"
    }
    ```
- **Response**:
    ```json
    {
        "review": "The service was excellent and exceeded expectations!",
        "response": "Thank you for your amazing review! We're thrilled to hear..."
    }
    ```

---

## ⚙️ **Configuration**
You can modify the following in `config.py`:
- **MODEL_NAME**: OpenAI model used for processing (e.g., `gpt-4`, `gpt-3.5-turbo`).
- **TEMPERATURE**: Controls LLM response randomness.

---

## 🛡️ **Error Handling**
1. **FastAPI**:
   - Returns HTTP status codes with meaningful error messages for API issues.
2. **Streamlit**:
   - Validates inputs and handles API failures with user-friendly messages.

---

## 🏗️ **Future Improvements**
1. **Authentication**: Secure the API with JWT or OAuth2.
2. **Database Integration**: Store feedback and responses for analytics.
3. **Deployment**: Containerize the app with Docker for easy deployment.
4. **Multi-Language Support**: Expand to handle reviews in different languages.
5. **Dashboard**: Add visual analytics for feedback trends.

---

## 🤝 **Contributing**
Contributions are welcome! Feel free to submit issues or pull requests.

---

## 💬 **Acknowledgments**
- **LangChain**: For providing powerful tools for LLM integrations.
- **FastAPI**: For creating a robust and easy-to-use API framework.
- **Streamlit**: For building interactive front-end applications.

---

Let me know if you need any further adjustments or improvements!