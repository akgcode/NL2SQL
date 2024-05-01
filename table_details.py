import pandas as pd
import streamlit as st
from operator import itemgetter
from langchain.chains.openai_tools import create_extraction_chain_pydantic
from langchain_core.pydantic_v1 import BaseModel, Field
from langchain_openai import ChatOpenAI
from langchain_community.utilities.sql_database import SQLDatabase

llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)
from typing import List
from pathlib import Path

import sqlite3
import glob
import os

# def extract_tables():
#     table_names = db.get_usable_table_names()

#     for table in table_names:

conn = sqlite3.connect(r'Songs.db')
path = r'data'
csv_files = glob.glob(os.path.join(path, "*.csv"))

print('Csv files are: ', csv_files)

for f in csv_files:
    if f == 'dataset.csv':
        songs_data = pd.read_csv(f)
        songs_data.to_sql('song', conn, if_exists='replace', index=False)

db = SQLDatabase.from_uri("sqlite:///Songs")

def get_table_details():
    # Read CSV file into d DataFrame
    table_description = pd.read_csv(r"data\database_details.csv")
    table_docs = []

    table_details = ""
    for index, row in table_description.iterrows():
        table_details = table_details + "Table Name:" + row['Table'] + "\n" + "Table Description:" + row['Description'] + "\n\n"
    return table_details

class Table(BaseModel):
    """Table in SQL database"""

    name: str = Field(description="Name of table in SQL database")

def get_tables(tables:List[Table]) -> List[str]:
    tables = [Table.name for table in tables]
    return tables

table_details = get_table_details()

table_details_prompt = f"""Return the names of All the SQL tables that might be relevant to the user question.
The tables are:

{table_details}

Remember to inlcude ALL POTENTIALLY RELEVANT tables, even if you're not sure that they're needed."""

table_chain = {"input": itemgetter("question")} | create_extraction_chain_pydantic(Table, llm, system_message= table_details_prompt) | get_tables