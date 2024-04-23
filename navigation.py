import streamlit as st
from time import sleep 
from streamlit.runtime.scriptrunner import get_script_run_ctx
from streamlit.source_util import get_pages

def get_current_page_name():
    ctx = get_script_run_ctx
    if ctx is None:
        raise RuntimeError("Coudldn't get script context")
    
    pages = get_pages("")

    return pages[ctx.page_script_hash]["page_name"]

def make_sidebar():
    with st.sidebar:
        st.title("NL2SQL Login page")
        st.write("")
        st.write("")

        if st.session_state.get("logged_in", False):
            st.page_link("pages/page1.py", label="Logged in")
            st.write("")
            st.write("")

            if st.button("Log out", key='Logout Button'):
                logout()

def logout():
    st.session_state.logged_in = False
    st.info("Logged out successfuly")
    sleep(0.5)
    st.switch_page("main.py")
