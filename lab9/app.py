import streamlit as st

st.set_page_config(page_title="Chatbot", page_icon="💬")
st.title("Lab 9: Chatbot Interface")
st.caption("A simple demo chatbot interface with session-based chat history.")

if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Hello! Ask me about Streamlit, Python, or data analysis."}
    ]

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

prompt = st.chat_input("Type your message")
if prompt:
    st.session_state.messages.append({"role": "user", "content": prompt})
    text = prompt.lower()
    if "streamlit" in text:
        reply = "Streamlit is a Python framework for building interactive data apps."
    elif "python" in text:
        reply = "Python is a programming language often used for data analysis and machine learning."
    elif "data" in text:
        reply = "Data analysis often includes cleaning, exploration, visualization, and interpretation."
    elif "hello" in text or "hi" in text:
        reply = "Hello! How can I help you learn today?"
    else:
        reply = "This is a demo chatbot. Try asking about Python, Streamlit, or data analysis."
    st.session_state.messages.append({"role": "assistant", "content": reply})
    st.rerun()

if st.button("Clear chat"):
    st.session_state.messages = []
    st.rerun()
