import streamlit as st
from openai import OpenAI

# Initialize OpenRouter client
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key="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",
)

st.title("🤖 TORO Chatbot")

if "messages" not in st.session_state:
    st.session_state.messages = []

def add_user_message(msg):
    st.session_state.messages.append({"role": "user", "content": msg})

def add_bot_message(msg):
    st.session_state.messages.append({"role": "assistant", "content": msg})

user_input = st.text_input("Ask your question:")

if st.button("Send") and user_input.strip():
    add_user_message(user_input)

    completion = client.chat.completions.create(
        extra_headers={
            "HTTP-Referer": "<YOUR_SITE_URL>",  # Optional
            "X-Title": "<YOUR_SITE_NAME>",      # Optional
        },
        model="openai/gpt-4o",
        messages=st.session_state.messages,
    )
    bot_reply = completion.choices[0].message.content
    add_bot_message(bot_reply)

if st.session_state.messages:
    for msg in st.session_state.messages:
        if msg["role"] == "user":
            st.markdown(f"**You:** {msg['content']}")
        else:
            st.markdown(f"**Bot:** {msg['content']}")
