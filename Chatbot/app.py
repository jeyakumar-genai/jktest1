import streamlit as st
import os
from dotenv import load_dotenv

from langchain.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationChain

# Load environment variables (ensure .env exists with your OpenAI key)
load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")

# Streamlit app title
st.title("💬 Conversational Chatbot (LangChain + OpenAI)")

# Set up conversational memory
if "memory" not in st.session_state:
    st.session_state.memory = ConversationBufferMemory(return_messages=True)

# Set up LLM (OpenAI GPT-3.5-Turbo by default)
llm = ChatOpenAI(
    model="gpt-3.5-turbo",
    temperature=0.7,
    api_key=openai_api_key
)

# Conversation chain
conversation = ConversationChain(
    llm=llm,
    memory=st.session_state.memory,
    verbose=False
)

st.markdown("Feel free to chat! This AI assistant will remember context within your session.")

# Streamlit chat UI
user_input = st.chat_input("Say something...")

if user_input:
    # Generate AI response
    response = conversation.predict(input=user_input)
    st.chat_message("user").write(user_input)
    st.chat_message("assistant").write(response)
