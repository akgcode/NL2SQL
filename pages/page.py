from main import *
import os
from openai import OpenAI
from pathlib import Path
import pandas as pd
from dotenv import load_dotenv
from langchain_community.callbacks import get_openai_callback
from datetime import datetime

load_dotenv()
st.markdown(f"Welcome **{username}")
st.title("Langchain NL2SQL chatbot")

#set OpenAI API key from streamlit secrets
api_key = os.getenv("OPENAI_API_KEY")
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
                print("Hitting openai callback function")
                MODEL_NAME = "gpt-3.5-turbo"
                start_time = timer()
                with get_openai_callback() as cb:
                    response = invoke_chain(prompt, st.session_state.messages)
                    st.markdown(response)
                    end_time = timer()
                    model_time_execution = end_time - start_time
                    tpm = (cb.total_tokens*60)/model_time_execution
                    now_time = pd.to_datetime(datetime.now().strftime('%d/%m/%Y, %H:%M:%S'))

                    cost_df = pd.DataFrame({'Time': now_time,
                                           'model': MODEL_NAME,
                                           'total_tokens':cb.total_tokens,
                                           'prompt_tokens':cb.prompt_tokens,
                                           'completion_tokens':cb.completion_tokens,
                                           'model_execution_time_sec':model_time_execution,
                                           'total_cost_USD':cb.total_cost,
                                           'TPM':tpm},
                                           index= [0])
                    file_path = r'data]poc_cost_record.csv'
                    if not os.path.isfile(file_path):
                        cost_df.to_csv(file_path, index=False)
                    else:
                        cost_df.to_csv(file_path, mode='a', header=False, index=False)

        st.session_state.messages.append({"role":"assistant", "content": response})

