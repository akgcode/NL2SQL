# NL2SQL
From Natural Language to SQL query generator
## Natural Language to SQL | SQL Query Generator using Langchain 🦜️🔗 
This repository contains code for a Streamlit application for interaction with SQLite3 database or a csv using natural language and generate the SQL query and consequent result. Also added examples for langchain demo to demonstrate the use of langchain simple llm calls and running chains using templates. 

## Project Overview
The goal of this project is to explore how various technologies can be implemented to enhance SQL queries using LLM, and LangChain, a natural language processing library. We aim to improve the efficiency and accuracy of SQL query writing by enabling users to input a few examples and have the system generate the corresponding SQL queries.

## Execution FLow

## User FLow

## Technologies Used
- Python
- Streamlit
- Jupyter Lab
- gpt-3.5-turbo
- LangChain
- SQLite3
- ChromaDB
- OpenAIEmbeddings
- few-shot learning

----
## Installation
1. Clone the repository:
`git clone https://github.com/akgcode/NL2SQL.git`
2. Create a new virtual environment
```
virtualenv myenv
source myenv/bin/activate #for ubuntu
myenv/Scripts/activate.bat #for windows
```
3. Install `langchain`,`openai`, `streamlit` and all other required libraries using pip from the requirements.txt file.
```
pip install -r requirements.txt
```

---
## Usage

1. Launch the app using this command
   `streamlit run main.py`
2. Login using test credentials
3. Upload a SQLite3 db or a csv file.
4. Enjoy the coversation with our in-house NL2SQL chatbot :)   


### Output

1. Login/Welcome Screen
 
2. File uploader

3. File being rendered as a pandas dataframe

4. A sample conversation
