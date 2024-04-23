import os

from dotenv import load_dotenv

load_dotenv()

db_user = os.getenv("db_user")
db_password = os.getenv("db_password")
db_host = os.getenv("db_host")
db_name = os.getenv("db_name")
os.environ["OPENAI_API_KEY"] = 'sk-proj-tOKrREM5RbEDmNr5n10lT3BlbkFJluavcVJZEUbj4uRRiL9i'
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

from langchain_community.utilities.sql_database import SQLDatabase
from langchain.chains import create_sql_query_chain
from langchain_openai import ChatOpenAI
from langchain_community.tools.sql_database.tool import QuerySQLDataBaseTool
from langchain.memory import ChatMessageHistory
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser

from operator import itemgetter

from table_details import table_chain as select_table
from prompts import final_prompt, answer_prompt

import streamlit as st
@st.cache_resource
def get_chain():
    print('creating chain')
    db = SQLDatabase.from_uri()
    llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)
    generate_query= create_sql_query_chain(llm,db,final_prompt)
    execute_query = QuerySQLDataBaseTool(db=db)
    rephrase_answer = answer_prompt | llm | StrOutputParser()
    chain = (
        RunnablePassthrough.assign(query= generate_query).assign(
            result= itemgetter("query") | execute_query
        )
        | rephrase_answer
    )
    return chain

def create_history(messages):
    history = ChatMessageHistory()
    for message in messages:
        if message["role"] == "user":
            history.add_user_message(message["content"])
        else:
            history.add_ai_message(message["content"])
    return history

def invoke_chain(question,messages):
    chain = get_chain()
    history = create_history(messages)

    try:
        response = chain.invoke({"question": question, "top_k": 3, "messages": history.messages})
        history.add_user_message(question)
        history.add_ai_message(response)

    except Exception as e:
        print (e)
    
    if response:
        return response
