import streamlit as st
import requests

# API key for Gemini (or your respective chatbot API)
API_KEY = "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"

# Define the API endpoint
API_URL = "https://api.gemini.com/chat"  # Replace with the correct Gemini API endpoint

# Function to get chatbot response using the API
def get_chatbot_response(message):
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    # Create the payload based on API's expected format
    payload = {
        "message": message  # Update based on Gemini's expected format
    }

    # Send the request to the Gemini API
    try:
        response = requests.post(API_URL, json=payload, headers=headers)
        response.raise_for_status()  # Raise an error if the response is not successful
        data = response.json()

        # Print the response for debugging purposes
        print("API Response:", data)
        
        if "response" in data:
            return data["response"]  # Adjust based on the actual response format
        else:
            return "Sorry, I couldn't understand that."
    except requests.exceptions.RequestException as e:
        print("Error during API request:", e)
        return "Sorry, there was an error with the chatbot service."

# Streamlit UI setup
st.title("Gemini Chatbot")

# Create a chat history container
if "chat_history" not in st.session_state:
    st.session_state["chat_history"] = []

# Input area for the user message
user_message = st.text_input("You: ", "")

# If the user sends a message
if user_message:
    # Get response from Gemini API
    bot_response = get_chatbot_response(user_message)
    
    # Store the chat history
    st.session_state["chat_history"].append({"user": user_message, "bot": bot_response})

# Display the chat history
if st.session_state["chat_history"]:
    for chat in st.session_state["chat_history"]:
        st.write(f"**You:** {chat['user']}")
        st.write(f"**Bot:** {chat['bot']}")
