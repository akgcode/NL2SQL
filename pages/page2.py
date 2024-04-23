from main import *
import os
from openai import OpenAI
from pathlib import Path
import pandas as pd
st.markdown(f"Welcome **{username}")
st.title("Langchain NL2SQL chatbot")

#set OpenAI API key from streamlit secrets
from dotenv import load_dotenv
api_key = 'sk-proj-tOKrREM5RbEDmNr5n10lT3BlbkFJluavcVJZEUbj4uRRiL9i'
client = OpenAI(api_key=api_key)

files_uploaded = st.file_uploader('**Database Uploader :red[:warning: No Client Data]**', accept_multiple_files=True, type=['.db','.csv'])

for file in files_uploaded:
    if file is not None:
        if Path(file.name).suffix=='.csv':

            df = pd.read_csv(file)
            df.to_csv(r'data\dataset.csv')
            st.dataframe(df)

if files_uploaded:
    from langchain_utils import invoke_chain
    
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

