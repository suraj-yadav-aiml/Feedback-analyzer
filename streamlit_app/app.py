import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000/process-feedback/"

st.set_page_config(
    page_title="Feedback Analyzer",
    page_icon="💬",
    layout="wide",
    initial_sidebar_state="expanded"
)

# App Header
st.markdown(
    """
    <style>
    .main-header {
        font-size: 40px;
        font-weight: bold;
        color: #4CAF50;
        text-align: center;
        margin-bottom: 20px;
    }
    .sub-header {
        font-size: 20px;
        text-align: center;
        color: #555;
        margin-bottom: 30px;
    }
    </style>
    <div class="main-header">💬 Feedback Analyzer</div>
    <div class="sub-header">Classify feedback sentiment and generate customized responses instantly.</div>
    """,
    unsafe_allow_html=True,
)

# Input Section
st.markdown("### 🚀 Enter Customer Feedback Below:")
review = st.text_area(
    label="Feedback Text",
    placeholder="Type or paste customer feedback here...",
    height=150
)

# Sidebar
with st.sidebar:
    st.markdown("### 🛠️ App Settings")
    st.markdown(
        """
        Adjust API configuration:
        - **Endpoint**: `http://127.0.0.1:8000`
        """
    )

# Submit Button
if st.button("Analyze Feedback 💡"):
    if not review.strip():
        st.error("Please enter feedback text before submitting!")
    else:
        with st.spinner("Analyzing feedback..."):
            try:
                # Send API Request
                response = requests.post(API_URL, json={"review": review})
                if response.status_code == 200:
                    data = response.json()
                    sentiment = "Positive" if "positive" in data["sentiment"].lower() else "Negative"
                    
                    # Display Results
                    st.success("Feedback successfully analyzed!")
                    st.markdown(f"### Sentiment: **{sentiment}**")
                    st.markdown("### 💬 Generated Response:")
                    st.markdown(f"```{data['response']}```")
                else:
                    st.error("Error: Unable to process feedback. Please try again.")
            except Exception as e:
                st.error(f"Error: {str(e)}")

# Footer
st.markdown(
    """
    ---
    <div style="text-align: center; font-size: 14px; color: #888;">
        Made with ❤️ using Streamlit and FastAPI.
    </div>
    """,
    unsafe_allow_html=True,
)
