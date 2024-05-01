from main import *
from openai import OpenAI
from langchain_utils import invoke_chain
import os
from dotenv import load_dotenv

make_sidebar()

st.markdown(f"Welcom **{username}")
st.title("Langchain NL2SQL Chatbot")

#set OpenAI API key from streamlit secrets
api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)

#Set s default model
if "openai_model" not in st.session_state:
    st.session_state["openai_model"] = "gpt-3.5-turbo"

#Initialize chat history
if "messages" not in st.session_state:
    # print("Creating session state")
    st.session_state.messages =[]

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

#Accept user input
if prompt := st.chat_input("What is up?"):
    #Add user message to char history
    st.session_state.messages.append({"role":"user", "content": prompt})
    #Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)
    
    #Display assistant response in chat message container
    with st.spinner("Generating response"):
        with st.chat_message("assistant"):
            response = invoke_chain(prompt, st.session_state.messages)
            st.markdown(response)
    st.session_state.messages.append({"role":"assistant", "content": response})
