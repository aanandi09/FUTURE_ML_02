import streamlit as st
from openai import OpenAI
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

st.set_page_config(
    page_title="Customer Support Chatbot",
    page_icon="💬",
    layout="centered"
)

# ---------------- CSS ----------------
st.markdown("""
<style>
/* Force full background */
html, body, [class*="st-"] {
    background-color: #fff1f5 !important;
}

/* Chat container */
.chat-container {
    max-width: 80px;
    margin: auto;
}

/* User message bubble */
.user-bubble {
    background-color: #fbcfe8;
    color: #1f2937;
    padding: 12px 16px;
    border-radius: 18px;
    margin: 10px 0;
    width: fit-content;
    max-width: 80%;
    margin-left: auto;
}

/* Bot message bubble */
.bot-bubble {
    background-color: #ffffff;
    color: #1f2937;
    padding: 12px 16px;
    border-radius: 18px;
    margin: 10px 0;
    width: fit-content;
    max-width: 80%;
    border: 1px solid #f9a8d4;
    margin-right: auto;
}

/* Input box */
textarea {
    background-color: #ffffff !important;
    border-radius: 12px;
}
</style>
""", unsafe_allow_html=True)

# ---------------- UI ----------------
st.markdown("<h1 class='chat-title'>💬 AI Customer Support Chatbot</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center;'>Ask about products, orders, payments, or support issues.</p>", unsafe_allow_html=True)

if "messages" not in st.session_state:
    st.session_state.messages = []

st.markdown("<div class='chat-container'>", unsafe_allow_html=True)

# Display messages
for msg in st.session_state.messages:
    if msg["role"] == "user":
        st.markdown(
            f"<div class='user-bubble'>{msg['content']}</div>",
            unsafe_allow_html=True
        )
    else:
        st.markdown(
            f"<div class='bot-bubble'>{msg['content']}</div>",
            unsafe_allow_html=True
        )

st.markdown("</div>", unsafe_allow_html=True)

# User input
user_input = st.chat_input("Ask your question here...")

if user_input:
    st.session_state.messages.append(
        {"role": "user", "content": user_input}
    )

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=st.session_state.messages
    )

    bot_reply = response.choices[0].message.content

    st.session_state.messages.append(
        {"role": "assistant", "content": bot_reply}
    )

    st.rerun()
