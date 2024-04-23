examples = [
    {
        "input": "List all customers in France with a credit over 20000.",
        "query": "SELECT * FROM customers WHERE country = 'France' AND creditLimit>20000"
    },
    {
        "input": "Get the highest payment amount made by any customer.",
        "query": "SELECT MAX(amount) FROM payments;"
    },
    {
        "input": "Show product details for products in the 'Motorcycles' product line.",
        "query": "SELECT * FROM products WHERE productLine"
    },
    {
        "input": "Retrieve the name of employees who report to employee number 1002",
        "query": "SELECT firstName, lastName FROM employees WHERE reportsTo = 1002"
    },
    {
        "input": "List all products with a stock quantity less than 7000.",
        "query": "SELECT productName, quantityInStock FROM products WHERE quantityInStock <7000"
    }
]

from langchain_community.vectorstores import chroma
from langchain_core.example_selectors import SemanticSimilarityExampleSelector
from langchain_openai import OpenAIEmbeddings
import streamlit as st

@st.cache_resource
def get_example_selector():
    example_selector = SemanticSimilarityExampleSelector.from_examples(
        examples,
        OpenAIEmbeddings,
        chroma,
        k=2,
        input_keys=["input"]
    )
    return example_selector