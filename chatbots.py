import streamlit as st
import requests

# Your OpenRouter API key (keep secret and safe)
API_KEY = "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"

# OpenRouter chat completions endpoint
API_URL = "https://openrouter.ai/api/v1/chat/completions"

headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json",
    # Optional headers to identify your app on OpenRouter site:
    # "HTTP-Referer": "https://your-app-url.com",
    # "X-Title": "TORO Chatbot",
}

st.title("🤖 TORO Chatbot using OpenRouter API")

user_input = st.text_input("Type your question or message here:")

# Keep conversation history in session state for multi-turn (optional)
if "conversation" not in st.session_state:
    st.session_state.conversation = []

if st.button("Send") and user_input.strip():
    # Append user input to conversation history
    st.session_state.conversation.append({"role": "user", "content": user_input})

    # Prepare payload with conversation messages
    data = {
        "model": "deepseek/deepseek-v3.2-exp",  # Use your chosen model here
        "messages": st.session_state.conversation,
        "temperature": 0.7,
        "max_tokens": 150,
        "stream": False  # Set True for streaming responses (advanced)
    }

    response = requests.post(API_URL, headers=headers, json=data)

    if response.status_code == 200:
        result = response.json()
        assistant_message = result['choices'][0]['message']['content']
        # Append assistant reply to conversation history
        st.session_state.conversation.append({"role": "assistant", "content": assistant_message})
        st.markdown(f"**Answer:** {assistant_message}")
    else:
        st.error(f"API error {response.status_code}: {response.text}")

# Optionally show full conversation
if st.checkbox("Show conversation history"):
    for msg in st.session_state.conversation:
        role = msg['role'].capitalize()
        st.markdown(f"**{role}:** {msg['content']}")
