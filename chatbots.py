import streamlit as st
import openai

# Set OpenRouter API base URL and your API key
openai.api_base = "https://openrouter.ai/api/v1"
openai.api_key = "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"

st.title("🤖 TORO Chatbot using OpenRouter via OpenAI Client")

if "messages" not in st.session_state:
    st.session_state.messages = []

def add_user_message(msg):
    st.session_state.messages.append({"role": "user", "content": msg})

def add_assistant_message(msg):
    st.session_state.messages.append({"role": "assistant", "content": msg})

user_input = st.text_input("Ask me anything...")

if st.button("Send") and user_input.strip():
    add_user_message(user_input)

    try:
        response = openai.ChatCompletion.create(
            model="openai/gpt-4o",  # Or your preferred OpenRouter model
            messages=st.session_state.messages,
            headers={
                "HTTP-Referer": "https://your-app-domain.com",  # Optional
                "X-Title": "TORO Chatbot",                       # Optional
            },
            temperature=0.7,
            max_tokens=150,
        )
        reply = response.choices[0].message.content
        add_assistant_message(reply)
    except Exception as e:
        st.error(f"API Error: {str(e)}")

if st.session_state.messages:
    for msg in st.session_state.messages:
        role = msg["role"]
        content = msg["content"]
        if role == "user":
            st.markdown(f"**You:** {content}")
        else:
            st.markdown(f"**Bot:** {content}")
