# Lab 3: Chatbot page
# TODO: Rename this file to fit your page. Keep the number at the front.
#
# A chatbot built with Pydantic AI (see the Pydantic AI pages on Canvas).
# It should:
#   - use a Pydantic AI Agent with instructions that fit your project's theme (no tools yet)
#   - use Streamlit's chat elements: st.chat_message and st.chat_input
#   - remember the conversation (message_history, saved in st.session_state)
#   - use try/except so an error shows a message instead of crashing the page
#   - stay on theme, without using any API or external data
#
# Your Gemini API key goes in .streamlit/secrets.toml as GOOGLE_API_KEY.

import os
import asyncio
import streamlit as st
from pydantic_ai import Agent
from pydantic_ai.models.google import GoogleModel
from pydantic_ai.providers.google import GoogleProvider


st.set_page_config(page_title="AI Dev Mentor", page_icon="🤖")

st.title("🤖 AI Senior Software Developer Mentor")
st.write(
    "Ask questions about software engineering careers, algorithms, debugging strategies, "
    "or technical interview preparation!"
)

# Load API Key from .streamlit/secrets.toml into environment for Pydantic AI
if "GOOGLE_API_KEY" in st.secrets:
    os.environ["GEMINI_API_KEY"] = st.secrets["GOOGLE_API_KEY"]
    os.environ["GOOGLE_API_KEY"] = st.secrets["GOOGLE_API_KEY"]

# Initialize Pydantic AI Agent (No tools allowed in Lab 3)
@st.cache_resource
def get_dev_agent():
    provider = GoogleProvider(api_key=st.secrets["GOOGLE_API_KEY"])
    model = GoogleModel("gemini-2.5-flash", provider=provider)
    return Agent(
        model,
        system_prompt=(
            "You are a friendly, encouraging Senior Software Developer mentoring a computer science student. "
            "Keep your answers clear, practical, and concise (under 150 words unless asked for code examples). "
            "Focus on software engineering concepts, best practices, debugging mindset, and career advice. "
            "IMPORTANT: You do NOT have access to live external APIs, GitHub data, or the internet. "
            "If the user asks for live repository stats, exact star counts, or real-time data, politely explain "
            "that you cannot look up live data and direct them to the GitHub Explorer page."
        ),
    )

agent = get_dev_agent()

# Initialize session state for display messages and Pydantic AI message history
if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "assistant",
            "content": "Hey there! 👋 I'm your AI Senior Dev Mentor. What coding concept, project idea, or SWE career question are you working on today?"
        }
    ]

if "pydantic_history" not in st.session_state:
    st.session_state.pydantic_history = []

# Display chat history using Streamlit chat elements
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input box at the bottom
if user_prompt := st.chat_input("Ask your software developer mentor..."):
    # 1. Display and save user message
    st.session_state.messages.append({"role": "user", "content": user_prompt})
    with st.chat_message("user"):
        st.markdown(user_prompt)

    # 2. Generate AI response with Try/Except error handling
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            try:
                try:
                    asyncio.get_event_loop()
                except RuntimeError:
                    asyncio.set_event_loop(asyncio.new_event_loop())

                result = agent.run_sync(
                    user_prompt,
                    message_history=st.session_state.pydantic_history
                )
                reply = result.output
                st.markdown(reply)

                # Save updated history so the chatbot remembers the conversation
                st.session_state.pydantic_history = result.all_messages()
                st.session_state.messages.append({"role": "assistant", "content": reply})

            except Exception as e:
                st.error(f"Sorry, something went wrong: {e}")
