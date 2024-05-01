import streamlit as st
import warnings
warnings.filterwarnings("ignore")

from time import sleep 
from navigation import make_sidebar

make_sidebar()

st.title("Welcome to NL2SQL")
st.write("Please login to continue (username `test`, password `test`).")

username = st.text_input("Username")
password = st.text_input("Password", type="password")

if st.button("Log in", type="primary"):
    if username == "test" and password == "test":
        st.session_state.logged_in = True
        st.success("Logged in successfuly")
        sleep(0.5)
        st.switch_page("pages/page.py")
    else:
        st.error("Incorrect credentials")
