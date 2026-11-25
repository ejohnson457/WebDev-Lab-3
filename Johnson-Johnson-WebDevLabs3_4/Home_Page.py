import streamlit as st

st.set_page_config(page_title="DevPulse: Software Engineering Explorer", page_icon="💻")

st.title("💻 DevPulse: Software Developer Explorer")
st.subheader("CS 1301 Web Dev Lab 3")

st.write(
    """
    Welcome to **DevPulse**, an interactive web application built for aspiring and current 
    **Software Developers**. Computing relies heavily on open-source collaboration, version control, 
    and community-driven tools. This app lets you explore real-time open-source repository trends 
    and chat with an AI software engineering mentor.
    """
)

st.markdown("### 📌 App Navigation")
st.markdown(
    """
    - **Page 1 (`2_GitHub_Explorer.py`):** Analyze top GitHub repositories by programming language, 
      filter by minimum star count, and compare repository metrics dynamically.
    - **Page 2 (`3_Dev_Mentor_Chat.py`):** Chat with an AI Senior Software Developer powered by 
      Google Gemini and Pydantic AI for career advice, coding concepts, and interview prep.
    """
)

st.info("👈 Use the sidebar on the left to navigate between pages!")
