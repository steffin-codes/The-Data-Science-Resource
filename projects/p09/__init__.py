import streamlit as st
from multiapp import MultiApp
from projects.p09 import App
from Helper import Functions
#TODO: Language Detector
def p09_md():
    try:
        text = Functions.get_file_content_as_string("projects/p09/README.md")
        if text:
            st.markdown(text)
        else: 
            st.info("Looks like it is empty 👀!!")
    except:
        st.error("Whoops there is no writeup for this project!")
    pass
def p09_py():
    try:
        code = Functions.get_file_content_as_string("projects/p09/App.py")
        if code:
            st.code(code, language='python')
        else: 
            st.info("How is this possible!!")
    except:
        st.error("Something is definetly messed up!")
        # TODO: Add code to contact me with screenshot?
    pass
def app():
    p09 = MultiApp()
    p09.add_app("Writeup", p09_md)
    p09.add_app("App", App.app)
    p09.add_app("Code", p09_py)
    p09.run_radio()   