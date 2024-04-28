# NL2SQL
From Natural Language to SQL query generator
## Natural Language to SQL | SQL Query Generator using Langchain 🦜️🔗 
This repository contains code for a Streamlit application for interaction with SQLite3 database or a csv using natural language and generate the SQL query and consequent result. Also added examples for langchain demo to demonstrate the use of langchain simple llm calls and running chains using templates. 

## Project Overview
The goal of this project is to explore how various technologies can be implemented to enhance SQL queries using LLM, and LangChain, a natural language processing library. We aim to improve the efficiency and accuracy of SQL query writing by enabling users to input a few examples and have the system generate the corresponding SQL queries.

## Execution FLow
![image](https://github.com/Deloitte-US/GenAI_SQL_Query_Generator_2.0/assets/165323714/43f6d551-1506-4408-80d6-646ae552839b)

## User FLow
![image](https://github.com/Deloitte-US/GenAI_SQL_Query_Generator_2.0/assets/165323714/975d7761-625a-44e7-aaf8-e471848fdef4)


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


## Installation
1. Clone the repository:
`git clone https://github.com/Deloitte-US/GenAI_SQL_Query_Generator_2.0.git `
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


## Usage

1. Launch the app using this command
   `streamlit run main.py`
2. Login using test credentials
3. Upload a SQLite3 db or a csv file.
4. Enjoy the coversation with our in-house NL2SQL chatbot :)   


### Output

1. Login/Welcome Screen
![image](https://github.com/Deloitte-US-Consulting/sampleReadme/assets/165323714/e079267f-4ed2-45f4-89b7-525828328517)
 
2. File uploader
![image](https://github.com/Deloitte-US-Consulting/sampleReadme/assets/165323714/7bafb953-dc58-474d-92b3-25fb079f1ce1)

3. File being rendered as a pandas dataframe
![image](https://github.com/Deloitte-US-Consulting/sampleReadme/assets/165323714/b3aaa415-d89a-45c0-936f-569c4baf7b79)

4. A sample conversation
![image](https://github.com/Deloitte-US-Consulting/sampleReadme/assets/165323714/0c64e373-7f81-4787-84c9-e11ba9750f3d)
