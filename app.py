import streamlit as st
from langchain.schema import HumanMessage, AIMessage
from chatbot import ask_question   # ✅ Import function

st.set_page_config(page_title="Groq Q/A Chatbot", page_icon="🤖")
st.title("🤖 Basic Q/A Chatbot (LangChain + Groq)")

# Chat history
if "messages" not in st.session_state:
    st.session_state["messages"] = []

# Show chat history
for msg in st.session_state["messages"]:
    with st.chat_message("user" if isinstance(msg, HumanMessage) else "assistant"):
        st.markdown(msg.content)

# User input
if prompt := st.chat_input("Ask me anything..."):
    user_msg = HumanMessage(content=prompt)
    st.session_state["messages"].append(user_msg)

    with st.chat_message("user"):
        st.markdown(prompt)

    # ✅ Call ask_question() from chatbot.py
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        answer = ask_question(prompt)
        message_placeholder.markdown(answer)

    st.session_state["messages"].append(AIMessage(content=answer))
