import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

st.set_page_config(page_title="Customer Support Chatbot", page_icon="🤖")

st.title("🤖 Customer Support Chatbot")
st.write("Ask me anything about your product, service, or issues!")


# Chat history
if "messages" not in st.session_state:
    st.session_state.messages = []


# User input
user_message = st.text_input("You:", placeholder="Type your message here...")

if user_message:
    st.session_state.messages.append({"role": "user", "content": user_message})

    # Send to OpenAI
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=st.session_state.messages
    )

    bot_reply = response.choices[0].message.content
    st.session_state.messages.append({"role": "assistant", "content": bot_reply})


# Display chat history
for msg in st.session_state.messages:
    if msg["role"] == "user":
        st.markdown(f"**🧑 You:** {msg['content']}")
    else:
        st.markdown(f"**🤖 Bot:** {msg['content']}")