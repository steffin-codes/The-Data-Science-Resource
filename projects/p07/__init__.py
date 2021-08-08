import streamlit as st
from multiapp import MultiApp
from projects.p07 import App
from Helper import Functions
#TODO: Whatsapp Chat Analyzer
def p07_md():
    try:
        text = Functions.get_file_content_as_string("projects/p07/README.md")
        if text:
            st.markdown(text)
        else: 
            st.info("Looks like it is empty 👀!!")
    except:
        st.error("Whoops there is no writeup for this project!")
    pass
def p07_py():
    try:
        code = Functions.get_file_content_as_string("projects/p07/App.py")
        if code:
            st.code(code, language='python')
        else: 
            st.info("How is this possible!!")
    except:
        st.error("Something is definetly messed up!")
        # TODO: Add code to contact me with screenshot?
    pass
def app():
    p07 = MultiApp()
    p07.add_app("Writeup", p07_md)
    p07.add_app("App", App.app)
    p07.add_app("Code", p07_py)
    p07.run_radio()   