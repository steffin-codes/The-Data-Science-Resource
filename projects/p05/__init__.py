import streamlit as st
from multiapp import MultiApp
from projects.p05 import App
from Helper import Functions

def p05_md():
    try:
        text = Functions.get_file_content_as_string("projects/p05/README.md")
        # to check locally
        # with open("projects/p05/README.md") as f:
        #     text = f.read() 
        if text:
            st.markdown(text)
        else: 
            st.info("Looks like it is empty 👀!!")
    except:
        st.error("Whoops there is no writeup for this project!")
    pass
def p05_py():
    try:
        code = Functions.get_file_content_as_string("projects/p05/App.py")
        if code:
            st.code(code, language='python')
        else: 
            st.info("How is this possible!!")
    except:
        st.error("Something is definetly messed up!")
        # TODO: Add code to contact me with screenshot?
    pass
def app():
    p05 = MultiApp()
    p05.add_app("Writeup", p05_md)
    p05.add_app("App", App.app)
    p05.add_app("Code", p05_py)
    p05.run_radio()   