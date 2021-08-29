import streamlit as st
from multiapp import MultiApp
from projects.p08 import App
from Helper import Functions
#TODO: Fake News Detector
def p08_md():
    try:
        text = Functions.get_file_content_as_string("projects/p08/README.md")
        if text:
            st.markdown(text)
        else: 
            st.info("Looks like it is empty 👀!!")
    except:
        st.error("Whoops there is no writeup for this project!")
    pass
def p08_py():
    try:
        code = Functions.get_file_content_as_string("projects/p08/App.py")
        if code:
            st.code(code, language='python')
        else: 
            st.info("How is this possible!!")
    except:
        st.error("Something is definetly messed up!")
        # TODO: Add code to contact me with screenshot?
    pass
def app():
    p08 = MultiApp()
    p08.add_app("Writeup", p08_md)
    p08.add_app("App", App.app)
    p08.add_app("Code", p08_py)
    p08.run_radio()   