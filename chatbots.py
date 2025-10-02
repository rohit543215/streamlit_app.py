import streamlit as st
import requests

# Your OpenRouter API key
API_KEY = "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"

# OpenRouter API endpoint
API_URL = "https://openrouter.ai/api/v1/chat/completions"

headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json",
}

st.title("TORO Chatbot using Deepseek Model via OpenRouter API")

user_input = st.text_input("Ask me anything...")

if st.button("Send") and user_input.strip():
    data = {
        "model": "deepseek-v3.2-exp",  # Use desired model
        "messages": [
            {"role": "user", "content": user_input}
        ],
        "temperature": 0.7,
        "max_tokens": 150,
    }

    response = requests.post(API_URL, headers=headers, json=data)

    if response.status_code == 200:
        result = response.json()
        answer = result['choices'][0]['message']['content']
        st.markdown(f"**Answer:** {answer}")
    else:
        st.error(f"API error: {response.status_code} - {response.text}")
